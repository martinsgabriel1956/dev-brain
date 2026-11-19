# Otimização de animações: pipeline de renderização, transform, opacity e a thread do compositor

Opa! Fala pessoal, sejam muito bem-vindos aí a mais uma aula da qual, na aula de hoje, nós vamos falar um pouquinho mais sobre otimizações em animações, né?

A gente viu aí em todas as aulas passadas sobre otimizações de desempenho para poder a gente utilizar bons formatos, para poder melhorar esse first load e todos os seus pormenores para poder a gente considerar. Mas eu deixei por último essa parte que a gente pode utilizar determinadas animações para poder melhorar a experiência do usuário, que isso conta para o Google, como a gente acabou de ver, e também como construir as animações de maneira mais eficiente, compreendendo um pouco mais sobre como são renderizados os elementos da nossa página.

Então, eu vou deixar também no Notion, tá bom? Então, por favor, se vocês tiverem mais curiosidade, podem entender. Mas eu já li esses artigos aqui, vou descrever aqui de maneira resumida, se você quiser saber mais detalhes, por favor, leia lá.

## Animação como comunicação e a tela de carregamento

Mas basicamente é o seguinte pessoal, as animações, elas são recursos para poder desviar ou então guiar a atenção do usuário da maneira correta. Então, é uma forma a mais de eu comunicar, assim como a gente utiliza as cores da forma correta para poder comunicar e guiar o usuário dentro da nossa interface, as animações são mais um recurso para isso. Então, por isso que não é interessante a gente sair utilizando animações em tudo que é canto, em tudo que é buraco, porque ao invés de ajudar, faz atrapalhar.

Mais uma coisa que é sempre interessante que eu coloco nos meus websites é essa página inicial de carregamento. Então, quando a gente acessa um determinado site, eu sempre coloco essa página inicial de carregamento para poder dar esse feedback para o usuário de que, ei, só aguardar um pouquinho que o site está sendo carregado e além disso, dar um tempo do website montar e evitar que ele seja montado de maneira errada ou então montado às coxas quando você tem uma baixa conexão, uma conexão ruim, ou então um celular com processador e uma GPU um pouquinho mais lenta.

Então, quando você adiciona esse screen loading, que é muitíssimo fácil, você pode dar uma olhadinha lá nos projetos do Spider-Man, você pode dar uma olhadinha no próprio projeto do Paybank, a gente trabalha isso só utilizando o GSAP e uma timeline. Então, esse tipo de animação é muitíssimo interessante, beleza?

## Teste no celular

Mas, vamos supor que você está construindo em um website e que está utilizando muitos elementos e que você está colocando animação em muitos elementos e que você viu que em determinados celulares está tendo queda de frames, está tendo um mau desempenho, o celular está esquentando, sei lá. Isso tudo, pessoal, muito de tudo que eu estou falando aqui é teste, teste, teste, teste, teste, teste.

Porque o que acontece, quando a gente está fazendo uma determinada animação, deixa eu até mudar para essa câmera aqui, quando a gente está fazendo uma determinada animação no computador, a gente tem que entender que o computador, geralmente, ele tem um hardware que não é minificado como o do celular. Então, ele tem uma zona de dissipação maior, ele geralmente é mais poderoso.

Por isso que o próprio Google, ele faz a divisão de análise de quando você abre um determinado website no computador e quando você abre um website no mobile. Porque hoje o mobile corresponde aí, vamos chutar aqui, conta de padaria, 50% ou mais dos acessos que são feitos em websites hoje em dia, ou então em apps, é tudo feito pelo celular, porque está na palma da mão pela facilidade. Então, a gente precisa considerar esse grande volume e tudo mais.

Então, quando você estiver escolhendo uma determinada animação para o seu website, tenha consciência de que você precisa testar em diferentes aparelhos, se possível. Sempre que eu estou fazendo um website aqui, eu não simulo ele somente aqui no desktop, eu faço questão de abrir ele, utilizando a mesma rede, você entra na mesma rede pelo seu celular, acessa ali o live server que você faz pelo próprio Visual Code, pelo próprio Visual Code Studio e você literalmente verifica como é o comportamento daquela animação.

Você verifica se o celular está travando e a gente vai entender um pouco mais por que o celular trava, por que tem queda de frame, qual é a ordem de renderização de determinada página, como é que a gente faz para poder melhorar o desempenho dessa animação ou até mesmo cortar.

Então, quando o website tem muitas animações, a primeira coisa é tentar otimizar dessa forma que a gente vai conversar aqui agora. Não deu certo, continuou travando, então capa no celular. Então, é melhor você ou deixar estático para o celular em algumas animações que você julga que pode você estar capando ali aquela movimentação, ou simplesmente tira mesmo, dá um display none, utiliza daquele recurso que a gente conversou nas aulas passadas e tudo mais.

## O pipeline de renderização

Mas basicamente, pessoal, quando a gente está renderizando, quando o nosso browser recebe aqueles códigos e ele vai renderizar as coisas para nós, ele vai literalmente traduzir aqueles códigos que ele recebeu em cores, em formatos, em pixels, ele passa por essas etapas aqui.

Então, por que algumas animações são lentas? Por favor, se vocês derem uma olhada com carinho para esse artigo aqui, é muitíssimo interessante.

Basicamente, olha só, é amplamente aceito uma taxa de quadro de 60 fps porque é fluido. O objetivo é animar qualquer coisa na web, então é uma grande referência tanto para jogos como aqui em renderização dentro do browser. Essa taxa de quadro garantirá suas animações terem uma aparência suave. Na web, um frame é o tempo que leva para realizar todo o trabalho necessário para atualizar e repintar a tela. Nós vamos entender um pouco mais o que significa isso.

Se o quadro não for concluído em 16.6 milissegundos, os usuários perceberão um atraso. Então, se eu estou querendo renderizar algo em 60 fps, cada quadro tem que ser feito em 16.7. Se demorar mais do que isso, eu vou perceber os travamentos. Ele vai ficar ali travando e não vai ficar tão fluido e eu vou conseguir perceber.

Basicamente, olha só, o pipeline de renderização de um browser é qual? Primeiro lugar, estilo. Segundo lugar, layout. Terceiro lugar, pintar. E quarto lugar, composto.

O que é o estilo? Calcule os estilos que estão sendo aplicados aos elementos. Então, é meio que um aparato geral, o que você está aplicando ali no CSS.

Segundo, layout. Gere a geometria. Espera aí, isso aqui é um quadrado? É um quadrado com borda? É o que? É um triângulo? Quantas bordas tem? Quais são os pixels? É um círculo? Qual é o border radius? Qual é o formato? Qual é a geometria daquilo que você está querendo me mostrar? Segundo ponto.

Terceiro, pintar. Literalmente, preencher os pixels em camadas.

Quarto ponto, desenhar as camadas. Como a gente já sabe, tem a propriedade z-index dentro do CSS para poder a gente ordenar se um determinado elemento está na frente do outro ou não. Então, ele vai definir isso.

E toda vez que ele renderiza, ele vai passar por esses quatro pontos nessa ordem. É isso que ele está dizendo aqui para nós.

## Transform × mudar a geometria

O que faz com que uma animação fique lenta? É quando você altera, por exemplo, a geometria. Ele tem que recalcular essa geometria base. Porque existe uma geometria que você pode modificar a partir da original, mas você continua guardando a original. Você guarda a modificação original e você modifica a partir da original. Essa é a propriedade transform do CSS. Mas existe outro tipo de modificação que é literalmente mudar a geometria. Vou te dar um pequeno exemplo.

É mais barato para o browser? Isso aqui ele está dizendo em outras palavras isso. É mais barato para o browser você pegar uma determinada geometria que está original e você alterar ela, mas guardar a geometria original, do que você mudar a geometria original. Porque ele vai ter que renderizar essa parte mais uma vez. E com mais elementos também.

Por exemplo, para poder ficar mais claro para vocês. Não tem a propriedade do transform? Então, se a gente vê aqui, já fazendo o link do como criar animações de alto desempenho, o que esse artigo está recomendando para a gente? Olha, para poder você ter alto desempenho, utilize somente essas três características. É obrigatório só utilizar essas? Não. Mas são as que têm mais desempenho. Por quê? Porque a propriedade do transform não vai alterar a geometria do elemento original.

Vamos supor que a gente desenhou um quadrado. A gente simplesmente foi lá, div, box, e aí a gente definiu um width de 64 pixels e um height de 64 pixels. Ou seja, a gente desenhou um quadradinho ali. E pintou de vermelho, por exemplo. Dando um exemplo aqui. Ele foi lá e renderizou. São renderizações básicas, você concorda comigo? Tanto pela área, como pela composição. Porque eu pintei de uma cor pura, eu não pintei de um gradiente. Eu não coloquei sombra. Porque quando você coloca sombra, dependendo da sombra, você tem que colocar mais camadas para poder deixar a sombra mais real. Ele vai ocupar um maior espaço. Se vai ocupar maior espaço, vai gastar mais pixels. Se vai gastar mais pixels, vai demorar mais para renderizar. Então, isso tudo você tem que levar em consideração.

E aí a propriedade transform, vamos supor que eu quero utilizar o transform scaleX. Então, se você for lá na W3C, vamos aqui no Google, google.com.br, a gente coloca W3C scaleX CSS 2D transform. Basicamente, olha só. Com esse transform aqui, nós temos essas propriedades aqui. Uma delas é a scaleX.

Então, se eu colocar scaleX 2.0, por exemplo. Eu desenhei um quadrado, correto? Se eu coloquei o scaleX, ele vai virar o quê? Vai virar um retângulo. Porque na escala do X, na horizontal, ele vai dobrar o tamanho do elemento. Mas na horizontal, quer dizer, na vertical, ele vai manter o tamanho. Então, ele vai virar um retângulo.

Vocês concordam comigo que a geometria original foi preservada nesse processo? Porque se eu tirar o scaleX, ele volta para o original. E eu posso conseguir esse mesmo efeito pegando o width, que estava de 64, e colocando em 128. Vocês concordam que vai ser o mesmo efeito? Se eu trocar o width de 64 para 28, ele vai ter o mesmo efeito de eu colocar um transform de 1 para 2 no scaleX. Mas qual que é o mais custoso?

Pois é, por incrível que pareça, o mais custoso é o width. Porque você está modificando a geometria da posição do elemento. Enquanto o transform está preservando o original, não preciso modificá-lo de novo, mas eu estou modificando ele a partir do original.

Quais são as outras coisas também? E por que ele colocou o opacity? Porque quando você coloca o opacity, ele também não altera a geometria. Ele só define literalmente a opacidade. Então, a geometria do elemento permanece a mesma. Então, eu quero que determinada coisa fique mais opaca. Entendeu?

Isso não significa dizer que quando você utiliza a opacidade, ou então o transform, que o transform é tão performático quanto o opacity. Isso é um engano. Porque o que acontece? A gente tem que sempre se lembrar desse pipeline de renderização. Ele sempre vai precisar renderizar novamente, quando você modificar a geometria e a posição. Ou seja, se você colocar vários elementos na tela com um translate, do transform translate, para poder ficar indo de um lado para o outro, pode ter queda de frame do mesmo jeito. Então, é só para você entender como tentar otimizar as animações nesse sentido.

Então, se possível, sempre utilize essas três características aqui. E tem essa will-change, que é uma característica muito interessante. Se a gente descer aqui, ele vai explicar para a gente. Evite propriedades que acionem o layout ou a pintura. Tá bom? E aí você força a criação da camada. Então, meio que você avisa para o CSS, olha só, ele vai mudar. Qual a propriedade? O transform. E aí você consegue melhorar o desempenho dela.

## Bom senso

Na minha visão, eu acredito que você aprofundar nesse tipo de coisa, no frigir dos ovos, ele não vai fazer muita diferença. Eu acredito que o que mais faz diferença é o bom senso. Porque eu já testei muito isso aqui. Eu já utilizei um site, por exemplo, com animações exageradas, com muitas animações ao mesmo tempo. Eu utilizei dessas técnicas aqui e continuo dando queda de frame do mesmo jeito. Então, vale muito mais a pena você ter o bom senso nesse sentido.

É lógico que é muitíssimo interessante a gente entender como é o processo por detrás dos panos. A gente entender como é que funciona o pipeline de renderização. Por que ele fala isso? Mas, no frigir dos ovos, pessoal, o que conta é o bom senso. Tá bom? Vocês podem testar aí.

## CSS × JavaScript e a thread do compositor

E uma outra coisa que eu sempre falei para vocês é qual que é a forma mais barata da gente fazer animações? Priorize o CSS puro. Você lembra que eu sempre dizia isso para você? Tem como fazer animações com JavaScript? Tem. Tem como fazer com CSS? Tem. Qual que é o menos custoso? CSS. Por que? Ele é nativo, ele é direto, e ele utiliza uma thread diferente daquela principal que é utilizada para poder, literalmente, fazer as ações do seu site. E ele está explicando isso bem aqui.

Então, o JavaScript é mais... Por exemplo, eu consigo fazer animações mais complexas com ele? Consigo. De forma mais fácil? Consigo. Mas tem esse lado da performance também. Então, sempre que é possível eu executar uma coisa mais simples, uma microinteração, um algo apenas com CSS puro, eu prefiro utilizar isso. Então, eu não saio utilizando toda e qualquer animação somente com JavaScript, por exemplo. Sempre que possível, CSS. Ah, é muito trabalhoso com CSS, não consigo executar com CSS e você vai para o JavaScript.

Mas olha só o que ele vai dizer aqui. Animações baseadas em CSS nos navegadores que suportam a API são normalmente tratadas em uma thread conhecida como thread do compositor. Isto é diferente da thread principal do navegador, onde são executados o estilo, o layout, a pintura e o próprio JavaScript. Isso significa que se o navegador estiver executando algumas das tarefas caras no thread principal, essas animações poderão continuar sendo interrompidas.

Basicamente, pessoal, o que ele está querendo dizer aqui? Para poder ficar mais claro para vocês, eu tenho que explicar para vocês um pouquinho, uma coisa pouca sobre gestão de tarefas quando a gente fala de, por exemplo, processador.

A gente sabe que existem tarefas e tarefas e o processador de um computador está sempre processando todas essas tarefas. E ele processa uma tarefa de cada vez. O que nos dá a impressão de ele ser multitarefas é que ele executa uma tarefa muito rápido e rapidamente corre para outra. Mas, no fundo, ele executa uma tarefa de cada vez. Só que ele é muito rápido, a gente está falando de gigahertz hoje em dia. Então, são escalas de 9, 10 elevado a 9. Então, é muito rápido, é coisa de nanossegundos que ele demora para poder fazer uma tarefa. E aí, tem tarefas que são prioritárias e tem tarefas que não são. E é assim que ele faz a gestão de tarefas dentro de um sistema operacional. Basicamente, é isso.

Quando a gente está falando do browser, é a mesma coisa. Existem ali uma fila de processos para poderem serem atendidos e eles podem utilizar de threads. Threads é basicamente um caminho virtual em que eu consigo, pelo fato do processador ser tão rápido, eu consigo dividir esse trabalho em mais threads, de forma que eu consiga executar coisas em paralelo, de fato, e essas informações consigam se encontrar, ou então que elas não dependam inteiramente de si, e aí eu consigo executar em paralelo e não dá problema. Meio que uma thread não depende da outra de forma direta para poder ser executada em questão de informações, de troca de informações. E aí eu posso colocar ele para realizar alguma coisa em uma thread e realizar outra. Então, esse é o famigerado paralelismo quando a gente fala da programação.

E aí, no nosso browser, acontece a mesma coisa. Só que quando a gente fala de CSS, ele vai executar na thread do compositor. E tem outra thread chamada thread principal. Pelo próprio nome, a gente já consegue definir que aquilo que é executado na thread principal, ele tem um caráter de importância com relação ao processo mais importante do que a thread do compositor. Ou seja, se você mandou alguma coisa para a thread principal e ela foi requisitada, ela vai passar na frente. Por isso que JavaScript está na thread principal.

Então, o que ele falou aqui? Isso significa que se o navegador estiver executando algumas tarefas caras, que são tarefas mais importantes, na thread principal, ele pode atrapalhar na outra thread que está sendo interrompida. Entendeu? Então, é melhor você utilizar CSS porque vai estar rodando na thread do compositor. Basicamente, é isso que ele está falando. Tá bom?

De qualquer forma, tem que sempre levar em consideração os pipelines de renderização, que são esses quatro aqui. Mesmo que você utilize todas essas técnicas e todas essas particularidades para poder a gente melhorar, é sempre o bom senso. Porque o que acontece? Renderizar uma determinada div com sombra, com gradiente, você está mudando o estilo, você está mudando o layout, você está tendo que pintar mais camadas. E isso é mais pesado mesmo você aplicando todas essas técnicas aqui de otimização de animações, basicamente. É isso que eu quero dizer para vocês.

Beleza, pessoal? Então, é isso. Utilizem de bom senso quando a gente estiver utilizando animações. Mais algumas características para a gente conseguir otimizar as animações também. E até a próxima.
