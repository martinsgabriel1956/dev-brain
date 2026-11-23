---
type: source
title: "Mentoria de UI Design: pesquisa, referências, patterns, leitura em Z e em F, contraste (FrontPUSH)"
aliases: ["FrontPUSH mentoria UI Design", "Mentoria UI Design", "mentoria de UI design", "#Mentoria: UI Design"]
date_created: 2026-11-23
date_updated: 2026-11-23
source_count: 0
tags: [ui-design, ux-design, design, mentoria, curso, pesquisa, referencias, padroes-de-interface, lei-de-jakob, e-commerce, wireframe, page-map, biblioteca-de-wireframes, modelagem-de-referencias, dribbble, behance, lapa-ninja, figma, ilustracoes, densidade-de-informacao, objetivo-da-interface, cta, botao-vs-link, hierarquia-visual, padrao-z, padrao-f, contraste, acessibilidade, who-can-use, hsb, luminosidade, regra-60-30-10, espaco-em-branco]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-mentoria-ui-design-referencias-patterns-leitura-z-f-contraste.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-23
---

# Mentoria de UI Design: pesquisa, referências, patterns, leitura em Z e em F, contraste (FrontPUSH)

## TL;DR

Mentoria ao vivo do [[wiki/entities/frontpush|FrontPUSH]] (cerca de 54 min, gravação começa no meio da fala) em que [[wiki/entities/nasser|Násser]] tenta "juntar os principais itens de UI". O fio é "todo o processo de design é intimamente ligado à pesquisa", e o resto sai disso:

- **Patterns e e-commerce:** Kabum, Magazine Luiza e Netshoes mudam pouco a UI porque "qualquer coisa da jornada do usuário que eu modifique nesse tipo de loja vai afetar diretamente a venda". A barra de busca grande no topo é o exemplo ([[wiki/concepts/padroes-de-interface]], [[wiki/concepts/lei-de-jakob]]).
- **Três fontes, todo dia:** [[wiki/entities/lapa-ninja|Lapa Ninja]], [[wiki/entities/dribbble|Dribbble]] e [[wiki/entities/behance|Behance]] dão "80% do que eu pesquiso"; entrar nelas deve virar rotina, como escovar o dente.
- **Modelar, não copiar:** o projeto [[wiki/entities/nubank|Nubank]] do curso saiu de shots colados no [[wiki/entities/figma|Figma]], um page map e um wireframe de média fidelidade; cada seção tem uma referência de origem. O site de [[wiki/entities/jonas-miller|Jonas Miller]] serve de exemplo de modelagem ([[wiki/concepts/modelar-referencias]]).
- **Arquivo de wireframes:** content, features, charts, steps, dispositivos, galeria, blog (padrão do G1), produto, preços; "UI hoje, pessoal, você precisa de pattern" ([[wiki/concepts/biblioteca-de-wireframes]]). Wireframe é conteúdo; cor e efeito vêm das plataformas de shots.
- **Tópicos e ilustração:** "o ser humano [...] entende melhor as coisas quando elas são feitas por tópicos"; a ilustração tem de comunicar a mensagem (banco "para todos" = pessoas de várias etnias) ([[wiki/concepts/densidade-de-informacao]], [[wiki/concepts/ilustracoes-em-interfaces]]).
- **Objetivo, botão e leitura:** toda página tem um objetivo, e a ação principal vai num botão, não num link. Ocidentais leem em Z (pouco conteúdo, landing page) ou em F (muito conteúdo, portal de notícias); o botão fica no caminho do Z ([[wiki/concepts/objetivo-da-interface]], [[wiki/concepts/hierarquia-visual]]).
- **Contraste:** [[wiki/entities/who-can-use|Who Can Use]] é "simplesmente obrigatório"; laranja de marca com branco reprova, escurecer no HSB ajuda ([[wiki/concepts/razao-de-contraste]], [[wiki/concepts/modelo-de-cor-hsb]]).
- **Três cores de fundo:** branco, preto ou azul-escuro, "porque são extremos de luz"; azul ~11% de luminosidade, amarelo 80% (lapso: 89%), verde ~60% "na meiuca" ([[wiki/concepts/luminosidade-das-cores]]).
- **60-30-10 e ímã visual:** na landing page da "Everyball", 60% claro, ~20% preto da tipografia, 10% azul; ícones em tom pastel, botão saturado: "é como se fosse um ímã visual" ([[wiki/concepts/regra-60-30-10]], [[wiki/concepts/espaco-em-branco]]).

## Key Claims

### Pesquisa e patterns no e-commerce

- "Primeiro, pesquisa muito antes para poder tomar as decisões mais assertivas possível."
- "O cérebro do ser humano é totalmente voltado para patterns [...] se você mudar um pattern do nada, você pode prejudicar e muito a tomada de decisão do usuário." Todo app bem projetado tem ilustração, texto, campo e botão no final, "fazendo um funil na ação do usuário, para que ele erre o menos possível" ([[wiki/concepts/padroes-de-interface]]).
- Kabum ("comprado pela Magalu recentemente"), Magazine Luiza e Netshoes: a UI "coincidentemente nunca mudou". Se alguém disser que vai modificá-la, "eles vão utilizar pequenas mudanças ao longo do tempo do que fazer uma atualização muito grande", porque o usuário "já sabe onde está o botão de adicionar novo endereço" ([[wiki/concepts/lei-de-jakob]]).
- "Toda e qualquer decisão que você saia do padrão nisso aqui, você pode acabar com a empresa." O e-commerce é o caso mais evidente, mas vale "dados as devidas proporções em outras UIs".
- Barra de busca: "uma barra grande no menu escrito Buscar, com um bom contraste no meio da tela", em vez de "só um iconezinho", porque "uma barra gigante vai facilitar o usuário a encontrar". Depois vêm as categorias, iguais nas três lojas.
- Para um blog (o aluno Luan pegou um freela): "pegar bons blogs, pesquisar em cada um deles e verificar quais são os padrões", para não "justificar sua UI como uma UI bonita". "No caso de e-commerce, o bonito não é o critério."

### Onde pesquisar

- Notion do curso, seção de inspirações: "praticamente eu utilizo o Lapa Ninja, o Dribbble e o Behance [...] 80% do que eu pesquiso sempre estão nessas três".
- "Se você quer ser UI designer, você vai ter que adicionar na sua rotina para você entrar nessas três plataformas todos os dias", para "construir uma biblioteca na sua cabeça".
- "Quando você está começando, você vai copiar e colar interfaces, não tenha dúvida disso. É um ótimo exercício", mas para avançar é preciso "pegar várias referências e saber construir novas coisas com elas".

### Modelar, não copiar: o caso Nubank

- Processo do projeto Nubank: "uma série de shots, copiei e colei aqui no Figma, fiquei olhando um para um, um para outro, desenhei um page map e aí sim começou a surgir as ideias" ([[wiki/concepts/page-map]], [[wiki/concepts/wireframe]]).
- Cada seção tem origem: o fundo com cards deitados, o CTA ao lado dos selos da Apple e da Google Play, o menu com menos informação, a seção com fotos de pessoas ("o Nubank tem muito disso de ser o banco mais próximo possível das pessoas"), os três cards com ícone.
- "A grande coisa não é você copiar e colar, é você modelar [...] eu vou juntar o que eu achei dessa [...] e eu vou ver se dá bom. Vai dar bom da primeira vez? É lógico que não" ([[wiki/concepts/modelar-referencias]]).
- Progressão: page map rabiscado, depois wireframe de média fidelidade. A ideia do cartão girando veio de um exemplo de perspectiva em CSS que ele já tinha feito: "é de tanto fazer que eu juntei as ideias" ([[wiki/concepts/fidelidade-de-prototipo]]).
- Pergunta de aluno: layout tem direito autoral? "Acredito que seções não têm problema." O site do Jonas Miller (figmento.cc) pegou referência dele e do Gilberto Prado, "só que ele modificou [...] adaptou para a identidade dele. Isso aqui não é cópia, isso aqui é modelagem". "Isso aqui é uma estrutura de um wireframe que é padrão." Também cita o "code-boost do Will", com o mentor ao lado e as aulas, "muito similar".

### Arquivo de wireframes e patterns

- Um arquivo do Figma "só de wireframe", que ele promete pôr no Notion: content, features ("pontos que destacam o seu produto ou serviço"), charts and numbers, steps, dispositivos e apps, galeria (slider, cards, aleatório; desktop e mobile), blog, produto (description, reviews, details) e preços ([[wiki/concepts/biblioteca-de-wireframes]]).
- O "Stage" (projeto citado como "do papai designer") repete o padrão de passos: "coincidentemente, pessoal, ou não é coincidência, é padronização".
- Blog: o card com notícia maior à esquerda "é o padrão do G1", "para dar destaque, para dar ênfase" ([[wiki/concepts/hierarquia-visual]]).
- "A partir do momento que você consegue pegar uma base, entender os princípios, entender os porquês das coisas, dali para frente é só treino." "E aí, como é que você cria uma coisa diferente para outra? Utilizando diferentes padrões."
- Divisão de trabalho: "Wireframes é mais ligado a conteúdo [...] o esqueleto do meu conteúdo"; para "disposição de cores, de efeitos", aí sim Dribbble, Behance e Lapa Ninja.

### Lapa Ninja, Dribbble e Halo Lab

- O Lapa Ninja "tem as categorias já certinhas" (e-commerce, corporativo, institucional) e mostra "já o UI final para você pegar feeling de cor, [...] de disposição, [...] de tipografia". Fluxo: copiar imagem, colar no Figma, "referência salva" ([[wiki/entities/lapa-ninja]]).
- Para o novo site do FrontPUSH, ele salvou referências "com três pontos" para mostrar UI, código e motion.
- No Dribbble, buscar o tema (dashboard) e "selecione pessoas boas aqui dentro", como a [[wiki/entities/halo-lab|Halo Lab]], "uma puta empresa digital americana" (ver Precisões).
- O aluno Luiz fazia o portfólio "em uma semana"; depois de passar mais tempo pesquisando, "fez um projeto [...] mais bem estruturado e ele conseguiu boas oportunidades".
- Sequência: pesquisa, sketchbook, wireframes, estrutura com [[wiki/concepts/grid-de-8-pontos]], wireframe "em escala de cinza", e só então a cor.
- Um aluno pede uma live sobre como buscar referências de código (slider, flip de card). Resposta: os projetos do curso foram escolhidos para cobrir essa variedade; o site do AJ foi codado com grid-system em Sass para chegar à exatidão do layout ([[wiki/concepts/grid-system]]).

### Ilustrações e tópicos

- "Eu saber conectar muito bem ilustrações com aquilo que eu estou comunicando." Se o banco "é para todos", buscar ilustrações "de várias etnias diferentes, participando de um mesmo banco" ([[wiki/concepts/ilustracoes-em-interfaces]]).
- "O ser humano consome melhor as coisas, ele entende melhor as coisas quando elas são feitas por tópicos. Isso é psicológico, neurológico, alguma coisa assim." Em vez de texto longo, extrair os itens (100% gratuito, sem taxa, melhor suporte) "e um link para você detalhar" ([[wiki/concepts/densidade-de-informacao]]).

### Objetivo da página, botão e leitura em Z e em F

- "O bonito é o simples. O menos é mais." "Você sempre vai ter um objetivo [...] Qual é o objetivo da sua página?" Na landing page do FrontPUSH: "que você conheça o meu trabalho e que você deixe o seu nome e o seu e-mail" ([[wiki/concepts/objetivo-da-interface]]).
- O destaque da ação "não é só com cor [...] é um conjunto de fatores". Primeiro, o formato: "Link, ele tem que parecer link. Botão, ele tem que parecer botão. O botão é para a tomada de ação, link é para o usuário explorar." Segundo, o contraste "nas principais seções do website".
- "Nós, povo ocidental, a gente sempre lê da esquerda para a direita"; "se você for projetar uma interface para o Japão, é diferente" (ver Precisões). "Ou a gente lê em Z, ou a gente lê em F."
- Z: "a maioria das interfaces", "o padrão de leitura quando você tem pouco conteúdo"; enxerga-se primeiro "o que é maior", "o que está na parte de cima", "o que está na esquerda". F: "quando você tem muito conteúdo, [...] portal de notícia": desce, lê para o lado, desce, lê para o lado ([[wiki/concepts/hierarquia-visual]]).
- "No meio do caminho do Z, eu sempre tenho um botão." Na landing page da "Everyball", "Use Everyball for Free" e "Get Started" são primários, "o Sign in é secundário"; a setinha que aparece no botão do FrontPUSH veio daí. Estrutura deles: "ilustração de um lado, descrição do outro, link", "justamente o padrão do Nubank".
- As três landing pages do FrontPUSH mostram a evolução: "é treino, é sentar e fazer 70 vezes".

### Contraste e as três cores das interfaces

- Who Can Use: "esse site aqui é obrigatório para você que está projetando interface". Laranja com branco "falhou"; se o laranja é cor de branding e vai no botão, "tenta dar uma escurecida nele" ([[wiki/entities/who-can-use]], [[wiki/concepts/razao-de-contraste]]).
- No seletor HSB, "nesse primeiro quadrante", "diminuir o brilho aumenta a saturação", "uma boa regra", não uma lei ([[wiki/concepts/modelo-de-cor-hsb]]). O laranja mais escuro continuou falhando: a ferramenta "considera o pior caso", "uma tipografia pequena em corpo de texto"; negrito e tamanho maior ajudam.
- A ferramenta "simula problemas visuais": catarata, glaucoma, deuteranopia, protanopia ([[wiki/concepts/acessibilidade]]).
- "A maioria das interfaces são três cores [...] uma cor clara de fato, ou é uma cor bem escura, ou é um azul escuro [...] porque são extremos de luz" ([[wiki/concepts/contraste]]).
- "O azul tem de 11% de luminosidade, quando eu vou para o amarelo, ele tem de 80%." Amarelo com texto branco "é o menor contraste possível que existe", "isso aqui é o dark pattern" (ver Precisões). Fundos escuros "nunca é um preto puro", têm "uma saturaçãozinha de azul". O verde, "60% de luminosidade", "está na meiuca", difícil com branco e com preto ([[wiki/concepts/luminosidade-das-cores]]).

### Regra 60-30-10 e o ímã visual

- A 60-30-10 "não é uma regra para ser seguida ao pé da letra, mas é uma essência". Na Everyball: 60% "essa cor clarinha" em dois tons próximos "para poder reforçar a divisão de seções"; o 30 é o preto da tipografia ("eu diria que é uns 20%"); 10% o azul de destaque ([[wiki/concepts/regra-60-30-10]]).
- "Ela é toda clean, ela tem um bom espaço em branco. [...] se eu colocar um pinguinho de outra cor no meio desse só branco, você vai olhar na hora. É como se fosse um ímã visual" ([[wiki/concepts/espaco-em-branco]]).
- Ícones "em tom pastel", botão saturado: "Onde está mais saturado? Nos pontos que o usuário precisa olhar." A seção de chamada tem "um gradiente do roxo para o azul gigantesco de fora a fora [...] com um botão branco no meio" ([[wiki/concepts/gradiente]]).

## Precisões e ressalvas

1. **Magalu, Kabum e Netshoes.** `[external]` O Magalu comprou a Netshoes em 2019 e a KaBuM! em 2021, por cerca de R$ 3,5 bilhões (alta, sem fetch). A dúvida "não sei se a Magalu comprou também a Netshoes" tem resposta: sim, antes da Kabum. Isso data a mentoria em 2021 ou depois.
2. **Os números de luminosidade são os da luma Rec. 601.** `[external]` Com Y = 0,299R + 0,587G + 0,114B, o azul puro dá 11%, o verde 59%, o vermelho 30% e o amarelo 89%. O azul (11%) e o verde (60%) da aula batem; o amarelo "80%" é lapso (a aula de variação de cores, na wiki, já diz 89%). A luminância relativa do WCAG usa outros pesos (0,2126/0,7152/0,0722, após linearizar), e nela o azul fica em 7% (alta). Ver [[wiki/concepts/luminosidade-das-cores]].
3. **Amarelo com branco não é "dark pattern".** Dark pattern é design que engana o usuário em favor do negócio ([[wiki/concepts/design-persuasivo]]); texto branco no amarelo é só contraste ruim, um erro de acessibilidade. O termo certo seria "bad UI", que ele mesmo usa na frase anterior (alta).
4. **"Diminuir o brilho aumenta a saturação"** não é uma propriedade do HSB, onde S e B são eixos independentes. É uma recomendação de caminho no seletor: ao escurecer, descer e ir para a direita juntos, para a cor não ficar acinzentada (inferência, alta). Ver [[wiki/concepts/modelo-de-cor-hsb]].
5. **F tem evidência, Z é heurística.** `[external]` O padrão em F vem dos estudos de eyetracking da Nielsen Norman Group (2006, revisitado em 2017), que o tratam como sintoma de texto mal estruturado, não como meta. O Z deriva do diagrama de Gutenberg e de prática de layout, com menos base empírica (média-alta). `[skill: ux-ui-mentor]` A referência `fluxos-ia.md` da skill traz a mesma divisão: F para texto denso, Z para landing pages e cards.
6. **Japão.** `[external]` Na web, o japonês é escrito quase sempre na horizontal, da esquerda para a direita; a escrita vertical (colunas da direita para a esquerda) aparece em livros, mangá e jornais. Os casos que de fato invertem o layout são as línguas RTL, como árabe e hebraico (alta).
7. **Tópicos ajudam, e há dado.** `[external]` No estudo de Nielsen de 1997 (*How Users Read on the Web*), texto escaneável melhorou a usabilidade medida em 47%, e conciso + escaneável + objetivo em 124% (alta, sem fetch). Não é "neurológico", mas o efeito é real.
8. **Direito autoral de layout.** `[external]` A Lei 9.610/98, art. 8º, exclui ideias, procedimentos e métodos da proteção; uma estrutura de seção padrão não é protegida, mas a expressão concreta (ilustrações, textos, fotos, código) e o conjunto-imagem podem ser (média; não é parecer jurídico). A resposta "seções não têm problema" vale para a estrutura, não para copiar arte ou texto.
9. **Halo Lab não é americana.** `[external]` É uma agência de design e desenvolvimento ucraniana, de Kharkiv, muito ativa no Dribbble (média-alta, sem fetch).
10. **Botão vs. link também é semântica.** `[skill: ux-ui-mentor]` A regra visual ("botão tem que parecer botão") tem par no código: `<button>` para ações e `<a href>` para navegação. Leitores de tela anunciam papéis diferentes, e trocar um pelo outro quebra teclado e expectativa (alta).
11. **Nomes reconstruídos da legenda:** Netshoes ("NetSchools"), Dribbble ("Dribble"), Halo Lab ("HaloLab"), Jonas Miller ("Jonas Milan", pela página existente; a grafia já era não verificada), Nubank ("Dubank", "do Bank"), Násser (Nassa, Násfer, Nasce, Nácio, NASA, NASSE). Ficaram literais: "Everyball"/"Every Bull" (o nome da landing page não foi identificado), "newsfial.com.br", "papai designer" e "Stage", "Logitech", "code-boost do Will", "baixo web", "Conteúdo existing".

## Entities

- [[wiki/entities/nasser]]: mentor.
- [[wiki/entities/frontpush]]: três landing pages mostradas como evolução; botão com setinha copiado da Everyball; objetivo da LP é captar nome e e-mail.
- [[wiki/entities/lapa-ninja]] (novo), [[wiki/entities/behance]] (novo), [[wiki/entities/dribbble]]: as três fontes de referência.
- [[wiki/entities/halo-lab]] (novo): estúdio a seguir no Dribbble.
- [[wiki/entities/figma]]: aba de referências e o arquivo de wireframes.
- [[wiki/entities/nubank]]: projeto do curso usado como caso de modelagem.
- [[wiki/entities/jonas-miller]]: site citado como exemplo de modelagem.
- [[wiki/entities/who-can-use]]: verificador de contraste.
- Sem página própria: Kabum, Magazine Luiza, Netshoes, G1, Everyball, Stage, Gilberto Prado, Will (code-boost), AJ, Luan e Luiz (alunos).

## Concepts

- [[wiki/concepts/modelar-referencias]] (novo)
- [[wiki/concepts/padroes-de-interface]], [[wiki/concepts/lei-de-jakob]]
- [[wiki/concepts/biblioteca-de-wireframes]], [[wiki/concepts/wireframe]], [[wiki/concepts/page-map]], [[wiki/concepts/fidelidade-de-prototipo]]
- [[wiki/concepts/ilustracoes-em-interfaces]], [[wiki/concepts/densidade-de-informacao]]
- [[wiki/concepts/objetivo-da-interface]], [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/contraste]], [[wiki/concepts/razao-de-contraste]], [[wiki/concepts/acessibilidade]], [[wiki/concepts/modelo-de-cor-hsb]], [[wiki/concepts/luminosidade-das-cores]]
- [[wiki/concepts/regra-60-30-10]], [[wiki/concepts/espaco-em-branco]], [[wiki/concepts/gradiente]]
- [[wiki/concepts/grid-de-8-pontos]], [[wiki/concepts/grid-system]]

## Open Questions

- Qual é a landing page "Everyball"? O nome soa como ASR de outra marca; sem ela não dá para conferir o 60-30-10 descrito.
- O arquivo de wireframes prometido no Notion é o mesmo da [[wiki/concepts/biblioteca-de-wireframes]] das aulas de wireframe?
- "Stage" e "papai designer": projeto e pessoa não identificados.
- A wiki já tem a aula em que ele desenha o page map do Nubank? A busca por referências que ele cita ("dá uma olhadinha lá no projeto do Nubank") pode estar em [[wiki/sources/wireframes-pratica-1-hero-page-map-frankenstein-referencias]].

## Raw Quotes

- "Todo o processo de design é intimamente ligado à pesquisa."
- "No caso de e-commerce, o bonito não é o critério."
- "A grande coisa não é você copiar e colar, é você modelar."
- "Link, ele tem que parecer link. Botão, ele tem que parecer botão."
- "É como se fosse um ímã visual."
