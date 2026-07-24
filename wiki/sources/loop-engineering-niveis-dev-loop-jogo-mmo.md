---
type: source
title: "Loop Engineering: Os Níveis do Dev Loop e um Jogo Completo Construído em um Final de Semana"
aliases: ["loop fixo", "loop criador", "dev loop", "níveis do dev loop", "loop engineering jogo mmo"]
date_created: 2026-07-24
date_updated: 2026-07-24
source_count: 0
tags: [loop-engineering, harness, spec-driven, ai-para-devs, rust, ban, playwright, e2e, tlc-spec-driven]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/loop-engineering-niveis-dev-loop-jogo-mmo.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-07-24
---

## TL;DR

Vídeo opinativo que propõe uma taxonomia de três níveis pré-existentes do "dev loop" (loop React → spec driven → humano no loop) e posiciona **Loop Engineering** como uma quarta camada acima, que tira o humano do ciclo de decisão entre specs. Introduz uma distinção nova em relação a outras fontes da wiki: **loop fixo** (sem side effect acumulado, ex.: avaliação de frameworks) vs. **loop criador** (gera roadmap → constrói → gera novo roadmap, com side effects reais e risco de perpetuar bugs — o padrão usado na migração do Ban para Rust). Demonstra o padrão com um estudo de caso próprio: um jogo completo construído em um final de semana com um framework chamado "TLC Spec Driven" rodando em loop, usando roadmap + `lessons.md` + state + handoff como memória entre iterações. Encerra com quatro perguntas objetivas para decidir se vale usar loop (harness bom, feedback rápido, stop condition confiável, backlog suficiente).

## Key Claims

1. **Taxonomia de três níveis do dev loop, anterior ao boom de "loop engineering"**: (1) *loop React* — um prompt, o agente itera sozinho até resolver aquele prompt (ReAct, primeiro loop agêntico popularizado); (2) *spec driven* — uma "receita" humana aciona vários loops React em sequência (planejar, design, uma task por vez), permitindo tarefas de horas em vez de minutos; (3) *humano no loop* — entre specs, o humano decide o próximo passo, faz triagem de bug, abre PR, consulta métricas.
2. **Loop Engineering = mais uma camada acima do nível 3**, automatizando a decisão que antes cabia ao humano entre specs — permitindo ir de "horas numa spec" para "dias em vários planos", potencialmente disparado por evento (ex.: puxar um incidente do Datadog, criar task, planejar, notificar, implementar, abrir PR) sem necessariamente usar o formato de spec.
3. **Diferença central entre loop agêntico e Cron Job/`while`**: no Cron Job um `if` determinístico decide se continua; no loop agêntico é o próprio modelo que interpreta um estado (ex.: um roadmap) e decide se há mais itens e se deve continuar — decisão não determinística, feita pelo modelo, não por código de controle.
4. **Loop fixo vs. loop criador (nomenclatura própria do autor, admitidamente não padronizada na indústria)**: loop fixo não tem side effect cumulativo entre execuções (ex.: uma skill "bench run" que orquestra três subagentes — `planner`, `implementer`, `evaluator` — para avaliar frameworks de spec driven; útil para automações, considerado seguro). Loop criador gera um roadmap, constrói algo, gera outro roadmap a partir do resultado, e assim por diante, até compor uma aplicação inteira — extremamente mais arriscado porque bugs gerados numa iteração se perpetuam nas iterações seguintes que constroem em cima deles. Foi o padrão usado na migração do Ban para Rust (>500.000 linhas).
5. **Estudo de caso — jogo completo construído em um loop criador durante um final de semana**: usando uma engine open source derivada de um MMO conhecido, o autor criou um roadmap inicial de 18 fases de alto nível (só a fundação do jogo — sem definição ainda de personagens/assets/animações), justificando o baixo detalhe pelo fato de não ser possível planejar fases futuras antes de a fase anterior estar implementada.
6. **Três artefatos de memória entre iterações do loop criador**: `lessons.md` (gerado pelo framework TLC Spec Driven, registra lições aprendidas para não repetir erros), *state* (o que foi feito numa fase, incluindo blockers) e *handoff* (o que o próximo agente precisa saber ao fim de uma fase grande). O framework TLC Spec Driven não gera o roadmap — isso é responsabilidade da camada de loop engineering acima dele.
7. **Padrão de execução do loop criador, replicando o relato do Ban**: pegar item do roadmap → planejar (gera spec) → implementar → verificar (subagente evaluator dedicado, até 3 tentativas de correção) → atualizar roadmap → próximo item. Rodou autonomamente por um final de semana inteiro usando o `/loop` do Cursor como mecanismo de disparo.
8. **Referência sólida como pré-condição de sucesso do loop criador**: o autor tinha uma engine JavaScript equivalente para validar contra; o Ban tinha (segundo o vídeo) ~1,3 milhão de asserções de teste pré-existentes no codebase original. Sem uma referência para validar, o risco de o loop criador divergir sem detecção é alto.
9. **O loop não roda "para sempre"**: ele esgota o roadmap e para — nesse ponto o humano precisa decidir o próximo roadmap (o loop não decide *o que* fazer a seguir, só *como* executar o que já está definido). O autor interveio três vezes ao longo de ~30 fases totais: fundação (18 fases) → pesquisa de personagens/animações e criação de skill "game designer" + skill "spec driven execution" (uma skill que ensina o TLC Spec Driven a rodar em loop) → mais ~10-15 fases → intervenção final para polimento e multiplayer.
10. **Pesquisa antecipada reduz a necessidade de prompts de esclarecimento durante o loop**: encapsular pesquisa prévia (ex.: como criar personagens/monstros/efeitos) numa skill dedicada evita que o loop pare pedindo input humano no meio da execução autônoma.
11. **Harness como fator decisivo da migração do Ban para Rust**: a linguagem em si funciona como harness — o compilador de Rust rejeita código memory-unsafe, então a IA não precisa "interpretar" se algo é seguro, apenas reagir a um erro objetivo de compilação. Zig (a linguagem anterior citada no vídeo) permite compilar código que só quebra em produção — harness mais fraco. Tipagem, arquitetura e compilador são todos formas de harness.
12. **Quase-falha própria do autor com testes e2e**: removeu testes Playwright end-to-end (persistidos/reexecutados) em favor de só integração+unidade por questão de velocidade, e os erros voltaram a se acumular sem detecção (jogo tem muitas variáveis). Correção: manteve e2e como critério de entrega de fase, mas sem salvá-los/acumulá-los — cada fase precisa rodar um Playwright ao vivo e provar que funciona ponta a ponta antes de ser considerada concluída.
13. **Limites explícitos do loop engineering**: não resolve uma suíte de testes fraca; não resolve a *intenção* — o loop não decide sozinho qual o próximo roadmap, isso é sempre decisão humana.
14. **Quatro perguntas para decidir se vale usar um loop**: (1) o harness é bom o suficiente para quase não revisar PRs? (2) o feedback (testes) é rápido? (3) existe uma stop condition confiável que aciona o humano? (4) há backlog suficiente para compensar o custo de montar a estrutura de loop, em vez de simplesmente planejar e fazer manualmente?
15. **Contexto de origem citado**: menção ao criador do OpenCode (Peter, descrito como mais "vibe coder", tendo feito o próprio OpenCode com vibe coding) e ao criador do Claude Code (Boris), ambos citados como vozes por trás do hype recente de "loop engineering" nas últimas semanas.

## Entidades e Conceitos Tocados

- [[wiki/concepts/loop-engineering]]
- [[wiki/concepts/spec-driven-development]]
- [[wiki/concepts/task-looper]]
- [[wiki/concepts/harness]]
- [[wiki/entities/claude-code]]
- [[wiki/concepts/vibe-coding]]
- [[wiki/concepts/human-in-the-loop]]
- [[wiki/concepts/rust-ownership-borrowing-lifetimes]]
- [[wiki/concepts/piramide-de-testes]]

## Contradições / Reforços com o Resto da Wiki

**Reforço direto:** [[wiki/sources/loop-engineering-planner-critic-grafo]] já descrevia loop engineering como o degrau seguinte a harness engineering, com componentes planner/executor/critic e a tese "você não faz o prompt, você desenha o sistema que faz o prompt" — esta fonte converge fortemente e adiciona uma dimensão temporal/histórica (os três níveis do dev loop que antecederam o termo) que a fonte anterior não detalhava. As duas fontes citam separadamente o criador do Claude Code e o do OpenCode como vozes centrais do hype — confirmação cruzada, não é a mesma citação reaproveitada.

**Complementar, sem contradição:** [[wiki/concepts/harness]] já registrava que tooling/tipagem/compilador funcionam como "sensores" que substituem julgamento subjetivo do modelo; esta fonte fornece um exemplo concreto e nomeado (Rust vs. Zig na migração do Ban) que reforça essa tese com um caso real de escolha de linguagem como decisão de harness.

**Novo ângulo não coberto antes:** a distinção loop fixo/loop criador é original desta fonte — nenhuma outra página da wiki nomeava essa dicotomia. Foi promovida para dentro de [[wiki/concepts/loop-engineering]] como seção nova.

**Tensão qualificada, já presente em outras fontes:** a mesma ressalva de [[wiki/sources/loop-engineering-planner-critic-grafo]] e [[wiki/sources/vibe-coding-limites-maturidade-profissional]] aparece aqui de forma mais operacional — via as "quatro perguntas" — em vez de uma afirmação geral de que "ainda precisa de engenheiro por perto".

## Open Questions

- O framework "TLC Spec Driven" citado no vídeo não tem página própria na wiki nem foi confirmado como ferramenta pública com esse nome exato — pode ser nome interno/apelido do autor. Não criada página de entidade por falta de confirmação externa.
- A afirmação de que o Ban tinha "~1,3 milhão de asserções de teste" antes da migração para Rust não é verificável nesta fonte (número citado de memória pelo autor, "se não me engano") — tratar como não confirmado.
- O nome completo da engine open source de MMO usada no jogo do autor não foi revelado no vídeo (citado como evitado "por direitos autorais") — não é possível linkar a uma entidade específica.
- Identidade do autor/canal do vídeo não confirmada no texto colado (sem nome, canal ou data de publicação disponíveis nesta transcrição).
