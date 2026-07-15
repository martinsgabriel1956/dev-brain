# Observabilidade de Ponta a Ponta com OpenTelemetry — Palestra em Amsterdã

Transcrição de fala corrida em português, limpa e organizada em seções. Vídeo em que o autor (canal "Eric", ver [[wiki/entities/eric-lenda]]) reapresenta, em formato de vídeo para o canal, uma palestra que deu em Amsterdã sobre observabilidade fullstack em aplicações modernas, unindo OpenTelemetry, sua experiência como especialista em performance de aplicações JavaScript e o uso de IA (via MCP servers) para automatizar investigação de incidentes.

Nota de transcrição: alguns nomes próprios e de ferramentas chegaram distorcidos pelo reconhecimento de fala (ex.: "Promitius"/"Promitos" → Prometheus; "Cubernets"/"Cubnets" → Kubernetes; "Cláudio" → Claude/Anthropic; "Grafano" → Grafana). Foram corrigidos por inferência de contexto técnico. Um caso permanece incerto e está sinalizado explicitamente no texto: o nome do framework da consultoria de performance mencionada ("Miture JS" / "mito").

## Abertura: o "novo normal" é sistemas caindo

O autor foi a Amsterdã palestrar em um dos maiores eventos de tecnologia da Europa sobre observabilidade de ponta a ponta com OpenTelemetry. Já havia feito vários vídeos sobre o tema, mas o diferencial dessa palestra é trazer a experiência de anos trabalhando como especialista em performance de aplicações JavaScript.

Promessa do conteúdo: instrumentar aplicações de ponta a ponta com OpenTelemetry (métricas, traces e logs ao longo de todo o ciclo de vida de uma requisição), correlacionar tudo isso com IA para identificar e corrigir erros mais rápido, e transformar telemetria em relatórios automatizados via servidores MCP — incluindo um caso real em que esse processo detectou que os próprios servidores do autor foram comprometidos.

Digressão pessoal: o autor já palestrou em mais de 20 países. O inglês não era fluente no início, mas a vontade de compartilhar conteúdo o levou a isso e também à primeira vaga internacional, há uns 5 anos. O ponto: não é preciso inglês perfeito para começar a se candidatar a vagas fora do Brasil — o que importa é entender os próximos passos e construir uma estratégia. (Bloco patrocinado por uma empresa de mentoria de carreira internacional, omitido do resumo técnico por não ser o foco da wiki.)

### O padrão que incomoda: sistemas offline viraram normal

Praticamente todo dia há notícia de algum sistema caindo — GitHub fora do ar, serviços principais de grandes empresas fora do ar. Quando o autor começou a programar, sistema fora do ar era inadmissível; hoje parece ter virado normal, seja com modelos de IA (ex.: APIs da Claude/Anthropic retornando `503` com mensagens do tipo "modelo ocupado, tente novamente", exigindo estratégias de retry) seja com serviços de infraestrutura corriqueiros.

### O padrão que incomoda: vulnerabilidades constantes

Exemplos citados:

- Um funcionário do GitHub instalou uma extensão maliciosa do VS Code Marketplace (mantido por GitHub/Microsoft) que baixou payload malicioso e obteve acesso ao repositório da empresa.
- Um ataque em massa à cadeia de suprimentos do NPM afetou mais de 84 pacotes, incluindo um pacote que impactou até o Codex (app da OpenAI) — o autor recebeu um alerta nativo do macOS avisando sobre malware no app e pedindo para deletar e reinstalar.

Conclusão do autor: a resposta não pode ser resignação ("é o novo normal") — o objetivo é observar melhor as aplicações para descobrir problemas antes do cliente final, e ser quem avisa o cliente, não o contrário.

## Vida de especialista em performance: o processo manual (pré-IA)

O trabalho do autor era investigar "quick wins": os melhores pontos de alteração para entregar valor rápido ao cliente. Exemplos de técnicas:

- **CPU profile / flame graph**: tirar uma "foto" da CPU do cliente para achar a função JavaScript que mais consome tempo de execução — candidata a estar travando o sistema.
- Quando o cliente já tinha uma ferramenta de APM (Datadog, New Relic ou concorrentes), o autor conseguia visualizar qual query de banco de dados é mais lenta e qual endpoint trava mais ou retorna mais erro.

Ponto central: sem visibilidade (dados) do software, não há o que investigar — é preciso instrumentação. Ferramentas de monitoramento pagas costumam ser negligenciadas por startups e empresas menores por custo, mas existem alternativas open source e gratuitas (ex.: stack Grafana rodando em Kubernetes, correlacionando front-end e back-end numa única ferramenta via OpenTelemetry — a maioria das pessoas sabe monitorar back-end, mas não sabe que dá para correlacionar dados do front-end também).

### Como era a investigação de um caso concreto (ex.: "carrinho de compras lento")

Cliente reportava algo como "o carrinho está demorando 30 segundos" ou "erros intermitentes". Processo manual do autor:

1. Entrar na base de logs e escrever queries para achar padrões.
2. Correlacionar dados de tracing (por onde o dado trafega entre microsserviços, e a velocidade de cada um).
3. Olhar métricas (tempo de resposta por endpoint, quais endpoints geram mais erro `500`).
4. Checar alertas configurados (ex.: CPU acima de 80%, endpoint X retornando muitos `500` em certos horários).
5. Agregar tudo em um relatório.

Adicionalmente, rodava a aplicação localmente com ferramentas de teste de carga, tirava profile de CPU local e investigava o ciclo de vida da aplicação (quais serviços downstream são chamados). Esse processo levava semanas — incluindo, às vezes, entrevistar desenvolvedores para chegar a uma conclusão.

### Ambientes divergentes: por que produção era o único alvo confiável

Ambientes de staging tinham dados e capacidade de máquina diferentes de produção, então não eram representativos do comportamento real dos clientes. Por isso o autor mirava direto em produção (ou simulava carga localmente com ferramentas como o **Clinic.js**, da NearForm, gratuita — citada como tendo "salvado a vida" do autor várias vezes) em vez de confiar em staging.

### Caso real: consultoria de performance em um framework popular

O autor prestou consultoria de performance para um framework JavaScript popularizado há muitos anos e ainda mantido hoje, investigando quais linhas poderiam ser alteradas para melhorar a capacidade de resposta do framework. **Nota de transcrição:** o nome do framework saiu distorcido na fala ("Miture JS", e no fechamento "entregar para a mito") — não foi possível identificar com confiança qual framework é. Registrado como pergunta em aberto na página de wiki correspondente em vez de arriscar um nome errado.

## Entrando a IA: por que o gargalo nunca foi a investigação, e sim os dados

A virada de chave do autor: todo o processo manual descrito acima era efetivo, mas lento — porque dependia de reunir dados espalhados manualmente. Uma vez que a aplicação já está instrumentada com OpenTelemetry (dados centralizados, correlacionáveis), a IA consegue automatizar a etapa de correlação e a geração do relatório — o que antes levava semanas passa a levar minutos.

### O que é o OpenTelemetry

Um **padrão** (não uma ferramenta proprietária de um único vendor): um SDK que instrumenta uma aplicação para coletar logs, métricas e traces de um único lugar, de forma agnóstica à ferramenta de monitoramento usada por trás. É open source e gratuito.

Ponto de destaque: o gráfico de contribuições do projeto ao longo dos anos mostra que praticamente todos os concorrentes do mercado de observabilidade contribuem para o mesmo padrão — New Relic, Splunk, Google, Amazon, Grafana, Datadog, entre outros. Cada um mantém sua própria ferramenta de coleta/visualização, mas todos falam o mesmo protocolo, o que beneficia a comunidade inteira.

### Os três tipos de dado coletados

- **Logs**: equivalentes a `console.log`, mas com contexto estruturado adicional automaticamente — linha de código de origem, versão do runtime (Node.js), ambiente, etc. — permitindo correlacionar padrões, não apenas ler uma linha solta.
- **Métricas**: tempo de uso/acesso agregado. Exemplos citados: métricas do runtime Node.js e do V8, e principalmente duração de requisições por método HTTP e rota exata — coletadas via OpenTelemetry, persistidas em banco e visualizadas no Grafana (open source, gratuito).
- **Traces**: o "rastro" de uma requisição, do início ao fim, atravessando serviços. Exemplo: uma requisição de back-end que bate no banco, executa uma query (ex.: 24 ms) e dentro dela um `SELECT` (ex.: 6 ms), até retornar ao usuário final. O trace mostra passo a passo onde o tempo foi gasto e onde apareceu um erro (ex.: uma dependência de terceiro respondendo `500` ou lentamente).

Com os três pilares coletados, dá para montar dashboards que já apontam, por exemplo, "914 erros 500 nesse endpoint" como ponto de partida da investigação. Lição central: **sem dados, a investigação começa no escuro.**

### Arquitetura básica de coleta

Fluxo: aplicação instrumentada (SDK OpenTelemetry, ex. pacote JavaScript) envia logs, métricas e traces para o **OpenTelemetry Collector**, que distribui os dados para os backends especializados (ex.: Prometheus para métricas, Loki para logs, Tempo/Jaeger para traces), e o Grafana atua como hub de consulta e visualização, correlacionando as três fontes.

Erro comum apontado: enviar dados direto da aplicação para Prometheus (ou outro backend) em vez de passar pelo Collector. Boa prática de produção é sempre passar pelo Collector — ele centraliza formatação e roteamento de dados num único ponto de configuração.

### Instrumentação de bibliotecas

Passo prático: buscar no NPM os pacotes de instrumentação das bibliotecas já usadas no projeto (ex.: instrumentação do módulo `fs`, do Knex — query builder de banco de dados — e do Redis, para saber quando o cache foi ou não usado). Cada instrumentação vira automaticamente um span/bloco no tracing, sem precisar reescrever código de negócio.

Caso real de impacto: numa empresa em que o autor trabalhou, adicionar essas ferramentas de investigação revelou que um pacote compartilhado por todos os microsserviços da empresa estava travando o event loop do Node.js. Atualizar esse pacote gerou um ganho de quase 50% na velocidade das aplicações — um exemplo do tipo de "quick win" que a instrumentação viabiliza.

Referência citada (sem URL captada na transcrição): um repositório de exemplo com uma aplicação completa multi-serviço instrumentada de ponta a ponta com OpenTelemetry, incluindo correlação de evento de clique no front-end até a query de banco de dados no back-end.

## IA + telemetria na prática: dois casos reais

### Caso 1 — Minerador de Bitcoin via vulnerabilidade em Next.js (EW Academy)

A aplicação da comunidade do autor (referida no áudio como "EW Academy", plataforma própria) é um Next.js que foi comprometido por uma vulnerabilidade conhecida do React/Next.js que permitia enviar código arbitrário na requisição e tê-lo interpretado/executado no servidor (RCE). O ambiente estava isolado em Kubernetes, então o atacante conseguiu executar código mas não escalar privilégios nem se espalhar para fora do container.

O autor não sabia inicialmente que havia uma vulnerabilidade — apenas notou um pico de uso de CPU e perguntou ao GitHub Copilot (via seus comandos de Kubernetes) o motivo. O Copilot investigou e reportou: um minerador de Bitcoin rodando em memória, iniciado a partir de um binário em `/tmp` que já havia se autodeletado do disco para se esconder, e que a tentativa de escalar privilégios/se espalhar havia falhado (container isolado).

### Caso 2 — Investigação de erro `500` correlacionando métricas, logs e traces via MCP

Ferramentas citadas: **Grafana MCP** (servidor MCP que expõe Prometheus, Loki e Tempo/Tracing ao editor/agente via Grafana como hub) e **Context7** (para obter documentação atualizada de uma biblioteca e já gerar um PR de correção).

Demonstração: o autor identifica um endpoint retornando muitos erros `500` no dashboard, escreve um prompt simples pedindo para investigar os últimos 15 minutos daquele endpoint e gerar um relatório final. O agente (com acesso aos MCPs configurados) consulta métricas no Prometheus, logs no Loki e traces, e retorna não só o diagnóstico, mas a causa exata em linhas de código específicas (ex.: "linhas 25 a 31: a aplicação não pode inicializar mais de duas conexões de banco simultâneas; é preciso aumentar o limite de conexões"). Detalhe notável: o editor não tinha acesso ao código-fonte do projeto nesse teste — apenas às bases de telemetria via MCP — e ainda assim chegou à causa raiz.

Extrapolação do autor: esse mesmo padrão poderia virar um agente automático rodando a cada deploy (ou disparado por um alerta de endpoint lento/com erro), que investiga, abre um PR de correção sozinho, e o time humano só revisa e aprova — em vez de investigar manualmente do zero.

## Fechamento

OpenTelemetry é um padrão — funciona com qualquer backend de observabilidade compatível (o autor cita explicitamente que ferramentas como New Relic falam o mesmo protocolo). Mensagem final: o valor não está na investigação em si nem na IA isoladamente — está na **coleta de dados**. É a existência dos dados coletados via OpenTelemetry que viabiliza tanto a correlação manual quanto a automação via IA. Recomendação: instrumentar agressivamente, criar alertas, entender logs e o ciclo de vida dos sistemas — o "novo normal" de aplicações caindo, vulneráveis e lentas não é uma fatalidade a ser aceita.
