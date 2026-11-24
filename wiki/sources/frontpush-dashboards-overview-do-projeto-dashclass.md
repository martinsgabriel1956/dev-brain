---
type: source
title: "Overview do projeto DashClass: origem, funcionalidades e fluxos (FrontPUSH)"
aliases: ["FrontPUSH dashboards aula 02", "DashClass aula 02", "02: Overview do Projeto DashClass", "overview do DashClass"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [dashboard, ui-design, ux-design, curso, plataforma-de-ensino, gamificacao, engajamento, fluxos, login, recuperacao-de-senha, checkout, painel-administrativo, sidebar, top-bar, modal, dropdown, grid, style-guide, wireframe, figma, notion, finclass, hotmart]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-dashboards-overview-do-projeto-dashclass.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-24
---

# Overview do projeto DashClass: origem, funcionalidades e fluxos (FrontPUSH)

## TL;DR

Segunda aula (cerca de 13 min) do módulo de dashboards do [[wiki/entities/frontpush|FrontPUSH]]. [[wiki/entities/nasser|Násser]] conta de onde veio o [[wiki/entities/dash-class|DashClass]] e passeia pelo arquivo do [[wiki/entities/figma|Figma]].

- **Origem:** "junção de projetos que desenvolvi para plataformas de ensino". Na [[wiki/entities/finclass|Finclass]] (Grupo Primo, web e app) ele trabalhou só no fluxo de exibição e personalização do player de vídeo, mas viu os fluxos de trabalho. No [[wiki/entities/como-se-virar|Como se virar (CSV)]], de uma dupla de médicos do Nordeste para calouros de medicina, fez "toda a parte [de] fluxo", e o forte era a [[wiki/concepts/gamificacao]]. Para [[wiki/entities/gustavo-web|Gustavo Web]] (PHP, ex-UpInside, hoje Black Dev) fez o design e os fluxos.
- **Não é cópia:** "pelo profissionalismo, eu não posso literalmente trazer o fluxo" de nenhum dos três. O DashClass é um mix "enxuto" que é "o feijão com arroz para poder fazer todo e qualquer tipo de dashboard" ([[wiki/concepts/modelar-referencias]]).
- **O que é:** "uma plataforma de ensino para disponibilizar aulas gravadas", "como se fosse a [[wiki/entities/hotmart|Hotmart]] que vocês estão me vendo", mais específica e com UI mais trabalhada.
- **Escopo (slide):** fluxo de pagamentos, login, gamificação, fluxo de usuário, painel administrativo, fluxo de aulas; adaptação para mobile e template em HTML/CSS/JS "em breve". Dashboard "dá muito trabalho", "mais do que um one page": "é muito dropdown, é muito modal".
- **Grid:** a sidebar pede "um novo modelo de grid, um pouco mais recuado, não é centralizado como [...] em landing pages", mas "a gente continua no padrão de 12 grids" ([[wiki/concepts/grid-system]]).
- **Arquivo:** aba de inspirações (prints de cards, gráficos e esquemas para o pontapé dos [[wiki/concepts/wireframe|wireframes]]), style guide e grids, telas, página de aulas. A home ainda está em wireframe.
- **Fluxos:** login e recuperação de senha (telefone ou e-mail); home com sidebar, top bar e modais de notificação e perfil; perfil com conquistas, preferências do player, troca de senha, tickets de dúvida, dados pessoais, notificações e progresso; cursos (salvos, episódios, material de apoio, fórum); pagamento (cartão, endereço, resumo, sucesso e erro); pesquisa e central de ajuda; painel administrativo (usuários, acessos, vendas por curso, fluxo de caixa, aulas com mais reações, chat, últimas vendas, CRUD de cursos e aulas).

## Key Claims

### Para que serve o projeto

- Objetivo da aula: "estabelecer todos os pilares" para "ter noções de como desenvolver um Dashboard, quais são os patterns, [...] quais são os fluxos que eu utilizei que podem ajudar vocês a desenvolverem qualquer outro tipo de Dashboard". O login, por exemplo, "vai ser bem similar em qualquer outro Dashboard" ([[wiki/concepts/padroes-de-interface]]).

### As três plataformas de origem

- Slide: "Junção de projetos que desenvolvi para plataformas de ensino, trabalhei em conjunto no FinClass e CSV." Na fala ele acrescenta: "esqueci de mencionar outro, que foi a plataforma de ensino do Gustavo Web, que faz PHP lá da Blackdev."
- **Finclass:** "uma plataforma de ensino do grupo primo para ensinar finanças", "um Dashboard, pessoal, gigantesco, que tem tanto a parte web como a parte do app". Ele trabalhou "em um pequeno fluxo voltado mais para a exibição de vídeo e personalização dos players de vídeo", "mas eu tive acesso aos fluxos de trabalho" ([[wiki/entities/finclass]]).
- **CSV, "a sigla para Como se virar":** "uma dupla de médicos que atua lá no Nordeste". "Quando as pessoas passam na faculdade de medicina, eles ficam muito perdidos." "O forte dessa plataforma seria uma estrutura de gamificação para poder melhor engajar o usuário, fazer com que ele cumpra todas as etapas, com que ele assista todas as aulas" ([[wiki/entities/como-se-virar]], [[wiki/concepts/gamificacao]]). Ele fez "toda a parte fluxo".
- Do CSV vem "toda essa estrutura de gamificação, de reação de aulas ao vivo que eu vou conseguir modelar algumas coisas para o DashClass".
- **Gustavo Web:** "era da UpInside, agora está meio que carreira solo na Black Dev"; "pelo menos toda a parte de design foi o que desenvolvi, fluxos e tudo mais" ([[wiki/entities/gustavo-web]]).
- Limite ético: "pelo profissionalismo, eu não posso literalmente trazer o fluxo da Finclass [...] do Como se virar [...] do projeto do Gustavo Web". O DashClass é feito "modelando, fazendo um mix dessas plataformas, trazendo o que é mais interessante e enxuto", "pegando a essência dos pilares de como construir um dashboard" ([[wiki/concepts/modelar-referencias]]).

### Briefing antes das telas

- Próxima aula: "o levantamento de requisitos, como literalmente a gente começa um dashboard, como a gente faz a levantamento de um briefing para poder descobrir quais são as informações que são mais importantes" ([[wiki/concepts/briefing]], [[wiki/concepts/requisitos-funcionais-e-nao-funcionais]]).
- Retoma a aula anterior: plataformas são "ferramentas específicas para determinada empresa ou negócio", e "uma determinada empresa de um determinado nicho quer uma plataforma com uma característica mais específica, e a gente tira e constrói isso também através de um briefing" ([[wiki/concepts/tipos-de-dashboard]]).

### Escopo e esforço

- "O que vai ter no DashClass? Fluxo de pagamentos, login, gamificação, fluxo de usuário, painel administrativo, fluxo de aulas", e, "ainda não terminado", "a adaptação para o mobile e um template em HTML, CSS e JavaScript para vocês utilizarem nos projetos de vocês". O slide marca esses dois como "(em breve)".
- "Dá muito trabalho para poder fazer um dashboard, mais do que um one page, porque é muito detalhe para a gente construir, é muito dropdown, é muito modal" ([[wiki/concepts/modal]]).
- Sidebar: "é um novo modelo de grid, um pouco mais recuado, não é centralizado como a gente costuma fazer em landing pages, então tem algumas modificações que são interessantes para a gente trazer na parte de código."

### O que é o DashClass

- "É uma plataforma de ensino para disponibilizar aulas gravadas para alunos assistirem, então é como se fosse a Hotmart que vocês estão me vendo, só que com um caráter bem mais específico, com uma UI talvez um pouquinho mais trabalhada" ([[wiki/entities/hotmart]], [[wiki/concepts/dashboard]]).
- O arquivo fica no Notion, com senha das "aulas do começo do FrontPUSH", e o aluno faz uma cópia.

### Inspirações, style guide e grid

- Segunda aba, inspirações: "muitos prints [...] que eu tirei de vários lugares", "com relação a informações, com relação a gráficos, então tem muitos cards e esquemáticos", "para poder a gente dar a primeira partida no nosso cérebro para poder construir os nossos wireframes".
- [[wiki/concepts/style-guide|Style guide]] e grids também estão no arquivo. "Os grids que a gente utiliza para dashboard são diferentes, eles têm um pequeno recuo, tem uns tamanhos ali que variam, mas a gente continua no padrão de 12 grids"; o detalhe fica para as próximas aulas ([[wiki/concepts/grid-system]]).

### Home e navegação

- Fluxos ("a cereja do bolo"): mobile só começado. Login; home com "os modelos de sidebar", "os modelos de top bar" e os modais que abrem ao clicar em notificações e no profile.
- Home: "curso de marketing digital, deixei em modelos de wireframes, ainda não subi para alta, alta, alta fidelidade"; seções continue de onde parou, principais instrutores, notificações, principais trilhas ([[wiki/concepts/fidelidade-de-prototipo]]).

### Fluxo de usuário

- Profile com "meus dados" e "meio que um sistema de conquistas básico para poder a gente estabelecer essa gamificação de forma simples".
- Preferências do player: velocidade (1.5x), volume (60%), qualidade (1080p), salvas "para todos os vídeos você não precisar ficar setando as mesmas informações sempre".
- Dados de acesso (senha antiga, senha nova). Tickets de dúvida por aula: quando a dúvida é respondida, o ticket aparece numa lista de "dúvidas já respondidas e é emitido uma notificação".
- Dados pessoais, notificações e "meu progresso": "quais são os cursos que eu estou assistindo e o quanto que eu já completei de cada curso". "Deixar essa parte [...] sempre exposta de que você não completou esses aqui, então falta completar isso, é interessante para poder a gente engajar melhor o usuário" ([[wiki/concepts/goal-gradient-effect]]).

### Cursos e aulas

- Fluxo de cursos: lista, cursos salvos, caracterização do curso, episódios, material de apoio, "uma tag para poder você enviar sua dúvida".
- Aula: material de apoio específico, "um fórum para poder você tirar as dúvidas ou então enviar suas dúvidas", e os cards dessas interações.

### Pagamento

- "Um pequeno fluxo de pagamento": ao escolher um curso, dados do cartão de crédito, endereço de cobrança, "meio que um resumo do pedido", e as telas de sucesso, "não foi possível concluir seu pagamento" e resumo, "informando isso aqui em modais e essas barrinhas de notificações". Haverá aulas específicas sobre esses recursos ([[wiki/concepts/feedback-do-sistema]]).

### Pesquisa, ajuda e login

- Pesquisa: o dashboard "é tão interessante que futuramente se a gente fosse desenvolver um webapp baseado nesse dashboard seria muitíssimo interessante", com "muitos filtros" ou levando funções do "projeto do blog de react" do curso.
- Central de ajuda: enviar mensagem, fale conosco, reportar um erro. Login com recuperação de senha "seja por telefone, seja por e-mail".

### Painel administrativo

- Modelos "para poder a gente adicionar usuário, ver os acessos, total de vendas de quais cursos estão vendendo mais, qual é o fluxo de caixa desse mês, quais são as aulas que têm mais reações, o chat, as últimas vendas" ([[wiki/concepts/tipos-de-dashboard]]).
- Também "dashboards específicos de tabelas e listas para vendas, para os usuários, para os cursos e para manter os cursos, adicionar novos cursos e novas aulas".

## Precisões e ressalvas

1. **O "como a Hotmart" é parcial.** Hotmart é marketplace e infraestrutura de venda para muitos produtores; o DashClass é a plataforma de um só produtor, com área do aluno e admin próprios. A comparação vale para a área de membros (inferência, alta). Ver [[wiki/entities/hotmart]].
2. **Painel admin = financeiro + estratégico.** Vendas por curso, fluxo de caixa e últimas vendas são o dashboard financeiro da aula 01; aulas com mais reações e acessos são o estratégico (engajamento). Fecha com o recorte "financeiro, estratégico e plataforma" de [[wiki/sources/frontpush-dashboards-introducao-para-que-serve-utilidades-tipos]] (inferência, alta).
3. **Progresso exposto é goal gradient, com cuidado.** `[skill: ux-ui-mentor]` A referência `onboarding.md` lista progresso, recompensa variável, status e pertencimento como os mecanismos da gamificação e avisa que ela falha quando a recompensa é vazia (badge sem significado) ou disfarça produto ruim (*overjustification*). O "falta completar isso" sempre visível funciona se mostra o que já foi feito; só a falta tende a desanimar, como o próprio Násser disse no exemplo dos "40 quilômetros" ([[wiki/concepts/goal-gradient-effect]]).
4. **"12 grids" é 12 colunas.** O recuo da sidebar tira a área de conteúdo do centro: o grid de 12 colunas passa a ocupar o espaço à direita da sidebar, em vez de um container centralizado (inferência, alta). `[skill: ux-ui-mentor]` A referência `grid-layout.md` chama isso de layout com navegação lateral e sugere container fluido para dashboards.
5. **"Gameficação" no slide** é erro de digitação; a fala diz gamificação.
6. **Login "bem similar em qualquer outro Dashboard"** é a [[wiki/concepts/lei-de-jakob]] aplicada: fluxos de autenticação são o lugar onde menos convém inventar.
7. **Quem é quem.** `[external]` UpInside Treinamentos é uma escola online de programação web (PHP) de Robson V. Leite (média, sem fetch). "Black Dev" ou "Blackdev": grafia não verificada. "Gustavo Web" corrige o "Gustavo Webb" da aula 01.
8. **O orçamento do freela.** O orçamento "UI Design Dashboard" de [[wiki/sources/frontpush-monetizacao-freelancer-modelos-de-orcamento-e-invoice]] (plataforma de cursos com gamificação, telas de administrador e de aluno, chat ao vivo, tickets de dúvida) agora casa bem com o Como se virar. Os itens de aluno do orçamento (perfil e preferências, tickets, progresso, aulas + fórum + arquivos, login + esqueci senha) reaparecem quase iguais no DashClass (inferência, média-alta).
9. **Nomes reconstruídos da legenda:** "Thin Class" → Finclass (3×; o slide escreve "FinClass"), "Dash Class" → DashClass (pelo slide), "Up Inside" → UpInside, "only pay" → one page, "front push" → FrontPUSH. Ficaram literais: "Blackdev" e "Black Dev", "reação de aulas ao vivo", "toda a parte fluxo".

## Entities

- [[wiki/entities/nasser]]: instrutor.
- [[wiki/entities/dash-class]]: o projeto.
- [[wiki/entities/finclass]]: player de vídeo; web e app.
- [[wiki/entities/como-se-virar]] (novo): plataforma CSV, gamificação.
- [[wiki/entities/gustavo-web]] (novo): professor de PHP, cliente de design e fluxos.
- [[wiki/entities/hotmart]]: comparação.
- [[wiki/entities/figma]], [[wiki/entities/frontpush]]
- Sem página própria: Grupo Primo, UpInside, Black Dev, Notion.

## Concepts

- [[wiki/concepts/gamificacao]] (novo)
- [[wiki/concepts/dashboard]], [[wiki/concepts/tipos-de-dashboard]]
- [[wiki/concepts/modelar-referencias]], [[wiki/concepts/padroes-de-interface]], [[wiki/concepts/lei-de-jakob]]
- [[wiki/concepts/briefing]], [[wiki/concepts/requisitos-funcionais-e-nao-funcionais]]
- [[wiki/concepts/grid-system]], [[wiki/concepts/style-guide]], [[wiki/concepts/wireframe]], [[wiki/concepts/fidelidade-de-prototipo]]
- [[wiki/concepts/modal]], [[wiki/concepts/feedback-do-sistema]]
- [[wiki/concepts/goal-gradient-effect]]

## Open Questions

- Qual é o recuo e quais são as larguras do grid de dashboard? Prometido para as próximas aulas.
- "Reação de aulas ao vivo": reações a aulas (o admin mostra "aulas com mais reações") ou aulas ao vivo com reações? O orçamento do freela tinha "chat ao vivo".
- O "blog de react" citado é o projeto do módulo de React do curso? Ainda não ingerido.

## Raw Quotes

- "É o feijão com arroz para poder fazer todo e qualquer tipo de dashboard."
- "Pelo profissionalismo, eu não posso literalmente trazer o fluxo da Finclass para vocês."
- "É como se fosse a Hotmart que vocês estão me vendo, só que com um caráter bem mais específico."
- "Dá muito trabalho para poder fazer um dashboard, mais do que um one page [...] é muito dropdown, é muito modal."
