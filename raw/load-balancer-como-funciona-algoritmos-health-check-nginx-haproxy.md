# Load Balancer: como funciona, algoritmos, health check, Nginx e HAProxy

> Transcrição de vídeo (PT-BR, canal não identificado), limpa de erros de ASR ("route hobbing" → round robin, "list connections" → least connections, "healthck" → health check, "NeNex" → Nginx, "H Proxy" → HAProxy, "ARB" → ALB).

## O problema

Imagine que sua aplicação está no ar e, de repente, uma promoção, um anúncio ou um post viral traz 50.000 pessoas ao mesmo tempo. O sistema cai: timeout, erro 503, usuários reclamando no Twitter e você reiniciando o servidor às 3 da manhã. A causa: todo o tráfego está em uma única máquina.

Uma aplicação (API, site) roda num servidor com memória, CPU, disco e rede — tudo finito. Com cinco usuários, tudo bem. Numa Black Friday, com centenas de milhares de requisições, o servidor engasga.

## A solução

Em vez de um servidor processando tudo, vários servidores fazendo exatamente a mesma coisa, dividindo a carga (ex.: 500 req/s → 100 para cada de 5 servidores). Resta decidir qual requisição vai para qual servidor: é o **load balancer** (balanceador de carga).

Analogia do restaurante: o cliente pergunta ao recepcionista onde há mesa; ele vê quais estão ocupadas e encaminha para a livre. O load balancer encaminha para o servidor menos sobrecarregado.

Benefícios:
- Se um servidor morre (por causa de uma requisição problemática), os outros continuam ativos; o usuário não percebe a falha.
- O sistema fica mais rápido porque a carga é bem dividida e não há falta de recurso.

**O load balancer não vira gargalo?** Pode, mas é um serviço muito mais leve que as aplicações; para sobrecarregá-lo seria preciso um volume infinitamente maior de requisições — impensável para uma aplicação de pequeno/médio porte.

## Algoritmos

- **Round Robin** — sequencial e cíclico (1 → 2 → 3 → 1...), como uma roleta. Simples, fácil de implementar, funciona bem quando os servidores são iguais (memória, CPU).
- **Weighted Round Robin** — igual, mas com pesos: você informa que um servidor aguenta o dobro, então recebe o dobro das requisições. Analogia: entregador de moto vs. de carro — o de carro leva mais entregas.
- **Least Connections** — em vez de sequencial, olha qual servidor tem menos requisições em andamento e manda para ele. Ex.: servidores com 100, 90 e 70 requisições simultâneas — o balanceador manda para o de 70 até igualar, depois para o de 90 etc.
- **IP Hashing** — calcula um hash do IP do cliente e usa o hash para escolher o servidor. Como o IP é o mesmo, o cliente cai sempre no mesmo servidor. Útil para aplicações que dependem de sessão/estado local (carrinho salvo em sessão, autenticação por sessão).

Na prática, a maioria dos load balancers segue os mesmos algoritmos; muda a configuração e a aplicação ao cenário.

## Onde fica na arquitetura

Cliente (navegador, app) → **load balancer** → várias instâncias da aplicação (ex.: um microsserviço de pedidos com 3, 5 ou 50 instâncias). O cliente requisita `seusite.com.br` (o load balancer), nunca precisa saber quantas instâncias existem.

Pode existir em várias camadas do fluxo; o mais comum é a **camada de aplicação (camada 7)**, na frente de toda a requisição. Aí ele decide não só entre instâncias do mesmo serviço, mas entre **serviços diferentes**: `/api` vai para um grupo de servidores, `/images` para outro — funcionando como **proxy reverso**. Ou seja, nem sempre é só balanceamento de carga.

## Health check

O load balancer não manda requisição para servidor morto. Como sabe? Cada servidor expõe uma rota `/health` que retorna "healthy". De tempos em tempos o balanceador faz a requisição a cada servidor; se algum não responde, é marcado como morto e sai do rodízio (não é mais considerado no round robin etc.). Sem isso haveria requisições em servidores mortos retornando 500/404 e o cliente sofreria. Com isso, "você consegue falhar sem ninguém perceber".

Na prática configura-se quantas falhas consecutivas marcam o servidor como morto e quantas respostas saudáveis o marcam como vivo de novo.

## Ferramentas

Duas opções: gerenciado pela cloud ou hospedado por você.
- **Nginx** — o mais famoso; não é só load balancer, é mais focado em proxy reverso, mas funciona muito bem como balanceador.
- **HAProxy** — totalmente focado em load balancing; a maioria das empresas grandes usa ou já usou, pela estabilidade (site "horroroso", segundo o autor).
- **Cloud** — AWS: ALB (camada de aplicação) e NLB (camada de transporte/rede); GCP também tem soluções de load balancing.

## Erros comuns

1. **Não usar health check** — o balanceador precisa saber que o servidor morreu; senão o cliente sabe. Adicione também observabilidade: logs e alertas para ser avisado quando uma aplicação cair.
2. **Não pensar na sessão** — aplicações que guardam sessão na memória do servidor, ao escalar horizontalmente, perdem o dado quando a segunda requisição cai em outro servidor. (Não é o ideal guardar sessão local.)
3. **Achar que o load balancer resolve tudo** — query mal feita, banco mal otimizado, processo lento: continua lento. "Load balancer não corrige código ruim."

## Encerramento

O autor está construindo um "architecture simulator" para desenhar e documentar arquiteturas e entender como as coisas funcionam (útil para entrevistas e para construir aplicações reais); pretende disponibilizá-lo em breve.
