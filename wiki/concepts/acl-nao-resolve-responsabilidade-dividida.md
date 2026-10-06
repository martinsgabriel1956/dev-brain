---
type: concept
title: "ACL não resolve responsabilidade dividida"
aliases: ["responsabilidade dividida entre legado e novo", "migrar entidade inteira"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [anti-corruption-layer, bounded-context, migracao, responsabilidade, strangler-fig]
skill: tech-mentor-backend
status: stub
---

# ACL não resolve responsabilidade dividida

Para [[wiki/sources/anti-corruption-layer-microsservicos-requisitos-arquiteturais]], a primeira exigência da [[wiki/concepts/anti-corruption-layer]] é **isolar subsistemas com responsabilidades claras** ("quase como pensar em [[wiki/concepts/bounded-context|Bounded Contexts]]"): quem requisita, quem responde, o que vai em cada mensagem. É a "grande dor" do padrão.

A camada ajuda quando uma alteração no sistema A não pode ser feita e é desviada para B. Ela **não** conserta uma mesma responsabilidade partida entre os dois lados. Exemplo do autor: salvar uma **pessoa** com parte no legado (entidade pessoa) e parte em microsserviços (telefone, endereço, e-mail): o "salvar" fica dividido e uma falha lá exige desfazer aqui. Conselho: **migrar a entidade inteira junto**, não parte no legado e parte no novo ([[wiki/concepts/strangler-fig-pattern]]).

Recomenda também uma camada por sistema consumidor ([[wiki/questions/acl-facade-vs-adapter-criterio-por-lado-ou-por-chamadas]]).

## Key sources

- [[wiki/sources/anti-corruption-layer-microsservicos-requisitos-arquiteturais]]
