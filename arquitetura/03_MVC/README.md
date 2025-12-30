# 3. MVC (Model-View-Controller)

## Conceito
Separa a aplicação em três componentes:

- **Model**: Dados e lógica de negócio
- **View**: Interface do usuário
- **Controller**: Intermediário entre Model e View

## Fluxo:
```
Usuário → Controller → Model → Controller → View → Usuário
```

## Componentes e Responsabilidades:

### Model (Modelo)
- **Responsabilidades:**
  - Dados e lógica de negócio
  - Acesso a dados (banco de dados)
  - Validação de regras de negócio
  - **NÃO conhece View nem Controller** (é independente)
  - **NÃO contém lógica de apresentação**

### View (Visão)
- **Responsabilidades:**
  - Interface do usuário (apresentação)
  - Exibe dados ao usuário
  - **NÃO deve acessar Model diretamente** (no MVC clássico)
  - **NÃO contém lógica de negócio**
  - Apenas exibe dados fornecidos pelo Controller

### Controller (Controlador)
- **Responsabilidades:**
  - **Recebe input do usuário**
  - Coordena Model e View
  - Processa requisições
  - Decide qual ação tomar
  - **Pode acessar tanto Model quanto View**
  - **NÃO deve conter lógica de negócio** (deve delegar ao Model)

## Exemplo em Python:

```python
# Model (dados e lógica de negócio)
class UsuarioModel:
    def buscar_todos(self):
        return [{"id": 1, "nome": "João"}, {"id": 2, "nome": "Maria"}]
    
    def buscar_por_id(self, id):
        # Busca no banco
        return {"id": id, "nome": "João"}

# View (apresentação)
class UsuarioView:
    def exibir_usuarios(self, usuarios):
        for u in usuarios:
            print(f"{u['id']}: {u['nome']}")

# Controller (coordena Model e View)
class UsuarioController:
    def __init__(self):
        self.model = UsuarioModel()
        self.view = UsuarioView()
    
    def listar_usuarios(self):
        usuarios = self.model.buscar_todos()
        self.view.exibir_usuarios(usuarios)
```

## MVC, MVP e MVVM: São Evoluções?

**Não são uma evolução linear!** São padrões diferentes criados para contextos diferentes:

- **MVC (1979)**: Criado para aplicações desktop (Smalltalk)
- **MVP (1990s)**: Criado para resolver problemas de teste no MVC (aplicações desktop)
- **MVVM (2005)**: Criado para WPF (Windows) com binding automático

**Não é que MVVM é "melhor" que MVP ou MVC** - cada um resolve problemas diferentes:
- **MVC**: Simples, coordenação manual
- **MVP**: View testável, desacoplamento
- **MVVM**: Binding automático quando framework suporta

**Escolha baseada no contexto, não na "evolução"!**

## Comparação: MVC vs MVP vs MVVM

### Diferenças Principais:

| Aspecto | **MVC** | MVP | MVVM |
|---------|---------|-----|------|
| **Intermediário** | **Controller** | Presenter | ViewModel |
| **View** | **Pode observar Model** (em algumas variações) | Passiva, não conhece Model | Sincroniza via binding |
| **Atualização** | **Controller coordena** | Presenter atualiza diretamente | Binding automático |
| **Lógica de apresentação** | **Pode estar na View** | Toda no Presenter | No ViewModel |
| **Conhecimento** | **Controller conhece View e Model** | Presenter conhece View e Model | ViewModel não conhece View |
| **Binding** | Não usa | Não usa | Binding bidirecional |
| **Fluxo** | **Usuário → Controller → Model → Controller → View** | Usuário → View → Presenter → Model → Presenter → View | Usuário ↔ View ↔ ViewModel ↔ Model |

### Características Únicas do MVC:

**MVC é diferente porque:**
- ✅ **Controller coordena** Model e View
- ✅ **View pode observar Model** (em algumas implementações)
- ✅ **Controller recebe input do usuário** diretamente
- ✅ Mais comum em aplicações web tradicionais

**Comparado com MVP:**
- MVP: View é passiva, Presenter controla tudo
- MVC: View pode ter alguma lógica, Controller coordena

**Comparado com MVVM:**
- MVVM: Binding automático, ViewModel mantém estado
- MVC: Coordenação manual, sem binding automático

### Quando usar cada um:

**Use MVC quando:**
- View pode ter alguma lógica simples
- Aplicações web tradicionais
- View pode observar mudanças no Model
- Precisa de coordenação simples entre componentes

**Use MVP quando:**
- Precisa de View completamente testável e passiva
- Aplicações desktop
- Quer desacoplamento total entre View e Model

**Use MVVM quando:**
- Framework suporta binding bidirecional (WPF, Angular, Vue.js)
- Precisa de sincronização automática entre View e dados

## Regras Importantes:

### ❌ O que NÃO fazer:
- **View acessar Model diretamente** (no MVC clássico)
- **Model conter lógica de apresentação**
- **View conter lógica de negócio**
- **Controller conter lógica de negócio** (deve estar no Model)

### ✅ O que fazer:
- Controller recebe input e coordena tudo
- Model é independente (não conhece View/Controller)
- View apenas exibe dados
- Lógica de negócio fica no Model

## Problemas Comuns:

### Fat Controller (Controller Gordo)
**Problema:** Controller fica com muita lógica de negócio.

**Solução:** Mover lógica de negócio para o Model ou criar Services.

**Exemplo de problema:**
```python
# ❌ ERRADO: Lógica de negócio no Controller
class UsuarioController:
    def criar_usuario(self, nome, email):
        # Validação no Controller (ERRADO!)
        if len(nome) < 3:
            return "Nome muito curto"
        if "@" not in email:
            return "Email inválido"
        # Lógica de negócio no Controller (ERRADO!)
        usuario = {"nome": nome, "email": email}
        # ...
```

**Exemplo correto:**
```python
# ✅ CORRETO: Lógica no Model
class UsuarioModel:
    def validar_usuario(self, nome, email):
        if len(nome) < 3:
            raise ValueError("Nome muito curto")
        if "@" not in email:
            raise ValueError("Email inválido")
    
    def criar_usuario(self, nome, email):
        self.validar_usuario(nome, email)
        # Criar usuário...

# Controller apenas coordena
class UsuarioController:
    def criar_usuario(self, nome, email):
        try:
            usuario = self.model.criar_usuario(nome, email)
            self.view.exibir_sucesso(usuario)
        except ValueError as e:
            self.view.exibir_erro(str(e))
```

## Vantagens:
- ✅ Separação clara de responsabilidades
- ✅ Fácil manutenção
- ✅ Reutilização de Models e Views
- ✅ Testes mais fáceis (cada componente testado isoladamente)
- ✅ Model independente (pode ser usado em diferentes Views)
