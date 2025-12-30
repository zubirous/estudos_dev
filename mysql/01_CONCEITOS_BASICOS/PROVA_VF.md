# Prova: CONCEITOS BÁSICOS - MySQL

## Provas de Verdadeiro ou Falso

## Questão 1 (Verdadeiro/Falso)
Uma Chave Primária pode ter valores NULL.

**Resposta:** Falso. Chave Primária NÃO pode ser NULL.


---

## Questão 2 (Verdadeiro/Falso)
VARCHAR(100) sempre ocupa 100 bytes no banco de dados.

**Resposta:** Falso. VARCHAR usa apenas o espaço necessário. Se você armazenar "João" (4 caracteres), ocupará menos de 100 bytes.


---

## Questão 3 (Verdadeiro/Falso)
Um campo do tipo BOOLEAN no MySQL armazena valores TRUE/FALSE diretamente.

**Resposta:** Falso. BOOLEAN é armazenado como TINYINT(1), onde 0=FALSE e 1=TRUE.


---

## Questão 4 (Verdadeiro/Falso)
O tipo TEXT pode armazenar até 65.535 caracteres.

**Resposta:** Verdadeiro. TEXT armazena até 65.535 bytes de texto.

---

## Questão 5 (Verdadeiro/Falso)
Um campo INT pode armazenar valores negativos.

**Resposta:** Verdadeiro. INT armazena valores de -2.147.483.648 a 2.147.483.647.

---

## Questão 6 (Verdadeiro/Falso)
DECIMAL é mais preciso que FLOAT para valores monetários.

**Resposta:** Verdadeiro. DECIMAL oferece precisão exata, enquanto FLOAT é aproximado. Use DECIMAL para valores monetários.

---

## Questão 7 (Verdadeiro/Falso)
CHAR(10) sempre ocupa 10 bytes, independente do valor armazenado.

**Resposta:** Verdadeiro. CHAR tem tamanho fixo, então CHAR(10) sempre ocupa 10 bytes (ou caracteres), preenchendo com espaços se necessário.

---

## Questão 8 (Verdadeiro/Falso)
ENUM é mais eficiente que VARCHAR para valores fixos.

**Resposta:** Verdadeiro. ENUM é mais eficiente em armazenamento e validação automática, mas menos flexível que VARCHAR.

---

## Questão 9 (Verdadeiro/Falso)
Um campo DATE armazena data e hora.

**Resposta:** Falso. DATE armazena apenas data (YYYY-MM-DD). Para data e hora, use DATETIME ou TIMESTAMP.

---

## Questão 10 (Verdadeiro/Falso)
Chave primária automaticamente cria um índice.

**Resposta:** Verdadeiro. Chave primária automaticamente cria um índice para busca rápida.