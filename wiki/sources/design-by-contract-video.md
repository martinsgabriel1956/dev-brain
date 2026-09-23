---
type: source
title: "Design by Contract (vídeo)"
aliases: ["design by contract video", "projeto por contrato"]
date_created: 2026-09-23
date_updated: 2026-09-23
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/design-by-contract-video.md
source_url: ""
author: "não identificado (canal com nome corrompido na transcrição)"
date_published: ""
date_ingested: 2026-09-23
source_count: 0
tags: [design-by-contract, bertrand-meyer, eiffel, pre-condicao, pos-condicao, invariante, oop, testes, property-based-testing]
skill: tech-mentor-backend
status: draft
---

# Design by Contract (vídeo)

## TL;DR

Vídeo curto que apresenta **Design by Contract (DbC)**: tratar a interação entre módulos de software como um contrato com direitos e responsabilidades. Criado por [[wiki/entities/bertrand-meyer]] na linguagem [[wiki/entities/eiffel]], o contrato tem três partes — pré-condições, pós-condições e invariantes ([[wiki/concepts/precondicao-poscondicao-invariante]]). Programa "correto" = faz exatamente o que o contrato diz, nem mais nem menos. Mesmo sem suporte nativo da linguagem, vale documentar o contrato em comentários. O autor distingue DbC de contratos de API (OpenAPI) e sinaliza [[wiki/concepts/property-based-testing]] como técnica relacionada.

## Key Claims

- **DbC foca em documentar e aceitar direitos e responsabilidades de módulos, aumentando a confiança na corretude.** Evidência: definição do autor; "correto" = nem mais nem menos que o acordado. → [[wiki/concepts/design-by-contract]]
- **Contrato = pré-condições + pós-condições + invariantes.** Pré: responsabilidade do **chamador**; pós: garantia da **rotina**, o que implica que ela sempre termina (sem laços infinitos); invariantes podem ser quebradas durante a execução, mas valem de novo ao final. → [[wiki/concepts/precondicao-poscondicao-invariante]]
- **Violação do contrato invoca um "remédio" acordado entre as partes** (no exemplo, lançar exceção). → [[wiki/concepts/excecao-vs-erro]]
- **Suporte varia por linguagem:** Clojure tem pré/pós-condições nativas (`:pre`/`:post`, asserções que lançam exceção); as demais podem imitar com condicionais. → [[wiki/entities/clojure]]
- **Contrato sem automação ainda vale:** documentar pré/pós/invariantes em comentário antes do método já ajuda quem consome.
- **Contrato de DbC ≠ contrato de API (OpenAPI/HTTP):** o segundo descreve a interface; segundo o autor (com ressalva "até onde pude ver"), não expressa pré/pós-condições. → [[wiki/concepts/contract-testing]]
- **Meyer é o autor do Open/Closed Principle** (o "O" do SOLID). → [[wiki/concepts/open-closed-principle]]

## Entities

[[wiki/entities/bertrand-meyer]] · [[wiki/entities/eiffel]] · [[wiki/entities/clojure]]

## Concepts

[[wiki/concepts/design-by-contract]] · [[wiki/concepts/precondicao-poscondicao-invariante]] · [[wiki/concepts/open-closed-principle]] · [[wiki/concepts/property-based-testing]] · [[wiki/concepts/contract-testing]] · [[wiki/concepts/fail-fast]] · [[wiki/concepts/encapsulamento]] · [[wiki/concepts/tdd]] · [[wiki/concepts/excecao-vs-erro]]

## Open Questions

- Transcrição automática muito corrompida no trecho biográfico de Meyer (ETH Zurich? UC Santa Barbara? Milão?) — leitura é inferência, **não** verificada. Ver notas no arquivo raw.
- O exemplo de "cláusulas condicionais" (limites de 10 mil / 100 mil) mistura regra de negócio com validação de contrato: é fluxo alternativo, não pré-condição no sentido estrito. A fonte não faz essa distinção.
- A afirmação de que contratos OpenAPI não têm pré/pós-condições é feita com ressalva pelo autor; não foi verificada aqui.
- Autor/canal e data de publicação desconhecidos.

## Raw Quotes

> "Um programa correto no design by contract é um programa que não faz nada a mais nem a menos do que aquilo que foi concordado no contrato."

> "É responsabilidade da rotina chamadora passar bons dados para a rotina que está sendo chamada."
