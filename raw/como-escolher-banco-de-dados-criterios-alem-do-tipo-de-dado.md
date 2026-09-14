# Como Escolher o Banco de Dados Certo (Além do Tipo de Dado)

Transcrição de vídeo (autor/canal não identificado), em português, sobre a pergunta mais comum em entrevistas de system design: "qual banco de dados você usaria?".

## Introdução

Essa é provavelmente a pergunta mais importante que vão te fazer numa entrevista de system design — ou até o ponto mais importante que você precisa decidir na hora que estiver fazendo o design do seu sistema. O banco de dados, na visão do autor, é o ponto mais importante de qualquer design de sistema. Essa pergunta é muito comum em entrevistas de system design; o autor gosta de começar suas entrevistas normalmente com banco de dados, e dá para ter uma ideia de como vai ser a evolução da conversa só pela resposta dessa pergunta.

Normalmente há dois grandes grupos de resposta para essa pergunta.

**Primeiro grupo (mais superficial, não errado, mas raso):** a pessoa pensa principalmente no *tipo do dado*. Ex.: "vou salvar um documento, um dado de esquema mais livre → banco documental (MongoDB)" ou "vou salvar um dado que precisa de relacionamentos, mais estruturado, normalizado → banco relacional". Essa resposta é considerada correta, mas superficial.

O autor quer trazer profundidade adicional: pensar não só na estrutura do dado em si, mas também na forma como ele é acessado, na frequência, no preço, e na forma como a informação é atualizada.

A seguir, os critérios detalhados, um a um, comparando bases relacionais (ex. Postgres), colunares, documentais (ex. MongoDB) e key-value (ex. DynamoDB).

## 1. Data Schema (esquema do dado)

O formato da informação armazenada. Se o esquema é estruturado/normalizado, ou se a frequência de atualização do esquema é alta, ou se não há consistência de esquema — saber isso de antemão indica se o dado se comporta melhor numa base relacional ou numa base documental. Bases colunares e key-value entram na discussão quando se fala de forma de acesso (próximo tópico).

## 2. Forma de acesso (padrão de consulta)

Como a informação vai ser consultada. Se a consulta pode variar por vários campos diferentes (ex.: um formulário em que o usuário escolhe buscar por id, por data de atualização, por nome), uma base que suporte SQL-like é mais fácil de usar — dá para adicionar/remover filtros (statements) na query.

Por outro lado, se a busca é estritamente por id (chave), reduzindo a busca a uma coluna/campo, um banco estilo key-value store (ex.: DynamoDB) entrega performance muito boa.

## 3. Mais escrita ou mais leitura

Algumas bases são otimizadas para escrita, outras para leitura.

**Postgres (instalação tradicional):** muito otimizado para leitura. Os índices tradicionais (B+ tree — B-tree com conexões nas folhas) são construídos esperando ficar no shared buffer (memória), entregando consultas em milissegundos de um dígito. Na escrita, é preciso recalcular/rebalancear o índice. Há configurações para aumentar o throughput de escrita: `CREATE TABLE ... UNLOGGED` (pula o write-ahead log), desativar `synchronous_commit` (não espera propagar o WAL pro disco — ganho de ~3-5%). Mas por padrão o Postgres é estruturado para performance de leitura.

**MongoDB / DynamoDB:** já têm por padrão sharding/separação em várias instâncias, escalabilidade horizontal — arquitetura mais otimizada para volume maior de escritas (embora suportem também carga de leitura alta).

## 4. Transacional vs. Storage

Se a estrutura de dados é muito mais transacional (muda com frequência) ou muito mais de armazenamento (storage, poucas mutações, volume grande).

Exemplo: tabela de 1 TB, manipulada com pouca frequência → forte em storage. Base menor (alguns GB) mas com volume de transações de leitura/escrita muito alto → forte em transação.

**Exemplo prático (e-commerce):**
- Carrinhos: mudam com muita frequência (usuário adiciona/remove), base menor pois carrinhos antigos são descartados → volume de escrita alto, storage relativamente enxuto.
- Catálogo de produtos: pouca atualização, base muito maior → forte em storage, fraco em transação.

**Implicação de custo/arquitetura:** no Postgres, tabela grande sem particionamento precisa subir o índice inteiro para memória (shared buffer) para ter performance boa — exige muita RAM. Se a tabela é grande e o volume de transações é baixo, você paga uma máquina grande com muita RAM só para manter o índice em memória, mas usa pouco. Nesse cenário faz mais sentido usar DynamoDB: o custo de storage no Dynamo é baixo, mas o custo de transação (leitura/escrita) é alto — é ali que "mora" o custo do Dynamo. Se você tem uma base grande com leitura/escrita de baixa frequência, um SGBD documental/serverless de storage barato compensa mais que deixar isso "sujando" um Postgres (índice inchado, bloat).

Quando o volume de escrita é muito alto numa base relacional MVCC (como o Postgres), ele vai apendando tuplas novas e versionando para controle de concorrência — isso suja a base, exigindo `VACUUM` frequente para remover tuplas antigas, o que degrada performance se não for bem gerenciado.

**Resumo da matriz de decisão desse critério:**
- Transações altas, base pequena, majoritariamente leitura → Postgres é fantástico.
- Transações baixas, storage muito alto → DynamoDB pode fazer mais sentido.
- Escrita muito alta → MongoDB faz mais sentido.

Repare que essa escolha (entre DynamoDB, MongoDB e Postgres) foi feita sem se preocupar com o formato da informação, mas sim com a frequência de atualização e o tipo de consulta.

## 5. Transação/Consistência (ACID vs. eventual)

Bases relacionais em geral seguem ACID (Atomicidade, Consistência, Isolamento, Durabilidade) nas transações. Bases NoSQL (documentais como MongoDB, key-value como DynamoDB) tendem a ter consistência eventual, principalmente quando há sharding — necessário para controlar e replicar a informação entre nós.

## 6. Latência

A latência está muito relacionada à performance do banco, e a performance é muito relacionada ao uso que está sendo dado a ele. Uma base otimizada para escrita usada com carga forte de leitura (ou vice-versa) pode ter latência impactada. Importante pensar no impacto de latência principalmente no *worst case*.

Exemplo: durante um `VACUUM` no Postgres para limpeza de tuplas mortas, é possível controlar o `fillfactor` (tanto do índice quanto da tabela/heap) para garantir melhor performance de update.

## 7. Escalabilidade

Bases relacionais tradicionais escalam principalmente de forma **vertical**. Mesmo com réplicas de leitura, o nó principal (onde chegam os INSERTs/UPDATEs) está limitado à capacidade de hardware daquele servidor. Para aumentar capacidade de escrita, é preciso escalar verticalmente. Existem opções de sharding manual para quebrar entre servidores, mas não é um processo natural/automático do banco — é mais manual.

Réplicas de leitura têm consistência eventual: o master escreve, replica para uma ou mais réplicas de leitura conforme a configuração, mas o request de leitura pode não chegar exatamente na réplica já atualizada — pequena latência/consistência eventual na leitura, geralmente aceitável em sistemas de alta performance.

Bases key-value estilo DynamoDB já fazem escalabilidade automática (nós para mais ou para menos, conforme o workload) — escalabilidade **horizontal** nativa, sem que o usuário precise se preocupar com isso.

## 8. Custo

O custo é um resumo de todos os critérios anteriores — só é possível calcular/ter noção do custo real depois de analisar toda a estrutura.

- Uso intensivo de RAM (ex.: manter índice grande em memória no Postgres) impacta bastante o custo da máquina.
- Acesso muito grande de leitura/escrita no DynamoDB gera custo alto.
- O data schema também importa para custo: se o tamanho do documento/registro é muito grande (ex.: 24 KB), no Postgres isso estoura o tamanho da página (heap) — o Postgres passa a salvar o dado como TOAST (binário referenciado fora da página principal), o que impacta performance mas **não** necessariamente aumenta o custo direto da operação (só custo de disco/transferência).
- No DynamoDB, o tamanho do payload importa diretamente para custo: cobrança em WCU (Write Cost Unit) e RCU (Read Cost Unit). Escrita: o documento é dividido por 1 KB — 24 KB = 24 WCU; se exigir consistência forte, cobra ainda mais (e mais ainda se escrever em mais de uma tabela simultaneamente). Leitura: dividido por 4 KB, cobrado sobre esse tamanho.
- Ou seja: no DynamoDB, o tamanho do payload importa diretamente para o custo; no Postgres, importa mais para performance/estrutura de armazenamento (heap vs. TOAST) do que para custo direto da operação.

## Conclusão

Conhecer o data schema não é relevante só para decidir "vou usar documental para não precisar de migration" — o tamanho da informação e a estrutura do dado influenciam custo, performance, e a forma como a base armazena (heap vs. binário referenciado). Saber articular tudo isso é o principal diferencial numa entrevista de system design, quando a pergunta "qual banco de dados você colocaria?" aparece — trazer esse racional completo demonstra profundidade de conhecimento, e é conhecimento relevante para o dia a dia real de escolha de banco de dados.

Em alguns cenários não há opção de escolha (empresa já padronizada em Postgres, Aurora, DynamoDB, Mongo etc.). Mas quando há liberdade de escolha, para encontrar a base mais barata, mais performática, que resolve o problema e permite evolução do sistema, é preciso pensar em pelo menos estes fatores:

1. Como vou salvar (data schema)?
2. Como vou acessar (forma de consulta)?
3. Vou ler mais ou escrever mais?
4. Vou ter mais transação ou mais data storage?
5. Preciso de consistência forte (ACID) ou eventual é aceitável?
6. Quais minhas restrições de latência (escrita e leitura)?
7. Como escalar essa base — a demanda flutua ao longo do dia ou é mais consistente?
8. De posse de tudo isso, qual o custo estimado e qual a melhor opção que faz sentido?
