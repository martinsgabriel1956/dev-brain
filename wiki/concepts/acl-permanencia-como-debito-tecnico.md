---
type: concept
title: "ACL: permanência como débito técnico"
aliases: ["acl temporária", "camada anticorrupção que nunca sai"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [anti-corruption-layer, debito-tecnico, migracao, legado]
skill: tech-mentor-backend
status: stub
---

# ACL: permanência como débito técnico

Em DDD, a [[wiki/concepts/anti-corruption-layer]] durar para sempre não é problema: faz parte da solução. Numa **migração** legado → microsserviços ela existe para levar o legado à versão nova; enquanto os dois sistemas coexistem faz sentido, depois vira [[wiki/concepts/tech-debt|débito técnico]] cada vez mais pesado de manter e evoluir ([[wiki/sources/anti-corruption-layer-microsservicos-requisitos-arquiteturais]]).

**Caso relatado:** legado totalmente migrado, mas um "croninho" atualizava uma tabela enorme (usada em data warehouse/relatórios) que um microsserviço também alterava; sem quebrar responsabilidades, o único caminho era pela ACL, com volta por vários microsserviços (cada um com seu micro database) e duplicidade de dados. A camada ainda existia quando o autor saiu da empresa.

Implicação prática: planejar a **saída** da ACL junto com a migração ([[wiki/concepts/strangler-fig-pattern]], fase Eliminate), incluindo dependências "esquecidas" como jobs e tabelas compartilhadas. Esta frase é leitura minha, não afirmação da fonte.

## Key sources

- [[wiki/sources/anti-corruption-layer-microsservicos-requisitos-arquiteturais]]
