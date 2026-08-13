---
type: concept
title: "NAS (Network Attached Storage)"
aliases: ["NAS", "network attached storage", "nuvem privada", "servidor de arquivos local"]
date_created: 2026-08-13
date_updated: 2026-08-13
source_count: 1
tags: [storage, hardware, nas, rede, backup, cs-fundamentals]
skill: tech-mentor-data
status: stub
---

# NAS (Network Attached Storage)

Servidor de armazenamento que **você mesmo monta e gerencia**: instala [[concepts/hd-disco-rigido|HDs]] nos compartimentos e o conecta à rede local, permitindo que várias pessoas acessem os arquivos remotamente dentro da mesma rede.

## NAS vs. nuvem pública

Mesma ideia — acesso a dados pela rede — com donos diferentes do hardware:

| | NAS | Nuvem (Google Drive, Dropbox, iCloud) |
|---|---|---|
| Hardware | seu | de terceiros |
| Custo | sem assinatura | assinatura por espaço |
| Manutenção | sua (updates, config) | do provedor |
| Redundância | você configura (RAID) | geo-redundância entre data centers |

## Cuidados

Fica ligado **24/7** → queda de energia pode corromper dados ou danificar os HDs. **Nobreak recomendado.** Exige mais configuração e manutenção que a nuvem. Chamar NAS de "nuvem" é simplificação: é rede local (LAN); só vira nuvem privada com acesso remoto configurado.

## Key Sources

- [[wiki/sources/tipos-de-armazenamento-de-dados]] — NAS como "nuvem que você administra"
