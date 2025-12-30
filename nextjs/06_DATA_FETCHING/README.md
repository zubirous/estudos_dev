# 6. DATA FETCHING

## Métodos de Data Fetching

| Método | Quando Executa | Onde Executa | Use Para |
|--------|---------------|--------------|----------|
| `getServerSideProps` | A cada requisição | Servidor | Dados dinâmicos, autenticação |
| `getStaticProps` | No build time | Servidor (build) | Conteúdo estático |
| `getStaticProps` + `revalidate` | Build + periodicamente | Servidor | Conteúdo que atualiza ocasionalmente |
| `useEffect` | No cliente (após renderização) | Cliente | Dados que não afetam SEO |

## getStaticProps vs getServerSideProps

- **getStaticProps**: 
  - Executa no build time
  - Estático, rápido
  - Dados podem ficar desatualizados
  - **Mais rápido que getServerSideProps**

- **getServerSideProps**: 
  - Executa a cada requisição
  - Dinâmico, sempre atualizado
  - Mais lento (processa a cada requisição)

## Quando usar cada um:

### getStaticProps:
- Blog posts
- Documentação
- Conteúdo estático
- Páginas que não mudam frequentemente

### getServerSideProps:
- Dashboard do usuário
- Dados personalizados por usuário
- Autenticação
- Dados que mudam constantemente

### ISR (getStaticProps + revalidate):
- Conteúdo que atualiza ocasionalmente
- Catálogo de produtos
- Blog que atualiza uma vez por dia
- Combina velocidade de SSG com atualização

### useEffect:
- **Dados que não afetam SEO**
- Dados que só precisam no cliente
- Dados que não são críticos para primeira renderização
- **NÃO usar para dados que afetam SEO** (executa no cliente após renderização)

## SEO:

- ✅ **getStaticProps ou getServerSideProps**: Executam no servidor, conteúdo disponível para crawlers (bom para SEO)
- ❌ **useEffect**: Executa no cliente, conteúdo não disponível para crawlers (ruim para SEO)
