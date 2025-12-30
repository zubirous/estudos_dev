# Como o Quiz Lê as Questões Automaticamente

## ✅ Sim, é totalmente automático!

O quiz lê e incorpora automaticamente todas as questões dos arquivos de prova. Veja como funciona:

## 📂 Estrutura de Arquivos

O quiz procura automaticamente por:
- `arquitetura/*/PROVA_ALTERNATIVAS.md` - Questões de múltipla escolha
- `arquitetura/*/PROVA_VF.md` - Questões verdadeiro/falso
- `mysql/*/PROVA_ALTERNATIVAS.md` - Questões de múltipla escolha
- `mysql/*/PROVA_VF.md` - Questões verdadeiro/falso
- `nextjs/*/PROVA_ALTERNATIVAS.md` - Questões de múltipla escolha
- `nextjs/*/PROVA_VF.md` - Questões verdadeiro/falso

## 🔄 Processo Automático

1. **Na inicialização do app** (`app.py`):
   - Cria o `QuestionParser` apontando para o diretório raiz
   - Chama `load_all_questions()` automaticamente
   - Carrega TODAS as questões de TODOS os tópicos

2. **O parser** (`question_parser.py`):
   - Percorre os diretórios `arquitetura/`, `mysql/`, `nextjs/`
   - Para cada subdiretório encontrado:
     - Verifica se existe `PROVA_ALTERNATIVAS.md` → chama `parse_alternativas_file()`
     - Verifica se existe `PROVA_VF.md` → chama `parse_vf_file()`
   - Combina todas as questões encontradas
   - Retorna um dicionário com todas as questões organizadas por tópico

3. **Formato esperado**:

### PROVA_ALTERNATIVAS.md:
```markdown
## Questão 1 (Múltipla Escolha)
Texto da pergunta?

a) Opção A
b) Opção B
c) Opção C
d) Opção D

**Resposta:** b) Opção B
```

### PROVA_VF.md:
```markdown
## Questão 1 (Verdadeiro/Falso)
Texto da pergunta?

**Resposta:** Verdadeiro. Explicação...
```

## ✨ Vantagens

1. **Automático**: Basta adicionar/editar arquivos e reiniciar o app
2. **Não precisa alterar código**: Adicione novas questões nos arquivos markdown
3. **Flexível**: Suporta múltipla escolha (a-d) e verdadeiro/falso
4. **Organizado**: Questões agrupadas por tópico automaticamente

## 🔧 Como Adicionar Novas Questões

1. **Adicione questões em arquivos existentes**:
   - Edite `PROVA_ALTERNATIVAS.md` ou `PROVA_VF.md` de qualquer tópico
   - Adicione novas questões no formato correto

2. **Crie novos tópicos**:
   - Crie um novo subdiretório em `arquitetura/`, `mysql/` ou `nextjs/`
   - Adicione `PROVA_ALTERNATIVAS.md` e/ou `PROVA_VF.md`
   - Reinicie o app

3. **Reinicie o app**:
   - Pare o servidor (Ctrl+C)
   - Execute `python app.py` novamente
   - As novas questões serão carregadas automaticamente!

## 📊 Status Atual

- **247 questões** carregadas automaticamente
- **33 tópicos** encontrados
- **2 tipos** de questões: Múltipla Escolha e Verdadeiro/Falso

## 🎯 Exemplo Real

O tópico `arquitetura/01_ARQUITETURA_VS_PADRAO` tem:
- 5 questões de alternativas (de `PROVA_ALTERNATIVAS.md`)
- 5 questões V/F (de `PROVA_VF.md`)
- Total: 10 questões carregadas automaticamente

Tudo isso sem precisar alterar código Python! 🚀

