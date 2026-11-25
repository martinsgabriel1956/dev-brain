---
type: source
title: "FrontPUSH, módulo de IA: o que acontece no backstage da IA? (parte 3)"
aliases: ["backstage da IA FrontPUSH", "harness como cabresto", "Jarvis do Homem de Ferro", "módulo de IA FrontPUSH aula teórica 3"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [harness, agente-ia, autonomia, human-in-the-loop, tool-call, llm, reasoning, codex, claude-code, fundamentos, ia]
skill: tech-mentor-ai
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-ia-o-que-acontece-no-backstage-da-ia.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-24
---

# FrontPUSH, módulo de IA: o que acontece no backstage da IA? (parte 3)

## TL;DR

Terceira aula teórica do módulo de IA do [[wiki/entities/frontpush|FrontPUSH]] ("aula três, se não me engano"), com cerca de 14 min e sem slides. Continua [[wiki/sources/frontpush-ia-o-que-sao-as-llms]]. [[wiki/entities/nasser|Násser]] recapitula os oito conceitos da escada e fecha os dois últimos. O **[[wiki/concepts/harness]]** é "o modelo que está controlando", "de cabresto", e "o que mais diferencia um modelo do outro" (ChatGPT × Codex × Claude Code). Os **[[wiki/concepts/agente-ia|agentes e autonomia]]** são "a cereja do bolo": o chat entrega um tutorial e "fala: faz"; o agente "entra no seu sistema operacional", pede permissões, roda os testes, lê os outputs e repete. A imagem do cabresto é a que mais se aproxima do sentido de harness usado na wiki (o arreio em volta do modelo). Mesmo assim, ele continua a fundir harness com "arquitetura", "modelo" e "metodologia por trás", e atribui ao harness as diferenças de geração de imagem e o "pensar" do modelo. A descrição do agente bate com o laço de [[wiki/concepts/tool-call|tool calls]] com [[wiki/concepts/human-in-the-loop|aprovação humana]]. Próxima aula: resumo geral e "qual é a nova barreira da inteligência artificial".

## Key Claims

### Recap da escada

- Os oito conceitos (da [[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia|parte 1]]) são a base: "se você entender minimamente esses oito conceitos, você vai entender o que uma inteligência artificial faz hoje".
- **Regras** ([[wiki/concepts/sistema-especialista]]): "programação condicional". Resolve ("um sistema minimamente inteligente [...] a gente consegue construir um caminho"), mas esbarra em "milhões de if e else encadeados". E mais: "se a gente está tendo que mexer, não é inteligência artificial, a gente está programando". Ver Contradições.
- **ML, redes neurais e deep learning**: spam aprendido por padrões estatísticos; palavras "mais fortes" pesam mais; múltiplas camadas consomem "GPUs, dados, modelos e arquiteturas".

### O Jarvis do Homem de Ferro: a LLM

- Para a IA "se comunicar com as pessoas", é preciso "fazer o Jarvis do Homem de Ferro": "a máquina precisa ter ferramenta para poder aprender como a gente conversa".
- A conversa depende de cultura, conjunções, abreviações e regionalismos ("uma pessoa do Sul [...] a pessoa do Nordeste"). A LLM é "específica para cuspir texto", "basicamente um tradutor" do deep learning para o humano: "mensagem, emissor, receptor, é o básico da comunicação" ([[wiki/concepts/llm-large-language-model]]).

### O harness como cabresto

- "Transformers, que faz parte de LLMs, e harness, que faz parte de arquiteturas"; "o harness é o modelo que está controlando ali, esse harness vem de cabresto [...] vai por essa direção, não vai por essa" ([[wiki/concepts/harness]]).
- Quando o Codex ou o [[wiki/entities/claude-code|Claude Code]] "fica lá pensando", "é o harness desse modelo [...] fazendo perguntas para ele mesmo" a partir do contexto e do pedido ([[wiki/concepts/reasoning-level]]).
- O modelo "vai na internet", pega o texto do usuário e o traduz "em tokens para poder aglutinar para poder consumir o menor recurso possível, porque os recursos são finitos" ([[wiki/concepts/tokenizacao]]).
- **O bolo:** os dados, os parâmetros e o contexto são os ingredientes, e a resposta é o bolo. O tamanho do bolo depende "daquilo que você pagou, que ninguém trabalha de graça, nem o Claude Code, nem o ChatGPT". O preço fica para aulas futuras.
- **"O harness é literalmente o que mais diferencia um modelo do outro."** "Todas consomem da internet, todas têm base de dados, todas estão recebendo parâmetros"; o que muda "é a arquitetura, é o modelo", ou seja, como cada uma traduz o contexto "nos melhores tokens possíveis, perdendo a menor informação possível". Os exemplos citados: o "Codex veio forte", o Claude Code "está codando melhor", uma IA "está fazendo imagens melhores".

### Agentes e autonomia ("a cereja do bolo")

- **Chat:** você pede como fazer uma requisição a uma API REST e mostrar o array ao usuário; a IA devolve "meio que um tutorial", passo a passo, e diz "vá lá e faz agora". Ela usou "do 1 ao 7" (até o harness), mas quem executa é você.
- **Agente:** "o Codex, o Claude Code que está instalado lá no seu computador, ele meio que entra no seu sistema operacional", ganha acesso aos diretórios e arquivos e diz "pode deixar que eu faça" ([[wiki/concepts/agente-ia]]).
- **Caso dele:** deu contexto, o diretório e o erro do console; o agente pediu "você permite que eu faça isso? Sim", rodou, viu os outputs, perguntou o que faltava, montou "um mini contexto" e repetiu até devolver ([[wiki/concepts/human-in-the-loop]], [[wiki/concepts/modos-de-permissao-claude-code]]).
- Por que a IA é "tão disruptiva": dados, processamento e modelos melhores fazem com que ela "consiga teoricamente te imitar". Com agentes é "melhor ainda mais, porque ela literalmente entra no seu PC". "Então cuidado com a Skynet [...] estou brincando" ([[wiki/concepts/agent-containment]]).
- Próximo passo: "qual é o futuro da IA, o que ela faz, o que ela não faz [...] qual é a nova barreira".

## Contradições e precisões

- **"Se tem que mexer, não é IA" × parte 1.** Na [[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia|parte 1]], os sistemas de regras eram "a primeira geração de IA", e o slide dizia que "IA NÃO significa necessariamente aprendizado". Agora o mesmo sistema "não é inteligência artificial". A definição clássica conta sistemas de regras como IA ([[wiki/concepts/inteligencia-artificial]], [[wiki/concepts/sistema-especialista]]). Os ramos do if/else continuam chamados de "probabilidades", embora sejam determinísticos. Confiança alta.
- **O cabresto acerta, a "arquitetura" não.** *Harness* é literalmente "arreio", e a imagem do cabresto coincide com a wiki: restrições, tools, contexto e laço *ao redor* do modelo ([[wiki/concepts/harness]]). Mas "o harness é o modelo" e "é a arquitetura, é o modelo" voltam a fundir os dois. O "pensar" é raciocínio do próprio modelo ([[wiki/concepts/reasoning-level]]); o harness decide quanto orçamento dá a ele e o que fazer com o resultado. Confiança alta.
- **"O harness é o que mais diferencia" é meia verdade.** Em agentes de código, o harness pesa muito: o mesmo modelo rende diferente em harnesses diferentes, e só a verificação dobra ou triplica a qualidade ([[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]], citado em [[wiki/concepts/harness]]). Já em imagens ("fazendo imagens melhores"), a diferença vem do modelo de geração, não do harness. E não é verdade que "todas consomem as mesmas coisas": dados, pós-treino e arquitetura (MoE, tamanho) variam entre os laboratórios. ChatGPT, Codex e Claude Code são **produtos**, ou seja, modelo + harness, e comparar os produtos mistura as duas coisas. Confiança média-alta.
- **"Ele vai na internet".** Só com uma tool de busca, que é um componente do harness. Sem ela, o modelo responde com o que está nos pesos e no contexto. Confiança alta.
- **"Aprendendo nesse processo".** Na inferência não há aprendizado nos pesos; o que muda de um passo para o outro é o contexto ([[wiki/concepts/bajulacao-llm]] já trata disso). Confiança alta.
- **Tokens "para aglutinar e consumir o menor recurso".** Está parcialmente certo: tokenizadores como o BPE são treinados para comprimir texto, e a conta é por token. Mas o modelo não escolhe "os melhores tokens" por pedido, porque a tokenização é fixa ([[wiki/concepts/tokenizacao]]). Confiança alta.
- **Lapsos literais no raw:** "como eu tenho um recurso infinito" (quer dizer finito), "concorda com mim", "qual foi o grande teor", "com os agentes melhor ainda mais", "árvore de prioridades, de probabilidades", "o que é o próximo do ser humano?".

## Entities

- [[wiki/entities/nasser]]: instrutor.
- [[wiki/entities/frontpush]]: curso, módulo de IA.
- [[wiki/entities/claude-code]], [[wiki/entities/codex-openai]]: exemplos de agente local.
- [[wiki/entities/openai]]: ChatGPT como exemplo de chat.

## Concepts

- [[wiki/concepts/harness]], [[wiki/concepts/reasoning-level]], [[wiki/concepts/tokenizacao]]
- [[wiki/concepts/agente-ia]], [[wiki/concepts/tool-call]], [[wiki/concepts/human-in-the-loop]], [[wiki/concepts/modos-de-permissao-claude-code]], [[wiki/concepts/agent-containment]]
- [[wiki/concepts/llm-large-language-model]], [[wiki/concepts/sistema-especialista]], [[wiki/concepts/inteligencia-artificial]]

## Open Questions

- Continuação: [[wiki/sources/frontpush-ia-como-dar-comandos-na-ia-da-forma-correta]] (parte 4: contexto, Lego, RAW → JPEG; a "nova barreira" ainda não apareceu).
- Qual é a "nova barreira" que a próxima aula promete? Custo, contexto, energia (já citados) ou confiabilidade dos agentes?
- O "tamanho do bolo para aquilo que você pagou" vai virar uma aula de preços, planos e limites por token?
- O curso vai separar modelo e harness quando comparar ChatGPT, Codex e Claude Code?

## Raw Quotes

- "Se a gente está tendo que mexer, não é inteligência artificial, a gente está mexendo, a gente está programando."
- "A gente precisa fazer o Jarvis do Homem de Ferro."
- "Esse harness vem de cabresto, como se fosse o contexto de cabresto [...] vai por essa direção, não vai por essa."
- "O harness é literalmente o que mais diferencia um modelo do outro."
- "Ele meio que entra no seu sistema operacional e fala assim, olha, eu já tenho agora acesso aos diretórios dele."
