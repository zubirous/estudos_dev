# 7. OTIMIZAÇÃO DE IMAGENS

## Componente Image

**Importante:** Use `<Image>` do Next.js ao invés de `<img>` para otimizações automáticas.

**Propriedades obrigatórias:** `src`, `alt`, `width`, `height`

```javascript
import Image from 'next/image'

export default function Home() {
  return (
    <Image
      src="/foto.jpg"
      alt="Descrição"
      width={500}
      height={300}
    />
  )
}
```

## Imagem Externa

Para usar imagens de domínios externos, configure em `next.config.js`:

```javascript
// next.config.js
module.exports = {
  images: {
    domains: ['example.com'],
  },
}
```

**Necessário:** Configurar domínio em `next.config.js` no campo `images.domains`

## Benefícios do componente Image:

- ✅ **Otimização automática** (reduz tamanho)
- ✅ **Lazy loading** (carrega apenas quando está prestes a aparecer na tela)
- ✅ **Conversão para WebP** quando suportado pelo navegador
- ✅ **Tamanhos responsivos** (gera múltiplos tamanhos)
- ✅ **Melhor performance** que tag `<img>` tradicional

## Por que usar Image ao invés de <img>?

- `<img>`: Sem otimizações, carrega tudo de uma vez
- `<Image>`: Otimizações automáticas, lazy loading, formato WebP

## É obrigatório usar Image?

**Não, mas é recomendado** para melhor performance. Você pode usar `<img>`, mas perderá as otimizações automáticas.

## Lazy Loading:

**Lazy loading** = Carregar imagens apenas quando estão prestes a aparecer na tela (não carrega todas de uma vez)
