# Sharding (Charging/Fragmentação) de Bancos de Dados

Transcrição de vídeo, limpa de erros de reconhecimento de fala e formatada em Markdown. Conteúdo já em português — nenhuma tradução necessária.

Dando continuidade na playlist de System Design, arquitetura de software e sistemas distribuídos, o vídeo de hoje ensina a escalar horizontalmente os bancos de dados através da técnica conhecida como **sharding** (também chamada de "charging" na fala, e de fragmentação). Além da técnica em si, o vídeo mostra como esse tipo de desafio aparece em entrevistas para programador ou arquiteto de software, e como raciocinar diante desse tipo de problema.

Fala pessoal, Renato Augusto aqui de novo, e dessa vez para ensinar a técnica de sharding, também conhecida como fragmentação dos bancos de dados. Essa técnica tem como intuito principal escalar horizontalmente os bancos de dados, e é ela quem vai definir se a aplicação vai conseguir suportar milhares ou até milhões de usuários.

## Partindo de uma arquitetura básica

A primeira coisa é pegar uma arquitetura bem básica — cliente/servidor, com usuários fazendo requisições para o servidor web, e o servidor web conversando com um banco de dados — e escalar essa arquitetura a partir do zero, até chegar no problema que o sharding resolve: escalabilidade horizontal do banco de dados.

Simulação: uma empresa começa a fazer marketing agressivo, o número de usuários aumenta, e isso gera gargalo tanto na aplicação quanto no banco de dados — muitos acessos simultâneos consomem recurso e a aplicação não aguenta a volumetria.

Primeira solução recomendada para esse tipo de problema, seja em entrevista ou na vida real: **escalabilidade vertical** — adicionar mais poder computacional (memória RAM, processamento) na instância. Quando a aplicação é crítica, de milhares ou milhões de usuários, parte-se para **escalabilidade horizontal**: criar réplicas do servidor e colocar um load balancer na ponta, que recebe todas as requisições e distribui a carga entre as réplicas.

### O gargalo que sobra: o banco de dados

Com várias réplicas da aplicação apontando para um único banco de dados, é o banco que passa a sofrer com toda a volumetria de requisições — ele trava, a aplicação cai e demora para responder, e a empresa começa a perder clientes. Isso é chamado de "dor do crescimento": todo software em ascensão, com novos usuários chegando, vai passar por isso.

### Escalando o banco antes de fragmentar

Antes de partir para sharding, a primeira tática é escalar o banco **verticalmente** — mais RAM, mais armazenamento. Combinado com isso, aplicar o básico:

- Índices no banco de dados
- Estratégia de cache (cache-aside pattern)
- Otimização de queries
- Réplicas de leitura (read replicas)

Importante: réplica **não é** escalabilidade horizontal do banco — é escala de performance/leitura. O banco principal (réplica primária) fica com a escrita, e as réplicas de leitura recebem as leituras; as instâncias da aplicação leem de um lado e escrevem do outro. Isso tem desafios próprios de consistência de dados.

### O teto físico

Mesmo somando escalabilidade vertical + índices + cache + queries otimizadas + read replicas, existe um teto: memória, armazenamento e poder de processamento não são infinitos. Quando se esgotam todas essas possibilidades, é hora de escalar horizontalmente o banco de dados através da técnica de **sharding**.

## O que é sharding

Sharding (o nome em inglês) é o mesmo que "charging" ou fragmentação — imagine uma pizza grande fatiada em vários pedaços. É a técnica de scale-out, a escalabilidade horizontal do banco de dados.

Um banco de dados tem várias tabelas — por exemplo, uma tabela de usuários. Ao fazer sharding desse banco, cada **fragmento (shard)** passa a ter um pedaço dos dados; nenhum shard armazena todos os dados.

Ponto importante: cada shard é um banco de verdade — tem seu próprio endereço de conexão, sua própria memória RAM, processador e armazenamento. São bancos separados, em hospedagens separadas. Isso é o nível mais alto de complexidade em bancos de dados: **distribuição de dados**.

A nova arquitetura fica assim: usuários → load balancer → réplicas da aplicação → vários shards (o antigo banco único, agora fragmentado).

## Shard key (chave de fragmentação)

A primeira coisa a definir ao fragmentar algo — e isso deve ser mencionado em entrevista — é a **shard key**: a chave de fragmentação. Ela é escolhida a partir da entidade/tabela mais importante do sistema. Em geral escolhe-se **uma única** shard key para o sistema todo.

A shard key é a coluna que serve de ponto de roteamento tanto para inserir quanto para recuperar dados, e para distribuir os dados entre os fragmentos.

### Exemplo: rede social

Numa mini rede social há tabelas de usuários, posts e comentários. O usuário é a entidade mais importante (assim como paciente é a entidade mais importante num sistema hospitalar, e pedido costuma ser a mais importante num e-commerce).

Exemplo: Lúcia (id 1) cria um post (id 566, com `user_id` = 1 como FK) e um comentário (com o `user_id` dela e o id do post comentado). Se, ao fragmentar, Lúcia caiu no shard 2, não faz sentido que o post dela vá para o shard 1 e o comentário para o shard 3 — porque isso obrigaria a aplicação a consultar múltiplos bancos, trazer tudo para a memória e juntar os dados, quebrando a proposta do sharding. O correto é que o post e os comentários de Lúcia sigam para o mesmo shard que ela.

### Características de uma boa shard key

- **Alta afinidade de relacionamento**: a chave é PK em uma tabela e FK em várias outras (alto poder de relacionamento).
- **Alta cardinalidade**: grande variedade de valores exclusivos.
- **Distribuição uniforme e aleatória** dos valores (a palavra "aleatória" é essencial).

Não precisa necessariamente ser um ID — pode ser qualquer coluna de qualquer tabela.

## Exemplo de shard key ruim: `created_at`

Fragmentar por `created_at` (data de criação) parece intuitivo — postagens de 2023 num shard, 2024 em outro, 2025 em outro — mas cria um **hotspot**: o shard mais recente concentra todo o tráfego, porque o feed de uma rede social mostra majoritariamente as postagens mais recentes.

Essa chave falha nos três critérios: baixa afinidade de relacionamento, baixa cardinalidade (poucos valores exclusivos — ex.: só 25 anos possíveis) e distribuição não aleatória (organizada por ordem cronológica).

## Exemplo de shard key boa, mas distribuição ruim: intervalos de `user_id`

Cenário: 2.500.000 usuários. Se a distribuição for feita por faixas fixas (0–1M no banco 1, 1M–2M no banco 2, 2M–2.5M no banco 3), o banco 3 é o que sofre mais, mesmo tendo só 500 mil usuários — porque, na maioria dos sistemas reais, os usuários mais recentes tendem a ser os mais ativos (os antigos podem já ter abandonado a plataforma). Aqui a chave (`user_id`) é boa (alta afinidade, alta cardinalidade), mas o **padrão de distribuição** é ruim.

Esse padrão de distribuição é chamado de **range-based sharding** (fragmentação baseada em intervalo). Não é de todo ruim, mas é raramente o padrão de mercado recomendado.

## Hash-based sharding

O padrão de mercado, mais simples e mais utilizado. Responde à pergunta "como a aplicação sabe onde está um dado".

Mecânica: pega-se a shard key e calcula-se o **módulo** (resto da divisão) pelo número de shards.

Exemplo com 3 shards: `user_id = 10` → `10 % 3 = 1` (resto 1) → o dado está/vai para o shard 1. `user_id = 30` → `30 % 3 = 0` → shard 0.

Numeração dos shards começa em **zero** (primeiro número positivo na computação), então com 3 shards os índices válidos são 0, 1 e 2 — nunca 3, pois o resto de uma divisão por 3 nunca é 3.

Quando não há uma coluna numérica inteira disponível (ex.: UUID), gera-se um **hash numérico não criptográfico** do valor, e aplica-se o módulo sobre esse hash. Requisito crítico: a função de hash tem que ser **determinística** — a mesma entrada sempre produz a mesma saída — senão o roteador aponta para o shard errado tanto na inserção quanto na recuperação do dado.

### Geração de ID em sistema distribuído

Ao criar um novo registro, não se usa auto-incremento do banco — isso geraria conflito/race condition em sistema distribuído. É necessário um **gerador de ID exclusivo/distribuído** (ex.: Snowflake do Twitter, ou uma implementação própria usando Redis — tema de vídeo anterior sobre encurtador de URL). O ID gerado é então passado pela função de hash/módulo para decidir o shard de destino antes da inserção.

### Limitação do hash simples: resharding

Se o número de shards muda (ex.: de 3 para 5), o cálculo do módulo muda, e o roteador passa a apontar para o shard errado para dados já existentes — exigindo **rebalanceamento**: redistribuir todos os dados entre os bancos, um trabalho custoso.

### Consistent hashing

Solução para esse problema: cria um anel virtual, distribui as chaves/shards nesse anel, e adicionar ou remover um shard exige mover apenas uma fração dos dados (não todos). É assim que bancos não relacionais com sharding nativo funcionam por baixo dos panos. Implementar isso manualmente é complexo — às vezes compensa mais migrar para um banco que já tem essa capacidade nativa.

## Desafios de arquiteturas com sharding

### 1. Problema da celebridade (hotspot por entidade)

Se um usuário com alcance monstruoso (exemplo dado: um jogador de futebol muito famoso) se cadastra e cai num shard específico, o volume de interações nas publicações dele pode sobrecarregar esse shard sozinho.

Soluções possíveis: distribuir manualmente os dados dessa entidade entre vários shards (trabalhoso), ou criar um **shard dedicado** só para essa celebridade (ou um grupo de celebridades), podendo inclusive escalar esse shard verticalmente com mais poder computacional.

### 2. Cross-shard operations

Uma query aparentemente simples (ex.: "10 posts mais populares" para a home) pode exigir consultar todos os shards, trazer os resultados para a memória, agregar e então responder — gerando latência alta.

Solução recomendada: camada de **cache**. Na primeira solicitação, faz-se a consulta cara em todos os shards e armazena-se o resultado em cache (com TTL, ex.: 5-10 minutos ou até 24h dependendo da regra de negócio); solicitações seguintes são servidas pelo cache, não pelo banco.

### 3. Transações distribuídas

Exemplo financeiro: transferir R$ 50 do usuário 1 para o usuário 2, quando os dois usuários estão em shards diferentes. Não é possível fazer uma transação atômica cobrindo os dois bancos como se fossem um só. Se o débito no shard do usuário 1 for concluído e, antes do crédito no shard do usuário 2, o sistema falhar, o dinheiro "desaparece" — o usuário 1 fica com saldo negativo e o usuário 2 nunca recebe o valor.

Solução mais recomendada: **Saga pattern** — sequência de transações locais que, em caso de falha em qualquer etapa, são desfeitas através de operações compensatórias nas etapas anteriores já concluídas.

## Tabelas sem relação direta com a shard key

Nem toda tabela tem relacionamento direto com a entidade escolhida como shard key. Exemplo hospitalar: paciente é a entidade principal (prontuário, médico, medicamento, doença estão todos ligados a ele), mas uma tabela como "fornecedor de medicamento" não tem FK para paciente. Da mesma forma, a tabela de médicos não tem FK direta para paciente (a relação passa pelo prontuário).

Abordagens possíveis:

- Criar um **shard global**, com as tabelas comuns/sem relacionamento direto com a shard key escolhida.
- **Replicar** essas tabelas em todos os shards (ex.: via mensageria/replicação de dados), para evitar consultas cross-shard. Essas tabelas não passam pelo roteador de hash — vão direto para qualquer shard, e ficam sincronizadas por replicação.

## Sharding, DDD e microsserviços

Não faz sentido tentar fazer sharding de um monolito gigantesco com centenas de tabelas — o resultado seria fragmentar poucas tabelas e replicar dezenas de outras em todos os bancos, o que não faz sentido.

Antes de pensar em sharding num cenário desses, é necessário pensar em **arquitetura de microsserviços**, e para isso é fundamental o **Domain-Driven Design (DDD)** — ele orienta como quebrar um monolito em pedaços menores que fazem sentido para o negócio (bounded contexts). A partir dos microsserviços resultantes, aí sim faz sentido aplicar sharding no banco de dados de um microsserviço específico. Não faz sentido tentar identificar uma única entidade principal e uma única shard key para um sistema inteiro com milhões de regras de negócio ainda não decomposto.

## Fechamento

O vídeo encerra convidando para curtir, se inscrever e comentar dúvidas, mencionando também o produto "Mapa do Arquiteto" (guia de carreira do zero até arquiteto de software/soluções, com roadmap de estudos).
