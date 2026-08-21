---
type: concept
title: "POSIX"
aliases: ["Portable Operating System Interface"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 1
tags: [posix, unix, portabilidade, padrao, historia-da-computacao]
skill: tech-mentor-backend
status: stub
---

# POSIX

Portable Operating System Interface — padrão criado no fim dos anos 80 para unificar as chamadas de sistema entre diferentes versões/distribuições do [[wiki/concepts/unix]]. Antes do POSIX, cada sabor de Unix tinha suas próprias variações de chamada de sistema, dificultando portar código entre eles.

## Por que importa

Um programa escrito em C para Unix, seguindo o padrão POSIX, podia ser levado para outro Unix sem precisar reescrever a parte de interação com o sistema operacional — o mesmo problema que a [[wiki/concepts/windows-api]] resolvia no ecossistema Windows, só que do lado Unix/portabilidade entre fabricantes em vez do lado de um único fornecedor.

## Key Sources

- [[wiki/sources/historia-e-evolucao-das-apis-bernardo-lobato]] — POSIX como padrão de portabilidade entre Unix, fim dos anos 80
