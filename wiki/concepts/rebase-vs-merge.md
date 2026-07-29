---
type: concept
title: "Rebase vs. Merge"
aliases: ["git rebase", "rebase de branch", "histórico linear git", "reescrita de histórico"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 1
tags: [git, rebase, merge, versionamento, branching, historico-git, conflito-de-merge]
skill: tech-mentor-leadership
status: draft
---

# Rebase vs. Merge

Duas formas distintas de integrar o histórico de uma branch de volta em outra — mesmo objetivo final (trazer as mudanças de uma branch para outra), consequências opostas sobre o histórico do Git.

## Merge

```
A---B---C  main
     \
      D---E  feature
# resultado: A---B---C---M  (M = merge commit, tem dois pais)
```

Preserva o histórico real — cada commit continua existindo com o SHA original, e um commit de merge (com dois pais) marca o ponto de integração. Auditável e seguro em branches compartilhadas: nada é reescrito, então quem já puxou a branch não perde referência.

## Rebase

```
A---B---C  main
             \
              D'--E'  feature (commits reescritos, novos SHAs)
```

Pega os commits exclusivos da branch atual e os "reaplica" em cima da ponta atual da branch de destino, um a um. Resultado: histórico linear, mais fácil de ler com `git log`, e mais efetivo para `git bisect`/`git blame` (não há bifurcação para navegar). O custo: os commits reescritos ganham **SHAs novos** — para o Git, são commits diferentes dos originais, mesmo com o mesmo conteúdo.

## Por que rebase é perigoso em branches compartilhadas

Como o rebase troca os SHAs, qualquer pessoa que já tenha puxado (`pull`) a versão antiga da branch fica com um histórico divergente do que foi reescrito remotamente — o próximo `pull` gera conflitos ou duplicação de commits. **Regra de ouro: nunca rebase em branches públicas/compartilhadas.** Rebase é ferramenta de repositório local (ou, no máximo, de uma branch de feature que só você usa, antes de abrir o PR).

**Regra prática:** rebase local antes de abrir PR (limpa seus próprios commits), merge para integrar na `main` (preserva o contexto de branches compartilhadas).

## Resolvendo conflito durante um rebase

Quando o mesmo trecho de arquivo foi alterado tanto na branch de destino quanto na branch que está sendo rebaseada, o Git para no commit conflitante e pede resolução manual antes de continuar:

```bash
git rebase main
# ... resolver o(s) arquivo(s) em conflito manualmente ...
git add .
git rebase --continue
# ou, para desistir e voltar ao estado anterior:
git rebase --abort
```

Diferente de um conflito de merge (resolvido uma vez, no commit de merge), um conflito de rebase pode se repetir a cada commit reaplicado, se vários deles tocarem o mesmo trecho.

## Interactive rebase — squash e limpeza de histórico local

```bash
git rebase -i HEAD~5  # abre editor com os últimos 5 commits

# pick   = manter
# reword = manter, editar mensagem
# edit   = parar para amendoar
# squash = combinar com commit anterior (mantém mensagem)
# fixup  = combinar, descartar mensagem
# drop   = remover commit
```

Ferramenta para transformar um histórico de trabalho bagunçado ("wip", "fix typo", "fix again") em um conjunto de commits [[wiki/concepts/atomic-commits|atômicos]] antes de abrir o PR — sem afetar ninguém, porque ainda é histórico local.

## Comparação

| | Rebase | Merge |
|---|---|---|
| Histórico | Linear, reescrito | Real, preservado (com merge commits) |
| `git bisect`/`git blame` | Mais efetivo | Mais ruidoso |
| Seguro em branch compartilhada | Não | Sim |
| Conflitos | Podem se repetir por commit | Resolvidos uma vez, no merge commit |
| Uso recomendado | Local, antes do PR | Integração final na branch principal |

## Ver também

- [[wiki/concepts/atomic-commits]] — squash via rebase interativo é a ferramenta prática para chegar a commits atômicos
- [[wiki/concepts/code-review]] — histórico limpo (pós-rebase local) facilita a revisão

## Key Sources

- [[wiki/sources/git-rebase-na-pratica]] — demonstração prática ponta a ponta: criação de branch, commit concorrente na main, rebase com conflito real, resolução via editor do VS Code, e reintegração na main
