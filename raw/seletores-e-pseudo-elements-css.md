# Seletores e pseudo-elements em CSS

Então, pessoal, agora nós vamos dar andamento sobre seletores. É uma coisa muito interessante quando a gente sabe utilizar os seletores.

A gente consegue aplicar muitos hacks porque, vocês viram, quando a gente está aqui no nosso CSS, a gente tem que tentar ser o mais otimizado possível, ou seja, criar a menor quantidade de classes possíveis de forma a garantir a consistência e organização do nosso código e outras coisas.

Dependendo da complexidade do layout que você está trabalhando, vai ser necessário, talvez, aplicar mais classes diferentes porque tem um ou outro que tem um estilinho diferente e você vai lá e tem que aplicar uma classe só por causa de um elemento para poder deixar igual, você pode aplicar outra classe e vai flodando, daqui a pouco você nem entende aquele tanto de classes ou então demora para poder executar esse tipo de coisa.

Com relação a isso, é muito importante saber dos seletores. Os seletores, quando bem aplicados, facilitam a nossa vida e um deles são esses aqui que eu vou explicar e demonstrar por meio de um artigo no W3C que é muito legal e a gente também vai conversar um pouco sobre pseudo-elements, que também são muito importantes para podermos definir o estado dos elementos.

Então, nós vamos demonstrar isso aqui na prática e vamos utilizar da melhor forma possível, então vamos lá.

## Seletores

Eu vou deixar esse link aqui embaixo para vocês, se vocês não encontrarem, basta digitar cssref w3schools, que são os seletores que a gente tem e é muito interessante que a gente vai clicando e vai mostrar para mim qual é a div que ele está selecionando.

A classe intro, ponto intro, ele vem aqui simplesmente onde tem aplicada a classe intro, vou até dar um zoom aqui para poder melhorar, ele vai onde tem a classe intro e seleciona para mim, então quando eu estou aplicando a classe intro no CSS, ele está olhando para esse elemento aqui, beleza?

Hashtag lastname, olha só, o ID ele só vai pegar a tag do lastname. Intro, lastname, ou seja, ele vai pegar esse elemento aqui dentro e o elemento de fora, ele vai aplicar o estilo para os dois ao mesmo tempo. Só o h1. H1, p, ele vai pegar todos os h1s da sua página e todos os parágrafos, todas as tags p da sua página e inclusive engloba outras tags, por exemplo, a tag b está dentro da tag p, então b de bola está dentro da p de pato e aí quando você aplica, o estilo dessa forma aqui vai estar aplicando para todos.

Div espaço p, aqui a gente começa a restringir, a gente vê que a vírgula aplica para todos, agora quando a gente coloca simplesmente espaço, é um tipo de seletor descendente, ou seja, selecione apenas os elementos parágrafos que estão dentro de uma tag div, então nem todas as tags p estão dentro de divs e eu quero que ele aplique esse estilo apenas para os parágrafos que estão dentro de uma tag maior, dentro de uma tag pai chamada div, então muito legal isso aí.

Div p, div traço p, a diferença entre eles é que tem como pai direto, porque desse jeito aqui ela pode estar dentro do p e que está dentro do p, então todo e qualquer p que esteja dentro da div vai pegar, já esse aqui força que seja filho direto, ou seja, se eu colocar um p dentro do p aqui, o segundo p, que seria o neto, não o filho direto, não vai aplicar.

Ul mais p é aquele parágrafo que está seguido da tag ul, então o único que tem como precedente a tag ul é esse parágrafo daqui, esse aqui tem como precedente outro parágrafo, esse aqui tem como precedente a tag h3, então é simplesmente a tag que antecede ele na ordem, então a única que antecede ele na ordem é a ul e assim a gente vai aplicando e pensando para todas as coisas, então não deixem de conferir isso aqui e entender como é que funciona os seletores em CSS.

O asterisco, como eu tinha dito, ele aplica para todos os elementos da página, exclusivamente em todos. Quando eu coloco uma classe que está junto ao parágrafo, ela vai aplicar essa classe somente àquela que está ligada ao parágrafo, então muito legal isso também.

Formatar formulários, eles são baseados nisso aqui, quando eu coloco, vamos supor, propriedades, então vamos supor que eu quero toda e qualquer ID que tenha a propriedade myAddress, eu quero utilizar esse ID, então eu consigo tirar pela propriedade, mas aí você fala: "Násser, mas espera aí, pelo ID você não faz pela hashtag, não seria mais fácil?" Sim, porque esse é o caso do ID, mas vamos supor que se fosse um input de texto que você queira modificar o background dele, o título ou o placeholder, são tags que você não consegue fazer como ID e aí vai precisar utilizar desse recurso aqui.

Então vocês vão clicando, vão conferindo e vão lendo aqui, tem a descrição de como funciona isso em inglês, está bem mais completo do que a minha apresentação, então sugiro que vocês seguem por aqui.

## Pseudo-elements

E agora os pseudo-elements. "Násser, o que significa, o que é pseudo-elements?"

Esse sufixo pseudo vem de falso, então é um falso elemento, é meio que um elemento ou um estado dentro de um outro, por exemplo, do tipo checked, ele está aplicado aos inputs radio ou checkbox, ou seja, é o estado dele de estar marcado, então com esse checked eu consigo estabelecer algumas funções ou estilos, para que ele se desencadeie quando algo está marcado. Então vamos supor que eu quero marcar um determinado estilo aqui, aí quando eu marco ele detecta que agora está marcado e ele marca esse estilo. Para vocês entenderem um pouco mais, tem um vídeo do meu YouTube onde eu faço tipo um hack utilizando esse pseudo-element para poder fazer o menu hambúrguer animado, então muito legal.

Esse aqui são os disabled, ou seja, vamos estilizar todos os campos que estejam desabilitados, habilitados, vazios, em foco, ou seja, com um clique, vamos supor que eu deixe esse aqui clicado, esse elemento está focado, ele está pronto para poder receber um texto que eu posso estilizar a maneira de como ele fica com esse focus aqui, então é muito importante para poder a gente aprender a fazer o estilo de formulários.

First-child é meio que primeiro filho, então sempre quando a gente tem uma classe ou uma tag, as que vêm logo após eles são filhos, são considerados filhos, então essa classe aqui, intro, ela tem três filhos, primeiro filho, segundo filho e terceiro filho, e aí eu consigo filtrar, fazer a estilização apenas do primeiro filho, aí eu faço first-child.

First-letter, a primeira letra, olha só que legal. First-line, primeira linha. First-of-type, primeiro desse tipo. Hover é o clássico quando você passa o mouse em cima, quando tem o efeito hover, de disparado é o efeito que a gente mais utiliza, que eu mais utilizo. In-range, out-of-range, inválido, válido, last-child que é o último filho.

Nth-child é quando você quer selecionar um elemento específico, no caso, even é o quê? Ímpar, odd ou é par, é alguma coisa assim, por exemplo, o elemento aqui da tabela é aqueles que são ímpares, você seleciona por esse, aqueles que são pares você seleciona por esse, o 1 ele seleciona, se eu me engano, o 1 ele vai selecionar, olha aqui, tem aqui a opção 1, last-child 1, ou seja, começa do começo e começa do final.

Last-of-type, only-child, se tiver um único filho e aí vocês vão conhecendo e aqui o root é quando a gente está definindo variáveis, então muito importante essa parte, não deixem de fuçar e entender como é que se dá os seletores em CSS utilizando esse site aqui, beleza?

Até a próxima!
