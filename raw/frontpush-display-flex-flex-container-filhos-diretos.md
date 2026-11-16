# Display flex: o flex-container e os filhos diretos que viram flex-itens

Então, pessoal, nós vamos começar agora. Como eu disse na aula passada, basicamente, a gente estuda dois pilares do Flexbox. A gente vai estudar primeiro as propriedades do flex-container, de como a gente define o Flexbox em containers.

Ah, Násser, o que é container?

Vou explicar para vocês, e depois como a gente aplica o Flexbox nos flex-itens.

## Os tipos de display

Então, basicamente é o seguinte, não tem aquele display, que é o display block, que a gente conversou também nas primeiras aulas de CSS básico? A gente entende que todas as tags são elementos de bloco, elas são box model. Por isso que a gente estudou o box model.

E aí tem o display-inline, que geralmente são para tipografias de texto, ou tipografias box de texto, ou seja, o span, o link, eles por padrão são display-inline. Tem o display-block, que se aplica a grande maioria e esmagadoras das outras tags, que é um padrão já do HTML. Tem o display-inline-block, e agora a gente está estudando o display-flex. Então, é assim que você aplica o Flexbox no primeiro momento.

## O que é o container

E aí você vai aplicar ele em um container. O que é o container? É literalmente a div da parte de fora. O Flexbox basicamente é uma div maior, onde quando você a define como um flex-container, automaticamente os filhos diretos se tornam flex-items.

Então, vamos supor que aqui eu tenho uma section e aqui eu tenho divs. Como eu tenho divs e se elas forem filhas diretas desse container aqui, automaticamente se tornaram flex-items.

## No código: centralizando o container

Então, vamos lá para o código para poder a gente enxergar isso da melhor forma possível. Vou apagar o que a gente escreveu até então. Vou apagar aqui também.

E o que eu vou fazer para poder deixar mais explicado? Vou aplicar aqui, section.container. A primeira coisa é definir um container.

Vou vir aqui no meu CSS, vou definir o body com o background-color, hashtag 1A1A1A. Da mesmíssima forma, eu vou aplicar aqui um Flexbox só para poder ele ficar no centro, mas calma que eu vou explicar. Então, não se acanhe. Display flex. Dei um justify-content center. Por quê? Para poder ele alinhar de forma horizontal e um align-items center para ele alinhar de maneira vertical.

Ou seja, toda e qualquer coisa que seja filho direto do body vai se tornar um flex-item. Então, o único que é flex-item aqui é a própria section. Percebeu? Então, eu estou definindo agora o meu body como flex-container. Mas calma que eu vou aplicar só no container para vocês entenderem da melhor forma possível.

Vou vir aqui e tratar a minha classe container. Vou deixar um max-width para poder ela ter um limite de 500 pixels. Vou definir um height também de 500 pixels para poder ficar quadradinho, para a gente enxergar como funciona. Vou aplicar um border de 5 pixels solid white para poder a gente enxergar.

Está aqui. Já apareceu.

Vou declarar ela como margin 0 auto. Por que, Násser? Porque vai ter margin 0 em cima e embaixo e automático de um lado e do outro. O que isso significa? Significa que vai se ajustar e ficar sempre ao centro. Então, meio que agora eu não preciso do display-flex aqui no body, ele já vai ficar centralizado. Porque quem está centralizando é essa minha margin, porque ela está automática na esquerda e automática na direita.

## Os itens: display block

Agora eu vou definir alguns itens que eu vou colocar aqui, div.item com a classe item e vou colocar item 1. E eu vou construir vários desses aqui dentro para a gente entender como é que acontece. Então, 2, 3, 4. Meio que já estão aqui.

Vou estilizar esses itens. Então, .item. Vou definir ele como um width que vai se ajustar. Vou definir somente um padding para poder a gente enxergar a caixinha da melhor forma possível. Então, vou definir um padding de 20 pixels para poder a gente enxergar e um background-color, vou colocar hashtag ccc.

Então, está aí. Vou colocar uma margenzinha para poder a gente enxergar de 5 pixels, diferenciar uma caixinha da outra. Então, está aí. Meio que eu estou vendo agora as caixinhas. Vou deixar um text-align center para as minhas caixinhas ficarem no centro.

Então, o que eu percebo? Quando eu tenho o display-block, que é o padrão do HTML, fica um item em cima do outro. Está vendo? Ele é exatamente assim e ele, por padrão, sempre ocupa 100% do elemento do pai. Então, se eu aumentar, por exemplo, o max-width do container de 600 para 700, olha só, as caixinhas vão acompanhar o tamanho, ou seja, está pegando, por padrão, também 100% do elemento do pai e o item automaticamente já vem como display-block.

## Display flex no container

E aí, o que acontece? Eu estou primeiro tratando do container. Então, vamos aplicar display-flex do container para ver o que acontece. Olha só o que aconteceu. Automaticamente, um item ficou um do lado do outro. Está vendo? Automaticamente.

E, automaticamente, o container se tornou um flex-container e esses itens aqui se tornaram flex-itens, porque eles são filhos diretos do container, da section. Se eu colocasse, por exemplo, um div do tipo span aqui dentro, ela não é filho direto, então ela não é um flex-item, certo? Então, é mais ou menos assim que funciona.

## Mais itens do que cabe

E aí, para poder a gente conhecer um pouco mais, que vocês já entenderam esse conceito, vamos verificar o que acontece quando eu coloco mais itens aqui dentro. Então, vamos lá, um, dois, três, quatro, eu coloco cinco, seis, sete, oito. Deixa eu colocar mais alguns para ver o que acontece. Nove, 10, 11, 12.

Olha só, eles começaram a extrapolar o meu max-width do meu container. E aí, a gente vai perceber que a gente vai precisar de outras propriedades agora aplicadas aos flex-itens para, por exemplo, eles identificarem os limites e quebrarem.

Então, no primeiro momento, o que vocês precisam entender nessa aula é isso, os filhos diretos se tornam flex-itens e o pai é o flex-container. Agora, a gente vai trabalhar algumas outras propriedades aqui para vocês entenderem mais na próxima aula.
