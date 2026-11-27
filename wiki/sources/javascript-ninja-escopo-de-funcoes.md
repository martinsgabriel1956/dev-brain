---
type: source
title: "Escopo de funções (JavaScript Ninja, semana 9, vídeo 01)"
aliases: ["JavaScript Ninja escopo de funções", "JS Ninja função dentro de função", "01 - Escopo de funções"]
date_created: 2026-11-26
date_updated: 2026-11-26
source_count: 0
tags: [javascript, escopo, funcoes, funcao-aninhada, hoisting, closure, var]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-escopo-de-funcoes.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-26
---

# Escopo de funções (JavaScript Ninja, semana 9, vídeo 01)

## TL;DR

Primeiro vídeo depois da "correção" do desafio 8 do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 11 min), de [[wiki/entities/fernando-daciuk|Fernando Daciuk]]. A semana 9 é inferida: o vídeo vem depois do desafio 8 e o curso fecha cada semana com um desafio. Continua de [[wiki/sources/javascript-ninja-programacao-funcional-parte-3|programação funcional, parte 3]] e retoma [[wiki/sources/javascript-ninja-escopo-de-variaveis-e-funcoes|escopo de variáveis e funções]], agora com a função como dona do escopo.

- **Função dentro de função:** `myFunction` declara `sum` e retorna `sum()`; o resultado é 3. Chamar `sum()` fora dá erro ("sum is not found" na legenda): a função interna tem como escopo "aquela função onde ela está dentro" ([[wiki/concepts/escopo-javascript]], [[wiki/concepts/funcoes-javascript]]).
- **A interna lê as variáveis da externa:** `number1` e `number2`, declaradas em `myFunction`, valem "para toda essa função", e `sum` as soma. A aula diz que `sum` faz o papel de algo que "a gente vai ver mais para frente", uma função "que consegue acessar parâmetros externos a ela" ([[wiki/concepts/closure-javascript]]; a legenda diz "uma coisa").
- **A posição da declaração não importa:** `sum` declarada antes das variáveis ainda devolve 3, porque só é executada depois que elas têm valor.
- **Função depois do `return`:** com `return sum()` antes de `function sum() {}`, a aula esperava `undefined`, já que tudo depois do `return` "o JavaScript simplesmente ignora", e a função roda normalmente. "Que magia é essa?" O nome é **hoisting**, assunto do próximo vídeo ([[wiki/concepts/hoisting-javascript]]).

## Key Claims

### Função dentro de função

- "A gente sabe que isso, uma função dentro de outra função, é permitido. Mas como fica o escopo dessa função?"
- `myFunction` cria `sum`, que retorna `1 + 2`, e devolve `sum()` invocada: "teoricamente, o resultado dessa função, quando é invocada, é para me retornar 3". Funcionou.
- Antes de dar nome, a aula tenta devolver a função "só invocada, que eu não dei o nome para ela", e diz "agora sim não funciona". O código não aparece na legenda.

### A interna não existe fora

- Um `console.log` com `sum()` no fim do arquivo: o primeiro log mostra 3, o segundo dá erro, "porque foi criado dentro da função".
- "Da mesma forma que variáveis [...] as funções também criadas dentro de outras funções, o escopo dela é aquela função onde ela está dentro."
- "Para eu [...] usá-la fora, que eu precisaria ter criado essa função sum de fora de myFunction."
- "A função sum, ela só existe enquanto myFunction existia. A partir do momento em que myFunction não existe mais [...] eu não consigo acessar a função interna."

### A interna lê o escopo da externa

- `number1` e `number2` dentro de `myFunction`, somadas em `sum`: "Isso aqui funciona. [...] Porque o escopo dessas variáveis aqui valem para toda essa função [...] desde o início [...] até o final dela."
- A `sum` "está fazendo o papel de uma coisa que é uma coisa, é uma função que ela consegue acessar parâmetros externos a ela", e o nome fica para depois.

### Posição das declarações

- Com `sum` escrita antes de `var number1`/`number2`, o resultado continua 3. Quando o interpretador passa pela função, "ele simplesmente verifica que essa função aqui existe, mas ele não executa"; as variáveis recebem valor e "logo depois eu faço a invocação da função sum".
- A regra que a aula tira: "independente da posição que eles foram criados, contanto que ela seja invocada somente depois que esses valores fossem criados".

### Função depois do return

- "A gente já viu que tudo que acontece depois do return o JavaScript simplesmente ignora." `function sum` vai para depois do `return sum()`.
- "Teoricamente [...] deveria retornar undefined, porque [...] ainda não existe." Mas "eu consigo executar normalmente a função".
- "Na verdade, o que acontece é algo chamado hoisting [...] A gente vai ver no próximo vídeo."

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para escopo, funções aninhadas ou hoisting no JavaScript básico. As precisões vêm da MDN e da especificação, marcadas `[external]`. As demos foram reproduzidas no Node 22.23 com os nomes reconstruídos (`myFunction`, `sum`, `number1`, `number2`).

1. **O erro é `ReferenceError: sum is not defined`.** A legenda diz "sum is not found"; o Node 22 imprime `ReferenceError: sum is not defined` (verificado). É o mesmo erro do local lido de fora em [[wiki/sources/javascript-ninja-escopo-de-variaveis-e-funcoes]].
2. **"Só existe enquanto myFunction existia" é meia verdade.** `[external]` Cada chamada cria um escopo novo com uma `sum` nova. Se `myFunction` devolvesse `sum` em vez de `sum()`, a função interna sobreviveria à externa e manteria `number1`/`number2` vivas. Isso é a [[wiki/concepts/closure-javascript|closure]] que a aula anuncia, e o `adder` de [[wiki/sources/javascript-ninja-programacao-funcional-parte-2]] já fazia isso. A frase vale para o exemplo do vídeo, em que só o resultado sai.
3. **"Parâmetros externos" são variáveis externas.** A interna lê qualquer nome do escopo de fora: variáveis, parâmetros e outras funções. É o escopo léxico de [[wiki/concepts/escopo-javascript]].
4. **A posição importa menos para declarações de função do que para valores.** `[external]` O hoisting leva a **declaração** de `function sum() {}` inteira ao topo do escopo, e de `var` só o nome, com valor `undefined`. Verificado no Node 22:
   - variáveis antes do `return`, função depois: 3 (a demo da aula);
   - variáveis e função depois do `return`: `NaN`, porque `sum` existe mas `number1` e `number2` ainda são `undefined` ([[wiki/concepts/null-e-undefined]]);
   - `var sum = function () {}` depois do `return`: `TypeError: sum is not a function`;
   - `const sum = () => 3` depois do `return`: `ReferenceError: Cannot access 'sum' before initialization` (zona morta temporal, [[wiki/concepts/var-let-const]], [[wiki/concepts/arrow-functions]]).
5. **"Ignora o que vem depois do return" vale para a execução, não para as declarações.** O `return` interrompe a execução, mas o motor registra as declarações do corpo inteiro antes de executar a primeira linha. O código depois do `return` nunca roda; só os nomes já existem.
6. **Funcionar não quer dizer recomendado.** `[external]` Guias como o da Airbnb proíbem usar a função antes de declará-la (`no-use-before-define` do ESLint, com `functions: true`; sem fetch, confiança média-alta), mesmo funcionando. O estilo da aula, com `return` antes das funções auxiliares, também tem defensores, porque põe o "o quê" antes do "como". A aula só mostra que funciona.
7. **Legenda.** Trocas principais: "na índia"→Ninja, "nasceu"→Daciuk, "mais infantil"/"uma infantil"/"mãe falante"/"uma fonte"→myFunction, "são"/"Same"/"San"/"Sand"/"Sandro"/"Santander"/"sangue"/"samba"/"Sambo"/"Ação"→sum, "Number One"/"One M8"→number1/number2, "queria"→crio, "Mitani olhava as equipes"/"metano"→return/o JavaScript, "ao default"→undefined, "Rei este"/"rei"→hoisting. Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/escopo-javascript]]
- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/hoisting-javascript]]
- [[wiki/concepts/closure-javascript]]
- [[wiki/concepts/var-let-const]]
- [[wiki/concepts/arrow-functions]]
- [[wiki/concepts/null-e-undefined]]
- [[wiki/concepts/programacao-funcional]]

## Open Questions

- **"Uma coisa que é uma coisa".** Provavelmente "uma closure, que é uma closure" (média). Ficou literal no raw. O nome bate com o anúncio de "ver mais para frente".
- **A primeira tentativa "não funciona".** Antes de nomear `sum`, a aula devolve uma função "só invocada, que eu não dei o nome". Talvez fosse `function () {...}()` como declaração, que dá `SyntaxError` ([[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]]). Não dá para reconstruir.
- **A demo das variáveis.** "vai o ano igual a 1 2 2", "passar uma, vai passar dois", "Mamberti", "os valores de Ana" e "o ano meio" parecem `var number1 = 1`, `var number2 = 2` e `number1` (média-baixa). Ficaram literais.
- **"Você chama aquilo noite"** e **"retornando na mesma noite"**: talvez "vou chamar aqui o node" e "number1 + number2"; literais.
- **"Vou dar um pocket aqui"**: talvez "vou dar um cat aqui", para mostrar o arquivo no terminal; literal.
- **"O insistiu o desafio 8"**: o trecho sobre a dificuldade do desafio ficou ilegível.
- **"Banco de Fomento pode morrer", "depois de oito anos", "Mark brilha"**: provavelmente frases sobre mover a função para depois do `return`; literais.

## Raw quotes

- "o escopo dela é aquela função onde ela está dentro"
- "ele simplesmente verifica que essa função aqui existe, mas ele não executa"
- "Que magia é essa?"

Vídeo seguinte na wiki: [[wiki/sources/javascript-ninja-hoisting]] (semana 9, vídeo 02), que explica o hoisting anunciado aqui.
