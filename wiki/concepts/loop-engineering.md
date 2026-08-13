---
type: concept
title: "Loop Engineering"
aliases: ["loop engineering", "engenharia de loop", "loop de harness", "loop fixo", "loop criador"]
date_created: 2026-07-10
date_updated: 2026-08-12
source_count: 7
tags: [loop-engineering, harness, agente, automacao, planner-executor-critic, loop-fixo, loop-criador, spec-driven, ralph-loop, anthropic, graph-engineering, loop-deterministico, loop-agentico, judge-pattern, orquestracao-de-modelos]
skill: tech-mentor-ai
status: stable
---

# Loop Engineering

Prática de desenhar o **ciclo completo** ao redor de um ou mais agentes — desde a entrada até a resposta final — como uma estrutura reutilizável e disparável automaticamente, em vez de escrever prompts manuais para cada tarefa. É o degrau seguinte a [[wiki/concepts/harness|harness engineering]] na progressão de abstração: prompt engineering melhora uma chamada, [[wiki/concepts/context-engineering-harness|context engineering]] melhora o contexto de uma chamada, harness engineering melhora o ambiente ao redor do modelo como um todo, e loop engineering melhora o ciclo inteiro que se repete.

## A Frase que Resume a Ideia

"Você não faz o prompt no agente, você desenha o sistema que faz o prompt." O trabalho de quem constrói o loop deixa de ser escrever instruções por tarefa e passa a ser desenhar a estrutura que gera instruções (e critérios de validação) para N tarefas, indefinidamente.

## Os Três Níveis do Dev Loop Anteriores ao Termo

Antes do termo "loop engineering" virar hype, já existia uma progressão de três níveis ([[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]]):

1. **Loop React** — um prompt, o agente itera (ferramentas, observação, próxima ação) até resolver aquele prompt. Primeiro loop agêntico popularizado, permite tarefas de minutos.
2. **Spec Driven** — o humano dá uma "receita" que dispara vários loops React em sequência (planejar → design → uma task por vez). Ver [[wiki/concepts/spec-driven-development]] e [[wiki/concepts/task-looper]]. Permite tarefas de horas.
3. **Humano no loop** — entre specs, um humano decide o próximo passo: abre PR, faz triagem de bug, consulta métricas, planeja a próxima spec. Ver [[wiki/concepts/human-in-the-loop]].

Loop engineering é proposto como uma **quarta camada**, que automatiza a decisão que antes cabia ao nível 3 — permitindo ir de "horas numa spec" para "dias em vários planos", possivelmente disparado por evento (ex.: puxar um incidente de observabilidade, triar, planejar, notificar, implementar, abrir PR), sem exigir necessariamente o formato de spec.

## Loop Agêntico vs. Cron Job

A diferença central entre um loop agêntico e um Cron Job/`while` tradicional: no Cron Job, um `if` determinístico decide se o loop continua. No loop agêntico, é o próprio modelo que interpreta um estado (ex.: um roadmap) e decide, de forma não determinística, se há mais itens e se deve prosseguir para o próximo.

## Loop Fixo vs. Loop Criador

Distinção proposta em [[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]] (nomenclatura própria do autor da fonte, não padronizada na indústria):

- **Loop fixo** — sem side effect cumulativo entre execuções; a segunda rodada não piora por causa da primeira. Exemplo: uma skill que orquestra três subagentes (`planner`, `implementer`, `evaluator`) para rodar avaliações repetidas de frameworks de spec driven. Considerado seguro; uso típico em automações.
- **Loop criador** — gera um roadmap, constrói algo a partir dele, gera outro roadmap com base no resultado, e assim por diante até compor uma aplicação inteira. Muito mais arriscado: bugs introduzidos numa iteração se perpetuam nas iterações seguintes que constroem em cima deles. Foi o padrão relatado na migração do Ban para Rust (>500.000 linhas de código) e replicado pelo autor da fonte na construção de um jogo completo em um final de semana.

### Pré-condição de Sucesso do Loop Criador: Referência Sólida

Um loop criador funciona bem quando existe algo sólido para validar contra — uma engine/codebase de referência ou uma suíte de testes robusta pré-existente (o Ban tinha, segundo a fonte, ~1,3 milhão de asserções de teste antes da migração — número não verificado de forma independente). Sem essa referência, o risco de divergência silenciosa entre iterações é alto.

### Memória Entre Iterações do Loop Criador

Três artefatos usados para dar contexto a cada nova iteração do loop: `lessons.md` (lições aprendidas, evita repetir erros já resolvidos), *state* (o que foi feito numa fase, incluindo blockers) e *handoff* (o que o próximo agente precisa saber ao fim de uma fase grande). O loop criador **não gera o próprio roadmap** — decidir o próximo roadmap continua sendo decisão humana; o loop só executa o que já está definido.

## Quatro Perguntas Para Decidir se Vale Usar um Loop

1. Existe um bom [[wiki/concepts/harness]] — a ponto de quase não revisar PRs manualmente?
2. O feedback (testes, lint, compilador) é rápido?
3. Existe uma *stop condition* confiável que aciona o humano?
4. Há backlog suficiente para compensar o custo de montar a estrutura de loop, versus simplesmente planejar e fazer manualmente?

## Loop Determinístico vs. Loop Agêntico

Divisão prática proposta em [[wiki/sources/loop-engineering-padroes-loop-deterministico-agentico]] (vídeo 2 da série de [[wiki/entities/pedro-nauke]]) como "a mais importante de todas" na hora de decidir modelo e custo:

- **Loop determinístico** — um script que, a cada novo round, abre uma sessão nova: todo o contexto anterior é descartado e um novo contexto é iniciado do zero. Exemplo: o [[wiki/concepts/spec-driven-development|Compose]]. Como cada round não lembra do anterior, precisa de um arquivo de **memória transitória** gravado em disco (via system prompt: ao fechar a run ou antes de compactar, grava o que aconteceu) para a próxima run recuperar contexto.
- **Loop agêntico** — via comando `/go` (implementado, com variações, pela maioria dos harnesses atuais — Claude Code, Codex, Hermes), nunca abre uma run nova: fica iterando na mesma run, compactando o contexto conforme enche. Depende não só do modelo, mas também da qualidade de compactação do harness. Quem julga se a run terminou é o próprio modelo — daí a importância de bons gates de verificação.

### Custo do Contexto Inicial em Modelos de Reasoning Alto

Em modelos de reasoning muito alto (GPT 5.6/Sol, Fable), o trecho mais custoso é a **formulação inicial do contexto**. No loop determinístico, quanto maior o reasoning do modelo, pior o resultado de custo — esse gasto de formulação de contexto é pago run atrás de run e descartado a cada novo round. Regra prática: se o loop já tem bom aparato de artefatos de estado salvos, um modelo com reasoning mais baixo evita pagar caro por raciocínio que será jogado fora. O mesmo raciocínio se aplica a tasks de spec driven já bem definidas — reasoning muito alto faz cada task demorar mais do que precisaria, porque o modelo sempre raciocina bastante mesmo quando a tarefa já está clara. Ver [[wiki/concepts/reasoning-level]].

### Teste do Autor: Breakdown de Tasks Melhora Resultado Mesmo em Loop Agêntico

Comparação reportada em [[wiki/sources/loop-engineering-padroes-loop-deterministico-agentico]]: spec driven quebrado em tasks (determinístico), spec driven quebrado em tasks (agêntico), e execução sem quebra de tasks (spec inteira direto pro loop). Resultado: sem breakdown prévio de tasks, o resultado piora tanto na definição de tarefas em runtime quanto na execução. Com artefatos de estado e breakdown definidos previamente (critérios de sucesso, lista de testes por task), o resultado melhora — inclusive em loop agêntico. Isso contraria a leitura popular de que "spec driven morre" em loops agênticos de long-running tasks.

## Padrão Judge

Um segundo agente sobe **em background** ao final de cada run e julga se a tarefa proposta foi de fato concluída — ele é "o dono da verdade", não o modelo que executou a run ([[wiki/sources/loop-engineering-padroes-loop-deterministico-agentico]]). Implementação típica via **stop hook** (a maioria dos harnesses já oferece): ao modelo sinalizar stop, o hook dispara o agente juiz (via comando ou integração no harness); se o juiz decide que a tarefa não terminou, ele mesmo gera um novo prompt contendo o que falta, fechando o ciclo de forma determinística por fora do modelo executor.

Mais útil em modelos menos densos em long-running tasks (cita Opus, Grok, Sonnet como exemplos que encerram o loop cedo demais em tarefas de horas). Em modelos frontier de reasoning muito alto (Fable, GPT 5.6) — capazes de sustentar um loop sozinhos por dias — o autor da fonte considera o judge um gasto desnecessário. É uma variante especializada do papel de Critic em [[wiki/concepts/planner-executor-critic]]: em vez de atuar dentro do ciclo planner→executor→critic, o judge atua **depois** que o modelo já declarou a run concluída, disparado por infraestrutura de hook do harness.

## Padrão Orquestrador de Modelos

Em vez de o modelo mais caro/denso implementar a tarefa, ele **orquestra** outros modelos mais baratos para implementação (e até review) por tipo de tarefa ([[wiki/sources/loop-engineering-padroes-loop-deterministico-agentico]]). No Compose (loop determinístico), isso é configuração direta por task. Em loop agêntico, precisa ser passado via prompt para um agente orquestrador, que decide dinamicamente qual modelo usar por tarefa — exemplo do autor: GPT 5.6 (reasoning medium) para back-end mais barato, Opus 4.8 ou Grok 4.5 para front-end mais rápido e barato. Resultado relatado: ganho tanto em custo de token quanto em velocidade de execução.

## Gerenciamento de Estado via Arquivo (Sem Precisar Ser Determinístico)

Pode ser feito via prompt ou skill, sem exigir código: pedir ao agente para manter um arquivo de estado (tipicamente `.md`, ex.: `state.md`) que trackeia tarefa concluída, próxima tarefa, lista de tarefas, decisões tomadas, erros e arquivos modificados. Numa spec de 10 tasks, o próprio agente cria esse arquivo com todas as informações para executar as 10 tasks uma por uma, seguindo um padrão formalizado ([[wiki/sources/loop-engineering-padroes-loop-deterministico-agentico]]). Ver implementação equivalente (roadmap + `lessons.md` + state + handoff) em [[wiki/concepts/task-looper]].

## Skills como Encapsulamento de Loop Não Determinístico

Uma skill pode dar toda a estrutura organizacional a um loop de spec driven: gerenciamento de estado, o que olhar na spec, gates de verificação, verificações finais, o que fazer após cada task, o que escrever de memória no output final — e pode habilitar outras skills durante a leitura, encadeando um processo. Fluxo relatado: task a task → skills de report e execution ao terminar a spec → skill de deep review, que gera issues resolvidas na mesma run → opcionalmente abre PR com description e squash merge, tudo autonomamente ([[wiki/sources/loop-engineering-padroes-loop-deterministico-agentico]]).

## Componentes de um Loop

Um loop de harness combina, tipicamente:

1. **[[wiki/concepts/planner-executor-critic|Planner]]** — LLM que decompõe a entrada em subtarefas, gerando prompt e [[wiki/concepts/rubrica-de-verificacao|rúbrica]] para cada uma
2. **Subagentes executores** — cada um recebe seu prompt gerado dinamicamente e produz um resultado (ver [[wiki/concepts/subagentes]])
3. **Verificador** — um modelo diferente do executor, que julga o resultado contra a rúbrica e aprova ou gera follow-up
4. **[[wiki/concepts/grafo-como-abstracao-de-agentes|Grafo]]** — a estrutura que controla o fluxo entre esses componentes, com condições de parada definidas por quem constrói o sistema (não pela LLM)

## Origem: o Padrão ReAct (2022/2023)

A ideia central de loop engineering não é nova em 2026 — vem do padrão **ReAct** (Reason + Act), de 2022/2023: um ciclo que agrega a resposta anterior ao contexto e repete até concluir a tarefa, compondo o próximo contexto a cada volta. Esse loop mínimo (`while` que acumula tool calls e respostas) é a base de todo [[wiki/concepts/ciclo-agente|agent loop]] e de todo sistema agêntico por trás dos harnesses atuais — não é peça nova, é o padrão sobre o qual harness e loop engineering foram construídos ([[wiki/sources/loop-engineering-harness-e-a-frase-que-viralizou]]).

## O Que Destravou Loops Longos em 2026 (Não Foi a Ideia do Loop)

Se a ideia do loop já existia desde o ReAct, o que mudou em 2026 foram três fatores externos à ideia em si:

1. **Modelos frontier aguentando long tasks** — reasoning atual permite planejar e decidir o próximo passo por horas/dias sem se perder; modelos menores/open source ainda se perdem depois de poucos passos.
2. **Harness evoluindo em compactação de contexto** — alimentado por um ciclo de retroalimentação: logs e tool calls gerados pelos harnesses viram dado de treinamento para versões futuras dos modelos.
3. **Estado persistente em arquivo/board** — um bom harness escreve o progresso em markdown no filesystem em vez de manter a tarefa inteira "na cabeça"; permite que a conversa estoure o contexto sem perder o ponto onde parou.

## Correção: "Loop Engineering Matou Harness Engineering" é uma Leitura Invertida

A frase que viralizou junto com o termo — "loop engineering é maior que harness engineering" ou "matou harness engineering" — inverte a relação real: **o loop contém o harness**, não o substitui. Tudo que sustenta um loop rodando por horas sem quebrar (compactação de contexto, estado persistente, execução confiável de tool calls) é harness, não loop; o loop é só o ciclo que roda por cima. Sem harness sólido por baixo, nenhum modelo — por mais inteligente — sustenta esse ciclo ([[wiki/sources/loop-engineering-harness-e-a-frase-que-viralizou]]).

## Origem Recente: o Ralph Loop (Geoffrey Huntley, Julho de 2025)

Entre o padrão ReAct (2022/2023) e o guia oficial da Anthropic (2026) há um ponto intermediário: em julho de 2025, o engenheiro australiano [[wiki/entities/geoffrey-huntley]] publicou o **Ralph Loop** — uma técnica deliberadamente simples, descrita como "uma linha de bash" que pega um prompt, manda para o agente, e roda de novo se a tarefa não terminou. Batizado em homenagem a Ralph Wiggum, personagem d'Os Simpsons, por ser tão simples que "parecia piada". Um ano depois, virou disciplina — a Anthropic publicou o guia oficial "Getting Started with Loops" ([[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]]). Ver [[wiki/concepts/ralph-loop]] para o stub dedicado.

## Os Quatro Níveis Oficiais de Loop (Guia da Anthropic)

Framework paralelo ao dos "três níveis do dev loop" acima (autor e nomenclatura diferentes, mesma progressão de autonomia crescente), atribuído ao guia oficial "Getting Started with Loops" da [[wiki/entities/anthropic]]:

1. **Turn-based** — cada prompt enviado já é o próprio loop: o agente coleta contexto, age, executa, checa, repete e responde. O humano dirige cada rodada. É o que a maioria já faz.
2. **Goal-based** — o humano entrega a condição de parada (ex.: "roda até os testes passarem", "roda até o build compilar"). O agente não para quando *acha* que terminou — para quando o critério objetivo é atingido. Quem já pratica [[wiki/concepts/tdd|TDD]] com testes escritos antes do código já tem o pré-requisito deste nível — os testes servem tanto de verificação quanto de condição de parada do loop.
3. **Time-based** — o humano entrega o gatilho (trigger); o loop roda em intervalo ou agendado, sem presença humana.
4. **Proactive** — o humano entrega só o prompt; o sistema observa e decide o quê e quando agir.

([[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]])

## Diferença para Harness Engineering

Harness engineering melhora o ambiente de uma única execução (tools disponíveis, contexto, memória — ver [[wiki/concepts/harness]]). Loop engineering trata a execução inteira como uma unidade repetível: o mesmo loop pode ser disparado por um prompt do usuário, por um schedule (ex.: rodar toda meia-noite verificando queda de vendas) ou por um evento externo, sem alterar a estrutura.

## Limite do Loop: Uma Métrica Nunca é Suficiente

[[wiki/sources/graph-engineering-do-loop-ao-grafo]] propõe [[wiki/concepts/grafo-como-abstracao-de-agentes|grafo]] como o degrau seguinte ao loop, motivado por um limite específico: um loop otimizando uma condição de parada baseada numa única métrica (ex.: reduzir CAC numa campanha) pode estar cego para outra métrica que piora em consequência (churn), derrubando o LTV e invalidando o próprio ganho (ver [[wiki/concepts/ltv-cac]]). A fonte atribui a ideia a um tweet de [[wiki/entities/peter-steinberger]] e especula que a origem prática do termo "graph engineering" foi ele rodando múltiplos loops em paralelo (~US$ 1 milhão/mês em tokens, segundo a fonte) até que esses loops começassem a conflitar entre si ou operar sobre informação desatualizada — motivando substituir "prompt + ticket" por um grafo passado a um orquestrador.

## Mudança de Nível de Abstração

Em vez de "eu crio código para resolver um problema", o loop resolve "uma categoria de problemas": o mesmo sistema (planner + subagentes + verificador) se adapta a diferentes entradas dentro do mesmo domínio, gerando harnesses dinamicamente para cada instância do problema.

## Risco Reconhecido: Não é o AutoGPT de Novo

Loops totalmente autônomos sem verificação (padrão AutoGPT/"AFF Loop") historicamente não avançaram — viravam sistemas rodando sem controle e sem garantia de qualidade. O que diferencia loop engineering, como descrito nesta fonte, é a combinação de rúbrica explícita + verificador com modelo distinto do executor + critério de parada definido pelo autor do sistema.

## Quando Vale a Pena

Para trabalho corporativo, pesquisa interna e entendimento de cliente (knowledge work), o padrão é descrito como altamente vantajoso. Para produção de codebase onde qualidade importa e token não é ilimitado, ainda é necessário um engenheiro por perto nos momentos de decisão — ver tensão equivalente em [[wiki/sources/vibe-coding-limites-maturidade-profissional]].

## Key Sources

- [[wiki/sources/loop-engineering-planner-critic-grafo]]
- [[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]] — taxonomia dos três níveis do dev loop, distinção loop fixo/loop criador, caso Ban→Rust, quatro perguntas de decisão
- [[wiki/sources/loop-engineering-harness-e-a-frase-que-viralizou]] — origem no padrão ReAct (2022/2023), três fatores que destravaram loops longos em 2026, correção da frase viral "loop engineering matou harness engineering"
- [[wiki/sources/loop-engineering-padroes-loop-deterministico-agentico]] — vídeo 2 da série de Pedro Nauke: divisão loop determinístico/agêntico, custo de contexto inicial em modelos de reasoning alto, padrão judge (stop hook), padrão orquestrador de modelos, gerenciamento de estado via `state.md`, skills como encapsulamento de loop
- [[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]] — origem do Ralph Loop (Geoffrey Huntley, julho de 2025); os quatro níveis oficiais de loop do guia da Anthropic (turn-based, goal-based, time-based, proactive)
- [[wiki/sources/vibe-coding-jogos-um-prompt-vs-varios-estagios-produto]] — "o teu único prompt na verdade vira 20-30 prompts": o agente faz teste end-to-end, verifica se o jogo funciona e itera até o resultado; loop goal-based aplicado a construção de jogo
