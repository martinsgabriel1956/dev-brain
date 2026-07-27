# O que o Entrevistador Está Pescando numa Entrevista de System Design (Padrão BigTech)

## Introdução

Eu sei, eu sei — a gente tá meio monotemático sobre system design. Prometo que a gente vai voltar à programação normal, mas você precisa entender que isso foi o meu hiperfoco do ano passado, e que nos últimos anos eu fiz mais ou menos 20 entrevistas de system design. Dessas 20, eu fui contratado em 5 empresas que cobraram entrevistas de system design.

## Como as entrevistas se dão — o padrão BigTech

As empresas têm seguido muito um padrão bigtech:

1. Entrevista de RH.
2. Algum tipo de entrevista técnica — às vezes é mais um questionário, com perguntas que podem envolver system design ou não.
3. Muito provavelmente algum teste LeetCode ou take-home / desafio de código.
4. Entrevista de system design.
5. Uma última reunião/entrevista — o "último level" — para ver o fit com o engineering manager e a equipe.

Vamos focar hoje na etapa de system design, com uma pegada bem bigtech. Por quê? Porque as bigtechs começaram esse formato, as outras empresas seguiram o padrão, e as bigtechs costumam cobrar as entrevistas de system design mais completas e mais difíceis. Se a gente estiver preparado pras entrevistas de bigtech, a gente tá preparado para todas.

## O desafio e os padrões mapeados

O entrevistador vai te dar um desafio. Existem alguns padrões de desafios já mapeados — encurtador de URL é um padrão clássico, streaming de vídeo é muito clássico, sistemas de recomendação, aplicativos como Uber/iFood (motoristas disponíveis escutando um pedido, algum deles aceita), Dropbox ou serviços similares.

## Etapa 1 — Entender o problema e levantar requisitos

A primeira etapa de verdade é entender o problema: como um encurtador de URL vai funcionar, de que maneira, quem é o público-alvo, se vai ter login, se vamos trackear métricas, quais são as features.

A partir daí, levanta-se os requisitos — geralmente primeiro os funcionais, depois os não funcionais: quantos usuários vão usar, quais features esses usuários vão utilizar, quais as limitações, o que está dentro e fora do escopo.

**O que o entrevistador está pescando aqui:** seu entendimento. A capacidade de pegar um problema vago e ir pontuando coisas até ter uma boa compreensão do problema, antes de propor uma solução decente. Isso é muito mais importante do que sair desenhando caixinha, fila, banco de dados, load balancer, API gateway direto.

Vale o ditado *garbage in, garbage out*: o input aqui é o nosso entendimento do problema. A solução só pode ser tão boa quanto a nossa capacidade de compreender o problema. Esse entendimento também demonstra maturidade — mostra que você já viu coisas, já trabalhou com coisas, sabe antecipar problemas que podem surgir.

Exemplo de levantamento: vamos desenhar isso para ser um app nativo, web, mobile ou os dois? Precisamos de notificações em tempo real? Precisamos de analytics (quantos usuários clicaram em qual link)? Esses pré-requisitos alteram como o sistema vai funcionar, então é interessante já incorporar isso no entendimento da solução desde o início.

### Requisitos funcionais vs. não funcionais

Dentro de requisitos funcionais, levanta-se como o negócio funciona: qual o tamanho máximo de uma URL que o usuário pode enviar, se o usuário pode escolher a URL curta, se o sistema vai trackear analytics de clique.

Tão importante quanto isso são os requisitos não funcionais: quais os requisitos de latência (é muito diferente encurtar uma URL em poucos milissegundos ou poder demorar 1 minuto), qual a disponibilidade, quanto tempo os links ficam armazenados, qual o volume de usuários/URLs/tráfego.

As bigtechs estão muito interessadas nisso porque é muito diferente fazer uma solução que roda na minha máquina, num único arquivo Node, e fazer uma solução para servir milhões de clientes distribuídos pelo mundo. A minha solução que funciona pra mim não vai funcionar para milhões de usuários. É imprescindível levantar essas dificuldades para mostrar que você está desenhando um negócio de verdade, não um projeto pessoal.

## Etapa 2 — Back-of-envelope estimations (BOE)

Depois dos requisitos, é comum a prática de back-of-envelope estimations (BOE) — "cálculo de padeiro" ou "cálculo de guardanapo". Não precisam ser precisas, mas precisam ser razoáveis. O entrevistador está buscando noção de escala.

Se eu faço um encurtador de URL para 1.000 usuários, é razoável falar "vamos jogar isso numa VPS de R$ 20 e vai funcionar" — e realmente vai. Mas quando lidamos com milhões de usuários, começamos a pensar:

- Quantos requests por segundo estamos servindo? O servidor aguenta? Se não, qual solução usar?
- Quanto de dado estamos armazenando? 500 MB cabe no meu PC; 20 TB já complica e causa lentidão — precisamos pensar em cache e outras soluções para acelerar o acesso.
- Quanta banda larga precisamos?

Depois dessas estimativas já temos uma noção razoável do tamanho e do escopo do que vamos desenhar.

## Etapa 3 — Design da API

Os próximos passos não são seguidos rigorosamente na ordem — são coisas que você pode fazer numa entrevista para demonstrar conhecimento. O design de uma API demonstra que você conhece o problema, sabe como o usuário vai acessar a solução e como as partes da solução vão se comunicar.

Exemplo simples (encurtador de URL): `POST /urls` com um corpo JSON contendo `longUrl`, retornando uma `shortUrl` na resposta. Isso é simples porque o encurtador de URL é um dos problemas mais simples que existem.

Exemplo mais complexo: upload de vídeos longos não é um `POST /video` com o binário do vídeo no corpo — isso não funciona. É preciso multipart upload, autenticação, e geralmente uma presigned URL (URL assinada). Um bom design de API demonstra que você sabe montar o sistema de verdade, não só decorar o formato REST básico.

## Etapa 4 — Esquema dos bancos de dados

É muito comum numa entrevista de system design desenhar soluções com múltiplos tipos de banco — a maioria dos grandes sistemas usa tanto SQL quanto NoSQL, cada um para a parte do problema em que é a melhor ferramenta:

- Partes mais transacionais, que exigem consistência forte, ficam num banco SQL.
- Partes que exigem mais throughput e lidam com dados menos estruturados ficam num banco NoSQL.

Às vezes existem links entre esses bancos: uma coluna de uma tabela SQL pode apontar para um endereço num banco NoSQL. Exemplo: usando um key-value store NoSQL como o DynamoDB, um campo pode apontar para uma URL no S3. Misturar diferentes bancos de dados de propósito mostra domínio sobre diferentes ferramentas e a capacidade de desenhar esquemas adequados a cada parte do problema.

## O que realmente importa: compreensão, não caixinhas

O mais importante numa entrevista de system design é a compreensão do problema — a capacidade de compreender bem um problema, propor uma solução, e saber estruturá-la. Não tem a ver com caixinhas e setinhas. Por isso a entrevista de system design não é uma entrevista de código — o código é quase um detalhe de implementação. O foco é arquitetura, infraestrutura, fluxos de dados, requisições, o que o cliente vê e não vê, e as relações entre as partes — uma visão do todo.

## Etapa 5 — Arquitetura de alto nível (High-Level Design)

Depois do esquema de dados, vem a parte que as pessoas mais associam a "entrevista de system design": o desenho da arquitetura de alto nível (HLD). É aqui que você mostra seu vocabulário: cliente, load balancer, CDN, API gateway, databases, cache, filas, workers, blob store.

É também aqui que o entrevistador pode tentar identificar se você só decorou os nomes das caixinhas ou se realmente entende e já usou essas peças. Pode ser interessante mencionar experiência real ("já usei Redis no passado para resolver esse tipo de problema como cache" ou "o WAF a gente usou o da Cloudflare, mesmo hospedando em outra cloud"). A arquitetura de alto nível também está ligada à compreensão do problema — ao que você quer entregar para o cliente e ao que quer que o sistema produza como um todo.

## Etapa 6 — Tradeoffs e escala sob pressão

Perto do fim do tempo (a entrevista dura entre 1h e 1h30, no máximo 2h), o entrevistador costuma aplicar pressão: "e se seu banco de dados cair?", "e se os usuários estiverem tendo um gargalo aqui, como você melhora?". Essa pressão leva a discutir tradeoffs e escala.

Toda escolha em computação vem com um custo — se não existissem tradeoffs, seria a mesma solução para todos os problemas. Um problema requer um tipo de solução mais adequado (não perfeito) para aquele contexto. SQL, por exemplo, é mais adequado para dados estruturados, mas um dos tradeoffs notórios é que ele pode tornar a escala de escrita mais difícil — por isso sistemas de throughput muito alto preferem NoSQL, abrindo mão das garantias ACID.

Termos recorrentes nessa fase: monolito vs. microsserviço, processos síncronos vs. assíncronos, teorema de CAP (consistência vs. disponibilidade vs. tolerância a partição de rede), identificação de possíveis *bottlenecks* (gargalos).

### Glossário PT/EN útil para entrevista em inglês

- Gargalo → *bottleneck*
- Vazão (nível de banco de dados) → *throughput*
- Problema N+1 → *N+1 problem*
- Problema da celebridade → *celebrity problem*
- Fanout

### Consistência é um tradeoff, não um absoluto

Nem tudo precisa estar consistente em todo momento. Se abrirmos mão de consistência, às vezes ganhamos escala e vazão — mas há coisas em que não dá para abrir mão: transações bancárias não podem abrir mão de consistência. Já o contador de likes de um vídeo pode: se o número real de likes é 301 mas aparece 302 para o usuário, na prática não faz diferença nenhuma. A compreensão do problema é o que define o que precisa ser preciso/consistente e o que pode aceitar uma garantia BASE em vez de ACID.

## Comunicação é o fio condutor

Acima de tudo, uma entrevista de system design — como toda entrevista — é sobre comunicação: a capacidade de expor um raciocínio claro. Ter o raciocínio na cabeça não basta se você não conseguir expor para a outra pessoa. Recomendação: estar sempre expondo o que está pensando, sua linha de raciocínio, fazendo perguntas ("faz sentido isso?", "entendi corretamente isso?"). Se você se comunica bem, é meio caminho andado.

## Fechamento

Existem vários recursos gratuitos sobre system design, tanto no canal do autor quanto em outros lugares na internet. O autor também tem um curso pago de system design (mais de um ano de produção, cobrindo banco de dados SQL/NoSQL, load balancers, API gateway, networking, preparação para entrevista e entrevistas na prática), com um mês de reembolso integral sem perguntas para quem comprar e não gostar.
