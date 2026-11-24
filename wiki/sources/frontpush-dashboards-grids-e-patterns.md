---
type: source
title: "Grids e patterns de dashboards no DashClass (FrontPUSH)"
aliases: ["FrontPUSH dashboards aula 03", "DashClass aula 03", "03: Grids & Patterns Dashboards", "grids e patterns de dashboard"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [dashboard, ui-design, grid, grid-de-colunas, offset, gutter, container, resolucao, breakpoint, padroes-de-interface, login, sidebar, topbar, app-launcher, cards, graficos, tabelas, filtros, formularios, modal, confirmacao, cor-semantica, psicologia-das-cores, figma, google, material-design]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-dashboards-grids-e-patterns.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-24
---

# Grids e patterns de dashboards no DashClass (FrontPUSH)

## TL;DR

Terceira aula (cerca de 15 min) do módulo de dashboards do [[wiki/entities/frontpush|FrontPUSH]]. Antes dos rabiscos, do mood board e do levantamento de requisitos, "a gente sempre começa dos Grids, a gente sempre começa dos Patterns".

- **Três grids, mesma base:** 12 colunas, como nas landing pages do curso, "para [...] a gente não mudar o modelo de forma muito abrupta". Muda só a largura da coluna e o offset, que empurra tudo para a direita para caber a sidebar. Slide: grid 1 = 70/30/240, grid 2 = 80/30/120, grid 3 = 66/30/280 (coluna/gutter/offset, em px). No [[wiki/entities/figma|Figma]]: tipo Left, não Center nem Stretch, em frame 1440 × 900 (16:10) ([[wiki/concepts/grid-de-dashboard]]).
- **Container curto de propósito:** 1170, 1290 e 1122 px, porque em empresa "geralmente eles colocam computadores [...] mais capadinhos", com HD ou Full HD "no máximo". O grid é fixo; fluido e [[wiki/concepts/breakpoint|breakpoints]] ficam para a adaptação mobile.
- **Sete patterns** "em todo e qualquer Dashboard" ([[wiki/concepts/patterns-de-dashboard]]):
  1. **Login:** "uma primeira barreira", porque o acesso "é restrito aos funcionários, aos gerentes".
  2. **[[wiki/concepts/sidebar|Sidebar]]:** "é como se fosse o menu das nossas Landing Pages", com os principais fluxos de navegação.
  3. **Top bar:** busca, notificações e usuário. Pode ter os "nove pontinhos" de apps, como o [[wiki/entities/google|Google]].
  4. **Cards e gráficos:** comparativos, com filtros.
  5. **Listas e tabelas:** filtros e ações.
  6. **Formulários:** com uma "sub-sidebar" do usuário.
  7. **Modais:** confirmar, avisar, informar.
- **Hierarquizar para não lotar:** dashboards antigos tinham "muitas informações concentradas em uma tela só"; launcher, menu que expande e sidebar "ajuda a classificar e hierarquizar" ([[wiki/concepts/hierarquia-visual]]).
- **Cores dos modais:** verde para sucesso, azul para informação, amarelo para aviso, vermelho para erro, branco para neutro. Ele chama isso de psicologia das cores; é [[wiki/concepts/cor-semantica]].

## Key Claims

### Grid e patterns antes de tudo

- Processo de UI de sempre: "brainstorm, [...] rabiscos, [...] wireframes, [...] mood board, [...] levantamento de requisitos, a gente vai construindo até chegar em uma UI final". "Mas a gente sempre começa dos Grids, a gente sempre começa dos Patterns, dos modelos iniciais da pesquisa" ([[wiki/concepts/wireframe]], [[wiki/concepts/briefing]]).
- Os patterns "vão sempre se repetir e [...] já vai ficar na nossa cabeça quando a gente começar a desenhar os nossos primeiros wireframes" ([[wiki/concepts/padroes-de-interface]]).

### Os três grids

- "Tem três modelos principais que eu costumo utilizar [...] o que eu estou utilizando é o Grid 1."
- Mesmas 12 colunas das landing pages: "a gente já está acostumado com esse tipo de modelo [...] tem várias features que a gente já consegue aplicar [...] ele é muito versátil, então não tem por que a gente mudar" ([[wiki/concepts/grid-de-colunas]], [[wiki/concepts/grid-system]]).
- "A única coisa que muda é que o width [...] muda um pouquinho [...] 70 pixels ou em 80 pixels, mudando apenas [...] o offset", deslocado à direita "para poder caber justamente aqui o nosso sidebar".
- Grid 1 no Figma: "12 colunas [...] do tipo Left, tá vendo que ele não está no Center, nem em Stretch [...] é um Grid fixo de largura de coluna de 70 pixels, um Gutter entre as colunas de 30 e um Offset [...] de 240 pixels". Grid 2: 80 px de coluna, offset de 120, gutter de 30. Grid 3 só aparece no slide: 66 px, gutter 30, offset 280.
- "Todos esses Grids [...] estão orientados ao frame 1440 por 900, padrão 16 por 10."
- "Variações [...] de um pouquinho mais de Offset, um pouquinho mais de Gutter [...] não tem problema nenhum." O objetivo é "não fazer uma discrepância muito grande do Grid que a gente costumeiramente sempre utiliza".
- Detalhes: aba Style Guide e Grids do arquivo, frame "Grid Dashboard 1", ligar a visibilidade ("o olhinho") e abrir os ajustes do layout grid.

### Por que telas pequenas

- Containers de 1290, 1170 e 1122 px: "ele é curtinho e é interessante". Dashboards "têm que ser feitos em telas pequenas": "costumeiramente são as resoluções que a gente utiliza em notebooks [...] em computadores mais antigos", e em empresa, "a não ser que a empresa [...] seja muito rica de verdade", os computadores são "mais capadinhos". "Você não vai ter [...] trabalhando numa tela 4K"; "HD, resolução Full HD, no máximo".
- Desenhar nesse tamanho faz com que "a compatibilidade daquilo que vai ser literalmente implementado na vida real seja bem próximo".
- "Os offsets [...] estão fixos e adequados para esse tipo de tela": ao aumentar o frame, o grid não muda. "É um Grid fixo, é um container fixo"; dá para torná-lo fluido "como a gente também faz isso em landing pages, vai ter o Breakpoint". "Vamos primeiro no Desktop, depois a gente faz a adaptação para o Mobile" ([[wiki/concepts/breakpoint]]).

### Patterns: o que são

- "Telas ou elementos [...] que vai estar presente em todo e qualquer Dashboard"; "é muito difícil você achar um Dashboard que não tenha essas estruturas", embora possa haver "um ou outro Pattern que em Dashboard não é utilizado" ([[wiki/concepts/patterns-de-dashboard]]).

### Login

- "Sempre vai ter uma telinha de Login. Afinal, nós estamos trabalhando com um ambiente empresarial em que o acesso às informações é restrito aos funcionários, aos gerentes [...] você tem que ter uma primeira barreira [...] para poder você estabelecer esse controle de acesso" ([[wiki/concepts/autenticacao-e-autorizacao]]).
- Slide: tela dividida, com formulário à esquerda ("Faça o login para acessar a plataforma", e-mail, senha com botão de mostrar, "Manter logado", "Esqueceu sua senha? Clique aqui", Entrar, "Ainda não tem uma conta?" e Criar conta) e um carrossel à direita ("Liberdade: assista de onde você quiser").

### Sidebar e top bar

- "Sidebar [...] é como se fosse o menu das nossas Landing Pages." O menu fica no topo "por um Pattern", "porque se eu ficar mudando demais esse Pattern, ele pode ser que piore a experiência do usuário"; a sidebar "contém os principais fluxos de navegação" ([[wiki/concepts/sidebar]], [[wiki/concepts/menu-fixo]]).
- Slide: versão recolhida (só ícones) e expandida (logo, Home, Cursos, Meu perfil, Administrativo; Suporte "abra um ticket para contatar o suporte"; Sair), com o item ativo marcado por uma barra à esquerda.
- Trocar de aplicativo: o Google, "por ele ser uma plataforma que tem inúmeros aplicativos", tem o ícone que abre "todos os Google Apps" (Conta, Pesquisa, Maps, YouTube, Play, Gmail, Finanças, Documentos). "Esses padrõezinhos [...] são costumeiramente mais utilizados em estruturas de Dashboard, estruturas de Web Apps" ([[wiki/entities/google]]).
- "Top Bar [...] é a barra agora do topo e não do lado, onde contém outros controles." No DashClass, "lembretes, de notificações e a parte de usuário" e busca. Slide: campo "Buscar...", sino com contador (3) e "Olá, Násser Yousef Ali" com dropdown.
- Pode ter "esses nove pontinhos [...] para poder você ter o acesso de outras sessões, porque você precisa classificar as informações de uma forma mais leve".
- "É muito comum, principalmente em Dashboards mais antigos [...] você ter muitas informações concentradas em uma tela só." "Três pontinhos", "um menu que expande", "uma Sidebar com essas informações" ajudam "a classificar e hierarquizar melhor essas informações" ([[wiki/concepts/hierarquia-visual]], [[wiki/concepts/densidade-de-informacao]]). Outros padrões virão com o [[wiki/entities/material-design|Material Design]].

### Cards e gráficos

- "Amplamente utilizado para poder a gente dispor as informações": "estabelecer os gráficos de forma comparativa [...] ajustando os filtros para poder a gente ter o melhor ambiente comparativo para poder melhor realizar [...] decisões, juntamente com os Cards" ([[wiki/concepts/dashboard]]).
- Slide (Painel Administrativo): vendas no mês (R$ 68.584,56) com medidor de 68% da meta; vendas por categoria (fisioterapia, neurologia, ortopedia); ranking de cursos mais vendidos com filtro; área de total de vendas por mês, curso X × curso Y; card de acessos (547 usuários únicos, −15% em 15 dias); ranking de aulas e reações; usuários contra o ano passado; chat; tabela de últimas vendas; botão "Adicionar usuário".

### Listas, tabelas e formulários

- "Como dispor as informações aqui dentro de listas e tabelas, quais são as principais informações, quais são os filtros. Vocês vão ver que tem muitos filtros [...] e as principais ações." Selecionar também segue os patterns, "para poder não confundir o usuário".
- Slide (Vendas): breadcrumb Início > Vendas; busca + Buscar + Filtrar; "03 resultados para a pesquisa"; filtros em dropdown (Conteúdo, Categoria, Ordenar por) com botão de limpar; colunas ordenáveis (ID, Cliente, Curso, NFe, Data, Valor, Ação); status da NFe com ícone, cor e texto (Emitida, Cancelada, Revisão); ações por linha (PDF, CSV, editar, excluir); exportar .pdf e .csv.
- Formulários: "uma sidebar específica para o usuário [...] meio que uma sub-sidebar", "que a gente também estabelece aqui como padrão". Slide: Meu perfil, Dados pessoais, Acesso, Minhas conquistas, Notificações, Preferências; formulário em seções (Dados pessoais, Informações pessoais, Endereço) com "Salvar alterações".

### Modais e cores

- "Caixinhas de confirmação": "eu vou executar determinada ação, sempre tem que ter uma caixinha me confirmando, me perguntando [...] e reafirmando a ação". Exemplos: "você tem certeza que [quer] excluir?"; "Ops, aconteceu algum erro, tentar novamente ou então reportar algum erro"; "deu certo, concluído" ([[wiki/concepts/modal]], [[wiki/concepts/feedback-do-sistema]]).
- "É muito comum em dashboard a gente utilizar de modais para poder reafirmar as ações que o usuário tomou, ou então questionar, ou então avisar, ou então informar."
- Cores do style guide, "utilizando a psicologia das cores": sucesso "verdinho", "você coloca ícones na cor verde"; informativo em azul; aviso "geralmente amarelo"; erro vermelho; "mensagens neutras, que são brancas" ([[wiki/concepts/cor-semantica]], [[wiki/concepts/psicologia-das-cores]]).
- Slide: "Você ainda está aí?" (autoplay); "Oops... Aconteceu um erro!" com "Tentar novamente"; "Dúvida enviada com sucesso!"; "Obrigado, Násser! Parabéns por ser um usuário Premium", com número do pedido e e-mail de confirmação para um endereço @comosevirar.com.br.
- Próxima aula: "mais modelos de wireframes", junto com o levantamento de requisitos.

## Precisões e ressalvas

1. **A conta dos containers fecha.** 12 × 70 + 11 × 30 = 1.170; 12 × 80 + 11 × 30 = 1.290; 12 × 66 + 11 × 30 = 1.122. Somando o offset, sobram 30 px à direita nos grids 1 (240 + 1.170 = 1.410) e 2 (120 + 1.290 = 1.410) e 38 px no grid 3 (280 + 1.122 = 1.402), dentro do frame de 1.440 (cálculo, alta). Ver [[wiki/concepts/grid-de-dashboard]].
2. **1440 não é "tela pequena" para todo mundo.** `[external]` Pelas séries da StatCounter, 1920 × 1080 lidera no desktop, mas 1366 × 768 e 1536 × 864 (notebook Full HD com escala de 125%) seguem comuns (média, sem fetch). Nessas telas o layout de 1.410 px estoura e precisa ser fluido, o que reforça a promessa de breakpoints. E 1440 × 900 é 16:10, proporção de MacBook; a maioria dos notebooks Windows é 16:9 (média-alta).
3. **Grid fixo no Figma, fluido no código.** `[skill: ux-ui-mentor]` A referência `grid-layout.md` recomenda container fluido para dashboards e tabelas e o layout "Dashboard (Mixed)": métricas no topo, gráfico largo + lista lateral, tabela embaixo. É o arranjo do slide de cards. Em CSS, a sidebar costuma ser uma coluna fixa e o conteúdo, uma coluna `1fr` com seu próprio grid de 12 (inferência, alta).
4. **Grid 2 provavelmente é o da sidebar recolhida.** O offset de 120 px combina com a sidebar só de ícones do slide, e o de 240 px com a expandida (inferência, média). A aula não explica o grid 3.
5. **"Psicologia das cores" aqui é cor semântica.** Verde = sucesso, vermelho = erro, amarelo = aviso, azul = informação é convenção de interface, não associação emocional. `[skill: ux-ui-mentor]` A referência `design-acessibilidade.md` lembra: "nunca use cor como único meio de informação". Os modais e os status da NFe do slide já fazem isso certo, com ícone, cor e texto juntos.
6. **Nem toda ação pede modal.** `[skill: ux-ui-mentor]` `modais-overlays.md` reserva o modal para ação destrutiva ou irreversível, input pequeno e alerta crítico; `estados-feedback.md` sugere toast de 3–4 s para ação relevante (ex.: "dúvida enviada") e página dedicada para ação crítica (pagamento); `ux-enterprise-b2b.md` prefere "desfazer" a confirmação em ações reversíveis. O "sempre tem que ter uma caixinha" vale para excluir, não para tudo.
7. **Tabelas de dashboard.** `[skill: ux-ui-mentor]` A referência enterprise trata a tabela como "um produto dentro do produto": chips de filtros ativos com "limpar tudo", exportação que respeita os filtros, estados de vazio e erro, seleção com ações em lote. O slide de Vendas já tem contador de resultados, filtros com limpar e exportação.
8. **Launcher do Google.** O ícone de apps do Google é uma grade de 3 × 3 pontos, e não "três pontinhos"; a própria fala se corrige depois ("nove pontinhos") (alta).
9. **Pistas da origem.** As categorias do slide (fisioterapia, neurologia, ortopedia) e o domínio @comosevirar.com.br no modal de compra mostram que as telas vêm do [[wiki/entities/como-se-virar|Como se virar]] (alta).
10. **Nomes reconstruídos da legenda:** "Dash Class" → DashClass (5×), "Nasser" → Násser, "Learning Pages" → landing pages, "DashPoint" → dashboard. Ficaram literais: "acesso de outras sessões" (provavelmente "seções"), "toda a partir do fluxo de Login", "Selecionar, que a gente também precisa". O slide da top bar mostra o nome "Násser Yousef Ali".

## Entities

- [[wiki/entities/nasser]]: instrutor.
- [[wiki/entities/dash-class]]: o projeto.
- [[wiki/entities/figma]]: layout grid tipo Left, frame 1440 × 900.
- [[wiki/entities/google]]: o launcher de apps como exemplo de pattern.
- [[wiki/entities/material-design]]: outros padrões prometidos.
- [[wiki/entities/como-se-virar]]: origem visível nas telas.
- [[wiki/entities/frontpush]]

## Concepts

- [[wiki/concepts/grid-de-dashboard]] (novo), [[wiki/concepts/patterns-de-dashboard]] (novo), [[wiki/concepts/sidebar]] (novo)
- [[wiki/concepts/grid-de-colunas]], [[wiki/concepts/grid-system]], [[wiki/concepts/breakpoint]]
- [[wiki/concepts/padroes-de-interface]], [[wiki/concepts/menu-fixo]], [[wiki/concepts/hierarquia-visual]], [[wiki/concepts/densidade-de-informacao]]
- [[wiki/concepts/autenticacao-e-autorizacao]]
- [[wiki/concepts/modal]], [[wiki/concepts/feedback-do-sistema]], [[wiki/concepts/cor-semantica]], [[wiki/concepts/psicologia-das-cores]]
- [[wiki/concepts/dashboard]], [[wiki/concepts/wireframe]], [[wiki/concepts/briefing]]

## Open Questions

- Para que serve o grid 3 (offset 280)? Sidebar mais larga, ou sidebar + sub-sidebar?
- Ele diz usar o grid 1 (offset 240), mas as telas dos slides mostram a sidebar recolhida. O grid muda quando a sidebar expande?
- Como o grid fixo vira fluido no código? Prometido para a adaptação mobile e o template HTML/CSS/JS.

## Raw Quotes

- "A gente sempre começa dos Grids, a gente sempre começa dos Patterns."
- "Sidebar, basicamente, é como se fosse o menu das nossas Landing Pages."
- "Você não vai ter, por exemplo, trabalhando numa tela 4K."
- "Sempre vai ter uma telinha de Login [...] você tem que ter uma primeira barreira."
