---
title: "A História dos Formatos de Imagem: TGA, GIF, JPEG, PNG, WebP, HEIC, AVIF e Mais"
source_url: ""
author: "desconhecido (canal YouTube)"
date_published: "desconhecido"
date_ingested: 2026-07-29
type: transcript
language: pt-BR
tags: [formatos-de-imagem, compressao, computacao-grafica, jpeg, png, gif, svg, webp, heic, avif, raw, tiff]
---

# A História dos Formatos de Imagem

> Nota: vídeo contém um trecho patrocinado (ChatLLM da Abacus.AI) inserido entre a seção do GIF e a do JPEG. O CTA comercial foi mantido por completude, mas não é o foco técnico da ingestão.

Você já reparou que praticamente toda imagem termina com uma sigla estranha — PNG, JPEG, GIF, SVG, WebP? À primeira vista todos parecem fazer exatamente a mesma coisa, mas a realidade é bem diferente: cada formato de imagem foi criado para resolver um problema específico. Alguns priorizam qualidade, outros economizam espaço, alguns suportam transparência, outros animações. E existe um detalhe que quase ninguém conhece: se colocarmos todos esses formatos em ordem de lançamento, eles contam praticamente a história da própria computação gráfica.

A seguir, os principais formatos de imagem que existem, em ordem cronológica — incluindo por que alguns são formados por milhões de pixels e outros por equações matemáticas complexas.

## TGA (1984)

O primeiro formato da lista. Enquanto muitos computadores ainda mal exibiam 16 cores, o TGA já havia sido criado para aplicações profissionais. Seu grande diferencial era o **canal Alfa** — uma camada extra responsável pela transparência. Isso o tornou um dos formatos preferidos para texturas, efeitos visuais e modelagem 3D.

A qualidade era tão boa que ele virou o padrão da indústria dos games, e continua vivo até hoje: arquivos de jogos como Counter-Strike ainda escondem milhares de arquivos TGA nas texturas de cenários e personagens. Mesmo com mais de 40 anos, continua sendo uma peça invisível da história dos videogames.

## PCX (1985)

Ficou famoso por ser o formato nativo do PC Paintbrush, programa que mais tarde deu origem ao Microsoft Paint. Sua maior inovação foi a **compressão RLE (Run-Length Encoding)**: se uma imagem tivesse 50 pixels brancos seguidos, em vez de gravar "branco" 50 vezes, o arquivo armazenava apenas "repita branco 50 vezes". Esse método reduzia bastante o tamanho de imagens com grandes áreas da mesma cor.

O PCX ainda permitia armazenar várias páginas em um único arquivo, funcionando quase como um PDF extremamente primitivo. Na metade dos anos 80, para muitos usuários de PC, ele era praticamente o álbum de fotos do computador.

## BMP (1986)

Lançado pela Microsoft, talvez seja o formato mais simples de toda a lista. O BMP não tenta economizar espaço — não usa compressão, simplesmente grava cada pixel exatamente como ele existe. O problema é que gera arquivos enormes: uma foto de apenas 2 MB em JPEG pode facilmente passar de 50 MB em BMP. Hoje praticamente não existe motivo para utilizá-lo, exceto em aplicações muito específicas, mas foi exatamente assim que tudo começou — sem compressão, sem otimizações, apenas armazenando cada pixel da imagem.

## GIF (1987)

Criado pela CompuServe durante os primeiros anos da internet. Na época foi revolucionário: além de comprimir imagens de forma eficiente, foi um dos primeiros formatos a suportar animações — algo essencial quando praticamente o mundo inteiro usava internet discada. O problema era a limitação de apenas 256 cores, por isso fotografias e imagens com muitos degradês nunca ficaram muito boas nesse formato.

Curiosidade: o GIF nunca desapareceu. Mesmo que hoje muitas plataformas usem pequenos vídeos muito mais eficientes, praticamente todo mundo continua chamando essas animações de "gifs" — o nome do formato virou o nome da própria ideia, algo que pouquíssimas tecnologias conseguem. Existe também uma discussão famosa sobre a pronúncia: o criador dizia que o correto era "jif", igual à marca americana de pasta de amendoim, enquanto a maioria continua dizendo "gif" com o G — e qualquer uma das duas sempre irrita alguém.

## JPEG (1992)

Provavelmente o formato de imagem mais utilizado do planeta. O objetivo era resolver um único problema: como reduzir drasticamente o tamanho de uma imagem sem que as pessoas percebam diferença na qualidade. Para isso, o JPEG utiliza **compressão com perdas** — remove informações consideradas pouco importantes para o olho humano. Ele divide a foto em pequenos blocos de 8x8 pixels e comprime cada um separadamente. Na maioria das vezes o resultado é praticamente imperceptível: uma foto de 10 MB pode virar um arquivo de apenas 2 MB mantendo aparência muito parecida.

O problema aparece quando a mesma imagem é editada e salva várias vezes: a cada novo salvamento, o JPEG aplica outra compressão e perde ainda mais qualidade. Por isso fotógrafos sempre trabalham no arquivo original e só exportam para JPEG no final.

Curiosidades:
- **JPG e JPEG são exatamente o mesmo formato** — a diferença de extensão existe apenas porque versões antigas do Windows aceitavam extensões com no máximo três letras.
- Arquivos JPEG armazenam metadados **EXIF**, que podem incluir a câmera utilizada, a data da foto e até as coordenadas de GPS de onde ela foi tirada — dependendo de onde a imagem é compartilhada, isso pode revelar a localização de quem tirou a foto sem que a pessoa perceba.

### Tentativas de sucessor: JPEG 2000 e JPEG XL

O **JPEG 2000** (anos 2000) entregava melhor qualidade e compressão, mas fracassou porque o JPEG tradicional já estava presente em praticamente todos os computadores do mundo. Mais recentemente, o **JPEG XL** (2021) suporta transparência, animações e compressão ainda melhor — tecnicamente excelente, mas com o mesmo problema de adoção: muitos navegadores e programas ainda estão decidindo se vão adotá-lo como novo padrão.

## PNG (1996)

Uma das histórias mais curiosas da lista. Tudo começou quando a empresa dona da patente do algoritmo do GIF anunciou que desenvolvedores passariam a pagar royalties para utilizar o formato — e a internet respondeu com um "não". Pouco tempo depois nasceu o PNG: totalmente gratuito, de código aberto e livre de patentes.

O grande diferencial do PNG é utilizar **compressão sem perdas** — nenhuma informação é descartada, e todos os pixels permanecem exatamente iguais ao arquivo original quando reaberto. Por isso é perfeito para logotipos, ícones, capturas de tela e qualquer imagem com textos ou bordas bem definidas. Também suporta **transparência verdadeira**, permitindo colocar uma imagem sobre qualquer fundo sem o famoso quadrado branco ao redor. A desvantagem é o tamanho dos arquivos: comparado ao JPEG, um PNG costuma ocupar muito mais espaço, e para fotografias essa diferença normalmente não compensa. Existe também o **APNG**, a versão animada do PNG, mas praticamente ninguém lembra dela.

## TIFF (1986)

Criado para uso profissional, utiliza compressão sem perdas, suporta múltiplas camadas, profundidade de cor extremamente alta e preserva absolutamente todos os detalhes da imagem. É por isso que fotógrafos, gráficas e estúdios utilizam TIFF quando precisam arquivar imagens sem perder qualidade. O preço dessa fidelidade: arquivos extremamente grandes. Dificilmente é usado no dia a dia, mas nos bastidores da fotografia profissional continua sendo um dos formatos mais importantes.

## RAW

Apesar de muita gente pensar que o RAW é um formato de imagem pronto, na verdade ele nem é uma imagem finalizada — é o conjunto de dados capturados pelo sensor da câmera antes de qualquer processamento. Contraste, nitidez, saturação, balanço de branco e até as cores finais ainda não foram definidos.

O RAW não é um único formato: cada fabricante tem a própria versão — Canon usa CR2, Nikon usa NEF, Sony usa ARW, e a Adobe criou o **DNG** numa tentativa de padronizar todos eles. A grande vantagem é oferecer muito mais liberdade na edição: como praticamente todas as informações originais estão presentes, é possível recuperar sombras, ajustar exposição e alterar cores com muito mais qualidade do que em um JPEG. Por isso fotógrafos profissionais quase sempre fotografam em RAW antes de exportar a imagem final.

## SVG (2001)

Criado pelo World Wide Web Consortium (W3C), o mesmo grupo responsável pelos padrões da própria internet. Funciona de forma completamente diferente dos formatos anteriores: enquanto JPEG, PNG e GIF armazenam milhões de pixels, o SVG armazena apenas **instruções matemáticas** — em vez de dizer qual cor existe em cada pixel, ele descreve linhas, curvas, formas geométricas e preenchimentos. É como ensinar o computador a desenhar a imagem em vez de simplesmente armazená-la.

Isso traz uma vantagem enorme: um SVG pode ser ampliado infinitamente sem perder qualidade — um ícone pode ter 32 pixels ou ocupar um outdoor inteiro e continuar perfeitamente nítido. Por isso praticamente todos os sites modernos utilizam SVG para logotipos, ícones e elementos de interface: além de ocupar pouco espaço, se adapta perfeitamente a qualquer resolução de tela.

## WebP (2010)

Apresentado pelo Google. Na época, a internet usava JPEG para fotografias, PNG para transparência e GIF para animações — a ideia do Google foi criar um único formato capaz de fazer tudo isso. O WebP suporta compressão com perdas e sem perdas, transparência e animações, e na maioria dos casos gera arquivos entre 20% e 30% menores que JPEG ou PNG mantendo praticamente a mesma qualidade.

No começo muita gente enxergou o WebP apenas como mais um padrão imposto pelo Google, e navegadores/programas demoraram anos para adotá-lo. Hoje essa discussão praticamente acabou: quase todos os navegadores oferecem suporte nativo, e muitos sites convertem automaticamente as imagens para WebP sempre que o navegador é compatível — tornando-o um dos formatos mais usados na internet moderna, mesmo sem que os usuários percebam.

## HEIC (~2015)

Criado pelo Moving Picture Experts Group (MPEG), o mesmo grupo responsável por diversos codecs de vídeo modernos. Ganhou fama em 2017 quando a Apple passou a utilizá-lo como formato padrão das fotos do iPhone. HEIC significa *High Efficiency Image Container* — em vez de usar uma compressão antiga como o JPEG, aproveita tecnologias modernas desenvolvidas originalmente para vídeo. Resultado: imagens ocupam muito menos espaço sem perda de qualidade perceptível, além de suportar maior faixa de cores (HDR) e preservar mais detalhes.

A Apple adotou o formato por um motivo prático: câmeras de celular melhoraram muito, as pessoas passaram a tirar milhares de fotos, e o armazenamento interno começou a acabar mais rápido. O maior problema do HEIC é a **compatibilidade** — nem todos os dispositivos ou programas conseguem abri-lo. Por isso o próprio iPhone geralmente converte a foto para JPEG automaticamente ao compartilhar, mas nem sempre — daí a clássica mensagem "não consigo abrir essa imagem".

## AVIF

Assim como o HEIC, nasceu da tecnologia usada em vídeos: utiliza o codec **AV1**, criado para oferecer uma das melhores compressões já desenvolvidas. A ideia: se um vídeo nada mais é do que uma sequência de imagens, por que não usar essa mesma tecnologia para comprimir uma única imagem? Hoje o AVIF oferece arquivos muito menores que JPEG e PNG mantendo praticamente a mesma qualidade, além de suportar transparência, HDR, maior profundidade de cores e produzir menos artefatos de compressão — reunindo, na teoria, praticamente todas as vantagens dos formatos modernos.

O problema, mais uma vez, foi a adoção: navegadores e programas de edição demoraram para dar suporte, e poucas pessoas trocam de formato sem um motivo forte. Essa situação está mudando lentamente — os principais navegadores já suportam AVIF, e grandes plataformas já utilizam o formato silenciosamente nos bastidores.

## PDF (não é um formato de imagem)

Apesar de muita gente tratar um PDF como se fosse uma imagem, na verdade não é um formato de imagem — funciona como um **contêiner de documentos**. Em vez de armazenar apenas uma fotografia, guarda todas as informações necessárias para montar uma página exatamente da mesma forma em qualquer computador ou impressora: textos, imagens, gráficos, tabelas, vetores, fontes e diversos outros elementos podem coexistir dentro de um único PDF. Um PDF pode conter dezenas de imagens diferentes — e é justamente essa capacidade de preservar o layout original que o transformou em um dos formatos mais usados do mundo para contratos, livros digitais, apostilas e documentos profissionais.
