---
type: source
title: "Interaction Point (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["interaction point", "ponto de interação", "xunit patterns glossary interaction point"]
date_created: 2026-09-02
date_updated: 2026-09-02
source_file: /home/nemomartins/Documentos/new/dev-study/raw/interaction-point-xunitpatterns.md
source_url: "http://xunitpatterns.com/interaction%20point.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-02
source_count: 0
tags: [testes, test-doubles, sut, doc, interaction-point, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# Interaction Point (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curtíssimo (uma frase) do Glossário do catálogo xUnitPatterns.com que define formalmente **interaction point** ("ponto de interação"): qualquer ponto no qual um teste interage com o [[wiki/sources/sut-xunitpatterns|SUT]]. É a categoria **mãe** dos dois termos já ingeridos isoladamente — [[wiki/sources/control-point-xunitpatterns]] (pedir algo ao SUT: entrada) e [[wiki/sources/observation-point-xunitpatterns]] (verificar o que o SUT fez ou se tornou: saída) — ambos definidos na wiki como "um tipo de interaction point", mas até agora sem que o próprio termo guarda-chuva tivesse fonte primária dedicada. Com este verbete, a hierarquia formal do glossário fecha por completo: **interaction point → control point | observation point**.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Interaction point é um ponto no qual um teste interage com o SUT | "A point at which a test interacts with the system under test (SUT)" | fonte primária (Meszaros) | alta |
| Interaction point pode ser control point ou observation point — sem terceira variante | "An interaction point can be either a control point or an observation point" | fonte primária | alta |

---

## Key Claims

### 1. Interaction point é a categoria mãe, não um terceiro tipo de ponto
A wiki já usava "interaction point" por menção indireta em [[wiki/sources/control-point-xunitpatterns]] e [[wiki/sources/observation-point-xunitpatterns]] ("It is a kind of interaction point" em ambos), mas sem fonte primária isolada do termo guarda-chuva. Este verbete confirma que a partição é binária e exaustiva ("can be **either**... **or**...") — todo ponto de interação de um teste com o SUT é, por definição, ou de controle ou de observação. Não existe categoria residual.

### 2. A definição amarra "interação" estritamente à relação teste-SUT
"A point at which a test interacts with the SUT" fixa o escopo: interaction point não descreve qualquer troca entre objetos do sistema, só a interação que o **teste** (o código de teste, executando em nome do desenvolvedor) tem com o SUT. Isso reforça a leitura já registrada em [[wiki/concepts/indirect-input-output]] de que control point e observation point são, especificamente, os dois lados de como o teste manipula e inspeciona o SUT — não um vocabulário genérico de comunicação entre componentes do próprio sistema.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/control-point-xunitpatterns]], [[wiki/sources/observation-point-xunitpatterns]] e [[wiki/sources/sut-xunitpatterns]]

## Conceitos Tocados

- [[wiki/concepts/indirect-input-output]] — interaction point é o nó raiz explícito da hierarquia control point/observation point que organiza o eixo entrada/saída indireta
- [[wiki/concepts/test-doubles]] — control point e observation point (agora com categoria mãe formalizada) são os dois mecanismos pelos quais um teste interage com o SUT ao redor de um Test Double

## Questões Abertas

- Com interaction point, control point e observation point todos ingeridos, a hierarquia formal desse ramo do glossário está completa. Restam do mesmo glossário, ainda por fonte primária isolada: **"direct input"**, **"indirect output"** e **"fixture teardown"** — conhecidos só por menção nas fontes já ingeridas.
- O verbete não esclarece se o "teste" da definição inclui código de fixture setup/teardown ou só o corpo do test method — a ambiguidade já existia implicitamente em control point (que cobre fixture setup/teardown) e não é resolvida aqui.

---

## Citações Relevantes

> "A point at which a test interacts with the system under test (SUT). An interaction point can be either a control point or an observation point."

*(Tradução completa em `raw/interaction-point-xunitpatterns.md`.)*
