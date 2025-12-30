# Prova: DATA FETCHING - Next.js

## Provas de Verdadeiro ou Falso

## Questão 1 (Verdadeiro/Falso)
getStaticProps executa no build time.

**Resposta:** Verdadeiro. getStaticProps executa apenas durante o build, gerando páginas estáticas.

---

## Questão 2 (Verdadeiro/Falso)
getServerSideProps executa a cada requisição.

**Resposta:** Verdadeiro. getServerSideProps executa no servidor a cada requisição, gerando conteúdo dinâmico.

---

## Questão 3 (Verdadeiro/Falso)
ISR permite regenerar páginas estáticas sem rebuild completo.

**Resposta:** Verdadeiro. ISR (Incremental Static Regeneration) permite regenerar páginas estáticas em background.

---

## Questão 4 (Verdadeiro/Falso)
useEffect deve ser usado para dados que afetam SEO.

**Resposta:** Falso. useEffect executa no cliente após renderização, então não afeta SEO. Use getStaticProps ou getServerSideProps para SEO.

---

## Questão 5 (Verdadeiro/Falso)
getStaticProps é mais rápido que getServerSideProps.

**Resposta:** Verdadeiro. getStaticProps gera páginas no build (estáticas), então é servido como arquivo estático, sendo mais rápido que getServerSideProps que processa a cada requisição.

---

## Questão 6 (Verdadeiro/Falso)
ISR combina velocidade de SSG com atualização de SSR.

**Resposta:** Verdadeiro. ISR gera páginas estáticas no build (rápidas) mas revalida periodicamente em background (atualizado).

---

## Questão 7 (Verdadeiro/Falso)
getStaticPaths é necessário para páginas estáticas dinâmicas.

**Resposta:** Verdadeiro. getStaticPaths define quais rotas devem ser geradas estaticamente em build time.

