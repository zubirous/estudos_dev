# Prova: NORMALIZAÇÃO - MySQL

## Provas de Verdadeiro ou Falso

## Questão 1 (Verdadeiro/Falso)
Normalização sempre melhora a performance de consultas.

**Resposta:** Falso. Normalização pode piorar performance em algumas consultas porque requer mais JOINs, mas melhora integridade e reduz redundância.

---

## Questão 2 (Verdadeiro/Falso)
Para estar em 2FN, a tabela deve estar primeiro em 1FN.

**Resposta:** Verdadeiro. As formas normais são cumulativas - para estar em 2FN, deve estar em 1FN primeiro.

---

## Questão 3 (Verdadeiro/Falso)
Normalização elimina completamente a redundância de dados.

**Resposta:** Falso. Normalização reduz redundância, mas pode não eliminá-la completamente. O objetivo é reduzir ao mínimo necessário.

---

## Questão 4 (Verdadeiro/Falso)
Uma tabela normalizada sempre tem melhor performance que uma não normalizada.

**Resposta:** Falso. Tabelas normalizadas podem ter performance pior em algumas consultas que requerem múltiplos JOINs, mas têm melhor integridade de dados.

---

## Questão 5 (Verdadeiro/Falso)
Dependência transitiva ocorre quando A → B → C, onde A não depende diretamente de C.

**Resposta:** Verdadeiro. Dependência transitiva é quando um atributo depende indiretamente de outro através de um terceiro atributo.