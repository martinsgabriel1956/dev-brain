---
type: source
title: "Todos os principais tipos de armazenamento de dados (em menos de 8 minutos)"
aliases: ["tipos de armazenamento", "storage media", "HD SSD nuvem NAS fita", "meios de armazenamento"]
date_created: 2026-08-13
date_updated: 2026-08-13
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/tipos-de-armazenamento-de-dados.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-08-13
source_count: 1
tags: [storage, hardware, hdd, ssd, nand, flash, nuvem, nas, fita-magnetica, lto, armazenamento-optico, cs-fundamentals]
skill: tech-mentor-data
status: stable
---

## TL;DR

Panorama dos principais meios de armazenamento de dados e o trade-off de cada um. A tese central: **não existe "melhor" absoluto — cada mídia otimiza um eixo diferente** (velocidade, custo/GB, durabilidade, portabilidade, isolamento de rede). Por isso empresas bilionárias ainda usam **fita magnética (LTO)** para backup de longo prazo: é barata, dura 30+ anos e, por ficar offline, é o meio mais seguro contra invasão — vantagens que nenhum SSD de última geração entrega. Cobre HD, SSD (SATA/NVMe), nuvem, NAS, óptico (CD/DVD/Blu-ray), pen drive, cartão de memória, disquete e fita.

## Key Claims

**Claim:** Não há mídia universalmente "melhor" — a escolha depende do eixo que você precisa otimizar.
**Evidence:** SSD ganha em velocidade e resistência a choque; HD ganha em custo/GB para capacidade grande; fita ganha em custo/GB de arquivamento, durabilidade (30+ anos) e segurança (offline); nuvem ganha em disponibilidade e geo-redundância. A fita, tecnologia "ultrapassada", segue em uso por IBM, governos e data centers exatamente por esses eixos.
**Confidence:** alta

**Claim:** HD (disco magnético giratório) troca velocidade por custo e capacidade.
**Evidence:** Braço atuador + cabeça de leitura/gravação sobre pratos revestidos de material magnético. 5400/7200 RPM ≈ 100–160 MB/s; modelos de alto desempenho a 10.000+ RPM. Capacidades de 500 GB a 2 TB+. Vida útil 3–5 anos; partes mecânicas o tornam vulnerável a choque, superaquecimento e queda de energia.
**Confidence:** alta

**Claim:** SSD é mais rápido, mais durável e mais resistente que HD porque não tem partes móveis.
**Evidence:** Armazena em células de memória NAND (flash), acesso eletrônico. Sem discos giratórios nem braços → resiste a choque/vibração e dura ~5–10 anos. SATA até ~600 MB/s; NVMe atinge vários GB/s. Atenção aos form factors NVMe — verificar compatibilidade física antes de comprar.
**Confidence:** alta

**Claim:** Nuvem e NAS são a mesma ideia (acesso a dados pela rede) com donos diferentes do hardware.
**Evidence:** Nuvem (Google Drive, Dropbox, iCloud) = servidores de terceiros, dados criptografados e duplicados em vários data centers → geo-redundância; paga-se assinatura por espaço. NAS = você monta o servidor, instala HDs e conecta à rede local; sem assinatura, mas exige manutenção e um nobreak (ligado 24/7, queda de energia corrompe dados/HDs).
**Confidence:** alta

**Claim:** Óptico (CD/DVD/Blu-ray) caiu em desuso, substituído por download digital e streaming.
**Evidence:** Laser lê pits microscópicos pela reflexão da luz. CD 700 MB, DVD 4,7/8,5 GB, Blu-ray 25/50 GB. Fragilidade: um risco pode tornar os dados ilegíveis.
**Confidence:** alta

**Claim:** Pen drive e cartão de memória são a mesma tecnologia (flash) do SSD, em formato portátil.
**Evidence:** Pen drive via USB — velocidade limitada pela versão: USB 2.0 até 480 Mb/s, USB 3.0 até 5 Gb/s, USB 3.1 até 10 Gb/s. Cartões (SD/miniSD/microSD) têm "classe de velocidade" que define leitura/gravação. Capacidades de MB (antigos) a TB (modernos).
**Confidence:** alta

**Claim:** Fita magnética é armazenamento **sequencial** — lenta para acesso aleatório, ideal para grande volume de arquivamento.
**Evidence:** Dados lidos na ordem de gravação. Barata, durável (30+ anos), alta capacidade (cartuchos LTO com vários TB) e segura por ficar offline. Trade-off aceito porque backup de longo prazo raramente precisa de acesso aleatório rápido.
**Confidence:** alta

## Ponte para a prática (arquitetura de dados)

O vídeo é hardware, mas o princípio é o mesmo do **[[wiki/concepts/storage-tiering]]** (Hot/Warm/Cold): SSD/NVMe = *hot* (acesso frequente, caro, rápido); HDD/Object Storage = *warm*; fita/S3 Glacier = *cold* (raro, barato, retrieval em minutos/horas). A fita é o equivalente físico do Glacier. `[skill: tech-mentor-data — data-architecture.md § Storage Tiering]`

## Entidades

- [[wiki/entities/ibm]] — citada como usuária de fita magnética para backup de longo prazo (linhagem LTO)
- [[wiki/entities/google]] — Google Drive como exemplo de nuvem
- Dropbox, iCloud (Apple), Microsoft — exemplos de nuvem (sem página dedicada)

## Conceitos

- [[wiki/concepts/hd-disco-rigido]]
- [[wiki/concepts/ssd]]
- [[wiki/concepts/memoria-flash]]
- [[wiki/concepts/fita-magnetica]]
- [[wiki/concepts/nas-network-attached-storage]]
- [[wiki/concepts/armazenamento-optico]]
- [[wiki/concepts/storage-tiering]]
- [[wiki/concepts/sistema-de-arquivos]] — camada de abstração que roda **sobre** qualquer uma dessas mídias

## Open questions

- **Unidade de velocidade:** o áudio mistura MB/s (HD, SSD, USB 2.0) com Gb/s (USB 3.x). Padrão da indústria: interfaces USB são especificadas em **gigabits** por segundo (USB 3.0 = 5 Gb/s ≈ 625 MB/s teóricos). Mantido como no original, mas vale a distinção bit vs. byte.
- **"NAS é armazenamento em nuvem":** simplificação do vídeo. NAS é rede local (LAN); só vira "nuvem privada" com acesso remoto configurado. Registrado como impreciso, não errado.

## Citações

> "Existem empresas bilionárias que ainda armazenam seus dados em fitas magnéticas — e que, dependendo do caso, esse tipo de armazenamento pode ser melhor que SSDs de última geração."

> "É o meio mais seguro, pois não está conectado à rede o tempo todo e é menos vulnerável a invasões." (sobre a fita)
