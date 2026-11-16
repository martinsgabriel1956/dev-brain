---
type: source
title: "Variáveis, tipos de dados e operadores em JavaScript (FrontPUSH)"
aliases: ["FrontPUSH variáveis e operadores", "módulo de JavaScript ES6, aula 02", "Variáveis & Operadores"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [javascript, variaveis, var-let-const, escopo, tipos-de-dados, typeof, objeto, concatenacao, template-literals, operadores, curso, frontend]
skill: lang-dynamic
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-variaveis-tipos-de-dados-operadores-javascript.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Variáveis, tipos de dados e operadores em JavaScript (FrontPUSH)

## TL;DR

Aula 02 do módulo de JavaScript ES6 do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]], que diz o nome e o sobrenome (Yousef, na grafia da legenda). A partir daqui ele some da tela e fica só a voz. A lição 01 anunciava a instalação do ambiente nesta aula, mas ela vai direto ao código.

- **Variável:** "um espacinho na memória" com uma "label"; serve para não ficar "redefinindo muitas coisas".
- **[[wiki/concepts/var-let-const|var, let e const]]:** antes do ES6 só existia `var`. `const` é "uma constante": reatribuir dá erro. `var` tem "caráter mais global" e ignora o bloco: `{ var nome = 'Yousef' }` sobrescreve o `nome` de fora. `let` "respeitou o bloco": imprime `Yousef` dentro e `Násser` fora.
- **Case sensitive:** `nome` e `Nome` são variáveis diferentes.
- **"Sete tipos de dados":** mostra string, number, boolean, undefined (variável sem valor), symbol e object ({} com chaves). Ver [[wiki/concepts/tipos-primitivos-javascript]] e [[wiki/concepts/null-e-undefined]].
- **"Tudo em JavaScript é objeto":** como no CSS "tudo é caixa" ([[wiki/concepts/box-model]]). Um objeto é "uma classe gigante, uma caixa" com variáveis e funções: `console` é a caixa, `.log` a função. `typeof` revela o tipo.
- **Concatenação:** `nome + ' ' + sobrenome`; sem o espaço, "juntou uma na outra". **Template string** do ES6: crase e `${}`, onde cabe "o que eu quiser de JavaScript". Ver [[wiki/concepts/template-literals]].
- **Operadores aritméticos:** `+`, `-`, `*`, `/` e `%` (resto), com `var soma = 200 + 200`. Ver [[wiki/concepts/operadores-aritmeticos-javascript]].

## Key Claims

### Variável

- "Variável é basicamente um nome que a gente define [...] eu fui lá na memória, aloquei um espacinho lá, defini uma label para esse espacinho chamado nome e coloquei o conteúdo Násser lá dentro."
- O motivo: "facilita a minha vida no código para eu não ficar redefinindo muitas coisas, simplesmente colocar um conteúdo em uma variável e depois simplesmente chamar ela, ou então manipular".

### var, let e const

- "Existem basicamente três tipos que a gente utiliza, que é o var, o let e o const." "Antes do ES6 só existia o var"; com o ES6 vieram o `let`, "muito parecido com o var", e o `const`.
- `const`: "é uma variável que não é para alterar o conteúdo dela ao longo do código". Ao fazer `nome = 'Yousef'`, o console avisa que "você está tentando atribuir um valor diferente a uma variável constante". "Você tem que definir um valor para ela e não pode mais alterar, esse é o escopo."
- `var` × `let`: "uma variável que tem um caráter mais global e uma variável que tem um caráter de bloco"; vai "ficar mais evidente" com funções.
- Demo: `nome = 'Násser'` fora; um bloco "como se fosse uma função" com `nome = 'Yousef'` e `console.log(nome)`; outro `console.log` depois. Com `var`, as duas saídas são `Yousef` ("mesmo sendo de blocos diferentes"). Com `let`, "plotou Yousef Násser, ou seja, ele respeitou o bloco".
- "O JavaScript é case sensitive [...] nome com o n minúsculo e uma outra variável aqui embaixo com o N maiúsculo [...] variáveis diferentes."

### Tipos de dados e objeto

- "Vamos conhecer um pouco sobre os sete tipos de dados": `let nome = 'Násser'` (string, "um conjunto de caracteres"); `let idade = 25` (numérico); `feliz = true` (booleano, "muito interessante [...] com estruturas condicionais"); `let nada` sem atribuir é `undefined`; `symbol`; e "por último um objeto [...] eu abro e fecho chaves".
- "Entender o que é objeto vai facilitar demais [...] porque justamente tudo em JavaScript é objeto. Lembra que eu dizia que lá em CSS tudo é div, tudo é caixa, aqui praticamente tudo é objeto."
- "O próprio console.log é um objeto, o que é um objeto, é basicamente uma classe gigante, uma caixa muito grande onde lá dentro tem variáveis e funções [...] console é o nome da caixa, .log é o nome da função que tem dentro de console."
- `typeof`: `string`, `number`, `boolean` e `object` para as variáveis da aula.

### Strings e operadores

- Concatenação com `+`: "ele juntou, só que ele não colocou o espaço [...] então você concatena com mais em JavaScript."
- Template string: "uma sintaxe do próprio ES6 para frente, onde você coloca [...] o acento em crase, para você não ficar emendando"; `${}` com "o que eu quiser de JavaScript aqui dentro". Exemplo: `` `${nome} tem o sobrenome ${sobrenome}` ``.
- Operadores: "operação de mais, operação de menos, operação de multiplicação, operação de divisão, operação de resto [...] esses aí são os operadores aritméticos que a gente vai trabalhar, por exemplo, em estruturas condicionais".

## Entities

- [[wiki/entities/nasser]]: instrutor (diz o nome e o sobrenome).
- [[wiki/entities/frontpush]]: curso; módulo de JavaScript ES6.
- [[wiki/entities/javascript]]: assunto da aula.

## Concepts

- [[wiki/concepts/var-let-const]]
- [[wiki/concepts/tipos-primitivos-javascript]]
- [[wiki/concepts/null-e-undefined]]
- [[wiki/concepts/template-literals]] (criado neste ingest)
- [[wiki/concepts/operadores-aritmeticos-javascript]] (criado neste ingest)
- [[wiki/concepts/string]]
- [[wiki/concepts/imutabilidade]]
- [[wiki/concepts/programacao-orientada-a-objetos]]
- [[wiki/concepts/box-model]]
- [[wiki/concepts/ecmascript]]
- [[wiki/concepts/logica-de-programacao]]
- [[wiki/concepts/igualdade-javascript]]

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para os fundamentos de JavaScript (variáveis, tipos, operadores); as precisões abaixo vêm do MDN e da especificação, marcadas como `[external]`.

- **`var` não é "global", é de função.** `[external]` `var` ignora o bloco `{}`, mas respeita a função: dentro de uma `function`, o `var nome = 'Yousef'` não vazaria (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var). Por isso o bloco "como se fosse uma função" engana: numa função, `var` e `let` dariam o mesmo resultado. A aula também não mostra o *hoisting* nem a leitura antes da declaração (`undefined` com `var`, `ReferenceError` com `let`). Ver [[wiki/concepts/var-let-const]].
- **`const` impede reatribuição, não mutação.** `[external]` `const pessoa = {}; pessoa.nome = 'x'` funciona. "Não é para alterar o conteúdo" vale para o vínculo, não para o objeto ([[wiki/concepts/imutabilidade]]). O erro da demo é `TypeError: Assignment to constant variable.` `const` também tem escopo de bloco, igual ao `let`, e exige valor na declaração. A wiki já registra a mesma confusão na NLW (Mayk Brito).
- **"Esse é o escopo"** depois do `const` não é escopo; é a regra de reatribuição. Escopo é onde o nome existe (bloco, função, módulo).
- **"Três tipos" de variável:** `var`, `let` e `const` são formas de declarar, não tipos. Os tipos são os do valor.
- **São oito tipos, e a aula mostra seis.** `[external]` Sete primitivos (string, number, bigint, boolean, undefined, symbol, null) e object (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures). Faltam `null` e `bigint`. A página [[wiki/concepts/tipos-primitivos-javascript]] já lista os oito, e `typeof null === "object"` é a armadilha clássica.
- **Nem tudo em JavaScript é objeto.** `[external]` Primitivos não são objetos e não têm propriedades próprias. `'Násser'.length` funciona porque o motor embrulha a string num objeto `String` temporário (*autoboxing*). Funções e arrays, esses sim, são objetos.
- **Objeto não é "uma classe gigante".** Objeto é um conjunto de propriedades (chave → valor), e uma propriedade que guarda função se chama método. Classe é um molde para criar objetos; em JS, `class` (ES2015) é sintaxe sobre protótipos ([[wiki/concepts/programacao-orientada-a-objetos]]). `console` é um objeto do ambiente (navegador, Node), não da linguagem; `log` é um método dele.
- **"O que eu quiser de JavaScript" no `${}`** é qualquer expressão (`${a + b}`, `${f()}`, ternário), não comandos como `if` ou `for` ([[wiki/concepts/template-literals]]). "Tipologia" na legenda é provavelmente "template literal" ou "template string" (confiança baixa; ficou literal no raw).
- **`+` não é só aritmético.** `[external]` Com uma string de um lado, vira concatenação: `'200' + 200` dá `'200200'`, e `'200' - 200` dá `0` (coerção). Falta o `**` (potência, ES2016). Nas condicionais quem decide são os operadores de comparação e lógicos (`===`, `>`, `&&`); o aritmético que mais aparece num `if` é o `%` (par ou ímpar). Ver [[wiki/concepts/operadores-aritmeticos-javascript]] e [[wiki/concepts/igualdade-javascript]].
- **`var soma`** depois de apresentar `let` e `const`: o código moderno usa `const` por padrão e `let` quando precisa reatribuir.
- **Variável como "espacinho na memória"** é uma boa imagem para começar. `[external]` Em JS o nome se liga a um valor: com objetos, duas variáveis podem apontar para o mesmo objeto, e mudar por uma aparece na outra.

## Open Questions

- "Quando acabar o de ler o código, eu quero que ele plote mais uma vez console.nome": a legenda junta `console.log` e `nome`; o código provavelmente é `console.log(nome)` fora do bloco.
- "Let string, onde é uma tipologia": "template literal"? A legenda não decide.
- A lição 01 anunciou a instalação de VS Code, Node e Git como aula 02; ou ela foi cortada ou ficou em outro módulo (há uma aula de ambiente no módulo de front-end: [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]).

## Raw quotes

- "literalmente é um espacinho na memória"
- "lá em CSS tudo é div, tudo é caixa, aqui praticamente tudo é objeto"
- "ele literalmente juntou uma na outra"
