---
type: concept
title: "Evidenciar o Problema"
aliases: ["simular o erro antes de alterar", "reproduzir o bug"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [bugs, debugging, reproducao, evidencia, qa, testes]
skill: tech-mentor-testing
status: draft
---

# Evidenciar o Problema

Passo 2 de [[wiki/concepts/tres-passos-para-lidar-com-bug]]: **fazer o erro acontecer antes de alterar qualquer coisa**. Entendido o erro, a solução fica clara; sem evidência o dev corrige "no olho" ([[wiki/concepts/armadilha-da-certeza-do-dev-experiente]]).

- **Não é só debug**: na sustentação pode faltar acesso ou tempo de montar o ambiente. A evidência pode ser um **log**, uma **mensagem/print do usuário** ou um comportamento na tela; depois se descobre como chegar ao mesmo ponto (tela, código, caso).
- **Converse**: o **QA** explora ("com o campo X dá erro, com outra opção não") e ensina a testar; o **usuário** colaborativo ensina o negócio. Evitar a frieza do "me manda o link".
- **Dados por último**: acesso ao banco de produção ajuda, mas pode ser proibido por compliance/[[wiki/concepts/lgpd]]; raramente é impeditivo. Se se sabe que o problema ocorre ao preencher X, simula-se em outro ambiente.

Relacionados: [[wiki/concepts/reprodutibilidade-de-bugs]] (reprodução depende de entradas/estado explícitos), [[wiki/concepts/debugging]], [[wiki/concepts/provar-que-corrigiu]] (a evidência vira o teste que se repete). Fonte: [[wiki/sources/como-sair-do-ciclo-de-bugs-e-retrabalho-andre-casciotti]].

## Key Sources

- [[wiki/sources/como-sair-do-ciclo-de-bugs-e-retrabalho-andre-casciotti]]
