---
date: 2026-09-14
tags: [transcricao, entrevista, dual-write-problem, outbox-pattern, cdc, debezium, kafka]
skill: tech-mentor-backend
level: intermediário/avançado
---

# Transactional Outbox Pattern: o Desafio de Entrevista do Cadastro de Usuário + E-mail de Boas-Vindas

> Transcrição de vídeo (fala corrida, sem pontuação original) em português, já no idioma original — sem necessidade de tradução. Estruturada em seções pelo agente para facilitar a leitura; conteúdo preservado na íntegra.

## Introdução: o Desafio de Entrevista

Imagina que você tá numa entrevista para programador e o desafio que chegou para você resolver dessa vez consiste basicamente em você criar uma API de cadastro de usuários onde toda vez que um usuário novo se cadastrar no nosso sistema você deve enviar um e-mail de boas-vindas para ele.

Aparentemente isso parece ser algo extremamente simples e fácil de ser feito — e realmente é até simples e fácil de se fazer. Só que o problema tá na intuição de 99,9% dos programadores para desenrolar esse tipo de desafio. Isso porque a intuição da maioria vai ser exatamente pegar os dados que o usuário enviou no corpo da requisição, criar um registro no banco de dados para de fato criar o usuário, e depois chamar algum serviço de terceiros para poder fazer o envio desse e-mail, ou até mesmo enviar isso para algum mecanismo de mensageria como um Kafka ou um RabbitMQ para que o envio do e-mail seja feito de maneira assíncrona.

Esse tipo de intuição é o tipo de intuição que vai te sacanear durante uma entrevista e também na vida real quando você tiver diante desse tipo de problema. Isso porque esse fluxo que eu acabei de criar aqui para você é o fluxo que esconde um problema invisível — e na maioria das vezes extremamente traiçoeiro — conhecido como **the dual write problem**, ou **problema da dupla escrita**, que acontece todas as vezes que você precisa realizar uma operação no banco de dados e depois precisa fazer alguma outra coisa. Todas as vezes que você precisar passar por esse fluxo, você vai se deparar com o problema da dupla escrita.

Esse tipo de problema é um dos problemas que mais reprovam candidatos de todos os níveis nas entrevistas, e é exatamente esse problema que você vai aprender a resolver no vídeo de hoje, utilizando um padrão de projeto extremamente simples e muito poderoso, conhecido como **Transactional Outbox Pattern**. Esse padrão é um padrão de resiliência que garante que você consiga manter o fluxo mesmo escrevendo em dois lugares, e é exatamente isso que você vai sair daqui sabendo no vídeo de hoje.

## O Problema da Dupla Escrita (Dual Write Problem)

Vamos começar entendendo o que é esse problema, como ele aparece na vida real quando você tiver trabalhando desenvolvendo suas aplicações atuando como programador ou arquiteto de software, e como isso também aparece nas suas entrevistas para programador — independente do seu nível de senioridade. Isso aparece tanto para programador júnior, pleno, sênior, tanto faz, até para programadores mais avançados e até para arquitetos. Esse tipo de problema não faz distinção; ele vai aparecer para você mais dia menos dia, e provavelmente ele já apareceu para você — você só não percebeu que ele tava ali.

### O Cenário: API de Cadastro + E-mail de Boas-Vindas

Vamos imaginar que a gente tá com o desafio de desenvolver uma API de cadastro de usuários que, após o cadastro do usuário, a gente precisa enviar um e-mail de boas-vindas para ele. Tarefinha super simples, sem mistério nenhum, sem nenhum tipo de complicação.

Os componentes: o usuário no front-end da aplicação, a API de cadastro (um servidor para hospedar esse back-end), e o banco de dados para armazenar o registro dos usuários.

O fluxo que naturalmente vai acontecer: o usuário preenche o formulário de cadastro (nome, e-mail, CPF, senha, data de aniversário, telefone e outros dados fictícios de exemplo). A requisição chega no back-end, que faz algumas validações e armazena esse registro no banco de dados, numa tabela de usuários (ID, nome, e-mail, senha, created_at, etc.).

Depois que o registro é inserido no banco, o próximo passo natural é chamar um provedor de envio de e-mails (SendGrid, algum serviço da AWS, etc.) para enviar o e-mail de boas-vindas. Alternativamente, a aplicação poderia enviar uma mensagem para uma fila de mensageria (Kafka, RabbitMQ, SQS — tanto faz), e quem quiser reagir a esse evento de "novo usuário cadastrado" que reaja. Por exemplo, um `notification-service` que fica escutando essa fila e, toda vez que chega o registro de um novo usuário cadastrado, cuida de enviar o e-mail — uma arquitetura orientada a eventos.

O que importa, independente do mecanismo escolhido, é que a gente armazena o registro no banco **e** precisa fazer alguma outra coisa. E é aqui que mora o problema.

### O Código Ingênuo (Fictício, para Ilustrar o Fluxo)

Um endpoint que recebe uma requisição e devolve uma resposta:

1. Extrai os dados da requisição.
2. Faz as validações.
3. Faz um `INSERT` no banco de dados (salva o usuário: nome, e-mail, etc. — na vida real seria via ORM, não SQL bruto; o SQL bruto aqui é só para ilustrar o que acontece por baixo dos panos).
4. Publica uma mensagem no Kafka (ou chama um serviço de terceiros — o problema acontece do mesmo jeito).
5. Retorna a resposta pro usuário (HTTP 201 Created).

**Por que isso não vai funcionar:** imagina que, conforme a validação dos dados foi feita e o usuário foi inserido no banco, na hora de executar a publicação da mensagem no Kafka a aplicação simplesmente morre — o processo é desligado, a instância cai, ou o próprio Kafka fica fora do ar (indisponibilidade, não conseguimos nos comunicar com ele).

O que acontece: o registro foi inserido no banco de dados, mas a mensagem não foi publicada no Kafka. Os serviços que reagiriam a esse cadastro (envio de e-mail, ativação de conta, etc.) nunca vão executar, porque a mensagem nunca chegou. O e-mail dele não vai ser enviado, o cadastro talvez não seja habilitado, e várias outras coisas que a arquitetura dependeria dessa mensagem nunca vão acontecer.

A mesma coisa aconteceria se o serviço de terceiros fosse chamado via HTTP diretamente para disparar o e-mail. O problema é que a gente está tentando fazer duas coisas ao mesmo tempo de maneira atômica, e isso não é garantido.

### A Primeira Tentativa Ingênua de Correção: Transação Local

A intuição seguinte, quando você se depara com esse problema, é: "isso é fácil de resolver, basta envolver tudo numa transação — se der certo, comita; se der errado, dá rollback."

Fluxo revisado (ainda fictício, para ilustrar a lógica):

1. Inicia uma transação (`BEGIN TRANSACTION`).
2. Dentro de um `try/catch`: insere o usuário no banco **e** publica a mensagem no Kafka.
3. Se tudo der certo: `COMMIT`.
4. Se algo der errado (ex.: Kafka fora do ar): `ROLLBACK` — nem o insert no banco nem a publicação acontecem.

**Por que isso também não funciona:** o problema é que a transação do banco de dados não tem como garantir atomicidade sobre uma operação externa como o Kafka. Imagina que a linha de execução chegue até a publicação no Kafka — a mensagem **é enviada** para o Kafka — e, exatamente no momento de dar o `COMMIT` da transação do banco, a aplicação morre, ou o banco de dados fica fora do ar, ou há uma falha de rede (lembrando do teorema CAP — tolerância a partições).

Se isso acontecer, o dado **não foi inserido no banco** (porque o commit não aconteceu), mas a mensagem **já foi enviada** para o Kafka. Isso não é atômico — você não consegue garantir que a transação do banco de dados e a publicação no Kafka aconteçam como uma unidade única.

Resultado prático: o usuário recebe o e-mail de boas-vindas, mas o cadastro dele (login, senha) não existe no banco de dados, porque o dado não foi inserido. Quando ele tentar logar na aplicação, vai dar "usuário inexistente" ou "senha inválida" — ele não vai conseguir logar, porque o registro dele não existe no banco.

Isso é exatamente o **problema da dupla escrita**: você tenta escrever em dois lugares de maneira completamente atômica, mas, em sistemas distribuídos ou chamadas independentes entre sistemas, isso não é possível — pelo menos não dessa forma. As coisas vão falhar, e você precisa estar preparado para que seu sistema tenha a liberdade de falhar e seja resiliente o suficiente para lidar com esse tipo de falha sem desmontar a aplicação, sem fazer o usuário sofrer e sem gerar inconsistência de dados.

### Outros Cenários Onde o Mesmo Problema Aparece

Esse problema acontece em todo cenário onde você precisa armazenar um dado no banco de dados **e** fazer qualquer outra operação:

- Armazenar um dado tanto no banco de dados quanto no **cache** (isso, inclusive, é outro padrão de projeto — um padrão de cache).
- Inserir um dado no banco de dados **e** armazenar algum log da aplicação no Elasticsearch.
- Enviar para um mecanismo de mensageria (RabbitMQ, Kafka, SQS).
- Chamar um serviço de terceiros via requisição.

Em todos esses casos, o cache, o Elasticsearch, o mecanismo de mensageria ou o serviço de terceiros pode falhar, e o problema é o mesmo.

Esse é um problema **invisível** — você só percebe que ele aconteceu quando ele explode. Ele não é facilmente identificável, porque olhando para o código tudo parece certo e bonitinho. O problema explode em produção: dados inconsistentes, ora o dado existe no banco, ora não existe, uma mensagem foi enviada para a fila mas o dado não estava no banco. Isso é extremamente difícil de investigar em produção.

Esse conceito precisa "entrar no sangue" do programador, porque ele aparece muito nas entrevistas e muito na vida real — toda vez que você está chamando o banco de dados e fazendo outra coisa, isso pode acontecer.

## A Solução: Transactional Outbox Pattern

A solução é um padrão de projeto simples e poderoso chamado **Transactional Outbox Pattern**. É um padrão de "caixa de saída" — pensa no correio: uma caixa de saída onde você deposita cartas para que alguém depois as retire e entregue.

### Como Funciona

Esse padrão não altera quase nada na arquitetura existente — introduz apenas dois elementos novos:

1. **Outbox table** — uma tabela adicional no mesmo banco de dados.
2. **Outbox Consumer** — um serviço que lê essa tabela e processa as mensagens pendentes.

O restante da arquitetura (o serviço de cadastro, o banco de dados, o message broker, o serviço de destino) permanece o mesmo.

### O Mecanismo com o Exemplo de Cadastro de Usuário

Quando o usuário se cadastra e os dados chegam na API:

1. A API armazena os dados na tabela de **usuários** (tabela de destino).
2. **Na mesma transação**, a API também insere um registro na tabela **`outbox_users`** — daí o nome "transactional outbox": a ideia é usar uma transação que grava, ao mesmo tempo, o dado de negócio e a mensagem que seria enviada.

Estrutura da tabela `outbox_users`:

- `id` — gerado de maneira incremental.
- `event_type` — tipo do evento (ex.: "novo usuário foi registrado").
- `user_id` — chave estrangeira vinculando o evento ao registro criado.
- `payload` — o corpo da mensagem que seria enviada (ex.: um JSON que seria publicado no Kafka, ou enviado a outro sistema em outro formato).
- `status` — inicialmente "pendente", porque essa mensagem ainda precisa ser lida e processada; é literalmente uma caixa de mensagens.

Depois que esses dois inserts (tabela de destino + tabela outbox) são feitos dentro da mesma transação, a aplicação dá o `COMMIT` e retorna a resposta.

**Por que isso resolve o problema:** se o banco falhar, nenhuma das duas operações é efetivada, e o usuário recebe um erro dizendo que não foi possível realizar o cadastro (plataforma instável). Ele não segue adiante, e não há dados inconsistentes — a operação é atômica: ou garante tudo, ou não garante nada. Quando o `COMMIT` acontece, a inserção no banco **e** a existência de uma mensagem pendente válida estão garantidas simultaneamente — porque ambas fazem parte da mesma transação local do banco de dados. Se algo falhar depois (no envio da mensagem), a gente tenta de novo, e tudo bem — porque a garantia de que existe uma mensagem válida esperando para ser enviada já foi assegurada.

### O Outbox Consumer

O **Outbox Consumer** é um serviço separado que, de tempos em tempos, executa algo como:

```sql
SELECT * FROM outbox_users
WHERE status = 'pendente'
ORDER BY id
LIMIT N
```

- Filtra apenas mensagens com status "pendente" (ainda não processadas).
- Ordena pelo `id` para garantir a ordem cronológica dos eventos.
- Limita a quantidade para não processar um volume excessivo de uma vez.

Depois de ler essas mensagens, o consumer envia cada uma para o mecanismo de mensageria (ex.: Kafka) usando o `payload` armazenado. Após o envio bem-sucedido, ele atualiza o `status` do registro para "processado".

Qualquer serviço que queira reagir a essa mensagem (emitir nota fiscal, enviar e-mail, fazer qualquer outra coisa necessária) pode consumir a partir da fila, com a garantia de que a mensagem realmente chegou lá — porque, se o consumer não conseguir enviar a mensagem, ele não atualiza o status para "processado", e a mensagem continua "pendente" para ser retentada.

O Outbox Consumer é literalmente um serviço simples que fica lendo o banco de dados e fazendo inserções no Kafka (ou outro destino), garantindo que as coisas aconteçam como devem acontecer, independente de falhas no meio do caminho — porque a transação atômica já garantiu que o dado do usuário foi inserido **e** que uma mensagem foi criada na caixa de saída do banco.

### Versão Avançada: CDC com Debezium

Existe uma versão mais avançada e rebuscada desse padrão: em vez de fazer buscas manuais (polling) no banco de dados, usar uma ferramenta de **CDC (Change Data Capture)** como o **Debezium**.

O Debezium lê as modificações que ocorrem no banco de dados a partir do arquivo de log (WAL) que os bancos de dados mantêm, monitorando todas as alterações. Quando um registro novo é inserido como "pendente", o Debezium lê essa mudança diretamente do log — e ele já tem integração nativa com o Kafka através de um mecanismo chamado **Kafka Connect**, conseguindo enviar a mensagem para o Kafka automaticamente, sem necessidade de gerenciar um processo de polling.

Os serviços que quiserem consumir essas mensagens conseguem fazê-lo tranquilamente a partir do Kafka.

> Nota do apresentador: esse mecanismo de CDC já foi ensinado num vídeo anterior do canal, ao arquitetar a arquitetura do "Ticket Master".

## Conclusão

O Transactional Outbox Pattern é apontado como um dos padrões de projeto favoritos do apresentador quando o assunto é resiliência de microsserviços e sistemas distribuídos.

O vídeo encerra com uma chamada para o produto **"Mapa do Arquiteto"** — um guia de carreira do apresentador com mais de 10.000 alunos, que cobre não apenas esse padrão, mas outros padrões de banco de dados, microsserviços e arquitetura de software em geral, junto com um roadmap de carreira (júnior → pleno → sênior → arquiteto) e acesso direto ao apresentador para dúvidas.
