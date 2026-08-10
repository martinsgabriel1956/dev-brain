# Monitoramento de Aplicações na Era da IA com Grafana Cloud e OpenTelemetry

Transcrição de fala corrida em português, limpa de erros de reconhecimento de fala, pontuada e organizada em seções. Vídeo do criador de conteúdo Eric (ver [[wiki/entities/eric-lenda]] — no áudio original o nome do canal foi transcrito de forma distorcida como "Eric Wend"/"Eric Winda"; mantido como o mesmo autor já catalogado na wiki por sobreposição total de tema, estilo e formato com [[wiki/sources/observabilidade-ponta-a-ponta-opentelemetry-ia-amsterdam]] — canal de Node.js/JavaScript, especialista em performance de aplicações). Vídeo patrocinado pelo Grafana Cloud, demonstrando a plataforma na prática com uma aplicação de exemplo com bug proposital.

Nota de transcrição: nomes de ferramentas corrigidos por inferência de contexto técnico (ex.: "Post SQL"/"posts" → PostgreSQL; "útil config" → `otel-config`/arquivo de configuração; "aluminos" → nome do serviço de exemplo, mantido como transcrito por ser só um identificador arbitrário criado pelo autor). Trecho de indicação de patrocínio de mentoria de carreira internacional (bloco solto no meio do vídeo, sem relação com o conteúdo técnico) foi resumido em vez de transcrito literalmente, por não ser o foco da wiki.

## Abertura: por que monitoramento importa mais na era da IA

Monitorar aplicações nunca foi tão importante quanto agora: entender o estado da aplicação, a velocidade dos times, como as APIs se relacionam entre si, e identificar problemas graves que muitas vezes passam despercebidos. A ferramenta apresentada é o Grafana, usada para coletar métricas, logs e traces e exibir tudo em dashboards — com destaque para um assistente de IA embutido que, a partir de prompts, gera relatórios, ajuda a entender o que está acontecendo na aplicação, cria alertas e os envia para canais como Discord.

## O problema histórico do monitoramento

Administrar logs, traces e métricas sempre foi uma tarefa confusa, complexa e cara: o volume de dados costuma ser alto, e estruturar o armazenamento correto exige trabalho. Levar isso para infraestrutura on-premise geralmente exige um especialista dedicado. A alternativa apresentada resolve isso sem custo inicial: a aplicação de demonstração envia todos os dados via **OpenTelemetry**, protocolo aberto que funciona com qualquer linguagem de programação.

## Grafana Cloud — primeiros passos

O Grafana pode ser usado open source e self-hosted (Docker Compose, Kubernetes), mas guardar grandes volumes de dados e correlacioná-los bem para investigar problemas graves é trabalhoso nesse modo. Por isso a demonstração usa o **Grafana Cloud** (parceiro do vídeo): conta gratuita, sem necessidade de cartão de crédito.

No painel inicial já existe um chat de assistente de IA. A plataforma permite criar dashboards e visualizar:

- **Métricas** — dados acumulados ao longo do tempo (tempo de resposta, duração de queries de banco de dados etc.).
- **Logs** — os "prints" que registram qual linha/processo executou, se um `if` foi satisfeito etc.
- **Traces** — mapeamento de qual linha/serviço executou o quê, permitindo montar a árvore de execução completa de uma requisição (ex.: API A chamou API B, que chamou um banco de dados, que coletou dados de um arquivo).

A correlação entre esses três sinais é descrita como o diferencial mais poderoso da ferramenta — sem isso, ou se paga caro para concorrentes, ou a aplicação roda "cega" até o pior acontecer.

Ao criar a conta, o Grafana Cloud já sobe automaticamente uma série de serviços prontos (visíveis em **Data Sources**): armazenamento de logs, gerenciamento de cardinalidade, analytics etc. — sem qualquer configuração manual.

## Instrumentando a aplicação de exemplo com OpenTelemetry

Fluxo seguido na demonstração, a partir do menu de onboarding do Grafana Cloud:

1. Selecionar o SDK do **OpenTelemetry** (não um SDK proprietário do Grafana) — isso garante que, se o Grafana for trocado por outra ferramenta no futuro, o código da aplicação não precisa mudar, só o backend de destino.
2. Selecionar a linguagem (JavaScript/Node.js no exemplo — o Grafana também tem instrumentação para frontend).
3. Selecionar a infraestrutura (Linux, mesmo rodando localmente em um Mac).
4. Escolher o modo de envio: **Direct** (aplicação envia direto para o endpoint do Grafana Cloud) — alternativa a rotear primeiro por um OpenTelemetry Collector já existente na própria infraestrutura do usuário (útil quando já existe um Collector local e se quer *também* espelhar os dados para o Grafana Cloud).
5. Criar um token de autenticação (nomeado livremente).
6. Configurar variáveis de ambiente: endpoint do serviço que recebe os dados, forma de autenticação, protocolo de comunicação.

A aplicação de exemplo (Fastify, dois endpoints — um health check e um endpoint que dispara as operações de negócio) já tem essas variáveis aplicadas num arquivo de configuração do OpenTelemetry, incluindo uma boa prática: em vez de enviar cada evento imediatamente, os dados são acumulados em memória e enviados **em lote** (batch) para a nuvem, reduzindo custo e sofrimento de rede.

A stack de infraestrutura sobe primeiro o PostgreSQL (`npm run infra:up`) e, depois, a aplicação (`npm start`), que já começa a emitir métricas, logs e traces para o Grafana Cloud sem qualquer configuração adicional além das variáveis de ambiente.

## Explorando os dados chegando no Grafana

Ao rodar a aplicação, ela gera um novo ID de serviço a cada inicialização (por isso aparecem múltiplas entradas de "aluminos" — nome do serviço de exemplo — no painel, uma por execução).

- Em **Metrics**: duração de chamadas HTTP, tempo de operações de banco, e métricas internas do próprio Node.js — tudo automático via OpenTelemetry.
- Em **Logs**: a exploração revelou uma taxa de erros HTTP `304`/erro de processamento, incluindo um timeout — sem que o autor tivesse olhado o código-fonte para saber o que causava isso.
- Em **Traces**: cada requisição rastreada nos últimos 30 minutos, com atributos como endpoint, IP, URL. As queries usam **PromQL**, linguagem específica do ecossistema Prometheus/Grafana para métricas e traces — uma barreira comum de aprendizado quando cada ferramenta de observabilidade tem sua própria linguagem de query.

## O assistente de IA do Grafana Cloud correlacionando logs, métricas e traces

Em vez do fluxo manual tradicional (entrar log a log, cruzar IDs entre bases, até achar a causa raiz), a demonstração usa o **chat assistente embutido no Grafana Cloud** — disponível diretamente na interface web, sem custo adicional de créditos de IA do editor de código do usuário. O assistente mantém contexto da aba ativa (muda o foco conforme se navega entre logs/métricas/traces) e aceita prompts em linguagem natural, prints, e pedidos para editar dashboards.

Prompt usado na demonstração (aproximado): pedir para o assistente investigar por que a aplicação "aluminos" está apresentando erros, correlacionando logs, métricas e traces, e mostrar um relatório do que pode estar acontecendo, incluindo a linha de código exata — sem fornecer nenhum contexto adicional sobre a aplicação.

Resultado:

- O assistente consultou automaticamente as três bases de dados (logs, métricas, traces) sem receber instruções de quais consultar.
- Gerou um relatório incluindo um diagrama Mermaid do fluxo do problema.
- Identificou a causa raiz: um bug na linha 52 do arquivo principal, onde uma conexão com o PostgreSQL é aberta e nunca é encerrada — esgotando o pool de conexões e causando os timeouts observados nos logs.
- Sugeriu o fix diretamente no relatório.

Verificação manual: o autor conferiu a linha apontada no editor de código e confirmou que era exatamente o comentário deixado de propósito no código de demonstração, validando a linha exata gerada pelo assistente.

A partir da mesma tela, o Grafana Cloud também permite:

- Criar um alerta de erros para a aplicação específica diretamente do relatório gerado.
- Criar dashboards automaticamente a partir da conversa.
- Configurar integração com GitHub (via **Integration Settings** → quick setup) para que o assistente possa abrir Pull Requests com a correção diretamente no repositório.

## Grafana MCP como alternativa via editor de código

Para quem prefere não sair do editor, existe o **Grafana MCP** (já coberto em vídeo anterior do canal), que permite fazer as mesmas perguntas de dentro do editor de código (ex. Claude Code) — mas nesse caminho o consumo é de créditos de IA do próprio editor do usuário. O fluxo via chat web do Grafana Cloud não consome esses créditos. Um teste rápido via editor ("quantos erros ocorreram na aplicação aluminos nos últimos 5 minutos") mostrou funcionamento equivalente, consultando Prometheus/logs conforme a pergunta.

## Extensibilidade: Skills do assistente

O Grafana Cloud permite configurar **skills** para o assistente — contexto adicional ensinando à IA o que colunas/campos específicos de uma fonte de dados significam, o que ajuda quando a fonte de dados é menos padronizada ou o assistente precisa de mais contexto de domínio para responder bem.

## Fechamento: por que instrumentar

Grafana é open source e gratuito, usado pelo autor há anos. Aplicações críticas em produção exigem: armazenamento seguro de dados de observabilidade, capacidade de correlacionar esses dados, e um "guia" para reconstruir o que aconteceu num incidente (inclusive para diferenciar um bug recorrente de uma invasão). Recomendação de não ficar preso a um único vendor — o OpenTelemetry como padrão aberto é o que garante portabilidade entre ferramentas de observabilidade.

Nota sobre o plano gratuito do Grafana Cloud: ao criar a conta aparece um período de trial de 15 dias, mas existe um **plano gratuito permanente** (sem expiração) além do trial, adequado para uso pessoal e para conhecer a ferramenta antes de contratar um plano pago para produção crítica.
