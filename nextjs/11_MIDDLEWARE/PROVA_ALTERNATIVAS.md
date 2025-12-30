# Prova: MIDDLEWARE - Next.js

## Provas de Alternativas

## Questão 1 (Múltipla Escolha)
Onde fica o arquivo middleware.js no Next.js?

a) pages/
b) Raiz do projeto
c) components/
d) public/

**Resposta:** b) Raiz do projeto

---

## Questão 2 (Múltipla Escolha)
Para que serve middleware no Next.js?

a) Criar páginas estáticas
b) Executar código antes de cada requisição (autenticação, redirecionamento, etc)
c) Gerenciar estado global
d) Compilar código

**Resposta:** b) Executar código antes de cada requisição (autenticação, redirecionamento, etc)

---

## Questão 3 (Múltipla Escolha)
O que o middleware pode fazer no Next.js?

a) Apenas redirecionar
b) Redirecionar, bloquear, modificar requisições
c) Apenas bloquear
d) Apenas modificar

**Resposta:** b) Redirecionar, bloquear, modificar requisições

---

## Questão 4 (Múltipla Escolha)
O campo `matcher` no middleware é usado para:

a) Definir qual middleware usar
b) Especificar quais rotas o middleware deve interceptar
c) Definir o método HTTP
d) Definir headers

**Resposta:** b) Especificar quais rotas o middleware deve interceptar

---

## Questão 5 (Múltipla Escolha)
Middleware no Next.js executa:

a) Apenas no cliente
b) Apenas no servidor, antes de processar a requisição
c) Apenas no servidor, depois de processar a requisição
d) No cliente e servidor

**Resposta:** b) Apenas no servidor, antes de processar a requisição

---

## Questão 6 (Múltipla Escolha)
Qual função do middleware permite redirecionar requisições?

a) redirect()
b) Response.redirect()
c) Router.redirect()
d) Next.redirect()

**Resposta:** b) Response.redirect()

---

## Questão 7 (Múltipla Escolha)
Para que serve o middleware no Next.js além de autenticação?

a) Apenas autenticação
b) Logging, validação de rotas, redirecionamento, etc
c) Apenas logging
d) Apenas validação

**Resposta:** b) Logging, validação de rotas, redirecionamento, etc

---

## Questão 8 (Múltipla Escolha)
Como acessar cookies no middleware do Next.js?

a) request.cookies.get('nome')
b) cookies.get('nome')
c) req.cookies('nome')
d) getCookie('nome')

**Resposta:** a) request.cookies.get('nome')

---

## Questão 9 (Múltipla Escolha)
O que acontece se o middleware não retornar nada?

a) A requisição é bloqueada
b) A requisição continua normalmente
c) A requisição é redirecionada
d) Ocorre um erro

**Resposta:** b) A requisição continua normalmente

---

## Questão 10 (Múltipla Escolha)
Como interceptar múltiplas rotas no middleware?

a) Criar múltiplos arquivos middleware.js
b) Usar array no matcher: matcher: ['/dashboard/:path*', '/admin/:path*']
c) Não é possível
d) Usar múltiplos exports

**Resposta:** b) Usar array no matcher: matcher: ['/dashboard/:path*', '/admin/:path*']
