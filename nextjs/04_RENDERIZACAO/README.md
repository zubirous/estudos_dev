# 4. RENDERIZAÇÃO - SSR, SSG, ISR

## SSR (Server-Side Rendering)
Renderiza no servidor a cada requisição.

**Função:** `getServerSideProps`
**Quando executa:** A cada requisição (no servidor)
**Características:**
- Executa a cada requisição
- Sempre dados atualizados
- Mais lento que SSG (processa a cada requisição)

**Quando usar:**
- Dados que mudam constantemente
- Dashboard com dados em tempo real
- Dados personalizados por usuário
- Conteúdo que precisa estar sempre atualizado

## SSG (Static Site Generation)
Gera páginas estáticas no build.

**Função:** `getStaticProps`
**Quando executa:** No build time (apenas durante o build)
**Características:**
- Executa apenas no build
- Páginas pré-renderizadas (rápidas)
- Dados podem ficar desatualizados até rebuild
- **Mais rápido que SSR** (servido como arquivo estático)

**Quando usar:**
- Blog posts
- Documentação
- Conteúdo estático
- Páginas que não mudam frequentemente

## ISR (Incremental Static Regeneration)
SSG com revalidação periódica.

**Função:** `getStaticProps` com `revalidate`
**Quando executa:** Build time + revalidação periódica em background
**Características:**
- Gera estático no build (rápido como SSG)
- Revalida em background após X segundos
- **Combina velocidade de SSG com atualização**
- **Permite regenerar páginas sem rebuild completo**

**Quando usar:**
- Conteúdo que atualiza ocasionalmente (ex: catálogo de produtos)
- Blog que atualiza uma vez por dia
- Conteúdo que precisa de atualização periódica mas não constante

## getStaticPaths (para rotas dinâmicas com SSG)

**Necessário:** Para rotas dinâmicas com SSG (ex: `pages/product/[id].js`)

**fallback:**
- `false`: Retorna 404 se não estiver em paths
- `true`: Gera página sob demanda
- `'blocking'`: Gera página sob demanda, aguarda renderização

## Comparação de Performance:

| Método | Velocidade | Dados Atualizados |
|--------|-----------|-------------------|
| **SSG** | ⚡⚡⚡ Mais rápido | ❌ Podem ficar desatualizados |
| **ISR** | ⚡⚡ Rápido | ✅ Atualizados periodicamente |
| **SSR** | ⚡ Mais lento | ✅ Sempre atualizados |

## Resumo:

- **SSG**: Mais rápido, dados podem ficar desatualizados
- **SSR**: Sempre atualizado, mais lento
- **ISR**: Rápido + atualização periódica (melhor dos dois mundos)
