# Prova: DQL (Data Query Language) - MySQL

## Provas de Verdadeiro ou Falso

## Questão 1 (Verdadeiro/Falso)
SELECT DISTINCT remove valores duplicados dos resultados.

**Resposta:** Verdadeiro. SELECT DISTINCT retorna apenas valores únicos, removendo duplicatas.

---

## Questão 2 (Verdadeiro/Falso)
WHERE pode usar funções de agregação como COUNT(*).

**Resposta:** Falso. WHERE não pode usar funções de agregação. Use HAVING após GROUP BY para filtrar com funções de agregação.

---

## Questão 3 (Verdadeiro/Falso)
BETWEEN é inclusivo, ou seja, inclui os valores de início e fim.

**Resposta:** Verdadeiro. BETWEEN 18 AND 65 inclui tanto 18 quanto 65.

---

## Questão 4 (Verdadeiro/Falso)
LEFT JOIN retorna todos os registros da tabela da esquerda, mesmo que não tenham correspondência na direita.

**Resposta:** Verdadeiro. LEFT JOIN retorna todos os registros da tabela da esquerda, com NULL nos campos da direita se não houver correspondência.

---

## Questão 5 (Verdadeiro/Falso)
INNER JOIN retorna apenas registros que têm correspondência em ambas as tabelas.

**Resposta:** Verdadeiro. INNER JOIN retorna apenas registros onde há correspondência entre as tabelas.

---

## Questão 6 (Verdadeiro/Falso)
ORDER BY pode ordenar por múltiplas colunas.

**Resposta:** Verdadeiro. ORDER BY pode ordenar por múltiplas colunas, exemplo: ORDER BY ativo DESC, nome ASC.

---

## Questão 7 (Verdadeiro/Falso)
LIMIT 10 OFFSET 20 retorna os primeiros 10 registros da tabela.

**Resposta:** Falso. LIMIT 10 OFFSET 20 pula os primeiros 20 registros e retorna os próximos 10.

---

## Questão 8 (Verdadeiro/Falso)
COUNT(*) conta todas as linhas, incluindo NULL.

**Resposta:** Verdadeiro. COUNT(*) conta todas as linhas, mesmo que contenham NULL. COUNT(coluna) não conta NULL.

