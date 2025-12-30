# Prova: CSS E ESTILOS - Next.js

## Provas de Alternativas

## Questão 1 (Múltipla Escolha)
Onde importar CSS global no Next.js?

a) Em qualquer componente
b) No _app.js
c) No index.js
d) Não pode importar CSS global

**Resposta:** b) No _app.js

---

## Questão 2 (Múltipla Escolha)
Como usar CSS Modules no Next.js?

a) Criar arquivo .css e importar
b) Criar arquivo .module.css e importar como objeto
c) Não é possível
d) Usar apenas Styled JSX

**Resposta:** b) Criar arquivo .module.css e importar como objeto

---

## Questão 3 (Múltipla Escolha)
Qual é a vantagem de CSS Modules?

a) Estilos globais
b) Estilos escopados por componente (não vazam)
c) Mais rápido
d) Não tem vantagem

**Resposta:** b) Estilos escopados por componente (não vazam) - CSS Modules geram nomes únicos

---

## Questão 4 (Múltipla Escolha)
O que é Styled JSX no Next.js?

a) Biblioteca externa
b) CSS built-in que permite escrever CSS dentro de componentes
c) CSS Modules
d) Não existe

**Resposta:** b) CSS built-in que permite escrever CSS dentro de componentes

---

## Questão 5 (Múltipla Escolha)
Como usar CSS Modules em um componente?

a) import styles from './styles.css'
b) import styles from './styles.module.css'
c) import './styles.css'
d) Não é possível

**Resposta:** b) import styles from './styles.module.css' - importa como objeto

---

## Questão 6 (Múltipla Escolha)
Como aplicar classes CSS Modules em um componente?

a) className="container"
b) className={styles.container}
c) class="container"
d) style="container"

**Resposta:** b) className={styles.container} - usa objeto styles importado

---

## Questão 7 (Múltipla Escolha)
Styled JSX usa qual sintaxe?

a) <style>...</style>
b) <style jsx>...</style>
c) <css>...</css>
d) <styled>...</styled>

**Resposta:** b) <style jsx>...</style> - tag style com atributo jsx

---

## Questão 8 (Múltipla Escolha)
CSS global no Next.js é aplicado:

a) Apenas na página atual
b) Em todas as páginas da aplicação
c) Apenas no componente atual
d) Nunca é aplicado

**Resposta:** b) Em todas as páginas da aplicação - CSS global importado no _app.js é aplicado globalmente

---

## Questão 9 (Múltipla Escolha)
Qual é a diferença entre CSS Modules e CSS global?

a) Não há diferença
b) CSS Modules são escopados, CSS global é aplicado em toda aplicação
c) CSS global é mais rápido
d) CSS Modules não funcionam

**Resposta:** b) CSS Modules são escopados por componente, CSS global é aplicado em toda aplicação

---

## Questão 10 (Múltipla Escolha)
No Next.js, você pode usar:

a) Apenas CSS Modules
b) Apenas Styled JSX
c) CSS Modules, Styled JSX e CSS global juntos
d) Apenas CSS global

**Resposta:** c) CSS Modules, Styled JSX e CSS global juntos - Next.js suporta todas as formas