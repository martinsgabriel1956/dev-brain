# Microsserviços

*uma definição deste novo termo arquitetural*

**Autores:** James Lewis e Martin Fowler
**Data de publicação:** 25 de março de 2014
**Fonte original:** https://martinfowler.com/articles/microservices.html
**Tags:** application architecture, microservices

> O termo "Arquitetura de Microsserviços" surgiu nos últimos anos para descrever uma forma particular de projetar aplicações de software como conjuntos de serviços implantáveis de forma independente. Embora não haja uma definição precisa desse estilo arquitetural, há certas características comuns em torno de organização por capacidade de negócio, implantação automatizada, inteligência nos endpoints e controle descentralizado de linguagens e dados.

---

"Microsserviços" — mais um novo termo nas ruas lotadas da arquitetura de software. Embora nossa inclinação natural seja passar por essas coisas com um olhar de desdém, esse pedaço de terminologia descreve um estilo de sistemas de software que consideramos cada vez mais atraente. Vimos muitos projetos usarem esse estilo nos últimos anos, e os resultados até agora têm sido positivos, a tal ponto que, para muitos dos nossos colegas, esse está se tornando o estilo padrão para construir aplicações corporativas. Infelizmente, no entanto, não há muita informação que descreva o que é o estilo de microsserviços e como fazê-lo.

Em resumo, o estilo arquitetural de microsserviços<sup>[1]</sup> é uma abordagem para desenvolver uma única aplicação como um conjunto de pequenos serviços, cada um rodando em seu próprio processo e se comunicando com mecanismos leves, geralmente uma API de recursos HTTP. Esses serviços são construídos em torno de capacidades de negócio e implantáveis de forma independente por uma esteira de implantação totalmente automatizada. Há um mínimo absoluto de gerenciamento centralizado desses serviços, que podem ser escritos em diferentes linguagens de programação e usar diferentes tecnologias de armazenamento de dados.

> **Nota de rodapé 1:** O termo "microsserviço" foi discutido em um workshop de arquitetos de software perto de Veneza em maio de 2011, para descrever o que os participantes viam como um estilo arquitetural comum que muitos deles vinham explorando recentemente. Em maio de 2012, o mesmo grupo decidiu por "microsserviços" como o nome mais apropriado. James apresentou algumas dessas ideias como um estudo de caso em março de 2012 na 33rd Degree em Cracóvia, em "Microservices - Java, the Unix Way", assim como Fred George por volta da mesma época. Adrian Cockcroft, na Netflix, descrevendo essa abordagem como "SOA de granularidade fina", foi pioneiro do estilo em escala web, assim como muitos outros mencionados neste artigo — Joe Walnes, Daniel Terhorst-North, Evan Botcher e Graham Tackley.

Para começar a explicar o estilo de microsserviços, é útil compará-lo ao estilo monolítico: uma aplicação monolítica construída como uma única unidade. Aplicações corporativas costumam ser construídas em três partes principais: uma interface de usuário do lado cliente (composta por páginas HTML e JavaScript rodando em um navegador na máquina do usuário), um banco de dados (composto por muitas tabelas inseridas em um sistema de gerenciamento de banco de dados comum, geralmente relacional) e uma aplicação do lado servidor. A aplicação do lado servidor tratará requisições HTTP, executará a lógica de domínio, buscará e atualizará dados do banco de dados e selecionará e populará views HTML a serem enviadas ao navegador. Essa aplicação do lado servidor é um *monolito* — um único executável lógico<sup>[2]</sup>. Qualquer mudança no sistema envolve construir e implantar uma nova versão da aplicação do lado servidor.

> **Nota de rodapé 2:** O termo monolito é usado pela comunidade Unix há algum tempo. Aparece em *The Art of Unix Programming* para descrever sistemas que ficam grandes demais.

Um servidor monolítico como esse é uma forma natural de abordar a construção de um sistema assim. Toda a lógica para tratar uma requisição roda em um único processo, permitindo usar os recursos básicos da linguagem para dividir a aplicação em classes, funções e namespaces. Com algum cuidado, é possível rodar e testar a aplicação no laptop de um desenvolvedor, e usar uma esteira de implantação para garantir que as mudanças sejam testadas e implantadas corretamente em produção. É possível escalar horizontalmente o monolito rodando várias instâncias atrás de um load balancer.

Aplicações monolíticas podem ter sucesso, mas cada vez mais as pessoas sentem frustrações com elas — especialmente à medida que mais aplicações são implantadas na nuvem. Os ciclos de mudança ficam amarrados entre si — uma mudança feita em uma pequena parte da aplicação exige que o monolito inteiro seja reconstruído e implantado. Com o tempo, costuma ser difícil manter uma boa estrutura modular, tornando mais difícil manter mudanças que deveriam afetar apenas um módulo restritas a esse módulo. Escalar exige escalar a aplicação inteira, em vez de apenas as partes que precisam de mais recursos.

**Figura 1: Monolitos e Microsserviços**

Essas frustrações levaram ao estilo arquitetural de microsserviços: construir aplicações como conjuntos de serviços. Além do fato de que os serviços são implantáveis e escaláveis de forma independente, cada serviço também fornece uma fronteira de módulo firme, permitindo inclusive que diferentes serviços sejam escritos em diferentes linguagens de programação. Eles também podem ser gerenciados por times diferentes.

Não afirmamos que o estilo de microsserviços seja novo ou inovador — suas raízes remontam pelo menos aos princípios de design do Unix. Mas achamos que poucas pessoas consideram uma arquitetura de microsserviços, e que muitos desenvolvimentos de software estariam melhor se a usassem.

## Características de uma Arquitetura de Microsserviços

Não podemos dizer que existe uma definição formal do estilo arquitetural de microsserviços, mas podemos tentar descrever o que vemos como características comuns às arquiteturas que se encaixam nesse rótulo. Como em qualquer definição que delineia características comuns, nem toda arquitetura de microsserviços tem todas as características, mas esperamos que a maioria das arquiteturas de microsserviços exiba a maioria das características. Embora nós, autores, tenhamos sido membros ativos dessa comunidade bastante informal, nossa intenção é tentar descrever o que vemos em nosso próprio trabalho e em esforços semelhantes de times que conhecemos. Em particular, não estamos estabelecendo uma definição à qual se deva aderir.

### Componentização via Serviços

Há muito tempo, na indústria de software, existe o desejo de construir sistemas encaixando componentes, de forma parecida com o que vemos no mundo físico. Nas últimas décadas, vimos um progresso considerável com grandes compêndios de bibliotecas comuns que fazem parte da maioria das plataformas de linguagem.

Ao falar de componentes, esbarramos na difícil definição do que faz um componente. Nossa definição é que um **componente** é uma unidade de software que é substituível e atualizável de forma independente.

Arquiteturas de microsserviços usarão bibliotecas, mas sua forma principal de componentizar o próprio software é dividindo-o em serviços. Definimos **bibliotecas** como componentes que são vinculados a um programa e chamados usando chamadas de função em memória, enquanto **serviços** são componentes fora de processo que se comunicam por um mecanismo como uma requisição de web service, ou chamada de procedimento remoto. (Esse é um conceito diferente do de objeto de serviço em muitos programas OO<sup>[3]</sup>.)

> **Nota de rodapé 3:** Muitos projetistas orientados a objetos, nós inclusive, usam o termo "objeto de serviço" no sentido de Domain-Driven Design, para um objeto que realiza um processo significativo que não está vinculado a uma entidade. Esse é um conceito diferente de como estamos usando "serviço" neste artigo. Infelizmente o termo serviço tem os dois significados e temos que conviver com o polissemismo.

Uma razão principal para usar serviços como componentes (em vez de bibliotecas) é que serviços são implantáveis de forma independente. Se você tem uma aplicação<sup>[4]</sup> composta por múltiplas bibliotecas em um único processo, uma mudança em qualquer componente único resulta em ter que reimplantar a aplicação inteira. Mas se essa aplicação for decomposta em múltiplos serviços, é de se esperar que muitas mudanças de serviço único exijam apenas que aquele serviço seja reimplantado. Isso não é absoluto — algumas mudanças alterarão interfaces de serviço, exigindo alguma coordenação —, mas o objetivo de uma boa arquitetura de microsserviços é minimizar isso através de fronteiras de serviço coesas e mecanismos de evolução nos contratos de serviço.

> **Nota de rodapé 4:** Consideramos que uma aplicação é uma construção social que une uma base de código, um grupo de funcionalidades e um corpo de financiamento.

Outra consequência de usar serviços como componentes é uma interface de componente mais explícita. A maioria das linguagens não tem um bom mecanismo para definir uma Interface Publicada explícita. Muitas vezes, apenas documentação e disciplina impedem que clientes quebrem o encapsulamento de um componente, levando a um acoplamento excessivamente rígido entre componentes. Serviços facilitam evitar isso usando mecanismos explícitos de chamada remota.

Usar serviços dessa forma tem desvantagens. Chamadas remotas são mais caras que chamadas em processo, e assim as APIs remotas precisam ter granularidade mais grosseira, o que costuma ser mais incômodo de usar. Se você precisa mudar a alocação de responsabilidades entre componentes, esses movimentos de comportamento são mais difíceis de fazer quando você está cruzando fronteiras de processo.

Em uma primeira aproximação, podemos observar que serviços mapeiam para processos em tempo de execução, mas isso é apenas uma primeira aproximação. Um serviço pode consistir em múltiplos processos que sempre serão desenvolvidos e implantados juntos, como um processo de aplicação e um banco de dados usado apenas por aquele serviço.

### Organizados em Torno de Capacidades de Negócio

Ao buscar dividir uma grande aplicação em partes, muitas vezes a gestão foca na camada tecnológica, levando a times de UI, times de lógica do lado servidor e times de banco de dados. Quando os times são separados dessa forma, até mudanças simples podem levar a um projeto entre times que consome tempo e aprovação orçamentária. Um time inteligente vai otimizar em torno disso e escolher o menor dos dois males — simplesmente forçar a lógica para dentro de qualquer aplicação a que tenha acesso. Lógica em todo lugar, em outras palavras. Esse é um exemplo da Lei de Conway em ação.

> "Qualquer organização que projeta um sistema (definido de forma ampla) produzirá um design cuja estrutura é uma cópia da estrutura de comunicação da organização."
> — Melvin Conway, 1968

**Figura 2: A Lei de Conway em ação**

A abordagem de divisão dos microsserviços é diferente: dividir em serviços organizados em torno de **capacidade de negócio**. Esses serviços implementam uma pilha ampla de software para aquela área de negócio, incluindo interface de usuário, armazenamento persistente e quaisquer colaborações externas. Consequentemente, os times são multifuncionais, incluindo toda a gama de habilidades necessárias para o desenvolvimento: experiência do usuário, banco de dados e gestão de projeto.

**Figura 3: Fronteiras de serviço reforçadas por fronteiras de time**

> **Sidebar — Qual o tamanho de um microsserviço?**
> Embora "microsserviço" tenha se tornado um nome popular para esse estilo arquitetural, o nome leva a um foco infeliz no tamanho do serviço, e a discussões sobre o que constitui "micro". Em nossas conversas com praticantes de microsserviços, vemos uma variedade de tamanhos de serviços. Os maiores tamanhos relatados seguem a noção de "Two Pizza Team" da Amazon (ou seja, o time inteiro pode ser alimentado com duas pizzas), o que significa não mais que uma dúzia de pessoas. Na escala menor, vimos configurações em que um time de meia dúzia de pessoas dava suporte a meia dúzia de serviços.
> Isso leva à questão de saber se há diferenças suficientemente grandes dentro dessa faixa de tamanho para que os tamanhos de serviço-por-dúzia-de-pessoas e serviço-por-pessoa não devessem ser agrupados sob um único rótulo de microsserviços. No momento, achamos melhor agrupá-los, mas é certamente possível que mudemos de ideia à medida que exploramos mais esse estilo.

Uma empresa organizada dessa forma é a www.comparethemarket.com. Times multifuncionais são responsáveis por construir e operar cada produto, e cada produto é dividido em vários serviços individuais que se comunicam via um barramento de mensagens.

Grandes aplicações monolíticas sempre podem ser modularizadas em torno de capacidades de negócio também, embora esse não seja o caso comum. Certamente incentivaríamos um time grande construindo uma aplicação monolítica a se dividir por linhas de negócio. O principal problema que vimos aqui é que elas tendem a ser organizadas em torno de *contextos demais*. Se o monolito abrange muitas dessas fronteiras modulares, pode ser difícil para membros individuais de um time encaixá-las em sua memória de curto prazo. Além disso, vemos que as linhas modulares exigem muita disciplina para serem cumpridas. A separação necessariamente mais explícita exigida pelos componentes de serviço torna mais fácil manter claras as fronteiras dos times.

### Produtos, não Projetos

A maioria dos esforços de desenvolvimento de aplicações que vemos usa um modelo de projeto: em que o objetivo é entregar um pedaço de software que então é considerado concluído. Na conclusão, o software é entregue a uma organização de manutenção, e o time do projeto que o construiu é desfeito.

Defensores de microsserviços tendem a evitar esse modelo, preferindo a noção de que um time deveria possuir um produto ao longo de todo o seu ciclo de vida. Uma inspiração comum para isso é a noção da Amazon de "você constrói, você opera" ("you build, you run it"), em que um time de desenvolvimento assume total responsabilidade pelo software em produção. Isso traz os desenvolvedores para contato diário com o comportamento do software em produção, e aumenta o contato com seus usuários, já que eles têm que assumir ao menos parte da carga de suporte.

A mentalidade de produto se conecta com a ligação a capacidades de negócio. Em vez de ver o software como um conjunto de funcionalidades a serem concluídas, existe um relacionamento contínuo em que a questão é como o software pode ajudar seus usuários a aprimorar a capacidade de negócio.

Não há razão para que essa mesma abordagem não possa ser adotada com aplicações monolíticas, mas a granularidade menor dos serviços pode facilitar a criação de relacionamentos pessoais entre desenvolvedores de serviço e seus usuários.

### Endpoints Inteligentes e Tubos Burros ("Smart Endpoints and Dumb Pipes")

Ao construir estruturas de comunicação entre diferentes processos, vimos muitos produtos e abordagens que enfatizam colocar bastante inteligência no próprio mecanismo de comunicação. Um bom exemplo disso é o Enterprise Service Bus (ESB), em que produtos de ESB costumam incluir facilidades sofisticadas para roteamento de mensagens, coreografia, transformação e aplicação de regras de negócio.

> **Sidebar — Microsserviços e SOA**
> Quando falamos sobre microsserviços, uma pergunta comum é se isso é apenas Service Oriented Architecture (SOA), que vimos há uma década. Há mérito nesse ponto, porque o estilo de microsserviços é muito parecido com o que alguns defensores de SOA vinham defendendo. O problema, no entanto, é que SOA significa coisas demais e diferentes entre si, e na maioria das vezes em que encontramos algo chamado "SOA", é significativamente diferente do estilo que descrevemos aqui, geralmente devido a um foco em ESBs usados para integrar aplicações monolíticas.
> Em particular, vimos tantas implementações malfeitas de orientação a serviços — desde a tendência de esconder complexidade em ESBs, até iniciativas fracassadas de vários anos que custaram milhões e não entregaram valor, até modelos de governança centralizada que ativamente inibem a mudança — que às vezes é difícil enxergar além desses problemas.
> Certamente, muitas das técnicas em uso na comunidade de microsserviços cresceram a partir das experiências de desenvolvedores integrando serviços em grandes organizações. O padrão Tolerant Reader é um exemplo disso. Esforços para usar a web contribuíram; usar protocolos simples é outra abordagem derivada dessas experiências — uma reação contra padrões centrais que atingiram uma complexidade, francamente, de tirar o fôlego.
> Essa manifestação comum de SOA levou alguns defensores de microsserviços a rejeitar completamente o rótulo SOA, embora outros considerem microsserviços uma forma de SOA, talvez "orientação a serviços feita corretamente". De qualquer forma, o fato de SOA significar coisas tão diferentes torna valioso ter um termo que defina de forma mais precisa esse estilo arquitetural.

A comunidade de microsserviços favorece uma abordagem alternativa: *endpoints inteligentes e tubos burros*. Aplicações construídas a partir de microsserviços têm como objetivo ser o mais desacopladas e coesas possível — elas possuem sua própria lógica de domínio e atuam mais como filtros no sentido clássico do Unix, recebendo uma requisição, aplicando lógica conforme apropriado e produzindo uma resposta. Isso é coreografado usando protocolos simples do tipo REST, em vez de protocolos complexos como WS-Choreography ou BPEL, ou orquestração por uma ferramenta central.

Os dois protocolos mais comumente usados são requisição-resposta HTTP com APIs de recursos e mensageria leve<sup>[7]</sup>.

> **Nota de rodapé 7:** Em extremos de escala, organizações costumam migrar para protocolos binários — protobufs, por exemplo. Sistemas que usam isso ainda exibem a característica de endpoints inteligentes, tubos burros — e trocam *transparência* por escala. A maioria das propriedades web, e certamente a vasta maioria das empresas, não precisa fazer essa troca — transparência pode ser uma grande vantagem.

> "Seja da web, não atrás da web."
> — Ian Robinson

Times de microsserviços usam os princípios e protocolos sobre os quais a world wide web (e, em grande medida, o Unix) foi construída. Recursos usados com frequência podem ser cacheados com muito pouco esforço por parte de desenvolvedores ou pessoal de operações.

A segunda abordagem em uso comum é mensageria sobre um barramento de mensagens leve. A infraestrutura escolhida costuma ser burra (burra no sentido de que atua apenas como roteador de mensagens) — implementações simples como RabbitMQ ou ZeroMQ não fazem muito mais que fornecer um tecido assíncrono confiável — a inteligência ainda vive nos endpoints que produzem e consomem mensagens, isto é, nos serviços.

Em um monolito, os componentes executam em processo e a comunicação entre eles é via invocação de método ou chamada de função. O maior problema ao transformar um monolito em microsserviços está em mudar o padrão de comunicação. Uma conversão ingênua de chamadas de método em memória para RPC leva a comunicações "tagarelas" (chatty) que não performam bem. Em vez disso, é preciso substituir a comunicação de granularidade fina por uma abordagem de granularidade mais grosseira.

### Governança Descentralizada

Uma das consequências da governança centralizada é a tendência de padronizar em uma única plataforma tecnológica. A experiência mostra que essa abordagem é restritiva — nem todo problema é um prego, e nem toda solução é um martelo. Preferimos usar a ferramenta certa para o trabalho, e embora aplicações monolíticas possam tirar proveito de diferentes linguagens até certo ponto, isso não é muito comum.

Ao dividir os componentes do monolito em serviços, temos uma escolha ao construir cada um deles. Quer usar Node.js para montar uma página de relatórios simples? Vá em frente. C++ para um componente particularmente complicado, quase em tempo real? Tudo bem. Quer trocar por um tipo diferente de banco de dados que atenda melhor ao comportamento de leitura de um componente? Temos a tecnologia para isso.

Claro, só porque você *pode* fazer algo não significa que *deveria* — mas particionar seu sistema dessa forma significa que você tem a opção.

Times construindo microsserviços também preferem uma abordagem diferente para padrões. Em vez de usar um conjunto de padrões definidos e escritos em algum lugar no papel, eles preferem a ideia de produzir ferramentas úteis que outros desenvolvedores possam usar para resolver problemas parecidos com os que estão enfrentando. Essas ferramentas costumam ser colhidas de implementações e compartilhadas com um grupo maior, às vezes, mas não exclusivamente, usando um modelo interno de código aberto. Agora que git e GitHub se tornaram o sistema de controle de versão de fato, práticas de código aberto estão se tornando cada vez mais comuns internamente.

A Netflix é um bom exemplo de organização que segue essa filosofia. Compartilhar código útil e, acima de tudo, testado em batalha, como bibliotecas, encoraja outros desenvolvedores a resolver problemas semelhantes de formas semelhantes, mas deixa a porta aberta para escolher uma abordagem diferente se necessário. Bibliotecas compartilhadas tendem a se concentrar em problemas comuns de armazenamento de dados, comunicação entre processos e, como discutimos mais adiante, automação de infraestrutura.

Para a comunidade de microsserviços, overheads (sobrecargas) são particularmente indesejados. Isso não quer dizer que a comunidade não valorize contratos de serviço — muito pelo contrário, já que tende a haver muito mais deles. É só que eles estão olhando para formas diferentes de gerenciar esses contratos. Padrões como Tolerant Reader e Consumer-Driven Contracts são frequentemente aplicados a microsserviços. Eles ajudam os contratos de serviço a evoluir de forma independente. Executar contratos orientados pelo consumidor como parte do seu build aumenta a confiança e fornece feedback rápido sobre se seus serviços estão funcionando. Conhecemos, de fato, um time na Austrália que orienta o build de novos serviços por contratos orientados pelo consumidor. Eles usam ferramentas simples que permitem definir o contrato de um serviço. Isso se torna parte do build automatizado antes mesmo do código do novo serviço ser escrito. O serviço então é construído apenas até o ponto em que satisfaz o contrato — uma abordagem elegante para evitar o dilema do YAGNI<sup>[9]</sup> ao construir novo software. Essas técnicas, e o ferramental que cresce em torno delas, limitam a necessidade de gerenciamento central de contratos ao diminuir o acoplamento temporal entre serviços.

> **Nota de rodapé 9:** "YAGNI" ou "You Aren't Going To Need It" é um princípio de XP e uma exortação a não adicionar funcionalidades até que se saiba que serão necessárias.

Talvez o ápice da governança descentralizada seja o ethos "construa / opere" popularizado pela Amazon. Times são responsáveis por todos os aspectos do software que constroem, incluindo operá-lo 24/7. Delegar esse nível de responsabilidade definitivamente não é a norma, mas vemos cada vez mais empresas empurrando responsabilidade para os times de desenvolvimento. A Netflix é outra organização que adotou esse ethos. Ser acordado às 3 da manhã todas as noites pelo seu pager certamente é um incentivo poderoso para focar em qualidade ao escrever código. Essas ideias estão o mais longe possível do modelo tradicional de governança centralizada.

### Gerenciamento de Dados Descentralizado

A descentralização do gerenciamento de dados se manifesta de várias formas. No nível mais abstrato, significa que o modelo conceitual do mundo vai diferir entre sistemas. Essa é uma questão comum ao integrar em uma grande empresa: a visão de vendas de um cliente vai diferir da visão de suporte. Algumas coisas chamadas de "clientes" na visão de vendas podem nem aparecer na visão de suporte. As que aparecem podem ter atributos diferentes e (pior) atributos comuns com semânticas sutilmente diferentes.

> **Sidebar — Padrões testados em batalha e padrões impostos**
> É meio contraditório que times de microsserviços tendam a evitar o tipo de padrão rígido e imposto estabelecido por grupos de arquitetura corporativa, mas usem de bom grado, e até evangelizem, o uso de padrões abertos como HTTP, ATOM e outros microformatos.
> A diferença chave é como os padrões são desenvolvidos e como são impostos. Padrões geridos por grupos como o IETF só *se tornam* padrões quando há várias implementações vivas deles no mundo mais amplo, e que frequentemente crescem a partir de projetos de código aberto bem-sucedidos.
> Esses padrões são um mundo diferente de muitos no mundo corporativo, que são frequentemente desenvolvidos por grupos com pouca experiência recente de programação, ou excessivamente influenciados por fornecedores.

Essa questão é comum entre aplicações, mas também pode ocorrer *dentro* de aplicações, particularmente quando essa aplicação é dividida em componentes separados. Uma forma útil de pensar sobre isso é a noção de Bounded Context do Domain-Driven Design. DDD divide um domínio complexo em múltiplos bounded contexts e mapeia as relações entre eles. Esse processo é útil tanto para arquiteturas monolíticas quanto de microsserviços, mas há uma correlação natural entre fronteiras de serviço e de contexto que ajuda a esclarecer e, como descrevemos na seção sobre capacidades de negócio, reforçar as separações.

Além de descentralizar decisões sobre modelos conceituais, microsserviços também descentralizam decisões de armazenamento de dados. Enquanto aplicações monolíticas preferem um único banco de dados lógico para dados persistentes, empresas costumam preferir um único banco de dados em uma gama de aplicações — muitas dessas decisões movidas por modelos comerciais de fornecedores em torno de licenciamento. Microsserviços preferem deixar cada serviço gerenciar seu próprio banco de dados, seja com instâncias diferentes da mesma tecnologia de banco, seja com sistemas de banco de dados totalmente diferentes — uma abordagem chamada Polyglot Persistence. É possível usar polyglot persistence em um monolito, mas aparece com mais frequência em microsserviços.

**Figura 4: Dados descentralizados**

Descentralizar a responsabilidade pelos dados entre microsserviços tem implicações para o gerenciamento de atualizações. A abordagem comum para lidar com atualizações tem sido usar transações para garantir consistência ao atualizar múltiplos recursos. Essa abordagem é frequentemente usada dentro de monolitos.

Usar transações dessa forma ajuda com a consistência, mas impõe um acoplamento temporal significativo, o que é problemático entre múltiplos serviços. Transações distribuídas são notoriamente difíceis de implementar e, como consequência, arquiteturas de microsserviços enfatizam coordenação sem transações entre serviços, com reconhecimento explícito de que a consistência pode ser apenas consistência eventual, e problemas são tratados por operações compensatórias.

Escolher gerenciar inconsistências dessa forma é um novo desafio para muitos times de desenvolvimento, mas é um desafio que muitas vezes corresponde à prática de negócio. Frequentemente, negócios lidam com um certo grau de inconsistência para responder rapidamente à demanda, tendo algum tipo de processo de reversão para lidar com erros. A troca vale a pena, desde que o custo de corrigir erros seja menor que o custo de negócio perdido sob maior consistência.

### Automação de Infraestrutura

Técnicas de automação de infraestrutura evoluíram enormemente nos últimos anos — a evolução da nuvem, e da AWS em particular, reduziu a complexidade operacional de construir, implantar e operar microsserviços.

Muitos dos produtos ou sistemas construídos com microsserviços estão sendo construídos por times com ampla experiência em Continuous Delivery e sua precursora, Continuous Integration. Times que constroem software dessa forma fazem uso extensivo de técnicas de automação de infraestrutura, ilustrado na esteira de build abaixo.

**Figura 5: esteira de build básica**

Já que este não é um artigo sobre Continuous Delivery, vamos chamar atenção apenas para algumas características-chave aqui. Queremos o máximo de confiança possível de que nosso software está funcionando, então rodamos muitos **testes automatizados**. A promoção de software funcionando "para cima" na esteira significa que **automatizamos a implantação** para cada novo ambiente.

> **Sidebar — Facilite fazer a coisa certa**
> Um efeito colateral que encontramos do aumento da automação, como consequência de entrega e implantação contínuas, é a criação de ferramentas úteis para ajudar desenvolvedores e o pessoal de operações. Ferramental para criar artefatos, gerenciar bases de código, montar serviços simples ou adicionar monitoramento e logging padronizados é bastante comum hoje. O melhor exemplo na web é provavelmente o conjunto de ferramentas de código aberto da Netflix, mas há outros, incluindo o Dropwizard, que usamos extensivamente.

Uma aplicação monolítica será construída, testada e passada por esses ambientes com bastante tranquilidade. Acontece que, uma vez que você investiu em automatizar o caminho para produção de um monolito, implantar *mais* aplicações não parece mais tão assustador. Lembre-se: um dos objetivos do CD é tornar a implantação chata (boring); então, seja com uma ou três aplicações, contanto que continue sendo chata, não importa<sup>[11]</sup>.

> **Nota de rodapé 11:** Estamos sendo um pouco desonestos aqui. Obviamente, implantar mais serviços, em topologias mais complexas, é mais difícil que implantar um único monolito. Felizmente, padrões reduzem essa complexidade — mesmo assim, investimento em ferramental é essencial.

Outra área em que vemos times usando automação extensiva de infraestrutura é no gerenciamento de microsserviços em produção. Em contraste com nossa afirmação acima de que, contanto que a implantação seja chata, não há tanta diferença entre monolitos e microsserviços, o cenário operacional de cada um pode ser marcadamente diferente.

**Figura 6: A implantação de módulos costuma diferir**

### Design para Falha

Uma consequência de usar serviços como componentes é que as aplicações precisam ser projetadas para tolerar a falha de serviços. Qualquer chamada de serviço pode falhar devido à indisponibilidade do fornecedor; o cliente tem que responder a isso da forma mais graciosa possível. Essa é uma desvantagem em comparação com um design monolítico, pois introduz complexidade adicional para lidar com isso. A consequência é que times de microsserviços refletem constantemente sobre como falhas de serviço afetam a experiência do usuário. O Simian Army da Netflix induz falhas de serviços e até de datacenters durante o horário de trabalho para testar tanto a resiliência da aplicação quanto o monitoramento.

> **Sidebar — O circuit breaker e código pronto para produção**
> Circuit Breaker aparece em *Release It!* ao lado de outros padrões como Bulkhead e Timeout. Implementados juntos, esses padrões são de importância crucial ao construir aplicações que se comunicam. Este post do blog técnico da Netflix faz um ótimo trabalho explicando a aplicação deles.

Esse tipo de teste automatizado em produção seria o suficiente para dar à maioria dos grupos de operação o tipo de calafrio que geralmente precede uma semana de folga. Isso não quer dizer que estilos arquiteturais monolíticos não sejam capazes de configurações sofisticadas de monitoramento — é só menos comum na nossa experiência.

Como serviços podem falhar a qualquer momento, é importante ser capaz de detectar falhas rapidamente e, se possível, restaurar o serviço automaticamente. Aplicações de microsserviços colocam muita ênfase em monitoramento em tempo real da aplicação, verificando tanto elementos arquiteturais (quantas requisições por segundo o banco de dados está recebendo) quanto métricas relevantes para o negócio (quantos pedidos por minuto estão sendo recebidos). Monitoramento semântico pode fornecer um sistema de alerta precoce de que algo está dando errado, disparando os times de desenvolvimento para investigar.

Isso é particularmente importante em uma arquitetura de microsserviços porque a preferência dos microsserviços por coreografia e colaboração baseada em eventos leva a comportamento emergente. Embora muitos especialistas elogiem o valor da emergência serendipitosa, a verdade é que comportamento emergente às vezes pode ser algo ruim. Monitoramento é vital para detectar rapidamente comportamento emergente ruim, para que possa ser corrigido.

> **Sidebar — Chamadas síncronas consideradas prejudiciais**
> Toda vez que você tem várias chamadas síncronas entre serviços, vai encontrar o efeito multiplicativo do downtime. Simplificando, isso é quando o downtime do seu sistema se torna o produto dos downtimes dos componentes individuais. Você enfrenta uma escolha: tornar suas chamadas assíncronas ou gerenciar o downtime. No www.guardian.co.uk, implementaram uma regra simples na nova plataforma — uma chamada síncrona por requisição de usuário —, enquanto na Netflix, o redesenho da API da plataforma incorporou assincronicidade ao tecido da API.

Monolitos podem ser construídos para serem tão transparentes quanto um microsserviço — de fato, deveriam ser. A diferença é que você absolutamente precisa saber quando serviços rodando em processos diferentes estão desconectados. Com bibliotecas dentro do mesmo processo, esse tipo de transparência é menos provável de ser útil.

Times de microsserviços esperariam ver configurações sofisticadas de monitoramento e logging para cada serviço individual, como dashboards mostrando status de disponibilidade e uma variedade de métricas operacionais e de negócio. Detalhes sobre status do circuit breaker, throughput atual e latência são outros exemplos que costumamos encontrar na prática.

### Design Evolutivo

Praticantes de microsserviços geralmente vêm de um histórico de design evolutivo e veem a decomposição de serviços como mais uma ferramenta para permitir que desenvolvedores de aplicações controlem mudanças em sua aplicação sem desacelerar a mudança. Controle de mudança não significa necessariamente redução de mudança — com as atitudes e ferramentas certas, é possível fazer mudanças frequentes, rápidas e bem controladas no software.

Sempre que você tenta quebrar um sistema de software em componentes, enfrenta a decisão de como dividir as peças — quais são os princípios pelos quais decidimos fatiar nossa aplicação? A propriedade chave de um componente é a noção de substituição e atualização independentes<sup>[12]</sup> — o que implica buscar pontos onde podemos imaginar reescrever um componente sem afetar seus colaboradores. Muitos grupos de microsserviços, aliás, vão além, esperando explicitamente que muitos serviços sejam descartados, em vez de evoluídos, no longo prazo.

> **Nota de rodapé 12:** De fato, Daniel Terhorst-North se refere a esse estilo como *Replaceable Component Architecture*, em vez de microsserviços. Como isso parece falar de um subconjunto das características, preferimos o último termo.

O site do The Guardian é um bom exemplo de aplicação que foi projetada e construída como monolito, mas vem evoluindo em direção a microsserviços. O monolito ainda é o núcleo do site, mas preferem adicionar novas funcionalidades construindo microsserviços que usam a API do monolito. Essa abordagem é particularmente útil para funcionalidades inerentemente temporárias, como páginas especializadas para lidar com um evento esportivo. Essa parte do site pode ser rapidamente montada usando linguagens de desenvolvimento rápido, e removida assim que o evento termina. Vimos abordagens semelhantes em uma instituição financeira, em que novos serviços são adicionados para uma oportunidade de mercado e descartados depois de alguns meses, ou até semanas.

Essa ênfase em substituibilidade é um caso especial de um princípio mais geral de design modular, que é orientar a modularidade pelo padrão de mudança<sup>[13]</sup>. Você quer manter juntas, no mesmo módulo, as coisas que mudam ao mesmo tempo. Partes de um sistema que mudam raramente deveriam estar em serviços diferentes daquelas que estão passando por muita movimentação atualmente. Se você se encontra mudando repetidamente dois serviços juntos, isso é um sinal de que eles deveriam ser fundidos.

> **Nota de rodapé 13:** Kent Beck destaca isso como um de seus princípios de design em *Implementation Patterns*.

Colocar componentes em serviços adiciona uma oportunidade para planejamento de release mais granular. Com um monolito, qualquer mudança exige um build e implantação completos da aplicação inteira. Com microsserviços, no entanto, você só precisa reimplantar o(s) serviço(s) que modificou. Isso pode simplificar e acelerar o processo de release. A desvantagem é que você tem que se preocupar com mudanças em um serviço quebrando seus consumidores. A abordagem tradicional de integração é tentar lidar com esse problema usando versionamento, mas a preferência no mundo dos microsserviços é usar versionamento apenas como último recurso. Podemos evitar muito versionamento projetando serviços para serem o mais tolerantes possível a mudanças em seus fornecedores.

## Microsserviços são o futuro?

Nosso objetivo principal ao escrever este artigo é explicar as principais ideias e princípios dos microsserviços. Ao dedicar tempo para isso, claramente achamos que o estilo arquitetural de microsserviços é uma ideia importante — que merece consideração séria para aplicações corporativas. Construímos recentemente vários sistemas usando esse estilo e conhecemos outros que o usaram e favorecem essa abordagem.

Entre os que conhecemos que estão de alguma forma sendo pioneiros nesse estilo arquitetural estão a Amazon, a Netflix, The Guardian, o UK Government Digital Service, realestate.com.au, Forward e comparethemarket.com. O circuito de conferências de 2013 estava cheio de exemplos de empresas migrando para algo que se classificaria como microsserviços — incluindo a Travis CI. Além disso, há bastante organizações que há muito tempo fazem o que classificaríamos como microsserviços, mas sem nunca usar esse nome (frequentemente isso é rotulado como SOA — embora, como dissemos, SOA venha em muitas formas contraditórias<sup>[14]</sup>).

> **Nota de rodapé 14:** E SOA dificilmente é a raiz dessa história. Lembro de pessoas dizendo "já fazemos isso há anos" quando o termo SOA apareceu no início do século. Um argumento era que esse estilo tem raízes na forma como programas COBOL se comunicavam via arquivos de dados nos primeiros dias da computação corporativa. Em outra direção, poderia se argumentar que microsserviços são a mesma coisa que o modelo de programação Erlang, mas aplicado a um contexto de aplicação corporativa.

Apesar dessas experiências positivas, no entanto, não estamos afirmando que temos certeza de que microsserviços são a direção futura das arquiteturas de software. Embora nossas experiências até agora sejam positivas em comparação com aplicações monolíticas, temos consciência de que não passou tempo suficiente para fazermos um julgamento completo.

Frequentemente, as verdadeiras consequências de decisões arquiteturais só ficam evidentes vários anos depois de serem tomadas. Vimos projetos em que um bom time, com forte desejo de modularidade, construiu uma arquitetura monolítica que se deteriorou ao longo dos anos. Muitas pessoas acreditam que essa deterioração é menos provável com microsserviços, já que as fronteiras de serviço são explícitas e difíceis de contornar remendando. Mas até vermos sistemas com idade suficiente, não podemos avaliar de verdade como arquiteturas de microsserviços amadurecem.

Certamente há razões pelas quais se poderia esperar que microsserviços amadurecessem mal. Em qualquer esforço de componentização, o sucesso depende de quão bem o software se encaixa em componentes. É difícil descobrir exatamente onde deveriam estar as fronteiras dos componentes. Design evolutivo reconhece as dificuldades de acertar as fronteiras e, portanto, a importância de ser fácil refatorá-las. Mas quando seus componentes são serviços com comunicação remota, refatorar é muito mais difícil do que com bibliotecas em processo. Mover código é difícil através de fronteiras de serviço, quaisquer mudanças de interface precisam ser coordenadas entre os participantes, camadas de compatibilidade retroativa precisam ser adicionadas, e o teste fica mais complicado.

Outra questão é que, se os componentes não se compõem de forma limpa, tudo que você está fazendo é deslocar complexidade de dentro de um componente para as conexões entre componentes. Isso não apenas move a complexidade, como a move para um lugar menos explícito e mais difícil de controlar. É fácil pensar que as coisas estão melhores quando você está olhando para dentro de um componente pequeno e simples, perdendo de vista conexões confusas entre serviços.

Por fim, há o fator da habilidade do time. Novas técnicas tendem a ser adotadas por times mais habilidosos. Mas uma técnica que é mais eficaz para um time mais habilidoso não vai necessariamente funcionar para times menos habilidosos. Já vimos bastante casos de times menos habilidosos construindo arquiteturas monolíticas bagunçadas, mas leva tempo para ver o que acontece quando esse tipo de bagunça ocorre com microsserviços. Um time ruim sempre vai criar um sistema ruim — é muito difícil dizer se microsserviços reduzem a bagunça nesse caso, ou a pioram.

Um argumento razoável que já ouvimos é que você não deveria começar com uma arquitetura de microsserviços. Em vez disso, comece com um monolito, mantenha-o modular, e o divida em microsserviços assim que o monolito se tornar um problema. (Embora esse conselho não seja ideal, já que uma boa interface em processo geralmente não é uma boa interface de serviço.)

Então escrevemos isso com otimismo cauteloso. Até agora, vimos o suficiente sobre o estilo de microsserviços para sentir que pode ser um caminho que vale a pena trilhar. Não podemos dizer com certeza onde vamos acabar, mas um dos desafios do desenvolvimento de software é que você só pode tomar decisões com base na informação imperfeita que tem em mãos no momento.

---

## Nota de tradução

Este documento é uma tradução livre para português (PT-BR) do artigo original em inglês "Microservices", de James Lewis e Martin Fowler, publicado em martinfowler.com em 25 de março de 2014. O conteúdo das imagens/figuras foi indicado apenas pela legenda (figuras não reproduzidas). Notas de rodapé foram inseridas como citações (blockquotes) próximas ao ponto de referência no texto, e sidebars/boxes foram marcados explicitamente como tal.
