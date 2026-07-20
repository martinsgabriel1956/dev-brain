---
type: concept
title: "Sistema Operacional Imutável"
aliases: ["immutable os", "so imutavel", "atomic os", "root read-only"]
date_created: 2026-07-20
date_updated: 2026-07-20
source_count: 1
tags: [immutable-os, nixos, fedora-silverblue, security, defense-in-depth, container]
skill: tech-mentor-security
status: stub
---

# Sistema Operacional Imutável

Sistema operacional em que a raiz do filesystem (`/`) é somente-leitura — um snapshot que nenhum processo, nem mesmo um rodando como root, consegue modificar diretamente. Exemplos: Fedora Silverblue/Atomic, NixOS. Contraste com um Linux tradicional, onde qualquer programa com privilégio de root pode escrever em qualquer parte do sistema.

## Mecanismo

- As ferramentas e ambientes de desenvolvimento rodam em containers isolados sobre essa base, em vez de instalados diretamente no sistema.
- O sistema base fica intocável durante o uso normal — mudanças acontecem via atualização de snapshot, não edição incremental do estado ao vivo.
- **Consequência de segurança:** se um processo malicioso (ou um agente de IA comprometido) escapar de uma camada de contenção como o [[wiki/concepts/agent-containment|AI Jail]] e tentar alterar o sistema, a mudança não persiste — no próximo reboot, o sistema volta ao estado original automaticamente.

## Papel na Defesa em Camadas

[[wiki/sources/ai-jail-sandbox-para-agentes-de-ia-akita]] posiciona o SO imutável como a terceira e mais radical camada de um modelo de três camadas (ver [[wiki/concepts/defense-in-depth]]):

1. Sessão — [[wiki/concepts/agent-containment]] (isola o processo em execução)
2. Código — Git com push manual (permite reverter dano ao repositório)
3. **Sistema operacional** — imutabilidade garante que dano ao SO em si não sobrevive a um reboot

Classificada pela fonte como o nível "hard paranoia" — não necessário para começar a se proteger (as camadas 1 e 2 já entregam a maior parte do ganho de segurança com muito menos fricção), mas relevante para quem quer a garantia mais forte possível.

## Relação com Outros Conceitos

- [[wiki/concepts/agent-containment]] — camada anterior/complementar; SO imutável é a rede de segurança para quando a contenção de processo falha.
- [[wiki/concepts/defense-in-depth]] — instância de camada de infraestrutura de mais alto custo/benefício mais radical.
- [[wiki/concepts/principio-do-menor-privilegio]] — mesmo root não tem privilégio de alterar a raiz do sistema permanentemente; o privilégio máximo do SO é, por design, limitado a mudanças transacionais/versionadas.

## Key Sources

- [[wiki/sources/ai-jail-sandbox-para-agentes-de-ia-akita]] — terceira camada do modelo de defesa em profundidade contra agentes de IA comprometidos
