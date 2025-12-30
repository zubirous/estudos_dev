# Prova: TRIGGERS - MySQL

## Provas de Verdadeiro ou Falso

## Questão 1 (Verdadeiro/Falso)
Triggers executam automaticamente quando ocorrem operações INSERT, UPDATE ou DELETE.

**Resposta:** Verdadeiro. Triggers são acionados automaticamente por essas operações.

---

## Questão 2 (Verdadeiro/Falso)
Um trigger BEFORE INSERT pode modificar os valores antes de inserir no banco.

**Resposta:** Verdadeiro. Triggers BEFORE podem modificar valores usando SET NEW.coluna = valor.

---

## Questão 3 (Verdadeiro/Falso)
Triggers AFTER podem impedir uma operação.

**Resposta:** Falso. Triggers AFTER executam depois da operação, então não podem impedi-la. Apenas triggers BEFORE podem fazer isso.

---

## Questão 4 (Verdadeiro/Falso)
Triggers são úteis para auditoria de dados.

**Resposta:** Verdadeiro. Triggers AFTER são comumente usados para registrar mudanças em tabelas de auditoria.

---

## Questão 5 (Verdadeiro/Falso)
É possível ter múltiplos triggers para a mesma operação em uma tabela.

**Resposta:** Verdadeiro. Pode haver múltiplos triggers para a mesma operação (ex: múltiplos BEFORE INSERT).

---

## Questão 6 (Verdadeiro/Falso)
OLD está disponível em triggers BEFORE INSERT.

**Resposta:** Falso. OLD está disponível apenas em triggers AFTER UPDATE e AFTER DELETE. BEFORE INSERT só tem NEW.

