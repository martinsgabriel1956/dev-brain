# Por que letras minúsculas economizam dados

Por que letras minúsculas economizam dados. Eu sei que muitos de vocês gostam de "escovar bits", então achei que seria interessante reagir a esse artigo aqui.

Letras minúsculas e maiúsculas usam a mesma quantidade de dados, um byte cada uma. Então é surpreendente saber que trocar letras maiúsculas por minúsculas economizaria dados. Por exemplo, eu peguei a página principal do Hacker News e reescrevi os títulos de cada artigo em "no case"/"sentence case" (que seria apenas a primeira letra maiúscula, ao invés de ser tudo "title case", que seria a primeira letra de cada palavra maiúscula), reduzindo assim o tamanho em 31 bytes.

Então aqui está o sentence case, que seria "The cat sat on the mat" usando apenas o T maiúsculo, e o title case, que seria cada letra inicial de cada palavra maiúscula.

Como é que pode ser verdade que trocar algumas letras maiúsculas por minúsculas economizaria dados? Essa é uma ótima pergunta, porque se a gente abrir aqui o terminal e fizer "Lucas Montano" (do canal Lucas Montano) e salvar isso num arquivo .txt, e depois converter tudo para lower case e tudo para upper case, a gente tem dois arquivos: um com toda a frase em lower case e um com toda a frase em upper case.

Se eu fizer `wc -c lowercase.txt`, o tamanho do arquivo está em 37 bytes. Agora se eu fizer `wc -c uppercase.txt`, o tamanho do arquivo também está em 37 bytes. Um está tudo em letra maiúscula e o outro está tudo em letra minúscula.

Então como pode ser verdade que mudar algumas letras de maiúscula para minúscula, no caso da página do Hacker News, conseguiu reduzir 31 bytes no tamanho do arquivo?

A resposta é **compression** (compressão/compactação). Não é intuitivo, mas assim que a gente entende como um texto é comprimido, começa a fazer sentido. Esse artigo ajuda a entender como funciona a compactação de texto usando exemplos interativos. O autor mostra como chegou à conclusão de que usar title case nas notícias do Hacker News emite carbono anual equivalente a um carro percorrendo toda a largura do Sri Lanka, e mostra exemplos de onde esse conhecimento pode ser usado para economizar dados sistematicamente.

## Por que letras minúsculas economizam dados

A compactação de texto é mais eficaz quando há uma variedade menor de caracteres no texto: caracteres menos comuns são usados com menos frequência, e caracteres ou grupos de caracteres são repetidos com mais frequência. Substituir caracteres maiúsculos por seus equivalentes minúsculos ajuda nesses três pontos, o que traz eficácia na compactação. Para entender por que isso funciona, é preciso entender como funciona a compactação.

## Como funciona a compactação de texto

Para explicar como funciona a compactação de texto, o artigo examina especificamente o algoritmo **deflate**, comumente usado em arquivos zip. Os princípios são os mesmos para outros algoritmos.

O gzip é baseado no deflate algorithm, que é uma combinação de **LZ77** e **Huffman coding**. Fazendo um gzip nos arquivos `lowercase.txt` e `uppercase.txt` criados antes (salvando como `lowercase.txt.gz` e `uppercase.txt.gz`), agora dá para comparar o tamanho dos dois arquivos compactados — antes de compactar o tamanho era igual.

Fazendo `wc -c uppercase.txt.gz`, o tamanho está em 61 bytes. Fazendo o mesmo para `lowercase.txt.gz`, o tamanho também está em 61 bytes. Testando com um texto maior (Lorem Ipsum, salvo em maiúscula e minúscula) para ver a diferença na compactação: isso mostra que nem sempre vale a pena — não é porque a compactação é mais eficiente com letras minúsculas que você deve começar a escrever tudo em minúsculo no seu código ou na sua página HTML.

Com um texto maior em letra maiúscula e letra minúscula, zipando os dois: o arquivo compactado de letra maiúscula ficou com 575 bytes, e o arquivo compactado de letra minúscula ficou com 574 bytes — uma economia de 1 byte nesse texto de exemplo.

## Codificação Huffman

O algoritmo de deflate começa com o Huffman encoding. Cada caractere em um arquivo de texto descompactado utiliza a mesma quantidade de dados — isso não é exatamente verdade, mas é verdade o suficiente para a explicação. Em UTF-8 isso é 8 bits (um bit é um binário, um ou zero). Um arquivo de texto usando UTF-8 codifica as letras assim (exemplo de cada letra).

Pegando uma palavra que use apenas quatro caracteres distintos, por exemplo "baobab": usando UTF-8, o texto "baobab" é codificado com 8 bits por caractere. Se soubermos que não precisamos de outras letras, podemos economizar dados alterando a codificação para usar menos bits: poderíamos mudar "B" maiúsculo para `10` e "b" minúsculo para `11` (por exemplo), e o texto compactado ficaria menor.

A palavra "bbab" contém quatro caracteres distintos — o melhor que podemos fazer é dar a cada um deles uma sequência de dois bits. Mas se "B" maiúsculo virar "b" minúsculo, teremos apenas três caracteres distintos e poderemos dar um passo adiante: poderíamos alterar a codificação para que o caractere usado com mais frequência (o "b" minúsculo) seja representado por apenas um bit, reduzindo a versão compactada de "baobab" para um binário ainda menor do que o mostrado antes. Fazemos isso usando o **Huffman encoding**: com ele, podemos representar caracteres usados com mais frequência com menos bits.

O artigo tem uma explicação interativa: digite um texto para ver suas formas binárias, compactada e não compactada. Exemplo com "Lucas Montano": binário não compactado 13 bytes, compactado usando codificação Huffman 5 bytes e 3 bits.

Para compactar um texto usando a codificação Huffman, primeiro é preciso construir uma tabela de frequência de todos os caracteres no texto: contar o número de ocorrências de cada caractere e ordená-los por frequência. Por exemplo, na palavra "Lucas Montano", o "n" aparece duas vezes, o "o" aparece duas vezes, o "a" aparece duas vezes, e assim por diante.

Depois construímos uma **árvore de Huffman**, seguindo estas regras:
1. Transforme cada caractere numa folha da árvore.
2. Pegue os dois caracteres (ou nós) com menor frequência e conecte-os com um nó.
3. Dê a esse nó a combinação das frequências das duas folhas/nós conectados.
4. Remova as duas folhas da lista e substitua pelo nó de conexão delas.
5. Repita o passo a passo até sobrar um único nó raiz.

É um pouco complicado no início, mas depois de pronto forma um diagrama em árvore, onde cada letra é uma folha, e a combinação de duas com a menor frequência forma um nó (por exemplo, "a" e "o" que têm frequência de 2 cada formam um nó com soma 4, e assim por diante em estrutura de árvore).

Podemos usar a árvore para descobrir a nova codificação de cada caractere: para determinar a codificação de um caractere, começamos no topo da árvore e descemos em direção ao caractere. Cada vez que descemos para a esquerda, adicionamos um zero; cada vez que descemos para a direita, adicionamos um um. Os caracteres que aparecem com mais frequência no texto exigem uma descida mais curta na árvore e, portanto, podem ser codificados com menos bits.

### Mais economia com árvores menores

Não podemos decodificar Huffman coding sem a árvore — então quando enviamos texto compactado com Huffman coding, enviamos a árvore junto. Ao usar menos letras maiúsculas no texto, aumentamos a chance de não haver nenhuma instância de letra maiúscula, ou seja, a árvore que enviamos também fica menor.

Por exemplo, se transformarmos um "a" minúsculo em maiúsculo, a árvore fica maior, porque o "A" maiúsculo precisa ser listado como uma folha separada. Ao invés de ter uma única folha "a" com frequência 2, passamos a ter duas folhas (um "A" maiúsculo e um "a" minúsculo), cada uma com frequência 1 — isso aumenta o tamanho da árvore e, consequentemente, torna a decodificação mais trabalhosa.

## LZSS / LZ77 (deflate)

O deflate também usa outro método de compactação: compacta os dados com Huffman coding e depois novamente usando o algoritmo **Lempel-Ziv-Storer-Szymanski (LZSS)**, uma variante do LZ77. Esse algoritmo funciona encontrando pedaços repetidos de dados e substituindo-os por uma referência mais curta à primeira vez que apareceram. A referência é feita substituindo a sequência repetida por um **ponteiro**, que consiste em dois números: o primeiro diz quanto tempo devemos voltar para encontrar a sequência original, e o segundo diz quanto tempo a sequência original tem.

Testando com "Lucas Montano" repetido: codificando usando LZSS, o tamanho ficou o mesmo para uma única ocorrência, mas ao adicionar mais repetições no final, o tamanho reduz — o ganho vem do intervalo dos ponteiros.

## Quantos dados podem ser salvos com letras minúsculas

Antes de começar a colocar tudo em letras minúsculas, é importante lembrar que existem "criminosos" muito piores em termos de desperdício de dados online — por exemplo, imagens não otimizadas, vídeos com reprodução automática, JavaScript não utilizado. Então primeiro faça essas melhorias antes de pensar em reduzir letras maiúsculas por minúsculas. Ainda assim, letras minúsculas são surpreendentemente eficazes.

### Exemplo: Hacker News

Substituindo maiúsculas e minúsculas por sentence case no Hacker News: peguei a primeira página do Hacker News e reescrevi o título de cada artigo em sentence case ao invés de title case. Cada arquivo HTML tinha exatamente o mesmo número de caracteres, mas quando compactado em arquivo zip, o arquivo em title case tinha 5.000 bytes e o arquivo em sentence case tinha um pouco menos — uma economia de 31 bytes. Talvez não seja muito, mas é um bom efeito colateral de tornar os títulos mais fáceis de ler (tudo em minúsculo também torna a leitura mais fácil).

Usando a fórmula fornecida pelo Sustainable Web Design, para cada visita ao Hacker News economizaríamos uma fração de gramas de carbono ao usar sentence case. Supondo que o Hacker News receba cerca de 10 milhões de visitas por dia, mudar para sentence case resultaria na prevenção de 105g de carbono diariamente — equivalente a queimar 4,3 galões de gasolina por ano, combustível suficiente para dirigir um Mini Cooper aproximadamente na largura do Sri Lanka.

### Código sistematicamente minúsculo

Em código que não diferencia maiúsculas de minúsculas, alguns minificadores automaticamente convertem código para minúsculas para economizar alguns bytes após a compactação — mas isso não é comum nem aplicado de forma consistente. Minificadores reduzem o tamanho do arquivo de código sem alterar seu funcionamento; qualquer otimização individual de um minificador provavelmente é pequena demais para se preocupar, mas coletivamente elas economizam muitos dados, tornando os sites mais rápidos e consumindo menos energia.

Por exemplo, muitos arquivos HTML começam com uma declaração de tipo de documento em maiúscula, como `DOCTYPE HTML`, mas a especificação HTML5 afirma que isso não diferencia maiúsculas de minúsculas — então um minificador de HTML poderia economizar dados alterando isso para tudo minúsculo.

Alguns exemplos de código que permitem letras minúsculas: cores hexadecimais, codificação de caracteres, expoentes em JavaScript, atributos de idioma, comandos de caminho SVG, entre outros.

## Conclusão

Vale reforçar que, antes de se preocupar com a árvore de Huffman, é melhor começar preocupando-se se as imagens estão otimizadas e se há um cache decente no site — porque, ao invés de economizar alguns bytes "escovando" a árvore de Huffman, é possível salvar dezenas de megabytes ou gigabytes, principalmente parando de usar JSON de forma ineficiente.
