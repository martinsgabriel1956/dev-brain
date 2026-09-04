# Arquitetura Monolítica

E aí galera, beleza? Hoje vou falar sobre arquitetura monolítica.

Todas as aplicações têm a sua arquitetura, e normalmente elas são arquitetura de microsserviços ou arquitetura monolítica. Na arquitetura monolítica ela tem as suas vantagens e desvantagens. É uma arquitetura, eu diria, um pouco mais antiga, mas muito utilizada. E, como eu disse, tem vantagens e desvantagens — vou explicar um pouquinho como ela funciona.

## Como funciona

Imagine o seguinte: você tem a sua aplicação. Primeiro de tudo, você tem sua aplicação — pode ser qualquer aplicação que você desenvolveu, sendo ela web ou não. Só que essa aplicação tem que se conectar a um banco de dados. Então ela se conecta a um banco de dados, e as pessoas — seu cliente — acessam a sua aplicação.

O que acontece quando o seu cliente acessa a sua aplicação? Ela vai ter diversas funcionalidades, que a gente estava chamando de módulo. Nossa aplicação pode ter, por exemplo, um módulo de vendas, pode ter um módulo de estoque, e pode ter outro módulo do lado de relatórios (se ela precisar de relatórios), e mais um monte de outros módulos.

Porém, note que ela é só uma aplicação — está toda interligada através do mesmo servidor. Isso é uma aplicação monolítica.

## Vantagens

### Deploy mais simples

Ela tem as suas vantagens e desvantagens. Por exemplo, quando você vai fazer um deploy para uma nova versão, acaba sendo mais fácil, porque você só precisa vir aqui e atualizar a sua única aplicação — porque ela é só um módulo (um artefato único).

### Reuso de código

Outro grande benefício é que você consegue reutilizar o código, de forma muito diferente de uma arquitetura de microsserviços. Vamos supor: você cria uma classe dentro da sua aplicação que se chama "produtos". O módulo de estoque pode usar essa classe, o módulo de vendas pode usar essa classe, eventualmente o módulo de relatórios pode usar essa classe — e é só uma classe. Se você for atualizar alguma coisa nela, simplesmente altera ali e todos os módulos acabam tendo acesso a essa informação atualizada. Isso geralmente é um pouco mais difícil de ser feito em microsserviços. Então, na arquitetura monolítica, você diminui bastante a duplicidade de código.

### Comunicação mais rápida entre módulos

Outro detalhe é que, como todos os módulos são bem interligados, quando um chama o outro você não acaba tendo consumo de rede. Então a comunicação entre os módulos é muito mais rápida — um módulo já conversa com o outro, um chama a classe do outro, e isso acaba sendo um pouco mais fácil, diferente de outros tipos de arquitetura.

## Desvantagens

### Deploys menos frequentes conforme o time cresce

Em contrapartida, conforme o sistema vai crescendo e diversas pessoas vão entrando — você pode ter mais de 15 desenvolvedores, por exemplo — você pode até usar um kit (ferramenta de gestão) para te ajudar, criar sprints, essas coisas ajudam um pouquinho, mas ainda assim fica meio difícil, porque todos estão mexendo na mesma aplicação. A quantidade de deploys acaba diminuindo, porque você não consegue fazer deploy de um módulo específico isoladamente — normalmente você tem que esperar a sprint terminar.

Por isso é comum ver empresas com um dia fixo pra deploy — toda quinta-feira, toda sexta-feira, ou duas vezes por semana — mas não dá pra fazer deploy toda hora, porque normalmente as aplicações monolíticas rodam num único servidor (claro que existem exceções, a não ser que você esteja usando um esquema de auto scaling, que é outra forma de fazer deploy — não vou entrar nesse assunto agora).

Então, arquitetura monolítica geralmente é um único servidor. Quando você vai fazer o deploy, vai ter uma pequena indisponibilidade, porque está atualizando a aplicação e o servidor fica indisponível durante isso. Isso acaba diminuindo a quantidade de deploys que você consegue fazer na sua aplicação. Apesar disso, às vezes ainda vale a pena usar esse tipo de arquitetura.

### Single point of failure

Tem um ponto muito grande: se alguém vier aqui e fizer um deploy do módulo de estoque, colocar uma versão 2, e por algum motivo essa versão 2 estiver com defeito (com um bug), ela pode afetar toda a sua aplicação. Por quê? Porque a sua aplicação tem todos os módulos juntos — então ela pode travar tudo, só por causa do bug de um único módulo. Isso é um pouco mais perigoso, porque você pode afetar todas as funcionalidades. Imagina: por causa de uma versão nova do módulo de estoque, o seu sistema de vendas para de funcionar. Isso é conhecido como **single point of failure** — um único ponto de falha, o que não é muito legal em algumas aplicações.

### Auto scaling mais difícil

Outra coisa: geralmente nesse tipo de aplicação é mais difícil fazer auto scaling. Imagina que o servidor tem o processamento consumindo, por exemplo, em torno de 80%. O que acontece se ele chegar perto de 100%? Você vai precisar aumentar a CPU. Como você faz isso? Se você estiver na AWS ou em outros provedores, geralmente você precisa desligar, trocar o tipo da instância, adicionar memória/CPU, e ligar de novo. É um processo rápido, mas gera indisponibilidade. Isso não acontece (ou acontece menos) quando você trabalha com microsserviços.

### Deploys mais complexos com muita gente mexendo ao mesmo tempo

Como já falei, dá pra usar ferramentas de gestão (kit/sprint), mas como muita gente mexe na mesma aplicação ao mesmo tempo, um pode afetar o outro, e os deploys ficam um pouco mais complexos.

## Fechamento

Então, galera, é isso — uma aplicação em arquitetura monolítica. Vou falar sobre outros tipos de arquitetura em outros vídeos. Qualquer dúvida, não deixem de colocar nos comentários, e se você não é inscrito no canal, deixe de escrever — inscreva-se — para receber notificações, que estou colocando conteúdo novo quase todos os dias. Então é isso aí, até o próximo vídeo.
