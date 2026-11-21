# Propriedade animation, parte 2: as curvas e o cubic-bezier

Opa, então, pessoal, aqui vai a parte 2, onde eu falei que a gente vai trabalhar um pouco mais essa função aqui para que a aula não ficasse tão exaustiva na primeira, então eu dividi em duas partes e a gente vai executar aquela animação que a gente fez no primeiro momento, só que agora utilizando a propriedade animation e conhecendo um pouco mais, aplicando na prática.

Mais uma vez, essas propriedades são uma avalanche, vocês estão conhecendo, se aprende com o tempo, não se acanhe, é com muita prática que você vai pegando, fazendo todo dia, então não se preocupe com relação a isso.

## O editor de curvas do Chrome

Ele tem essa ferramenta aqui para poder a gente conhecer um pouco mais de como funcionam as curvas, esse aqui é o ease-in-out, ou seja, ele faz uma curvinha no começo e faz uma curvinha no final, então você percebe que ele vai mais devagar, depois mais rápido e depois mais devagar.

O ease, você percebe que ele vai um pouquinho mais devagar, mais devagar e depois vai mais rápido, esse aqui é o ease-out, que é o contrário. E aí, esses aqui são as formas de curva padrão do sistema, então se você colocar ease meio que já está ok essa forma, porque ela é muito utilizada. Aqui tem outras formas, que é a out-sine e a gente vai conhecer a forma das curvas, está vendo?

Aliás, como é que eu faço para acessar isso aqui? É só você vir no console, clicar na sua div, que aqui é o class-box, que é onde a gente está aplicando, ele vai aparecer aqui, esse Open cubic bezier editor, e aí tem como você ir conhecendo as curvas, out-back e conhecendo elas, que são todos padrões legais para poder a gente estar aplicando nos nossos projetos.

## Criando a própria curva

Ah, Násser, mas eu quero um padrão que é só o meu, aí você pode vir aqui e estabelecer o cubic-bezier, e aí você cria o seu próprio padrão de movimento, então você percebe que esse padrão aqui, o que eu estou fazendo? Ela está vindo muito rápida, aqui ela está quase parando e depois saindo rápida de novo, está vendo?

Deixa eu aumentar aqui, acredito que está ruim para vocês visualizarem, aí melhorou, então tem como eu criar a minha própria curva, no próprio console, então o que eu estou fazendo aqui?

Mais longe está da minha reta aqui, dessa reta cinza aqui, mais rápido é, então eu posso fazer assim, ela vai ficar muito rápida nesse primeiro trecho, está vendo? Muito rápido, mais do que nesse segundo, se eu esticar mais ainda aqui, ela vai praticamente parar no meio, e como fez uma curva aqui, ela vai ir e voltar, e aí depois ela vai rápido de novo, então você consegue meio que acompanhar, esse editor do Google Chrome é muito legal para poder a gente conhecer essa parte, para a gente construir a nossa transição entre os estados da melhor forma possível.

## O site cubic-bezier

Ou você pode vir aqui no Google, digitar cubic-bezier, vem aqui nessa primeira ferramenta, eu até deixei também no Notion, salvo me engano, onde ele consegue fazer a transição, aqui são os modos padrões, tem como mudar a duração, e ele faz a comparação de um modo normal, linear, com o que você acabou de criar aqui, mais uma vez, eu deixei muito rápido, então ele vai fazer o quê? Muito rápido, depois ele vai ficar devagar, depois muito rápido de novo, fazendo uma transição, indo e voltando, porque aqui ficou curvada.

E aí isso eu fui pegando com o tempo, depois de muito executar, eu fui entendendo como é que funciona esse gráfico aqui, você pode ver que é tempo, quanto você faz aqui da esquerda para a direita, que é o tempo, literalmente é a sua linha do tempo, e aqui no eixo vertical é a progressão, você percebe, vai rápido, rápido, rápido, como tem uma curvinha aqui, ele vai, depois volta, depois rápido, rápido de novo, e vai para o ponto inicial.

Se eu quiser deixar ele só rápido, eu tenho que deixar isso reto, o mais reto possível, para poder ele não ir e voltar, como eu tirei a curva aqui no meio, ele vai, depois vai de novo, vai rápido, fica um pouquinho parado aqui, vai rápido de novo, e a progressão de 2,3 segundos, e aqui eu estou fazendo a comparação desse módulo que eu criei, dessa curva específica, e estou vendo a transição, onde faz em dois segundos.

Se eu quiser essa transição, é só vir aqui em copy, aí eu copio, e ao invés de colocar ease, eu coloco o cubic-bezier, então ele já vai aplicar essa curva para mim, muito legal essa parte mesmo, então se eu vir aqui em salvar, e ver aqui de como está ficando a minha animação, se eu salvar aqui, olha só, ele está aplicando justamente essa curva, está vendo? Exatamente ela.

## A curva do carro freando

E a gente pode colocar a curva que a gente quiser, e aí a gente vai ter que começar a estudar qual é o tipo de curva, por isso que quando eu estava explicando aqui para vocês, qual é o tipo de curva que eu aplico quando eu estou freando um carro, ele tem que vir primeiro rápido, e aí quando ele está freando, ele vai diminuindo devagar, não pode ser abrupto e nem começar devagar, o carro primeiro vem rápido, depois que ele vai freando, vai indo devagar, então eu preciso passar essa noção na curva do motion, na curva que faz e caracteriza a transição entre os estados, então é isso que eu queria dizer para vocês.

Tudo junto, beleza?
