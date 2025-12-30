# 8. ARQUITETURA MONOLÍTICA

## Conceito
Aplicação construída como uma unidade única e indivisível.

## Características:
- Todo código em um único deploy
- Compartilha banco de dados
- Mais simples de desenvolver e testar

## Vantagens:
- ✅ Simplicidade de desenvolvimento
- ✅ Fácil debugging
- ✅ Transações ACID simples
- ✅ Menor latência (sem rede entre serviços)

## Desvantagens:
- ❌ Escalabilidade limitada
- ❌ Acoplamento forte
- ❌ Uma falha afeta todo sistema
- ❌ Deploy de todo sistema para pequenas mudanças

## Quando usar:
- Sistema pequeno/médio
- Equipe pequena
- Simplicidade é importante
