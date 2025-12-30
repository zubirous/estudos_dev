# 2. DDL (Data Definition Language) - Estrutura

## CREATE TABLE

```sql
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    idade INT,
    ativo BOOLEAN DEFAULT TRUE,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## CONSTRAINTS:

- `NOT NULL`: Campo obrigatório
- `UNIQUE`: Valores únicos (pode ter múltiplas UNIQUE, permite um NULL)
- `PRIMARY KEY`: Chave primária (UNIQUE + NOT NULL) - apenas uma por tabela
- `FOREIGN KEY`: Chave estrangeira
- `CHECK`: Validação de valor (MySQL 8.0.16+)
- `DEFAULT`: Valor padrão
- `AUTO_INCREMENT`: Incremento automático (só funciona com INT/BIGINT)

**IMPORTANTE:**
- Uma tabela pode ter apenas **uma PRIMARY KEY**, mas pode ter **múltiplas UNIQUE**
- `CHECK` constraint foi adicionada apenas no **MySQL 8.0.16+**
- `PRIMARY KEY` não permite NULL, enquanto `UNIQUE` permite um NULL

## CHECK Constraint (MySQL 8.0.16+)

```sql
-- Validar valor na criação da tabela
CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    preco DECIMAL(10,2),
    quantidade INT,
    CHECK (preco > 0),
    CHECK (quantidade >= 0)
);

-- Adicionar CHECK em coluna existente
ALTER TABLE produtos 
ADD CONSTRAINT chk_preco CHECK (preco > 0);
```

## FOREIGN KEY (Chave Estrangeira)

```sql
CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    valor DECIMAL(10,2),
    data_pedido DATE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        ON DELETE CASCADE      -- Se usuário for deletado, deleta pedidos
        ON UPDATE CASCADE      -- Se id do usuário mudar, atualiza pedidos
);
```

**Ações ON DELETE/ON UPDATE:**
- `CASCADE`: Propaga a ação (delete/update) para registros relacionados
- `RESTRICT` / `NO ACTION`: Impede a ação se houver registros relacionados
- `SET NULL`: Define o campo como NULL (campo deve permitir NULL)
- `SET DEFAULT`: Define valor padrão

## ALTER TABLE

```sql
-- Adicionar coluna
ALTER TABLE usuarios ADD COLUMN telefone VARCHAR(20);

-- Modificar coluna
ALTER TABLE usuarios MODIFY COLUMN nome VARCHAR(200);

-- Renomear coluna
ALTER TABLE usuarios CHANGE COLUMN nome nome_completo VARCHAR(200);

-- Deletar coluna
ALTER TABLE usuarios DROP COLUMN telefone;

-- Adicionar constraint UNIQUE
ALTER TABLE usuarios ADD CONSTRAINT uk_email UNIQUE (email);

-- Remover constraint
ALTER TABLE usuarios DROP CONSTRAINT uk_email;

-- Adicionar índice
ALTER TABLE usuarios ADD INDEX idx_email (email);
```

**IMPORTANTE:**
- `MODIFY COLUMN` e `CHANGE COLUMN` podem modificar colunas
- `DEFAULT` é usado quando valor não é especificado na inserção
- FOREIGN KEY pode ser criado de diferentes formas (CREATE TABLE, ALTER TABLE ADD CONSTRAINT, ALTER TABLE ADD FOREIGN KEY)

-- Imagine que você tem duas caixas: uma caixa chamada "usuarios" e outra chamada "pedidos".
-- Cada pedido precisa saber de QUAL usuário ele pertence. Para garantir isso,
-- usamos algo chamado "chave estrangeira" (FOREIGN KEY).

-- Pense assim: é como se cada pedido tivesse um crachá do usuário dono dele.
-- Só pode usar um crachá (usuario_id) que existe na caixa de usuários!

-- Exemplo simples:
-- Suponha uma tabela "usuarios" com usuários:
-- | id | nome   |
-- |----|--------|
-- |  1 | Maria  |
-- |  2 | João   |

-- E uma tabela "pedidos":
-- | id | usuario_id | valor |
-- |----|------------|-------|
-- | 10 |     1      | 100.0 |
-- | 11 |     2      | 150.0 |

-- O usuario_id do pedido indica de quem é aquele pedido.

-- MAS, se tentarmos colocar usuario_id=3 (que não existe), o banco diz: "Não pode!"
-- É a regra da chave estrangeira, só aceita crachás válidos!

-- Às vezes, quando criamos a tabela "pedidos", não colocamos a regra da chave estrangeira ali na hora.
-- Se esquecermos, podemos adicionar depois, assim:

-- PASSO A PASSO:
-- 1. A coluna usuario_id já deve existir na tabela pedidos.
-- 2. Agora, mandamos o banco criar a ligação (regra):

ALTER TABLE pedidos 
ADD CONSTRAINT fk_usuario  -- aqui estamos apenas dando um nome à regra; os parâmetros da regra (coluna e referência) são definidos nas próximas linhas
FOREIGN KEY (usuario_id)  -- dizendo qual coluna da tabela "pedidos" é a chave estrangeira
REFERENCES usuarios(id);  -- dizendo que só pode ter valores iguais a algum id que já exista na tabela "usuarios"

-- Assim, toda vez que você tentar colocar um pedido, o banco vai perguntar:
-- "Esse usuario_id existe lá na caixa de usuários? Se não existir, não pode!"

-- Isso ajuda a não bagunçar o estoque! Ninguém vai ter pedidos sem dono!
```

## DROP TABLE

```sql
-- Cuidado! Remove tabela e todos os dados
DROP TABLE usuarios;

-- Mais seguro: remove apenas se existir
DROP TABLE IF EXISTS usuarios;
```

