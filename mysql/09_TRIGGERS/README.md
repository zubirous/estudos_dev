# 9. TRIGGERS (Gatilhos)

## Trigger BEFORE INSERT

```sql
DELIMITER //
CREATE TRIGGER before_usuario_insert
BEFORE INSERT ON usuarios
FOR EACH ROW
BEGIN
    IF NEW.idade < 0 THEN
        SET NEW.idade = 0;
    END IF;
END //
DELIMITER ;
```

## Trigger AFTER UPDATE

```sql
DELIMITER //
CREATE TRIGGER after_pedido_update
AFTER UPDATE ON pedidos
FOR EACH ROW
BEGIN
    IF NEW.valor != OLD.valor THEN
        INSERT INTO auditoria (tabela, acao, registro_id)
        VALUES ('pedidos', 'UPDATE', NEW.id);
    END IF;
END //
DELIMITER ;
```

**Triggers** são procedimentos automáticos que executam antes ou depois de operações INSERT, UPDATE ou DELETE.
