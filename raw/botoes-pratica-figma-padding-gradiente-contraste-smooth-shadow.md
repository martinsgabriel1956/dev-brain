# Botões na prática no Figma: padding, gradiente, contraste e sombras suaves

Então, pessoal, conforme a gente combinou, depois da teoria, da gente ter discutido sobre esses temas aqui, vamos aqui voltar para o Figma, onde a gente vai construir alguns botões aqui e ver na prática como é que a gente faz isso.

## Altura e padding

Vou utilizar aqui como padrão esse próprio botão que eu fiz, vou colocar ele com a altura de 56. Lembrando, vai construir botão para interface, coloque um mínimo de 44 pixels.

Deixa eu copiar aqui também o texto, vamos lá. Pode fazer isso com Ctrl D ou Ctrl C, Ctrl V, que ele vai copiar para você. Clique com o botão direito, bring to front, que ele vai vir para a parte da frente.

Então, como eu disse, sempre procure colocar o espaçamento aqui, não tem como você medir certinho. Eu vou colocar aqui algum outro quadrado para vocês verificarem, mas olha só, ele está com a largura de 108. Então, eu vou procurar deixar no espaçamento, por exemplo, de 64. Vai ficar 64 de um lado, 64 de outro e eu vou ajustar aqui.

É bom que o próprio Figma faz essas medições para a gente de forma automática, você percebe que ele vai traçando as linhas. Então, está aí um botão legal de 64 de padding de um lado, 64 de padding do outro. No Figma é um pouco difícil de controlar isso, mas no CSS é muito fácil, porque ele vai ajustar o padding de acordo com o conteúdo. Então, você coloca o padding e não precisa mais estressar com isso.

Tem como colocar um pouco mais? Tem, não tem problema nenhum e não é uma regra que a gente leva muito ao pé da letra. Então, por exemplo, posso deixar 96. Então, 96 de um lado, 96 de outro e eu coloco aqui, meio que já está aí o meu botão, com a altura de 56 pixels.

## Branding, gradiente e contraste

Feito isso, sempre coloque o branding da sua marca, no meu caso, é esse gradiente aqui, porque o gradiente é mais bonito, enche mais os olhos do que uma cor sólida. Então, se eu fosse aplicar essa cor aqui, por exemplo, é legal, sim, dependendo da interface do branding que você tem, mas sempre que possível tente aplicar um gradiente que fique uma coisa mais interessante.

Sempre é importante a gente garantir a melhor legibilidade possível, ou seja, eu posso aplicar tanto um branco como um preto, no caso aqui ele está com um bom contraste entre eles. Lógico que o preto vai ter um contraste melhor, mas o branco não fica tão estourado, se fosse, por exemplo, um amarelo. Deixa eu colocar um amarelo aqui. Com certeza, nesse botão aqui, eu teria que colocar preto, a gente vai discutir isso um pouco mais em tipografia também,

## Border-radius, hover e tamanho do texto

para poder ter o border-radius aqui, border-radius 16, onde a gente consegue aplicar e a grande questão do momento é saber aplicar o efeito hover e como a gente exporta depois isso para o CSS.

E aqui eu mantive o tamanho 16, que já está meio que esquematizado aqui, o tamanho 16, a gente também vai estabelecer esses padrões de tamanho de texto em tipografia, a gente vai discutir isso e também quando a gente chegar na parte de interfaces web, quando a gente estiver construindo um style guide, inclusive isso aqui vai ficar para download.

## Plugin Smooth Shadow

Um plugin que é muito, muito legal, que vocês depois procurem para poder deixar as sombras as mais realistas possíveis é esse Smooth Shadow, depois vocês dão uma olhada, dão uma procurada, do nada mudou, eu queria aplicar no botão, deixa eu voltar aqui, não está aqui, vamos tentar aplicar nesse botão.

Você percebe que aqui você consegue mudar o quão opaco ou não está as sombras, aqui você modifica a quantidade de layers, está vendo crescendo aqui do lado, quanto mais camadas de drop shadow você aplica, teoricamente mais realista fica a sua sombra, então eu sempre aplico quatro ou seis layers para poder dar essa sensação e esse próprio plugin vai aplicando de forma gradativa, então a sombra que é mais perto tem uma opacidade maior e aí conforme vai se afastando as sombras vão ficando mais opacas, mais transparentes, dando aquela sensação de penumbra no botão e trazendo, consequentemente, mais realidade.

Então no alpha eu sempre deixo assim, bem pouquinho mesmo, o offset é literalmente o deslocamento da sombra, não sei se vocês estão conseguindo visualizar, eu vou aumentar a opacidade de propósito para vocês visualizarem, a opacidade, olha só, as sombras atacando, está vendo? Então sempre é legal deixar deslocada para baixo, vou diminuir aqui o alpha para poder ficar mais ou menos aqui, o blur é justamente o quão desfocado está a sombra, então aqui eu tenho como deixar nada desfocado e aí desfocado, entendeu?

E aqui eu venho aqui e seleciono a cor, no caso está preto e aí eu tenho que pegar a cor laranja, que eu nem lembro qual é, vou pegar aqui, por exemplo, essa cor laranja aqui, então é esse hexadecimal, eu copio, Ctrl C, venho aqui, abro o plugin, Smooth Shadow, é o color aqui, e aí você vai ajustando, porque o offset deles não fica muito bom, e aí você consegue aplicar, tem aquelas regrinhas lá no meu post, em soma eu deixo assim para poder ficar um pouco mais realista mesmo e aqui você tem um belo grau do que você aplica, não sei porque está dando pau esse negócio, mas está aqui, aplicou certinho.

Você percebe que elas têm que ser bem, como se diz, bem suaves, são sombras bem suaves mesmo para você aplicar, você percebe que a sombra fica mais na parte de baixo do botão, compreende, sei lá, se eu fosse estabelecer aqui, 80%, ela não cobre tudo, não é para ficar ao redor de tudo, é para ficar na parte de baixo, compreendendo aqui mais ou menos 80%.

## Sombras do Pegasus Design System

E aí eu gosto muito do design system do Pegasus, é só vocês colocarem lá no community do Figma, Pegasus design system, vocês vão achar e olha só a sombra que eles aplicam nos cards, tanto que é legal, tanto que fica bonito, entendeu?

Eu acredito que eu vi aqui em branding, olha só, a sombra de como eles aplicaram aqui e criaram o estilo da sombra, a gente vai discutir, vai ter uma sessão só para a gente trabalhar com sombras, e aí eu não quero dar spoiler lá, mas já dando o spoiler, olha só o jeitão das sombras, então só você clicar duas vezes, aí você vem aqui na propriedade aqui e clica nesse edit style, aí você vai conseguir ver, ele aplicou 32 para baixo, um blur de 64, 100 spread e 8% na cor 111, que é um cinza escuro, e aí vocês vão conhecendo os padrões de design system famosos e bonitos visualmente e literalmente copia para suas interfaces.

## Sombra sem plugin: o curinga

Quando eu não quero aplicar ou utilizar nenhum tipo de plugin, eu faço esse curinga aqui, eu venho aqui, deixo ele na parte de baixo, e aí geralmente eu aplico um blur que seja o dobro ou igual, então aqui eu aplico 32, 16, isso, legal, aí o blur eu deixo geralmente de 32, que é o dobro ou até um pouquinho mais, isso aqui não é uma regra, mas é meio que um caminho para você estar aplicando e com uma sombra bem suave, está vendo?

E aí eu coloco a cor de branding, e aí de no máximo 40%, então dependendo dela, deixo de 25%, vou diminuindo, e aí você percebe que a sombra está vazando muito aqui para o lado, para poder ela encurtar e ficar a 80% do elemento, eu sempre adiciono um spread negativo, então eu coloco menos 10, percebe que já ficou bem mais suave, está vendo? E ele sumiu aqui da parte do lado e ficou uma sombra um pouco mais suave, eu coloco menos 12, menos 16, e eu vou controlando o efeito hover para quando eu passar o mouse e deixar isso muito bem claro no meu style guide, beleza galera?

Então eu acredito que essas são as considerações que eu tenho a fazer sobre botões.
