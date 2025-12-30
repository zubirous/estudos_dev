# 3. DML (Data Manipulation Language) - Dados

## INSERT

```sql
-- Inserir um registro
INSERT INTO usuarios (nome, email, idade) 
VALUES ('João', 'joao@email.com', 25);

-- Inserir múltiplos registros
INSERT INTO usuarios (nome, email, idade) VALUES
('Maria', 'maria@email.com', 30),
('Pedro', 'pedro@email.com', 28);

-- Inserir com valores padrão
INSERT INTO usuarios (nome, email) 
VALUES ('Ana', 'ana@email.com');

-- INSERT IGNORE: Ignora erros de chave primária/única duplicada
INSERT IGNORE INTO usuarios (id, nome, email) VALUES
(1, 'João', 'joao@email.com'),
(2, 'Maria', 'maria@email.com');
-- Se id 1 já existir, ignora o erro e continua com id 2

-- INSERT ... ON DUPLICATE KEY UPDATE: Insere se não existir, atualiza se existir
INSERT INTO usuarios (id, nome, email) VALUES (1, 'João', 'joao@email.com')
ON DUPLICATE KEY UPDATE nome = 'João', email = 'joao@email.com';
-- Se id 1 já existir, atualiza nome e email. Se não existir, insere novo registro
```

## UPDATE

```sql
-- Atualizar todos os registros (CUIDADO!)
UPDATE usuarios SET idade = idade + 1;

-- Atualizar com WHERE
UPDATE usuarios 
SET idade = 26, nome = 'João Silva'
WHERE id = 1;

-- Atualizar múltiplas linhas
UPDATE usuarios 
SET ativo = FALSE
WHERE idade < 18;

-- UPDATE com JOIN: Atualizar registros com base em dados de outra tabela
-- Exemplo: Imagine que você adicionou uma coluna "total_pedidos" na tabela "usuarios" para guardar a quantidade de pedidos de cada usuário.
-- Suponha que você quer atualizar o total de pedidos APENAS para usuários que tenham pelo menos um pedido acima de 100 de valor.

UPDATE usuarios u
INNER JOIN pedidos p ON u.id = p.usuario_id
SET u.total_pedidos = (
    SELECT COUNT(*) FROM pedidos WHERE usuario_id = u.id
)
WHERE p.valor > 100;

-- Como funciona:
-- 1. O JOIN faz a ligação entre cada usuário (u) e seus pedidos (p) pelo campo de usuário.
-- 2. O SET atualiza o campo "total_pedidos" do usuário para ser igual ao total de pedidos que ele já possui (contando todos os pedidos, não só os acima de 100).
-- 3. O WHERE limita a atualização somente aos usuários que possuam ao menos um pedido acima de 100.
-- Isso garante que somente os usuários "ativos" (com pedidos grandes) tenham o campo "total_pedidos" atualizado.

-- Observação:
-- Se o usuário tiver mais de um pedido acima de 100, ele pode ser atualizado mais de uma vez (mas o valor final será sempre o total de pedidos desse usuário, pois o SET usa COUNT em todos os pedidos dele).
-- Um UPDATE com JOIN é muito útil quando você precisa atualizar dados em uma tabela baseando-se em informações relacionadas de outra tabela, sem precisar fazer vários comandos separados.

**IMPORTANTE:** Sempre use WHERE no UPDATE para evitar atualizar todos os registros!

## DELETE

-- Deletar com WHERE (sempre usar WHERE!)
DELETE FROM usuarios WHERE id = 1;

-- Deletar múltiplos registros
DELETE FROM usuarios WHERE idade < 18;

-- Deletar todos (CUIDADO!)
DELETE FROM usuarios;  -- Remove todos os dados, mas mantém estrutura

-- TRUNCATE: Mais rápido, reseta AUTO_INCREMENT
TRUNCATE TABLE usuarios;


## DELETE vs TRUNCATE

- **DELETE**: 
  - Remove registros
  - Pode ter WHERE
  - Mantém estrutura
  - Mais lento (registra cada linha deletada)
  - **NÃO reseta AUTO_INCREMENT** (continua do último valor)
  
- **TRUNCATE**: 
  - Remove todos registros
  - Não pode ter WHERE
  - Mantém estrutura
  - **Mais rápido** (não registra cada linha individualmente)
  - **Reseta AUTO_INCREMENT** (volta para 1)

**Por que TRUNCATE é mais rápido?**
TRUNCATE não registra cada linha deletada individualmente no log de transações, tornando a operação muito mais rápida que DELETE.

