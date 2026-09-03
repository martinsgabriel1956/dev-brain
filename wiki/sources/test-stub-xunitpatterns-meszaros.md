---
type: source
title: "Test Stub (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["test stub meszaros", "stub", "responder", "saboteur", "xunit test patterns test stub"]
date_created: 2026-08-30
date_updated: 2026-08-30
source_file: /home/nemomartins/Documentos/new/dev-study/raw/test-stub-xunitpatterns-meszaros.md
source_url: "http://xunitpatterns.com/Test%20Stub.html"
author: "Gerard Meszaros"
date_published: 2007-01-01
date_ingested: 2026-08-30
source_count: 0
tags: [testes, test-doubles, stub, xunit, sut, doc, control-point, fonte-primaria]
skill: tech-mentor-testing
status: stable
---

# Test Stub (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Página canônica do padrão **Test Stub** no catálogo xUnitPatterns.com — a variação de [[wiki/concepts/test-doubles|Test Double]] dedicada a servir de **ponto de controle** para as **entradas indiretas** do SUT. Define o Test Stub como uma implementação específica de teste de uma interface da qual o SUT depende, configurada para responder com valores (ou exceções) que exercitam código não testado, e instalada no lugar da implementação real. Ao contrário do Mock Object, o Test Stub **não verifica** as saídas indiretas do SUT — sua única função é fornecer entradas controladas. Introduz duas variações centrais não detalhadas na página guarda-chuva de Test Double: **Responder** (entradas válidas, "caminho feliz") e **Saboteur** (entradas inválidas/exceções, para forçar tratamento de erro). Também cobre **Temporary Test Stub**, **Procedural Test Stub**, **Entity Chain Snipping** (substituir uma cadeia inteira de objetos relacionados por um único stub), e a dualidade **Hard-Coded vs. Configurable Test Stub**. Repete os alertas já vistos em Test Double: ter sempre um teste sem stub, não substituir o que se quer verificar, e cuidado com *Overspecified Software*.

**Nota de proveniência:** o site oficial (xunitpatterns.com) estava fora do ar (`ECONNREFUSED`) no momento da ingestão. O conteúdo em `raw/test-stub-xunitpatterns-meszaros.md` foi reconstruído via proxy de leitura + buscas que citam o texto original — fiel à estrutura e ao conteúdo técnico, mas não confirmado como transcrição literal frase a frase. Tratar citações diretas com confiança levemente menor que as demais fontes primárias já ingeridas deste site.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Test Stub é ponto de controle de entradas indiretas; não verifica saídas indiretas (isso é papel de Mock/Spy) | Definição central + seção "Distinções Importantes" | fonte primária (reconstruída) | alta |
| Existem duas variações de uso por natureza da entrada: **Responder** (válida) e **Saboteur** (inválida/exceção) | Seção "Variações" | fonte primária (reconstruída) | alta |
| Saboteur força caminhos de tratamento de erro; teste correspondente segue Simple Success Test, não Expected Exception Test — porque se espera que o SUT capture a exceção internamente | Exemplo de código com `TimeProviderEx` e explicação do padrão de teste esperado | fonte primária (reconstruída) | média-alta (exemplo específico, lógica consistente com o resto da taxonomia) |
| Entity Chain Snipping substitui uma cadeia de objetos relacionados (`Customer → Address → City → State`) por um único stub | Seção "Variações" / exemplo dedicado | fonte primária (reconstruída) | alta |
| Mesmos alertas de Test Double se aplicam: sempre ter teste sem stub; não substituir o que se quer verificar; excesso → Overspecified Software / Fragile Tests | Seção "Cuidados" | fonte primária (reconstruída) | alta (consistente com [[wiki/sources/test-double-xunitpatterns-meszaros]]) |

---

## Key Claims

### 1. Test Stub é metade do eixo controle/observação — só a metade "controle"
Onde [[wiki/sources/test-double-xunitpatterns-meszaros]] já estabelece o eixo controle-vs-observação para os cinco tipos, esta fonte aprofunda especificamente o lado do **Stub**: ele é usado quando há **código não testado** por falta de controle sobre a **entrada indireta** do SUT (ver [[wiki/sources/indirect-input-xunitpatterns]]), e **não** quando é preciso verificar uma saída — nesse caso o padrão correto é Mock Object ou Test Spy, não Stub.

### 2. Responder vs. Saboteur — a distinção que faltava no verbete guarda-chuva
A página de Test Double já citava a existência do Stub, mas não detalhava esta subdivisão prática: um **Responder** entrega entradas válidas para testar o caminho normal (geralmente com um **Simple Success Test**); um **Saboteur** entrega entradas inválidas ou lança exceções para verificar como o SUT reage a falhas do seu DOC. É uma distinção operacional útil ao escrever testes de tratamento de erro sem precisar orquestrar a falha real do componente dependido.

### 3. Entity Chain Snipping — stub como atalho para fixture setup complexo
Quando o SUT navega por uma cadeia de objetos relacionados só para chegar a um valor needed, criar a cadeia inteira (`Customer → Address → City → State`) no teste é caro e frágil. O padrão sugere "cortar" a cadeia stubando diretamente o objeto de entrada (`Customer`) para responder já com o valor final necessário — reduz o *fixture setup* e melhora a legibilidade, ao custo de acoplar o teste à forma como o SUT navega a cadeia.

### 4. Hard-Coded vs. Configurable — a mesma dualidade construtiva de Test Double, aplicada ao Stub
Reforça o que já estava registrado em [[wiki/concepts/test-doubles]]: a pergunta "como construir" (hard-coded no código do teste vs. configurável via *fixture setup*, muitas vezes gerado por reflexão/proxy dinâmico como no exemplo com JMock) é ortogonal à pergunta "por que usar" (Stub vs. Mock vs. Fake). Um Stub pode ser tanto hard-coded quanto configurável — a escolha depende de reutilização entre testes.

### 5. Mesmos guardrails de Test Double, sem novidade normativa
Os cuidados listados (ao menos um teste sem stub; não substituir o SUT em vez da dependência; excesso de stubs → Fragile Tests via Overspecified Software) replicam integralmente os já documentados em [[wiki/sources/test-double-xunitpatterns-meszaros]] — não é um claim novo, é a mesma regra reafirmada no contexto específico do Stub.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor da fonte; mesma autoria da fonte-mãe de Test Double

## Conceitos Tocados

- [[wiki/concepts/test-doubles]] — conceito central; Test Stub é uma das cinco variações, agora com fonte primária dedicada
- [[wiki/concepts/tdd]] — Temporary Test Stub é citado como uso comum em TDD, evoluindo para classe real
- [[wiki/concepts/unit-test-solitario-vs-sociavel]] — Stub é a ferramenta típica do unit test solitário (London school)

## Questões Abertas

- **Confiabilidade da extração:** por indisponibilidade do site original no momento da ingestão, o texto em `raw/` foi reconstruído via ferramenta de terceiros (proxy de leitura) e buscas — não é garantidamente uma transcrição literal. Se o site voltar ao ar, vale reingerir/comparar para confirmar fidelidade das citações diretas.
- **"Observation point" e "indirect output" ainda não têm verbete de glossário isolado ingerido** (mesma lacuna já registrada em [[wiki/sources/test-double-xunitpatterns-meszaros]]) — o par completo do eixo controle/observação segue incompleto do lado "saída".
- Nenhuma contradição encontrada com o que já estava na wiki sobre Test Doubles — esta fonte é estritamente elaborativa/complementar.

---

## Citações Relevantes

> "Its purpose is to derail whatever the [SUT] is trying to do so we can see how the [SUT] copes with these circumstances." (sobre o Saboteur)

> "We really should have at least one test that verifies it works without a Test Stub."
