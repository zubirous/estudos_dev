# Prova: OTIMIZAÇÃO - MySQL

## Provas de Alternativas

## Questão 1 (Múltipla Escolha)
Qual comando analisa o plano de execução de uma query?

a) ANALYZE
b) EXPLAIN
c) DEBUG
d) CHECK

**Resposta:** b) EXPLAIN

---

## Questão 2 (Múltipla Escolha)
Qual é uma boa prática para otimizar queries?

a) Usar SELECT * sempre
b) Evitar índices
c) Usar índices em colunas de WHERE, JOIN, ORDER BY
d) Usar funções em colunas de WHERE

**Resposta:** c) Usar índices em colunas de WHERE, JOIN, ORDER BY

---

## Questão 3 (Múltipla Escolha)
Por que evitar SELECT *?

a) Retorna muitas colunas desnecessárias
b) Aumenta uso de memória e rede
c) Pode tornar queries mais lentas
d) Todas as alternativas acima

**Resposta:** d) Todas as alternativas acima

---

## Questão 4 (Múltipla Escolha)
Por que evitar funções em colunas de WHERE?

a) Funções impedem uso de índices
b) Funções são mais rápidas
c) Funções não afetam performance
d) Funções são obrigatórias

**Resposta:** a) Funções impedem uso de índices - WHERE YEAR(data) = 2024 é lento, melhor usar WHERE data >= '2024-01-01'

---

## Questão 5 (Múltipla Escolha)
Qual tipo de acesso é o pior no EXPLAIN?

a) index
b) range
c) ALL
d) ref

**Resposta:** c) ALL - significa que todas as linhas da tabela são examinadas (full table scan)

---

## Questão 6 (Múltipla Escolha)
Para otimizar queries grandes, use:

a) SELECT *
b) LIMIT
c) Sem filtros
d) Múltiplas queries desnecessárias

**Resposta:** b) LIMIT - limita quantidade de resultados retornados

---

## Questão 7 (Múltipla Escolha)
O que significa type: ALL no EXPLAIN?

a) Usa índice
b) Full table scan - examina todas as linhas
c) Busca rápida
d) Usa cache

**Resposta:** b) Full table scan - examina todas as linhas da tabela (pior performance)

---

## Questão 8 (Múltipla Escolha)
Qual é uma boa prática para otimizar queries?

a) Usar funções em WHERE
b) Selecionar apenas colunas necessárias
c) Usar SELECT * sempre
d) Não usar índices

**Resposta:** b) Selecionar apenas colunas necessárias - reduz uso de memória e rede

---

## Questão 9 (Múltipla Escolha)
Por que usar LIMIT em queries grandes?

a) Limita quantidade de resultados
b) Reduz processamento e uso de memória
c) Melhora performance
d) Todas as alternativas acima

**Resposta:** d) Todas as alternativas acima

---

## Questão 10 (Múltipla Escolha)
O que o EXPLAIN mostra sobre uma query?

a) Plano de execução
b) Índices usados
c) Linhas examinadas
d) Todas as alternativas acima

**Resposta:** d) Todas as alternativas acima - EXPLAIN mostra como o MySQL executa a query