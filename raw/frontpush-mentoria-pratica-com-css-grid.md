# Mentoria: Prática com CSS Grid

Então vamos lá, vamos dar um review de, por exemplo, construir um layout desse aqui. Tipo assim, estou utilizando CSS Grid. Primeiro vou explicar por que é mais complicado, por exemplo, você fazer isso com flexbox, que com Grid sai bem mais fácil.

Então, primeira coisa, crie aqui uma pastinha. Vou criar aqui um index.html, HTML5, vamos aqui dar um zoom e uma pastinha chamada CSS, new file style.css, vamos fazer o link do CSS aqui, CSS barra, ver se já está funcionando.

Vamos aplicar aqui o hack para poder tirar o margin, o padding de todos os elementos, box-sizing, border-box, no body, width 100%, height 100, background-color, 07, 07, 07, a gente starta o SAS e vamos abrir isso aqui para ver.

Então está aí, já está funcionando o meu sistema.

## Grid container e grid itens

Então a primeira coisa que eu quero fazer aqui é criar uma div, uma seção, uma section com o nome de container, porque da mesma forma que a gente faz com o flexbox, a gente precisa de um container pai, que ele vai ser tipo o grid pai, o grid container, e todos os filhos diretos viram grid itens, do mesmo jeito que a gente fazia com o flexbox, define o container pai como flex container, e aí automaticamente os filhos diretos dessa div viram flex itens, então é a mesma coisa aqui com o display grid.

Só que o que acontece? Por que seria tão difícil a gente fazer esse layout aqui utilizando o CSS Grid? O CSS Flexbox, porque o CSS Flexbox é unidimensional, então sempre quando a gente está fazendo um layout em que ele é composto por linhas, onde não tem, por exemplo, linhas e colunas sendo mescladas, a gente faz com o flexbox, mas qual o problema desse layout aqui? Aqui ele não é composto só de linha, está vendo? Vem uma linha aqui, só que ela é mesclada, então isso aqui dá para fazer com o flexbox? Dá, só que eu vou fazer flexbox dentro do flexbox, que fica dentro do flexbox, vai virando uma salada, então quando a gente mexe com duas dimensões, mesclando linhas e colunas, é melhor o CSS Grid, quando é só uma dimensão, a gente faz com o flexbox, que é mais fácil.

## Linhas, colunas e áreas no Excel

Então a primeira coisa que a gente tem que pensar é justamente em linhas e colunas, eu vou abrir aqui o Excel só para poder facilitar o entendimento, por exemplo, quando eu quero mesclar uma linha e uma coluna, o que eu faço? Eu quero, por exemplo, pintar todas as bordas, eu quero mesclar essas duas células, eu seleciono elas e eu quero que essas quatro células virem uma só, concorda comigo? Eu aperto mesclar e centralizar, ele automaticamente pinta elas todas.

Então isso aqui, A1 e A2, B1 e B2 viram uma área só, é como se eu definisse, sei lá, a área 1, isso aqui é a área 1, e eu quero que isso aqui seja a área 2, do C1 até C5, até o F1 até o F5, então olha só, eu defini várias células pequenas, venho aqui, mesclar e centralizar, e eu digo que essa aqui é a área 2, sacou? E aí eu venho aqui, defini essa aqui como outra área, então eu clico e seleciono, mesclar e centralizar, venho aqui, mesclar e centralizar, e aqui, mesclar e centralizar.

Então viu aí como é que a gente faz? A gente mescla linha e coluna, então o CSS Grid é exatamente a mesma coisa.

Então como é que eu vou mesclar e centralizar? Você tem que pensar isso aqui como se fosse uma tabela cheia de células pequenas, se você visualizar bem, a gente pode dividir em uma linha, você vai pegar sempre o menor elemento, o menor elemento é esse Figma aqui, então toma ele com o tamanho de uma linha, se eu pegar ele, aqui vai dar uma linha e aqui outra linha, então aqui dá mais ou menos duas linhas, e aqui embaixo duas linhas também, então são cinco linhas, então eu posso vir aqui, vou pegar aqui vermelhinho, deixar 5% bem de leve, primeira linha, segunda linha, terceira linha, quarta linha, quinta linha, a gente meio que já conseguiu desenhar o nosso layout.

Agora a gente precisa das colunas, as colunas do mesmo jeito, isso aqui é uma matriz 5 por 5, então a gente define essa coluna, essa coluna aqui do meio, essa coluna aqui do meio e essa coluna aqui. Aqui você poderia ter colocado seis colunas, que ela está mais esticada e tal, sim, mas como elas são vizinhas, quando você mandar mesclar e centralizar é a mesma coisa, então você pode deixar 5 por 5 assim, sem problema, porque quando você vai mesclar isso aqui, mescla aqui, vai juntar tudo, mescla aqui, vai juntar tudo também, então vai ficar meio que dando na mesma, mas se você quiser realmente, você pode colocar seis, não tem problema nenhum, mas vamos fazer 5 por 5, você percebe que esse aqui é uma célula 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25. Então, 5 por 5 eu tenho 25 células, mas percebe que a área de cores, ela detém de 1, 2, 3, 4, 5, 6, tem 6, só que eu vou mesclar e centralizar essa lista aqui, vou pintar, sei lá, de verde para vocês visualizarem.

Então, eu vou mesclar e centralizar todas essas aqui e eu vou chamar essa área de A, área A, você pode chamar da área que você quiser, eu estou chamando de A, vou pegar todas essas áreas aqui, está vendo, e vou definir esse aqui como B, B, venho aqui, defino essas aqui como C, vou definir o Figma pequeno como D, ele só ocupa uma célula, então venho aqui a letra D e por último, para poder selecionar, eu defini essas aqui como letra E, está entendendo até agora?

Sim, tranquilo.

Aí você define primeiro essas áreas, a primeira coisa é você dividir o seu layout dessa forma aqui para poder a gente conseguir desenhar isso, então vamos lá, uma vez que eu defini isso, agora eu venho aqui e vou definir a minha class container, o que eu vou estilizar nela?

## Estilizando o container e os itens

.container, primeira coisa eu vou definir nele um max-width, sei lá, de 1440 pixels e um margin zero auto. Vou dar um background-color para ele de hashtag 090909 e um border, um px solid, só para poder a gente visualizar o container, a gente não está vendo porque ele não tem altura, então se eu definir aqui a 700 pixels, está aí, está enxergando agora, então está aqui o nosso container, já está aqui, eu vou dar um padding no body, só para poder a gente visualizar o container, vou deixar, sei lá, 24 pixels em cima e embaixo, 16 de um lado e de outro, só para poder a gente visualizar o nosso container aqui certinho, sem precisar ficar colado.

E aí eu vou definir agora os itens aqui dentro, então eu vou definir div, vou dar o nome dela de item A, item B, item C, item D e item E, e eu vou estilizar agora as minhas seções com base nesse desenho que a gente acabou de fazer aqui.

Só vou colocar aqui dentro um h1 falando cores, um parágrafo aqui lorem ipsum, só para poder a gente ter um conteúdo e preencher para não ficar totalmente vazio, e vou lá no Google Fonts rapidão, Google Fonts. Pegar o Roboto, a gente seleciona algumas fontes aqui, Ctrl C, Ctrl V e o font-family aqui, e vamos estilizar aqui, h1, a gente coloca o font-family, coloca color white e o parágrafo da mesma forma, esse mesmo font-family, só que nós vamos colocar um cinza 555, para ver como está ficando, vamos salvar aqui, cores, está lá, todos os itens, eu vou fazer isso, então primeiro cores, depois, sei lá, interface, interface, aí eu tinha colocado aqui tipografia, o item D era o Figma, vamos lá, Figma, e aqui era elementos, então todos eles vêm colocados em display block, então fica um embaixo do outro certinho.

Vamos agora estilizar os itens, item A, o item B, item C e tudo mais, então primeiro eu quero aplicar para todos uma classe item, é mais fácil, item, item, item, item, salvei e eu vou estilizar aqui item.

Vou deixar aqui um background-color, hashtag 0B, 0B, 0B e um border do mesmo jeito, mas nele eu vou aplicar também um padding, só para poder a gente deixar a interface respirando, coloca 16 pixels, 16 pixels de todos os lados, está legal, então está aí.

## display grid, grid-template-areas e grid-area

Vou colocar também o margin, vou deixar o margin para aplicar no display grid, melhor, então vamos lá, agora que a gente vai começar a definir todas as áreas utilizando display grid, como é que a gente faz?

O display grid a gente vai aplicar no container, no pai, então a gente vem aqui e aplica display grid, automaticamente o que acontece? Acontece que todos os elementos vão preencher o tamanho do container, automaticamente, quando você aplica o display grid, ele meio que parece que está no display block, porque continua um elemento embaixo do outro, por padrão, não é que nem o display flex, que quando você aplica fica um do lado do outro, aqui fica um embaixo do outro, normal, como se tivesse em display block, aí você vê que ele preencheu toda a área, então o display grid faz isso aí, e o que a gente vai definir é o grid-template-areas, onde nós vamos escrever uma matriz 5 por 5, então a gente vem aqui e nós vamos literalmente escrever isso aqui, as células, então as três primeiras células, não é a letra A, então faço AAA e aqui eu faço BB, então faço AAABB, foi a primeira linha, aí eu posso fazer ele sequencial, posso continuar escrevendo aqui, mas é bom a gente se colocar sempre em forma de matriz para a gente visualizar como está ficando, aí mais uma vez eu faço AAABB, está vendo? BB, aqui embaixo eu faço CCEEE, copio e colo aqui, faço CCEEE e mais uma vez eu faço CCEEE, então já tem uma matriz 5 por 5 definindo esse sistema de grid aqui, está vendo?

E aí simplesmente eu tenho que indicar quem é quem, então eu tenho o item A, o item B e tudo mais, então vamos lá, eu defino que o item A tem o grid-area, quem ele é? É o A, enquanto o B é o B, o C é o C, quando você salva, automaticamente ele já desenhou para você, certinho, eu quero uma distância entre os elementos, aí você coloca o grid-gap, você coloca 16 pixels, então 8 pixels, vai ter uma distância de 8 pixels entre os grids, 8 pixels, 16 pixels, ele já fica responsivo, ele vai manter esse layout até nos menores, se eu quero facilitar para o mobile eu desenhar um novo layout, é o que você faz?

## Novo layout com media query

Você dá um max-width, ou um media, você faz aqui um media screen e max-width, dá 960 pixels, e aí você vai definir um container aqui dentro, onde você vai mudar o grid-template-areas, eu quero mudar de uma matriz 5 por 5 para uma 4 por 4 e eu quero que ele fique um do lado do outro e tudo mais, então é só você modificar aqui que ele vai ler o novo grid-template-areas e vai aplicar, e aí você tem como construir esses layouts de grids para galerias de forma bem mais fácil, fechou?
