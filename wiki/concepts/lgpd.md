---
type: concept
title: "Lgpd"
aliases: []
date_created: 2026-09-22
date_updated: 2026-11-24
source_count: 7
tags: [lgpd]
skill: tech-mentor-security
status: stub
---

# Lgpd

Stub criado durante sweep de lint (links quebrados) a partir de referências em 2 página(s) da wiki — conteúdo completo pendente de ingest dedicado.

## Contexto das citações

- Em [[wiki/sources/data-privacy]]: [[wiki/concepts/lgpd]]
- Em [[wiki/sources/lgpd-gdpr]]: [[wiki/concepts/lgpd]]

## Pendências

Página não nasceu de um ingest próprio; TL;DR acima é reconstruído apenas a partir do texto das páginas que a citam. Precisa de fonte dedicada para virar `draft`/`stable`.

## Como requisito não funcional

Na [[wiki/sources/frontpush-dashboards-principios-parte-2|aula 05 do módulo de dashboards]], "respeitar a lei geral de proteção de dados" aparece entre os requisitos não funcionais de um dashboard, que [[wiki/entities/nasser|Násser]] chama de "perfumaria". A LGPD é obrigação legal, e ainda cria tensão com o CRUD: direito à eliminação dos dados × guarda fiscal de vendas.

## Minimização no levantamento

Na [[wiki/sources/frontpush-dashboards-levantamento-de-requisitos-dashclass|aula 06 do módulo de dashboards]]: "data de aniversário? Talvez, não sei [...] dar parabéns". É o caso do princípio da necessidade (art. 6º, III): coletar só o mínimo para a finalidade. O CPF se justifica pela nota fiscal, mas pode ser pedido só na compra.

## Key sources

- [[wiki/sources/data-privacy]]
- [[wiki/sources/lgpd-gdpr]]
- [[wiki/sources/openrouter-como-profissional-provedores-quantizacao-retencao-fallback-ronald-hulk]] — retenção de dados do provedor de LLM como ponto de conformidade; ZDR e `data_collection: deny`
- [[wiki/sources/arquitetura-orientada-a-eventos-luiz-gago-faria-otavio-santana-eduardo-macris]] — evento enxuto (só ID) evita expor dado pessoal; dado completo passa por API com gestão de quem consome ([[wiki/concepts/evento-enxuto-vs-evento-gordo]])
- [[wiki/sources/frontpush-dashboards-principios-parte-2]]: FrontPUSH, dashboards aula 05: LGPD como requisito não funcional
- [[wiki/sources/frontpush-dashboards-levantamento-de-requisitos-dashclass]]: FrontPUSH, dashboards aula 06: data de aniversário e CPF

## Key sources (adição 2026-10-14)

- [[wiki/sources/como-sair-do-ciclo-de-bugs-e-retrabalho-andre-casciotti]] — restrição de acesso ao banco de produção por compliance/LGPD não impede evidenciar um bug; simular em outro ambiente ([[wiki/concepts/evidenciar-o-problema]])
