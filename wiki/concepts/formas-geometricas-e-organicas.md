---
type: concept
title: "Formas Geométricas e Orgânicas"
aliases: ["formas em UI", "geométrico vs orgânico", "forma geométrica", "forma orgânica", "psicologia das formas", "border-radius e personalidade"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 8
tags: [ui, ui-design, formas, geometrico, organico, branding, border-radius, elementos-da-interface]
skill: ux-ui-mentor
status: stub
---

# Formas Geométricas e Orgânicas

Um dos [[wiki/concepts/elementos-da-interface]]. A ideia, emprestada do branding, é que as formas sempre comunicam algo. Há duas leituras principais, que não são regras e se misturam ([[wiki/sources/formas-geometricas-organicas-predominancia-harmonia]]):

| | Geométrica | Orgânica |
|---|---|---|
| Formas | Quadrado, círculo, retângulo, hexágono; regulares e exatas | Feitas à mão, ilustração, fotografia; irregulares |
| Comunica | Precisão, exatidão, racionalidade | Impressão, emoção, realidade |
| Nicho típico | Transferências, bancos, arquitetura | Produtos infantis, comida (hamburgueria) |
| Tipografia | Cantos retos; serifa em arquitetura | Arredondada (Poppins, Pampers, Lego) |

## O arredondamento

A mesma forma geométrica muda de mensagem com o raio da borda. Completamente reta, ela é exata ao máximo; arredondada, perde o "pontiagudo" e fica mais confortável. "Tudo aquilo que não machuca geralmente é redondo": por isso a tipografia da Pampers e a identidade do Lego são redondas, embora o Lego seja feito de "cubinhos".

O [[wiki/entities/frontpush]] usa o meio-termo: a fonte Saira, quadrada com cantos arredondados, para passar precisão sem exagero.

## Dois sentidos de "segurança"

A aula usa a palavra para coisas diferentes. No fintech, a forma geométrica passa segurança como robustez e confiança racional. No produto para bebês, a forma redonda passa segurança como conforto, algo que não machuca. A escolha depende do que o [[wiki/concepts/contexto-do-usuario|público]] precisa sentir.

## Predominância, não pureza

"O segredo está na predominância." Um botão reto numa interface orgânica não é erro: o caráter orgânico pode vir de ilustrações, imagens e cor, e o contraste entre os dois pode ser proposital ([[wiki/concepts/contraste]]). Ver [[wiki/concepts/harmonia-visual]].

## Olhar de dev

`[skill: ux-ui-mentor]` Em código, essa decisão vive em tokens: `--radius-*` (0 para marca reta, 8 px ou pill para marca suave) muda junto com `--font-family-heading`. Definir o raio como token semântico evita botões com 4, 6 e 12 px espalhados, o que quebraria a [[wiki/concepts/consistencia-visual]].

## Formas da natureza do lado geométrico

Na parte 2 da aula ([[wiki/sources/formas-exemplos-praticos-radius-consistencia-projetos]]), o [[wiki/entities/frontpush]] usa elipse, ondas senoidais e um céu com estrelas, eclipses e planetas, formas da natureza que "remetem a matemática, racionalidade". O critério da tabela acima é a regularidade da forma, não a origem: órbita e senoide são natureza e são exatas.

## Na prática: três projetos, três raios

O mesmo autor aplica o eixo a três projetos próprios: FrontPUSH com 8 px (meio-termo), [[wiki/entities/spider-man-projeto-nasser|Spider-Man]] com 3–4 px e elementos inclinados (fora da caixa), [[wiki/entities/creatorpush|Creator Push]] mais redondo (mais perto do usuário). Detalhes em [[wiki/concepts/border-radius]].

## Formas nos ícones

A sensação das formas vale para ícones: arestas retas passam sobriedade; arredondar "ameniza" e deixa mais amigável. Násser escolhe a família de ícones por isso: mais arredondada no Creator Push, mais "firme" no FrontPUSH ([[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]]). Ver [[wiki/concepts/familia-de-icones]].

## Ícones só de formas geométricas

Em [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]], os ícones do FrontPUSH partem de quadrado, retângulo, círculo, triângulo, hexágono e triângulo escaleno combinados, com traços retos; até logos orgânicos (o gato do GitHub, o foguinho da Hotmart) viram retos.

## Formas como elemento de composição

Linhas, ângulos e círculos tracejados passam "uma ideia um pouco mais geométrica" no fundo; a [[wiki/entities/playstation|PSN]] usa quadrado, X, triângulo e círculo como ambiência de marca ([[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]]). Ver [[wiki/concepts/elementos-de-composicao]].

## Retângulo e círculo em toda parte

"Toda a interface é composta de formas": cards, retângulos arredondados, círculo no perfil. Retângulo e círculo predominam em ícones, imagens, cards e links ([[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]).

## Exemplos de sites: Dropbox, Madero, Coco Bambu, Nubank

Na versão "W7" da aula de formas ([[wiki/sources/formas-geometricas-organicas-exemplos-dropbox-madero-coco-bambu-nubank]]), a mesma tese vem com sites reais: o [[wiki/entities/dropbox]] é reto e azul e põe o orgânico na prova de clientes; Madero e Coco Bambu são orgânicos pela foto de comida e usam a letra como contraste; um site de arquitetura é regular; o [[wiki/entities/nubank]] é geométrico, mas arredonda as bordas e usa fotos de pessoas; o C6 Bank fica no regular. A pergunta de partida é "o que você está querendo comunicar?". Exemplos do orgânico: "uma vagem nunca vai ser reta, que nem uma régua"; um pão nunca é "um oval perfeito".

## Formas nos botões

A aula de botões "W7" aplica o eixo a seis formas de botão ([[wiki/concepts/formas-de-botoes]]) e reforça que "um site totalmente geométrico [...] fica muito longe da pessoa": precisa de "um tempero" orgânico ([[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]]). `[external]` A preferência por curvas tem base experimental: Bar e Neta (2006), *Psychological Science* (https://doi.org/10.1111/j.1467-9280.2006.01759.x).

## Key Sources

- [[wiki/sources/formas-geometricas-organicas-predominancia-harmonia]]
- [[wiki/sources/formas-exemplos-praticos-radius-consistencia-projetos]] — FrontPUSH, Spider-Man e Creator Push; formas da natureza como geométricas
- [[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]] — ícones retos x arredondados seguem a identidade visual
- [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]] — ícones do FrontPUSH só com formas geométricas e traços retos
- [[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]] — formas geométricas como elementos de composição; PSN
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — retângulo e círculo como formas dominantes
- [[wiki/sources/formas-geometricas-organicas-exemplos-dropbox-madero-coco-bambu-nubank]] — versão "W7" da aula: Dropbox, Madero, Coco Bambu, arquitetura, Nubank, C6 Bank
- [[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]] — formas aplicadas a botões; geométrico puro afasta
