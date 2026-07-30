---
type: concept
title: "Compactação de Texto (Huffman Coding, Deflate, LZSS/LZ77)"
aliases: ["huffman coding", "deflate", "lzss", "lz77", "compressão de texto", "text compression"]
date_created: 2026-07-27
date_updated: 2026-07-29
source_count: 2
tags: [cs-fundamentals, compressao, huffman-coding, deflate, lzss, encoding]
skill: cs-fundamentals
status: stub
---

# Compactação de Texto

Reduzir o número de bytes necessários para representar um texto sem perder informação (compactação sem perdas / *lossless*). O algoritmo **deflate** — usado em gzip e arquivos zip — combina duas técnicas complementares: **Huffman coding** e **LZSS** (variante de LZ77).

## Huffman coding

Ideia central: caracteres usados com mais frequência recebem códigos binários mais curtos; caracteres raros recebem códigos mais longos. Isso só funciona porque, ao contrário de UTF-8 (onde todo caractere ocupa 8 bits fixos), o Huffman coding usa comprimento variável por caractere.

Construção da árvore de Huffman:
1. Conte a frequência de cada caractere no texto e transforme cada um numa folha.
2. Pegue os dois nós (folhas ou já combinados) com menor frequência e conecte-os sob um nó novo, cuja frequência é a soma dos dois.
3. Remova os dois nós originais da lista e substitua pelo nó combinado.
4. Repita até sobrar um único nó raiz.

Para obter o código de um caractere, desça da raiz até a folha: esquerda = `0`, direita = `1`. Caracteres mais frequentes ficam mais próximos da raiz (código curto); caracteres raros ficam mais fundos (código longo).

**Consequência prática:** a árvore precisa ser transmitida junto com os dados compactados — sem ela, é impossível decodificar. Isso significa que reduzir a *variedade* de caracteres distintos no texto (não só sua frequência) encolhe tanto os códigos quanto a própria árvore. Exemplo: unificar "a" e "A" num único caractere ("a") remove uma folha inteira da árvore, porque a frequência das duas ocorrências vai para uma única folha em vez de duas folhas separadas com frequência 1 cada.

## LZSS / LZ77

Depois do Huffman coding, o deflate aplica **LZSS** (Lempel-Ziv-Storer-Szymanski, variante do LZ77 original): encontra sequências repetidas de dados e substitui a repetição por um **ponteiro** de dois números — (1) a distância até a ocorrência anterior da sequência, (2) o comprimento da sequência repetida. Quanto mais repetição literal houver no texto, maior o ganho — um texto com uma frase repetida várias vezes comprime desproporcionalmente melhor do que o mesmo volume de texto sem repetição.

## Por que letras minúsculas comprimem melhor

Ver [[wiki/sources/por-que-letras-minusculas-economizam-dados]] para a demonstração completa: trocar maiúsculas por minúsculas não muda o tamanho do arquivo *antes* de compactar (cada caractere UTF-8 ocupa 1 byte independente de caixa), mas reduz a variedade de caracteres distintos — o que encolhe a árvore de Huffman e aumenta a chance de sequências repetidas coincidirem exatamente (facilitando o LZSS). O ganho é real, mas modesto: no caso de estudo do Hacker News, reescrever títulos de title case para sentence case economizou apenas 31 bytes por carregamento de página. É uma otimização de cauda longa — imagens não otimizadas, autoplay de vídeo e JavaScript não utilizado desperdiçam ordens de magnitude mais dados do que qualquer ajuste de maiúscula/minúscula.

## Relação com HTTP/2 HPACK

[[wiki/sources/http-tcp-quic]] documenta que o HTTP/2 usa **HPACK** para compactar headers — HPACK também usa uma tabela de Huffman estática (baseada em frequências típicas de headers HTTP) como parte da sua compactação, o mesmo princípio de "caracteres mais frequentes, códigos mais curtos" aplicado a um domínio diferente (headers HTTP em vez de texto livre).

## Huffman coding em imagens

O mesmo Huffman coding descrito acima não é exclusivo de texto/HTTP: [[wiki/sources/historia-dos-formatos-de-imagem]] documenta que tanto JPEG quanto PNG usam Huffman coding como passo final de compressão — no JPEG, sobre os coeficientes já quantizados pela DCT (compressão com perdas); no PNG, sobre a saída do deflate (compressão sem perdas), o mesmo par Huffman + LZSS documentado aqui. Ver [[wiki/concepts/compressao-com-perdas-vs-sem-perdas]] e [[wiki/concepts/formato-jpeg]].

## Ver também

- [[wiki/concepts/big-o]] — Huffman coding e LZSS não mudam a complexidade assintótica do texto, mudam a densidade de informação por byte.
