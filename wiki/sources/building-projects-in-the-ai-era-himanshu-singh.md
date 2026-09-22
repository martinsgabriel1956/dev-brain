---
type: source
title: "Building Projects in the AI Era for Software Engineers"
aliases: ["building projects ai era", "himanshu singh vibe coding", "agentfriendlycode usetu.la"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 0
tags: [vibe-coding, prompt-engineering, autonomy-slider, hallucination, human-in-the-loop, subagentes, governanca-de-codigo-gerado-por-ia]
skill: tech-mentor-ai
status: stable
source_file: "raw/building-projects-in-the-ai-era-for-software-engineers.md"
source_url: "https://hsnice16.medium.com/building-projects-in-the-ai-era-for-software-engineers-72f3ddcd2a40"
author: "Himanshu Singh"
date_published: "2026-09-13"
date_ingested: "2026-09-21"
---

## TL;DR

Himanshu Singh, engenheiro full-stack focado em Web3, construiu dois projetos ([agentfriendlycode.com](https://agentfriendlycode.com/) e [usetu.la](https://usetu.la/)) inteiramente via IA, sem ler ou digitar código manualmente. Compartilha cinco práticas empíricas: fazer muitas perguntas antes de pedir implementação (brainstorm → user flow → segurança → arquitetura → só então codar); um checklist de verificação explícito rodado antes de cada commit em vez de revisão linha a linha; encerrar a sessão e recomeçar do zero ao notar sinais de alucinação/degradação; usar referências visuais (screenshots de UI com problema apontado) em vez de descrição textual; e usar um único agente por vez, não swarms — ao contrário de parte da comunidade.

---

## Reivindicações Principais

**Claim:** Perguntas extensas antes de pedir implementação (brainstorm de soluções → user flow → segurança → arquitetura) produzem melhor entendimento do agente sobre o que é esperado.
**Evidência:** Relato de primeira mão, sem métrica comparativa — o autor descreve o próprio fluxo, não testa alternativa.
**Confiança:** Média — consistente com o padrão "Tell It" já documentado em [[wiki/concepts/prompt-engineering]], mas sem dado quantitativo.

**Claim:** Um checklist de verificação explícito pedido ao próprio agente antes de cada commit (best practices, comentários, consistência entre arquivos, ausência de vazamento de dados sensíveis, UX/segurança) substitui a leitura linha a linha do código gerado.
**Evidência:** Prática relatada, rodada "antes de cada commit e às vezes no meio de mudanças grandes"; sem verificação externa de que o checklist realmente captura os problemas que uma leitura humana capturaria.
**Confiança:** Média — é uma variante concreta da tensão já registrada em [[wiki/concepts/code-review]] ("Por Que o Looking Good to Me Aumentou com Agentes Autônomos") e em [[wiki/concepts/governanca-de-codigo-gerado-por-ia]], mas o autor não relata nenhum incidente que o checklist tenha deixado passar.

**Claim:** Encerrar a conversa e iniciar uma sessão nova ao perceber respostas "não tão boas" é uma forma prática (não técnica) de lidar com alucinação/degradação.
**Evidência:** Heurística subjetiva do autor ("posso estar errado"), sem medição de tokens ou threshold formal.
**Confiança:** Média — consistente com o mecanismo documentado em [[wiki/concepts/degradacao-de-contexto]] (`/clear` + nova sessão), mas aplicado por sinal qualitativo, não por contagem de tokens.

**Claim:** Fornecer uma referência visual (screenshot apontando o problema específico de UI) produz melhor resultado do que descrever o problema em texto, geralmente em poucas iterações.
**Evidência:** Observação empírica do autor sobre UI especificamente; não generaliza para outros tipos de tarefa.
**Confiança:** Alta como padrão específico de UI — consistente com a recomendação já documentada em [[wiki/concepts/prompt-engineering]] ("Verificação Embutida no Prompt") de comparar screenshot com design de referência.

**Claim:** Um único agente por sessão (não swarms/múltiplos agentes em paralelo) é suficiente para o volume de trabalho do autor.
**Evidência:** Autor observa outros desenvolvedores no X rodando swarms, mas não adota isso — atribui a diferença ao próprio volume de tarefas, não a uma crítica técnica ao padrão de swarm.
**Confiança:** Baixa como generalização — é uma escolha pessoal de escala, não um argumento contra swarms; ver [[wiki/concepts/subagentes]] para benchmarks de campo que tratam a questão de granularidade com mais rigor.

---

## Entidades

- [[wiki/entities/himanshu-singh]] — autor do relato, engenheiro full-stack focado em Web3

## Conceitos

- [[wiki/concepts/prompt-engineering]] — padrão de perguntas extensas antes de implementar como variante do "Tell It"/spec-first
- [[wiki/concepts/vibe-coding]] — dois projetos construídos inteiramente por IA sem código manual, mas com disciplina de verificação (não é vibe coding "no talo" sem critério)
- [[wiki/concepts/human-in-the-loop]] — checklist de verificação pré-commit como forma de HITL delegada ao próprio agente, não ao humano lendo o diff
- [[wiki/concepts/code-review]] — checklist explícito como substituto declarado da leitura linha a linha
- [[wiki/concepts/governanca-de-codigo-gerado-por-ia]] — caso de zero leitura de código com julgamento deslocado para perguntas upfront + checklist de verificação, não para revisão pós-geração
- [[wiki/concepts/alucinacao-llm]] — reiniciar sessão como mitigação heurística/qualitativa
- [[wiki/concepts/degradacao-de-contexto]] — mesmo mecanismo do `/clear` + nova sessão, mas disparado por percepção subjetiva de qualidade, não por contagem de tokens
- [[wiki/concepts/autonomy-slider]] — volume próximo do máximo (zero código manual, zero leitura) mas com disciplina de verificação explícita, não "faz o que quiser" sem critério
- [[wiki/concepts/subagentes]] — contraponto anedótico: um único agente basta para o volume de trabalho do autor, sem necessidade de swarm

## Ver também

- [[wiki/sources/vibe-coding-limites-maturidade-profissional]] — mesma tensão central (o que a IA não supre sozinha), mas focada em contexto organizacional/arquitetura em vez do fluxo pessoal de verificação
- [[wiki/sources/code-was-never-the-hard-part-reacao-lucas-montana]] — outro relato de dev sênior sem escrever código manualmente há meses, com revisão automatizada substituindo leitura humana
- [[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] — outra mitigação para o mesmo problema (perda da janela de revisão incremental), via skill que inverte quem audita quem

---

## Conexões com Outras Sources

- [[wiki/sources/porque-nunca-confiar-em-llm-alucinacao]] — a mitigação "reiniciar sessão" desta fonte é qualitativa/heurística, enquanto aquela fonte documenta um pipeline formal (RAG + LLM-as-judge medindo faithfulness) para o mesmo problema de fundo
- [[wiki/sources/extrair-melhor-codigo-de-agentes-ia-planejamento-plan-mode-skills]] — mesmo padrão de "prompt específico + contexto/referência" reduzindo a necessidade de retrabalho
- [[wiki/sources/subagentes-quando-vale-a-pena-custo-velocidade-tlc-spec-driven]] — contraste direto: aquela fonte testa rigorosamente quantos subagentes valem a pena; esta fonte relata, sem testar, que um único agente já é suficiente para o próprio volume

---

## Perguntas Abertas

- O checklist de verificação pré-commit relatado aqui já capturou algum bug real que teria passado despercebido, ou é apenas uma prática preventiva sem incidente documentado que a justifique?
- A ausência de swarms é escolha deliberada por menor volume de trabalho (como o autor sugere) ou também reflete o mesmo achado do benchmark em [[wiki/sources/subagentes-quando-vale-a-pena-custo-velocidade-tlc-spec-driven]] de que granularidade excessiva piora qualidade?
- Como o "hack" de reiniciar sessão ao notar alucinação se compara, em eficácia, ao threshold técnico de ~400k tokens documentado em [[wiki/concepts/degradacao-de-contexto]] — o sinal qualitativo do autor aparece antes ou depois do limiar técnico?

---

## Citações

> "Before committing, I always ask the agent to do these things: Make sure the code is following all the best practices [...] Make sure you do it carefully. This is important."

> "Whenever I start seeing a not-so-good response, I try to end the conversation with a closing statement, then close the terminal, and start a fresh new session."

> "If you give the agent a reference for what you are expecting and what the correct thing should look like, it produces a good output within a couple of iterations."

> "I have seen folks on X mentioning how they are running swarms of agents to do multiple things at once [...] But I don't think I can do that right now. Maybe because I don't have that many things to run at once."
