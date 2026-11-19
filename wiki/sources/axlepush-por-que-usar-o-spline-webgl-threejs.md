---
type: source
title: "Por que usar o Spline? (AxlePUSH)"
aliases: ["AxlePUSH aula 01", "Por que o Spline", "Spline × Three.js"]
date_created: 2026-11-19
date_updated: 2026-11-19
source_count: 0
tags: [3d, spline, webgl, threejs, gltf, no-code, curso, frontend, ui-design]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/axlepush-por-que-usar-o-spline-webgl-threejs.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-19
---

# Por que usar o Spline? (AxlePUSH)

## TL;DR

Primeira aula transcrita do [[wiki/entities/axlepush|AxlePUSH]], cerca de 15 minutos e sem código (o falante diz "segunda aula"; o arquivo se chama "01"). O instrutor, provavelmente [[wiki/entities/nasser|Násser]] (ver abaixo), explica por que o curso de assets 3D para a web usa o [[wiki/entities/spline|Spline]] e não o [[wiki/entities/three-js|Three.js]].

- **O curso:** "criação de assets 3D para projetos web". HTML, CSS e JavaScript, ou uma ferramenta no-code, são pré-requisito e não fazem parte do conteúdo.
- **3D no navegador:** precisa de [[wiki/concepts/webgl|WebGL]] e de bibliotecas como o Three.js. Os modelos vêm do [[wiki/entities/blender|Blender]] ou do [[wiki/entities/cinema-4d|Cinema 4D]], exportados em [[wiki/concepts/formato-gltf|GLB/glTF]], e "toda a manipulação" é "via código". Quem renderiza é a placa de vídeo ([[wiki/concepts/gpu|GPU]]): ele ouve os fans ligarem.
- **Curva de aprendizado:** Three.js exigiria "saber JavaScript para caramba". Foi por isso que ele nunca levou 3D para o [[wiki/entities/frontpush|FrontPUSH]] ([[wiki/concepts/curva-de-aprendizado]]).
- **Spline "caiu como uma luva":** traz features de modelagem dos programas complexos de forma mais simples, sem toda a iluminação e as sombras, porque roda na web. Limita o tamanho dos GLB importados. É colaborativo, em tempo real e web-based, e atende "80%, 90% ou até mais dos casos".
- **No Spline:** modelos, animações, interatividade e importação de arquivos. O curso trabalha a integração e a exportação, inclusive com o [[wiki/entities/webflow|Webflow]], que "anunciou recentemente" uma parceria com o Spline.
- **Público:** devs, UI designers e devs no-code. Exportar só foto ou vídeo já serve ao designer, e os elementos 3D da landing page foram recoloridos para o [[wiki/concepts/branding|branding]] roxo e rosa do curso.

## Key Claims

- **Pré-requisito explícito.** "Não é para você aprender a parte de programação da web [...] essa parte não é nesse curso". Ele repete isso três vezes. Evidência: fala direta.
- **3D no browser exige WebGL e uma biblioteca.** "Para poder você trazer uma renderização 3D para dentro de um browser, você vai precisar utilizar do WebGL e de bibliotecas como o Three.js." Correto quanto ao WebGL. A biblioteca é opcional na teoria (dá para chamar a API crua), mas na prática quase todo mundo usa uma. Ver as precisões.
- **Fluxo profissional.** Modelar num programa (Blender, Cinema 4D), exportar "geralmente [em] GLB", carregar no Three.js e programar zoom, movimento e interações. Ele mostra a página "carregando elementos 3D" da documentação do Three.js, que cita .glb e .gltf.
- **A GPU faz o trabalho.** "Isso aqui é tudo a placa de vídeo que faz utilizando o Three.js." Evidência: os fans da placa ligam durante a demonstração dos exemplos.
- **O custo é o código.** "A parte de você manipular e criar os efeitos é bem mais complexa, porque é direto no código." O curso pede "um pouco de HTML e CSS"; o Three.js pediria JavaScript a fundo.
- **O Spline simplifica porque precisa rodar na web.** Uma cena "a ponto de nível de cinema" travaria no navegador, então o próprio Spline limita iluminação, sombras e o tamanho dos GLB importados. O limite exato não é dito.
- **Suficiente na maioria dos casos.** "80%, 90% ou até mais dos casos de quem quer ter uma experiência web". É opinião dele, sem medição.
- **Integração no-code.** O Webflow "fez uma grande atualização falando sobre a integração com Spline". Confirmado como `[external]` abaixo.
- **Uso sem código.** Exportar o modelo "em foto" ou "em vídeo" "já é suficiente para um UI designer, designer gráfico".

## Entities

- [[wiki/entities/axlepush]]: o curso; landing page com features tiradas do site do Spline.
- [[wiki/entities/spline]]: a ferramenta escolhida.
- [[wiki/entities/three-js]]: a alternativa descartada por exigir código.
- [[wiki/entities/blender]] e [[wiki/entities/cinema-4d]]: programas profissionais de modelagem ("conheço muito o Blender, de ser famoso, não de mexer nele").
- [[wiki/entities/webflow]]: ferramenta no-code com integração nativa do Spline.
- [[wiki/entities/frontpush]]: o curso anterior, que nunca teve 3D; também citado no desconto.
- [[wiki/entities/nasser]]: instrutor (inferido).
- [[wiki/entities/creatorpush]]: outro curso da mesma família "PUSH" (só pela marca; não citado na aula).

## Concepts

- [[wiki/concepts/webgl]]: API de gráficos acelerados por GPU no navegador.
- [[wiki/concepts/formato-gltf]]: .glb e .gltf, os formatos de troca dos modelos.
- [[wiki/concepts/gpu]]: quem renderiza a cena.
- [[wiki/concepts/curva-de-aprendizado]]: o motivo de trocar código por ferramenta visual.
- [[wiki/concepts/alto-nivel-vs-baixo-nivel]]: Spline sobre bibliotecas sobre WebGL, uma pilha de abstrações.
- [[wiki/concepts/compatibilidade-entre-navegadores]]: "qualquer browser"; "às vezes não funciona corretamente".
- [[wiki/concepts/plugin-de-navegador]]: o WebGL dispensa "plugins de terceiros".
- [[wiki/concepts/branding]] e [[wiki/concepts/elementos-de-composicao]]: elementos 3D recoloridos para "dar maior ambiência".

## Precisões e tensões com a wiki

- **Autoria.** O falante não diz o nome. Ele fala do FrontPUSH como seu ("eu nunca cheguei a trazer algo parecido para o front push"), e a marca segue o padrão FrontPUSH/Creator Push. Por isso o autor é provavelmente [[wiki/entities/nasser]]. Confiança média-alta.
- **Nome do curso.** A legenda diz "Excel Push" e "Excel"; o nome da pasta das transcrições é "AxlePUSH". Corrigido para AxlePUSH e "Axle". A grafia exata da marca não foi conferida.
- **Data da gravação.** `[external]` O Webflow lançou o elemento nativo do Spline na Webflow Conf 2023, em outubro de 2023 ([recap da keynote](https://webflow.com/blog/webflow-conf-2023-keynote-recap), [página da integração](https://webflow.com/integrations/spline)). Como ele diz "anunciou recentemente", a aula é provavelmente do fim de 2023. O "falecido Internet Explorer" combina: o IE 11 foi aposentado em junho de 2022 `[external]`. Confiança média.
- **Definição de WebGL truncada.** A legenda perdeu cerca de 15 s (00:03:39–00:03:54) enquanto ele lia a definição. `[external]` O WebGL é uma API JavaScript da Khronos, baseada no OpenGL ES, que desenha gráficos 2D e 3D num `<canvas>` (WebGL 1.0 em 2011, WebGL 2 em 2017). Ver [[wiki/concepts/webgl]].
- **"Melhora drasticamente o desempenho geral da sua página".** Exagero do texto que ele leu. A GPU acelera o desenho da cena, mas uma página com 3D fica mais pesada que a mesma página sem 3D: o runtime em JS, o modelo baixado, a memória de vídeo e a bateria. Os fans que ele ouve são esse custo, que no celular do visitante vira calor e bateria. `[skill: tech-mentor-frontend]` A referência recomenda detectar o suporte (`getContext("webgl2")`, `"gpu" in navigator`) e ter fallback. Confiança alta.
- **"Bibliotecas como o Three.js" não são obrigatórias.** O Three.js é uma camada sobre o WebGL (cena, câmera, renderer, mesh). Existem o Babylon.js, o PlayCanvas e, para só exibir um modelo, o `<model-viewer>` do Google, que carrega um glTF com uma tag HTML e quase nenhum código `[skill: tech-mentor-frontend]`. Para o caso "mostrar um modelo girando" isso enfraquece um pouco o argumento de que o 3D exige "JavaScript para caramba". O argumento continua valendo para cenas com animação e interação.
- **Próximo passo do 3D na web.** `[skill: tech-mentor-frontend]` O WebGPU (Chrome 113+, Safari 18+) é o sucessor do WebGL, e o Three.js já tem um `WebGPURenderer`. Não aparece na aula.
- **Limite de importação do Spline.** Uma busca não achou o valor oficial do limite de GLB (`[external]`, busca de 2026-11-19 sem resultado na documentação do Spline). Fica como pergunta aberta.
- **Blender × Cinema 4D.** `[external]` O Blender é livre e gratuito (GPL); o Cinema 4D é comercial, da Maxon. A aula os põe lado a lado sem citar essa diferença, que pesa para quem estuda sozinho.

## Open Questions

- Qual é o limite de tamanho de GLB no Spline, e ele mudou desde 2023?
- O que a aula 00 (ou "primeira aula") cobriu? Ele diz "mais uma vez" sobre a landing page e o pré-requisito.
- Quais são "os dois principais projetos do AxlePUSH"? Ficam para a próxima aula.
- "O falecido Internet Explorer ou Microsoft": provavelmente "Microsoft Edge", com palavra perdida na legenda; deixado literal.
- "Implicar em 3D para o web": provavelmente "aplicar 3D"; deixado literal.

## Raw quotes

- "Senta que lá vai a história"
- "Por isso que o Spline caiu como uma luva"
- "Imagina isso aqui tudo no código, entendeu?"
