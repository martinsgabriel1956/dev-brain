---
type: source
title: "Paleta de cores na prática: referências no Dribbble, modo HSB, variações e cores neutras"
aliases: ["paleta de cores na prática", "aula prática de cores", "variação de cores no HSB", "cor de base nas cores neutras"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 0
tags: [ui, ui-design, design, cor, paleta-de-cores, hsb, cores-complementares, cores-neutras, figma, dribbble, referencias, style-guide]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/paleta-de-cores-na-pratica-dribbble-hsb-variacoes-cores-neutras.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-15
---

# Paleta de cores na prática: referências no Dribbble, modo HSB, variações e cores neutras

## TL;DR

Primeira aula prática do bloco de cores do curso de UI de [[wiki/entities/nasser|Násser]] (cerca de 15 min), no [[wiki/entities/figma]]. Ele parte de esquemas prontos (complementar, neutra + uma cor, monocromática, análoga) e escolhe um par complementar: roxo como **cor de base**, amarelo como **cor de destaque**, mais um claro (F1/F2) e um escuro (30 30 30, 20 20 20) neutros ([[wiki/concepts/paleta-de-cores]]). As cores vêm de [[wiki/concepts/repertorio|referências]]: print de um shot do [[wiki/entities/dribbble]], conta-gotas no Figma e busca por hexadecimal no próprio Dribbble. No seletor, use o [[wiki/concepts/modelo-de-cor-hsb|modo HSB]] e fique no "primeiro quadrante", sem saturação nem brilho no máximo. A [[wiki/concepts/variacao-tonal-de-cor|variação]] mais escura baixa o brilho 10–15 pontos e sobe a saturação; a mais clara faz o contrário. O resultado manual fica perto do que uma ferramenta gera. Por fim, os [[wiki/concepts/neutros-tingidos|neutros recebem um pouco da matiz da base]] (overlay ou HSB com matiz 247 e saturação 4), com passos menores, e o preto vira uma escada de cinza. Tudo isso alimenta o style guide.

## Key Claims

### Esquemas e papéis

- **Quatro exemplos de paleta:** complementares (salmão/vermelho e verde, roxo e amarelo, azul e amarelo, azul e laranja), uma neutra de base com uma só cor, monocromática e análoga. Ver [[wiki/concepts/paleta-de-cores]].
- **Neutra + uma cor:** "comum, por exemplo, no Nubank", "roxo e branco e as suas variações"; e "toda a estrutura dos meus cursos": preto de base, o resto "apenas com uma cor", com gradientes "para poder ficar um pouco mais charmoso". Ver [[wiki/entities/nubank]] e [[wiki/entities/frontpush]] (inferido: o site do curso é preto com azul).
- **Base e destaque:** o roxo é a cor de base, o amarelo a "cor de enfoque, a minha cor de destaque, porque elas são complementares", e "o amarelo se destaca muito bem no roxo". Ver [[wiki/concepts/contraste]] e [[wiki/concepts/hierarquia-visual]].
- **Neutros de partida:** um claro "F1, um F2", que "não seja o branco chapado"; um escuro "por volta de 30, 30, 30" ou "20, 20, 20". Margem para trabalhar dos dois lados.

### Referências: de onde vêm as cores

- **"Criatividade você se constrói com uma biblioteca de boas referências."** É a resposta ao "como eu faço para tirar o bloqueio criativo?". Ver [[wiki/concepts/repertorio]].
- **Dribbble:** "a maior rede social de design do mundo" (com o "se não me engano" dele). Crie conta, use *Like this shot* e *Save shot*. Ver [[wiki/entities/dribbble]].
- **Do print ao hexadecimal:** print da tela, colar no Figma, conta-gotas sobre um shape, cor capturada.
- **Busca por cor:** "barra colors" no Dribbble abre a página de cores ("agora eles mudaram para shots"); filtro com o hexadecimal; mais filtros (Figma, downloads, só fotos). Ele deixa "sempre tudo". Sem login, a página "fica travando".
- **Instagram:** "sigam os perfis profissionais" que ele segue; ele se considera "sempre me alimentando de boas referências".
- **A referência não precisa ser copiada:** "não necessariamente use os mesmos tons"; o roxo da referência "é mais tendido até para o azul" e "um pouco menos saturado".

### Modo HSB e o primeiro quadrante

- **"Deixo em modo HSB quando você estiver compondo a sua paleta."** Ver [[wiki/concepts/modelo-de-cor-hsb]].
- **Primeiro quadrante:** divida o quadrado do seletor "em quatro" e prefira o primeiro. "Não é uma regra, mas são boas práticas."
- **Tons pastéis são leves:** cor "um pouco mais para cá" puxa para o pastel, que "transmite isso de ser mais leve, de ser mais suave". O roxo e o amarelo escolhidos estão em tons pastéis; o azul e o amarelo mais fortes também caem perto do primeiro quadrante.
- **Não "topar":** "nunca deixe a cor que você vai fazer as variações depois muito saturada" nem "com brilho topado"; "coloque literalmente aqui no meio". O motivo: com o canal no máximo, fica difícil gerar as variações, "mas também tem muita ferramenta para isso".

### Variações mais escuras e mais claras

- **Escurecer = brilho para baixo e saturação para cima.** "Pela intuição, diminuo o brilho" de 10 a 15 pontos (78 → 62), mas "isso não é suficiente": aumente também a saturação, "não necessariamente na mesma proporção". Ver [[wiki/concepts/variacao-tonal-de-cor]].
- **Por quê:** a variação "fica mais natural". Só baixar o brilho (78 → 61) parece "balela" de tão próximo; com mais distância (brilho 50, saturação 67–68), a diferença fica "mais acentuada".
- **Clarear = brilho para cima e saturação para baixo:** brilho 90 e saturação cerca de 10 pontos menor; depois brilho 96–97 e saturação 30.
- **"Muito, muito, muito de um teste":** vá mexendo "até que a paleta de cores te agrade ou se encaixa ao branding, ao cliente"; "meio que não existe regra".
- **Conferir com a ferramenta:** ele põe a cor numa ferramenta da aula anterior (não nomeada), coloca as duas escalas lado a lado e conclui que "o nosso conceito está bem estipulado". Repete o processo para o amarelo.

### Cor de base nas cores neutras

- **Harmonizar os neutros:** "dar um pouco da cor de base nessas cores neutras". Ver [[wiki/concepts/neutros-tingidos]] e [[wiki/concepts/harmonia-visual]].
- **Método 1, overlay:** copiar o roxo, pôr em modo overlay sobre o branco e trazer para a frente; o branco "não está branco totalmente sem saturação". Ver [[wiki/concepts/blend-modes]].
- **Método 2, HSB direto:** o conta-gotas mostra saturação 4 na matiz 247, "a mesma matiz do nosso roxinho"; então basta pôr o branco na matiz da base (245–247) e "adicionar um pouquinho de saturação".
- **Passos menores no branco:** brilho 98 → 95/96 → 92, saturação +1 por passo, porque "qualquer mudança no branco, a diferença é bem mais acentuada". Para clarear: brilho 99 com saturação 3, brilho 100 com saturação 2.
- **No preto, a saturação dispara:** em overlay, "a saturação ficou muito alta"; baixar a opacidade para 50% leva a saturação a 22; para 10%, a 9. "O branco é mais facilmente afetado do que o preto" (ver Tensões).
- **Escada de cinza:** a cor escura de composição fica "por volta de um A, um F, ou então dois" (leitura: 1A, 1F ou 20 por canal); as vizinhas seguem uma escadinha ("1,5", "1,00", "3,3", "4,4", literal na fala).

### Para onde vai

- **Projeto do Nubank:** lá só se trabalham os neutros com uma cor; aqui, uma complementar "por enquanto".
- **Exercício:** desenvolver as outras paletas do slide.
- **Style guide:** a paleta "vai servir muito, muito, muito" no style guide e em "aplicar estilos de maneira ordenada e organizada de forma a priorizar a consistência na ferramenta do Figma". Ver [[wiki/concepts/consistencia-visual]].

## Entities

- [[wiki/entities/nasser]]: autor. Ele diz o próprio nome ("Primeiro, Násser, por que você escolheu essas cores").
- [[wiki/entities/dribbble]]: fonte de referências e busca por hexadecimal.
- [[wiki/entities/figma]]: seletor em HSB, conta-gotas, overlay, opacidade.
- [[wiki/entities/nubank]]: exemplo de neutra + uma cor; projeto do curso.
- [[wiki/entities/frontpush]]: "a estrutura dos meus cursos" (preto + uma cor + gradiente); ligação inferida.
- Sem página própria: Instagram, a ferramenta de variação da aula anterior (não nomeada).

## Concepts

- [[wiki/concepts/paleta-de-cores]] (novo)
- [[wiki/concepts/modelo-de-cor-hsb]] (novo)
- [[wiki/concepts/variacao-tonal-de-cor]] (novo)
- [[wiki/concepts/neutros-tingidos]] (novo)
- [[wiki/concepts/repertorio]]
- [[wiki/concepts/contraste]]
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/harmonia-visual]]
- [[wiki/concepts/blend-modes]]
- [[wiki/concepts/consistencia-visual]]

## Tensões com a wiki

- **"O branco é mais facilmente afetado do que o preto"**, mas a demo mostra o contrário no número: o preto em overlay fica "muito alto" de saturação e pede opacidade de 50% e depois 10%. As duas falas cabem se "afetado" for a diferença visível (passos no branco aparecem mais) e não o número de saturação. `[external]` Pela fórmula do overlay (W3C Compositing Level 1, https://www.w3.org/TR/compositing-1/#blendingoverlay), fundo claro usa *screen* e fundo escuro usa *multiply*: o resultado no escuro carrega quase só a cor de cima. Num preto 20 20 20, pouca luz já dá saturação alta no HSB, porque a saturação é medida relativa ao brilho. Leitura minha, não dita na aula.
- **Overlay sobre branco puro não tinge.** `[external]` Pela mesma fórmula, com fundo 1,0 o *screen* devolve 1,0; o tingimento visto vem do branco F1/F2 (não FFFFFF) escolhido antes. Bate com "que ela não seja o branco chapado".
- **HSB não é HSL.** `[external]` No HSB, brilho 100 com saturação 0 é branco, e brilho 100 com saturação alta é a cor pura; no HSL, luminosidade 100 é sempre branco (https://en.wikipedia.org/wiki/HSL_and_HSV). Por isso a receita "brilho para baixo, saturação para cima" é do HSB; no HSL ela muda de forma. `[skill: ux-ui-mentor]` A skill prefere HSL ou OKLCH no código: no OKLCH, mesmo L dá o mesmo brilho percebido entre matizes, o que o HSB não garante (amarelo e roxo com brilho 78 não parecem igualmente claros).
- **Paleta vira token.** `[skill: ux-ui-mentor]` A escala manual é a camada de primitivos (`purple-100…900`); componentes usam tokens semânticos (`color-brand`, `color-accent`, `color-background`). O style guide prometido é onde isso se fixa.
- **Amarelo de destaque e contraste.** `[skill: ux-ui-mentor]` Texto sobre amarelo pastel ou amarelo sobre branco costuma falhar o 4.5:1; amarelo funciona como fundo de botão com texto escuro ou sobre o roxo. A aula não mede contraste.
- **Repertório, de novo.** A tese "criatividade se constrói" já aparece em [[wiki/sources/como-aprender-ui]]; aqui ganha o caso concreto (do shot ao hex).

## Open Questions

- **Qual ferramenta de variação?** "Aquela ferramenta que a gente trabalhou" está numa aula anterior, ainda não ingerida.
- **Edição do curso:** FrontPUSH ou "W7"? A aula não diz.
- **Escada de cinza:** "um A, um F, ou então dois" e "1,5", "1,00", "3,3", "4,4" mantidos literais; a leitura em hexadecimal (1A, 1F, 20; 15, 10, 33, 44) é inferência.
- **Saturação no primeiro passo escuro:** "se aqui dá 53, eu vou aumentar para 55" contradiz o "10 a 15 pontos" dito logo antes. O número exato não aparece na legenda.
- **Aula sobre gradientes** prometida ("por que eu gosto tanto de utilizá-los").
- `date_published` vazio.

## Raw Quotes

> "Criatividade você se constrói com uma biblioteca de boas referências."

> "Se eu diminuir o brilho, eu tenho que aumentar a saturação, não necessariamente na mesma proporção."

> "Isso faz com que a nossa interface seja mais harmônica."

## Ver também

- [[wiki/sources/como-aprender-ui]] — "criatividade se constrói", mood board
- [[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]] — variação monocromática de azul no FrontPUSH
- [[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]] — blend modes no Figma
