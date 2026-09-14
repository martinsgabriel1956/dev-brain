---
type: concept
title: "Engenharia Reversa"
aliases: ["reverse engineering", "disassembly", "decompilação"]
date_created: 2026-08-27
date_updated: 2026-09-14
source_count: 2
tags: [cs-fundamentals, lang-systems, seguranca, baixo-nivel, ia]
skill: lang-systems
status: stub
---

# Engenharia Reversa

Processo de analisar um binário compilado — tipicamente partindo de **assembly** — para reconstruir a lógica original em uma linguagem de mais alto nível como C, entendendo o comportamento de um programa sem acesso ao seu código-fonte. Citada em [[wiki/sources/guia-programacao-baixo-nivel-c-arquitetura-so-embarcados]] como uma das áreas de aplicação de [[wiki/concepts/linguagem-c|programação de baixo nível]], junto de segurança ofensiva/defensiva, ainda que o vídeo não a aprofunda além de mencioná-la.

## Aplicada a LLMs: Extração de Dados Via Agente

[[wiki/sources/ia-nao-vai-substituir-desenvolvedor-2026-governanca-seguranca]] usa o mesmo termo num contexto diferente do binário/assembly acima: engenharia reversa do **comportamento de um agente de IA**, não de um programa compilado. Com poucas interações bem desenhadas (5-6, segundo a fonte), um atacante consegue reconstruir e extrair dados/regras de negócio que a empresa expôs ao agente, sem precisar de acesso a código-fonte nem a um binário — o "programa" sendo reconstruído é o comportamento do sistema de prompt/contexto por trás do agente. Ver [[wiki/concepts/ataque-de-destilacao-e-extracao-de-dados-llm]] para a distinção com ataques de destilação em escala.

## Key sources

- [[wiki/sources/ia-nao-vai-substituir-desenvolvedor-2026-governanca-seguranca]] — engenharia reversa de comportamento de agente de IA para extração de dados corporativos expostos, com poucas interações
- [[wiki/sources/guia-programacao-baixo-nivel-c-arquitetura-so-embarcados]]
