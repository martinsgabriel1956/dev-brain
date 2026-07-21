# 3 pilares para testes automatizados e produtividade no dia a dia

> Transcrição de vídeo em português, fornecida pelo usuário como texto corrido (fala + trechos repetidos de edição/hesitação, sem pontuação/parágrafos). Reescrita como Markdown estruturado por seções, preservando o conteúdo e a ordem original, removendo apenas repetições de fala e cacoetes de edição de vídeo (ex.: "ah porra", "de novo", trechos cortados e retomados). Sem necessidade de tradução (fonte já em português). Autor identificado pelo próprio autor ao final do vídeo como "Erick Wendel" (menção a "eu sou Erick Wendel, te vejo no próximo vídeo"), criador de conteúdo sobre Node.js e testes automatizados, autor do treinamento citado "Método TDD/TJS".

Não é um vídeo para ensinar testes automatizados, mas lições valiosas que dá para levar para o dia a dia de trabalho: como o autor desenvolve testes automatizados, como divide as tarefas e qual o ferramental base que usa para iniciar um projeto.

Toda vez que você inicia um projeto novo, bate a dúvida sobre o que o projeto deveria ter desde o início — tanto ferramental que às vezes bate aquela ansiedade de pular direto para a implementação do código, e lá na frente você percebe que faltou alguma coisa e já é tarde para aplicar. O autor criou o próprio método para pensar, planejar e implementar projetos, onde testes automatizados aceleram a produtividade.

Quando envolvido em alguma tarefa, por menor que seja, o autor segue três pilares:

1. Só cair para a implementação depois de ter certeza do que precisa ser feito.
2. Tudo que for entregue precisa ser validado com testes automatizados.
3. Todo projeto precisa ter o setup de testes, o modo de depuração e o hot reload ativados antes de começar a codificar.

É comum receber uma tarefa, abrir o editor de código, sair construindo a estrutura do projeto, implementando rotas de API ou criando layout de páginas — e rapidamente se pegar pensando "o que era para fazer mesmo?". Aí você cai na real, percebe que o que estava fazendo não tinha nada a ver com o projeto, e acaba jogando tempo no lixo.

## Pilar 1 — Entender o problema antes de codificar

O grande problema em desenvolvimento é a comunicação. Lidar com código é o menor dos problemas — entender e ser entendido é o maior desafio. É comum times de produto passarem tarefas, o desenvolvedor implementar o que foi pedido, e lá na frente encontrarem alguma coisa que não estava prevista, obrigando a retrabalhar tudo.

A tática:

- Pergunte o que precisa ser feito e anote.
- Depois da explicação, diga o que você entendeu e a lógica das coisas.

É comum, nessa etapa, começar a falar e a pessoa te interromper para corrigir ou complementar algo. Nesse caso, avise: "calma, eu vou te explicar o que eu entendi, e depois que eu terminar você me diz o que está errado e o que faltou." Repita o processo até ter certeza de que realmente entendeu.

Isso mostra maturidade e faz a pessoa que está explicando repensar se a estratégia proposta é realmente a melhor. Com o tempo, você passa a antecipar problemas no próprio momento em que a pessoa está explicando a tarefa — por exemplo: "então é para eu atualizar a data de acesso toda vez que um usuário se logar, mas o que acontece se o cliente simplesmente sair da página sem deslogar?" Isso faz a pessoa perceber que o problema não estava tão claro quanto imaginava.

Esse hábito ajuda a ganhar respeito no time, dá certeza de que os principais problemas foram cobertos, e permite estimar tarefas sabendo que nada vai entrar no meio do planejamento — evitando trabalho em cima de suposições erradas.

## Pilar 3 — Ferramental: live reload, depuração e testes automatizados no editor

No início de um projeto, ou até mexendo em um projeto já em andamento, é comum sair implementando funcionalidades e, para validar se algo está funcionando ou verificar algum valor, perder muito tempo: dar um `console.log` na variável, disparar um request pelo Postman, esperar, e ver se o console log imprimiu; ou ir direto na página e ficar clicando em botões para depois ver o console log.

O problema é que isso geralmente precisa ser repetido várias vezes: alterar o código, disparar contra a aplicação, verificar o console log, e de novo — o que é uma perda de tempo, porque exige sair do ambiente de desenvolvimento e às vezes navegar por várias páginas ou caminhos da aplicação só para conferir se algo funcionou.

A dica é: no momento de criar o projeto (ou ao voltar a um projeto antigo), gastar as primeiras horas configurando o ambiente de desenvolvimento para ganhar agilidade até o fim do projeto. Passo a passo:

### 1. Live reload

Configurar os scripts do projeto para observar o código e reiniciar o servidor automaticamente a cada alteração.

- Para projetos web/navegador: o pacote **Browser Sync** é recomendado.
- Em Node.js (versões mais recentes): basta passar a flag `--watch` para ativar o live reload nativamente.

### 2. Modo de depuração no editor

Habilitar o modo de depuração no editor (ex.: VS Code) para que, ao apertar F5, ele rode o script com live reload e permita inspecionar o código clicando em uma linha, sem precisar sair do editor. Dando `Ctrl+S` para salvar, o modo de depuração reinicia automaticamente e o projeto para na linha marcada.

- Para o editor entender que o projeto deve rodar em modo de depuração, em Node.js basta passar a flag `--inspect`.

### 3. Ambiente de testes automatizados integrado ao debug

Com as duas práticas acima, ainda seria necessário disparar o request manualmente (clicando em botão ou usando alguma ferramenta) para validar algo, o que ainda tira o desenvolvedor do ambiente. Por isso falta configurar o ambiente de testes automatizados: toda vez que se dá `Ctrl+S` no código, os testes rodam, passam pela linha alterada e, se quiser, dá para colocar um breakpoint na linha e inspecionar os valores.

A diferença: antes seria preciso inicializar o servidor, colocar um `console.log`, verificar os valores em uma ferramenta externa, reiniciar manualmente e repetir o processo inteiro até resolver o problema. Com o setup completo, basta apertar F5, as validações rodam automaticamente, e dá para parar nas linhas sem sair da ferramenta.

### Montando o setup na prática (Node.js 20 + VS Code)

Ambiente usado: Node.js 20 e VS Code. É importante usar a mesma versão para reproduzir os mesmos recursos.

1. Inicializar o projeto e criar dois arquivos de exemplo: `service.js` e `service.test.js`. Exemplo simples usado: uma função que retorna o nome do usuário em caixa alta.
2. Configurar `"type": "module"` no `package.json`, para poder usar import/export (ESM).
3. Script de dev com live reload:
   ```json
   "dev": "node --watch service.js"
   ```
   Qualquer alteração no arquivo reinicia o servidor automaticamente — sem precisar descer ao terminal para reiniciar manualmente.
4. Script de testes, indicando a pasta de testes:
   ```json
   "test": "node --test test/"
   ```
   Por padrão, o runner nativo do Node.js (`node --test`) procura arquivos terminados em `.test.js`.
5. Cobertura de testes (ainda experimental no Node.js nessa versão):
   ```json
   "test:cover": "node --test --experimental-test-coverage test/"
   ```
   A flag `--experimental-test-coverage` mostra quais linhas do código executado estão cobertas por teste. Importante notar: no momento da gravação, essa flag ainda é experimental — a keyword deve sair conforme a feature amadurece nas versões futuras do Node.js.
6. Script de debug, linkando o debugger do VS Code à aplicação:
   ```json
   "test:debug": "node --inspect --experimental-test-coverage --watch --test test/"
   ```
   A flag `--inspect` abre uma porta (no exemplo, 9229) para conectar o Chrome DevTools ou o VS Code em modo de depuração. Combinado com `--watch`, qualquer alteração reinicia o projeto, roda os testes e valida a cobertura.
7. Configuração do `launch.json` no VS Code (necessária para rodar via `package.json`, garantindo que o mesmo comando funcione para qualquer pessoa do time, independentemente do editor usado):
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "type": "node",
         "request": "launch",
         "name": "Run test debugger",
         "runtimeExecutable": "npm",
         "runtimeArgs": ["run", "test:debug"],
         "skipFiles": ["<node_internals>/**"],
         "console": "integratedTerminal"
       }
     ]
   }
   ```
   - `skipFiles` faz o debugger ignorar código interno do Node.js (módulos internos) ao inspecionar.
   - `console: "integratedTerminal"` faz o resultado do comando aparecer dentro de um terminal integrado no VS Code, em vez de abrir um terminal novo a cada F5.
   - Observação prática: durante a montagem do setup, o autor notou que `--experimental-test-coverage` (coverage) não funcionou corretamente em conjunto com o modo de depuração (`--inspect`) — o coverage não aparecia. A recomendação final foi remover o coverage do script de debug e mantê-lo apenas no script de teste "normal" (sem debug).

Com o setup pronto, dar F5 já:
   - inicia o projeto em modo watch,
   - conecta o debugger automaticamente a cada `Ctrl+S`,
   - permite colocar breakpoints dentro dos próprios testes e dentro do código de produção,
   - permite inspecionar variáveis pelo "Debug Console" do VS Code, inclusive executando expressões arbitrárias ali (ex.: `user.email.replace(/\W/g, '-')`) sem alterar o valor real, ou atribuindo um novo valor à variável ali mesmo para testar um cenário.

### Tipagem forte em JavaScript puro via JSDoc

Sem precisar de TypeScript, dá para ter tipagem forte e autocomplete usando **JSDoc**:

1. Criar um arquivo `types.js` definindo os tipos de entrada e saída, por exemplo:
   ```js
   /**
    * @typedef {Object} IncomingUser
    * @property {string} name
    * @property {string} email
    * @property {string} password
    */

   /**
    * @typedef {Object} OutcomingUser
    * @property {string} name
    * @property {string} email
    */
   ```
2. No arquivo de implementação, importar o `types.js` e anotar o parâmetro da função com `@param {IncomingUser} user` — o VS Code passa a oferecer autocomplete de todas as propriedades do tipo ao digitar `user.`.
3. Anotar também o retorno com `@returns {OutcomingUser}` — o editor passa a validar e sugerir o formato do valor retornado, mesmo sem TypeScript.
4. O mesmo padrão vale no arquivo de teste: importar os tipos e anotar a variável de entrada com `@type {IncomingUser}` para ter autocomplete ao montar o objeto de teste.

## Pilar 2 — Como dividir uma tarefa em casos de teste, na prática

Depois de mapear o que precisa ser feito (pilar 1) e montar o setup do projeto (pilar 3), é hora de dividir o problema em pedaços. Exemplo usado: o repositório da **Rinha de Backend**, desafio online onde desenvolvedores implementam um projeto simples (independente de linguagem ou banco de dados) para comparar performance e acurácia. O desafio é uma web API que registra transações de crédito e débito de um cliente e guarda o histórico.

A especificação descreve o formato de entrada (valor da operação, tipo — crédito ou débito —, e descrição), mas não deixa explícita a regra de negócio completa — o que já é, em si, uma informação importante para anotar.

A partir das anotações do pilar 1, o autor recomenda criar três campos-guia para cada cenário, porque eles ajudam a decidir o que testar e como testar:

- **Entrada**: ex. endpoint com ID nas transações e o objeto da transação (valor 1000, tipo crédito/débito, descrição).
- **Processamento**: enquanto a regra não está clara, deixar em branco.
- **Saída**: conforme a especificação, deve retornar status code 200 e um objeto com o limite atual e o saldo do cliente.

Lendo as regras de negócio, aparecem informações valiosas: uma transação de crédito deve ser somada ao saldo do cliente; uma de débito deve ser subtraída. Casos de erro também aparecem: se uma requisição de débito deixar o saldo inconsistente, a API deve retornar status code 422 sem completar a transação; se o ID enviado for de um cliente inexistente, deve retornar 404.

Isso significa voltar às anotações e complementar, por exemplo pensando no caso de uma transação de débito: se o valor enviado excede o limite do cliente, deve retornar um erro dizendo que não é possível completar a transação. Para dividir ainda mais a tarefa, vale adicionar aos casos o formato "dado / quando / então" (Given/When/Then):

> Dado um cliente com saldo atual de 1000 e limite de 1000, quando receber o pedido de saque de R$ 2.000, então retorna status code 422 sem processar a transação.

E também o mapeamento completo entrada → processamento → saída para cada caso, por exemplo:

- **Entrada**: endpoint de clientes com ID nas transações, objeto `{ valor: 1000, tipo: "débito", descrição: "qualquer descrição" }`.
- **Processamento**: verificar o limite e o saldo atual, subtrair o valor da transação do saldo, verificar se o resultado excede o limite do cliente; se exceder, não processar a transação.
- **Saída**: status code 422.

Com tudo mapeado, é hora de voltar ao editor, criar o arquivo de teste e, para cada caso dividido em entrada/processamento/saída, criar algo como uma tarefa — um teste anotado (`it(...)` marcado, a ser implementado depois). Só depois de mapear todos os casos é que se cai para a implementação, e na hora de escrever o código do teste, escreve-se exatamente o que está nas anotações. Dessa forma, fica claro exatamente o que precisa ser validado — e usando as configurações de live reload, debug e automação de testes direto do editor, se uma regra estiver errada basta clicar na linha e inspecionar o problema.

## Conclusão

Entregar o que foi pedido corretamente não é opcional — mas também não é automático, porque somos humanos e cometemos erros. Os três pilares resumidos:

1. Só implemente algo que você tenha plena certeza do que precisa ser feito.
2. Faça um setup mínimo no projeto que ganhe velocidade (live reload, debug, testes automatizados integrados).
3. Valide tudo que for entregue com testes automatizados.

O autor menciona, como material mais aprofundado sobre o tema, um treinamento próprio (citado no vídeo como "Método TDD"/"Método TJS") de cerca de 4 horas, cobrindo desenho de testes, ferramental e cenários complexos do dia a dia.
