# Escalabilidade Horizontal, Load Balancers e Fundamentos de Redes

> Transcrição de vídeo (formatada em Markdown, sem tradução). Fonte: vídeo sobre escalabilidade vertical/horizontal, camadas do modelo OSI e algoritmos de balanceamento de carga, com demonstração prática usando Nginx.

## Introdução

Muitos desenvolvedores acreditam que escalabilidade horizontal se resume simplesmente a criar réplicas do servidor e adicionar um load balancer na ponta dessas réplicas para balancear as requisições entre elas. Só que existe um oceano imenso de informações por trás dessa suposta escalabilidade, que vai muito além dessa fração resumida do assunto geralmente propagada por aí.

O vídeo mostra como essas ferramentas funcionam por baixo dos panos, ensina os fundamentos de redes de computadores necessários para lidar com escalabilidade vertical e horizontal, e ainda roda um load balancer na prática para demonstrar o funcionamento real.

## Escalabilidade Vertical (Scale Up)

Escalabilidade vertical é o primeiro passo antes de pensar em escalar qualquer coisa horizontalmente.

Imagine um servidor hospedando uma aplicação (site, e-commerce, software da empresa) com usuários acessando-a. Quando a empresa faz uma boa gestão e boas campanhas, a tendência natural é que o número de usuários aumente ao longo do tempo. O desafio é que o servidor começa a ficar sobrecarregado com o número de requisições, pois foi projetado para uma carga específica no início e agora precisa lidar com muito mais usuários simultâneos. Isso causa quedas e lentidão, prejudicando a experiência do usuário e podendo gerar perda de dinheiro para a empresa.

A primeira solução, antes de falar de escala horizontal, é escalar verticalmente: adicionar mais poder computacional ao servidor — mais memória RAM, mais poder de processamento, mais armazenamento. Com isso o servidor ganha capacidade para lidar com o número atual de usuários simultâneos.

### Desafios da escalabilidade vertical

Toda decisão arquitetural envolve tradeoffs. Os desafios da escala vertical são:

1. **Recursos computacionais são limitados.** Não é possível adicionar memória RAM, poder de processamento ou armazenamento infinitos numa máquina — existe um teto. Além disso, esses recursos ficam progressivamente mais caros conforme crescem.
2. **Single Point of Failure (SPOF) — ponto único de falha.** Como se trata de uma aplicação importante (por isso está sendo escalada), ter apenas uma máquina significa que, se ela cair (por exemplo, o data center falhar), toda a aplicação fica fora do ar. Não há redundância nem resiliência.
3. **Crescimento contínuo de usuários.** Se a empresa continuar crescendo, eventualmente se atinge o teto da escala vertical, ou fica inviável provisionar mais recursos, e o servidor volta a ficar sobrecarregado.

É nesse momento que entra a escala horizontal — mas não faz sentido escalar horizontalmente antes de esgotar a escala vertical.

## Escalabilidade Horizontal

Funciona criando réplicas do servidor (servidores separados com a mesma aplicação) e adicionando um load balancer para receber todas as requisições dos usuários e balancear a carga entre os servidores.

Vantagens:
- Os servidores réplica não precisam de hardware extremamente robusto — a carga que antes ia para uma única máquina agora é dividida entre várias.
- O load balancer fica na ponta recebendo o volume total de requisições, pois foi projetado especificamente para isso, operando numa camada de baixo nível.

### Arquitetura típica

Na prática, geralmente:
- O IP público do load balancer é exposto na internet para os usuários se conectarem.
- Os servidores ficam numa rede privada da empresa, por questões de segurança. O load balancer conhece essa rede privada e consegue se comunicar com os servidores, mas a internet externa não tem acesso direto a eles.

Esse é o conhecimento que a maioria dos desenvolvedores já possui. Mas existe um universo de conceitos de redes de computadores por trás do Load Balancer que é essencial para system design — por exemplo, saber escolher o algoritmo certo e a camada de rede certa em que o load balancer deve operar, como no caso da arquitetura do WhatsApp.

## Tipos de Load Balancers

### Baseados em hardware
Equipamentos físicos que fazem a função de balanceamento de carga:
- **F5 Big-IP** — o mais famoso e utilizado.
- **Citrix NetScaler** — também muito utilizado.
- **A10 Networks Thunder** — conhecido como GLB (Global Load Balancer). Em vez de balancear carga para servidores específicos, balanceia entre data centers diferentes (ex.: EUA, Brasil, Suíça). É raro encontrar esse cenário no dia a dia, exceto em empresas com arquitetura premissa ou provedores de infraestrutura.

### Baseados em software
Programas instalados e configurados em servidores para atuar como balanceadores:
- **Nginx** — o mais famoso e utilizado.
- **HAProxy** — concorrente direto do Nginx.
- **Traefik**

Esses três são os que mais aparecem no dia a dia real de configuração.

### Baseados em cloud
Balanceadores oferecidos por provedores de nuvem:
- **AWS**: ALB (Application Load Balancer) e NLB (Network Load Balancer).
- **Google Cloud**: Google Cloud Load Balancer.
- **Microsoft Azure**: Azure Load Balancer e Azure Application Gateway.

Por que AWS e Azure oferecem dois balanceadores diferentes? Porque eles cumprem funções diferentes e operam em camadas de rede diferentes:
- **ALB** (AWS) opera na camada 7 do modelo OSI.
- **NLB** (AWS) opera na camada 4.
- **Google Cloud Load Balancer** opera tanto em camada 4 quanto em camada 7.
- **Azure Load Balancer** opera em camada 4; **Azure Application Gateway** opera em camada 7.

Os balanceadores de hardware e software mencionados acima geralmente operam tanto em camada 4 quanto em camada 7, dependendo apenas da configuração escolhida.

## Modelo OSI e as Camadas de Rede

O modelo OSI descreve como a internet funciona por baixo dos panos — fundamento essencial de redes de computadores para qualquer programador.

### Camada 7 (Aplicação)

É a camada com que usuários interagem diretamente: navegador, protocolos como HTTP, FTP, Telnet, SMTP. Depois dela vêm as camadas de apresentação, sessão, transporte, rede (network), enlace e física.

**Analogia:** um balanceador de camada 7 é como enviar uma carta pelos Correios. Você entrega a carta ao atendente, que cola selo, carimba e a encaminha por todos os trâmites internos (camadas de apresentação, sessão) até chegar à camada de transporte (o "motorista"), que consulta o "GPS" (camada de rede) para definir a rota e finalmente trafega pela camada física (as estradas/cabos de rede).

### Camada 4 (Transporte)

Protocolos: TCP, UDP, SSL, TLS — os protocolos mais fundamentais de redes.

**Analogia:** um balanceador de camada 4 é como entregar a carta diretamente na mão do caminhoneiro, sem passar pela agência dos Correios. Ele só olha o endereço (IP de origem/destino) e leva ao destino, sem interceptar ou interpretar o conteúdo.

Um balanceador de camada 4 é "cego": só enxerga IP de origem e IP de destino. Não interpreta HTTP, não lê headers, não faz autenticação, não entende JWT — apenas encaminha a mensagem para o destino.

### Quando usar Load Balancer de Camada 4

Indicado para aplicações que demandam:
- WebSocket massivo
- Jogos online / comunicação em tempo real
- Conexões TCP ou UDP persistentes entre cliente e servidor

Características: alto throughput, baixa latência.

**Exemplos:**
- **Jogos em tempo real (ex.: FPS)**: usam UDP em vez de HTTP, pois cada frame/tiro gerando uma requisição HTTP seria inviável (overhead de desempacotar sessão, headers, cookies a cada interação). A conexão UDP fica aberta (uma espécie de túnel) enquanto o jogador está online.
- **Videoconferência (ex.: Google Meet)**: também usa UDP, que permite perda de pacotes — por isso a imagem "pixela" ou trava quando a internet está ruim.
- **WhatsApp**: usa WebSocket, não HTTP. Ao abrir o app, ele fecha uma conexão WebSocket com o load balancer, que por sua vez fecha uma conexão WebSocket com o servidor, permanecendo conectado indefinidamente. (Mencionado como preparação para um futuro vídeo, em duas partes, sobre a arquitetura completa do WhatsApp.)

Esse tipo de conhecimento (em qual camada OSI um load balancer opera) é frequentemente cobrado em entrevistas de system design.

### Quando usar Load Balancer de Camada 7

Indicado para aplicações baseadas em HTTP: aplicações web, microsserviços, e-commerce, apps móveis via API.

Características:
- Intercepta e desempacota a requisição HTTP.
- Consegue rotear com base na URL (ex.: `/pedidos` vai para o cluster de pedidos, `/pagamento` vai para o cluster de pagamentos).
- Permite autenticação JWT, leitura de headers/cookies, rate limiting, etc.

Em cerca de 90% dos casos de aplicações tradicionais, usa-se Layer 7.

**Resumo:** Layer 4 apenas repassa pacotes com base em IP de origem/destino (rápido e "burro"); Layer 7 intercepta e interpreta a requisição, permitindo controle mais granular.

## Algoritmos de Balanceamento de Carga

Demonstração prática usando Nginx como load balancer e três servidores simples em Go, rodando nas portas 8001, 8002 e 8003, com o Nginx configurado na porta 8080 usando um bloco `upstream` chamado `backend` e `proxy_pass`.

### Round Robin

Algoritmo padrão de qualquer load balancer. Distribui as requisições de forma circular entre os servidores: uma para o primeiro, uma para o segundo, uma para o terceiro, e repete o ciclo.

Testado na prática: cada atualização de página no navegador (porta 8080) alterna sequencialmente entre os três servidores (1 → 2 → 3 → 1 → 2 → 3...).

É o algoritmo mais simples, mas não resolve todos os problemas — usá-lo sem critério em produção pode causar problemas.

### Weighted Round Robin

Balanceamento ponderado pelo peso de cada servidor. Útil quando o servidor original (já escalado verticalmente) é mantido com mais capacidade e as réplicas horizontais são menores e mais baratas — quem sofre a carga principal é o load balancer.

Configuração: adicionar a diretiva `weight` a um servidor (ex.: `weight=3`), fazendo com que a cada N requisições, mais delas sejam direcionadas ao servidor mais robusto, e o restante distribuído uniformemente entre os demais.

### Least Connections

Balanceia com base no menor número de conexões ativas em cada servidor. Mais inteligente que o Round Robin porque considera que requisições podem ter tempos de resposta muito diferentes (uma tarefa simples responde rápido; gerar um relatório ou dashboard demora mais). O algoritmo direciona novas requisições para o servidor com menos conexões ativas no momento, equilibrando a carga real de trabalho, não apenas a quantidade de requisições.

Configuração: trocar a diretiva `weight` pela diretiva `least_conn` no bloco `upstream`.

### Least Response Time (Least Time)

Balanceia com base no tempo de resposta de cada servidor. Se um servidor está respondendo mais lento (por exemplo, 600ms contra 150ms e 250ms dos demais), o algoritmo envia menos requisições a ele, dando tempo para investigar o problema e evitando sobrecarregar um servidor já degradado.

Configuração: diretiva `least_time` — porém disponível apenas na versão paga do Nginx (Nginx Plus). Em serviços de load balancer em nuvem, esse tipo de configuração costuma ser mais simples.

### Sticky Round Robin (Session Persistence)

Resolve o problema de aplicações monolíticas que não são stateless (sessão de login gerenciada pelo próprio servidor, sem JWT). Quando um usuário cai em um servidor específico na primeira requisição, todas as requisições subsequentes desse mesmo usuário são direcionadas ao mesmo servidor, permitindo manter a sessão sem quebrar a escalabilidade horizontal.

Documentação e outros algoritmos (como Random e IP Hash) estão disponíveis no site oficial do Nginx.

### Alternando entre Camada 4 e Camada 7 no Nginx

- Para operar em **camada 7**: usar bloco `http` com diretiva `location`.
- Para operar em **camada 4**: usar bloco `stream` em vez de `http`, removendo o `location`. Nesse modo, o Nginx apenas fecha a conexão TCP/UDP e não interpreta a requisição HTTP — por isso, testar via navegador com múltiplos reloads resulta na conexão ficando presa sempre no mesmo servidor (não balanceia por requisição HTTP), pois o balanceamento por requisição não é o modelo do Layer 4.

## Conclusão

Os pontos centrais cobertos:
- Diferença entre escalabilidade vertical e horizontal, e por que a vertical vem primeiro.
- Tipos de load balancers: hardware, software e cloud.
- Camadas 4 e 7 do modelo OSI e quando usar cada uma.
- Algoritmos de balanceamento: Round Robin, Weighted Round Robin, Least Connections, Least Response Time e Sticky Round Robin.
- Demonstração prática de configuração com Nginx.

Recomendação: configurar esses balanceadores na prática (por exemplo, seguindo a documentação oficial do Nginx) é a melhor forma de fixar o aprendizado.
