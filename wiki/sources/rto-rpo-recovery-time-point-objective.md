---
type: source
title: "RTO e RPO — Recovery Time / Point Objective"
aliases: ["RTO", "RPO", "Recovery Time Objective", "Recovery Point Objective"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 0
tags: ["rto", "rpo", "disaster-recovery", "confiabilidade", "arquitetura", "infra"]
skill: tech-mentor-infra
status: stable
source_file: "raw/rto-rpo-recovery-time-point-objective.md"
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-08-03
---

# RTO e RPO — Recovery Time / Point Objective

## TL;DR

Aula curta em português (transcrição, sem necessidade de tradução) que introduz dois indicadores focados em cenários de desastre: **RTO (Recovery Time Objective)** — quanto tempo leva para restaurar um serviço indisponível — e **RPO (Recovery Point Objective)** — quanto de dado é aceitável perder, medido a partir do último backup válido. A tese central é que esses dois números não são detalhe operacional: eles precisam ser definidos *antes* de escolher a arquitetura, porque o padrão arquitetural escolhido impõe um piso de RTO/RPO possível, e o valor tolerável de cada um depende inteiramente do negócio (sistema financeiro vs. e-commerce vs. microsserviço de catálogo têm tolerâncias completamente diferentes).

## Key Claims

1. **RTO é o tempo de recuperação do serviço após uma queda**, e algumas arquiteturas têm um piso estrutural de RTO que não dá para contornar sem mudar o padrão.
   - Evidência: *"tem arquiteturas que o tempo de recuperação, se você escolher um padrão ali, é quase impossível você atender menos que 1h, por exemplo."*

2. **RTO precisa ser confrontado com o custo de downtime do negócio, não decidido isoladamente.** O exemplo usado é um site de vendas que fatura ~$1.000/minuto — duas horas de indisponibilidade têm um custo direto e quantificável que deve pressionar a escolha arquitetural.
   - Evidência: *"esse é um site de vendas que você vende ali 1.000 dólares por minuto. Quanto dinheiro você não vai perder em duas horas?"*

3. **RPO é definido pela distância até o último backup válido, não por um número abstrato.** Se o incidente ocorre ao meio-dia e o último backup foi às 10h, o RPO efetivo daquele incidente é de duas horas de dados perdidos.
   - Evidência: *"imagina se agora é meio-dia que deu problema. O último backup foi das 10h. Você perdeu duas horas de dados."*

4. **A tolerância a perda de dados (RPO) é estritamente dependente do domínio de negócio — não existe um valor "correto" universal.** Um sistema financeiro não tolera nenhuma janela de perda (não pode haver ambiguidade sobre quem transferiu o quê); um e-commerce não pode perder vendas já registradas; mas um microsserviço de cadastro de produtos para venda pode, em alguns casos, absorver a perda de duas horas de registros sem inviabilizar o negócio.
   - Evidência: *"vamos pensar um sistema financeiro [...] não tem como você perder duas horas [...] então não é cabível"* vs. *"eu poderia perder duas horas de todos os meus registros que foram adicionados [...] isso iria afetar o negócio, mas às vezes eu posso comportar isso."*

5. **RTO e RPO devem ser definidos antes da arquitetura, não depois.** Conhecer esses dois números é o que determina qual padrão arquitetural, qual estratégia de backup/replicação e qual design de sistema são necessários — não o contrário.
   - Evidência: *"você tem que saber qual que é o RTO e o RPO da sua aplicação para saber qual é a arquitetura na qual arquitetura você precisa implementar, qual o padrão que você precisa implementar [...] qual que vai ser o design dela."*

## Entities

Nenhuma entidade nomeada (pessoa, empresa, produto) — aula genérica/didática, usa exemplos hipotéticos (site de vendas, sistema financeiro, microsserviço de catálogo) sem citar ferramentas ou empresas específicas.

## Concepts

- [[wiki/concepts/rto]] (novo)
- [[wiki/concepts/rpo]] (novo)
- [[wiki/concepts/alta-disponibilidade]]
- [[wiki/concepts/sre]]
- [[wiki/concepts/finops]]
- [[wiki/concepts/tolerancia-a-falha]]

## Open Questions

- A fonte não menciona explicitamente "Disaster Recovery" ou "backup" como estratégia nomeada (Multi-Region, cold/warm/hot standby) — fica implícito que RPO é função do intervalo de backup, mas os mecanismos concretos (snapshot, replicação assíncrona, WAL shipping) não são detalhados.
- Não há discussão de como RTO/RPO se relacionam formalmente com [[wiki/concepts/sla]]/[[wiki/concepts/slo]] — a aula trata RTO/RPO como indicadores próprios de cenário de desastre, distintos (mas complementares) ao par SLI/SLO/SLA já documentado na wiki para disponibilidade contínua.
- O exemplo de custo ($1.000/minuto) não é aprofundado em uma fórmula (ex.: custo esperado de downtime = RTO × receita/minuto × probabilidade de incidente) — fica como raciocínio qualitativo, não quantitativo.

## Raw Quotes

> "Existem dois indicadores. Um se chama RTO de Recovery Time Objective [...] e aí nós temos o RPO, que é o Recovery Point Objective."

> "Você tem que saber qual que é o RTO e o RPO da sua aplicação para saber qual é a arquitetura na qual você precisa implementar."

## Key Sources (páginas que citam esta fonte)

—
