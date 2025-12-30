# Quiz App - Teste de Conhecimentos

Aplicação web para testar conhecimentos em Arquitetura, MySQL e Next.js.

## Características

- ✅ 95+ questões de 33 tópicos diferentes
- ✅ Questões de múltipla escolha
- ✅ Questões verdadeiro/falso
- ✅ Feedback imediato com explicações
- ✅ Resultados detalhados com revisão
- ✅ Barra de progresso
- ✅ Design responsivo e moderno

## Instalação Rápida

### Windows:
**PowerShell:**
```powershell
cd quiz_app
.\start.ps1
```
*Se der erro de política, execute primeiro: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`*

**CMD:**
```cmd
cd quiz_app
start.bat
```

**Manual (qualquer terminal):**
```bash
cd quiz_app
python -m venv venv
venv\Scripts\activate          # Windows
# ou
source venv/bin/activate       # Linux/Mac
pip install -r requirements.txt
python app.py
```

### Linux/Mac:
```bash
# Na pasta quiz_app
chmod +x start.sh
./start.sh
```

## Instalação Manual

1. Crie e ative o ambiente virtual:
```bash
cd quiz_app
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
python app.py
```

4. Acesse no navegador:
```
http://localhost:5000
```

## Estrutura

- `app.py`: Aplicação Flask principal
- `question_parser.py`: Parser para arquivos markdown de questões
- `templates/`: Templates HTML (index, quiz, results)
- `static/`: Arquivos CSS e JavaScript
- `test_parser.py`: Script de teste do parser

## Como Usar

1. Acesse `http://localhost:5000`
2. Escolha um tópico (ex: "MySQL: Conceitos Basicos")
3. Responda as questões
4. Veja feedback imediato após cada resposta
5. Ao final, visualize seus resultados e revisão completa

## Tópicos Disponíveis

- **Arquitetura**: MVC, MVP, MVVM, Microserviços, Monolítico, SOA, etc.
- **MySQL**: DDL, DML, DQL, Índices, Transações, Views, Procedures, etc.
- **Next.js**: Roteamento, Renderização, API Routes, Data Fetching, etc.

