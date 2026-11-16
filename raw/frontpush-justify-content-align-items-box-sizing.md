# Justify-content e align-items: alinhar os flex-itens (e um parêntese sobre box-sizing)

Então, pessoal, agora nós vamos continuar a parte de flexbox, como eu tinha dito na última aula, justify-content.

## Correção: wrap-reverse

Só deixa eu corrigir uma coisinha que eu falei errado. Eu fui lá ver minha aula, que eu sempre dou uma confere para ver se está tudo certo: aqui eu coloquei inverse e o certo é reverse. Aí, quando eu coloquei aqui reverse, funcionou legal. Olha só, ele quebra de forma reversa: em vez de ser 1, 2, 3, 4, 5, 6, ele faz em uma ordem diferente. Então, aqui eu tenho 5, 6, aqui eu tenho 10, enfim, ele só quebra de maneira reversa.

## Justify-content

Agora nós vamos trabalhar a propriedade flex justify-content. Mais ou menos, se eu fosse dizer para vocês, é como os itens, você vai dizer para os flex-itens como eles têm que se organizar no quesito horizontal.

E aí, flex-start, a gente percebe que é meio que o padrão. Então você percebe que quando você define o display flex, tem um monte de propriedades que já são definidas de forma padrão. A gente estuda cada uma delas em cada parte quando a gente está tratando aqui, então é importante que sempre a gente está lembrando desse tipo de coisa: a gente sabe que flex-direction é sempre row, e aqui o justify-content é sempre flex-start.

Deixa eu diminuir aqui, deixar só 4 itens para poder a gente organizar da melhor forma possível. Está aqui. E, ao invés de deixar o item com um height de 100%, eu vou forçar que ele tenha um max-height de 100px, vamos diminuir o tamanho dele só para a gente entender da melhor forma possível, está bom?

Então vamos lá, o que eu quero ver aqui? Flex-start, eu vejo que todos ficam alinhados meio que à esquerda. E esses desenhinhos que eu fiz aqui, acredito que eles auxiliam para poder a gente estar tratando esse tipo de coisa. Vamos mudar aqui do center, vamos ver o que acontece. Então simplesmente a gente está mudando a forma de como eles se organizam no caráter horizontal. Flex-end, flex-end. Então é como se fosse o quê? O que eu estou fazendo aqui? Alinha à esquerda, alinha ao centro, alinha à direita, basicamente são essas opções aí.

## Space-between e space-around

Agora, a que eu mais utilizo do justify-content de cara é o center aqui e o space-between. O space-around talvez não tanto, mas é bom utilizar ele porque ele deixa justamente um espacinho aqui, você não precisa colocar o padding. Então a gente vai visualizar isso aqui agora.

Vamos colocar então o space-around para ver como que acontece. Ele meio que deixa um espacinho aqui, então quando você está construindo um menu responsivo, é interessante você pensar no space-around, que ele sempre vai deixar um espacinho aqui entre eles.

Agora, se você colocar space-between, ele vai meio que colar e literalmente deixar o máximo de espaço entre os flex-itens. Ele cola lá no canto e, para poder eu melhorar e não ficar sempre colado, tem que colocar algum tipo de padding. Então é legal você considerar o space-around quando você estiver construindo menu responsivo, e a gente vai tratar disso aí tanto no caso da Nubank como nos nossos projetinhos, quando a gente terminar aqui de estudar sobre isso.

E por fim, não é só isso mesmo, sempre leia a teoria para poder entender ele da melhor forma possível.

## Align-items e o combo de centralizar

E agora nós vamos falar um pouquinho sobre align-items. Então, se o justify-content ele tratava mais do caráter horizontal, o align-items ele trata mais do caráter vertical. Vamos lá, vamos aplicar ele aqui também.

Então vocês começam a entender por que sempre naqueles meus projetos do YouTube, que eu quero que tudo fique no centro, tudo e qualquer coisa que eu quero fique no centro, o que eu sempre faço? Display flex. Eu venho aqui no body, display flex. Quando eu faço isso, o meu body vira um flex-container, os meus filhos diretos viram flex-itens na hora, ele já fica como flex-direction row e aquelas propriedades todas padrão. E aí eu sei que o justify-content por padrão é o flex-direction, start, só que eu não quero, eu quero que ele fique no centro, e o align-items. Ou seja, eu quero que você centralize na horizontal e centralize na vertical. Então, sempre que eu digito assim, sempre é o combo desses três aqui, tá bom?

## Parêntese: box-sizing

Ah, Násser, o que é o box-sizing? O que é o box-sizing? Meio que é o seguinte, eu vou explicar isso aqui para vocês. Vamos supor que eu tenha a minha caixinha aqui e você percebe que, quando eu dou um padding na minha caixinha, vamos supor, vou dar um padding maior, vou deixar 20 pixels em cima e embaixo e 50 de um lado e de outro, e aí ela vai ficar com o caráter mais retangular.

Quando eu defino o box-sizing border-box, o que acontece? Eu estou falando para a caixa meio que não considerar, não aumentar de tamanho a minha caixa de acordo com o tamanho do conteúdo. Porque se eu, por exemplo, eliminar isso aqui... Ah, Násser, não mudou nada. É porque o meu conteúdo é diferente. Se eu colocar item, item, item e item aqui no primeiro, você vai ver que ele vai mudar o tamanho.

Então eu sempre deixo como referência o tamanho da caixa, sempre o tamanho da caixa, não com relação ao conteúdo. Eu prefiro que o conteúdo estique, porque se eu aumentar o conteúdo, aí a caixa aumenta junto, e eu não quero isso, eu quero que a minha caixa fique do tamanho que eu estabeleci. Então, em todos os projetos eu sempre coloco box-sizing border-box para ele dar prioridade para a caixa e não para o conteúdo. O conteúdo tem que quebrar se for necessário. Item 1.

## Os valores de align-items

Vamos lá, vamos voltar então. O que eu fiquei de explicar agora sobre align-items? Então vamos colocar aqui, align-items. Então o stretch, vamos ver aqui, sempre a gente coloca e vê como é que acontece. Então o stretch... Ah, Násser, não está acontecendo nada. É porque eu defini o minimum-height aqui, o max-height aqui, então ele vai ajustar o tamanho vertical.

Flex-start, vamos colocar aqui, vamos ver o que acontece. Da mesmíssima maneira, deixa eu colocar aqui o justify-content flex-start para a gente entender também qual é a diferença. Então ele sempre vai ficar alinhado lá no topo, é isso que ele está dizendo, sempre fica alinhado ao topo, na questão vertical. Por isso que não mudou tanto e você não... "Ah, você aplicou a propriedade e não mudou nada". Agora eu vou aplicar o center, agora vai fazer mais a diferença. Então ele está alinhando, gente, verticalmente.

Por isso que o flex-start a gente não percebeu, porque ele é o padrão do sistema. Então, assim como o justify-content tem como flex-start, o padrão do sistema é o flex-start no align-items também. Flex-end vai alinhar na parte de baixo.

O baseline ele vai ajustar de acordo com o conteúdo. Então, para poder forçar essa diferença, deixa eu ver como é que eu vou fazer, vou aplicar aqui um estilo inline, style, font-size, vou aplicar aqui de 50px, vou deixar o item 1 ficar bem grande. Vou aplicar, por exemplo, no item 2 uma fonte um pouquinho menor, para poder enfatizar como é que se dá esse efeito, porque ele ajusta agora de acordo com a baseline do conteúdo. Então eu vou deixar assim e a gente vem aqui e coloca baseline para poder ver como é que se dá o alinhamento.

Então, basicamente, são esses. A próxima aula a gente vai falar sobre align-content. Então é isso, vou explicar assim em duplas, porque acredito que o entendimento facilita um pouquinho mais.
