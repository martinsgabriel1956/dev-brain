---
type: source
title: "Por que sua code base degrada — e como conter a entropia"
aliases: ["por que a code base degrada", "code rot", "por que sua codebase apodrece", "estrategias contra code rot"]
date_created: 2026-08-10
date_updated: 2026-08-10
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/por-que-code-bases-degradam-estrategias-code-rot.md
source_url: ""
author: "não identificado (canal BR de DSA/LeetCode)"
date_published: ""
date_ingested: 2026-08-10
source_count: 0
tags: [tech-debt, entropia-de-software, code-rot, refactoring, estimativa, planejamento, testes-de-integracao, bus-factor, feature-freeze, engineering-management, liderança]
skill: tech-mentor-leadership
status: stable
---

## TL;DR

Vídeo (pt-BR) que responde a uma pergunta recorrente na carreira do autor: **por que toda code base se degrada com o tempo, e o que fazer a respeito**. A tese central é que a degradação (*code rot* / [[wiki/concepts/entropia-de-software|entropia de software]]) é o estado *natural* — requisitos evoluem sobre arquitetura estática, o contexto de quem escreveu se perde entre trocas de equipe, hotfixes sob pressão empilham gambiarras, e casos não previstos forçam adaptações locais. Os sinais: atraso crônico, queda de velocidade, testes negligenciados/flaky, "classes super-homem" ([[wiki/concepts/god-object|God Objects]]) e "Devs Gandalf" (conhecimento concentrado numa única pessoa — [[wiki/concepts/bus-factor|bus factor]] = 1). As contramedidas propostas são **majoritariamente organizacionais, não de código**: nunca alocar 100% da capacidade (deixar ~20% de folga — *Principles of Product Development Flow*), [[wiki/concepts/boy-scout-rule|regra do escoteiro]] enforçada no PR, medir o erro de estimativa contra a [[wiki/concepts/planning-fallacy|falácia do planejamento]], code owners com módulos documentados, um padrão de arquitetura enforçado pela liderança, e [[wiki/concepts/teste-de-integracao-estreito-vs-amplo|testes de integração]] como critério de aceitação. Secundárias: [[wiki/concepts/feature-freeze|feature freeze]], análise estática ([[wiki/concepts/complexidade-ciclomatica|complexidade ciclomática]], cobertura) com o alerta da [[wiki/concepts/goodharts-law|Lei de Goodhart]], linters/tipagem gradual, e documentação via testes + [[wiki/concepts/adr-architecture-decision-record|ADRs]]/comentários. Fecho: *"qualidade é uma prática, não uma feature"*.

## Contexto sobre a fonte

Vídeo de um canal brasileiro que vende cursos de **estrutura de dados e algoritmos / LeetCode** e um curso "Roadmap pro seu próximo emprego" (o autor diz dar todas as aulas no Excalidraw). O nome do autor não é declarado na transcrição — deixado como *não identificado* no frontmatter para não inventar autoria (ver Perguntas em Aberto). A transcrição também contém dois blocos publicitários (patrocínio da escola de investimentos "AVP" na abertura e a divulgação dos cursos no fim), preservados em `raw/` mas fora do escopo técnico desta ingestão.

## Key Claims

**Claim:** A degradação de uma code base é o comportamento *natural e esperado*, não uma anomalia — o estado de baixa entropia (código organizado) é que exige trabalho contínuo para ser mantido.
**Evidence:** Enumera quatro forças estruturais: (1) requisitos evoluem sobre arquitetura estática que não foi planejada para evoluir tão rápido; (2) perda de contexto entre trocas de equipe (ex.: quem começou orientado a funções puras vs. quem chegou depois e foi para OO, sem documentação); (3) hotfix sob pressão que "joga a bola pra frente"; (4) casos não previstos que forçam gambiarras locais.
**Confidence:** média-alta — coerente com a literatura de [[wiki/concepts/entropia-de-software]] e do *Pragmatic Programmer* (analogia de jardinagem), opinião de experiência de campo sem dado quantitativo.

**Claim:** Existe um conjunto reconhecível de **sinais** de code base degradando: atraso crônico de prazos, queda geral de velocidade (inclusive de review), testes negligenciados/flaky, monolito distribuído com "classes super-homem" e dependência de um "Dev Gandalf".
**Evidence:** Descreve a espiral: apagar incêndio toda sprint → só corrigir 2 bugs e "meia feature" por sprint → pressão para reescrever uma "V2 do zero", que por sua vez envelhece e reapresenta os mesmos problemas.
**Confidence:** média — sintomas amplamente reconhecidos na indústria; o encadeamento causal é experiencial, não medido.

**Claim:** Nunca se deve alocar 100% da capacidade da equipe — a folga (~20%) é o que absorve bugs imprevistos e o deploy que falha sem forçar emissão de dívida técnica.
**Evidence:** Atribui a ideia ao livro *Principles of Product Development Flow* (Donald Reinertsen — ver [[wiki/entities/principles-of-product-development-flow]]). Raciocínio: se 100% do recurso foi gasto, a única forma de responder a um imprevisto é a gambiarra rápida (dívida). Modelo proposto: ~80% features, ~20% bug fixes/refatoração.
**Confidence:** média-alta — alinhado com teoria de filas/utilização (utilização perto de 100% dispara o tempo de espera) e com [[wiki/concepts/tech-debt-como-ferramenta]].

**Claim:** A [[wiki/concepts/boy-scout-rule|regra do escoteiro]] deve ser *enforçada no code review* — nenhum PR pode deixar o código pior do que estava. A única exceção aceitável é hotfix (por urgência); prazo de feature apertado **não** é justificativa.
**Evidence:** "A feature vai atrasar de qualquer forma" — a gambiarra não recupera o prazo, só transfere custo pra frente.
**Confidence:** alta — consistente com o princípio já documentado e com a cultura de [[wiki/concepts/code-review]].

**Claim:** A [[wiki/concepts/planning-fallacy|falácia do planejamento]] é universal; o problema grave não é errar a estimativa, é **não mensurar o erro** dela. Uma empresa que planeja 40 story points e entrega 30 repetidamente, sem medir esse gap, "vive num mundo que não é real".
**Evidence:** Exemplo do upload de vídeo: a estimativa ignora ~50% de chance de imprevisto e ignora o ciclo de idas e voltas do PR. O autor se declara cético de estimativas em geral, mas enfático de que estimar sem medir o erro é inútil.
**Confidence:** média-alta — a mensuração do erro de estimativa é prática defensável; a cifra "50% de chance de imprevisto" é ilustrativa, não empírica.

**Claim:** Testes de **integração** são o ponto de melhor custo-benefício segundo o consenso que o autor observa entre empresários/CTOs — mais do que unitários (vistos por alguns como inúteis) e end-to-end (vistos como caros). Podem ser critério de aceitação por task.
**Evidence:** Relato de conversas com "empresários e outros CTOs" (agora parte do trabalho do autor). Liga testes de integração à prevenção de code rot.
**Confidence:** baixa-média — é uma generalização de opinião de terceiros sem amostragem; o valor relativo dos tipos de teste é contextual (ver [[wiki/concepts/teste-de-integracao-estreito-vs-amplo]]).

**Claim:** A prevenção é **majoritariamente organizacional, não de código**: entender que a equipe tem capacidade finita e que usar 100% dela é criar dívida; não planejar o crescimento saudável é escolher deixar a entropia crescer.
**Evidence:** Ordena as contramedidas por importância, colocando folga de capacidade, regra do escoteiro, mensuração de estimativa, code owners e padrão enforçado *acima* das táticas de ferramenta (linter, análise estática, freeze).
**Confidence:** média-alta — tese central, bem argumentada, sem dado quantitativo.

**Claim:** Ferramental e métricas ajudam, mas **no momento em que uma métrica vira objetivo ela deixa de ser útil** ([[wiki/concepts/goodharts-law|Lei de Goodhart]]) — meta de "100% de cobertura" gera testes inúteis; 5% de cobertura, porém, é sinal legítimo de subteste.
**Evidence:** Cita complexidade ciclomática e cobertura como sinais úteis mas não-autossuficientes; defende linters, tipagem gradual (proibir `any` em TS sem justificativa comentada) e o build que quebra se as regras não passarem (praticado na empresa do autor).
**Confidence:** alta — a formulação da Lei de Goodhart no vídeo é essencialmente correta.

**Claim:** Documentação da *decisão* (por quê) é mais durável quando vive perto do código: testes como documentação de regra de negócio, [[wiki/concepts/adr-architecture-decision-record|ADRs]] e comentários explicando decisões não usuais reduzem a dependência do "Dev Gandalf".
**Evidence:** Exemplo: um teste chamado "garante que um usuário não pode criar mais do que quatro produtos" enforça *e* documenta a regra. Reconhece o risco de doc fora do código divergir, mas "melhor ter do que não ter".
**Confidence:** média-alta — alinhado com [[wiki/concepts/living-documentation]] e a prática de ADR.

## Entidades

- [[wiki/entities/principles-of-product-development-flow]] — livro de Donald Reinertsen, fonte da regra de nunca alocar 100% da capacidade (folga de fluxo).

## Conceitos

- [[wiki/concepts/entropia-de-software]] — tema central (code rot / decay).
- [[wiki/concepts/folga-de-capacidade-slack]] — **novo** — nunca alocar 100%; a regra dos ~20%.
- [[wiki/concepts/feature-freeze]] — **novo** — semana sem features novas para repaginar arquitetura.
- [[wiki/concepts/bus-factor]] — **novo** — o "Dev Gandalf" como sintoma de bus factor = 1.
- [[wiki/concepts/boy-scout-rule]] · [[wiki/concepts/tech-debt-como-ferramenta]] · [[wiki/concepts/god-object]] · [[wiki/concepts/planning-fallacy]] · [[wiki/concepts/goodharts-law]] · [[wiki/concepts/dora-metrics]] · [[wiki/concepts/living-documentation]] · [[wiki/concepts/adr-architecture-decision-record]] · [[wiki/concepts/refactor-vs-rewrite-matrix]] · [[wiki/concepts/estimativas-de-software]] · [[wiki/concepts/complexidade-ciclomatica]] · [[wiki/concepts/teste-de-integracao-estreito-vs-amplo]] · [[wiki/concepts/code-review]] · [[wiki/concepts/refatoracao]]

## Perguntas em Aberto

- **Autoria não confirmada.** A transcrição não declara o nome do autor; sabe-se apenas que é um canal BR que vende curso de DSA/LeetCode e um "Roadmap pro seu próximo emprego", com aulas dadas no Excalidraw. `author` ficou como "não identificado" e `source_url` vazio — a resolver se a fonte original (URL do vídeo) aparecer.
- **Atribuição do livro.** A regra "nunca 100% de capacidade" foi atribuída no vídeo a *Principles of Product Development Flow* sem citar Reinertsen pelo nome nem página; a atribuição de autoria aqui vem de conhecimento externo `[external]`, não da transcrição — ver a entidade para a nota de verificação.

## Citações preservadas

> "O natural, na verdade, é que ela se degrade mesmo — isso é o que é observado."

> "As pessoas não necessariamente odeiam Java. Elas odeiam trabalhar em code base de Java que começou 10 anos atrás e cresceu de maneira desorganizada."

> "No momento em que uma métrica vira um objetivo, essa métrica deixa de ser útil."

> "Qualidade é uma prática, não é uma feature que você implementa."
