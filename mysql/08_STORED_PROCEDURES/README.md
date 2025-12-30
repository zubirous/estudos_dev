# 8. STORED PROCEDURES (Procedimentos Armazenados)

## Criar Procedure

```sql
-- Criar procedure
DELIMITER //
CREATE PROCEDURE obter_usuarios_por_idade(IN idade_min INT, IN idade_max INT)
BEGIN
    SELECT * FROM usuarios
    WHERE idade BETWEEN idade_min AND idade_max;
END //
DELIMITER ;

-- Chamar procedure
CALL obter_usuarios_por_idade(18, 65);

-- Deletar procedure
DROP PROCEDURE obter_usuarios_por_idade;
```

**Stored Procedures** são funções armazenadas no banco de dados que podem receber parâmetros e executar lógica SQL complexa.
