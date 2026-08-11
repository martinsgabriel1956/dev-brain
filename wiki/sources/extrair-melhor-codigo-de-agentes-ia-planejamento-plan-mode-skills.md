---
type: source
title: "Extrair um Código Melhor dos Agentes de IA: Planejamento, Plan Mode e Skills"
aliases: ["verdent plan mode skills", "refatorar com strategy pattern ia", "erro numero um usando ia"]
date_created: 2026-08-11
date_updated: 2026-08-11
source_count: 0
tags: [plan-mode, skills, prompt-engineering, refatoracao, strategy-pattern, alucinacao-llm, verdent, coding-agents]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/extrair-melhor-codigo-de-agentes-ia-planejamento-plan-mode-skills.md
source_url: ""
author: ""
date_published: 2026
date_ingested: 2026-08-11
---

# Extrair um Código Melhor dos Agentes de IA: Planejamento, Plan Mode e Skills

## TL;DR

Transcrição de vídeo demonstrando, na IDE **Verdent AI**, três mudanças pequenas que elevam muito a qualidade do código gerado por agentes: (1) **prompt específico + contexto** (arquivos, referências, o design pattern desejado) em vez de prompt genérico; (2) **modo plan** — a IA mapeia dependências, monta uma especificação técnica com diagrama Mermaid, pergunta em pontos ambíguos e só programa depois que o plano é revisado/comentado; (3) **skills** — camada de injeção de contexto acionada automaticamente por descrição/keywords, que sobrescreve o comportamento genérico da LLM e combate alucinação de pacotes e a necessidade de repetir padrões internos. O "erro número um" é deixar a IA escrever código **sem planejar antes**. Exemplo prático: refatorar dois gateways de pagamento (Stripe, Abacate Pay) num app Next.js aplicando o [[wiki/concepts/strategy-pattern|Strategy Pattern]].

## Afirmações-chave

| Afirmação | Evidência | Confiança |
|---|---|---|
| O erro nº 1 dos devs usando IA é deixá-la escrever código sem planejar primeiro | Tese central do vídeo | Média-alta (opinião fundamentada) |
| Prompt genérico ("organize/refatore") transfere decisões subjetivas para a IA, abrindo espaço para erro | Demonstração: refatoração rasa (só moveu arquivos de pasta) | Alta |
| Iniciar um chat do zero zera o contexto e evita contaminação da tarefa anterior | Prática demonstrada | Alta (alinha com [[wiki/concepts/separacao-de-contextos]]) |
| Modo plan faz a IA mapear dependências e gerar uma especificação técnica revisável antes de codar | Demonstração | Alta (alinha com [[wiki/concepts/plan-mode]]) |
| No modo plan, a IA pergunta antes de decidir em pontos ambíguos, em vez de assumir a resposta mais provável | Demonstração | Média-alta (depende da ferramenta/modelo) |
| Mencionar arquivos e uma URL de referência (Refactoring Guru) no prompt melhora o resultado | Demonstração | Alta |
| Alucinação de pacotes/métodos ocorre porque LLMs foram treinadas em código público, não no código interno da empresa | Explicação do autor | Média-alta (mecanismo plausível) |
| Skill = arquivo `SKILL.md` (markdown) cujo título/descrição decidem quando ela é acionada automaticamente | Demonstração + inspeção do arquivo | Alta (alinha com [[wiki/concepts/skills-agente]]) |
| Skill só injeta o corpo quando acionada — economiza janela de contexto | Explicação do autor | Alta (lazy loading, ver [[wiki/concepts/skills-agente]]) |
| Contexto demais/irrelevante pode confundir o modelo — mais informação nem sempre é melhor | Explicação do autor | Alta (alinha com [[wiki/concepts/degradacao-de-contexto]]) |
| Existe uma "skill que cria skills" (Skill Creator) que lê seu próprio `SKILL.md` e roda scripts para gerar novas skills | Demonstração na Verdent | Alta (é [[wiki/concepts/meta-prompting|meta]]) |
| Skills da comunidade podem ser importadas; o valor de criar as próprias é adaptá-las ao contexto interno da empresa | Importou skill de front-end de terceiro | Alta |

## Entidades

- [[wiki/entities/verdent-ai]] — IDE com IA nativa usada na demonstração (múltiplos agentes paralelos, skills, modo plan); em beta.
- [[wiki/entities/refactoring-guru]] — catálogo de design patterns usado como referência no prompt e empacotado como `references/` da skill criada.
- [[wiki/entities/anthropic]] — criadora do padrão de skills de harness (nov/2025), referenciada indiretamente pelo formato usado.

## Conceitos

- [[wiki/concepts/plan-mode]] — planejar antes de executar; especificação técnica revisável.
- [[wiki/concepts/skills-agente]] — injeção de contexto sob demanda; combate alucinação e repetição.
- [[wiki/concepts/prompt-engineering]] — especificidade e contexto (arquivos, referências).
- [[wiki/concepts/refatoracao]] — o caso de uso do vídeo (comportamento externo preservado, front end intacto).
- [[wiki/concepts/strategy-pattern]] — o padrão aplicado aos gateways de pagamento.
- [[wiki/concepts/alucinacao-llm]] — pacotes/métodos inexistentes; por que ocorre.
- [[wiki/concepts/meta-prompting]] — a skill que cria skills.
- [[wiki/concepts/separacao-de-contextos]] — chat do zero para não contaminar a tarefa.
- [[wiki/concepts/degradacao-de-contexto]] — contexto demais confunde o modelo.
- [[wiki/concepts/codigo-legado-ia]] — o cenário de abertura (refatorar legado com IA).
- [[wiki/concepts/design-patterns]] — o catálogo empacotado na skill de referência.

## Perguntas em aberto

- O autor afirma que a IA "pergunta antes de decidir em pontos ambíguos" no modo plan. Isso depende fortemente da ferramenta e do modelo — não é garantido em todo harness. Candidato a triangulação com [[wiki/concepts/plan-mode]] (que não documenta o comportamento de perguntar como intrínseco).
- A demonstração ("qualidade infinitamente superior") não é acompanhada de testes automatizados rodando verdes — a validação do resultado é visual/estrutural, não empírica. Contrasta com a exigência de cobertura de testes documentada em [[wiki/concepts/refatoracao]].

## Quotes

> "O erro número um entre os devs hoje utilizando IA é deixar que ela escreva o código sem planejar primeiro."

> "Organizar código é subjetivo... quando fica muito amplo, fica aberto pra decisão da IA — e quem acaba decidindo é a IA."

> "Toda skill nada mais é do que um arquivo markdown que vai dar contexto para alguma tarefa, para eu não precisar ficar repetindo isso sempre."

> "Não é só porque você passou mais informação que a IA vai trazer um resultado melhor — o contexto também tem que ser otimizado pra tarefa."
