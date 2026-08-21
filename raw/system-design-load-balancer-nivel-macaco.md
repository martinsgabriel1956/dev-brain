# System Design — Load Balancer Explicado do Zero (Aula "Nível Macaco")

Transcrição de aula em vídeo, sem título/canal/autor explícitos no texto além do apelido usado pelo próprio apresentador. Idioma original: português (pt-BR) — sem necessidade de tradução.

## Abertura — metodologia do curso

O apresentador se identifica pelo apelido "Horácio Fiasco" / "Fiascão" e conta que foi convidado por "Mateus Leandro" para dar essa aula dentro de um curso de System Design. Descreve seu estilo de ensino como diferente de outros professores de programação (cita "Mateus" e "Luciano" como referências de estilo distinto): explica os conceitos "como se o ouvinte fosse um grande macaco — mas não qualquer macaco, o macaco mais burro da floresta", numa didática deliberadamente informal, mas sem simplificar demais o conteúdo técnico. Antes de começar, propõe uma pergunta de entrevista de emprego para o espectador pausar o vídeo e responder: "o que você sabe sobre load balancer, e qual a diferença entre os tipos?"

Anuncia o escopo da aula: layer 4 vs layer 7, Nginx, AWS, Global Load Balancers, reverse proxy — tudo demonstrado num simulador de servidor que sobrecarrega uma aplicação ao vivo para mostrar, na prática, como diferentes topologias de load balancer se comportam.

## Nível 1 — poucos usuários, sem load balancer

Cenário inicial no simulador: um grupo de usuários (exemplo: 200) faz requisições diretamente a um único servidor, que por sua vez repassa a um único banco de dados. Cada pedido do usuário ao servidor é uma **requisição** (o exemplo usado é consultar saldo num banco/Itaú).

Com 200 usuários fazendo ~200 requisições por segundo, o servidor único aguenta tranquilamente, com baixíssima latência e zero falhas — a simulação confirma isso (mostrando taxa de falha, requisições recebidas e latência total, ex.: ~150-290ms). O apresentador enfatiza o princípio central desse nível: **quando a complexidade é baixa, poucos usuários e a latência está baixa, não existe necessidade de load balancer** — introduzi-lo nesse cenário seria over-engineering, ou seja, complicar a arquitetura sem necessidade real.

### O que é latência, na analogia usada

Latência é definida como o intervalo entre o pedido (request) e a resposta (response). A analogia dada: uma conversa normal — "Oi, qual o seu nome?" seguida de resposta imediata — tem latência baixa; se a outra pessoa (o "macaco que fala português") demora um minuto para processar e responder, a latência é alta, mesmo que a resposta final esteja correta. Aplicações com poucos usuários e arquitetura simples (o exemplo usado é um SaaS fictício de "certidão de nascimento para cachorro") não precisam de load balancer — a arquitetura de nível 1 é adequada para um CRUD com 5, 10 ou até 200 usuários.

## Nível 2 — múltiplos usuários, servidor único sobrecarrega

A pergunta que motiva o nível 2: o que acontece se esse SaaS crescer de 200 para 2.000 usuários simultâneos, todos batendo nas mesmas features e no mesmo banco de dados?

Na simulação, ao subir a carga para 2.000 usuários contra um único servidor e um único banco de dados, o sistema degrada imediatamente: a barra de saúde do servidor fica vermelha, aparecem dezenas de falhas por segundo (o exemplo mostra ~30% das requisições falhando — a cada 10 pedidos, 3 não recebem resposta e derrubam parte da aplicação). O apresentador conecta esse cenário à motivação do curso inteiro: em nível pleno/sênior, o profissional precisa entender arquitetura e escalabilidade horizontal e vertical — não é conteúdo de júnior.

### Introduzindo o load balancer

A solução demonstrada é inserir um **load balancer** entre os clientes e múltiplos servidores (a simulação evolui de 1 para 2, 3 e depois 4 servidores, todos conectados ao mesmo banco de dados único). O load balancer ("balanceador de carga") intercepta toda a carga que um único servidor tomaria e decide, requisição a requisição, para qual servidor disponível encaminhar — evitando que qualquer servidor fique sobrecarregado enquanto outro está ocioso.

Na demonstração prática:
- Com 2 clientes e 1 load balancer + 1 servidor: ainda há falhas sob carga alta.
- Adicionando um segundo servidor conectado ao load balancer: as falhas começam a cair e a latência diminui.
- Com 3 e depois 4 servidores atrás do mesmo load balancer: as falhas praticamente desaparecem, cada servidor recebe uma fatia da carga e nenhum fica sobrecarregado — o load balancer usa aqui o algoritmo de **round robin** (mencionado explicitamente, com promessa de aprofundamento posterior no curso).
- Ao reduzir de volta para 2 servidores com a mesma carga alta, os erros voltam a subir — evidenciando que o load balancer sozinho não resolve capacidade insuficiente; é preciso ter servidores suficientes atrás dele.

### Escalonamento sob demanda (autoscaling)

O apresentador cita que provedores como AWS e Azure oferecem escalonamento **on demand**: ao atingir um limiar de usuários (exemplo dado: 1.999), um novo servidor é provisionado automaticamente e passa a receber tráfego do load balancer; quando a demanda cai (exemplo: volta para 200-500 requisições/s), servidores extras podem ser desligados. A ideia central: a infraestrutura escala conforme a necessidade, não precisa ficar fixa no pico.

### Nem todo load balancer é igual

Fecha o nível 2 adiantando que existem diferentes tipos de load balancer — alguns fazem "perfilamento" de informação da requisição (leem headers, cookies), outros não; alguns fazem bloqueio e geolocalização — tema do nível 3.

## Nível 3 — tipos de load balancer

### L4 vs. L7

- **L4 (layer 4)**: não inspeciona o conteúdo da requisição. Qualquer requisição é encaminhada para a rota "menos engarrafada" — decisão cega ao conteúdo, baseada só em transportar tráfego. Exemplo dado: 100 usuários, 50 vão para o servidor 1, 50 vão para o servidor 2, sem distinção de tipo de pedido.
- **L7 (layer 7)**: lê o tipo da requisição — headers, cookies — e direciona com base nisso, por exemplo mandando um usuário autenticado como admin para uma rota específica (`/admin`) enquanto o restante vai para uma rota comum. Exemplo dado: de 100 usuários, 99 vão para a rota padrão e 1 (autenticado, com token/credenciais corretos) vai para uma rota autenticada distinta.

### Global Load Balancer

Filtra a requisição também pela **geolocalização** do cliente, não só pelo conteúdo. É a explicação técnica por trás de conteúdo bloqueado por região (Netflix, YouTube) que motiva o uso de VPN, e também do porquê o ping varia em jogos online: a escolha do servidor físico (ex.: capitais como Rio de Janeiro, São Paulo, Pernambuco, Salvador — ou, no exemplo internacional, servidor na Argentina vs. em São Paulo) não é decidida pelo usuário, e sim pelo global load balancer, que direciona pela geolocalização de origem da requisição.

### Application Load Balancer vs. Gateway Load Balancer

- **Application Load Balancer**: o comportamento já descrito no L4/L7 — direciona para rotas/servidores diferentes.
- **Gateway Load Balancer**: aplica políticas de segurança e firewall sobre o tráfego. Citado como exemplo de uso real o modelo de funcionamento da Cloudflare.

### Ferramentas e produtos citados

Nginx, AWS, Azure, além dos tipos Application Load Balancer e Gateway Load Balancer. Também é citado o **Ingress** do Kubernetes como um tipo de load balancer voltado especificamente para rotear tráfego entre diferentes rotas de um cluster (mencionado como tópico a aprofundar depois no curso, sem exigir conhecimento prévio de Kubernetes nesse momento).

### Demonstração final de estresse

Para fechar, o apresentador adiciona múltiplos grupos de clientes contra apenas 2 servidores atrás de 1 load balancer e mostra o sistema estourando (falhas altíssimas, ex.: 99 falhas, requisições nem chegando a passar) — reforçando visualmente que load balancer não é solução mágica sem capacidade de servidor suficiente por trás.

## Perguntas frequentes ("perguntas burras") respondidas ao final

**1. Para escalar, preciso sempre ficar adicionando novos servidores?**
Não. Adicionar servidores é uma técnica, não a única. O curso vai cobrir outras, como cache — que evita bater no servidor/banco de dados repetidamente para a mesma informação.

**2. Posso ter múltiplos load balancers?**
Tecnicamente sim, mas o apresentador afirma nunca ter visto essa prática aplicada e não saber para que serviria — resposta pessoal, não uma negação técnica categórica.

**3. Posso ter múltiplos bancos de dados?**
Sim, e é prática comum em sistemas distribuídos: bancos separados por função (ex.: banco de leitura, banco de escrita, banco consolidado geral) ou por tipo de dado (ex.: Elasticsearch para busca, Cassandra para eventos, Redis para cache) — conceito citado como **polyglot persistence**: usar múltiplos bancos de dados especializados para necessidades diferentes dentro do mesmo sistema.

**4. Load balancer e DNS são a mesma coisa?**
Não. Analogia usada: num restaurante, o **DNS decide em qual mesa você senta** (decide a rota/destino, traduzindo IP em nome/endereço), enquanto o **load balancer decide qual garçom vai te atender** (decide quem/como atende a requisição dentro daquela rota). Diferenças concretas apontadas:
- O load balancer pode fazer o trabalho L7 (ler headers/cookies e mandar para rota autenticada); o DNS não faz esse tipo de inspeção.
- O load balancer verifica a **saúde** dos servidores de destino (health check) e redireciona se um servidor estiver sobrecarregado ou fora do ar; o DNS apenas traduz IP em nome e direciona para uma rota, sem saber se aquela rota está saudável — por isso é possível acessar um site e cair num erro no meio do caminho após a resolução DNS, algo que o DNS não previne.

## Encerramento

O apresentador resume que o objetivo da aula foi deixar clara a utilidade prática do load balancer e como ele resolve, na prática, o problema de escalar um sistema de poucos para muitos usuários simultâneos, com promessa de aprofundamento de tipos e algoritmos específicos nas aulas seguintes do curso.
