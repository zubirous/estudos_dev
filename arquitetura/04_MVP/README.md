# 4. MVP (Model-View-Presenter)

## Conceito
Similar ao MVC, mas o Presenter é mais ativo:

- **Model**: Dados
- **View**: Interface (passiva)
- **Presenter**: Toda a lógica de apresentação

## Fluxo:
```
Usuário → View → Presenter → Model → Presenter → View → Usuário
```

## MVC, MVP e MVVM: Relação entre eles

**Não são uma evolução sequencial!** São padrões diferentes para contextos diferentes:

- **MVC (1979)**: Base, coordenação manual
- **MVP (1990s)**: Evolução do MVC para melhorar testabilidade (View passiva)
- **MVVM (2005)**: Criado para frameworks com binding (WPF)

**MVP surgiu para resolver problemas do MVC:**
- ✅ View passiva (mais testável)
- ✅ Desacoplamento total View-Model
- ✅ Presenter controla tudo

**Mas MVP não é "melhor" que MVC** - depende do contexto:
- **MVC**: Simples, web tradicional
- **MVP**: Desktop, testes, controle total
- **MVVM**: Frameworks modernos com binding

## Comparação: MVP vs MVC vs MVVM

### Diferenças Principais:

| Aspecto | MVC | MVP | MVVM |
|---------|-----|-----|------|
| **Intermediário** | Controller | **Presenter** | ViewModel |
| **View** | Pode observar Model | **Passiva, não conhece Model** | Sincroniza via binding |
| **Atualização da View** | Controller coordena | **Presenter atualiza diretamente** | Binding automático |
| **Lógica de apresentação** | Pode estar na View | **Toda no Presenter** | No ViewModel |
| **Conhecimento** | Controller conhece View e Model | **Presenter conhece View e Model** | ViewModel não conhece View |
| **Fluxo** | Usuário → Controller → Model → Controller → View | **Usuário → View → Presenter → Model → Presenter → View** | Usuário ↔ View ↔ ViewModel ↔ Model |

### Características Únicas do MVP:

**MVP é diferente porque:**
- ✅ **View é completamente passiva** ("burra")
- ✅ **Presenter faz tudo**: processa, formata e atualiza View
- ✅ **View não conhece Model** (desacoplamento total)
- ✅ **Presenter conhece View e Model** (intermediário ativo)

**Comparado com MVC:**
- MVC: View pode observar Model, Controller coordena
- MVP: View não conhece Model, Presenter controla tudo

**Comparado com MVVM:**
- MVVM: Binding automático, ViewModel não conhece View
- MVP: Presenter conhece View e atualiza diretamente

### Quando usar cada um:

**Use MVC quando:**
- View pode ter alguma lógica simples
- Aplicações web tradicionais
- View pode observar mudanças no Model

**Use MVP quando:**
- Precisa de View completamente testável e passiva
- Aplicações desktop
- Quer desacoplamento total entre View e Model
- Presenter precisa controlar toda apresentação

**Use MVVM quando:**
- Framework suporta binding bidirecional (WPF, Angular, Vue.js)
- Precisa de sincronização automática entre View e dados
- Quer ViewModel testável sem conhecer View

## Responsabilidades:

### Model:
- Dados e lógica de negócio

### View:
- Interface do usuário (passiva)
- **NÃO conhece Model diretamente**
- **Apenas exibe dados** fornecidos pelo Presenter
- **NÃO contém lógica de negócio**
- **NÃO processa dados**

### Presenter:
- **Conhece View e Model** (intermediário)
- **Contém toda lógica de apresentação**
- **Processa e formata dados** para exibição
- **Atualiza View diretamente**

## Vantagens:
- ✅ View pode ser facilmente testada (é passiva)
- ✅ Presenter pode ser testado independentemente da View
- ✅ Separação clara de responsabilidades
- ✅ View não conhece Model (desacoplamento)
