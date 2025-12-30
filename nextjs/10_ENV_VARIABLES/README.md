# 10. ENVIRONMENT VARIABLES

## Conceito
Variáveis de ambiente para configurações que variam entre ambientes (desenvolvimento, produção).

## Como Acessar:
**Sintaxe:** `process.env.VARIAVEL`

```javascript
const dbUrl = process.env.DATABASE_URL
const apiUrl = process.env.NEXT_PUBLIC_API_URL
```

## Tipos de Variáveis:

### Variáveis Privadas (sem NEXT_PUBLIC_):
- **Acessíveis:** Apenas no servidor
- **Onde usar:** `getServerSideProps`, API Routes, etc
- **Exemplo:** `DATABASE_URL`, `API_KEY`

### Variáveis Públicas (com NEXT_PUBLIC_):
- **Acessíveis:** No cliente e servidor
- **Onde usar:** Componentes do cliente, qualquer lugar
- **Exemplo:** `NEXT_PUBLIC_API_URL`

## Arquivos de Ambiente:

- **`.env.local`**: Para desenvolvimento local
- **`.env.production`**: Para produção

## Regras Importantes:

- ✅ **Variáveis sem `NEXT_PUBLIC_`**: Apenas no servidor
- ✅ **Variáveis com `NEXT_PUBLIC_`**: Expostas ao cliente
- ✅ **Nunca exponha chaves secretas ao cliente!** (código JavaScript no cliente é visível e chaves podem ser roubadas)
- ✅ **Úteis para configurações que variam entre ambientes**

## Exemplo:

```javascript
// .env.local
DATABASE_URL=postgresql://...  // Privada (servidor apenas)
NEXT_PUBLIC_API_URL=http://localhost:3000/api  // Pública (cliente e servidor)

// Código
const dbUrl = process.env.DATABASE_URL  // Apenas no servidor
const apiUrl = process.env.NEXT_PUBLIC_API_URL  // Cliente e servidor
```
