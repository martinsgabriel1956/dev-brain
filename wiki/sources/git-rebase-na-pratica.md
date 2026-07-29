---
type: source
title: "Git Rebase na Prática"
aliases: ["git rebase tutorial", "rebase na prática", "como usar git rebase"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 0
tags: [git, rebase, merge, versionamento, branching, historico-git, conflito-de-merge]
skill: tech-mentor-leadership
status: stable
source_file: "raw/git-rebase-na-pratica.md"
source_url: ""
author: "não identificado (canal patrocinado pela Alura, não há nome de autor na transcrição)"
date_published: ""
date_ingested: "2026-07-29"
---

## TL;DR

Tutorial prático de `git rebase`: por que existe (a `main` avança enquanto uma branch de feature é desenvolvida, e um merge direto criaria um commit "que não serve para nada"), o que ele faz de fato (reposiciona a *base* da branch de feature para a ponta atual da branch de origem, reescrevendo os SHAs dos commits) e como resolver o conflito que aparece nesse processo. Demonstração completa via terminal + VS Code: cria-se a branch `feature` a partir de dois commits da `main`, a `main` recebe um commit concorrente que altera o mesmo arquivo, e `git rebase main` (rodado a partir da `feature`) gera um conflito resolvido manualmente antes de `git rebase --continue`. Fecha com a regra central do vídeo: rebase é ferramenta de **repositório local** — nunca deve reescrever histórico de branch pública/compartilhada, onde a prática correta é pull request + merge.

---

## Reivindicações Principais

**Claim:** Quando uma branch de feature fica aberta enquanto a `main` recebe outros commits, um `git merge` direto da feature de volta pra `main` tende a gerar um commit de merge "que não serve para nada"; a alternativa é trazer a feature para cima do estado atual da `main` antes de integrar.
**Evidência:** Diagrama desenhado no início do vídeo (extensão de desenho do VS Code) mostrando `main` com `commit 1` → `commit 2`, branch `feature` criada do `commit 2` com dois commits próprios, e a `main` avançando em paralelo com um `commit 3`.
**Confiança:** Alta — é a motivação didática padrão para introduzir rebase, consistente com a definição em [[wiki/concepts/rebase-vs-merge]].

**Claim:** `git rebase <branch-alvo>` reposiciona os commits exclusivos da branch atual para a ponta de `<branch-alvo>`, criando novos commits com novos SHAs (não reaproveita os commits antigos).
**Evidência:** Demonstração ao vivo — `git checkout feature && git rebase main` — seguida de inspeção do histórico (extensão Git History do VS Code) mostrando o `commit 3` da `main` inserido na linha do tempo da `feature`, com os commits da feature reordenados por cima.
**Confiança:** Alta — comportamento documentado e esperado do `git rebase`; confirma o mecanismo já registrado em [[wiki/concepts/rebase-vs-merge]] (seção "Rebase: reescreve commits da branch sobre a base atual").

**Claim:** Rebase gera conflito quando o mesmo arquivo foi alterado tanto na branch de origem quanto na branch alvo — nesse caso, precisa ser resolvido manualmente antes de continuar.
**Evidência:** Demonstração ao vivo: `commit 3` na `main` e os commits da `feature` alteram a mesma linha do mesmo arquivo; `git rebase main` para com conflito, resolvido no editor de merge do VS Code (comparação lado a lado + aceitar as duas mudanças) e finalizado com `git add .` + `git rebase --continue`.
**Confiança:** Alta — reproduzido passo a passo, incluindo o uso do editor de conflitos nativo do VS Code.

**Claim:** Depois do rebase bem-sucedido, a branch de feature fica pronta para ser integrada na `main` sem gerar merge divergente, porque o último commit em comum entre as duas branches passa a bater.
**Evidência:** Sequência final do vídeo: `git checkout main && git rebase feature` trazendo o histórico completo (commit 3 + commits da feature) para a `main`.
**Confiança:** Alta — consequência lógica direta de como o rebase reposiciona o ponteiro de branch; o autor observa que alternativamente poderia ter feito um merge normal depois do primeiro rebase, com o mesmo resultado.

**Claim:** Rebase reescreve o histórico do Git (SHAs mudam) e por isso só deve ser usado em repositórios **locais** — nunca em branches públicas/remotas compartilhadas, onde a prática correta é pull request seguido de merge.
**Evidência:** Afirmação explícita e repetida ao longo do vídeo (introdução e conclusão), sem contra-exemplo demonstrado ao vivo de uso em repositório remoto.
**Confiança:** Alta — é a regra de ouro documentada de forma idêntica em [[wiki/concepts/rebase-vs-merge]] ("nunca rebase em branches públicas/compartilhadas"), citada aqui de forma independente por outra fonte.

---

## Comandos Demonstrados

```bash
git init
git add .
git commit -m "commit 1"
git commit -m "commit 2"

git checkout -b feature      # cria a branch de feature a partir do commit 2
git commit -m "feature: primeira alteração"
git commit -m "feature: segunda alteração"

git checkout main
git commit -m "commit 3"     # commit concorrente no mesmo arquivo

git checkout feature
git rebase main              # gera conflito
# resolução manual do conflito
git add .
git rebase --continue

git checkout main
git rebase feature           # traz a feature já realinhada para a main
```

---

## Entidades e Conceitos

- [[wiki/concepts/rebase-vs-merge]] — atualizado, conceito central desta fonte (já existia via `references/git-advanced.md` da skill `tech-mentor-leadership`; esta fonte adiciona uma demonstração prática ponta a ponta com resolução de conflito)
- [[wiki/concepts/atomic-commits]] — histórico linear pós-rebase é pré-condição para commits/PRs legíveis
- [[wiki/concepts/code-review]] — regra prática "rebase local antes de abrir PR, merge para integrar" citada na skill de liderança técnica

---

## Perguntas Abertas

- A fonte não demonstra `git rebase -i` (interactive rebase/squash) nem cita explicitamente esse comando, embora prometa um vídeo futuro sobre squash — [[wiki/concepts/rebase-vs-merge]] já documenta `git rebase -i` via skill, então não há gap de conteúdo, só gap de demonstração nesta fonte específica.
- Não fica claro quem é o autor/canal do vídeo (a transcrição não se identifica, apenas menciona o patrocínio da Alura) — diferente de outras fontes de Git na wiki, não foi possível criar ou vincular uma entidade de autor.

---

## Citações

> "Usar o Git para versionamento é tão importante quanto para um cozinheiro saber acender um fogão."

> "[Rebase] é um comando super poderoso, mas também super perigoso — por isso mesmo é importante entender e usar de forma correta, porque se cair em mãos erradas pode literalmente estragar... o versionamento do projeto."

> "Essa é uma estratégia utilizada, repito, em repositórios locais — não se deve utilizar em repositório público."
