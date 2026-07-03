---
type: concept
title: "Tríade CIA"
aliases: ["CIA Triad", "Confidencialidade Integridade Disponibilidade", "Confidentiality Integrity Availability"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 1
tags: [triade-cia, confidencialidade, integridade, disponibilidade, security, iso-27001]
skill: tech-mentor-security
status: draft
---

## Definição

Os três pilares fundamentais que qualquer sistema de segurança da informação precisa garantir — o objetivo final em torno do qual toda a estrutura da [[wiki/concepts/iso-27001]] e do [[wiki/concepts/sgsi-isms]] é construída. **Não** se refere à agência de inteligência americana — é o acrônimo *Confidentiality, Integrity, Availability*.

## Os três pilares

- **Confidencialidade** — "só entra quem pode". Ex.: um funcionário sem credencial, chave SSH ou token JWT válido recebe *access denied* ao tentar ler a tabela de salários.
- **Integridade** — o dado gravado é o mesmo que será lido. Nenhum update malicioso no banco, nenhum *man-in-the-middle* alterando o payload em trânsito. Mecanismos: hashes, assinaturas digitais, commits Git assinados.
- **Disponibilidade** — o sistema está ativo e resiliente a picos de acesso. Envolve redundância, backup testado (restore, não só backup) e proteção contra DDoS. Um sistema seguro que ninguém consegue acessar é inútil.

## Por que importa

É o critério que justifica cada controle do Anexo A da ISO 27001: todo controle existe para proteger um (ou mais) desses três pilares. Ao avaliar um novo controle de segurança, a pergunta é "qual dos três pilares da tríade ele protege, e contra qual ameaça?".

## Key Sources

- [[wiki/sources/iso-27001-dicionario-programador]] — definição dos três pilares com exemplos técnicos (JWT, hashes, commits assinados, redundância)

## Conceitos Relacionados

[[wiki/concepts/iso-27001]] · [[wiki/concepts/sgsi-isms]] · [[wiki/concepts/audit-log]] · [[wiki/concepts/principio-menor-privilegio]]
