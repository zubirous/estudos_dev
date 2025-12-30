# 7. VIEWS (Visões)

## Criar View

```sql
-- Criar view
CREATE VIEW usuarios_ativos AS
SELECT id, nome, email
FROM usuarios
WHERE ativo = TRUE;

-- Usar view
SELECT * FROM usuarios_ativos;

-- Atualizar view
CREATE OR REPLACE VIEW usuarios_ativos AS
SELECT id, nome, email, idade
FROM usuarios
WHERE ativo = TRUE;

-- Deletar view
DROP VIEW usuarios_ativos;
```

**Views** são consultas SQL armazenadas como se fossem tabelas. Úteis para simplificar consultas complexas e reutilizar lógica.
