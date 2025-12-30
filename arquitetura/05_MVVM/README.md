# 5. MVVM (Model-View-ViewModel)

## Conceito
Usado principalmente em aplicações com binding de dados:

- **Model**: Dados
- **View**: Interface
- **ViewModel**: Estado e lógica de apresentação (bridge entre Model e View)

## Características:
- **ViewModel mantém estado da View**
- **Binding bidirecional** (View ↔ ViewModel)
- **ViewModel não conhece View diretamente** (binding através de data binding)
- **View nunca acessa Model diretamente** (sempre via ViewModel)

## MVC, MVP e MVVM: Evolução ou Alternativas?

**Não são uma evolução linear obrigatória!** São padrões diferentes para contextos diferentes:

### História:
- **MVC (1979)**: Base - coordenação manual
- **MVP (1990s)**: Evolução do MVC para melhorar testabilidade
- **MVVM (2005)**: Criado especificamente para WPF com binding automático

### Relação:
- **MVP evoluiu do MVC** para resolver problemas de teste (View passiva)
- **MVVM evoluiu do MVP** para aproveitar binding automático de frameworks modernos

**Mas não significa que MVVM é sempre melhor:**
- **MVC**: Ainda muito usado (web tradicional)
- **MVP**: Melhor quando não há binding (controle total)
- **MVVM**: Melhor quando framework suporta binding (menos código)

**Escolha baseada no seu contexto, não na "evolução"!**

## Comparação: MVVM vs MVC vs MVP

### Diferenças Principais:

| Aspecto | MVC | MVP | MVVM |
|---------|-----|-----|------|
| **Intermediário** | Controller | Presenter | ViewModel |
| **View** | Pode observar Model | Passiva, não conhece Model | Sincroniza via binding |
| **Atualização** | Controller coordena | Presenter atualiza diretamente | **Binding automático bidirecional** |
| **Estado da View** | Não mantém | Não mantém | **ViewModel mantém** |
| **Conhecimento** | Controller conhece View e Model | Presenter conhece View e Model | **ViewModel NÃO conhece View diretamente** |
| **Binding** | Não usa | Não usa | **Binding bidirecional (View ↔ ViewModel)** |
| **Fluxo** | Usuário → Controller → Model → Controller → View | Usuário → View → Presenter → Model → Presenter → View | **Usuário ↔ View ↔ ViewModel ↔ Model** |

### Características Únicas do MVVM:

**MVVM é diferente porque:**
- ✅ **Binding bidirecional automático** (View ↔ ViewModel)
- ✅ **ViewModel mantém estado da View** (não apenas dados)
- ✅ **ViewModel não conhece View diretamente** (binding através de data binding)
- ✅ **Sincronização automática** (mudanças se propagam automaticamente)

**Comparado com MVC:**
- MVC: Controller coordena manualmente
- MVVM: Binding automático, sem coordenação manual

**Comparado com MVP:**
- MVP: Presenter atualiza View diretamente (conhece View)
- MVVM: ViewModel não conhece View, binding faz a sincronização

## Por que usar MVVM ao invés de MVP?

### Vantagens do MVVM sobre MVP:

**1. Menos código manual:**
- **MVP**: Presenter precisa atualizar View manualmente (`view.setNome()`, `view.setEmail()`, etc.)
- **MVVM**: Binding automático - você apenas atualiza ViewModel, View atualiza sozinha

**2. Sincronização bidirecional automática:**
- **MVP**: Se usuário digita no campo, você precisa ler da View e atualizar Model manualmente
- **MVVM**: Usuário digita → ViewModel atualiza automaticamente → Model atualiza automaticamente

**3. ViewModel não conhece View:**
- **MVP**: Presenter conhece View (acoplamento)
- **MVVM**: ViewModel não conhece View (desacoplamento total)

**4. Menos código boilerplate:**
- **MVP**: Muito código repetitivo para atualizar View
- **MVVM**: Framework faz o trabalho pesado

**5. Melhor para formulários complexos:**
- **MVP**: Cada campo precisa ser atualizado manualmente
- **MVVM**: Formulários inteiros sincronizam automaticamente

### Quando MVVM é melhor que MVP:

**Use MVVM quando:**
- ✅ Framework suporta binding (WPF, Angular, Vue.js, React com hooks)
- ✅ Formulários com muitos campos (binding automático economiza código)
- ✅ Precisa de sincronização bidirecional frequente
- ✅ Quer menos código manual de atualização
- ✅ Aplicações modernas com data binding nativo

**Use MVP quando:**
- ✅ Framework não suporta binding (aplicações desktop antigas)
- ✅ Precisa de controle total sobre atualizações
- ✅ Aplicações simples sem muitos formulários
- ✅ Não há suporte a data binding no framework

## Responsabilidades:

### ViewModel:
- **Mantém e gerencia estado da View**
- **Serve como bridge entre Model e View**
- **Não conhece View diretamente** (binding através de mecanismos de data binding)
- Contém lógica de apresentação

### View:
- Interface do usuário
- **Nunca acessa Model diretamente** (sempre via ViewModel)
- Sincroniza automaticamente com ViewModel através de binding

## Binding Bidirecional:
- **View ↔ ViewModel** (ambas as direções)
- Mudanças na View atualizam ViewModel automaticamente
- Mudanças no ViewModel atualizam View automaticamente

## Quando usar MVVM:
- Framework suporta **binding de dados bidirecional** (WPF, Angular, Vue.js)
- Formulários complexos com muitos campos
- Precisa de sincronização automática entre View e dados
- Quer reduzir código manual de atualização
- Aplicações modernas com suporte nativo a data binding

## Vantagens:
- ✅ ViewModel pode ser testado independentemente da View
- ✅ Desacoplamento entre View e Model
- ✅ Sincronização automática através de binding
- ✅ Ideal para frameworks com suporte a data binding
