---
type: source
title: "Princípios do Design: eixo, simetria, consistência, contraste e simplicidade"
aliases: ["aula princípios do design", "princípios do design ui", "eixo simetria consistência simplicidade"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 0
tags: [ui, ui-design, design, eixo-visual, simetria, consistencia, contraste, hierarquia-visual, espaco-em-branco, simplicidade, acessibilidade, icones, identidade-visual]
skill: ux-ui-mentor
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/principios-do-design-eixo-simetria-consistencia-simplicidade.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-13
---

# Princípios do Design: eixo, simetria, consistência, contraste e simplicidade

## TL;DR

Primeira aula de "princípios do design" do módulo de UI Design do [[wiki/entities/frontpush|FrontPUSH]], de [[wiki/entities/nasser|Násser]]. A ideia é fixar os princípios que vão explicar as aulas seguintes (grids, ícones, tipografia). Cinco blocos. **[[wiki/concepts/eixo-visual|Eixo]]**: linha imaginária que organiza elementos para alinhar, reforçar uma divisão, sugerir movimento ou continuidade. **[[wiki/concepts/simetria-visual|Simetria]]**: cards iguais dão sensação de fim (e-commerce); assimetria sugere feed infinito (Explorar do Instagram). **[[wiki/concepts/consistencia-visual|Consistência]]**: escolher um padrão e segui-lo (uma família de ícones, uma paleta), o que vira identidade visual. **[[wiki/concepts/contraste|Contraste]]**: sem ele não há acessibilidade, sobretudo na tipografia. **[[wiki/concepts/simplicidade-visual|Simplicidade]]**: o ser humano consome pouco por vez, então apresentar aos poucos e usar [[wiki/concepts/espaco-em-branco|espaço em branco]] (Google, site do iPhone 12) em vez da tela de ERP lotada.

## Key Claims

### Eixo

- **Eixo é uma linha imaginária que organiza um grupo de elementos na interface.** Serve para alinhar, reforçar, dar ideia de movimento ou de continuidade. Ver [[wiki/concepts/eixo-visual]].
- **Alinhamento cria ordem e sinaliza categoria.** Itens no mesmo eixo e com o mesmo tamanho são lidos como da mesma categoria (músicas do mesmo álbum num app de música). Slide: "Quando organizados em um eixo, o design aparenta ser mais ordenado."
- **Reforço: quebrar o eixo marca subordinação.** Um item deslocado para fora do eixo principal é lido como parte do item acima, como o retweet ou a resposta no feed do [[wiki/entities/twitter|Twitter]]. É o mesmo mecanismo de agrupamento da [[wiki/concepts/lei-da-proximidade-gestalt]].
- **Movimento: card cortado na borda mostra que há mais.** A [[wiki/entities/netflix|Netflix]] corta de propósito o último card da fileira. Slide: num eixo horizontal, "o próprio cérebro entende que tem continuidade".
- **Continuidade: sem ponto final definido, o olho segue o eixo.** O Explorar do Instagram ([[wiki/entities/meta|Meta]]) usa dois eixos não simétricos e fotos de tamanhos diferentes, e o resultado é o feed infinito. Os Reels ganham mais área para criar [[wiki/concepts/hierarquia-visual]].
  - `[skill: ux-ui-mentor]` Infinite scroll serve a feeds exploratórios, mas impede bookmarking e deixa o rodapé inacessível. A aula mostra só o lado do engajamento.
- **Grids virão depois.** Grids "são literalmente colunas" e reaproveitam esses eixos.

### Simetria

- **Simetria = elementos organizados em relação ao eixo da mesma maneira.** Cards do mesmo tamanho lado a lado dão equilíbrio e a sensação de que a lista tem fim. Ver [[wiki/concepts/simetria-visual]].
- **E-commerce usa simetria porque o catálogo acaba.** "Por mais grande que seja a loja, não tem recursos infinitos." O Instagram tem tantas fotos que é tratado como infinito e usa assimetria.

### Consistência

- **Consistência é escolher um padrão e segui-lo.** Vale para ícones, paleta, identidade visual. "O design bonito é aquele consistente." Ver [[wiki/concepts/consistencia-visual]].
- **Ícones: uma família por projeto.** No [[wiki/entities/figma|Figma]], o autor mostra o Feather Icons (o que mais usa, gratuito, só contorno, mesmo traço, "filho de uma mesma pessoa"). Misturar com um pacote de linha do Iconify, de contorno diferente, quebra a consistência mesmo sendo os dois de linha. O Iconly tem variações (preenchido, duas cores, linha, linha com cortes, curvado); a escolha entre elas fica para a aula de ícones.
- **Cores: uma paleta mantida.** O site do [[wiki/entities/frontpush]] usa preto, branco e um único azul gradiente com transparência em toda a interface, sem trocar o tom.
- **Consistência vira identidade visual.** O objetivo é olhar e reconhecer a empresa. Exemplos: Apple (iMac, iPhone, iPad e MacBook seguem a mesma identidade; tirando a logo, ainda parece Apple) e Logitech. O autor diz que identidade visual cresceu na pandemia e na pós-pandemia.
  - `[skill: ux-ui-mentor]` É a heurística 4 de Nielsen (consistência e padrões), que a skill aplica também a palavras e ações: botão "Salvar" numa tela e "Confirmar" em outra para a mesma ação.

### Contraste

- **Sem contraste não há acessibilidade.** "Como é que eu vou deixar algo acessível se eu não consigo enxergar direito?" Vale para ilustrações e tudo mais, mas pesa mais na tipografia. Ver [[wiki/concepts/contraste]].
- Slide (não falado): contraste "define a prioridade" e opera por **tamanho, peso tipográfico, cor e preenchimento**, não só por cor.

### Simplicidade

- **O ser humano tem um ponto focal e consome pouco por vez.** Monitor gigante não ajuda muito porque o ângulo de visão é limitado; telas grandes servem para dividir tarefas, mas o foco continua em uma de cada vez. O autor cita "alguns estudos" sem dizer quais (confiança baixa nesse ponto específico). Ver [[wiki/concepts/simplicidade-visual]].
- **Simplicidade é apresentar a informação "de maneira picada".** Estabelecer uma ordem de apresentação, uma informação de cada vez, para ficar palatável.
- **Contraexemplo: ERP brasileiro que faz tudo.** Controle financeiro, nota fiscal, idioma, telefone, e-mail, comprador e quantidade numa tela só. Um funcionário novo precisaria de ajuda: "esses sistemas que têm tudo geralmente não conduzem para nada", porque há "300 mil jornadas diferentes" na mesma tela. Ver [[wiki/concepts/sobrecarga-de-informacao]] e [[wiki/concepts/carga-cognitiva]].
- **Exemplo: a home do [[wiki/entities/google|Google]].** Logo, barra de pesquisa, dois botões. Os milhões de recursos ficam atrás de "mais do Google" (os três pontinhos), e os links mais usados (Imagens, Gmail) ficam no canto. O autor supõe que isso saiu de "uma grande pesquisa" (inferência dele).
- **Espaço em branco é literalmente vazio, pode ser preto.** Ao ver que não há nada ao redor, o usuário foca no que importa para decidir naquela jornada. Ver [[wiki/concepts/espaco-em-branco]].
- **Exemplo: site do iPhone 12 Pro.** A página tem uma barra de rolagem enorme porque apresenta todos os recursos, mas a primeira tela tem só a foto, o nome e "um salto radical".
- **Big techs como referência porque o erro custa caro.** Se o Google erra uma jornada, prejudica milhões. (Nota: em [[wiki/sources/como-aprender-ui]] o mesmo autor recomenda redesenhar startups, não big techs; aqui as big techs são exemplo a estudar, não a redesenhar. Não há conflito.)
- **Acessibilidade: o designer projeta para outra pessoa.** Slide: "O design não é pra você designer, é para o usuário", com os itens Feedback e Uso de patterns. Retoma "o usuário talvez não seja você" de [[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]].

### Hierarquia (só nos slides)

O autor adia hierarquia para uma aula própria, mas os slides que o usuário enviou já trazem o conteúdo. Hierarquia é "nível de importância dos elementos", por quatro meios. Ver [[wiki/concepts/hierarquia-visual]].
- **Tamanho:** "Naturalmente, olhamos primeiro para os maiores elementos." Ex.: destaque em feed de notícias.
- **Forma:** "Um elemento diferente dos demais visualmente se destaca."
- **Posição:** elementos fixos e no topo têm mais hierarquia, "pois lemos de cima pra baixo".
- **Cores:** "Cores que contrastam mais detém de maior hierarquia visual." Ex.: feed do Instagram.

## Entities

- [[wiki/entities/nasser]]: autor. Nesta aula ele fala o próprio nome ("Ah, Násser, como assim?") e chama o site do FrontPUSH de seu.
- [[wiki/entities/frontpush]]: paleta preto, branco e azul como exemplo de consistência.
- [[wiki/entities/figma]]: onde ele abre os pacotes de ícones.
- [[wiki/entities/google]]: home como exemplo de simplicidade e espaço em branco.
- [[wiki/entities/netflix]]: card cortado (eixo de movimento).
- [[wiki/entities/twitter]]: retweet deslocado (eixo de reforço).
- [[wiki/entities/meta]]: Explorar do Instagram (continuidade, assimetria).
- Sem página própria: Apple, Logitech, Feather Icons, Iconify, Iconly.

## Concepts

- [[wiki/concepts/eixo-visual]] (novo)
- [[wiki/concepts/simetria-visual]] (novo)
- [[wiki/concepts/consistencia-visual]] (novo)
- [[wiki/concepts/espaco-em-branco]] (novo)
- [[wiki/concepts/simplicidade-visual]] (novo)
- [[wiki/concepts/contraste]]
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/ui-design]]
- [[wiki/concepts/padroes-de-interface]]
- [[wiki/concepts/lei-da-proximidade-gestalt]]
- [[wiki/concepts/carga-cognitiva]]
- [[wiki/concepts/sobrecarga-de-informacao]]

## Tensões com a wiki

- **Autoria resolvida.** [[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]] e [[wiki/entities/nasser]] tratavam como inferida a ligação Násser ↔ FrontPUSH. Esta aula liga os dois: o autor diz o próprio nome e mostra frontpush.com.br como "a minha interface".
- **Simetria vs. infinito.** A aula associa simetria a fim e assimetria a infinito. Isso descreve dois casos (e-commerce, Instagram), não uma regra: nada impede um grid simétrico com scroll infinito, e o que sinaliza fim é a paginação ou o rodapé visível, não só a simetria. Leitura do agente, não da aula.
- **Variações do Iconly respondidas na aula de ícones** ([[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]]): escolha pela identidade visual (linha = sóbrio; preenchido e arredondado = amigável) e use uma só. Ver [[wiki/concepts/familia-de-icones]].

## Open Questions

- Quais "estudos" sobre ângulo de visão e monitor grande o autor tinha em mente?
- A aula promete aulas próprias de grids, ícones (como escolher entre preenchido, linha, duas cores), cores (matizes) e hierarquia. A aula seguinte do curso, [[wiki/sources/elementos-da-interface-introducao-ui-design]], abre o módulo de [[wiki/concepts/elementos-da-interface]] e confirma o roteiro (espaçamentos, linhas, formas, ícones etc.; cores e tipografia em módulos próprios). A aula de espaço em branco ([[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]]) retoma a home do Google, agora como macro espaço, e liga a consistência ao [[wiki/concepts/grid-de-8-pontos]]. Grids de colunas ainda não foram ingeridos.
- `date_published` vazio. O exemplo do iPhone 12 Pro e a menção a "pós-pandemia" sugerem gravação entre fins de 2020 e 2021.
- A legenda tem uma lacuna de ~17 s (00:20:18 a 00:20:35) logo após o exemplo do iPhone; provavelmente rolagem da página sem fala.

## Raw Quotes

> "O design bonito é aquele consistente."

> "Esses sistemas que têm tudo geralmente não conduzem para nada."

> "Eu falo espaço em branco, é literalmente vazio, pode ser espaço preto."

> "O designer projeta telas para uma outra pessoa e não para ele mesmo."
