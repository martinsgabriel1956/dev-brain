# Como Projetar Sistemas: Um Passo a Passo Completo (Estudo de Caso: Encurtador de URLs)

> Transcrição de vídeo em português, colada pelo usuário no chat e reorganizada em seções/parágrafos para leitura (removidas repetições e hesitações de fala; conteúdo não traduzido — já em português). Autor/canal não identificado explicitamente na transcrição.

## Abertura

Começar a projetar sistemas pode ser assustador, já que envolve não só ter a base técnica para tomar boas decisões, mas também ter o entendimento profundo do problema que você quer resolver. Hoje vamos resolver um problema clássico de entrevistas técnicas e, no final, você vai ter um passo a passo para projetar qualquer sistema.

Para começo de conversa: o que é arquitetura de software? É o processo de determinar os componentes de um sistema, definir como eles vão se comunicar entre si e garantir que tudo atenda a um conjunto de requisitos e padrões de qualidade. Nas entrevistas técnicas, você pode ver esse processo sendo chamado de *system design*.

A palavra-chave quando projetamos sistemas é **tradeoffs**. Esses são os prós e contras que analisamos em cada decisão de arquitetura, e pesamos contra quais aspectos de qualidade são mais importantes no nosso sistema — geralmente equilibrando velocidade de resposta, custo e complexidade. Vamos ver isso na prática.

## Passo 1 — Entender o Problema

Vamos projetar um encurtador de URLs. O fluxo de uso é simples: usuários enviam uma URL longa, o sistema cria uma URL curta para substituir e cria um mapeamento interno que associa a URL curta à original, então retorna a versão curta para os usuários. Depois, quando um cliente acessa a URL curta, o sistema reconhece e redireciona o usuário para o local correto.

## Passo 2 — Identificar Requisitos

A regra de ouro para projetar sistemas é: **"Não invente as regras, faça perguntas de esclarecimento."** É isso que o entrevistador espera em uma entrevista de arquitetura. Suas perguntas devem te guiar a entender exatamente como seu produto final deve ser e quaisquer requisitos ou restrições específicas.

Quando falamos de requisitos em arquitetura de sistema, podemos dividi-los em dois tipos: **requisitos funcionais** e **requisitos não funcionais**. Requisitos funcionais, como o nome sugere, especificam as principais funcionalidades do sistema e o que o usuário pode esperar delas. Requisitos não funcionais, por outro lado, falam do aspecto técnico, cobrindo elementos que garantem a qualidade do sistema, como performance, escalabilidade, disponibilidade, segurança, entre outros.

### Requisitos Funcionais

Direto do enunciado do problema podemos derivar:

1. Usuários devem poder enviar uma URL longa e receber uma URL curta como retorno.
2. Quando um cliente acessa uma URL curta, ele deve ser redirecionado para a URL longa original.

Algo que não estava explícito nas instruções do problema, mas seria uma boa pergunta para fazer ao entrevistador, é se devemos implementar algum tipo de registro de conta, para que usuários possam gerenciar suas URLs curtas criadas, tendo uma visão centralizada e podendo habilitar, desabilitar ou até deletar as URLs geradas. Vamos imaginar que perguntamos ao entrevistador e ele disse que sim. Agora temos novos requisitos funcionais:

3. Usuários devem poder se registrar e fazer login no sistema.
4. Usuários devem poder gerenciar suas próprias URLs curtas, incluindo habilitar, desabilitar ou deletá-las.

Lembre-se que o entrevistador pode não te entregar todos os detalhes de cara. Eles não estão tentando te enganar ou querendo que você falhe, mas estão checando sua habilidade de pensar no fluxo de uso completo, na experiência do usuário e em considerar casos extremos.

### Requisitos Não Funcionais

Você pode perguntar ao entrevistador se existem requisitos não funcionais específicos, como preocupações de segurança ou limitações de tecnologia, mas em termos gerais de qualidade de sistema vamos imaginar que nossas prioridades são:

- O sistema deve ter uma relação de um para um entre URLs curtas e longas correspondentes — ou seja, queremos prevenir geração duplicada de URLs curtas ou uma URL curta que aponte para mais de uma URL longa.
- O sistema deve ter baixa latência — ou seja, o tempo entre a requisição do cliente e a resposta deve ser curto. Você pode definir um limite específico, como responder em menos de 100 milissegundos, por exemplo.
- O sistema deve ser altamente disponível — ou seja, deve estar continuamente disponível com nenhum ou quase nenhum tempo fora do ar.
- O sistema deve ser resiliente a falhas — ou seja, deve ser capaz de se adaptar e se recuperar de erros e falhas.

## Passo 3 — Prever Padrões de Tráfego

Esse é o ponto da entrevista em que queremos começar a introduzir números. Em um cenário de mundo real, tentaríamos fazer previsões baseadas em dados que já temos, como quantos clientes nosso sistema tem, quantas vezes por dia eles usam cada operação e o crescimento esperado da empresa. Em uma entrevista, é uma boa ideia perguntar ao entrevistador essas informações, ou inventar seus próprios números e perguntar se parecem plausíveis.

Nesse cenário, podemos imaginar:

- 1 milhão de novas URLs curtas criadas por dia.
- 100 milhões de redirecionamentos por dia.
- Pico médio de tráfego de aproximadamente 10.000 redirecionamentos por segundo.
- Retenção de dados esperada de 5 anos.

Algo importante a notar é a **proporção de leitura para escrita** do nosso sistema: 100 leituras para 1 escrita. Isso é típico para um encurtador de URL, já que uma única URL curta tende a ser acessada muitas vezes após ser criada. Isso significa que nosso sistema vai precisar de muito mais poder de processamento para redirecionar do que para criar URLs — algo a se considerar em termos da necessidade de escalabilidade.

Escalar significa adaptar a infraestrutura do sistema para suportar mudanças no tráfego — em outras palavras, dar mais recursos em momentos de pico de requisição e remover recursos quando não são mais necessários. Considerar isso é crucial para o requisito não funcional de ter um sistema altamente disponível.

### Monolito vs. Microsserviços

Isso leva a um conceito importante de arquitetura de software: monolito versus microsserviços. Um monolito é uma unidade única de uma aplicação que centraliza todos os componentes — você pode imaginar como um canivete suíço. Microsserviços, por outro lado, quebram o software em serviços menores e independentes, especializados em uma única parte da aplicação — como se fossem diferentes ferramentas em uma caixa de ferramentas.

A análise de tradeoffs entre monolitos e microsserviços é uma discussão mais longa para outro vídeo, mas uma coisa que vale destacar: o monolito pode adicionar complexidade em termos de escalabilidade, já que não podemos escalar apenas as funcionalidades que precisam — temos que escalar a unidade inteira. Microsserviços oferecem flexibilidade porque podemos escalar cada componente independentemente. Considerando que nosso sistema tem a realidade de ter 100 vezes mais leituras do que escritas, sem restrições extras, a inclinação é quebrá-lo em microsserviços.

## Passo 4 — Desenhar Componentes em Alto Nível

Agora que temos nossos requisitos, podemos começar a visualizar em alto nível quais partes diferentes compõem o sistema e onde estão os pontos de conexão. Como decidido no passo anterior, o backend será dividido em microsserviços — um serviço para cada funcionalidade:

- Um serviço para **criar** URLs curtas.
- Um serviço para **redirecionar** URLs curtas para suas versões originais.
- Um terceiro serviço para lidar com **registro e login de usuários**.

Esses serviços precisam estar conectados a um **banco de dados** para persistir e acessar o mapeamento entre URLs longas e curtas, assim como dados de usuários. Também precisamos de um componente de **front end**, para que os usuários possam interagir com o sistema — chamamos isso de **cliente**. Vamos adicionar também um **serviço de autenticação**, responsável por lidar com registro de usuário, login e emissão de tokens que identificam quem é o usuário nas requisições subsequentes. E finalmente precisamos de um **conector de API**, que é o ponto de entrada para as requisições do cliente serem direcionadas ao backend.

Note que ainda não estamos dizendo qual banco de dados ou qual linguagem de programação estamos usando — isso vem depois. Primeiro queremos entender o formato do sistema.

## Passo 5 — Definir APIs

Com os componentes definidos, podemos começar a esboçar o contrato entre eles. Uma API é uma interface que define como duas aplicações se comunicam: o que uma pode pedir e o que a outra responde. Vamos mantê-las simples e focadas nas operações principais:

- `POST` para criação — recebe uma URL longa no corpo da requisição e retorna a URL curta gerada. Esse é o ponto de entrada para o serviço de encurtamento de URLs.
- `GET /{código curto}` — recebe o código curto no path e responde com HTTP 301 ou 302, redirecionando para a URL longa original.
- `POST` para registro — recebe dados do usuário, como e-mail e senha, e cria uma nova conta de usuário.
- `POST` para login — recebe credenciais do usuário e retorna um token de autenticação, que o cliente vai usar em toda requisição protegida daquele ponto em diante.
- `GET` para listagem — retorna a lista de URLs curtas pertencentes ao usuário autenticado, para que possam gerenciá-las.
- `PUT`/`PATCH` para edição — permite que usuários editem URLs, habilitando ou desabilitando.
- `DELETE` — permite que usuários deletem suas próprias URLs curtas.

## Passo 6 — Selecionar a Stack Técnica

Perceba como, até esse ponto, não pensamos em serviços ou tecnologias específicas — o ponto principal é resolver o problema, e a implementação vem como consequência. Agora que temos os requisitos determinados e a base dos componentes, podemos pensar na stack técnica, ou seja, nas ferramentas específicas. Para esse exemplo, vamos ver como a arquitetura ficaria usando serviços da AWS.

- **Amazon EC2** — uma instância para cada microsserviço. São instâncias de servidores que você pode configurar e gerenciar, permitindo escalabilidade independente. Para garantir resiliência e disponibilidade, podemos adicionar pelo menos dois servidores por microsserviço — isso é chamado de **redundância de servidores**, e assegura que, mesmo se um servidor falhar, a aplicação ainda estará rodando no outro e não vai cair.
  - Alternativa: ir de **serverless** e criar diferentes funções Lambda para cada serviço. Aplicações serverless têm o benefício de escalar automaticamente, mas vêm com seus próprios desafios.
- **Amazon Elastic Load Balancer** — já que estamos usando instâncias de servidor gerenciadas, adicionamos um load balancer para distribuir o tráfego entre os diferentes servidores.
- **AWS Amplify** — hospeda a aplicação front end, com deploys automatizados, CDN e HTTPS prontos para uso.
- **Amazon API Gateway** — o conector de API, que roteia as requisições para os microsserviços.
- **Amazon Cognito** — para autenticação, lidando com registro de usuário, login e emissão de tokens sem precisar construir isso do zero. Integra com o API Gateway para autorizar os endpoints protegidos definidos anteriormente.
- **Banco de dados** — a decisão mais básica é escolher entre SQL e NoSQL. A principal diferença está em como cada um estrutura os dados: um banco SQL é estruturado como tabelas com linhas e colunas, enquanto um banco NoSQL é construído em pares chave-valor, que tendem a ter menor latência em leituras. Um banco SQL pode ser preferido se você tem dados altamente estruturados e quer realizar diferentes operações de *join*. Nesse caso, os dados são simples, facilmente estruturados como pares chave-valor, e os requisitos não funcionais esperam que se priorize baixa latência — então a escolha é **NoSQL**, adicionando **Amazon DynamoDB** ao diagrama.

Essa é uma das combinações válidas, não a única. Um conjunto diferente de tradeoffs poderia levar a um banco relacional, um serviço com containers ou uma estratégia de autenticação diferente. O que importa é ser capaz de justificar cada escolha contra os requisitos.

## Passo 7 — Considerar Restrições de Implementação

Para muitas entrevistas técnicas, o que fizemos até aqui pode ser suficiente: mostramos ao entrevistador que entendemos o problema e seus requisitos, projetamos o fluxo em alto nível e sugerimos uma stack técnica baseada em tradeoffs específicos. Mas você ainda pode ir além e apontar preocupações de nível mais baixo. Uma boa forma de fazer isso é revisar sua lista de requisitos e checar se você cobriu tudo.

**Requisitos funcionais:**
- Usuários devem poder enviar uma URL longa e receber uma URL curta em retorno. ✅
- Quando um cliente acessa uma URL curta, ele deve ser redirecionado para a URL longa original. ✅
- Usuários devem poder se registrar e fazer login no sistema. ✅
- Usuários devem poder gerenciar suas próprias URLs curtas, incluindo habilitar, desabilitar e deletá-las. ✅

**Requisitos não funcionais:**
- O sistema deve ter baixa latência. ✅ (considerado nas escolhas de arquitetura)
- O sistema deve ser altamente disponível. ✅ (podemos escalar partes do backend independentemente)
- O sistema deve ser resiliente a falhas. ✅ (redundância de servidores)
- O sistema deve ter uma relação de um para um entre URLs curtas e URLs longas correspondentes. ⚠️ **Não abordado ainda.**

Em uma entrevista, o entrevistador poderia apontar essa lacuna, ou poderia fazer uma anotação silenciosa sobre a falta de atenção a detalhes. Existem algumas opções para resolver isso, e cada uma vem com seus próprios tradeoffs: uma possibilidade é fazer hash da URL longa e pegar os primeiros caracteres como URL curta, e, antes de escrever no banco de dados, checar se a URL curta já existe. Em caso positivo, pode-se adicionar um pequeno *salt* (pente/sal) à URL curta e refazer o hash até conseguir uma URL única.

Parabéns — você acabou de projetar um encurtador de URLs.

## Fechamento — Lições Gerais

Antes de encerrar, três coisas que fazem a maior diferença para quem está começando a projetar sistemas:

1. **Arquitetura de software é uma questão de prática.** Quanto mais sistemas você projeta — seja na vida real ou em exercícios teóricos — mais padrões você começa a reconhecer, e mais rápido o cérebro conecta um problema novo a algo que você já viu. É por isso que estudar problemas clássicos é tão valioso: encurtadores de URL, apps de chat, feeds de notícia, sistemas de reserva, plataformas de streaming de vídeo. Esses problemas sempre aparecem em entrevistas não porque os entrevistadores são preguiçosos, mas porque cada um exercita um conjunto diferente de fundamentos. Uma vez que você projetou cada um deles, começa a ter blocos de construção reutilizáveis para os próximos sistemas.

2. **Pense criticamente sobre cada decisão que você toma.** Não escolha um banco de dados porque todo mundo usa, ou uma tecnologia porque está na moda. Pergunte por quê — e, mais importante, pergunte o que você está abrindo mão ao escolher alguma coisa. Cada decisão de arquitetura tem um custo, e ser capaz de articular esses tradeoffs é o que separa alguém que só memorizou respostas de alguém que realmente entende o que está fazendo.

3. **Invista nos fundamentos.** Coisas como bancos de dados funcionam por debaixo dos panos, como cache muda a performance, o que acontece em uma requisição de rede — esses conceitos aparecem em absolutamente todo sistema que você vai projetar. Quanto mais forte for sua base, menos intimidante qualquer novo problema vai parecer.

Projetar sistemas é menos sobre saber a resposta certa e mais sobre pensamento estruturado. Se você passa pelos requisitos, padrões de tráfego, componentes, APIs e escolhas de tecnologia, e justifica cada decisão contra um tradeoff, você está no caminho certo. O encurtador de URLs projetado aqui é um problema clássico de entrevista, mas o framework funciona para quase qualquer coisa: comece pelo problema, não pela tecnologia.
