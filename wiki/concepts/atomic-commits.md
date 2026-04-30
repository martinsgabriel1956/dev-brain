---
type: concept
title: "Atomic Commits"
aliases: ["commit atômico", "commits pequenos", "PR pequeno", "unidade funcional de commit"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 2
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

## Ver também

- [[definicao-de-pronto]] — commit atômico é parte da definição de pronto
- [[testar-proprio-codigo]] — teste vai junto no mesmo commit

## Key Sources

- [[wiki/sources/habitos-ruins-de-programador]]
- [[wiki/sources/4-habitos-programador-ineficiente]]
