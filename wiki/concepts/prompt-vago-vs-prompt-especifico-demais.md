---
type: concept
title: "Prompt Vago vs. Específico Demais"
aliases: ["tamanho do prompt", "prompt grande ou pequeno"]
date_created: 2026-10-08
date_updated: 2026-11-25
source_count: 2
tags: [prompt-engineering, ia, especificacao]
skill: tech-mentor-ai
status: draft
---

# Prompt Vago vs. Específico Demais

**TL;DR:** Prompt específico demais faz a IA seguir o pedido mesmo havendo solução melhor; vago demais faz ela alucinar e preencher com o que "tem em mente". O ponto ótimo exige que você saiba o que quer.

## Os dois extremos

- **Específico demais:** o modelo obedece, mesmo que conheça algo melhor.
- **Vago demais:** completa lacunas com o padrão do treino (dados da internet). "Cria uma API de produtos" deixa em aberto CQRS, repository, minimal API vs. MVC, autenticação/Identity.

Analogia de Balta: [[wiki/concepts/software-como-construcao-civil]] (milhares de casas possíveis; a melhor depende da necessidade). Fonte: [[wiki/sources/por-que-programadores-tem-os-melhores-prompts-ia-amplia-distancia-balta]]. Liga com [[wiki/concepts/prompt-engineering]], [[wiki/concepts/alucinacao-llm]] e [[wiki/concepts/clareza-antes-do-prompt]].

**Confiança:** média; sem experimento, só experiência relatada.

## FrontPUSH: a landing page do "faz aí para mim"

[[wiki/sources/frontpush-ia-como-dar-comandos-na-ia-da-forma-correta]] dá o exemplo do extremo vago: pedir ao Codex "uma landing page que faça conversão" para uma empresa de engenharia nova, "faz aí para mim", sem tecnologia nem como vai rodar. É "muito parâmetro vazio", e a IA "vai ter que supor e vai alucinar". A saída proposta é dividir em peças ([[wiki/concepts/decomposicao-de-problemas]]) e dar contexto técnico curto. A aula não trata do outro extremo, o específico demais.

## Key sources

- [[wiki/sources/por-que-programadores-tem-os-melhores-prompts-ia-amplia-distancia-balta]] — origem desta página
- [[wiki/sources/frontpush-ia-como-dar-comandos-na-ia-da-forma-correta]]: FrontPUSH, módulo de IA, parte 4: o pedido vago de landing page como contraexemplo
