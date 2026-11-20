---
type: source
title: "Otimização de animações: pipeline de renderização, transform, opacity e a thread do compositor (FrontPUSH)"
aliases: ["FrontPUSH otimização aula 07", "Otimização de Animações", "módulo de otimização, aula 07"]
date_created: 2026-11-19
date_updated: 2026-11-20
source_count: 0
tags: [performance, animacao, rendering-pipeline, layout, paint, composite, transform, opacity, will-change, compositor-thread, main-thread, 60fps, gsap, loading-screen, mobile, curso, frontend]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-19
---

# Otimização de animações: pipeline de renderização, transform, opacity e a thread do compositor (FrontPUSH)

## TL;DR

Aula 07 do módulo de otimização do [[wiki/entities/frontpush|FrontPUSH]], cerca de 21,5 min. Encerra o módulo. O autor é [[wiki/entities/nasser|Násser]]: ele não diz o nome, mas a autoria se apoia na sequência das aulas, no "eu coloco nos meus websites" e nos projetos Spider-Man e "Paybank". Ele resume artigos do Notion, principalmente o do web.dev sobre animações de alto desempenho.

- **Animação comunica** e guia a atenção, como a cor. Não deve ir "em tudo que é canto".
- **Tela de carregamento:** ele sempre põe uma. Ela dá feedback e "tempo do website montar" em conexão ruim ou celular fraco. É feita com [[wiki/entities/gsap|GSAP]] e uma timeline, como nos projetos [[wiki/entities/spider-man-projeto-nasser|Spider-Man]] e "Paybank" ([[wiki/concepts/feedback-do-sistema]]).
- **Teste no celular:** "teste, teste, teste". Ele abre o Live Server do VS Code no celular pela mesma rede. O mobile é "50% ou mais" dos acessos. Se a animação continua travando, "capa no celular": deixa estática ou usa `display: none`.
- **60 fps = 16,6 ms por quadro** ([[wiki/concepts/taxa-de-quadros-60fps]]). O pipeline é estilo → layout → pintura → composição, e ele diz que o navegador passa pelas quatro etapas "toda vez que ele renderiza" ([[wiki/concepts/critical-rendering-path]], [[wiki/concepts/reflow-layout]], [[wiki/concepts/paint-composite]]).
- **`transform` × `width`:** `scaleX(2)` e `width` de 64 para 128 px dão "o mesmo efeito", mas `width` muda a geometria e custa mais. O `transform` "guarda a original". `opacity` também não mexe na geometria ([[wiki/concepts/transition-e-transform-css]]).
- **Mas `transform` "não é tão performático quanto o opacity":** muitos elementos com `translate` "pode[m] ter queda de frame do mesmo jeito". `will-change` "força a criação da camada".
- **Bom senso > técnica:** "no frigir dos ovos", as otimizações "não vão fazer muita diferença" quando há animação demais.
- **CSS antes de JS:** a animação CSS roda na thread do compositor, separada da thread principal (estilo, layout, pintura, JS). Na explicação dele, a thread principal "é mais importante" e "passa na frente", então tarefas caras nela interrompem as animações ([[wiki/concepts/thread]], [[wiki/concepts/concorrencia]], [[wiki/concepts/event-loop-performance-js]]).

## Key Claims

- **Animação é comunicação.** "As animações, elas são recursos para poder desviar ou então guiar a atenção do usuário da maneira correta", "assim como a gente utiliza as cores"; usá-las "em tudo que é buraco [...] ao invés de ajudar, faz atrapalhar."
- **Tela de carregamento evita site "montado às coxas".** "Dar esse feedback para o usuário de que, ei, só aguardar um pouquinho [...] e além disso, dar um tempo do website montar e evitar que ele seja montado de maneira errada" com conexão ruim ou "uma GPU um pouquinho mais lenta". "Muitíssimo fácil": GSAP e uma timeline.
- **Desktop esconde o problema.** O computador tem "hardware que não é minificado como o do celular", "uma zona de dissipação maior"; por isso o Google separa a análise de computador e mobile, que é "conta de padaria, 50% ou mais dos acessos".
- **Teste em aparelho real.** "Eu não simulo ele somente aqui no desktop [...] você entra na mesma rede pelo seu celular, acessa ali o live server que você faz pelo próprio Visual Code".
- **Ordem: otimizar, depois cortar.** "A primeira coisa é tentar otimizar [...] Não deu certo, continuou travando, então capa no celular", deixando estático ou com `display: none` (o recurso das [[wiki/sources/frontpush-otimizacao-de-imagens-mobile-desktop-classes-mixin|classes `.desktop`/`.mobile`]]).
- **Orçamento de quadro.** "É amplamente aceito uma taxa de quadro de 60 fps"; "se o quadro não for concluído em 16.6 milissegundos, os usuários perceberão um atraso."
- **Quatro etapas, sempre.** "Primeiro lugar, estilo. Segundo lugar, layout. Terceiro lugar, pintar. E quarto lugar, composto"; layout "gere a geometria" (borda, círculo, border-radius); pintar é "preencher os pixels em camadas"; composição ordena camadas (ele cita `z-index`). "Toda vez que ele renderiza, ele vai passar por esses quatro pontos nessa ordem."
- **Transform preserva a original.** "É mais barato para o browser você pegar uma determinada geometria que está original e você alterar ela, mas guardar a geometria original, do que você mudar a geometria original." O artigo pede "somente essas três características"; "é obrigatório? Não. Mas são as que têm mais desempenho."
- **Sombra e gradiente custam.** Um quadrado vermelho de 64×64 é renderização "básica"; sombra pede "mais camadas para poder deixar a sombra mais real", que "vai gastar mais pixels" e "demorar mais para renderizar".
- **`width` é o mais custoso.** "Se eu trocar o width de 64 para 28 [*sic*, 128], ele vai ter o mesmo efeito de eu colocar um transform de 1 para 2 no scaleX [...] por incrível que pareça, o mais custoso é o width."
- **`transform` não é tão leve quanto `opacity`.** "Isso não significa dizer [...] que o transform é tão performático quanto o opacity. Isso é um engano"; "ele sempre vai precisar renderizar novamente, quando você modificar a geometria e a posição", e vários elementos com `translate` "pode ter queda de frame do mesmo jeito".
- **`will-change` avisa antes.** "Você força a criação da camada. Então, meio que você avisa para o CSS, olha só, ele vai mudar. Qual a propriedade? O transform."
- **Bom senso vence.** "Eu já utilizei um site [...] com animações exageradas [...] utilizei dessas técnicas aqui e continuo dando queda de frame do mesmo jeito."
- **CSS é o mais barato.** "Priorize o CSS puro"; "ele é nativo, ele é direto, e ele utiliza uma thread diferente daquela principal"; JS faz animações "mais complexas" e "de forma mais fácil", mas para microinteração, CSS.
- **Thread principal "passa na frente".** "Aquilo que é executado na thread principal, ele tem um caráter de importância [...] mais importante do que a thread do compositor [...] ela vai passar na frente. Por isso que JavaScript está na thread principal." E: tarefas caras na principal "pode[m] atrapalhar na outra thread".
- **Processador, uma tarefa por vez.** "Ele processa uma tarefa de cada vez. O que nos dá a impressão de ele ser multitarefas é que ele executa uma tarefa muito rápido"; threads como "caminho virtual" que permite "executar coisas em paralelo", "o famigerado paralelismo".

## Entities

- [[wiki/entities/nasser]]: instrutor; autoria pela sequência e pelos projetos próprios.
- [[wiki/entities/frontpush]]: curso; aula 07, a última do módulo de otimização.
- [[wiki/entities/gsap]]: timeline da tela de carregamento.
- [[wiki/entities/spider-man-projeto-nasser]]: projeto com tela de carregamento.
- [[wiki/entities/google]]: análise separada de mobile e desktop no PageSpeed; web.dev como fonte do artigo.

## Concepts

- [[wiki/concepts/taxa-de-quadros-60fps]]: 60 fps, 16,6 ms, queda de frame.
- [[wiki/concepts/critical-rendering-path]], [[wiki/concepts/reflow-layout]], [[wiki/concepts/paint-composite]]: estilo → layout → pintura → composição.
- [[wiki/concepts/transition-e-transform-css]]: `transform`, `opacity`, `will-change`.
- [[wiki/concepts/mobile-animacoes-performaticas]]: animar no celular.
- [[wiki/concepts/thread]], [[wiki/concepts/concorrencia]], [[wiki/concepts/paralelismo]]: thread principal × compositor; "uma tarefa de cada vez".
- [[wiki/concepts/event-loop-performance-js]]: tarefas longas na thread principal.
- [[wiki/concepts/gpu]]: composição de camadas.
- [[wiki/concepts/feedback-do-sistema]]: tela de carregamento.
- [[wiki/concepts/core-web-vitals]]: loader × LCP; animação em JS × INP.
- [[wiki/concepts/acessibilidade]]: `prefers-reduced-motion`, ausente.

## Precisões e tensões com a wiki

- **A thread principal não "passa na frente" do compositor; a explicação está invertida.** O artigo do web.dev diz o contrário do que a aula lê: se a thread principal estiver ocupada com tarefas caras, as animações do compositor "podem continuar sem ser interrompidas" (no original, *these animations can keep going without being interrupted*; sem fetch nesta sessão). Essa é a vantagem do compositor. As threads não têm prioridade uma sobre a outra; são independentes. O compositor só precisa da thread principal quando algo muda o layout ou a pintura. O JavaScript não fica na thread principal por ser "mais importante": fica lá porque mexe no DOM, que só a thread principal toca (cálculo pesado vai para Web Workers) ([[wiki/concepts/thread]], [[wiki/concepts/event-loop-performance-js]]). Confiança alta.
- **Nem todo quadro passa pelas quatro etapas; esse é o ponto do artigo.** O pipeline completo é JavaScript → estilo → layout → pintura → composição, e há três caminhos. Mudar `width` ou `top` refaz layout, pintura e composição. Mudar `color` ou `box-shadow` refaz pintura e composição. Mudar `transform` ou `opacity` de um elemento em camada própria só refaz a composição ([[wiki/concepts/paint-composite]], [[wiki/concepts/reflow-layout]]). `[external]` https://web.dev/articles/rendering-performance. Confiança alta.
- **`transform` e `opacity` estão na mesma classe de custo.** Os dois são composição pura quando o elemento já tem camada. O `translate` não "renderiza novamente" a geometria: os outros elementos não se movem e não há layout. A queda de frame com muitos elementos em `translate` vem de outros fatores:
  - camadas demais ou grandes demais (memória de GPU);
  - elementos sem camada, que repintam;
  - animação dirigida por JavaScript a cada quadro, que volta para a thread principal.

  Confiança alta.
- **A explicação "guarda a geometria original" chega perto, mas o mecanismo é outro.** O `transform` não entra no layout: a caixa continua ocupando o espaço original no fluxo, e a GPU transforma a camada já pintada. Por isso `scaleX(2)` não dá "o mesmo efeito" que `width: 128px`. A escala estica o conteúdo (texto e borda distorcem, a imagem pode borrar) e não empurra os vizinhos. Confiança alta.
- **Animação CSS não é automaticamente do compositor.** Só `transform`, `opacity` (e, em alguns navegadores, `filter`) animam fora da thread principal. Um `@keyframes` que anima `width`, `top` ou `box-shadow` roda na thread principal igual a JS. "Navegadores que suportam a API" fala da Web Animations API: `element.animate()` em JS também vai para o compositor com `transform`/`opacity`. Já o GSAP escreve estilo inline a cada quadro pela thread principal (`requestAnimationFrame`), então a tela de carregamento com timeline do GSAP não roda no compositor ([[wiki/entities/gsap]]). Confiança alta.
- **`will-change` é dica, e tem custo.** Ele pede ao navegador que promova o elemento para camada própria antes da animação, evitando o "salto" do primeiro quadro. Cada camada gasta memória de GPU. Por isso vale aplicar em poucos elementos, pouco antes de animar, e remover depois; `will-change` em tudo piora. "Evite propriedades que acionem o layout ou a pintura" é outra recomendação do mesmo artigo, não parte do `will-change`. Confiança alta.
- **"Três características"?** O artigo atual do web.dev resume em `transform` e `opacity` ("stick to transform and opacity"). O texto clássico do html5rocks (Paul Lewis, 2013) listava quatro coisas baratas de animar: posição, escala, rotação e opacidade. As "três" da tela não ficam claras; talvez sejam `transform`, `opacity` e `will-change`. Confiança média.
- **16,6 ms é o teto, não o orçamento.** 1000/60 = 16,67 ms, mas o navegador tem trabalho próprio a cada quadro, e o web.dev recomenda cerca de 10 ms para o seu código. Telas de 90 e 120 Hz, comuns em celulares, baixam o quadro para 11 e 8,3 ms ([[wiki/concepts/taxa-de-quadros-60fps]]). Confiança alta.
- **Tela de carregamento tem custo nas Core Web Vitals.** Um loader que cobre a página esconde conteúdo que já chegou. O LCP mede quando o maior elemento *visível* aparece, então o loader atrasa o LCP, e um loader em JS (GSAP) ainda depende do download e da execução do script. As causas do site "montado às coxas" têm correção direta, sem esconder a página ([[wiki/concepts/core-web-vitals]]):
  - fonte trocando: `font-display`;
  - imagem sem `width`/`height`: CLS;
  - CSS que chega tarde: CSS crítico.

  Isso entra em tensão com as [[wiki/sources/frontpush-google-pagespeed-core-web-vitals-acessibilidade-meta-tags|aulas 05]] e [[wiki/sources/frontpush-relatorio-pagespeed-imagens-render-blocking-dom-regra-80-20|06]], que priorizam o primeiro carregamento. Loader faz sentido em web app ou experiência 3D que precisa baixar assets antes de funcionar ([[wiki/entities/axlepush|AxlePUSH]]). Confiança alta.
- **Animação dirigida por JS pesa no INP.** Trabalho de animação na thread principal compete com o tratamento de cliques: tarefas longas atrasam a resposta, e é isso que o INP mede ([[wiki/concepts/event-loop-performance-js]]). Confiança alta.
- **Falta `prefers-reduced-motion`.** Para "deixar estático" há um gatilho além do celular fraco: a preferência do sistema de reduzir movimento. `@media (prefers-reduced-motion: reduce)` (no GSAP, `gsap.matchMedia()`) desliga ou encurta animações para quem tem vestibulopatia ou enxaqueca (WCAG 2.3.3, AAA) ([[wiki/concepts/acessibilidade]]). Confiança alta.
- **"Uma tarefa de cada vez" vale por núcleo.** Um núcleo alterna tarefas rápido (concorrência por fatia de tempo). Processadores atuais têm vários núcleos, que executam ao mesmo tempo de verdade (paralelismo). Thread não existe "porque o processador é rápido"; é a unidade que o sistema agenda, e threads do mesmo processo compartilham memória ([[wiki/concepts/concorrencia]], [[wiki/concepts/paralelismo]]). "10 elevado a 9" é o giga de gigahertz: um ciclo leva menos de 1 ns, mas uma "tarefa" leva muitos ciclos. Confiança alta.
- **Testar no aparelho tem ferramentas além do Live Server.** O Live Server serve na porta 5500, e o celular abre `http://<IP-do-computador>:5500` na mesma rede. Também ajudam:
  - o throttling de CPU do Chrome DevTools (4× e 6×) e o painel Performance;
  - em Rendering, "Paint flashing", "Layer borders" e o medidor de FPS;
  - depuração remota do Android via USB (`chrome://inspect`).

  O PageSpeed mobile já emula um celular médio com CPU 4× mais lenta e 4G lento (sem fetch; confiança média-alta).
- **Mobile passa de 50%.** O tráfego web mundial em celular fica em torno de 60% desde 2023 (StatCounter; sem fetch; confiança média). O Google também indexa pela versão mobile (*mobile-first indexing*). "Minificado" na fala quer dizer miniaturizado: o celular dissipa menos calor e reduz o clock quando esquenta (*thermal throttling*).
- **Sombra animada repinta.** Animar `box-shadow` repinta a cada quadro. O truque comum é pôr a sombra num `::after` e animar só a `opacity` dele. Gradientes e sombras grandes aumentam a área de pintura, como ele diz ([[wiki/concepts/paint-composite]]). Confiança alta.
- **"W3C" deve ser o W3Schools.** A busca "scaleX CSS 2D transform" e a página com a lista de funções lembram o tutorial "CSS 2D Transforms" do W3Schools, que não é o W3C (consórcio que publica as especificações). Confiança média.
- **Lapsos e ASR.** "64 para 28" é 128 (dito certo antes). "Display nano" virou `display: none`. "Wheel change" virou `will-change`. "Paybank" ficou literal: provavelmente é o projeto Nubank, citado com o Homem-Aranha na [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss|aula de Sass]] (confiança média).

## Continuação: biblioteca ou CSS puro

A tensão GSAP × CSS puro desta aula vira tópico de módulo no mini curso de animação: "utilizar uma biblioteca ou CSS puro" ([[wiki/sources/frontpush-introducao-motion-design-css-animations-grade-do-curso]], [[wiki/concepts/motion-design]]).

## Open Questions

- Quais são as "três características" na tela do artigo?
- "Paybank" é o projeto Nubank ([[wiki/entities/nubank]]) ou outro projeto do curso?
- O loader do Spider-Man espera o `load` da página ou um tempo fixo? Quanto atrasa o LCP medido?

## Raw quotes

- "Em tudo que é canto, em tudo que é buraco, porque ao invés de ajudar, faz atrapalhar."
- "teste, teste, teste, teste, teste, teste"
- "Não deu certo, continuou travando, então capa no celular."
- "Por incrível que pareça, o mais custoso é o width."
- "No frigir dos ovos, pessoal, o que conta é o bom senso."
- "Priorize o CSS puro."
