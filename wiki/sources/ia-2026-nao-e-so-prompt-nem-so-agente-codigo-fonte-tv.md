---
type: source
title: "IA em 2026 Não É Mais Só Sobre Prompts ou Agentes (Código Fonte TV)"
aliases: ["IA 2026 vocabulário técnico", "loop engineering graph engineering memory layers CDF", "83% para 98,5% adoção IA devs"]
date_created: 2026-08-19
date_updated: 2026-08-19
source_count: 0
tags: [tech-mentor-ai, loop-engineering, graph-engineering, memory-layers, spec-driven-development, mcp, subagentes, langchain, adocao-ia, pesquisa-salarial, hostinger]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/ia-2026-nao-e-so-prompt-nem-so-agente-codigo-fonte-tv.md
source_url: ""
author: "Código Fonte TV"
date_published: "2026"
date_ingested: 2026-08-19
---

# IA em 2026 Não É Mais Só Sobre Prompts ou Agentes (Código Fonte TV)

## TL;DR

Vídeo do canal [[wiki/entities/codigo-fonte-tv]] argumentando que, em 2026, "saber usar IA" deixou de significar prompt engineering básico e passou a exigir um vocabulário técnico novo — Loop Engineering, Graph Engineering, Memory Layers, Spec-Driven Development, MCP e mais. Usa a própria pesquisa salarial do canal como evidência de adesão (83% dos devs usavam IA para programar em 2024 → 98,5% em 2026) e uma linha do tempo GitHub Copilot (2021) → ChatGPT (2022) → Claude (2023) para contextualizar a virada. Cita a LangChain como responsável por batizar tanto "loop engineering" quanto "graph engineering" em 2026, e o Boris (criador do Claude Code) como voz recorrente sobre graph engineering. Traz também uma novidade específica do Claude Code — mensagens cruzadas entre subagentes via um recurso chamado "list agents" — e um bloco patrocinado da Hostinger.

## Key Claims

1. **Adesão de devs a IA para programar saltou de 83% (2024) para 98,5% (2026)**, segundo a pesquisa salarial própria do canal. Ambos os números são citados como vindos da mesma pesquisa (pesquisa.codefonte.com.br), permitindo comparação direta ano a ano — mesma metodologia (amostra de quem responde a divulgação do canal, não survey probabilístico de mercado, como já registrado em [[wiki/sources/golang-mercado-salarios-pesquisa-2024]]). [skill: tech-mentor-ai — nenhuma referência específica; claim de mercado, não técnica]

2. **Linha do tempo de lançamento: GitHub Copilot (jun/2021) → ChatGPT (2022) → Claude (mar/2023, "devagarzinho")** — usada para mostrar a distância entre o "autocomplete com comentário" de 2021 e o cenário agêntico de 2026. A ordem e os anos são consistentes com o consenso público de mercado (não checados contra fonte primária nesta ingestão).

3. **Loop Engineering (LangChain, 2026): todo agente opera num loop observar→decidir→agir→observar, e a LangChain nomeou formalmente a disciplina de projetar esses loops.** Confirma, com uma terceira fonte independente, a origem já registrada em [[wiki/concepts/loop-engineering]] (via [[wiki/sources/loop-engineering-harness-e-a-frase-que-viralizou]] e [[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]]) — sem contradição, apenas reforço. Lista as mesmas perguntas de engenharia já documentadas (quando terminar o loop, quantas tentativas, quando pedir ajuda humana, o que fazer se uma ferramenta falhar, como evitar consumo descontrolado de tokens).

4. **Graph Engineering (LangChain, 2026): grafo como abstração para fluxos de agente mais complexos que um loop simples suporta** — nós = operação/chamada de modelo/ferramenta/outro agente; arestas = próximo passo. Mesma tese já central em [[wiki/concepts/grafo-como-abstracao-de-agentes]]; esta fonte atribui a cunhagem do *termo* à LangChain (2026) de forma mais explícita do que a fonte anterior (que atribuía a ideia a um tweet de Peter Steinberger, sem nomear quem batizou o termo). **Boris, criador do Claude Code**, é citado como alguém que já discutiu graph engineering publicamente — primeira menção na wiki ligando Boris a este tópico especificamente (as menções anteriores a Boris, em [[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]], eram sobre `CLAUDE.md`/documentação como harness, não sobre grafos).

5. **Memory Layers: memória de agente não é só "guardar o chat"** — inclui memória de curto prazo, informações persistentes, resumos, artefatos de execução, e recuperação seletiva do que é relevante para a tarefa atual. Atribuído (com transcrição foneticamente incerta, "OPA") à própria Anthropic: distinção entre contexto de trabalho, memória para execuções futuras, e artefatos revisados como fonte confiável. Alinha-se à taxonomia cognitiva→técnica já documentada em `references/ai/agent-memory.md` (skill tech-mentor-ai) — working memory / persistent memory / artefatos revisados mapeiam razoavelmente bem a working memory / episódica-semântica / e um conceito próximo de "golden dataset" ou fonte de verdade curada. [skill: tech-mentor-ai]

6. **Hierarquia do `CLAUDE.md` (máquina → usuário → projeto → pasta) é tratada explicitamente como uma forma de memória** — já documentado na wiki via [[wiki/concepts/claude-md]] e [[wiki/concepts/rules-agente]], mas esta fonte é a que enquadra a hierarquia de rules como *memory layer*, e não só como configuração/regras.

7. **Prática de campo dos apresentadores: pedir ao agente para gerar documentação numa pasta `docs/` do projeto ao final de cada tarefa**, para servir de memória persistente consultável na próxima sessão — mesmo padrão já coberto em [[wiki/concepts/spec-driven-development#Estado: Registro de Decisões Pós-Planejamento]] (artefato de estado) e em [[wiki/concepts/loop-engineering#Gerenciamento de Estado via Arquivo]], mas relatado aqui como hábito pessoal dos autores, não como parte de uma spec ou loop formal.

8. **Mensagens cruzadas entre subagentes via recurso "list agents" (Claude Code)** — quando o Claude Code usa subagentes, um subagente agora consegue "promptar" outro agente diretamente; o recurso lista todos os agentes disponíveis no contexto, permite que um agente identifique qual é o mais adequado para uma subtarefa e dispare esse outro agente, opcionalmente deixando-o rodando em paralelo e retomando depois. Claim específico e verificável: existe uma tool chamada `ListAgents` que enumera agentes endereçáveis via mensagem — não estava documentado na wiki antes desta fonte. Ver [[wiki/concepts/subagentes]].

9. **Spec-Driven Development: a especificação vira "fonte de verdade" em vez de documentação auxiliar** — reafirma a tese central já coberta em profundidade em [[wiki/concepts/spec-driven-development]]. Cita o **Spec Kit do GitHub** como ferramenta específica para esse fluxo — já mencionado en passant na wiki (tabela "Ferramentas de Suporte" de [[wiki/concepts/spec-driven-development]]), sem contradição.

10. **Bloco patrocinado Hostinger**: reforça padrões já documentados (deploy de um clique de Claude Code 24x7, Codex, n8n, Docker; servidor no Brasil) e acrescenta produtos não citados antes nesta wiki para a Hostinger — **Horizons** (criação de MVP com IA, com banco de dados, usado pelo canal num hackathon) e um **serviço de GPU em lista de espera** (treino/inferência de modelos). Cita também "openla" (nome provavelmente mal transcrito) e **Hermes Agent** como opções de agente disponíveis, e o **Dokploy** como ferramenta usada pelo próprio canal para gerenciar containers (deploy direto do GitHub, versionamento, backups) — não confundir com o "Coolify" já citado em outras fontes patrocinadas pela Hostinger ([[wiki/sources/ddos-sim-flood-servidor-find-my-saas]]); são produtos de PaaS self-hosted distintos, ambos compatíveis com deploy de um clique na Hostinger.

## Entidades Mencionadas

- [[wiki/entities/codigo-fonte-tv]] — canal autor
- [[wiki/entities/anthropic]] — criadora do Claude, citada na linha do tempo e na distinção de memória (atribuição "OPA" incerta)
- [[wiki/entities/claude-code]] — CLAUDE.md, list agents, deploy na Hostinger
- [[wiki/entities/boris]] — citado sobre graph engineering
- [[wiki/entities/openai]] — ChatGPT, Codex
- [[wiki/entities/codex-openai]] — citado como alternativa ao Claude Code
- [[wiki/entities/opencode]] — citado na lista de harnesses agênticos
- [[wiki/entities/devin-ai]] — citado como precursor histórico
- [[wiki/entities/hostinger]] — bloco patrocinado
- [[wiki/entities/langchain]] *(nova)* — atribuída a cunhagem de "loop engineering" e "graph engineering" em 2026

## Conceitos Tocados

- [[wiki/concepts/loop-engineering]]
- [[wiki/concepts/grafo-como-abstracao-de-agentes]]
- [[wiki/concepts/agent-memory-tres-camadas]]
- [[wiki/concepts/subagentes]]
- [[wiki/concepts/spec-driven-development]]
- [[wiki/concepts/mcp-server]]
- [[wiki/concepts/claude-md]]
- [[wiki/concepts/niveis-adocao-ia-l0-l4]]

## Open Questions

- **"OPA" como possível erro de transcrição de "a própria Anthropic"** — o áudio original não é acessível para verificação direta nesta ingestão; tratado como leitura mais provável dado o contexto (a frase segue imediatamente citando o `CLAUDE.md` do Claude Code). Se uma fonte futura confirmar um produto/empresa real chamado "OPA" nesse espaço, esta atribuição deve ser corrigida.
- **Nome do produto de agente "openla" (Hostinger) não confirmado** — mesmo padrão de transcrição fonética incerta já visto com o "Nine Router" em [[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]]; possivelmente "n8n" mal transcrito de novo, possivelmente um produto distinto — não verificável a partir desta fonte.
- **Atribuição de "graph engineering" à LangChain, mais Boris como voz pública sobre o tema, não vem com link ou citação direta** — mesmo padrão já visto em [[wiki/sources/graph-engineering-do-loop-ao-grafo]] (que atribuía a mesma ideia a um tweet de Peter Steinberger sem link direto). As duas fontes não se contradizem (LangChain batiza o termo formal; Steinberger e Boris são vozes que discutem a ideia publicamente), mas nenhuma das duas foi verificada contra a fonte primária.
- **O item "list agents" é o claim mais verificável e mais novo desta fonte** — descreve um comportamento que corresponde a uma tool real de listagem/mensagens entre agentes no Claude Code; candidato a expansão futura na wiki se uma fonte técnica (changelog oficial, documentação) detalhar o mecanismo exato de handoff e roteamento.

## Raw Quotes

> "Em 2026, a Leng Chain [LangChain] passou a usar esse termo de loop engineering para discutir ali como esses ciclos eles precisam ser projetados."

> "Você não faz o prompt no agente, você desenha o sistema que faz o prompt." *(paráfrase do próprio raciocínio do vídeo sobre a mudança de nível de abstração, não citação direta de terceiro)*

> "Ele tem um recurso chamado list agents onde ele lista todos os agentes disponíveis ali naquele contexto e ele sabe qual é o agente que é o melhor para executar determinada tarefa."

> "Talvez a nova skill de um desenvolvedor não seja 'ah, eu sei usar IA' — na verdade ele tem que saber engenharia de software com IA."
