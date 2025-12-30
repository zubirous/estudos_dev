# 5. ÍNDICES

## O que são Índices?

**Índices** são estruturas que aceleram buscas no banco de dados, funcionando como um "índice de livro" - em vez de ler todas as páginas, você vai direto ao que precisa.

**Analogia:** Sem índice = ler livro inteiro para encontrar uma palavra. Com índice = ir direto à página certa.

## Criar Índices

```sql
-- Índice simples
CREATE INDEX idx_email ON usuarios(email);

-- Índice único
CREATE UNIQUE INDEX idx_email_unique ON usuarios(email);

-- Índice composto (múltiplas colunas)
CREATE INDEX idx_nome_idade ON usuarios(nome, idade);

-- Índice na criação da tabela
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255),
    INDEX idx_email (email),
    INDEX idx_nome_idade (nome, idade)
);
```

## Quando usar cada tipo de Índice?

### 1. Índice Simples (INDEX)

**Quando usar:**
- Colunas usadas frequentemente em `WHERE`
- Colunas usadas em `JOIN` (chaves estrangeiras)
- Colunas usadas em `ORDER BY`
- Colunas com muitos valores diferentes (alta cardinalidade)

**Exemplos:**

```sql
-- ✅ BOM: Busca frequente por email
SELECT * FROM usuarios WHERE email = 'joao@email.com';
CREATE INDEX idx_email ON usuarios(email);

-- ✅ BOM: JOIN frequente
SELECT * FROM usuarios u
INNER JOIN pedidos p ON u.id = p.usuario_id;
CREATE INDEX idx_usuario_id ON pedidos(usuario_id);

-- ✅ BOM: Ordenação frequente
SELECT * FROM usuarios ORDER BY data_cadastro DESC;
CREATE INDEX idx_data_cadastro ON usuarios(data_cadastro);

-- ❌ EVITAR: Coluna com poucos valores diferentes (ex: sexo: M/F)
-- Índice não ajuda muito, overhead não compensa
```

### 2. Índice Único (UNIQUE INDEX)

**Quando usar:**
- Garantir que valores sejam únicos (além de acelerar buscas)
- Campos que devem ser únicos mas não são chave primária
- Campos usados para login/identificação (email, CPF, etc.)

**Exemplos:**

```sql
-- ✅ BOM: Email deve ser único e é usado em buscas
CREATE UNIQUE INDEX idx_email_unique ON usuarios(email);
-- Garante que não haverá emails duplicados E acelera busca

-- ✅ BOM: CPF único
CREATE UNIQUE INDEX idx_cpf ON usuarios(cpf);

-- ✅ BOM: Username único
CREATE UNIQUE INDEX idx_username ON usuarios(username);

-- Diferença entre UNIQUE INDEX e PRIMARY KEY:
-- PRIMARY KEY: Não pode ser NULL, só uma por tabela
-- UNIQUE INDEX: Pode ser NULL (mas só um NULL único), pode ter vários
```

### 3. Índice Composto (Múltiplas Colunas)

**Quando usar:**
- Quando você busca/ordena por múltiplas colunas juntas
- Quando a combinação de colunas é usada frequentemente
- **IMPORTANTE:** Ordem das colunas importa! (leftmost prefix rule)

**Exemplos:**

```sql
-- ✅ BOM: Busca por nome E idade juntos
SELECT * FROM usuarios WHERE nome = 'João' AND idade = 25;
CREATE INDEX idx_nome_idade ON usuarios(nome, idade);

-- ✅ BOM: Ordenação por múltiplas colunas
SELECT * FROM usuarios ORDER BY cidade, idade DESC;
CREATE INDEX idx_cidade_idade ON usuarios(cidade, idade);

-- ⚠️ ATENÇÃO: Ordem importa!
-- Índice idx_nome_idade (nome, idade) funciona para:
--   ✅ WHERE nome = 'João'
--   ✅ WHERE nome = 'João' AND idade = 25
--   ❌ WHERE idade = 25  (não usa o índice eficientemente!)

-- ✅ BOM: Índice composto para JOIN + filtro
SELECT * FROM pedidos p
INNER JOIN usuarios u ON p.usuario_id = u.id
WHERE p.status = 'pendente' AND p.data_pedido >= '2024-01-01';
CREATE INDEX idx_status_data ON pedidos(status, data_pedido);
```

### 4. Índice na Criação da Tabela

**Quando usar:**
- Quando você já sabe que certas colunas precisarão de índice
- Mais eficiente criar junto com a tabela
- Evita reconstrução da tabela depois

**Exemplo:**

```sql
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Já tem índice automático
    email VARCHAR(255),
    nome VARCHAR(100),
    idade INT,
    cidade VARCHAR(50),
    INDEX idx_email (email),              -- Índice simples
    UNIQUE INDEX idx_email_unique (email), -- Índice único
    INDEX idx_cidade_idade (cidade, idade) -- Índice composto
);
```

## Quando NÃO usar Índices:

```sql
-- ❌ Tabelas muito pequenas (< 1000 registros)
-- Overhead do índice pode ser maior que o benefício

-- ❌ Colunas atualizadas muito frequentemente
-- Cada UPDATE precisa atualizar o índice também

-- ❌ Colunas com poucos valores diferentes (baixa cardinalidade)
-- Ex: sexo (M/F), status (ativo/inativo)
-- Índice não ajuda muito na busca

-- ❌ Colunas raramente usadas em consultas
-- Índice ocupa espaço e torna INSERT/UPDATE mais lentos

-- ❌ Colunas com muitos valores NULL
-- Índices não são muito eficientes com NULL
```

## Regras Gerais:

### ✅ Use Índices quando:
- Tabela tem muitos registros (> 10.000)
- Coluna é usada frequentemente em WHERE, JOIN ou ORDER BY
- Coluna tem alta cardinalidade (muitos valores diferentes)
- Consultas estão lentas e você identificou o gargalo

### ❌ Evite Índices quando:
- Tabela é pequena (< 1.000 registros)
- Coluna é atualizada constantemente
- Coluna tem baixa cardinalidade (poucos valores diferentes)
- Coluna raramente é usada em consultas

## Impacto dos Índices:

**Vantagens:**
- ✅ Acelera SELECT (busca muito mais rápida)
- ✅ Acelera JOINs
- ✅ Acelera ORDER BY
- ✅ Acelera GROUP BY em alguns casos

**Desvantagens:**
- ❌ Torna INSERT mais lento (precisa atualizar índice)
- ❌ Torna UPDATE mais lento (precisa atualizar índice)
- ❌ Torna DELETE mais lento (precisa atualizar índice)
- ❌ Ocupa espaço em disco

## Exemplos Práticos Completos:

```sql
-- 1. Tabela de usuários: índice em email (busca frequente)
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE,  -- Índice único automático
    nome VARCHAR(100),
    INDEX idx_nome (nome)  -- Busca por nome
);

-- 2. Tabela de pedidos: índice em usuario_id (JOIN frequente)
CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    valor DECIMAL(10,2),
    data_pedido DATE,
    status VARCHAR(20),
    INDEX idx_usuario (usuario_id),  -- Para JOIN
    INDEX idx_data (data_pedido),    -- Para filtros de data
    INDEX idx_status_data (status, data_pedido)  -- Busca por status e data
);

-- 3. Ver índices existentes
SHOW INDEX FROM usuarios;

-- 4. Remover índice
DROP INDEX idx_email ON usuarios;

-- 5. Analisar uso de índice (EXPLAIN)
EXPLAIN SELECT * FROM usuarios WHERE email = 'joao@email.com';
-- Verifique se a coluna 'key' mostra o nome do índice usado
```

**IMPORTANTE:**
- Chave primária (`PRIMARY KEY`) automaticamente tem índice
- Chave estrangeira (`FOREIGN KEY`) geralmente precisa de índice manual
- Use `EXPLAIN` para verificar se seus índices estão sendo usados
- Monitore performance: se INSERT/UPDATE ficarem lentos, pode ser excesso de índices
