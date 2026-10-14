---
type: concept
title: "Dependência de Caminho em Tecnologia (Path Dependence)"
aliases: ["path dependence", "herança histórica das linguagens"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [lang-systems, historia, path-dependence, arquitetura, c]
skill: lang-systems
status: draft
---

# Dependência de Caminho em Tecnologia

Nada surge do nada: muito do que se usa hoje (C, x86, [[wiki/concepts/abi]] de C) vem de decisões dos anos 60–70 e persiste porque muita coisa depende delas. Lição de [[wiki/sources/por-que-c-e-alto-nivel-abstracao-portabilidade-hardware]]: C venceu a "batalha das linguagens" no degrau logo acima do [[wiki/concepts/assembly]] por ter compiladores para quase toda arquitetura ([[wiki/concepts/portabilidade-de-codigo-entre-arquiteturas]]), **não por ser perfeito**; superá-lo é difícil de imaginar. Se vale mudar e quanto esforço (tempo, dinheiro, pessoas) justificaria é questão em aberto — o autor cita o risco de "unificar tudo" e depois surgir a GPU quebrando a unificação. Posição dele: não aceitar "está ruim, mas é assim"; gosta de [[wiki/entities/zig]], embora outros prefiram construir sobre C ou usar linguagens que [[wiki/concepts/transpilador|transpilam]] para C. Ver [[wiki/concepts/retrocompatibilidade-x86]] e [[wiki/concepts/comportamento-indefinido]].

## Key sources

- [[wiki/sources/por-que-c-e-alto-nivel-abstracao-portabilidade-hardware]]
