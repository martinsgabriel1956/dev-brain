# A História e Evolução das APIs

Você já parou pra pensar como um botão "login com Google" funciona em qualquer site? Como um app de clima consegue te trazer uma previsão do tempo sem ter uma estação meteorológica aí na sua rua? Isso é tudo feito via APIs, que é o tema do vídeo de hoje. E se você acha que esse assunto é muito básico e que já sabe tudo sobre o tema, fica até o final do vídeo — deve ter um ou dois pontos aqui que vão te surpreender. Então já leu o cardápio aí e espera que o garçom traga os seus dados, e o vídeo já vai começar.

Olá dev, eu sou Bernardo Lobato e hoje a gente vai falar sobre esse tema tão importante no desenvolvimento moderno, mas que infelizmente muita gente não dá a devida atenção pros fundamentos que são as APIs. Vamos entender aqui o que é uma API, como surgiu esse conceito, e como se tornou algo tão importante assim pro nosso dia a dia do desenvolvimento no decorrer dos anos.

Primeiramente eu queria dizer que, conforme o roteiro desse vídeo foi evoluindo e conforme eu fui reunindo as informações para formar esse material, eu percebi que ficaria um vídeo demasiadamente grande. Para tratar com a qualidade que eu gosto de tratar os meus temas aqui nos vídeos, eu resolvi quebrar em partes. Essa primeira parte a gente vai falar um pouquinho sobre o histórico de APIs — como surgiu esse conceito, de onde surgiu, e também como a gente chegou nos nossos protocolos atuais, no nosso padrão de desenvolvimento atual. Nos próximos vídeos a gente vai detalhando mais especificamente cada um desses protocolos e desses padrões.

## Definição formal

API significa Application Program Interface, e é um conjunto de regras e contratos que permitem que módulos conversem entre si — que a gente consiga estabelecer uma conexão entre dois ou mais módulos. Destaque aqui pra palavra "módulo", que não quer dizer necessariamente que seja uma outra aplicação ou uma aplicação disponibilizada via rede. Claro que na programação moderna, no nosso desenvolvimento atual do dia a dia, podemos até entender API como "aquilo que faz dois sistemas conversarem entre si", mas a gente chega lá.

Vamos fazer aqui uma breve viagem histórica e entender de onde vieram esses conceitos que utilizamos hoje, e como eles foram evoluindo até se tornarem esse pilar fundamental no dia a dia de todo desenvolvedor.

## Anos 60 e 70 — mainframes e as primeiras APIs locais

Nos anos 60 e 70, quando a computação ainda era dominada pelos mainframes, a ideia de API já existia, mas num formato bem diferente do que conhecemos hoje. Naquela época, API não significava comunicação em rede, e sim uma coleção de rotinas, bibliotecas e comandos que os programadores podiam reutilizar para interagir com o sistema. Por exemplo, ao invés de escrever todo o código para acessar um disco, o desenvolvedor chamava uma função exposta pelo sistema operacional. Essas funções eram as chamadas interfaces de programação.

As primeiras APIs padronizavam a forma como os programas conversavam com o hardware e com o próprio sistema operacional. Grandes fabricantes, como a IBM com o seu IBM System/360, forneciam essas interfaces para que diferentes linguagens e aplicações conseguissem rodar no mesmo mainframe, na mesma máquina. Isso foi revolucionário porque abriu espaço para reutilização de código e para que softwares se tornassem menos dependentes de um hardware específico.

Ou seja: nos anos 60 e 70 as APIs eram locais e voltadas para o próprio computador — ainda não existia internet, mas a essência já tava lá: fornecer uma camada de abstração que facilitasse a vida do desenvolvedor, e assim a gente conseguisse criar interoperabilidade, no caso, com o próprio sistema operacional.

## Anos 70 — minicomputadores, Unix e as chamadas de sistema

Nos anos 70, ainda na era de ouro dos mainframes, começava a surgir um novo conceito: o dos minicomputadores. Além disso, foi nos anos 70 que sistemas operacionais como o Unix começaram a ganhar força. O Unix trouxe a filosofia de pequenas funções reutilizáveis que podiam ser combinadas, e a ideia de "chamadas de sistema" se consolidou como uma forma padronizada de API entre programas e o kernel.

Esse modelo influenciou fortemente tudo que veio depois — inclusive muitas das ideias presentes nesse modelo do Unix foram reaproveitadas posteriormente em modelos como o REST com JSON, por exemplo.

Ou seja, nos anos 70 as APIs estavam deixando de ser apenas uma coleção de rotinas para se tornar contratos muito bem definidos entre software e sistema operacional — cada um desses contratos com uma interface muito bem definida e com o menor tamanho possível.

## Anos 80 — PCs pessoais, WinAPI e POSIX

Foi nos anos 80 que a computação saiu um pouquinho dos mainframes e minicomputadores e entrou na era dos PCs pessoais. Foi nessa década que as APIs começaram a se popularizar para fora dos ambientes corporativos gigantes e entrar no dia a dia de usuários mais comuns, e claro, para quem desenvolvia para microcomputadores.

O grande destaque aqui é a WinAPI, ou Windows API, lançada junto com as primeiras versões do Microsoft Windows. Ela permitia que desenvolvedores criassem janelas, botões, menus, e interagissem de forma padronizada com o sistema operacional. Esse foi um marco porque deu um conjunto de funções comuns para todos que desenvolviam para Windows, o que acabou sendo algo essencial para a explosão desse sistema operacional a partir daí.

Do outro lado, no mundo Unix, consolidava-se o POSIX, um padrão criado no fim dos anos 80 para unificar as chamadas de sistema entre diferentes versões do Unix. O POSIX foi crucial para trazer portabilidade: um programa escrito em C para Unix, por exemplo, poderia facilmente ser levado para outro sem precisar reescrever tudo.

Aqui temos o início da era moderna em que o desenvolvimento de aplicações poderia ser baseado nas APIs do sistema operacional. O programador já não precisava mais descer tanto de nível no seu código para poder criar aplicações complexas com janelas, menus, botões etc., e não precisava reinventar a roda a cada novo programa que fosse implementado.

Pra gente ter uma ideia: jogos como Prince of Persia precisavam interagir com vídeo, som e teclado antes do Windows — cada jogo tinha que implementar essas rotinas manualmente. Mas conforme a WinAPI evoluiu, ela começou a oferecer uma base comum para lidar com gráficos e entradas de usuário.

## Anos 90 — APIs remotas e o início da web

Já nos anos 90 a gente viu surgir as APIs remotas e a web, que estava nascendo ali, bem no seu começo. Padrões como CORBA e RMI começaram a surgir — eram complexos, mas abriam caminho para essa integração em rede que a gente vê nos dias de hoje.

## Anos 2000 — SOAP, REST e a economia das APIs

Nos anos 2000 a internet já tava consolidada, e o grande desafio passou a ser fazer sistemas diferentes conversarem pela web. É nessa década que surgem as APIs web como a gente conhece.

O destaque inicial foi o SOAP, ou Simple Object Access Protocol, que usava XML para estruturar mensagens enviadas por HTTP, e era muito usado em sistemas corporativos. Trouxe uma padronização importante: contratos formais descritos em um arquivo chamado WSDL, e forte integração com ferramentas empresariais. A contrapartida era burocracia, configurações complexas, mensagens enormes e muito acoplamento. Mas não se engane: o padrão SOAP ainda é muito utilizado até hoje, e em muitas aplicações funciona muito bem.

Foi também nos anos 2000 que a arquitetura REST foi apresentada pela primeira vez, em uma tese de doutorado. No começo, REST parecia apenas mais uma ideia acadêmica, mas com a popularização do JSON como formato de dados — que era bem mais leve e bem mais amigável que o XML — o REST passou a ganhar tração.

Ao longo da década, gigantes da web começaram a expor suas APIs publicamente. eBay, Amazon e Salesforce foram pioneiras, seguidas por Google, Facebook e Twitter. Isso inaugurou a chamada "economia das APIs" — as empresas passaram a disponibilizar dados e serviços para que outros desenvolvedores pudessem construir em cima desses dados.

Os anos 2000, portanto, marcaram uma transição entre as APIs locais e corporativas para APIs abertas e baseadas na web. Foi quando a API deixou de ser apenas uma ferramenta interna de desenvolvimento e passou a ser uma estratégia de negócios.

## Anos 2010 — REST+JSON como padrão de mercado, GraphQL e gRPC

Nos anos 2010 as APIs REST com JSON se consolidaram como padrão de mercado — eram simples, rápidas e funcionavam bem pra web e pros apps móveis que estavam explodindo ali na época. O boom dos smartphones fez as APIs se tornarem indispensáveis: praticamente todo aplicativo precisava de um backend, e este era exposto via API.

Foi quando vimos o surgimento do GraphQL, por exemplo, trazendo a ideia de permitir que o cliente pedisse exatamente os dados que precisava, sem sobrecarga de informações. Essa abordagem ganhou tração em aplicativos com interfaces complexas, como redes sociais — inclusive o próprio Facebook foi o criador desse formato.

Ao mesmo tempo, o gRPC, já lançado pelo Google também em 2015, trouxe alta performance para comunicações entre microsserviços, usando Protobuf no lugar do JSON. Isso refletia a transição para arquiteturas de microsserviços, que acabavam dependendo de APIs para tudo.

Outro marco dos anos 2010 foi o crescimento da chamada "API economy", em que empresas como Stripe, Twilio e SendGrid se tornaram bilionárias — e o produto oferecido por essas empresas eram APIs. Nesse período, AWS, Google Cloud e Azure também expandiram exponencialmente, oferecendo centenas de APIs para serviços em nuvem.

## Anos 2020 — infraestrutura crítica

Agora nos anos 20, percebemos APIs em absolutamente tudo: de aplicações de celular até IoT, carros conectados e inteligência artificial. APIs de IA generativa, como da OpenAI, mudaram a forma como os desenvolvedores integram modelos de linguagem e visão em seus sistemas.

Outro movimento forte é o de APIs event-driven e APIs de tempo real, com protocolos como WebSocket e webhook sendo utilizados em fintechs e em sistemas de streams e notificações instantâneas. A preocupação também com segurança, versionamento e governança foi ganhando destaque no decorrer dos últimos anos — padrões como OAuth, OpenID Connect e API Gateway surgiram para proteger e organizar o uso massivo dessas APIs.

Em resumo, nos anos 2020 as APIs deixaram de ser meramente um meio técnico para ajudar desenvolvedores, e viraram infraestrutura crítica no mundo digital. Sem elas, a internet moderna — que vai desde pagamentos via Pix até integração com chatbots ou inteligência artificial — simplesmente não funciona, simplesmente deixa de existir.

## Encerramento

Mas você lembra qual foi a primeira API que você consumiu quando tava começando no desenvolvimento, ou qual foi a primeira API que você desenvolveu e disponibilizou? Conta aqui nos comentários pra gente enriquecer essa discussão. Vou deixar dois vídeos no final desse aqui, em que um eu falo sobre API Gateway, que pode funcionar como um complemento para isso aqui caso você ainda não tenha assistido, e o outro eu falo sobre microsserviços, que muito dos conceitos que eu já comentei nesse vídeo — principalmente sobre isso — eu exploro ali com um detalhamento um pouquinho maior.
