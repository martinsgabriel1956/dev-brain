---
type: concept
title: "Argumentos e atributos de um resource"
aliases: ["argument reference", "attribute reference"]
date_created: 2026-10-26
date_updated: 2026-10-26
source_count: 1
tags: [terraform, resource, inputs, outputs, documentacao]
skill: tech-mentor-infra
status: draft
---

# Argumentos e atributos

Toda página de resource no [[wiki/concepts/terraform-registry]] tem:

- **Argumentos (inputs)** — o que você escreve no [[wiki/concepts/terraform-blocos|bloco]]; obrigatórios ou opcionais. Ex.: `region` é opcional (herda do provider); `ami` parece opcional mas é **obrigatório a menos que se passe `launch_template`** — a documentação exige ler o texto, não só a etiqueta.
- **Atributos (outputs)** — informações geradas **após** a criação (ARN, DNS público, IP). Podem alimentar outros recursos.

Fonte: [[wiki/sources/introducao-ao-terraform-iac-devops]]. Exemplo prático: [[wiki/concepts/ami]].

## Key sources

- [[wiki/sources/introducao-ao-terraform-iac-devops]]
