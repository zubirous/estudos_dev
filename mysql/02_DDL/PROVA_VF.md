# Prova: DDL (Data Definition Language) - MySQL

## Provas de Verdadeiro ou Falso

## Questão 1 (Verdadeiro/Falso)
AUTO_INCREMENT funciona apenas com tipos INT e BIGINT.

**Resposta:** Verdadeiro. AUTO_INCREMENT funciona apenas com tipos INT e BIGINT.

---

## Questão 2 (Verdadeiro/Falso)
Uma tabela pode ter múltiplas PRIMARY KEY.

**Resposta:** Falso. Uma tabela pode ter apenas uma PRIMARY KEY, mas pode ter múltiplas UNIQUE.

---

## Questão 3 (Verdadeiro/Falso)
FOREIGN KEY com CASCADE deleta automaticamente registros relacionados.

**Resposta:** Verdadeiro. FOREIGN KEY com CASCADE propaga a ação (DELETE ou UPDATE) para registros relacionados.

---

## Questão 4 (Verdadeiro/Falso)
CHECK constraint é suportada em todas as versões do MySQL.

**Resposta:** Falso. CHECK constraint foi adicionada apenas no MySQL 8.0.16+.

---

## Questão 5 (Verdadeiro/Falso)
DEFAULT define valor padrão para uma coluna quando não especificado.

**Resposta:** Verdadeiro. DEFAULT define valor padrão que é usado quando um valor não é especificado na inserção.

---

## Questão 6 (Verdadeiro/Falso)
ALTER TABLE pode adicionar, modificar e remover colunas.

**Resposta:** Verdadeiro. ALTER TABLE permite adicionar (ADD), modificar (MODIFY) e remover (DROP) colunas de uma tabela existente.

---

## Questão 7 (Verdadeiro/Falso)
PRIMARY KEY não permite NULL e não pode repetir valores.

**Resposta:** Verdadeiro. PRIMARY KEY combina UNIQUE + NOT NULL, garantindo valores únicos e não nulos.

---

## Questão 8 (Verdadeiro/Falso)
UNIQUE permite múltiplas constraints na mesma tabela.

**Resposta:** Verdadeiro. Uma tabela pode ter múltiplas constraints UNIQUE, ao contrário de PRIMARY KEY que só permite uma.