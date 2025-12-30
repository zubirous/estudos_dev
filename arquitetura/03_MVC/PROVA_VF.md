# Prova: MVC (Model-View-Controller)

## Provas de Verdadeiro ou Falso

## Questão 1 (Verdadeiro/Falso)
No padrão MVC, a View pode acessar diretamente o Model.

**Resposta:** Falso. No MVC clássico, a View nunca acessa o Model diretamente. O Controller é o intermediário.

---

## Questão 2 (Verdadeiro/Falso)
No MVC, o Model pode conter lógica de apresentação.

**Resposta:** Falso. O Model contém apenas lógica de negócio e acesso a dados, nunca lógica de apresentação.

---

## Questão 3 (Verdadeiro/Falso)
No MVC, o Controller coordena Model e View.

**Resposta:** Verdadeiro. O Controller recebe input do usuário, interage com o Model, e atualiza a View.

---

## Questão 4 (Verdadeiro/Falso)
No MVC, o View pode conter lógica de negócio.

**Resposta:** Falso. O View apenas exibe dados, não deve conter lógica de negócio.

---

## Questão 5 (Verdadeiro/Falso)
No MVC, o Model não conhece o View nem o Controller.

**Resposta:** Verdadeiro. O Model é independente e não conhece View nem Controller.

---

## Questão 6 (Verdadeiro/Falso)
MVC facilita manutenção através de separação de responsabilidades.

**Resposta:** Verdadeiro. MVC separa responsabilidades claramente, facilitando manutenção e evolução do código.

---

## Questão 7 (Verdadeiro/Falso)
No MVC, o Controller pode acessar tanto Model quanto View.

**Resposta:** Verdadeiro. O Controller conhece e coordena tanto Model quanto View.

---

## Questão 8 (Verdadeiro/Falso)
O problema "Fat Controller" acontece quando o Controller tem muita lógica de negócio.

**Resposta:** Verdadeiro. Fat Controller ocorre quando lógica de negócio fica no Controller ao invés de estar no Model ou Services.