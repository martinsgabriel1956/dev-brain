# Flexbox, prática 2: um desafio de layout e as dicas de estrutura de divs

Opa, então pessoal, pegando essa onda de novos exercícios para poder aplicar os itens do Flexbox, eu dei uma complicadinha aqui. Estou bolando alguns layouts que são mais difíceis de serem executados com o Flexbox, porque você tem que pensar de como você vai compor a estrutura de divs para poder aplicar todos os conceitos. Então, isso aqui eu considero um desafio um pouco mais acima desse aqui do YouTube. Então, vale a dica: se você quiser praticar o Flexbox, tente fazer esse carinha aqui, onde eu vou dar as principais sacadas que você tem que ter, tá bom?

## O menu

A parte do menu não muda absolutamente nada. Talvez você possa colocar, por exemplo, inverte sobre produtos e contato, você pode colocar ele aqui no centro, só para modificar diferente. E aqui você pode colocar alguns botões de call to action, um estilo de menu diferente que você pode estar projetando. Dá para fazer também só com o Flexbox, só que você tem que utilizar, por exemplo, de media query para poder sumir com os itens.

Nossa, como assim? Porque você percebe que aqui, quando a gente bate aqui, como tem poucos itens, não precisa, por exemplo, sumir e aparecer com um ícone de hambúrguer. Quanto mais coisas você coloca no menu, mais você precisa estar vinculando ele com algum tipo de media query para poder tirar uma div e adicionar uma outra. E você tem mais noção disso, por exemplo, no projeto do Nubank que eu fiz. Se você não sabe, dá uma olhadinha lá, que eu já tenho mostrando como se dá isso.

Mas olha só, utilizando o Flexbox está aqui um bom desafio, que eu posso estar fazendo esse exercício aqui posteriormente, mas fica para exercício, para vocês treinarem.

## A estrutura HTML: container e três flex-itens

Basicamente, vou dar aqui a dica de qual estrutura HTML que vocês precisam ter. Mais uma vez, você vai ter uma div container englobando todos os elementos de acordo com o grid que você estabeleceu, seja ele de 1.200 pixels, 1.440 pixels, como eu deixei aqui, deixei esse grid aqui, onde vai englobar todos os elementos.

Aqui dentro, nós temos uma div englobando todos esses carinhas aqui, todos esses carinhas aqui, nós temos uma div assim, onde nós temos três flex-itens. Então, você vai fazer uma div para esse carinha, uma outra div para esse carinha aqui e uma outra div para esse carinha aqui, concorda comigo? São os flex-itens. Vou até modificar a cor deles para poder sempre facilitar o entendimento, então coloco um azulzinho, está bom? Está tô, pessoal, mas entendam a essência do que eu estou querendo passar.

Aí você vai ter outra div aqui dentro, porque uma tem que pegar literalmente a imagem do thumb que você está colocando aqui e outra para o texto, ou simplesmente coloca aqui as três direto e coloca elas orientadas em coluna, também é possível fazer isso com todos.

## Pensar em colunas e quebrar em ABC

Aqui, como é que você vai fazer nessa estrutura aqui? Mais uma vez, sempre pense no flexbox como em colunas primeiro. Você vai fazer uma para esse aqui, uma coluna para esse aqui e uma coluna para esse aqui, de forma que, quando eles quebrem, quebre um, esse aqui para baixo e esse aqui para baixo. Então estrutura ABC, e vai quebrar em ABC em coluna, simplesmente assim.

Pode aplicar aquele mesmo princípio que eu falei: ou troca de row para column, utilizando o media query, ou simplesmente adiciona um flex-wrap e configura o flex-basis desses três aqui, de forma que estabeleça a melhor responsabilidade possível para o que você quer criar.

## Flex-itens dentro de flex-itens

Dentro desse aqui, eu tenho três flex-itens, concordam comigo? Vou colocar aqui uma cor verde. Dentro desse aqui eu tenho três flex-itens, que é esse carinha, esse carinha e esse carinha. Eles precisam ser filhos direto desse azul aqui, para poder funcionar da mesmíssima forma esse aqui, só que aqui eu tenho dois filhos e aqui eu tenho três filhos.

Aqui, mais uma vez, você pode colocar ele em display block, então um filho só consegue resolver isso aqui, mas se você quiser organizar, você pode colocar mais divs aqui, mas aqui não é necessário. E mais uma vez, uma div, uma aqui dentro da outra. Então acredito que essa estrutura aqui você vai estar aplicando ao longo desse layout para poder codar, beleza, galera?

Então é isso, mais alguns exercícios de flexbox. Pretendo trazer outros um pouquinho complicados, mas é sempre interessante a gente estar exercitando, porque depois no layout fica bem mais fácil de executar, beleza? Então falou, galera, até a próxima.
