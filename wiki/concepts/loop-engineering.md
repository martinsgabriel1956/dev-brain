---
type: concept
title: "Loop Engineering"
aliases: ["loop engineering", "engenharia de loop", "loop de harness", "loop fixo", "loop criador"]
date_created: 2026-07-10
date_updated: 2026-07-24
source_count: 2
tags: [loop-engineering, harness, agente, automacao, planner-executor-critic, loop-fixo, loop-criador, spec-driven]
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
