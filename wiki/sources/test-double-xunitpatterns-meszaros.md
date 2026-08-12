---
type: source
title: "Test Double (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["test double meszaros", "imposter", "xunit test patterns test double", "dublê de teste primária"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/test-double-xunitpatterns-meszaros.md
source_url: "http://xunitpatterns.com/Test%20Double.html"
author: "Gerard Meszaros"
date_published: 2007-01-01
date_ingested: 2026-08-12
source_count: 0
tags: [testes, test-doubles, mock, stub, fake, spy, dummy, xunit, sut, doc, fonte-primaria]
skill: tech-mentor-testing
status: stable
---

# Test Double (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Página canônica do padrão **Test Double** no catálogo xUnitPatterns.com — a **fonte primária** da taxonomia que a wiki até agora só tinha via [[wiki/entities/martin-fowler|Fowler]] (secundária). Escrita pelo próprio [[wiki/entities/gerard-meszaros|Gerard Meszaros]] como versão preliminar do capítulo do livro *xUnit Test Patterns* (2007, p. 522). Define **Test Double** ("Impostor") como termo guarda-chuva: substituir um **DOC** (componente-dependência real) por um "equivalente específico para teste" que só precisa expor a **mesma API** — não replicar o comportamento. Estabelece o vocabulário preciso — **SUT**, **DOC**, **entrada/saída indireta**, **ponto de controle/observação** — e classifica as cinco variações por *como/por que* se usa o double: **Dummy** (só preenche assinatura, nunca é usado), **Stub** (ponto de controle de entradas indiretas), **Spy** (Stub que grava saídas indiretas), **Mock** (verifica saídas indiretas — ênfase na verificação, não "Stub + asserção"), **Fake** (implementação funcional simplificada, nem controle nem observação). Usa a analogia do **dublê de cinema** (só precisa parecer o suficiente para a cena) e alerta: sempre ter ao menos um teste sem double, não substituir o que se quer verificar, e o excesso de doubles gera *Fragile Tests* por *Overspecified Software*.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Test Double é o termo guarda-chuva; as cinco variações (Dummy/Stub/Spy/Mock/Fake) são subtipos classificados por como/por que se usa | Estrutura do capítulo: seção "Variações" enumera cada tipo com seu papel distinto | fonte primária (Meszaros) | alta |
| O Test Double só precisa fornecer a **mesma API** do DOC real — não replicar o comportamento nem implementar a interface inteira | "It merely has to provide the same API as the real one" / "we don't need to implement the whole interface of the DOC" | fonte primária | alta |
| Mock ≠ "Stub + asserções" — a diferença é a **ênfase na verificação** das saídas indiretas, um uso fundamentalmente diferente | "a Mock Object is a lot more than just a Test Stub plus assertions; it is used a fundamentally different way" | fonte primária (definição de autor) | alta (é definição normativa, não empírica) |
| Test Spy é "apenas um" Stub com capacidade de gravação; o estilo de teste se parece mais com Stub do que com Mock | "the Test Spy is 'just a' Test Stub with some recording capability" | fonte primária | alta |
| Dummy Object não é bem um Test Double — é alternativa aos padrões de valor (Literal/Derived/Generated Value) | "a Dummy Object isn't really a Test Double per se" | fonte primária | alta |
| Usar Test Double testa o SUT numa configuração diferente da produção → é preciso ao menos um teste sem double | "we really should have at least one test that verifies it works without a Test Double" | fonte primária (recomendação) | alta |
| Excesso de Test Doubles causa Fragile Tests via Overspecified Software | "excessive use of Test Doubles can result in Fragile Tests as a result of Overspecified Software" | fonte primária | média-alta (causalidade afirmada, sem dado quantitativo) |
| Fake substituindo banco por hash tables em memória tornou testes ~50× mais rápidos | Relato do sidebar "Faster Tests Without Shared Fixtures" | fonte primária (relato de experiência) | média (número específico de um caso, não benchmark generalizável) |

---

## Key Claims

### 1. O vocabulário preciso: SUT, DOC, entrada/saída indireta, pontos de controle/observação
A contribuição durável desta fonte não é só a taxonomia — é o **vocabulário formal** que a sustenta. Substitui-se o **DOC** (*Depended-On Component*), nunca o **SUT** (*System Under Test*). O que motiva escolher cada tipo de double é a direção do dado: **entrada indireta** (o SUT recebe do DOC → precisa de um **ponto de controle** → Stub/Mock) vs. **saída indireta** (o SUT dispara sobre o DOC → precisa de um **ponto de observação** → Spy/Mock). Esse eixo controle-vs-observação é o que organiza os cinco tipos e é o que falta na descrição informal "mock é fake com asserção". Ver [[wiki/concepts/test-doubles]].

### 2. Classificação por papel (por que), não por construção (como)
Meszaros separa explicitamente duas perguntas: **por que** usar o double (define Dummy/Stub/Spy/Mock/Fake) vs. **como** construí-lo (Hard-Coded vs. Configurable Test Double, ortogonais ao tipo). Um Mock pode ser hard-coded ou gerado por toolkit; a técnica de construção não muda o papel. Essa separação evita a confusão comum de tratar "mock" como sinônimo de "objeto gerado por biblioteca de mocking".

### 3. Mock vs. Stub vs. Spy — a distinção fina
- **Stub**: ponto de **controle** de entradas indiretas — força o SUT por caminhos específicos.
- **Spy**: um Stub que também **grava** as saídas indiretas para verificação *posterior* pelo teste (estilo de asserção parecido com Stub).
- **Mock**: verifica as saídas indiretas com **ênfase na verificação** — pode falhar o teste *durante* a interação (expectativas). É "usado de forma fundamentalmente diferente", não é Stub + asserção.

Isso refina a "regra de ouro" já registrada na wiki ([[wiki/concepts/test-doubles]]) e o eixo London/Detroit ([[wiki/concepts/unit-test-solitario-vs-sociavel]]).

### 4. A analogia do dublê e o princípio "fiel o suficiente"
Como o dublê de cinema só precisa parecer o ator "o suficiente para a cena", o Test Double só precisa expor a API que *aquele teste* exercita — não a interface inteira do DOC. Diferentes testes podem ter doubles diferentes para o mesmo DOC. É a base conceitual do [[wiki/concepts/teste-de-integracao-estreito-vs-amplo|narrow integration test]] e liga-se à necessidade de garantir que o double seja fiel o bastante ([[wiki/concepts/contract-testing]], [[wiki/concepts/self-initializing-fake]]).

### 5. Os alertas — quando o Test Double vira armadilha
Três guardrails da fonte primária: (a) ter **ao menos um teste sem double**, porque o SUT roda numa config diferente da produção; (b) **não substituir a parte que se quer verificar** (senão testa-se o software errado); (c) **excesso de doubles → Fragile Tests** por *Overspecified Software*. Alinha-se ao code smell já registrado ("5+ mocks = acoplamento alto demais") e à preferência Fake > Mock em [[wiki/concepts/test-doubles]].

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor da fonte e criador da taxonomia; esta é a **fonte primária** dele (antes só tínhamos o relato de Fowler)
- [[wiki/entities/martin-fowler]] — divulgou/popularizou esta taxonomia no bliki (2006), antes do livro sair

## Conceitos Tocados

- [[wiki/concepts/test-doubles]] — conceito central; ganha fonte primária + vocabulário SUT/DOC/entrada-saída indireta
- [[wiki/concepts/teste-de-integracao-estreito-vs-amplo]] — double é a peça que viabiliza o narrow integration test
- [[wiki/concepts/unit-test-solitario-vs-sociavel]] — Stub/Mock definem solitário vs. sociável
- [[wiki/concepts/contract-testing]] — garante que o double seja fiel o suficiente ao DOC real
- [[wiki/concepts/self-initializing-fake]] — variação de Fake que se autovalida contra o serviço real
- [[wiki/concepts/tdd]] — contexto onde os doubles são usados
- [[wiki/concepts/piramide-de-testes]] — doubles são a ferramenta dos testes unitários
- [[wiki/concepts/testes-integracao-banco-real]] — Fake em memória vs. banco real (tradeoff velocidade × fidelidade)

---

## Questões Abertas

- **"Mock" na fonte (2007) ≠ "mock" das bibliotecas modernas.** Frameworks como Jest/Vitest/Mockito chamam de "mock" qualquer double gerado — que na taxonomia de Meszaros pode ser Stub, Spy ou Mock. A wiki deve manter a distinção conceitual mesmo quando a ferramenta usa o termo de forma frouxa. Não é contradição, é deriva de vocabulário; registrar ao ingerir fontes de ferramentas de mocking.
- O número "~50× mais rápido" (Fake em memória vs. banco) é um relato de caso único do livro, não benchmark reproduzível — usar como ilustração, não como métrica.
- A fonte é uma **versão preliminar** do capítulo (o próprio site avisa que "o conteúdo mudou substancialmente" na versão publicada, p. 522). Divergências finas com a edição final do livro são possíveis; a taxonomia e as definições centrais, porém, são estáveis e batem com o relato de Fowler já ingerido.

---

## Citações Relevantes

> "We replace a component on which the SUT depends with a 'test-specific equivalent.'"

> "The Test Double doesn't have to behave exactly like the real DOC; it merely has to provide the same API as the real one so that the SUT thinks it is the real one!"

> "How closely the stunt double needs to resemble the actor depends on the nature of the scene."

> "A Mock Object is a lot more than just a Test Stub plus assertions; it is used a fundamentally different way."

> "So in many ways the Test Spy is 'just a' Test Stub with some recording capability."

> "We really should have at least one test that verifies it works without a Test Double. [...] excessive use of Test Doubles can result in Fragile Tests as a result of Overspecified Software."
