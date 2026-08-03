---
type: source
title: "Large Scale Architecture vs. Complex Architecture"
aliases: ["large scale vs complex", "arquitetura de larga escala vs complexa"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 0
tags: [system-design, arquitetura, escalabilidade, complexidade, over-engineering, legado, sharding, control-plane]
skill: tech-mentor-system-design
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/large-scale-vs-complex-architecture.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-08-03
---

# Large Scale Architecture vs. Complex Architecture

## TL;DR

Aula que separa dois eixos independentes de uma arquitetura: **large scale** (capacidade de atender volume/TPS alto via divisão — sharding, camadas de compute/storage, control plane) e **complexidade** (interdependência, poliglotismo, regras de negócio acopladas ao passado). Uma arquitetura pode ser as duas coisas, uma delas, ou nenhuma. Complexidade é mais comum em enterprises antigas (legado tipo mainframe → AS/400 → Linux/Windows convivendo) do que em startups recentes. O autor recusa dar um checklist objetivo para classificar "complexidade" — trata como julgamento relativo — e admite abertamente não ter resposta, terminando a aula com uma pergunta aberta para a audiência.

## Key Claims

**Claim:** Large scale e complexidade são dimensões independentes de uma arquitetura — uma não implica a outra.
**Evidence:** O autor afirma explicitamente que large scale "não necessariamente é complexa" e que complexidade "acontece em todos os tipos de arquitetura... com large scale ou não". Uma arquitetura pode ter sharding implementado a nível de código sem ser poliglota/interdependente como uma arquitetura complexa "de fato".
**Confidence:** média — é uma distinção conceitual pessoal do autor, apresentada como definição de dicionário adaptada ("escalar" como verbo), não uma taxonomia de mercado com fonte citada.

**Claim:** Complexidade é mais frequente em ambientes enterprise legados por precisarem "conviver com o passado" (refatoração gradual em vez de substituição).
**Evidence:** Exemplo dado: empresa que migrou de mainframe para AS/400, depois Linux, depois Windows, sem nunca desligar completamente as camadas anteriores — gerando comunicação heterogênea (SOAP, REST, batch, mensageria) entre workloads remanescentes em cada plataforma.
**Confidence:** alta como observação qualitativa de consultoria; os números específicos de workloads por plataforma citados no vídeo são anedóticos e ficaram marcados como incertos no `raw/`.

**Claim:** Large scale se apoia no princípio de "dividir para conquistar", exigido por picos de tráfego e a necessidade de alta disponibilidade.
**Evidence:** Exemplo de sharding (mover usuário de shard A para shard B) como técnica central de divisão; menção a diferentes tecnologias de storage (S3, CDN, Redis/Memcached) coexistindo por necessidade de escala, não por legado.
**Confidence:** alta — consistente com [[wiki/concepts/sharding]] e [[wiki/concepts/db-sharding]] já documentados na wiki.

**Claim:** Arquiteturas large scale precisam de um "control plane" — camada de controladores separada do software que atende o negócio — para operações como mover dados entre shards.
**Evidence:** Exemplo dado é justamente a movimentação de um usuário entre shards, que exige lógica de coordenação própria, distinta da aplicação que serve o usuário final.
**Confidence:** alta — alinhado à definição já presente em [[wiki/concepts/control-plane]] (ainda que aquela página seja focada em Kubernetes/databases, não em sharding de aplicação).

**Claim:** Over-engineering e "over thinking" são os dois anti-padrões simétricos que geram desperdício — o primeiro por excesso de ferramental/tecnologia (comum em large scale), o segundo por excesso de pensamento/regras não simplificadas (comum em arquitetura complexa).
**Evidence:** Autor associa over-engineering explicitamente ao contexto de large scale ("as vezes até pensa: eu preciso de tanto, tanto, tanto... faz over engineering") e over thinking ao contexto de complexidade de regra de negócio ("as vezes também tem um over que não simplifica as coisas").
**Confidence:** média — é uma distinção terminológica que o autor não deriva de literatura, mas que é coerente com o conceito já estabelecido de [[wiki/concepts/over-engineering]].

**Claim:** Não existe um checklist objetivo ou métrica confiável para classificar uma arquitetura como "complexa" — é relativo ao observador.
**Evidence:** O próprio autor declara não classificar arquiteturas dessa forma e explicitamente recusa a ideia de um checklist com pontuação, argumentando que os patterns ajudam "dos dois jeitos" independente da classificação.
**Confidence:** alta quanto à posição do autor (é uma opinião declarada, não um fato a verificar); pergunta deixada aberta para a audiência, sem resolução no material.

## Concepts & Entities Touched

[[wiki/concepts/over-engineering]] · [[wiki/concepts/accidental-complexity]] · [[wiki/concepts/essential-complexity]] · [[wiki/concepts/control-plane]] · [[wiki/concepts/sharding]] · [[wiki/concepts/db-sharding]] · [[wiki/concepts/alta-disponibilidade]] · [[wiki/concepts/refactor-vs-rewrite-matrix]] · [[wiki/concepts/codigo-legado-ia]] · [[wiki/concepts/large-scale-architecture]] · [[wiki/concepts/arquitetura-complexa]]

## Open Questions

- Não há métrica objetiva proposta para "quão complexa" é uma arquitetura — permanece um julgamento qualitativo, tanto na fonte quanto na wiki até agora.
- O vídeo não detalha os patterns específicos prometidos ("vamos ver isso quando falar dos patterns") — provavelmente aula seguinte da mesma série; próximas fontes dessa série devem preencher a lacuna.
- Os números exatos de workloads por plataforma no exemplo de legado (mainframe/AS-400/Linux/Windows) são incertos na transcrição original — mantidos como anedóticos, não como dado verificável.
