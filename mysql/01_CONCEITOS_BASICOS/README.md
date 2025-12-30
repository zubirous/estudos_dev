# 1. CONCEITOS BÁSICOS - MySQL

## Banco de Dados Relacional
- **Tabela**: Estrutura que armazena dados em linhas (registros) e colunas (campos)
- **Chave Primária (PK)**: Identificador único de cada registro (não pode ser NULL, não pode repetir)
- **Chave Estrangeira (FK)**: Referência a chave primária de outra tabela
- **Índice**: Estrutura que acelera consultas (similar ao índice de um livro)

## Tipos de Dados Principais

### Numéricos:
- `INT` / `INTEGER`: Números inteiros (-2.147.483.648 a 2.147.483.647)
- `BIGINT`: Números inteiros grandes
- `DECIMAL(M,D)` / `NUMERIC(M,D)`: Números decimais precisos (M=total dígitos, D=decimais)
- `FLOAT` / `DOUBLE`: Números de ponto flutuante (aproximados)

### Strings:
- `VARCHAR(n)`: String de tamanho variável até n caracteres (usa apenas espaço necessário)
- `CHAR(n)`: String de tamanho fixo com n caracteres (preenche com espaços)
- `TEXT`: String longa (até 65.535 caracteres)
- `LONGTEXT`: String muito longa

### Data/Hora:
- `DATE`: Data (YYYY-MM-DD)
- `TIME`: Hora (HH:MM:SS)
- `DATETIME`: Data e hora (YYYY-MM-DD HH:MM:SS)
- `TIMESTAMP`: Data e hora com timezone (auto-atualiza em alguns casos)
  - Valor padrão: `CURRENT_TIMESTAMP` (quando não especificado)
  - Pode auto-atualizar quando o registro é modificado (se configurado)

### Booleanos:
- `BOOLEAN` / `BOOL`: Armazenado como TINYINT(1), 0=FALSE, 1=TRUE

### ENUM:
- `ENUM('valor1', 'valor2', ...)`: Lista de valores permitidos (conjunto fixo e limitado)
- Mais eficiente em armazenamento e validação automática
- Menos flexível que VARCHAR
- Use quando tiver conjunto fixo de valores (ex: status: 'ativo', 'inativo', 'pendente')

**Exemplo:**
```sql
CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    status ENUM('ativo', 'inativo', 'pendente') DEFAULT 'pendente'
);
```

## Conceitos Importantes:

**Chave Primária (PK):**
- Identifica unicamente um registro na própria tabela
- Não pode ser NULL
- Não pode repetir
- Automaticamente tem índice

**Chave Estrangeira (FK):**
- Referencia PK de outra tabela
- Cria relacionamento entre tabelas
- Pode ser NULL (se permitido)
- Pode repetir (permite múltiplos relacionamentos)

**VARCHAR vs CHAR:**
- **VARCHAR**: Tamanho variável, usa apenas espaço necessário (mais comum)
- **CHAR**: Tamanho fixo, preenche com espaços (para campos de tamanho fixo conhecido)

