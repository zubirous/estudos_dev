# 5. API ROUTES

## Conceito
Criar endpoints de API dentro do projeto Next.js, sem precisar de servidor separado.

## Localização:
- **Arquivos em `pages/api/`** se tornam endpoints automaticamente
- `pages/api/users.js` → endpoint `/api/users`
- `pages/api/user/[id].js` → endpoint `/api/user/123`, `/api/user/456`, etc

## Handler:
- Recebe `req` (request) e `res` (response)
- **Similar a Express.js**
- **Executa apenas no servidor** (Node.js)

## Métodos HTTP:
- **Pode processar todos os métodos HTTP**: GET, POST, PUT, DELETE, etc
- Verificar método com `req.method`

## Exemplo Básico:

```javascript
// pages/api/users.js
export default function handler(req, res) {
  if (req.method === 'GET') {
    res.status(200).json({ message: 'GET request' })
  } else if (req.method === 'POST') {
    res.status(201).json({ message: 'POST request', body: req.body })
  } else {
    res.status(405).json({ message: 'Method not allowed' })
  }
}
```

## Rotas Dinâmicas:

```javascript
// pages/api/user/[id].js
export default function handler(req, res) {
  const { id } = req.query  // Acessa parâmetro [id]
  
  if (req.method === 'GET') {
    res.status(200).json({ userId: id })
  }
}
```

**Acessar parâmetros:** `req.query` ou `req.params` (dependendo da configuração)

## Características:
- ✅ **Executa apenas no servidor** (não no cliente)
- ✅ **Similar a Express.js** (req, res)
- ✅ **Pode processar todos os métodos HTTP**
- ✅ **Útil para criar APIs dentro do projeto** (sem servidor separado)
- ✅ **Suporta rotas dinâmicas** usando `[id].js`
