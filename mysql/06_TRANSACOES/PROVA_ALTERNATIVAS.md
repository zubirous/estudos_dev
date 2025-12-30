# Prova: TRANSAÇÕES - MySQL

## Provas de Alternativas

## Questão 1 (Múltipla Escolha)
O que significa ACID em transações?

a) Atomicity, Consistency, Isolation, Durability
b) Array, Collection, Index, Database
c) Apenas um acrônimo sem significado
d) Add, Create, Insert, Delete

**Resposta:** a) Atomicity, Consistency, Isolation, Durability

---

## Questão 2 (Múltipla Escolha)
Qual comando desfaz todas as mudanças de uma transação?

a) COMMIT
b) ROLLBACK
c) START TRANSACTION
d) END TRANSACTION

**Resposta:** b) ROLLBACK

---

## Questão 3 (Múltipla Escolha)
O que significa Atomicidade em transações?

a) Tudo ou nada - transação completa ou nenhuma mudança
b) Transações não interferem umas nas outras
c) Mudanças permanecem após commit
d) Banco sempre em estado válido

**Resposta:** a) Tudo ou nada - transação completa ou nenhuma mudança

---

## Questão 4 (Múltipla Escolha)
Qual é o nível de isolamento padrão do MySQL InnoDB?

a) READ UNCOMMITTED
b) READ COMMITTED
c) REPEATABLE READ
d) SERIALIZABLE

**Resposta:** c) REPEATABLE READ - é o padrão do MySQL InnoDB

---

## Questão 5 (Múltipla Escolha)
Qual comando confirma e salva permanentemente as mudanças de uma transação?

a) ROLLBACK
b) COMMIT
c) START TRANSACTION
d) SAVE

**Resposta:** b) COMMIT - confirma e salva permanentemente as mudanças

---

## Questão 6 (Múltipla Escolha)
O que significa Durabilidade em transações ACID?

a) Transações não interferem umas nas outras
b) Mudanças permanecem após commit
c) Banco sempre em estado válido
d) Tudo ou nada

**Resposta:** b) Mudanças permanecem após commit - durabilidade garante persistência

---

## Questão 7 (Múltipla Escolha)
O que significa Consistência em transações ACID?

a) Tudo ou nada
b) Transações não interferem umas nas outras
c) Banco sempre em estado válido
d) Mudanças permanecem após commit

**Resposta:** c) Banco sempre em estado válido - consistência garante que o banco mantém regras e constraints válidas

---

## Questão 8 (Múltipla Escolha)
O que significa Isolamento em transações ACID?

a) Tudo ou nada
b) Transações não interferem umas nas outras
c) Banco sempre em estado válido
d) Mudanças permanecem após commit

**Resposta:** b) Transações não interferem umas nas outras - isolamento garante que transações concorrentes não interferem

---

## Questão 9 (Múltipla Escolha)
Qual comando inicia uma transação?

a) COMMIT
b) ROLLBACK
c) START TRANSACTION ou BEGIN
d) END TRANSACTION

**Resposta:** c) START TRANSACTION ou BEGIN - ambos iniciam uma transação

---

## Questão 10 (Múltipla Escolha)
Qual nível de isolamento é o mais rápido mas menos seguro?

a) READ UNCOMMITTED
b) READ COMMITTED
c) REPEATABLE READ
d) SERIALIZABLE

**Resposta:** a) READ UNCOMMITTED - menos isolamento, mais rápido, mas pode ler dados não commitados