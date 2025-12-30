# 📚 Estudos Dev

Sistema completo de estudos para desenvolvimento e arquitetura de software, com foco em **Arquitetura**, **MySQL** e **Next.js**. Inclui material teórico organizado e aplicação prática de quiz automatizada.

## 🎯 Visão Geral

Este repositório contém:
- 📖 **Material de Estudo**: Conteúdo teórico organizado por tópicos
- 🧠 **Sistema de Quiz**: Aplicação web automatizada com 247+ questões
- 🏗️ **Arquitetura Moderna**: Padrões e conceitos fundamentais
- 🗄️ **Banco de Dados**: MySQL completo com conceitos avançados
- ⚛️ **Frontend**: Next.js com boas práticas e conceitos críticos

## 📂 Estrutura do Projeto

```
estudos_dev/
├── arquitetura/          # Padrões arquiteturais
│   ├── 01_ARQUITETURA_VS_PADRAO/
│   ├── 02_ARQUITETURA_EM_CAMADAS/
│   ├── 03_MVC/
│   ├── 04_MVP/
│   ├── 05_MVVM/
│   ├── 06_ARQUITETURA_3_TIER/
│   ├── 07_MICROSERVICOS/
│   ├── 08_MONOLITICO/
│   ├── 09_CLIENTE_SERVIDOR/
│   ├── 10_SOA/
│   └── 11_DESIGN_PATTERNS/
├── mysql/               # Banco de dados MySQL
│   ├── 01_CONCEITOS_BASICOS/
│   ├── 02_DDL/
│   ├── 03_DML/
│   ├── 04_DQL/
│   ├── 05_INDICES/
│   ├── 06_TRANSACOES/
│   ├── 07_VIEWS/
│   ├── 08_STORED_PROCEDURES/
│   ├── 09_TRIGGERS/
│   ├── 10_OTIMIZACAO/
│   └── 11_NORMALIZACAO/
├── nextjs/              # Framework Next.js
│   ├── 01_O_QUE_E_NEXTJS/
│   ├── 02_ESTRUTURA_PROJETO/
│   ├── 03_ROTEAMENTO/
│   ├── 04_RENDERIZACAO/
│   ├── 05_API_ROUTES/
│   ├── 06_DATA_FETCHING/
│   ├── 07_OTIMIZACAO_IMAGENS/
│   ├── 08_CSS_ESTILOS/
│   ├── 09_META_TAGS_SEO/
│   ├── 10_ENV_VARIABLES/
│   └── 11_MIDDLEWARE/
├── quiz_app/           # Aplicação de quiz
│   ├── app.py
│   ├── question_parser.py
│   ├── requirements.txt
│   ├── static/
│   ├── templates/
│   └── *.md (documentação)
├── RESUMO_RAPIDO.md    # Revisão rápida dos conceitos
└── README.md
```

## 🚀 Como Usar

### 📖 Material de Estudo

Cada tópico contém:
- **README.md**: Explicação teórica detalhada
- **PROVA_ALTERNATIVAS.md**: Questões de múltipla escolha
- **PROVA_VF.md**: Questões verdadeiro/falso

Para estudar:
1. Navegue até o tópico desejado
2. Leia o `README.md` para conceitos teóricos
3. Pratique com as questões de prova

### 🧠 Sistema de Quiz

O quiz carrega automaticamente todas as questões dos arquivos markdown.

#### Instalação Rápida

**Windows:**
```powershell
cd quiz_app
.\start.ps1
```

**Linux/Mac:**
```bash
cd quiz_app
chmod +x start.sh
./start.sh
```

#### Instalação Manual

```bash
cd quiz_app
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python app.py
```

Acesse: `http://localhost:5000`

#### Funcionalidades do Quiz

- ✅ **247+ questões** organizadas por tópicos
- ✅ **33 tópicos** cobrindo Arquitetura, MySQL e Next.js
- ✅ Questões de **múltipla escolha** e **verdadeiro/falso**
- ✅ **Feedback imediato** com explicações
- ✅ **Resultados detalhados** com revisão completa
- ✅ **Barra de progresso** visual
- ✅ **Design responsivo** e moderno

## 📊 Estatísticas

- **247 questões** carregadas automaticamente
- **33 tópicos** organizados
- **3 áreas principais**: Arquitetura, MySQL, Next.js
- **2 tipos de questões**: Múltipla escolha e Verdadeiro/Falso

## 🏗️ Arquitetura - Conceitos Críticos

### Padrões Principais
- **MVC**: Model-View-Controller
- **MVP**: Model-View-Presenter
- **MVVM**: Model-View-ViewModel
- **Monolítico vs Microserviços**
- **Arquitetura em Camadas (3-Tier)**
- **SOA**: Service-Oriented Architecture
- **Design Patterns**: Singleton, Factory, Repository, Observer, Strategy

### Diferenças Críticas
- MVC: View acessa Model | MVP: View passiva | MVVM: Binding bidirecional
- Monolítico: Simples, um deploy | Microserviços: Complexo, múltiplos deploys

## 🗄️ MySQL - Conceitos Críticos

### Operações Essenciais
- **JOINs**: INNER, LEFT, RIGHT (mais importante!)
- **WHERE vs HAVING**: Filtragem antes/depois do GROUP BY
- **DELETE vs TRUNCATE**: Com/sem WHERE, AUTO_INCREMENT
- **Transações ACID**: Atomicity, Consistency, Isolation, Durability

### Conceitos Avançados
- **Normalização**: 1FN, 2FN, 3FN
- **Índices**: Otimização de consultas
- **Views**: Tabelas virtuais
- **Stored Procedures**: Lógica no banco
- **Triggers**: Automação de ações

## ⚛️ Next.js - Conceitos Críticos

### Estratégias de Renderização
- **SSR**: Server-Side Rendering (a cada requisição)
- **SSG**: Static Site Generation (no build)
- **ISR**: Incremental Static Regeneration (build + revalidação)

### Funcionalidades Principais
- **File-based Routing**: Sistema de rotas automático
- **API Routes**: Endpoints serverless
- **Data Fetching**: getStaticProps, getServerSideProps, getStaticPaths
- **Image Optimization**: Componente Image otimizado
- **Middleware**: Interceptação de requisições

## 🛠️ Tecnologias Utilizadas

### Backend (Quiz App)
- **Python 3.11+**
- **Flask**: Framework web
- **Jinja2**: Templates HTML
- **Markdown**: Parsing de questões

### Frontend (Quiz App)
- **HTML5/CSS3**: Estrutura e estilos
- **JavaScript**: Interatividade
- **Responsive Design**: Mobile-first

### Documentação
- **Markdown**: Conteúdo estruturado
- **Git**: Controle de versão

## 🤝 Como Contribuir

### Adicionando Novo Conteúdo

1. **Crie estrutura de tópico**:
   ```
   [area]/[numero]_[NOME_TOPICO]/
   ├── README.md
   ├── PROVA_ALTERNATIVAS.md
   ├── PROVA_VF.md
   ```

2. **Formato das questões**:

   **Múltipla Escolha (PROVA_ALTERNATIVAS.md)**:
   ```markdown
   ## Questão 1 (Múltipla Escolha)
   Texto da pergunta?

   a) Opção A
   b) Opção B
   c) Opção C
   d) Opção D

   **Resposta:** b) Opção B
   ```

   **Verdadeiro/Falso (PROVA_VF.md)**:
   ```markdown
   ## Questão 1 (Verdadeiro/Falso)
   Texto da pergunta?

   **Resposta:** Verdadeiro. Explicação...
   ```

3. **Reinicie o quiz**: As questões são carregadas automaticamente!

### Melhorando o Código
- Pull requests são bem-vindos
- Siga as melhores práticas de código
- Adicione testes quando aplicável

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🎯 Objetivo

Este repositório serve como:
- **Material de referência** para estudos em desenvolvimento
- **Sistema de avaliação** de conhecimentos adquiridos
- **Base para expansão** com novos tópicos e tecnologias
- **Exemplo prático** de aplicação web simples com Python/Flask

---

**Boa sorte nos estudos!** 🚀
