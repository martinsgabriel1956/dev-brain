---
type: concept
title: "Domínio (nome + TLD)"
aliases: ["domínio", "domain", "TLD", "top level domain", "nome de domínio"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_count: 1
tags: [rede, dominio, dns, tld, web]
skill: tech-mentor-networking
status: stub
---

# Domínio (nome + TLD)

**Nome legível pelos humanos para o endereço de um servidor na internet.** Existe para não precisarmos decorar um [[wiki/concepts/endereco-ip|endereço IP]] (ex.: `192.178.255.212`); digitamos `fernandakipper.com`. É, na prática, o que o [[wiki/concepts/dns|DNS]] **traduz** de volta para IP.

## Anatomia: nome personalizado + TLD

```
fernandakipper . com
└─ nome        └─ TLD (Top Level Domain / extensão)
   personalizado
```

O ponto separa as duas partes. Consequência importante: **mesmo nome + TLD diferente = domínio diferente**, podendo ter donos diferentes.

- `fernandakipper.com` ≠ `fernandakipper.com.br` — domínios distintos.
- Ao registrar, `fernandakipper.com` pode estar indisponível ("already taken") enquanto `.net`, `.info`, `.xyz` estão livres.
- TLDs mais populares: `.com` e `.com.br`; `.org` é muito usado por órgãos governamentais/regulamentados.

Domínios são comprados em **registradores** (ex.: [[wiki/entities/godaddy]], [[wiki/entities/hostinger]]), onde também se configuram os **name servers** que decidem para qual DNS o domínio aponta.

## Key sources
- [[wiki/sources/enderecos-ip-dns-dominios-https-aws-fernanda-kipper]] — domínio como tradução de IP; composição nome + TLD; TLD diferente = domínio diferente
