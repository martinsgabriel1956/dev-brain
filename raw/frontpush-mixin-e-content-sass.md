# As propriedades @mixin e @content no Sass

Então, pessoal, vamos dar continuidade às nossas aulas de CSS e Sass, onde a gente está conhecendo os fundamentos e principais recursos desse pré-processador, que ajuda demais a gente na programação do CSS. E hoje, na aula de hoje, nós vamos estar conhecendo um pouco mais sobre os recursos do mixin e do content. Esses dois aqui, quando utilizados de maneira conjunta, vocês vão ver os benefícios que esses dois trazem.

Então, basicamente, com esse recurso de mixin, eu tenho a capacidade de criar funções pré-definidas ou até com argumentos, o que facilita demais, porque basicamente é um trecho de código que eu posso personalizar ou então pré-definir para poder utilizar em vários outros projetos e criar bibliotecas e tudo mais. O que, consequentemente, melhora e possibilita o aproveitamento de código.

Consequentemente, se a gente tem funções com a capacidade de, por exemplo, colocar argumentos, e ele devolve alguma resposta, onde a gente pode agrupar ele em outras tags, permite a criação de sistemas mais completos e complexos.

Também tem a facilidade de adicionar aqueles prefixos, traço webkit, traço moz, para poder melhorar a compatibilidade, além de facilitar na criação da função de responsividade, que eu já implementei no projeto do Nubank e vou estar retomando mais uma vez para poder mostrar esse recurso.

## A sintaxe do mixin

Basicamente, essa é a estrutura que a gente vai estar utilizando, essa é a sintaxe do mixin. Entenda mixin como se fosse uma função de fato, mas aqui o nome é mixin. E aí você vai abrir com arroba mixin, aqui é o nome do seu mixin, você vai dar o nome de uma função para você chamar em qualquer parte do código. Aqui você pode, ou não, passar argumentos. No caso aqui, eu estou passando o argumento de cor com um default de cor FA, FA, FA, que também é possível de passar.

E aqui é como se fosse um mixin de fonte, de título, onde eu defino um font-size, um color com a variável cor que eu posso passar aqui, e um content. Basicamente, esse content aqui, eu estou dizendo o que para o Sass? "Olha, se ele abrir esse mixin, adicionar esse mixin e colocar algum código dentro dele, o que ele colocar dentro do código vai aparecer aqui." É meio que um copia e cola, uma variável que, quando você insere aqui dentro, ele vai colar aqui.

E aqui um pequeno exemplo. Vamos supor que eu aplicasse esse mixin aqui nesse h1: eu simplesmente dou um include, o nome do mixin, com a cor que eu quero, e, olha só, o conteúdo que eu coloquei aqui dentro, que é o content, ele vai ser carregado para cá automaticamente. O que vai ser plotado? Vai ser plotado um h1 com o font-size de 36 pixels, com a cor branca, FFF, e com o line-height de 110%, está bom?

Então, é meio que essa é a estrutura, e eu vou mostrar na prática o quão benefício têm essas duas funções. Enfim, sem mais delongas, vamos lá, onde eu vou demonstrar para vocês função de responsividade utilizando esse recurso, para vocês entenderem o quão poderoso é esse recurso quando bem utilizado.

## Responsividade com CSS puro

Então, vamos lá, vou apagar essa seção que eu expliquei na aula passada, vamos lá, vamos dar continuidade.

E aí, pessoal, o que eu quero estabelecer aqui? Primeiro, vamos estilizar esse parágrafo de forma que a cor dele, o color, seja cinza, de forma que a gente consiga visualizar. Vou aumentar o tamanho do h1, vou colocar um font-size de 72 pixels, por exemplo, e vai ficar bem grande esse objetivo. Da mesma forma, eu posso vir aqui, adicionar um font-size, e vocês vão entender o porquê que eu estou fazendo isso, por exemplo, de 24 pixels no parágrafo, que também vai ficar grande dessa forma.

Quando a gente precisa construir um ambiente responsivo, a gente tem noção de que a gente precisa adequar o tamanho das coisas ao tamanho da tela, concordam comigo? Por exemplo, nesse exemplo que eu estou citando aqui para vocês, nós temos um "Hello World com Sass", ou seja, um título, aqui temos um corpo de texto que está grande para essa tela, por exemplo, não, ele está adequado a essa tela, desculpe.

Só que, se eu fosse diminuindo essa tela, diminuindo, diminuindo, e chegasse à tela de um celular, por exemplo, eu acredito que o tamanho desse título e desse texto aqui, dadas as devidas proporções, ele está grande demais. Então você poderia diminuir tanto esse como esse por causa da tela, de forma que você adeque o tamanho da tipografia ao tamanho da tela. Então, isso é um básico de UI Design alinhado à responsividade.

E, quando a gente precisa fazer esse tipo de coisa com CSS padrão, como é que faria? Quais são as skills para poder a gente aplicar mixins e content de uma forma muito efetiva para poder a gente utilizar nos nossos projetos? O que a gente precisa fazer?

A gente pode construir esse tipo de responsividade com media queries. Então eu faço media screen and e abro, por exemplo, um max-width, vamos supor de 720 pixels. O que esse comando está dizendo para mim? Ou seja, vai pegar o tamanho da tela e você vai aplicar o estilo que eu colocar aqui dentro quando o tamanho da tela for menor ou igual a 720 pixels.

Então, o que eu posso fazer? Por exemplo, eu posso colocar um body e colocar o background-color dele de red, só para a gente ver se isso vai funcionar. E, quando a gente diminui, olha só, quando ele chegar em 720 pixels de largura, ele vai ler isso aqui, ele vai ler esse trecho de código. Então vamos lá, olha só, chegou em 720, ele mudou para o vermelho.

Eu vou colocar aqui 960, para poder ficar um número menor, para poder a gente demonstrar aqui na tela. Então vamos lá, a gente já viu que aqui funcionou, mas, quando chega em 960 pixels, ele aplica o background red. Então isso aqui já está funcionando.

Para poder construir a responsividade, o que eu teria que fazer? Eu teria que declarar o parágrafo aqui dentro e diminuir o font-size do parágrafo, por exemplo, para 16, e também teria que fazer a mesma coisa com o h1 e diminuir o tamanho dele para o quê? Por exemplo, 48, mantendo as mesmíssimas características, só mudando o font-size. Então isso aqui já seria uma responsividade com relação à tipografia.

Então, quando eu chego aqui, ele diminuiu. Então eu aumentei um pouquinho mais, passou da resolução de 960 para cima, ele aplica esse font-size aqui e esse font-size aqui, e, quando ele diminui, automaticamente ele mudou para 16 e para 48, adequando-se melhor à tela do dispositivo.

Então esse aqui é um jeito padrão de CSS puro que, por exemplo, quando você tem um trecho muito grande de código, você precisa sempre ver: "eu coloquei quanto no modo de tela desktop?", e depois você tem que descer novamente para poder ver qual foi o estilo que você aplicou aqui no media query. Então, por ser em dois lugares diferentes, fica um pouco desconexo.

## Um mixin de responsividade

Agora eu vou fazer utilizando mixins, para vocês verem o quão mais fácil fica. Como bem sabem, eu posso criar aqui um mixin com o nome de responsive, onde eu vou construir aqui dentro essa questão da responsividade. Então eu posso muito bem colocar aqui um media query da mesmíssima forma que eu fiz, and, coloco aqui um max-width de 960 pixels, e aqui dentro eu vou colocar o content. E o que essa função está dizendo para nós? Vou deixar ela aqui lá no começo do nosso arquivo aqui.

O que esse mixin está dizendo para nós? Eu criei uma função chamada responsive que eu vou poder chamar em todo e qualquer bloco, onde o conteúdo que eu passar dentro desse mixin, podendo ser fixo ou não. Por exemplo, se eu colocar fixo, eu posso colocar alguma característica aqui fora, então colocar font-variant small caps, e isso aqui é uma função fixa. Quando eu quero uma função mais variável, que eu mesmo coloque, eu coloco um content.

Então, olha só a beleza desse mixin, está vendo que voltou ao normal? Eu posso vir aqui no h1 e simplesmente dar um include do mixin responsive, está vendo? Quando eu dei esse include e eu não coloquei nenhum conteúdo, ele simplesmente vai aplicar o que tem de fixo aqui, ou seja, o small caps. Então vamos lá, quando eu salvo, a minha tipografia ficou com o small caps, mas ela continua sem ficar responsiva, então não mudou absolutamente nada, somente isso aqui.

Então eu posso colocar a característica fixa que eu quiser aqui dentro e construir o mixin do jeito que eu bem entender também, de aplicar em qualquer lugar simplesmente dando um include responsive, com o nome do mixin que eu dei aqui para ele.

Mas tem a opção também de eu colocar um content, um conteúdo aqui dentro, que o conteúdo que eu abri e colocar aqui dentro do meu mixin, colocar aqui dentro, ele automaticamente vai aparecer bem aqui, ou seja, ele já vai carregar dentro do media query. Então, quando eu abrir esse responsive, eu posso muito bem colocar dentro do próprio h1 um font-size de 48 pixels.

Então, olha só o que vai acontecer: quando chegou em 960, está vendo? Ele automaticamente modificou para mim, utilizando esse recurso do Sass do mixin junto com o content. Então, olha só como é que a minha responsividade fica bem mais fácil visualmente, porque eu estou aplicando no h1: aqui fora eu aplico para desktop, e aqui dentro eu aplico para dispositivos tablets ou mobile.

## Tablet e mobile

Se eu quero tamanhos diferentes, eu quero aplicar um para o tablet e um para o celular, por exemplo, nada te impede. Você pode criar um responsive-tablet, e aí você cria um outro mixin, responsive-mobile, para poder se colocar nos celulares, e vai lá e modifica, por exemplo, aqui de 960 você pode colocar para 720, no mobile um dia menor. E aí aqui você vai colocar responsive-tablet, e, por exemplo, quando chegar em 720, que é o mobile, você diminui mais ainda, por exemplo, 36 pixels.

E aí vamos ver se está funcionando: ele diminuiu mais ainda. Então nós temos aqui o maior; quando ele chegou em 960, ele diminuiu; e quando ele chegou em 720, ele diminuiu novamente. Então, só com mixin e com o content, eu consigo criar várias funções pré-definidas e adicioná-las onde eu bem entender.

Então eu posso muito bem, além de colocar small caps, eu posso colocar um text transform capitalized, por exemplo, ou então, deixa eu ver aqui uma outra opção, uppercase, deixar todas as letras em caixa alta. E aí, uma vez que eu mudo aqui, ele muda em todos os conteúdos. E, da mesmíssima forma, eu posso adicionar isso aqui no meu parágrafo e diminuir para 18 e depois para 16, está vendo?

"Ah, mas eu quero que, quando vá para o mobile, eu quero uma cor diferente, eu quero dar mais ênfase, então eu quero deixar mais visível", por exemplo. Então você pode muito bem colocar aqui color gray, para quando for no responsivo mobile dessa tag aqui, ele vai aplicar. Então vamos ver: ficou com o cinza mais claro quando trocou.

Então, olha só o poder que você tem de criar funções predefinidas aqui em cima, onde eu quero criar uma função de texto, ou então de texto de título. Então, title: você cria uma função de título e adiciona as skills de título, como, por exemplo, uppercase, small caps, ou então você vai colocar um peso tipográfico maior, como bolder, e aí você simplesmente vincula esse mixin dando um include dentro da tag que você quer aplicar, e também colocando o content se você quiser adicionar mais alguma coisa, beleza, pessoal?

Então, esse aqui é um recurso importantíssimo que eu uso para a responsividade dos meus projetos, vinculado a estruturas encadeadas de ifs, para deixar isso aqui ainda mais elástico, mas é um ótimo recurso que o Sass tem a nos oferecer. Então, falou, pessoal, até a próxima.
