---
type: concept
title: "Acoplamento entre Slices"
aliases: ["autoacoplamento entre slices", "slice chamando slice"]
date_created: 2026-10-01
date_updated: 2026-10-01
source_count: 1
tags: [vertical-slice, acoplamento, disciplina, integracao]
skill: tech-mentor-backend
status: stub
---

# Acoplamento entre Slices

## TL;DR

No [[wiki/concepts/vertical-slice-architecture]] é **permitido** uma slice chamar outra sem compartilhar código, tratando-a como cliente (um request). A "pegadinha" de [[wiki/sources/vertical-slice-organizar-codigo-por-funcionalidade-bernardo-lobato]]: sem cuidado, o código volta a ter [[wiki/concepts/acoplamento]] forte entre slices sem que ninguém perceba. Isso, somado à tentação de unificar modelos numa classe central ([[wiki/concepts/dominio-centralizado-vs-modelo-por-slice]]), é o principal risco do padrão.

## Mitigações citadas / inferidas

- Acompanhamento rigoroso de cada nova implementação (citado).
- Estar "sempre de olho nas integrações" entre slices (citado).
- [inferência] Medir dependências com [[wiki/concepts/metricas-de-acoplamento]]; preferir integração por contrato/evento ([[wiki/concepts/comunicacao-assincrona]]) a chamada direta de classe.

## Key sources

- [[wiki/sources/vertical-slice-organizar-codigo-por-funcionalidade-bernardo-lobato]]
