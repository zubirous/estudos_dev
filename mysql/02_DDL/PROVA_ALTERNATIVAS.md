# Prova: DDL (Data Definition Language) - MySQL

## Provas de Alternativas

## Questão 1 (Múltipla Escolha)
Qual constraint garante que um campo não pode ser NULL?

a) UNIQUE
b) NOT NULL
c) PRIMARY KEY
d) DEFAULT

**Resposta:** b) NOT NULL


---

## Questão 2 (Múltipla Escolha)
O que faz AUTO_INCREMENT?

a) Cria automaticamente valores únicos incrementando
b) Cria automaticamente valores aleatórios
c) Cria automaticamente valores zero
d) Não faz nada

**Resposta:** a) Cria automaticamente valores únicos incrementando


---

## Questão 3 (Múltipla Escolha)
Qual ação ON DELETE deve ser usada se você quer deletar um registro e automaticamente deletar todos os registros relacionados?

a) RESTRICT
b) CASCADE
c) SET NULL
d) NO ACTION

**Resposta:** b) CASCADE


---

## Questão 4 (Múltipla Escolha)
Qual comando remove uma tabela e todos seus dados?

a) DELETE TABLE
b) TRUNCATE TABLE
c) DROP TABLE
d) REMOVE TABLE

**Resposta:** c) DROP TABLE


---

## Questão 5 (Múltipla Escolha)
Qual comando é usado para adicionar uma constraint UNIQUE a uma coluna existente?

a) ADD UNIQUE
b) ALTER TABLE ADD CONSTRAINT
c) MODIFY UNIQUE
d) CREATE UNIQUE

**Resposta:** b) ALTER TABLE ADD CONSTRAINT

---

## Questão 6 (Múltipla Escolha)
Qual a diferença entre PRIMARY KEY e UNIQUE?

a) Não há diferença
b) PRIMARY KEY não permite NULL, UNIQUE permite um NULL
c) PRIMARY KEY permite múltiplas, UNIQUE não
d) PRIMARY KEY é mais rápido

**Resposta:** b) PRIMARY KEY não permite NULL e só pode haver uma por tabela, UNIQUE permite um NULL e pode haver múltiplas.

---

## Questão 7 (Múltipla Escolha)
Qual comando adiciona uma coluna a uma tabela existente?

a) ADD COLUMN
b) ALTER TABLE ADD COLUMN
c) INSERT COLUMN
d) CREATE COLUMN

**Resposta:** b) ALTER TABLE tabela ADD COLUMN nome_tipo

---

## Questão 8 (Múltipla Escolha)
Qual comando remove uma coluna de uma tabela?

a) DELETE COLUMN
b) DROP COLUMN
c) REMOVE COLUMN
d) DROP TABLE

**Resposta:** b) ALTER TABLE tabela DROP COLUMN nome_coluna

---

## Questão 9 (Múltipla Escolha)
Qual comando modifica uma coluna existente?

a) MODIFY COLUMN
b) CHANGE COLUMN
c) ALTER COLUMN
d) Todas as alternativas acima

**Resposta:** d) Todas as alternativas acima - MODIFY e CHANGE podem modificar colunas

---

## Questão 10 (Múltipla Escolha)
FOREIGN KEY com RESTRICT:

a) Deleta registros relacionados
b) Impede ação se houver registros relacionados
c) Define valor NULL
d) Não faz nada

**Resposta:** b) Impede ação se houver registros relacionados - bloqueia DELETE ou UPDATE

---

## Questão 11 (Múltipla Escolha)
A constraint CHECK (MySQL 8.0.16+):

a) Valida valores inseridos
b) Cria índice
c) Define chave primária
d) Cria foreign key

**Resposta:** a) Valida valores inseridos - verifica se valor atende condição

---

## Questão 12 (Múltipla Escolha)
Qual comando cria uma constraint FOREIGN KEY?

a) CREATE FOREIGN KEY
b) ADD CONSTRAINT FOREIGN KEY
c) ADD FOREIGN KEY
d) Todas as alternativas acima

**Resposta:** d) Todas as alternativas acima - diferentes formas de criar FOREIGN KEY

---

## Questão 13 (Múltipla Escolha)
O valor padrão de uma coluna é usado quando:

a) Valor é especificado
b) Valor não é especificado
c) Valor é NULL
d) Valor é zero

**Resposta:** b) Valor não é especificado - DEFAULT é usado quando valor não é fornecido

---

## Questão 14 (Múltipla Escolha)
Qual comando remove uma constraint de uma tabela?

a) DROP CONSTRAINT
b) DELETE CONSTRAINT
c) REMOVE CONSTRAINT
d) DROP TABLE

**Resposta:** a) ALTER TABLE tabela DROP CONSTRAINT nome_constraint

---

## Questão 15 (Múltipla Escolha)
AUTO_INCREMENT é usado para:

a) Criar valores únicos incrementando automaticamente
b) Criar valores aleatórios
c) Criar valores zero
d) Não faz nada

**Resposta:** a) Criar valores únicos incrementando automaticamente - comum em chaves primárias