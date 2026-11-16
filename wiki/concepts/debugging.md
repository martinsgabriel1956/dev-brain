---
type: concept
title: "Debugging"
aliases: ["depuração", "encontrar bugs"]
date_created: 2026-07-09
date_updated: 2026-11-16
source_count: 9
tags: [debugging, resolucao-de-problemas, pensamento-estruturado]
skill: tech-mentor-leadership
status: stub
---

## Definição

Processo de investigar um comportamento incorreto de um sistema até encontrar e corrigir sua [[causa-raiz]]. Na prática do dia a dia, debugging é a aplicação direta do método de [[pensamento-estruturado]] a um problema técnico concreto: entender o problema antes de mexer no código, decompor via [[arvore-de-decomposicao]], testar hipóteses ([[hipotese-e-validacao]]) em vez de assumir, e só então intervir no ponto exato do gargalo.

## Relação com outros conceitos

- [[pensamento-estruturado]] — o método geral do qual debugging é uma aplicação
- [[arvore-de-decomposicao]] — como quebrar um bug vago ("sistema lento") em perguntas específicas
- [[causa-raiz]] — o alvo final da investigação
- [[hipotese-e-validacao]] — validar suposições com dados antes de agir
- [[pensamento-regressivo]] — mapear o fluxo de trás para frente a partir do estado esperado

## Setup prático: debugger conectado desde o primeiro commit

Em vez de depurar via `console.log` + reiniciar servidor manualmente, [[wiki/concepts/setup-live-reload-debug-testes]] descreve como conectar o debugger do editor (`--inspect` do Node.js + `launch.json` do VS Code) direto ao ciclo de live reload e testes automatizados — permitindo breakpoints e inspeção de variáveis (inclusive via um "Debug Console" tipo REPL) sem sair do editor a cada hipótese testada.

## Quando Parar de Depurar Sozinho

[[wiki/sources/como-fazer-perguntas-certas-ciclo-de-2-horas]] propõe um limite prático: depois de ~2 h ([[wiki/concepts/ciclo-de-2-horas]]) sem sucesso, levar o que se investigou a alguém com uma [[wiki/concepts/pergunta-bem-formulada]] — o "erro exato + o que já tentei" é justamente o produto do processo de depuração.

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] corrige bugs ao vivo:
- **Cidades acumuladas** ("um erro de lógica").
- **`querySelectorAll` no lugar de `querySelector`**, achado pela mensagem do console de que `addEventListener` não é uma função.
- **Um `href` vazio** que recarregava a página.

Usa `console.log` em cada passo do algoritmo: "Console log tira todas as dúvidas da gente". Lembra que "a gente sempre tem bugs em nossas aplicações é normal".

## Na NLW #1, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] rastreia o dado com `console.log` nas duas pontas: no navegador, com "Preserve log" para não perder no reload, e no terminal, para o servidor. Também simula um erro de propósito (`INSERT INT`) para testar o `res.send("Erro no cadastro")`, e usa a aba Network para ver as requisições.

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], Mayk lê os erros em voz alta: `near "Fernandes": syntax error` (faltavam aspas), uma vírgula sobrando, `no such column`, `filter is not defined`, "Cannot POST /save-classes" (rota com nome diferente) e um espaço solto na query. "Identificar, entender, resolver." O SQL "não fala exatamente onde tá o erro".

Em [[wiki/sources/frontpush-estruturas-condicionais-booleanos-comparadores-javascript]], [[wiki/entities/nasser|Násser]] faz do `console.log` um hábito: "o programador sempre tem que estar plotando no console para ver qual é a direção que o código está tomando" quando há "bifurcações". O depurador do DevTools faz o mesmo sem editar o código.

## Key Sources

- [[wiki/sources/pensamento-estruturado-resolucao-de-problemas]]
- [[wiki/sources/3-pilares-testes-automatizados-produtividade]] — setup de debugger integrado a live reload e testes via Node.js `--inspect` + VS Code `launch.json`
- [[wiki/sources/como-fazer-perguntas-certas-ciclo-de-2-horas]] — limite de tempo e como transformar a investigação em pergunta
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — aplicação a APIs: conferir as peças da requisição no DevTools em vez de tentar de novo (ver [[wiki/concepts/debug-de-requisicao-http]])
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: três bugs ao vivo; console.log como sonda
- [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]]: console.log nas duas pontas; erro simulado; Network
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: NLW #2, dia 5: lendo erros de SQL e de rota

## Key sources (adição 2026-10-14)

- [[wiki/sources/como-sair-do-ciclo-de-bugs-e-retrabalho-andre-casciotti]] — debug diagnostica mas **não prova** a correção; evidenciar o erro antes e repetir o mesmo teste depois ([[wiki/concepts/evidenciar-o-problema]], [[wiki/concepts/provar-que-corrigiu]])
- [[wiki/sources/frontpush-estruturas-condicionais-booleanos-comparadores-javascript]]: FrontPUSH, JavaScript aula 03: console.log em cada bifurcação
