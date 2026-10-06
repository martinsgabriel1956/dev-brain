---
type: concept
title: "Reprodutibilidade de Bugs"
aliases: ["bug não reproduzível", "reproduzir bug em produção"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [debugging, reprodutibilidade, estado-externo, logs]
skill: tech-mentor-backend
status: draft
---

# Reprodutibilidade de Bugs

Propriedade de conseguir reproduzir localmente um erro de produção. Cai quando a função depende de estado que os logs não mostram ([[wiki/concepts/dependencia-externa-oculta]]).

## Cenário do vídeo

`calculatePrice(30)` falha em produção; os logs mostram só o parâmetro 30; localmente não falha. A causa: só falha para usuário *retail* com produto de estoque zero — dados vindos do banco, não do parâmetro. Mesmo sintoma com estado global mutado por outra requisição ([[wiki/concepts/estado-global-em-servidor]]).

## Como melhorar

Entradas explícitas (parâmetros/[[wiki/concepts/request-context]]) para que o log contenha o necessário; funções puras onde possível. **Inferência minha:** logar o estado externo lido (usuário, estoque) junto da chamada; ver [[wiki/concepts/observabilidade]].

## Key sources

- [[wiki/sources/estado-global-stateless-side-effects-reprodutibilidade-galego]]
