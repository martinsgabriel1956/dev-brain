# Três Estágios de Acoplamento e o Observer Pattern na Prática

**Fonte:** Transcrição de vídeo (canal não identificado na transcrição)
**Tema:** Acoplamento, Factory Pattern, Observer Pattern — refatoração de um jogo em JavaScript
**Data de adição:** 2026-08-04

---

É sério: você vai se sentir mais inteligente quando aprender design patterns. O motivo é bem simples e vou explicar de uma forma que você vai começar a notar as linhas do seu código de uma forma diferente, mais sofisticada. Isso significa que você vai estar aprendendo sobre arquitetura de software, principalmente sobre o critério **acoplamento**, que é uma das piores doenças que um software grande pode pegar. E não vai ser difícil, porque eu vou colocar uma sequência de ilustrações na tela que vai deixar fácil para qualquer pessoa acompanhar.

Fiquei pensando muito sobre qual seria a melhor didática para conseguir passar essa informação para vocês, e acho que consegui encontrar. Vou propor que vocês se façam uma pergunta bem simples, mas bem especial, toda vez que olharem uma linha de código. A boa notícia é que, dentro desse vídeo, a gente vai conseguir aplicar tudo isso na prática — inclusive vamos reformar o código do nosso jogo de duas formas, para novamente não deixar o seu cérebro escapar desse conhecimento.

Se você não está acompanhando a playlist, não tem problema. Em resumo: no vídeo passado a gente deixou o código no estágio de "ameba" — tem coisas misturadas, como por exemplo a responsabilidade da camada de input misturada com regras de negócio do jogo. Está tudo junto ali, mas de início é difícil perceber isso, e ainda mais difícil conseguir entender o que está acoplado ou não. Para treinar o seu cérebro a cobrar isso do seu código, nada melhor do que sempre se fazer um questionamento a cada linha de código. E essa pergunta é bem simples: **de quem é essa linha?**

Se você continuamente fizer essa pergunta, vai começar a prestar atenção na resposta. Aí a sua cabeça vai entrar numa recursão, porque você vai começar a se perguntar se essa resposta está certa — e é isso que vai começar a mostrar as divisórias do seu sistema, os limites dos componentes, e se um componente está acoplado a outro. Dentro de um sistema, se você 100% das vezes conseguir responder que aquela linha de código pertence ao mesmo componente, você tem um software "ameba" total. E se você não souber responder com clareza, você não tem a compreensão sobre a modelagem do seu código.

## Os três estágios de acoplamento

Fiquei pensando: como é que eu vou mostrar para vocês acoplamento de uma forma abstrata? Aí comecei a enxergar que existem três estágios de acoplamento. Os três estágios são igualmente importantes — nenhum é melhor que o outro, e já explico por quê.

Dando uma passada rápida:

1. **Primeiro estágio**: você possui código de vários componentes misturados, tudo ao mesmo tempo.
2. **Segundo estágio**: os componentes estão isolados, mas um componente chama o outro de forma estática/explícita.
3. **Terceiro estágio**: os componentes não se conhecem nem de forma estática — não existe declaração ou chamada direta dentro de um para o outro.

Para chegar nesse terceiro nível de desacoplamento, vamos utilizar um design pattern chamado **Observer**. A gente vai passar por todos esses estágios dentro desse vídeo, e na verdade já programamos um deles — o nosso código atual da camada de input está uma bagunça.

Se me perguntar "de quem é esse código?", é difícil responder. A primeira linha até é fácil: tenho o evento, tem uma chave que foi pressionada, então tem uma variável chamada "key press" que com certeza é da responsabilidade da camada de input. Mas se eu começar a descer, fica difícil saber de quem é. Na metade parece que é da camada de input, mas depois tem uma certa regra de negócio que faz uma verificação sobre uma regra do jogo, e logo embaixo tem outra regra de jogo. É estranho começar a responder isso dentro da camada de input.

Voltando para a ilustração: é como se a gente tivesse várias responsabilidades emaranhadas dentro de um mesmo local. E por que eu falei que um estágio de desacoplamento não é mais importante que o outro? Porque fazer esse tipo de código é excelente para protótipos — para você conseguir, da forma mais rápida e barata, testar sua ideia. É tão importante quanto o resto, porque você também aprende rápido o que você não sabia sobre a sua própria ideia, e isso só se descobre colocando a mão na massa, executando. Garanto que vão surgir várias coisas bizarras nessa hora.

## Segundo estágio: isolando com Factory

Para a gente conseguir chegar no segundo estágio de desacoplamento, as camadas precisam estar isoladas — mas mesmo assim existe um certo acoplamento, porque uma das camadas vai ter que conhecer a outra, porque vai estar escrito no código, de forma explícita/estática, um método (ou o que for) a ser executado de outro componente.

Para o nosso código conseguir chegar nesse segundo estágio, primeiro vamos isolar a camada do jogo num componente separado. Vamos criar esse arquivo de uma forma bem simples, mas depois vamos deixá-lo robusto ao ponto de se separar de fato num arquivo isolado. Vocês vão tomar um susto quando a gente usar esse exato mesmo arquivo para a dinâmica do jogo no front-end e também no back-end — vamos fazer algo assustadoramente prático, mas isso fica um pouco mais para frente.

O design pattern que vou usar para isolar a nossa camada de jogo se chama **Factory**. Não vale a pena aprofundar demais nesse pattern dentro desse vídeo, mas em resumo: é um pattern super normal onde você tem uma função normal que, quando executada, retorna uma instância — retorna o objeto — e você vai poder utilizar esse objeto.

Agora tenho em mãos uma função chamada `createGame` que, quando executada, retorna um objeto. Dentro desse objeto a gente vai conseguir acessar uma propriedade chamada `multiplayer`, que tem uma função que recebe um comando como parâmetro. Esse comando é um objeto que tem uma propriedade `keyPress`. Quando escutamos esse método, ele vai jogar na tela algo como "player X key pressed".

No navegador, criando uma instância desse jogo (`const state = createGame()`), a gente consegue acessar o método `multiplayer`, passando um comando do tipo `{ player: 1, action: 'up' }` — e era isso que a gente precisava para começar a programar o segundo estágio de desacoplamento.

Para engatar isso na camada de input, primeiro renomeei a variável `game` para `state`, porque quero aproveitar o nome `game` para um próximo passo. Criei a instância do jogo (`const game = createGame()`) e fiz um negócio que todo desenvolvedor tem certa resistência em fazer: deletar código. Selecionei tudo que a gente tinha ali e deletei. Quanto menos resistência você oferecer para deletar código, melhor — é como reconstruir um músculo: às vezes você precisa quebrar ele para reconstruir de uma forma melhor, mais robusta.

Programando a chamada do método: a primeira linha continua sendo claramente da camada de input (`event.target.value` — isso é sem dúvida input). O comando em si ainda é meio estranho, ainda não sei responder claramente de quem é — depois vou deixar isso mais dinâmico. Mas `game.multiplayer(...)` com certeza é da camada de game — o método não tem do que duvidar.

Para afrouxar ainda mais o acoplamento, você poderia usar injeção de dependência para injetar uma instância do objeto jogo. Mas lembre: mesmo no segundo estágio, a camada de input ainda acaba conhecendo o código da camada do jogo — e tudo bem, a maioria dos softwares é construída assim, incluindo com injeção de dependências, que é fundamental para conseguir fazer teste unitário e de integração.

Só o fato de termos chegado no segundo estágio de desacoplamento já significa que vou poder mexer na camada do jogo sem tocar em uma linha da camada de input. Implementei dentro do método `multiplayer` tudo que a gente tinha antes de deletar o código — nada muito diferente, na real. O que fiz foi puxar para dentro do escopo do `createGame` o nosso estado, que contém os players e as frutas, e no final exponho na camada pública do objeto que ele retorna. Toda a lógica de comandos que a gente tinha criado no vídeo anterior virou um `switch` dentro do método `multiplayer`, no lugar daquele monte de `if`. Isso não resolve a quantidade de condicionais — é virtualmente a mesma coisa. No próximo vídeo vou refazer isso e remover todas as condicionais.

Como a camada de renderização não estava acessando o estado do jogo através do método, temporariamente exponho o caminho para ela conseguir voltar a acessar os players e as frutas. Voltando ao navegador, dando refresh, funciona normalmente, com o adicional do log que foi colocado no método do jogo — mesmo comportamento de antes.

## Terceiro estágio: Observer Pattern

E agora me pergunto: como seria o terceiro estágio de desacoplamento? Agora vem a parte legal: como é que eu consigo fazer esse código continuar funcionando sem sequer ter essa função declarada no meio do código de forma estática? É aí que entra o design pattern **Observer**.

Na minha visão, esse é o pattern mais simples de utilizar se você quiser chegar nesse estágio de desacoplamento. Vai existir um objeto chamado **subject** — por enquanto, numa perspectiva simplificada, é o objeto principal. Em seguida existem outros objetos que a gente vai chamar de **observers**, que vão observar o subject. A mecânica é: toda vez que o subject alterar seu estado, ou fizer algo que ache importante, ele vai notificar os observers — mas de uma forma especial. Digo isso porque o subject não está preocupado se alguém está escutando ele ou quem está escutando ele — é como se fosse um objeto "arrogante" que, quando achar necessário, só fala: "toma, quem tiver interessado nessa informação, aqui está." Os interessados recebem a informação e fazem o que quiserem com ela.

Talvez vocês estejam se perguntando: até que ponto eu consigo dar para todos os meus objetos esse poder de "falar" (emitir informações) ou de "observar" (receber essas informações)? Teoricamente é ilimitado — é só questão de implementar os métodos certos nos objetos. É isso que vamos fazer em vários objetos do jogo.

Vamos transformar a função de renderização no subject. Mas antes vou primeiro transformá-la numa factory, da mesma forma que fiz com a camada do jogo, para isolar ela, e em seguida vou implementar os métodos necessários para transformar ela no seu subject de fato. Não fiz nada demais — a única coisa que fiz foi criar uma factory e mover todo o código da implementação passada para dentro dela, sem mexer em nada. Salvando e voltando ao navegador, o reflexo se comporta exatamente da mesma forma que antes — mas agora tenho a modelagem que preciso para transformar isso num subject e, em seguida, encaixar os outros componentes do jogo para eles começarem a observar seus movimentos.

### O que foi implementado

São três coisas principais:

1. Criei um método chamado **`subscribe`**, que recebe uma função observadora. Essa é a forma de um observer se registrar dentro de um subject.
2. Guardei essa função em algum lugar: dentro de um array chamado `observers`, que fica dentro da variável de estado (`state`). É um objeto que contém a lista dos observadores.
3. Criei uma segunda função/método chamado **`notifySubscribers`**, que recebe o comando e propaga a notificação — fazendo um loop por todos os observers e executando cada função que estiver ali dentro.

Alguém pode se perguntar: dentro dessa função que faz o loop para avisar os outros, isso é o "observer" em si? Não achei um padrão em implementações que, por exemplo, recebem o objeto inteiro e executam uma função padronizada tipo `update` — onde todos os objetos sempre executariam uma função `update`. Acho muito mais flexível passar a função na qual você quer que o dado chegue — você pode passar qualquer função que quiser. Por isso o parâmetro se chama `observerFunction`: pode ser qualquer função, nem precisa ser de um "observer" formal. O subject vai pegar essa função e executá-la com os valores que estiverem dentro do objeto comando.

A cada `keyPress` que um jogador fizer, o subject vai notificar todos os observers registrados: dentro do `keydown`, chamamos `notifySubscribers`, passando um objeto com o player e a ação pressionada — o mesmo formato que era injetado no `game.multiplayer` antes. Vai fazer um loop por todas as funções registradas e, para cada uma, vai executá-la com esse objeto de comando.

Agora uma pergunta importante: dentro desse código inteiro, tem alguma linha de código da camada de jogo? Não. Não tem uma linha de código da camada de jogo aqui. Isso é incrível — tão incrível que, ao salvar e voltar para o navegador tentando mexer no jogo, vai dar problema, porque não registramos nenhum observer. Tanto que aparece no log "notify: 0" — toda vez que aperto uma tecla, ele de fato está executando a função de notify, só que com zero observers registrados.

Vamos registrar um observer. Só dentro do `main.js` é que essas duas camadas vão se comunicar. Voltando ao navegador com refresh, o jogo volta a se mexer. Um outro teste interessante: comentando o código do `subscribe` e salvando, o jogo deveria parar de se mexer — e para. Descomentando de volta, funciona novamente.

## Trade-off: complexidade vs. flexibilidade

Uma pergunta honesta que vocês podem estar se fazendo: isso trouxe mais complexidade — e o benefício compensa? Ótima pergunta, e é por isso que eu gosto de programar. É sempre um trade-off: isso com certeza traz mais complexidade, e se você fizer só um `subscribe` com um `observer`, talvez não valha a pena mesmo. Mas a partir do momento que você começa a anexar mais observers, começa a ficar muito interessante, porque o impacto no código existente é praticamente zero.

Por exemplo: imagina que eu não quero só atualizar o código no cliente, mas também, ao mesmo tempo, mandar os exatos mesmos comandos para o servidor. Simulando um componente de rede (`network`) que se inscreve para escutar exatamente os mesmos comandos — é só chamar o método `subscribe`, o mesmo método que está exposto para escutar os comandos, o quanto quiser. Se você quiser atualizar várias partes de uma tela através do mesmo evento, é só inscrever vários observers para o mesmo subject.

E é legal porque você pode fazer isso de forma dinâmica, como fizemos no meio do código, dentro do browser mesmo (lembra que fizemos o `subscribe` no meio do código?). Isso dá o poder de, dependendo do que aparecer na tela, você fazer o `subscribe` ali — ou até descobrir métodos que ainda não implementamos e vamos implementar depois. Do contrário, sem esse desacoplamento, você teria que implementar dentro do objeto principal todos os métodos e condicionais para ficar checando se aquele negócio está aparecendo na tela ou não.

Mas o benefício real ainda está por vir. Dada a dinâmica multiplayer e a necessidade de usar a camada de network apenas quando implementarmos essas coisas, é aí que vocês vão perceber o quanto esse pattern vai acelerar todo o desenvolvimento.

## Próximos passos

O próximo passo agora é finalizar a camada do jogo, porque em seguida a gente começa a entrar na camada de network, no servidor.
