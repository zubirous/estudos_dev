# 2. ARQUITETURA EM CAMADAS (Layered Architecture)

## Conceito
Divide o sistema em camadas horizontais, cada uma com responsabilidade específica.

## Camadas Típicas:

```
┌─────────────────┐
│   Apresentação  │ ← UI, API endpoints
├─────────────────┤
│    Negócio      │ ← Regras de negócio
├─────────────────┤
│  Acesso Dados   │ ← Banco de dados
└─────────────────┘
```

### Exemplo em Python:

```python
# Camada de Acesso a Dados
class UsuarioRepository:
    def buscar_por_id(self, id):
        return {"id": id, "nome": "João"}

# Camada de Negócio
class UsuarioService:
    def __init__(self):
        self.repository = UsuarioRepository()
    
    def obter_usuario(self, id):
        usuario = self.repository.buscar_por_id(id)
        if not usuario:
            raise ValueError("Usuário não encontrado")
        return usuario

# Camada de Apresentação (API)
class UsuarioController:
    def __init__(self):
        self.service = UsuarioService()
    
    def get_usuario(self, id):
        try:
            usuario = self.service.obter_usuario(id)
            return {"status": 200, "data": usuario}
        except ValueError as e:
            return {"status": 404, "error": str(e)}
```

## Responsabilidades das Camadas:

### Camada de Apresentação:
- Interface do usuário (UI)
- API endpoints
- Recebe e valida entrada do usuário
- Formata dados para exibição

### Camada de Negócio:
- Regras de negócio
- Validação de dados
- Lógica de processamento
- Coordenação entre camadas

### Camada de Acesso a Dados:
- Persistência de dados
- Consultas ao banco de dados
- Abstração do banco de dados
- Operações CRUD

## Vantagens:
- ✅ Separação clara de responsabilidades
- ✅ Fácil manutenção e teste
- ✅ Independência entre camadas
- ✅ Permite reutilização de código
- ✅ Facilita substituição de camadas (ex: trocar banco de dados)

## Desvantagens:
- ❌ Pode adicionar latência por camadas
- ❌ Pode ser complexo para aplicações simples
- ❌ Pode dificultar otimizações cross-layer
- ❌ Pode gerar overhead de comunicação entre camadas
