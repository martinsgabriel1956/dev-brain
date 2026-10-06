---
type: concept
title: "ACL: requisitos arquiteturais afetados"
aliases: ["quando aplicar anti-corruption layer", "matriz de requisitos da acl"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [anti-corruption-layer, requisitos-arquiteturais, trade-off, microsservicos, migracao]
skill: tech-mentor-backend
status: draft
---

# ACL: requisitos arquiteturais afetados

Critério do autor de [[wiki/sources/anti-corruption-layer-microsservicos-requisitos-arquiteturais]] para decidir se a [[wiki/concepts/anti-corruption-layer]] vale a pena numa migração para [[wiki/concepts/microsservicos]]: comparar o padrão com os requisitos arquiteturais de maior criticidade para o negócio (ver [[wiki/concepts/requisitos-funcionais-e-nao-funcionais]]).

| Efeito | Requisitos | Por quê |
|---|---|---|
| **Ajuda** | time to market, manutenibilidade, integrabilidade, adaptabilidade | Não se altera o legado; integração isolada na camada; mudanças do lado novo não vazam |
| **Parcial** | segurança, testabilidade | Camada é um ponto extra de ataque/parse; difícil testar a volta ao legado e ter visão integrada |
| **Impactado, com contorno** | disponibilidade, observabilidade, experiência do usuário | Chamadas lentas/retries acumulam conexões no legado; trace fim a fim mais difícil; mais tempo de resposta |
| **Impactado (degrada)** | performance, escalabilidade, elasticidade | Salto de rede extra; escalar um lado não escala o outro; custo sobe e dificilmente desce |

**Regra do autor:** se os quatro primeiros são altos, o padrão faz sentido; se performance, escalabilidade ou elasticidade são o requisito dominante, reconsiderar. Se a manutenibilidade é baixa mas o time to market é alto, ainda pode valer. Não é fórmula mágica; exige criticidade ponderada e o requisito mais importante explícito.

**Ressalva:** a classificação é julgamento do autor, não medição; os termos "atendido/parcial/inferido" são dele. Complementa com [[wiki/concepts/diferenca-semantica-entre-sistemas]] (quando não usar) e [[wiki/concepts/acl-permanencia-como-debito-tecnico]].

## Key sources

- [[wiki/sources/anti-corruption-layer-microsservicos-requisitos-arquiteturais]]
