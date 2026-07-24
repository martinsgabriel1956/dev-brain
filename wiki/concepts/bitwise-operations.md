---
type: concept
title: "Bitwise Operations (AND, OR, Left Shift)"
aliases: ["bit manipulation", "operações bitwise", "AND OR shift", "manipulação de bits", "bitmask"]
date_created: 2026-07-22
date_updated: 2026-07-22
source_count: 1
tags: [bitwise, bit-manipulation, mascara, cs-fundamentals, numero-binario]
skill: cs-fundamentals
status: draft
---

# Bitwise Operations (AND, OR, Left Shift)

Operações que atuam diretamente nos bits de um valor, em vez de tratá-lo como número. Três operações formam a base de praticamente qualquer algoritmo de parsing/encoding binário: **AND**, **OR** e **left shift**.

## AND (`&`) — Extrair ou Zerar Bits

Bit resultante é `1` **somente se ambos os bits forem `1`**. Usado para:
- **Zerar bits irrelevantes**: `& 0` num grupo de bits sempre produz `0`, "apagando" essa região.
- **Verificar se um padrão de bits está presente**: comparar o resultado de um AND com uma máscara contra um valor esperado.
- **Extrair um subconjunto de bits**: uma máscara com `1`s exatamente nas posições desejadas preserva só esses bits.

```go
b0 & 0xE0 == 0xC0   // os 3 bits mais altos de b0 são exatamente 110?
r := rune(b0) & 0x1F // mantém só os 5 bits menos significativos
```

## OR (`|`) — Mesclar Bits de Fontes Diferentes

Bit resultante é `1` se **pelo menos um** dos dois bits for `1`. Usado para combinar grupos de bits vindos de lugares diferentes num único valor — desde que essas regiões não se sobreponham (senão o resultado mistura informação).

```go
r = r | data // funde os bits de "r" com os bits de "data"
```

## Left Shift (`<<`) — Abrir Espaço

Desloca todos os bits N posições para a esquerda; as posições que sobram à direita são preenchidas com zero. Equivale a multiplicar por `2^N`, mas o uso mais comum em parsing binário não é aritmético — é **abrir espaço** para encaixar o próximo grupo de bits antes de um OR.

```go
r = r << 6 // abre 6 bits de espaço à direita, para receber o próximo grupo via OR
```

## Padrão Composto: Extrair → Deslocar → Mesclar

A combinação recorrente em algoritmos de parsing binário (protocolos, encodings, flags) é:

1. **AND** com uma máscara para isolar os bits de interesse de um byte/valor.
2. **Left shift** para posicionar esses bits no lugar certo dentro do valor final.
3. **OR** para mesclar com os bits já acumulados.

Repetido byte a byte, esse padrão constrói um valor maior a partir de fragmentos menores.

## Aplicação Real: Decode de UTF-8

[[wiki/sources/algoritmo-decode-utf8-com-tdd]] usa exatamente esse padrão composto para reconstruir uma [[unicode|runa Unicode]] de 32 bits a partir de 1 a 4 bytes de um caractere [[utf-8]]: cada byte de continuação tem seus 2 bits de prefixo removidos via AND (`& 0x3F`), é deslocado para a posição correta via left shift, e mesclado ao resultado acumulado via OR.

## Outras Aplicações Comuns

- **Feature flags / permissões como bitmask**: `READ | WRITE` combina flags; `perms & WRITE != 0` verifica se uma flag está setada.
- **`iota` em Go para bitmask**: `const (Read = 1 << iota; Write; Exec)` gera `1, 2, 4` — ver [[go-fundamentos]].
- **Parsing de protocolos binários**: TCP flags, headers de protocolo, cores em hexadecimal.

## Relação com Outros Conceitos

- [[utf-8]] — decode/encode usa AND+shift+OR para montar/desmontar runas
- [[go-fundamentos]] — `iota` com left shift para bitmask em Go

## Key Sources

- [[wiki/sources/algoritmo-decode-utf8-com-tdd]]
