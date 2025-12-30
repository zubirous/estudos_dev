# 2. ESTRUTURA DE PROJETO

## Estrutura Básica:

```
meu-projeto/
├── pages/              # Páginas (roteamento automático)
│   ├── api/           # API Routes
│   ├── index.js       # Página inicial (/)
│   ├── about.js       # Página /about
│   ├── _app.js        # Componente raiz
│   └── _document.js   # Personalização do HTML
├── public/            # Arquivos estáticos
├── components/        # Componentes React
├── styles/            # Estilos
└── package.json
```

## Arquivos Importantes:

### `pages/_app.js`
- **Componente que envolve todas as páginas**
- **Executa no cliente e servidor** (durante SSR)
- Importar CSS global aqui

### `pages/_document.js`
- **Personalização do HTML** (`<html>`, `<head>`, `<body>`)
- **Executa apenas no servidor** durante SSR (não no cliente)
- Use para modificar estrutura HTML base

### `next.config.js`
- **Configurações do Next.js**
- Configurar domínios de imagens, variáveis de ambiente, etc

### `pages/api/`
- **Endpoints da API**
- Cada arquivo vira um endpoint em `/api/`

### `public/`
- **Arquivos estáticos acessíveis publicamente**
- **Acessíveis pela URL raiz** (ex: `/logo.png` acessa `public/logo.png`)
- Servidos estaticamente e acessíveis via URL

### `components/`
- **Componentes React reutilizáveis**
- Podem ser importados e usados em qualquer página
