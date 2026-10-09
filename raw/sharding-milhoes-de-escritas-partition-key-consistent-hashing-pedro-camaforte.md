# Sharding: como Instagram, Discord e Notion aguentam milhões de escritas por segundo

Transcrição de vídeo de Pedro Camaforte (canal de system design/entrevistas), limpa de erros de reconhecimento de fala e formatada em Markdown. Conteúdo já em português — nenhuma tradução necessária. Correções de ASR: "charging/chard/charde" → sharding/shard; "inscritas" → escritas; "to PC" → 2PC; "Cila DB" → ScyllaDB; "partid jonk" → partition key; "cash" → cache; "ParaGB/PostGs/Pegris" → PostgreSQL.

## Abertura

Será que o banco de dados favorito, aquele clássico de sempre, aguenta mais de 100.000 escritas por segundo? Como gigantes como Instagram, Discord e Notion aguentam milhões de escritas por segundo? O vídeo trata da estratégia de **sharding**: todos os pormenores, estratégias, principais desafios e como implementar corretamente. É a continuação do vídeo "como escalar escritas", onde sharding foi citado entre várias estratégias, mas era complexo e amplo demais e ganhou vídeo dedicado. Ao final: como decidir em entrevista se vale ou não implementar sharding e como responder às perguntas que o entrevistador pode fazer.

## Quando sharding passa a ser necessário

Cliente chamando servidor, que escreve num PostgreSQL.

- **10.000 escritas/s:** PostgreSQL bem configurado numa máquina OK aguenta tranquilamente (visto no vídeo de escalar escritas).
- **25.000 escritas/s:** o banco começa a "chorar": queries ficam lentas, backups que levavam minutos passam a levar horas.
- **Solução: escala vertical** — máquina super potente na AWS, tunada, paga-se uma fortuna e chega-se a ~50.000 escritas/s. Honestamente, é muito difícil uma empresa passar desse número: é por segundo, exige volume muito alto.
- **100.000 escritas/s** (aplicação global, usuários nos EUA, Brasil, Europa): nem a instância mais forte da AWS aguenta.

Se um banco só não aguenta, divide-se em múltiplos bancos: isso é **sharding** — pegar um banco único e dividi-lo em 1, 2, 3… quantos shards forem necessários. É **escala horizontal**, enquanto aumentar a potência da máquina é **escala vertical**. A vertical tem limite (não dá para pagar US$ 50.000/mês e receber recurso infinito; o hardware tem teto). A horizontal escala "infinitamente" (fica mais cara, mas cresce conforme a necessidade).

Exemplo: se cada shard aguenta ~25.000 escritas/s, 4 shards atendem 100.000/s.

Perguntas que o sharding traz: qual estratégia usar? Como o servidor sabe para qual banco mandar cada query? Como busca os dados de cada shard? E se precisar rebalancear (4 ou 5 shards não bastam)? Como fazer sem desbalancear o volume?

## Passo 1: Partition key

Em entrevista, a primeira coisa a deixar explícita é **qual é a partition key**: a coluna que comanda a distribuição dos dados entre os shards. Uma boa partition key tem três propriedades:

1. **Alta cardinalidade** — valores praticamente infinitos/muito grandes, para poder distribuir em vários shards. Contra-exemplo: `is_premium` (booleano) → só dois shards possíveis. Um ID é boa escolha.
2. **Distribuição equilibrada** — contra-exemplo: país como chave; o shard do Vaticano seria muito menor que o do Brasil.
3. **Alinhada às queries** do produto.

Uma partition key ruim é o oposto de tudo isso.

### Exemplos bons

- **Rede social (Instagram):** `user_id`. Queries típicas: "posts desse usuário", "configurações", "histórico" → alta cardinalidade, distribuição igual, queries alinhadas.
- **E-commerce:** `order_id`. Tudo gira em torno do pedido (atraso, produtos, método de pagamento). Todos os dados relacionados a uma order vivem juntos no mesmo shard — a partition key garante que dados relacionados a ela estejam juntos.

### Exemplos ruins

- **App de finanças com `plano` (free/assinante):** baixa cardinalidade (2 shards) e distribuição desigual (a maioria é free).
- **App de eventos/shows por `data do evento`:** shard 2024, 2025, 2026… A maioria das pessoas pesquisa eventos do ano atual (2026), então o shard mais recente superaquece e os outros quase não recebem acesso. A data sozinha como partition key não é boa.

Conclusão: em entrevista, pense no que o produto pede, como montaria as queries, e escolha a partition key com base nelas.

## Passo 2: Estratégia de distribuição

### Range-based

Divide por faixas. Exemplo do vídeo anterior: pela inicial do nome (A–I, J–R, S–Z) — foi só ilustração, pois:
- há limite de letras (acaba o alfabeto);
- há muito mais nomes começando com A do que com X ou Z.

Alternativa: faixa de ID (0–1M no shard 1, 1M–2M no shard 2…). Escala "infinitamente", mas:
- no começo todos ficam no shard 1 e os outros ficam vazios — se levar 10 anos para chegar a 1 milhão de usuários, a complexidade do sharding não se justifica;
- estatisticamente os **usuários mais recentes são os mais ativos**: se demorou 8 anos para chegar a 3 milhões, os usuários entre 2M e 3M são os mais ativos, e o shard 3 superaquece (**hot shard**) enquanto os shards 1 e 2 ficam subutilizados.

### Directory-based

Uma tabela auxiliar (shard map) diz em que shard cada usuário está (ex.: usuário 7 → shard 2; 76 → shard 1; 22 → shard 5). O servidor consulta o diretório e só então vai ao shard.

- ✅ Flexibilidade: é fácil realocar um usuário de carga muito alta para um shard mais vazio.
- ❌ **Ponto único de falha:** se o diretório cair, a aplicação não sabe acessar os outros shards.
- ❌ **Overhead dobrado:** duas chamadas a bancos por operação; 100.000 chamadas/s viram 200.000. Não escala.

Tem seu caso de uso (ver hot spots, abaixo).

### Hash-based (padrão de mercado)

Aplica-se um hash à partition key (ex.: `user_id`); o hash é determinístico (mesma entrada → mesmo valor). Qualquer algoritmo serve, de preferência rápido. Depois, **módulo pelo total de shards** define o destino (índices de 0 a N-1). Como o hash produz valores pseudo-aleatórios, a distribuição é uniforme, independente do nome do usuário ou de quando entrou. Para adicionar shards, aumenta-se o N do módulo. Sem hot shards por distribuição.

**Problema:** ao passar de 3 para 4 shards, `hash % 3` vs `hash % 4` mudam o destino de quase todas as chaves (ex.: um valor que caía no shard 1 passa a cair em outro) → seria preciso remanejar os dados de todos os shards. Não há solução perfeita; engenharia é escolher o menor trade-off.

### Consistent hashing

Usado por baixo dos panos por bancos como Cassandra e ScyllaDB. Imagina-se um **círculo** com espaço de hash gigantesco (no exemplo, 0 a 99). Os shards são posicionados em pontos do círculo (shard 1 em 0, shard 2 em 33, shard 3 em 66). Ao fazer o hash da chave, localiza-se o ponto no círculo e anda-se no **sentido horário** até o shard mais próximo (chave 20 → shard 2; chave 34 → shard 3).

Vantagem: ao adicionar um shard (ex.: shard 4 na posição 82), só migram os dados da faixa entre 66 e 82 (que antes iam para o shard 1) para o shard 4. Os shards 2 e 3 ficam quietos. Não é perfeito, mas o impacto do rebalanceamento é muito menor.

**Virtual nodes:** na prática cada shard ocupa múltiplos pontos do círculo, para que o novo shard receba um pouco de dados de cada shard existente, em vez de tirar metade de um só e deixar uns cheios e outros pela metade. (O autor pode fazer vídeo dedicado.)

**Padrão em entrevista:** sharding **hash-based com consistent hashing**.

## Desafios do sharding (perguntas comuns de entrevista)

### 1. Hot spots

Mesmo com a partition key perfeita e hash + consistent hashing, pode haver hotspot: Neymar, Cristiano Ronaldo e Messi caírem no mesmo shard, com milhões de interações em stories/fotos/reels (**problema das celebridades**), ou um **post viral** (centenas de milhões de views/likes/comentários). Duas soluções, com trade-offs:

1. **Shard dedicado** para a celebridade (com hardware mais forte), migrando-a para lá. Os outros usuários do shard original não são afetados. Aqui o **directory-based** se encaixa: consulta-se o diretório para saber se é celebridade e redireciona-se ao shard específico. Trade-offs do directory-based valem.
2. **Partition key composta:** subdividir o shard grande usando hash de `ID + N` (N = número ou data/semana). Ex.: dados de uma semana num shard, na semana seguinte no próximo; ou `ID_usuário + 1`, `+2`, `+3`… Trade-off: para buscar todos os posts da pessoa é preciso consultar shard por shard. Mitigação: **camada de cache** para as leituras. Requer algoritmo para identificar os sub-shards.

### 2. Queries cross-shard

A partition key é escolhida para que a query caia num único shard, mas há casos inevitáveis, como "top 10 posts mais populares da plataforma": consulta o top 10 de cada shard (pode ser 20 shards), agrega e extrai o top 10 real. Isso deve ser **exceção, não regra** — se acontece demais, a partition key está errada ou sharding não é a estratégia certa. Mitigações:

- **Cache com TTL** (ex.: 5 minutos): a primeira chamada demora alguns segundos; milhares de outras leem do cache instantaneamente. Trade-off: troca-se **frescor dos dados por latência** (quem lê depois de 4 minutos vê dados de 4 minutos atrás).
- **Desnormalização:** ex.: a Joana comenta no post do João (que está no shard do João). Para listar todos os comentários da Joana seria preciso varrer N shards. Solução: ao comentar, escreve-se também no shard da Joana (uma tabela auxiliar/referência de comentários, sem replicar post nem usuário inteiros). Trade-off: leitura mais rápida, escrita mais complexa (sempre dois lugares). Vale se for feature central do produto.

### 3. Consistência (transações entre shards)

Exemplo: transferência bancária de R$ 10 de Maria (shard 1) para João (shard 3). Em banco único, uma transação (`BEGIN … COMMIT`) garante atomicidade. Com shards (bancos físicos diferentes) não há transação única: se debitou a Maria e falhou o crédito ao João, como devolver? Duas soluções (relacionadas ao vídeo de saga pattern):

- **2PC (two-phase commit):** um orquestrador/coordenador pergunta aos shards se conseguem fazer a operação; quando todos confirmam, dispara o commit; se algum falhar, manda os outros desfazerem. Existe e é usado em alguns sistemas, mas **não é o mais recomendado** em grandes sistemas distribuídos.
- **Saga pattern (mais usado):** microações **compensatórias** para cada ação. A Maria é debitada e comitada; se o crédito ao João falhar, o servidor (ou mensageria, se forem servidores distintos) dispara a ação compensatória: reembolsar a Maria. Imperfeito (o dinheiro aparece descontado e depois devolvido, com notificação e histórico), mas é o que iFood, Uber e empresas gigantes já aceitam — ineficiente? Não: é muito eficiente.

## Decidir se vale usar sharding: faça conta

Sharding **nem sempre é necessário**. Na parte de requisitos não funcionais da entrevista, descubra: quantos usuários, volume de dados trafegado, tamanho dos dados (100.000 usuários trafegando 10 KB é diferente de 5 MB cada), relação leitura/escrita. Fazer conta em frente ao entrevistador e concluir "não vale a pena sharding aqui, um Postgres simples basta" passa **mais senioridade** do que citar sharding por reflexo. Lembrete: um PostgreSQL parrudo na AWS aguenta até ~50.000 escritas/s; 2 milhões de usuários que só leem podem gerar ~500 escritas/s — ridículo para justificar sharding.

Se precisar usar sharding, o roteiro:
1. Defina a **partition key** (e justifique pelas queries).
2. Explique a **estratégia de distribuição**: por padrão hash-based (pode ser composto conforme requisitos), com **consistent hashing**.
3. Fale dos **trade-offs** de cada escolha.
4. **Crescimento:** se o entrevistador perguntar "e se usuários e escritas crescerem 10×?" — "não muda nada": o consistent hashing já permite rebalancear da forma mais eficiente.

## Qual banco usar

PostgreSQL não é nativamente voltado a sharding — dá para fazer, mas precisa de extensões/plugins. Bancos como **Cassandra** e **ScyllaDB** (um "Cassandra tunado") têm sharding por natureza e algoritmos mais eficientes para ingerir muitas escritas por segundo. O autor planeja um vídeo dedicado sobre Cassandra/ScyllaDB.
