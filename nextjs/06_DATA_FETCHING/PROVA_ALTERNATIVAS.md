# Prova: DATA FETCHING - Next.js

## Provas de Alternativas

## Questão 1 (Múltipla Escolha)
Quando usar getStaticProps?

a) Dados que mudam constantemente
b) Dashboard do usuário
c) Conteúdo estático (blog, documentação)
d) Dados que precisam de autenticação

**Resposta:** c) Conteúdo estático (blog, documentação)

---

## Questão 2 (Múltipla Escolha)
Quando usar getServerSideProps?

a) Conteúdo estático
b) Dados dinâmicos ou personalizados por usuário
c) Nunca usar
d) Apenas em produção

**Resposta:** b) Dados dinâmicos ou personalizados por usuário

---

## Questão 3 (Múltipla Escolha)
Quando getStaticProps executa?

a) A cada requisição
b) No build time
c) No cliente
d) Nunca executa

**Resposta:** b) No build time - executa apenas durante o build

---

## Questão 4 (Múltipla Escolha)
Quando getServerSideProps executa?

a) No build time
b) A cada requisição
c) No cliente
d) Uma vez apenas

**Resposta:** b) A cada requisição - executa no servidor a cada requisição

---

## Questão 5 (Múltipla Escolha)
Para que serve ISR (Incremental Static Regeneration)?

a) Gerar páginas apenas no build
b) Gerar páginas no build e revalidar periodicamente
c) Gerar páginas apenas no servidor
d) Gerar páginas apenas no cliente

**Resposta:** b) Gerar páginas no build e revalidar periodicamente - combina SSG com atualização

---

## Questão 6 (Múltipla Escolha)
Quando usar useEffect para data fetching?

a) Dados que afetam SEO
b) Dados que não afetam SEO
c) Dados estáticos
d) Dados que mudam constantemente

**Resposta:** b) Dados que não afetam SEO - useEffect executa no cliente após renderização

---

## Questão 7 (Múltipla Escolha)
Qual método de data fetching executa no servidor durante o build?

a) getServerSideProps
b) getStaticProps
c) useEffect
d) useState

**Resposta:** b) getStaticProps - executa no servidor durante o build

---

## Questão 8 (Múltipla Escolha)
Qual método de data fetching executa no servidor a cada requisição?

a) getStaticProps
b) getServerSideProps
c) useEffect
d) useState

**Resposta:** b) getServerSideProps - executa no servidor a cada requisição

---

## Questão 9 (Múltipla Escolha)
Para dados que mudam ocasionalmente (ex: catálogo de produtos), use:

a) getStaticProps com revalidate (ISR)
b) getServerSideProps
c) useEffect
d) useState

**Resposta:** a) getStaticProps com revalidate (ISR) - combina velocidade de SSG com atualização periódica

---

## Questão 10 (Múltipla Escolha)
Qual método é melhor para SEO?

a) useEffect (executa no cliente)
b) getStaticProps ou getServerSideProps (executam no servidor)
c) useState
d) Todos são iguais

**Resposta:** b) getStaticProps ou getServerSideProps - executam no servidor, conteúdo disponível para crawlers de busca