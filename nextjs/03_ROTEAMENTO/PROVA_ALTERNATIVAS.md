# Prova: ROTEAMENTO - Next.js

## Provas de Alternativas

## Questão 1 (Múltipla Escolha)
Qual arquivo cria a rota /about?

a) pages/about.js
b) components/about.js
c) src/about.js
d) public/about.js

**Resposta:** a) pages/about.js

---

## Questão 2 (Múltipla Escolha)
Como criar uma rota dinâmica no Next.js?

a) Usando [param].js
b) Usando (param).js
c) Usando <param>.js
d) Usando {{param}}.js

**Resposta:** a) Usando [param].js

---

## Questão 3 (Múltipla Escolha)
Qual sintaxe cria uma rota catch-all no Next.js?

a) [...slug].js
b) [slug].js
c) (slug).js
d) {{slug}}.js

**Resposta:** a) [...slug].js - captura múltiplos segmentos

---

## Questão 4 (Múltipla Escolha)
Como navegar entre páginas no Next.js?

a) Usando tag <a>
b) Usando componente Link do next/link
c) Usando window.location
d) Qualquer método

**Resposta:** b) Usando componente Link do next/link - recomendado pelo Next.js

---

## Questão 5 (Múltipla Escolha)
Como navegar programaticamente no Next.js?

a) window.location.href
b) router.push() do useRouter
c) Link component
d) Não é possível

**Resposta:** b) router.push() do useRouter - permite navegação programática

---

## Questão 6 (Múltipla Escolha)
Qual rota corresponde ao arquivo pages/user/[id].js?

a) /user
b) /user/[id]
c) /user/123, /user/456, etc
d) /[id]/user

**Resposta:** c) /user/123, /user/456, etc - qualquer valor depois de /user/

---

## Questão 7 (Múltipla Escolha)
Qual sintaxe cria uma rota catch-all opcional no Next.js?

a) [...slug].js
b) [[...slug]].js
c) [slug].js
d) (slug).js

**Resposta:** b) [[...slug]].js - catch-all opcional, também captura a rota sem parâmetros

---

## Questão 8 (Múltipla Escolha)
Como acessar parâmetros de rota dinâmica no Next.js?

a) props.params
b) useRouter().query
c) window.location
d) req.params

**Resposta:** b) useRouter().query - retorna objeto com parâmetros da rota

---

## Questão 9 (Múltipla Escolha)
O Next.js usa roteamento:

a) Baseado em configuração
b) File-based routing (baseado em arquivos)
c) Baseado em código
d) Manual

**Resposta:** b) File-based routing (baseado em arquivos) - cada arquivo em pages/ vira uma rota

---

## Questão 10 (Múltipla Escolha)
Qual arquivo cria a rota inicial (/) no Next.js?

a) pages/home.js
b) pages/index.js
c) pages/main.js
d) pages/root.js

**Resposta:** b) pages/index.js - cria a rota raiz (/)