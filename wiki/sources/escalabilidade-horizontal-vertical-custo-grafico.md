---
type: source
title: "Escalabilidade Horizontal vs Vertical — Diferença e Custo"
aliases: ["escalabilidade horizontal vertical custo", "scale up vs scale out custo"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 0
tags: [system-design, escalabilidade, escalabilidade-vertical, escalabilidade-horizontal, finops, resiliencia]
skill: tech-mentor-system-design
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/escalabilidade-horizontal-vertical-custo-grafico.md
source_url:
author: desconhecido (aula curta, série de System Design)
date_published:
date_ingested: 2026-08-03
---

# Escalabilidade Horizontal vs Vertical — Diferença e Custo

## TL;DR

Aula curta e introdutória sobre a diferença entre escalabilidade horizontal e vertical, com foco em duas analogias visuais (horizonte para horizontal, imagem esticada por todos os lados para vertical) e um exemplo gráfico de custo/consumo ao longo do tempo: horizontal permite adicionar exatamente a capacidade necessária (ex.: um servidor a mais), enquanto vertical em cloud providers geralmente força dobrar o tamanho da instância — gerando capacidade ociosa e desperdício de dinheiro.

## Key Claims

1. **Horizontal é adicionar servidores sem indisponibilidade** — os servidores existentes continuam operando normalmente enquanto novos são adicionados, do mesmo tamanho ou não.
2. **Vertical online existe mas é arriscado** — hypervisors já suportam aumento de CPU/memória online há tempos, mas redução é rara ("ninguém tem coragem") e o caso comum ainda envolve indisponibilidade (refresh da aplicação, reboot, stop/start), dependendo do hypervisor ou cloud provider.
3. **Horizontal permite granularidade fina de capacidade** — no exemplo gráfico, um pico de consumo é resolvido adicionando apenas um servidor extra, sem dobrar nada.
4. **Vertical em cloud providers costuma forçar dobrar o tamanho da instância** — não é possível adicionar um número "quebrado" de CPU/memória; o próximo tier geralmente é o dobro do anterior. Isso gera desperdício visível quando a aplicação é um monolito centralizado não modularizado, obrigado a subir inteiro mesmo que só precisasse de um pouco mais de capacidade.
5. **Servidores menores e mais numerosos aumentam resiliência** — mais réplicas menores significam menos impacto por ponto único de falha; se uma cai, as outras continuam operando.
6. **Vertical primeiro, horizontal quando necessário — mas arquiteturas legadas podem não comportar horizontal** — reforça a ordem consolidada na wiki, com a ressalva de que sistemas legados às vezes não têm alternativa a vertical.

## Entidades Mencionadas

- Hypervisor (genérico, sem produto nomeado)
- Cloud Provider (genérico, sem nomear AWS/GCP/Azure)

## Conceitos Tocados

- [[escalabilidade-horizontal]]
- [[escalabilidade-vertical]]
- [[finops]]
- [[robustez-de-sistemas]]

## Open Questions

- A fonte não nomeia o cloud provider nem o hypervisor específico — a afirmação de "geralmente é o dobro do anterior" para tiers de instância é uma generalização não verificada contra uma tabela de preços real (ex.: AWS EC2 nem sempre dobra exatamente, existem tiers intermediários em algumas famílias).
- Não há tratamento de banco de dados ou camada de dados nesta fonte — ela fica restrita à camada de compute genérica.

## Raw Quotes

> "Eu tive a capacidade de aumentar aqui, ó, só um servidor. Eu não precisei dobrar o tamanho de um meu servidor."

> "Olha o desperdício que eu tenho aqui. Essa quantidade de memória eu não precisava dela [...] Isso aqui é um fogo, eu tô torrando meu dinheiro de fato."

> "Quanto mais servidores, quer dizer que se um deu problema e tudo mais, os outros continuam operando."
