# Prova: ARQUITETURA EM CAMADAS

## Provas de Alternativas

## Questão 1 (Múltipla Escolha)
Quais são as três camadas principais da arquitetura em camadas?

a) Frontend, Backend, Database
b) Apresentação, Negócio, Acesso a Dados
c) Model, View, Controller
d) Cliente, Servidor, API

**Resposta:** b) Apresentação, Negócio, Acesso a Dados

---

## Questão 2 (Múltipla Escolha)
Quantas camadas geralmente compõem uma arquitetura em camadas típica?

a) 2
b) 3
c) 4
d) Pode variar

**Resposta:** d) Pode variar, mas geralmente 3 (Apresentação, Negócio, Dados)

---

## Questão 3 (Múltipla Escolha)
Qual camada é responsável pela validação de dados?

a) Apresentação
b) Negócio
c) Dados
d) Todas

**Resposta:** b) Negócio - a camada de negócio deve validar regras de negócio.

---

## Questão 4 (Múltipla Escolha)
Qual camada é responsável pela interface do usuário?

a) Apresentação
b) Negócio
c) Dados
d) Servidor

**Resposta:** a) Apresentação - camada de apresentação lida com UI e API endpoints

---

## Questão 5 (Múltipla Escolha)
Qual camada é responsável pela persistência de dados?

a) Apresentação
b) Negócio
c) Acesso a Dados
d) Servidor

**Resposta:** c) Acesso a Dados - camada de acesso a dados lida com banco de dados

---

## Questão 6 (Múltipla Escolha)
Qual é uma vantagem da arquitetura em camadas?

a) Separação clara de responsabilidades
b) Fácil manutenção e teste
c) Permite reutilização de código
d) Todas as alternativas acima

**Resposta:** d) Todas as alternativas acima

---

## Questão 7 (Múltipla Escolha)
Qual é uma desvantagem da arquitetura em camadas?

a) Pode adicionar latência por camadas
b) Pode ser complexo para aplicações simples
c) Pode dificultar otimizações cross-layer
d) Todas as alternativas acima

**Resposta:** d) Todas as alternativas acima

---

## Questão 8 (Múltipla Escolha)
Na arquitetura em camadas, qual camada pode acessar qual camada?

a) Apresentação pode acessar diretamente Dados
b) Cada camada só conhece a camada abaixo dela
c) Todas as camadas podem acessar todas
d) Dados pode acessar Apresentação

**Resposta:** b) Cada camada só conhece a camada abaixo dela - hierarquia de acesso

---

## Questão 9 (Múltipla Escolha)
A arquitetura em camadas permite:

a) Trocar banco de dados sem alterar código de negócio
b) Testar camadas independentemente
c) Reutilizar código de negócio
d) Todas as alternativas acima

**Resposta:** d) Todas as alternativas acima

---

## Questão 10 (Múltipla Escolha)
Qual camada contém as regras de negócio?

a) Apresentação
b) Negócio
c) Dados
d) Servidor

**Resposta:** b) Negócio - camada de negócio contém regras de negócio e lógica de processamento