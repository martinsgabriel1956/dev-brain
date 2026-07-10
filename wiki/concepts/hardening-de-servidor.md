---
type: concept
title: "Hardening de Servidor"
aliases: ["server hardening", "hardening", "endurecimento de servidor"]
date_created: 2026-07-10
date_updated: 2026-07-10
source_count: 1
tags: [hardening, ssh, sshd, seguranca, defense-in-depth, presets]
skill: tech-mentor-security
status: stub
---

## Definição

Processo de reduzir a superfície de ataque de um servidor desativando funcionalidades desnecessárias e restringindo o que é permitido por padrão — aplicação prática de [[wiki/concepts/defense-in-depth]] e [[wiki/concepts/secure-by-default]] na configuração de um host, não só na arquitetura da aplicação.

## Exemplo: hardening de SSH

No contexto de [[wiki/concepts/ssh]], hardening tipicamente significa, no `sshd_config`:

- Desativar `PasswordAuthentication`, `PermitEmptyPasswords` e `PermitRootLogin`, deixando `PubkeyAuthentication` como único método aceito.
- Desativar `AllowTcpForwarding` a menos que SSH Tunnels sejam explicitamente necessários.

Uma fonte da wiki descreve uma ferramenta com **presets escalonados** — "paranoico" (fecha praticamente tudo, mantém só autenticação por chave), "equilibrado" (libera redirecionamento TCP e outras conveniências) e "básico" — ilustrando hardening como um espectro configurável, não um estado binário.

## Relação com outros conceitos

- [[wiki/concepts/ssh]] — exemplo concreto de superfície a ser endurecida.
- [[wiki/concepts/defense-in-depth]] — hardening é uma camada; não substitui as demais.
- [[wiki/concepts/secure-by-default]] — o objetivo do hardening é aproximar a configuração real do default mais seguro possível.
- [[wiki/concepts/attack-surface]] — hardening reduz diretamente a superfície exposta.

## Key Sources

- [[wiki/sources/ssh-chaves-como-funcionam]]
