# Prova: RENDERIZAÇÃO - Next.js

## Provas de Alternativas

## Questão 1 (Múltipla Escolha)
Qual função executa no servidor a cada requisição?

a) getStaticProps
b) getServerSideProps
c) getInitialProps
d) useEffect

**Resposta:** b) getServerSideProps

---

## Questão 2 (Múltipla Escolha)
Qual a diferença entre SSR e SSG?

a) SSR executa no build, SSG a cada requisição
b) SSR executa a cada requisição, SSG no build
c) Não há diferença
d) SSR é mais rápido

**Resposta:** b) SSR executa a cada requisição, SSG no build

---

## Questão 3 (Múltipla Escolha)
Qual método de renderização é melhor para páginas que mudam frequentemente?

a) SSG
b) SSR
c) ISR
d) CSR

**Resposta:** b) SSR, pois gera conteúdo a cada requisição

---

## Questão 4 (Múltipla Escolha)
Qual função do Next.js permite regenerar páginas estáticas sem rebuild?

a) getStaticProps
b) getServerSideProps
c) getStaticPaths
d) revalidate

**Resposta:** d) revalidate - usado no ISR para regenerar páginas

---

## Questão 5 (Múltipla Escolha)
Qual método de renderização é melhor para um blog?

a) SSR
b) SSG
c) ISR
d) CSR

**Resposta:** b) SSG ou c) ISR - blog geralmente tem conteúdo estático, SSG ou ISR são ideais

---

## Questão 6 (Múltipla Escolha)
Qual método de renderização é melhor para um dashboard com dados em tempo real?

a) SSG
b) SSR
c) ISR
d) CSR

**Resposta:** b) SSR - dashboard precisa de dados atualizados a cada requisição

---

## Questão 7 (Múltipla Escolha)
ISR (Incremental Static Regeneration) combina:

a) SSR e CSR
b) SSG e atualização periódica
c) Apenas SSR
d) Apenas SSG

**Resposta:** b) SSG e atualização periódica - páginas estáticas que revalidam em background

---

## Questão 8 (Múltipla Escolha)
getStaticProps executa:

a) A cada requisição
b) No build time
c) No cliente
d) Continuamente

**Resposta:** b) No build time - executa apenas durante o build para gerar páginas estáticas

---

## Questão 9 (Múltipla Escolha)
getServerSideProps executa:

a) No build time
b) A cada requisição
c) No cliente
d) Uma vez apenas

**Resposta:** b) A cada requisição - executa no servidor a cada requisição para dados dinâmicos

---

## Questão 10 (Múltipla Escolha)
Para rotas dinâmicas com SSG, é necessário usar:

a) getStaticProps apenas
b) getStaticProps e getStaticPaths
c) getServerSideProps apenas
d) Nenhum

**Resposta:** b) getStaticProps e getStaticPaths - getStaticPaths define quais rotas gerar, getStaticProps gera dados

---

## Questão 11 (Múltipla Escolha)
Qual é mais rápido: SSG, SSR ou ISR?

a) SSG (estático no build)
b) SSR (processa a cada requisição)
c) ISR (estático com revalidação)
d) SSR e ISR são iguais

**Resposta:** a) SSG - páginas estáticas pré-renderizadas são mais rápidas que processamento dinâmico