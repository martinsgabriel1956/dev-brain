# Como funciona o Node.js

Bom, e antes da gente partir para o código, primeiro a gente precisa falar um pouquinho sobre o Node.js, que é a tecnologia de back-end que a gente vai usar para desenvolver todos os projetos ao decorrer do curso. Então, bora lá!

## O que é o Node.js

E a primeira coisa que a gente precisa ver, então, obviamente, é o que é o tal do Node.js. Diferente do que muita gente pensa, o Node não é uma linguagem de programação. O Node é uma plataforma, ou você pode chamar também de runtime, que permite que a gente execute código JavaScript, que aí sim é uma linguagem de programação do lado do servidor.

Inicialmente, como você deve saber, mas se você não sabia, você vai ficar sabendo agora, o JavaScript foi criado para executar apenas nos nossos browsers, para a gente rodar apenas nos nossos navegadores. Só que, lá em 2008, uma versão do Chrome foi lançada e junto com essa versão, veio um carinha chamado V8. O V8 é um interpretador de código JavaScript.

O que é um interpretador de código? Vamos por partes. Vamos imaginar que você é um brasileiro que está tentando conversar com um japonês. Se você não falar português, aliás, se você não falar japonês e o japonês não falar português, você concorda comigo que essa comunicação não vai acontecer? Vocês não vão conseguir se comunicar? Para que ela aconteça, você precisa de alguma coisa ali no meio do caminho, seja uma pessoa, por exemplo, que fala os dois idiomas ou até mesmo um Google Tradutor da vida, para que você consiga colocar ali o texto em português e na outra ponta saia em japonês e vice-versa.

É exatamente esse o relacionamento do JavaScript com a máquina. A máquina, ela não consegue entender o código JavaScript que a gente escreve. A gente precisa de alguma coisa ali no meio do caminho, que pegue o código que a gente escreve e traduz para uma linguagem, para um idioma, entre aspas, que a máquina vai conseguir compreender. E é exatamente esse o papel do V8, de um interpretador de código, no caso aqui do V8, para interpretar o código JavaScript.

Então entendido o que é o V8, por que eu te expliquei tudo isso? Basicamente porque lá em 2009, de novo, aqui a timeline, 2008 foi lançado o V8, o V8 é open source, ou seja, é código aberto, quem quiser pode ir lá, pode acessar e ver o código. Então, lançou em 2008, em 2009, um carinha chamado Ryan Dahl, pegou esse V8 e executou ele no servidor, ou seja, para interpretar o código JavaScript ao invés do lado do cliente, do servidor, e aí nasceu o que a gente conhece hoje como Node.js.

## Call Stack

Beleza, então entendido o que é o Node, agora a gente vai começar a se aprofundar um pouquinho mais e entender como é que o Node executa o código que a gente escreve, como é que funciona a arquitetura que ele tem ali por trás. E para isso a gente vai começar falando então sobre a Call Stack, que é a pilha de processamento do nosso código, ou seja, todas as funções que a gente executa vão para essa pilha. Eu sei que pode estar um pouco confuso de entender, mas relaxa que a gente vai ver isso aí agora.

Então vamos começar analisando esse código aqui. Quando a gente executar ele, o JavaScript vai ler de cima para baixo, vai declarar todas as três funções que a gente está criando ali em cima, e lá no final de tudo ele vai invocar a função printDouble passando o valor 2. Quando ele invocar essa função é que entra a nossa Call Stack em ação, entra em cena.

Bom, como eu disse, todas as funções que a gente executa dentro do nosso código vão para dentro da nossa Call Stack, vão para dentro da nossa pilha de processamento. Então a função printDouble já está lá, beleza? Aí dentro da função printDouble a gente está chamando ali na primeira linha a função double, logo a função double também vai para dentro da nossa Call Stack. E aí dentro da função double a gente chama a função multiply. Então imagino que você já deva presumir que a função multiply também precisa ir lá para dentro da minha Call Stack.

Bom, e aqui a gente chegou no seguinte. Dentro da função multiply a gente não vai para mais nenhum lugar, a gente não chama nenhuma outra função ou coisa assim. A gente simplesmente pega os argumentos de A e B, multiplica um pelo outro e retorna o resultado. Então a partir do momento que a função multiply está retornando essa multiplicação quer dizer que o papel dela já foi concluído. Logo ela pode simplesmente sair da nossa Call Stack porque ela não está mais precisando processar nada. E a mesma coisa acontece com a função double. Ela só precisava pegar o valor, o retorno da função multiply e retornar para frente. Então ela também pode sair da nossa pilha.

E aqui a gente já conseguiu identificar uma característica da Call Stack que é a seguinte. A primeira função que entra é a última a sair. Então a multiply, como vocês viram, ela foi a última função que entrou ali dentro da nossa Call Stack e foi a primeira que saiu. Em contrapartida, a função printDouble foi o ponto de entrada, foi a função que a gente executou lá embaixo do nosso script, ou seja, foi a primeira coisa que a gente executou e ela ainda está ali na pilha. Então a gente já chamou a função double, chamou multiply, a multiply já saiu da pilha, a double já saiu da pilha e a printDouble ainda está lá.

Então voltando para dentro da função printDouble agora, depois que a gente fez a multiplicação, ele chama aquele console.log passando o resultado para a gente fazer o log dentro do nosso console. Então a função console.log vai para dentro da nossa Call Stack, executa, já sai da pilha e aí não tem mais nada para a gente fazer dentro da printDouble. Então o processamento do nosso código acabou e a printDouble também sai da nossa Call Stack.

Então com esse exemplo eu acho que ficou bem claro que a Call Stack não é nenhum [bicho de sete cabeças]. Muito pelo contrário, é bem simples, é bem fácil entender ela, só que ao mesmo tempo tem um peso muito grande no nosso código e por isso que é muito importante a gente saber da existência dela e como é que é o funcionamento. Beleza? Então vamos continuar.

## Single thread e I/O não bloqueante

Uma outra característica do Node é que ele é single thread, isso está diretamente relacionado com a nossa Call Stack. Por quê? Porque se ele é single thread, quer dizer que ele tem apenas uma Call Stack e se ele tem apenas uma Call Stack, quer dizer que ele consegue executar apenas uma coisa por vez.

E aí você vai me perguntar, como assim Mateus? Eu ouço por aí todo mundo falando que o Node ele é non-blocking I/O, ou seja, ele tem input e output de dados de forma não bloqueante, o que a gente conhece também como execução de código assíncrono, ou seja, a gente consegue por exemplo deixar uma requisição, uma query executando no banco de dados enquanto processa um outro tipo de conteúdo aqui e aí quando aquela query termina a gente passa uma função de callback e tudo mais para pegar os valores. Como é que você está me falando que o Node ele não consegue executar mais de uma coisa ao mesmo tempo?

De fato ele não consegue, tá? A gente só tem uma Call Stack e aquela pilha de processamento enquanto ela está ocupada a gente não consegue executar outra coisa. E aí você vai me perguntar então, beleza, mas por que que todo mundo fala que ele é non-blocking I/O e que ele consegue executar mais de uma coisa ao mesmo tempo? Porque de fato ele é non-blocking I/O e de fato ele também consegue executar mais de uma coisa ao mesmo tempo.

E ele consegue isso mesmo sendo single thread porque debaixo dos panos ali ele roda com uma biblioteca escrita em C chamada libuv. E essa libuv implementa dois carinhas que são os responsáveis, quem possibilita que a gente execute esses códigos assíncronos entre aspas em background. E esses carinhas se chamam thread pool e event loop que a gente já vai conversar um pouquinho. E a libuv não serve só para isso, ela também implementa toda a parte de file system do Node, de DNS e coisa assim. Então é uma biblioteca bem completa e dá muitos poderes para o Node, diga-se de passagem.

## Thread pool e event loop

Então vamos ver um exemplo agora para a gente entender como é que funciona essa thread pool e esse event loop. Bom, aqui eu tenho um exemplo bem simples, um código bem pequenininho e a nossa Call Stack que a gente já conhece. E aí executando esse código então na primeira linha a gente tem o console[.log]. Como a gente já viu, ele entra na Call Stack, executa e já sai dela. Parte para a linha de baixo.

Na linha de baixo a gente tem a função db.query e é aqui que a brincadeira começa. Essa função db.query é o que a gente chama de função bloqueante. Isso quer dizer que ela leva um certo tempo para ser executada, por isso que ela é entre aspas bloqueante. Por quê? Porque ela precisa se conectar no banco de dados, executar a query, esperar o banco responder, trazer as informações de volta e tudo mais. Tudo isso leva um determinado tempo.

E esse tempo, se o Node não tomasse nenhuma ação em cima disso, essa função db.query ficaria travada ali na minha Call Stack bloqueando a execução do meu código. Ou seja, a gente não conseguiria passar para a linha de baixo até a função db.query ser resolvida. Ou seja, até o banco de dados retornar os dados para a gente. E por isso que a gente chama isso de função bloqueante, porque ela bloqueia a nossa pilha de processamento, a nossa Call Stack.

Só que o Node não deixa isso acontecer. O que ele faz? Ele entende que essa função aqui vai bloquear a minha Call Stack, e aí ele fala, opa, eu não vou deixar isso acontecer. Então ele pega a execução dessa query e joga para dentro da libuv, dentro do nosso thread pool. E ali no thread pool ele vai executando essa query, e enquanto essa query está executando lá no thread pool, ele tira o db.query da minha Call Stack e o meu código continua executando normalmente. Então ele parte para a linha de baixo ali, que é o meu console log depois, e acabou o código, entre aspas, o código principal no caso.

Então ali na minha thread pool, ele está executando a minha query, está executando a minha query. Quando essa query terminar, o que ele faz? Ele joga para dentro de uma callback queue a função de callback que a gente passou ali como segundo argumento no código. Então ali a gente tem uma function callback que recebe erro e data e tudo mais.

Então essa função, se a gente traduzir do inglês para o português, callback significa, vai, numa tradução literal, seria ligue de volta. É como se a gente estivesse pedindo para o Node falar, depois que isso aqui terminar de executar, você me liga de volta e me passa esses dados. É mais ou menos isso, uma analogia bem besta, mas que eu acho que faz muito sentido e fica mais claro para você entender o que é um callback.

Beleza, então ele joga essa função de callback com os dados já retornados do banco de dados para dentro dessa callback queue, e aí aqui entre a nossa callback queue e a nossa call stack, a gente tem o que a gente chama de event loop, que é como se fosse um while true que fica toda hora indo na minha callback queue e vendo se tem alguma função pronta lá para ele executar.

Quando ele encontrar, ele vai ficar perguntando, tem, não, tem, não, tem, não. Quando ele perguntar, tem, e a callback queue responder, opa, tem uma função aqui, o que ele faz? Ele vai para dentro da minha call stack, verifica a call stack está liberada, ou seja, não tem nenhuma função pendente para ser executada ali dentro, não. Então o que ele faz? Ele puxa a função de callback da minha callback queue para a minha call stack, e aí continua o processamento do código normal.

Então dentro da minha callback, eu tenho aquele console log data, ele executa o console log data, tira da minha pilha, dentro da minha função de callback eu não tenho mais nada, então ele também tira a função de callback da minha pilha, e é assim que o Node consegue executar código assíncrono.

E por essa aula é isso, então deu para a gente ter uma visão macro bem legal de como é que o Node funciona por baixo dos panos, e agora eu te vejo na próxima aula.
