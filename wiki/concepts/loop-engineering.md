---
type: concept
title: "Loop Engineering"
aliases: ["loop engineering", "engenharia de loop", "loop de harness", "loop fixo", "loop criador"]
date_created: 2026-07-10
date_updated: 2026-07-28
source_count: 4
tags: [loop-engineering, harness, agente, automacao, planner-executor-critic, loop-fixo, loop-criador, spec-driven, ralph-loop, anthropic]
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
- [[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]] — origem do Ralph Loop (Geoffrey Huntley, julho de 2025); os quatro níveis oficiais de loop do guia da Anthropic (turn-based, goal-based, time-based, proactive)
