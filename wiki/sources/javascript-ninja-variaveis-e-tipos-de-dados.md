---
type: source
title: "Variáveis e tipos de dados (JavaScript Ninja, aula 01, parte 2)"
aliases: ["JavaScript Ninja aula 01", "JS Ninja variáveis e tipos de dados", "01 - Variáveis e tipos de dados"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [javascript, variaveis, var, tipos-de-dados, number, float, string, boolean, null, undefined, object, array, notacao-de-ponto, notacao-de-colchetes, nodejs, repl, tipagem-dinamica]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-variaveis-e-tipos-de-dados.md"
source_url: ""
author: "Fernando Daciuk (inferido da legenda)"
date_published: ""
date_ingested: 2026-11-24
---

# Variáveis e tipos de dados (JavaScript Ninja, aula 01, parte 2)

## TL;DR

Segunda parte da primeira aula do curso [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 15 min), com [[wiki/entities/fernando-daciuk|Fernando Daciuk]] digitando no REPL do [[wiki/entities/nodejs|Node]]. Aula da era ES5: só aparece `var`.

- **Variável** é "um nome simbólico que você vai dar para um tipo de valor", declarado com `var` e atribuído com `=`. Sem valor, ela é `undefined`. O nome vem de "um valor que pode variar": `x` passa por `undefined`, `0`, `1`, `1.2`, string, boolean, `null` e objeto ([[wiki/concepts/var-let-const]], [[wiki/concepts/sistema-de-tipos]]).
- **number:** inteiro e decimal ("float, ou como números reais") são o mesmo tipo ([[wiki/concepts/tipos-primitivos-javascript]]).
- **string:** aspas duplas ou "apóstrofo", "isso não tem diferença alguma" ([[wiki/concepts/string]]).
- **boolean:** `true` ou `false`.
- **null e undefined:** `null` é "nenhum valor"; `undefined`, "a ausência de valor". "Na maior parte das vezes a gente vai tratar eles como sendo a mesma coisa" ([[wiki/concepts/null-e-undefined]]).
- **object:** literal com chaves, propriedades `chave: valor`, leitura e escrita com ponto: `pessoa.altura = 1.90` ([[wiki/concepts/objetos-javascript]]).
- **array:** "uma lista de valores" entre colchetes, índice a partir de 0: `numeros[3]` dá `4` ([[wiki/concepts/array]]).
- **"Não existem arrays":** "eles nada mais são do que objetos". Prova: `pessoa['altura']` funciona como `pessoa.altura`. "A notação de objeto é mais rápida, então procuro usar sempre que possível" ([[wiki/concepts/notacao-de-ponto-e-colchetes]]).

Continua em [[wiki/sources/javascript-ninja-operadores-aritmeticos]] (operadores aritméticos).

## Key Claims

### Variáveis

- "Ele é um nome simbólico que você vai dar para um tipo de valor [...] para você declarar uma variável, você precisa usar a palavra-chave var."
- No terminal: "vou acessar a interface do Node para poder digitar os comandos". `var x` + Enter; "ela não tem nenhum valor [...] o valor dela é undefined, ou é um valor indefinido".
- "Como eu faço para atribuir um valor [...]? Eu vou usar o sinal de igual." Depois de `x = 0`, "X já não é mais avaliado como undefined como antes. Agora ele é avaliado como valor zero."
- "Variável, ela tem esse nome exatamente por esse motivo [...] ela tem um valor que pode variar, que pode mudar": `undefined` → `0` → `1`.

### number

- "1.2 também é um tipo de número, mas é um tipo de número conhecido como float, ou como números reais [...] números decimais também são válidos em JavaScript." O detalhe fica "para frente, quando falar da estrutura lexical".

### string e boolean

- "Hello World não é um número [...] mas sim uma sequência de caracteres. Strings em JavaScript, elas são representadas por qualquer caractere dentro de aspas duplas [...] ou dentro de apóstrofo."
- "Em algumas linguagens de programação é diferente e elas precisam que você coloque dentro aspas duplas, mas o JavaScript [...] você pode usar tanto com aspas duplas como apóstrofo."
- "Boolean é representado basicamente true ou false [...] algo que é verdadeiro ou algo que é falso" ([[wiki/concepts/logica-booleana]]).
- Atalho de passagem: Control L limpa o terminal; no Mac, "provavelmente deve ser Command L".

### null e undefined

- "O valor null, na verdade, significa nenhum valor, significa que o X não tem valor nenhum definido para ele." `undefined` "é parecido com null, não é a mesma coisa, mas ele, digamos assim, a ausência de valor".
- "O null, ele representa o valor de uma variável quando ela não tem nenhum valor [...] e undefined representa quando a variável não existe, mas no JavaScript a variável pode existir e pode continuar tendo valor undefined."
- "Os dois têm uma função bastante parecida de deixar uma variável sem valor"; as "pequenas diferenças" ficam para "alguns casos específicos".

### Objetos

- Objeto e array são "dois tipos de dados [...] bastante importantes"; o objeto é "um dos temas mais importantes em JavaScript", porque "a maior parte das coisas [...] a gente vai estar tratando diretamente com esse tipo de dado".
- Literal: "uma representação com o chaves e eu fecho chaves". "Um objeto, ele tem propriedades e métodos [...] as propriedades são basicamente coisas que têm um objeto" ([[wiki/concepts/programacao-orientada-a-objetos]]).
- Exemplo: `var pessoa = { altura: 1.87, peso: 90 }`. Leitura: "para você pegar a altura ou o peso da pessoa, é usar o ponto".
- "Existem duas formas": criar "todo ele de uma vez só" (o literal atribuído à variável) ou "usar a própria notação de objeto": `pessoa.altura = 1.90`, `pessoa.peso = 80`. "O peso continua o mesmo, porque eu só mudei a propriedade a altura."

### Arrays

- "Ele é uma lista, uma lista de valores." `var numeros = []` é "o meu array vazio"; `numeros = [1, 2, 3, 4, 5, 6]`.
- "Ele é acessado por índices [...] números iniciados a partir do zero": "a primeira posição do array, na verdade a posição 0". Para o 4, "o índice 3".
- Erro de digitação ao vivo: `numero[3]` dá "o número não está definido [...] porque eu não tenho essa variável".

### Arrays são objetos

- "Na verdade, no JavaScript não existem arrays [...] eles nada mais são do que objetos." Prova: `pessoa['altura']`, passando "uma string com o valor do índice", também dá a altura, "tanto com aspas simples como as duplas".
- "A notação de objeto é mais rápida, então procuro usar sempre que possível."
- Próximo vídeo: operadores.

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para os fundamentos de JavaScript (variáveis, tipos, notação de propriedade); as precisões vêm do MDN e da especificação, marcadas `[external]` (sem fetch neste ingest, a partir do conhecimento base; confiança alta salvo indicação).

1. **O `undefined` depois de `var x` no REPL não é o valor de `x`.** O REPL imprime o valor de conclusão da instrução, e uma declaração `var` não tem valor: por isso aparece `undefined` até em `var x = 0`. O `x` sozinho é que mostra o valor da variável. O "apareceu aqui ou ali" da legenda é, quase certamente, esse eco (média-alta).
2. **"undefined representa quando a variável não existe" está errado, e a própria aula mostra.** `[external]` Ler uma variável não declarada lança `ReferenceError: numero is not defined`: é o "não está definido" do erro de digitação. `undefined` é o valor de uma variável declarada sem atribuição, de uma propriedade que não existe e de função sem `return`. A exceção é `typeof naoDeclarada`, que dá `"undefined"` sem erro (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined). Ver [[wiki/concepts/null-e-undefined]].
3. **null e undefined não são "a mesma coisa" na maior parte das vezes.** `null == undefined` é `true`, mas `===` dá `false`; `typeof null` é `"object"`; parâmetro default só reage a `undefined`; `JSON.stringify` remove chaves com `undefined` e mantém `null`. Já documentado em [[wiki/concepts/tipos-primitivos-javascript]] e [[wiki/concepts/igualdade-javascript]].
4. **Todo number é ponto flutuante.** `[external]` Não há tipo inteiro separado: `number` é IEEE 754 de 64 bits (double), e `1` e `1.2` são o mesmo tipo. "Float" e "números reais" são aproximações: `0.1 + 0.2 !== 0.3`, e inteiros só são exatos até `Number.MAX_SAFE_INTEGER` (2^53 − 1). Para além disso, `bigint` (ES2020, posterior à aula) (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number).
5. **Faltam tipos.** A aula cita number, string, boolean, null, undefined, object e array. `[external]` Pela especificação atual são oito: sete primitivos (string, number, bigint, boolean, undefined, symbol, null) e object. Array não é tipo próprio: `typeof []` é `"object"`, e se testa com `Array.isArray`. `symbol` chegou no ES2015 e `bigint` no ES2020, depois da gravação (inferência de data, média).
6. **"Não existem arrays" exagera um pouco.** `[external]` Arrays são objetos, e os índices são chaves de propriedade convertidas para string (`numeros['3']` funciona). Mas são objetos especiais (*exotic objects*): `length` se atualiza sozinho, há `Array.prototype` com `push`, `map` etc., e os motores guardam arrays densos de forma contígua. Ver [[wiki/concepts/array]] e [[wiki/concepts/objetos-javascript]].
7. **"A notação de objeto é mais rápida" não se sustenta hoje.** Com chave literal, `obj.a` e `obj['a']` geram o mesmo acesso nos motores modernos (V8, SpiderMonkey). A preferência pelo ponto é de legibilidade, e os linters a impõem (regra `dot-notation` do ESLint). Colchetes são obrigatórios quando a chave é dinâmica (`obj[chave]`) ou não é identificador válido (`obj['data-id']`) (inferência a partir do conhecimento base, média-alta). Ver [[wiki/concepts/notacao-de-ponto-e-colchetes]].
8. **Aspas simples e duplas são equivalentes, mas há a crase.** `[external]` O ES2015 acrescentou a template literal com crase e `${}` ([[wiki/concepts/template-literals]]). A diferença prática entre `'` e `"` é só qual delas precisa de escape dentro do texto.
9. **Só `var`.** A aula é anterior a `let` e `const` (ES2015) ou não os usa. O código moderno usa `const` por padrão e `let` quando reatribui. A wiki já tem os detalhes de escopo de função e hoisting em [[wiki/concepts/var-let-const]].
10. **Tipagem dinâmica, não "valor que varia".** A mesma `x` recebe número, string, booleano e objeto sem erro: é a [[wiki/concepts/sistema-de-tipos|tipagem dinâmica]] do JavaScript. O tipo está no valor, não na variável.
11. **Propriedades e métodos.** A aula define propriedade, mas não mostra método (propriedade que guarda função). O FrontPUSH, aula 05, cobre isso e o `this` ([[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]]).
12. **Legenda ruim.** O ASR trocou quase todos os termos técnicos: "vai"→var, "mod"/"noite"→Node, "Rei"/"Harry"/"R"→array, "nu"/"no"→null, "default"/"anel de"→undefined, "bullying"→boolean, "estilingue"→string, "estranhos"→Strings, "fonte"→float, "inimigos"/"incitar"→índices. A lista completa e os trechos deixados literais estão no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor (nome reconstruído da legenda "Fernanda Gentil").
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.
- [[wiki/entities/nodejs]]: REPL usado nas demonstrações.

## Concepts

- [[wiki/concepts/var-let-const]]
- [[wiki/concepts/tipos-primitivos-javascript]]
- [[wiki/concepts/null-e-undefined]]
- [[wiki/concepts/string]]
- [[wiki/concepts/logica-booleana]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/array]]
- [[wiki/concepts/notacao-de-ponto-e-colchetes]] (criado neste ingest)
- [[wiki/concepts/programacao-orientada-a-objetos]]
- [[wiki/concepts/sistema-de-tipos]]
- [[wiki/concepts/template-literals]]
- [[wiki/concepts/igualdade-javascript]]

## Open Questions

- "Basicamente, o padrão é o número de jovens, que são números decimais": provavelmente fala de o padrão ser ponto flutuante (double?). A legenda não decide.
- "Os mais conhecidos, pelo menos sob o nome de boolean, null, undefined": "nome de" pode ser "number", e "sob o" pode ser "string". Ficou literal.
- "A representação literal do objeto vai ser esse finalzinho de bichado e se fecha chaves": provavelmente "abre e fecha chaves".
- "Aspas simples como com uma seta": a crase? Em 2015 seria estranho; mais provável "aspas duplas".
- Data e número da aula no curso: o vídeo se diz "segunda parte da primeira aula". A busca na web não achou a página da aula (https://www.tabnews.com.br/Devi/aula-01-tudo-sobre-variaveis e outros resultados eram de outros cursos).

## Raw quotes

- "um nome simbólico que você vai dar para um tipo de valor"
- "ela tem um valor que pode variar, que pode mudar"
- "no JavaScript não existem arrays [...] eles nada mais são do que objetos"
- "A notação de objeto é mais rápida, então procuro usar sempre que possível."
