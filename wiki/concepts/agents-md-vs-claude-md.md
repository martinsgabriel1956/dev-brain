---
type: concept
title: "AGENTS.md vs. CLAUDE.md"
aliases: ["agents.md", "fragmentação de config de agentes", "controvérsia agents md shopify"]
date_created: 2026-09-14
date_updated: 2026-09-21
source_count: 2
tags: [claude-code, agents-md, claude-md, padronizacao, interoperabilidade, multi-agente, shopify]
skill: tech-mentor-ai
status: stub
---

# AGENTS.md vs. CLAUDE.md

## TL;DR

Conflito de padronização entre agentes de codificação de IA: o formato `AGENTS.md` surgiu como um arquivo de instruções/contexto de projeto compartilhado, lido por múltiplos agentes de diferentes fornecedores (ex. Codex, da [[wiki/entities/openai|OpenAI]]). O [[wiki/entities/claude-code|Claude Code]] da [[wiki/entities/anthropic|Anthropic]], porém, lê apenas o seu próprio formato, [[wiki/concepts/claude-md|CLAUDE.md]] — obrigando projetos que usam mais de um agente a manter os dois arquivos em paralelo.

## A Controvérsia Pública (Shopify)

Segundo relatado em [[wiki/sources/guia-claude-code-para-startups-anthropic-ai-native-sdlc]], **Tobi Lütke**, CEO da [[wiki/entities/shopify|Shopify]], declarou publicamente (no Twitter/X) estar considerando banir o Claude Code dentro da empresa até a Anthropic mudar sua posição e passar a suportar o `AGENTS.md`. Um funcionário da Anthropic (citado na fonte como "Tarik", grafia incerta) respondeu publicamente, justificando a escolha com o argumento de que o modelo Claude é "muito diferente" dos demais, e por isso o Claude Code só lê o `CLAUDE.md`.

> **Nota de verificação**: os detalhes exatos dessa troca pública (texto literal, nomes corretos, se houve resposta oficial da empresa) não foram confirmados contra os posts originais nesta sessão — relatados de memória pelo autor da fonte.

## A Crítica ao Argumento da Anthropic

A fonte argumenta que a justificativa "o modelo é muito diferente, por isso não lemos configuração de outros agentes" é inconsistente por si só: se modelos diferentes de fato não são intercambiáveis e um *system prompt* tem impacto relevante na performance (fato já bem estabelecido — ver [[wiki/concepts/prompt-engineering]]), então por essa mesma lógica um único `CLAUDE.md` também não deveria servir igualmente bem para todos os modelos de uma mesma família da Anthropic (ex. Sonnet vs. modelos mais fortes como "Fable"). O argumento é usado para sustentar que a recusa em ler `AGENTS.md` é uma decisão de posicionamento de mercado/lock-in, não puramente técnica.

## O Problema Real: Compartilhamento de Skills

Independente da controvérsia pública específica, a fonte aponta que compartilhamento de "skills"/configurações entre equipes é uma dor real e recorrente entre as startups entrevistadas no playbook da Anthropic. Sem um padrão compartilhado entre agentes, cada equipe (ou cada agente usado) acaba mantendo sua própria versão de regras, o que gera divergência de comportamento e trabalho duplicado de manutenção.

## Contradição com Outra Fonte da Wiki

[[wiki/entities/anthropic]] já registrava, a partir de [[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]], uma menção de passagem a uma **preferência da própria Anthropic por `AGENTS.md`** (atribuída a [[wiki/entities/boris|Boris]], criador do Claude Code). Isso está em tensão direta com o relato desta fonte, de que o Claude Code só lê `CLAUDE.md` e que a Anthropic recusou publicamente adotar `AGENTS.md` na controvérsia com Tobi Lütke. Nenhuma das duas fontes é uma referência primária (changelog oficial, documentação) — ambas são relatos de segunda mão. Registrado como contradição em aberto, não resolvida nesta sessão: pode refletir uma mudança de posição da Anthropic entre os dois momentos, informação desatualizada em uma das fontes, ou imprecisão de uma das transcrições.

## Enquadramento: Documentação para uma "Terceira Audiência"

[[wiki/sources/7-coisas-desenvolvedores-2026-max-lorian]] enquadra o fenômeno de um ângulo distinto da controvérsia de padronização: para além de qual formato específico vence, o autor observa que repositórios passaram a ter uma **terceira audiência** de leitores — além do compilador e dos humanos que mantêm o código, agora existe o agente, que precisa saber o que pode mudar, como testar, quais fronteiras importam e qual comando realmente funciona "apesar do que o README diz". O GitHub já vai além: usa o Copilot para *gerar* as instruções que depois vão guiar o próprio Copilot no repositório — documentação que aprende a se reproduzir. O autor nota o efeito colateral: trabalho de engenharia que ficava perpetuamente adiado porque humanos conseguiam contornar a bagunça (ex. um build process que só vive na cabeça de um dev específico) agora tem um "cliente" sem bom senso algum, e passa a doer a cada execução de agente — pressão indireta para formalizar exatamente o tipo de regra que arquivos como `AGENTS.md`/`CLAUDE.md` tentam capturar.

## Relação com Outros Conceitos

- [[wiki/concepts/claude-md]] — o lado "Anthropic" da fragmentação
- [[wiki/concepts/sdlc-nativo-de-ia]] — listado como uma das lacunas do framework de 5 regras
- [[wiki/entities/codex-openai]] — agente que lê `AGENTS.md`

## Key Sources

- [[wiki/sources/guia-claude-code-para-startups-anthropic-ai-native-sdlc]]
- [[wiki/sources/7-coisas-desenvolvedores-2026-max-lorian]] — enquadra `AGENTS.md`/`CLAUDE.md` como documentação para uma "terceira audiência" (o agente), além de compilador e humano
