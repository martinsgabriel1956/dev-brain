---
type: concept
title: "Memória Compartilhada Distribuída"
aliases: ["distributed shared memory", "DSM"]
date_created: 2026-08-21
date_updated: 2026-08-21
source_count: 1
tags: [sistemas-distribuidos, coordenacao, memoria-associativa]
skill: tech-mentor-backend
status: stub
---

# Memória Compartilhada Distribuída

Abstração que dá a processos rodando em máquinas diferentes a ilusão de acessar um espaço de memória único e compartilhado, mesmo sem memória física compartilhada. O [[wiki/concepts/tuple-space|tuple space]] é uma forma específica de memória compartilhada distribuída baseada em **memória associativa**: em vez de endereços, o acesso é por casamento de padrão sobre o conteúdo das tuplas.

## Key sources

- [[wiki/sources/tuple-space-wikipedia]] — tuple space classificado explicitamente como "uma forma de memória compartilhada distribuída"
