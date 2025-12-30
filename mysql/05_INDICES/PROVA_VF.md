# Prova: ÍNDICES - MySQL

## Provas de Verdadeiro ou Falso

## Questão 1 (Verdadeiro/Falso)
Índices sempre melhoram a performance de todas as operações.

**Resposta:** Falso. Índices aceleram SELECT mas podem tornar INSERT/UPDATE mais lentos.

---

## Questão 2 (Verdadeiro/Falso)
Chave primária automaticamente cria um índice.

**Resposta:** Verdadeiro. Chave primária sempre tem índice automaticamente para garantir unicidade e busca rápida.

---

## Questão 3 (Verdadeiro/Falso)
Índices são recomendados para tabelas muito pequenas.

**Resposta:** Falso. Índices têm overhead e não compensam em tabelas muito pequenas, onde a busca sequencial já é rápida.

---

## Questão 4 (Verdadeiro/Falso)
Índice composto pode ser criado em múltiplas colunas.

**Resposta:** Verdadeiro. Índice composto permite indexar múltiplas colunas juntas, útil para consultas que usam várias colunas.

---

## Questão 5 (Verdadeiro/Falso)
Índices devem ser criados em colunas usadas em ORDER BY.

**Resposta:** Verdadeiro. Índices em colunas usadas em ORDER BY aceleram a ordenação dos resultados.

---

## Questão 6 (Verdadeiro/Falso)
Quanto mais índices, melhor a performance.

**Resposta:** Falso. Muitos índices podem piorar performance de INSERT/UPDATE porque cada índice precisa ser atualizado. Use índices apenas onde necessário.

---

## Questão 7 (Verdadeiro/Falso)
CREATE UNIQUE INDEX garante que valores sejam únicos.

**Resposta:** Verdadeiro. CREATE UNIQUE INDEX cria um índice único que garante que não haverá valores duplicados na coluna.