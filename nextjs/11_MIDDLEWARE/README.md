# 11. MIDDLEWARE

## Conceito
Executa código **antes de cada requisição** no servidor, antes de processar a requisição.

## Localização:
- **Arquivo `middleware.js` na raiz do projeto** (não em `pages/`)

## O que pode fazer:
- ✅ **Redirecionar** requisições
- ✅ **Bloquear** requisições
- ✅ **Modificar** requisições
- ✅ **Autenticação** (verificar tokens, cookies)
- ✅ **Logging** (registrar requisições)
- ✅ **Validação de rotas**

## Exemplo Básico:

```javascript
// middleware.js (raiz do projeto)
export function middleware(request) {
  // Executa antes de cada requisição
  const token = request.cookies.get('token')  // Acessar cookies
  
  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
    return Response.redirect(new URL('/login', request.url))  // Redirecionar
  }
  
  // Se não retornar nada, requisição continua normalmente
}
```

## Configuração do Matcher:

**O campo `matcher`** especifica quais rotas o middleware deve interceptar:

```javascript
export const config = {
  // Intercepta apenas rotas que começam com /dashboard
  matcher: '/dashboard/:path*',
  
  // Ou múltiplas rotas (array)
  matcher: ['/dashboard/:path*', '/admin/:path*'],
  
  // Ou todas exceto algumas
  matcher: [
    '/((?!api|_next/static|_next/image|favicon.ico).*)',
  ],
}
```

## Características:

- ✅ **Executa apenas no servidor, antes de processar a requisição**
- ✅ **Pode acessar cookies**: `request.cookies.get('nome')`
- ✅ **Pode redirecionar**: `Response.redirect()`
- ✅ **Se não retornar nada**: Requisição continua normalmente
- ✅ **Útil para**: Autenticação, logging, validação de rotas, redirecionamento
- ✅ **Use `matcher`** para otimizar performance (interceptar apenas rotas necessárias)
