# 9. META TAGS E SEO

## Head Component

**Importar:** `import Head from 'next/head'`

```javascript
import Head from 'next/head'

export default function Home() {
  return (
    <>
      <Head>
        <title>Minha Página</title>
        <meta name="description" content="Descrição da página" />
        <meta name="keywords" content="palavra1, palavra2" />
        <meta property="og:title" content="Título para redes sociais" />
      </Head>
      <div>Conteúdo</div>
    </>
  )
}
```

## O que são Meta Tags?

**Meta tags** são tags no `<head>` do HTML, **não visíveis na página**, mas usadas por:
- Mecanismos de busca (SEO)
- Reden sociais (como conteúdo aparece ao compartilhar)
- Navegadores (título, descrição)

## Tipos de Meta Tags:

### 1. Título:
```javascript
<title>Minha Página</title>
```

### 2. Meta Description:
```javascript
<meta name="description" content="Descrição da página" />
```

### 3. Open Graph Tags (Redes Sociais):
**Começam com `og:`** (ex: `og:title`, `og:description`, `og:image`)

```javascript
<meta property="og:title" content="Título para redes sociais" />
<meta property="og:description" content="Descrição para redes sociais" />
```

**Para que servem:** Definir como conteúdo aparece quando compartilhado em redes sociais

## Características:

- ✅ **Cada página pode ter suas próprias meta tags personalizadas**
- ✅ **Importantes para SEO e redes sociais**
- ✅ **Não são visíveis na página** (ficam no `<head>`)
- ✅ **Melhoram resultados de busca** e aparência em redes sociais
