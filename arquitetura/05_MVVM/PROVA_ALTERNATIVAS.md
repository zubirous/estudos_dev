# Prova: MVVM (Model-View-ViewModel)

## Provas de Alternativas

## Questão 1 (Múltipla Escolha)
Qual característica é típica do MVVM?

a) View conhece Model diretamente
b) Binding bidirecional entre View e ViewModel
c) Controller coordena tudo
d) Presenter atualiza View

**Resposta:** b) Binding bidirecional entre View e ViewModel

---

## Questão 2 (Múltipla Escolha)
Qual é a principal diferença entre MVC, MVP e MVVM?

a) MVC tem binding bidirecional, MVP tem View passiva, MVVM tem Controller
b) MVC tem Controller, MVP tem View passiva, MVVM tem binding bidirecional
c) Não há diferenças
d) São a mesma coisa

**Resposta:** b) MVC tem Controller, MVP tem View passiva, MVVM tem binding bidirecional

---

## Questão 3 (Múltipla Escolha)
No MVVM, o ViewModel:

a) Conhece a View diretamente
b) Não conhece a View diretamente (binding através de data binding)
c) É o mesmo que Controller
d) Não existe

**Resposta:** b) Não conhece a View diretamente (binding através de mecanismos de data binding)

---

## Questão 4 (Múltipla Escolha)
MVVM é especialmente útil para:

a) Aplicações sem binding de dados
b) Aplicações com binding de dados bidirecional
c) Aplicações apenas desktop
d) Aplicações apenas web

**Resposta:** b) Aplicações com binding de dados bidirecional

---

## Questão 5 (Múltipla Escolha)
No MVVM, quem mantém o estado da View?

a) View diretamente
b) ViewModel
c) Model
d) Controller

**Resposta:** b) ViewModel - ViewModel mantém e gerencia estado da View

---

## Questão 6 (Múltipla Escolha)
Binding bidirecional no MVVM significa:

a) View → ViewModel apenas
b) ViewModel → View apenas
c) View ↔ ViewModel (ambas as direções)
d) Não há binding

**Resposta:** c) View ↔ ViewModel (ambas as direções) - mudanças em ambos se sincronizam automaticamente

---

## Questão 7 (Múltipla Escolha)
No MVVM, a View:

a) Acessa Model diretamente
b) Nunca acessa Model diretamente (sempre via ViewModel)
c) É a mesma que Controller
d) Não existe

**Resposta:** b) Nunca acessa Model diretamente - toda comunicação passa pelo ViewModel

---

## Questão 8 (Múltipla Escolha)
Qual padrão é melhor para aplicações WPF, Angular ou Vue.js?

a) MVC
b) MVP
c) MVVM
d) Todos são iguais

**Resposta:** c) MVVM - esses frameworks suportam data binding bidirecional, ideal para MVVM

---

## Questão 9 (Múltipla Escolha)
Uma vantagem do MVVM é:

a) ViewModel pode ser testado independentemente da View
b) View conhece ViewModel diretamente
c) Não há separação de responsabilidades
d) View acessa Model diretamente

**Resposta:** a) ViewModel pode ser testado independentemente da View - desacoplamento permite testes isolados

---

## Questão 10 (Múltipla Escolha)
No MVVM, o ViewModel serve como:

a) Apenas estado
b) Bridge entre Model e View
c) Apenas lógica de negócio
d) Apenas apresentação

**Resposta:** b) Bridge entre Model e View - ViewModel conecta Model e View através de binding