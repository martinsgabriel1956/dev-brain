---
type: concept
title: "MicroservicePremium"
aliases: ["microservice premium", "prêmio de microsserviços", "sobretaxa de microsserviços"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 1
tags: [microsservicos, monolito, arquitetura, martin-fowler, custo-beneficio]
skill: tech-mentor-backend
status: stub
---

# MicroservicePremium

Termo cunhado por Martin Fowler em [[wiki/sources/monolith-first-martin-fowler]] para o custo estrutural de adotar [[wiki/concepts/microsservicos]]: gerenciar um conjunto de serviços distribuídos (comunicação de rede, deploys independentes, observabilidade distribuída, consistência eventual) é mais caro operacionalmente do que rodar um [[wiki/concepts/monolito]]. Mesmo defensores de microsserviços reconhecem esse prêmio — ele só compensa quando o sistema é complexo o suficiente para que os benefícios (escala seletiva, times independentes, deploy independente) superem o custo. Para aplicações simples ou no início de um projeto novo, o prêmio favorece o monolito — é a base do argumento [[wiki/concepts/yagni|YAGNI]] em [[wiki/concepts/monolith-first]].

## Key Sources

- [[wiki/sources/monolith-first-martin-fowler]] — cunhagem do termo, argumento central de que o prêmio só compensa em sistemas complexos
