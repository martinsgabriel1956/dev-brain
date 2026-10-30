---
type: source
title: "Como a Anthropic faz code review com agentes — as sete camadas (e o que dá para copiar)"
aliases: ["Anthropic sete camadas de revisão", "queijo suíço do code review", "code review lights-off Anthropic"]
date_created: 2026-10-26
date_updated: 2026-10-26
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/anthropic-code-review-por-agentes-sete-camadas.md
source_url: ""
author: "não identificado (canal brasileiro de engenharia de software com IA)"
date_published: ""
date_ingested: 2026-10-26
source_count: 1
tags: [tech-mentor-ai, code-review, agentes, anthropic, claude-code, review-md, llm-as-judge, evals, feature-flag, ownership, lights-off]
skill: tech-mentor-ai
status: stable
---

## TL;DR

Vídeo (PT-BR) que comenta um post da [[wiki/entities/anthropic]] sobre como ela revisa ~30 mil mudanças de código por dia, ~90% escritas e revisadas pelo [[wiki/entities/claude-code|Claude]]. O modelo é o **queijo suíço de sete camadas** ([[wiki/concepts/revisao-em-camadas-queijo-suico]]): revisão por subagente de contexto limpo → CI → review multiagente por consenso ([[wiki/concepts/consenso-multiagente-em-code-review]], guiado por [[wiki/concepts/review-md]]) → segurança → humanos dimensionados por um classificador ([[wiki/concepts/classificador-de-risco-de-revisao-humana]]) → fila de merge → release gradual atrás de flag. A pergunta muda de "alguém leu?" para "o que pode dar errado e qual checagem pega melhor?", com a trava de que menos revisão **não** pode significar mais reverts. A confiança vem tanto das camadas quanto de **reverter em minutos** ([[wiki/concepts/confianca-por-reversibilidade]]); o revisor é validado com **incidentes viram evals** ([[wiki/concepts/eval-de-revisor-a-partir-de-incidentes]]) e o ruído é controlado com teto de rodadas ([[wiki/concepts/ruido-e-loop-de-nitpick-em-revisao-por-agente]]). O apresentador então contrapõe três papers que limitam o quanto isso se generaliza ([[wiki/concepts/limites-empiricos-de-revisao-por-ia]]).

## Key Claims

**Claim:** Na Anthropic, mudanças de código por dia foram de ~200–500 (maio) para mais de 30.000 (setembro); ~90% escritas pelo Claude, e todo PR passa por revisão de agente antes de qualquer pessoa.
**Evidence:** números lidos pelo apresentador a partir do post da Anthropic. **Confidence:** média-baixa — o "200.500" da legenda é ambíguo e o salto (~60–150×) não foi checado no post original. Ver [[wiki/entities/anthropic]].

**Claim:** A pergunta de revisão mudou de "alguém leu esse código?" para "o que pode dar errado se esse commit for para produção e qual checagem pega isso melhor (automática, pesquisa ou manual)?", com a condição de que **menos revisão humana não pode significar mais coisas quebrando** — medem reverts e incidentes em produção; se um sobe, não houve economia, só deslocamento de trabalho (de revisar para consertar).
**Evidence:** citação do post ("nobody on the team keeps a complete mental model of Claude Code in their head…"). **Confidence:** alta como princípio declarado. Ver [[wiki/concepts/revisao-em-camadas-queijo-suico]], [[wiki/concepts/code-review]].

**Claim:** Sete camadas: (1) testes/build/lint + segundo agente de contexto limpo sobre o diff; (2) CI/CD; (3) Claude Code Review em todo PR (diff × repositório inteiro × intenção declarada); (4) segurança; (5) humanos por nível de risco; (6) fila de merge; (7) pós-merge atrás de flag interna com release gradual, conserto ou revert.
**Evidence:** descrição camada a camada. **Confidence:** alta quanto ao relato; a camada 4 só foi citada de passagem. Ver [[wiki/concepts/revisao-em-camadas-queijo-suico]].

**Claim:** Contexto limpo no revisor importa porque o raciocínio do agente autor contamina a revisão; exemplo da "febre" (contexto antigo de dor de cabeça enviesa a resposta).
**Evidence:** analogia do apresentador + paper que ele diz ter comentado na semana anterior (não identificado). **Confidence:** média — mecanismo plausível e alinhado a [[wiki/concepts/separacao-de-contextos]]; o paper não foi citado. Ver [[wiki/concepts/revisao-por-agente-independente]].

**Claim:** Vários agentes caçam bugs em paralelo; um grupo separado verifica cada achado; só vira comentário o que é confirmado por consenso; estilo/limpeza e achados não unânimes são descartados. Os filtros foram testados em A/B nos próprios PRs. Os comentários saem com severidade e rótulo (importante / nitpick / pré-existente).
**Evidence:** relato do post (e do artigo do HackerRank mencionado). **Confidence:** média-alta como desenho; a taxa de filtragem não foi dada. Ver [[wiki/concepts/consenso-multiagente-em-code-review]].

**Claim:** `REVIEW.md` é escrito pelo dono do código e diz ao revisor o que importa: a falha em documentação é *mentir*, em configuração é *apontar para o lugar errado*; exige arquivo e linha como prova e limita nitpicks por PR. Erro recorrente real vira lint/CLAUDE.md/skill; falso positivo vira linha no `REVIEW.md`.
**Evidence:** exemplos citados do post. **Confidence:** alta. Ver [[wiki/concepts/review-md]], [[wiki/concepts/claude-md]].

**Claim:** Humanos por nível: nenhum (doc, feature interna, atrás de flag), pelo menos um (produto normal e áreas sensíveis — cache, auto-updater, system prompt; pode ser o próprio autor), dois (hot code). Um classificador escolhe o nível e um segundo o confere; "quem define o nível é a mudança, não o autor".
**Evidence:** descrição da camada 5. **Confidence:** alta quanto ao relato. Ver [[wiki/concepts/classificador-de-risco-de-revisao-humana]], [[wiki/concepts/llm-as-judge]].

**Claim:** Metade do segredo é a capacidade de desfazer em minutos (mudança pequena + feature flag + revert rápido + observabilidade + autor com ownership), que torna a revisão um detalhe tolerável; o apresentador espelha com PRs ≤300 linhas e deploy feito pelo próprio autor.
**Evidence:** inferência do apresentador ("pelo menos isso que eu tô entendendo lendo eles"). **Confidence:** média — interpretação, não afirmação explícita do post. Ver [[wiki/concepts/confianca-por-reversibilidade]], [[wiki/concepts/feature-flag]], [[wiki/concepts/canary-release]].

**Claim:** Todo incidente vira caso de eval: PR causador + conserto/revert, confirmado por um engenheiro do código; toda mudança no revisor (prompt, modelo, ferramenta) é rodada contra esses casos — teste de regressão do revisor.
**Evidence:** descrição do post. **Confidence:** alta quanto ao relato. Ver [[wiki/concepts/eval-de-revisor-a-partir-de-incidentes]], [[wiki/concepts/golden-dataset]].

**Claim:** Barulho custa mais com autor-agente: houve um PR com 50+ rodadas numa noite. Correção: após 3 rodadas o revisor para e manda o autor repensar; rodadas seguintes olham só o delta; bugs são apontados por classe inteira. PRs resolvidos em uma rodada foram de 65% para 78%.
**Evidence:** números do post lidos pelo apresentador; o dado de "5+ rodadas" ficou ilegível. **Confidence:** média. Ver [[wiki/concepts/ruido-e-loop-de-nitpick-em-revisao-por-agente]].

**Claim:** A proporção de reverts caiu >40% de junho a setembro, mas os PRs mergeados mais que dobraram — logo, por PR melhorou, mas o número absoluto de reverts pode ter subido.
**Evidence:** dado do post + conta do apresentador (inferência). **Confidence:** média (a conta é correta se as duas premissas valem; nenhuma foi verificada). Ver [[wiki/concepts/limites-empiricos-de-revisao-por-ia]].

**Claim:** Generalização limitada: (a) benchmark de revisores (Microsoft) — 71% de bugs nos 5 primeiros comentários em repositórios abertos, queda forte em repositórios fechados; (b) ETH Zurique — testes escritos por agente passam 88% na suíte válida mas pegam <60% dos bugs plantados; (c) 67.774 PRs de agentes vs 5.000 humanos — agentes precisam de fix posterior ~1,5× mais, e ~70% dos fixes são feitos pelo próprio agente.
**Evidence:** papers citados oralmente, links só na descrição do vídeo (não verificados aqui). **Confidence:** média-baixa até checar os papers. Ver [[wiki/concepts/limites-empiricos-de-revisao-por-ia]].

**Claim:** O que sobra para humanos: decidir se vale construir, revisar o perigoso, revisar arquitetura que vira padrão, ler evidência (saída de teste, não resumo do agente) e ser dono do resultado ("mergeou, é seu") — sem *blame*, porque quem fez tem mais contexto.
**Evidence:** fecho do post. **Confidence:** alta. Ver [[wiki/concepts/ownership-proativo]], [[wiki/concepts/extreme-ownership]], [[wiki/concepts/blameless-post-mortem]].

## Entities

[[wiki/entities/anthropic]], [[wiki/entities/claude-code]], [[wiki/entities/microsoft]] (autoria do benchmark de revisores, segundo o apresentador). ETH Zurique e HackerRank são citados mas não têm página. Apresentador não identificado.

## Concepts

Novos: [[wiki/concepts/revisao-em-camadas-queijo-suico]], [[wiki/concepts/consenso-multiagente-em-code-review]], [[wiki/concepts/review-md]], [[wiki/concepts/classificador-de-risco-de-revisao-humana]], [[wiki/concepts/eval-de-revisor-a-partir-de-incidentes]], [[wiki/concepts/ruido-e-loop-de-nitpick-em-revisao-por-agente]], [[wiki/concepts/confianca-por-reversibilidade]], [[wiki/concepts/limites-empiricos-de-revisao-por-ia]], [[wiki/concepts/llm-as-judge]] (stub).
Ligados: [[wiki/concepts/code-review]], [[wiki/concepts/revisao-por-agente-independente]], [[wiki/concepts/separacao-de-contextos]], [[wiki/concepts/matriz-risco-dificuldade-review-ia]], [[wiki/concepts/claude-md]], [[wiki/concepts/harness-de-qualidade]], [[wiki/concepts/quality-gate]], [[wiki/concepts/feature-flag]], [[wiki/concepts/canary-release]], [[wiki/concepts/golden-dataset]], [[wiki/concepts/evals-llm]], [[wiki/concepts/trunk-based-development]], [[wiki/concepts/ownership-proativo]], [[wiki/concepts/extreme-ownership]], [[wiki/concepts/blameless-post-mortem]], [[wiki/concepts/human-in-the-loop]].

## Open Questions

- Qual é o post original da Anthropic e o texto exato do `REVIEW.md` de exemplo? (link só na descrição do vídeo)
- Quais são os três papers (título/autores/links) e os números batem com o relato oral?
- Qual a taxa de falso positivo/negativo do revisor multiagente e o custo em tokens por PR?
- A queda de reverts "por PR" compensa o aumento absoluto? Qual o MTTR real das reversões?
- Quais gates substituem a camada 5 em times sem token "infinito"? (ver [[wiki/concepts/matriz-risco-dificuldade-review-ia]])

## Raw quotes

> "nobody on the team keeps a complete mental model of Claude Code in their head, and we don't think anyone needs to"
> "quem define o nível é a mudança, não o autor"
> "o agente constrói software que ele não consegue verificar"
> "você mergeou, você é o dono; quebrou, você conserta"
