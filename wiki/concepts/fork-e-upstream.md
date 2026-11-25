---
type: concept
title: "Fork e upstream (fluxo de contribuição por fork)"
aliases: ["fork", "upstream", "remote upstream", "syncing a fork", "sincronizar fork", "fork workflow", "forkar"]
date_created: 2026-11-24
date_updated: 2026-11-25
source_count: 2
tags: [git, github, fork, upstream, pull-request, branch, colaboracao]
skill: lang-dynamic
status: stub
---

# Fork e upstream

Fluxo para contribuir com um repositório em que você não tem permissão de escrita. O *fork* é uma cópia do repositório na sua conta; o clone local tem dois *remotes*: `origin` (o seu fork, onde você faz push) e `upstream` (o original, de onde você só puxa). A entrega é um pull request da branch do fork para o original `[external]` (https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks). Ver [[wiki/concepts/git]], [[wiki/entities/github]].

```bash
git remote add upstream https://github.com/<dono-original>/<repo>.git
git checkout main
git fetch upstream            # baixa commits; atualiza upstream/main
git merge upstream/main       # traz para a main local
git push origin main          # atualiza o fork
git checkout -b minha-mudanca # uma branch por entrega
# ... commits ...
git push origin minha-mudanca # e abre o pull request no GitHub
```

`fetch` não altera branches locais; só o merge (ou `git pull upstream main`, que faz os dois). O GitHub oferece o botão *Sync fork* e `gh repo sync` para o mesmo efeito. A regra que evita conflito: não commitar na branch padrão do fork, que deve espelhar o upstream; cada mudança vive na própria branch (*feature branch*), e os pull requests ficam independentes. Não confundir com [[wiki/concepts/git-flow]].

## No JavaScript Ninja, semana 3, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-metodos-de-objeto-continuacao]], é o fluxo de entrega dos desafios semanais: `origin` é `fdaciuk/curso-javascript-ninja` (o fork do aluno) e `upstream`, `da2k/curso-javascript-ninja` (o do curso). A master "sempre atualizada com o repositório principal" e com os desafios em branco; cada desafio numa branch (`challenge-03`), enviada com push e pull request. Recomenda a linha de comando porque o software do GitHub da época "não suporta mais de um remote" (afirmação não verificada). Ainda usa `master`; repositórios novos no GitHub usam `main` desde 2020.

## No JavaScript Ninja, semana 6, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-estrutura-de-repeticao-while]], o desafio da semana 6 segue "o mesmo" fluxo: atualizar a master, fazer o merge, criar a branch do desafio (a legenda diz "tablets gera em 06"; deve ser `challenge-06`), fazer o desafio e abrir pull request no repositório principal. Dúvidas "melhor até" por issue no GitHub, para a resposta servir a outros alunos.

## Key sources

- [[wiki/sources/javascript-ninja-metodos-de-objeto-continuacao]]: JavaScript Ninja, semana 3, vídeo 03: origin × upstream, branch por desafio, pull request
- [[wiki/sources/javascript-ninja-estrutura-de-repeticao-while]]: JavaScript Ninja, semana 6, vídeo 02: mesmo fluxo para o desafio 06
