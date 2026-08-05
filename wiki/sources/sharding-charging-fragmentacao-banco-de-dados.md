---
type: source
title: "Sharding (Charging/Fragmentação) de Bancos de Dados"
aliases: ["charging de banco de dados", "fragmentação de banco de dados", "sharding na prática"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 0
tags: [system-design, sharding, banco-de-dados, shard-key, consistent-hashing, saga-pattern, ddd, escalabilidade]
skill: tech-mentor-system-design
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/sharding-charging-fragmentacao-banco-de-dados.md
source_url: ""
author: "Renato Augusto"
date_published: null
date_ingested: 2026-08-03
---

# Sharding (Charging/Fragmentação) de Bancos de Dados

## TL;DR

Vídeo de [[wiki/entities/renato-augusto]], continuação direta da playlist de System Design já mapeada em [[wiki/sources/escalabilidade-horizontal-load-balancer-algoritmos]] e [[wiki/sources/escalabilidade-vertical-horizontal-system-design]]. Percorre o caminho didático completo até o [[wiki/concepts/sharding|sharding]] de banco de dados: escalabilidade vertical → horizontal da aplicação → gargalo no banco → escalar o banco verticalmente + índices/cache/read replicas → teto físico → sharding como último recurso. Detalha a escolha da **shard key** com dois exemplos negativos analisados em profundidade (fragmentar por `created_at` gera hotspot por baixa cardinalidade e distribuição não aleatória; fragmentar `user_id` por faixas fixas gera hotspot mesmo com boa chave, por comportamento real do usuário — usuários recentes tendem a ser mais ativos), contrasta **range-based** vs. **hash-based sharding** (com exemplo passo a passo do cálculo de módulo, incluindo por que a numeração de shard começa em zero), cita **consistent hashing** como solução para o custo de resharding do hash simples, e nomeia três desafios operacionais de arquiteturas shardeadas: problema da celebridade (hotspot por entidade), cross-shard operations (resolvido com cache) e transações distribuídas (resolvido com [[wiki/concepts/saga-pattern]]). Fecha argumentando que sharding só faz sentido depois de decompor um monolito em microsserviços via [[wiki/concepts/ddd|DDD]] — tentar fragmentar um monolito inteiro com centenas de tabelas não tem uma única entidade/shard key candidata.

## Claims Principais

| Claim | Evidência | Confiança |
|---|---|---|
| Réplica de leitura (read replica) não é escalabilidade horizontal do banco — é escala de performance/leitura; a escrita continua concentrada no primário | Distinção explícita feita pelo autor ao listar as táticas anteriores ao sharding | Alta — consistente com [[wiki/concepts/read-replicas]] |
| Fragmentar por `created_at` (ou qualquer coluna cronológica) gera hotspot porque o acesso real do sistema (feed de rede social) concentra tráfego nos dados mais recentes — a chave tem baixa afinidade de relacionamento, baixa cardinalidade (poucos valores exclusivos, ex. 25 anos possíveis) e distribuição não aleatória | Exemplo construído passo a passo com contagem de anos como cardinalidade | Alta — consistente com a advertência contra range-based sharding para acesso não uniforme em [[wiki/concepts/db-sharding]] |
| Uma shard key pode atender aos três critérios formais (alta afinidade, alta cardinalidade) e ainda assim gerar hotspot, se o **padrão de distribuição** escolhido (faixas fixas de `user_id`) não for aleatório — o autor separa explicitamente "boa chave" de "boa distribuição" | Exemplo com 2.500.000 usuários divididos em 3 bancos por faixa fixa; banco com a faixa mais recente de IDs sofre mais mesmo tendo menos usuários, por comportamento real (usuários recentes tendem a ser mais ativos) | Alta — nuance de campo não coberta explicitamente antes na wiki; complementa a tabela de trade-offs de [[wiki/concepts/sharding]] |
| Numeração de shard começa em zero por convenção de módulo: com N shards, o resto de `chave % N` nunca pode ser N, então os índices válidos são 0 a N-1 | Explicação matemática direta (módulo = resto de divisão) | Alta — fato matemático, não interpretação |
| Geração de ID para inserção em sistema shardeado não deve usar auto-incremento do banco (gera race condition em ambiente distribuído) — requer gerador de ID exclusivo/distribuído (cita Snowflake do Twitter e uma implementação própria via Redis de vídeo anterior sobre encurtador de URL) | Explicação do fluxo de inserção: gerar ID → aplicar hash/módulo para decidir o shard → só então inserir | Alta — consistente com o problema geral de geração de ID em sistemas distribuídos já documentado indiretamente via [[wiki/concepts/control-plane]] |
| Consistent hashing resolve o custo de resharding do hash simples movendo apenas uma fração dos dados ao adicionar/remover shard, ao invés de todos os dados (que é o que acontece quando o número de shards muda o valor do módulo) | Explicação do anel virtual, citada como mecanismo por trás de bancos não relacionais com sharding nativo | Alta — consistente com [[wiki/concepts/db-sharding]], que já cita consistent hashing como solução ao mesmo problema |
| "Problema da celebridade": uma única entidade com alcance desproporcional pode sobrecarregar sozinha o shard em que caiu; soluções citadas são distribuição manual dos dados dessa entidade entre shards, ou um shard dedicado (possivelmente escalado verticalmente) só para ela | Exemplo hipotético de usuário com alcance monstruoso numa rede social | Média-alta — é um padrão conhecido de hotspot por chave específica (analogia com "hot key" em sistemas de cache/particionamento), mas o vídeo não cita nome formal nem fonte externa para o termo "problema da celebridade" |
| Cross-shard operations (ex.: "10 posts mais populares" exigindo fan-out para todos os shards) devem ser resolvidas com uma camada de cache, evitando repetir o fan-out a cada requisição | Explicação de cache com TTL aplicado ao resultado agregado | Alta — consistente com [[wiki/concepts/cache]] e com o padrão scatter-gather citado em [[wiki/concepts/db-sharding]] |
| Transações que cruzam shards (ex.: transferência financeira entre usuários em shards diferentes) não podem ser atômicas como uma transação local; a solução recomendada é o [[wiki/concepts/saga-pattern|Saga pattern]] com transações compensatórias | Exemplo de Pix falhando entre débito e crédito em shards diferentes | Alta — consistente com [[wiki/concepts/saga-pattern]] já documentado |
| Tabelas sem relação direta com a shard key escolhida (ex.: fornecedor de medicamento num sistema hospitalar cuja shard key é paciente) devem ir para um **shard global** ou ser **replicadas** em todos os shards via mensageria, contornando o roteador de hash | Exemplo do domínio hospitalar (paciente como entidade central, prontuário, médico, medicamento) | Alta — primeira vez que a wiki documenta esse mecanismo específico (shard global / replicação de tabelas sem FK à shard key) |
| Sharding só faz sentido depois de decompor um monolito grande em microsserviços via DDD — tentar fragmentar um monolito com centenas de tabelas resulta em fragmentar poucas tabelas centrais e replicar dezenas de outras em todo shard, o que não compensa | Argumento de fechamento, ligando sharding, DDD e arquitetura de microsserviços | Alta — reforça diretamente a tese central já documentada em [[wiki/concepts/microsservicos]] (decomposição por bounded context antes de qualquer escala de infraestrutura) |

## Conceitos Abordados

- [[wiki/concepts/sharding]]
- [[wiki/concepts/db-sharding]]
- [[wiki/concepts/consistent-hashing]]
- [[wiki/concepts/saga-pattern]]
- [[wiki/concepts/escalabilidade-horizontal]]
- [[wiki/concepts/escalabilidade-vertical]]
- [[wiki/concepts/read-replicas]]
- [[wiki/concepts/ddd]]
- [[wiki/concepts/microsservicos]]
- [[wiki/concepts/cache]]

## Entidades Abordadas

- [[wiki/entities/renato-augusto]]

## Observações / Contradições

Nenhuma contradição com o que já está registrado na wiki. Esta fonte é uma continuação explícita da playlist de System Design de [[wiki/entities/renato-augusto]] já parcialmente mapeada em [[wiki/sources/escalabilidade-horizontal-load-balancer-algoritmos]] — o próprio vídeo recapitula escalabilidade vertical/horizontal antes de introduzir sharding, reforçando a ordem de escalonamento já documentada em [[wiki/concepts/escalabilidade-vertical]] e [[wiki/concepts/escalabilidade-horizontal]].

Ponto novo mais concreto para a wiki: a distinção entre "boa shard key" e "boa distribuição" (exemplo de `user_id` particionado por faixa fixa) — [[wiki/concepts/sharding]] e [[wiki/concepts/db-sharding]] já documentavam os critérios formais de shard key (cardinalidade, afinidade, distribuição uniforme), mas não tinham um exemplo explícito mostrando que uma chave "correta" nos três critérios ainda pode falhar se o *método* de fragmentação (range fixo vs. hash) não for aleatório. Também novo: o mecanismo do "shard global"/replicação de tabelas sem FK à shard key, e o "problema da celebridade" como nome informal para hotspot por entidade específica — nenhum dos dois tinha página ou seção própria antes desta ingestão.

## Perguntas Abertas

- O termo "problema da celebridade" não é atribuído a nenhuma fonte formal externa pelo autor — vale investigar se corresponde a um termo mais estabelecido na literatura de sistemas distribuídos (ex.: "hot key problem", citado em contextos de particionamento do Redis Cluster e do Cassandra).
- A fonte não detalha a implementação do "gerador de ID exclusivo" além de citar Snowflake e uma menção a vídeo anterior (encurtador de URL) não presente nesta wiki — fica em aberto se esse vídeo já foi ou será ingerido separadamente.
