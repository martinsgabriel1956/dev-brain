---
type: source
title: "FrontPUSH, módulo de IA: como dar comandos na IA da forma correta? (parte 4)"
aliases: ["como dar comandos na IA FrontPUSH", "como usar a IA FrontPUSH", "foto RAW e JPEG do contexto", "não copie prompts", "módulo de IA FrontPUSH aula teórica 4"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_count: 0
tags: [prompt-engineering, contexto, janela-de-contexto, degradacao-de-contexto, alucinacao, decomposicao, code-review, custo-de-llm, claude-code, codex, fundamentos, ia]
skill: tech-mentor-ai
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-ia-como-dar-comandos-na-ia-da-forma-correta.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-25
---

# FrontPUSH, módulo de IA: como dar comandos na IA da forma correta? (parte 4)

## TL;DR

Quarta aula teórica, "uma das últimas", do módulo de IA do [[wiki/entities/frontpush|FrontPUSH]]. Tem cerca de 17,5 min e um slide ("Como usar a IA? Conceitos importantes"). Continua [[wiki/sources/frontpush-ia-o-que-acontece-no-backstage-da-ia]]. A tese de [[wiki/entities/nasser|Násser]] é que "o resultado da inteligência artificial é o reflexo daquilo que você sabe". Por isso ele não copia prompts ([[wiki/concepts/copiador-de-prompt]]): dá um contexto técnico, específico e curto, porque parâmetro faltando vira [[wiki/concepts/alucinacao-llm|alucinação]] ([[wiki/concepts/ia-como-amplificador]], [[wiki/concepts/especialista-leva-vantagem-com-ia]]). Chats longos "se perdem" ([[wiki/concepts/degradacao-de-contexto]]), então é melhor dar "pequenos contextos" e abrir outro chat quando a IA sai do funil. A cada prompt, "o resumo perde informação, que nem comprimir uma foto": uma foto RAW de 6K (70 MB) vira um JPEG (15 MB) ([[wiki/concepts/context-compaction]]). O código deve ser montado "como peças de Lego" ([[wiki/concepts/decomposicao-de-problemas]]). Anthropic (Claude) e OpenAI (Codex) são "os dois principais times" para programar e, como "empresa não é ONG", o contexto custa e "cada vez vai ficar mais caro". De "três PR" para "40" pressiona o [[wiki/concepts/code-review]]. A aula confunde de novo **parâmetros** (pesos do modelo) com **especificações do prompt** e com contexto. Também se contradiz ao pedir "pequenos contextos [...] passo a passo, mais seccionado" e, no fim, "de uma vez só, não ficar estendendo nem picando". Ver Contradições.

## Key Claims

### O resultado reflete quem pede

- "Pessoal antes me perguntava muito no Instagram, qual foi o prompt que você usou?". Quem copiou não chegou ao resultado "porque você não soube definir minimamente o contexto". Ele diz: "eu não [...] copio e colo prompt mais de lugar nenhum" ([[wiki/concepts/copiador-de-prompt]]).
- "O resultado da inteligência artificial é o reflexo daquilo que você sabe." Sem o parâmetro específico, "ela vai tentar supor, você deve estar utilizando isso, mas você também pode estar utilizando aquilo" e "começar a inventar" ([[wiki/concepts/ia-como-amplificador]], [[wiki/concepts/prompt-vago-vs-prompt-especifico-demais]]).
- "Aqui a gente começa a separar os homens dos meninos." Por isso a IA "não é uma ferramenta que vai tomar o emprego de todo mundo": é preciso definir o que se quer "da maneira mais técnica e específica possível, porque você trabalha de maneira específica" ([[wiki/concepts/especialista-leva-vantagem-com-ia]]). Sem dizer o jeito e a metodologia usados, a IA alucina e "você vai estragar todo o código posterior".

### Chats longos e pequenos contextos

- Um amigo foi somando "mais contexto, mais parâmetro" até que, no fim do chat do Claude Code ou do Codex, a IA "começou a escrever um monte de negócio que não tinha nada a ver". Ele "ganhou velocidade [...] de uma maneira mentirosa" e preferiu "começar do zero de novo" a limpar tudo ([[wiki/concepts/degradacao-de-contexto]]).
- "Eu prefiro muito mais dar pequenos contextos para poder resolver um determinado problema [...] não estender demais." "Use a menor quantidade de prompt possível." Se a IA "não está sendo um funil", abra outro prompt ou outro chat e "tenta deixar o mais mastigado possível".

### Conceitos importantes (slide)

- "Parâmetros: define recurso computacional, não é infinito." "Contexto: também é limitado e vai ser sempre resumido." ([[wiki/concepts/janela-de-contexto]], [[wiki/concepts/context-compaction]])
- "O melhor jeito é pensar no código como peças de lego." "Se eu pedir pra montar, a IA se perde. Ela não cria, ela replica coisa que existe na internet." ([[wiki/concepts/decomposicao-de-problemas]], [[wiki/concepts/ia-generativa]])
- "Harness e modelos: Melhores para programação é o Claude e Codex." ([[wiki/entities/anthropic]], [[wiki/entities/claude-code]], [[wiki/entities/openai]], [[wiki/entities/codex-openai]])
- "Quando vamos programar, arquitetura de software estoura parâmetros e contexto."
- "Como dar contexto, tentar ser o mais claro, objetivo possível e de uma vez só. A cada prompt, resume e perde informação. Que nem comprimir uma foto." "Foto 6k RAW (70MB) >> JPEG Alta qualidade (15MB)."

### Empresas, custo e tradução

- Anthropic ("dona da Claude Code") e OpenAI ("dona do ChatGPT, do Codex") são "as duas principais hoje quando a gente fala de programação"; há "outras milhões", mas para contextos mais específicos.
- "Empresa não é ONG": há gasto com recursos, pessoal e gestão, e o serviço "precisa ter um retorno". O mercado fica para as próximas aulas ([[wiki/concepts/corrida-preco-qualidade-llm]]).
- A LLM "aglutina" o que você fala "como se fosse um mapa mental" em tokens, "como se fosse uma tradução": "quanto maior é essa conversa, maior é a tradução, mais informação é perdida". Na tradução simultânea para o chinês, "se eu falar demais", talvez chegue "com 80% de precisão".

### A foto RAW e o JPEG

- Uma foto 6K em RAW tem "de 70, de 50, a 100 MB", com "várias camadas para poder editar", "uma determinada camada de vermelho, de verde e de azul", curvas de cor e uma aparência "mais lavada". Ele avisa: "eu também posso estar errando porque eu não sou um fotógrafo profissional".
- "Quando a gente está passando para a IA, ela vai transformar para um JPEG [...] você perde todas as informações"; "toda a tradução implica nessa perca de qualidade". Mesmo um programador, com contexto "concisa, clara e concreta e simples", "tem perda, imagina quando não se tem".

### Peças de Lego

- Contraexemplo: no Codex, "eu quero uma landing page que faça conversão [...] para uma empresa de engenharia que está começando agora [...] faz aí para mim". Sem tecnologia, sem como vai rodar, com "muito parâmetro vazio", a IA "vai ter que supor e vai alucinar". O melhor é "mais passo a passo, mais seccionado e explicando cada parte".
- "Toda empresa tem o seu contexto": metodologia e "o que ela fez ou deixou de fazer, por quê". Quem tem de passar isso à IA é você, "de maneira técnica e o mais curta possível".
- "Antes [...] tinha três PR, hoje tem 40, como é que vai ficar o code review disso?" ([[wiki/concepts/code-review]], [[wiki/concepts/gargalo]]).

### Fecho

- "Quem fica [...] extremamente dependente de prompt são pessoas que realmente não sabem mexer com Inteligência Artificial." No máximo, pergunte a quem escreveu "como é que você descreveu, o que é importante falar".
- Sem essa noção, "muito provavelmente você vai ter retrabalho [...] falha de segurança" ([[wiki/concepts/degradacao-de-seguranca-iterativa-ia]]).
- "Não tem como ter contexto ilimitado e cada vez vai ficar mais caro." A prática vem com o "meu workflow" nas próximas aulas.

## Contradições e precisões

- **Dois sentidos de "parâmetro".** Na fala, "parâmetro" é ora o detalhe que falta no prompt ("muito parâmetro vazio", "deu os parâmetros corretos"), ora o limite do modelo ("ele tem limite de parâmetros", "define recurso computacional", "arquitetura de software estoura parâmetros"). No sentido técnico usado na [[wiki/sources/frontpush-ia-o-que-sao-as-llms|parte 2]] (pilar 4), parâmetros são os pesos fixos do modelo, e um prompt não os "estoura". O que estoura é a [[wiki/concepts/janela-de-contexto]]. O primeiro sentido equivale a especificação ou restrição do pedido. Confiança alta.
- **"Pequenos contextos" × "de uma vez só".** O slide e o fecho pedem "de uma vez só, não ficar estendendo nem picando"; o meio da aula pede "pequenos contextos" e "mais passo a passo, mais seccionado". A conciliação provável: tarefas pequenas (Lego), cada uma com o contexto completo num prompt só, em chats curtos. A aula não diz isso. Confiança média (interpretação).
- **"Contexto vai ser sempre resumido" / "a cada prompt, resume".** O resumo (compactação) acontece quando o harness se aproxima do limite, não a cada mensagem. Antes disso, a perda é de *atenção* em contextos longos ([[wiki/concepts/degradacao-de-contexto]]), não de compressão. A analogia RAW → JPEG descreve bem a compactação, mas não cada prompt ([[wiki/concepts/context-compaction]]). Confiança alta.
- **RAW não tem "camadas de vermelho, verde e azul".** O RAW guarda a leitura do sensor sob o filtro de Bayer, com um valor de cor por fotosito e mais bits (12 a 14) do que o JPEG (8). As cores RGB completas só surgem no *demosaicing*. A aparência "lavada" vem do perfil plano, não de falta de dados. Os tamanhos (50 a 100 MB em RAW, ~15 MB em JPEG de alta qualidade) são plausíveis para sensores de 45 a 60 MP. O autor já tinha avisado que podia errar. Confiança média-alta.
- **"Ela não cria, ela replica coisa que existe na internet" (slide).** É uma simplificação: modelos generalizam e recombinam padrões, e também podem memorizar trechos. Não são uma busca na internet ([[wiki/concepts/ia-generativa]]). Confiança alta.
- **"Cada vez vai ficar mais caro".** O preço por token para uma capacidade fixa tem caído rapidamente (cerca de 10x por ano, na estimativa da a16z). O que pode subir é o gasto total (mais tokens, agentes, modelos de raciocínio) e o preço dos modelos de ponta. [external] https://a16z.com/llmflation-llm-inference-cost/. Ver [[wiki/concepts/corrida-preco-qualidade-llm]]. Confiança média-alta.
- **"Os dois principais times".** Claude e Codex lideram benchmarks de código como o SWE-bench em 2025–2026, mas Gemini e modelos abertos (Qwen, DeepSeek, Kimi) estão perto. É opinião de mercado, não um fato fixo. Confiança média.
- **Lapsos literais no raw:** "Eu não colo copio e colo prompt", "a dona da Claude Code", "outras milhões de inteligentes artificiais", "perca de qualidade", "Mega brain" (nome ou chamamento no Codex, não identificado), "Claude, Codex cada vez mais melhore", "não mais é isso".

## Entities

- [[wiki/entities/nasser]]: instrutor.
- [[wiki/entities/frontpush]]: curso, módulo de IA.
- [[wiki/entities/anthropic]], [[wiki/entities/claude-code]]: "dona da Claude Code", melhor para programar.
- [[wiki/entities/openai]], [[wiki/entities/codex-openai]]: ChatGPT e Codex.

## Concepts

- [[wiki/concepts/copiador-de-prompt]] (novo), [[wiki/concepts/prompt-vago-vs-prompt-especifico-demais]], [[wiki/concepts/clareza-antes-do-prompt]], [[wiki/concepts/prompt-engineering]]
- [[wiki/concepts/ia-como-amplificador]], [[wiki/concepts/especialista-leva-vantagem-com-ia]]
- [[wiki/concepts/janela-de-contexto]], [[wiki/concepts/degradacao-de-contexto]], [[wiki/concepts/context-compaction]], [[wiki/concepts/alucinacao-llm]]
- [[wiki/concepts/decomposicao-de-problemas]], [[wiki/concepts/code-review]], [[wiki/concepts/gargalo]], [[wiki/concepts/degradacao-de-seguranca-iterativa-ia]]
- [[wiki/concepts/corrida-preco-qualidade-llm]], [[wiki/concepts/ia-generativa]]

## Open Questions

- Como fica o "workflow" prometido: um chat por peça de Lego? CLAUDE.md ou AGENTS.md para o "contexto da empresa"?
- A aula de mercado vai sustentar "cada vez vai ficar mais caro" contra a queda do preço por token?
- "Mega brain" é o nome de um agente ou de uma configuração no Codex?

## Raw Quotes

- "O resultado da inteligência artificial é o reflexo daquilo que você sabe."
- "Ele ganhou velocidade, entre aspas, de uma maneira mentirosa, mas ele teve que retornar."
- "Use a menor quantidade de prompt possível."
- "Antes [...] tinha três PR, hoje tem 40, como é que vai ficar o code review disso?"
- "É assim que você aprende a mexer de fato e não se torna um copiador de prompt."
