# 4 Hábitos de Programador Ruim

Você não é um programador ruim. Você pode ter hábitos de um programador ruim. E dentro desse vídeo a gente vai ver quatro desses hábitos, para dar uma clareada no que pode estar acontecendo.

## Ser vs. estar

É muito importante você aprender a diferença entre **ser** algo e **estar** algo. Por exemplo, quando as pessoas escrevem nos comentários dos vídeos algo do tipo "poxa, mas eu não sou um bom programador", eu fico louco — porque é como se eu tivesse lido algo do tipo "putz, eu sou cansado". Não: você pode **estar** cansado, assim como você pode **estar** num nível de programação ou desenvolvimento ruim.

E eu não sei se vocês já perceberam, mas parece que às vezes o cérebro se faz de burro. É muito engraçado: o pedaço de carne mais sofisticado desse planeta inteiro se depara com duas escolhas — uma que talvez vá gerar progresso, mas desconforto garantido; e outra que com certeza não vai gerar progresso, mas pelo menos o conforto está garantido.

Você pode estar se perguntando: "mas, só para confirmar — na primeira alternativa você não está garantido o progresso, mas está garantido o desconforto?" Sim. E é por isso que vídeos como certos conteúdos de confronto direto vão gerar a mesma quantidade de desconforto e progresso. E se você parar para pensar: se eles não gerassem desconforto, talvez não teriam chance alguma de gerar o progresso que geraram.

O artigo de hoje não vai gerar esse nível de desconforto, mas vai gerar um "eu preciso parar de fazer essas coisas".

O artigo foi escrito por um autor chamado Dan Abramov e se chama algo como "For Web Dev" (na ficha dele) — o link está na descrição.

## Hábito ruim número 1: falar "assim" para tudo

Como o autor do artigo colocou: falar "sim" para todo mundo, tentar ajudar em tudo, é sim uma postura muito louvável. Agora, a vida me ensinou rapidinho que uma promessa, na verdade, é uma dívida — e você tem que tomar muito cuidado para não sair assumindo dívidas de forma descontrolada, porque o limite do tempo vai estourar e os juros são extremamente caros.

E mesmo que você dê conta de falar "sim" para todo mundo, a sua performance como programador — a sua produtividade no geral — vai lá para baixo, de tantas vezes que você vai ser interrompido.

Eu sempre fui uma pessoa que falava "sim" para todo mundo, principalmente quando entrava em uma empresa nova — é um comportamento super normal. Se você está entrando numa tribo nova, em que as pessoas ainda te enxergam como um desconhecido, você quer mostrar que serve para alguma coisa.

Só que, às vezes, chega a um ponto em que eu comecei a perceber que eu virava uma espécie de "nicotina" — as pessoas ficavam viciadas em querer escutar a minha opinião sobre alguma coisa que elas iam fazer, sobre algum risco que elas iam tomar. Por exemplo: a pessoa escreveu um e-mail perigoso de se mandar, e ela pedia a minha opinião antes de mandar esse e-mail.

Chegou um ponto em que eu lia o e-mail, mas falava para a pessoa que eu ia dar minha opinião só depois que ela tivesse mandado o e-mail. E eu fazia isso por um motivo bem simples: se eu revisar o seu e-mail e der minha opinião — e talvez até alterar alguma coisa nele — se esse e-mail der errado, a gente vai dividir a culpa; e se esse e-mail der certo, a gente vai dividir a conquista.

Se você parar para pensar, vai ser muito mais poderoso para essa pessoa se ela assumir 100% do risco e 100% do retorno. São dessas pequenas oportunidades e interações — e são várias — que você começa a destravar novos líderes dentro da sua empresa, ao invés de ficar diluindo sempre na mesma pessoa. Você inclusive pode ter trabalhado numa empresa em que ela só consegue rodar se uma pessoa específica está disponível — isso é um saco, e é justamente o oposto de destravar as outras pessoas.

Isso leva a outra condição pela qual eu passava: as pessoas vinham com dúvidas em busca da resposta — só que tinha uma coisa estranha: parecia que elas vinham com o cérebro desligado. Aí eu falava: "interessantíssimo esse problema, e eu sei exatamente a resposta, mas não vou falar — você tem ferramentas o suficiente dentro da sua cabeça para descobrir a resposta também." Aí parecia que o cérebro da pessoa ligava de volta.

Agora, por favor, percebam se o nível de senioridade da pessoa está compatível com o nível de risco que ela está assumindo. Você não vai deixar uma pessoa que acabou de entrar na empresa, mal sabe programar, e ganhou acesso ao banco de dados de produção, te perguntar "vou dar sequência aqui no banco de dados de produção para atualizar o nome de um cliente" — achando que ela entende o mínimo de SQL — e não intervir. Nesse caso, o dia dela nessa firma vai ser bem agitado (e não no bom sentido).

No meio do artigo, o autor destaca uma frase de Paulo Coelho que diz o seguinte: "quando disser sim para os outros, certifique-se de não estar dizendo não para si mesmo." E eu adicionaria ainda que, se você estiver toda hora aniquilando o risco das outras pessoas, você também vai estar inibindo o surgimento de novos líderes.

## Hábito ruim número 2: a sua definição da palavra "pronto" possivelmente não é "pronto"

Na verdade, programação tem uma característica interessante: o ato de você digitar letras e números para formar um código é apenas uma das milhares de tarefas que um profissional precisa fazer. E é visível a diferença de comportamento entre um programador que entendeu isso versus um programador que ainda não teve esse clique.

Se você acredita que pegar uma issue, programar de primeira, e marcar lá no Jira que está finalizado — que o seu trabalho está pronto — é bem possível que você esteja muito longe disso. E eu falo isso porque: você chegou a olhar para o seu código de forma crítica e se perguntar se algum outro desenvolvedor conseguiria entender isso de forma fácil? Se não, essa é a maior lâmina que você tem para refatorar um código — e significa que realmente não está pronto, que o que você tinha entregado era apenas um rascunho.

Fora isso, a alteração que você fez teve algum reflexo em documentação? E, quando você está na posição de fazer o envio de um código (um pull request), você acaba lendo o diff à procura de erros de estilização do código mais do que realmente o que importa, que é a regra de negócio — só que isso é mais difícil de entender. E, por último, você acabou testando só o caminho feliz dessa implementação — e é por isso que a gente tem o próximo item.

## Hábito ruim número 3: não testar o seu próprio código

Nessa parte do artigo, o autor trata de um contexto em que existe um programador e um QA — alguém especializado em testar o código. Independente se na sua empresa tem essa configuração ou não, você testar somente o caminho feliz de um código que você acabou de fazer chega a ser tão bobo quanto você me falar que você concorda com a sua própria opinião.

Você precisa aprender a escrever testes automatizados, e eu sugiro que você comece o quanto antes, para ganhar prática e ganhar velocidade — inclusive até chegar ao ponto de, um dia, ser "enganado" pelo seu próprio teste, o que dói pra caramba. Então garanta o comportamento das coisas funcionando, e garanta também quando elas deveriam retornar mensagens de erro.

## Hábito ruim número 4: fazer commits gigantescos

Essa é fácil. Qualquer sensação que você sente quando precisa fazer o envio de um pull request gigantesco é um saco — você não sabe quando é que aquilo vai terminar, e aí não bate nem a vontade de começar.

O que eu quero dizer com isso é que é muito comum você fazer um commit que quebra um teste e, na sequência, fazer outro commit que conserta esse teste. O que eu sugiro que você faça daqui pra frente é: no mesmo commit, fazer a alteração do código e a alteração que faz o teste passar — transforme isso numa unidade de alteração funcional, e não num diário. Você vai perceber como cada commit vai se transformar numa coisa mais valiosa e bem modelada.

## Fechamento

Você está percebendo que tudo isso aqui está relacionado a ser um programador melhor, com menos hábitos ruins, e como consequência, mais bem remunerado. Super conectado a isso tem um vídeo no canal que vai mostrar para você — e para o seu chefe — por que bons desenvolvedores deveriam ser muito bem remunerados. É um vídeo que bombou aqui no canal, e se você procura ser mais valorizado na nossa área, é mandatório que você assista ele do início ao fim. Esse vídeo se chama "Checklist do Programador Sênior".

Falou, valeu!
