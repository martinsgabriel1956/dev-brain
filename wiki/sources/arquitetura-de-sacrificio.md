---
type: source
title: "Arquitetura de Sacrifício (Sacrificial Architecture) — Martin Fowler"
aliases: ["sacrificial architecture", "arquitetura de sacrificio", "arquitetura sacrificial"]
date_created: 2026-08-10
date_updated: 2026-08-10
source_count: 0
tags: [arquitetura, evolutionary-design, monolito, microsservicos, tech-debt, refatoracao, martin-fowler, ebay, google]
skill: tech-mentor-backend
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/arquitetura-de-sacrificio.md
source_url: "https://martinfowler.com/bliki/SacrificialArchitecture.html"
author: "Martin Fowler"
date_published: 2014-10-20
date_ingested: 2026-08-10
---

# Arquitetura de Sacrifício (Sacrificial Architecture)

## TL;DR

Artigo do bliki de Martin Fowler (2014) que reformula um instinto comum: jogar fora uma base de código **não é fracasso**. "Frequentemente o melhor código que você consegue escrever hoje é um código que você vai descartar daqui a alguns anos." Uma **[[wiki/concepts/arquitetura-de-sacrificio|arquitetura de sacrifício]]** é escolhida *deliberadamente* aceitando que, com sucesso, ela precisará ser substituída — porque crescimento exponencial não é gentil com decisões arquiteturais (a arquitetura certa para o eBay de 1996 não é a de 2006). Regra do Google: projete para 10× a necessidade atual e planeje reescrever antes de 100×. Pontos-chave: (1) no início, priorize **flexibilidade** sobre performance/escala — ter usuários demais numa base pouco performática é um problema melhor que o inverso; (2) sacrifício **não** dispensa qualidade interna — boa **modularidade** ([[wiki/concepts/monolito-modular]]) é o que permite substituir módulos individuais em vez do sistema inteiro; (3) cuidado com a **contabilidade** (amortização da base de código pode travar a substituição); (4) um **[[wiki/concepts/monolito|monolito]]** costuma ser uma boa arquitetura de sacrifício — [[wiki/concepts/microsservicos|microsserviços]] adicionam distribuição e assincronia (amplificadores de complexidade) cedo demais; (5) quem escreve o código sacrificial é quem decide sacrificá-lo — dinâmica muito diferente de um time novo que odeia código herdado.

## Key Claims

**Claim:** Descartar uma base de código não é sinal de fracasso; código de vida curta ainda entrega muito valor.
**Evidence:** O eBay passou por Perl (1995, feito num fim de semana) → C++/Windows (1997) → Java (2002). As versões descartadas não foram erro: "boa parte desse sucesso foi construída sobre o software descartado dos anos 90." Sucesso pode ser construído sobre código "há muito enviado para o `/dev/null`".
**Confidence:** alta

**Claim:** Crescimento exponencial invalida decisões arquiteturais — a arquitetura certa depende da escala do momento.
**Evidence:** "A arquitetura certa para o eBay de 1996 não vai ser a arquitetura certa para o eBay de 2006. A de 1996 não aguentaria a carga de 2006, mas a versão de 2006 é complexa demais para construir, manter e evoluir frente às necessidades de 1996."
**Confidence:** alta

**Claim:** A diretriz pode virar política organizacional (regra do "10×").
**Evidence:** No Google, a regra explícita é projetar para 10× a necessidade atual; se as necessidades ultrapassam uma ordem de grandeza, muitas vezes é melhor jogar fora e refazer. Subsistemas são redesenhados e descartados a cada poucos anos.
**Confidence:** alta

**Claim:** No início, flexibilidade importa mais que performance/escalabilidade.
**Evidence:** Cedo você tem menos certeza do que o sistema precisa fazer; foque em flexibilidade para mudar features. "Conseguir usuários demais numa base de código pouco performática costuma ser um problema melhor do que o inverso." Contraponto a "performance é uma feature" (Jeff Atwood): qualquer feature se escolhe contra outras — é trade-off de negócio, não regra absoluta.
**Confidence:** alta

**Claim:** Arquitetura sacrificial ≠ abandonar qualidade interna; modularidade é o que habilita a substituição.
**Evidence:** "Sacrificar qualidade interna vai te morder mais rápido do que o momento da substituição." Boa modularidade ajuda a substituir; explorar a melhor estrutura modular numa versão inicial gera conhecimento para a substituição. Conforme o sistema cresce, é mais eficaz sacrificar **módulos individuais** — só possível com boas fronteiras de módulo.
**Confidence:** alta

**Claim:** Contabilidade/amortização pode impedir a substituição de um sistema inviável.
**Evidence:** Fowler relata casos reais de organizações relutantes em substituir sistemas claramente inviáveis por causa da forma como amortizavam a base de código. Mais provável em grandes empresas.
**Confidence:** média (relato anedótico do autor, sem números)

**Claim:** Um monolito costuma ser uma arquitetura de sacrifício melhor que microsserviços.
**Evidence:** Substituibilidade modular é argumento pró-microsserviços, mas microsserviços implicam distribuição e assincronia — "amplificadores de complexidade". Projetos que adotaram microsserviços sem necessidade desaceleraram seriamente o pipeline de features. Melhor: monolito primeiro, microsserviços depois para "ir desmontando-o gradualmente".
**Confidence:** alta

**Claim:** O direito de sacrificar código pertence a quem o escreveu.
**Evidence:** "O time que escreve a arquitetura de sacrifício é o time que decide que chegou a hora de sacrificá-la." Diferente de um time novo que odeia código herdado sem entender o contexto em que foi escrito. Sacrificar conscientemente o próprio código é dinâmica distinta.
**Confidence:** alta

## Entities

- **Martin Fowler** — autor; ThoughtWorks; bliki. Ver [[wiki/sources/microsservicos-martin-fowler-james-lewis]], [[wiki/sources/application-boundary-martin-fowler]], [[wiki/sources/refatoracao-pragmatic-programmer-martin-fowler-2a-edicao]].
- **eBay** — caso canônico de reescritas sucessivas (Perl → C++ → Java) sob crescimento exponencial.
- **Google** — regra organizacional do "projete para 10×, reescreva antes de 100×".
- **Jeff Atwood** — autor da frase "performance é uma feature", relativizada por Fowler.

## Concepts

- [[wiki/concepts/arquitetura-de-sacrificio]] — o conceito central (criado nesta ingestão).
- [[wiki/concepts/monolito]] — a arquitetura de sacrifício recomendada por padrão.
- [[wiki/concepts/microsservicos]] — substituibilidade modular vs. amplificação de complexidade cedo demais.
- [[wiki/concepts/monolito-modular]] — modularidade como habilitador da substituição por módulos.
- [[wiki/concepts/strangler-fig-pattern]] — o "desmontar gradualmente" o monolito em microsserviços.
- [[wiki/concepts/ciclo-de-mudanca-de-arquitetura]] e [[wiki/concepts/ciclo-da-desgraca-software]] — sacrifício consciente vs. reescrita big-bang por ódio ao legado.
- [[wiki/concepts/tech-debt-como-ferramenta]] — sacrifício deliberado como dívida assumida com intenção.
- [[wiki/concepts/over-engineering]] — priorizar flexibilidade cedo evita otimização prematura.
- [[wiki/concepts/refatoracao]] — alternativa incremental à substituição total.
- [[wiki/concepts/escalabilidade-horizontal]] — a escala que invalida a arquitetura inicial.
- [[wiki/concepts/feature-flag]] — feature sacrificial liberada a um subconjunto de usuários.
- [[wiki/concepts/application-boundary]] — fronteiras (de módulo/serviço) como construção social e técnica.

## Open Questions / Contradictions

- **Sacrifício vs. `strangler-fig`**: Fowler recomenda "monolito primeiro, microsserviços depois para desmontá-lo gradualmente" — isto é essencialmente o [[wiki/concepts/strangler-fig-pattern]]. A tensão registrada em [[wiki/concepts/ciclo-da-desgraca-software]] é que a substituição *big-bang* (reescrita do zero) frequentemente reproduz o mesmo problema; o artigo mitiga isso ao insistir em modularidade e em sacrificar **módulos**, não o sistema todo, à medida que ele amadurece.
- **Quem decide sacrificar**: a tese "o direito de sacrificar pertence a quem escreveu" contrasta com contextos reais em que o time original saiu (bus factor / perda de contexto — ver [[wiki/sources/por-que-code-bases-degradam-estrategias-code-rot]]). Nesse caso, quem herda tem o código sem o contexto que justificaria (ou não) o sacrifício.
- **Regra do "10×" do Google**: apresentada como fato organizacional, sem citação primária no artigo. Confiança na regra é alta como *heurística*, média como afirmação factual verificável.

## Raw quotes

> "But often the best code you can write now is code you'll discard in a couple of years time."

> "At Google, the explicit rule is to design a system for ten times its current needs, with the implication that if the needs exceed an order of magnitude then it's often better to throw away and replace from scratch."

> "Knowing your architecture is sacrificial doesn't mean abandoning the internal quality of the software. […] Good modularity is a vital part of a healthy code base, and modularity is usually a big help when replacing a system."

> "Microservices imply distribution and asynchrony, which are both complexity boosters. […] So a monolith is often a good sacrificial architecture, with microservices introduced later to gradually pull it apart."

> "The team that writes the sacrificial architecture is the team that decides it's time to sacrifice it. […] It's easy to hate code you didn't write, without an understanding of the context in which it was written."
