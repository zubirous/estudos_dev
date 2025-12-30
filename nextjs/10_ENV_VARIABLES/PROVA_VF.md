# Prova: ENVIRONMENT VARIABLES - Next.js

## Provas de Verdadeiro ou Falso

## Questão 1 (Verdadeiro/Falso)
Variáveis sem NEXT_PUBLIC_ são acessíveis no cliente.

**Resposta:** Falso. Variáveis sem NEXT_PUBLIC_ são acessíveis apenas no servidor.

---

## Questão 2 (Verdadeiro/Falso)
Variáveis com NEXT_PUBLIC_ são expostas ao cliente.

**Resposta:** Verdadeiro. Variáveis com prefixo NEXT_PUBLIC_ são expostas ao cliente e podem ser acessadas no navegador.

---

## Questão 3 (Verdadeiro/Falso)
É seguro expor chaves secretas com NEXT_PUBLIC_.

**Resposta:** Falso. Nunca exponha chaves secretas com NEXT_PUBLIC_ porque código JavaScript no cliente é visível para qualquer pessoa.

---

## Questão 4 (Verdadeiro/Falso)
Variáveis de ambiente podem ser usadas em API routes do Next.js.

**Resposta:** Verdadeiro. Variáveis de ambiente (com ou sem NEXT_PUBLIC_) podem ser usadas em API routes, que executam no servidor.

---

## Questão 5 (Verdadeiro/Falso)
O arquivo .env.local é commitado no git.

**Resposta:** Falso. .env.local deve ser adicionado ao .gitignore e não deve ser commitado, pois contém informações sensíveis específicas do ambiente local.

---

## Questão 6 (Verdadeiro/Falso)
Variáveis privadas podem ser usadas em getServerSideProps.

**Resposta:** Verdadeiro. getServerSideProps executa no servidor, então pode usar variáveis privadas (sem NEXT_PUBLIC_).

---

## Questão 7 (Verdadeiro/Falso)
Variáveis privadas podem ser usadas em componentes do cliente.

**Resposta:** Falso. Variáveis privadas (sem NEXT_PUBLIC_) não são acessíveis em componentes do cliente que executam no navegador.

---

## Questão 8 (Verdadeiro/Falso)
Variáveis de ambiente são acessadas via process.env no Next.js.

**Resposta:** Verdadeiro. Variáveis de ambiente são acessadas via process.env.VARIAVEL no Next.js, similar ao Node.js.
