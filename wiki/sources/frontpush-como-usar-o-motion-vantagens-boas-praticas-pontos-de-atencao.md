---
type: source
title: "Como usar o motion: vantagens, boas práticas e cuidados (FrontPUSH)"
aliases: ["FrontPUSH motion aula 02", "Como usar o motion?", "Vantagens e boas práticas do motion", "CSS Animations, aula 02"]
date_created: 2026-11-20
date_updated: 2026-11-20
source_count: 0
tags: [motion-design, animacao, microinteracao, pontos-de-atencao, hierarquia-visual, contraste, feedback, hover, svg, performance, curso, frontend, ux]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-como-usar-o-motion-vantagens-boas-praticas-pontos-de-atencao.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-20
---

# Como usar o motion: vantagens, boas práticas e cuidados (FrontPUSH)

## TL;DR

Aula 02 do mini curso de CSS Animations do [[wiki/entities/frontpush|FrontPUSH]], cerca de 13,5 minutos, teórica, com slide e demonstrações no site pessoal de [[wiki/entities/nasser|Násser]] (a legenda o chama pelo nome duas vezes). É o tópico "Vantagens e boas práticas motion" da grade da aula 01 ([[wiki/sources/frontpush-introducao-motion-design-css-animations-grade-do-curso]]).

- **Para que serve:** o [[wiki/concepts/motion-design|motion]] cria **pontos de atenção** e guia o usuário na jornada; animação "não [é] puramente estética". O olho vai para o que se move, porque a visão periférica percebe movimento rápido.
- **Erro e feedback:** vermelho, vibração e piscar chamam o usuário para o que precisa ser corrigido; exemplo da senha errada que faz o celular vibrar ([[wiki/concepts/feedback-do-sistema]]).
- **[[wiki/concepts/microinteracao|Microinterações]]:** "as formas de um sistema responder a ação de um usuário". No site dele: botão que cresce e ganha sombra no hover, barrinha que cresce sob os links do menu ([[wiki/concepts/affordance]]).
- **Regra principal: "não coloque motion em tudo".** Motion funciona por [[wiki/concepts/contraste]], como a [[wiki/concepts/hierarquia-visual]] do texto: com tudo se mexendo, "não tem contraste" e o usuário perde o foco.
- **Valor:** diferencial "no mar de páginas estáticas", agrega valor, permite "cobrar mais"; o site animado já lhe trouxe clientes. Animações escondidas dão "sentimento de descoberta" e prendem o usuário.
- **O preço:** "o sistema pode ficar mais lento". O site dele é exagerado de propósito, porque "esse é o meu produto"; compensa com [[wiki/concepts/formato-svg|SVG]] e o mínimo de imagens.
- **Identidade:** SVG desenhado em linhas conforme o scroll "cria identidade" ([[wiki/concepts/identidade-visual]]). Exemplos ficam no Notion do curso.

## Key Claims

### Motion guia e cria pontos de atenção

- "As animações cumprem um papel muito importante na tela." O motion vem "com força e com muita tendência em 2020, em 2021", em slides, interfaces e apps.
- Atenção é "o maior ativo das pessoas hoje nas redes sociais" (stories). "As pessoas tendem a prestar mais atenção nos pontos onde tem movimento, cria ponto de atenção." As animações "não são puramente estéticas, elas ajudam a direcionar o olhar do usuário, guiar o usuário na sua jornada".
- Exemplo do e-commerce: cadastro, CPF, dados pessoais e bancários, endereço, escolha e quantidade de produtos ("não necessariamente na ordem"). "Para você guiar ele da melhor forma possível, é legal você criar pontos de atenção."
- Erro vermelho, celular que vibra, informação que pisca: "está chamando a atenção do usuário do que ele precisa fazer". Senha errada no celular: "ele vibra, ele está te dando alguma informação"; a animação "facilita o usuário perceber o que precisa ser corrigido". Ver [[wiki/concepts/feedback-do-sistema]].
- Por que funciona: "pelo fato de a gente ter uma visão periférica, qualquer movimentação fora do nosso foco é rapidamente percebida pelo cérebro".

### Microinterações

- "Microinterações, que são as formas de um sistema responder a ação de um usuário, então quando eu clico em algum lugar, quando eu passo o mouse, ele me responde de alguma forma que aquilo ali é um item clicável." Ver [[wiki/concepts/microinteracao]].
- No botão do site, o design já diz que é clicável (contraste, "cara de botão", call to action claro). A microinteração é "mais um indicativo": no hover "ele cresce, ele coloca uma sombra". Ver [[wiki/concepts/botoes-em-interfaces]] e [[wiki/concepts/affordance]].
- Nos links do menu, uma barrinha cresce no hover: "estou dando informação para o usuário de que é um item clicável, de que é um link".

### Não coloque motion em tudo

- "Se o meu grande objetivo é criar pontos de atenção [...] eu presto atenção naquilo que tem contraste, se tem um monte de coisa movimentando na minha tela, onde eu vou prestar atenção? [...] o grande lance é ter foco."
- Analogia com a hierarquia do texto: o título é lido primeiro porque é branco, maior e os outros estão em cinza; "o motion é exatamente a mesma coisa". O foco vem do "contraste de estar em uma tela totalmente fixa, totalmente estática e algo se movimentando". Ver [[wiki/concepts/hierarquia-visual]] e [[wiki/concepts/contraste]].
- Autocrítica: "talvez eu tenha carregado um pouco nessa minha página inicial, talvez tenha sido um erro", mas a animação de abertura é mais leve, uma é "mais agressiva" e o resto da página fica parado; o texto só entra quando se rola até ele.

### Diferencial e valor

- "O motion é um grande diferencial no mar de páginas estáticas." Agrega valor ao produto, eleva o nível das interfaces, permite "até cobrar mais", leva "a outro patamar de profissionalismo", porque "não é todos que sabem executar".
- "Eu já consegui clientes de cara só pelas minhas páginas serem bem aplicadas o motion."
- "Sentimento de descoberta": num site "carregado de motion", as pessoas "passam um pouco mais de tempo [...] porque pode ter alguma animação escondida", pela "curiosidade do ser humano".

### O preço

- "A grande sacada mesmo é você colocar onde ajuda o usuário, porque o preço que você paga pelo motion é [...] o sistema pode ficar mais lento, que é o caso da minha página."
- Por que o site dele exagera: "porque esse é o meu produto"; "por ser o meu site pessoal, eu preciso demonstrar [...] que eu sei mexer". Otimiza com "SVGs em todas as minhas páginas" e "o mínimo de imagem".
- Sites no Notion do curso: no scroll, "ele vai construindo esse SVG em forma de linhas"; "cria identidade, [...] dependendo da animação que você aplica". Um projeto recente dele vai trabalhar isso.

### O slide

"Vantagens e boas práticas do motion", com a nota "São argumentos para agregar mais valor nas suas interfaces" e o item "Vantagens e cuidados": guiar o usuário na sua jornada; não coloque motion em tudo (→ serve para criar pontos de atenção; você presta atenção naquilo que está em contraste; se colocar motion em tudo, não tem contraste); é um diferencial num mar de páginas estáticas; consegue agregar mais valor no seu produto; te leva a outro patamar de profissionalismo e domínio; ajuda na compreensão de tarefas; consegue prender mais o usuário (→ dá o sentimento de descoberta); microinterações e respostas: não deve ser puramente estético; coloque onde ajude o usuário, caso contrário o sistema pode ficar mais lento; "É legal..."; "[...]". "Ajuda na compreensão de tarefas" não tem fala própria; o exemplo do e-commerce chega perto.

## Entities

- [[wiki/entities/nasser]]: instrutor; site pessoal como vitrine de motion.
- [[wiki/entities/frontpush]]: curso; mini curso de CSS Animations.

## Concepts

- [[wiki/concepts/motion-design]]: para que serve e quando não usar.
- [[wiki/concepts/microinteracao]]: resposta do sistema à ação do usuário (página criada nesta ingestão).
- [[wiki/concepts/feedback-do-sistema]]: erro em vermelho, vibração, piscar.
- [[wiki/concepts/affordance]]: hover como reforço de "clicável".
- [[wiki/concepts/botoes-em-interfaces]]: botão que cresce com sombra.
- [[wiki/concepts/hierarquia-visual]]: motion segue a mesma lógica do texto.
- [[wiki/concepts/contraste]]: contraste de movimento.
- [[wiki/concepts/identidade-visual]]: animação cria identidade.
- [[wiki/concepts/formato-svg]]: SVG para otimizar e desenhar no scroll.
- [[wiki/concepts/acessibilidade]]: piscar, vermelho e movimento.
- [[wiki/concepts/taxa-de-quadros-60fps]]: o "preço" em desempenho.

## Precisões e tensões com a wiki

- **Erro só em vermelho não basta.** "Informação visual em vermelho com cores que remetem que alguma coisa deu erro": cor não pode ser o único sinal. `[external]` WCAG 1.4.1 (Use of Color, A) e 3.3.1 (Error Identification, A) pedem o erro identificado em texto, com ícone ou mensagem ([[wiki/concepts/acessibilidade]]). Confiança alta.
- **Piscar tem limite.** `[external]` WCAG 2.3.1 (Three Flashes, A): nada pisca mais de três vezes por segundo; 2.2.2 (Pause, Stop, Hide, A): conteúdo que pisca ou se move por mais de 5 s precisa de controle. E `prefers-reduced-motion` continua fora do curso; a aula 01 já anotou a ausência. Confiança alta.
- **Vibração na web.** O exemplo é de celular nativo. `[external]` Na web, a Vibration API (`navigator.vibrate`) não existe no Safari/iOS; o equivalente visual é o "shake" do campo, que deve vir com texto. Confiança média-alta, sem fetch.
- **Visão periférica e movimento.** Correto: a periferia da retina tem pouca resolução de detalhe e alta sensibilidade a movimento, e o início de um movimento captura a atenção (Abrams e Christ, 2003). É também por isso que movimento demais distrai. `[external]` sem fetch; confiança alta no fenômeno, média na citação.
- **Microinteração tem nome e estrutura.** `[external]` Dan Saffer, *Microinteractions* (O'Reilly, 2013): gatilho, regras, feedback, loops e modos. A definição de Násser cobre o feedback; o gatilho também pode ser do sistema (notificação). Confiança alta. Ver [[wiki/concepts/microinteracao]].
- **Hover não existe no toque.** O reforço de "clicável" pelo hover some no celular; o design de repouso precisa bastar, como ele mesmo diz do botão ([[wiki/concepts/affordance]]). `[skill: tech-mentor-frontend]` Animar `box-shadow` repinta a cada quadro; o truque comum é animar a `opacity` de um pseudo-elemento com a sombra pronta, e a barrinha do menu com `transform: scaleX()` ([[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]]).
- **SVG nem sempre é o mais leve.** "Eu sempre coloco SVGs [...] para poder deixar o mais otimizado possível." Para ilustrações, sim; mas SVG inline com muitos nós infla o DOM, o aviso que a aula 06 de otimização mostrou ([[wiki/sources/frontpush-relatorio-pagespeed-imagens-render-blocking-dom-regra-80-20]]). Tensão.
- **"O sistema fica mais lento" depende do que se anima.** A aula 07 de otimização mostra que `transform`/`opacity` em CSS rodam no compositor; o preço maior está em animar layout, em JS na thread principal e em telas de carregamento que atrasam o LCP ([[wiki/concepts/taxa-de-quadros-60fps]]).
- **"Descoberta" × encontrabilidade.** Animação escondida funciona num portfólio, cujo objetivo é mostrar habilidade (ele mesmo separa "meu produto" do caso geral). Em produto, interação que só se descobre por acaso esconde funcionalidade. "Passar mais tempo no site" também pode ser sinal de confusão. Inferência; confiança média.
- **SVG desenhado no scroll.** `[skill: tech-mentor-frontend]` A técnica usual anima `stroke-dashoffset` sobre `stroke-dasharray` ligada à rolagem (GSAP ScrollTrigger ou, hoje, `animation-timeline: scroll()`/`view()` em CSS).
- **Data.** "Muita tendência em 2020, em 2021" situa a gravação por volta de 2021, coerente com o resto do FrontPUSH.

## Open Questions

- Que "projeto que eu fiz recentemente" vai trabalhar a identidade pela animação? Talvez o [[wiki/entities/spider-man-projeto-nasser|Spider-Man]] (inferência).
- Quais sites estão no Notion na lista "sites usando SVG"?
- "Ter no seu role": provável "rol" (lista de argumentos); deixado literal. "Deixou esse elemento em cool motion": provável "com motion"; deixado literal.
- Entre 11:20 e 11:29 a legenda fica 9 s sem texto, logo depois de "esse é o meu produto, entendeu?". Talvez uma pausa para demonstrar o site, talvez fala não transcrita.

## Raw quotes

- "não são puramente estéticas, elas ajudam a direcionar o olhar do usuário"
- "não coloque motion em tudo"
- "o grande lance é ter foco"
- "um grande diferencial no mar de páginas estáticas"
- "o preço que você paga pelo motion"
- "Porque esse é o meu produto, entendeu?"
