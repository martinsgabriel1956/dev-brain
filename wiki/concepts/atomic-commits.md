---
type: concept
title: "Atomic Commits"
aliases: ["commit atômico", "commits pequenos", "PR pequeno", "unidade funcional de commit"]
date_created: 2026-04-22
date_updated: 2026-08-11
source_count: 4
tags: [git, commits, hábitos, craftsmanship, code-review, qualidade]
skill: tech-mentor-leadership
status: stable
---

# Atomic Commits

Prática de fazer **commits que representam uma única unidade funcional de mudança** — alteração de código + teste que a valida, juntos no mesmo commit.

## O problema do commit gigante

PR gigante = revisor não sabe onde começar = ninguém quer revisar = review superficial ou postergado indefinidamente.

```
❌ Commit diário/dump:
   - Fix things
   - More fixes
   - WIP
   - Finally working

✅ Commits atômicos:
   - feat: add email validation to user creation
   - test: cover invalid email case in createUser
   - fix: prevent duplicate user on race condition
```

## O padrão anti-atômico mais comum

Fazer um commit que **quebra** um teste e, no commit seguinte, fazer o commit que **corrige** o teste. Isso cria dois commits que não fazem sentido individualmente.

```
❌ commit A: change user validation logic    ← quebra teste
   commit B: fix test for validation         ← conserta

✅ commit A: refactor user validation + update tests
```

## Regra prática

> Cada commit deve deixar o repositório num estado funcional e compreensível.

Se alguém fizer `git bisect` e cair no seu commit, o código deve fazer sentido e os testes devem passar.

## Benefícios

- **Revisão mais fácil**: contexto claro em cada mudança
- **Rollback cirúrgico**: reverter uma feature sem afetar outra
- **Histórico legível**: `git log` vira documentação
- **`git bisect` funciona**: cada commit é um estado válido

## Tamanho de PR

Não existe número mágico de linhas, mas o princípio é: **um PR deve ser revisável em uma sessão de foco**. Se você não consegue revisar em 20-30 minutos, está grande demais.

## Rebase interativo como ferramenta prática

[[wiki/concepts/rebase-vs-merge]] documenta o comando que efetivamente produz commits atômicos a partir de um histórico bagunçado: `git rebase -i` com `squash`/`fixup`/`reword` local, antes de abrir o PR — sem afetar branches compartilhadas, já que ainda é reescrita de histórico local.

## Um-arquivo-um-commit como facilitador de rebase

[[wiki/sources/git-flow-farsa-solucao-maturidade-rebase-lucas-montano]] usa uma variante disciplinada de commits atômicos como base de um fluxo de integração por [[wiki/concepts/rebase-vs-merge|rebase]]: em edições, **um arquivo por commit** (múltiplos arquivos só em criação de projeto/pasta). O benefício prático é sobre conflito: como o [[wiki/concepts/rebase-vs-merge|rebase]] resolve conflitos commit a commit, granularizar por arquivo faz cada conflito cair num único arquivo, resolvido intencionalmente — o que, na experiência da fonte (4 anos), eliminou as regressões de "consertei e voltou a quebrar". É o mesmo princípio ("cada commit é um estado compreensível") aplicado a tornar o rebase gerenciável em um [[wiki/concepts/trunk-based-development|fluxo só-main]].

## Ver também

- [[definicao-de-pronto]] — commit atômico é parte da definição de pronto
- [[testar-proprio-codigo]] — teste vai junto no mesmo commit
- [[wiki/concepts/rebase-vs-merge]] — mecânica de rebase e squash usada para chegar a commits atômicos

## Key Sources

- [[wiki/sources/habitos-ruins-de-programador]]
- [[wiki/sources/4-habitos-programador-ineficiente]]
- [[wiki/sources/git-rebase-na-pratica]] — demonstração prática de rebase e histórico linear
- [[wiki/sources/git-flow-farsa-solucao-maturidade-rebase-lucas-montano]] — um-arquivo-um-commit como facilitador de conflitos de rebase num fluxo só-main
