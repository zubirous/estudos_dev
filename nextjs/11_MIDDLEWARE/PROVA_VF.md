# Prova: MIDDLEWARE - Next.js

## Provas de Verdadeiro ou Falso

## Questão 1 (Verdadeiro/Falso)
Middleware no Next.js executa antes de cada requisição.

**Resposta:** Verdadeiro. Middleware executa antes de processar a requisição, permitindo interceptar e modificar requisições.

---

## Questão 2 (Verdadeiro/Falso)
Middleware no Next.js é útil apenas para autenticação.

**Resposta:** Falso. Middleware é útil para autenticação, logging, validação de rotas, redirecionamento e muito mais.

---

## Questão 3 (Verdadeiro/Falso)
O arquivo middleware.js deve ficar na pasta pages/ no Next.js.

**Resposta:** Falso. O arquivo middleware.js deve ficar na raiz do projeto, não em pages/.

---

## Questão 4 (Verdadeiro/Falso)
Middleware pode redirecionar requisições usando Response.redirect().

**Resposta:** Verdadeiro. Middleware pode usar Response.redirect() para redirecionar requisições antes de processá-las.

---

## Questão 5 (Verdadeiro/Falso)
Middleware executa apenas no servidor, não no cliente.

**Resposta:** Verdadeiro. Middleware executa no servidor Node.js antes de processar a requisição.

---

## Questão 6 (Verdadeiro/Falso)
O campo matcher é obrigatório no middleware do Next.js.

**Resposta:** Falso. O campo matcher é opcional, mas recomendado para otimizar performance interceptando apenas rotas necessárias.

---

## Questão 7 (Verdadeiro/Falso)
Middleware pode modificar headers da requisição.

**Resposta:** Verdadeiro. Middleware pode ler e modificar headers da requisição antes de processá-la.

---

## Questão 8 (Verdadeiro/Falso)
Pode haver múltiplos middlewares no mesmo projeto Next.js.

**Resposta:** Falso. Pode haver apenas um arquivo middleware.js na raiz do projeto, mas ele pode interceptar múltiplas rotas usando o matcher.
