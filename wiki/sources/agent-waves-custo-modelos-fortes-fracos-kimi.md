---
type: source
title: "Agent Waves + Modelos Fortes e Fracos: Otimizando Custo de API de IA"
aliases: ["agent waves kimi k3 k2", "coordinator worker custo llm", "modelo forte fraco subagentes"]
date_created: 2026-09-04
date_updated: 2026-09-04
source_count: 1
tags: [agent-waves, subagentes, custo-de-ia, kimi, moonshot-ai, opencode, model-routing, cache-de-tokens]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/agent-waves-custo-modelos-fortes-fracos-kimi.md
source_url: ""
author: "desconhecido (canal não identificado na transcrição)"
date_published: "desconhecida"
date_ingested: 2026-09-04
---

## TL;DR

Vídeo apresenta "Agent Waves" — nome recente dado ao padrão já conhecido de orquestração multiagente paralela (coordenador quebra a tarefa em subtarefas, workers executam em paralelo) — e propõe uma alavanca de custo específica: usar um modelo caro/forte (Kimi K3) só no coordenador (planejamento, breakdown, decisão), e delegar toda a implementação a um modelo mais barato (Kimi K2.7 Code). Uma simulação no Google Colab estima R$110/mês com um único agente forte vs. R$73/mês com Agent Waves forte+fraco (~34% de economia). Um teste real na API da Kimi via OpenCode, com a mesma tarefa (preview de e-mail num painel admin), confirma a direção do efeito mas com diferença pequena em valor absoluto (~US$0,42 vs. ~US$0,40, uma economia de só ~US$0,02 — não os ~34% da simulação): o autor atribui a modéstia do ganho ao tamanho pequeno da tarefa testada e a uma implementação deliberadamente não otimizada da estratégia. O achado estrutural mais importante: subagentes usam **mais tokens de input** que um agente único (contexto reinjetado a cada spawn), mas isso só compensa em custo se esses tokens extras forem de um modelo barato — se o coordenador delegar para outro agente caro, a paralelização vira custo puro, sem economia.

## Key Claims

1. **"Agent Waves" é rebatismo de um padrão multiagente já praticado pela comunidade**, não uma técnica nova: um coordenador (primary coordinator) faz o breakdown da tarefa complexa em subtarefas paralelizáveis ("waves"), que são despachadas a workers/subagentes. Confiança alta — o autor é explícito sobre isso ser conhecido antes do nome ganhar tração. Reforça diretamente o "Padrão Orquestrador" já documentado em [[wiki/concepts/subagentes]].
2. **A alavanca de custo específica é atribuir papéis de modelo por função no pipeline**: modelo forte/caro (Kimi K3) restrito ao coordenador — que faz pesquisa, planejamento, breakdown e decisão — e modelo mais barato (Kimi K2.7 Code) para todos os workers de implementação, uma vez que a tarefa já está bem especificada. Este é o núcleo prescritivo da fonte: o ganho de custo do multiagente **depende inteiramente** dessa segregação de modelo por papel — não é uma propriedade automática de paralelizar.
3. **Alerta central e contraintuitivo: usar o mesmo modelo caro em todos os subagentes de um Agent Wave aumenta o custo total, não reduz.** Isso porque cada subagente precisa de contexto próprio reinjetado (arquivos, instruções) — se esse contexto extra for cobrado ao preço do modelo caro, a soma supera a de um único agente forte fazendo tudo sequencialmente sem reinjeção repetida.
4. **Preços citados da Kimi (Moonshot AI), usados na simulação e no teste real:** Kimi K3 — US$15/M output, US$3/M input em cache miss, US$0,30/M input em cache hit; Kimi K2.7 Code — US$1,4/M output, US$0,95/M input em cache miss, US$0,19/M input em cache hit. Isso é uma diferença de custo de input de cerca de 3× a 10× dependendo do regime de cache. Ver [[wiki/entities/moonshot-ai]].
5. **Simulação (Google Colab, cenário hipotético, não benchmark real):** tarefa grande quebrada em 6 subtarefas, repetida 6×/mês, ~700 tokens de input do usuário e ~2.500 tokens de contexto por subagente. Resultado: agente único (K3 só) = R$110/mês; Agent Waves (K3 coordinator + K2.7 worker) = R$73/mês — ~34% de economia. Confiança média: números de uma simulação de brinquedo com estimativas arredondadas pelo autor, não uma medição de sistema real rodando em produção.
6. **No regime de Agent Waves, o volume de input tokens é maior que no agente único**, porque cada subagente novo exige reinjeção de contexto inicial (arquivos, instruções) — o agente único recebe o contexto uma vez só e segue sem reinjetar. Esse aumento de tokens de input é a razão estrutural pela qual delegar a um modelo caro anularia o ganho (Key Claim 3): o próprio mecanismo de paralelização gera overhead de tokens, que só é economicamente seguro se caírem no preço do modelo barato.
7. **Teste real na API da Kimi via [[wiki/entities/opencode|OpenCode]], mesma tarefa (adicionar preview de e-mails num painel admin de newsletter) em dois modos:** agente único com K3 (modo "high"/reasoning alto) custou ~US$0,42 (medido por diferença de saldo antes/depois na plataforma, alterou 6 arquivos, 298 adições/25 remoções, incluiu testes unitários); Agent Waves (K3 coordinator delegando para K2.7 worker, com pedido adicional de criar uma worktree nova) custou uma diferença de saldo equivalente a ~US$0,40 — uma economia de só ~US$0,02, muito abaixo da proporção (~34%) vista na simulação. Confiança média-baixa: é uma única execução de cada cenário, sem repetição para controlar variância, tarefa pequena e simples (baixo volume total de tokens amplifica ruído proporcional).
8. **O próprio autor atribui a discrepância entre simulação (~34% de economia) e teste real (~5% de economia) a dois fatores**: (a) a tarefa testada foi deliberadamente pequena/simples, então o overhead de tokens extra da paralelização (Key Claim 6) consome proporcionalmente mais da economia potencial; e (b) a implementação de Agent Waves usada no teste foi "a mais porca possível" — só um prompt textual pedindo para "planejar e delegar", sem uma pipeline de orquestração real, specs estruturadas, ou fluxo automático — e ainda gerou trocas de conversa extras (o agente perguntou o que fazer com uma worktree que já tinha alterações), consumindo tokens que o cenário do agente único não teve. Esta é uma explicação não testada — o autor não rodou uma versão "bem feita" de Agent Waves para confirmar quanto da diferença viria de cada fator.
9. **A economia projetada deveria aumentar com a escala/complexidade da tarefa** (mais subtarefas paralelizáveis, mais volume de implementação por worker) — mas isso é conjectura do autor, não testado neste vídeo com uma segunda tarefa maior. Mesmo padrão de extrapolação não verificada já registrado em [[wiki/sources/subagentes-quando-vale-a-pena-custo-velocidade-tlc-spec-driven]] para o eixo de granularidade de subagentes.
10. **A Moonshot AI oferece tanto acesso via API paga por token quanto assinatura mensal com créditos** (citada com faixa de preço de alguns dólares a ~US$199/mês) — mencionado como alternativa de acesso, sem comparação de custo-benefício entre os dois modelos de cobrança para o caso de uso do vídeo.

## Entidades e Conceitos Tocados

- [[wiki/concepts/subagentes]]
- [[wiki/concepts/roteamento-automatico-de-modelo]]
- [[wiki/entities/moonshot-ai]]
- [[wiki/entities/opencode]]
- [[wiki/concepts/ai-gateway-llm-router]]
- [[wiki/concepts/cache]]

## Contradições / Reforços com o Resto da Wiki

**Reforço direto e complementar:** [[wiki/concepts/subagentes]] já documentava o "Padrão Orquestrador" (subagente CTO despachando para especialistas) e um benchmark de granularidade de subagentes ([[wiki/sources/subagentes-quando-vale-a-pena-custo-velocidade-tlc-spec-driven]]) mostrando que *quantos* subagentes usar afeta custo/qualidade/tempo. Esta fonte adiciona um eixo ortogonal e até então ausente na página: não "quantos subagentes", mas "qual modelo cada papel do pipeline deve usar" — o benchmark do TLC Spec Driven usava aparentemente o mesmo modelo em todos os subagentes (o texto daquela fonte não distingue modelo do coordenador vs. modelo dos workers); esta fonte torna essa distinção explícita e argumenta que ela é a alavanca de custo mais direta, potencialmente complementar (não excludente) à otimização de granularidade já registrada.

**Reforço direto e específico:** [[wiki/concepts/roteamento-automatico-de-modelo]] já catalogava vários eixos de roteamento (custo/complexidade via classificador, categoria estática do Custom Router da Abacus, tolerância a guardrail). Esta fonte introduz um eixo novo — roteamento **por papel dentro de um único pipeline multiagente** (coordenador vs. worker), diferente de todos os casos anteriores, que roteavam entre *requisições/tarefas independentes*, não entre *papéis hierárquicos da mesma tarefa*.

**Reforço direto:** [[wiki/entities/moonshot-ai]] já tinha uma linha sobre o Kimi K3 vencendo o Fable em custo num benchmark do Cline ([[wiki/sources/precificacao-ancoragem-anthropic-opus-5-lancamento]]). Esta fonte adiciona preços granulares por regime de cache (hit/miss) dos próprios K3 e K2.7, e um caso de uso concreto onde o próprio K3 é tratado como "o caro" dentro da família Kimi (contraste interno, não com outro provider).

**Sem contradição identificada.** A fonte não conflita com nenhuma claim anterior da wiki; ela é consistente com o modelo geral de "triângulo custo × performance × qualidade" já em [[wiki/concepts/ai-gateway-llm-router]].

## Open Questions

- **Discrepância entre simulação (~34% de economia) e teste real (~5%) não foi reconciliada com uma segunda medição controlada** — o autor especula duas causas (tamanho da tarefa, implementação "porca" do Agent Wave) mas não isola qual pesa mais, nem testa uma versão mais bem estruturada da técnica para comparar.
- **Não há repetição de execução para controlar variância** — cada cenário (agente único, Agent Waves) rodou uma única vez; diferenças de saldo de poucos centavos de dólar são sensíveis a ruído de execução (ex.: o agente único poderia ter tido sorte e feito menos iterações).
- **Autor/canal não identificado** no texto da transcrição fornecida — sem nome completo ou link do vídeo, não é possível verificar a fonte original nem localizar a planilha/notebook do Google Colab citado.
- **Preços exatos do Kimi K3/K2.7 não foram verificados contra a documentação oficial da Moonshot** — números vêm apenas da leitura de tela do autor no vídeo, sem link para a página de pricing.

## Raw Quotes

> "Se vocês esverem trabalhando com Agent Waves mas na Agent Wave de vocês vocês usam sempre o mesmo modelo que é o modelo mais caro, vocês estão só gastando mais."

> "Eu não tenho que olhar só para tokens, eu tenho que olhar para custo final também."

> "A estratégia ali de Agent Wave que eu segui foi a pior de todas, a mais porca possível."
