# Otimização de imagens, parte 1: SVG, WebP e lazy loading

Olá, fala pessoal, sejam bem-vindos aí à nossa terceira aula de otimização de webpages, do qual a gente já conversou sobre minificar os arquivos CSS, já explicamos o porquê dentro do console, já falamos de quando utilizar CDN ou não, o que você tem que pesar para poder realizar a sua decisão, não utilizar arquivos inline e nem incorporado, vamos tentar sempre priorizar arquivos externos para poder a gente utilizar do benefício do cache, e agora a gente vai falar muito sobre imagens, muito sobre imagens e SVGs, então essa aula vai ser dedicada a gente explicar um pouco mais dessas características, o que a gente tem que levar em consideração, quais são os melhores formatos hoje em dia.

## Dá para vetorizar?

Primeira coisa pessoal, sempre, tem PNG no seu site? Tem JPG? Tem PNG, tem JPG? Primeira coisa que você tem que se perguntar, isso aqui a gente dá para transformar em um vetor? Primeira coisa que você tem que se perguntar, você tem como transformar isso aí em um vetor? Se não, porque, ah, é uma fotografia, não tem como transformar em um vetor? Até tem, mas às vezes você transforma em base64, não vale a pena, porque fica um código tão estrondoso de gigantesco, que às vezes nem vale a pena. E aí, quando for fotografia, otimiza a fotografia.

Se não for fotografia, se for algo que você olha assim, cara, isso aqui dá para vetorizar? Vetorize, utiliza SVGs. Ah, não, se é uma fotografia, não tem como, beleza, utiliza o PNG ou o JPG. Já já a gente vai falar sobre isso, que o melhor hoje em dia é o WebP.

Mas, tem que utilizar PNG ou JPG, você vai nesse site aqui, TinyImage, TinyImage, que é o do panda aqui. Então, você vai conseguir dropar os seus arquivos WebP, PNG ou JPG, beleza? E aí ele vai fazer a compressão para você. E notoriamente isso aqui já dá uma diferença do caramba, tá bom, pessoal?

Tem muita gente que, por exemplo, utiliza as imagens, às vezes do próprio Figma, você não faz a devida otimização, ou então não faz a adaptação, se aquilo ali é interessante, se você tem uma imagem específica carregada para o mobile, ou uma imagem específica carregada para o desktop, já já a gente vai falar sobre isso.

Mas, em via de regra, todas as imagens otimize, para poder ele fazer essa redução de tamanho, porque quando a gente fala de imagens na requisição, é uma das coisas que assim, se você resolver isso aqui, já resolve coisa de 60%, 70%, de verdade, tá? Tem muito site que se você só fizer isso aqui, só realizar esse passo, quando tem muitas imagens, já ajuda demais, entendeu? Já deixa o site outra coisa, beleza?

Ah, Násser, então, qual é a primeira coisa que você tem que se perguntar? É uma imagem que ele dá para vetorizar? É uma imagem de um logo? É uma imagem de uma ilustração? É uma imagem do quê? Dá para vetorizar? Tente vetorizar.

Ah, Násser, eu não sei como vetorizar. Então, você vai dar uma olhada lá nas aulas de Figma, tá bom? Onde eu explico como utilizar a Pen Tool, ou como utilizar, por exemplo, o plugin, o plugin que chama Image Tracer. Esse aqui, Image Tracer. Então, dá uma olhadinha, sempre que você puder.

Por exemplo, vou citar aqui um pequeno exemplo para vocês. Logo Adidas. Você vem aqui, lá nas imagens, logo Adidas. Ah, eu quero pegar essa imagem aqui e colocar no meu site, tá? Você está vendo que ela é uma imagem. Está vendo? Ela é uma imagem. Pessoal, isso aqui dá para vetorizar, isso aqui é uma logo. Então, o que você faz? Vem aqui no Image Tracer. Pei, transformei isso aqui de forma rápida, simples, maravilhosa. Está aqui, tudo vetorizado, está vendo aqui? Olha os pontinhos aí, está vendo os pontinhos? Está tudo vetorizado. O Image Tracer fez isso aqui para mim.

Então, sempre que você puder utilizar, utilize SVGs, que é indiscutível a diferença de SVGs para imagens. Eu sou da época que quando tinha ícone, eu utilizava imagens. Eu utilizava PNG quando era ícone. Hoje em dia, o SVG é mais leve e você pode esticar ele por ele ser vetor. Você pode esticar, ele não perde resolução. Então, pode estar executando. Mesmo no mobile, no desktop, o SVG vai ficar top. Então, sempre coloque o SVG.

Então, são ilustrações vetorizadas, são trechos de códigos que definem os elementos, cores e gradientes, ou seja, é texto, texto é muito mais leve. E por ser código, ele é manipulável pelo CSS e muito mais leve. Então, é indiscutível isso aqui.

## WebP

A NASA não tem como fazer otimização. Mas, mas, mas, mas, mas... Tem algumas formas de a gente melhorar mais ainda.

Primeira coisa, transformar para WebP. Então, literalmente, você vem aqui no Google, conversor de JPG para WebP. Está aqui. Vão aparecer um monte, que inclusive já estão roxinhos, que eu já visitei, onde eu estou fazendo essa adaptação nesse site aqui do Solten. Eu estou fazendo essa tradução do JPG e PNG para poder utilizar o WebP.

Porque o próprio Google, quando a gente faz aqui o Page Insights, se vocês darem uma olhadinha aqui, ele aqui, disponibilize imagens em formatos de última geração. O que ele está falando para mim? Pega todas as imagens que você tem em JPG e PNG e transforma em WebP. Então, o próprio Google vai recomendar isso aí para você. E é só essa conversão, já facilita demais.

## Lazy loading

Segunda coisa, colocar carregamento sob demanda. O que é o carregamento sob demanda? É o ponto que eu vou falar aqui no outro tópico. Utilize o recurso lazy loading.

Anteriormente, quando a gente não tinha esse recurso aqui de forma nativa, a gente tinha que, literalmente, pedir para o JavaScript verificar a distância da imagem para o topo da página. Então, o que a gente fazia? Eu já faço esse tipo de recurso tem um tempinho já. Só que antes ele não era nativo, então era mais chato da gente implementar.

O que a gente pedia? A gente sabe que, pela árvore DOM de elementos, cada elemento a gente consegue fazer a distância do elemento para o topo da página. Então, a gente consegue pegar isso em pixels. Vamos supor que você está em uma tela que ela é 1920x1080, ou seja, a altura da sua tela é 1080 pixels. Concorda comigo? Mas vamos supor que tem uma imagem que ela está lá embaixo, lá embaixo, lá embaixo, no site. Que ela está a uma distância de 2000 pixels. Você concorda comigo que quando você abrir o site pela primeira vez, essa imagem não vai aparecer?

Se ela não vai aparecer, por que eu vou dar esse trabalho para o browser fazer a requisição toda uma vez se eu nem sei se o usuário vai descer para lá? Então, é interessante a gente sempre fazer um recarregamento sob demanda.

O que a gente fazia anteriormente? A gente pegava essa distância e pedia para ele não renderizar, renderizar com SRC vazio. E aí, quando ele chegava a uma distância ali próxima, por exemplo, se eu estou falando de 1080 pixels, que é o tamanho da tela, quando ele chegava ali em 1500 pixels, ele ativava e passava o caminho daquela imagem e aí sim ele conseguiria renderizar, fazer o download daquela imagem.

Hoje em dia, mão na roda. O que você precisa fazer? Você só vai aplicar o termo loading lazy nas suas imagens. Então, aqui. Eu tenho um determinado logo. Ah, eu quero otimizar ela. Loading, você vai colocar lazy.

Isso aqui está sendo implementado de forma nativa em todos os browsers. Para poder você verificar se isso aqui está compatível com todos os browsers, é só você ir no site Can I Use. E dar uma olhada aqui em lazy. Então, lazy. Loading lazy. Então, aqui. Loading lazy. Loading via attribute for images and iframes. Então, dá para você utilizar em tags de imagem e iframes, que são as mais pesadas.

A gente vai utilizar muito desse recurso aqui quando a gente estiver fazendo as páginas, por exemplo, do drone. Então, do drone, vamos lá na imagem do drone, nasseryousef.com.br barra drone, que é o nosso site onde a gente vai usar e abusar dos elementos 3D, utilizando de iframes ou então dos elementos viewers, das tags viewers, para poder a gente utilizar desse recurso aqui. Então, estou fazendo um estudo bem maior de como a gente fazer a otimização quando a gente utiliza de muitos elementos 3D em páginas desse tipo, que utilizam desse tipo de recurso aqui. Beleza?

Então, como o próprio site aqui do Can I Use nos diz, isso ele diz, suportado em vários browsers já, tá vendo? Só você pegar aqui a versão, dá uma olhadinha em lazy loading.

E aí você faz isso, pessoal, para todas as imagens do seu site, tá bom? Sai colocando essa clausulazinha em todas as tags de imagem, imagens e iframes, que o próprio browser vai verificar a distância, o browser vai fazer todo esse cálculo e vai ver se vale a pena carregar ou não. Então, a gente estabelece um carregamento sob demanda e faz com que as requisições do seu site não sejam feitas sem necessidade, tá? Então, se o usuário estiver chegando naquela imagem, ela vai ser carregada de maneira tranquila.

Vocês podem ver que se eu abrir aqui o Solstheim, vamos lá, vamos abrir aqui, mais uma vez inspecionar, vamos aqui na aba Network e vamos começar a baixar aqui o nosso site. Olha só, carregou o vídeo agora. Vocês viram que não estava carregado? Carregou agora. Carregou o 5.png e o 8.png.

Nossa, você não fez as otimizações para transformar de WebP até agora, eu falei ainda não, tá? Mas olha só, conforme eu for baixando o meu site, ele vai fazendo as outras requisições. Tá vendo? Agora que apareceu os outros vídeos. Tá vendo? Conforme eu for descendo, ele vai carregando. É o carregamento sob demanda que ajuda demais na nossa performance. Beleza, pessoal?

Então, é isso. Essa é uma pequena aulinha para poder a gente falar um pouquinho mais sobre imagens e SVGs. E até a próxima.
