# 6. ARQUITETURA EM CAMADAS (3-Tier / N-Tier)

## 3-Tier (Três Camadas)

1. **Apresentação (Presentation Layer)**: Interface do usuário
2. **Lógica de Negócio (Business Logic Layer)**: Regras do negócio
3. **Acesso a Dados (Data Access Layer)**: Persistência

## Regra Fundamental:
**Cada camada só conhece a camada abaixo dela** (hierarquia de comunicação)

## Responsabilidades das Camadas:

### Camada de Apresentação:
- Interface do usuário (UI)
- API endpoints
- Recebe e valida entrada do usuário
- Formata dados para exibição

### Camada de Negócio (Business Logic Layer):
- **Regras de negócio**
- **Validações**
- Lógica de processamento
- Coordenação entre camadas

### Camada de Acesso a Dados:
- **Persistência** (banco de dados)
- Consultas ao banco
- Abstração do banco de dados
- Operações CRUD

## Vantagens:
- ✅ Separação clara de responsabilidades
- ✅ Fácil substituição de camadas (ex: trocar banco de dados)
- ✅ Facilita manutenção
- ✅ **Cada camada pode ser trocada independentemente**
- ✅ **Permite escalar camadas independentemente**

## Também conhecida como:
- **Arquitetura em camadas (Layered Architecture)**
