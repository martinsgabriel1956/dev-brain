---
type: source
title: "FrontPUSH, módulo de IA: meu workflow de IA (mídia) (aula 7)"
aliases: ["workflow de mídia com IA do Násser", "não existe mais o prompt", "site do robô FrontPUSH", "módulo de IA FrontPUSH aula 7"]
date_created: 2026-11-27
date_updated: 2026-11-27
source_count: 0
tags: [ia-generativa, geracao-de-imagem, geracao-de-video, meta-prompting, prompt-engineering, chatgpt, gemini, nano-banana-pro, midjourney, kling-ai, topaz-video, direitos-autorais, mood-board, ui-design, ia]
skill: tech-mentor-ai
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-ia-meu-workflow-de-ia-midia.md"
source_url: ""
author: "Násser"
date_published: "2026-07 (gravação, inferida de \"estamos na metade do ano\")"
date_ingested: 2026-11-27
---

# FrontPUSH, módulo de IA: meu workflow de IA (mídia) (aula 7)

## TL;DR

Primeira aula prática do módulo de IA do [[wiki/entities/frontpush|FrontPUSH]], com cerca de 30 min, tela compartilhada e sem slides. Vem depois de [[wiki/sources/frontpush-ia-o-futuro-da-ia-parte-2]]. [[wiki/entities/nasser|Násser]] mostra o panorama do fluxo de imagem e vídeo por trás dos sites do robô, do [[wiki/entities/spider-man-projeto-nasser|Spider-Man]] e de outros. A tese de abertura é "não existe mais esse negócio de prompt": quem conhece os princípios conversa com o chatbot, por voz, com contexto e referências, e pede que ele escreva o prompt para a outra IA ([[wiki/concepts/meta-prompting]], [[wiki/concepts/copiador-de-prompt]]). Tudo começa antes do chatbot, com referências do Pinterest e do Dribbble num [[wiki/concepts/mood-board]].

A divisão de tarefas:
- **Gemini com [[wiki/entities/nano-banana-pro|Nano Banana Pro]]:** "melhor" para as primeiras imagens.
- **GPT imagem:** "melhorou bastante" e às vezes entende melhor as modificações.
- **[[wiki/entities/midjourney|Midjourney]]:** as imagens mais "cinematográficas", mas "péssimo" para editar.
- **[[wiki/entities/kling-ai|Kling AI]]:** "o rei dos vídeos", com takes de 5 s emendados para não alucinar.
- **[[wiki/entities/topaz-video|Topaz Video]]:** 1080p → 4K e 24 → 60 fps.

A demonstração central é o site do robô, inspirado no de Lando Norris: a foto do autor e a armadura sobrepostas com [[wiki/entities/three-js|Three.js]]. As versões pioram a cada pedido no mesmo chat (a corrente "deu uma bombeadinha"). Ele lê isso como compactação de contexto e conclui: refazer em outro chat e, em código, "atuar como um sênior" em pedaços pequenos. A conclusão prática vale, mas o mecanismo é sobretudo a [[wiki/concepts/deriva-em-edicao-iterativa-de-imagem|deriva de cada edição sobre a imagem anterior]]. Também contornou o filtro de direitos autorais do Homem-Aranha sem nomear o personagem. Ver Contradições.

## Key Claims

### "Não existe mais esse negócio de prompt"

- O pedido recorrente ("Násser, qual foi o prompt que você usou?") é coisa "lá do começo". Hoje, "se você conhecer minimamente os princípios [...] você não vai precisar mais de prompt" ([[wiki/concepts/copiador-de-prompt]], continuação de [[wiki/sources/frontpush-ia-como-dar-comandos-na-ia-da-forma-correta]]).
- Antes da IA, o designer pesquisava no [[wiki/entities/dribbble|Dribbble]], no Landingfolio e em sites de landing pages; isso continua sendo o primeiro passo: "eu pesquiso boas fotos, eu pesquiso boas referências" ([[wiki/concepts/modelar-referencias]]). "Um prompt só resolve a sua vida [...] isso não existe, e se existir, estão mentindo, são marqueteiros."
- "A IA aumenta a régua": os "medianos, mais encostadas, que não estudavam, que não tinham metodologia [...] vão morrer para a inteligência artificial". Com um humano operando, o resultado "não fica genérico [...] fica com mais identidade". A IA vai "substituir as pessoas ruins" ([[wiki/concepts/especialista-leva-vantagem-com-ia]]).

### O chatbot escreve o prompt

- "Eu posso conversar com o chatbot para poder lhe fazer o prompt para mim": fala informal, por microfone, com "contexto", "referências técnicas" e "delimitações técnicas". Depois pede "eu preciso gerar um prompt para inteligência artificial, X para Y para Z" e refina ([[wiki/concepts/meta-prompting]]).
- "Muito simples e chega a ser ridículo, eu converso com o GPT." Usa o GPT porque "o Nubank deu uma licença para mim [...] GPT Pro" ([[wiki/entities/nubank]]), mas "utilizaria o Gemini, utilizaria o Claude [...] o princípio não muda".

### Referências antes do chatbot

- "Eu começo pelas imagens, para depois gerar os vídeos." "O trabalho começa antes, é como se fosse um mood board": procura versões boas do personagem, anexa as fotos e só então descreve ([[wiki/concepts/mood-board]]).
- No Gemini, "criar imagem" habilita o Nano Banana Pro. O "GPT imagem", lançado "dois, três meses" antes, "melhorou bastante" e "às vezes ele entende até melhor" as modificações; para "as primeiras imagens", o Nano Banana segue "o melhor [...] isso pode mudar".
- **Direitos autorais:** com o Homem-Aranha "é meio difícil", porque "os detentores dos direitos [...] já estão boicotando". A IA responde "tem direitos autorais, peça outra coisa". No vídeo, "eu não falava que era o Homem-Aranha, para poder tentar fugir dos direitos autorais".

### O projeto do robô e a perda de qualidade

- O site imita a página de Lando Norris: "quando você passa o mouse [...] revela quem está por trás da máscara". São duas imagens (a pessoa e o capacete ou armadura) sobrepostas com [[wiki/entities/three-js|Three.js]]; o layout está no [[wiki/entities/figma|Figma]].
- As primeiras versões "ficaram feias". A cada novo pedido no mesmo chat, a corrente "deu uma bombeadinha", e depois de uma pausa "olha só o tanto que piorou". Ele pediu "recupere o contexto do chat" e "ele não recuperou 100%". Leitura dele: "tem uma compressão dos dados, um resumo dos dados" ([[wiki/concepts/context-compaction]], [[wiki/concepts/degradacao-de-contexto]]).
- Regra prática: "tenta fazer em uma aba só, se estiver errando demais, abre outro prompt e faz de novo"; "já exclua aquele chat, já inicio outro". Em código, "atuar como um sênior, conferindo as principais pontas e fazendo de forma mais picada". Falar "15 minutos dando um prompt" ("que nem o Thiago Finch, olha, Mega Brain, faz isso") deu "mais distorções, tanto de imagem quanto de código".
- **Rosto:** "não ficou muito parecido comigo". Há "técnicas [...] para você colocar JSON, referência de imagem", mas ele "ainda não encontrou" uma que funcione.
- **Pedido de estúdio:** referência do Pinterest, "fundo branco, tendendo para o cinza, uma leve iluminação, key light, iluminação de cinema [...] objetivo, direto e reto". A pessoa saiu melhor no Gemini ("o que define que foi feito pelo Gemini é essa estrelinha"), e o robô, no ChatGPT.
- **Pedido da armadura:** "faça uma armadura preta, futurista com leds azuis [...] não mexa no posicionamento da pessoa [...] proporção 16 por 9, alta qualidade, 4K, como se fosse uma renderização, clean". Ainda errou: o robô ficou "um pouquinho torto" e a nuca saiu "fora da armadura".

### Como eu crio mídia

1. **Chatbot (GPT, Gemini ou Claude):** contexto com palavras-chave, "simples, direta e objetiva", mais as fotos de referência. Outra técnica: pedir ao chatbot que descreva uma imagem de referência "em JSON" para reproduzi-la.
2. **Gemini/Nano Banana e GPT:** o Gemini "é muito bom", e o GPT vem "em segundo lugar" para coisas mais simples. Ambos editam fotos; o Midjourney, não.
3. **Midjourney:** "é péssimo" para editar, mas "é onde faz as imagens mais bonitas [...] cinematográfico". O GPT escreve o prompt e ele "copia e cola". Antes só havia o Discord ("barra e imagine"); hoje há interface web. Também faz vídeo, "minimamente bom".
4. **Kling AI:** "o rei dos vídeos", "que você pensa que foi realmente filmado". Mesmo método: "um vídeo a partir de um frame", "16 por 9, qualidade máxima, aspecto realista [...] como se fosse um drone [...] não quero vultos". Transição entre duas imagens ([[wiki/concepts/start-frame-e-end-frame]]), com referências como "monte a armadura como se fosse o Homem de Ferro" e o caso de uma Ferrari "que ficou absurdo", com rodas ainda distorcidas. Takes de 5, 10 ou 15 s; "eu tento fazer sempre takes menores de 5 segundos e emendando um no outro, para poder ele não alucinar". O modelo citado é o "vídeo 2.6", sem áudio; os mais recentes gastam mais créditos.
5. **Topaz Video:** upscaling de 1080p com escolha de modelo, nitidez e reconstrução de detalhes, mais "interpolação de frames, em 24 frames eu consigo transformar em 60", para chegar a "4K 60" ([[wiki/concepts/upscaling-com-ia]]).

- **Custos:** GPT e Gemini/Nano Banana "gratuito, mas limitado"; Midjourney "pago, mas relativamente barato"; Kling por créditos "sob demanda".
- "Existem outras ferramentas? Com certeza [...] não o melhor, mas o que eu utilizo." Próximos passos: aulas por ferramenta, o workflow de código e o projeto final "Axies Pro" ([[wiki/concepts/pipeline-de-midia-com-ia]]).

## Contradições e precisões

- **A piora no mesmo chat não é (só) compactação de contexto.** Numa edição de imagem, cada versão é gerada a partir da imagem anterior. Pequenas perdas e reinterpretações se acumulam (a corrente "bombeada", o rosto que se afasta), como copiar uma cópia. Isso acontece mesmo com o contexto longe do limite. A compactação e a [[wiki/concepts/degradacao-de-contexto|degradação]] de chats longos somam efeito sobre as *instruções*, não sobre os pixels. A saída que ele usa vale para os dois casos: voltar à melhor versão, começar outro chat e reanexar o original. "Recupere o contexto" não funciona, porque o modelo não recupera o que saiu da janela. Ver [[wiki/concepts/deriva-em-edicao-iterativa-de-imagem]]. Confiança média-alta.
- **"Não existe mais prompt" × meta-prompting.** O prompt continua existindo; quem o escreve é o chatbot ([[wiki/concepts/meta-prompting]]). A frase é sobre *copiar* prompts, não sobre a técnica, e bate com a parte 4. Confiança alta.
- **Fugir do filtro de direitos autorais.** Não nomear o Homem-Aranha engana o filtro, mas não resolve a questão: personagens e seu visual são protegidos, e os estúdios processam geradores de imagem. Disney e Universal processaram o Midjourney em junho de 2025. Para portfólio pessoal o risco é baixo; para cliente, não. Na [[wiki/sources/frontpush-ia-como-eu-crio-imagens-e-videos-com-ia|aula de mídia]] a wiki já registrou que tirar o logo não tira o desenho industrial. Confiança alta no fato do processo, média na avaliação de risco.
- **Tensão com a aula de mídia** sobre quem faz o quê. Lá, o Midjourney criava do zero e o Nano Banana Pro alterava uma foto existente. Aqui, o Nano Banana é o melhor para "as primeiras imagens" e o GPT entende melhor as modificações. É a mesma lógica (escolher a ferramenta pela tarefa) com o ranking atualizado: "isso pode mudar". Confiança alta.
- **"A estrelinha" do Gemini** é a marca d'água visível. Além dela, as imagens do Google levam o SynthID invisível. Remover a estrela não remove a proveniência. Confiança alta.
- **Datas e números.** "GPT imagem" lançado "dois, três meses" antes de julho de 2026 e a licença "GPT Pro" via Nubank não foram verificados (confiança baixa). Interface web do Midjourney e vídeo do Midjourney (V1, jun. 2025) conferem (alta). "Vídeo 2.6" é coerente com o Kling 2.6, de dez. 2025 (média).
- **Lapsos literais no raw:** "PupSense", "FIOPSINAS", "XPRO" e "Axies Pro" (nomes de projetos não identificados; o site do joystick da aula de mídia aparecia como "exispro"), "modifique essa ESS", "roisinha", "o all", "esse parte", "um inteligente artificial", "perca", "ficou 100%, mas tem alguns textos". Há lacunas na legenda perto de 00:10:41, 00:11:15 e 00:16:46.

## Entities

- [[wiki/entities/nasser]]: instrutor.
- [[wiki/entities/frontpush]]: curso, módulo de IA.
- [[wiki/entities/nano-banana-pro]], [[wiki/entities/google]]: Gemini e a "estrelinha".
- [[wiki/entities/openai]]: ChatGPT e "GPT imagem".
- [[wiki/entities/midjourney]], [[wiki/entities/kling-ai]], [[wiki/entities/topaz-video]]: as etapas de imagem e vídeo.
- [[wiki/entities/nubank]]: a licença do GPT.
- [[wiki/entities/three-js]], [[wiki/entities/figma]], [[wiki/entities/dribbble]]: ferramentas de site, layout e referência.
- [[wiki/entities/spider-man-projeto-nasser]]: projeto citado.

## Concepts

- [[wiki/concepts/pipeline-de-midia-com-ia]], [[wiki/concepts/meta-prompting]], [[wiki/concepts/copiador-de-prompt]]
- [[wiki/concepts/deriva-em-edicao-iterativa-de-imagem]] (novo), [[wiki/concepts/context-compaction]], [[wiki/concepts/degradacao-de-contexto]]
- [[wiki/concepts/mood-board]], [[wiki/concepts/modelar-referencias]], [[wiki/concepts/especialista-leva-vantagem-com-ia]]
- [[wiki/concepts/start-frame-e-end-frame]], [[wiki/concepts/upscaling-com-ia]]

## Open Questions

- O que são "PupSense", "FIOPSINAS", "XPRO" e o projeto final "Axies Pro"? Provavelmente o site do joystick (X's Pro?), mas a grafia não se confirma.
- A "aula só de Midjourney" e a "aula só do Kling" vão mostrar os prompts que o GPT gerou, já que ele diz que "posso colocar algumas referências de prompt"?
- Que técnica de JSON e referência ele vai usar para manter o rosto, já que "ainda não encontrei"?

## Raw Quotes

- "Hoje em dia não tem mais esse negócio de prompt."
- "É lógico que a IA aumenta a régua."
- "Muito simples e chega a ser ridículo, eu converso com o GPT."
- "Se estiver errando demais, abre outro prompt e faz de novo."
- "Eu não falava que era o Homem-Aranha, para poder tentar fugir dos direitos autorais."
