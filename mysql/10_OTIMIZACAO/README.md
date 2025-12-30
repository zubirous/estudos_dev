# 10. OTIMIZAÇÃO E PERFORMANCE

## EXPLAIN - Analisar Queries

```sql
-- Ver plano de execução
EXPLAIN SELECT * FROM usuarios WHERE email = 'joao@email.com';

-- Informações importantes:
-- - type: Tipo de acesso (ALL=pior, index=melhor)
-- - key: Índice usado
-- - rows: Linhas examinadas
-- - Extra: Informações adicionais
```

## Dicas de Otimização:

1. **Use índices** em colunas de WHERE, JOIN, ORDER BY
2. **Evite SELECT *** - selecione apenas colunas necessárias
3. **Use LIMIT** em consultas grandes
4. **Evite funções** em colunas de WHERE: `WHERE YEAR(data) = 2024` é lento
   - Melhor: `WHERE data >= '2024-01-01' AND data < '2025-01-01'`
5. **Normalize** o banco (evitar redundância)
6. **Use UNION** ao invés de múltiplas queries quando possível
