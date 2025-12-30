# Prova: ROTEAMENTO - Next.js

## Provas de Verdadeiro ou Falso

## Questão 1 (Verdadeiro/Falso)
Rotas aninhadas no Next.js usam a mesma pasta para criar sub-rotas.

**Resposta:** Verdadeiro. Criando uma pasta com o mesmo nome da rota e colocando index.js dentro cria uma sub-rota.

---

## Questão 2 (Verdadeiro/Falso)
Rotas dinâmicas são geradas no build time.

**Resposta:** Falso. Rotas dinâmicas são geradas em runtime ou via getStaticPaths.

---

## Questão 3 (Verdadeiro/Falso)
O Next.js usa file-based routing, onde cada arquivo em pages/ vira uma rota.

**Resposta:** Verdadeiro. O Next.js usa file-based routing, onde cada arquivo em pages/ automaticamente vira uma rota.

---

## Questão 4 (Verdadeiro/Falso)
O componente Link do Next.js requer tag <a> dentro dele.

**Resposta:** Falso. Em versões antigas sim, mas nas versões mais recentes não é necessário. O Link pode envolver qualquer elemento.

---

## Questão 5 (Verdadeiro/Falso)
useRouter pode ser usado para navegação programática no Next.js.

**Resposta:** Verdadeiro. useRouter fornece métodos como push(), replace(), back() para navegação programática.

---

## Questão 6 (Verdadeiro/Falso)
Rotas catch-all [...slug].js capturam múltiplos segmentos de URL.

**Resposta:** Verdadeiro. Catch-all [...slug].js captura todos os segmentos após a rota base e retorna como array.

---

## Questão 7 (Verdadeiro/Falso)
Rotas catch-all opcionais [[...slug]].js também capturam a rota sem parâmetros.

**Resposta:** Verdadeiro. Catch-all opcional [[...slug]].js captura a rota com ou sem parâmetros.

---

## Questão 8 (Verdadeiro/Falso)
O arquivo pages/index.js cria a rota /index no Next.js.

**Resposta:** Falso. pages/index.js cria a rota raiz (/), não /index.

---

## Questão 9 (Verdadeiro/Falso)
useRouter().query retorna os parâmetros da rota dinâmica.

**Resposta:** Verdadeiro. useRouter().query retorna um objeto com os parâmetros da rota dinâmica.