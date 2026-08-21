# CQRS e Event Sourcing Explicado na Prática

> Transcrição de vídeo (português) explicando CQRS (Command Query Responsibility Segregation) e Event Sourcing juntos, partindo do conceito primitivo de CQS em nível de função até a aplicação em sistemas reais (e-commerce, bancos, Shopify). Inclui um trecho patrocinado pela Abacus AI (ferramenta "DeepAgent") comparando geração de MVP com Claude/DeepAgent vs. ChatGPT.

---

## Introdução

Pode deixar o like e se inscrever aqui embaixo que eu garanto que esse vídeo vai ser muito bom. Essas duas coisas — CQRS e Event Sourcing — são geralmente ensinadas juntas, e eu vou ensinar elas também juntas, porque teoricamente são dois conceitos separados. Teoricamente CQRS é um conceito, Event Sourcing é outro conceito. O "x" da questão é que, em aplicações de mundo real, quando a gente fala de Event Sourcing, a gente quase sempre tá falando de CQRS — segundo dois dos maiores experts nesse tema.

CQRS é apenas uma noção muito simples de ser compreendida: é a noção de que existe um modelo diferente para atualizar as informações do que para ler essas informações. Ou seja, CQRS foge um pouco daquilo que a gente pensa como sendo um CRUD simples web — foge um pouco do create, read, update, delete — porque o read vai ser um modelo à parte de todos os outros. A gente tem aqui dois modelos diferentes.

Por que que a gente geralmente vai querer ter esses dois modelos diferentes? Por que que a gente vai então querer implementar CQRS? Para atingir esse objetivo, muito provavelmente, em quase todo sistema real que a gente vai implementar isso, a gente vai tá implementando com o objetivo de Event Sourcing. Então, no vídeo de hoje, a gente vai entender o que é CQRS, Event Sourcing, como isso é útil, e vai ser uma discussão bem legal de arquitetura e padrões de design.

Antes disso, um recado da patrocinadora do canal, a Abacus AI. O que dá para ver é um timelapse comparando a Abacus AI (ferramenta DeepAgent) contra o ChatGPT criando o mesmo aplicativo, a partir de um prompt simples para construir um web app inspirado no Notion que permite que o usuário crie documentos. A Abacus AI criou o app em três iterações de prompt, em cerca de 15 minutos, resultando num MVP funcional que se parece com o Notion, deployável na própria infra, com conexão a banco de dados — código real, com autenticação, rotas, componentes de UI. O DeepAgent custa cerca de US$10/mês, com alguns limites de uso.

Em comparação, pedindo ao agente do ChatGPT (GPT Plus) para gerar algo equivalente, o resultado foi um único arquivo Python sem `requirements`, que nem chegou a rodar de primeira — precisou pedir para consertar, e mesmo assim ficou um arquivo único de ~600 linhas de Python sem autenticação, sem estrutura, que não funcionou. A diferença de "grandeza" entre os dois resultados, para o mesmo prompt, foi descrita como muito grande.

Na descrição do vídeo original ficam duas referências: um artigo do Martin Fowler sobre CQRS e uma palestra (talk) do Greg Young sobre CQRS e Event Sourcing.

## CQS: a raiz conceitual de CQRS

Vamos lá, letra por letra: **C**ommand **Q**uery **R**esponsibility **S**egregation — CQRS. Separação entre o que é um comando e o que é uma query, e a utilização de modelos diferentes para se fazer um comando e para se fazer uma query.

Existe um conceito anterior a CQRS — CQS (Command Query Separation) — que se aplica não a um sistema inteiro, mas a nível de função: quando você tem um `get` e quando você tem um `set`.

- Um `get` não altera absolutamente nada de estado, e retorna um valor. Geralmente um `get` não recebe parâmetro (embora possa). Ele retorna um valor e jamais pode mutar estado, jamais pode causar alterações nos dados.
- Um `set` é o contrário: recebe como parâmetro as coisas que vão mudar, e não retorna nada.

Essa é a forma mais primitiva de separar o que é um comando e o que é uma query — pensa em getters e setters no Java, onde `set` altera/muta estado e `get` apenas busca e retorna o estado.

## De função para sistema: write model e read model

Levando essa ideia de uma função para um sistema inteiro: imagina um client no topo (o front, o usuário final) interagindo com o sistema. Abaixo dele, uma camada de command/query, depois um handler, um modelo, e no fim tudo persiste num banco de dados. Quando o usuário faz uma query (um `get`), os dados voltam desse banco de dados para cima.

Se a gente quiser aplicar segregação de comando e query, a gente separa isso em um **write model** (modelo de escrita) e um **read model** (modelo de leitura) — que podem ser diferentes entre si, inclusive nos "renders". Isso praticamente quebra a aplicação em duas aplicações, dois sistemas diferentes.

Isso já tem alguma utilidade, mas ainda estamos imaginando tudo escrevendo no mesmo banco de dados. Em um sistema normal — pensa num "Twitter da vida" — quando você lê posts, você lê centenas deles, e escreve um post. É comum que o número de escritas seja ordens de grandeza menor que o número de leituras: você lê muito mais do que escreve. Um sistema pode ter, num dia, 100 escritas e 10.000 leituras — perfeitamente plausível (pensa em quantos views um vídeo do YouTube recebe depois de ser publicado uma única vez).

Por isso a gente pode escalar os dois sistemas de formas diferentes — o sistema de read escala mais do que o de write, porque se lê mais do que se escreve.

## Fragmentando o banco: bancos diferentes para read e write

O verdadeiro ganho começa quando a gente fragmenta o banco de dados: um banco para write, que replica para diferentes bancos de read — permitindo escalabilidade horizontal. Além disso, existe vantagem natural em usar bancos de naturezas diferentes para finalidades diferentes.

Exemplo: para agregar um grande número de views de vídeos, pode ser interessante usar um **banco de dados colunar** (orientado a colunas, não a linhas) — esse banco replica os dados de uma database principal. Pode-se manter também um Postgres simples para queries mais complexas e estruturadas. Esses bancos podem inclusive servir clientes diferentes: um banco colunar serve um sistema de analytics, o Postgres serve o read model "normal", e pode existir ainda um banco para logs.

Para escritas rápidas, é comum pensar em NoSQL (ex.: DynamoDB, MongoDB) — isso é apenas ilustrativo, não uma recomendação de uso obrigatório.

## O impedance mismatch

Imagina um e-commerce, com operações como criar uma ordem — recebendo do front uma lista de produtos, quantidades, preços, e o ID do customer. Esse evento de "criar uma ordem" cabe muito bem em um único objeto JSON. Mas ao traduzir isso para linhas e colunas de um banco relacional, deixa de ser um único objeto: vira uma linha na tabela `users`, duas linhas na tabela `product`, duas linhas em `order_line_items`, e pelo menos uma linha em `order` (com um `order_id`). Um produto simples se transforma em quatro linhas em quatro tabelas diferentes — isso é o chamado **impedance mismatch**.

Por que manter essas quatro linhas em quatro tabelas? Para manter a consistência/estrutura do modelo relacional (Postgres).

## Por que "ler o estado final" não basta: motivação para eventos

Imagina um carrinho de compras sendo escrito continuamente num banco: produto 1, produto 2 adicionados; depois um evento remove o produto 1; depois o usuário confirma a ordem. O usuário tomou três ações diferentes (três eventos), mas o banco de dados só guarda o **resultado final** dessas três operações — não dá para ver o passo a passo do que o usuário fez.

Exemplo: trabalhando numa empresa como a Shopify, se alguém quiser saber quantas pessoas estão removendo produtos do carrinho, essa informação não existe no banco — só o estado final. Seria necessária uma tabela nova, catalogando cada evento que altera uma ordem (uma linha por ação tomada).

Isso é o objetivo de Event Sourcing: uma linha que cataloga todas as ações que os usuários tomaram, que resultaram no snapshot final da ordem. Isso conecta com o conceito de **write-ahead log (WAL)**: quando você submete ações num banco (Postgres, por exemplo), ele não persiste imediatamente na memória de longo prazo — primeiro escreve num log (quase como um TXT) a sequência de ações que vão ser tomadas, e só depois reflete isso no estado presente do banco. Ou seja, o próprio Postgres faz Event Sourcing internamente.

O objetivo de Event Sourcing, então, é garantir que informações não sejam perdidas — que os eventos gerados pelo usuário (criar ordem, remover produto, confirmar ordem) estejam presentes e sejam **auditáveis**. Event Sourcing é também sobre auditabilidade.

## Analogia bancária: o ledger

Numa indústria séria como a bancária: o saldo exibido no app do banco muito provavelmente não é só uma coluna no banco de dados — a verdade final do saldo é a força resultante de todas as transações feitas (transação 1, transação 2, transação 3...). Se acontecer um erro — um bug que altera indevidamente o saldo para um valor absurdo —, o banco não confia numa coluna isolada: ele roda/revisita todas as transações da conta e identifica se o resultado bate com o saldo. Tendo transação por transação, também é possível identificar qual transação específica é fraudulenta.

Event Sourcing é interessante porque, tendo o conjunto de todos os eventos gerados no sistema, dá para descartar o banco de estado atual — desde que se tenha isso que se chama de **ledger** (livro-razão): o conjunto de todos os eventos. A partir dele, rodando os eventos do início ao fim, obtém-se o estado atual como resultante.

## CQRS + Event Sourcing juntos

Voltando a CQRS: se o sistema segue uma arquitetura de Event Sourcing, o write model escreve **eventos** — "criar ordem com X, Y, Z", "remover produto da ordem", "confirmar ordem" — e só se preocupa com isso. Esses eventos passam por algum mecanismo (ex.: Kafka, um "event algo") que pega os dados e os transforma numa **projeção** — outra forma de esses dados serem acessados/lidos.

Os eventos são a **única fonte de verdade**: o estado atual do sistema é sempre a força resultante de todos os eventos feitos naquele sistema. A partir disso, é possível projetar esses eventos num Postgres, num Cassandra, num Neo4j, ou no que for necessário para leitura. Isso implica um custo de **consistência eventual**, porque a escrita está de um lado do sistema e a leitura (uma replicação/reflexo do que foi escrito) está do outro.

O interessante: migrar de banco de dados passa a ser trivial, desde que os eventos não sejam perdidos — tendo todos os eventos em sequência, dá para migrar para qualquer banco, qualquer modelo de visualização, qualquer estrutura.

O evento pode ter uma estrutura interna completamente diferente do objeto de leitura — é exatamente o caso do exemplo de "criar ordem" com o impedance mismatch descrito acima: um payload com ID do consumidor, order lines, IDs de produtos, preços — e a reconstrução em linhas/tabelas pode ser feita de N maneiras diferentes a partir desse mesmo payload.

## Imutabilidade dos eventos

Event Sourcing é sobre auditabilidade e **eventos imutáveis**. Para que os eventos sirvam como única fonte de verdade e o sistema seja confiável, os eventos precisam ser imutáveis.

Exemplo: se uma transação erroneamente creditou R$1.000 quando deveria ser R$100, a solução não é apagar/alterar a transação já salva — é o que um contador faz: nunca apagar a transação, mas adicionar outra transação que reverte o que a anterior fez (uma transação inversa, removendo R$1.000), seguida da transação correta (+R$100). A partir dessas três transações, conclui-se que o resultado final foi +R$100.

A maioria das indústrias maduras que quer forte auditabilidade sobre o que acontecia em determinado momento do sistema (o exemplo do Shopify de adicionar/remover itens do carrinho) precisa de eventos organizados dessa forma.

## Quando (não) usar: decisão de domínio, não decisão técnica

Isso é CQRS e Event Sourcing. Agora, importante: geralmente isso é guiado por necessidade de domínio, não decisão técnica.

Recomendação inicial é a **não recomendação**: se o sistema é um CRUD simples, não há necessidade disso — isso adiciona bastante complexidade na aplicação. É fato: nem o maior defensor de CQRS/Event Sourcing vai dizer que isso é menos complexo que um CRUD simples — é mais complexo.

Existem indústrias que precisam disso — indústria bancária, e qualquer indústria que queira auditabilidade. Existem também motivos técnicos legítimos: escalar um lado (escritas) de uma maneira e o outro (leituras) de outra; escritas podem ser em NoSQL, leituras num SQL simples; uma equipe pode desenvolver o lado de escrita e outra o lado de leitura. Todos esses motivos técnicos podem existir, mas CQRS/Event Sourcing é geralmente motivado pelo **domínio** — a lógica de negócio exigindo isso, não uma decisão puramente técnica. Geralmente é uma decisão de "eu preciso dar auditabilidade dos meus eventos".

### Efeitos colaterais e benefícios

- Ter um ledger de tudo que aconteceu no sistema faz com que mudanças/migrações de banco de dados não sejam tão assustadoras — nunca se perde um dado. Mesmo um incidente destrutivo no banco (ex.: um `rm -rf` acidental no diretório de dados do Postgres) é recuperável reconstruindo o estado a partir dos eventos, sem depender do estado atual para derivar os estados seguintes.
- Reprodução de bugs: se um bug ocorreu em um horário específico (ex.: 23:00:45), dá para rodar as transações até esse ponto, ver qual era o estado, rodar o próximo evento que o usuário fez (independentemente de qual seja — ex.: "update name de um produto") e reproduzir exatamente o bug e a situação daquele momento específico do sistema.
- Essa lógica de domínio (ex.: "criar uma ordem com tais produtos") tende a mudar pouco ao longo do tempo — pode-se adicionar um campo a mais aos eventos, mas a ação em si se mantém estável. Isso também se encaixa com Domain-Driven Design: os eventos vêm do domínio, e é importante que o evento reflita a ação sendo tomada no domínio.
- Com todos os eventos disponíveis, é possível rodar análises mais ricas (ex.: "big data" sobre os eventos, traçar causalidade) — muito mais informação e detalhe do que uma "foto estática" do estado (que é o que um banco de dados tradicional oferece).
- A consequência (não a causa) desse desenho é que, em algum momento, existe um SQL (ou banco equivalente) que materializa os dados para leitura mais fácil — mas essa é a ação tomada a partir do evento, e sempre é possível traçar de volta qual foi o evento que resultou nessa ação.
