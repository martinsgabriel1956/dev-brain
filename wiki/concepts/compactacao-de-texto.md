---
type: concept
title: "Compactação de Texto (Huffman Coding, Deflate, LZSS/LZ77)"
aliases: ["huffman coding", "deflate", "lzss", "lz77", "compressão de texto", "text compression"]
date_created: 2026-07-27
date_updated: 2026-08-28
source_count: 4
tags: [cs-fundamentals, compressao, huffman-coding, deflate, lzss, lz77, gzip, encoding, priority-queue]
skill: cs-fundamentals
status: draft
---

# Compactação de Texto

Reduzir o número de bytes necessários para representar um texto sem perder informação (compactação sem perdas / *lossless*). O algoritmo **deflate** — usado em gzip e arquivos zip — combina duas técnicas complementares, nessa ordem: primeiro **LZ77** (LZSS), depois **Huffman coding**.

## Gzip é formato de arquivo, não algoritmo

[[wiki/sources/gzip-deflate-huffman-lz77]] desfaz uma confusão comum: **gzip não é um algoritmo de compressão**. "Gzip" nomeia duas coisas ao mesmo tempo — (1) a ferramenta de linha de comando do Linux e (2) uma **especificação de formato de arquivo comprimido** (a estrutura de header/trailer que envolve os dados). O algoritmo que de fato comprime os dados dentro de um arquivo `.gz` é o deflate, descrito abaixo. É possível inspecionar o header hexadecimal de um arquivo gzip real com `xxd <arquivo>.gz` — os primeiros bytes pertencem à especificação gzip em si, distintos do stream deflate ilegível que vem depois.

## LZ77 / LZSS (primeiro passo do deflate)

O deflate aplica primeiro **LZ77** (a variante usada pelo deflate é chamada **LZSS**, Lempel-Ziv-Storer-Szymanski): encontra sequências repetidas de dados e substitui a repetição por um **ponteiro** de volta à ocorrência anterior. Quanto mais repetição literal houver no texto, maior o ganho — um texto com uma frase repetida várias vezes comprime desproporcionalmente melhor do que o mesmo volume de texto sem repetição.

**Mecânica (sliding window):** [[wiki/sources/gzip-deflate-huffman-lz77]] detalha que o LZ77 escaneia o texto usando dois buffers — um **search buffer** (o que já foi visto, janela de busca por repetições) e um **look-ahead buffer** (o que ainda será lido). Por isso o algoritmo pode "perder" uma sequência que de fato se repete no texto, se a ocorrência anterior já saiu da janela do search buffer — a compressão não é uma busca global no arquivo inteiro, é local à janela.

**Representação — triplet, não token único:** cada sequência repetida encontrada não vira um token arbitrário (como um id de hashmap); ela vira um **triplet** — `(offset, length, caractere)`:
- **offset** — distância até a ocorrência anterior da sequência;
- **length** — comprimento da sequência repetida;
- **caractere** — o próximo caractere literal após a sequência repetida.

## Huffman coding (segundo passo do deflate)

Depois do LZ77, o deflate aplica **Huffman coding**. Ideia central: caracteres usados com mais frequência recebem códigos binários mais curtos; caracteres raros recebem códigos mais longos. Isso só funciona porque, ao contrário de ASCII/UTF-8 (onde todo caractere ocupa uma quantidade **fixa** de bits — 7 bits em ASCII puro), o Huffman coding usa comprimento **variável** por caractere. Ver [[wiki/concepts/ascii]].

Construção da árvore de Huffman, via uma **priority queue** (fila de prioridade) ordenada por frequência crescente:
1. Conte a frequência de cada caractere no texto e transforme cada um numa folha; insira todas as folhas na priority queue.
2. Remova os dois nós de **menor** frequência da fila (folhas ou já combinados) e conecte-os sob um nó novo, cuja frequência é a soma dos dois.
3. Reinsira o nó combinado na priority queue no lugar dos dois originais.
4. Repita até sobrar um único nó raiz — a árvore de Huffman completa.

Para obter o código de um caractere, desça da raiz até a folha: esquerda = `0`, direita = `1`. Caracteres mais frequentes ficam mais próximos da raiz (código curto, ex.: 2 bits); caracteres raros ficam mais fundos (código longo, ex.: 3+ bits) — ver [[wiki/concepts/priority-queue]] para a estrutura de dados usada na construção, e [[wiki/concepts/arvore]] para a árvore binária resultante.

**Consequência prática:** a árvore precisa ser transmitida junto com os dados compactados — sem ela, é impossível decodificar. Isso significa que reduzir a *variedade* de caracteres distintos no texto (não só sua frequência) encolhe tanto os códigos quanto a própria árvore. Exemplo: unificar "a" e "A" num único caractere ("a") remove uma folha inteira da árvore, porque a frequência das duas ocorrências vai para uma única folha em vez de duas folhas separadas com frequência 1 cada.

## Por que letras minúsculas comprimem melhor

Ver [[wiki/sources/por-que-letras-minusculas-economizam-dados]] para a demonstração completa: trocar maiúsculas por minúsculas não muda o tamanho do arquivo *antes* de compactar (cada caractere UTF-8 ocupa 1 byte independente de caixa), mas reduz a variedade de caracteres distintos — o que encolhe a árvore de Huffman e aumenta a chance de sequências repetidas coincidirem exatamente (facilitando o LZSS). O ganho é real, mas modesto: no caso de estudo do Hacker News, reescrever títulos de title case para sentence case economizou apenas 31 bytes por carregamento de página. É uma otimização de cauda longa — imagens não otimizadas, autoplay de vídeo e JavaScript não utilizado desperdiçam ordens de magnitude mais dados do que qualquer ajuste de maiúscula/minúscula.

## Relação com HTTP/2 HPACK

[[wiki/sources/http-tcp-quic]] documenta que o HTTP/2 usa **HPACK** para compactar headers — HPACK também usa uma tabela de Huffman estática (baseada em frequências típicas de headers HTTP) como parte da sua compactação, o mesmo princípio de "caracteres mais frequentes, códigos mais curtos" aplicado a um domínio diferente (headers HTTP em vez de texto livre).

## Huffman coding em imagens

O mesmo Huffman coding descrito acima não é exclusivo de texto/HTTP: [[wiki/sources/historia-dos-formatos-de-imagem]] documenta que tanto JPEG quanto PNG usam Huffman coding como passo final de compressão — no JPEG, sobre os coeficientes já quantizados pela DCT (compressão com perdas); no PNG, sobre a saída do deflate (compressão sem perdas), o mesmo par Huffman + LZSS documentado aqui. Ver [[wiki/concepts/compressao-com-perdas-vs-sem-perdas]] e [[wiki/concepts/formato-jpeg]].

## Relação com Brotli

[[wiki/concepts/brotli]] é um algoritmo mais recente (Google) que generaliza o mesmo par LZ77-like + codificação por frequência descrito aqui, adicionando um dicionário estático embutido com os termos mais comuns da web. [[wiki/sources/hospedando-site-completo-em-url-fragment-brotli-webassembly]] documenta um caso extremo de uso: comprimir um site inteiro com Brotli para caber dentro do [[wiki/concepts/fragment-identifier-url]] de uma URL, sem servidor — como não há servidor para negociar `Content-Encoding: br`, o descompressor teve que ser reimplementado e rodado no cliente via [[wiki/concepts/webassembly]].

## Ver também

- [[wiki/concepts/big-o]] — Huffman coding e LZSS não mudam a complexidade assintótica do texto, mudam a densidade de informação por byte.

## Key sources

- [[wiki/sources/por-que-letras-minusculas-economizam-dados]]
- [[wiki/sources/gzip-deflate-huffman-lz77]] — distinção gzip (formato) vs. deflate (algoritmo), triplet do LZ77 (offset/length/caractere), sliding window (search + look-ahead buffer), e priority queue na construção da árvore de Huffman
- [[wiki/sources/hospedando-site-completo-em-url-fragment-brotli-webassembly]] — Brotli como evolução do mesmo par LZ77 + codificação por frequência, aplicado a um caso extremo de compressão de site inteiro sem servidor
