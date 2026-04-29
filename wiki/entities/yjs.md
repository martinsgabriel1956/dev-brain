---
type: entity
title: "Y.js"
aliases: ["yjs", "y.js"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 1
tags: [crdt, colaboracao-tempo-real, offline-first, open-source]
skill: tech-mentor-system-design
status: stub
---

# Y.js

Biblioteca open-source de CRDT de sequência para edição colaborativa em tempo real. Padrão da indústria para texto e estruturas colaborativas.

**Características:**
- CRDT de sequência eficiente — resolve conflitos sem servidor de sequenciamento
- Suporte a offline-first — aplica mudanças localmente, sincroniza quando online
- Bindings para Monaco (VS Code), ProseMirror, CodeMirror, Quill
- Providers: WebSocket (y-websocket), WebRTC (y-webrtc), IndexedDB (persistência local)

**Usado por:** Linear, Liveblocks (como base), várias ferramentas colaborativas.

**Criado por:** Kevin Jahns.

## Key Sources

- [[sources/crdt-colaboracao-tempo-real]]
