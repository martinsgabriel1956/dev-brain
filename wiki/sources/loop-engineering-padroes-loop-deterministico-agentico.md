---
type: source
title: "Loop Engineering: Padrões para o Loop Trabalhar Sozinho (Determinístico vs. Agêntico, Judge, Orquestrador, Estado, Skills)"
aliases: ["loop determinístico vs agêntico", "padrão judge", "padrão orquestrador de modelos", "loop engineering vídeo 2"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_count: 0
tags: [loop-engineering, harness, spec-driven, ai-para-devs, compose, codex, reasoning-level, planner-executor-critic, judge-pattern, orquestracao-de-modelos, gerenciamento-de-estado, skills]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/loop-engineering-padroes-loop-deterministico-agentico.md
source_url: ""
author: "Pedro Nauke (inferido — ver nota de identificação abaixo)"
date_published: ""
date_ingested: 2026-08-12
---

## TL;DR

Segundo vídeo da série de três de [[wiki/entities/pedro-nauke]] sobre Loop Engineering (o primeiro é [[wiki/sources/loop-engineering-harness-e-a-frase-que-viralizou]]). Propõe a divisão mais importante em loop engineering prático: **loop determinístico** (script que abre sessão nova a cada round, depende de memória transitória gravada em disco; pior com modelos de reasoning alto por pagar o custo de contexto inicial run atrás de run) vs. **loop agêntico** (via `/go` do harness, nunca abre run nova, compacta em vez de reiniciar, quem julga se terminou é o próprio modelo). Relata teste comparativo do autor — spec driven sem quebra de tasks teve pior resultado que spec driven com breakdown prévio, mesmo em loop agêntico. Descreve quatro padrões operacionais: **padrão judge** (segundo agente em background, via stop hook, julga se a run realmente terminou), **padrão orquestrador** (modelo caro/denso orquestra modelos baratos por tipo de tarefa em vez de implementar ele mesmo), **gerenciamento de estado via arquivo** (`state.md` trackeando tasks, decisões, erros, arquivos modificados) e **skills que encapsulam o loop** (exemplo próprio: skill de spec-driven + report + QA + deep review + PR/squash merge, tudo numa run). Fecha afirmando que, nos testes do autor, o loop agêntico tem substituído partes do loop determinístico (mesmo o próprio Compose) para modelos de reasoning alto, por evitar o autoconsumo de contexto do modelo determinístico.

## Nota de Identificação do Autor

O texto colado não traz nome, canal ou data de publicação. A atribuição a [[wiki/entities/pedro-nauke]] é inferida por três sinais: (1) o falante chama o Compose de "a ferramenta que eu criei" — Compose já é atribuído a Pedro Nauke em [[wiki/concepts/spec-driven-development]] e [[wiki/concepts/worktree-paralelismo]]; (2) a abertura recapitula literalmente o conteúdo do primeiro vídeo já ingerido ([[wiki/sources/loop-engineering-harness-e-a-frase-que-viralizou]] — "loop = para de dar prompt, passa a desenhar o loop"), que aquela fonte já registrava como primeiro de uma série de três vídeos do mesmo autor; (3) o padrão retórico e as opiniões técnicas (preferência por modelos densos como orquestrador, ceticismo com custo de reasoning alto) são consistentes com o perfil já registrado na entidade. **Não confundir** com o autor autoidentificado como "Hulk" em [[wiki/sources/loop-engineering-planner-critic-grafo]], uma série totalmente diferente.

## Key Claims

1. **Divisão central: loop determinístico vs. loop agêntico.** Loop determinístico = script que, a cada round, abre uma sessão nova (contexto anterior descartado) — exemplo dado é o próprio Compose. Loop agêntico = via comando `/go` (implementado, com variações, pela maioria dos harnesses — Claude Code, Codex, Hermes), nunca abre run nova, fica iterando na mesma run e compactando o contexto conforme enche. A escolha entre os dois decide qual modelo usar e quanto se gasta.

2. **Loop determinístico precisa de memória transitória gravada em disco**, porque cada round começa do zero. Instrução via system prompt: ao fechar uma run ou antes de compactar, gravar tudo que aconteceu num arquivo em disco para a próxima run recuperar contexto.

3. **Custo do contexto inicial em modelos de reasoning alto**: em modelos como GPT 5.6/Sol ou Fable (reasoning alto, "pensam muito antes de executar"), o trecho mais custoso é a formulação inicial do contexto. No loop determinístico, quanto maior o "long reasoning" do modelo, pior — porque esse custo de formulação de contexto é pago run atrás de run, e o contexto é descartado a cada novo round. Recomendação do autor: se o loop já tem bom aparato de artefatos de estado salvos, usar um modelo com reasoning mais baixo no loop determinístico evita pagar caro por raciocínio que será descartado.

4. **Aplicação ao spec driven quebrado em tasks**: como cada task já tem artefatos bem definidos, colocar reasoning muito alto (GPT 5.6, Fable) faz cada task demorar mais do que precisaria, porque o modelo sempre faz um reasoning alto mesmo quando a tarefa já está bem especificada.

5. **Codex é, para o autor, o harness que melhor entrega o loop agêntico via `/go`** — evoluiu muito em compactação de contexto, a ponto de a compactação "quase não fazer mais efeito perceptível" de tão eficiente. Combinado a um modelo como GPT 5.6, que é treinado sobre os próprios logs (JSON) gerados pelo Codex, existe um ciclo de retroalimentação: cada novo modelo GPT fica melhor em long-running tasks por causa do treinamento sobre dados do próprio Codex.

6. **No loop agêntico, quem julga se a run terminou é o próprio modelo** — daí a recomendação de sempre ter bons gates de verificação, para evitar que o modelo se perca no meio do caminho.

7. **Teste comparativo do autor sobre spec driven em loop**: comparou (a) spec driven quebrado em tasks em loop determinístico, (b) spec driven quebrado em tasks em loop agêntico, (c) execução sem quebra de tasks (spec inteira direto pro loop). Resultado reportado: sem quebra de tasks, o resultado foi pior tanto na definição de tarefas em runtime quanto na execução — mais demorado. Com artefatos de estado e breakdown de tasks definidos previamente (critérios de sucesso, lista de testes, descrição mínima por task), o resultado melhorou — inclusive quando o loop era agêntico (não determinístico). Contraria a visão popular de que "spec driven morre" em loops agênticos de long-running tasks.

8. **Padrão Judge**: um segundo agente sobe em background ao final de cada run e julga se a tarefa proposta foi de fato concluída — ele é "o dono da verdade", não o modelo que executou. Implementação via `stop hook` (a maioria dos harnesses tem): ao modelo sinalizar stop, o hook dispara o agente juiz (via comando ou integração no harness); se o juiz decide que não terminou, ele mesmo gera um novo prompt contendo o que falta, fechando o ciclo.

9. **Quando o padrão judge compensa**: mais útil em modelos "menos densos" em long-running tasks — cita Opus, Grok, Sonnet como exemplos que encerram o loop cedo demais em tarefas de horas. Em modelos frontier de reasoning muito alto (Fable, GPT 5.6), o autor considera o judge um gasto desnecessário — esses modelos já sustentam o loop sozinhos por muito tempo (relata casos de mais de dois dias rodando direto).

10. **Padrão Orquestrador**: em vez de o modelo caro/denso implementar, ele orquestra modelos mais baratos para implementação (e até review) por tipo de tarefa. No Compose (determinístico), isso é configuração direta por task. Em loop agêntico, precisa ser passado via prompt para um agente orquestrador, que decide dinamicamente qual modelo usar por tarefa. Exemplo do autor: GPT 5.6 (reasoning medium) para back-end mais barato, Opus 4.8 ou Grok 4.5 para front-end mais rápido e barato. Avaliação do autor: bom resultado tanto em custo de token quanto em velocidade.

11. **Gerenciamento de estado via arquivo, sem precisar ser determinístico**: pode ser feito via prompt ou skill, pedindo ao agente para manter um arquivo de estado (o autor usa `.md`, cita algo como "state spec") que trackeia: tarefa feita, próxima tarefa, lista de tarefas, decisões tomadas, erros, arquivos modificados. Exemplo: spec com 10 tasks — o próprio agente cria o arquivo de estado com todas as informações para executar as 10 tasks uma por uma, seguindo um padrão formalizado.

12. **Skills como forma de encapsular loop engineering não determinístico**: o autor cita uma skill própria (nome incerto na transcrição, foneticamente "C Loop Tests") que dá toda a estrutura organizacional a um loop de spec driven — gerenciamento de estado, o que olhar na spec, gates de verificação, verificações finais, o que acontece após cada task, o que escrever de memória no output final. A skill pode habilitar outras skills durante a leitura, encadeando um processo.

13. **Fluxo completo relatado pelo autor**: task a task → ao terminar todas as tasks da spec, executa skills de "report" e "execution" próprias → executa skill de deep review, que gera issues que o próprio agente resolve na mesma run → opcionalmente abre PR com description e faz squash merge, tudo autonomamente. Funciona bem, segundo o autor, com GPT 5.6/Fable, ou com padrão judge quando o modelo é menos denso.

14. **Loop agêntico substituindo o determinístico**: o autor relata substituir cada vez mais o próprio Compose (loop determinístico) por essa abordagem agêntica, porque, com modelos de reasoning alto, isolar contexto a cada round (loop determinístico) traz resultado pior por autoconsumo e reformulação repetida de contexto — deixar o modelo se autogerenciar tem trazido resultado melhor nos testes do autor.

## Entidades e Conceitos Tocados

- [[wiki/entities/pedro-nauke]]
- [[wiki/concepts/loop-engineering]]
- [[wiki/concepts/harness]]
- [[wiki/entities/codex-openai]]
- [[wiki/concepts/reasoning-level]]
- [[wiki/concepts/spec-driven-development]]
- [[wiki/concepts/task-looper]]
- [[wiki/concepts/planner-executor-critic]]
- [[wiki/concepts/modelo-frontier]]
- [[wiki/concepts/estado]]

## Contradições / Reforços com o Resto da Wiki

**Reforço direto:** [[wiki/sources/loop-engineering-harness-e-a-frase-que-viralizou]] (vídeo 1 da mesma série) já situava o loop como algo que "contém" o harness e listava três fatores que destravaram loops longos em 2026 (modelo, harness, estado persistente); esta fonte detalha operacionalmente o terceiro fator (estado persistente via `state.md`) e acrescenta a divisão determinístico/agêntico que a primeira fonte não explorava com esse nível de detalhe.

**Tensão qualificada com [[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]]:** aquela fonte (série diferente) também usa o termo "loop fixo" (sem side effect) vs. "loop criador" — nomenclatura própria do autor daquela fonte, não idêntica à divisão determinístico/agêntico desta fonte, embora ambas tratem de eixos ortogonais de classificação de loop (uma pelo side effect acumulado, outra pelo mecanismo de execução/contexto). Não é contradição — são dois recortes diferentes do mesmo espaço de problema, e não devem ser fundidos sem qualificação.

**Novo ângulo não coberto antes:** o "padrão judge" via `stop hook` como agente independente que julga e reabre a run é mais específico do que o Critic/verificador já documentado em [[wiki/concepts/planner-executor-critic]] — lá o Critic normalmente atua dentro do próprio ciclo PEC (planner→executor→critic), enquanto aqui o judge é um agente separado, disparado por hook de infraestrutura do harness, após o modelo já ter declarado a run como concluída. Vale registrar como variante/especialização do papel de Critic, não substituí-lo.

**Tensão não resolvida com [[wiki/concepts/reasoning-level]]:** essa página já registrava, a partir de outras fontes, que "tarefa bem definida (spec pronta): mesmo com extra-high, o modelo não desperdiça tanto quanto parece". Esta fonte afirma o oposto para tasks de spec driven já bem definidas — reasoning muito alto faz cada task demorar mais do que precisaria. Possível reconciliação (não confirmada): a regra antiga fala de desperdício de qualidade/tokens, esta fonte fala de desperdício de tempo/latência — não seriam necessariamente incompatíveis, mas nenhuma fonte compara os dois eixos diretamente. Marcado como tensão aberta em [[wiki/concepts/reasoning-level]]. Em complemento (sem tensão): a fonte também adiciona uma regra nova sobre loops determinísticos que reiniciam sessão a cada round, onde reasoning alto é desperdício recorrente por repetir a formulação inicial de contexto — esse caso específico não estava coberto antes.

**Sem contradição com [[wiki/concepts/spec-driven-development]] / [[wiki/concepts/task-looper]]:** reforça a tese já registrada de que breakdown de tasks + artefatos de estado melhora o resultado do loop, agora com um teste comparativo específico (com/sem breakdown, determinístico/agêntico) que nenhuma outra fonte da wiki tinha reportado.

## Open Questions

- Nome exato da skill "C Loop Tests" citada pelo autor não está confirmado — transcrição fonética incerta; pode ser "SpecLoop Tests", "Seek Loop Tests" ou nome interno não documentado publicamente. Não criada página de entidade/ferramenta por falta de confirmação.
- O termo "Qwaya" citado como nome de processo/ferramenta ao final do fluxo de skills não foi identificado com confiança — mantido como transcrição literal no `raw/`, sem link na wiki.
- Atribuição de autoria a Pedro Nauke é inferida (ver nota acima), não confirmada por metadado externo (sem nome de canal, data ou URL na transcrição colada). Se o usuário confirmar ou corrigir a autoria, atualizar esta fonte e [[wiki/entities/pedro-nauke]].
- Não fica claro no vídeo se "GPT 5.6" e "Sol" seguem sendo o mesmo modelo (já registrado como ambíguo em [[wiki/concepts/modelo-frontier]]) — a fonte usa os dois nomes de forma intercambiável sem esclarecer.
- **Tensão nova registrada em [[wiki/concepts/modelo-frontier]]:** esta fonte trata GPT 5.6 como modelo comercial de uso diário (reasoning medium selecionável, usado para backend), enquanto [[wiki/sources/mitos-fable-5-bloqueio-governo-eua-cyberseguranca]] registra GPT 5.6 como modelo bloqueado pelo governo dos EUA por capacidade ofensiva de cybersegurança. Não resolvido — pode ser colisão de nome entre modelos distintos.
