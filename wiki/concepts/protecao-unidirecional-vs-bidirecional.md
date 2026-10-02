---
type: concept
title: "Proteção Unidirecional vs Bidirecional"
aliases: ["bloqueio em um sentido", "isolamento bidirecional"]
date_created: 2026-10-02
date_updated: 2026-10-02
source_count: 1
tags: [networking, firewall, seguranca-de-rede, segmentacao]
skill: tech-mentor-networking
status: draft
---

# Proteção Unidirecional vs Bidirecional

**Unidirecional:** uma regra `drop` clientes→interna: o cliente acessa a internet e não a rede interna; a interna acessa a internet normalmente. **Bidirecional (3 redes):** clientes (10.0.0.x), funcionários (172.16.0.x), empresa (192.168.0.x), com ~5 regras (mostradas só em slide): nenhuma rede inicia conexão para as outras; [[wiki/concepts/client-isolation]] nos APs de clientes e funcionários, nunca na empresa. [external, skill `network-security.md`] Firewall *stateful* já permite retorno de conexões iniciadas de dentro; por isso um único `drop` de origem→destino não corta respostas legítimas — mas a **ordem das regras** importa e o vídeo não a trata. Ver [[wiki/concepts/segmentacao-de-rede-por-faixa-de-ip-e-firewall]], [[wiki/concepts/blast-radius]].

## Key sources

- [[wiki/sources/seguranca-rede-wifi-pequeno-comercio-mikrotik-isolamento-clientes]]
