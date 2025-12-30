# Prova: MVP (Model-View-Presenter)

## Provas de Verdadeiro ou Falso

## Questão 1 (Verdadeiro/Falso)
No MVP, a View conhece o Model diretamente.

**Resposta:** Falso. No MVP, a View é passiva e não conhece o Model diretamente. O Presenter é o intermediário.

---

## Questão 2 (Verdadeiro/Falso)
No MVP, o Presenter atualiza a View diretamente.

**Resposta:** Verdadeiro. O Presenter é responsável por atualizar a View com dados do Model.

---

## Questão 3 (Verdadeiro/Falso)
No MVP, a View contém lógica de negócio.

**Resposta:** Falso. A View é "burra" e apenas exibe dados. A lógica fica no Presenter e Model.

---

## Questão 4 (Verdadeiro/Falso)
MVP é similar ao MVC, mas com Presenter ao invés de Controller.

**Resposta:** Verdadeiro. A principal diferença é que MVP usa Presenter que é mais ativo na atualização da View.

---

## Questão 5 (Verdadeiro/Falso)
No MVP, a View pode acessar diretamente o Model quando necessário.

**Resposta:** Falso. No MVP, a View nunca acessa o Model diretamente. Toda comunicação passa pelo Presenter.

---

## Questão 6 (Verdadeiro/Falso)
No MVP, o Presenter conhece tanto View quanto Model.

**Resposta:** Verdadeiro. O Presenter conhece View e Model, sendo o intermediário entre ambos.

---

## Questão 7 (Verdadeiro/Falso)
No MVP, a View é "burra" e apenas exibe dados.

**Resposta:** Verdadeiro. A View no MVP é passiva e apenas exibe dados que o Presenter fornece, sem lógica própria.

---

## Questão 8 (Verdadeiro/Falso)
MVP facilita testes porque View é passiva e Presenter pode ser testado isoladamente.

**Resposta:** Verdadeiro. Como View é passiva, pode ser facilmente mockada, e Presenter pode ser testado independentemente de View.

---

## Questão 9 (Verdadeiro/Falso)
No MVP, toda lógica de apresentação está no Presenter.

**Resposta:** Verdadeiro. No MVP, o Presenter contém toda lógica de apresentação, formatação de dados, e atualização da View.

