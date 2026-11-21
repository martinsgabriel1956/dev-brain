# Como usar o SVG: tag img, background-image, iframe/object/embed e inline

Então vamos lá, pessoal, na aula de hoje nós vamos ver as quatro principais formas, acredito que são as únicas quatro, não vi em outros lugares uma forma que saia dessas quatro aqui, mas se houver, por favor me avise para poder atualizar a aula, mas eu vejo essas aqui como as principais e vou dizer quais que eu utilizo, quais que eu não utilizo e qual a vantagem e desvantagem de cada uma.

E aqui vocês vão ver algumas particularidades que fazem com que trabalhar com SVG pode ser um pouquinho mais complicado, no sentido de inserir isso, principalmente quando você tem uma página com muitas ilustrações, vocês vão entender esse processo.

## Preparando o projeto

Então a primeira coisa é utilizar como uma imagem, literalmente utilizando a tag img que a gente está acostumado do próprio HTML, então vou demonstrar essa parte aqui na prática, onde eu já exportei esse SVG aqui, vou até exportar ele novamente, só que eu vou exportar ele com o fundo transparente, vou selecionar aqui o modo SVG e vou demonstrar para vocês na prática como é que se dá esse processo.

Vamos lá, vou recortar ele e vou colocar nessa pastinha chamada SVG que eu já abri no meu Visual Studio Code e aí eu vou criar uma pastinha chamada SVG e vou colocar o meu AppMessages aqui dentro e eu vou renomear isso só para app para poder ficar mais fácil.

Vamos criar aqui uma página HTML, então index.html de fora, HTML5 para poder a gente ter a primeira estrutura, onde aqui eu tenho a nossa aulinha, a aula SVG, onde a gente vai ver as principais propriedades. Deixa eu abrir aqui no Google Chrome para poder ficar lado a lado, para a gente visualizar da melhor forma possível as alterações que a gente vai estar fazendo.

Deixa eu criar aquele clássico CSS, esse aqui não pode faltar e eu crio aqui uma pastinha chamada CSS, aí eu crio um style.scss, que é um sass, mais uma vez, tem a aulinha de sass lá no meu YouTube, se você não sabe o que é sass, é um pré-processador só para poder a gente dar um boost no nosso alcance, com relação à compatibilidade dos comandos.

Eu vou aplicar aquele padding para poder tirar de todos os elementos, margem, colocar o box-size em border-box como referência, vou aplicar aqui no body, um width 100%, um height 100 e o background-color é aquele hashtag 1A1A1A que eu sempre estou utilizando e eu aperto para poder rodar o sass, ele compila, gera para mim o arquivo CSS um pouco mais otimizado com relação à inserção de WebKit, que traz mais compatibilidade entre os browsers, então ele fica mais performático, com mais compatibilidade.

## Compatibilidade no Can I Use

Uma coisa que eu esqueci, pessoal, de falar na primeira aula é o Can I Use, outra vantagem do SVG, já abri aqui, ele está compatível com a grande maioria de browsers, está vendo, pessoal, tem o Android browser, que ele não está sendo suportado, mas ele é muito antigo, está vendo? E aqui no Internet Explorer 6 e 8, então também muito, muito antigo, esses dois aqui têm uma taxa muito pequena, está vendo aqui, está em 0% de total de uso nele e 0,09% do uso do Internet Explorer, para todos os outros ele tem uma compatibilidade muito boa de todos os outros navegadores.

Então outra particularidade para você estar utilizando ele, está certo?

## SVG × PNG: o peso do arquivo

Então vamos lá, vamos salvar aqui, já está funcionando, onde nós temos aqui o SVG na nossa pastinha, web.svg. Primeira coisa, pessoal, olha só a estrutura do SVG, como é que se dá o código de um SVG, não se preocupe que a gente vai estar estudando o que significa cada coisinha desse aqui, ou pelo menos a maioria deles a gente vai estar entendendo por cima, mas é assim que é um código SVG.

E olha só a primeira diferença que eu quero mostrar para vocês e olha só quanto está pesando esse arquivo SVG, 8KB, está vendo? Propriedades aqui, para a gente ver em detalhes, tamanho 7,47, tamanho de disco 8KB.

Agora se eu pegar essa mesma imagem do mesmo jeito aqui e fazer o export dele para PNG, vamos ver o tamanho desse arquivo. Está aqui o PNG, acabou de abrir, pode ver que ele está transparente, a mesmíssima coisa, vamos clicar em propriedades, olha só, 728KB, então nós temos uma diferença notória de quantas vezes a gente só pega aqui 728 e dividido por 8, então 91 vezes mais leve, se eu pegar 8 e multiplicar por 91, vai estar o peso desse PNG, para vocês verem a diferença que tem do SVG para os modos de imagem e o tanto que ele contribui para performance dos nossos websites, esse aqui é o código onde a gente vai estudar ele ao longo das próximas aulas, mas calma, a primeira a gente vai ver como é que a gente insere ele.

## Primeiro jeito: a tag img

Primeiro jeito que eu disse para vocês, eu vou estabelecer aqui uma tag imagem e aí sempre tem o source e o source eu coloco caminho, como eu estou no index.html, eu já entro direto na pasta SVG, app.svg, dá um save e olha só, ele já está funcionando, mas quando ele se tornar responsivo, basta eu vir aqui no CSS e estilizar essa tag img, de forma que ela tenha 100% do tamanho do pai e eu vou forçar ela a ser responsiva, onde o elemento pai é o elemento body, que é da tela que também está em 100%, então você percebe que olha só a facilidade que dá para poder ele tornar fluido e detendo de todas essas propriedades e facilidades do mesmo jeito.

Então esse é o primeiro jeito, o segundo jeito que eu também coloquei aqui no Figma, estou esquecendo aqui onde está a aula, aqui é utilizando a tag img, eu utilizo esse jeito, geralmente quando eu estou utilizando algum tipo de ícone que eu não estou querendo animar ou fazer muitas modificações, eu coloco ele com uma tag img, que é bem simples, às vezes eu quero simplesmente uma imagem para ficar responsivo, do jeito que eu mostrei aqui para vocês, um ícone, ou qualquer coisa do tipo, não quero manipular tanto assim, eu utilizo essa tag e a desvantagem dela é que não tem edição no DOM, não tem como ter interação com o CSS, porque está dentro da tag img, não é o SVG puro, por assim dizer.

## Segundo jeito: background-image

Eu posso também utilizar ele como background image, então eu posso muito bem vir aqui, por exemplo, eu escrevo aqui uma div com a classe box, que tem uma div box. E aí eu vou lá no meu CSS e vou estilizar essa div class box, onde eu posso colocar aqui, background image, e eu pego aqui uma URL, como a minha array está sendo no CSS, eu tenho que voltar uma pasta, aí eu volto a pasta, entro no SVG, coloco aqui, posso colocar aqui background, e eu aplico as mesmas características que eu falei lá no script-fe, onde eu expliquei mais ou menos como é que a gente manipula essas propriedades de background, onde eu posso colocar background-size, cover, para poder ele pegar o tamanho da caixa, e aí eu coloco aqui o tamanho da caixa de width 100%, da mesmíssima maneira, e vamos ver como é que se dá o resultado.

Eu tenho que definir width-height, um height fixo, porque senão ele não vai aparecer, está aí. Então, da mesmíssima maneira, como eu defini um height fixo, deixa eu colocar um height aqui de 100vh, está aí, então da mesmíssima maneira tem como utilizar ele como um background também.

## Terceiro jeito: iframe, object ou embed

Esse objeto aqui, pessoal, eu não vou nem exemplificar para vocês, porque ele é muito ruim, é quando eu coloco ele em um iframe, em um object ou em um embed de forma embarcada, ele pode ser interpretado de forma diferente, ele é lento, é quando eu gero um código gigantesco para poder traduzir esse SVG aqui, então é um modo muito ruim que nem acho que vale a pena eu mostrar aqui para vocês, porque eu não vou utilizar ele de nenhuma forma, mas se vocês tiverem curiosidade, depois vocês pesquisem sobre data URI, essa forma, só que ela é lenta, só vi desvantagem e nem cheguei a considerar.

## Quarto jeito: inline

E esse cara aqui, que é o módulo que eu mais utilizo, que é o inline, que é literalmente o SVG puro, onde ele permite a edição no DOM, na árvore de elementos, onde eu consigo ter cada elemento de uma maneira separada e conseguir ter o CSS para interagir com cada uma dessas partes, então permite animação e interação HTML e não precisa fazer request HTTP, então isso aqui é uma vantagem porque não precisa ficar renderizando a página e pesando mais ainda, então o próprio SVG é literalmente um código direto, então ao invés de aplicar ele através de alguma div ou através de alguma tag, eu simplesmente venho aqui, Ctrl A, seleciono, Ctrl C e colo direto no meu HTML, Ctrl V, ele tem aqui e está aqui o meu SVG.

100%, vou poder pegar 100% do elemento do pai e ele fica responsivo do mesmo jeito, a desvantagem de você utilizar esse elemento aqui é que vocês podem ver que é o volume de código, olha só, um SVG teoricamente não é simplão, mas também não é muito complexo, vocês vão ver o tamanho do código quando eu tenho um SVG assim com muitos elementos, com muitas sombras ou então com vários elementos em si, vários caminhos, vários objetos dentro dele, fica bem maior que isso aqui, imagina você colocar vários blocos desse no seu código, tipo manchando o seu código, deixando ele muito maior, muito grande, onde você precisa de técnicas para poder deixar isso mais organizado possível.

E isso também é uma particularidade que eu vou falar para vocês que tem uma biblioteca do JavaScript que faz isso, meio que dá um include, então está aqui o arquivo SVG, ele vem aqui e dá um include nessa página, eu vou mostrar para vocês, se você utiliza PHP também dá para fazer, então vamos utilizar a linguagem de programação para poder inserir o SVG de forma inline aqui direto no nosso HTML para poder permitir isso tudo.

## Fechamento

Então essas são as quatro principais formas de utilizar o SVG, nós vamos dar muito enfoque nessa aqui porque é a que permite a gente fazer animação e interação, mas nos outros projetos a gente também vai utilizar essas duas formas aqui, beleza pessoal? Então na próxima aula a gente vai ver a questão de estudar mesmo como é a estrutura do SVG e a gente vai continuar avançando nesse sentido, beleza? Até a próxima aula.
