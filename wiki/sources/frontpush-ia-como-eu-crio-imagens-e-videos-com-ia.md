---
type: source
title: "FrontPUSH, módulo de IA, aula 01: como eu crio imagens e vídeos com IA"
aliases: ["como eu crio imagens e vídeos com IA", "mídia com IA do Násser", "joystick com IA", "módulo de IA FrontPUSH aula 01"]
date_created: 2026-11-23
date_updated: 2026-11-23
source_count: 0
tags: [ia-generativa, geracao-de-imagem, geracao-de-video, prompt-engineering, meta-prompting, midjourney, kling-ai, nano-banana-pro, topaz-video, upscaling, scroll-animation, performance, frontend, ui-design]
skill: tech-mentor-ai
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-ia-como-eu-crio-imagens-e-videos-com-ia.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-23
---

# FrontPUSH, módulo de IA, aula 01: como eu crio imagens e vídeos com IA

## TL;DR

Primeira aula do módulo de IA do [[wiki/entities/frontpush|FrontPUSH]], publicada como vídeo não listado no YouTube, 38 min. [[wiki/entities/nasser|Násser]] mostra como fez a mídia de um site de produto "estilo [[wiki/entities/apple|Apple]]" para um joystick, com a hero animada pelo scroll ([[wiki/concepts/animacao-por-sequencia-de-frames-no-scroll]]). O fluxo ([[wiki/concepts/pipeline-de-midia-com-ia]]) tem quatro etapas, cada uma com uma ferramenta. Primeiro, uma referência opcional. Depois, o ChatGPT ou o Gemini escrevem os prompts a partir de áudio ditado ([[wiki/concepts/meta-prompting]]). As fotos saem do [[wiki/entities/midjourney|Midjourney]] (do zero) ou do [[wiki/entities/nano-banana-pro|Nano Banana Pro]] (a partir de uma foto). Os vídeos saem do [[wiki/entities/kling-ai|Kling AI]], com [[wiki/concepts/start-frame-e-end-frame|start frame e end frame]]. O [[wiki/entities/topaz-video|Topaz Video]] faz o [[wiki/concepts/upscaling-com-ia|upscale]] para 4K60, e o resultado é reduzido para 1080p30 no site. A tese que atravessa a aula: quanto menos a IA precisa inventar, melhor o resultado.

## Key Claims

### Por que IA, e por que código nativo

- O site foi "codado full, código nativo", sem Framer ou page builder, porque alguns efeitos e seções não sairiam nativamente nessas ferramentas. Para ele, o [[wiki/entities/webflow|Webflow]] e o Framer são as ondas de agora, depois do Dreamweaver.
- Alternativas à IA: contratar renderização profissional ("a brincadeira fica muito cara") ou usar mídia pronta, o que cria problemas de direitos autorais e de uso.
- Ele calcula "quatro meses de muito estudo e muito teste" e diz que a habilidade serve a UI designers e a devs que querem entregar o projeto de ponta a ponta.

### Quais IAs, e por quê

| Etapa | Ferramenta | Uso declarado | Custo declarado |
|---|---|---|---|
| Prompt | ChatGPT ou Gemini | Escreve o prompt detalhado a partir da descrição ditada | Plano gratuito |
| Foto do zero | Midjourney | Criar sem referência; fotos abstratas ou "profissionais" | Basic, US$ 10/mês, mais horas extras de US$ 4 |
| Foto a partir de foto | Nano Banana Pro | Modificar ou recriar uma referência | Gratuito com limite; "US$ 96 por mês" no pago (ver ressalvas) |
| Vídeo | Kling AI | "Campeão" em qualidade; start frame e end frame | Créditos avulsos: "US$ 5, 330 em créditos" |
| Aprimoramento | Topaz Video | Upscale, interpolação de frames, nitidez | Comprou vitalício por cerca de R$ 1 mil (v6); hoje é assinatura de US$ 25 a 58/mês |

- Se tivesse que escolher uma só, seria Midjourney + ChatGPT gratuito, pelo custo-benefício.
- **Método antes de ferramenta:** sempre vai existir uma IA nova e mais barata, mas sem "um mínimo método" a pessoa vive "contratando novas inteligências artificiais" sem melhorar o fluxo ([[wiki/concepts/apego-a-ferramentas]]).
- Sobre o mercado: "eu penso que essa bolha está prestes a estourar", embora a IA seja "uma mudança de paradigma muito grande" ([[wiki/concepts/hype-de-ia]]).

### O fluxo, etapa por etapa

1. **Referência (opcional).** Com uma foto de base, a descrição "combina" com ela e o resultado tende a melhorar. Sem foto, a descrição precisa de mais detalhes.
2. **Prompt pela IA.** Ele grava áudio longo no app do ChatGPT, "de forma pausada, sem pressa", e lapida o resultado: "eu uso a IA para poder escrever os prompts das outras IAs" ([[wiki/concepts/meta-prompting]], [[wiki/concepts/prompt-engineering]]).
3. **Fotos.** Midjourney para criar do zero, Nano Banana Pro para alterar uma foto existente.
4. **Vídeos.** Volta ao ChatGPT para escrever o prompt do Kling AI e gera o vídeo.
5. **Aprimoramento.** O Topaz Video nivela tudo em 4K60 para depois reduzir a 1080p30 ou 1080p60. A lógica: "você tem que produzir o conteúdo acima [...] porque nessas conversões perde-se qualidade".

### Por que 1080p30 no site

- O 1080p "abraça a maioria das mídias" e dispositivos, inclusive mobile, com "um desempenho infinitamente melhor" que 4K60. Na tela 4K dele, a mídia aparece "um pouquinho esticada" e pixelada em alguns pontos, um custo que ele aceita: "a gente precisa abrir mão de alguma coisa" ([[wiki/concepts/core-web-vitals]], [[wiki/concepts/otimizacao-de-imagens]]).
- No fim, ele avisa que o 4K60 "é um peso gigantesco" e precisa de "uma série de otimizações" antes de entrar no site, que ficam para depois.

### Prática: Midjourney (do zero)

- Exemplo de um cliente que vende aquecimento de piscinas. Ele ditou casas modernas e modestas, conforme o público-alvo, fotos de drone e panorâmicas "como se fosse a apresentação de uma casa para [...] vender no mercado imobiliário".
- Parâmetros: `--ar 16:9` (ou 9:16, 21:9, 4:3) e `--v 7`. Cada prompt gera quatro imagens. Os comandos são Vary (variar), Upscale, Remix (outra referência), Zoom, More (reenviar) e Animate.
- O Animate tem modo automático ("low motion") e loop. O loop serve para elementos de site: um vídeo de 3 a 5 s, "mais ou menos do tamanho de uma imagem", rodando sem fim.
- A foto ficou boa e o vídeo, "satisfatório" em SD. A vegetação do vídeo saiu feia, e o joystick recriado no Midjourney a partir de anexo ficou "deformado".

### Prática: Nano Banana Pro (a partir de referência)

- As fotos reais do controle tinham logos e escritas: "isso pode me dar problema de direitos autorais". O prompt, montado pelo ChatGPT, pediu para manter "o material, a textura, a iluminação, o posicionamento" e tirar logos e escritas.
- Num segundo prompt, pediu pequenas rotações, novas iluminações e um tom de branco levemente diferente, e recebeu quatro versões em posições diferentes. Tudo no plano gratuito.

### Prática: Kling AI (start frame e end frame)

- O Kling "precisa de um bom direcionamento". Quando tem que "inventar muita coisa", erra. Por isso ele pede "movimentações tranquilas, suaves" ([[wiki/concepts/start-frame-e-end-frame]]).
- **Erro 1, frames distantes:** dois frames muito diferentes sem descrever a transição (rotacionar no eixo X e Y, focar no joystick) deram um vídeo ruim.
- **Erro 2, sem end frame:** o modelo "começou a inventar uns botões que não existem".
- **Acerto:** frente → verso do controle só funcionou depois de dizer "a primeira imagem é a frente do controle e a outra é o verso [...] faça isso de maneira leve, suave".
- **Encadeamento:** o end frame de um clipe é o start frame do próximo. Assim ele montou o vídeo longo da seção do site, que volta à posição inicial para fechar o loop. Para zooms suaves, só o start frame basta.
- Configuração: native audio desligado, 720p ou 1080p, de 3 a 15 s (ele usa 3 a 5 s), 16:9, uma saída por vez para gastar menos créditos e testar mais. A saída fica em 1080p30.

### Prática: Topaz Video

- Enhancement com upscale de 2x: de 1080p "fica próximo do 4K", "não vai ficar um 4K nativo". O 4x só para resoluções muito pequenas, e "na maioria das vezes não reconstrói muito bem, porque ele precisa inventar muita coisa" ([[wiki/concepts/upscaling-com-ia]]).
- Modelos: Proteus (geral, "o que eu mais utilizo"), Artemis (ruído e nitidez), Gaia (alta qualidade, animação), Theia (fidelidade e detalhe), e um "específico para upscaling 4x" sem nome na fala.
- Ajustes: Recover Detail em 50, depois pequenos incrementos. Pouco Sharpen e pouco Reduce Noise, para não apagar a textura do controle. Dehalo ligado. Frame Interpolation para sair em 4K60. Preview de 5 frames, que depende de uma boa placa de vídeo.
- Nos testes, mais Sharpen acendeu as bordas, mas "denuncia muito a parte escrita". O DeNoise deixou a imagem "artificial demais". Não existe receita única: carro, renderização e vídeo comum pedem ajustes diferentes, "fui aprendendo apanhando".

## Precisões e ressalvas

- **Kling AI, não "CleanAI"** `[external]`, alta: a legenda transcreveu "CleanAI". Start/end frame, créditos, 720p/1080p e native audio batem com o Kling AI da Kuaishou ([klingai.com](https://klingai.com), sem fetch).
- **O Nano Banana Pro é de imagem** `[external]`, alta: é o Gemini 3 Pro Image, do [[wiki/entities/google|Google]] (nov. 2025; [blog.google](https://blog.google/technology/ai/nano-banana-pro/), sem fetch). "Modificar vídeos" na fala parece lapso por "fotos", e é com fotos que ele demonstra. Os planos pagos do Gemini (AI Pro, AI Ultra) não custam US$ 96/mês até onde sei, então o valor fica em dúvida (baixa confiança).
- **"Midjourney, US$ 4 por mês" é lapso:** pouco antes ele diz US$ 10/mês no Basic e US$ 4 por hora extra, que é o preço da hora extra de GPU rápida (`[external]`, alta; [Comparing Midjourney Plans](https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans), sem fetch). Ele também diz que o vídeo do Midjourney sai em "720p e 30 fps". Até onde sei, o SD do Midjourney é 480p e o HD (720p) fica nos planos Standard ou acima (`[external]`, média).
- **Tirar o logo não tira a propriedade intelectual** `[external]`, alta: o desenho do produto pode ter proteção própria (no Brasil, desenho industrial no INPI; também conjunto-imagem, o *trade dress*). Uma cópia "extremamente similar" de um controle que existe continua sendo aquele controle. Imagem gerada por IA sem autoria humana suficiente também não tem direito autoral nos EUA ([US Copyright Office, relatório parte 2, jan. 2025](https://www.copyright.gov/ai/), sem fetch). A aula trata direitos autorais só como "logos e escritas".
- **Marca d'água e proveniência** `[skill: tech-mentor-ai]`, média-alta: as imagens do Gemini levam o watermark invisível SynthID, e o plano gratuito também põe uma marca visível. Reencode, recorte e upscale removem os metadados C2PA, mas não necessariamente o watermark. Antes de pôr no site de um cliente, vale conferir os termos de uso comercial de cada ferramenta.
- **Por que produzir acima e reduzir** `[external]`, média: reduzir de 4K para 1080p é *supersampling* e esconde artefatos de compressão e de geração. Mas o ganho do caminho 1080p → 4K → 1080p vem do *denoise* e do realce de detalhe do Topaz, não da resolução, porque o upscale não cria informação real, só detalhe plausível. É o mesmo "precisa inventar" que ele aponta no 4x.
- **Interpolação ≠ upscale** `[external]`, alta: no Topaz, o 30 → 60 fps é feito por modelos de interpolação (Apollo, Chronos), separados do Proteus. "Nivelar a 4K a 60 fps" junta as duas operações.
- **"Bolha prestes a estourar"** é opinião sem dado, e esta wiki tem um argumento contrário em [[wiki/concepts/hype-de-ia]] ("não é bolha no sentido clássico").

## Entities

- [[wiki/entities/nasser]]: autor; site de portfólio e projeto do joystick.
- [[wiki/entities/frontpush]]: o curso e o novo módulo de IA, com vagas abertas para acesso vitalício.
- [[wiki/entities/midjourney]] (novo), [[wiki/entities/nano-banana-pro]] (novo), [[wiki/entities/kling-ai]] (novo), [[wiki/entities/topaz-video]] (novo).
- [[wiki/entities/openai]] (ChatGPT), [[wiki/entities/google]] (Gemini, Nano Banana Pro), [[wiki/entities/apple]] (o estilo de página de produto), [[wiki/entities/webflow]] (e o Framer, como alternativa no-code).

## Concepts

- [[wiki/concepts/pipeline-de-midia-com-ia]] (novo)
- [[wiki/concepts/start-frame-e-end-frame]] (novo)
- [[wiki/concepts/animacao-por-sequencia-de-frames-no-scroll]] (novo)
- [[wiki/concepts/upscaling-com-ia]] (novo)
- [[wiki/concepts/meta-prompting]], [[wiki/concepts/prompt-engineering]], [[wiki/concepts/ia-generativa]], [[wiki/concepts/hype-de-ia]], [[wiki/concepts/apego-a-ferramentas]], [[wiki/concepts/secao-hero]], [[wiki/concepts/otimizacao-de-imagens]], [[wiki/concepts/core-web-vitals]]

## Open Questions

- Como a sequência de frames entra no site (canvas? `<img>` trocado? quantos frames, que formato, que peso)? Fica para o evento e para as aulas de código.
- Quais otimizações levam o 4K60 até o 1080p30 do site (codec, bitrate, WebM/AV1, pôster)?
- O que é "exispro" / "Waxes Pro", o caminho do site no portfólio? A legenda não deixa claro.
- Qual é o modelo do Topaz "específico para upscaling 4x" (provavelmente o Rhea)?

## Raw Quotes

- "Eu uso a IA para poder escrever os prompts das outras IAs."
- "Quando você não especifica ele inventa."
- "Você tem que produzir o conteúdo acima, em uma resolução acima."
