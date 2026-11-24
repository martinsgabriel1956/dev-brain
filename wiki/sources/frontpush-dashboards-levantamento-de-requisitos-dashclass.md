---
type: source
title: "Levantamento de requisitos do DashClass: atores, entidades e gamificação (FrontPUSH)"
aliases: ["FrontPUSH dashboards aula 06", "DashClass aula 06", "06: Levantamento de Requisitos", "levantamento de requisitos do DashClass"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [dashboard, levantamento-de-requisitos, atores-do-sistema, entidades, atributos, crud, modelagem-de-dados, relacionamentos, chave-estrangeira, muitos-para-muitos, cpf, lgpd, minimizacao-de-dados, nota-fiscal, pagamento, gamificacao, notificacoes, plataforma-de-ensino, reuniao-com-cliente]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-dashboards-levantamento-de-requisitos-dashclass.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-24
---

# Levantamento de requisitos do DashClass: atores, entidades e gamificação (FrontPUSH)

## TL;DR

Sexta aula (cerca de 13 min) do módulo de dashboards do [[wiki/entities/frontpush|FrontPUSH]]. [[wiki/entities/nasser|Násser]] aplica no iPad o método das aulas 04 e 05 ao [[wiki/entities/dash-class|DashClass]], num levantamento "bem simplificado", "com poucos atores de propósito", porque "cada ator que tem no sistema aumenta drasticamente a quantidade de telas" e de relacionamentos.

- **Três atores, dois fluxos:** aluno (assiste aulas, interage, dá feedback, compra), funcionário e administrador, os dois com acesso "mais administrativo" e "restrito a determinadas telas". Saem dois fluxos: aluno e administrativo ([[wiki/concepts/atores-do-sistema]]).
- **Três entidades:** user (id, perfil, e-mail, data de aniversário, nome e sobrenome, CPF), venda (id, forma de pagamento, id do funcionário, id do comprador, parcelado ou à vista, quitado, prazo, NF-e, data, itens) e produtos, que são os cursos (id, id do comprador, data, situação, nome, capa, instrutores, módulos, aulas). "E aqui eu estou chutando" ([[wiki/concepts/modelagem-de-dados]]).
- **Entidade = CRUD = telas:** do user saem "telas de cadastro", "para listar e pesquisar", "para poder atualizar" e "para deletar". "Você já sabe quais são as telas que vão sair daqui" ([[wiki/concepts/crud]]).
- **Gamificação como "não funcional":** no [[wiki/entities/como-se-virar|Como se virar (CSV)]] era o que "mais bateram na tecla": progresso, o que falta, recompensas, medalha aos 70%, próxima fase aos 80% com questionário. Isso exige "uma estrutura de informação muito grande": notificações e uma hierarquia clara de cursos, módulos e aulas. "O usuário só sabe que ele quer [...] gamificação, mas como que vai fazer isso? Aí já é papel seu, do designer" ([[wiki/concepts/gamificacao]]).
- **A reunião:** perguntar "como é que vocês pensam de fazer isso? Qual a estrutura que vocês já têm? [...] Qual é a experiência de vocês?", "uma conversa franca com o dono do negócio", avaliar na hora "é possível, não é possível? Dou conta, não dou conta?", anotar, desenhar e voltar numa segunda reunião com as dúvidas ([[wiki/concepts/levantamento-de-requisitos]]).

## Key Claims

### Simplificado de propósito

- "É um levantamento de requisitos bem simplificado [...] tem poucos atores de propósito porque dá muito trabalho para poder a gente executar cada fluxo."
- "Cada ator que tem no sistema aumenta drasticamente a quantidade de telas, a quantidade de relacionamentos entre as entidades." É "um demonstrativo [...] para poder você pegar a essência".

### Atores e fluxos

- "O DashClass [...] é uma plataforma de ensino [...] eu tenho três principais atores": aluno, funcionário, administradores ([[wiki/concepts/atores-do-sistema]]).
- Alunos "vão com certeza assistir as aulas", "vão interagir, eles vão dar os feedbacks e vão ser os compradores". "Automaticamente se ele é um comprador, [...] vai ter venda."
- Funcionário e administrador: "a caráter mais administrativo". "Eu vou ter um fluxo que é de alunos e eu vou ter outro fluxo que é do administrativo", e "o administrativo vai ter acesso restrito a determinadas telas" ([[wiki/concepts/rbac]]).

### Entidade user

- "Pelos atores aqui, eu já tenho uma entidade chamada usuário [...] Eu vou chamar aqui de user." "Eu já estou fazendo aqui uma abstração" ([[wiki/concepts/modelagem-de-dados]]).
- Atributos, "e aqui eu estou chutando": identificador; perfil, "porque ele pode ser administrador ou um usuário normal"; e-mail, para "mandar um novo código de acesso"; data de aniversário ("talvez, não sei", para o sistema dar parabéns); nome, sobrenome; CPF, para a nota fiscal, "que também é uma chave identificadora" ([[wiki/concepts/atributos-como-campos-de-formulario]]).
- "Se ele virou uma entidade, eu preciso fazer o famigerado CRUD": telas de cadastro, listar e pesquisar, atualizar, deletar. "Ponto" ([[wiki/concepts/crud]]).

### Entidade venda

- "Venda também é uma entidade": id; "a natureza da venda", cartão de crédito, boleto, PIX.
- "Quem realizou essa venda": id do funcionário, "uma chave que ele vai vir do usuário"; id do comprador, "que também vai vir de usuário". "Então, eu tenho um relacionamento entre vendas e usuário" ([[wiki/concepts/chave-estrangeira]]).
- Parcelado ou à vista, "está quitado?", "já passou o prazo?", "já emitiu nota fiscal?" (NF-e), data, e "os itens. O que foi comprado".

### Entidade produtos (cursos)

- "O que é o nosso produto? São as aulas, né? São os cursos. Então, os produtos são os cursos. Então, eu acabei de descobrir outra entidade." "Os produtos vão se relacionar com vendas."
- Atributos: id ("toda entidade tem o seu ID"), "quem foi que ele comprou" (id do comprador), data da compra, situação de pagamento, nome do curso, capa, instrutores, quantidade de módulos e de aulas ([[wiki/concepts/relacionamento-muitos-para-muitos]], ver Precisões).
- "Três principais entidades dentro do nosso sistema. Usuário, venda e produtos, cursos."

### Gamificação, notificações e estrutura de aulas

- Próximo passo: perguntar os requisitos funcionais e não funcionais. "Isso aqui são muitos requisitos funcionais. Mas, quais são os não funcionais, talvez? [...] Por exemplo, eu quero que tenha alguma estrutura de gamificação" ([[wiki/concepts/requisitos-funcionais-e-nao-funcionais]]).
- No projeto do CSV, a gamificação "foi justamente uma das coisas que [...] mais bateram na tecla": "sempre mostrar o progresso que ele está, sempre mostrar o que está faltando, sempre dar algum tipo de recompensa", para "terminar aquele curso que ele comprou" e "se engajar mais" ([[wiki/concepts/gamificacao]], [[wiki/entities/como-se-virar]]).
- "Se você está querendo fazer uma estrutura de gamificação, eu preciso de uma estrutura de informação muito grande", porque "é um sistema novo [...] ele não conhece". "O sistema de notificação e informações [...] precisa ser bem trabalhado. Uma coisa leva a outra."
- "O usuário, ele só sabe que ele quer uma estrutura de gamificação, mas como que vai fazer isso? Aí já é papel seu, do designer."
- Estrutura de aulas: materiais de apoio; "cursos, de aulas, de módulos bem definidos, bem hierarquizados, para poder eu mostrar o progresso". Exemplos: "você já [...] fez 70%, para poder ganhar uma nova medalha", "complete 80% desse curso, para poder você passar para a próxima fase, tem um pequeno questionário" ([[wiki/concepts/goal-gradient-effect]]).

### A conversa com o cliente

- "Você vai abstraindo conforme a gente vai conversando [...] imaginando, abstraindo e anotando. Então, é literalmente esse processo aqui, que eu faço quando eu tenho algum tipo de reunião" ([[wiki/concepts/levantamento-de-requisitos]]).
- Perguntas: "como é que faz isso? Como é que faz aquilo? Como é que vocês pensam de fazer isso? Qual a estrutura que vocês já têm? Qual é a experiência de vocês com relação a isso? O que vocês acham que melhor encaixou no modelo de negócio de vocês?" "É uma conversa franca com o dono do negócio" ([[wiki/concepts/briefing]]).
- "Conforme ele for falando as funções [...] eu já tenho que ter a expertise de falar, é possível, não é possível? Dou conta, não dou conta?"
- Depois do desenho, "vai aparecer algumas dúvidas", e "em uma segunda oportunidade, você pode chegar na pessoa e conseguir tirar suas dúvidas" ([[wiki/concepts/workflow-de-reunioes-do-freela]]).
- Próxima aula: traduzir tudo em wireframes e fluxos.

## Precisões e ressalvas

1. **Gamificação é requisito funcional.** Medalhas, progresso, questionários e notificações são comportamentos do sistema; não funcional é atributo de qualidade (segurança, desempenho, disponibilidade, conformidade). A confusão vem da aula 05, que chamou não funcional de "características que o cliente pode pedir" (alta). Ver [[wiki/concepts/requisitos-funcionais-e-nao-funcionais]].
2. **Produto não tem "id do comprador".** Um curso é vendido a muitos alunos e uma venda pode ter vários cursos: é relação muitos-para-muitos, resolvida por uma tabela de itens da venda (venda_id, curso_id, preço). A data e a situação de pagamento são da venda, não do curso. E o acesso do aluno ao curso (e o progresso dele) pede uma entidade de matrícula (inferência, alta). Ver [[wiki/concepts/relacionamento-muitos-para-muitos]].
3. **Faltam entidades que a própria aula pede.** Módulo, aula, material de apoio, progresso por aula, conquista ou medalha, questionário, notificação, ticket de dúvida: todos aparecem nas aulas 02 e 06 e nenhum entra no modelo de "três entidades". Ele avisa que é simplificado, mas a gamificação depende justamente dessas (alta).
4. **CPF não deve ser a chave.** O CPF é chave candidata, mas a chave primária deve ser o id interno; CPF muda de status, pode faltar (comprador estrangeiro) e é dado pessoal. Ver [[wiki/concepts/chave-primaria]] (alta).
5. **Minimização de dados.** "Data de aniversário? Talvez, não sei" é o caso que a [[wiki/concepts/lgpd]] trata no princípio da necessidade (art. 6º, III): coletar só o mínimo para a finalidade. "Dar parabéns" é finalidade fraca para guardar data de nascimento; o CPF se justifica pela nota fiscal, mas pode ser pedido só na compra (alta).
6. **Perfil com dois valores não cobre três atores.** "Administrador ou um usuário normal" deixa o funcionário de fora; o perfil precisa de pelo menos aluno, funcionário e administrador, e o "acesso restrito a determinadas telas" é [[wiki/concepts/rbac]] (alta).
7. **Id do funcionário numa venda online.** Numa plataforma de cursos, quase toda venda é autosserviço no checkout, sem funcionário; o campo faz sentido só para vendas manuais ou para o vendedor que fechou um contrato. Pagamento (tentativas, boleto vencido, PIX expirado, estorno) costuma virar entidade própria, separada da venda (inferência, média-alta).
8. **Perguntas de reunião.** `[skill: ux-ui-mentor]` A referência `pesquisa.md` recomenda perguntas abertas sobre comportamento real ("me conta como você acompanha o progresso dos seus alunos hoje") em vez de "você gostaria de uma feature de...". As perguntas de Násser são abertas, mas várias pedem opinião sobre solução ("o que vocês acham que melhor encaixou"); vale somar perguntas sobre o que eles fazem hoje.
9. **Nomes reconstruídos da legenda:** "Dash Class" → DashClass (3×), "NFE" → NF-e. Ficaram literais: "compradores de conteúdo" (talvez "consumidores"), "quem comprou a venda", "a caráter mais administrativo".

## Entities

- [[wiki/entities/nasser]]: instrutor; quadro no iPad.
- [[wiki/entities/dash-class]]: o sistema modelado.
- [[wiki/entities/como-se-virar]]: origem da exigência de gamificação.
- [[wiki/entities/frontpush]]

## Concepts

- [[wiki/concepts/levantamento-de-requisitos]] (novo)
- [[wiki/concepts/atores-do-sistema]], [[wiki/concepts/rbac]]
- [[wiki/concepts/modelagem-de-dados]], [[wiki/concepts/crud]], [[wiki/concepts/atributos-como-campos-de-formulario]]
- [[wiki/concepts/chave-primaria]], [[wiki/concepts/chave-estrangeira]], [[wiki/concepts/relacionamento-muitos-para-muitos]]
- [[wiki/concepts/lgpd]], [[wiki/concepts/requisitos-funcionais-e-nao-funcionais]]
- [[wiki/concepts/gamificacao]], [[wiki/concepts/goal-gradient-effect]]
- [[wiki/concepts/briefing]], [[wiki/concepts/workflow-de-reunioes-do-freela]]

## Open Questions

- O DashClass vai ter de fato as entidades de módulo, aula, progresso e conquista? As telas da aula 02 (meu progresso, minhas conquistas, tickets) pressupõem que sim.
- Instrutor é ator? Aparece como atributo de curso e como "principais instrutores" na home, mas não entre os três atores.
- A próxima aula desenha os fluxos: os dois (aluno e administrativo) viram quantas telas?

## Raw Quotes

- "Cada ator que tem no sistema aumenta drasticamente a quantidade de telas."
- "E aqui eu estou chutando, tá bom, pessoal?"
- "Você já sabe quais são as telas que vão sair daqui."
- "O usuário, ele só sabe que ele quer uma estrutura de gamificação, mas como que vai fazer isso? Aí já é papel seu, do designer."
- "É uma conversa franca com o dono do negócio, para poder entender o negócio dele."
