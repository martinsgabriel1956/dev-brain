---
type: source
title: "Elementos da interface: ícones, parte 1 (conceito, comunicação, identidade visual e famílias de ícones)"
aliases: ["aula de ícones", "ícones parte 1", "iconografia", "iconografia em UI"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 0
tags: [ui, ui-design, design, elementos-da-interface, icones, iconografia, carga-cognitiva, padroes-de-interface, consistencia, identidade-visual, material-design, formas, acessibilidade]
skill: ux-ui-mentor
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/icones-parte-1-conceito-comunicacao-identidade-visual-familias.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-13
---

# Elementos da interface: ícones (parte 1)

## TL;DR

Aula teórica de [[wiki/entities/nasser|Násser]] sobre [[wiki/concepts/icones-em-interfaces|ícones]], no módulo de elementos da interface do [[wiki/entities/frontpush|FrontPUSH]]; a parte 2 (prática: grids, tamanho, como construir) fica para a aula seguinte. Slide: "um ícone é um símbolo, uma representação visual de um objeto, ação ou ideia usados em algum contexto para comunicar algo". Cinco ideias: (1) **ícone pode representar uma ideia, uma ação ou o próprio objeto**: a engrenagem não é sobre engrenagem, é "configuração"; o chip da Apple é literalmente o processador; (2) **o significado vem dos [[wiki/concepts/padroes-de-interface|patterns]]**: o usuário aprende engrenagem, sininho, "+", hambúrguer e nuvem porque os vê todo dia, mas há ícones abstratos que nem todos conhecem (a avó dele não reconheceu o "compartilhar" de três bolinhas); (3) **ícone [[wiki/concepts/simplicidade-visual|simples]] reduz a [[wiki/concepts/carga-cognitiva]]**, e ícone ao lado do texto em tópicos deixa a interface mais leve (site da Apple); (4) **[[wiki/entities/material-design]]**: ícones de sistema "simple, modern, friendly", sem detalhe demais, geométricos e com [[wiki/concepts/consistencia-visual|shapes consistentes]]; (5) **o estilo do ícone segue a identidade visual** e se usa **uma [[wiki/concepts/familia-de-icones|família de ícones]]** por projeto: [[wiki/entities/iconly]] arredondado e preenchido no [[wiki/entities/creatorpush|Creator Push]] (amigável), linha do [[wiki/entities/feather-icons]] no FrontPUSH (mais firme e profissional).

## Key Claims

### O que é um ícone

- **Definição do slide:** "Um ícone é um símbolo, uma representação visual de um objeto, ação ou ideia usados em algum contexto para comunicar algo. Os ícones do sistema simbolizam ações, arquivos, dispositivos e diretórios comuns." Ver [[wiki/concepts/icones-em-interfaces]].
- **Nem sempre é literal.** Para um substantivo abstrato (amor), "duas pessoas e um coraçãozinho no meio" até comunica, "porém ele não é simples".
- **Simplicidade máxima**, princípio "lá atrás" ([[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]]), para "reduzir a carga cognitiva". Ver [[wiki/concepts/simplicidade-visual]] e [[wiki/concepts/carga-cognitiva]].

### Padrões aprendidos

- **"O ser humano é movido por padrões."** Quem usa o [[wiki/entities/google]] todo dia sabe que a engrenagem configura e que os "nove pontinhos" abrem os apps do Google; repetido, vira pattern. Ver [[wiki/concepts/padroes-de-interface]] e [[wiki/concepts/reconhecimento-de-padroes]].
- **Exemplos de ícone-ideia:** sininho → notificações; arroba → e-mail ou usuário; box → 3D, cubo, módulo; "+" → adicionar (no Instagram: story, publicação, Reels).
- **Ícones mais abstratos:** o "compartilhar" de três bolinhas. "Teste de usabilidade com a minha vó": ela não o reconhecia; identificava melhor a "setinha indo assim para fora".
- **Três pontinhos x três tracinhos.** O "more vertical" abre mais opções; os três tracinhos (hambúrguer) dizem "isto é um menu", e a maioria dos sites mobile os usa quando o menu é comprimido.
- **Nuvem = internet.** O ícone "fiel" seria computadores ligados por fios, complexo demais; a metáfora da nuvem "acima de nós" também explica download (puxa para baixo) e upload.
- **"Pistas visuais, senso comum de ícones"** (slide): o uso amplo cria o pattern, e "eu já entendo o que aquele ícone pode fazer".

### Objeto x ação

- **Ícone que representa o objeto:** CPU, chip, hardware. Exemplo hipotético: na Apple, anunciar o processador do novo iPhone com um ícone de chip.
- **"É diferente do engrenagem, que ele já está convidando para uma ação."** Nos dois casos, "sempre é para comunicar alguma coisa".
- **O retroprojetor em japonês:** sem entender a língua, ele achou como trocar o idioma "me guiando pelos ícones". Os ícones "comunicam de forma universal determinadas coisas", ressalvando que "pode depender da cultura".

### Ícones acompanhando o texto (site da Apple)

- **O ícone complementa o que o usuário vê e "auxilia na tomada de ação".**
- **Na seção analisada**, o título vem antes por tamanho, posição (em cima, à esquerda) e cor mais viva; a descrição fica em cor neutra; e "ele acompanha sempre um ícone aqui do lado". Ver [[wiki/concepts/hierarquia-visual]].
- **Exemplos:** acessibilidade, acessórios, visualizar em 3D (AR), câmera de 12 MP, vídeo, "cinco cores de GPU" com ícone de velocidade, o chip A15 "do próprio iPad".
- **"O ser humano [...] é extremamente visual"**: com ícone, a informação passa "bem mais rápido". Tópicos são mais fáceis de ler que um bloco de texto, e tópicos com ícone "comunicam bem mais". "Ponto importante para você deixar sua interface um pouco mais leve é atrelar itens [...] junto a ícones."

### Material Design: simplicidade e consistência

- **Recomenda ler a página de iconografia do [[wiki/entities/material-design]]** (link na descrição da aula).
- **"System icons are designed to be simple, modern, friendly and sometimes quirky."** Nos exemplos de fazer e não fazer: câmera com detalhe demais; o like não precisa da "onduração dos dedos" nem da unha do polegar. "Sempre deixe ele geométrico em shapes consistentes."
- **Icon design templates e icon size** são padronização, tratados na parte prática.
- **"Consistência, estou sempre batendo na tecla":** em ilustrações, tipografia, cores, tamanhos e shapes. Se a família usa formas regulares (círculo, quadrado, pentágono, triângulo), uma curva aleatória "desconecta". Ver [[wiki/concepts/consistencia-visual]] e [[wiki/concepts/formas-geometricas-e-organicas]].
- **Grids para construir ícones** ficam para a aula seguinte.

### Padronização de identidade visual

- **Liga com a aula de formas:** arestas retas passam uma sensação; arredondar "ameniza", fica mais amigável ([[wiki/sources/formas-geometricas-organicas-predominancia-harmonia]], [[wiki/sources/formas-exemplos-praticos-radius-consistencia-projetos]]).
- **Ícones "se alinham à identidade visual"**, à sensação da marca, empresa, produto ou serviço.
- **Demonstração no [[wiki/entities/figma]]:** plugin [[wiki/entities/iconly]] v2.3 contra [[wiki/entities/feather-icons]] (telefone, câmera, user). Um tem traços mais retos e "abruptos", com "sobriedade"; o outro é mais arredondado, amigável e **preenchido**, enquanto o primeiro é **vazado** (feito pela stroke). Isso introduz a **classificação de ícones** (linha x preenchido). Ver [[wiki/concepts/familia-de-icones]].
- **"Para os meus projetos eu utilizo muito elementos de linha."** O preenchido entra quando a interface é mais amigável e se quer "dar mais cor" e destacar o ícone.
- **Creator Push x FrontPUSH:** no style guide do [[wiki/entities/creatorpush|Creator Push]], família mais arredondada, porque o produto foi desenhado para ser amigável e "mais perto das pessoas"; no FrontPUSH, um ar "mais firme, [...] mais exato, [...] mais profissional".
- **Não é regra rígida:** sensação amigável não proíbe ícone de linha; é "um dos pontos que você deve alinhar".

### Família de ícones

- **Mesmo raciocínio das ilustrações** ([[wiki/concepts/ilustracoes-em-interfaces]]): "foi o mesmo cara que fez com o mesmo traço".
- **Feather Icons como exemplo de família:** todos de linha, stroke width 2, nenhum traço "extremamente reto", cantos arredondados em todos.
- **O Iconly tem várias famílias:** bold, bulk, light ("são os de linha do bulk", fala ambígua; ver open questions).
- **Links de famílias no Notion do curso.** "Aquela regra de sempre": escolher uma família conectada à identidade visual e usar só ela ao longo da interface, para "harmonizar todos os elementos". Ver [[wiki/concepts/harmonia-visual]].
- **Biblioteca própria "exige estudo, não recomendo para iniciantes"**; princípios na aula 2.

## Entities

- [[wiki/entities/nasser]]: autor ("Násser aqui").
- [[wiki/entities/feather-icons]] (novo): família de linha, stroke 2, cantos arredondados; usada no FrontPUSH.
- [[wiki/entities/iconly]] (novo): plugin v2.3, famílias bold, bulk, light; arredondado e preenchido no Creator Push.
- [[wiki/entities/material-design]]: página de iconografia.
- [[wiki/entities/google]]: engrenagem e "nove pontinhos" como pattern aprendido.
- [[wiki/entities/frontpush]] e [[wiki/entities/creatorpush]]: os dois projetos comparados.
- [[wiki/entities/figma]]: onde roda o plugin do Iconly.
- Sem página própria: Apple (site do iPhone/iPad), Instagram ("+"), Notion.

## Concepts

- [[wiki/concepts/icones-em-interfaces]] (novo)
- [[wiki/concepts/familia-de-icones]] (novo)
- [[wiki/concepts/carga-cognitiva]]
- [[wiki/concepts/simplicidade-visual]]
- [[wiki/concepts/padroes-de-interface]]
- [[wiki/concepts/reconhecimento-de-padroes]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/formas-geometricas-e-organicas]]
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/harmonia-visual]]
- [[wiki/concepts/ilustracoes-em-interfaces]]

## Tensões com a wiki

- **"Ícones comunicam de forma universal" x NN/g.** O próprio Násser ressalva cultura e mostra que a avó não reconhece o "compartilhar". `[external]` A Nielsen Norman Group vai além: ícones "universais" são raros (casa, impressora, lupa); a maioria é ambígua, até o hambúrguer às vezes significa lista, e por isso ícones precisam de rótulo de texto. Também sugere a "regra dos 5 segundos" (se você leva mais de 5 s para pensar num ícone, ele provavelmente não comunica) e testar o reconhecimento com usuários (https://www.nngroup.com/articles/icon-usability/). O padrão da Apple mostrado na aula, ícone + título + descrição, é exatamente ícone com rótulo.
- **O "compartilhar" depende da plataforma** (inferência do agente): as três bolinhas ligadas são o share do Android/Material; a "setinha indo para fora" lembra o share do iOS (caixa com seta para cima). A avó provavelmente reconhecia o padrão do aparelho que usa, o que reforça "pattern aprendido", não "universal".
- **Ícone sozinho precisa de nome acessível.** `[skill: ux-ui-mentor]` Ícone funcional sem texto visível leva `aria-label` no elemento pai (ou `title` no SVG); ícone informativo pede contraste mínimo de 3:1; alvo de toque de pelo menos 44×44 px, "nunca ícones de 16px clicáveis sozinhos"; em idiomas RTL, ícones direcionais (setas, chevrons) espelham e os não direcionais (engrenagem, coração) não. Ver [[wiki/concepts/texto-alternativo]].
- **FrontPUSH "reto" x "nenhum totalmente reto".** Aqui o FrontPUSH tem os ícones de traço "mais reto" e "abrupto"; em [[wiki/sources/formas-exemplos-praticos-radius-consistencia-projetos]], "nenhum é totalmente reto" e até os quadrados têm "bordinhas arredondadas". Não é contradição: o próprio Násser diz que o Feather tem cantos arredondados em todos os ícones. "Reto" é relativo à comparação com o Iconly.
- **Fecha a pendência da aula de princípios.** Em [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]], a escolha entre as variações do Iconly "fica para a aula de ícones"; aqui a resposta é: escolha pela identidade visual (linha = sóbrio, preenchido e arredondado = amigável) e use uma só.
- **Feather Icons conferido.** `[external]` O README diz que cada ícone é desenhado num grid de 24×24 "with an emphasis on simplicity, consistency, and flexibility", e os SVGs usam `stroke-width="2"`, `stroke-linecap="round"` e `stroke-linejoin="round"` (https://github.com/feathericons/feather), confirmando "stroke 2" e "cantos arredondados".
- **Material Design não verificado.** A página de ícones de sistema do M2 (https://m2.material.io/design/iconography/system-icons.html) não traz o texto no HTML estático, como já tinha acontecido com a de imagens; a citação fica como lida pelo autor na tela.

## Open Questions

- **"Onduração dos dedos"**: provável "ondulação"; mantido literal.
- **"Tem o light, são os de linha do bulk"**: fala ambígua; o Iconly tem estilos light, bold, bulk, broken, two-tone e curved, e a wiki já registrava as variantes ([[wiki/concepts/consistencia-visual]]). Não ficou claro a qual ele se refere.
- **Qual dos dois ícones ele chama de "reto" e qual de "arredondado"** na demonstração? Pela sequência (linha nos projetos dele, preenchido no Creator Push), o Feather é o mais "sóbrio" e o Iconly o mais amigável; inferência, porque a fala usa só "esse aqui".
- **"Cinco cores de GPU"**: "cores" em inglês (núcleos), mantido literal.
- **Quais famílias estão no Notion do curso?** Não ditas.
- `date_published` vazio.

## Continuação

A parte 2 saiu: [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]] (preenchido x linha como hierarquia, tamanho, simetria, [[wiki/concepts/grid-de-icones|grid]], constraints e componentes). A pendência "grids para construir ícones fica para a aula seguinte" está fechada; o "icon size" do Material foi conferido no M3 (24dp, live area 20dp).

## Raw Quotes

> "O ser humano é movido por padrões, principalmente quando a gente fala de interfaces."

> "Já estou falando aqui de teste de usabilidade com a minha vó."

> "Sempre deixe ele geométrico em shapes consistentes."

> "Escolher uma família de ícones que está conectada com aquilo que você quer transportar."

## Ver também

- [[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia]] — a mesma aula teórica na edição "W7": senso comum, dicas (clareza, legibilidade, alinhamento, personalidade), no máximo duas famílias
