# A propriedade @import e os partials no Sass

Opa, então pessoal, vamos dar continuidade às nossas aulas, onde nós vamos começar a falar dos fundamentos do Sass, e o primeiro recurso que a gente vai estar apresentando aqui agora é o recurso @import. Você vai ver que os recursos do Sass, quando tem algum tipo de função, ele sempre começa com um arroba. Então aqui, @import, como o próprio nome sugere, ele possibilita você importar arquivo Sass dentro de outros arquivos Sass e compilar isso tudo em um arquivo só. E qual é a vantagem disso?

Primeiro, que melhora a organização. Por exemplo, você pode criar um arquivo só de cores, outro só de tipografia, outro só de layout, outro só de botões, fazendo com que aquele arquivo gigantesco que ficaria de CSS, você se perde muito fácil nesses arquivos. Então, quando você categoriza, você tem essa vantagem de ter mais organização, e também utiliza mais ou menos o conceito de componentes.

Otimiza a request do seu site. Por quê? Porque, por mais que você no Sass esteja dividido os arquivos em vários, um para cores, um para tipografia, um para layout, etc., ele vai compilar isso tudo em um arquivo só, que é a maneira mais otimizada de você colocar o CSS nos seus websites quando estiverem em produção, porque tem menos arquivos para carregar. Por mais que ele fique mais pesado, demora mais a requisição do que carregar um arquivo um pouquinho mais pesado, então melhora também a otimização do site.

O que eu vou dizer para vocês também é que a ordem importa. Lembre-se que o CSS lê linha a linha. Então, se tem um arquivo que você definiu um mixin, por exemplo, em tipografia, aliás, que você está utilizando um mixin, ou seja, uma função que esteja contida, por exemplo, em layout.scss, e você declarou ele depois de tipografia, onde você utiliza essa função aqui, ele vai dar erro. Então você tem que primeiro declarar o layout, que é, por exemplo, o lugar onde você define as funções, para depois importar os outros arquivos que utilizam dessa função, desse mixin. Vou explicar isso para vocês, não se preocupe.

E a última coisa que eu preciso falar para vocês é que tem o uso de partials, melhora e faz com que seja carregado em um só arquivo e não compile vários arquivos individuais. Calma, que eu vou explicar para vocês agora.

## Preparando o projeto

Então vamos abrir aqui o nosso "hello world com o Sass", onde eu vou criar um novo arquivo chamado style.scss, onde a gente vai estabelecer os primeiros recursos para poder a gente entender como é que funciona esse import.

Pessoal, eu vou fazer aqui uma formatação simples, então margin 0, box-sizing border-box. Vou aplicar aqui o body com 100% para poder forçar que ele sempre esteja no tamanho da tela, vou aplicar aqui um background-color, hashtag 0c0c0c, e aplicar um display flex, justify-content center e align-items center, para poder a gente começar a entender isso.

Vamos rodar o Sass aqui, olhei, funcionou, já está rodando perfeitamente, e ele cuspiu aqui esse arquivo CSS bonitinho. E aí é sempre interessante a gente observar como ele cospe esse CSS, ou como otimizado ele vai ficar, e é sempre bom reforçar para poder a gente entender a sintaxe. E aqui o link do CSS já está devidamente feito.

Deixa eu colocar aqui um h1, onde eu vou colocar color white, para poder a gente estar enxergando esse carinha aqui.

## Um arquivo de cores

E vamos demonstrar a função import. Vamos supor que eu venha aqui e queira criar um novo arquivo chamado colors.scss. Criei esse arquivo, onde eu posso, por exemplo, colocar aqui uma variável, onde eu posso colocar branco, e aí eu coloco fff, posso colocar cinza, então gray, e eu posso colocar hashtag ccc, para eu utilizar todas as variáveis de cores de forma categorizada. Então eu sei que esse arquivo Sass aqui vai conter as variáveis das cores, para, quando eu quiser modificar alguma cor, basta eu modificar nessas variáveis aqui e ele vai modificar ao longo de todos os meus arquivos.

Então, uma vez que são definições, e lembre-se que a ordem importa, então eu preciso definir esse colors aqui em primeiro. Então, logo no começo do nosso arquivo, eu preciso vir aqui, dar um import e colocar aqui colors.scss. Ele está exatamente no mesmo diretório, mas eu poderia muito bem criar uma pastinha aqui e colocar o caminho dela perfeitamente, mas como o style.scss e o colors.scss estão no mesmo lugar, não é necessário.

Então perceba que eu salvei aqui. Vou adicionar até uma outra cor aqui chamada preto, onde eu posso colocar hashtag 0c, 0c, 0c, e olha só, eu importei o colors aqui para dentro, e olha só como o meu style.css está sendo plotado. Calma, que eu ainda não utilizei. Então, ao invés de colocar hashtag 0c, 0c, 0c, eu vou colocar em forma de variável, por exemplo, preto; aqui eu vou colocar branco.

E aí eu vou colocar um pequeno span aqui, span só para a gente colorir e entender como é que se dá esse processo. Então vamos lá, coloquei aqui o span, e aí eu vou estilizar o span aqui dentro. E aí eu posso colocar, eu sei que o span está dentro do h1 e eu quero estilizar apenas o span dentro do h1, então eu posso muito bem colocar aqui span, e aqui colocar color gray.

E olha só o que vai acontecer, pessoal: quando eu atualizo, você percebe que eu coloquei no Sass com variáveis, coloquei preto, coloquei branco, coloquei gray, que são as cores que eu coloquei aqui. Até misturei em inglês com português, então não é legal, então deixa eu colocar aqui cinza, deixa eu colocar aqui cinza.

E vamos ver como ficou. Vou colocar aqui hashtag 555, escurecer mais um pouquinho. Então está aí, já salvou, só me certifiquei aqui, salvou, e eu alterei aqui, está vendo, pessoal? Coloquei aqui um cinza bem mais escuro, até ficou mais escuro do que eu queria, então coloquei 444. Posso salvar aqui, salvo aqui também, e olha só, ele modifica com as cores em outro arquivo.

## Partials

Só que tem um pequeno porém. Primeira coisa, você percebe que ele compila isso tudo em um arquivo só, style.css, que esse é o meu objetivo: gerar tudo em um único arquivo para eu vincular no meu index.html e ter essa subdivisão apenas no Sass. Porque, mais uma vez, se eu vincular vários arquivos em CSS, prejudica a otimização do website, porque vai ter vários requests de arquivo CSS.

E olha só, o colors: você vai perceber que, como ele é um arquivo Sass, também foi gerado nele um colors.css, está vendo? Foi também gerado um colors e um colors.css.map, e isso aqui não é muito interessante. O legal é eu gerar apenas esse arquivo CSS e não ficar gerando outros .css aqui dentro, eu quero ter apenas um.

E é por isso que eu coloquei aqui o recurso do uso de partials, onde, quando você coloca esse underline no começo do arquivo, você já está dizendo para o Sass o seguinte: "apenas copie e cole o Sass, mas gere apenas um arquivo final, não arquivos individuais de cada arquivo Sass, faça apenas no principal", ou seja, apenas no style.

Então, como eu posso modificar essa configuração aqui? Eu vou deletar esse carinha, vou deletar o map também, e aqui eu tenho o colors, eu vou renomear ele, vou colocar aqui o underline antes, e eu já tornei esse arquivo um partials. E eu posso simplesmente fazer um import colors, não necessariamente aqui eu preciso colocar .scss, que já vai funcionar.

E olha só, vocês percebem que eu acabei de salvar, ele não gerou um novo arquivo CSS do colors, e continua aplicando aqui, perfeitamente normal. Então, se eu vir aqui e modificar, por exemplo, a red, essa cor, ela também vai modificar automaticamente, e já está fazendo um import aqui. E, mais uma vez, ele está meio que pegando esse trecho, copiando, colando bem aqui onde está o import, por isso que a ordem importa, e gerando apenas um arquivo style.css já com as cores bem estabelecidas.

E olha só, como eu coloquei o h1 aqui dentro e o span, olha só como que ele cuspiu essa relação, bem organizado, já de maneira mais intuitiva, que eu acredito que assim é mais intuitivo. E assim gerando um arquivo CSS maior, mas que você pode até se perder mais facilmente nesse aqui, e no Sass ele fica mais organizado, porque tem essa seção de hierarquia aqui, você entende que esse está dentro dessa tag. Acredito que assim é mais fácil.

Então esse é o recurso de import, pessoal, que é muito importante para a gente melhorar a organização, e é assim que funciona, beleza? Então, falou, galera, até a próxima.
