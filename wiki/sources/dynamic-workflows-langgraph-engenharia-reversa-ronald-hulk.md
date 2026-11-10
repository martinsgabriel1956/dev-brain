---
type: source
title: "Dynamic Workflows sem Claude Code: engenharia reversa e implementação em LangGraph"
aliases: ["dynamic workflows langgraph", "dynamic workflows ronald hulk", "workflow spec langgraph"]
date_created: 2026-11-10
date_updated: 2026-11-10
source_count: 0
tags: [tech-mentor-ai, dynamic-workflow, langgraph, harness, subagentes, orquestracao, context-engineering, verificacao-adversaria, tracing]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/dynamic-workflows-langgraph-engenharia-reversa-ronald-hulk.md
source_url: ""
author: "Ronald Hulk"
date_published: ""
date_ingested: 2026-11-10
---

# Dynamic Workflows sem Claude Code: engenharia reversa e implementação em LangGraph

## TL;DR

Vídeo de [[wiki/entities/ronald-hulk]] que reimplementa em [[wiki/concepts/langgraph|LangGraph]] a ideia dos [[wiki/concepts/dynamic-workflow|Dynamic Workflows]] do [[wiki/entities/claude-code|Claude Code]]. A tese: entre o workflow determinístico e o agente livre existe um meio-termo, em que o agente cria um plano e esse plano vira uma estrutura rígida executada na hora. O grafo do autor tem um esqueleto fixo (comando, planner, montagem da harness, subagentes em subgrafos com verificador, avaliador global, síntese); o que muda a cada execução é a **workflow spec** gerada pelo modelo. Dos seis [[wiki/concepts/padroes-de-workflow-dinamico|padrões]] do artigo da Anthropic, ele diz ter dois completos e dois parciais. O código fica no repositório fechado da comunidade dele, então nada da implementação pôde ser conferido.

## Key Claims

1. **Dynamic Workflows ocupa o meio entre workflow determinístico e agente.** Evidência: o agente gera o plano, o plano vira estrutura rígida, a estrutura executa. A documentação define o recurso como um script JavaScript que orquestra muitos subagentes, escrito pelo Claude e executado em ambiente isolado ([docs](https://code.claude.com/docs/en/workflows) `[external]`). Confiança: alta para o mecanismo.

2. **Workflows garantem repetibilidade e auditoria; por isso renderam mais dinheiro ao autor do que agentes.** Evidência: experiência pessoal, sem números. A garantia vale para o fluxo de controle, não para a saída dos nós de LLM, como mostra [[wiki/concepts/determinismo-vs-probabilismo-em-ia]]. Num workflow dinâmico, o próprio plano muda entre execuções (inferência). Confiança: média como princípio, baixa para a parte financeira.

3. **Os novos padrões derivam dos padrões antigos do artigo da Anthropic de fim de 2024.** Evidência: o autor cita paralelização, routing e chaining. "Building Effective Agents" é de 19/12/2024 e lista prompt chaining, routing, parallelization, orchestrator-workers e evaluator-optimizer ([Anthropic](https://www.anthropic.com/engineering/building-effective-agents) `[external]`). A derivação é leitura do autor. Confiança: alta para as datas e os nomes, média para a derivação.

4. **Separar o trabalho em nós dá melhor qualidade e menor custo, porque cada LLM recebe só o contexto da sua tarefa.** Evidência: argumento sobre o tamanho nominal do contexto e a perda de desempenho conforme ele cresce; o restante fica no estado do grafo. A perda é documentada por [Context Rot](https://www.trychroma.com/research/context-rot) e [Lost in the Middle](https://arxiv.org/abs/2307.03172) `[external]`. Ver [[wiki/concepts/degradacao-de-contexto]]. O vídeo não mede qualidade nem custo. Confiança: alta para a degradação, média para o ganho.

5. **A harness dinâmica tem um esqueleto físico; a parte dinâmica é a workflow spec.** Evidência: o trace mostra critério de parada, critério de síntese, nome, fases, definição do subagente e prompts gerados. O autor diz que o modelo "literalmente cria um MD" sobre o workflow. Confiança: média, pois vem só da demonstração.

6. **Cada subagente é um subgrafo, e o planner decide quantos abrir, até 160.** Evidência: limite configurado pelo autor ("160 porque eu quis"). O vídeo não diz como faz o fan-out; a API `Send` do LangGraph cobre o caso em que o número de itens só é conhecido em runtime ([docs](https://docs.langchain.com/oss/python/langgraph/graph-api-send-command.md) `[external]`). No Claude Code, os limites padrão são 16 agentes concorrentes e 1.000 por execução `[external]`. Confiança: média.

7. **Cada subagente é conferido por outro, e um avaliador global olha o conjunto antes da síntese.** Evidência: o verificador manda refazer ou registra um warning no estado e segue. Confiança: média. Relaciona-se a [[wiki/concepts/planner-executor-critic]].

8. **Modelos diferentes por nó.** Evidência: modelo maior no planner, modelo pequeno na verificação, Qwen 3.7 Max na síntese, tudo configurado no env file via [[wiki/entities/openrouter]]. O modelo [existe na OpenRouter](https://openrouter.ai/qwen/qwen3.7-max) `[external]`. Ver [[wiki/concepts/camada-de-aplicacao-vs-modelo]]. Confiança: alta como técnica.

9. **O dado da empresa determina o valor da solução.** Evidência: o relatório da demo cita métricas de funil e briefings fornecidos pelo autor. Não há como avaliar se a conclusão sobre "gargalos operacionais" é boa. Confiança: média como princípio, baixa para a demo.

10. **O Claude Code roda na máquina do usuário, e a versão do autor roda em servidor.** Evidência: fala do autor. O contraste é exagerado: os workflows também rodam em sessões cloud, em `-p` e pelo Agent SDK `[external]`. O que continua válido é controlar o runtime e embutir o fluxo num produto próprio. Confiança: baixa como diferença absoluta.

11. **No Claude Code só dá para usar modelos Anthropic, com esforço "extra high, ultra", e gasta muito token.** Evidência: fala do autor sobre o post. O alerta de custo está confirmado ("significantly more tokens"). Esforço alto não é exigido: basta pedir um workflow ou usar `ultracode`, e só este depende de suporte a `xhigh`. Os docs não declaram restrição de modelo, mas listam apenas provedores de Claude `[external]`. Confiança: alta para o custo; o requisito de esforço está errado.

12. **Um engenheiro da Anthropic comparou o recurso a um salto tão grande quanto skills e subagentes.** Evidência: post mostrado na tela, sem identificação. A pesquisa não achou o post; a frase mais próxima é de um terceiro, [Artem Zhutov](https://artemxtech.substack.com/p/claude-dynamic-workflows-for-your) `[external]`. X não pôde ser pesquisado. Confiança: não verificada.

13. **Quem constrói desde antes se distancia da "massa", e especialista em IA não é especialista em Claude Code.** Evidência: opinião e autopromoção. O autor diz usar mais Codex e OpenCode. O ditado da maré é conhecido pela [carta de Buffett de 1992](https://www.berkshirehathaway.com/letters/1992.html) `[external]`. Confiança: baixa, é posicionamento.

## O que foi implementado, segundo o autor

| Padrão ([artigo](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code) `[external]`) | Estado na versão LangGraph |
|---|---|
| Fan-out-and-synthesize | Completo |
| Adversarial verification | Completo |
| Classify-and-act | Parcial: depende de `/pesquisar` ou `/auditoria`, sem classificação inteligente |
| Loop until done | Parcial: retry em falha de resposta ou de API |
| Generate-and-filter | Não implementado (nome por exclusão; o vídeo não cita) |
| Tournament | Não implementado (nome por exclusão; o vídeo não cita) |

## Raw quotes

- "Você vai usar o agente para criar um plano, e esse plano vai ser transformado em uma estrutura rígida."
- "Ela não é dinâmica no ar. Nada é dinâmico magicamente."

## Entidades

- [[wiki/entities/ronald-hulk]]: autor.
- [[wiki/entities/claude-code]]: produto com o recurso original.
- [[wiki/entities/anthropic]]: autora do recurso e dos artigos.
- [[wiki/entities/openrouter]]: acesso aos modelos.
- [[wiki/entities/langsmith]]: o autor diz ter os três modelos ali "só passando as variáveis"; a tela de trace parece ser dele, mas é inferência.
- [[wiki/entities/opencode]], [[wiki/entities/codex-openai]]: ferramentas que o autor diz preferir hoje.
- [[wiki/entities/rock-pro]]: citada como "Rock Pro Empresas".
- Sem página própria: Qwen 3.7 Max, ChatGPT, Claus (colaborador da comunidade).

## Conceitos

- [[wiki/concepts/dynamic-workflow]]: página criada neste ingest.
- [[wiki/concepts/padroes-de-workflow-dinamico]]: página criada neste ingest.
- [[wiki/concepts/langgraph]], [[wiki/concepts/grafo-como-abstracao-de-agentes]]
- [[wiki/concepts/planner-executor-critic]]
- [[wiki/concepts/harness]], [[wiki/concepts/subagentes]]
- [[wiki/concepts/degradacao-de-contexto]]
- [[wiki/concepts/determinismo-vs-probabilismo-em-ia]]
- [[wiki/concepts/camada-de-aplicacao-vs-modelo]]
- [[wiki/concepts/modalidades-de-paralelismo-claude-code]]

## Relação com fontes anteriores

- [[wiki/sources/loop-engineering-planner-critic-grafo]] mostra o que parece ser a base desta implementação: autor identificado como Hulk, LangGraph, planner gerando prompts e rubricas, teto de cerca de 160 subtarefas. Esta fonte acrescenta a workflow spec e o avaliador global.
- **Tensão:** [[wiki/concepts/planner-executor-critic]] diz que o verificador deve ser outro modelo, o que o autor faz. Ele descreve a verificação como tarefa fácil, para um modelo pequeno; a wiki a trata como o ponto que garante qualidade.

## Open Questions

- O loop until done parcial é só retry técnico? O vídeo também descreve o verificador pedindo para refazer, que já é um laço de qualidade.
- A spec é Markdown ou saída estruturada? O autor diz MD; o trace mostra campos.
- Gerar código (Claude Code) ou gerar dados para um grafo fixo (autor): qual dá mais flexibilidade e qual dá mais segurança? A fonte não compara.
- Qual é o custo real por execução com até 160 subagentes? O vídeo não informa.
