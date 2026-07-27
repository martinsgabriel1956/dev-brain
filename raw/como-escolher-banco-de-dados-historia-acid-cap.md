# Como Escolher o Banco de Dados Certo: História, ACID, CAP e Números Reais

## Introdução

Você já escolheu um banco de dados porque era o que o tutorial usava? Ou porque era o que o colega conhecia? Ou simplesmente porque era o que você sempre usou?

Se a resposta for sim para qualquer uma dessas, esse vídeo é pra você. Porque escolher banco de dados errado não é um problema que aparece no dia 1, ele aparece no dia que você tem mil usuários conectados. Seu sistema começa a engasgar e você percebe que a fundação estava errada desde o início. E refatorar banco de dados em produção é uma das experiências mais dolorosas que o engenheiro de software pode ter.

Hoje o vídeo entrega três coisas:

1. A história real de como bancos de dados nasceram, porque entender a origem explica porque as coisas são como são hoje.
2. Os conceitos fundamentais que a maioria dos devs pulam, e que são exatamente o que separa quem planeja banco de dados de quem só instala banco de dados.
3. Os números reais de cada banco — limites, benchmarks, casos de uso — com total transparência sobre o que esses números assumem e o que eles não consideram.

## A pré-história: antes de existir banco de dados, existia o caos

Para entender por que os bancos de dados modernos são como são, é preciso entender o problema que eles vieram resolver.

Estamos nos anos 70 e 80, linguagens dominantes: COBOL, Clipper, Assembly. Nessa época não existia sistema gerenciador de banco de dados. Os sistemas guardavam dados em arquivos ISAM (Indexed Sequential Access Method), ou simplesmente em arquivos texto e CSV, manipulados na mão.

O problema: cada programa que queria ler um arquivo (por exemplo, arquivo de clientes) precisava saber exatamente em qual byte começava o nome, em qual byte começava o salário, quantos bytes pular para chegar ao próximo registro. O programa estava acoplado à estrutura física do arquivo. Se você precisasse adicionar um novo campo — telefone, e-mail — mudava a estrutura do arquivo, e todos os módulos que liam aquele arquivo quebravam, sem exceção. Não existia o conceito de independência de dados.

A busca era um horror. Se um sistema em Clipper precisasse encontrar todos os clientes do Rio de Janeiro sem índice por estado, ele lia o arquivo inteiro, registro por registro, sequencialmente, do início ao fim — força bruta. Com índice, a coisa ficava mais fácil (posicionava o ponteiro direto no primeiro registro encontrado e fazia um laço a partir dali), mas ainda era lento.

Resultado: lentidão monstruosa, inconsistência de dados garantida, e código tão acoplado à estrutura de dados que qualquer mudança virava um projeto de semanas.

### A virada de chave: Edgar F. Codd (IBM, 1970)

Em 1970, o pesquisador Edgar F. Codd, da IBM, publicou o paper "A Relational Model of Data for Large Shared Data Banks". A ideia central: o programa não deveria precisar saber como os dados estão armazenados fisicamente no disco. Você declara o que quer, o sistema decide como buscar. Isso se chamou **independência de dados** — e virou o fundamento de tudo o que existe hoje.

- 1979: Oracle lança o Oracle V2, primeiro banco relacional comercial.
- 1983: IBM lança o DB2.

O modelo relacional ainda domina 50 anos depois não por falta de inovação ou por ser "legado" — é que o problema que ele resolve (consistência, integridade, independência de dados) nunca mudou.

## Os fundamentos: conceitos que muitos tutoriais pulam

### Conceito 1 — ACID: o contrato de confiança do banco relacional

ACID é um acrônimo de quatro propriedades que um banco relacional garante nas transações:

- **Atomicidade**: uma transação é tudo ou nada. Exemplo clássico: transferência bancária, debita R$500 na conta A, credita R$500 na conta B. Se qualquer uma das duas operações falhar (queda de energia, erro de rede, etc.), o banco desfaz tudo. Não existe "debitou mas não creditou" — ou as duas acontecem, ou nenhuma acontece.
- **Consistência**: o banco nunca vai de um estado válido para um estado inválido. Se existe uma regra ("estoque não pode ser negativo"), o banco garante essa regra mesmo com mil transações simultâneas.
- **Isolamento**: duas transações simultâneas não se enxergam. Se dois usuários compram o último produto em estoque ao mesmo tempo, o banco garante que apenas um consiga — o outro recebe erro. Sem duplicidade, sem condição de corrida.
- **Durabilidade**: quando o banco confirma a transação (commit), o dado está gravado definitivamente. Pode cair a energia, pode reiniciar o servidor — quando voltar, a transação estará lá.

Esses quatro pilares são o motivo pelo qual sistemas financeiros, sistemas de saúde e qualquer sistema onde dado errado significa dinheiro perdido ou vida em risco usam bancos relacionais. Bancos NoSQL em geral abrem mão de parte dessas garantias em troca de outra coisa — é o que o próximo conceito explica.

### Conceito 2 — Teorema CAP: por que você não pode ter tudo

Proposto por Eric Brewer em 2000, uma das ideias mais importantes da computação distribuída: em um sistema distribuído, você pode garantir no máximo duas de três propriedades ao mesmo tempo.

- **C — Consistência**: todo nó do sistema vê os mesmos dados ao mesmo tempo. Se eu escrever um dado agora, qualquer leitura imediata em qualquer servidor vê esse dado.
- **A — Availability (Disponibilidade)**: o sistema sempre responde. Mesmo que alguns nós estejam com problema, alguém responde a requisição.
- **P — Partition Tolerance (Tolerância à partição)**: o sistema continua funcionando mesmo se a comunicação entre nós cair.

Em sistemas distribuídos reais, falhas de rede acontecem — quebra não é hipótese, é realidade. Então P é quase sempre obrigatório. O que sobra é escolher entre C e A.

- Bancos relacionais tradicionais escolhem **consistência**: se houver dúvida sobre qual é o dado correto, o banco para e espera resolver. Prefere indisponibilidade temporária a dado errado.
- Bancos NoSQL, em geral, escolhem **disponibilidade**: o sistema sempre responde, mesmo que o dado retornado seja ligeiramente defasado. Isso se chama **consistência eventual** — em algum momento todos os nós convergem para o mesmo valor, mas pode não ser imediato.

Quando alguém diz "usa MongoDB que é mais rápido", o que está dizendo de fato é: esse banco abre mão de algumas garantias de consistência em troca de velocidade e escala. Dependendo do sistema, isso é uma troca excelente; dependendo do sistema, é um desastre. Entender o CAP é entender que escolha de banco não é técnica — é de negócio.

## Os bancos, os números e a realidade

Nota de transparência: todos os limites citados abaixo assumem uma **instância única** (um servidor), sem replicação, sem cluster, sem escala horizontal.

- **Escala horizontal**: adicionar mais servidores ao sistema.
- **Escala vertical**: colocar mais recursos (RAM e CPU) no mesmo servidor.

Qualquer banco pode ter seus limites multiplicados com a arquitetura certa, mas quem não entende os limites do banco sozinho não entende o banco em cluster/escala.

### MySQL — o mais popular, mas com teto

Queridinho da web há 30 anos: fácil de instalar, fácil de aprender, documentação em qualquer idioma. Mas tem um comportamento que muita gente descobre da pior forma.

**Conexões simultâneas ≠ usuários online.** Distinção crítica: imagine 600 usuários navegando no sistema agora — a maioria lendo, pensando, preenchendo formulário. Nesse momento, zero conexões ativas no banco. Quando um clica em "salvar", a aplicação abre conexão, executa o insert e fecha em milissegundos. Na prática, 600 usuários simultâneos numa aplicação web típica geram entre 20 e 50 conexões simultâneas reais no banco, dependendo do comportamento da aplicação. O que de fato ocupa uma conexão é: query longa rodando, transações abertas e não comitadas, ou o clássico erro de dev júnior — aplicação que abre conexão e esquece de fechar.

Números reais:
- Padrão de fábrica (sem mudar `my.cnf`): 151 conexões.
- Em servidores com 128–256 GB de RAM: viável operar com 5.000–10.000 conexões.
- Em máquinas com 512 GB: configurações documentadas chegando a 100.000.
- Cada conexão usa ~1 MB de RAM para gerenciar a thread → 10.000 conexões = 10 GB de overhead só de conexão, antes de processar qualquer dado.
- Acima de 5.000 conexões em instância única, o MySQL começa a apresentar degradação séria (context switching de threads vira gargalo).

Quando estoura o limite: não tem fila nem espera gentil — o banco retorna imediatamente erro **1040 "Too many connections"**. Detalhe: o MySQL reserva uma conexão extra acima do limite exclusivamente para o usuário `root`, pensado para emergências (o DBA consegue entrar para diagnosticar mesmo com todas as conexões esgotadas).

Volume de dados: até 1 TB por instância, MySQL se comporta bem com índices corretos. Acima de 10 milhões de linhas por tabela, índice bem planejado deixa de ser opção e vira obrigação. (Analogia: um livro sem sumário — para achar um assunto você vê o livro inteiro; com índice, vai direto na página. Sem índice = varredura total; com índice = acesso direto. Em 10 milhões de linhas, a diferença é segundos versus milissegundos.)

Quem usa: ~80% da web. Facebook usa MySQL massivamente (hoje via MyRocks, fork otimizado para SSD). Uber tem partes do legado em MySQL. WordPress, Shopify, Twitter nos primórdios.

Resumo: excelente para 80% dos CRUDs do mundo real. Engasga com relatórios complexos, muitos joins pesados ou dados geoespaciais.

### PostgreSQL — o "operudo", escolha de quem já extraiu tudo do MySQL

Banco para o qual a galera migra quando o MySQL já não aguenta mais — migração sempre acompanhada da frase "devia ter começado com Postgres desde o início".

**Arquitetura de conexões — diferença fundamental**: enquanto MySQL usa uma thread por conexão, o Postgres usa **processos separados** — cada conexão nova é um fork de processo no SO. Isolamento melhor (um processo trava, não derruba os outros), mas custo maior: manter 500 conexões IDLE no Postgres consome recurso real mesmo sem query rodando. Por isso o padrão da indústria com Postgres é usar obrigatoriamente um gerenciador de pool externo, o **PgBouncer**, que multiplexa centenas de conexões da aplicação em muito menos conexões reais com o banco.

Com PgBouncer: milhares de conexões na aplicação, banco vê algumas centenas. Limite prático de conexões diretas: 500–2.000, dependendo de hardware/config.

Volume de dados: sobe para centenas de terabytes sem problema de arquitetura. Em cargas analíticas com CTEs e agregações pesadas, benchmarks independentes mostram Postgres até 50% mais rápido que MySQL em cargas de trabalho similares.

Recursos que fazem diferença:
- **JSONB nativo**: documento dentro do banco relacional, com índice — feature de primeira classe, não gambiarra.
- **PostGIS**: transforma o Postgres em banco geoespacial de primeira linha (ex: "restaurantes num raio de 2km" com performance real).
- **pgvector**: extensão crítica para IA — busca semântica, embeddings, similaridade vetorial, tudo dentro do Postgres.
- **MVCC** (Multiversion Concurrency Control) mais completo que o do MySQL — importa muito em sistemas com muitas transações simultâneas e alta concorrência.

Quem usa: Apple (logs de dados em CDN, em escala massiva), Instagram (migrou parte do sistema para fugir das limitações do MySQL), Reddit, Notion, Heroku.

### Oracle — a besta corporativa, preço de apartamento

Tanque de guerra: quando você precisa de garantia, suporte e performance em qualquer cenário, ele entrega — mas você paga o preço correspondente.

Concorrência: com **RAC** (Real Application Cluster), múltiplos servidores físicos acessam o mesmo banco como se fosse uma instância única. Instância única dedicada suporta entre 10.000–65.000 sessões ativas, dependendo do hardware; com RAC, esse número se multiplica horizontalmente.

Recursos únicos no mercado:
- **Flashback Query**: consulta o dado como estava em qualquer ponto do passado, sem restaurar backup.
- **Advanced Compression**: compressão inteligente que reduz custo de storage em produção.
- **Particionamento nativo avançado**: divide tabelas enormes em pedaços gerenciáveis, transparente para a aplicação.

Esses recursos existem há décadas no Oracle; outros bancos estão implementando versões deles aos poucos.

Problema: licenciamento por núcleo de CPU — um servidor de 24 cores pode custar milhões de reais por ano só de licença. Além disso, Oracle exige DBA sênior dedicado para gerenciar parâmetros de memória (SGA, PGA); mal configurados, degradam tudo.

Quem usa: grandes bancos, grandes instituições financeiras, grandes governos — sistemas que não podem errar e têm budget para isso.

### Microsoft SQL Server — a escolha natural no ecossistema Windows/.NET

Se a empresa respira Windows, .NET, Excel, Power BI, o SQL Server faz sentido operacionalmente — não porque é tecnicamente superior ao Postgres em tudo, mas porque a integração nativa com o ecossistema Microsoft elimina fricção que existiria com outros bancos.

Limites por edição:
- **Express (gratuita)**: 10 GB de tamanho máximo por banco, uso de apenas 1 socket/4 cores de CPU, 1 GB de RAM para buffer pool. Com esses limites, degradação sensível acima de 50 usuários simultâneos escrevendo ativamente.
- **Standard (paga)**: eleva o teto para 128 GB de memória e remove o limite de tamanho de banco. Para médias empresas, aguenta 200–1.000 conexões simultâneas dependendo do hardware.

Diferencial real: o **SSMS** (SQL Server Management Studio) é a ferramenta gráfica de administração de bancos mais completa disponível. Integração nativa com Power BI/Excel via Power Query, e SSIS para ETL.

Quem usa: empresas de médio porte com stack Microsoft, mercado financeiro com Excel conectado via Power Query, ERPs como SAP em algumas configurações.

### SQLite — o subestimado: zero servidor, máxima velocidade local

SQLite não é um servidor de banco de dados — é uma biblioteca C incluída no projeto. Sem processo rodando, sem instância, sem configuração de rede. O banco inteiro é um único arquivo no disco.

Limites técnicos: tamanho teórico de até 281 TB; na prática, manter abaixo de 1 TB. Leitura absurdamente rápida (tudo local, zero latência de rede).

O limite que importa: **concorrência de escrita**. SQLite usa lock global do banco para escrita — uma transação de escrita bloqueia o banco inteiro. Leituras simultâneas funcionam bem em modo WAL (Write-Ahead Logging), mas escritas concorrentes são serializadas. Regra objetiva: se mais de dois ou três processos precisam escrever simultaneamente, não use SQLite.

Quem usa (surpreendente): todo app Android e iOS tem um SQLite interno. Chrome e Firefox guardam histórico, bookmarks e cookies em SQLite. O gerenciador de pacotes npm usa SQLite. Aviões Airbus usam SQLite em sistemas de aviônica, certificado pela norma **DO-178C** — a certificação mais rigorosa de software embarcado aeronáutico do mundo.

Quando usar: app mobile/desktop com usuário único, protótipos de MVPs rápidos, testes automatizados onde não se quer subir um servidor, sistemas embarcados.

### Redis — memória é velocidade, arma de precisão

Redis não é substituto de banco de dados relacional — é uma arma de precisão. Usado na hora certa, o sistema voa; usado errado, você perde dados em produção.

Conceito: chave-valor em memória RAM, com suporte a estruturas de dados ricas (strings, hashes, listas, sets, sorted sets, streams, bitmaps).

Performance: acima de 100 mil operações por segundo em hardware comum; com pipeline e batching, chega a 1 milhão de OPS/s. Latência sub-milissegundo, porque tudo está na RAM.

Persistência — dois mecanismos:
- **RDB**: snapshots periódicos em disco.
- **AOF** (Append-Only File): loga cada operação.

Atenção: o foco é velocidade e memória. Se o servidor cair sem AOF configurado, os dados são perdidos desde o último snapshot. Entenda o que está sendo configurado antes de pôr em produção.

Onde o Redis realmente resolve:
- **Cache de sessão**: sessão guardada no Redis com TTL de 30 minutos; cada requisição valida em sub-milissegundos, sem ir ao banco relacional.
- **Rate limit**: limitar 100 requests/minuto por IP — contadores automáticos são o padrão da indústria.
- **Contadores em tempo real**: visualizações, ranking de produtos mais vendidos na última hora, contagem de likes — sorted sets do Redis resolvem isso de forma trivial e ultra rápida.
- **Fila de processamento**: com Redis Streams, filas de processamento assíncrono (ex: download de vídeo vai para fila, worker processa em background).
- **Pub/Sub**: broadcast em tempo real entre serviços.

Ponto que poucos tutoriais deixam claro: em quase 100% dos casos reais, Redis **não é o banco principal** — ele vive em cima de um banco relacional (MySQL, PostgreSQL, Oracle), que é a fonte de verdade. Redis é a camada de velocidade na frente; quando o cache expira, busca no banco real e recarrega no Redis. É uma arquitetura de duas camadas de leitura.

Quem usa: Twitter (cache de timeline), GitHub (cache de objetos), Stack Overflow (cache de queries de exceções), Instagram (filas de processamento de notificações).

### MongoDB — flexibilidade de esquema, para o problema certo

MongoDB resolve um problema específico muito bem — o problema é quando se tenta usá-lo para tudo.

Conceito: documento BSON (JSON binário), sem esquema fixo. Cada documento na mesma coleção pode ter campos completamente diferentes.

Exemplo concreto — e-commerce: notebook tem processador, RAM, polegadas, placa de som, peso; camiseta tem tamanho, cor, material, gênero; livro tem ISBN, autor, editora, número de páginas, edição. Em SQL, as duas opções são ruins: (1) tabela com 200 colunas onde 180 ficam nulas na maioria dos registros, ou (2) arquitetura EAV (entity-attribute-value), tecnicamente correta mas um pesadelo de performance em queries. No MongoDB, cada produto é um documento com só os campos que fazem sentido para ele — simples, sem desperdício. Quando surge um novo tipo de produto com campos novos, basta começar a inserir, sem migration, sem ALTER TABLE, sem downtime.

Outros casos ideais: sistema de log e eventos (milhões de registros por hora, esquema evoluindo com o tempo), dados de IoT (cada sensor pode enviar valores/estruturas ligeiramente diferentes), CMS (tipo de conteúdo varia muito entre entidades).

Trade-off que ninguém fala: **joins não existem de forma nativa** — você desnormaliza os dados e usa `$lookup`, que tem custo. Se um sistema tem relacionamento complexo (clientes, pedidos, itens, fornecedores, todos se referenciando), o MongoDB vai fazer você sofrer — o banco relacional foi criado para isso.

MongoDB não substitui o banco relacional, ele complementa: catálogo de produtos em MongoDB para flexibilidade, mas pedido, pagamento, cliente e estoque ficam no PostgreSQL/Oracle, porque esses dados exigem transações, integridade referencial e consistência absoluta. Arquitetura real é sempre a combinação — saber qual banco resolve qual problema é o que separa o engenheiro de software de um dev que só segue tutorial.

Limites técnicos: até 65.536 conexões simultâneas em instância única. Excelente para escrita volumosa, inserção de alta frequência.

Quem usa: Mercado Livre e Amazon (catálogo de produtos), plataformas de analytics de comportamento, sistemas de log (como Graylog).

## Quando usar cada um — guia direto, sem hype

- **App mobile/desktop, usuário único** → **SQLite**: zero overhead, zero instalação, máxima velocidade local.
- **Blog, loja simples, sistema interno, CRUD padrão** → **MySQL**: rápido de desenvolver, vasta documentação, funciona para a maioria dos casos (atende hoje mais de 80% da web).
- **Sistema financeiro, relatórios complexos, dados geoespaciais, busca vetorial por IA** → **PostgreSQL**: robustez, extensibilidade, ACID sólido, ecossistema de extensões.
- **Empresa grande, budget real, missão crítica com SLA contratual e suporte 24/7** → **Oracle**: você paga caro, mas o suporte existe quando o sistema cair às 3h da manhã.
- **Stack Microsoft, integração com Excel/Power BI/.NET** → **SQL Server**: sistema integrado robusto, reduz fricção operacional.
- **Cache de sessão, rate limiting, contador em tempo real, filas leves, proteção contra carga** → **Redis**: sub-milissegundo é o padrão, não a exceção.
- **Catálogo com esquema variável, dados de log/IoT, conteúdo não estruturado** → **MongoDB**: flexibilidade de documento sem custo de esquema fixo.

## Conclusão — três ideias para levar

1. **Banco de dados não é detalhe de implementação, é decisão de arquitetura.** Decisão de arquitetura tomada errado no início é cara de desfazer depois.
2. **ACID e CAP não são teorias acadêmicas.** São o motivo pelo qual sistemas financeiros usam Oracle e não MongoDB, e o motivo pelo qual um e-commerce de catálogo pode usar MongoDB sem sofrer com isso. Quando você entende o trade-off, a escolha deixa de ser opinião e vira engenharia.
3. **Todos os números citados (conexões, volume, latência) são em instâncias únicas, sem escala horizontal.** É basicamente o piso, o ponto de partida. Quando você adiciona réplicas, shards, clusters e proxies, esse volume aumenta, mas o comportamento fundamental de cada banco não muda — por isso é preciso entender o banco sozinho antes de entender o banco distribuído.
