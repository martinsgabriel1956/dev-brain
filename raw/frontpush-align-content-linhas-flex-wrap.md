# Align-content: alinhar as linhas de flex-itens quando há quebra

Fala pessoal, agora eu podia ter explicado o align-content depois que eu fui perceber, mas vamos gravá-lo aqui agora porque ele se dá justamente pelos vários elementos. Vamos mostrar aqui.

## Por que precisa de vários itens e de flex-wrap

Então, deixa eu mudar aqui, voltar o que a gente tinha feito, vamos deixar aqui exatamente do mesmo tamanho para poder a gente realizar esses testes. Está aqui do tipo baseline, então vamos lá. Vamos deixar aqui, por exemplo, do tipo center. Você percebe que no center ele meio que move o grupo todinho.

E se eu aplicar o align-content aqui, literalmente não vai fazer diferença nenhuma. Por quê? Eu só tenho um grupo pequeno. Para poder fazer diferença eu preciso ter um grupo maior, então eu vou copiar aqui, colar duas vezes, colocar 5, 6, 7, 8, 9, 10, 11, 12, com maiores itens assim.

E também a propriedade do flex-wrap tem que estar ativada para poder essa propriedade fazer sentido. Por quê? Porque ela ajusta quando tem muitos itens quebrados e ele vai gerenciar como eles vão se posicionar, da mesmíssima maneira que a gente fez nos outros, utilizando os mesmos princípios.

## Flex-start e flex-end

Então vamos lá, se a gente vier aqui em aplicar um align-content, vamos lá, o align-content, então vamos começar do começo, flex-start. O que o flex-start fazia no justify-content? Ele ajustava, ele alinhava à esquerda. Assim como o align-items, se eu colocar flex-start, ele vai o quê? Deixar lá no topo, tipo colado no topo, porque ele alinha na vertical, então vai ficar tudo colado no topo.

O flex-start no align-content: está vendo que os itens estão espaçados um do outro? Eles vão colar na parte de cima. Então está aí, colaram todos na parte de cima. Se eu quero que eles colem na parte de baixo, então vamos lá, flex-end, vão colar todos na parte de baixo.

Então é a maneira de como os itens se espaçam entre si quando eu tenho vários itens e eles estão com a propriedade de flex-wrap, e aí sim cabe o align-content. Por isso que a gente utiliza menos. Na maioria das vezes, pessoal, eu não vou utilizar esse tanto de item aqui. Pode acontecer em alguma interface? Sim, mas na maioria das vezes eu coloco três, nunca chega a ter muitas linhas acontecendo e eu faço mais uso do flex-direction. Mas é bom para a gente entender, para a gente lembrar.

## Stretch, center, space-between e space-around

E flex-end, flex-start, flex-stretch. A gente viu que o stretch vai completar o máximo possível, ele vai pegar o tamanho que tem disponível dentro do container e vai completar. Foi assim que a gente viu no align-items stretch da última vez, ele meio que dá um width ou um height de 100%. Então a gente vai lá, coloca flex, coloca aqui stretch. Como eu defini alguma margem aqui, ele não completou, mas olha só, ele vem nesse padrão tentando completar ao máximo.

Vamos ver aqui o center, vamos ver como funciona o center: todos ficam alinhados ao centro. Space-between e space-around. Então você percebe que é o mesmo conceito, só que aplicado de maneiras diferentes. São posições relativas com relação ao container ou com relação aos próprios conteúdos, que são os flex-itens; ou space-between, onde ele vai ficar colado. Então o space-around vai ter um espacinho, então, mais uma vez, ele vai deixar o espacinho em cima e o espacinho embaixo, e aí o space-between vai completar.

## Testar em coluna

E essas propriedades é sempre bom a gente trocar para column para ver como é que funciona. Então sempre troca para coluna e vai vendo o que vai acontecendo para você entender o máximo da propriedade. Olha só em coluna como é que acontece: space-between; se eu for colocar space-around em coluna, como é que fica? Ele dá um espacinho daqui e um aqui. Se eu colocar flex-start, vamos lá.

Então é legal a gente sempre estar testando as várias possibilidades para a gente ver o tanto de posicionamento. Você começa a perceber, isso aqui já é uma reflexão que eu já disse nessa aula, o tanto de posicionamento diferente que você pode só apenas com flexbox dentro de um mesmo container.

Vamos supor que eu quero simplesmente organizar as informações. Você percebe que eu vou precisar de um flex-start para poderem ficarem aqui à esquerda, e eu dou um space-around para poderem ficarem, vamos supor, distribuídos aqui. Mas se eu quiser que todo mundo fique alinhado também, é só eu dar um flex-start, vai todo mundo colar na parte esquerda e na parte do topo.

Então é legal a gente entender, e quando a gente for aplicar vai ficar bem mais fácil de a gente vir aqui, lembrar e voltar dessas propriedades. Na próxima aula a gente vai falar sobre flex-grow.
