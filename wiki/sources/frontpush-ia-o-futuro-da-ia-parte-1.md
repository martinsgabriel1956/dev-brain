---
type: source
title: "FrontPUSH, módulo de IA: o futuro da IA, parte 1 (aula 5)"
aliases: ["o futuro da IA FrontPUSH", "time verde e time laranja", "IA vai virar Netflix", "não falta dinheiro, falta recurso", "módulo de IA FrontPUSH aula 5"]
date_created: 2026-11-27
date_updated: 2026-11-27
source_count: 0
tags: [mercado-de-ia, anthropic, openai, google, modelo-de-negocio, ipo, subsidio, enshittification, scaling-laws, energia, chips, terras-raras, hype, ia]
skill: tech-mentor-ai
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-ia-o-futuro-da-ia-parte-1.md"
source_url: ""
author: "Násser"
date_published: "2026-07 (gravação, segundo o autor)"
date_ingested: 2026-11-27
---

# FrontPUSH, módulo de IA: o futuro da IA, parte 1 (aula 5)

## TL;DR

"Bate-papo" de cerca de 25 min do módulo de IA do [[wiki/entities/frontpush|FrontPUSH]], gravado "no início de julho de 2026", com um slide ("O futuro da IA pt.1"). Continua [[wiki/sources/frontpush-ia-como-dar-comandos-na-ia-da-forma-correta]]. [[wiki/entities/nasser|Násser]] sustenta quatro teses:

- **Empresas.** Para código, são "o time verde e o time laranja": [[wiki/entities/openai|OpenAI]] (GPT, [[wiki/entities/codex-openai|Codex]]) e [[wiki/entities/anthropic|Anthropic]] ([[wiki/entities/claude-code|Claude Code]]). A Anthropic estaria à frente por ter acertado o B2B desde o início. O [[wiki/entities/google|Google]] "deu uma moscada", mas aguenta perder dinheiro e oferece a API de melhor custo-benefício.
- **Narrativas.** Sem IPO, as duas vivem de investidor, operam em prejuízo para formar base de clientes e depois vão "aumentar". Vai acontecer "o que já aconteceu com a [[wiki/entities/netflix|Netflix]]": preço maior, planos piores, propaganda ([[wiki/concepts/enshittification]], [[wiki/concepts/corrida-preco-qualidade-llm]]). Slide: "Aproveite, tudo vai ficar mais caro".
- **Custo × energia.** A curva de resultado por parâmetro "começou a deitar" ("Curva de energia x parâmetros: já chegou no limite"), e a corrida agora é "a melhora dos modelos" ([[wiki/concepts/scaling-laws]]). "Não falta dinheiro, falta recurso": chips, RAM, energia, água e "terras raras".
- **Paradigma.** A IA "não vai morrer mais"; é "uma quebra de paradigma que nem a internet" ([[wiki/concepts/hype-de-ia]]).

Problemas futuros no slide: "idiotização das pessoas" ([[wiki/concepts/atrofia-cognitiva]]), "não há recursos pra tankar todo mundo" e "gasto absurdo de energia". A análise de mercado é opinião declarada ("é a minha experiência"). As precisões principais: terras raras não são silício, cobre nem ouro, e o gargalo dos chips está em fábrica, encapsulamento, memória HBM e energia. O platô é do pré-treino, não do progresso. A previsão "tudo vai ficar mais caro" convive com a queda do preço por token. Ver Contradições.

## Key Claims

### Contexto e recap

- "Estou gravando no início de julho de 2026 [...] é muito provável que tudo isso aqui tenha mudado." É "a última aula para a gente bater esse papo" antes de "demonstrar 100% o meu workflow".
- A IA ficou disruptiva ao juntar os oito conceitos da [[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia|parte 1]]: "pegar o Deep Learning e avançar para transformers e LLM". "Esses conceitos já existiam."
- Barreiras atuais: "quantidade de dados, quantidade de parâmetros, escala computacional e a energia", além de "uma barreira tecnológica". A IA anda "a passos cavalários" porque "são injetados bilhões de dólares todos os dias".

### As empresas de IA (slide: Anthropic, OpenAI, Google)

- "Time verde e time laranja, escolha seu lado": Anthropic "com o Claude Code, todos os Claudes" e OpenAI "com o GPT e o Codex". O Google aparece "para explicar um pouquinho do contexto", com o Gemini (chatbot) e o [[wiki/entities/nano-banana-pro|Nano Banana Pro]] (imagem).
- **OpenAI:** "deu o ponto de partida" e tem "a maior quantidade de usuários"; ChatGPT é a "primeira referência" de IA para leigos. "Principal erro [...] na minha opinião": "não acertou muito na metodologia de negócio" e "foi acertar, mais ou menos, o modelo de negócio muito recentemente". O único salto teria sido o GPT-4; "do outro 5 foram marginais ou até pioras". Também tentou o Sora e outras vertentes sem acertar no B2B.
- **Anthropic:** "desde o início, construir algo B2B", e o carro-chefe é o Claude Code. "Eu vejo que as empresas têm uma preferência maior em contratar o Claude Code." A OpenAI "vem correndo atrás".
- **Na prática (dele):** prefere o Claude Code em projetos complexos, "mais disciplinado, ele se perde menos". Usa mais o Codex por ser mais barato ("ganhei uma assinatura do ChatGPT"). Como trabalha "mais seccionado", "não percebi enormes diferenças" ([[wiki/concepts/decomposicao-de-problemas]]).

### As narrativas de IA (slide: IPO, base de clientes, operar em prejuízo)

- "Nenhuma delas está em IPO [...] no momento da gravação"; "elas vivem de dinheiro de investidor", e por isso Claude Code, GPT e Codex "são mais acessíveis" e "até lascando com nós desenvolvedores" e com designers de toda espécie, porque os agentes "com um bom modelo do que é o harness" avançam ([[wiki/concepts/harness]]).
- Para o IPO é preciso "prometer lucro" e "perenidade", com "um modelo de negócio bem estabelecido": assinatura. Primeiro o serviço sai barato, "muitas das vezes operando em prejuízo", para "formar uma base de clientes", porque o cliente fidelizado "tende a permanecer" ([[wiki/concepts/lock-in-vendor-ia]]).
- **Analogia da internet de casa:** a fibra da Oi "era bala"; depois da venda, "acho que o nome da empresa é Nio", o upload piorou e ele precisa do 5G para usar o app do banco. Só agora pensa em trocar, porque "a não ser que a empresa me decepcione muito", ninguém troca. Com a Anthropic e a OpenAI, ao adotar um workflow, é "similar".
- **A Netflix:** assinatura mais cara, serviço pior, mais planos, os baratos "com propaganda", limite de dispositivos e de qualidade ("só em 1080p, não pode 4K"), "só dispositivos móveis". "Isso tudo vai acontecer com o OpenAI e com o Anthropic" ([[wiki/concepts/enshittification]]).
- "Quando passar um pouco essa onda [...] um dia vai chegar."

### Custo × energia (slide)

- "Quanto mais você aumenta os parâmetros [...] maior é o resultado", mas também o consumo: "energia", "componentes eletrônicos", "capacidade de resfriamento". A curva "começou a deitar": "eles já chegaram mais ou menos em um platô com relação à quantidade de parâmetros" ([[wiki/concepts/scaling-laws]]).
- As empresas bilionárias compram na TSMC, e "tudo aumentou": "a crise da memória RAM", "a crise das placas de vídeo, que nunca mais baixou de preço"; a [[wiki/entities/nvidia|Nvidia]] "cortou o chip [...] e está vendendo mais caro" ([[wiki/concepts/memoria-ram]], [[wiki/concepts/gpu]]).
- Nova corrida: "a melhora dos modelos", não "aplicar mais parâmetros".
- "Não falta dinheiro, falta recurso": "cobre, ouro, prata, silício" e, para extraí-los, "terras raras", em que "a China está voando, se não me engano é a maior". Ele avisa: "eu tenho que até estudar essa parte". Há limite também de energia e de água para resfriar os data centers. Dados prometidos para a parte 2.

### Google

- "Poderia ter saído na frente da OpenAI, o Google deu uma moscada." A lógica do IPO "não se aplica muito": com "outros N braços" de receita, perder dinheiro com IA "não faz muitíssima diferença".
- Por isso, "é a que oferece melhor custo-benefício com relação a sua API", boa para "um startup, fazer um SaaS". O Nano Banana Pro seria melhor "para algumas aplicações".
- "Não sou o Jedi [...] todo dia lança uma inteligência artificial nova"; o fluxo dele vem nas próximas aulas, "mas pode ter outra ferramenta melhor" ([[wiki/concepts/apego-a-ferramentas]]).

### Problemas futuros (slide)

- "Idiotização das pessoas", "Não há recursos pra tankar todo mundo", "Gasto absurdo de energia". Ficam para a parte 2.
- Slide: "A IA foi uma quebra de paradigma que nem a internet. Aprenda sobre, nunca vai voltar atrás."

## Contradições e precisões

- **Terras raras ≠ cobre, ouro, prata e silício.** Terras raras são 17 elementos (neodímio, disprósio etc.), usados sobretudo em ímãs e em quantidades pequenas em semicondutores. O silício vem da areia de quartzo; cobre, ouro e prata são metais comuns de mineração. O gargalo de hardware para IA em 2025–2026 está na capacidade de fábrica e de encapsulamento avançado (CoWoS da TSMC), na memória HBM, que puxou a alta de preço da DRAM, e na energia elétrica, não nas terras raras. A China domina mesmo as terras raras: cerca de 60–70% da mineração e cerca de 90% do refino. [external] IEA, Global Critical Minerals Outlook, https://www.iea.org/reports/global-critical-minerals-outlook-2024. Ver também [[wiki/concepts/export-controls-chips-ia]]. Confiança alta no conceito, média-alta nos percentuais (sem fetch).
- **O platô é do pré-treino, não do progresso.** O retorno decrescente de escalar parâmetros e dados no pré-treino é amplamente reconhecido (Sutskever, NeurIPS 2024: "pre-training as we know it will end"). O ganho migrou para pós-treino com reforço e computação na inferência (modelos de raciocínio), o que bate com "a melhora dos modelos". As [[wiki/concepts/scaling-laws]] descrevem lei de potência (retorno decrescente), não um teto. "Já chegou no limite" é forte demais. Confiança média-alta.
- **"Tudo vai ficar mais caro" × preço por token.** O preço para uma capacidade fixa caiu cerca de 10x ao ano (LLMflation, a16z), e os planos atuais são subsidiados, como a aula diz. As duas coisas podem ser verdade: preço unitário caindo e conta subindo com mais uso, agentes e fim do subsídio. A analogia com a Netflix é plausível, mas é previsão. Ver [[wiki/concepts/corrida-preco-qualidade-llm]] e o registro da [[wiki/sources/frontpush-ia-como-dar-comandos-na-ia-da-forma-correta|parte 4]]. Confiança média.
- **Anthropic à frente no B2B.** Há evidência a favor: em meados de 2025, a Menlo Ventures estimou a fatia da Anthropic no uso empresarial de LLM via API em cerca de 32%, contra cerca de 25% da OpenAI. Já a OpenAI lidera com folga em usuários do consumidor (cerca de 800 milhões semanais em out. 2025). [external] https://menlovc.com/perspective/2025-mid-year-llm-market-update/. Confiança média-alta (sem fetch). "GPT-5 marginal ou pior" é opinião; a recepção do lançamento (ago. 2025) foi mista.
- **"O Google deu uma moscada".** O Transformer saiu do Google ("Attention Is All You Need", 2017; ver [[wiki/entities/google]]), e o Google não lançou um chatbot antes do ChatGPT. Isso sustenta a frase. Confiança alta.
- **Tensão com a aula de mídia.** Em [[wiki/sources/frontpush-ia-como-eu-crio-imagens-e-videos-com-ia]], ele disse "essa bolha está prestes a estourar". Aqui, a IA "não vai morrer mais", só a "onda" de investimento vai passar. As duas cabem juntas: bolha financeira com tecnologia que fica, como na internet pós-2000 ([[wiki/concepts/hype-de-ia]]). Confiança média (interpretação).
- **Netflix.** O plano com anúncios (2022), o fim do compartilhamento gratuito (2023) e o fim do plano básico sem anúncios em vários mercados conferem. O plano só para celular existe em alguns países. Confiança alta.
- **Oi → Nio.** A fibra da Oi foi vendida à V.tal e opera como Nio desde 2024–2025. Confiança média-alta.
- **Lapsos literais no raw:** "a passos cavalários", "ela tirou para vários lados" (provável "atirou"), "do outro 5", "correndo atrás do Boi", "a Anthropic, que é OpenAI" e "a Anthropic da OpenAI" (4×, provável "Anthropic e OpenAI"), "a Nvidia cortou o chip" (não identificado), "uma empresa pessoal, não é uma ONG", "não sou o Jedi". Há duas lacunas de ~10 s na legenda (00:12:29 e 00:22:32).

## Entities

- [[wiki/entities/nasser]]: instrutor.
- [[wiki/entities/frontpush]]: curso, módulo de IA.
- [[wiki/entities/anthropic]], [[wiki/entities/claude-code]]: "time laranja", B2B.
- [[wiki/entities/openai]], [[wiki/entities/codex-openai]]: "time verde", consumidor.
- [[wiki/entities/google]], [[wiki/entities/nano-banana-pro]]: a "moscada" e a API barata.
- [[wiki/entities/netflix]]: o modelo de encarecimento.
- [[wiki/entities/nvidia]]: GPUs mais caras.

## Concepts

- [[wiki/concepts/enshittification]] (novo), [[wiki/concepts/corrida-preco-qualidade-llm]], [[wiki/concepts/lock-in-vendor-ia]]
- [[wiki/concepts/scaling-laws]], [[wiki/concepts/gpu]], [[wiki/concepts/memoria-ram]], [[wiki/concepts/export-controls-chips-ia]]
- [[wiki/concepts/hype-de-ia]], [[wiki/concepts/atrofia-cognitiva]], [[wiki/concepts/apego-a-ferramentas]]
- [[wiki/concepts/harness]], [[wiki/concepts/decomposicao-de-problemas]]

## Open Questions

- A parte 2 vai trazer os dados prometidos (curva de energia, consumo de água)? E a "idiotização das pessoas"?
- O que significa "a Nvidia cortou o chip"? Corte de oferta de GPUs de consumo, versão reduzida para a China ou outra coisa?
- Até a data do ingest (nov. 2026), alguma das duas fez IPO? A wiki não registra.

## Raw Quotes

- "Eu diria que é o time verde e o time laranja, escolha seu lado."
- "O que vai acontecer com a Anthropic, que é OpenAI, com relações de inteligência artificial, é o que já aconteceu com a Netflix."
- "Não falta dinheiro, pessoal, entenda isso, não falta dinheiro, falta recurso."
- "A Inteligência Artificial, como a gente conhece hoje, ela não vai morrer mais."
- "O Google deu uma moscada."
