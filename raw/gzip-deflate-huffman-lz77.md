# O Que É Gzip de Verdade (Deflate, LZ77 e Huffman Coding)

> Transcrição de vídeo do YouTube (autor não identificado, em português). Limpa de marcas de ASR (pontuação, repetições, erros de transcrição corrigidos por contexto — ex.: "lit code" → "LeetCode", "isk"/"ich"/"queem Ach" → "ASCII", "Bane retrieve" → "binary tree", "priority Skill" → "priority queue", "ruffman coding" → "Huffman coding") e organizada em seções. Conteúdo e ordem das ideias preservados.

## Introdução: gzip não é o que você pensa

Você realmente sabe o que é gzip? Quando a gente fala sobre gzip para programadores, a pessoa já pensa logo em HTML: "ah, gzip é só uma forma de comprimir os arquivos HTML para eles irem mais rápido pro browser". Mais ou menos, mas não é bem isso.

E se eu te falar que gzip **não é um algoritmo de compressão ou compactação**? Gzip na verdade são duas coisas diferentes ao mesmo tempo:

1. A **ferramenta** que a gente usa no Linux — vem por padrão, é aquele comando de terminal onde a gente coloca `gzip <nome-do-arquivo>` e ele compacta o arquivo pra gente.
2. A **especificação** em si. A especificação gzip não fala sobre compressão — ela nada mais é do que um **formato de arquivo comprimido**.

Ou seja: gzip não é um algoritmo de compressão, é um **formato de arquivo**. O algoritmo de compressão/compactação mais usado pelos arquivos gzip é o **deflate**.

## Do texto aos bits

Vamos entender como isso tudo funciona por debaixo dos panos, começando com um arquivo HTML simples (uma tabela).

Quando o computador vê esse arquivo, ele não vê o que a gente está vendo. Ele não vê a palavra "table" — ele vê uma sequência de bits/bytes. Não são nem caracteres em si: o computador vê o byte `t`, o byte `a`, o byte `b`... e esses bytes têm uma representação visual para nós, humanos, mas por debaixo dos panos isso é só número (ver vídeo linkado do próprio autor sobre como Strings funcionam, não detalhado aqui).

Como saber quantos bytes um arquivo gasta em memória? Usando apenas caracteres ASCII (sem acento), cada caractere ocupa 1 byte — e espaço em branco (*whitespace*) também é um caractere. No exemplo do vídeo: 285 caracteres = 285 bytes. Multiplicando por 8, isso dá 2.280 bits que o arquivo consome de memória.

## Deflate: o algoritmo por trás do gzip

É aqui que entra o algoritmo de compressão chamado **deflate**, o comumente utilizado pelo gzip. Simplificando bastante (o algoritmo é complexo demais para caber inteiro em um vídeo):

1. Primeiro ele roda a compressão **LZ77**.
2. Depois roda **Huffman coding**.

Essa combinação — primeiro LZ77, depois Huffman coding — é o que se chama de algoritmo **deflate** (ou só *flate*).

Importante: os dois algoritmos, e por consequência o deflate, são **lossless** (sem perdas) — o arquivo fica menor, mas nenhum bit de informação é perdido. Existem compressões mais agressivas que diminuem ainda mais o tamanho do arquivo, mas deixam de ser lossless (há perda de informação). Isso não é comum em arquivos de texto, mas é muito comum em vídeo e imagem — é por isso que, ao subir um vídeo para o YouTube, ele nunca tem a mesma qualidade do vídeo original: o YouTube faz uma compressão que não é lossless.

## LZ77: o primeiro passo do deflate

O que o LZ77 faz é procurar **sequências de caracteres repetidos** — uma estrutura de dados/algoritmo de LeetCode entrando em ação de verdade. Ele é implementado usando a técnica de **sliding window**.

Basicamente ele escaneia todo o texto procurando áreas onde os caracteres se repetem. Exemplo no vídeo: numa lista de datas como "1 de fevereiro, 2 de fevereiro, 3 de fevereiro, 4 de fevereiro...", o trecho " de fevereiro" se repete muitas vezes. O algoritmo:

1. Apaga essa sequência repetida e salva numa "tabelinha" (como um hashmap).
2. Substitui a sequência por um token/keyword. Ex.: " de fevereiro" vira o token `A`, e a tabela registra `A = " de fevereiro"`.
3. Repete isso para toda sequência de caracteres que se repete no texto. Outro exemplo do vídeo: `/td` aparecendo várias vezes no HTML (fechamento de tags de tabela) poderia virar o token `B`.

**Isso é uma simplificação para entender a lógica** — não é exatamente assim que o algoritmo funciona. Na prática, o LZ77 usa a técnica de sliding window com dois buffers: um **search buffer** e um **look-ahead buffer**. Por consequência, ele pode acabar "jogando fora" sequências de caracteres que de fato se repetem, mas que já saíram do search buffer (não estão mais na janela).

Além disso, o LZ77 não transforma a sequência repetida num token único como "A" — ele transforma a sequência num **triplet**, uma tupla de três itens:

1. **Offset** — a distância até a ocorrência anterior da sequência.
2. **Length** — o tamanho da sequência repetida.
3. **Caractere** — o próximo caractere após a sequência repetida.

Esse algoritmo é complexo demais para caber inteiro neste vídeo (o autor comenta que poderia fazer um vídeo dedicado só a ele, mediante pedido nos comentários).

## Huffman coding: o segundo passo do deflate

Depois do LZ77, ainda dá pra comprimir mais — é aí que entra a segunda parte do deflate: **Huffman coding**. Ele funciona através de uma **binary tree** — mais uma estrutura de dados do dia a dia que parecia só existir em entrevista de LeetCode, mas está literalmente rodando toda vez que você faz um request HTTP para um servidor que retorna um arquivo gzipado.

Como o algoritmo funciona:

1. Conta cada caractere que aparece no arquivo, individualmente.
2. Coloca esses elementos numa **priority queue** (fila de prioridade) ordenada pela frequência de cada um — os elementos com **menor frequência primeiro**, indo até os que aparecem mais vezes.
3. Cada elemento da priority queue vira uma **folha** da binary tree.
4. Começa o processo de construção da árvore.

### Exemplo passo a passo (árvore separada, não o HTML de exemplo)

Suponha as frequências contadas:

- `a` → 77 vezes
- `b` → 5 vezes
- `e` → 10 vezes
- (e outros caracteres, incluindo `g`, `f`, `c`, `d`, no exemplo do vídeo)

Passo 1 — ordenar em ordem crescente de frequência: `b` (5), `e` (10), ... (o caractere que aparece menos vezes vem primeiro).

Passo 2 — pegar os **dois menores números** da lista (`b`=5 e `e`=10), somá-los, e criar uma árvore cujo nó raiz tem o valor somado (15): à esquerda o menor valor (`b`=5), à direita o outro (`e`=10).

Passo 3 — remover `b` e `e` da lista original e colocar essa nova árvore (valor 15) no lugar deles. A lista fica reordenada: `15, f, g, c, d, a` (exemplo ilustrativo da ordem after-merge do vídeo).

Passo 4 — repetir o algoritmo: pegar os dois menores da lista (`15` e `f`, sendo `f`=20), somar (35), formar uma nova árvore, remover os dois da lista e inserir a árvore de valor 35 no lugar.

Passo 5 — reordenar de novo (pode mudar a ordem — no exemplo, `g` com frequência 30 passa a vir antes do nó de valor 35) e seguir repetindo o algoritmo até sobrar um único nó (a árvore final).

### Por que isso economiza memória

A árvore tem dois tipos de nó:

- **Nós internos** — não representam nenhum caractere, só ligam a outros nós.
- **Nós folha** — representam um caractere; não apontam para nenhum outro nó.

Para achar o código binário de um caractere, desce-se da raiz até a folha: braço direito = bit `1`, braço esquerdo = bit `0`.

- O caractere `a` (representado normalmente em ASCII com um byte inteiro, valor 65) nessa árvore de exemplo é alcançado indo direita → direita, ou seja, é representado com apenas **2 bits**: `11`.
- O caractere `g` (que normalmente também "gastaria" um byte inteiro em ASCII) é alcançado indo direita → esquerda → esquerda, ou seja, é representado com **3 bits**: `100` (conforme a trilha descrita no vídeo).

A diferença chave: em ASCII, todo caractere usa uma quantidade **fixa** de bits (7 bits). Na árvore de Huffman, cada caractere pode ter uma quantidade **diferente** de bits — e a ordenação por frequência é o motivo: caracteres que aparecem **menos vezes** acabam com **mais bits** (ficam mais fundo na árvore), e caracteres que aparecem **mais vezes** (como `a`, o mais frequente no exemplo) ficam com **menos bits** (mais perto da raiz). É basicamente assim que o gzip funciona por debaixo dos panos, através do algoritmo deflate.

## Vendo o resultado com xxd

A mesma tabela HTML de exemplo, compactada em gzip, vira um arquivo ilegível a olho nu. Só que no Vim (ou terminal) existe um comando que ajuda a ler esse arquivo: **`xxd`**. Rodando esse comando, a gente tem a representação **hexadecimal** de cada byte do arquivo — muito mais legível. No cabeçalho (os primeiros bytes) desse arquivo é que entra o **gzip de fato**, sem ser o algoritmo de compressão deflate (o header da especificação gzip em si).

## Encerramento

O autor menciona ter feito um vídeo exclusivo para membros do canal mostrando como ler o header desse arquivo (o cabeçalho do arquivo zipado), e estar preparando outro vídeo exclusivo sobre como implementar a árvore binária de Huffman em código. Pede comentários para saber se vale a pena um vídeo dedicado só ao LZ77/algoritmo deflate, e reforça que conteúdo técnico historicamente engaja menos no canal.
