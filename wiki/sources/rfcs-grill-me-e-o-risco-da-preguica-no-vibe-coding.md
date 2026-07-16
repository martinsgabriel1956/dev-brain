---
type: source
title: "RFCs, Grill Me e o Risco da Preguiça no Vibe Coding"
aliases: ["rfcs e grill me", "preguiça no vibe coding", "cdf cafe rfc grill me"]
date_created: 2026-07-16
date_updated: 2026-07-16
source_count: 0
tags: [tech-mentor-ai, rfc, grill-me, skills-agente, ddd, quality-gate, vibe-coding, code-review]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding.md
source_url: ""
author: "CDF Café (Código Fonte TV)"
date_published: ""
date_ingested: 2026-07-16
---

# RFCs, Grill Me e o Risco da Preguiça no Vibe Coding

## TL;DR

Episódio do CDF Café ([[wiki/entities/codigo-fonte-tv]]) argumentando que a compressão do ciclo planejamento→execução trazida pela IA elimina o tempo de reflexão que antes vinha "de graça" com a lentidão de codar manualmente, e que isso está fazendo devs pararem de revisar tanto o código gerado quanto as especificações do próprio produto. A saída defendida tem duas pernas: (1) RFCs como fonte da verdade que a IA segue para não alucinar arquitetura — com devs que rodam agentes autônomos gastando ~80% do tempo em RFC e 20% em execução — e especificações técnicas agnósticas à linguagem de programação (tese do Fabrício Arcanjo, focada em DDD e padrões, que permite transpilar a mesma arquitetura para Rust/.NET/Java/Go/TypeScript a partir de um único documento); (2) a skill **Grill Me** (Matt Pocock), que inverte quem revisa quem — a IA entrevista o dev sobre decisões de implementação até atingir entendimento mútuo, em vez do dev ler linha a linha o código gerado. Complementarmente, quality gates/linters com limites de tamanho de função/arquivo forçam a IA a modularizar (caso prático: o app code.persua.com). O autor é explícito sobre não gostar de escrever documentação e tratar a Grill Me como o hack que resolveu isso para ele.

## Key Claims

1. **A velocidade do ciclo planejamento→execução via IA elimina o tempo de reflexão que antes era gratuito** — no modelo cascata pré-IA, a lentidão de desenhar diagramas UML/DER e codificar manualmente forçava uma pausa reflexiva; hoje o dev vai do brainstorm com a IA à execução em minutos, e é fácil parar de revisar tanto o código gerado quanto as regras que a IA coloca no sistema ao longo de um loop autônomo.
2. **RFC (Request for Comments) é a fonte da verdade que evita que a IA alucine arquitetura** — sem uma RFC bem definida, o código gerado pode violar padrões da empresa; isso deveria ser reforçado por linter/análise estática/quality gate em pull request, não substituído por eles.
3. **Inversão de tempo: de codificação para planejamento** — devs que deixam agentes rodando de forma autônoma reportam gastar ~80% do tempo em RFCs e 20% em execução (citado como analogia ao princípio de Pareto), invertendo a proporção histórica onde a maior parte do tempo ia para codificação.
4. **A janela de revisão incremental desapareceu com o aumento do "effort" dos agentes** — antes (uso de Claude Code via CLI) o dev revisava e corrigia a IA passo a passo durante a geração; com harnesses que rodam por mais tempo, geram próprios testes automatizados e entram em loops longos, não sobra tempo para revisar tudo antes de concluir a tarefa — e ninguém quer trocar "escrever código" por "ler 10.000 linhas de código por dia" (paralelo ao "looking good to me" em pull requests).
5. **Especificações técnicas agnósticas à linguagem de programação** (tese de Fabrício Arcanjo, discutida no Stubborn Club) — documentar entradas/saídas rigorosamente em Markdown, focado em DDD e padrões, permite pedir a um agente de IA para implementar (ou "transpilar") a mesma arquitetura em linguagens diferentes (Rust, .NET, Java, Go, TypeScript) a partir de uma única especificação, reduzindo ambiguidade.
6. **Workforce multiagente por skills pequenas (<70 linhas), não prompt genérico** (relato de "Conrado" no Stubborn Club) — separar agentes por papel (dev, QA, PO) com skills curtas baseadas em especificações técnicas reduz a carga do agente coder (de ~15% para ~10% do trabalho total), porque outros quality gates (ex.: skill de QA) absorvem o restante.
7. **A skill Grill Me (Matt Pocock) inverte o sentido da revisão** — descrição original: entrevistar o usuário incansavelmente sobre um plano/design até alcançar entendimento compartilhado, resolvendo cada ramo da árvore de decisão. O autor adaptou o prompt para que a IA o questione especificamente sobre decisões de implementação relevantes ao domínio/regra de negócio (cada `if`/cláusula relevante gera uma pergunta), permitindo mover rápido sem ler linha a linha — é a IA que audita o entendimento do dev, não o contrário. Ver [[wiki/entities/matt-pocock]].
8. **Quality gates com limites estruturais (tamanho de função, linhas por arquivo, duplicação) forçam a IA a modularizar** — caso prático: o autor pediu para a IA modularizar o app **code.persua.com** ("sabor" do Persua para aprender system design/leetcode) via flavors, e limites de análise estática levaram a decisões concretas de build (desabilitar componentes/assets não usados por flavor, inspecionar o artefato final para verificar compliance com regras de modularização).
9. **Satya Nadella (Microsoft) descreveu um "paradoxo da informação invertida"** — entre os pontos citados: manter traces de como a informação e os problemas são encontrados, evals, "adapted weights" e "memory accumulates" como onde a organização constrói confiança entre capital humano e capital de tokens. O autor é explícito que uma RFC sozinha não garante evals nem quality gate, mas dá um norte e a oportunidade de conhecer o sistema sendo construído. Ver [[wiki/concepts/capital-de-tokens]].
10. **Nenhuma dessas práticas é vista como bala de prata** — o autor reforça, ao final, não haver "certo ou errado" definitivo: é experimentação coletiva em tempo real da comunidade (Stubborn Club) sobre como manter entendimento de projeto em escala de geração de código via IA.

## Entidades Mencionadas

- [[wiki/entities/codigo-fonte-tv]] — canal autor (segmento CDF Café)
- [[wiki/entities/matt-pocock]] — criador da skill Grill Me, citada e adaptada pelo autor
- [[wiki/entities/microsoft]] — Satya Nadella e o "paradoxo da informação invertida"
- [[wiki/entities/fabricio-arcanjo]] — defende especificações técnicas agnósticas à linguagem de programação, focadas em DDD e padrões

## Conceitos Tocados

- [[wiki/concepts/rfc-request-for-comments]]
- [[wiki/concepts/vibe-coding]]
- [[wiki/concepts/skills-agente]]
- [[wiki/concepts/ddd]]
- [[wiki/concepts/code-review]]
- [[wiki/concepts/capital-de-tokens]]
- [[wiki/concepts/quality-gate]]

## Open Questions

- "Stubborn Club" é grafado foneticamente na transcrição ("Studio Bottom Club" / "Stupan Club") — mantido como "Stubborn Club" por ser a leitura mais provável de um encontro quinzenal de compartilhamento de conhecimento entre devs, mas sem confirmação ortográfica de fonte primária.
- O sobrenome "Fabrício Arcanjo" e o relato atribuído a "Conrado" vêm de uma comunidade fechada (Stubborn Club) sem link público verificável — tratar as teses atribuídas a eles como relato de segunda mão do autor do vídeo, não como declaração pública citável diretamente.
- "Paradoxo da informação invertida" de Satya Nadella é citado de memória/segunda mão (post no Twitter mencionado, sem link capturado na transcrição) — mesma ressalva já registrada em [[wiki/sources/custo-real-ia-tokens-produtividade-demissoes]] sobre citações de Nadella nesta wiki.
- "Sala da vida" e "efforts" dos agentes são termos usados de forma solta na transcrição (provavelmente "thinking mode"/reasoning effort de modelos como o Claude) — mantidos próximos ao original por não haver confirmação de qual produto/feature específica o autor tinha em mente.
- Não há confirmação se "code.persua.com" e o app "Persua" têm página própria nesta wiki — não foi encontrada entidade equivalente; tratar como produto do próprio autor do canal, sem página dedicada por ora (baixa relevância fora deste contexto específico de modularização por flavor).

## Raw Quotes

> "Sem uma RFC bem definida, o código que a IA gera pode violar a tua arquitetura ou qualquer outro requisito."

> "O que eu tenho ouvido de programadores que conseguem deixar a IA rodando de forma autônoma é que eles estão gastando cerca de 80% do tempo deles em RFCs e 20% na execução."

> "Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree." — descrição original da skill Grill Me, de Matt Pocock

> "Eu consigo agora ir rápido, mover rápido, e ao invés de eu revisar toda linha de código da IA, a IA meio que revisa o meu entendimento sobre o código que ela tá gerando."

> "É assim que tu consegue gerar 10.000 linhas de código por dia — mas tu não pode só ter agentes pra revisar, só ter agentes pra testar, só ter linter [...] se tu deixar o entendimento do teu próprio projeto ir por água abaixo."
