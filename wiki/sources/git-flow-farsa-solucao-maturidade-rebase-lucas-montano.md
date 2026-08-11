---
type: source
title: "Git Flow é uma Farsa? A Solução, Maturidade e o Processo com Rebase (Lucas Montano)"
aliases: ["git flow é uma farsa", "solução git flow lucas montano", "processo com rebase lucas montano", "maturidade git"]
date_created: 2026-08-11
date_updated: 2026-08-11
source_count: 0
tags: [tech-mentor-leadership, git-flow, rebase-vs-merge, trunk-based-development, ci-cd, maturidade-tecnica, cargo-cult, processo, times-pequenos, lucas-montano]
skill: tech-mentor-leadership
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/git-flow-farsa-solucao-maturidade-rebase-lucas-montano.md
source_url:
author: Lucas Montano
date_published:
date_ingested: 2026-08-11
---

# Git Flow é uma Farsa? A Solução, Maturidade e o Processo com Rebase (Lucas Montano)

## TL;DR

Continuação do vídeo anterior de [[wiki/entities/lucas-montano]] ("Git Flow é uma farsa"), agora entregando a "solução" prometida — e a tese de que **não existe solução universal**. O núcleo do vídeo é sobre [[wiki/concepts/maturidade-tecnica|maturidade]]: Git não é só ferramenta, é parte do processo e da natureza de cada empresa; o profissional maduro busca **princípios**, não uma receita para encaixar em toda empresa, e **se adapta ao processo da empresa** em vez de impor um "método master". Montano enquadra o hype em torno do Git Flow como [[wiki/concepts/cargo-cult-tecnologico|cargo cult]] — solução elevada a "padrão industrial" por influenciadores ("modificadores de cultura") sem que a indústria de fato a use, mesmo padrão de squads-do-Spotify, ágil e OO. A solução dele (que funcionou por 4 anos, **só em times pequenos**, e admitidamente **não escala**) é um fluxo próximo de [[wiki/concepts/trunk-based-development|trunk-based]]: (1) CI como *single command deploy* frictionless; (2) um **dono** por entrega; (3) **só a `main`** como fonte de verdade (sem branch `dev` de vida longa); (4) integração via **[[wiki/concepts/rebase-vs-merge|rebase]]**, não merge, para evitar o "subway train from hell" e obter *fast-forward merges* limpos. O rebase exige disciplina (rebase recorrente 1–2×/semana, um-arquivo-um-commit) e ownership centralizado — o que o torna inviável para times grandes.

## Key Claims

1. **Git Flow é uma farsa / falácia da bolha dev** — "me diga uma grande empresa que está usando Git Flow". Foi "elevado à estátua de padrão industrial pelos influenciadores sem que de fato a indústria usasse isso". Instância explícita de [[wiki/concepts/cargo-cult-tecnologico]].
2. **Influenciadores são "modificadores de cultura"** — pegam um post/uma palestra e a comunidade Tech abraça a ideia "como se fosse um gospel". Aconteceu com o movimento ágil, orientação a objetos e squads. Mesma tese do vídeo de Clean Code (referência interna do autor).
3. **O caso dos squads do Spotify** — a ideia nasceu de um post/palestra do Spotify, foi reproduzida à exaustão, e o próprio time original veio a público dizer que o Spotify **não** usava daquela maneira. Não significa que squads não funcionem — o ponto é que "é muito mais fácil comunicar um argumento sensacionalista do que comunicar maturidade". Reforça o exemplo já registrado em [[wiki/concepts/cargo-cult-tecnologico]].
4. **Por que demorou a responder: comunicar maturidade é mais difícil que comunicar sensacionalismo** — não existe resposta "a + b"; a demora foi porque a resposta honesta é "depende", que vende mal.
5. **Não existe processo sem trade-off; nenhum processo está "quebrado"** — em 3 empresas por que passou desde que fechou a própria (~2023), nenhuma usava Git da mesma forma e nenhuma tinha o processo quebrado; existiam prós e contras, mas funcionava. "Cada empresa compra um processo com prós e contras que fazem sentido para ela." Ver [[wiki/concepts/maturidade-tecnica]].
6. **Git é parte do processo e da natureza da empresa, não só uma ferramenta** — inclusive numa empresa grande atual, o processo de levar tarefa a produção é "a coisa mais maluca que já vi", trabalhoso, mas funciona (e estão evoluindo para algo mais automático). O que importa é o processo **funcionar**.
7. **A solução dele mira times pequenos, onde burocracia é o problema** — e mesmo assim tem prós e contras. Sustenta que Git Flow tem "muito mais contras que prós" para empresa pequena.
8. **Passo 1 — CI como *single command deploy* frictionless** — em time pequeno, CI não precisa ser GitHub/GitLab Actions; pode ser a máquina do dev, desde que a entrega seja **um comando**. Objetivo: eliminar o estado "código pronto mas não em produção". Ver [[wiki/concepts/ci-cd]]. Usa um ambiente de **staging** idêntico ao de produção (só muda URL e capacidade) como ambiente produtivo de teste.
9. **Passo 2 — um dono por entrega (ownership)** — cada entrega tem um dev responsável (tipicamente pleno) que a leva a produção e orquestra dependências. Necessário porque o rebase resolve conflitos **commit a commit** — oneroso, exige atenção centralizada. Conecta com [[wiki/concepts/bus-factor]] (é justamente a centralização que não escala).
10. **Passo 3 — só a `main` como fonte de verdade** — sem branch `dev`/`main` de vida longa. Toda feature concluída vai para a `main` (pode ir a produção ou ficar em staging). Evita o trabalho extra de manter conflitos entre uma `dev` atrasada e uma `prod` que recebe hotfix. É a essência do [[wiki/concepts/trunk-based-development]].
11. **Passo 4 — rebase, não merge, para integrar** — merge gera o "*subway train from hell*" (linhas de branching ilegíveis); rebase deixa a ordem das entregas clara (importante para prestar contas a cliente na consultoria) e produz **fast-forward merges** — "bloquinhos de merge bem definidos".
12. **Disciplina de rebase recorrente evita a regressão "consertei e voltou a quebrar"** — rebase 1–2×/semana (não só na hora do merge) mantém conflitos pequenos; com **um-arquivo-um-commit**, cada conflito é num único arquivo e resolvido intencionalmente. Em 4 anos (2020–2024) isso eliminou aquelas regressões clássicas. Ver [[wiki/concepts/atomic-commits]] e [[wiki/concepts/rebase-vs-merge]].
13. **Mudou de ideia: o rebase-flow NÃO escala** — o "BO" do rebase é que ele **reescreve a branch da feature**; se der ruim, perde-se a versão original — responsabilidade alta. Só funciona onde a atenção pode ser centralizada em uma pessoa; em time grande, centralizar o merge "vira uma loucura". Antes ele achava que era o processo que revolucionaria a indústria; hoje o defende **apenas para times pequenos** (e nota que IA reduz muito o custo do rebase hoje).
14. **Maturidade = adaptar-se ao processo da empresa, não impor o seu** — "não ache que você vai chegar numa empresa com processo funcionando e um super método master, e a empresa vai adotar o que você trouxe; é você que se adapta". Quanto mais sênior a pessoa, mais concorda que não existe resposta final. Ver [[wiki/concepts/maturidade-tecnica]].

## Entidades Mencionadas

- [[wiki/entities/lucas-montano]] — autor; ensina Golang no canal, fechou a própria empresa ~2023, usou o rebase-flow por 4 anos na consultoria. (Na transcrição auto-gerada se identifica como "Lucas Badico TV" — provável garble; atribuição a Lucas Montano pelo conjunto de sinais.)
- Spotify — citado como origem do hype de squads que o próprio time depois desmentiu (exemplo de cargo cult).

## Conceitos Tocados

- [[wiki/concepts/git-flow]]
- [[wiki/concepts/trunk-based-development]]
- [[wiki/concepts/rebase-vs-merge]]
- [[wiki/concepts/ci-cd]]
- [[wiki/concepts/maturidade-tecnica]]
- [[wiki/concepts/cargo-cult-tecnologico]]
- [[wiki/concepts/atomic-commits]]
- [[wiki/concepts/bus-factor]]

## Open Questions

- **Autoria/nome:** a transcrição auto-gerada registra "Lucas Badico TV". Atribuído a [[wiki/entities/lucas-montano]] por forte convergência de sinais (o vídeo anterior "Git Flow é uma farsa", ensino de Golang, membership do canal, ter fechado a empresa ~3 anos antes) — mas o nome literal difere; tratar a atribuição como provável, não confirmada nominalmente.
- **Contradição parcial com [[wiki/concepts/ci-cd]]:** a página de CI/CD documenta o fluxo didático `feature → dev/staging → main` (de [[wiki/sources/continuous-integration-delivery-deploy-vs-release]]); esta fonte argumenta **contra** manter uma branch `dev` de vida longa, defendendo só a `main`. Não é erro de nenhuma das duas — são escolhas com trade-offs diferentes (o staging aqui é um *ambiente*, não uma *branch* de vida longa).
- O vídeo não cita link do post original de squads do Spotify nem do desmentido do time original — tratar como relato do autor, não verificado contra fonte primária.
- "Copa acabou" e a cadência de "4 em 4 anos" datam o vídeo de forma vaga (contexto de Copa do Mundo); sem data de publicação na transcrição.

## Raw Quotes

> "Me diga uma grande empresa que está usando Git Flow."

> "Para mim, Git Flow é uma das maiores falácias que a gente tem na nossa bolha dev."

> "É muito mais fácil comunicar uma verdade sensacionalista do que comunicar maturidade."

> "Em nenhuma empresa eles usavam Git da mesma maneira, e em nenhuma empresa o processo estava quebrado."

> "Git é muito mais do que só uma ferramenta. Git é parte do processo e da natureza da empresa."

> "A entrega tem que ser em um comando. [...] tem que ser um negócio frictionless."

> "No meu sistema só existe main. Não existe outra branch de vida longa."

> "Quando a gente usa merge, começa a criar o que eu chamo de subway train from hell."

> "O 'BO' do rebase é que ele modifica a branch da feature de forma que, se der ruim, você quase perdeu o projeto original."

> "É você que tem que se adaptar ao método da empresa, ao processo da empresa."

> "Não existe uma resposta final, uma resposta matadora. E quanto mais sênior a pessoa, mais ela vai concordar comigo."
