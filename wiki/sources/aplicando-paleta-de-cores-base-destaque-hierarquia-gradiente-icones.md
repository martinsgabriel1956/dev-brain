---
type: source
title: "Aplicando a paleta de cores: base e destaque, hierarquia, gradiente e ícones"
aliases: ["aplicação da paleta de cores", "aplicando a paleta", "paleta roxo e amarelo", "paleta do Quarto Criativo"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 0
tags: [ui, ui-design, design, cor, paleta-de-cores, contraste, hierarquia-visual, gradiente, icones, figma, elementos-de-composicao]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/aplicando-paleta-de-cores-base-destaque-hierarquia-gradiente-icones.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-15
---

# Aplicando a paleta de cores: base e destaque, hierarquia, gradiente e ícones

## TL;DR

Aula prática no [[wiki/entities/figma]] (cerca de 11 min) que continua a aula em que a turma montou a [[wiki/concepts/paleta-de-cores|paleta]] (essa aula anterior ainda não foi ingerida). A paleta segue o modelo **"base e enfoque"**: uma cor de base (roxo, com tons mais escuros e mais claros), uma cor de destaque (amarelo) e neutros para o texto. Ele mostra como usá-la. Num card roxo, o amarelo marca o que importa (perfil, nome) e o branco fica com o resto: [[wiki/concepts/hierarquia-visual|hierarquia]] pela cor. Numa interface monocromática, a mesma hierarquia sairia de **variações de cinza**, por isso a paleta precisa de uma escala de cinza. Um elemento de composição amarelo atrás de texto branco perde [[wiki/concepts/contraste]]; ele resolve com um **gradiente linear**. A cor principal **"não necessariamente precisa ser tudo"**: o site pode ser branco (60% da interface), com blocos em cinza e só o hero em roxo, porque roxo em tudo "fique enjoativo". A paleta reproduz a do designer de marcas [[wiki/entities/quarto-criativo|Quarto Criativo]], indicado como referência. Fecha com [[wiki/concepts/icones-em-interfaces|ícones]] em tons pastéis (preenchimento roxo, fundo pastel, stroke amarelo) e com a diferença entre redimensionar com Move (V) e com Scale (K) no Figma. Tudo isso vai servir ao style guide, mais adiante no curso.

## Key Claims

### O modelo da paleta

- **"Base e enfoque"**: "aquela paleta que tem uma cor de base, depois tem uma cor de destaque para poder compor e tem as cores neutras para poder ajudar na composição de texto e tudo mais". Também entram [[wiki/concepts/elementos-de-composicao|elementos de composição]]. Ver [[wiki/concepts/paleta-de-cores]].
- **Roxo como base**: "o roxo é a nossa corzinha de base", com "variações de tons mais escuros e de tons mais claros" abaixo dele.
- **Objetivo da paleta**: "um dos objetivos da paleta de cores é ter um bom contraste". Branco e amarelo contrastam bem com o roxo. Ver [[wiki/concepts/contraste]].

### Hierarquia pela cor

- **Amarelo no que importa**: num card, a informação importante ("o meu perfil", "o meu nome") vai em amarelo para "chamar a atenção do usuário"; o que, "por hierarquia textual", importa menos fica em branco. Ver [[wiki/concepts/hierarquia-visual]].
- **Sem cor de destaque**: numa interface "totalmente monocromática", ele usaria "um branco um pouco mais forte" e "um cinza um pouco mais clarinho". Mas as variações de cinza teriam de ser maiores, porque a diferença "está muito pouca". "Por isso que é importante a gente também ter a escala de cinza."
- **Destaque de trecho**: dentro da paleta, dá para destacar "alguma parte do texto" em amarelo.

### Gradiente contra a falta de contraste

- Ele põe um elemento de composição amarelo (ou "amarelo um pouquinho mais pastel") atrás do texto. A objeção, na voz do aluno: "não tem contraste do branco com o amarelo, então você está dificultando a vida do usuário".
- **A saída**: "aplicar um gradiente linear", que vai do amarelo até sumir. Fica "um detalhezinho, um entalhe", "dando algum efeito" no card. Ver [[wiki/concepts/elementos-de-composicao]].

### A cor principal não precisa ser tudo

- "Minha cor principal vai compor a minha interface, não necessariamente precisa ser tudo." A interface "pode ser muito bem light": corpo todo em branco, quebras com blocos em cinza, e só o banner principal ("no wireframe hero") em roxo. Ver [[wiki/concepts/wireframe]].
- No card fica mais fácil pôr tudo em roxo; no site, roxo em tudo "fique enjoativo". A proposta é que "60% da minha interface seja branca". Ver [[wiki/concepts/paleta-de-cores]].
- Do "outro lado" do layout, ele aplica o branco, itens em roxo e destaca a parte "paleta de cores" com quadradinhos roxos e o título em amarelo: "estou começando a compor as minhas interfaces".

### Referência: Quarto Criativo

- "Eu estou meio que reproduzindo a paleta de cores do Quarto Criativo", descrito como "um design de marcas". O feed dele serve de catálogo de "como aplica uma paleta de cores". Ver [[wiki/entities/quarto-criativo]].
- A hierarquia de texto ali "ele não fez aqui com escala de cinza, mas ele pegou um tom pastel e aplicou".
- "A gente ainda vai trabalhar a hierarquia": a hierarquia tipográfica fica para outra aula.

### Ícones com tons pastéis

- "Construir ícones utilizando os tons pastéis também é muito legal"; "de preferência preenchido, sempre dá certo com itens preenchidos". Ver [[wiki/concepts/icones-em-interfaces]].
- **Receita**: ícone de seta num círculo. Desagrupa (Ctrl+G agrupa, Ctrl+Shift+G desagrupa), pinta o Fill da seta de roxo "para poder dar um contraste maior", o círculo com "um pastel bem clarinho", tira o stroke e deixa o stroke da bolinha em amarelo. "Se fosse construir os ícones do Quarto Criativo."
- **Move x Scale**: aumentar com o Move (V), mesmo segurando Shift, não aumenta os atributos: "a grossura da setinha ela se mantém". "Não faça isso." Com o Scale, "ele vai aumentar de forma proporcional". Ver [[wiki/entities/figma]].

### Para onde vai

- "Todo esse trabalho vai ser de imensa importância quando a gente estiver complementando nosso style guide." Ele também diz que pretende escrever como é a própria paleta e como foi feita.

## Entities

- [[wiki/entities/nasser]]: autor (o nome aparece na objeção do aluno, "Ah, Násser", legenda "Nárcio"; padrão já visto em [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]]).
- [[wiki/entities/quarto-criativo]] (novo): designer de marcas cuja paleta a aula reproduz.
- [[wiki/entities/figma]]: ferramenta da aula; Fill, stroke, agrupar, Move x Scale.

## Concepts

- [[wiki/concepts/paleta-de-cores]] (novo)
- [[wiki/concepts/contraste]]
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/elementos-de-composicao]]
- [[wiki/concepts/icones-em-interfaces]]
- [[wiki/concepts/wireframe]]

## Tensões com a wiki

- **Branco sobre amarelo.** A própria aula admite que falta contraste. `[skill: ux-ui-mentor]` Texto normal pede 4.5:1 (WCAG AA); branco sobre amarelo fica bem abaixo disso. O gradiente ameniza porque o texto passa a ficar sobre o roxo em boa parte; onde o texto cruza o trecho amarelo, o problema continua. A regra que fica: o elemento de composição não pode estar atrás do texto em alto contraste com o fundo, como em [[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]].
- **"60% branca"** lembra a regra 60-30-10 (dominante, secundária, destaque) `[external]`, mas a aula não fala em 30 nem em 10. O amarelo usado com pouca frequência bate com a "cor de destaque escassa" de [[wiki/concepts/hierarquia-visual]] e o Isolation Effect de [[wiki/concepts/contraste]].
- **Amarelo como destaque x amarelo como warning.** Em [[wiki/concepts/cor-semantica]], amarelo é warning. Aqui ele é cor de marca. `[skill: ux-ui-mentor]` Funciona se o amarelo de destaque e o de warning forem tokens separados, ou se o warning vier sempre com ícone e texto.
- **Hierarquia só por cor.** Amarelo x branco hierarquiza bem quando há contraste com o fundo. `[skill: ux-ui-mentor]` A skill pede que nenhuma informação crítica dependa só de cor; tamanho e peso entram na aula de hierarquia tipográfica prometida.
- **Move x Scale.** `[external]` No Figma, a ferramenta Scale (atalho K) redimensiona stroke, efeitos e texto na mesma proporção; o redimensionamento comum (Move, V) mantém a espessura do stroke. A aula descreve isso certo, mas não diz o atalho (https://help.figma.com).

## Open Questions

- **"É Nasher"** no fim da primeira frase: não está claro o que o tópico é. Pode ser o nome do autor mal colocado ou uma palavra perdida. Mantido literal no raw.
- **"Módulo de base e enfoque"**: provável "modelo"; mantido literal.
- **"Um cinza um pouco mais curinho"**: "escurinho" ou "clarinho"? Mantido literal.
- **"Alguma artesia"**: palavra não identificada (talvez "arte"); mantida literal.
- **Aula anterior** (construção da paleta) e **aula de hierarquia** prometidas; não ingeridas.
- **Quarto Criativo**: não verificado fora da aula (nome, perfil, cores exatas).
- `date_published` vazio.

## Raw Quotes

> "Lembra que um dos objetivos da paleta de cores é ter um bom contraste, concorda comigo?"

> "Minha cor principal vai compor a minha interface, não necessariamente precisa ser tudo, galera."

> "Se eu aumentar com o Move, ele aumenta sem aumentar os atributos."

## Ver também

- [[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]] — elementos de composição em baixo contraste no fundo
- [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]] — ícone preenchido destaca; cor e posição sobem a hierarquia
- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]] — botão na cor de contraste da paleta
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — cor que informa (azul, vermelho, amarelo)
