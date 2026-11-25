---
type: concept
title: "Zonas de Desconhecimento"
aliases: ["unknown unknowns com IA", "falso positivo da IA"]
date_created: 2026-10-08
date_updated: 2026-11-25
source_count: 2
tags: [ia, prompt, conhecimento, falso-positivo]
skill: tech-mentor-ai
status: draft
---

# Zonas de Desconhecimento

**TL;DR:** Os melhores usuários de IA têm poucas zonas de desconhecimento: quanto menos você ignora o que existe e o que pode dar errado, melhor o prompt.

## Dois riscos

1. **Falso positivo:** achar que está certo, mas está errado.
2. **Não saber que está errado** (ou que existe algo melhor): o pior, pois você nem sabe o que questionar.

Mitigar os dois é o que melhora o prompt. Ao desenhar uma arquitetura, quem sabe qual quer, por quê e o que pode falhar usa a IA só como parceiro de conversa e execução ([[wiki/sources/por-que-programadores-tem-os-melhores-prompts-ia-amplia-distancia-balta]]). Variante do falso positivo já citada em [[wiki/concepts/ia-como-amplificador]] e [[wiki/concepts/alucinacao-llm]]. Consequência: [[wiki/concepts/especialista-leva-vantagem-com-ia]] e [[wiki/concepts/fundamentos-e-teoria-na-era-da-ia]].

**Confiança:** média.

## Origem do termo em design de software

"Não saber que está errado" é o que [[wiki/entities/john-ousterhout]] chama de *unknown unknowns* (incógnitas desconhecidas), o pior dos três [[wiki/concepts/sintomas-de-complexidade-ousterhout|sintomas de complexidade]]: há algo que você precisa saber, mas não tem como descobrir o quê, nem se existe algum problema ([[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]]). Lá o remédio é tornar o sistema óbvio; aqui, reduzir o que se ignora antes de delegar à IA.

## Key sources

- [[wiki/sources/por-que-programadores-tem-os-melhores-prompts-ia-amplia-distancia-balta]] — origem desta página
- [[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]] — unknown unknowns no sentido de Ousterhout
