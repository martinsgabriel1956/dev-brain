---
type: concept
title: "Quality Gate"
aliases: ["quality gates", "portão de qualidade", "gate de qualidade", "análise estática em pull request"]
date_created: 2026-07-16
date_updated: 2026-08-27
source_count: 9
tags: [quality-gate, linter, analise-estatica, clean-code, modularizacao, ia, milestone, criterios-de-qualidade, ratchet, babysitting-de-agentes, branch-protection]
skill: tech-mentor-testing
status: draft
---

# Quality Gate

Conjunto de regras automatizadas (linter, análise estática, limites estruturais) que um pull request precisa passar antes de ser mergeado. Diferente de uma [[wiki/concepts/rfc-request-for-comments|RFC]] — que define o que deve ser feito antes de codar — o quality gate valida o que foi de fato produzido, incluindo código gerado por IA.

## Definições Formais da Literatura

[[wiki/sources/gate-de-qualidade-definicoes-formais]] reforça que não existe uma definição única e "mais correta" de quality gate — é um conceito com múltiplas formulações complementares na literatura de engenharia de software:

- **Checklist formal + aprovação por gate** (autor não identificado com confiança na transcrição da fonte) — listas de verificação formais usadas ao longo da vida de um projeto; em cada gate ocorre aprovação formal e aceitação, com avaliação da qualidade e integridade do produto comunicada aos stakeholders corretos.
- **Milestone com critérios pré-definidos** (autor não identificado com confiança na transcrição da fonte) — quality gates são milestones e pontos de decisão com critérios pré-definidos e focados na qualidade.
- **Ponto de verificação de ciclo de vida (Schneider)** — um quality gate é um ponto de verificação onde um conjunto de critérios de qualidade pré-definidos precisa ser atendido para que o processo avance de uma etapa para outra em seu ciclo de vida; nessa visão o gate cumpre o papel de milestone através de regras que atendem a padrões de qualidade.

Dessas três visões, a fonte extrai características estruturais válidas independente da definição escolhida:

- **Exige critérios de entrada e saída explícitos** — sem eles não há como avaliar objetivamente se o gate foi atingido.
- **Pode existir no ciclo de desenvolvimento ou no ciclo de teste** — não é exclusivo de uma fase específica.
- **É disparado por critérios, não por datas** — o gate é atingido quando os critérios são cumpridos, não em um prazo fixo do calendário.
- **Produz um resultado binário** — aprovado ou reprovado, sem estado intermediário.
- **Múltiplos gates podem rodar em paralelo, avaliados por pessoas diferentes** — ex.: um dev trabalha em um gate de qualidade de código enquanto outro dev trabalha, simultaneamente, em um gate que avalia se a quantidade e severidade de defeitos abertos atende ao critério de aprovação para produção.

Essa camada teórica generaliza o que já era descrito de forma prática em [[wiki/concepts/pipeline-de-qualidade]] — cada camada de uma pipeline de qualidade (lint, tipagem, cobertura, segurança, mutação, E2E) é, na prática, um quality gate no sentido formal acima: um ponto de verificação com critérios de entrada/saída definidos e resultado binário.

## Quality Gate Forçando Clean Code em Código Gerado por IA

[[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] argumenta que quality gates com **limites estruturais** — tamanho máximo de função, quantidade de funções por arquivo, quantidade de linhas por arquivo, percentual aceitável de duplicação — não servem só para barrar código ruim: eles mudam o comportamento da própria IA durante a geração. Ao limitar o tamanho de uma função ou arquivo, a IA é forçada a pensar em como modularizar o projeto para respeitar o limite, em vez de gerar um bloco monolítico que só depois seria refatorado.

**Caso prático citado (app code.persua.com):** ao pedir para a IA modularizar um app por "flavor" (variante de build), o processo passou por etapas sucessivas — primeiro modularização com `if`s em runtime (trechos de código não executados dependendo do flavor buildado), depois questões de build mais finas: desabilitar renderização de componentes não usados, desabilitar arquivos/pacotes/assets por flavor para reduzir o tamanho final do build, e inspecionar o artefato final para verificar compliance com as regras de modularização definidas.

## Ratchet: A Baseline Só Pode Melhorar

[[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] detalha o mecanismo que torna um quality gate sustentável quando ~100% do código é gerado por IA: o padrão [[wiki/concepts/ratchet-baseline|ratchet]] ("catraca"). Em vez de exigir um padrão de qualidade ideal (o que faria todo PR falhar num projeto que nunca teve controle de qualidade), o gate congela o estado atual de métricas — violações de lint, % de duplicação, % de cobertura, arquivos acima de um limite de tamanho — como baseline, e bloqueia qualquer PR que piore qualquer uma delas, mesmo que seja por 0,1 ponto percentual. A partir daí o repositório só pode melhorar ou empatar. Isso desloca a exigência de "a IA precisa acertar de primeira" para "a IA não pode regredir o que já existe" — um critério objetivo, automatizável e compatível com deixar a IA escrever a maior parte (ou toda) a base de código sem o projeto virar um "slop" em poucos meses.

## Babysitting: o Agente Monitora o Próprio Pull Request

A mesma fonte descreve um padrão operacional que fecha o loop do quality gate: depois de abrir o PR, o próprio agente de IA fica em **babysitting** — verificando repetidamente se o CI está verde e se revisores (Copilot, ferramenta externa, ou um humano) deixaram comentários; quando há comentários, o agente os endereça e resolve as conversas no GitHub, até o PR poder ser mergeado. A recomendação prática é encapsular esse comportamento numa skill dedicada e customizável (ver [[wiki/concepts/skills-agente]]), em vez de reexplicar o fluxo a cada tarefa.

## Exemplo de Pipeline de CI Concreto

A mesma fonte documenta um pipeline real por trás do quality gate: `npm ci` (instalação determinística) → `npm audit --audit-level critical` (bloqueia merge) → `npm audit --audit-level high` (avisa, não bloqueia) → lint → testes com coverage (Jest) → um script de quality gate que coleta métricas (incluindo duplicação via `jscpd`), compara contra a baseline congelada, e escreve um sumário em Markdown com métricas, baseline e falhas. Os artefatos (coverage, relatórios) são enviados como upload do CI — não apenas comentados no PR — porque **o próprio agente de IA precisa ter acesso a eles** durante o babysitting para entender o que está falhando, não só um humano lendo a UI do PR. Ver também a instância paralela desse padrão para qualidade de *modelo* (não só de código) em [[wiki/concepts/pipeline-de-qualidade]].

## Quality Gate Não Substitui Entendimento do Projeto

A mesma fonte é explícita sobre o limite dessa prática: **"tu não pode só ter agentes pra revisar, só ter agentes pra testar, só ter linter [...] se tu deixar o entendimento do teu próprio projeto ir por água abaixo."** Quality gates, testes automatizados e linters rodando em paralelo garantem qualidade objetiva e mensurável, mas não substituem o dev entender as regras que a IA colocou no sistema — para isso, a fonte recorre à skill [[wiki/concepts/skills-agente|Grill Me]] como complemento, não como substituto.

## Branch Protection como Mecanismo de Enforcement

Todos os exemplos acima descrevem *o que* um gate verifica; [[wiki/sources/underengineering-overengineering-mario-souto]] descreve o mecanismo mínimo que transforma um check de CI em gate de fato — sem ele, lint e teste podem rodar e falhar sem impedir o merge. No GitHub, isso é feito via regra de proteção de branch (Settings → Branches): exigir pull request antes de merge, e marcar os nomes dos jobs do GitHub Actions (ex.: `lint`, `test`) como *required status checks*. Só a partir dessa configuração o "passou/não passou" descrito na definição formal de quality gate (resultado binário, critério de entrada/saída) vira, de fato, bloqueante — antes disso é só um relatório que qualquer um pode ignorar.

## Quatro Técnicas Concretas Para Transformar a Lista de Uncle Bob em Gate de CI

[[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]] parte da mesma lista de métricas citada por [[wiki/entities/uncle-bob]] (cobertura, dependency structure, complexidade ciclomática, tamanho de módulo, mutation tests) e detalha quatro gates bloqueantes concretos, cada um capturando um tipo de degradação típica de código gerado por LLM:

1. **[[wiki/concepts/complexidade-ciclomatica|Complexidade ciclomática (CCN)]]** — limite de exemplo entre 1 e 20; captura a tendência de LLMs de escrever funções longas com muitos `if`s aninhados.
2. **Cobertura + [[wiki/concepts/teste-de-mutacao|mutation testing]]** — metas de exemplo citadas: 85% de cobertura + 60% de mutation score; captura testes que executam código sem validar comportamento.
3. **Tamanho de módulo/arquivo** — limite de exemplo de 300 linhas por arquivo; captura "god files" de 3.000 a 5.000 linhas.
4. **Estrutura de dependências (dependency structure)** — detecta import circular, camadas invertidas (controller chamando model direto) e módulo de implementação acessando outro módulo de implementação sem passar por um módulo de API exposto propositalmente; ver [[wiki/concepts/acoplamento]].

A fonte enquadra essas quatro técnicas como a resposta prática ao mesmo problema descrito em "Babysitting" e no exemplo de pipeline de CI acima: o volume de código gerado (a fonte cita ~10.000 linhas/dia) torna revisão manual linha a linha inviável, e a resposta não é abandonar qualidade, é mover o critério de aprovação para provas objetivas que rodam em segundos no CI, sem exigir leitura humana.

## O Gate Não Decide Sozinho *Quando* Confiar Nele

[[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]] adiciona a camada de decisão humana *acima* do gate: um gate verde é condição necessária mas não suficiente para dispensar leitura. A fonte propõe a [[wiki/concepts/matriz-risco-dificuldade-review-ia|matriz risco × dificuldade]] para decidir, PR a PR, se o resultado binário do gate basta (baixo risco → merge automático desde que haja teste), se exige amostragem (risco médio), ou se ainda precisa de revisão humana em pares (alto risco: auth, pagamentos, migração de banco). A mesma fonte relata o Quality Gate de [[wiki/entities/lucas-montano]] — [[wiki/concepts/ratchet-baseline|baseline]] congelada + agente em babysitting + revisor de IA lendo o `CLAUDE.md`/`review.md` do projeto — como instância prática desta página, ecoando [[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]].

## Clean Code Não Morreu, Migrou Para o Gate

[[wiki/sources/code-was-never-the-hard-part-reacao-lucas-montana]] contra-argumenta diretamente a tese de que "Clean Code virou irrelevante" com a IA escrevendo o código: o conhecimento de Clean Code não desapareceu, migrou de disciplina manual (escrever bem) para critério verificável automaticamente (microbenchmarks + análise estática determinística, tipo SonarQube, rodando em CI antes do merge). O ponto central da fonte: isso não é "IA revisando IA" — é o dev escrevendo o próprio gate que audita o que a IA produziu, o que ainda exige entender os princípios do livro pra saber o que codificar como regra.

## O Gate Como Condição de Parada de um Loop Noturno

[[wiki/sources/loop-engineering-guia-pratico-casos-reais-desastres-lucas-montano]] descreve o mesmo mecanismo aplicado a um [[wiki/concepts/loop-engineering|loop]] agêntico rodando sem supervisão em tempo real: o gate (testes passando, build sem erro, lint zerado, diff de print via Playwright) é o que decide, volta a volta, se o agente comita ou corrige — sem esse resultado binário e verificável, "o loop passa a noite inteira produzindo lixo com total confiança de que está indo bem". Critérios subjetivos como "deixa mais bonito" são explicitamente descartados como não verificáveis, reforçando a exigência de critério de entrada/saída explícito já documentada acima na visão de Schneider.

## Key Sources

- [[wiki/sources/code-was-never-the-hard-part-reacao-lucas-montana]] — Clean Code como fonte dos critérios codificados no gate, não como disciplina de quem escreve o código à mão
- [[wiki/sources/loop-engineering-guia-pratico-casos-reais-desastres-lucas-montano]] — gate como condição de parada verificável de um loop noturno sem supervisão
- [[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]]
- [[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]] — matriz risco × dificuldade como camada de decisão acima do gate; Quality Gate de Lucas Montano com baseline e babysitting
- [[wiki/sources/gate-de-qualidade-definicoes-formais]] — definições formais da literatura (checklist/aprovação por gate, milestone com critérios pré-definidos, ponto de verificação de Schneider) e características estruturais (critérios de entrada/saída, disparo por critério não por data, resultado binário, gates em paralelo)
- [[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] — padrão ratchet/baseline, babysitting de PR por agentes, pipeline de CI concreto (npm audit em dois níveis, jscpd para duplicação)
- [[wiki/sources/underengineering-overengineering-mario-souto]] — branch protection com required status checks como mecanismo mínimo de enforcement, sobre um pipeline de apenas lint + teste
- [[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]] — quatro gates concretos (CCN, cobertura+mutation, tamanho de módulo, dependency structure) para transformar a lista de métricas de Uncle Bob num pipeline de CI real
- [[wiki/sources/code-review-morreu-uncle-bob-push-force-prod-lucas-montano]] — "qualidade de código é mensurável, não subjetiva"; o quality gate no CD como o substituto que "já surgiu" para a revisão linha a linha (contra o "algo precisa surgir no lugar" de Gergely Orosz)
