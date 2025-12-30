# 3. ROTEAMENTO (File-based Routing)

## Conceito
Next.js usa **file-based routing** (roteamento baseado em arquivos) - cada arquivo em `pages/` vira uma rota automaticamente.

## Páginas Básicas

```
pages/index.js      → http://localhost:3000/  (rota raiz, não /index)
pages/about.js      → http://localhost:3000/about
pages/contact.js    → http://localhost:3000/contact
```

**Importante:** `pages/index.js` cria a rota raiz (`/`), não `/index`

## Roteamento Dinâmico

```
pages/user/[id].js          → /user/123, /user/456 (qualquer valor)
pages/product/[slug].js     → /product/notebook, /product/mouse
pages/post/[...all].js      → /post/a/b/c (catch-all - captura múltiplos segmentos)
pages/docs/[[...slug]].js   → /docs, /docs/a, /docs/a/b (optional catch-all - também captura rota sem parâmetros)
```

**Rotas dinâmicas são geradas em runtime ou via getStaticPaths** (não apenas no build time)

## Rotas Aninhadas

**Criar sub-rotas:** Criar uma pasta com o mesmo nome da rota e colocar `index.js` dentro cria uma sub-rota.

## Acessar Parâmetros de Rota Dinâmica

Use `useRouter().query` para acessar parâmetros:

```javascript
import { useRouter } from 'next/router'

export default function User() {
  const router = useRouter()
  const { id } = router.query  // Acessa parâmetro [id]
  return <h1>User ID: {id}</h1>
}
```

**`useRouter().query` retorna um objeto com os parâmetros da rota dinâmica**

## Navegação:

### Usando Link (recomendado):
```javascript
import Link from 'next/link'

<Link href="/about">Ir para About</Link>
```

**Nota:** Em versões mais recentes, o Link pode envolver qualquer elemento (não requer tag `<a>`)

### Usando useRouter (navegação programática):
```javascript
import { useRouter } from 'next/router'

const router = useRouter()
router.push('/about')  // Navega programaticamente
```

**`useRouter` fornece métodos como `push()`, `replace()`, `back()` para navegação programática**

## Tipos de Rotas Dinâmicas:

- **`[param].js`**: Rota dinâmica simples (ex: `/user/123`)
- **`[...slug].js`**: Catch-all (captura múltiplos segmentos: `/post/a/b/c`)
- **`[[...slug]].js`**: Catch-all opcional (também captura rota sem parâmetros: `/docs` ou `/docs/a/b`)
