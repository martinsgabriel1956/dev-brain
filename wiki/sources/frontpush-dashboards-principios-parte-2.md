---
type: source
title: "Princípios de dashboards, parte 2: levantamento de requisitos, atores, entidades, CRUD e uma ação por tela (FrontPUSH)"
aliases: ["FrontPUSH dashboards aula 05", "DashClass aula 05", "05: Princípios pt.2", "princípios de dashboard parte 2"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [dashboard, levantamento-de-requisitos, requisitos-funcionais, requisitos-nao-funcionais, lgpd, crud, atores-do-sistema, rbac, entidade, atributos, modelagem-de-dados, relacionamentos, formularios, campos, filtros, hierarquia-visual, fluxos, botoes, primario-secundario, mood-board, wireframe]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-dashboards-principios-parte-2.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-24
---

# Princípios de dashboards, parte 2: levantamento de requisitos, atores, entidades, CRUD e uma ação por tela (FrontPUSH)

## TL;DR

Quinta aula (cerca de 17 min) do módulo de dashboards do [[wiki/entities/frontpush|FrontPUSH]], de novo no iPad. Antes de patterns e wireframes vem o **levantamento de requisitos**, assunto que "tanto designer como desenvolvedores precisam saber, principalmente o desenvolvedor". O quadro: levantamento de requisitos → atores do sistema, fluxos, banco de dados; mood board, reuniões, objetivos; patterns, wireframes.

- **Funcionais × não funcionais:** funcional é "uma função que o seu sistema precisa desempenhar" (vendas por região, fluxo de caixa, manter usuários). Não funcional é seguro, respeitar a [[wiki/concepts/lgpd|LGPD]], rápido, "rodar em espelhamento", que ele chama de "arredores [...] por exemplo, perfumaria" (ver Precisões) ([[wiki/concepts/requisitos-funcionais-e-nao-funcionais]]).
- **Atores, em hierarquia:** funcionário, gerente, administrador ou CEO, e o comprador, que "está fora dos atores [...] no quesito administrativo" mas é ator. "Todos são usuários", e o usuário precisa de um perfil para o "acesso hierárquico" ([[wiki/concepts/atores-do-sistema]]).
- **Manter = CRUD:** "manter ou gerenciar" uma entidade é poder criar, ler, atualizar e deletar. Usuários e vendas viram entidades; "o CRUD é meio que uma necessidade universal" ([[wiki/concepts/crud]]).
- **Atributo vira campo:** venda = id, id do usuário, id do funcionário, valor, parcelada ou não. "Os atributos, quando a gente traduz para a nossa interface, são os campos" dos formulários. Esquecer o CPF do comprador obriga a voltar no banco e nos campos ([[wiki/concepts/atributos-como-campos-de-formulario]], [[wiki/concepts/modelagem-de-dados]]).
- **Relacionamentos:** uma venda liga um comprador e um funcionário; isso define formulário, banco, ordem de cadastro e os filtros ("me passa todas as vendas [...] com o ID desse usuário") ([[wiki/concepts/chave-estrangeira]]).
- **Uma ação por tela:** "nunca coloque muitos botões": um primário preenchido e um secundário só com contorno. Fluxos com nome específico (recuperar senha por SMS, por e-mail). O custo: "vai ter muita tela" ([[wiki/concepts/fluxos-bem-definidos]], [[wiki/concepts/botoes-em-interfaces]]).

## Key Claims

### Por que requisitos

- A aula "vai linkar absolutamente tudo": "as principais etapas que a gente precisa passar para poder a gente construir bons dashboards [...] bons sistemas". O assunto já apareceu "nas primeiras aulas do blog" do curso.
- O termo é "um pouco mais comum quando a gente fala para desenvolvedores", mas "tanto designer como desenvolvedores precisam saber".

### Funcionais e não funcionais

- "Os funcionais, como o próprio nome já diz, são aqueles requisitos que literalmente desempenham alguma função." Exemplo: "eu quero que no meu dashboard eu tenha uma relação especial de quantas vendas foram feitas de acordo com a região, para eu saber qual região onde eu vou mais investir"; também "fazer o fluxo de caixa, fazer o fluxo de usuários, manter usuários" ([[wiki/concepts/requisitos-funcionais-e-nao-funcionais]]).
- "Os não funcionais são [...] os arredores que podem ou não ser importantes, podem ou não ser, por exemplo, perfumaria." Exemplos: "que ele seja seguro, [...] que ele respeite a lei geral de proteção de dados, [...] que ele seja rápido, [...] que ele rode em espelhamento"; "características que o cliente pode pedir" ([[wiki/concepts/lgpd]]).
- Do levantamento saem "os principais fluxos, os atores do sistema e o banco de dados".

### CRUD e atores

- "A gente remete muito ao CRUD [...] create, read, update e delete, ou seja, criar, ler, atualizar e deletar. Então, o sistema vai sempre precisar realizar esses quatro pilares aqui, em tudo que ele for fazer" ([[wiki/concepts/crud]]).
- "Atores do sistema, basicamente é, quem é que vai operar o sistema?" Funcionário, gerente; "acima do gerente tem alguém? Tem a parte do administrador? Ou então os CEOs, que eles têm outro acesso personalizado?" ([[wiki/concepts/atores-do-sistema]]).
- "Geralmente, você consegue estabelecer eles de forma hierárquica", o que já dá uma visão dos "rabiscos iniciais do sistema para poder definir fluxos".

### Entidades e "manter"

- "Uma vez que eu tenho os atores do sistema, todos são usuários." "Obrigatoriamente, em todo sistema eu tenho um usuário, porque senão eu não tenho como mexer no sistema."
- "Eu tenho que manter o usuário. O que significa esse manter? É que para o usuário eu tenho que ter um CRUD." "Isso a gente chama manter ou gerenciar."
- "Usuários [...] virou uma entidade [...] a gente está começando a modelar como é que vai ser o sistema." "Com certeza, vendas" é outra, também com CRUD ([[wiki/concepts/modelagem-de-dados]]).

### Atributos viram campos

- O banco "tem que estar alinhado com o CRUD". Atributos de venda: "um ID, porque cada venda tem um identificador", "um ID de usuário", "um ID de um funcionário, para saber quem foi que [...] operacionalizou essa venda", "o valor da venda", "se ela foi parcelada ou não".
- "Os atributos, quando a gente traduz para a nossa interface, são os campos. São campos que a gente vai colocar lá nos inputs, nos nossos formulários" ([[wiki/concepts/atributos-como-campos-de-formulario]], [[wiki/concepts/formulario-html]]).
- Atributos de usuário saem dos fluxos: perfil para o "acesso hierárquico"; e-mail para "mandar um código de verificação" na recuperação de senha. "Você já tem que pensar nos fluxos, nessa etapa inicial, em uma modelagem. Porque senão você vai ter que voltar no processo todas as vezes" ([[wiki/concepts/rbac]]).
- O comprador "é um usuário que está fora dos atores do sistema no quesito administrativo. Mas ele continua sendo um ator", porque é preciso o cadastro dele "para poder [...] emitir nota fiscal", com CPF, "para poder ajustar a receita".
- Sem esse levantamento, "a gente não sabe quais são os atributos de cada entidade". Exemplo: "fiz o usuário aqui sem CPF, só com o identificador", e aí é voltar e pôr o atributo "no banco de dados" e "na parte de campos".

### Relacionamentos

- "Um funcionário e um comprador estão vinculados a uma venda." Os relacionamentos definem "a estrutura do meu formulário", "a estrutura do meu banco de dados", "se eu tenho que cadastrar primeiro uma entidade para poder existir outra" ([[wiki/concepts/chave-estrangeira]]).
- E definem o "ler": "eu quero as vendas só desse usuário. Aí eu tenho que pegar o ID do usuário [...] e perguntar para a entidade de vendas, ei, me passa todas as vendas que você tem com o ID desse usuário aqui". "Eu preciso muito de filtros quando estou definindo dashboards."
- "Funcionário pode entrar, pode sair": o sistema precisa atualizar, criar e deletar registros sempre. "O CRUD é meio que uma necessidade universal quando você tem uma entidade."

### Depois dos requisitos, patterns e wireframes

- Tudo isso sai de perguntar "para o cliente como é o negócio dele, do que se trata, quais são os objetivos", junto com "mood boards, reuniões, objetivos" ([[wiki/concepts/briefing]], [[wiki/concepts/pesquisa-com-usuario]]).
- "Uma vez que você fez isso, aí sim você pode partir para os patterns e para os wireframes", já sabendo "as informações que teoricamente são necessárias e onde alocar" ([[wiki/concepts/patterns-de-dashboard]], [[wiki/concepts/wireframe]]).
- As próximas aulas fazem "um breve levantamento de requisitos" do [[wiki/entities/dash-class|DashClass]].

### Hierarquia e uma ação por tela

- Hierarquia, retomada: "aquilo que está maior, aquilo que está em uma forma diferente, [...] em um contraste maior, [...] no topo, [...] para a esquerda, eu enxergo primeiro" ([[wiki/concepts/hierarquia-visual]]).
- "Coloque uma ação em cada tela [...] Não coloque muitas ações em uma tela só." Na tela de vendas há informação, filtros e registros "com determinadas ações" (excluir, verificar a nota fiscal).
- "Nunca coloque muitos botões [...] Geralmente, a gente coloca dois botões. Um primário [...] preenchido, e outro secundário, só com o contorno do botão" ([[wiki/concepts/botoes-em-interfaces]]).
- Nomear fluxos específicos: recuperar senha por SMS, por e-mail, login "de forma ininterrupta", uma venda. "Quanto mais específico você for, mais específico você está sendo na ação e mais direcionado" ([[wiki/concepts/fluxos-bem-definidos]]).
- "Qual é a parte negativa disso? É que vai ter muita tela [...] vai ser fantástico para a experiência do usuário, mas vai dar muito trabalho."

## Precisões e ressalvas

1. **Requisito não funcional não é perfumaria.** Segurança, desempenho, disponibilidade e conformidade com a LGPD costumam definir a arquitetura e são os mais caros de mudar depois; a LGPD nem é opcional, é obrigação legal. A ressalva "podem ou não ser importantes" não muda o rótulo errado (alta). Ver [[wiki/concepts/requisitos-funcionais-e-nao-funcionais]].
2. **Nem toda entidade tem CRUD completo.** Venda raramente é deletada: é cancelada, por exigência fiscal e de auditoria (o slide de vendas da aula 03 já tinha NF-e "Cancelada"). Usuário também costuma ser desativado (*soft delete*). E há tensão real: a LGPD dá ao titular o direito à eliminação dos dados, enquanto a lei fiscal exige guardar documentos. "Necessidade universal" vale para a pergunta, não para a resposta (alta). Ver [[wiki/concepts/crud]].
3. **Ator é papel, não pessoa, e nem sempre é gente.** Na modelagem de casos de uso (UML), ator é um papel externo que interage com o sistema; sistemas externos também são atores (gateway de pagamento, emissor de nota fiscal). A hierarquia funcionário → gerente → admin vira papéis e permissões (alta). `[skill: ux-ui-mentor]` A referência `ux-enterprise-b2b.md` trata isso como [[wiki/concepts/rbac]]: papel = conjunto de permissões, menor privilégio por padrão, permissões aditivas, e na UI esconder o que o usuário nunca poderá fazer ou desabilitar com explicação.
4. **Atributo e campo não são 1:1.** Muitos atributos nunca viram campo (id, datas de auditoria, id do funcionário vindo da sessão), e alguns campos não viram atributo (confirmar senha). Também convém pedir só o que o fluxo precisa no momento: o CPF pode ser pedido no checkout, não no cadastro (inferência, alta). Ver [[wiki/concepts/atributos-como-campos-de-formulario]].
5. **Ordem diferente da aula 03.** Lá: "a gente sempre começa dos Grids, a gente sempre começa dos Patterns", e depois se levanta requisitos. Aqui: requisitos primeiro, "aí sim você pode partir para os patterns e para os wireframes". O quadro desta aula põe patterns e wireframes no fim. Na prática as duas convivem: patterns são repertório; requisitos decidem quais entram.
6. **"Uma ação por tela" × ações por linha.** O slide de vendas tem quatro ações em cada linha da tabela. Não é contradição: ações contextuais de linha são outro nível; a regra dos dois botões vale para as ações principais da tela (inferência, alta).
7. **"Relação especial" e "espelhamento".** Provavelmente "relação espacial", isto é, vendas por região (um mapa), e espelhamento como replicação ou alta disponibilidade. Ficaram literais no `raw/`.
8. **Nomes reconstruídos da legenda:** "Dash Class" → DashClass (2×), "Nárcio" → Násser. Ficaram literais: "eu já voltei o gerente", "eu venho os registros", "tanto para designers", "os funcionais e não os funcionais".

## Entities

- [[wiki/entities/nasser]]: instrutor; quadro no iPad (Procreate, paleta "FrontPUSH 2.0").
- [[wiki/entities/dash-class]]: levantamento de requisitos prometido para as próximas aulas.
- [[wiki/entities/frontpush]]: "as primeiras aulas do blog" como referência.

## Concepts

- [[wiki/concepts/atores-do-sistema]] (novo), [[wiki/concepts/atributos-como-campos-de-formulario]] (novo)
- [[wiki/concepts/requisitos-funcionais-e-nao-funcionais]], [[wiki/concepts/lgpd]]
- [[wiki/concepts/crud]], [[wiki/concepts/modelagem-de-dados]], [[wiki/concepts/chave-estrangeira]], [[wiki/concepts/rbac]]
- [[wiki/concepts/formulario-html]], [[wiki/concepts/briefing]], [[wiki/concepts/pesquisa-com-usuario]]
- [[wiki/concepts/hierarquia-visual]], [[wiki/concepts/fluxos-bem-definidos]], [[wiki/concepts/botoes-em-interfaces]]
- [[wiki/concepts/patterns-de-dashboard]], [[wiki/concepts/wireframe]], [[wiki/concepts/dashboard]]

## Open Questions

- Quais são as "primeiras aulas do blog" em que ele tratou de requisitos? Provavelmente o projeto de blog em React, ainda não ingerido.
- No DashClass, quais são os atores? Aluno, instrutor, administrador? Fica para o levantamento das próximas aulas.
- Como ele trata o "deletar" de vendas e usuários no DashClass: exclusão ou cancelamento?

## Raw Quotes

- "O CRUD é meio que uma necessidade universal quando você tem uma entidade."
- "Os atributos, quando a gente traduz para a nossa interface, são os campos."
- "Você já tem que pensar nos fluxos, nessa etapa inicial, em uma modelagem. Porque senão você vai ter que voltar no processo todas as vezes."
- "Coloque uma ação em cada tela."
- "Qual é a parte negativa disso? É que vai ter muita tela."
