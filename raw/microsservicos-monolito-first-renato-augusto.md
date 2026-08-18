# Por Que Você Não Deve Começar Um Projeto com Microsserviços

## Introdução: a obsessão pelo hype

Nos últimos anos os microsserviços se tornaram quase um requisito obrigatório no mercado de tecnologia. Se você já abriu o LinkedIn e procurou por vagas para programador, sabe que praticamente a maioria delas exige conhecimento em microsserviços, mensageria (RabbitMQ, Kafka), Kubernetes, AWS, serverless, e por aí vai. Esses são os requisitos do momento — e com isso a ideia de que microsserviços são a solução para todos os problemas se espalhou de forma quase contagiosa. A sensação é de que, se você não adotar microsserviços no teu projeto, vai ficar para trás. E o pior: você começa a acreditar que todo sistema precisa ser construído dessa maneira, como se essa fosse a única forma de construir sistemas modernos e escaláveis.

Este vídeo mostra por que você não deve começar um projeto utilizando microsserviços, qual é a relação que isso tem diretamente com Domain-Driven Design, e qual é a melhor arquitetura para iniciar um projeto do zero — arquitetura que até as maiores empresas de tecnologia do mundo já estão adotando.

## A armadilha da obsessão por microsserviços

Muita gente acha que microsserviços são um objetivo, e não uma ferramenta — que um sistema distribuído cheio de pequenos serviços independentes automaticamente significa um software moderno, escalável e preparado para crescer. Essa ideia se espalhou tanto que parece que qualquer projeto precisa nascer assim.

O que muita gente não sabe é que até as gigantes da tecnologia já começaram a repensar essa abordagem. Um exemplo: a Amazon, há menos de 2 anos, divulgou uma notícia dizendo que migrou parte do sistema da Amazon Prime Video de volta para uma arquitetura monolítica, e conseguiu reduzir em mais de 90% os custos de infraestrutura na AWS, além de obter menor complexidade sistêmica e muito mais eficiência operacional.

Antes de torcer o nariz e achar que "monolito é coisa ultrapassada": não se trata daquele sistema gigante, desorganizado e difícil de manter. Trata-se de um tipo diferente de monolito, projetado para resolver exatamente os problemas que levaram tantas empresas a adotar microsserviços prematuramente.

## Entendendo monolitos

Pensa no monolito como o sistema que centraliza todas as funcionalidades dentro dele mesmo — tudo roda dentro de um mesmo processo, e todas as partes do sistema (cadastro de cliente, processamento de pedido, geração de relatório) estão no mesmo lugar. Geralmente o monolito tem apenas um banco de dados para toda a aplicação e um repositório para o código-fonte.

**Vantagens:** é simples de desenvolver, testar e escalar — verticalmente e até horizontalmente.
- Escala vertical: adicionar mais recursos ao servidor (memória, poder de processamento, armazenamento) para atender uma carga maior de requisições, sem precisar dividir a aplicação em microsserviços.
- Escala horizontal: criar réplicas do sistema e colocá-las debaixo de um load balancer, que recebe as requisições dos usuários e as distribui entre as várias instâncias.

**Desvantagens:**
- Se uma parte do sistema precisa de mais recursos que outra (ex.: a área de pagamentos recebendo a maioria das requisições numa enxurrada), não dá para escalar só essa área — é preciso escalar o monolito como um todo, o que pode ser ineficiente e um desperdício de recurso.
- O monolito tradicional costuma ter acoplamento forte a nível de código — mexer numa parte pode acabar afetando outras partes, tornando o sistema mais frágil e difícil de manter a longo prazo.
- Dificuldade de trabalho em equipe: uma equipe grande trabalhando numa única base de código, com centenas de PRs subindo um por cima do outro, pode virar um verdadeiro caos.

## Entendendo microsserviços

Numa arquitetura baseada em microsserviços — "o sonho de todo Júnior implementar" — o sistema é dividido em pequenos serviços independentes que se comunicam entre si via rede ou via mensageria. Cada microsserviço tem seu próprio banco de dados, seu próprio ciclo de vida, e pode ser desenvolvido em tecnologias diferentes.

Isso traz a possibilidade de escalar cada microsserviço de forma independente. Exemplo: se o microsserviço de pagamentos é o que está recebendo a maioria das requisições, escala-se só ele — verticalmente (mais poder computacional) ou horizontalmente (novas réplicas) — tratando cada serviço de forma independente.

Outras vantagens: times separados por microsserviço, o que facilita a especialização de cada time no contexto em que trabalha; e a possibilidade de construir cada microsserviço com uma linguagem diferente — por exemplo, Rust ou Go num serviço crítico que precisa de velocidade e poder de processamento, e Java com Spring, PHP com Laravel, JavaScript com Nest, C# em serviços menores ou com foco em produtividade.

## As desvantagens dos microsserviços (o lado sombrio que ninguém te conta)

### Motivo 1 — Complexidade sistêmica exponencial

Quando você está começando um projeto, o foco principal tem que ser a entrega de valor e o desenvolvimento rápido de novas funcionalidades. Com microsserviços, você adiciona uma camada extra de complexidade desde o primeiro dia:

- sistema de comunicação entre os microsserviços;
- ferramentas para pipelines de CI/CD, deploy e versionamento independente de cada microsserviço;
- monitoramento, tracing, observabilidade, log;
- um banco de dados próprio por microsserviço;
- mecanismos de mensageria (RabbitMQ, SQS, Kafka);
- um bom time de DevOps para gerenciar toda essa infraestrutura;
- domínio obrigatório de padrões como CQRS, Event-Driven Architecture, Event Storming, Domain-Driven Design.

E isso tudo é só a ponta do iceberg. É aqui que entra o princípio **YAGNI** (You Ain't Gonna Need It — "você não vai precisar disso"). Quando você começa um novo sistema, quanta certeza você tem de que ele vai ser útil para o usuário final? Muitas vezes a melhor forma de descobrir se uma ideia de software é boa é construir uma versão simplista dela — um MVP — e ver o quão bem ela funciona. Durante essa primeira fase, a prioridade total tem que ser velocidade, para começar a receber feedback logo. O tempo que devia ser gasto construindo funcionalidades essenciais do domínio acaba sendo desperdiçado com infraestrutura e complexidade desnecessária — sem contar que equipes menores geralmente não têm especialistas em arquiteturas distribuídas para lidar com esses desafios, e o time acaba se perdendo na configuração de infraestrutura antes mesmo de validar o produto no mercado.

### Motivo 2 — Microsserviços não é para qualquer software

Arquitetura de microsserviços é extremamente poderosa, mas não é para "software de padaria", nem de mercadinho, nem de médio porte. Essa arquitetura foi criada para escalar não só o sistema, mas também os times.

Pensa: se você tem um monolito hoje com 10 programadores, qual é a lógica de migrar para microsserviços? Cada microsserviço precisa de um time dedicado — não é saudável que todos os programadores deem manutenção em todos os microsserviços (o programador vira "o pato": nada, anda e voa, mas não faz nada direito). Os times precisam ser especialistas naquele serviço ou domínio específico — é por isso que microsserviços ajudam a escalar os times, não só o sistema.

A ideia é: quando a equipe chegar a dezenas ou centenas de programadores e começar a ter problemas com todo mundo mexendo na mesma base de código, aí sim faz sentido pensar em quebrar a aplicação em microsserviços — porque nesse momento existe o cenário ideal **e** a necessidade. Grave essa palavra: necessidade.

### Motivo 3 — Falta de conhecimento de domínio da aplicação (o motivo principal)

Quando se escolhe microsserviços direto, a chance de dar tudo errado é extremamente alta, justamente porque ainda não há conhecimento de domínio suficiente no começo do projeto. O domínio ainda está sendo descoberto — regras de negócio, processos, entidades, tudo em constante evolução. É como construir uma casa sem planta completa: dá para levantar as paredes, mas a chance de ter que derrubar uma parte e refazer é enorme. Você inevitavelmente acaba criando microsserviços que não representam corretamente as responsabilidades do sistema.

**Exemplo (e-commerce):** no início, parece que basta um microsserviço de produtos, um de pedidos e um de clientes. Conforme o negócio evolui, percebe-se que gestão de estoque é crucial e está completamente ligada a produtos, ou que promoções afetam tanto produtos quanto pedidos. Aí é preciso refatorar todos os microsserviços, mudar a comunicação entre eles, e ainda ajustar os bancos de dados (cada um com o seu próprio) — retrabalho constante que poderia ter sido evitado esperando entender melhor o domínio da aplicação primeiro.

## Domain-Driven Design como resposta

É exatamente aqui que entra o Domain-Driven Design (DDD). DDD não é uma arquitetura, não é uma forma de organizar as pastinhas do projeto — é uma abordagem de desenvolvimento de software que coloca o domínio do negócio no centro de tudo. Ajuda a entender a complexidade do negócio, modelar entidades e regras de negócio, e criar um modelo de domínio rico, expressivo e alinhado ao negócio.

Com DDD, aprende-se a identificar os **bounded contexts** — os contextos delimitados da aplicação, que são as áreas do negócio com responsabilidades bem definidas. No e-commerce, por exemplo: um contexto delimitado para catálogo de produtos, outro para processamento de pedidos, outro para gestão de clientes, e assim por diante. Cada contexto delimitado tem seu próprio modelo de domínio, suas próprias regras de negócio e sua própria linguagem — no DDD, a "linguagem ubíqua" (ubiquitous language).

Só depois que a aplicação estiver madura o suficiente — a ponto de se conseguir olhar o código e identificar cada módulo/bounded context muito bem definido — é que faz sentido pensar em microsserviços.

## Monolith First (Martin Fowler)

É exatamente aqui que entra a solução proposta por Martin Fowler, chamada **Monolith First** ("Monolito Primeiro"). A criação desse princípio se deu após duas percepções de Fowler, um dos maiores nomes da engenharia de software:

1. Quase todas as histórias de microsserviços bem-sucedidas começaram com um monolito que ficou muito grande e depois foi quebrado e dividido em microsserviços.
2. Quase todos os casos em que se ouviu falar de um sistema criado do zero já como microsserviços acabaram tendo sérios problemas.

Fowler complementa dizendo que foi ao perceber esse padrão que vários arquitetos de software começaram a argumentar que não se deve começar um projeto com microsserviços — mesmo com certeza absoluta de que o sistema vai ficar grande o suficiente para valer a pena.

No blog de Martin Fowler há uma imagem que ilustra a situação: ao começar a desenvolver um sistema, existem dois caminhos.

- **Caminho de cima** (ir direto para microsserviços): um monte de dragões pegando fogo — ilustra a complexidade extrema e a dificuldade de seguir por esse caminho, justamente porque ainda não se entendem bem os limites do domínio, falta conhecimento profundo do negócio, e ainda existe toda a complexidade de infraestrutura já descrita. É, sem dúvida, o caminho mais arriscado e tortuoso.
- **Caminho de baixo** (começar com arquitetura monolítica): aqui não se trata de um monolito bagunçado, mas de um **monolito modular** — um sistema que, apesar de ser um bloco único de código, é organizado internamente em módulos bem definidos, cada um com responsabilidade clara e objetiva.

## Monolito modular na prática

O monolito modular é representado, na imagem do blog de Fowler, como um retângulo preto (o sistema) com peças coloridas dentro dele (os módulos = os bounded contexts do DDD). Num e-commerce, por exemplo: um módulo para catálogo de produtos, um para pedidos, um para carrinho de compras, um para clientes, um para pagamentos, e por aí vai. Cada módulo tem suas próprias entidades, suas próprias regras de negócio, seus próprios testes unitários e de integração, e pode até ter seu próprio esquema no banco de dados — mesmo compartilhando a mesma conexão.

**Exemplo de repositório real (C#):** um projeto usado como exemplo de monolito modular tem, dentro de `src/modules`, diversos módulos como `administration`, `meetings`, `payments`, `registration`, `user-access`. Cada módulo segue a mesma estrutura de diretórios com camadas bem definidas: camada de aplicação (use cases), camada de domínio (entidades), e camada de testes (integração e unidade). É uma mistura de **Clean Architecture** com **DDD**: o DDD ajuda a delimitar os bounded contexts, e a Clean Architecture ajuda a separar a aplicação em camadas (aplicação, domínio, infraestrutura).

Quando o código/monolito chega nesse nível de maturidade — dá para bater o olho e perceber um bounded context bem definido — aí sim faz sentido pensar em estrangular o monolito e extrair os módulos para microsserviços, levando em conta se existe necessidade real. Na maioria esmagadora dos casos, um monolito modular bem feito é uma boa alternativa aos microsserviços, e mais do que suficiente. Assim se corre menos risco, se aprende mais sobre o negócio, e a arquitetura evolui junto com o conhecimento — muito mais inteligente do que tentar adivinhar tudo de cara e sair construindo um monte de microsserviços.

O monolito é o ponto de partida. Só depois de ter conhecimento de domínio suficiente, e conseguir enxergar como separar a aplicação, é que começa a jornada para microsserviços.

## Livros recomendados

- *Migrando Sistemas Monolíticos para Microsserviços* — Sam Newman
- *Criando Microsserviços* (2ª edição) — Sam Newman
- *Domain-Driven Design* — Eric Evans (o "livro azul", precursor do DDD)

## Encerramento

Recomendação de curtir o vídeo, se inscrever no canal e considerar o clube de membros. Convite para deixar dúvidas nos comentários.

---
**Fonte:** transcrição de vídeo do YouTube, autor Renato Augusto (identificado pela auto-apresentação "Renato Augusto aqui de novo" no início da transcrição e pelo estilo de conteúdo — padrões de projeto, arquitetura, system design — consistente com o autor já indexado na wiki como [[wiki/entities/renato-augusto]]).
