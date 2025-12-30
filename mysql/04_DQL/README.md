# 4. DQL (Data Query Language) - Consultas

## SELECT Básico

```sql
-- Selecionar todas as colunas
SELECT * FROM usuarios;

-- Selecionar colunas específicas
SELECT nome, email FROM usuarios;

-- Alias de colunas
SELECT nome AS nome_completo, email AS e_mail FROM usuarios;

-- SELECT DISTINCT (valores únicos)
SELECT DISTINCT idade FROM usuarios;
```

## WHERE - Filtros

```sql
-- Operadores de comparação
SELECT * FROM usuarios WHERE idade = 25;
SELECT * FROM usuarios WHERE idade > 25;
SELECT * FROM usuarios WHERE idade >= 25;
SELECT * FROM usuarios WHERE idade < 25;
SELECT * FROM usuarios WHERE idade <= 25;
SELECT * FROM usuarios WHERE idade != 25;  -- ou <>
SELECT * FROM usuarios WHERE idade <> 25;

-- Operadores lógicos
SELECT * FROM usuarios 
WHERE idade > 25 AND ativo = TRUE;

SELECT * FROM usuarios 
WHERE idade < 18 OR idade > 65;

SELECT * FROM usuarios 
WHERE NOT ativo = TRUE;

-- BETWEEN (inclusivo)
SELECT * FROM usuarios WHERE idade BETWEEN 18 AND 65;

-- IN (lista de valores)
SELECT * FROM usuarios WHERE idade IN (25, 30, 35);

-- LIKE (busca de padrões)
SELECT * FROM usuarios WHERE nome LIKE 'João%';   -- Começa com João
SELECT * FROM usuarios WHERE nome LIKE '%Silva';  -- Termina com Silva
SELECT * FROM usuarios WHERE nome LIKE '%João%';  -- Contém João
SELECT * FROM usuarios WHERE nome LIKE 'J__o';    -- J + 2 caracteres + o

-- IS NULL / IS NOT NULL
SELECT * FROM usuarios WHERE telefone IS NULL;
SELECT * FROM usuarios WHERE telefone IS NOT NULL;
```

## ORDER BY - Ordenação

```sql
-- Ordenar ascendente (padrão)
SELECT * FROM usuarios ORDER BY nome ASC;

-- Ordenar descendente
SELECT * FROM usuarios ORDER BY idade DESC;

-- Múltiplas ordenações
SELECT * FROM usuarios ORDER BY ativo DESC, nome ASC;
```

## LIMIT - Limitar Resultados

```sql
-- Limitar quantidade
SELECT * FROM usuarios LIMIT 10;

-- Paginação (OFFSET)
SELECT * FROM usuarios LIMIT 10 OFFSET 20;  -- Pula 20, pega 10
-- Equivalente a:
SELECT * FROM usuarios LIMIT 20, 10;  -- Sintaxe alternativa
```

## Funções de Agregação

```sql
-- COUNT: Contar registros
SELECT COUNT(*) FROM usuarios;
SELECT COUNT(DISTINCT idade) FROM usuarios;

-- SUM: Soma
SELECT SUM(valor) FROM pedidos;

-- AVG: Média
SELECT AVG(idade) FROM usuarios;

-- MIN/MAX: Mínimo/Máximo
SELECT MIN(idade) FROM usuarios;
SELECT MAX(valor) FROM pedidos;

-- Combinado
SELECT 
    COUNT(*) AS total_usuarios,
    AVG(idade) AS media_idade,
    MIN(idade) AS menor_idade,
    MAX(idade) AS maior_idade
FROM usuarios;
```

## GROUP BY - Agrupamento

### Para que serve?

**GROUP BY** agrupa linhas que têm o mesmo valor em uma ou mais colunas, permitindo aplicar funções de agregação (COUNT, SUM, AVG, etc.) em cada grupo.

### Exemplo Prático:

Imagine uma tabela `usuarios`:
```
nome      | idade | cidade
----------|-------|--------
João      | 25    | SP
Maria     | 30    | RJ
Pedro     | 25    | SP
Ana       | 30    | RJ
Carlos    | 25    | SP
```

**SEM GROUP BY** (erro - não funciona):
```sql
-- Isso dá ERRO! Não pode usar COUNT(*) sem GROUP BY quando há outras colunas
SELECT idade, COUNT(*) FROM usuarios;  -- ❌ ERRO
```

**COM GROUP BY** (correto):
```sql
-- Agrupa por idade e conta quantos têm cada idade
SELECT idade, COUNT(*) AS quantidade
FROM usuarios
GROUP BY idade;
```
**Resultado:**
```
idade | quantidade
------|------------
25    | 3
30    | 2
```

### Quando usar GROUP BY?

Use quando precisar:
- **Contar** quantos registros têm cada valor (ex: quantos usuários por cidade)
- **Somar** valores agrupados (ex: total de vendas por vendedor)
- **Calcular médias** por grupo (ex: média de idade por departamento)
- **Encontrar máximos/mínimos** por grupo (ex: maior salário por cargo)

### Exemplos Completos:

```sql
-- 1. Quantos usuários têm cada idade?
SELECT idade, COUNT(*) AS quantidade
FROM usuarios
GROUP BY idade;

-- 2. Total de vendas por vendedor
SELECT vendedor_id, SUM(valor) AS total_vendas
FROM vendas
GROUP BY vendedor_id;

-- 3. Média de idade por cidade
SELECT cidade, AVG(idade) AS media_idade
FROM usuarios
GROUP BY cidade;

-- 4. GROUP BY com múltiplas colunas
SELECT cidade, idade, COUNT(*) AS quantidade
FROM usuarios
GROUP BY cidade, idade;  -- Agrupa por cidade E idade

-- 5. GROUP BY com HAVING (filtro após agrupamento)
SELECT idade, COUNT(*) AS quantidade
FROM usuarios
GROUP BY idade
HAVING quantidade > 5;  -- Só mostra idades com mais de 5 pessoas

-- 6. WHERE vs HAVING:
-- WHERE: Filtra ANTES do agrupamento
-- HAVING: Filtra DEPOIS do agrupamento
SELECT idade, COUNT(*) AS quantidade
FROM usuarios
WHERE ativo = TRUE        -- Filtra antes (só usuários ativos)
GROUP BY idade
HAVING quantidade > 5;    -- Filtra depois (só grupos com mais de 5)
```

## JOIN - Relacionamento entre Tabelas

### Para que serve?

**JOIN** combina dados de duas ou mais tabelas relacionadas em uma única consulta, usando uma coluna comum entre elas.

### Exemplo Prático:

Imagine duas tabelas relacionadas:

**Tabela `usuarios`:**
```
id | nome    | email
---|---------|---------------
1  | João    | joao@email.com
2  | Maria   | maria@email.com
3  | Pedro   | pedro@email.com
```

**Tabela `pedidos`:**
```
id | usuario_id | valor | data_pedido
---|------------|-------|------------
10 | 1          | 100   | 2024-01-15
11 | 1          | 50    | 2024-01-20
12 | 2          | 200   | 2024-01-18
```

### Tipos de JOIN:

#### 1. INNER JOIN (Mais comum)
**Retorna apenas registros que existem em AMBAS as tabelas.**

```sql
SELECT u.nome, p.valor, p.data_pedido
FROM usuarios u
INNER JOIN pedidos p ON u.id = p.usuario_id;
```

**Resultado:**
```
nome  | valor | data_pedido
------|-------|------------
João  | 100   | 2024-01-15
João  | 50    | 2024-01-20
Maria | 200   | 2024-01-18
```
**Observação:** Pedro não aparece porque não tem pedidos.

**Quando usar:** Quando você precisa apenas dos dados que têm correspondência em ambas as tabelas.

#### 2. LEFT JOIN (Muito usado)
**Retorna TODOS os registros da tabela da esquerda + correspondentes da direita (NULL se não houver).**

```sql
SELECT u.nome, p.valor
FROM usuarios u
LEFT JOIN pedidos p ON u.id = p.usuario_id;
```

**Resultado:**
```
nome  | valor
------|-------
João  | 100
João  | 50
Maria | 200
Pedro | NULL    -- Aparece mesmo sem pedidos!
```
**Observação:** Pedro aparece mesmo sem pedidos, com valor NULL.

**Quando usar:** Quando você quer TODOS os registros da primeira tabela, mesmo que não tenham correspondência na segunda (ex: listar todos os usuários e seus pedidos, incluindo quem não tem pedidos).

#### 3. RIGHT JOIN (Menos usado)
**Retorna TODOS os registros da tabela da direita + correspondentes da esquerda (NULL se não houver).**

```sql
SELECT u.nome, p.valor
FROM usuarios u
RIGHT JOIN pedidos p ON u.id = p.usuario_id;
```

**Resultado:** Igual ao INNER JOIN neste exemplo, mas se houvesse um pedido sem usuário correspondente, ele apareceria com nome NULL.

**Quando usar:** Quando você quer TODOS os registros da segunda tabela, mesmo que não tenham correspondência na primeira (raro na prática).

### Comparação Visual:

```
INNER JOIN:    A ∩ B  (apenas intersecção)
LEFT JOIN:     A      (todos de A + correspondentes de B)
RIGHT JOIN:    B      (todos de B + correspondentes de A)
FULL JOIN:     A ∪ B  (todos de ambos, não suportado no MySQL)
```

### Exemplos Completos:

```sql
-- 1. INNER JOIN: Usuários e seus pedidos (só quem tem pedidos)
SELECT u.nome, u.email, p.valor, p.data_pedido
FROM usuarios u
INNER JOIN pedidos p ON u.id = p.usuario_id;

-- 2. LEFT JOIN: Todos os usuários e seus pedidos (inclui quem não tem)
SELECT u.nome, COUNT(p.id) AS total_pedidos
FROM usuarios u
LEFT JOIN pedidos p ON u.id = p.usuario_id
GROUP BY u.id, u.nome;

-- 3. Múltiplos JOINs: Usuários, pedidos e produtos
SELECT u.nome, p.valor, pr.nome_produto
FROM usuarios u
INNER JOIN pedidos p ON u.id = p.usuario_id
INNER JOIN produtos pr ON p.produto_id = pr.id;

-- 4. LEFT JOIN com WHERE: Usuários que NÃO têm pedidos
SELECT u.nome
FROM usuarios u
LEFT JOIN pedidos p ON u.id = p.usuario_id
WHERE p.id IS NULL;  -- Só quem não tem pedidos

-- 5. JOIN com alias (recomendado para clareza)
SELECT 
    u.nome AS usuario,
    p.valor AS valor_pedido,
    p.data_pedido AS data
FROM usuarios u
INNER JOIN pedidos p ON u.id = p.usuario_id
WHERE p.valor > 100;
```

## UPDATE com JOIN (DML em contexto de consultas)

### Para que serve?

Permite atualizar uma tabela usando dados ou condições de outra tabela relacionada, combinando UPDATE com JOIN.

### Exemplos Práticos:

```sql
-- 1. Atualizar total de pedidos dos usuários baseado em pedidos recentes
UPDATE usuarios u
INNER JOIN pedidos p ON u.id = p.usuario_id
SET u.total_pedidos = (
    SELECT COUNT(*) FROM pedidos WHERE usuario_id = u.id
)
WHERE p.data_pedido >= '2024-01-01';
-- Atualiza apenas usuários que têm pedidos a partir de 2024-01-01

-- 2. Marcar usuários que têm ou não têm pedidos (usando LEFT JOIN)
UPDATE usuarios u
LEFT JOIN pedidos p ON u.id = p.usuario_id
SET u.tem_pedidos = CASE WHEN p.id IS NOT NULL THEN TRUE ELSE FALSE END;
-- TRUE para quem tem pedidos, FALSE para quem não tem

-- 3. Atualizar saldo de usuários baseado em transações
UPDATE usuarios u
INNER JOIN transacoes t ON u.id = t.usuario_id
SET u.saldo = u.saldo + t.valor
WHERE t.status = 'confirmada';

-- 4. Atualizar com múltiplos JOINs
UPDATE usuarios u
INNER JOIN pedidos p ON u.id = p.usuario_id
INNER JOIN produtos pr ON p.produto_id = pr.id
SET u.ultimo_produto_comprado = pr.nome
WHERE p.data_pedido = (
    SELECT MAX(data_pedido) FROM pedidos WHERE usuario_id = u.id
);
```

**Importante:** 
- Use INNER JOIN quando quiser atualizar apenas registros que têm correspondência
- Use LEFT JOIN quando quiser atualizar todos os registros da primeira tabela
- Sempre teste com SELECT antes de fazer UPDATE!

## WHERE vs HAVING (CRÍTICO!)

- **WHERE**: Filtra ANTES do GROUP BY (não pode usar funções de agregação)
- **HAVING**: Filtra DEPOIS do GROUP BY (pode usar funções de agregação)

