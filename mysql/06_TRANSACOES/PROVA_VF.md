# Prova: TRANSAÇÕES - MySQL

## Provas de Verdadeiro ou Falso

## Questão 1 (Verdadeiro/Falso)
ROLLBACK desfaz todas as mudanças de uma transação.

**Resposta:** Verdadeiro. ROLLBACK cancela todas as mudanças da transação atual.

---

## Questão 2 (Verdadeiro/Falso)
COMMIT salva permanentemente as mudanças de uma transação.

**Resposta:** Verdadeiro. COMMIT confirma e salva permanentemente as mudanças.

---

## Questão 3 (Verdadeiro/Falso)
Atomicidade significa que todas as operações da transação devem ser executadas ou nenhuma.

**Resposta:** Verdadeiro. Atomicidade garante "tudo ou nada" - ou todas operações executam ou nenhuma.

---

## Questão 4 (Verdadeiro/Falso)
READ UNCOMMITTED é o nível de isolamento mais seguro.

**Resposta:** Falso. READ UNCOMMITTED é o nível com menos isolamento (menos seguro). SERIALIZABLE é o mais seguro.

---

## Questão 5 (Verdadeiro/Falso)
Isolamento garante que transações não interferem umas nas outras.

**Resposta:** Verdadeiro. Isolamento garante que transações concorrentes não interferem entre si.

---

## Questão 6 (Verdadeiro/Falso)
Consistência garante que o banco sempre está em estado válido.

**Resposta:** Verdadeiro. Consistência garante que o banco sempre mantém estado válido após cada transação.

---

## Questão 7 (Verdadeiro/Falso)
Durabilidade garante que mudanças confirmadas são permanentes mesmo em caso de falha.

**Resposta:** Verdadeiro. Durabilidade garante que transações confirmadas (COMMIT) persistem mesmo após falhas do sistema.

---

## Questão 8 (Verdadeiro/Falso)
REPEATABLE READ é o nível de isolamento padrão do MySQL InnoDB.

**Resposta:** Verdadeiro. REPEATABLE READ é o nível de isolamento padrão do MySQL InnoDB, oferecendo bom equilíbrio entre consistência e performance.

---

## Questão 9 (Verdadeiro/Falso)
Transações só funcionam com engines que suportam, como InnoDB no MySQL.

**Resposta:** Verdadeiro. Transações só funcionam com engines que suportam (InnoDB no MySQL). MyISAM não suporta transações.

---

## Questão 10 (Verdadeiro/Falso)
SAVEPOINT permite fazer rollback parcial dentro de uma transação.

**Resposta:** Verdadeiro. SAVEPOINT cria pontos de salvamento que permitem fazer ROLLBACK TO para voltar a um ponto específico sem desfazer toda a transação.

---

## Questão 11 (Verdadeiro/Falso)
READ COMMITTED evita dirty reads mas pode ter non-repeatable reads.

**Resposta:** Verdadeiro. READ COMMITTED lê apenas dados commitados (evita dirty reads), mas pode ter non-repeatable reads (leituras repetidas podem retornar valores diferentes).

---

## Questão 12 (Verdadeiro/Falso)
SERIALIZABLE é o nível de isolamento mais rápido.

**Resposta:** Falso. SERIALIZABLE é o nível de isolamento mais lento, pois executa transações como se fossem sequenciais. READ UNCOMMITTED é o mais rápido.

