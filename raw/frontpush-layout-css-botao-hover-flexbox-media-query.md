# Layout no CSS: estilo de um botão, hover e transition, flexbox e media query

Opa, fala pessoal, Násser aqui, sejam bem-vindos a mais uma aula de CSS. Na aula de hoje eu vou falar um pouquinho para vocês sobre os outros recursos do CSS e um deles é layout.

## Estilizando um botão

A gente acabou de ver, pessoal, que o CSS serve para poder a gente estilizar, então vamos lá, dar um pequeno exemplo aqui para vocês. Vamos supor que eu vim aqui e criei um botão, button, e coloque aqui, vamos estilizar esse botãozinho aqui. Como é que eu faço? Eu venho aqui, seleciono ele de alguma forma, utilizando os seletores das aulas que a gente já fez.

Vamos supor que eu queira tirar a borda dele, então borda é zero, ele tirou a borda. Vamos lá que eu coloque um background-color blue, está aí.

Ah, mas eu quero que ele tenha um padding, o button está muito apertado, então vamos colocar um padding de 10 pixels, então ele deu 10 pixels em cima e embaixo do lado do outro, beleza. Mas além disso, eu quero um margin, mas um margin só na parte de cima porque ele está colado ali, então vamos colocar 10 pixels também, desceu.

Mas eu quero que a borda faça um chanfradinho nas pontas, então coloca 4 pixels para ele chanfrar. Ah, mas eu quero uma circunferência, então você vai colocar 50%.

## Hover, transform e transition

Então vocês estão vendo que com o CSS, quando você vai conhecer nas propriedades, você pode colocar color white, você consegue estabelecer muitas coisas de comportamento, por exemplo, eu quero que quando eu passe o mouse em cima desse botão, ele cresça de tamanho, aí você vem aqui a button:hover, esse pseudo-element vai especificar quais são as características do botão que você quer que modifique quando eu passar o mouse em cima. Então, por exemplo, eu quero que ele pegue a propriedade transform e a escala dele aumente 5%, 0.05, olha lá, ele está aumentando.

Para poder isso acontecer de maneira suave, eu coloco um transition, você quer que faça essa transição em quanto tempo? Um segundo, então você coloca aqui em um segundo, ease, olha só, quando você passa o mouse agora, ele vai aumentar no início de um segundo, deixa eu colocar em 300 milissegundos, está vendo lá? Deixa eu aumentar para 1.2, olha lá.

## Do Figma ao CSS

Então você está percebendo que o CSS tem essa característica. Qual é a característica? É a característica de estilizar tudo, então a gente consegue muito bem pegar o que a gente fez aqui no Figma e conseguir traduzir para o CSS de maneira plena, porque é espaçamento, são caixinhas, essa caixa aqui tem um chão, tem um fundo diferente, tem um fundo de imagem, tem um fundo de linear-gradient, tem tal tipografia, como é que eu faço para modificar a tipografia? Você pode colocar que é o font-family, Courier New, está aí, entendeu? Ah, eu quero uma fonte mais pesada, com um peso tipográfico maior, você vai vir em font-weight, por exemplo, você vai colocar bold para ficar mais grossa a tipografia, então você está vendo que essas propriedades você vai entender ao longo do tempo, mas o CSS tem essa propriedade, eu vou conseguir estilizar do jeito que eu quero.

## Layout: desktop e mobile

Mas ele tem outra propriedade que é layout, então esse lance de a gente construir um layout para o desktop e um layout para o mobile, para o seu celular, você também faz com o CSS, mais um recurso dele e eu vou utilizar essa aula aqui para poder te exemplificar isso.

Por isso que tem, por exemplo, o CSS Flexbox e o CSS Grid Layout, ou Grid System com Sass, utilizando float e tudo mais, do qual eu vou dar uma palinha aqui para vocês, no primeiro momento você só entenda que ele tem essa função, se você quiser aprender mais sobre cada recurso, dá uma olhadinha nos módulos de Flexbox, de Grid Layout, de Grid System com Sass.

Mas olha só, eu tenho aqui uma div container, um div class item e eu quero que eles fiquem em linha, você está vendo que eles estão um embaixo do outro, então eles sempre são assim, mas eu quero que eles fiquem um lado do outro e aí quando for, por exemplo, para o mobile, eu quero que eles fiquem em coluna, então eu quero fazer esse toggle, como é que eu faço isso com o CSS?

## display: flex

Então vamos lá, nós temos aqui o container, primeira coisa, eu vou começar a mexer nas propriedades da caixa, é por isso que essas aulas que eu estou dando aqui, pessoal, são de Flexbox, quer saber tudo vai no módulo, quando eu aplico o display flex no container, eu estou falando, pega todos os seus filhos diretos, eles vão virar flex-itens e o container é o flex pai, automaticamente um vai ficar do lado do outro, quer ver? Um ficou do ladinho do outro, então eles já estão em linha, e é por padrão que o flex-direction é row, ou seja, linha em inglês, mas eu quero que quando vá para o mobile, ele fique em coluna, o que eu posso fazer?

## Media query: coluna abaixo de 960 px

Eu adiciono um media query e eu falo, a partir de tal resolução, fica em coluna, então o que eu posso fazer? Eu adiciono aqui um media screen and eu coloco aqui um max-width e uma determinada resolução, por exemplo, 960 pixels, o que eu quero que ele faça no container? Eu quero que o flex-direction vá para a coluna, então olha só, ele já modificou, está vendo?

Deixa eu aumentar essa tela, então pessoal, voltamos só para ter um cortezinho, é porque o Chrome estava salvando o arquivo no cache, não estava modificando, mas enfim, voltamos, basicamente é o seguinte, eu faço media screen, max-width e defino essa resolução, o que eu estou dizendo para o CSS? Fala assim, CSS, seguinte, você vai prestar atenção nesse trecho de código somente quando a tela do dispositivo for menor ou igual a 960 pixels, aí ele vai ler esse trecho aqui, do contrário, ele só vai ler esse.

Então você vai perceber que o seguinte, se eu vir aqui em inspecionar, vou deixar essa tela aqui maior, olha só, eu tenho aqui 1015, você está vendo que ele está vermelho, a partir do momento que eu chegar lá em 960, ele trocou para verde e os elementos ficaram em coluna, então é assim que eu faço responsividade, uma das formas que eu faço responsividade com o CSS é dessa forma.

## Estilo e layout

Fiz isso aqui só para poder ilustrar para vocês que o CSS não tem só a função de estilização, mas ele também tem a função de layout do seu site, você vai conseguir configurar a característica dele de ser desktop ou de ser mobile e as demais nuances de você, esse aqui eu tenho que diminuir a imagem, porque no mobile a tela é menor, eu preciso fazer isso, todas essas coisas você faz pelo CSS, está bom?

Então essa aula aqui é só para a gente trabalhar isso, enfatizar isso e tem aulas específicas para poder a gente trabalhar essa propriedade do CSS, beleza? Então falou pessoal, até a próxima.
