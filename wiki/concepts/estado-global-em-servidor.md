---
type: concept
title: "Estado Global em Servidor"
aliases: ["global state", "estado global", "estado global no servidor"]
date_created: 2026-10-06
date_updated: 2026-11-27
source_count: 3
tags: [estado-global, stateless, backend, singleton, cache]
skill: tech-mentor-backend
status: draft
---

# Estado Global em Servidor

Estado mutável acessível por qualquer requisição de um processo servidor: cache in-memory (`Map`, Redis instanciado no processo), variável no topo de um módulo (módulos JS se comportam como [[wiki/concepts/singleton-pattern]]), config mutável, `currency`/`discount` fora de função ou numa classe compartilhada. Se uma requisição altera, altera para **todos os usuários**, o que quebra o princípio [[wiki/concepts/stateless]] do HTTP.

## Consequências

- Contaminação entre requests e dependência da **ordem das chamadas** (ver [[wiki/concepts/efeito-colateral]]).
- [[wiki/concepts/race-condition]] com requests paralelos.
- Bugs não reproduzíveis ([[wiki/concepts/reprodutibilidade-de-bugs]]).
- Bugs **sutis**: o exemplo óbvio (`currentUser`) é raro; o comum é `currency`/`discount` ou cache.

## Remédios

[[wiki/concepts/request-context]], estado local passado explicitamente ([[wiki/concepts/dependencia-externa-oculta]]), [[wiki/concepts/dependency-injection]]. Exceção: [[wiki/concepts/estado-global-inofensivo]].

Ver também [[wiki/concepts/estado-compartilhado]] (versão mais geral, sem foco em servidor).

## No JavaScript Ninja, semana 4, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-escopo-de-variaveis-e-funcoes]], o mesmo problema no navegador da era ES5: globais colidem entre scripts e não são coletadas. No servidor, o global é compartilhado entre requisições ([[wiki/concepts/poluicao-do-escopo-global]]).

## Globais impedem duas instâncias (Ousterhout, cap. 7)

[[wiki/sources/filosofia-do-design-de-software-cap-07-camada-diferente-abstracao-diferente]] (7.5) dá mais uma consequência: com variáveis globais, não dá para ter duas instâncias independentes do sistema no mesmo processo, porque os acessos conflitam. Parece não importar em produção, mas importa em testes. A saída do livro é o [[wiki/concepts/objeto-de-contexto]], um por instância.

## Key sources

- [[wiki/sources/estado-global-stateless-side-effects-reprodutibilidade-galego]]
- [[wiki/sources/javascript-ninja-escopo-de-variaveis-e-funcoes]]: JavaScript Ninja, semana 4, vídeo 03: globais no navegador
- [[wiki/sources/filosofia-do-design-de-software-cap-07-camada-diferente-abstracao-diferente]] — globais impedem várias instâncias no mesmo processo (7.5)
