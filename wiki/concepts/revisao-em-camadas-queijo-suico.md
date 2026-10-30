---
type: concept
title: "Revisão em Camadas (Queijo Suíço)"
aliases: ["swiss cheese code review", "sete camadas de revisão", "defesa em profundidade de PR"]
date_created: 2026-10-26
date_updated: 2026-10-26
source_count: 1
tags: [code-review, agentes, qualidade, anthropic, defesa-em-profundidade, lights-off]
skill: tech-mentor-ai
status: draft
---

# Revisão em Camadas (Queijo Suíço)

Em vez de um único revisor (humano ou agente), empilhar camadas de checagem imperfeitas — cada uma com "furos" — de modo que um bug só chega à produção se atravessar todos. É como a [[wiki/entities/anthropic]] descreve seu pipeline para ~30 mil mudanças/dia em [[wiki/sources/anthropic-code-review-por-agentes-sete-camadas]].

## A pergunta que muda

De "alguém leu esse código?" para **"o que pode dar errado se isso for para produção e qual checagem pega melhor?"** — com a trava de que menos revisão humana **não pode** aumentar reverts nem incidentes; se subirem, só se trocou revisar por consertar.

## As sete camadas

| # | Camada | O que faz |
|---|---|---|
| 1 | Pré-PR | testes, build, lint + **segundo agente de contexto limpo** revisando o diff ([[wiki/concepts/revisao-por-agente-independente]]) |
| 2 | CI/CD | lint, tipos, testes, build; vermelho trava o merge ([[wiki/concepts/quality-gate]]) |
| 3 | Review por agentes em todo PR | diff × repositório inteiro × intenção do PR; consenso ([[wiki/concepts/consenso-multiagente-em-code-review]]) |
| 4 | Segurança | citada de passagem |
| 5 | Humanos por nível | 0 / 1 / 2 pessoas via classificador ([[wiki/concepts/classificador-de-risco-de-revisao-humana]]) |
| 6 | Fila de merge | checagens rodam de novo sobre a main |
| 7 | Pós-merge | flag interna, release gradual, conserto ou revert ([[wiki/concepts/confianca-por-reversibilidade]]) |

## Leitura [skill: tech-mentor-ai]

As camadas 1–3 e 6 são determinísticas ou probabilísticas **independentes entre si**; o ganho do queijo suíço depende de os furos não se alinharem, o que justifica contexto limpo e agentes distintos. A camada 7 é a rede de segurança que torna aceitável o falso negativo das anteriores. Ver [[wiki/concepts/harness-de-qualidade]] para o ferramental e [[wiki/concepts/matriz-risco-dificuldade-review-ia]] para a versão de transição para times que ainda revisam 100%.

## Ressalvas

- O apresentador separa o que é replicável (contexto limpo, `REVIEW.md`, teto de rodadas) do "sonho de consumo" (custo de tokens, código público que o modelo conhece) — ver [[wiki/concepts/limites-empiricos-de-revisao-por-ia]].

## Key sources

- [[wiki/sources/anthropic-code-review-por-agentes-sete-camadas]]
