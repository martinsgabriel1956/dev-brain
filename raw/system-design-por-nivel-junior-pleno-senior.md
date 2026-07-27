# System Design para Cada Nível: Júnior, Pleno e Sênior

Transcrição de vídeo de Augusto Galego sobre o que é esperado de cada nível de senioridade (júnior, pleno, sênior) em termos de System Design — tanto em entrevistas técnicas quanto no trabalho do dia a dia.

## Introdução: uma tarefa impossível

Eu tenho nas minhas mãos uma tarefa que é efetivamente impossível: dizer o que é esperado de um júnior a nível de system design, o que é esperado de um pleno e o que é esperado de um sênior. Essa tarefa é impossível porque nenhuma empresa sequer concorda na definição do que é um júnior, um pleno ou um sênior. Se elas não concordam nessa definição, é impossível eu dizer o que é esperado para cada um desses níveis. Mesmo assim, vou tentar tirar uma média aqui, falar algo que eu acho razoável para cada um desses cenários.

Eu sou Augusto Galego, tenho 12 anos de experiência na área de software, sendo os últimos cinco trabalhando para empresas gringas. Baseado nessa trajetória, vou te contar o que eu acho razoável de system design para cada um desses diferentes níveis.

## Entrevista vs. trabalho: duas coisas diferentes

Primeiro preciso separar duas coisas: existe uma diferença entre como você vai ser entrevistado para um trabalho e como você vai trabalhar nesse trabalho.

Nas entrevistas de system design, geralmente é cobrada de você uma compreensão do todo: montar um sistema completo, incluindo arquitetura, esquemas de banco de dados, tradeoffs, infra, design de API, escalabilidade, filas, etc.

No seu emprego, sinceramente, se você for júnior ou pleno, provavelmente não vai fazer isso. Se você for sênior, talvez. No trabalho, ao invés da compreensão do todo, você geralmente vai precisar de uma visão rasa do todo, mas um entendimento fundamental daquela parte específica em que você atua. Se você é um dev que trabalha na API, precisa entender bem a API. Se lida com esquemas de banco, precisa entender bem o banco. Se é DevOps, precisa entender bem a infra. Seria legal se todo mundo entendesse tudo, mas não é nisso que você vai trabalhar no dia a dia.

O único momento em que você geralmente une absolutamente tudo isso na carreira é quando você é sênior (ou mais) e está construindo uma feature nova para integrar num sistema, ou um sistema novo inteiro. Esse trabalho geralmente não é delegado a plenos nem a júniors — por isso a compreensão do todo é mais importante para quem é mais sênior.

Só que a empresa não tá nem aí para essa distinção: ela entrevista todo mundo baseada no mesmo padrão (o padrão que o Google usa, que todo mundo copiou). As entrevistas de system design hoje em dia são muito parecidas entre júnior, pleno e sênior — o que muda é o nível de profundidade esperado.

## Júnior

### No trabalho

Para trabalhar numa empresa no dia a dia, um júnior precisa de pouquíssimo system design. Precisa entender o que é um server, o que é um cliente, o que é um banco de dados, um pouco de arquitetura, um pouco de networking. Um júnior que de fato é júnior não desenha sistemas completos, raramente escreve os próprios testes, e não tira uma feature da cabeça dele fazendo o design de todo o sistema da feature.

### Na entrevista

A entrevista, porém, vai cobrar system design — só que numa profundidade rasa. O objetivo da entrevista de system design não é você cuspir um sistema pronto para produção (ninguém consegue desenhar o system design do Instagram pronto para produção em uma hora — nem o próprio Instagram). A entrevista serve para você demonstrar uma certa fundação de conhecimento, comunicação clara e raciocínio lógico.

**Exemplo de raciocínio lógico — jogo de xadrez ao vivo:** dois players interagem com um servidor. Em algum momento é o turno do player 1: ele pode agir, o player 2 está bloqueado. Quando o player 1 executa a ação, o player 2 precisa ser avisado (para desbloquear a vez dele) e o player 1 precisa ficar bloqueado. Como comunicar isso em tempo quase real sem causar inconsistência? Existem várias soluções (polling, WebSockets, etc.) — para um júnior, propor polling simples ("o player 2 dá um GET a cada 5 segundos até ser a vez dele") já é um raciocínio razoável, e às vezes até para sênior essa é a solução correta, desde que você saiba argumentar.

**O que é esperado de conhecimento de júnior:** compreensão muito boa dos componentes básicos de arquitetura — como um banco de dados funciona, o que é uma API e como ela funciona, o fluxo cliente-servidor, um pouco de protocolos de comunicação (HTTP, RPC). É legal saber o que é cache e o que é fila, mas o que é realmente obrigatório para qualquer profissional de software é: banco de dados, API, relação cliente-servidor e algum protocolo de comunicação.

**Formato de entrevista para júnior:** geralmente um sistema simples, sem conhecimento específico exigido — uma API simples, um encurtador de URL, o exemplo do xadrez (que tem só dois usuários e não precisa ser tão em tempo real quanto um League of Legends ou CS). O resultado esperado é: clarificar requisitos, definir features, descrever fluxos de read/write, desenhar a API, um pouco do esquema do banco, explicar alguns tradeoffs e desenhar uma arquitetura de alto nível.

## Pleno

Além dos componentes de júnior (API, cliente-servidor, networking), para pleno é legal ter compreensão de workers, API gateway, load balancer, tradeoffs entre SQL e NoSQL, Blob Store e talvez CDN.

**Nota do autor:** hoje em dia pleno e sênior se confundem muito — a linha está borrada. Ele traça a linha mesmo assim, mas reconhece que na prática pleno tende a virar sênior rapidamente.

**Racional das decisões:** para júnior, muitas vezes basta saber que algo existe, sem explicar bem os tradeoffs ("vamos botar um banco de dados aqui porque resolve nosso problema"). Para pleno, a decisão já precisa ter um racional — por que SQL em vez de NoSQL, por exemplo — e idealmente ligado a algum conhecimento prático (júnior muitas vezes não tem prática; pleno já interagiu na prática com um NoSQL, um SQL, uma Blob Store, um worker, um Lambda, uma API num API Gateway).

**Na entrevista de pleno:** tudo que é esperado de júnior, mas com mais especificidade — requisitos funcionais e não funcionais, mais atenção à API (payloads, endpoints), melhor modelagem do esquema do banco, algum nível de estimativa e de escalabilidade (que geralmente não é cobrado de júnior), identificação de gargalos (bottlenecks) e algum nível de fault tolerance (o que acontece se as coisas quebrarem, qual o único ponto de falha, o que pode melhorar). Ainda assim, dificilmente isso entra em detalhes muito profundos.

## Sênior

Para sênior é esperada profundidade — baseada na experiência — e maturidade. Onde o pleno "leu por cima" o que é NoSQL e SQL, o sênior precisa citar tradeoffs entre eles e ter um julgamento mais fino sobre o que usar em cada situação. Não se avalia mais se você sabe que um load balancer existe (isso já é dado) — se avalia se você consegue usar essa compreensão para montar um sistema que escala para milhões de usuários, seguindo os padrões esperados no nível sênior.

### No trabalho

É no nível sênior que o system design se torna mais crucial no dia a dia: às vezes você escreve os testes, as features, faz o design da API e do esquema, enquanto plenos e júniors implementam cada teste individualmente — mas você precisa ter a compreensão do todo para desenvolver a feature. Às vezes cai no colo do sênior desenvolver o sistema inteiro do zero para uma equipe trabalhar em cima (já aconteceu com o autor várias vezes) — e aí é preciso decidir SQL ou NoSQL, Lambda ou servidor dedicado, monolito ou microsserviços, e justificar cada decisão. Isso é mais o cargo de um tech lead, um CTO ou um staff engineer em várias empresas — daí "sênior plus".

### Na entrevista

Para sênior/sênior-plus, a entrevista exige conhecer os componentes citados (workers, API gateway, Lambda), mas o foco passa a ser tradeoffs: monolito vs. microsserviços, escala, teorema de CAP. Não é só resolver o problema, é discutir os tradeoffs da resolução. A palavra-chave é **escalabilidade** — você está sempre pensando em escala (no mínimo milhões de usuários), identificando gargalos (CPU? network?).

**Problemas mais complexos:** desenhar um Netflix, a parte do Uber que encontra motoristas próximos, um iFood, um sistema de busca como o Google, um sistema de recomendação como o newsfeed de uma rede social ou do Twitter. É óbvio que você não consegue desenhar a Netflix inteira — você tem que escolher suas batalhas e decidir as features mais importantes.

**Postura esperada:** você não reage mais à conversa, você a lidera. Para júnior e pleno a entrevista é muito mais reativa (você responde ao que é perguntado); para sênior é esperado que você inverta o papel, lidere a conversa, seja quem pergunta e clarifica.

**Estimativas mais precisas:** com só uma ou duas horas de entrevista, estimativas precisas ajudam a identificar de antemão o que vai virar gargalo — e resolver isso preventivamente, não reativamente. Você escolhe uma batalha (ex.: escalar um banco de dados para multi-região, adicionar sharding, adicionar cache) e é questionado em profundidade: que tipo de cache (cache-aside ou outro)? Como faz o sharding horizontal vs. vertical? Como faz as partições? Como lida com os IDs? Aqui entram reader replicas, Federation e outras soluções raras que poucas empresas do planeta usam (Netflix, Uber/Google).

Você vai abusar de background jobs e workers para aliviar a carga do sistema. Vai falar sobre diferentes formas de deploy, tradeoffs de infra/arquitetura no deploy, teorema de CAP, e o tradeoff latência vs. vazão vs. disponibilidade. Escolha suas batalhas: em algum ponto o entrevistador vai entrar em profundidade em algum tópico específico.

**Exemplo — Netflix e restrição geográfica de conteúdo:** como resolver que um usuário pode assistir um filme no Brasil mas não pode assistir na Alemanha? Resposta esperada de sênior: CDN no Brasil e na Alemanha, identificação global de onde pertence a assinatura do usuário, localização por região para buscar o conteúdo certo.

### Resumo dos três níveis

- **Júnior:** precisa conseguir solucionar o problema e demonstrar que conhece algo de arquitetura/infra.
- **Pleno:** precisa resolver o problema e mostrar que conhece de fato aquilo que está sendo utilizado (com alguma prática).
- **Sênior:** vai para uma solução de maneira mais ótima e mais profunda, liderando a conversa e discutindo tradeoffs.

## Nota de encerramento

O autor menciona ter lançado, no mês da gravação, um curso completo de System Design (mais de um ano de produção), cobrindo banco de dados, NoSQL, filas, load balancer, API gateway, autenticação, WAF, rate limiting, Saga, CQRS, DNS, Blob Store, cache, CDN, entrevistas práticas simuladas (inclusive fazendo o papel de recrutador). Oferece um mês de reembolso integral sem perguntas. Reforça que também produz bastante conteúdo gratuito sobre System Design no canal.
