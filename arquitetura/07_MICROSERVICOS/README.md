# 7. ARQUITETURA MICROSERVIÇOS

## Conceito
Sistema dividido em serviços pequenos e independentes, cada um executando em processo separado.

## Características:
- Cada serviço tem sua própria base de dados
- Comunicação via APIs (REST, gRPC, etc)
- Deploy independente
- Escalabilidade independente

## Estrutura:
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Serviço    │     │  Serviço    │     │  Serviço    │
│  Usuários   │     │  Pedidos    │     │  Produtos   │
│             │     │             │     │             │
│  DB Users   │     │  DB Orders  │     │  DB Products│
└─────────────┘     └─────────────┘     └─────────────┘
```

## Vantagens:
- ✅ Escalabilidade independente
- ✅ Tecnologias diferentes por serviço
- ✅ Deploy independente
- ✅ Falhas isoladas

## Desvantagens:
- ❌ Complexidade de comunicação
- ❌ Consistência distribuída é difícil
- ❌ Maior overhead operacional
