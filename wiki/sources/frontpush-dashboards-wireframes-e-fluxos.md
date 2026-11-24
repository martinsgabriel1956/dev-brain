---
type: source
title: "Wireframes e fluxos do DashClass: do levantamento de requisitos às telas (FrontPUSH)"
aliases: ["FrontPUSH dashboards aula 07", "DashClass aula 07", "07: Wires e Fluxos", "wireframes e fluxos do DashClass"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [dashboard, wireframe, fluxos, caminho-feliz, login, recuperacao-de-senha, login-social, home, resumo, sidebar, topbar, cards, continue-de-onde-parou, gamificacao, checkout, trilhas, rbac, rastreabilidade-de-requisitos, sketchbook, modo-escuro, hover, material-design, figma, inspiracoes]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-dashboards-wireframes-e-fluxos.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-24
---

# Wireframes e fluxos do DashClass: do levantamento de requisitos às telas (FrontPUSH)

## TL;DR

Sétima aula (cerca de 20 min) do módulo de dashboards do [[wiki/entities/frontpush|FrontPUSH]]. [[wiki/entities/nasser|Násser]] transforma o levantamento da aula 06 em fluxos e esboços de tela no iPad, e depois mostra o arquivo do [[wiki/entities/dash-class|DashClass]] no [[wiki/entities/figma|Figma]]. O quadro abre com "Wireframes, fluxos, Moodboard".

- **Primeiro os fluxos, a partir do usuário:** "pensa como se você fosse o usuário. [...] Primeira tela, o que eu tenho que fazer?" O login abre o fluxo do sucesso (login, boas-vindas, cadastro), o de esquecer a senha (e-mail ou SMS, código, nova senha, ou link por e-mail) e o de entrar com o Google ([[wiki/concepts/fluxos-bem-definidos]], [[wiki/concepts/caminho-feliz]]).
- **A Home é o hub:** "a página do fluxo central", um resumo com "continue de onde parou", um card de gamificação ("você já conseguiu tais troféus") e sugestões de cursos. Dela saem os fluxos de atualizar dados, tickets de dúvida, notificações, dados de acesso e preferências: "cada uma dessas aqui vai ser uma tela".
- **Onde fica cada coisa:** na [[wiki/concepts/sidebar]], "as principais entidades" (home, cursos, administração, suporte, logout); na top bar, busca, apps, notificações e perfil, "no canto superior direito", como no [[wiki/entities/google|Google]]. O ícone de administração "só vai aparecer para funcionários": "o sistema verifica o perfil" ([[wiki/concepts/rbac]]).
- **Fluxo de pagamento:** meus cursos → sugestões ou "novas trilhas" (nome tirado da [[wiki/entities/rocketseat|Rocketseat]]) → detalhe do curso com conteúdo programático → checkout.
- **Método:** rabiscar num sketchbook ou "folha grande", nomear os fluxos, **ticar cada requisito** do levantamento ("coloca um monte de checkbox lá"), e só depois passar para wireframes e "ir enxertando" com peças de UI (cards, dropdowns, modais), "não é na sorte [...] tem que ter um porquê" ([[wiki/concepts/rastreabilidade-de-requisitos]], [[wiki/concepts/wireframe]]).
- **Modo escuro e hovers:** o DashClass todo em dark, "por ser uma plataforma de vídeos" em que o aluno passa horas olhando; hover em listas e tabelas como "resposta à interação", com regras do [[wiki/entities/material-design|Material Design]] ([[wiki/concepts/modo-escuro]]).

## Key Claims

### Completar o levantamento e abstrair

- Depois do levantamento, "você vai pegar todas aquelas anotações e vai tentar completar ao máximo", perguntando ao cliente "até chegar em um consenso", e então "traduzir tudo aquilo [...] e abstrair em telas, abstrair em conteúdo, abstrair em fluxos". "Essa etapa é do Mood Board que a gente costuma fazer" ([[wiki/concepts/levantamento-de-requisitos]]).
- "Geralmente eu começo pelos fluxos." "A gente vai começar lá do começo. Pensa como se você fosse o usuário."

### Fluxos de login

- "Você vai começar a dar nome aos fluxos. Qual que é o primeiro fluxo? É o fluxo do sucesso. É como se nada tivesse dado errado." Login, "uma telinha de boas-vindas", cadastrar com e-mail e senha; "ele vai ser direcionado para onde? Quais são as primeiras mensagens que vão aparecer?" ([[wiki/concepts/caminho-feliz]]).
- "Como é que eu vou ter a noção de construir isso? Olhando para modelos." "É um exercício de abstração, é difícil, é normal": olhar inspirações, wireframes, modelos prontos e "o modelo que eu disponibilizei para vocês no DashClass" ([[wiki/concepts/modelar-referencias]]).
- Esqueci a senha: "tem o fluxo do e-mail e tem o fluxo do SMS". Pedir o e-mail ou o telefone, "conferir no banco de dados se isso deu certo", pedir o código enviado, "bateu o código de acesso, insira sua nova senha", "ou então, acesse pelo link que foi enviado pelo e-mail". Ao final, "é redirecionado para essa primeira tela".
- Login com o Google: "você vai tentar esboçar as telinhas de logar com o Google" ([[wiki/concepts/openid-connect]]).

### A Home como resumo

- "Eu preciso dar um aparato geral, mas [...] deixar claro para o usuário que ele tem que continuar de onde ele parou", "para ele não terminar as coisas pelo meio do caminho" ([[wiki/concepts/dashboard]]).
- Patterns: sidebar "sempre [...] do lado" com logo, Home e cursos: "as principais entidades que a gente desenhou, elas ficam aqui", mais logout e suporte. Top bar: "busca, [...] acesso a outros aplicativos do sistema, [...] acesso ao meu perfil, [...] uma barrinha de notificações". "Ah, Násser, como é que você sabe disso? Patterns" ([[wiki/concepts/patterns-de-dashboard]], [[wiki/concepts/sidebar]]).
- "As principais ações do sistema estão no seu lado esquerdo, na sidebar, as principais entidades": comprar curso, acessar, assistir, painel administrativo. Conta "no canto superior direito", como em "qualquer aplicativo" do Google ([[wiki/entities/google]]).
- Resumo em cards: "continue de onde parou", com thumbnail do último curso; em segundo plano, gamificação ("você já conseguiu tais troféus, continue assim, parabéns"); sugestões de novos cursos ("você está concluindo esse curso aqui [...] tem esse outro curso") ([[wiki/concepts/gamificacao]]).
- "Você não precisa desenhar tudo igualzinho [...] Isso aqui é somente um esboço inicial [...] Isso aqui é só o esqueleto" ([[wiki/concepts/fidelidade-de-prototipo]]).

### Os fluxos que saem da Home

- "A Home é o fluxo, é a página do fluxo central. Ele pode desembocar para vários outros fluxos."
- Atualizar meus dados ("olha só o CRUD do usuário bem aqui"), endereço, senha, preferências, central de ajuda, tickets de dúvida, notificações, dados de acesso, preferências. "E cada uma dessas aqui vai ser uma tela" ([[wiki/concepts/crud]]).
- Preferências: velocidade do player, resolução. Dados de acesso: senha antiga, nova, confirmação. Notificações: cursos concluídos, aulas novas. Tickets: dúvidas respondidas ou não, "que aí me linka com o fórum que tá lá nas aulas".
- "Percebe quantos fluxos a gente tá construindo? E [...] a gente só escreveu."

### Sidebar, perfil e administração

- Ícones da sidebar: home, meus cursos ("outra saída de fluxo"), perfil (todos os fluxos do perfil), outros aplicativos da plataforma.
- "Você não vai acertar de primeira, garanto para você [...] ele sempre está passível de atualizações." "Sempre comece pela Home, por esse resumo, porque ele vai te dar meio que um ponto de partida para vários fluxos. E aí você desenvolve cada ação em seu determinado fluxo e nomeia os seus fluxos."
- Administração: "esse ícone [...] só vai aparecer para funcionários [...] o sistema verifica o perfil, ele aparece ou não esse ícone", dando "acesso exclusivo ao painel administrativo" a quem "tem um perfil correto para isso" ([[wiki/concepts/rbac]], [[wiki/concepts/atores-do-sistema]]).
- Perfil na top bar, "por que que é isso, Násser? Patterns." "Você poderia estruturar de uma maneira um pouquinho diferente da minha? Lógico que sim." Para isso, a aba de inspirações.

### Fluxo de pagamento

- Sidebar → cursos → "meus cursos"; abaixo, "sugestões de novos cursos. Ou então, novas trilhas. [...] Peguei esse trilhas lá da Rocketseat" ([[wiki/entities/rocketseat]]).
- "O sistema vai identificar que esse curso aqui você não adquiriu. Clicou aqui, ele vai para um meio que um checkout." Tela de detalhe com conteúdo programático e botão de checkout, que leva ao pagamento.

### Rabiscar, ticar, enxertar

- "O ideal é você ter [...] um sketchbook [...] Já fazendo meu merchan aqui. Ou então, uma folha grande", anotando "esse aqui é o fluxo tal". Depois, "você passa para cá como wireframe" e, "como o seu esqueleto já está montado, você só vai enxertando" ([[wiki/concepts/wireframe]]).
- "Conforme você for fazendo os fluxos, você olha lá para o seu levantamento de requisito e sai ticando [...] coloca um monte de checkbox lá [...] até você extinguir todo o levantamento de requisitos. Desenhou todos os fluxos, você passa para [...] os wireframes" ([[wiki/concepts/rastreabilidade-de-requisitos]]).
- "Dashboard não é algo fácil, é muito detalhe, é muita coisa, é normal."
- No Figma, as telas estão marcadas com "etiquetas", que são os fluxos definidos. Para enxertar, "voltar aos princípios básicos de UI Design": estruturas de cards, dropdowns, modais, "como se fosse pecinhas de quebra-cabeça". Escolher um card "não é na sorte [...] Tem que ter um porquê" ([[wiki/concepts/porque-das-decisoes-de-design]], [[wiki/concepts/biblioteca-de-wireframes]]).
- "A gente está projetando, literalmente, algo que precisa de uma bagagem grande de UI Design."

### Modo escuro e hovers

- "As nossas aulas aqui, estão todas em Dark Pattern. Quer dizer, em Dark Pattern, não, né? Em modo Dark." Foi um questionamento feito ao cliente: "por ser uma plataforma de vídeos em que a pessoa está sempre olhando [...] horas e horas [...] pode cansar suas vistas e quando você está em um modo Dark, pode ficar mais confortável os olhos" ([[wiki/concepts/modo-escuro]]).
- "Existem Hovers em muitas listas [...] nas tabelas [...] Existe sempre uma resposta à interação." São "detalhezinhos que fazem a diferença", com "o Material Design estabelecendo lá todas as regrinhas" ([[wiki/concepts/feedback-do-sistema]]).
- Próximas aulas: artigos sobre como alocar informações, escolher gráficos e "regrinhas de UI Design".

### O arquivo no Figma (capturas)

- Páginas: Cover, Inspirations, StyleGuide & Grids, UI DashClass, Aulas. Na de inspirações, frames de kits prontos (Vuesax Analytics Dashboard, Analytics Dashboard Dark, Ecommerce Dashboard, Chat App, Mail App, Todo App, páginas de checkout, endereço e pagamento de e-commerce) e links de referência.
- Estilos locais: texto (heads, body), cor (cian, blue, black, white, gradient, gray, auxiliary) e grid (Desktop, iOS, Android, iPad, Dashboard 1, 2 e 3) ([[wiki/concepts/grid-de-dashboard]], [[wiki/concepts/style-guide]]).

## Precisões e ressalvas

1. **Modo escuro não é, por si, mais confortável.** `[external]` Estudos de polaridade (resumidos pela Nielsen Norman Group em 2020) mostram que texto escuro sobre fundo claro é lido com mais precisão por quem tem visão normal; o modo escuro ajuda em ambiente com pouca luz e para parte das pessoas com baixa visão (média-alta, sem fetch). Para uma plataforma de vídeo, o argumento mais forte é outro: fundo escuro some ao redor do player e não compete com o vídeo, a convenção de cinema que Netflix e YouTube seguem (inferência, alta). `[skill: ux-ui-mentor]` A referência `design-system.md`: dark mode "não é inverter as cores", é um tema com decisões próprias; evitar preto puro e branco puro, superfícies em camadas e bordas no lugar de sombras. Ver [[wiki/concepts/modo-escuro]].
2. **"Dark Pattern" corrigido na hora.** Desta vez ele mesmo corrige para "modo Dark". Dark pattern é outra coisa: design que engana o usuário ([[wiki/concepts/design-persuasivo]]). Na mentoria de UI Design o termo saiu errado e ficou.
3. **Hover não basta.** Em tela de toque não há hover, e quem navega por teclado precisa de foco visível. `[skill: ux-ui-mentor]` Estados de interação vêm em conjunto: hover, foco, pressionado, desabilitado. Ver [[wiki/concepts/indicador-de-foco]] (alta).
4. **Esconder o ícone não protege o painel.** Esconder a administração de quem não tem perfil é o padrão certo de interface (a referência `ux-enterprise-b2b.md`: esconder o que o usuário nunca poderá fazer), mas a autorização tem de ser verificada no servidor, em cada rota e requisição; a interface só reflete a regra (alta). Ver [[wiki/concepts/autenticacao-e-autorizacao]].
5. **"Continue de onde parou" é reconhecimento, não memória.** A sexta heurística de Nielsen (reconhecer em vez de lembrar), que a referência `teoria.md` lista, e o padrão de serviços de streaming como a [[wiki/entities/netflix|Netflix]] (inferência, alta).
6. **Ticar requisitos é rastreabilidade.** A lista com checkbox é uma matriz de rastreabilidade simples: cada requisito aponta para a tela ou fluxo que o atende, e nada fica sem dono. Funciona nos dois sentidos: tela sem requisito também é sinal de escopo inventado (inferência, alta). Ver [[wiki/concepts/rastreabilidade-de-requisitos]].
7. **"Etapa do Mood Board".** Mood board costuma ser o painel de referências visuais (cor, tipografia, clima); aqui o termo cobre a fase de traduzir requisitos em fluxos e esboços, que é mais *user flow* e *wireframe* do que mood board (inferência, média).
8. **Nomes reconstruídos da legenda:** "Dash Class" → DashClass (3×), "esquecer o seu senhor" → esquecer a sua senha (o quadro diz "Esquecer a senha"), "Nárcio" → Násser (2×), "ROM" → Home, "Rocket City" → Rocketseat. Ficaram literais: "dando procedimento", "de abstrair, animar", "olhando para as animações, quer dizer, para as inspirações" (correção dele), "já fazendo meu merchan aqui".

## Entities

- [[wiki/entities/nasser]]: instrutor.
- [[wiki/entities/dash-class]]: os fluxos e o arquivo.
- [[wiki/entities/figma]]: páginas, estilos e grids do arquivo.
- [[wiki/entities/google]]: conta no canto superior direito como pattern.
- [[wiki/entities/rocketseat]]: de onde veio o nome "trilhas".
- [[wiki/entities/material-design]]: regras de hover e estados.
- [[wiki/entities/netflix]]: referência de "continue de onde parou".
- [[wiki/entities/frontpush]]
- Sem página própria: Vuesax (kit de dashboard nas inspirações).

## Concepts

- [[wiki/concepts/rastreabilidade-de-requisitos]] (novo), [[wiki/concepts/modo-escuro]] (novo)
- [[wiki/concepts/fluxos-bem-definidos]], [[wiki/concepts/caminho-feliz]], [[wiki/concepts/openid-connect]]
- [[wiki/concepts/dashboard]], [[wiki/concepts/patterns-de-dashboard]], [[wiki/concepts/sidebar]], [[wiki/concepts/grid-de-dashboard]]
- [[wiki/concepts/levantamento-de-requisitos]], [[wiki/concepts/crud]], [[wiki/concepts/rbac]], [[wiki/concepts/atores-do-sistema]], [[wiki/concepts/autenticacao-e-autorizacao]]
- [[wiki/concepts/wireframe]], [[wiki/concepts/fidelidade-de-prototipo]], [[wiki/concepts/biblioteca-de-wireframes]], [[wiki/concepts/modelar-referencias]], [[wiki/concepts/porque-das-decisoes-de-design]], [[wiki/concepts/style-guide]]
- [[wiki/concepts/gamificacao]], [[wiki/concepts/feedback-do-sistema]], [[wiki/concepts/indicador-de-foco]], [[wiki/concepts/design-persuasivo]]

## Open Questions

- O cliente pediu o modo escuro ou foi decisão dele? A fala mistura os dois ("um dos questionamentos que eu fiz [...] e que eu também decidi").
- Haverá modo claro como alternativa? A referência da skill recomenda respeitar `prefers-color-scheme`.
- Quais são os "artigos" prometidos sobre alocar informações e escolher gráficos?

## Raw Quotes

- "Pensa como se você fosse o usuário."
- "A Home é o fluxo, é a página do fluxo central."
- "Você não vai acertar de primeira, garanto para você."
- "Vai desenhando e vai ticando [...] até você extinguir todo o levantamento de requisitos."
- "Não é na sorte, né? Tem que ter um porquê."
