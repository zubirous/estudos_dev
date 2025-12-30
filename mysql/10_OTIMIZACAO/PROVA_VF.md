# Prova: OTIMIZAÇÃO - MySQL

## Provas de Verdadeiro ou Falso

## Questão 1 (Verdadeiro/Falso)
EXPLAIN mostra o plano de execução de uma query.

**Resposta:** Verdadeiro. EXPLAIN analisa e mostra como o MySQL executa a query.

---

## Questão 2 (Verdadeiro/Falso)
Usar funções em colunas de WHERE melhora performance.

**Resposta:** Falso. Funções em colunas de WHERE impedem uso de índices, tornando queries mais lentas.

---

## Questão 3 (Verdadeiro/Falso)
SELECT * é sempre mais rápido que selecionar colunas específicas.

**Resposta:** Falso. SELECT * retorna todas as colunas, aumentando uso de memória e rede. Selecione apenas colunas necessárias.

---

## Questão 4 (Verdadeiro/Falso)
Índices devem ser usados em colunas de WHERE, JOIN e ORDER BY.

**Resposta:** Verdadeiro. Índices aceleram essas operações.

---

## Questão 5 (Verdadeiro/Falso)
Normalização sempre melhora performance de consultas.

**Resposta:** Falso. Normalização pode piorar performance em algumas consultas porque requer mais JOINs, mas melhora integridade e reduz redundância.

---

## Questão 6 (Verdadeiro/Falso)
LIMIT pode melhorar performance de queries grandes.

**Resposta:** Verdadeiro. LIMIT limita quantidade de resultados, reduzindo processamento e uso de memória.

