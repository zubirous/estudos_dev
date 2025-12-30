# Prova: RENDERIZAÇÃO - Next.js

## Provas de Verdadeiro ou Falso

## Questão 1 (Verdadeiro/Falso)
SSG é sempre mais rápido que SSR.

**Resposta:** Verdadeiro. SSG gera páginas no build, então é servido como arquivo estático, sendo mais rápido que SSR que processa a cada requisição.

---

## Questão 2 (Verdadeiro/Falso)
getStaticProps executa no build time.

**Resposta:** Verdadeiro. getStaticProps executa apenas durante o build para gerar páginas estáticas.

---

## Questão 3 (Verdadeiro/Falso)
getServerSideProps executa a cada requisição.

**Resposta:** Verdadeiro. getServerSideProps executa no servidor a cada requisição, gerando conteúdo dinâmico.

---

## Questão 4 (Verdadeiro/Falso)
ISR permite regenerar páginas estáticas sem rebuild completo.

**Resposta:** Verdadeiro. ISR permite regeneração incremental de páginas estáticas em background sem rebuild completo.

---

## Questão 5 (Verdadeiro/Falso)
SSG é melhor para dados que mudam a cada requisição.

**Resposta:** Falso. SSG gera páginas no build, então dados ficam desatualizados até rebuild. Use SSR para dados que mudam a cada requisição.

---

## Questão 6 (Verdadeiro/Falso)
getStaticPaths é necessário para rotas dinâmicas com SSG.

**Resposta:** Verdadeiro. getStaticPaths define quais rotas dinâmicas devem ser geradas no build quando usando SSG.

---

## Questão 7 (Verdadeiro/Falso)
ISR combina velocidade de SSG com atualização de SSR.

**Resposta:** Verdadeiro. ISR gera páginas estáticas (rápidas como SSG) mas revalida periodicamente em background (atualizado como SSR).