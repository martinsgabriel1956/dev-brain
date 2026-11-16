---
type: source
title: "Tipografia: negrito, itálico, tracking, kerning e maiúsculas"
aliases: ["aula 05 de tipografia", "negrito tracking kerning maiúsculas", "variáveis tipográficas"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 0
tags: [ui, ui-design, design, tipografia, peso-tipografico, tracking, kerning, letter-spacing, maiusculas, contraste, hierarquia-visual, figma, css, botoes]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/tipografia-negrito-italico-tracking-kerning-maiusculas.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-15
---

# Tipografia: negrito, itálico, tracking, kerning e maiúsculas

## TL;DR

Aula 05 do módulo de [[wiki/concepts/tipografia]] do curso [[wiki/entities/frontpush]] (edição "W7", de [[wiki/entities/nasser|Násser]]), a última das "variáveis tipográficas". É a primeira aula do módulo que entra na wiki; as aulas 03 (altura de linha e largura) e 04 (alinhamento e espaçamento) ainda não foram ingeridas. Cinco ideias: (1) **negrito e itálico são [[wiki/concepts/contraste]]**: um "pingo" de peso diferente num texto de peso uniforme puxa o olho, por isso vale para detalhes, não para períodos inteiros ([[wiki/concepts/peso-tipografico]]); (2) **[[wiki/concepts/tracking]]** é a distância igual entre todas as letras, e se abre quando o texto está todo em maiúsculas, em menus e botões; (3) **no [[wiki/entities/figma]], o Inspect mostra o [[wiki/concepts/css]]** (`letter-spacing`, `font-family`, `font-style`, `font-weight`), e o Figma só oferece pesos que a fonte tem, ao contrário do navegador, que "falsifica" o estilo que não foi carregado do Google Fonts ou do Adobe Fonts; (4) **[[wiki/concepts/kerning]]** é a distância entre dois caracteres específicos, coisa de logotipo, com o jogo KernType para treinar; (5) **[[wiki/concepts/texto-em-maiusculas|maiúsculas]]** no mesmo tamanho (16 px) já sobem a [[wiki/concepts/hierarquia-visual]], e andam junto com o tracking em [[wiki/concepts/botoes-em-interfaces|botões]], CTAs e links.

## Key Claims

### Negrito e itálico

- **Função: destacar.** "Lembre gente, sempre é contraste": cor, forma, tamanho e, na tipografia, negrito e itálico. Ver [[wiki/concepts/contraste]].
- **Mecanismo:** num texto todo no mesmo peso, "você coloca uma palavrinha em negrito [...] naturalmente o seu olho vai olhar para aquela palavrinha"; com o itálico acontece "da mesmíssima maneira". É "um pingo em meio a um universo diferente".
- **Dose:** "em detalhes, em pontos importantes"; negrito num período inteiro "não faz sentido, porque o contraste se dá justamente quando tem um detalhe".
- **Uso típico:** negrito "principalmente em títulos"; itálico "em e-mails, endereços", um destaque "um pouco mais sutil". Ver [[wiki/concepts/peso-tipografico]].

### Tracking

- **Definição:** "a distância entre letras"; o nome "não sugere", ele teve "que até pesquisar". Ver [[wiki/concepts/tracking]].
- **Para quê:** "define maior legibilidade e estilo dependendo da fonte". Não é para tudo, mas "quando você coloca elas todas em maiúsculas, é interessante você colocar uma maior distância".
- **Onde:** itens de menu ("a parte de links do seu site que teoricamente reúne as principais funcionalidades") e botões, sobretudo call to action. No próprio site, os botões estão "totalmente em maiúsculas e eu coloquei um letter spacing para poder chamar mais atenção".

### Figma, CSS e estilos falsos

- **Figma → CSS:** a configuração de tracking no Figma "é o letter-spacing, que é a propriedade lá do CSS". A aba **Inspect** mostra como escrever cada propriedade. Ver [[wiki/entities/figma]] e [[wiki/concepts/css]].
- **`em`:** o Inspect dá o letter-spacing em `em`, "uma unidade relativa que se baseia em 16 pixels", "meio que você quer 10% de 16 pixels".
- **`font-weight`:** é o peso; trocar para Medium muda o valor para 500. O peso "pode ser estabelecido de 100 até 700", escrito por número ou por nome; ele usa o número "na maioria das vezes", ou `bold`, que "sempre remete ao tamanho 700".
- **Estilo falso:** no Google Fonts ou no Adobe Fonts é preciso selecionar cada peso usado (ex.: light 300, regular e bold) antes de "fazer o link"; se esquecer algum e aplicá-lo no CSS, "ele vai se tornar falso". O Figma "se preocupa em ser real": só lista os pesos que a fonte tem. A Mukta tem extra light, light, regular, medium, semibold, bold e extra bold; outras fontes "são mais limitadas". Ver [[wiki/concepts/peso-tipografico]].
- **Justificado (de passagem):** na caixa de texto, o justificado deixa distâncias entre palavras de "X" e de "3, 4X"; por isso "a gente quase não usa o justificado", sempre alinhado à direita ou à esquerda.

### Kerning

- **Definição:** "a distância específica entre dois caracteres". O tracking aplica "exatamente a mesma distância" a todas as letras; o kerning ajusta um par. Ver [[wiki/concepts/kerning]].
- **Onde:** "muito utilizado em criação de marcas", sempre "em um pequeno trecho", nunca em corpo de texto.
- **Para quê:** aproximar de propósito duas letras "para poder fazer a ligatura", para que "se liguem e crie uma outra forma"; ou afastá-las "para poder criar personalidade e identidade".
- **Treino:** o site KernType (type.method.ac), onde se ajusta o kerning de palavras e confere em "Done".

### Maiúsculas

- **Efeito:** "geram maior contraste, maior hierarquia". Demonstração no Figma: o mesmo texto em 16 px, normal e em maiúsculas ("com case"); a versão em maiúsculas "já causa uma hierarquia maior". Ver [[wiki/concepts/texto-em-maiusculas]] e [[wiki/concepts/hierarquia-visual]].
- **Onde:** botões, call to action, links, "muito utilizado juntamente com o tracking para poder melhorar a legibilidade e definir estilo".

## Entities

- [[wiki/entities/nasser]]: autor. Logo "W7" no slide e pasta "FrontPush" do transcript; ele não diz o nome nesta aula.
- [[wiki/entities/frontpush]]: curso; "meu website" com botões em maiúsculas e letter-spacing é provavelmente a landing do FrontPUSH (inferência).
- [[wiki/entities/figma]]: Inspect, letter-spacing, pesos disponíveis por fonte.
- Sem página própria: Google Fonts, Adobe Fonts, Mukta, KernType (Method of Action).

## Concepts

- [[wiki/concepts/tipografia]]
- [[wiki/concepts/peso-tipografico]] (novo)
- [[wiki/concepts/tracking]] (novo)
- [[wiki/concepts/kerning]] (novo)
- [[wiki/concepts/texto-em-maiusculas]] (novo)
- [[wiki/concepts/contraste]]
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/botoes-em-interfaces]]
- [[wiki/concepts/css]]

## Tensões com a wiki

- **"De 100 até 700" x a própria Mukta.** A Mukta mostrada na aula tem extra bold, que é 800. `[external]` No CSS, `font-weight` aceita palavras-chave (`normal` = 400, `bold` = 700) e números de 1 a 1000 no CSS Fonts Level 4; as fontes costumam ir de 100 a 900 (https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight). Confiança alta. O "até 700" vale para muitas fontes, não como limite.
- **`em` não é "16 pixels".** `[external]` `em` é relativo ao `font-size` do próprio elemento; 16 px é só o padrão do navegador para o texto raiz (https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Values_and_units). Num botão de 14 px, `0.1em` dá 1,4 px. É justamente por isso que o tracking em `em` escala com a fonte. O Figma mostra o letter-spacing em %, e 10% equivale a `0.1em`. Confiança alta.
- **Kerning não faz ligatura.** `[external]` Ligatura é um glifo próprio que substitui dois caracteres (fi, fl); kerning só muda o espaço entre um par. Num logotipo, encostar letras até se fundirem é desenho de marca, não kerning de fonte. A aula junta as duas ideias. Confiança alta.
- **Itálico em e-mails e endereços.** A convenção não é comum. `[skill: ux-ui-mentor]` A skill lista itálico para "citações, ênfase, metadados". Tratar como preferência do autor.
- **Tracking aberto x apertado.** A aula só fala em abrir. `[skill: ux-ui-mentor]` Corpo de texto fica em 0, CAPS e labels abrem +0.05em a +0.1em, e títulos grandes (36 px+) apertam -0.02em a -0.04em. Os "10%" da aula batem com o limite superior para CAPS.
- **Maiúsculas e acessibilidade.** `[skill: ux-ui-mentor]` Maiúsculas cansam em blocos longos; ficam para labels curtos. `[external]` Escrever em minúsculas no HTML e usar `text-transform: uppercase` no CSS evita que leitores de tela soletrem palavras digitadas em caixa alta como siglas (comportamento varia por leitor; confiança média).
- **Justificado.** Concorda com a skill: `[skill: ux-ui-mentor]` "Evite texto justificado (cria rios de espaço em colunas estreitas)".

## Open Questions

- **Correções de ASR:** "passamento" → espaçamento (o slide tem a seção Espaçamento da aula anterior); "sem bold" → semibold.
- **"Só que com case":** provavelmente a opção Case (letter case) das configurações de texto do Figma; mantido literal.
- **"Fazer a ligatura":** mantido; ver Tensões.
- **Slide:** "Maiúsculas > Distância entre 2 caracteres" repete o subtítulo do Kerning; parece erro de cópia no slide. A seção Espaçamento do slide (line-height, quebrar a cada 4 a 8 linhas) é da aula 04, não desta.
- **Aulas 03 e 04** do módulo estão na pasta de transcrições mas não foram ingeridas.
- `date_published` vazio.

## Raw Quotes

> "Lembre gente, sempre é contraste."

> "Se você esquecer de algum desses estilos e aplicar lá no CSS, ele vai se tornar falso."

> "O kerning é a distância específica entre dois caracteres."
