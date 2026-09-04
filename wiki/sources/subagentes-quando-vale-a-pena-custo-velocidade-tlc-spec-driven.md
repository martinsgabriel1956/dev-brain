---
type: source
title: "Subagentes: Quando Vale a Pena — Um Case Real de Custo x Velocidade"
aliases: ["case tlc spec driven subagentes", "sweet spot subagentes", "quando usar subagentes"]
date_created: 2026-09-03
date_updated: 2026-09-03
source_count: 1
tags: [subagentes, spec-driven-development, janela-de-contexto, custo-de-ia, tlc-spec-driven, anthropic, cognition, benchmark]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/subagentes-quando-vale-a-pena-custo-velocidade-tlc-spec-driven.md
source_url: ""
author: "desconhecido (indícios apontam para o mesmo autor/canal de spec-driven-development-otimizando-contexto-agentes)"
date_published: "desconhecida"
date_ingested: 2026-09-03
---

## TL;DR

Vídeo (aula de comunidade, autor não identificado por nome completo) apresenta um benchmark de campo comparando quatro formas de rodar a mesma spec de 17 tasks (integração com Stripe, via skill **TLC Spec Driven**): sem subagentes, um subagente por task, subagentes agrupados por fase, e um "sweet spot" de três subagentes agrupando tasks relacionadas. O achado central: granularidade excessiva de subagentes (um por task) **piora** tempo, custo em tokens e qualidade simultaneamente — porque cada subagente recarrega contexto do zero e fragmenta a visão do todo — enquanto um agrupamento coeso em poucos subagentes (três, no caso testado) iguala ou supera o desempenho de rodar tudo num único agente, com a vantagem de terminar com a janela de contexto do agente principal muito mais livre para correções.

## Key Claims

1. **Benchmark de 4 cenários na mesma tarefa (spec de 17 tasks, integração Stripe via TLC Spec Driven):** sem subagentes (baseline: ~9M tokens, nota 0,93, janela final 74%); 1 subagente por task (25M tokens — +150% vs. baseline —, nota 0,81, 43 min); agrupado por fases (15M tokens, nota 0,90, janela final 32%, 35 min); 3 subagentes agrupando tasks relacionadas (10M tokens, nota 0,95, janela final 26%, 18 min). Confiança média-alta: números vêm de uma única run de benchmark narrada em vídeo, sem link para dashboard ou planilha bruta, mas com metodologia consistente entre os quatro cenários (mesma spec, mesma tarefa, mesmo critério de nota) — diferente da fonte [[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]], que citava números de terceiros (Artificial Analysis) sem controle de metodologia.
2. **Granularidade excessiva (um subagente por task) piora custo, tempo E qualidade ao mesmo tempo — não é um trade-off, é estritamente pior nos três eixos** frente ao baseline sem subagentes. Causa apontada: cada subagente inicia sem contexto e recarrega arquivos do zero; com 17 tasks, isso significa recarregar contexto 17 vezes, além de fragmentar a visão do todo o suficiente para derrubar a qualidade da implementação (0,93 → 0,81). Reforça, com número concreto, o que [[wiki/concepts/subagentes]] já registrava qualitativamente sobre o "Padrão Orquestrador" e a economia de restringir escopo por subagente.
3. **Poluição da janela do agente principal escala com o número de subagentes, não com o volume de trabalho por subagente:** cada subagente retorna um output ao agente pai; mais subagentes (mesmo que cada um faça menos) significa mais outputs acumulados na janela do principal. É por isso que o cenário "agrupado por fases" (menos subagentes, cada um com mais trabalho coeso) termina com janela do principal em 32%, contra 74% do baseline sem subagente nenhum — o principal delega o trabalho pesado e recebe de volta só sínteses.
4. **Existe um sweet spot de agrupamento (3 subagentes, no caso testado) onde tempo, custo em tokens e qualidade ficam estatisticamente equivalentes a rodar tudo num único agente, mas a janela de contexto final do principal fica livre (26%) em vez de quase saturada (74%).** Isso dá margem para correções pós-implementação sem risco de degradação por janela cheia — o baseline sem subagentes, ao terminar em 74% num one-shot, já teria pouco espaço para ajustes antes de estourar a janela de 200k tokens. Ver [[wiki/concepts/janela-de-contexto]].
5. **A vantagem de custo do agrupamento em poucos subagentes coesos deve aumentar com o tamanho da tarefa** — a comparação foi feita com apenas 17 tasks (spec pequena/média); em specs maiores (o autor cita hipoteticamente mais de 100 tasks), o cenário sem subagentes tenderia a inflar a janela e o custo de forma desproporcional, enquanto o cenário agrupado continuaria com folga — mas essa extrapolação **não foi testada no vídeo**, é conjectura do autor sobre a mesma curva observada em 17 tasks.
6. **Pesquisa da Anthropic (citada de segunda mão, sem link) reporta custo até 15× maior com sistemas multi-agente, mas resposta melhor em 90% dos casos** — o autor conecta isso à degradação de um agente único rodando por muito tempo, e especula (sem testar) que, se a pesquisa da Anthropic tivesse agrupado tasks de forma menos granular (como no cenário 3/4 deste benchmark), o custo provavelmente cairia para perto do de um agente único. Confiança baixa: é citação de memória de uma pesquisa não linkada, mais a especulação do próprio autor sobre a causa do resultado dela — dois níveis de inferência sem fonte primária conferida.
7. **Cognition (Devin, adquiriu Windsurf) defende que subagentes são perigosos porque fragmentam o contexto — cada ação do agente carrega uma decisão registrada na janela, que um subagente novo não herda.** O autor liga isso diretamente ao cenário 2 (granularidade excessiva) deste benchmark, e argumenta que trabalhar a partir de uma spec compartilhada (em vez de deixar o agente pai fragmentar contexto livremente ao delegar) é o antídoto: o subagente, ao carregar a spec, recebe contexto suficiente sem depender de decisões implícitas do pai. Ver [[wiki/entities/devin-ai]].
8. **Modelo mental de decisão proposto (4 critérios):** (a) research/varredura de codebase → sempre vale subagente, não polui a janela do principal; (b) tarefas longas com muitas tasks → considerar subagentes, mas evitar granularidade excessiva; (c) tarefas pequenas e fortemente acopladas → manter na mesma janela, monitorando o quanto ela enche; (d) trabalho paralelizável → subagentes ganham velocidade, mas de novo sem fragmentar demais. Este é o núcleo prescritivo da fonte, derivado diretamente dos 4 cenários testados.

## Entidades e Conceitos Tocados

- [[wiki/concepts/subagentes]]
- [[wiki/concepts/spec-driven-development]]
- [[wiki/concepts/janela-de-contexto]]
- [[wiki/entities/anthropic]]
- [[wiki/entities/devin-ai]]
- [[wiki/concepts/rpi-workflow]]

## Contradições / Reforços com o Resto da Wiki

**Reforço direto e quantificado:** [[wiki/concepts/subagentes]] já descrevia, na seção "Disparo a Partir do Breakdown de Tasks de um Spec-Driven", o padrão de despachar um subagente por grupo paralelizável de tasks (citando o mesmo caso de campo de [[wiki/sources/spec-driven-development-otimizando-contexto-agentes]] — 4 subagentes para ~40 tasks). Esta fonte não contradiz esse padrão; ela adiciona a variável que faltava: **quantos** subagentes são bons, com números de tempo/custo/qualidade para justificar por que "1 subagente por task" (extremo oposto de "1 agente para tudo") é uma escolha ruim, não uma escolha só mais cara.

**Reforço direto:** [[wiki/concepts/janela-de-contexto]] já registrava, via [[wiki/sources/spec-driven-development-otimizando-contexto-agentes]], a heurística de manter uso em ~200k tokens mesmo com janelas de até 1M disponíveis, por risco de alucinação. Esta fonte dá um mecanismo concreto para *como* subagentes ajudam a cumprir essa heurística no agente principal (outputs sintetizados em vez de todo o trabalho bruto) — mas nota que subagentes mal agrupados (cenário 2) consomem mais tokens *no total do sistema*, mesmo reduzindo a janela do principal.

**Reforço direto:** [[wiki/entities/devin-ai]] tinha até agora apenas uma fonte (sobre cloud agents / Claude Tag), sem nenhuma menção à posição da Cognition sobre multi-agente. Esta fonte adiciona esse ângulo: Cognition como voz cética em relação a subagentes, argumento de fragmentação de decisões — dado novo, sem contradição com o conteúdo anterior da página (que tratava de um tema diferente, cloud agents via Slack).

**Tensão não resolvida, sinalizada pela própria fonte:** a citação da pesquisa da Anthropic ("custo até 15× maior com multi-agente, mas resposta melhor em 90% dos casos") não bate diretamente com os números deste próprio benchmark, onde o cenário mais caro (1 subagente por task, +150% de tokens) teve a **pior** nota de qualidade, não uma nota melhor. O autor reconhece a diferença e especula que a causa é granularidade (a pesquisa da Anthropic não teria agrupado tasks), mas isso não foi verificado — nem contra a pesquisa original da Anthropic, nem replicado neste benchmark. Registrado como open question abaixo.

## Open Questions

- **Pesquisa da Anthropic citada sem link:** o número "15× mais caro, 90% de respostas melhores" não foi conferido contra a publicação original — não é possível confirmar se ela mede o mesmo tipo de granularidade testado neste vídeo, nem se a "resposta melhor em 90% dos casos" é compatível com "nota caiu de 0,93 para 0,81" deste benchmark sob alta granularidade. Candidato a nova fonte se a pesquisa da Anthropic for localizada e ingerida separadamente.
- **Generalização para specs maiores (>100 tasks) não testada:** a fonte conjectura que o sweet spot de poucos subagentes ficaria ainda mais vantajoso em specs grandes, mas não há dado de benchmark para tarefas maiores que as 17 tasks testadas.
- **"3 subagentes" é um número específico deste caso (17 tasks), não uma constante universal** — a própria fonte recomenda replicar a metodologia (comparar granularidade do framework de spec-driven usado, agrupar de forma similar) em vez de aplicar literalmente "3" a qualquer projeto. Não há fórmula matemática publicada relacionando nº de tasks a nº ideal de subagentes, apesar do vídeo prometer uma "fórmula prática" na introdução.
- **Autoria não confirmada:** a menção direta à skill "TLC Spec Driven" e a "nossa comunidade" aponta para o mesmo autor/canal de [[wiki/sources/spec-driven-development-otimizando-contexto-agentes]], mas isso não está confirmado por nome completo na transcrição.
- **Nome de ferramenta/run não identificado ("pur tesk"):** aparece na transcrição como nome de uma interface ou run mostrada em tela; não foi possível confirmar a grafia ou identidade exata da ferramenta.

## Raw Quotes

> "Muita granularidade não vale a pena. Tem um custo extremamente alto e muito lento."

> "Toda a leitura, varredura de código, é muito bom [usar subagente] — [...] é bom pra janela do agente principal e também bom pra te escalar, não polui a janela."

> "A gente pode dar uma... Pesquisando mais a fundo, eu fui ver se isso batia com as últimas coisas da indústria. A indústria tá meio dividida em dois pontos, mas o que eu encontrei se encaixa nos dois opostos."
