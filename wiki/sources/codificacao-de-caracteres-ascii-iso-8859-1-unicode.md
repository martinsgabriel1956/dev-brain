---
type: source
title: "Codificação de Caracteres: ASCII, ISO-8859-1 e Unicode"
aliases: ["aula codificação de caracteres", "professor olibário codificação", "exercício decode ascii beca"]
date_created: 2026-07-31
date_updated: 2026-07-31
source_count: 0
tags: [ascii, iso-8859-1, latin-1, unicode, charset, encoding, cs-fundamentals, aula]
skill: cs-fundamentals
status: stable
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/codificacao-de-caracteres-ascii-iso-8859-1-unicode.md"
source_url: ""
author: "Professor Olibário"
date_published: ""
date_ingested: "2026-07-31"
---

## TL;DR

Aula curta (transcrição em português, sem necessidade de tradução) do professor Olibário sobre codificação de caracteres: por que ASCII usa só 7 dos 8 bits disponíveis (128 valores, 0–127), suas limitações (sem acentos, sem alfabetos não latinos), a ISO-8859-1/Latin-1 como extensão de 8 bits totalmente compatível com ASCII até 127 e que acrescenta caracteres acentuados (0–255), e a Unicode como charset universal (8 a 32 bits, UTF-8 como encoding mais comum na web). Fecha com um exercício de decodificação manual de uma mensagem de 4 bytes ASCII (`66 69 67 65` → "BECA"), demonstrando a contiguidade do alfabeto na tabela a partir do 65 (`A`).

---

## Claims Principais

### 1. ASCII usa 8 bits de armazenamento, mas só 7 são dados — o primeiro é bit de verificação
**Evidência:** O professor descreve a tabela ASCII como usando 1 byte (8 bits) por símbolo, mas apenas 7 bits efetivamente compõem o valor do caractere; o bit restante é tratado como bit de verificação/paridade.
**Confidence:** Média-alta — consistente com a origem histórica do ASCII (7-bit code, bit extra usado para paridade em transmissão serial), mas é uma simplificação didática: a wiki já documenta em [[wiki/concepts/ascii]] que ASCII moderno é tratado como charset de 128 valores (0–127) que cabe integralmente em 1 byte, sem necessariamente enquadrar o 8º bit como "verificação" em todo contexto de uso atual (ex.: em UTF-8, esse bit é o que distingue ASCII de bytes de continuação multi-byte). Framing complementar, não contraditório.

### 2. 7 bits de dados limitam ASCII a 128 valores (0–127)
**Evidência:** `127` em binário é `1111111` (7 bits em 1), então o intervalo representável é `0` a `2^7 - 1`.
**Confidence:** Alta — matemática direta, já documentada em [[wiki/concepts/ascii]].

### 3. ASCII não contempla caracteres acentuados nem alfabetos não latinos
**Evidência:** O professor cita explicitamente árabe, chinês e japonês como exemplos de sistemas de escrita fora do alcance da tabela, e nota que por isso ASCII não é usado com frequência no Brasil (falta de acentos: á, ã, ç, etc.).
**Confidence:** Alta — já documentado em [[wiki/concepts/ascii]] ("Limitação: 128 Caracteres Não São Suficientes").

### 4. Os primeiros 32 valores da tabela ASCII (0–31, mais o 127) são caracteres de controle não imprimíveis
**Evidência:** Exemplos dados: caractere nulo (terminador de string em C), Esc, Backspace.
**Confidence:** Alta — consistente com a tabela ASCII padrão e com a estrutura já documentada em [[wiki/concepts/ascii]] (0–31 controle, 32–126 imprimíveis, 127 DEL).

### 5. Letras maiúsculas começam em 65 (`A`) e são contíguas na tabela ASCII
**Evidência:** Base do exercício de decodificação: `65=A, 66=B, 67=C, 68=D, 69=E`, com letras minúsculas vindo depois de um bloco de caracteres especiais.
**Confidence:** Alta — fato tabular direto, já usado como exemplo em [[wiki/concepts/ascii]] (tabela de mapeamento decimal/binário/caractere).

### 6. ISO-8859-1 (Latin-1) usa 8 bits completos e é idêntica a ASCII até 127
**Evidência:** Descrição direta: 8 bits (1 bit a mais que ASCII) dobra o espaço representável para 0–255; os primeiros 128 valores permanecem idênticos à tabela ASCII, e os 128 novos valores (128–255) incluem caracteres acentuados.
**Confidence:** Alta — consistente com a definição normativa de ISO/IEC 8859-1, e coerente com o princípio de retrocompatibilidade que a wiki já documenta para [[wiki/concepts/utf-8]] em relação ao ASCII (mesmo princípio, charset diferente).

### 7. Unicode usa de 8 a 32 bits (até 4 bytes) e cobre símbolos de todos os idiomas do mundo
**Evidência:** Descrição do professor de que Unicode escala até 4 bytes de informação por símbolo, e que UTF-8 é o encoding mais comum na web.
**Confidence:** Média-alta como resumo didático — a wiki já documenta com mais precisão em [[wiki/concepts/unicode]] que Unicode é o *charset* (espaço de codepoints U+0000–U+10FFFF) e que UTF-8/UTF-16/UTF-32 são os *encodings* que serializam esse charset em bytes; a aula não faz essa distinção charset/encoding explicitamente (chama Unicode de "codificação" e depois "UTF-8" como uma variante dela), o que é uma imprecisão terminológica frente ao que já está consolidado em [[wiki/concepts/charset]].

### 8. Exercício: a sequência de bytes `01000010 01000101 01000011 01000001` decodifica para "BECA" em ASCII
**Evidência:** Separando os 32 bits em 4 grupos de 8 e convertendo cada grupo para decimal: `66, 69, 67, 65` → `B, E, C, A` → "BECA", usando a contiguidade do alfabeto a partir do 65 (`A`).
**Confidence:** Alta — verificado pela aritmética binário-decimal-ASCII apresentada na própria aula; a transcrição automática degrada o final da frase (soa como "rebeca"), mas o resultado matematicamente consistente com os valores apresentados é "BECA", não "REBECA" — tratado como `[transcrição incerta]` no `raw/`, resolvido aqui pela lógica do exercício, não pela transcrição literal.

---

## Entidades Mencionadas

Nenhuma entidade nova relevante — o professor Olibário não tem página própria na wiki (aula avulsa, sem outras fontes ou menções cruzadas até o momento); não foi criada entidade para evitar stub órfão de baixo valor.

## Conceitos Tocados

- [[wiki/concepts/ascii]] — página já existente; esta fonte reforça a estrutura de bits (7 dados + 1 verificação) e a tabela de contiguidade alfabética usada no exercício
- [[wiki/concepts/charset]] — página já existente; a fonte ilustra na prática por que Unicode "por si só" (sem um encoding) não decodifica bytes
- [[wiki/concepts/unicode]] — página já existente; esta fonte contribui o framing didático (8–32 bits) e nota de imprecisão terminológica (Unicode tratado como "codificação" em vez de charset)
- [[wiki/concepts/utf-8]] — página já existente; mencionada como o encoding mais comum de Unicode na web
- **ISO-8859-1 (Latin-1)** — conceito novo, sem página própria até esta ingestão; criada como stub em `wiki/concepts/iso-8859-1-latin-1.md`

## Armadilhas Documentadas

1. **Confundir Unicode (charset) com UTF-8 (encoding)** — a aula usa "codificação" tanto para Unicode quanto para UTF-8 de forma intercambiável; a wiki já resolve essa ambiguidade em [[wiki/concepts/charset]] e [[wiki/concepts/unicode]] — vale a distinção ao estudar por esta fonte.
2. **Tratar o "bit de verificação" do ASCII como universal** — em contextos modernos (ex.: UTF-8), o oitavo bit de um byte ASCII é sempre `0` e serve para o decoder distinguir ASCII de bytes multi-byte — não é usado como paridade de transmissão na prática de armazenamento em memória atual. Ver [[wiki/concepts/ascii]] ("O Fast Path do ASCII num Decoder UTF-8").
3. **Transcrição degradada no fechamento do exercício** — a palavra final soa como "rebeca" na transcrição automática, mas a decodificação correta dos valores apresentados na aula é "BECA"; resolvido pela aritmética, não pela transcrição literal.

## Contradições / Questões Abertas

Nenhuma contradição encontrada contra páginas já existentes na wiki — esta fonte é consistente com [[wiki/concepts/ascii]], [[wiki/concepts/charset]] e [[wiki/concepts/unicode]], e introduz apenas o conceito novo de ISO-8859-1/Latin-1, ainda não coberto.
