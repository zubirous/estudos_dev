# Prova: ARQUITETURA EM CAMADAS

## Provas de Verdadeiro ou Falso

## Questão 1 (Verdadeiro/Falso)
Camadas podem pular a camada adjacente e acessar diretamente outras camadas.

**Resposta:** Falso. Camadas devem seguir uma hierarquia e só podem acessar a camada imediatamente abaixo.

---

## Questão 2 (Verdadeiro/Falso)
A arquitetura em camadas permite fácil substituição de uma camada sem afetar outras.

**Resposta:** Verdadeiro. Uma das vantagens é que você pode trocar a camada de dados (ex: MySQL para PostgreSQL) sem alterar a camada de negócio.

---

## Questão 3 (Verdadeiro/Falso)
Na arquitetura em camadas, a camada de Apresentação pode acessar diretamente a camada de Dados.

**Resposta:** Falso. Cada camada só pode acessar a camada imediatamente abaixo dela. Apresentação acessa Negócio, que acessa Dados.

---

## Questão 4 (Verdadeiro/Falso)
A camada de Negócio é responsável pela validação de dados e regras de negócio.

**Resposta:** Verdadeiro. A camada de Negócio contém regras de negócio, validação de dados e lógica de processamento.

---

## Questão 5 (Verdadeiro/Falso)
A arquitetura em camadas pode adicionar latência devido à comunicação entre camadas.

**Resposta:** Verdadeiro. Uma desvantagem é que a comunicação entre camadas pode adicionar overhead e latência.

---

## Questão 6 (Verdadeiro/Falso)
A arquitetura em camadas facilita testes, pois cada camada pode ser testada independentemente.

**Resposta:** Verdadeiro. Uma das vantagens é que cada camada pode ser testada isoladamente, facilitando testes unitários e de integração.

---

## Questão 7 (Verdadeiro/Falso)
A camada de Acesso a Dados contém regras de negócio.

**Resposta:** Falso. A camada de Acesso a Dados apenas lida com persistência (banco de dados). Regras de negócio ficam na camada de Negócio.

---

## Questão 8 (Verdadeiro/Falso)
A arquitetura em camadas é sempre melhor que outras arquiteturas.

**Resposta:** Falso. Arquitetura em camadas tem vantagens e desvantagens. Para aplicações simples, pode adicionar complexidade desnecessária.