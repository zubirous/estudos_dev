# Prova: CONCEITOS BÁSICOS - MySQL

## Provas de Alternativas

## Questão 1 (Múltipla Escolha)
Qual a diferença entre VARCHAR e CHAR?

a) VARCHAR é para números, CHAR é para texto
b) VARCHAR tem tamanho variável, CHAR tem tamanho fixo
c) VARCHAR só aceita letras, CHAR aceita números
d) Não há diferença

**Resposta:** b) VARCHAR tem tamanho variável, CHAR tem tamanho fixo


---

## Questão 2 (Múltipla Escolha)
O que é uma Chave Primária (PK)?

a) Uma referência para outra tabela
b) Identificador único de cada registro (não pode ser NULL, não pode repetir)
c) Um campo que pode repetir valores
d) Um campo obrigatório mas pode ter valores duplicados

**Resposta:** b) Identificador único de cada registro (não pode ser NULL, não pode repetir)


---

## Questão 3 (Múltipla Escolha)
O que é uma Chave Estrangeira (FK)?

a) Identificador único de cada registro
b) Referência a chave primária de outra tabela
c) Um campo obrigatório
d) Um tipo de dado

**Resposta:** b) Referência a chave primária de outra tabela


---

## Questão 4 (Múltipla Escolha)
Qual tipo de dado é melhor para armazenar valores monetários?

a) FLOAT
b) DOUBLE
c) DECIMAL(10,2)
d) INT

**Resposta:** c) DECIMAL(10,2) - oferece precisão exata, enquanto FLOAT e DOUBLE são aproximados.


---

## Questão 5 (Múltipla Escolha)
Qual é o valor padrão de um campo do tipo TIMESTAMP quando não especificado?

a) NULL
b) CURRENT_TIMESTAMP
c) 1970-01-01
d) 0000-00-00

**Resposta:** b) CURRENT_TIMESTAMP

---

## Questão 6 (Múltipla Escolha)
Qual tipo de dado é melhor para armazenar emails?

a) CHAR(100)
b) VARCHAR(255)
c) TEXT
d) ENUM

**Resposta:** b) VARCHAR(255) - tamanho variável e suficiente para emails

---

## Questão 7 (Múltipla Escolha)
Qual tipo de dado é melhor para armazenar descrição longa?

a) VARCHAR(255)
b) TEXT
c) CHAR(100)
d) ENUM

**Resposta:** b) TEXT - adequado para textos longos (até 65.535 caracteres)

---

## Questão 8 (Múltipla Escolha)
Qual tipo de dado é melhor para armazenar código de país (ex: "BRA", "USA")?

a) VARCHAR(3)
b) CHAR(3)
c) TEXT
d) ENUM

**Resposta:** b) CHAR(3) - tamanho fixo de 3 caracteres, mais eficiente

---

## Questão 9 (Múltipla Escolha)
Qual tipo de dado armazena números decimais com precisão exata?

a) FLOAT
b) DOUBLE
c) DECIMAL
d) INT

**Resposta:** c) DECIMAL - oferece precisão exata, enquanto FLOAT e DOUBLE são aproximados

---

## Questão 10 (Múltipla Escolha)
Qual tipo de dado é melhor para armazenar data apenas (sem hora)?

a) DATETIME
b) TIMESTAMP
c) DATE
d) TIME

**Resposta:** c) DATE - armazena apenas data (YYYY-MM-DD)

---

## Questão 11 (Múltipla Escolha)
O que é um índice em banco de dados?

a) Chave primária
b) Estrutura que acelera consultas
c) Chave estrangeira
d) Tipo de dado

**Resposta:** b) Estrutura que acelera consultas - similar ao índice de um livro

---

## Questão 12 (Múltipla Escolha)
ENUM é melhor que VARCHAR para:

a) Valores que mudam frequentemente
b) Conjunto fixo e limitado de valores
c) Textos longos
d) Valores numéricos

**Resposta:** b) Conjunto fixo e limitado de valores - mais eficiente e validação automática