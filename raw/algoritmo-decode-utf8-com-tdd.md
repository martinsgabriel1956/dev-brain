# Como Transformar um Slice de Bytes em uma String Utilizando o Encode UTF-8

**Formato:** Transcrição de vídeo (YouTube)
**Idioma original:** Português (BR)
**Data de transcrição:** 2026-07-22
**Linguagem de código usada nos exemplos:** Go
**Vídeo relacionado:** continuação direta de "Como Strings Realmente Funcionam (por Baixo dos Panos)" — no final daquele vídeo o autor perguntou se o público queria um vídeo explicando como implementar, de fato, um algoritmo de encode/decode UTF-8. Este vídeo é a resposta a esse pedido.

> **Nota de precisão:** apesar do título dizer "encode", a função efetivamente implementada no vídeo é um **decoder** — ela recebe um slice de bytes e devolve a runa (codepoint) que esses bytes representam. Em terminologia UTF-8, *encode* é o sentido runa → bytes; *decode* é bytes → runa. O conteúdo abaixo preserva a linguagem usada pelo autor, mas a função construída é `DecodeRune`.

---

## Introdução

O autor já fez um vídeo no canal explicando o que é uma string e como ela funciona por baixo dos panos (linkado como vídeo anterior/relacionado). Ao final daquele vídeo, perguntou ao público se valeria a pena fazer um vídeo mostrando como criar, na prática, um algoritmo de encode/decode de uma string em UTF-8. Muitas pessoas pediram — daí este vídeo.

**Aviso do autor:** por ser um vídeo bem técnico, o engajamento tende a ser mais baixo — pedido explícito de like, inscrição e comentários para ajudar o canal.

### Disclaimer sobre o algoritmo

O algoritmo implementado é **intencionalmente básico**, para favorecer entendimento sobre o padrão UTF-8. Existem formas mais eficientes de implementar esse encoding — inclusive versões *branchless*. O objetivo aqui não é performance, é um algoritmo que:

- funciona;
- passa em todos os testes;
- é possível de ler e entender o funcionamento do padrão UTF-8 olhando para o código.

---

## Por Que TDD Faz Sentido Aqui

O autor já fez um vídeo sobre testes onde defende que **TDD funciona muito bem quando você já sabe qual é a interface, qual é o input e qual é o output esperado** — e esse é exatamente o caso de implementar um algoritmo de decode UTF-8: a especificação (RFC) já define entrada e saída esperadas.

### Importando os testes da standard library de Go como oráculo

Em vez de escrever os testes do zero — o que arriscaria deixar de fora edge cases importantes — o autor **copiou os testes do pacote `unicode/utf8` da standard library de Go** e os adaptou (o código final não é 100% idêntico ao da stdlib, então alguns ajustes foram necessários).

Vantagens dessa abordagem:

- os testes da stdlib já cobrem sequências de bytes **inválidas** (edge cases difíceis de imaginar do zero);
- os testes cobrem também strings **válidas** com bastante caracteres especiais, exercitando a implementação em casos complexos;
- se o código passar em todos os testes da stdlib de Go, é um forte indício de que a implementação está correta e robusta.

Como em todo ciclo TDD (RED → GREEN → REFACTOR), a primeira execução dos testes — antes mesmo da função existir — falha propositalmente. Essa é a confirmação de que os testes estão de fato testando algo.

---

## A Função

```go
func DecodeRune(b []byte) (rune, int, error) {
    // implementação
}
```

- **Input:** um slice de bytes (`[]byte`).
- **Output:**
  1. a **runa** decodificada a partir desse slice;
  2. o **tamanho** (`size`), em bytes, que essa runa consumiu do input;
  3. um **erro**, caso a sequência de bytes seja inválida.

**Observação do autor:** fazer o *decode* é muito mais simples do que **validar** se o input é um UTF-8 válido — a validação é a parte realmente complexa do algoritmo.

---

## Ponto de Partida: a Especificação (RFC)

A implementação parte diretamente da especificação do UTF-8 (RFC 3629, referenciada no vídeo como "RFC UTF-8" — pesquisável no Google). O RFC é descrito como curto e enxuto, valendo a leitura.

A peça central da RFC usada no vídeo é a tabela que define como caracteres de 1, 2, 3 e 4 bytes são codificados:

```
Char. number range  |        UTF-8 octet sequence
(hexadecimal)        |              (binary)
--------------------------------------------------------
0000 0000-0000 007F  | 0xxxxxxx
0000 0080-0000 07FF  | 110xxxxx 10xxxxxx
0000 0800-0000 FFFF  | 1110xxxx 10xxxxxx 10xxxxxx
0001 0000-0010 FFFF  | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
```

Essa tabela é colada como comentário no código, já que o autor volta a consultá-la o tempo todo durante a implementação.

---

## Passo 1 — O Primeiro Byte Decide Tudo

A implementação sempre começa lendo o **primeiro byte** do input (`b0`), porque é ele que determina quantos bytes (1 a 4) formam o caractere.

### Validação: input vazio

Antes de indexar `b[0]`, é preciso validar que o input não é vazio — senão a indexação gera um pânico em tempo de execução.

```go
if len(b) == 0 {
    return 0, 0, errors.New("empty input")
}

b0 := b[0]
```

### Caso 1 — Caracteres ASCII (1 byte)

UTF-8 é 100% compatível com ASCII: os 128 primeiros caracteres (valores 0–127, ou `0x00`–`0x7F`) são caracteres ASCII de 1 byte. Se `b0 < 0x80`, o byte já é a runa completa — não é preciso nenhuma conta:

```go
switch {
case b0 < 0x80: // ASCII
    return rune(b0), 1, nil
}
```

Nesse ponto o código já compila; os testes ainda falham (esperado — a função só cobre ASCII).

---

## Passo 2 — Bitwise Operations: AND, OR e Left Shift

Para detectar e decodificar caracteres multi-byte, o autor usa três operações bit a bit:

- **AND (`&`)** — bit resultante é `1` somente se **ambos** os bits forem `1`. Usado para "zerar" bits que não interessam e para checar se bits específicos estão setados.
- **OR (`|`)** — bit resultante é `1` se **pelo menos um** dos bits for `1`. Usado para juntar/mesclar bits de fontes diferentes num único valor.
- **Left shift (`<<`)** — desloca todos os bits para a esquerda N casas, abrindo espaço (preenchido com zero) à direita. Usado para "dar espaço" para os bits do próximo byte antes de fazer o OR.

### Detectando o comprimento do caractere pelo primeiro byte

Pela tabela do RFC:

| Prefixo do 1º byte | Significado |
|---|---|
| `0xxxxxxx` | 1 byte (ASCII) |
| `110xxxxx` | 2 bytes |
| `1110xxxx` | 3 bytes |
| `11110xxx` | 4 bytes |

Para checar se `b0` começa com `110`, a lógica é: zerar todos os bits que não importam (fazendo AND com `0`) e comparar os bits relevantes com `1`. Isso equivale a fazer:

```go
b0 & 0xE0 == 0xC0   // caractere de 2 bytes: prefixo 110xxxxx
b0 & 0xF0 == 0xE0   // caractere de 3 bytes: prefixo 1110xxxx
b0 & 0xF8 == 0xF0   // caractere de 4 bytes: prefixo 11110xxx
```

O autor recomenda usar uma ferramenta online de conversão binário → hexadecimal para chegar nesses valores (`0xE0`, `0xC0`, `0xF0`, `0xF8`), preferência pessoal por hexadecimal em vez de decimal ao trabalhar com binário.

```go
switch {
case b0 < 0x80: // ASCII — 1 byte
    return rune(b0), 1, nil
case b0&0xE0 == 0xC0: // 2 bytes
    // size = 2
case b0&0xF0 == 0xE0: // 3 bytes
    // size = 3
case b0&0xF8 == 0xF0: // 4 bytes
    // size = 4
}
```

---

## Passo 3 — Montando a Runa (Descartar os Bits de Tamanho, Juntar os Bits de Dados)

Segundo o RFC, os bits marcados como `x` na tabela são os únicos que fazem parte do caractere de fato — os bits de prefixo (que indicam o tamanho) precisam ser descartados.

Uma `rune` em Go ocupa 32 bits (4 bytes) e consegue representar qualquer codepoint Unicode. Quando um `byte` é convertido para `rune`, o Go preenche os bits mais significativos com zero e preserva os bits do byte original nos bits menos significativos.

### Caractere de 2 bytes

1. Descartar os 3 bits de prefixo do primeiro byte com AND `0x1F` (mantém os 5 bits de dados):
   ```go
   r := rune(b0) & 0x1F
   ```
2. Abrir espaço para os 6 bits de dados do segundo byte com um left shift de 6 casas:
   ```go
   r = r << 6
   ```
3. Extrair os 6 bits de dados do segundo byte (`b1`) descartando o prefixo `10` com AND `0x3F`:
   ```go
   data := rune(b[1]) & 0x3F
   ```
4. Juntar os dois grupos de bits com OR:
   ```go
   r = r | data
   ```

Antes disso, é preciso validar que o input tem pelo menos 2 bytes (senão indexar `b[1]` gera pânico):

```go
if len(b) < 2 {
    return 0, 0, errors.New("invalid length")
}
```

### Caractere de 3 bytes

Mesma lógica, com três grupos de bits:

```go
if len(b) < 3 {
    return 0, 0, errors.New("invalid length")
}

r := rune(b0) & 0x0F
r = (r << 12) |
    ((rune(b[1]) & 0x3F) << 6) |
    (rune(b[2]) & 0x3F)
```

### Caractere de 4 bytes

```go
if len(b) < 4 {
    return 0, 0, errors.New("invalid length")
}

r := rune(b0) & 0x07
r = (r << 18) |
    ((rune(b[1]) & 0x3F) << 12) |
    ((rune(b[2]) & 0x3F) << 6) |
    (rune(b[3]) & 0x3F)
```

Nesse ponto, rodando **apenas os testes de strings válidas** (o autor testa separadamente, porque validar input inválido é ordens de magnitude mais difícil do que decodificar input válido), todos passam.

---

## Passo 4 — Validando Input Inválido

Com o "caminho feliz" funcionando, faltam as validações que tornam o decoder robusto contra UTF-8 malformado.

### 4.1 — Caso default (nenhum padrão bateu)

Se `b0` não bater com nenhum dos quatro prefixos válidos (`0xxxxxxx`, `110xxxxx`, `1110xxxx`, `11110xxx`), o input é inválido:

```go
default:
    return 0, 0, errors.New("invalid utf8")
```

### 4.2 — Surrogate pairs (proibidos em UTF-8)

O RFC proíbe explicitamente que os codepoints reservados para *surrogate pairs* de UTF-16 (`U+D800`–`U+DFFF`) apareçam como resultado de uma decodificação UTF-8:

```go
if r >= 0xD800 && r <= 0xDFFF {
    return 0, 0, errors.New("surrogate half")
}
```

### 4.3 — Bytes de continuação

Todo byte de continuação (o 2º, 3º ou 4º byte de um caractere multi-byte) **sempre** começa com o prefixo `10`. Nenhum outro tipo de byte começa com esse prefixo — logo, a presença desse prefixo é o que identifica um byte de continuação.

Checagem: `byte & 0xC0 == 0x80`.

Isso precisa ser validado tanto para "ainda tenho bytes suficientes e eles são bytes de continuação válidos" quanto para "um caractere ASCII (1 byte) não pode ser seguido por um byte de continuação solto":

```go
// Exemplo para ASCII: se o input tem mais de 1 byte e o próximo byte
// é um byte de continuação, algo está errado (haveria um byte de
// continuação "solto", sem um byte líder antes dele).
if len(b) > 1 && b[1]&0xC0 == 0x80 {
    return 0, 0, errors.New("invalid length")
}
```

Para os caracteres de 2, 3 e 4 bytes, cada byte de continuação (`b1`, `b2`, `b3` conforme o caso) precisa passar por essa mesma checagem:

```go
b1 := b[1]
if b1&0xC0 != 0x80 {
    return 0, 0, errors.New("invalid continuation byte")
}
```

Repetido para `b2` (caracteres de 3 e 4 bytes) e `b3` (caracteres de 4 bytes).

Depois dessas checagens, restam apenas **2 testes falhando** de toda a suite — e o autor relata ter gastado bastante tempo até entender a causa raiz. Não era um problema nos testes importados da stdlib; era um bug real no algoritmo.

### 4.4 — Overlong encoding

**Regra do UTF-8:** todo caractere deve ser codificado usando a **menor quantidade de bytes possível**. Codificar um caractere com mais bytes do que o necessário é chamado de **overlong encoding** e é proibido pelo padrão — mesmo que, bit a bit, a sequência "pareça" um UTF-8 válido.

Exemplo didático dado no vídeo: o caractere `A` (decimal 65) cabe em 1 byte ASCII. Mas nada impediria, mecanicamente, de codificá-lo como uma sequência de 2 bytes (`110xxxxx 10xxxxxx`) preenchendo os bits de dados com o mesmo valor 65. Rodando o algoritmo de decode nessa sequência "forçada", o resultado seria corretamente o codepoint 65 (`A`) — só que essa forma de codificação é overlong e precisa ser rejeitada.

**Caso ASCII (1 byte):** não há o que validar — não existe forma mais curta que 1 byte.

**Caso 2 bytes:** o menor codepoint que exige 2 bytes é 128 (`0x80`). Se a runa decodificada for menor que isso, houve overlong:

```go
if r < 0x80 {
    return 0, 0, errors.New("overlong encoding")
}
```

**Caso 3 e 4 bytes — a parte mais difícil:** checar só o valor final da runa não basta de forma genérica; o autor usa uma checagem específica sobre o **segundo byte**, condicionada ao valor do **primeiro byte**:

```go
// 3 bytes: o menor primeiro byte possível é 0xE0. Quando b0 == 0xE0,
// o segundo byte tem que ser >= 0xA0 — do contrário, o caractere
// poderia ter sido representado com apenas 2 bytes.
if b0 == 0xE0 && b1 < 0xA0 {
    return 0, 0, errors.New("overlong encoding")
}
```

Justificativa: o primeiro codepoint que realmente precisa de 3 bytes é `U+0800`, cuja codificação UTF-8 é `E0 A0 80`. Qualquer sequência começando com `E0` cujo segundo byte seja menor que `A0` representa um codepoint que caberia em 2 bytes — logo, overlong.

A mesma lógica se aplica ao caso de 4 bytes (checagem análoga sobre `b0 == 0xF0` e o valor mínimo do segundo byte).

### 4.5 — Codepoint máximo do Unicode

Depois de resolver o overlong, ainda restava 1 teste falhando — e essa foi a parte que mais tempo tomou do autor para diagnosticar. Unicode tem um valor mínimo (0, o caractere NUL) e um **valor máximo**: `U+10FFFF`. Qualquer runa decodificada acima desse valor é inválida:

```go
if r > 0x10FFFF {
    return 0, 0, errors.New("character too large")
}
```

Com essa última checagem, **todos os testes passam** — incluindo a suite inteira importada da standard library de Go.

---

## Resultado Final

O algoritmo final:

1. Lê o primeiro byte (`b0`) e valida que o input não é vazio.
2. Usa AND com máscaras (`0xE0`, `0xF0`, `0xF8`) para detectar se o caractere é de 1, 2, 3 ou 4 bytes a partir do prefixo de `b0`.
3. Valida o comprimento do slice antes de indexar cada byte de continuação.
4. Valida que cada byte de continuação segue o padrão `10xxxxxx` (AND com `0xC0` == `0x80`).
5. Monta a runa combinando AND (extrair bits de dados), left shift (abrir espaço) e OR (mesclar bits) para cada byte envolvido.
6. Rejeita *surrogate pairs* (`U+D800`–`U+DFFF`).
7. Rejeita *overlong encoding* (caracteres codificados com mais bytes do que o mínimo necessário).
8. Rejeita codepoints acima do máximo Unicode (`U+10FFFF`).
9. Caso nenhum prefixo válido seja encontrado no primeiro byte, retorna erro de UTF-8 inválido.

O autor reforça, ao final, que esta não é a implementação mais rápida possível (existem versões *branchless* mais eficientes), mas é uma implementação **legível**, que **passa em toda a suite de testes oficial do pacote `unicode/utf8` de Go**, e que serve para entender de fato como o padrão UTF-8 funciona por dentro.

---

## Resumo dos Conceitos

| Conceito | O que é |
|---|---|
| **`DecodeRune(b []byte) (rune, int, error)`** | Função implementada: decodifica o primeiro caractere de um slice de bytes |
| **AND (`&`)** | Zera bits irrelevantes / verifica se bits específicos estão setados |
| **OR (`\|`)** | Mescla bits de fontes diferentes num único valor |
| **Left shift (`<<`)** | Abre espaço à direita para os bits do próximo byte |
| **Prefixo do 1º byte** | Determina o tamanho do caractere: `0`, `110`, `1110`, `11110` |
| **Byte de continuação** | Sempre começa com `10xxxxxx` |
| **Overlong encoding** | Codificar um caractere usando mais bytes do que o mínimo necessário — proibido |
| **Surrogate pairs** | Faixa `U+D800`–`U+DFFF`, reservada para UTF-16, proibida como resultado de decode UTF-8 |
| **Codepoint máximo Unicode** | `U+10FFFF` |
| **TDD com testes importados** | Copiar a suite de testes de uma implementação de referência (aqui, a stdlib de Go) como oráculo de corretude |

---

## Conceitos-chave

- [[utf-8]]
- [[unicode]]
- [[ascii]]
- [[charset]]
- [[string]]
- [[tdd]]
- [[go-fundamentos]]
- [[go-stdlib]]
- [[rfc-request-for-comments]]
- [[bitwise-operations]]
- [[overlong-encoding]]
