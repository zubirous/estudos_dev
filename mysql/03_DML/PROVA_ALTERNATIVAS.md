# Prova: DML (Data Manipulation Language) - MySQL

## Provas de Alternativas

## Questão 1 (Múltipla Escolha)
Qual comando remove todos os dados mas mantém a estrutura da tabela e reseta AUTO_INCREMENT?

a) DELETE FROM tabela
b) TRUNCATE TABLE tabela
c) DROP TABLE tabela
d) REMOVE FROM tabela

**Resposta:** b) TRUNCATE TABLE tabela


---

## Questão 2 (Múltipla Escolha)
Qual é a diferença entre DELETE e TRUNCATE?

a) Não há diferença
b) DELETE pode ter WHERE, TRUNCATE não pode
c) TRUNCATE pode ter WHERE, DELETE não pode
d) DELETE remove a tabela, TRUNCATE remove apenas dados

**Resposta:** b) DELETE pode ter WHERE, TRUNCATE não pode


---

## Questão 3 (Múltipla Escolha)
Qual comando é mais rápido para remover todos os registros de uma tabela?

a) DELETE FROM tabela
b) TRUNCATE TABLE tabela
c) DROP TABLE tabela
d) São iguais

**Resposta:** b) TRUNCATE TABLE tabela - é mais rápido porque não registra cada linha deletada individualmente.

---

## Questão 4 (Múltipla Escolha)
O que faz INSERT ... ON DUPLICATE KEY UPDATE?

a) Atualiza sempre
b) Insere se não existir, atualiza se existir (baseado em PK/UNIQUE)
c) Deleta duplicados
d) Ignora duplicados

**Resposta:** b) Insere se não existir, atualiza se existir baseado em chave primária ou única.

---

## Questão 5 (Múltipla Escolha)
O que faz INSERT IGNORE?

a) Insere sempre
b) Ignora erros de chave primária/única duplicada e continua
c) Deleta duplicados
d) Atualiza duplicados

**Resposta:** b) Ignora erros de chave primária/única duplicada e continua com outros registros

---

## Questão 6 (Múltipla Escolha)
Qual comando remove uma tabela completamente (estrutura e dados)?

a) DELETE TABLE
b) TRUNCATE TABLE
c) DROP TABLE
d) REMOVE TABLE

**Resposta:** c) DROP TABLE - remove tabela completamente (estrutura e dados)

---

## Questão 7 (Múltipla Escolha)
Qual é a diferença entre DELETE e TRUNCATE em relação a AUTO_INCREMENT?

a) Ambos resetam AUTO_INCREMENT
b) DELETE mantém AUTO_INCREMENT, TRUNCATE reseta
c) DELETE reseta, TRUNCATE mantém
d) Nenhum afeta AUTO_INCREMENT

**Resposta:** b) DELETE mantém AUTO_INCREMENT (continua do último valor), TRUNCATE reseta AUTO_INCREMENT (volta para 1)

---

## Questão 8 (Múltipla Escolha)
UPDATE com JOIN permite:

a) Atualizar apenas uma tabela
b) Atualizar uma tabela baseado em condições de outra tabela
c) Atualizar múltiplas tabelas simultaneamente
d) Não é possível usar UPDATE com JOIN

**Resposta:** b) Atualizar uma tabela baseado em condições de outra tabela - útil para atualizações complexas