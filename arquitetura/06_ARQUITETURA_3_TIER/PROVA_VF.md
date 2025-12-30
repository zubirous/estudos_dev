# Prova: ARQUITETURA 3-TIER

## Provas de Verdadeiro ou Falso

## Questão 1 (Verdadeiro/Falso)
Na arquitetura 3-Tier, cada camada só conhece a camada abaixo dela.

**Resposta:** Verdadeiro. Esta é a regra fundamental da arquitetura em camadas - cada camada só conhece a camada imediatamente abaixo.

---

## Questão 2 (Verdadeiro/Falso)
Na arquitetura 3-Tier, a camada de Apresentação pode acessar diretamente a camada de Acesso a Dados.

**Resposta:** Falso. A camada de Apresentação só pode acessar a camada de Negócio, que por sua vez acessa a camada de Acesso a Dados.

---

## Questão 3 (Verdadeiro/Falso)
A arquitetura 3-Tier facilita a manutenção e substituição de camadas.

**Resposta:** Verdadeiro. Como as camadas são independentes, você pode substituir uma camada (ex: trocar banco de dados) sem afetar outras.

---

## Questão 4 (Verdadeiro/Falso)
A camada de Negócio contém regras de negócio e lógica de validação.

**Resposta:** Verdadeiro. A camada de Negócio (Business Logic Layer) contém todas as regras de negócio e validações.

---

## Questão 5 (Verdadeiro/Falso)
A arquitetura 3-Tier é também chamada de arquitetura em camadas (Layered Architecture).

**Resposta:** Verdadeiro. Arquitetura 3-Tier é um tipo de arquitetura em camadas com três camadas principais.

---

## Questão 6 (Verdadeiro/Falso)
Na arquitetura 3-Tier, você pode trocar o banco de dados sem alterar a camada de negócio.

**Resposta:** Verdadeiro. Como cada camada só conhece a camada abaixo, trocar banco de dados (camada de dados) não afeta camada de negócio.

---

## Questão 7 (Verdadeiro/Falso)
A arquitetura 3-Tier permite escalar camadas independentemente.

**Resposta:** Verdadeiro. Você pode escalar a camada de apresentação (servidores web) independentemente da camada de dados (servidores de banco), por exemplo.

---

## Questão 8 (Verdadeiro/Falso)
Na arquitetura 3-Tier, a camada de apresentação pode acessar diretamente o banco de dados.

**Resposta:** Falso. A camada de apresentação só pode acessar a camada de negócio, que por sua vez acessa a camada de dados.

