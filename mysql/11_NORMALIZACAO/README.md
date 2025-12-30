# 11. NORMALIZAÇÃO (Formas Normais)

## 1FN (Primeira Forma Normal)
- Cada coluna deve ter apenas um valor atômico
- Sem repetição de grupos de colunas

## 2FN (Segunda Forma Normal)
- Deve estar em 1FN
- Todos atributos não-chave dependem totalmente da chave primária

## 3FN (Terceira Forma Normal)
- Deve estar em 2FN
- Não há dependência transitiva (A → B → C, onde A não depende diretamente de C)

**Exemplo:**
```
❌ Antes (não normalizado):
pedidos(id, cliente, cidade_cliente, produto, preco)

✅ Depois (normalizado):
clientes(id, nome, cidade_id)
cidades(id, nome)
pedidos(id, cliente_id, produto_id)
produtos(id, nome, preco)
```
