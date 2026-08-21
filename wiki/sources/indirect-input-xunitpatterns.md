---
type: source
title: "Indirect Input (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["indirect input", "entrada indireta", "xunit patterns glossary indirect input"]
date_created: 2026-08-21
date_updated: 2026-08-21
source_file: /home/nemomartins/Documentos/new/dev-study/raw/indirect-input-xunitpatterns.md
source_url: "http://xunitpatterns.com/Indirect%20Input.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-08-21
source_count: 0
tags: [testes, test-doubles, sut, doc, stub, control-point, xunit, fonte-primaria]
skill: tech-mentor-testing
status: stable
---

# Indirect Input (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curto do Glossário do catálogo xUnitPatterns.com que define formalmente **indirect input** ("entrada indireta"): o valor que o [[wiki/concepts/test-doubles|SUT]] recebe de outro componente (o [[wiki/concepts/test-doubles|DOC]]) e que afeta seu comportamento — retorno de função, parâmetro de saída (out) atualizado, ou exceção/erro levantado pelo DOC. É o mesmo vocabulário já registrado via [[wiki/sources/test-double-xunitpatterns-meszaros]], mas aqui isolado como definição própria, citável independentemente: a entrada indireta é o que motiva o uso de um **ponto de controle** e, tipicamente, de um **Test Stub** para injetá-la no SUT.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Indirect input é qualquer valor que afeta o comportamento do SUT e vem de um componente do qual ele depende (DOC) | "we call those values indirect inputs of the SUT" | fonte primária (Meszaros) | alta |
| Indirect inputs cobrem três formas concretas: retorno de função, parâmetro out atualizado, erro/exceção do DOC | "actual return values of functions, updated (out) parameters of procedures or subroutines, and any errors or exceptions raised by the DOC" | fonte primária | alta |
| Testar indirect input exige um ponto de controle no "lado de trás" (back side) do SUT | "requires the appropriate control point on the 'back side' of the SUT" | fonte primária | alta |
| O Test Stub é o mecanismo típico para injetar indirect inputs no SUT | "We often use a Test Stub to inject the indirect inputs into the SUT" | fonte primária | alta |

---

## Key Claims

### 1. Indirect input é definido pela direção do dado, não pelo mecanismo
A definição de Meszaros isola o critério que separa uma entrada indireta de uma **entrada direta** (parâmetro passado explicitamente na chamada ao SUT): não é *como* o valor chega, é *de onde* ele vem — um DOC, não o chamador do teste. Isso é o mesmo eixo já sintetizado em [[wiki/concepts/test-doubles]] (seção "Vocabulário formal SUT/DOC"), mas aqui a fonte primária cobre apenas o lado de entrada, sem misturar com saída indireta — o que a torna a citação mais precisa para esse metade específica do vocabulário.

### 2. "Back side" do SUT como imagem para o ponto de controle
A frase "control point on the back side of the SUT" reforça a intuição espacial usada na wiki para explicar Stub vs. Spy/Mock: entrada indireta entra pelo "fundo" do SUT (dependências que ele consulta), enquanto saída indireta sai pela mesma via em direção contrária. Controlar o fundo = Stub; observar o fundo = Spy/Mock. Ver [[wiki/concepts/indirect-input-output]].

### 3. Relação direta com Test Stub, não com Mock ou Spy
Diferente do verbete de saída indireta (que aponta para Spy/Mock), este verbete aponta especificamente para **Test Stub** como a ferramenta padrão. Isso confirma a distinção já registrada em [[wiki/sources/test-double-xunitpatterns-meszaros]]: Stub controla o que entra, Spy/Mock observam o que sai.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/test-double-xunitpatterns-meszaros]]

## Conceitos Tocados

- [[wiki/concepts/indirect-input-output]] — conceito criado nesta ingestão para hospedar o vocabulário indirect input/output, control point/observation point
- [[wiki/concepts/test-doubles]] — Test Stub como mecanismo de injeção de indirect input
- [[wiki/concepts/unit-test-solitario-vs-sociavel]] — o eixo entrada/saída indireta que distingue estilo de asserção Stub/Mock

## Questões Abertas

- Este verbete é parte de um glossário maior (o mesmo catálogo de onde veio [[wiki/sources/test-double-xunitpatterns-meszaros]]); os verbetes irmãos "indirect output", "direct input", "control point" e "observation point" ainda não foram ingeridos individualmente — candidatos naturais a próxima ingestão para fechar o vocabulário completo.

---

## Citações Relevantes

> "When the behavior of the system under test (SUT) is affected by the values returned by another component whose services it uses, we call those values indirect inputs of the SUT."

> "Indirect inputs may be actual return values of functions, updated (out) parameters of procedures or subroutines, and any errors or exceptions raised by the depended-on component (DOC)."

> "Testing of the SUT behavior with indirect inputs requires the appropriate control point on the 'back side' of the SUT. We often use a Test Stub to inject the indirect inputs into the SUT."

*(Tradução completa em `raw/indirect-input-xunitpatterns.md`.)*
