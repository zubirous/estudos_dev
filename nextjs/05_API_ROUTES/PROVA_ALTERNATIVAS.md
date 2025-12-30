# Prova: API ROUTES - Next.js

## Provas de Alternativas

## Questão 1 (Múltipla Escolha)
Onde ficam as API Routes no Next.js?

a) src/api
b) pages/api
c) components/api
d) public/api

**Resposta:** b) pages/api

---

## Questão 2 (Múltipla Escolha)
Qual endpoint corresponde ao arquivo pages/api/users.js?

a) /users
b) /api/users
c) /api/users.js
d) /pages/api/users

**Resposta:** b) /api/users - arquivos em pages/api/ geram endpoints em /api/

---

## Questão 3 (Múltipla Escolha)
O que o handler de uma API Route recebe?

a) req e res (similar a Express.js)
b) request e response
c) context
d) params apenas

**Resposta:** a) req e res (similar a Express.js)

---

## Questão 4 (Múltipla Escolha)
Como criar uma rota dinâmica de API?

a) pages/api/user/[id].js
b) pages/api/user/(id).js
c) pages/api/user/{id}.js
d) pages/api/user/:id.js

**Resposta:** a) pages/api/user/[id].js - usa colchetes para rotas dinâmicas

---

## Questão 5 (Múltipla Escolha)
API Routes no Next.js são executadas:

a) Apenas no cliente
b) Apenas no servidor
c) No cliente e servidor
d) Nunca executam

**Resposta:** b) Apenas no servidor - API Routes são executadas no servidor Node.js

---

## Questão 6 (Múltipla Escolha)
API Routes podem processar quais métodos HTTP?

a) Apenas GET
b) GET, POST, PUT, DELETE e outros
c) Apenas POST
d) Apenas GET e POST

**Resposta:** b) GET, POST, PUT, DELETE e outros - todos os métodos HTTP

---

## Questão 7 (Múltipla Escolha)
Como acessar parâmetros de rota dinâmica em uma API Route?

a) req.params
b) req.query
c) req.body
d) req.params ou req.query

**Resposta:** d) req.params ou req.query - dependendo da configuração da rota

---

## Questão 8 (Múltipla Escolha)
API Routes são úteis para:

a) Apenas criar APIs externas
b) Criar endpoints de API dentro do projeto Next.js
c) Apenas criar páginas
d) Não são úteis

**Resposta:** b) Criar endpoints de API dentro do projeto Next.js

---

## Questão 9 (Múltipla Escolha)
Qual endpoint corresponde ao arquivo pages/api/user/[id].js?

a) /api/user/[id]
b) /api/user/:id
c) /api/user/123, /api/user/456, etc
d) /user/[id]

**Resposta:** c) /api/user/123, /api/user/456, etc - qualquer valor depois de /api/user/

---

## Questão 10 (Múltipla Escolha)
Como processar requisições POST em uma API Route?

a) if (req.method === 'POST')
b) if (req.type === 'POST')
c) if (req.request === 'POST')
d) Não é possível

**Resposta:** a) if (req.method === 'POST') - verifica o método HTTP da requisição