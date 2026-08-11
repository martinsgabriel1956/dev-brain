---
type: source
title: "Vibe Coding de Jogos: 1 Prompt vs. 8, e os Estágios de um Produto"
aliases: ["por que uns vibe codam em um prompt", "snowboarder test opus 5", "estagios de maturidade de produto", "jogo de golfe chatgpt agente"]
date_created: 2026-08-11
date_updated: 2026-08-11
source_count: 0
tags: [vibe-coding, prompt-engineering, loop-engineering, agente-ia, mvp, ltv-cac, canais-de-distribuicao, produto, jogos, unreal-engine]
skill: tech-mentor-ai
status: stable
source_file: "raw/vibe-coding-jogos-um-prompt-vs-varios-estagios-produto.md"
source_url: ""
author: "desconhecido (vídeo YouTube, criador brasileiro — Stupid Button Club)"
date_published: ""
date_ingested: "2026-08-11"
---

## TL;DR

Por que alguns vibe codam um jogo em 1 prompt e outros em 8? Testando os dois casos virais (snowboarder test em one-shot com Opus 5/Fable 5 vs. jogo de golfe do ThePrimeagen em 8 prompts e ~72M tokens), o autor replica ele mesmo um MVP de golfe no modo agente do ChatGPT com Unreal Engine, em 3 prompts. A conclusão é que a diferença não é o modelo nem sorte: é **conhecimento do domínio + bom senso no prompt + colocar o agente em loop** (o "único prompt" na prática vira 20-30 iterações de teste end-to-end até o resultado). Na segunda metade, apresenta um framework de **estágios de maturidade de produto** (0 a 5) e argumenta que o gargalo da maioria dos fundadores não é técnica, é definição de produto e domínio de canais de distribuição / unit economics.

---

## Reivindicações Principais

**Claim:** A diferença entre entregar um jogo jogável em 1 prompt e em 8 não é o modelo, é conhecimento do domínio + bom senso no prompt (incluindo fornecer assets/referências).
**Evidência:** O autor replicou um MVP de golfe em 3 prompts e argumenta que teria sido 1 se tivesse fornecido os assets — supõe que o jogo de referência que viralizou usou imagens/referências fornecidas, enquanto no dele o modelo gerou o visual mais básico com componentes padrão.
**Confiança:** Média — argumento plausível e coerente com [[wiki/concepts/prompt-engineering]], mas baseado em inferência sobre o setup alheio, não em comparação controlada.

**Claim:** Um "único prompt" bem feito na prática vira 20-30 prompts: o agente faz teste end-to-end, verifica se o jogo funciona e itera até o resultado final.
**Evidência:** No experimento, o agente do ChatGPT escreveu o próprio script para rodar o jogo no Mac e testou sozinho; o autor nem contou "rodar o jogo" como prompt separado.
**Confiança:** Alta — consistente com [[wiki/concepts/loop-engineering]] (loop goal-based / criador) e [[wiki/concepts/autonomy-slider]].

**Claim:** Dar full access ao computador para o agente funciona, mas ainda exige intervenção humana em pontos triviais.
**Evidência:** O agente travou por falta de Git/repositório, precisou que o autor rodasse `git init`, e exigiu criação/login manual de conta na Epic Games para rodar a Unreal Engine. O modo voz ("Mega Brain") foi abandonado por lentidão.
**Confiança:** Alta — relato direto de execução (não verificável externamente, mas detalhado).

**Claim:** O agente projetou uma integração jogo↔celular com postura de segurança razoável por padrão, mesmo sem ser pedido explicitamente.
**Evidência:** Servidor HTTPS temporário local no Mac, UDP só em localhost direto para a Unreal (nenhuma porta do jogo aberta na rede), descarte de pacotes inválidos, token de sessão aleatório por execução embutido no QR code, validação no Node e não gravação de telemetria; o iPhone controlou a bola via acelerômetro pelo Safari.
**Confiança:** Média-alta como relato; contrasta com o padrão documentado de que "segurança nunca é padrão" em código de IA (ver [[wiki/concepts/vibe-coding]]) — vale registrar como contraexemplo pontual, não como refutação.

**Claim:** O gargalo da maioria dos fundadores não é técnica — é definição de produto e de "estar pronto".
**Evidência:** Enquete própria com >1000 techfounders brasileiros: 67% não colocaram produto no ar, 31% faturam <R$5.000, 1,7% passaram de R$5.000. O autor propõe um framework de estágios 0-5.
**Confiança:** Média — o diagnóstico é opinião embasada em enquete não metodologicamente descrita; os números são autorreportados.

**Claim:** Passar de R$5.000 para R$50.000/mês é essencialmente reinvestir mantendo o CAC baixo enquanto se aumentam leads frios; o gap entre estágio 4 e 5 é de distribuição/unit economics, não de produto.
**Evidência:** Argumento sobre CAC/LTV; exemplo de terceiro (Antônio/Real Oficial) gastando ~R$100k/mês em ads no cartão pessoal como caso de "fórmula já achada".
**Confiança:** Média — raciocínio de unit economics correto em tese (ver [[wiki/concepts/ltv-cac]]); exemplo é anedótico e de segunda mão.

**Claim:** A demanda por software está aumentando apesar da IA, e serviço está virando produto.
**Evidência:** Pessoas fora de TI vibe codam soluções que continuam sendo código (scripts Python/JS); software houses empacotam orquestração de agentes e vendem como serviço (analogia ao boom dos sites locais nos anos 2000).
**Confiança:** Média — tendência plausível e alinhada a [[wiki/concepts/visao-de-negocio-do-desenvolvedor]], sem dados de mercado citados.

---

## Conceitos

- [[wiki/concepts/vibe-coding]] — o tema central; caso concreto de vibe coding de jogo com agente autônomo
- [[wiki/concepts/prompt-engineering]] — a tese "a diferença é o prompt + fornecer assets", não o modelo
- [[wiki/concepts/loop-engineering]] — "1 prompt vira 20-30" via teste end-to-end e iteração autônoma
- [[wiki/concepts/autonomy-slider]] — full access ao computador como ponto extremo de delegação
- [[wiki/concepts/agente-ia]] — modo agente do ChatGPT executando setup, instalação e testes sozinho
- [[wiki/concepts/agent-containment]] — a integração com o celular como exemplo de superfície de rede minimizada (UDP localhost, token por QR, descarte de pacotes)
- [[wiki/concepts/mvp]] — o jogo de golfe como MVP jogável construído por vibe coding
- [[wiki/concepts/ltv-cac]] — o gap entre estágios 4 e 5 é unit economics: manter CAC baixo com leads frios
- [[wiki/concepts/canais-de-distribuicao]] — recorrência (estágio 3) depende de identificar canais (YouTube, Instagram, SEO, afiliados)
- [[wiki/concepts/estagios-de-maturidade-de-produto]] — o framework 0-5 apresentado
- [[wiki/concepts/visao-de-negocio-do-desenvolvedor]] — serviço virando produto; demanda por software crescendo com a IA

## Entidades

- [[wiki/entities/openai]] — ChatGPT (modo agente + voice mode "Mega Brain") como ferramenta do experimento
- [[wiki/entities/anthropic]] — Opus 5 / Fable 5 citados nos casos virais (snowboarder test, one-shot)
- [[wiki/entities/the-primeagen]] — criou o jogo de golfe com Opus 5 em 8 prompts / ~72M tokens
- [[wiki/entities/unreal-engine]] — engine usada para construir o jogo de golfe

## Ver também

- [[wiki/sources/vibe-coding-limites-maturidade-profissional]] — onde vibe coding brilha (MVP/protótipo) vs. onde exige julgamento; complementa a fronteira aqui
- [[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]] — "Sol" (GPT) e "Fable" como modelos/apelidos citados; contexto de custo/velocidade
- [[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]] — loop de agente aplicado a construção de jogo, mesmo padrão de iteração

---

## Perguntas Abertas

- Quanto custaria via API o mesmo experimento que consumiu ~5% do limite semanal da subscription do ChatGPT? (O autor deixa o cálculo em aberto para os espectadores.)
- O "one-shot" viral (snowboarder test) foi genuíno ou dependeu de assets/referências fornecidos que não aparecem no relato? A comparação 1-prompt vs. 8-prompts é justa sem controlar o setup?
- A boa postura de segurança do agente na integração com o celular é comportamento consistente do modelo ou sorte pontual? Contradiz o padrão "segurança nunca é padrão" registrado em [[wiki/concepts/vibe-coding]]?

---

## Citações

> "Aquele teu único prompt, na verdade, vira 20, 30 prompts, porque o modelo vai fazer teste end-to-end, vai verificar se o jogo tá funcionando e vai ficar iterando até chegar no resultado final."

> "Depende muito do conhecimento que tu tem sobre criar jogos. (...) O que importa mesmo é tu colocar ele em loop."

> "Não é falta de técnica — é falta de definição do teu produto, do que é ele estar pronto."

> "O que te impede de chegar num valor maior recorrente é manter o CAC baixo enquanto tu aumenta os leads frios entrando na tua plataforma."

> "A demanda por software, por incrível que pareça, tá aumentando."
