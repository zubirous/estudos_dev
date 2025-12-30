# 6. TRANSAÇÕES

## O que são Transações?

**Transações** são um conjunto de operações SQL que devem ser executadas como uma única unidade. Ou todas as operações são executadas com sucesso, ou nenhuma é executada (tudo ou nada).

**Analogia:** Transferência bancária: você precisa debitar de uma conta E creditar em outra. Se uma falhar, ambas devem ser desfeitas.

## ACID - Propriedades das Transações

### 1. Atomicity (Atomicidade)
**"Tudo ou nada"** - Todas as operações da transação são executadas completamente, ou nenhuma é executada.

**Exemplo:**
```sql
START TRANSACTION;
UPDATE conta SET saldo = saldo - 100 WHERE id = 1;  -- Debitar
UPDATE conta SET saldo = saldo + 100 WHERE id = 2;  -- Creditar
-- Se qualquer uma falhar, ambas são desfeitas
COMMIT;
```

### 2. Consistency (Consistência)
O banco sempre permanece em um estado válido. Regras de integridade são mantidas.

**Exemplo:**
```sql
START TRANSACTION;
-- Garante que saldo nunca fica negativo
UPDATE conta SET saldo = saldo - 100 WHERE id = 1;
-- Se saldo ficar negativo, transação falha e é revertida
COMMIT;
```

### 3. Isolation (Isolamento)
Transações simultâneas não interferem umas nas outras. Cada transação vê o banco como se estivesse sozinha.

**Exemplo:**
```sql
-- Transação 1 (Sessão A)
START TRANSACTION;
SELECT saldo FROM conta WHERE id = 1;  -- Vê 1000
UPDATE conta SET saldo = 900 WHERE id = 1;
-- Ainda não commitou

-- Transação 2 (Sessão B)
SELECT saldo FROM conta WHERE id = 1;  -- Ainda vê 1000 (não vê mudança não commitada)
```

### 4. Durability (Durabilidade)
Após COMMIT, as mudanças são permanentes, mesmo em caso de falha do sistema.

**Exemplo:**
```sql
START TRANSACTION;
UPDATE conta SET saldo = 1000 WHERE id = 1;
COMMIT;  -- Agora está salvo permanentemente
-- Mesmo se o servidor cair, a mudança permanece
```

## Controle de Transações

### Sintaxe Básica

```sql
-- Iniciar transação
START TRANSACTION;
-- ou
BEGIN;

-- Comandos SQL...
UPDATE usuarios SET idade = 26 WHERE id = 1;
INSERT INTO pedidos (usuario_id, valor) VALUES (1, 500);

-- Confirmar (salvar permanentemente)
COMMIT;

-- Cancelar (desfazer tudo)
ROLLBACK;
```

**IMPORTANTE sobre END IF e Aninhamento:**

**Estrutura de Aninhamento:**
```
START TRANSACTION;          ← Inicia transação
    IF condição THEN         ← IF está DENTRO da transação
        -- comandos SQL
        COMMIT;             ← Finaliza a transação (que começou antes do IF)
    ELSE
        -- comandos SQL
        ROLLBACK;           ← Finaliza a transação (que começou antes do IF)
    END IF;                 ← Fecha apenas o bloco IF (sintaxe SQL)
```

**Pontos importantes:**
- O `IF` está **aninhado dentro** da transação iniciada por `START TRANSACTION`
- Quando você executa `COMMIT;` ou `ROLLBACK;` **dentro do IF**, você está finalizando a transação que começou **antes do IF**
- O `END IF;` apenas fecha o bloco condicional `IF...THEN...ELSE` (obrigatório por sintaxe SQL)
- `END IF;` **NÃO finaliza transações** - apenas fecha blocos condicionais

**O que acontece se não fechar o IF?**
Mesmo que a transação já tenha sido finalizada com `COMMIT;` ou `ROLLBACK;` dentro do IF, você **DEVE** fechar o bloco `IF` com `END IF;`. Caso contrário, você terá um **erro de sintaxe SQL**:

```sql
-- ❌ ERRADO: Sem END IF (erro de sintaxe!)
START TRANSACTION;          -- Transação iniciada
IF @saldo >= 100 THEN       -- IF dentro da transação
    UPDATE conta SET saldo = saldo - 100 WHERE id = 1;
    COMMIT;                 -- Transação finalizada (a que começou antes do IF)
-- ERRO: IF não foi fechado! "You have an error in your SQL syntax..."

-- ✅ CORRETO: Com END IF
START TRANSACTION;          -- Transação iniciada
IF @saldo >= 100 THEN       -- IF dentro da transação
    UPDATE conta SET saldo = saldo - 100 WHERE id = 1;
    COMMIT;                 -- Finaliza a transação (que começou antes do IF)
END IF;                     -- OBRIGATÓRIO: fecha o bloco IF (sintaxe SQL)
```

**Resumo:**
- `IF` está **dentro** da transação (aninhado)
- `COMMIT;` ou `ROLLBACK;` dentro do IF finalizam a transação que começou antes do IF
- `END IF;` é **obrigatório** para fechar blocos `IF...THEN...ELSE` (sintaxe SQL)
- São coisas **independentes**: você pode finalizar a transação dentro do IF, mas ainda precisa fechar o IF

**Exemplos:**

```sql
-- ✅ CORRETO: Transação simples SEM IF (não precisa END IF)
START TRANSACTION;
UPDATE conta SET saldo = saldo - 100 WHERE id = 1;
UPDATE conta SET saldo = saldo + 100 WHERE id = 2;
COMMIT;  -- Finaliza a transação

-- ✅ CORRETO: Transação COM IF (precisa END IF para fechar o IF)
START TRANSACTION;              -- 1. Inicia transação
SELECT saldo INTO @saldo FROM conta WHERE id = 1;
IF @saldo >= 100 THEN           -- 2. IF dentro da transação
    UPDATE conta SET saldo = saldo - 100 WHERE id = 1;
    COMMIT;                      -- 3. Finaliza a transação (que começou na linha 1)
ELSE
    ROLLBACK;                    -- 3. Finaliza a transação (que começou na linha 1)
END IF;                          -- 4. Fecha o bloco IF (sintaxe SQL), NÃO a transação (já foi fechada acima)
```

### Exemplo 1: Transferência Bancária

```sql
-- Transferir 100 de conta 1 para conta 2
START TRANSACTION;

-- Verificar saldo suficiente
SELECT saldo INTO @saldo_atual FROM conta WHERE id = 1;
IF @saldo_atual >= 100 THEN
    -- Debitar conta origem
    UPDATE conta SET saldo = saldo - 100 WHERE id = 1;
    
    -- Creditar conta destino
    UPDATE conta SET saldo = saldo + 100 WHERE id = 2;
    
    -- Registrar histórico
    INSERT INTO transacoes (conta_origem, conta_destino, valor) 
    VALUES (1, 2, 100);
    
    COMMIT;  -- Tudo certo, salvar (finaliza a transação)
ELSE
    ROLLBACK;  -- Saldo insuficiente, desfazer tudo (finaliza a transação)
END IF;  -- Fecha o bloco IF, NÃO a transação (já foi finalizada acima)
```

### Exemplo 2: Criar Pedido com Estoque

```sql
-- Criar pedido e atualizar estoque
START TRANSACTION;

-- Verificar estoque
SELECT quantidade INTO @estoque FROM produtos WHERE id = 5;
IF @estoque >= 10 THEN
    -- Criar pedido
    INSERT INTO pedidos (usuario_id, produto_id, quantidade, valor)
    VALUES (1, 5, 10, 500);
    
    SET @pedido_id = LAST_INSERT_ID();
    
    -- Atualizar estoque
    UPDATE produtos SET quantidade = quantidade - 10 WHERE id = 5;
    
    -- Registrar histórico
    INSERT INTO historico_estoque (produto_id, quantidade, tipo)
    VALUES (5, -10, 'venda');
    
    COMMIT;  -- Finaliza a transação
ELSE
    ROLLBACK;  -- Estoque insuficiente (finaliza a transação)
END IF;  -- Fecha o bloco IF, NÃO a transação (já foi finalizada acima)
```

### Exemplo 3: Atualizar Múltiplas Tabelas

```sql
-- Atualizar perfil de usuário e histórico
START TRANSACTION;

UPDATE usuarios 
SET nome = 'João Silva', email = 'joao@email.com' 
WHERE id = 1;

INSERT INTO historico_alteracoes (usuario_id, campo, valor_antigo, valor_novo)
VALUES (1, 'nome', 'João', 'João Silva');

INSERT INTO historico_alteracoes (usuario_id, campo, valor_antigo, valor_novo)
VALUES (1, 'email', 'joao.antigo@email.com', 'joao@email.com');

-- Se qualquer INSERT falhar, tudo é revertido
COMMIT;
```

### Exemplo 4: Deletar com Dependências

```sql
-- Deletar usuário e todos seus dados relacionados
START TRANSACTION;

-- Deletar pedidos
DELETE FROM pedidos WHERE usuario_id = 1;

-- Deletar comentários
DELETE FROM comentarios WHERE usuario_id = 1;

-- Deletar histórico
DELETE FROM historico WHERE usuario_id = 1;

-- Por último, deletar usuário
DELETE FROM usuarios WHERE id = 1;

-- Se qualquer DELETE falhar (ex: constraint), tudo é revertido
COMMIT;
```

### Exemplo 5: SAVEPOINT (Pontos de Salvamento)

```sql
-- Permite fazer rollback parcial dentro de uma transação
START TRANSACTION;

UPDATE conta SET saldo = saldo - 100 WHERE id = 1;
SAVEPOINT ponto1;  -- Salvar estado aqui

UPDATE conta SET saldo = saldo - 50 WHERE id = 2;
SAVEPOINT ponto2;  -- Salvar estado aqui

UPDATE conta SET saldo = saldo - 200 WHERE id = 3;
-- Se algo der errado aqui, pode voltar ao ponto2
ROLLBACK TO ponto2;  -- Volta ao ponto2, mantém mudanças até ponto1

-- Ou voltar ao início
ROLLBACK TO ponto1;  -- Volta ao ponto1

COMMIT;
```

### Exemplo 6: Transação com Tratamento de Erro

```sql
-- Usando variáveis para controlar erros
START TRANSACTION;

SET @erro = 0;

-- Operação 1
UPDATE conta SET saldo = saldo - 100 WHERE id = 1;
IF ROW_COUNT() = 0 THEN
    SET @erro = 1;
END IF;  -- Fecha o primeiro IF (verificação de erro)

-- Operação 2
UPDATE conta SET saldo = saldo + 100 WHERE id = 2;
IF ROW_COUNT() = 0 THEN
    SET @erro = 1;
END IF;  -- Fecha o segundo IF (verificação de erro)

-- Decidir commit ou rollback
IF @erro = 0 THEN
    COMMIT;  -- Finaliza a transação
    SELECT 'Transação concluída com sucesso' AS resultado;
ELSE
    ROLLBACK;  -- Finaliza a transação
    SELECT 'Erro na transação, todas as mudanças foram revertidas' AS resultado;
END IF;  -- Fecha o bloco IF, NÃO a transação (já foi finalizada acima)
```

## Quando Usar Transações?

### ✅ Use Transações quando:

1. **Operações relacionadas** que devem acontecer juntas
   ```sql
   -- Criar pedido + atualizar estoque + registrar histórico
   ```

2. **Manter integridade** entre múltiplas tabelas
   ```sql
   -- Deletar usuário + todos seus dados relacionados
   ```

3. **Operações críticas** que não podem falhar parcialmente
   ```sql
   -- Transferência bancária, pagamento, etc.
   ```

4. **Precisar desfazer** mudanças se algo der errado
   ```sql
   -- Se qualquer passo falhar, tudo volta ao estado anterior
   ```

### ❌ NÃO precisa de Transação quando:

1. **Operação única e simples**
   ```sql
   UPDATE usuarios SET idade = 25 WHERE id = 1;  -- Não precisa
   ```

2. **Operações independentes**
   ```sql
   -- Cada UPDATE é independente, não precisa transação
   UPDATE usuarios SET idade = 25 WHERE id = 1;
   UPDATE usuarios SET idade = 30 WHERE id = 2;
   ```

## Níveis de Isolamento

Os níveis de isolamento controlam como transações simultâneas veem os dados umas das outras.

### 1. READ UNCOMMITTED (Menor isolamento)
- Pode ler dados não commitados de outras transações
- Mais rápido, mas pode causar "dirty reads"
- **Raramente usado** em produção

**Exemplo do Problema:**
```sql
-- Transação A
START TRANSACTION;
UPDATE conta SET saldo = 500 WHERE id = 1;  -- Não commitou ainda

-- Transação B (READ UNCOMMITTED)
SELECT saldo FROM conta WHERE id = 1;  -- Vê 500 (dado não commitado!)
-- Se Transação A fizer ROLLBACK, Transação B viu dado incorreto
```

### 2. READ COMMITTED
- Lê apenas dados commitados
- Evita "dirty reads", mas pode ter "non-repeatable reads"
- Padrão em muitos bancos (PostgreSQL, Oracle)

**Exemplo:**
```sql
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- Transação A
START TRANSACTION;
SELECT saldo FROM conta WHERE id = 1;  -- Vê 1000
-- Transação B commitou mudança: saldo = 900
SELECT saldo FROM conta WHERE id = 1;  -- Agora vê 900 (mudou!)
```

### 3. REPEATABLE READ (Padrão MySQL InnoDB)
- Garante que leituras repetidas retornam o mesmo valor
- Evita "dirty reads" e "non-repeatable reads"
- Pode ter "phantom reads"

**Exemplo:**
```sql
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;

-- Transação A
START TRANSACTION;
SELECT saldo FROM conta WHERE id = 1;  -- Vê 1000
-- Transação B commitou mudança: saldo = 900
SELECT saldo FROM conta WHERE id = 1;  -- Ainda vê 1000 (consistente!)
COMMIT;
-- Agora vê 900 (após commit)
```

### 4. SERIALIZABLE (Maior isolamento)
- Máximo isolamento, transações executam como se fossem sequenciais
- Mais lento, mas evita todos os problemas de concorrência
- Use apenas quando necessário

**Exemplo:**
```sql
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

-- Transações são executadas uma de cada vez
-- Garante máxima consistência, mas pode ser muito lento
```

### Comparação dos Níveis:

| Nível | Dirty Read | Non-Repeatable Read | Phantom Read | Performance |
|-------|------------|---------------------|--------------|-------------|
| READ UNCOMMITTED | ❌ Sim | ❌ Sim | ❌ Sim | ⚡⚡⚡ Mais rápido |
| READ COMMITTED | ✅ Não | ❌ Sim | ❌ Sim | ⚡⚡ Rápido |
| REPEATABLE READ | ✅ Não | ✅ Não | ❌ Sim | ⚡ Médio |
| SERIALIZABLE | ✅ Não | ✅ Não | ✅ Não | 🐌 Mais lento |

### Configurar Nível de Isolamento:

```sql
-- Para a próxima transação
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
START TRANSACTION;
-- ...

-- Para todas as transações da sessão
SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;

-- Para todas as transações do servidor (requer privilégios)
SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;

-- Ver nível atual
SELECT @@transaction_isolation;
```

## Exemplos Práticos Completos

### Exemplo 1: E-commerce - Processar Pedido

```sql
START TRANSACTION;

-- 1. Verificar estoque
SELECT quantidade INTO @estoque FROM produtos WHERE id = 5;
IF @estoque < 10 THEN
    ROLLBACK;  -- Finaliza a transação
    SELECT 'Estoque insuficiente' AS erro;
ELSE
    -- 2. Criar pedido
    INSERT INTO pedidos (usuario_id, total) VALUES (1, 500);
    SET @pedido_id = LAST_INSERT_ID();
    
    -- 3. Adicionar itens
    INSERT INTO pedido_itens (pedido_id, produto_id, quantidade, preco)
    VALUES (@pedido_id, 5, 10, 50);
    
    -- 4. Atualizar estoque
    UPDATE produtos SET quantidade = quantidade - 10 WHERE id = 5;
    
    -- 5. Atualizar saldo do usuário
    UPDATE usuarios SET saldo = saldo - 500 WHERE id = 1;
    
    COMMIT;  -- Finaliza a transação
    SELECT 'Pedido criado com sucesso' AS sucesso;
END IF;  -- Fecha o bloco IF, NÃO a transação (já foi finalizada acima)
```

### Exemplo 2: Sistema Bancário - Transferência

```sql
START TRANSACTION;

-- Verificar saldo origem
SELECT saldo INTO @saldo_origem FROM conta WHERE id = 1;
IF @saldo_origem < 1000 THEN
    ROLLBACK;  -- Finaliza a transação
    SELECT 'Saldo insuficiente' AS erro;
ELSE
    -- Debitar origem
    UPDATE conta SET saldo = saldo - 1000 WHERE id = 1;
    
    -- Creditar destino
    UPDATE conta SET saldo = saldo + 1000 WHERE id = 2;
    
    -- Registrar transferência
    INSERT INTO transferencias (conta_origem, conta_destino, valor, data)
    VALUES (1, 2, 1000, NOW());
    
    COMMIT;  -- Finaliza a transação
    SELECT 'Transferência realizada' AS sucesso;
END IF;  -- Fecha o bloco IF, NÃO a transação (já foi finalizada acima)
```

### Exemplo 3: Sistema de Votos - Evitar Duplicação

```sql
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
START TRANSACTION;

-- Verificar se já votou
SELECT COUNT(*) INTO @ja_votou 
FROM votos 
WHERE usuario_id = 1 AND eleicao_id = 5;

IF @ja_votou > 0 THEN
    ROLLBACK;  -- Finaliza a transação
    SELECT 'Você já votou nesta eleição' AS erro;
ELSE
    -- Registrar voto
    INSERT INTO votos (usuario_id, eleicao_id, candidato_id)
    VALUES (1, 5, 3);
    
    -- Atualizar contador
    UPDATE candidatos SET total_votos = total_votos + 1 WHERE id = 3;
    
    COMMIT;  -- Finaliza a transação
    SELECT 'Voto registrado' AS sucesso;
END IF;  -- Fecha o bloco IF, NÃO a transação (já foi finalizada acima)
```

## Boas Práticas

1. **Mantenha transações curtas** - Quanto mais tempo aberta, maior chance de conflito
2. **Use o nível de isolamento adequado** - Não use SERIALIZABLE se não precisar
3. **Sempre trate erros** - Use ROLLBACK em caso de erro
4. **Evite operações lentas dentro de transações** - Como envio de email, processamento pesado
5. **Teste cenários de falha** - O que acontece se algo der errado no meio?

**IMPORTANTE:**
- Transações só funcionam com engines que suportam (InnoDB no MySQL)
- MyISAM não suporta transações
- AUTOCOMMIT está ativo por padrão (cada comando é uma transação)
- Use `SET autocommit = 0` para desativar autocommit na sessão
- **Transações são finalizadas com `COMMIT;` ou `ROLLBACK;`, NÃO com `END IF;`**
- `END IF;` fecha apenas blocos condicionais `IF...THEN...ELSE`, não a transação
