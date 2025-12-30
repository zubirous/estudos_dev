# Prova: DML (Data Manipulation Language) - MySQL

## Provas de Verdadeiro ou Falso

## Questão 1 (Verdadeiro/Falso)
É possível usar WHERE com TRUNCATE TABLE.

**Resposta:** Falso. TRUNCATE TABLE remove todos os registros e não aceita WHERE.


---

## Questão 2 (Verdadeiro/Falso)
INSERT IGNORE ignora apenas erros de chave primária duplicada.

**Resposta:** Verdadeiro. INSERT IGNORE ignora erros de chave primária e chave única duplicada, continuando com os outros registros.

---

## Questão 3 (Verdadeiro/Falso)
DELETE sem WHERE deleta todos os registros da tabela.

**Resposta:** Verdadeiro. DELETE sem cláusula WHERE deleta todos os registros, mas é mais lento que TRUNCATE.

---

## Questão 4 (Verdadeiro/Falso)
UPDATE sem WHERE atualiza todos os registros da tabela.

**Resposta:** Verdadeiro. UPDATE sem cláusula WHERE atualiza todos os registros da tabela, o que geralmente não é desejado.

---

## Questão 5 (Verdadeiro/Falso)
INSERT IGNORE ignora erros e continua inserindo outros registros.

**Resposta:** Verdadeiro. INSERT IGNORE ignora erros (ex: chave duplicada) e continua inserindo os outros registros da lista.

---

## Questão 6 (Verdadeiro/Falso)
TRUNCATE TABLE reseta o AUTO_INCREMENT.

**Resposta:** Verdadeiro. TRUNCATE TABLE reseta o AUTO_INCREMENT, fazendo o próximo valor ser 1.

---

## Questão 7 (Verdadeiro/Falso)
INSERT ... ON DUPLICATE KEY UPDATE pode inserir ou atualizar baseado em chave duplicada.

**Resposta:** Verdadeiro. Se a chave primária ou única já existir, atualiza. Se não existir, insere novo registro.

---

## Questão 8 (Verdadeiro/Falso)
UPDATE com JOIN é útil para atualizar uma tabela baseado em condições de outra tabela.

**Resposta:** Verdadeiro. UPDATE com JOIN permite atualizar uma tabela usando condições de outra tabela relacionada.