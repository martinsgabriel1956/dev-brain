# Desenho para Escalar até 1 Milhão de Usuários

> Aula liberada gratuitamente no YouTube, parte de um curso pago de System Design (mais de 90 aulas). Baseada no livro *System Design Interview* de Alex Xu (ByteByteGo). O objetivo é fazer um apanhado de técnicas usadas numa entrevista de system design para escalar um serviço, começando do exemplo mais simples e evoluindo conforme a demanda cresce.
>
> _Nota: blocos de venda/pitch do curso (início e fim) omitidos por não serem conteúdo técnico._

## O ponto de partida: um único servidor

A aplicação mais simples possível:

- Um **usuário** — na prática, um app mobile (celular) ou um browser — faz requisições (requests).
- Essas requisições chegam num **servidor web** (web server) que roda a nossa aplicação e responde ao usuário.

Isso é o mínimo necessário para ter um serviço na web que funciona. Às vezes esse mínimo é suficiente.

## Adicionando um banco de dados

Para durabilidade/persistência, quase toda aplicação precisa de um **banco de dados**, com uma conexão com o servidor.

Por que precisamos de um banco:

1. Armazenar grandes quantidades de dados — não faz sentido guardar dentro do servidor.
2. O servidor pode cair ou resetar; sem persistência, perderíamos toda a informação.

**Qual banco?** A escolha específica importa menos que a decisão **SQL vs NoSQL**. Por padrão: **SQL**. A maioria das aplicações convenciona começar com SQL, mas você pode argumentar por NoSQL se souber justificar.

Quando optar por **NoSQL**:

- Dependência de **latência super baixa**.
- **Esquema flexível** — logs, JSON, dados que mudam muito e não têm esquema fixo.
- **Throughput muito alto** — muitos dados transacionados num período curto (ex.: armazenar todos os requests recebidos), quantidades enormes de dados.

## Escalando o servidor (vertical vs horizontal)

Conforme o servidor recebe mais requests, dá para aumentar o tamanho da máquina (escala vertical). Mas isso não escala bem:

- Existe um **limite físico** do tamanho de uma máquina — você nunca vê uma Netflix rodando num único servidor.
- **Single Point of Failure (SPOF)**: se o único servidor cai, a aplicação cai. O banco de dados também é um SPOF (corrigido depois).

**Solução — múltiplos servidores (escala horizontal):** como os dados já estão persistidos no banco (e não no servidor), dá para ter uma aplicação distribuída em vários servidores, que leem e escrevem no mesmo banco. Formamos um **cluster de servidores**.

### Load Balancer

Com múltiplos servidores, o usuário precisa saber para qual servidor mandar o request. A solução é o **load balancer**: ele direciona os requests para o servidor que quiser, usando diferentes técnicas de redirecionamento.

Ganhos: aplicação mais robusta (menos propensa a cair se um servidor falhar) e maior vazão para muitos usuários. Os servidores deixam de ser o gargalo — agora o gargalo e SPOF é o banco de dados.

## Escalando o banco de dados (replicação)

Para dar mais vazão e reduzir falhas, faz-se **replicação**:

- Um banco para **escrita (writes)** e réplicas apenas para **leitura (reads)**.
- A maioria das aplicações tem **mais leituras do que escritas**.
- Escreve num banco → replica a escrita nas réplicas → lê das réplicas.

Por que separar? Escrever em dois bancos simultaneamente pode gerar **inconsistência** / **race condition**.

**E se o banco de escrita cair (SPOF)?** Como todos compartilham os mesmos dados, **promove-se** uma das réplicas de leitura a banco de escrita.

## Cache

Bancos de dados costumam ter certa lentidão (network, buscas). Para melhorar a velocidade, adiciona-se uma **cache**:

- Os servidores consultam a cache **antes** do banco.
- Se a cache não tiver a informação, consulta-se o banco.

Cuidados:

- A cache pode ser um **SPOF** — precisa de boa **política de invalidação** (expirar o que está em cache).
- A aplicação precisa estar apta a lidar com o fato de que **a cache às vezes não responde / pode cair**.

## CDN (arquivos estáticos)

Serviços que lidam com **arquivos estáticos grandes** (filme, foto, logo do site, página HTML) podem ter esses arquivos como gargalo de rede.

Solução: manter arquivos estáticos numa **CDN**. Arquivo estático é algo que não muda (ou muda muito infrequentemente). O usuário requisita direto da CDN, aliviando a carga do serviço e dando impressão de mais velocidade (ex.: a página inicial chega muito mais rápido).

## Servidores sem estado (stateless) + NoSQL para sessões

O cluster de backend deve ser **sem estado (stateless)**. Motivo: se o estado de login ficar dentro de um servidor e o próximo request do usuário cair em outro servidor, ele aparece deslogado — má experiência.

- Login em cache às vezes é apropriado.
- Para **sessões (sticky sessions)**, preferências do usuário e coisas acessadas com muita frequência (lentas num banco tradicional), pode-se usar um **NoSQL** de auxílio.
- Esse NoSQL **não pode estar dentro de nenhum servidor web**, pois os servidores podem cair ou ser desativados.

## Filas e Workers (processamento assíncrono)

Para aplicações com **computações pesadas** (processamento de vídeo/imagem, gerar PDFs) que podem ser feitas de forma assíncrona:

- A aplicação cria **jobs** numa **fila** (modelo **publisher/subscriber**): publica trabalhos a serem executados.
- Os jobs são puxados da fila por um **subscriber**.
- Quem processa é um **worker** (threads rodando em outra máquina, um lambda etc.), que processa os itens em sequência.

Isso dá vazão às requisições pesadas, aliviando os servidores web para responderem o usuário de forma rápida.

## Tooling (observabilidade)

É comum representar no system design os serviços de **tooling** rodando fora dos servidores principais: login, observabilidade, métricas, monitoramento, health checks, logs de erros. Bem comum, mesmo que pouco falado.

## Diversificação global (multi-região)

Última etapa (quando necessária): replicar todo esse conjunto (cluster, cache etc.) em mais de uma **região / data center**.

- Ex. Amazon: um data center nos EUA (US East 1) e outro em outra região (US West, ou EU Central 1 na Europa).
- Um **load balancer com roteamento baseado em geolocalização** (ou outras formas) roteia o tráfego para o data center certo.
- Exceção: o **NoSQL de sticky sessions** é compartilhado entre regiões.

Isso adiciona complexidade, mas com isso o serviço escala para milhões de usuários. Muito provavelmente, mesmo **sem** múltiplos data centers, já se atingiria o marco de 1 milhão de usuários servidos.

## Fechamento

Esse é o ferramental básico (porém completo) de como desenhar um sistema para escalar para muitos usuários. É o que se acaba usando numa entrevista, e muitas aplicações, vistas de um nível alto, se parecem com esse desenho.
