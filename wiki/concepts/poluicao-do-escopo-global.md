---
type: concept
title: "Poluição do escopo global (JavaScript)"
aliases: ["poluição do escopo global", "global namespace pollution", "variável global implícita", "implicit global", "global leak", "globais acidentais"]
date_created: 2026-11-24
date_updated: 2026-11-25
source_count: 3
tags: [javascript, escopo, escopo-global, var, modo-estrito, memoria, boas-praticas]
skill: lang-dynamic
status: stub
---

# Poluição do escopo global (JavaScript)

Colocar nomes no escopo global sem necessidade. Num script de navegador, todos os scripts da página dividem o mesmo global, então qualquer nome ali pode colidir com outro, ser sobrescrito por outro script e ficar vivo até a aba fechar ([[wiki/concepts/escopo-javascript]]).

## Como acontece

- `var` ou `function` no topo de um script (não módulo): viram propriedade de `window`/`globalThis`. `[external]`
- **Global implícita:** atribuir a um nome nunca declarado (`total = 0`, inclusive dentro de função) cria a global no modo não estrito, no momento em que a linha roda. No modo estrito é `ReferenceError`. `[external]`
- `let`/`const` no topo de um script ficam no global léxico: não viram propriedade de `window`, mas ainda colidem entre scripts.

## Por que é ruim

- **Colisão de nomes:** dois scripts com `var config` se sobrescrevem; `var name` troca `window.name`. `[external]`
- **Memória:** o global é raiz do coletor de lixo, então o que ele referencia nunca é coletado enquanto a referência existir ([[wiki/concepts/gerenciamento-de-memoria]]).
- **Acoplamento:** qualquer função pode ler e alterar o valor; o fluxo de dados fica invisível. No servidor, o mesmo problema aparece como estado mutável compartilhado entre requisições ([[wiki/concepts/estado-global-em-servidor]]). Constantes sem mutação são a exceção inofensiva ([[wiki/concepts/estado-global-inofensivo]]).

Crockford põe as globais no topo das "partes horríveis" do JavaScript (*JavaScript: The Good Parts*, 2008, apêndice A). `[external]`

## Remédios

- Declarar sempre (`const`, `let`; na era ES5, `var`) ([[wiki/concepts/var-let-const]]).
- `'use strict'`, ou código em módulos ES e classes, onde o modo estrito é o padrão.
- Módulos ES: cada arquivo tem escopo próprio; só sai o que for exportado.
- Na era ES5: IIFE (`(function () { ... })()`) e um único objeto namespace (`var App = {}`).
- Lint: `no-undef` e `no-implicit-globals` do ESLint. `[external]`

## No JavaScript Ninja, semana 4, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-escopo-de-variaveis-e-funcoes]], o escopo global "é algo ruim" e "um erro de design da linguagem". Mostra a global implícita (atribuir sem `var` dentro da função cria a variável no global depois da invocação) e cita dois custos: "conflito de nomes" e memória que o JavaScript "não vai poder limpar". Remédio da aula: "sempre utilize a palavra-chave var". O modo estrito, a IIFE e os módulos não aparecem.

## No JavaScript Ninja, semana 6, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operador-virgula-e-switch]], trocar as vírgulas de `var a = 1, b = 2, c = 3` por ponto e vírgula "cria a, b, c como variáveis globais, porque eu não estou utilizando a palavra-chave pra eles". Na verdade só `b` e `c` viram globais implícitas (o `a` continua com `var`), e só fora do modo estrito. A versão mais traiçoeira da mesma armadilha é `var a = b = c = 3`.

## Key sources

- [[wiki/sources/javascript-ninja-escopo-de-variaveis-e-funcoes]]: JavaScript Ninja, semana 4, vídeo 03: global como erro de design; variável sem var; conflito de nomes e memória
- [[wiki/sources/javascript-ninja-retorno-de-funcoes-com-arrays-e-objetos]]: JavaScript Ninja, semana 5, vídeo 01: retornar objeto da função em vez de criá-lo no global (germe do module pattern)
- [[wiki/sources/javascript-ninja-operador-virgula-e-switch]]: JavaScript Ninja, semana 6, vídeo 01: ponto e vírgula no lugar da vírgula vira global implícita
