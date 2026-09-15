# Por Dentro da Arquitetura do Nubank: Como Escalar para 122 Milhões de Clientes

> Transcrição (com pequenas correções de ASR) de vídeo do YouTube sobre a arquitetura técnica do Nubank.
> Canal/autor: não identificado no áudio.
> Idioma original: português (Brasil) — nenhuma tradução necessária.
> Data de visualização: ~2026

---

## Abertura — O Problema de Escala

Imagina que são 8 horas da manhã de uma segunda-feira, você tá saindo para pegar um metrô em São Paulo e, chegando lá, encontra tudo entupido de gente, como sempre — muita gente com o celular na mão, acessando o aplicativo do banco, seja para conferir o saldo, pagar um café ou transferir dinheiro. Agora multiplica isso por **122 milhões de clientes** espalhados pelo Brasil, México e Colômbia, **72 bilhões de eventos por dia** passando pela infraestrutura, e **4.000 microsserviços** rodando simultaneamente. E se qualquer coisa der errado, ou você só tiver uma conexão lenta com o aplicativo, já fica indignado.

Mas como que o Nubank faz isso funcionar? Neste vídeo, uma visão por dentro da arquitetura de um dos maiores bancos digitais do mundo — não é teoria, são decisões reais que o Nubank documentou publicamente.

## O Tamanho do Problema

Para entender a arquitetura, primeiro é preciso entender o tamanho do problema. O Nubank começou em 2013 com um único produto — um cartão de crédito —, um time reduzido e poucas linhas de código. Com base em dados de 2025, o Nubank possui:

- Mais de **122 milhões de clientes**
- **20 shards** só no Brasil
- Mais de **4.000 microsserviços**
- **72 bilhões de eventos Kafka por dia**
- **600 TB de logs** ingeridos diariamente
- Milhões de requisições por segundo

Ponto crucial: quando você cresce nessa velocidade, uma arquitetura que suporta 1 milhão de clientes provavelmente vai quebrar com 10 milhões. E o que funciona com 10 milhões vai colapsar com 100 milhões. O Nubank precisou reinventar a arquitetura várias vezes ao longo dos anos, e as decisões tomadas no início — algumas consideradas arriscadas na época — foram o que permitiu essa escala.

## Decisão 1 — A Linguagem de Programação: Clojure

Em 2013, quando todo mundo usava Java, Python ou Ruby, o Nubank escolheu uma linguagem muito diferente: **Clojure**. Clojure é uma linguagem funcional que roda na JVM; na época, quase ninguém usava para sistemas em produção — era considerada acadêmica. Mas o CTO Edward Wible viu algo que outros não viram: a **imutabilidade**.

Em programação funcional, os dados são imutáveis — uma vez criados, não mudam. Para modificar algo, você cria uma nova versão. Por que isso importa num banco? Imagine dois processos tentando atualizar o saldo de uma conta ao mesmo tempo: com dados mutáveis, você tem race conditions, inconsistência, bugs que aparecem do nada. Com dados imutáveis, cada transação cria uma nova versão do estado — não existe sobrescrever, só existe adicionar.

## Decisão 2 — O Banco de Dados: Datomic

Essa decisão conecta diretamente com a segunda grande escolha: o Nubank não usa SQL tradicional nem Postgres no core — usa **Datomic**. Datomic é um banco de dados também imutável — pensa nele como "um Git para o seu banco de dados". No modelo tradicional, quando você atualiza um registro, o valor antigo desaparece (é sobrescrito). No Datomic, cada mudança é um **fato novo** adicionado a uma timeline — o histórico completo fica preservado.

Se um cliente liga reclamando de uma cobrança de seis meses atrás, o Nubank consegue ver exatamente como o sistema estava naquele momento. Não é um backup — é o estado real, navegável no tempo. Uma citação atribuída a Edward Wible, publicada no site do Nubank:

> "Eu não encontrei uma opção melhor que o Datomic, com esse conceito de tempo como cidadão de primeira classe. Para mim, isso faz toda a diferença."

O Nubank acreditou tanto no Datomic que, em 2020, comprou a empresa que desenvolve o banco de dados.

A arquitetura do Datomic é separada em leitura e escrita: um **transactor** processa todas as escritas, e múltiplos **peers** fazem a leitura, escalando horizontalmente. O storage por trás pode ser DynamoDB, um banco relacional, ou qualquer outro backend de armazenamento. Isso resolve um problema clássico: escrita que precisa de consistência e leitura que precisa de performance — o Datomic entrega os dois.

## Decisão 3 — Kafka como Sistema Nervoso

Se o Datomic é o cérebro, o Kafka pode ser considerado o sistema nervoso. O Nubank processa **72 bilhões de eventos por dia** através do Kafka. Toda ação no sistema gera eventos: cliente abriu o app, cliente consultou saldo, transação foi aprovada, pagamento foi processado.

Eles usam um padrão chamado **Event Sourcing**: em vez de guardar só o estado atual, você guarda todos os eventos que levaram àquele estado. Pensa no seu extrato bancário: você não vê só o saldo de R$ 1.000 — você vê cada depósito, cada saque, cada transferência. O saldo é o resultado de aplicar todos esses eventos em sequência.

O Kafka funciona como um log imutável e distribuído — as mensagens ficam lá por dias ou semanas, permitindo que diferentes serviços processem no próprio ritmo. Uma citação atribuída à InfoQ:

> "Nós modelamos tudo no banco como stream processing. Até batch jobs são distribuídos como streams de mensagens no Kafka."

Isso permite um desacoplamento radical: o serviço que aprova a transação não precisa saber que existe um serviço de notificação push — ambos consomem do mesmo tópico Kafka de forma independente.

## Decisão 4 — Sharding via Scalability Units

Em 2016, o Nubank enfrentou um problema raro: **a AWS ficou sem máquinas**. Uma citação do site do Nubank:

> "Melhorias de escalabilidade como sharding funcionaram bem por um tempo, mas eventualmente bateram em limites físicos — incluindo a AWS ficando sem máquinas para acompanhar o ritmo de crescimento do Nubank."

A maioria das empresas resolve escala com sharding de banco de dados: você divide os dados em múltiplos bancos. Mas o Nubank percebeu que isso resolve só o problema do banco de dados — e se o gargalo estiver em outro lugar? No Kafka, no batch job, na rede?

A solução foi mais radical: um esquema de **Scalability Units** — clonar a infraestrutura inteira. Cada shard do Nubank não é só uma partição do banco de dados; é uma **cópia completa de toda a infraestrutura**: todos os microsserviços, clusters Kafka dedicados, bancos Datomic separados, redes isoladas. Hoje, no Brasil, são **20 shards**. Cada shard é responsável por um grupo de clientes; quando você faz login no app, o sistema sabe em qual shard você está e roteia todas as suas requisições para lá.

Por que isso é bom:

- **Isolamento de falhas** — se um shard cai, só uma fração dos clientes é afetada
- **Previsão de escala** — sabem exatamente quanto cada shard aguenta de requisições
- **Deploys seguros** — dá para testar uma implantação em um shard antes de ir para todos

## Decisão 5 — Autorização de Transação em Menos de 100ms

O momento mais crítico do sistema é a autorização de transação. Quando você passa o cartão do Nubank numa maquininha, acontece uma corrida contra o tempo: a maquininha envia para o adquirente, o adquirente envia para a Mastercard ou Visa, a bandeira envia para o Nubank, e o Nubank tem que responder "aprovado" ou "negado". Tudo isso precisa acontecer em **menos de 100ms** — demorar mais, a transação falha.

O sistema de autorização precisa verificar se o cartão é válido, checar o limite disponível, rodar análise de fraude, registrar a transação e retornar a resposta. Recentemente, o time de engenharia conseguiu reduzir a latência crítica de ~10.000ms para **288ms no P90** — uma redução de 76%.

Como? Removendo dependências síncronas do caminho crítico. Em vez de buscar dados em tempo real, eles **precomputam e materializam** as informações necessárias. Hoje, a maioria das requisições é atendida com um único lookup em um datastore de baixa latência — os cálculos pesados acontecem no momento da **escrita**, não da **leitura**.

## Decisão 6 — Observabilidade In-House: Alexandria

Com 4.000 microsserviços, é preciso saber o que está acontecendo. O Nubank gera **600 TB de logs por dia**; os engenheiros rodam **15.000 queries por dia**, escaneando 150 PB de dados (aproximado, conforme relatado). No início, usavam uma solução de terceiros para logs, mas com o crescimento ficou inviável — há até uma citação no site do Nubank:

> "Chegamos a um ponto em que poderíamos contratar o Lionel Messi como engenheiro de software pagando o mesmo valor que pagávamos pela solução externa."

Então construíram a própria plataforma, chamada **Alexandria**. A arquitetura da Alexandria tem quatro componentes:

1. **Ingestão** — microbatch via Kafka
2. **Processamento** — filtros e agregações customizados
3. **Storage** — em S3, em formato colunar, com 95% de compressão
4. **Query engine** — distribuída

O resultado: 50% mais barato que a solução anterior, com controle total sobre os dados. Isso se integra com os três pilares clássicos de observabilidade: métricas, logs e traces.

## Decisão 7 — Plataforma Antifraude

Todo esse sistema precisa ser protegido. A plataforma de defesa do Nubank processa **450 milhões de eventos por dia**. A arquitetura é dividida em:

- **Detecção** — regras manuais mais modelos de machine learning
- **Ação** — bloquear, alertar ou deixar passar

Um detalhe inteligente: se uma regra simples já consegue classificar a transação como suspeita, o modelo de machine learning **nem roda** — economizando tempo e recurso. Recentemente, refatoraram o orquestrador para um modelo baseado em **DAG** (grafo acíclico dirigido): cada componente espera apenas pelos dados de que precisa, e nada mais. Resultado: a latência caiu de **550ms para 350ms** em fluxos complexos.

## Recapitulação

O que faz o Nubank funcionar em escala:

1. **Clojure e imutabilidade** — dados que não mudam eliminam classes inteiras de bugs em sistemas concorrentes
2. **Datomic** — banco de dados onde o tempo é cidadão de primeira classe; histórico completo, auditável e navegável
3. **Kafka e Event Sourcing** — 72 bilhões de eventos por dia fluindo pelo sistema
4. **Scalability Units** — em vez de particionar só o banco, clonam a infraestrutura inteira; 20 shards no Brasil
5. **Read path otimizado** — pré-computar no momento da escrita para ter leituras em milissegundos
6. **Observabilidade in-house (Alexandria)** — construída internamente quando a conta com fornecedor terceiro ficou proibitiva
