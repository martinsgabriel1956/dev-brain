---
type: concept
title: "String"
aliases: ["string", "cadeia de caracteres", "string internals", "strings imutáveis"]
date_created: 2026-06-10
date_updated: 2026-11-24
source_count: 9
tags: [strings, encoding, cs-fundamentals, imutabilidade, charset, utf-8, decode]
skill: cs-fundamentals
status: stable
---

# String

Por baixo dos panos, uma string não é um tipo primitivo opaco. É um **slice de bytes** acompanhado de três atributos: tamanho, [[charset]] e [[utf-8|encoding]].

## O Que Uma String Precisa Para Existir

| Atributo | Função |
|---|---|
| **Tamanho** | Intervalo de endereços de memória — onde a string começa e termina |
| **Charset** | Mapeamento: valor numérico → caractere |
| **Encoding** | Algoritmo: sequência de bytes → caractere |

## String é um Slice de Bytes

A representação interna de uma string é um array de bytes. Isso tem implicações diretas:

```go
s := "Hello, 世界"
fmt.Println(len(s))                        // 13 bytes
fmt.Println(utf8.RuneCountInString(s))     // 9 runas (caracteres visuais)
```

Os dois caracteres chineses ocupam 3 bytes cada em UTF-8. `len()` conta bytes; para contar caracteres visuais é preciso decodificar as runas.

## O Perigo de Indexar por Byte

```go
b := s[7]              // pega apenas o 1º byte do caractere chinês
fmt.Println(string(b)) // caractere incorreto — encoding quebrado
```

`s[i]` retorna o byte na posição `i`, não o caractere `i`. Em strings com caracteres multi-byte, isso retorna um fragmento inválido.

Para iterar corretamente:

```go
for i, r := range s {  // range itera runas, não bytes
    fmt.Println(i, r)
}
```

## Por Que Strings São Imutáveis

Quase todas as linguagens modernas (Go, Java, Python, C#, JavaScript, Rust) tornam strings imutáveis. O motivo é técnico: alterar um byte arbitrário numa string UTF-8 pode sobrescrever parte de um caractere multi-byte, corrompendo silenciosamente o encoding.

Exemplo hipotético (não compila em Go):
```go
s[7] = 'w'  // tentaria substituir 1 byte de um caractere de 3 bytes → encoding quebrado
```

A única linguagem citada como exceção é PHP, onde strings são mutáveis — mas manipulação direta não é recomendada pelo mesmo motivo.

Ver [[imutabilidade]] para o princípio geral; este verbete cobre o caso específico de strings.

## Runa (Go)

Em Go, `rune` é um alias para `int32` — representa um codepoint [[unicode]] completo. Uma runa sempre representa um caractere visual inteiro, independente de quantos bytes ele ocupa em memória.

## Relação com Outros Conceitos

- [[charset]] — o mapeamento que diz qual valor corresponde a qual caractere
- [[ascii]] — o charset+encoding mais antigo; 128 caracteres, 1 byte por caractere
- [[unicode]] — o charset universal; não define como armazenar em bytes
- [[utf-8]] — o encoding mais usado para Unicode; largura variável, compatível com ASCII
- [[imutabilidade]] — o princípio que protege o encoding de ser corrompido

## Como uma Runa é Reconstruída a Partir de Bytes

[[wiki/sources/algoritmo-decode-utf8-com-tdd]] implementa, na prática, o processo inverso da indexação por byte descrita acima: dado um slice de bytes, reconstrói a runa completa usando [[bitwise-operations|AND, OR e left shift]] — a mesma lógica que o Go executa internamente ao converter bytes em caracteres UTF-8.

## Na NLW #1, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]]: em JavaScript, string se escreve com aspas duplas, simples ou crase; a crase permite interpolação com `${}` (`` `<p>${i}</p>` ``). Uma string solta no código "não serve pra nada" sem ir para uma variável ou função.

Em [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]], a string é "um conjunto de caracteres" entre aspas, concatenada com `+` ou montada com [[wiki/concepts/template-literals|template literal]].

Em [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]], `name.toUpperCase()` funciona porque, na fala da aula, a string "já se torna um objeto" e "herda" métodos. A string continua primitiva; o método vem de `String.prototype` por *autoboxing*.

Em [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]], `nome.length` dá 6 para "Násser", e o autocomplete lista os métodos herdados de `String.prototype` (`indexOf`, `matchAll`; o "lastChild" da legenda é provavelmente `lastIndexOf`).

Em [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]], `item.toUpperCase()` dentro do `forEach` põe todas as marcas em caixa alta.

Em [[wiki/sources/frontpush-modules-js-import-export-default]], `upperName` devolve a string "com a função upperCase [...] em caixa alta": é o método `toUpperCase()`.

## No JavaScript Ninja, aula 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]], string é "uma sequência de caracteres" entre aspas duplas ou "apóstrofo": "isso não tem diferença alguma" em JavaScript, ao contrário de linguagens que exigem aspas duplas. A crase da [[wiki/concepts/template-literals|template literal]] veio depois (ES2015).

## Key Sources

- [[wiki/sources/como-strings-realmente-funcionam]]
- [[wiki/sources/algoritmo-decode-utf8-com-tdd]] — implementação do algoritmo de decode bytes → runa
- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: três tipos de aspas; template string
- [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]]: FrontPUSH, JavaScript aula 02: string, concatenação e template string
- [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]]: FrontPUSH, JavaScript aula 04: toUpperCase e autoboxing
- [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]]: FrontPUSH, JavaScript aula 05: length e métodos de String.prototype
- [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]]: FrontPUSH, JavaScript aula 07: toUpperCase em cada item
- [[wiki/sources/frontpush-modules-js-import-export-default]]: FrontPUSH, JavaScript aula 17: toUpperCase em upperName
- [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]]: JavaScript Ninja, aula 01: aspas simples ou duplas, sem diferença
