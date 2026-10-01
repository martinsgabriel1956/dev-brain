---
type: concept
title: "Architecture Sinkhole"
aliases: ["architecture sinkhole anti-pattern", "antipadrão sinkhole", "camadas pass-through"]
date_created: 2026-10-01
date_updated: 2026-10-01
source_count: 1
tags: [antipadrao, arquitetura-em-camadas, camadas-fechadas, vertical-slice]
skill: tech-mentor-backend
status: stub
---

# Architecture Sinkhole

## TL;DR

Antipadrão do [[wiki/concepts/arquitetura-em-3-camadas|padrão em camadas]]: o request atravessa camadas fechadas (controller → service → repository) **sem que nenhuma adicione lógica** — cada camada apenas repassa, "porque é preciso seguir o padrão". Resultado: arquivos, pastas e indireção sem valor, e mudanças mínimas que tocam muitos arquivos. [[wiki/sources/vertical-slice-organizar-codigo-por-funcionalidade-bernardo-lobato]] usa o antipadrão como motivação para o [[wiki/concepts/vertical-slice-architecture]].

## Notas

- O vídeo grafa "architecture syncle" (erro de legenda); o nome corrente é *Architecture Sinkhole*.
- [external, não verificado nesta ingestão] O termo é atribuído a Mark Richards (*Software Architecture Patterns*, O'Reilly), com a heurística 80/20 de requests pass-through; a página da O'Reilly retornou 403 e não foi confirmada. Tratar a atribuição como memória do modelo, não como fato citado.
- Alívio clássico das camadas fechadas: abrir camadas — mas isso troca o problema por mais acoplamento; a alternativa do vídeo é mudar o eixo de corte (por funcionalidade).

## Key sources

- [[wiki/sources/vertical-slice-organizar-codigo-por-funcionalidade-bernardo-lobato]] — nomeia o antipadrão como problema que o Vertical Slice resolve
