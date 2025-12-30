# 9. ARQUITETURA CLIENTE-SERVIDOR

## Conceito
Cliente faz requisições, servidor processa e retorna respostas.

## Tipos:
- **2-Tier**: Cliente ↔ Servidor
- **3-Tier**: Cliente ↔ Servidor de Aplicação ↔ Servidor de Banco de Dados

## Fluxo:
```
Cliente → Requisição → Servidor → Processa → Resposta → Cliente
```

## Exemplo:
```python
# Cliente (simulado)
class Cliente:
    def fazer_requisicao(self, url, dados):
        return {"status": "ok", "data": "resposta"}

# Servidor (simulado)
class Servidor:
    def processar_requisicao(self, dados):
        return {"resultado": f"Processado: {dados}"}
```
