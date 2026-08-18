# CQRS e Event Sourcing — Full Cycle (Wesley Williams)

> Transcrição de vídeo do canal Full Cycle, apresentado por Wesley Williams, sobre CQRS (Command Query Responsibility Segregation) e Event Sourcing.

## Introdução

Chega um momento na carreira em que, ou a gente é alocado para trabalhar em grandes projetos, ou a gente quer trabalhar em grandes projetos independente dessa decisão. Para trabalhar em grandes aplicações, eventualmente você precisa ter um arsenal diferente de estratégias para fazer sua aplicação ter mais performance e também conseguir escalar. Uma dessas estratégias é conhecida como CQRS, ou Command Query Responsibility Segregation. Além disso, para complementar essa estratégia, também vamos falar sobre um assunto bem chamativo no mundo das grandes aplicações: Event Sourcing.

Olá pessoal, tudo bem? Seja muito bem-vindo a mais um vídeo aqui no canal Full Cycle. Meu nome é Wesley Williams e no vídeo de hoje a gente vai falar sobre CQRS e Event Sourcing, e como isso pode mudar a forma de você programar, entregar suas aplicações e fazer com que seus sistemas possam escalar, ter muito mais performance e, eventualmente, se integrar mais facilmente com outros sistemas. O grande ponto é que CQRS mais Event Sourcing é uma bela dobradinha, e eu quero explorar esses pontos hoje com você.

## Como são normalmente as nossas aplicações

Normalmente a nossa aplicação fica no meio, e logo em seguida temos o nosso banco de dados. Acredito que a grande maioria das aplicações que a gente encontra no dia a dia é algo desse tipo. Quando trabalhamos dessa forma, temos diversas vantagens: todas as regras de negócio acontecem num único lugar, temos um único banco de dados, então conseguimos trabalhar com transações e garantir a consistência dos dados. Não tem nada de errado com isso.

Porém, invariavelmente, nossas aplicações podem começar a precisar de mais alguma coisa. Vamos imaginar que essa aplicação demanda muita escrita no banco de dados. O que acontece? O banco de dados começa a virar um gargalo por conta de tanta escrita que precisamos fazer. Muita gente já vai pensar em sharding, ou em criar um banco de dados só para escrita e espelhar os outros só para consultas — e a gente pode realmente fazer esse tipo de coisa. Mas é interessante notar que eu posso ter um banco de dados numa tecnologia, e opcionalmente um outro banco de dados numa outra tecnologia, responsável apenas pela leitura da aplicação.

## Exemplo com DDD: agregados

Vamos imaginar que estou trabalhando com Domain-Driven Design (DDD) e tenho um agregado de ordem de serviço. Esse agregado tem a ordem, o pedido, o cliente, quem indicou esse cliente, e as compras de quem indicou. Se isso é um agregado, toda vez que eu uso meu modelo de domínio — por exemplo, um repositório — e peço uma ordem, eu trago automaticamente tudo isso junto. Quando carrego tudo isso na memória, consigo aplicar minhas regras de negócio e garantir as invariantes do meu domínio, garantir que elas não são violadas.

Uma vez que estou trabalhando com agregados, fica muito mais fácil pegar os pedidos de um cliente, alterar um dado, mudar uma data, adicionar uma observação em quem indicou. Se você já estudou Domain Design, isso ajuda bastante.

Porém, toda vantagem tem uma desvantagem: apesar de garantir consistência nos dados ao manipular esses objetos dentro do domínio, existe uma força muito grande de busca por essas informações — eventualmente preciso fazer várias consultas para pegar esse agregado. E o mais interessante: se alguém quer fazer uma consulta nessas informações só para exibi-las, às vezes essa consulta nem faria sentido, porque eu quero mostrar apenas parte dos dados, mas o repositório sempre traz tudo.

## Separando o sistema em duas partes

Não seria interessante se parte do sistema mantivesse exatamente essa linha de agregados — eu posso ter um trilhão de agregados, garantindo a consistência dos dados, e toda vez que o usuário pede uma ação que gera mudança no sistema, eu mudo, adiciono ou altero esses agregados? Mas às vezes o usuário só quer pegar informação, um relatório, exibir dados — e para exibir dados, essas informações não precisam estar organizadas da mesma forma. Você não precisa trazer o agregado inteiro só para exibir um dado de um pedido.

Então imagine que o sistema é dividido em duas partes: uma parte segue os agregados, o modelo de domínio, roda as regras de negócio e realiza mudanças no sistema (insere, altera, deleta registros). Na hora de ler essas informações, esquecemos essa estrutura mais engessada e trazemos apenas as informações que o cliente final está querendo. Isso gera uma liberdade muito grande, porque não fico mais preso a esse fluxo — simplesmente penso "consulta de pedido com essas colunas" e trago a consulta.

E mais legal ainda: já pensou se o banco de dados de consulta fosse pensado apenas para exibir os dados — ou seja, ter views materializadas que trazem os dados de forma tão simples que um SELECT resolve a vida inteira, evitando joins e peso nas consultas? Esse banco pode ser orientado a documentos, um novo SQL, ou até orientado a grafo, se os dados que quero exibir usam recursos de grafo.

## Comandos e consultas

Quando você tem a possibilidade de fazer mudanças de um lado do sistema e consultas de outro lado, de forma independente, você ganha superpoder em diversos aspectos: organiza o sistema para receber comandos e organiza o sistema para receber consultas. O banco usado para comandos não precisa ser o mesmo banco usado para consultas, e você consegue escolher a melhor tecnologia para cada caso.

Toda vez que você quer mudar alguma coisa — adicionar um cliente, criar uma ordem — você dispara um **comando**. Um comando é quando você pede ao sistema para realizar uma mudança, mas não quer saber o resultado imediatamente. Você dispara o comando e não fica esperando para ver se deu certo. Do outro lado, quando você quer pegar resultados, relatórios, saber se aquele comando deu certo, você faz a **leitura** dos dados. Então: leitura de um lado, escrita do outro. A escrita vem através de uma intenção, que chamamos de comando; a leitura é específica para exibir o que você realmente precisa, independente da regra de domínio.

Um ponto importante: não existe bala de prata. Se ao inserir uma nova ordem de serviço no sistema eu enviar só um comando, preciso ter um mecanismo depois para verificar se a ordem deu certo ou não. É por isso que muitas vezes queremos aproveitar esse gancho e trabalhar com **Event Sourcing**.

## CQRS: origem e definição

Essa técnica de separar comandos e consultas foi criada por **Greg Young** — o nome dela é CQRS, Command Query Responsibility Segregation. É baseada numa outra pegada anterior chamada CQS (Command Query Separation). CQRS significa que eu segrego, separo a parte de comandos e a parte de consultas — o sistema tem duas responsabilidades diferentes: uma área de comandos, uma área de leitura.

## Event Sourcing

Normalmente quando você trabalha com CQRS, também trabalha com eventos. Alguns dizem que Event Sourcing tem que ser utilizado com CQRS; outros dizem o contrário, que CQRS tem que ser utilizado com Event Sourcing. Não necessariamente você precisa trabalhar com Event Sourcing enquanto trabalha com CQRS — mas essa é a opinião de muitos autores na área, e o motivo é o seguinte: toda vez que você executa um comando, ele produz alguma alteração, alguma mudança, e toda mudança gera um **evento**. Um evento é algo que já aconteceu: a porta aberta, a ordem inserida, o produto comprado.

Se eu tiver um banco de dados recebendo todos os eventos que aconteceram no sistema, isso significa que, se eu rodar o replay desses eventos, todos eles vão acontecer de novo e eu vou chegar exatamente no mesmo estado atual do sistema. O exemplo mais clássico é a conta bancária: o saldo é a diferença entre todos os créditos e todos os débitos. Se eu somar todos os créditos e subtrair todos os débitos de uma conta com 10 anos de histórico, chego ao saldo final. Ou seja, quando tenho todo o histórico do que aconteceu, consigo saber, em qualquer momento do tempo, como estava o estado da aplicação, porque tenho todos os eventos.

Então, toda vez que executamos um comando e algo acontece, podemos pegar os eventos produzidos e jogá-los num banco de dados que armazena todos os eventos que aconteceram. Existem até bancos de dados específicos para isso, como o Event Store, feitos para dar suporte a Event Sourcing.

### O exemplo do Datomic (Nubank)

Algumas aplicações e bancos de dados têm um comportamento bem interessante. Numa talk da galera do Nubank, foi apresentado um banco de dados pouco conhecido chamado **Datomic**. A sacada do Datomic é que você nunca exclui um registro — o banco é imutável. Se eu mudo o nome de "Wesley" para "Wesley Williams", ele cria um novo registro com a modificação daquela linha, e eu tenho um histórico de tudo que aconteceu sempre. Isso garante auditoria e garante que os dados não fiquem perdidos no meio da história. Se você pensa em como trabalhamos hoje com banco de dados normalmente: eu tenho um cliente chamado Wesley, mudei o nome dele, e não sei mais como era o nome antigo — só sei o nome atual. O Event Sourcing garante que eu consigo recuperar como era o nome antes da alteração.

### Remodelando a partir dos eventos

Outra possibilidade interessante: imagine que você modelou um banco de dados, tem todos os eventos, roda todas as regras, e depois não gosta da modelagem que fez. Você pode deletar esse banco, criar outro com modelagem diferente, e aplicar novamente todos os eventos — porque você tem tudo que aconteceu e não precisa se preocupar tanto.

### Command Sourcing (ideia de Greg Young)

Uma ideia que Greg Young apresentou numa palestra, e que o autor do vídeo nunca viu ninguém aplicando de fato, é o **Command Sourcing**. Os eventos são tudo que aconteceu no passado — mas não sabemos exatamente *como* aconteceu, só que aconteceu. Já imaginou ter todos os comandos armazenados, e não só os eventos? O mesmo comando pode gerar resultados diferentes de acordo com a época/contexto — por exemplo, numa época de juros muito altos você tem um resultado, numa época de juros muito baixos você roda o mesmo comando e vê um resultado diferente. Isso te dá a possibilidade de simular como seria o sistema numa outra situação, em outro momento do tempo — algo que muitas empresas gostariam de ter para simular decisões de negócio diferentes. Ou seja: um banco de dados para os eventos que aconteceram, e outro banco de dados para todos os comandos que fizeram esses eventos serem gerados.

## Quando vale a pena usar CQRS

Muita gente já começa um projeto usando CQRS porque sabe que o sistema vai escalar, que vai ter um sistema de mensageria, etc. Não existe uma única forma "certa" de começar. O grande conceito que você precisa entender é que seu sistema de leitura e de gravação é totalmente diferente — você pode ter um modelo de dados de um lado e outro modelo de dados do outro.

O principal erro que as pessoas cometem ao trabalhar com CQRS é tentar aproveitar os mesmos models (ou DTOs) da área de comandos na área de leitura — aí as coisas começam a dar errado. Pensando no "S" do SOLID (Single Responsibility): você sabe que algo está ferindo esse princípio quando duas coisas têm razões diferentes de mudança. Se a área de comando muda por um motivo e a área de leitura não muda pelo mesmo motivo, você está quebrando esse princípio ao juntá-las. É importante entender que comando e leitura são duas partes que, dentro do sistema, basicamente não se comunicam.

É preciso ter maturidade no desenvolvimento para trabalhar com eventos: ao emitir um comando, ele vai executar algo e provavelmente disparar um evento, que será armazenado, cairá numa fila, etc. Também é preciso ter maturidade para entender que todo comando, no final do dia, retorna `void` — por isso é mais rápido, porque você só dispara a solicitação e não fica esperando o resultado. Na leitura, você consegue pegar os dados, ou processar isso num sistema de filas/mensageria, ler, processar, e saber se algo deu errado.

## Conclusão

CQRS e Event Sourcing formam uma arquitetura que, sem dúvida, não vai resolver todos os problemas, mas que em alguns projetos grandes você vai precisar usar — ou pelo menos ter essa opção. A grande sacada de um desenvolvedor é conhecer as opções que tem disponíveis dentro de um contexto: uma vez que você conhece as opções, consegue tomar uma decisão melhor. O problema é quando você não conhece as opções e fica preso a uma única saída.
