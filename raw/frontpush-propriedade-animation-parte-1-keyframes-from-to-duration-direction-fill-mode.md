# Propriedade animation, parte 1: keyframes e as propriedades de animação

Opa, fala pessoal, agora nós vamos trabalhar a tão esperada e tão aclamada propriedade de animação, propriamente dito. Até então, a gente estava preparando o terreno, nós estávamos falando de conceitos para poder a gente chegar aqui e entender um pouco mais dessa propriedade, e a partir dela a gente vai executar muitos exemplos e conhecer mais como funciona isso aqui na prática.

Não se preocupe se você não entender tudo de cara, eu aconselho muito a tudo que eu fizer aqui nessa aula você tentar replicar e fuçar bastante, porque você vai aprender muito na prática esse negócio.

## animation e transition

Para poder a gente começar, eu queria voltar só nessa aula aqui de princípios de motion, lembrar desses conceitos, lembrar que nós temos uma linha do tempo, o CSS é de 0% até 100%, onde você define o tempo dela, então vocês vão entender um pouco mais desse conceito, entender o que é keyframe e entender esse carinha aqui que é o ponto-chave que eu quero trabalhar com vocês.

A tag animation simplesmente estabelece uma transição entre n estados, assim como a propriedade transition, que eu falei em alguma aula e para trás, que eu citei um exemplo de transitar entre um efeito hover, quando eu estava clicando nesse quadradinho aqui e ele estava rotacionando, eu estava utilizando o transition. A limitação do transition é que eu consigo utilizar apenas dois estados, um inicial e um final, e aí eu consigo estabelecer uma curva de transição e colocar o tempo de transição.

No animation eu consigo fazer essas configurações do transition e um pouco mais que a gente vai trabalhar agora, a gente vai passar agora, mas é o mesmo princípio, é isso que eu quero deixar bem claro.

## keyframes: from e to

Vamos abrir aqui o nosso exercício onde você lembra que a gente estava editando tudo pelo console e a gente mudava os valores e dava essa impressão de animação, só que agora nós vamos fazer propriamente dito utilizando o keyframes.

Então primeira coisa antes da gente iniciar, keyframes, agora é que vocês vão entender a magia do negócio mais ou menos. Vou dar um nome para esse keyframes que eu vou deixar de box, que é o mesmo nome da classe, não tem problema nenhum, abri e fechei e aqui eu vou começar a descrever como será minha linha do tempo definindo os keyframes.

Lembra que eu disse lá nessa aula que a animação se baseia em keyframes, onde eu vou deixando estados e vou especificando como é aquele estado e quando ele vai transitar de um estado para outro, ele vai ver o que muda dentre as propriedades que você estabeleceu e vai fazer essa transição de forma suave e não abrupta, é por isso que a gente vai entender um pouco mais do motion agora.

Então vamos lá, aqui eu posso colocar de duas formas, quando eu tenho apenas dois estados eu posso colocar from e to, de maneira bem simples do inglês, o from é tipo assim desde aqui ou então fato inicial ou ele está partindo daqui e indo para cá.

E aqui dentro dessas duas tags eu simplesmente vou colocar as propriedades que eu quero que mude, eu posso moldar absolutamente toda e qualquer propriedade do CSS, então se eu colocar o width de 50 pixels e colocar um width de 100 pixels, ele vai fazer essa transição dessa propriedade.

A única diferença e por isso que eu enfatizei, não é que você só vai poder utilizar a transform, eu dei um enfoque maior nessa propriedade porque com ela a gente vai conseguir fazer efeitos que com as propriedades básicas do CSS talvez a gente não consiga, então a gente conhecer essas propriedades aqui dá um ar de profissionalismo e até de liberdade de a gente fazer muita coisa, por isso que eu dei enfoque nelas, mas no keyframes nós podemos animar toda e qualquer propriedade do CSS que você viu até hoje, então desde cor, largura, padding, altura, box model, tudo que você colocar aqui ele vai fazer a transição, certo?

Então para poder a gente começar aqui e colocar alguns exemplos e passear dentre elas, vamos por exemplo deixar essa mesma opção de width, eu vou partir dele de 0 pixels até 100 pixels para ser formado a nossa div box, voltando aqui e apenas colocando essa seção aqui, vamos passear aqui pelas propriedades.

## As propriedades de animation

animation-name literalmente é o nome do nosso keyframe, então eu tenho que falar para ele, pega essa tag aqui box e segue o keyframe box, ele vai puxar então esse keyframe aqui vai ler ele.

animation-duration, ele vai estabelecer lógico a duração da minha linha do tempo, lembrando que a minha linha do tempo é de 0% a 100%, mas se eu não estou vendo 0% a 100% aqui, é porque eu coloquei o from e to, mas eu poderia muito bem colocar 0% aqui, 0% e 100%, sem problema nenhum, se eu quiser mais pontos eu preciso utilizar dessa nomenclatura, por cento aqui, então se eu precisar de colocar três pontos ou mais, eu vou colocar por cento, então eu posso colocar aqui 2%, 3%, 4%, 5%, quanto eu quiser, ele vai fazer essa transição, mas quando eu tenho apenas 2%, deixa assim ou com o from e o to, deu erro aqui, mas é porque eu deixei em branco.

Vamos lá, o animation-duration é literalmente o tempo da nossa linha do tempo, olha só, bem simples, então vamos supor que eu deixe aqui 2 segundos, pode deixar o tempo tanto em segundos como em milissegundos, aqui em ms.

animation-direction, literalmente ele vai dizer como o meu objeto vai transitar na minha linha do tempo, normal é o que? Ele vai de 0% até 100%, normal, e inclusive esse é o modo padrão, reverse, como o próprio nome já disse, ele vai de 100% a 0%, mas eu pedi para ele rodar quantas vezes, não faz sentido ele fazer alternada, mas é aquele negócio, essa propriedade alternate faz sentido quando eu tenho, e cito também o animation-interaction-count, que é quantas vezes eu quero que essa animação aconteça, eu posso estabelecer tanto um número fixo, duas vezes, eu quero que execute três vezes, ou maneira infinita, então na grande maioria das minhas animações eu deixo infinite e alternate, ele vai do 0% até o 100%, do 100% até o 0%, do 0% até o 100%, do 100% até o 0%, e o alternate-reverse, justamente ele vai ficar trocando essa ida, indo, por exemplo, do 0% até o 100%, do 100% até o 0%, e depois do 100%, agora vai partir do 100% e para o 0%, depois do 0% até o 100%, enfim, vai ficar invertendo, vocês vão entender melhor quando a gente estiver nos exemplos.

E eu posso muito bem colocar animation-interaction-count, é iteration, e eu coloco aqui para rodar, por exemplo, duas vezes, eu posso colocar o animation-fill-mode, ele é o que? Normal, como o valor padrão, só que eu tenho como colocar forwards e backwards, o que significa esse negócio? Quando você deixa ele normal, o que acontece? Tem aqui o estado da sua classe, vamos supor que eu deixe ele com width de 100, e aí na animação eu quero que ele vá para 150, certo?

Quando eu deixo ele normal, ele vai começar com 100 e vai vir aqui e ler, eu quero que execute esse keyframe, e leia esse keyframe e faça a animação, ele vai vir aqui no keyframe, vai o que? Colocar primeiro em 0, ele vai até 150, fez duas vezes, demorando 2 segundos cada, assim que acabar toda a iteração, toda a animação, ele vai voltar para esse modo aqui, então meio que ele vai de 0 até 150 e quando acabar de rodar aqui, ele vai voltar para 100, vamos supor que você quer que ele fique no estado final, que ele quer que fique em 150 e fique fixo, ele não volte para o estado inicial dele, e aí você vai colocar forwards, e se você quiser que ele comece com as características do frame inicial, você vai colocar backwards, e mais uma vez vocês vão entender com os exemplos, só estou explicando primeiro, então deixa aqui normal.

O que está faltando? Fill mode, o direction, delay, assim como o próprio nome já diz, bem intuitivo essa parte, animation-delay é literalmente um tempo para você deixar meio que em standby, então vamos supor que ele carregou o CSS, se eu não deixar em nada, ele vai executar assim que ler, então o animation-delay padrão é 0 segundos, se eu quiser que ele demore um pouco, vamos supor 2 segundos, ele vai ficar nesse estado inicial dele aqui, vai esperar 2 segundos e aí sim ele vai começar a animação.

E o animation time function é a forma, é a curva, então animation time function, olha só, tem o cubic-bezier, que eu também vou explicar para vocês, para não ficar essa aula muito longa, acho que eu vou dividir em duas vezes, mas é literalmente a curva e vocês vão entender o porquê, então eu tenho essas quatro curvas aqui padrões, tenho até mais que eu vou mostrar para vocês, tem como criar sua própria curva utilizando o cubic-bezier, que eu vou deixar em outra aula para poder deixar bem dividido e não muito massivo, mas a gente vai conhecer essas curvas aqui, é a forma de como vai transitar de um ponto a outro, e na maioria das vezes eu utilizo o ease, é a transição que eu acho mais legal, padrão, certo?

## Os exemplos do W3Schools

Vamos ver como é que ela funciona, vamos ver aí, olha só o que está acontecendo, mas antes eu quero passear aqui nas propriedades, nessas mesmas propriedades do W3Schools, antes da gente ir lá e aplicar na prática, que é para poder deixar o mais completo possível o conhecimento de vocês dessas propriedades, utilizando os exemplos deles, então não deixe de vir aqui, clicar, fuçar, teste, ele tem exemplos para exemplificar, olha só o que eu ia dizer, mas tem vários exemplos e falam o valor padrão da propriedade, então você acaba entendendo um pouco mais de como acontece isso na prática.

E aí você basta vir aqui em Play It e você vai começar a entender, demorou um segundo, se eu colocar cinco segundos, um, dois, três, quatro, cinco, aí só depois que ele entrou na linha do tempo.

O animation direction, olha só, default value, que é o normal, que eu acabei de falar para vocês, o normal, ele simplesmente vai fazer a transição do 0% ao 100%, normal, reverse, como o próprio nome já diz, ele vai do 100% até o 0%, o alternate, ele vai do 0% até o 100%, depois do 100% até o 0%, e o alternate-reverse, do 100% até o 0%, do 0% até o 100%, ele simplesmente inverteu, fechar aqui.

Animation duration, tem aqui um exemplo também, para você entender isso da melhor forma possível, um segundo, dois segundos, três segundos, é simplesmente o tempo do seu keyframe total, quanto vai durar a sua animação, o que mais, vamos ver aqui mais alguns exemplos.

O animation fill mode, do forwards, vamos lá, deixa eu ver aqui alguns exemplos, tem o both, que eu nem expliquei, olha só o que acontece, do primeiro keyframe, antes da animação começar, retém o valor de estilo do último keyframe, quando ela termina, então olha só, o último keyframe, color blue, o primeiro keyframe, color yellow, e no estado inicial da div, está vermelho, então deixa eu apertar aqui o Runner, ele vai começar com o estado inicial e vai terminar com o estado final, olha a reação aqui, o red, em um primeiro momento, e pode ver que ele deixou o animation delay de dois segundos, que era para aparecer vermelho, porque não começou ainda, mas como eu coloquei o modo both, ele já vai começar, independente do delay nas configurações do primeiro keyframe, então é interessante vocês verem aqui e pensar nesses exemplos.

O backwards, como eu tinha dito para vocês, ele está com animation delay de dois segundos, e ele está começando com o yellow, era para começar com o red, porque tem um delay aqui, então ele espera dois segundos para literalmente ler e executar o keyframe, mas como eu deixei backwards, o que ele está falando? Começa com as características do primeiro keyframe, então ele começa com o amarelo, está certo? Já o forwards, foi o que eu tinha dito para vocês, ele vai terminar e vai ficar nas características do último keyframe, ou seja, o último keyframe é o quê? 200 pixels, que ele fez a transição e o background blue, exatamente como ele terminou aqui, certo?

Deixa eu ver aqui mais alguns exemplos para a gente fechar essa primeira parte, backwards, animation-interaction-count, tem aqui uma vez, ele vai lá, terminou, volta para o estado inicial, foi o que eu disse, ele leu o keyframe, terminou, volta para o estado inicial, duas vezes, ele vai lá duas vezes, olha só, está certo que essa animação está um pouco lenta, mas olha só, é duas vezes fazendo 0, 100, depois 0, 100, você tem que tomar cuidado para colocar um alternate de forma que não fique abrupto, e aqui em infinite que ele vai ficar para sempre, certo? Interaction-count ou infinity, esse mesmo exemplo aqui.

animation-play-state, olha só, um que eu nem acabei de citar e está aqui, tem como você colocar ele pausado, tem como você pausar a animação, tem como deixar ela como running, aqui é o DefaultFollowing, e sempre vai estar rodando, ou simplesmente pausar, pausei, running, tipo um play-pause, literalmente, running, pause, running, pause, running, tem como você configurar isso também.

E o animation time function, que é a curva, se ela é linear, se ela é ease, ease-in, onde a gente vai trabalhar um pouco mais na próxima aula, então calma lá, e o cubic-bezier, que é uma ferramenta interessantíssima, mas ele tem aqui os valores padrões, aquele negócio é a curva, o linear é a mesma velocidade sempre, o ease, quando você olha para a curva, ele é mais rápido no começo e mais devagar no final, está vendo? O ease-in, o que você percebe? É porque aqui está ruim esse frame aqui, mas eu vou mostrar na próxima aula um frame que dá para vocês perceberem com mais ênfase essa diferença, certo?

## O shorthand animation

Então essas aqui são as principais propriedades, não, de animation, acho que são todas, foi mal, e essa tag animation aqui é um resumo de todas as outras propriedades, então quando eu estou escrevendo as minhas animações, eu não faço desse jeito, eu faço assim, meio que já está na minha cabeça, animation, aí eu coloco o nome, que é box, eu coloco o tempo, que é três segundos, eu coloco a forma da curva, que é ease, eu coloco infinity e coloco alternate, então eu coloquei tudo isso em uma tag só, mas eu já sei o que significa cada um e ele vem aqui e executa para mim normalzinho, fica infinito executando a animação, beleza?

Na próxima aula a gente vai trabalhar um pouco mais sobre essa curva aqui, entender como ela funciona e de fato botar essa nossa animação aqui para rodar, beleza? Até a próxima.
