# Box model no CSS: margin, padding, bloco e inline, width, height e unidades de medida

Opa, fala pessoal, Násser aqui, sejam bem-vindos a mais uma aula de CSS, na aula de hoje a gente vai conversar um pouquinho sobre box-model, elementos de caixa.

Nas aulas passadas a gente falou um pouquinho sobre seletores, de como a gente seleciona os elementos do HTML no CSS para poder estilizar, beleza. A gente já está entendendo que o CSS serve para poder a gente fazer o estilo, a gente vai modificar a cor, modificar o posicionamento, modificar o espaçamento, modificar a fonte, tipografia, espaçamento entre os elementos, eu vou selecionar esses elementos e vou aplicar essas propriedades nele, de estilo em si, beleza.

## Tudo são caixinhas

Porém, vocês vão perceber, e eu já falei isso nas aulas passadas, que tudo aqui é caixa, tudo são caixinhas, pelo fato do HTML ser uma linguagem de marcação, toda marcação tem a sua respectiva tag, e a sua tag é uma caixinha, é uma div, e a gente precisa aprender quais são as principais propriedades quando a gente mexe com caixinhas, então a aula é para isso.

## Montando o exemplo: container e itens

Vamos criar aqui uma section onde a gente vai trabalhar essa propriedade. O nome dessa section aqui, pessoal, eu vou dar uma class para ela e ela vai se chamar container, class container. Dentro dessa class container, eu vou criar divs que têm um nome de item, então tem um item, tem um item, tem um item, está aqui. Então tenho três divs dentro dessa class container, nós vamos começar a estilizar isso aqui, section .container, eu estou falando da mesma div, do qual eu vou dar uma borda nela e eu sempre falo isso para todos os meus alunos, coloca borda na div para poder você enxergar o elemento, então você pode ver que ela está aqui, como não tem conteúdo nenhum dentro dela, ela está vazia.

Ao invés de colocar div itens vazios, eu vou colocar aqui um h1, eu vou colocar caixa um, aqui eu vou colocar caixa dois e aqui eu vou colocar caixa três, está aí. Deixe-me colocar aqui errado, caixa um, caixa dois, caixa três, se eu quero estilizar os meus h1 eu quero que ele tenha cor branca, então está aí, a gente acabou de fazer.

Agora, explicando os elementos de caixa, cada container tem uma class chamada item, então se eu vir aqui e chamar item e também dar uma borda para ele, vou dar um border solid green, vai perceber que cada caixinha tem a sua caixinha, sempre são caixinhas, você viu que independente de ser section, independente de ser div, independente de ser texto, sempre é uma caixinha.

## margin: o espaçamento de fora

Só que existem propriedades de espaçamento dessa caixinha, por exemplo, se eu vir aqui no item e utilizar uma propriedade chamada margin, ela define o espaçamento fora da caixa, e aí tem como eu dar espaçamento na parte de cima, dos dois lados e a parte de baixo, do qual, quando eu quero dar espaçamento na parte de cima, que é margin-top, eu vou colocar, por exemplo, 24 pixels, ou seja, em todas as caixinhas, na parte de cima da caixa, ela deu um espaçamento de 24 pixels.

Nossa, eu não entendi, porque todos espaçaram, então nós vamos selecionar somente o primeiro item, que é o quê? nth-child, ou seja, só a primeira caixa deu esse espaçamento, está vendo? Eu posso, por exemplo, colocar item e colocar borda nesse item, então está aí, só a primeira deu esse espaçamento, dá um espaçamento maior, 48 pixels, olha lá.

Ah, mas agora eu quero um espaçamento na parte direita, right, ou então left, ou então bottom, que é o espaçamento na parte de baixo, bottom, left, parte esquerda, right, parte direita, top, parte de cima.

E aí tem um modelo contraído dessas propriedades, que eu posso fazer, por exemplo, margin, eu quero dar um espaçamento de 12 pixels em cima e embaixo, então eu coloco assim, 12 pixels, e eu quero 24 pixels de um lado e de outro, eu coloco assim, 24 pixels, vocês entenderam?

## padding: o espaçamento de dentro e o sentido horário

E está dando espaçamento fora dessa caixa, isso aqui é a propriedade margin, que vocês vão ver demais quando estiver trabalhando disso, só que margin é um espaçamento na parte de fora, tem um padding, que é o espaçamento da parte de dentro, e segue a mesma lógica, eu quero um espaçamento de 48 pixels na parte de cima, então eu faço 48 pixels, e é sempre assim, no sentido horário, começa pela parte de cima, aí eu quero agora, sei lá, eu vou definir aqui no h1 a borda, só para vocês visualizarem melhor, colocar aqui um px solid pink, está aí.

Quando você não digita nada, 48 pixels, ele deu 48 pixels na parte de cima, na parte de baixo, na parte do lado e na parte do outro, se você colocar 48 e 12, ele deu 48 em cima, 48 embaixo, 12 de um lado e 12 do outro, e se você escrever o 48 e 12 e, por exemplo, sei lá, 24 e 32, isso aqui é o top, então eu vou até comentar essa parte e vou escrever assim.

Isso aqui é a mesma coisa de você escrever o seguinte, padding, o primeiro é top, o segundo é right, o terceiro é bottom e esse aqui é left, ele sempre faz assim, no círculo, no sentido horário, então essa aqui é a forma contraída para eu fazer assim, padding top, aí eu coloco o valor, sei lá, 48 pixels, padding right, aí eu coloquei aqui 12, então 12, padding left, coloquei aqui 24, não, é padding bottom, scoop bottom e agora sim padding left, 32, então eu escrever isso aqui é a mesma coisa de eu escrever isso aqui.

Então tem formas contraídas, tem forma mais simples e formas completas, Násser, estou entendendo, mas está complicado como eu vou lembrar disso tudo, de tanto você fazer, você vai pegar isso aqui e box-model você está fazendo o tempo inteiro, porque é espaçamento entre caixinhas, então isso aqui a gente sempre vai estar fazendo, só que é interessante a gente sempre lembrar disso.

## Bloco, inline e inline-block

E por padrão, pessoal, tem alguns elementos que são elementos de bloco, e tem alguns elementos que são padrões de linha, padrões de linha são aqueles elementos de texto, por exemplo, eles não se comportam exatamente como um elemento de bloco, eles seguem um pouco o fluxo de texto, então pode ser que você aplique uma determinada propriedade em um elemento de linha que é um h1, é um link, é um span e ele não vai funcionar direito porque ele não é um elemento de bloco, ele é um elemento inline.

Então eu já estou falando de display para vocês, também vocês vão entender, display nada mais é de como a caixinha se comporta, quais são as propriedades, funções e recursos que aquela caixinha vai ter, se for um display-block que é a imensa maioria, só não os elementos de texto, mas a maioria das caixinhas de forma genérica assim, didática, vai ser elemento de bloco, você vai conseguir colocar um margin, um padding normal e vai funcionar, nos elementos de texto eles são inline, então tem algumas coisas que elas não funcionam direito, vai testar e você vai ver que não vai funcionar muito bem.

Mas tem também um inline-block que ele vai continuar com algumas características de linha, vocês estão percebendo aqui as modificações, só que ainda vai ser caixa, você percebeu que quando eu defini ele como inline, olha só, eles ignoraram as características de bloco, que são as características de espaçamento e tal, quando eu coloquei inline-block, ele meio que pega dos dois mundos essas características, pode ver que eles tiveram espaçamento de novo, está vendo?

E aí, se eu quero que meu elemento tenha elemento, seja característica de bloco, está tudo certo, inline-block, e aí vocês vão conseguir perceber essas diferentes na prática, por exemplo, quando eu defino um width, eu quero que essa caixinha tenha 250 pixels de largura, em elementos de links, às vezes você deixar um elemento muito grande assim no elemento de link é complicado, ele fala o quê? Cara, é melhor deixar o link do tamanho do conteúdo, então você percebe que ele não está seguindo a linha de um bloco, ele está seguindo a linha de conteúdo, por isso que ele é mais inline, então esse é um exemplo que tem para vocês e eu já deixo claro que existem essas diferenças, de propriedades, mas o que eu queria só nessa aula é mostrar elementos de blocos que encarem tudo como se fosse uma caixinha para poder você organizar o conteúdo e que tem o margin e o padding para poder a gente começar a executar.

## width e height

Quais são as outras características de elementos de bloco? Cara, o width, como o próprio nome já diz, largura, height, altura, então eu quero que ele tenha 250 pixels de altura.

## Medidas fixas e relativas

Uma outra coisa que é interessante a gente falar são as medidas dos blocos, eu estou utilizando pixels, que quando eu estou falando de medidas fixas é o que eu mais utilizo, são pixels, mas por exemplo, tem pontos, se você colocar pt também funciona, só que é uma outra unidade de medida, eu prefiro utilizar pixels, porque a gente está em uma tela bem mais próxima, eu acredito que tem polegadas também, então olha só, fica bem maior o tamanho, olha o tamanho da caixa, como é que fica em polegadas, então essas são medidas fixas, tem medidas fixas e medidas relativas, quais são as medidas relativas?

Quando você define porcentagem, por exemplo, mas você colocou, sei lá, 250% de altura, mas é 250% do quê? Do pai, então o h1 é filho de alguém, ele é filho de quem no caso aqui? Ele é filho da div class-item, ele vai pegar 250% do pai, então ele sempre vai ter como referência isso.

E tem também, por exemplo, as viewport units, que é a altura e largura da sua tela, então, por exemplo, se eu colocar vw, ele vai pegar a largura do seu dispositivo, da sua tela, vamos supor que seja, sei lá, você está no seu celular e a largura da sua tela, horizontal ali é 375 pixels, ele vai pegar 250% de 375 pixels e vai definir aquilo ali como tamanho, a altura, você vai colocar vh, por isso que em muitas divs eu coloco, por exemplo, 100vh, que é o quê? Cara, pega a tela inteira, você pode ver que essa div aqui está exatamente o tamanho da minha tela, como eu coloquei 100vh, se eu colocar 80vh, ela ficou 80%, entendeu?

## Encerramento

E você vai pegando isso ao decorrer das aulas, mas é interessante, meio que dá um panorama geral aqui, mas ao mesmo tempo não flodar vocês de informações, não deixem de pesquisar, tentar implementar isso, mas a gente vai ter um projetinho prático para poder a gente exercitar isso, então é isso pessoal, até a próxima.
