# Princípios de motion: linha do tempo, keyframes e transição entre estados

Então, pessoal, agora nós vamos conversar um pouco sobre princípios de motion.

Como o próprio nome já sugere, eu vou estar tratando alguns conceitos básicos para podermos entender como se dá o movimento, como é que se dá o motion design na interface, principalmente no CSS.

Lembrando que essas noções eu aprendi muito quando estava trabalhando com o programa do Adobe, do After Effects, para quem não conhece, para quem não sabe. É um programa do pacote Adobe, onde é justamente feito para poder fazer as animações, só que é de um nível muito mais complexo que no CSS, mas os princípios meio que se estabelecem. Certo?

Então, para podermos começar, para podermos entender, não tem como eu citar esses três conceitos aqui. Para podermos entender o que são keyframes, como é que se dá a transição entre N estados, porque o motion é feito justamente assim.

## Linha do tempo

Então, onde eu coloco esses dois aqui dentro da linha do tempo?

A linha do tempo literalmente é o tempo transcorrido de uma determinada animação, onde você define um tempo. Ah, eu quero que essa animação dure dois segundos. Essa é a linha do tempo, para poder aparecer uma determinada forma geométrica ou desaparecer alguma forma, ou aparecer algum texto, ele tem um determinado tempo, onde é determinada linha do tempo.

Nossa, não tem nada de interessante até aqui agora, mas eu vou demonstrar para vocês na prática.

Você define esse tempo como sendo um, dois segundos, ou até milissegundos, onde você consegue colocar pontos aqui, para poder dizer como esse objeto vai se movimentar, se ele vai crescer de um momento para o outro, ou se ele simplesmente vai aparecer já no tamanho original, se ele vai de uma opacidade de zero até uma opacidade de um, se ele vai de uma escala de zero até uma escala de um, ou se ele vai combinar esses dois efeitos, ele tanto vai de uma opacidade zero para uma opacidade um, tanto como ele vai crescer de pequeno até maior, até o tamanho normal dele, onde você vai colocando todos esses efeitos em keyframes, onde você vai lendo essas informações na sua linha do tempo e vai aplicando, vou demonstrar na prática para vocês entenderem da melhor forma possível.

## Keyframes

Mas o que é muito interessante também de eu citar para vocês, que além da linha do tempo tem a de como transita entre esses N estados, que são os keyframes.

Para quem não sabe keyframe, key vem de chave, frame vem de foto, é literalmente um breakpoint, um ponto, onde você adiciona uma determinada característica de forma que quando passa na fluidez do tempo, você pensa que é algo fluido, que é algo contínuo, que é justamente o conceito do vídeo, o vídeo nada mais é do que uma sequência de fotos tiradas, certo?

Só que como as fotos são tiradas pelo celular de forma muito rápida, quanto mais frames você tem em um segundo, mais fluido parece, por isso que quando você faz um vídeo em 60 fps ou quando você joga um jogo em 60 fps, ele parece mais fluido, porque tem mais frames em uma mesma janela de tempo e você consegue transmitir mais fluidez.

Então o keyframe é literalmente os pontos que você estabelece na linha do tempo que você consegue construir o seu motion, aquilo que você quer passar, a informação que você quer passar, o motion que você quer construir, certo?

## Transição entre estados

E a transição entre estes pontos, estados é muito importante, o motion que é a propriedade do keyframes que trouxe no CSS3, é justamente eu conseguir emendar vários estados em uma linha do tempo, então eu meio que posso colocar quantos estados eu quiser aqui dentro, de 0% a 100%, eu posso fazer um estado em 0,5%, outro em 0,7%, outro em 1%, outro em 5%, outro em 10%, em 20%, enfim, vocês já entenderam, eu consigo colocar N estados aqui dentro e construir estes keyframes, estes pontos onde eu vou modificando as propriedades do objeto, seja com escala, seja com opacidade, seja com translado, seja com skew, que aí eu consigo meio que inverter o objeto, deitar o objeto e construir literalmente um movimento, onde a transição entre eles é muito importante, porque eu dei um exemplo aqui, frear um carro.

Quando você está freando um carro, meio que o movimento é esse, eu preciso aplicar um movimento onde no começo do percurso o carro está mais rápido, quando ele vai freando, a velocidade dele vai diminuir, então se isso aqui for um gráfico de velocidade onde quanto mais perto aqui, mais rápido é, e aqui ele vai devagarzinho, então a transição entre os estados é muito importante, a gente vai ver todas as transições e como construir a nossa própria transição para poder a gente passar um motion, porque se eu fosse aplicar, por exemplo, o estilo linear ou frear um carro, seria totalmente irreal, concorda comigo?

Linear é esse aqui, a mesma velocidade que ele está no começo do percurso e a mesma velocidade que ele está no final, então talvez para poder frear um carro, eu teria que utilizar a transição do tipo ease, onde ele é mais o que? Aqui é o ease invertido, ele é mais rápido aqui no começo e depois ele vai freando um pouquinho, então a gente vai também estudar a transição entre os estados, para poder não ficar só na teoria.

## Na prática: a animação de lançamento do curso

Eu vou mostrar aqui uma animação que eu fiz para quando estava faltando três dias para o lançamento do curso, então olha só como é que se dá a animação, eu vou dar um F5, você percebe que a bolinha fez um determinado movimento, vamos analisar só essa bolinha pretinha aqui, só essa bolinha que apareceu aqui no começo, você percebe o que está acontecendo nela, quais são os keyframes dela?

Ela veio com um keyframe de escala, ou seja, ela começou pequena, ficou maior e depois diminuiu, então ela meio que foi de uma escala de 0 até uma escala de 1,2, que ela aumentou 20% em relação ao seu tamanho original e aí depois voltou para o seu tamanho original, então vamos aqui, F5 de novo para você perceber que a bolinha fez isso.

Fora isso, você percebe que o keyframe que eu também apliquei é um keyframe de opacidade, que ela veio transparente e no momento 20% do meu keyframe, ela já ficou 100% e eu consegui enxergar a bolinha como um todo.

E esse aqui é um elemento da minha animação, e eu aplico uma linha do tempo para cada um deles, o 3 é uma outra linha do tempo, essa bolinha girando, você está vendo que ela não está girando da mesma forma que essa aqui, esse primeiro arco dessa bolinha pequenininha, azul, ela está em um time diferente desse outro arco aqui, então é uma outra linha do tempo, então meio que eu tenho uma linha do tempo para cada elemento e aí eu trato de forma generalista isso aí.

Vou abrir aqui o código bem rapidinho para vocês entenderem, está aqui o CSS, esse aqui é o código, keyframe, eu estou aplicando o bounce in, eu acho que na bolinha, e aí ela começa opaca, ou seja, opacidade 0, e aqui eu vou definindo os keyframes, e olha só, a escala dela não era de 0, era de 0,3, então 30% do tamanho original dela quando ela começou no keyframe, a 50% do tempo, de 2 segundos, eu defini aqui o tempo do keyframe, ela já está com a opacidade em 1, ou seja, já está parecendo normal, e olha só a escala de 1, depois ela diminui um pouquinho, depois ela volta, e aí causa esse efeito que a gente acabou de ver aqui, para vocês entenderem calma que a gente vai tratar de muitos exemplos, vai ser essa parte bem calma para vocês entenderem como é que se dá o processo, mas eu já quero mostrar na prática como se dá para vocês irem entendendo, essa parte de animation aqui é um pouco pesada, vou deixar um pouco para depois, mas olha só, a primeira órbita, eu tenho a órbita 1 e a órbita 2, eu apliquei duas animações, dois keyframes, o primeiro keyframe é para aparecer, nesse keyframe de aparecer, simplesmente aqui, opacidade 0, escala 0,3, e aí no final eu quero que ele apareça e tenha a escala normal, padrão, ou seja, o tamanho padrão dele, e apliquei uma transição, apliquei um determinado delay e disse como é para terminar essa animação, calma que a gente vai aplicar tudo isso aqui, e apliquei um outro keyframe a esse mesmo elemento que é a órbita 1, que ele já dura sete segundos, que é onde eu defino a minha linha do tempo, o que eu quero que ele faça? Olha, no primeiro momento ele permaneça rodando em 0 deg, e aí ao final desses sete segundos ele tenha rodado 360, que é essa órbita aqui, então você percebe que as duas estão rodando.

Tudo se baseia nisso, em vários elementos, aplicando vários keyframes, numa mesma linha do tempo, cada um de forma independente ou não, é mais ou menos esse o princípio que a gente vai tratar, que a gente vai começar a nossa jornada para vocês entenderem cada etapa desse processo.
