---
type: source
title: "Mainframe as a Service: Casas Bahia, SulAmérica e o zCloud da Kyndryl"
aliases: ["maas casas bahia", "zcloud kyndryl", "ir para nuvem sem abandonar mainframe"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 0
tags: [mainframe, cloud, maas, kyndryl, zcloud, lpar, virtualizacao, multitenancy, capex-opex, modernizacao]
skill: tech-mentor-infra
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/mainframe-as-a-service-casas-bahia-sulamerica-kyndryl-zcloud.md
source_url:
author: desconhecido (vídeo em PT-BR; autor do livro "Introdução à Plataforma Mainframe")
date_published:
date_ingested: 2026-09-29
---

# Mainframe as a Service: Casas Bahia, SulAmérica e o zCloud da Kyndryl

## TL;DR

Vídeo que usa a migração das [[wiki/entities/casas-bahia]] (e, um ano antes, da [[wiki/entities/sulamerica]]) para o **zCloud** da [[wiki/entities/kyndryl]] para separar dois conceitos que costumam vir misturados: **onde** a aplicação executa e **como** a infraestrutura é **consumida**. As duas empresas adotaram [[wiki/concepts/mainframe-as-a-service]] — o [[wiki/concepts/mainframe]] continua (COBOL, DB2, CICS, JCL), mas passa a ser alugado como capacidade elástica e [[wiki/concepts/multi-tenancy|multitenant]] em vez de ser comprado e operado no data center próprio. O argumento: a [[wiki/concepts/virtualizacao]] e o compartilhamento de recursos nasceram no mainframe ([[wiki/concepts/lpar]]); logo, [[wiki/concepts/cloud-como-modelo-de-consumo]] não implica abandonar o mainframe. Ganhos: [[wiki/concepts/capex-vs-opex]] (capital imobilizado vira custo operacional), fim da [[wiki/concepts/dimensionamento-para-o-pico|capacidade ociosa do pico]] e equipe de especialistas compartilhada. Conclusão: [[wiki/concepts/modernizacao-de-mainframe]] e nuvem não são opostos — "a empresa foi para a nuvem e o mainframe foi junto".

## Key Claims

| Claim | Evidence | Confidence |
|---|---|---|
| Casas Bahia migrou o mainframe para o zCloud da Kyndryl; a SulAmérica fez o mesmo um ano antes (saúde, vida, previdência) | narração | Alta — [external] Kyndryl anunciou a SulAmérica em out/2023 (https://www.kyndryl.com/us/en/about-us/news/2023/10/zcloud-transformation-for-brazilian-insurance-agency) e a conclusão da migração das Casas Bahia (https://www.kyndryl.com/br/pt/services/core-enterprise-zcloud); data exata das Casas Bahia não verificada |
| "Nuvem" não implica x86/microsserviços/reescrita; empresas foram para um modelo de nuvem mantendo o mainframe | narração | Alta (definição); a generalização de mercado é do autor |
| Distinguir *onde executa* de *como a infra é consumida* é o eixo correto para entender modernização | argumento do autor | Alta (lógica); enquadramento do autor |
| Modelo tradicional força superdimensionar capacidade para o pico; o excedente fica ocioso ("dinheiro parado") | exemplo varejo (terça de agosto × Black Friday) | Alta (padrão bem conhecido) |
| Virtualização e compartilhamento/elasticidade de recursos nasceram no mainframe, não na AWS | narração | Alta [external] — VM/CP-67 da IBM, anos 1960 (https://en.wikipedia.org/wiki/Hardware_virtualization); não citado com fonte no vídeo |
| PR/SM cria partições lógicas (LPARs) que rodam SOs diferentes, isoladas e independentes na mesma máquina | narração | Alta [external] (https://en.wikipedia.org/wiki/Logical_partition) |
| Se há isolamento entre sistemas, o compartilhamento entre **empresas** diferentes é o passo natural → multitenância | dedução do autor | Média — inferência plausível; isolamento de LPAR não é suficiente sozinho para o multitenant (rede, storage, operação) |
| MaaS = contratar LPARs de mainframe do provedor; cliente não sabe em qual máquina física roda; compra capacidade, não hardware | narração | Alta [external] — zCloud descrito como MaaS multitenant (https://www.kyndryl.com/us/en/services/mainframe/managed-infrastructure/zcloud) |
| Capital imobilizado (CAPEX) vira custo operacional (OPEX) | narração + gráfico hipotético de MIPS | Alta (conceito); magnitude da economia **não** quantificada |
| O provedor assume e compartilha especialistas (CICS, DB2, z/OS, storage, performance) — para algumas empresas isso vale mais que a economia de infra | narração | Média — opinião do autor, sem dado |
| Sistemas corporativos evoluem por integração heterogênea (mainframe ↔ SaaS ↔ microsserviços em nuvem híbrida ↔ J2EE), não por substituição | narração | Média-alta — coerente com [[wiki/concepts/modernizacao-de-mainframe]] |

## Entidades

- [[wiki/entities/kyndryl]] (zCloud; confirma a leitura de "Kindrew") · [[wiki/entities/casas-bahia]] (novo) · [[wiki/entities/sulamerica]] (novo) · [[wiki/entities/ibm]] (origem de PR/SM/LPAR — inferência do contexto) · [[wiki/entities/aws]] · [[wiki/entities/microsoft]] (Azure) · [[wiki/entities/google]] (Google Cloud)

## Conceitos

- [[wiki/concepts/mainframe-as-a-service]] (novo) · [[wiki/concepts/lpar]] (novo) · [[wiki/concepts/virtualizacao]] (novo) · [[wiki/concepts/cloud-como-modelo-de-consumo]] (novo) · [[wiki/concepts/capex-vs-opex]] (novo) · [[wiki/concepts/dimensionamento-para-o-pico]] (novo)
- Tocados: [[wiki/concepts/mainframe]], [[wiki/concepts/modernizacao-de-mainframe]], [[wiki/concepts/cobol]], [[wiki/concepts/multi-tenancy]], [[wiki/concepts/finops]], [[wiki/concepts/vendor-lock-in-cloud]], [[wiki/concepts/planejamento-de-capacidade]], [[wiki/concepts/arquitetura-complexa]], [[wiki/concepts/mercado-de-trabalho-mainframe-cobol]]

## Open Questions

- **Sem números:** o vídeo não quantifica a economia do MaaS; o gráfico de MIPS é explicitamente hipotético. Não dá para concluir que MaaS sai mais barato que mainframe próprio.
- **Lock-in:** trocar mainframe próprio por MaaS de um provedor troca dependência de hardware por dependência de contrato/provedor — o vídeo não discute. Ver [[wiki/concepts/vendor-lock-in-cloud]] (análogo, não idêntico).
- **Isolamento:** LPAR isola partições, mas o vídeo trata isolamento e multitenância como quase equivalentes; requisitos regulatórios (dados de saúde/seguros) não são discutidos.
- **Elasticidade real:** o vídeo fala em "capacidade elástica" no MaaS; os limites práticos (contrato de capacidade mínima, tempo para ampliar LPAR) não são descritos.
- Data e escopo exatos da migração das Casas Bahia e nome do autor/canal não constam na fonte.

## Trechos

> "As empresas foram para um modelo de nuvem sem que isso significasse necessariamente abandonar o mainframe."

> "Capacidade subutilizada é dinheiro parado."

> "Quando a gente escuta falar que a empresa migrou pra nuvem, não necessariamente o mainframe foi desligado."
