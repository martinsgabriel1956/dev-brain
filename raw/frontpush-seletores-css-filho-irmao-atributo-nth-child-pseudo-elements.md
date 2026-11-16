# Seletores no CSS: filho direto, irmão adjacente, universal, atributo, vírgula, nth-child e pseudo-elements

Opa, fala pessoal, Násser aqui, sejam muito bem-vindos, dando continuidade ao que a gente falou nas aulas passadas. Agora, nós vamos focar um pouquinho mais em seletores no CSS. Então, apenas relembrando, vocês lembram que você pode fazer os seletores por meio da tag, por meio de class ou id. Porém, a gente vai imergir um pouco mais nisso, porque esse assunto é deverasmente importante, porque ele vai ajudar até em JavaScript um pouquinho. Por que eu falo isso? Então, vamos começar aqui. Quando a gente precisa literalmente estudar um pouco sobre as várias formas de como a gente seleciona um determinado elemento no CSS, é muito similar ou deveras igual do que a gente faz no JavaScript. Então, às vezes, a gente precisa selecionar um elemento via JavaScript, que a gente ainda vai estudar, então não tenha pressa, primeiro vamos ver isso aqui, que a gente precisa entender um pouco mais sobre esses seletores.

E eu gostaria de deixar claro, pessoal, que essa aula aqui é o básico e o essencial para poder a gente estudar e continuar estudando, porque o que eu queria dizer é que até hoje eu aprendo CSS, até hoje eu pesquiso sobre CSS e isso deve ser algo presente na vida do programador, é ele sempre estar perto da documentação.

Então, eu vou mostrar aqui os principais seletores, aqueles que eu mais utilizo no dia a dia, mas pode ser que você utilize outros seletores e é interessante que você verifique, que você literalmente tenha curiosidade e aí eu vou te passar os links e as dicas de como conseguir fazer isso. Então, vamos lá, sem mais delongas, vamos lá.

## Pais e filhos: filho direto e descendente

Primeira coisa, pessoal, o que eu queria falar é os seletores com relação a pais e filhos, existem seletores que a gente consegue organizar isso aí, por exemplo, a gente sabe que esse section aqui, essa seção que eu acabei de criar, ela é pai do parágrafo e do span, concorda comigo? Mas vamos supor que ao invés de ser span, eu tenho aqui o p, então eu faço uma div e dentro desse div eu coloco um outro p. Então, nós temos dois parágrafos, vamos entender um pouco mais sobre os seletores de pais e filhos.

Quando você quer, por exemplo, selecionar o seletor que é filho direto ou então um filho que simplesmente está dentro, essa é a diferença. Por exemplo, nós temos aqui a section, vamos supor que eu queira selecionar somente os parágrafos que estão dentro da section, mas que são filhos diretos, filhos diretos é aquele que literalmente é filho, ele não é neto, ele não é tataraneto, ele não está dentro do bloco, ele é filho direto, ou seja, subsequente, ou seja, o único parágrafo filho direto é esse aqui, esse aqui é filho também, mas ele é meio que neto, vocês entenderam a dinâmica?

Então, quando eu quero selecionar somente o filho direto, eu sempre coloco um símbolo de maior p, se eu vir aqui e colocar um color white, ele vai ficar branco somente esse, ao passo que se eu apagar ele e simplesmente deixar com espaço, ele vai entender todo e qualquer parágrafo que estiver dentro da section, se eu salvar isso aqui, os dois vão ficar brancos, entendeu? Então, muito interessante isso.

## Irmãos: o adjacente

Agora, vamos supor que eu queira estudar um pouquinho os seletores de irmãos, vamos supor que por meio dos irmãos aqui, eu coloco um span aqui, então o primeiro é um parágrafo, o segundo é um span, você vai perceber que o span e o parágrafo são irmãos, vamos supor que eu queira selecionar todos os spans que eles têm como irmão anterior um parágrafo.

Então, calma, eu vou deixar aqui um outro span escrito teste e eu tenho três filhos, então esses dois aqui são spans, mas no seletor aqui, eu vou falar o seguinte, selecione para mim o span que esteja adjacente a um parágrafo, ou seja, do lado de um parágrafo, entendeu? Então, eu só vou selecionar esse span aqui, esse aqui não está do lado de um parágrafo, ele está do lado de um outro span, então se eu apertar esse aqui, só ele vai ficar branco, esse outro span teste aqui, você vai ver que ele não ficou.

## Seletor universal

Então vocês podem ver um pouco mais disso, por exemplo, se você digitar em seletores aqui, dentro do MDN Firefox, deixa eu mandar a minha câmera para cá, do qual temos os seletores básicos que a gente já viu, que são as tags, classe ID, seletores universais, isso aqui, pessoal, é basicamente o quê?

Quando você quer fazer um reset dos seus seletores, se eu quero que todos os textos por padrão sejam brancos inicialmente, é lógico que você consegue colocar classes ou IDs depois para poder realizar suas, como se diz, variações, com importâncias diferentes, como vocês lembram que eu apliquei uma classe, ela se sobressaiu da tag, ela tem uma hierarquia um pouquinho maior, então quando você quer, por exemplo, selecionar todos os seletores, tudo, tudo, tudo, fique branco, você vai colocar assim, color, por exemplo, white, então por padrão tudo vai vir branco, mas eu quero que esse link aqui fique preto, eu quero que esse link aqui fique azul, aí você vai aplicar uma classe nesse determinado link, então meio que você vai generalizar, aplicar tudo e depois só vai fazer tratamentos pequenos, você vai utilizar o asterisco, então esse é o seletor universal

## Seletor de atributo

E por atributo, o atributo é literalmente assim, eu não quero modificar, então você também consegue selecionar somente aqueles inputs que têm por atributo o texto.

Então vamos supor que eu faça aqui um formulário, dentro desse formulário eu vou ter um input:button e o input:text, input dois pontos text, então está aí, são dois inputs que vão aparecer aqui, a princípio eles têm a mesma configuração, mas utilizando esse atributo aqui, por exemplo, atributo é igual a valor, eu posso estabelecer ele desse jeito aqui, eu quero tratar de um input, porém qual é o atributo desse input? É o que? Type, então eu venho aqui, type é igual a texto, ou seja, eu vou fazer a modificação somente dos inputs que são type text, então deixa eu colocar aqui, aqua, por exemplo, o background-color, você vai ver que esse aqui também é um input, que é o button, porém ele não foi modificado, somente o input-text, que eu coloquei aqui o seletor com base no atributo, está certo?

## Vírgula: vários elementos de uma vez

Então, uma outra característica aqui, já falei sobre os adjacentes, os pais e filhos e existem, pessoal, diversos outros atributos, por exemplo, eu vim aqui, digitei na W3C mais alguns atributos para vocês darem uma olhada, quando você tem vírgula, vamos supor que eu queira selecionar vários elementos de uma vez só, por exemplo, os títulos, então eu posso vir aqui e criar uma nova seção, e aqui dentro eu vou colocar h1, título h1, vou fazer o título h2 e o título h3, então h2, h3 e aqui h2 e h3, então eu criei os meus títulos aqui e eu quero que eles todos fiquem brancos, então eu posso selecionar o h1, o h2 e o h3, ao invés de colocar color é hashtag ccc, que é um cinza clarinho, isso aqui é a mesma coisa de fazer, h1, color é hashtag ccc, aí eu faço de novo, h2, color é hashtag ccc, então é um jeito mais compresso e mais objetivo a gente selecionar os três ao mesmo tempo, utilizando vírgula, por exemplo.

## first-letter

Por atributo, por pseudo elements, isso aqui é muito interessante também, eu vou falar alguns, mas só para vocês terem noção do tanto de seletores que tem, o first letter, por exemplo, é quando você quer que a primeira letra de cada parágrafo, por exemplo, sempre seja maiúscula, first letter, então se você pegar parágrafo assim e colocar first letter e aplicar desse jeito aqui, meio que utilizando pseudo elements, você está fazendo a seleção de que toda a primeira letra dos parágrafos vão ser maiúsculas, por exemplo, você pode colocar assim, text transform capitalized, ou então eu quero que toda seja negrito, então você vai colocar um font weight bold, entendeu?

## nth-child, first-child e last-child

Então, pessoal, essa aula é só para poder falar que existem vários seletores, os principais eu falei aqui para vocês, entendeu? Muitos a gente vai aprender ao decorrer do curso, por exemplo, o nth-child eu utilizo muito, o que é o nth-child? Child vem de criança, ou seja, filho, se a gente for trazer aqui para os elementos.

Então, vamos supor que dentro dessa lista aqui, dessa lista ul, eu tenho três filhos, são os lis, então eu queira, por exemplo, o ul, eu quero o primeiro filho dele, então vamos lá, aí eu vou colocar aqui, nth-child, vou colocar o filho número um, aliás, do li, do li ou dele, vamos ver aqui, deixa eu voltar para cá, eu quero que o primeiro tenha um background-color, deixa eu ver aqui, blue-violet, olha lá, eu quero colocar o dois, eu quero colocar o três, então os nth-child fazem isso, tem como eu adicionar o nth-child, por exemplo, last-child, sempre vai ser o último elemento, tem o first-child, se não me engano, que tem o primeiro, tem como eu selecionar apenas elementos pares ou elementos ímpares, assim, dentro de filhos.

Então isso tudo por meio de seletores, você precisa saber todos? Absolutamente não, os principais eu falei aqui para vocês, mas tem alguns que são interessantes que quando você utiliza o seu CSS, ele vai se tornando mais profissional, então essa aula aqui é para poder apresentar para vocês o que são seletores, literalmente são formas de a gente escolher os elementos que a gente vai estar formatando com o CSS.

## after e before

O que eu utilizo muito também é, por exemplo, o after e o before, esses eu utilizo demais, por quê? Por exemplo, que você está utilizando aqui um article, eu vou criar aqui um article, aí eu venho aqui, seleciono o article, mas eu quero o pseudo-element dele, o que é o pseudo-element after ou before? É como se fosse duas divs, uma que fica na frente do elemento, outra que fica depois do elemento, Násser, como assim? É a mesma coisa de você ter aqui uma div, sendo que você vai ter uma div antes dela e uma div após ela, antes e depois do elemento, só que você não precisa criar outra div para poder manipular ele e ele é filho do article, entendeu? Então por isso que é interessante.

Então, por exemplo, quando eu vou lá no FrontPUSH, deixa eu acessar aqui, o frontpush.com .br, vocês vão perceber que em alguns botões eu coloco um iconezinho, por exemplo, entrar para a turma, você está vendo que tem um iconezinho de uma setinha, essa setinha eu coloquei com o pseudo-element e a gente trabalha de como a gente utiliza esse pseudo-element, literalmente é uma div, mas só que pelo fato de você utilizar o pseudo-element, o seu código fica mais clean, o seu HTML não fica muito poluído e isso dá uma cara mais profissional de como você está programando, tem como fazer só utilizando divs como eu escrevi aqui? Sim, tem como, mas você vai profissionalizando cada vez mais e tem algumas particularidades para poder você fazer esse pseudo-element funcionar, eu vou fazer aqui de maneira bem rápida.

## Criando um pseudo-element na prática

Por exemplo, você vem aqui no article, você vai colocar uma borda nele de 1px solid green, só para poder a gente visualizar e ele vai ter um width de 500px e um height de 500px também, então vamos lá, deixa eu salvar, está aqui, apareceu, deixa eu diminuir isso aqui, deixa eu colocar 200px só, então está aqui o meu article que é a minha divzinha, está bem aqui.

Ah, eu quero adicionar um pseudo-element nele, primeira coisa, eu defino o pai, que é o article, como um position relative, eu não sei o que é position relative, estou adiantando algumas aulas, é só você ir na aula de position e voltar para cá para você entender de forma total, mas eu deixo ela assim, venho aqui em article, agora eu defino, por exemplo, um elemento after, o elemento after eu vou deixar ele com conteúdo vazio, com position absolute, com top 0 e um left 0, e aí eu vou definir ele com o mesmo tamanho do pai, ou seja, 100% e um height de 100%, eu posso colocar de 50%, então vamos lá, 50%, e aí eu vou deixar aqui um background-color blue, só para vocês visualizarem, olha aí, é uma div que é filha dele e que eu meio que estou manipulando ela, assim ela está no HTML, ela não está aqui no HTML, se eu apagar essa div e apagar essa div, ela não está aparecendo aí, mas mesmo assim eu consigo colocar elementos aqui dentro, então eu posso colocar um ícone, posicionar ele dentro do meu elemento pai.

## Encerramento

Então é isso que eu tenho que falar sobre seletores, estudem, sempre que tiver um novo seletor, uma nova forma de fazer, eu sempre vou explicar ela nos diferentes projetos, mas é isso, até a próxima aula.
