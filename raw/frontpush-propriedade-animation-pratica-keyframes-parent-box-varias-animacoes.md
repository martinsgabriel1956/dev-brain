# Propriedade animation na prática: keyframes no parent e no box e várias animações

Então, pessoal, agora nós vamos de fato juntar tudo que a gente disse nas duas últimas aulas, vamos juntar os conceitos, tudo que a gente discutiu aqui. Eu reitero que você treine primeiro, que você entenda o que eu estou fazendo em cada passo, e é normal não entender tudo de primeira. Você vai pegando, você vai entendendo, você vai fuçando, mas você aprende muito fazendo. Então, não deixe de repetir as coisas que eu estou fazendo aqui.

## Os keyframes box e parent

Vamos, então, colocar aqueles efeitos que a gente colocou lá naquele primeiro momento, onde a gente estava mudando as configurações aqui pelo próprio console. E o que eu estava fazendo lá no console? Tem aqui o keyframes box. O que eu quero que ele mude? É o rotateX. Então, eu quero vir aqui, rotateX. Aliás, transform rotateX. E eu quero que ele faça de 0deg até 360deg, está certo? Deixa eu salvar aqui.

Então, eu quero que o box aqui dentro faça essa transição. E eu quero que ele faça essa transição juntamente com o meu parent aqui. Então, no meu parent, eu vou criar outro keyframe chamado parent para a nossa div de cima, para essa div aqui. E aí, eu quero que ela rotacione no eixo Y também de 0 a 360. Então, está aí.

## Aplicando com o shorthand

E aí, eu vou aplicar agora as animações. Vamos lá. Como é que eu vou aplicar aqui? Animation. Então, eu vou dizer o quê? Qual é o nome da animação do meu keyframe? Eu quero o box. Eu quero que essa linha do tempo seja de três segundos. Eu quero que ela se comporte com a curva ease. Eu quero que ela seja infinita e eu quero que ele vá alternando, faça de maneira alternada. Essa aqui de cara é a configuração que eu mais utilizo.

Se eu quisesse colocar algum tipo de delay, eu colocaria o delay aqui, dois segundos. Ele já identifica isso aqui como dois segundos. Aqui é sempre a duração, aqui é sempre o delay. E aí, meio que eu estou já englobando as características que eu sempre utilizo no dia a dia. São quase sempre essas. No máximo, eu coloco também um forwards aqui no final para poder fixar e deixar assim que acabar a animação no último frame que foi estabelecido. Mas, no caso, eu não quero agora não. Veja só assim.

E aqui em cima, eu quero aplicar exatamente a mesma coisa, só que aqui eu vou mudar para parent e aqui eu quero de 10 segundos, porque eu quero que essa bichinha gire mais devagar do que o do box. O box eu quero que ele seja mais rápido e que isso demore menos. E eu quero sem delay, então eu posso apagar que ele vai ficar sem delay e a gente vai executar para ver como está funcionando isso.

Olha aí como está dando a nossa animação. Legal, não é? Se você quiser aumentar mais ou deixar um pouco mais lento, coloca 5 segundos e aqui 15 segundos. Ele vai ficar transitando entre essas animações e está aí. Já criei um sisteminha legal e como ele é infinito, ele nunca acaba, ele sempre vai ficar aqui. Ele não vai voltar para o estado inicial.

## iteration-count finito

Agora, se eu colocasse, por exemplo, o iteration-count, só quero que execute três vezes e não de maneira infinita. Três vezes, vamos lá. Ele vai fazer três vezes esse movimento, depois vai parar e vai voltar para o estado inicial que está aqui na div .parent e na div .box inicialmente estabelecido. Está aí, terminou o tempo de 15 segundos desse maior. Começou de novo, mas ele voltou. Enfim, vocês conseguiram entender o que eu quis passar.

Vou diminuir o tempo para dois segundos e esse aqui um segundo para poder ir bem rapidão. Vamos ver o que acontece. Rodou, rodou, está aí e vai voltar para o estado inicial. Voltou para o estado inicial. O que eu estava falando não estava mentindo, correto. Beleza, galera?

## Várias animações na mesma classe

Então, essa aqui é a aplicação que eu posso emendar vários keyframes ao mesmo estilo, ao mesmo estilo, a mesma tag, a mesma classe. Então, se eu criasse, por exemplo, um outro keyframe aqui, um outro keyframe que, além dele fazer essa rotação, eu quero que ele mude a cor. Então, changeColor. Esse changeColor, eu quero que ele vá de uma cor background-color red para um background-color blue.

Eu quero que ele, juntamente disso tudo, eu vou colocar uma outra linha do tempo que ele faça essa transição. Então, vou colocar aqui de cinco segundos, aqui de 15 segundos e vir aqui e colocar... Eu separo uma linha da outra por uma vírgula, venho aqui e coloco changeColor. Vamos ver o que acontece.

Esse linear-gradiente aqui está meio que me atrapalhando, deixa eu apagar ele aqui. Está aí, agora sim. Ele está mudando a cor juntamente em uma outra... Keyframe, está vendo? E ela também é totalmente independente, eu posso colocar muito bem, trocar... Deixa eu colocar em infinito. Vai em infinito nas três. Vai em infinito, rodando para sempre. E vamos supor que eu quero colocar um segundo, para mudar bem rápido mesmo. Aí, infinite alternate vai ficar mudando para sempre, fazendo essa transição. Beleza?

## Trocando a curva pelo cubic-bezier

Ah, agora eu quero mudar a curva, eu não quero essa curva, eu quero que ele mude uma curva que eu vou criar. Aí, você vem aqui no cubic-bezier, vamos criar aqui uma curva. Supor que eu quero que ele faça muito rápido, muito rápido e depois vamos ver como fica. E no final, muito devagar, está vendo? Quase pararam.

E eu quero essa curva aqui, você vem aqui, copy e no lugar do ease, você coloca essa cubic-bezier, você vai ver que agora o flow vai mudar. Agora, se eu vir aqui em salvar, vamos ver como está a transição. Já mudou. Como o tempo está maior, está 15 segundos, 5 segundos, talvez você não está entendendo muito bem essa transição. Se eu diminuir aqui no box para 2 segundos, você vai perceber um pouco mais a transição, como ela está diferente, está vendo? Ficou mais acentuada essa transição, mas ele está aplicando certinho.

Beleza, galera? Então, olha o que eu falo para vocês, treinem muito, fucem muito e exercitem a criatividade de vocês para poder modificar essas características e, olha, vocês perceberam que quando você conhece animação, que é muito da sua criatividade, dos exemplos que a gente vai desenvolver aqui, para você desenvolver uma biblioteca de efeitos na sua cabeça, para você ir aprendendo com o tempo, mas não deixe de experimentar e tentar executar tudo isso que a gente desenvolveu até aqui nessas aulas para poder a gente aprender as propriedades. Beleza, galera? Até a próxima.
