---
type: concept
title: "Supply Chain Security"
aliases: ["supply chain security", "seguranca de cadeia de suprimentos de software", "ataque de supply chain"]
date_created: 2026-07-20
date_updated: 2026-07-20
source_count: 2
tags: [supply-chain-security, sbom, slsa, sigstore, cosign, dependency-pinning, sca, npm, security]
skill: tech-mentor-security
status: stable
---

# Supply Chain Security

Proteção contra comprometimento introduzido através de dependências de terceiros — bibliotecas, pacotes, artefatos de build — em vez de vulnerabilidades no próprio código da aplicação. Cobre três vetores principais: **dependências** (SCA + SBOM + hash pinning), **artefatos de build** (assinatura com Sigstore/Cosign + SLSA provenance) e **runtime** (admission controller verifica assinaturas antes de rodar).

## O Vetor Mais Comum: Pacotes Comprometidos

[[wiki/sources/ai-jail-sandbox-para-agentes-de-ia-akita]] descreve o padrão de ataque mais direto: uma biblioteca popular do npm (citado o caso do Axios, não verificado por fonte primária nesta ingestão) é comprometida e um script malicioso é injetado no hook `postinstall` do `package.json`. A vítima não precisa executar nada além de `npm install` — o hook dispara automaticamente. O mesmo padrão já afetou o Composer (PHP) e o ecossistema Python (PyPI), segundo a mesma fonte.

**Regra prática defendida pela fonte:** tratar toda dependência de terceiro como potencialmente hostil até prova em contrário — inclusive pacotes populares e com milhões de downloads, já que popularidade não é proteção contra comprometimento de conta de mantenedor ou de infraestrutura de publish.

## Defesa em Nível de Máquina: Conter o Agente, Não Só o Pacote

Uma camada de defesa adicional, tratada em detalhe em [[wiki/concepts/agent-containment]], parte de uma premissa diferente: em vez de tentar impedir que qualquer pacote malicioso chegue (via SCA/SBOM/pinning), **assume-se que ele vai chegar** e limita-se o raio de explosão isolando o processo que instala/executa pacotes (incluindo o próprio agente de IA que roda `npm install` em nome do usuário) — via sandbox como o [[wiki/entities/bubblewrap]]. É [[wiki/concepts/defense-in-depth]] aplicado especificamente à cadeia de suprimentos: SBOM/SCA são a primeira linha (prevenção), sandboxing de execução é a segunda (contenção do dano quando a primeira falha).

## Vetores Cobertos (Visão Geral)

- **Dependências:** SCA (Software Composition Analysis) + SBOM (Software Bill of Materials, formatos CycloneDX/SPDX) + hash pinning de versões.
- **Artefatos de build:** assinatura keyless com Sigstore/Cosign (certificado temporário via Fulcio a partir de OIDC token do CI, registro em Rekor) + SLSA provenance (níveis 0–3 de confiança de build).
- **Runtime/execução local:** contenção de processo (AI Jail/Bubblewrap) para o caso em que o pacote comprometido já está instalado e executa código arbitrário na máquina do desenvolvedor ou do agente de IA.

## Relação com Outros Conceitos

- [[wiki/concepts/agent-containment]] — mitigação de runtime quando SBOM/SCA falham em bloquear o pacote comprometido.
- [[wiki/concepts/defense-in-depth]] — supply chain security bem-feita é, ela mesma, múltiplas camadas (SBOM, assinatura, sandboxing), não uma ferramenta única.
- [[wiki/concepts/principio-do-menor-privilegio]] — um script `postinstall` idealmente não deveria ter os mesmos privilégios do usuário que roda `npm install`; contenção de agente é uma forma de aproximar esse ideal na prática.

## Key Sources

- [[wiki/sources/supply-chain-security]] — SBOM, SLSA, Sigstore/Cosign como pilares de dependências e artefatos de build
- [[wiki/sources/ai-jail-sandbox-para-agentes-de-ia-akita]] — vetor de ataque via `postinstall` malicioso e defesa via contenção de processo/agente
