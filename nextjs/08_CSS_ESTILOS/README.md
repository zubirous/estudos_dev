# 8. CSS E ESTILOS

Next.js suporta **CSS Modules, Styled JSX e CSS global** - você pode usar todos juntos.

## CSS Modules:

**Vantagem:** Estilos escopados por componente (não vazam para outros componentes)

**Como usar:**
1. Criar arquivo `.module.css` (ex: `styles/Home.module.css`)
2. Importar como objeto: `import styles from './styles.module.css'`
3. Usar: `className={styles.container}`

```javascript
// styles/Home.module.css
.container {
  padding: 20px;
}

.title {
  color: blue;
}
```

```javascript
// pages/index.js
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Título</h1>
    </div>
  )
}
```

**Características:**
- Estilos escopados (não vazam)
- CSS Modules geram nomes únicos automaticamente
- Evita conflitos de nomes

## Global CSS:

**Aplicado em todas as páginas da aplicação**

**Onde importar:** No `_app.js` (não em componentes individuais)

```javascript
// styles/globals.css
body {
  margin: 0;
  font-family: Arial;
}
```

```javascript
// pages/_app.js
import '../styles/globals.css'

export default function App({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

**Características:**
- Aplicado em todas as páginas
- Deve ser importado no `_app.js`
- Use para estilos globais (reset, fontes, etc)

## Styled JSX (built-in):

**CSS built-in** que permite escrever CSS dentro de componentes

**Sintaxe:** `<style jsx>...</style>`

```javascript
export default function Home() {
  return (
    <div>
      <h1>Título</h1>
      <style jsx>{`
        h1 {
          color: blue;
        }
      `}</style>
    </div>
  )
}
```

## Comparação:

| Tipo | Escopo | Onde Importar | Use Para |
|------|--------|---------------|----------|
| **CSS Modules** | Escopado (não vaza) | No componente | Estilos por componente |
| **CSS Global** | Todas as páginas | No `_app.js` | Estilos globais |
| **Styled JSX** | Escopado | Dentro do componente | CSS inline no componente |

**Você pode usar todos juntos!**
