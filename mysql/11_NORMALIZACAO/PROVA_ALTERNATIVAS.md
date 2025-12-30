# Prova: NORMALIZAÇÃO - MySQL

## Provas de Alternativas

## Questão 1 (Múltipla Escolha)
O que é normalização?

a) Processo de organizar dados para reduzir redundância
b) Processo de aumentar redundância
c) Processo de deletar dados
d) Não é um conceito de banco de dados

**Resposta:** a) Processo de organizar dados para reduzir redundância

---

## Questão 2 (Múltipla Escolha)
Na 1FN (Primeira Forma Normal), cada coluna deve ter:

a) Múltiplos valores
b) Apenas um valor atômico
c) Nenhum valor
d) Valores nulos

**Resposta:** b) Apenas um valor atômico

---

## Questão 3 (Múltipla Escolha)
O que é a 2FN (Segunda Forma Normal)?

a) Cada coluna tem um valor atômico
b) Está em 1FN e todos atributos não-chave dependem totalmente da chave primária
c) Não há dependência transitiva
d) Tabela não tem redundância

**Resposta:** b) Está em 1FN e todos atributos não-chave dependem totalmente da chave primária

---

## Questão 4 (Múltipla Escolha)
O que é a 3FN (Terceira Forma Normal)?

a) Cada coluna tem um valor atômico
b) Todos atributos dependem da chave primária
c) Está em 2FN e não há dependência transitiva
d) Tabela não tem chave primária

**Resposta:** c) Está em 2FN e não há dependência transitiva

---

## Questão 5 (Múltipla Escolha)
O que é dependência transitiva?

a) A → B → C, onde A depende de C
b) A depende diretamente de B
c) A não depende de nada
d) B depende de A

**Resposta:** a) A → B → C, onde A depende indiretamente de C através de B (dependência transitiva)

---

## Questão 6 (Múltipla Escolha)
Qual é o objetivo principal da normalização?

a) Aumentar redundância
b) Reduzir redundância e melhorar integridade
c) Aumentar performance
d) Simplificar consultas

**Resposta:** b) Reduzir redundância e melhorar integridade dos dados

---

## Questão 7 (Múltipla Escolha)
Normalização sempre melhora performance?

a) Sim, sempre
b) Não, pode piorar performance em algumas consultas
c) Não afeta performance
d) Sempre piora performance

**Resposta:** b) Não, pode piorar performance em algumas consultas porque requer mais JOINs, mas melhora integridade

---

## Questão 8 (Múltipla Escolha)
Em uma tabela normalizada, onde ficam informações sobre clientes?

a) Na tabela de pedidos
b) Em uma tabela separada de clientes
c) Em múltiplas tabelas
d) Não é armazenado

**Resposta:** b) Em uma tabela separada de clientes - normalização separa dados relacionados em tabelas diferentes

---

## Questão 9 (Múltipla Escolha)
Qual problema a normalização resolve?

a) Performance lenta
b) Redundância de dados e inconsistência
c) Falta de índices
d) Falta de chaves primárias

**Resposta:** b) Redundância de dados e inconsistência - normalização reduz duplicação e melhora integridade

---

## Questão 10 (Múltipla Escolha)
Uma tabela em 3FN está também em:

a) Apenas 1FN
b) 1FN e 2FN
c) Apenas 2FN
d) Nenhuma forma normal

**Resposta:** b) 1FN e 2FN - para estar em 3FN, deve estar também em 2FN e 1FN