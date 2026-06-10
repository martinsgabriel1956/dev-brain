# Como Strings Realmente Funcionam (por Baixo dos Panos)

**Formato:** Transcrição de vídeo (YouTube)
**Idioma original:** Português (BR)
**Data de transcrição:** 2026-06-10
**Linguagem de código usada nos exemplos:** Go

---

## Introdução

Quando a gente começa a estudar programação, dependendo da linguagem, uma das primeiras estruturas de dados que a gente vê são as Strings — a não ser que você comece por C, que aí as strings não são abstraídas e você tem que lidar com ponteiros.

Na grande maioria das linguagens (Go, Python, Java, C#, PHP), o conceito de string é abstraído do desenvolvedor. E em praticamente todas essas linguagens, **Strings são imutáveis**. A única exceção é o PHP, mas mesmo assim não é recomendado mexer com strings diretamente.

Mas por que Strings são imutáveis? Esse vídeo explica como strings realmente funcionam por debaixo dos panos — e elas são bem mais complexas do que parecem.

---

## Como o Computador Interpreta Dados

Uma CPU só vê transistores: 1 e 0, ligado ou desligado. Para que uma string exista, ela precisa de **três coisas**:

1. **Tamanho da string** — o intervalo de endereços de memória a ser lido
2. **Charset** — o mapeamento de valor binário → caractere
3. **Encoding** — o algoritmo que diz como interpretar a sequência de bytes

---

## ASCII: Charset e Encoding ao Mesmo Tempo

Um dos charsets mais famosos é o **ASCII**. Nos computadores modernos não conseguimos dividir memória em menos de 8 bits (1 byte), mas o ASCII foi criado para funcionar em **7 bits** — ou seja, 128 caracteres possíveis (0 a 127).

A famosa tabela ASCII mapeia cada valor para um caractere. Por exemplo:

| Valor decimal | Caractere |
|---|---|
| 72 | H |
| 101 | e |
| 108 | l |
| 111 | o |

O ASCII é simultaneamente um **charset** e um **encoding** porque 1 byte é suficiente para representar qualquer um dos 128 caracteres — não existe ambiguidade na interpretação.

### Exemplo em Go

```go
s := "Hello"
b := s[0]           // pega o primeiro byte
fmt.Println(b)      // 72
fmt.Println(string(b)) // H
```

O valor `72` está salvo naquele espaço de memória. Quando instruímos o Go a interpretar esse byte como string, ele vai à tabela ASCII, encontra `72 = H`, e imprime `H`.

### Limitação do ASCII

ASCII só suporta 128 caracteres. Isso significa:

- Acentos não existem
- Emojis não existem
- Qualquer idioma fora do alfabeto inglês não pode ser representado

---

## Unicode e UTF-8: Charset vs. Encoding

Para resolver as limitações do ASCII, surgiu o **Unicode** — e um pouco depois, o **UTF-8**.

### Unicode é apenas um Charset

Unicode é somente um **mapeamento** (charset): o valor X corresponde ao caractere Y. Ele não diz como armazenar esse valor em bytes.

Alguns valores do Unicode não cabem em 1 byte — para representar certos caracteres, você precisa de mais de um byte.

### UTF-8 é o Encoding do Unicode

O UTF-8 é um **algoritmo de encoding** que determina como uma sequência de bytes deve ser interpretada para representar caracteres Unicode. Ele é o padrão mais usado hoje em dia.

**Propriedade importante:** UTF-8 é 100% compatível com ASCII — qualquer caractere ASCII é representado da mesma forma em UTF-8.

> Curiosidade: o UTF-8 foi criado por **Ken Thompson** e **Rob Pike** — os mesmos criadores da linguagem Go.

---

## Strings São Arrays de Bytes

Por baixo dos panos, uma string não é nada mais do que um **slice (array) de bytes**.

### O Problema com Caracteres Multi-byte

```go
s := "Hello, 世界"
// Hello = 5 chars
// , = 1 char
// (espaço) = 1 char
// 世界 = 2 chars
// Total visível: 9 "caracteres"

fmt.Println(len(s)) // 13 — não 9!
```

Por quê 13? Porque os caracteres chineses precisam de **mais de 1 byte** para ser representados em UTF-8. O `len()` em Go retorna o número de bytes, não de caracteres visíveis.

### Runas em Go

Em Go, uma **runa** (`rune`) é um tipo de 32 bits (4 bytes) capaz de representar qualquer caractere Unicode. Quando queremos contar caracteres reais:

```go
fmt.Println(utf8.RuneCountInString(s)) // 9 — o número de runas
```

A string tem 9 runas, mas 13 bytes na memória.

---

## O Perigo de Indexar Strings com Caracteres Multi-byte

Quando você faz `s[i]` numa string, está pegando o **i-ésimo byte**, não o i-ésimo caractere.

```go
s := "ä Hello"  // 'ä' usa 2 bytes em UTF-8

b := s[0]
fmt.Println(b)        // 195  (apenas o primeiro byte de 'ä')
fmt.Println(string(b)) // Ã   (caractere errado — encoding quebrado)
```

Ao pegar só o primeiro byte de um caractere multi-byte, você quebra o encoding e obtém um caractere completamente diferente.

---

## Por Que Strings São Imutáveis

Esse é o motivo fundamental: **é muito fácil quebrar o encoding de uma string** se você permitir alterações arbitrárias de bytes.

Imagine tentar substituir o caractere chinês `世` (que ocupa 3 bytes) pelo caractere `w` (que ocupa 1 byte):

```go
// Exemplo hipotético — isso NÃO compila em Go
s[7] = 'w'  // erro de compilação: strings são imutáveis
```

Se o compilador permitisse isso, você estaria sobrescrevendo apenas 1 dos 3 bytes que formam `世`, corrompendo completamente o encoding da string.

Ao tornar strings imutáveis, as linguagens garantem que o encoding nunca seja quebrado acidentalmente.

---

## Resumo dos Conceitos

| Conceito | O que é |
|---|---|
| **Charset** | Mapeamento: valor numérico → caractere |
| **Encoding** | Algoritmo: sequência de bytes → caractere |
| **ASCII** | Charset + encoding, 7 bits, 128 caracteres |
| **Unicode** | Charset universal, mas não define encoding |
| **UTF-8** | Encoding para Unicode, compatível com ASCII |
| **Rune (Go)** | Tipo de 32 bits que representa um codepoint Unicode |
| **`len(s)` em Go** | Número de **bytes**, não de caracteres |
| **String imutável** | Proteção contra corrupção de encoding |

---

## Conceitos-chave

- [[charset]]
- [[encoding]]
- [[ascii]]
- [[unicode]]
- [[utf-8]]
- [[imutabilidade]]
- [[byte]]
- [[rune]]
- [[string]]
