# Rate Limit em APIs: história, onde aplicar e estado compartilhado (Bernardo Lobato)

Transcrição de vídeo (pt-BR) do canal de Bernardo Lobato, sobre arquitetura e segurança de APIs. ASR bruto limpo, pontuado e organizado em seções; conteúdo técnico preservado, sem tradução (já estava em português). Pedidos de like/inscrição/compartilhamento omitidos. Termos reconhecidos erroneamente pelo ASR foram corrigidos pelo contexto: "P/PI" = API; "edp/endpoint" = endpoint; "leick bucket" = leaky bucket; "IPI gate/API Gator" = API Gateway; "AF" = WAF; "Cash for Redna Azure" = Azure Cache for Redis; "Google Memory Store" = Google Memorystore; "single punch of failure" = single point of failure; "Nests" = NestJS; "Bucket 4J" = Bucket4j; "rate limitar/RIT Limit" = rate limiter/rate limit. **Ambíguo:** "Kong ou ox" (provável Kong ou Envoy/APISIX; não resolvido).

## Abertura

Como limitar que um login seja quebrado por força bruta, impedir que um usuário abuse de uma API cara que consome muitos recursos, ou evitar automações agressivas nos endpoints? O vídeo trata de **rate limit** no desenho de APIs e na segurança das aplicações: de onde surgiu, onde aplicar e quais tecnologias existem. Não é um conceito da era do desenvolvimento web. É uma espécie de controle de taxa de consumo de um recurso, seja uma API simples ou uma arquitetura distribuída complexa.

## Viagem histórica: redes de pacotes

O problema é mais antigo que a web. Nas primeiras décadas das **redes de pacotes** surgiu a necessidade de controlar a taxa com que os dados entravam na rede, para lidar com tráfego irregular e evitar que certos fluxos prejudicassem a rede toda. Rede de pacotes: os dados não viajam num fluxo único e contínuo; vários dispositivos compartilham a mesma infraestrutura e pacotes de comunicações diferentes são intercalados. É a base de praticamente qualquer rede moderna e da própria internet.

Dois conceitos importantes:

- **Traffic shaping:** controla o fluxo de dados, normalmente retendo temporariamente alguns pacotes para que sejam transmitidos a uma determinada taxa.
- **Traffic policing:** abordagem mais rígida; verifica se o tráfego respeita uma política e, ao ultrapassar o limite, pode descartar ou marcar os pacotes excedentes.

### Leaky bucket (fluxo previsível)

Imagine um balde que recebe água numa velocidade qualquer, mas tem uma saída controlada. Mesmo que a água chegue de forma irregular, a saída ocorre numa taxa previsível. Aplicado a redes, controla o ritmo com que o tráfego é encaminhado.

### Token bucket (permite picos controlados)

Em vez de controlar a saída, há **tokens (fichas)** acumulados num balde (bucket), que tem um limite de capacidade. Em intervalos regulares novos tokens entram (ex.: 2 por segundo, 100 por segundo). Quando chega uma requisição ou tráfego, o sistema verifica se há tokens: se sim, retira um e aprova; se o balde está vazio, a requisição é rejeitada ou adiada.

Essas estratégias estabeleceram uma ideia que persiste: em vez de apenas responder "pode ou não pode ser atendida", controla-se a **taxa** com que o recurso é consumido. Com a popularização das APIs e da chamada **API Economy**, os mesmos princípios passaram a fazer parte de APIs, gateways, load balancers e outros componentes de sistemas distribuídos.

### HTTP 429

Até então ainda não existia o famigerado **HTTP 429**. Veio em 2012 com a **RFC 6585**, que definiu **429 Too Many Requests**: indica que o cliente enviou requisições demais num determinado período. Opcionalmente a resposta informa, via **Retry-After**, quanto tempo esperar antes de tentar de novo. (Link da RFC na descrição do vídeo.)

## Definição

Rate limit é um mecanismo para controlar **quantas vezes um recurso pode ser acessado num intervalo de tempo**. O recurso pode ser um documento, um endpoint ou uma aplicação inteira. Exemplo: um cliente pode fazer no máximo 100 requisições por minuto; com 80, tudo continua normal; na 101ª o sistema pode rejeitar e responder 429 Too Many Requests. A requisição **não precisa necessariamente ser rejeitada**: dependendo de como o limite foi implementado e do algoritmo usado, há outras estratégias além da rejeição (a serem vistas depois).

## Perguntas de design antes de implementar

Parece simples, mas é preciso responder:

- Onde colocar o limite: no código, na API, na rede?
- Como identificar o que limitar: nome de usuário, API key, IP?
- Quando a requisição é contabilizada: só depois de responder 200? Se a requisição falhar, conta para o rate limit?
- O que fazer quando o limite é atingido?
- O limite vale só para alguns endpoints ou para o sistema inteiro?

Ou seja: o "rate limiterzinho" colocado no código da API não basta como visão de arquitetura.

## Onde posicionar o rate limit (três lugares, em alto nível)

### 1. Na aplicação

Há mais contexto para decidir: limitar por usuário, endpoint, ID, qualquer regra de negócio. Controle total do código e muita flexibilidade. **Trade-off:** cada instância da aplicação precisa compartilhar o estado do limite, isto é, cada réplica precisa aplicar a mesma política e enxergar o mesmo estado de consumo (tratado adiante).

### 2. Externo à aplicação: API Gateway, proxy reverso, load balancer

A política é centralizada e evita que requisições excessivas cheguem aos serviços. É boa camada para limites gerais, mas pode perder o contexto específico do domínio; se o limite depende de regras de negócio, pode não ser o lugar ideal. Reduz drasticamente a carga sobre a aplicação e é boa escolha para regras mais gerais, como limitar endpoints ou clientes específicos. Um **API Gateway**, por ser de mais alto nível, permite políticas mais sofisticadas que um load balancer, devido à configuração e a mecanismos próprios de autenticação, autorização, identificação de cliente, roteamento e outras políticas de API.

### 3. Na borda: CDN ou WAF

Se usar provedor de nuvem, o tráfego é bloqueado muito cedo, economizando recursos. A nível de infraestrutura é útil para mitigar padrões de tráfego abusivo e faz parte de uma estratégia maior de proteção contra **DDoS**. Mas é péssimo para regras que dependem de lógica de negócio, pois tem ainda menos conhecimento que API Gateway, load balancer e a própria aplicação. (Vídeo do canal sobre CDNs indicado.)

## Como implementar (decisões arquiteturais, não tutorial)

### Borda

Em plataformas como o **Cloudflare** (se a aplicação está hospedada lá), é possível configurar regras de rate limit em características da requisição, como o caminho da URL, o país ou outras informações disponíveis, aplicando ações de bloqueio ou mitigação ainda na borda. Isso protege a aplicação e os recursos de infraestrutura. Provedores de nuvem também oferecem rate limit diretamente no serviço contratado, com regras por IP ou outros critérios de agregação, sem alterar o código.

### Camada intermediária (API Gateway / load balancer)

- **Spring Cloud Gateway:** tem o filtro **RequestRateLimiter**, normalmente combinado com Redis; usa **token bucket** e permite definir limites para uma **chave personalizada** (API key, nome de usuário, e-mail etc.).
- **Kong** (e outro gateway/proxy citado de forma ambígua): amplamente usados para centralizar políticas de rate limit. Vantagem: vários serviços compartilham a mesma política sem precisar implementar a preocupação em cada aplicação.
- API Gateway costuma oferecer políticas mais sofisticadas; proxy ou load balancer normalmente trabalham com regras mais genéricas de tráfego.

### Aplicação

É provavelmente a camada mais rica, pois o rate limit pode usar informações do domínio: usuário autenticado, plano contratado, tenant, endpoint, permissões, regras de negócio. Depende de linguagem/tecnologia:

- **Java:** **Bucket4j**, muito usada para implementar token bucket na aplicação, com limites por usuário, API ou qualquer chave definida pelo desenvolvedor; integra-se a filtros da aplicação e aos mecanismos de segurança do Spring, deixando a aplicação do limite relativamente transparente.
- **JavaScript (NestJS):** o ecossistema tem o **Throttler**, que funciona via **guards** e permite aplicar limites globais ou por rota; oferece estrutura pronta para identificação do cliente e suporta diferentes mecanismos de armazenamento quando a aplicação tem múltiplas instâncias.

## O problema do estado compartilhado em arquiteturas distribuídas

Um dos problemas mais interessantes e chatos de rate limit aparece quando a aplicação deixa de ter uma única instância. Exemplo: três instâncias da mesma API, limite de 100 requisições por minuto por usuário. Se cada instância mantiver seu próprio contador em memória, o usuário pode fazer até 100 requisições em cada instância; no pior caso, **300 no total**, o que quebra totalmente a política. Não existe mais um estado único representando o consumo daquele recurso por aquele usuário.

**Solução:** colocar o estado num **armazenamento compartilhado externo** à aplicação; todas as instâncias consultam e atualizam o mesmo estado. Isso introduz novos trade-offs: **latência, concorrência, consistência e disponibilidade**, e o próprio estado compartilhado passa a ser uma dependência mais crítica. Um rate limit aparentemente simples vira um problema clássico de estado compartilhado em sistemas distribuídos.

Tecnologias possíveis: **Redis** ("tão falado e às vezes infame"); equivalentes de nuvem como **Google Memorystore** (Google Cloud), **Azure Cache for Redis** (Azure) e **DynamoDB** (AWS); ou um banco tradicional / solução própria menos sofisticada para mais flexibilidade. Não são equivalentes e têm trade-offs próprios; consultar a documentação e ver qual se adequa melhor ao desenho.

**Ponto particularmente interessante:** o próprio rate limiter pode virar **gargalo no sistema que deveria proteger**. Como todas as requisições precisam consultar um estado centralizado, o mecanismo precisa ser tão escalável e resiliente quanto a própria aplicação e **não deve virar um single point of failure** no desenho.

## Resumo do autor

- **Na aplicação:** mais contexto, mas mais complexidade.
- **API Gateway / load balancer:** equilíbrio entre controle e centralização.
- **Na borda:** menos contexto, bloqueio mais cedo e menor custo para a infraestrutura.
- **O rate limit altera o comportamento do cliente:** um cliente que recebe 429 precisa saber o que fazer: aplicar **backoff**, ter uma **política de retry** ou mesmo desistir. Implementar rate limit impacta a experiência e o comportamento dos consumidores da API.
- **Não é preciso escolher uma só camada:** pode-se combinar estratégias na aplicação, na borda e no API Gateway, aproveitando os trade-offs de cada uma.

## Fechamento

O vídeo ficou na parte arquitetural: onde colocar o controle, que contexto ele precisa conhecer, como o estado é compartilhado e as consequências das escolhas. Quanto mais distribuída e complexa a arquitetura, mais essas decisões importam. Ficou faltando detalhar os **algoritmos de rate limit: fixed window, sliding window, leaky bucket e token bucket**, planejado para uma **segunda parte** se este vídeo for bem. O autor pede nos comentários relatos de quem já implementou esse tipo de controle.
