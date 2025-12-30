# Prova: ENVIRONMENT VARIABLES - Next.js

## Provas de Alternativas

## Questão 1 (Múltipla Escolha)
Como expor uma variável de ambiente ao cliente no Next.js?

a) Colocar no .env
b) Adicionar prefixo NEXT_PUBLIC_
c) Não é possível
d) Sempre está exposta

**Resposta:** b) Adicionar prefixo NEXT_PUBLIC_

---

## Questão 2 (Múltipla Escolha)
Variáveis sem NEXT_PUBLIC_ são acessíveis:

a) Apenas no cliente
b) Apenas no servidor
c) No cliente e servidor
d) Não são acessíveis

**Resposta:** b) Apenas no servidor

---

## Questão 3 (Múltipla Escolha)
Variáveis com NEXT_PUBLIC_ são acessíveis:

a) Apenas no cliente
b) Apenas no servidor
c) No cliente e servidor
d) Não são acessíveis

**Resposta:** c) No cliente e servidor

---

## Questão 4 (Múltipla Escolha)
Qual arquivo de variáveis de ambiente é usado para desenvolvimento local?

a) .env.production
b) .env.local
c) .env.public
d) .env.client

**Resposta:** b) .env.local - usado para desenvolvimento local

---

## Questão 5 (Múltipla Escolha)
Por que não devemos expor chaves secretas ao cliente?

a) Não há problema
b) Código JavaScript no cliente é visível e chaves podem ser roubadas
c) Cliente não pode ver código
d) Chaves não são importantes

**Resposta:** b) Código JavaScript no cliente é visível e chaves podem ser roubadas

---

## Questão 6 (Múltipla Escolha)
Como acessar variáveis de ambiente no código Next.js?

a) env.VARIAVEL
b) process.env.VARIAVEL
c) config.env.VARIAVEL
d) getEnv('VARIAVEL')

**Resposta:** b) process.env.VARIAVEL

---

## Questão 7 (Múltipla Escolha)
Qual arquivo de variáveis de ambiente é usado para produção?

a) .env.local
b) .env.production
c) .env.development
d) .env

**Resposta:** b) .env.production - usado para produção

---

## Questão 8 (Múltipla Escolha)
Onde variáveis privadas (sem NEXT_PUBLIC_) podem ser usadas?

a) Apenas em componentes do cliente
b) Apenas no servidor (getServerSideProps, API routes)
c) Em qualquer lugar
d) Não podem ser usadas

**Resposta:** b) Apenas no servidor (getServerSideProps, API routes, etc)

---

## Questão 9 (Múltipla Escolha)
Qual prefixo é necessário para expor variáveis ao cliente?

a) PUBLIC_
b) NEXT_PUBLIC_
c) CLIENT_
d) EXPOSE_

**Resposta:** b) NEXT_PUBLIC_ - prefixo necessário para expor variáveis ao cliente

---

## Questão 10 (Múltipla Escolha)
Variáveis de ambiente são úteis para:

a) Apenas chaves secretas
b) Configurações que variam entre ambientes (desenvolvimento, produção)
c) Apenas URLs
d) Nada

**Resposta:** b) Configurações que variam entre ambientes (desenvolvimento, produção)