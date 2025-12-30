# Prova: ÍNDICES - MySQL

## Provas de Alternativas

## Questão 1 (Múltipla Escolha)
O que são índices em banco de dados?

a) Chaves estrangeiras
b) Estruturas que aceleram consultas
c) Tipos de dados
d) Constraints

**Resposta:** b) Estruturas que aceleram consultas

---

## Questão 2 (Múltipla Escolha)
Em que situações é recomendado usar índices?

a) Tabelas muito pequenas
b) Colunas atualizadas constantemente
c) Colunas usadas frequentemente em WHERE e JOINs
d) Nunca usar índices

**Resposta:** c) Colunas usadas frequentemente em WHERE e JOINs

---

## Questão 3 (Múltipla Escolha)
Qual comando cria um índice simples?

a) ADD INDEX
b) CREATE INDEX
c) MAKE INDEX
d) NEW INDEX

**Resposta:** b) CREATE INDEX

---

## Questão 4 (Múltipla Escolha)
O que é um índice composto?

a) Índice em uma única coluna
b) Índice em múltiplas colunas
c) Índice único
d) Índice primário

**Resposta:** b) Índice em múltiplas colunas

---

## Questão 5 (Múltipla Escolha)
Índices tornam quais operações mais lentas?

a) SELECT
b) INSERT e UPDATE
c) DELETE
d) CREATE TABLE

**Resposta:** b) INSERT e UPDATE - índices aceleram SELECT mas tornam INSERT/UPDATE mais lentos

---

## Questão 6 (Múltipla Escolha)
A chave primária tem índice automaticamente?

a) Sim, sempre
b) Não, nunca
c) Apenas se especificado
d) Apenas em tabelas grandes

**Resposta:** a) Sim, sempre - chave primária automaticamente cria um índice

---

## Questão 7 (Múltipla Escolha)
Qual comando cria um índice único?

a) CREATE INDEX
b) CREATE UNIQUE INDEX
c) CREATE INDEX UNIQUE
d) ADD UNIQUE INDEX

**Resposta:** b) CREATE UNIQUE INDEX

---

## Questão 8 (Múltipla Escolha)
Índices são recomendados para colunas usadas em:

a) Apenas WHERE
b) WHERE, JOIN, ORDER BY
c) Apenas JOIN
d) Nunca usar índices

**Resposta:** b) WHERE, JOIN, ORDER BY - índices aceleram essas operações

---

## Questão 9 (Múltipla Escolha)
O que acontece quando você cria muitos índices em uma tabela?

a) Melhora performance de todas operações
b) Piora performance de INSERT/UPDATE
c) Não afeta performance
d) Acelera apenas SELECT

**Resposta:** b) Piora performance de INSERT/UPDATE - cada índice precisa ser atualizado

---

## Questão 10 (Múltipla Escolha)
Como deletar um índice?

a) DELETE INDEX
b) DROP INDEX
c) REMOVE INDEX
d) DROP TABLE

**Resposta:** b) DROP INDEX nome_do_indice ON nome_da_tabela