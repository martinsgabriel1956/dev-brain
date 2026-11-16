---
type: source
title: "JStack, aula 03: o que são módulos no Node.js"
aliases: ["JStack aula 03", "módulos no Node", "require e module.exports"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [nodejs, javascript, modulos, commonjs, require, module-exports, exports, esm, npm, modulos-nativos, os, desestruturacao, shorthand-property, arrow-function, vs-code, jstack, iniciante]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/jstack-o-que-sao-modulos.md"
source_url: ""
author: "Mateus Silva (inferido)"
date_published: ""
date_ingested: 2026-11-16
---

# JStack, aula 03: o que são módulos no Node.js

## TL;DR

Terceira aula (cerca de 10 min) do [[wiki/entities/jstack]], com [[wiki/entities/mateus-silva]] (autoria quase certa: o exemplo imprime "Mateus Silva"). Primeira aula com código. Ela cobre:

1. **Ambiente.** Pasta `Modules`, `code .` para abrir no [[wiki/entities/vs-code|VS Code]] (se não funcionar, "Install code command" pela command palette e reabrir o terminal); `node index.js` roda um arquivo, e a extensão pode ser omitida.
2. **Três tipos de módulo.** "Módulos são conjuntos de código, ponto." Os que a gente cria ("todos os arquivos JavaScript são módulos"), os nativos (`http`, `os`, `dns`, `v8`) e os pacotes do npm (adiados para o próximo capítulo). Ver [[wiki/concepts/modulos-nodejs]].
3. **`require` e `module.exports`.** Chamar `printName` em outro arquivo dá `printName is not defined`; com `require('./printName')` vira `is not a function`; só funciona depois de `module.exports = printName`. O `require` serve "pra importar todos os tipos de módulos".
4. **Exportar mais de um dado.** Um objeto com *shorthand* (`module.exports = { printName, lastName }`), acessado como `modulo.printName` ou por [[wiki/concepts/desestruturacao-javascript|desestruturação]]; ou `exports.lastName = 'Silva'` e `exports.printName = (name) => ...` direto na declaração.
5. **Módulo nativo.** `const os = require('os')` sem caminho relativo; `os.type` imprime `Darwin` no macOS.

A aula ensina CommonJS sem dizer o nome nem citar o ESM (`import`/`export`), hoje o padrão da linguagem e suportado pelo Node. Também não avisa da armadilha de misturar `exports.x` com `module.exports = {...}`. Ver "Tensões e precisões".

## Key Claims

### Ambiente

- **Abrir no VS Code.** "Comando code e eu passo o ponto aqui pra indicar que eu quero abrir a pasta que eu tô no momento." Se o comando não existir: command palette ("command shift P no Mac, control shift P no Windows e no Linux"), "install code", e "você fecha o terminal, abre de novo" para recarregar as configurações. Usa o terminal integrado "pra gente não precisar ficar trocando de janela".
- **Executar.** "A gente só precisa executar o comando Node e a gente passa pra ele qual é o caminho até o arquivo": `node index.js` imprime `hello world`. "A gente também consegue omitir a extensão", mas "eu prefiro deixar sempre com a extensão, porque fica mais claro". Ver [[wiki/entities/nodejs]].

### O que são módulos e os três tipos

- **Definição.** "Módulos são conjuntos de código, ponto. Nem ponto e vírgula, é ponto", "que a gente consegue ou não reutilizar".
- **1. Os que a gente cria.** "O mais comum e o que a gente vai mais usar." Em Caps Lock: "Dentro do Node, todos os arquivos JavaScript são módulos": `index.js` é um, `abc.js` seria outro.
- **2. Nativos.** "Já vêm dentro do próprio Node. A gente não precisa criar nada, a gente só importa eles." O `http` será usado "a partir da próxima aula pra criar um servidor HTTP"; há módulos "de sistema operacional, de DNS, do V8".
- **3. Pacotes do npm.** "O NPM é o Node Package Manager", "basicamente um lugar pra gente conseguir publicar esses módulos que a gente cria [...] com a comunidade, e aí todo mundo consegue fazer a instalação deles". Fica "em Standby" até o próximo capítulo, que começa a usar dependências externas. Ver [[wiki/concepts/gerenciador-de-pacotes]].
- **"Capítulo" × "módulo".** Ele evita dizer "módulo do curso" para não confundir com "módulo do Node".

### require e module.exports

- **Escopo por arquivo.** Chamar `printName('Mateus')` no `index.js` dá `printName is not defined`, porque "o index ele não consegue enxergar o que tem dentro do meu printName".
- **`require`.** "É exatamente essa função que a gente usa pra importar todos os tipos de módulos", seja arquivo próprio, nativo ou do npm.
- **Caminho relativo e extensão.** Para os próprios módulos, "a gente precisa passar o caminho relativo" (`./printName`), e "a gente não precisa pôr o .js".
- **Guardar numa constante.** "A gente precisa salvar esse módulo dentro de uma constante": `const printName = require('./printName')`.
- **Exportar.** Sem export, o erro muda para `printName is not a function`: "a gente precisa dizer pro Node quais informações a gente quer que sejam acessíveis de outros módulos". Com `module.exports = printName`, imprime "Mateus".

### Exportar mais de um dado

- **Objeto com shorthand.** `const lastName = 'Silva'` e `module.exports = { printName, lastName }`; "isso aqui é a short syntax do JavaScript": em vez de `lastName: lastName`, "quando o nome da propriedade é o mesmo nome da variável, a gente omite".
- **Qualquer valor.** "Esse module.exports pode ser qualquer tipo de dado": função, variável, objeto, array, string, número.
- **Acessar.** Com o objeto, o import antigo quebra; ele renomeia para `módulo` e usa `módulo.printName(...)` com template string, imprimindo "Mateus Silva". Ou desestrutura: `const { printName, lastName } = require('./printName')`. Ver [[wiki/concepts/desestruturacao-javascript]].
- **Segunda forma.** "Exportar no momento em que a gente tá criando": `exports.lastName = 'Silva'` e `exports.printName = (name) => ...`, "um pouco mais enxuto" com arrow function. Ver [[wiki/concepts/funcoes-javascript]].

### Módulos nativos

- **Sem caminho.** `const os = require('os')` ("de operational system"); "no caso dos módulos do node a gente não passa o caminho relativo [...] até porque a gente nem sabe onde é que estão esses módulos de verdade".
- **IntelliSense.** `os.` lista os métodos; `console.log(os.type...)` e `node index` mostram "darwin, [...] que no caso é o do mac os".
- **Fecho.** O objetivo era apresentar "o tal do require que a gente vai usar bastante, o que que é o module exports, o exports, enfim, todo esse paranauê".

## Tensões e precisões

- **Isso é CommonJS, e o ESM ficou de fora.** `require`/`module.exports` é o sistema CommonJS, original do Node. O padrão da linguagem é o ESM (`import`/`export`), suportado no Node com `"type": "module"` no `package.json` ou arquivos `.mjs` `[external]` https://nodejs.org/api/esm.html. Desde o Node 22.12/20.19 o `require()` também carrega ESM síncrono sem flag `[skill: lang-dynamic]`. O "require [...] pra importar todos os tipos de módulos" vale só dentro de CJS. Ver [[wiki/concepts/modulos-nodejs]].
- **Extensão opcional só no CJS.** O `require` tenta `.js`, `.json` e `.node` e procura `index.js` em pastas. No ESM o especificador relativo precisa da extensão completa (`./printName.js`) `[external]` https://nodejs.org/api/esm.html#mandatory-file-extensions.
- **Por que `printName is not defined`.** O Node embrulha cada arquivo CJS numa função `(exports, require, module, __filename, __dirname) => {...}`. Por isso cada arquivo tem escopo próprio, e por isso `exports` e `require` "existem" sem import `[external]` https://nodejs.org/api/modules.html#the-module-wrapper.
- **`exports` × `module.exports`.** `exports` é só uma referência inicial a `module.exports`. Reatribuir `exports = {...}` não exporta nada, e fazer `module.exports = {...}` depois de `exports.x = ...` descarta o `x` `[external]` https://nodejs.org/api/modules.html#exports-shortcut. A aula mostra as duas formas sem esse aviso.
- **Não é preciso guardar numa constante.** `require('./arquivo')` sozinho executa o módulo pelos efeitos colaterais (registrar algo, ler config).
- **Cache.** O módulo roda uma vez; `require`s seguintes devolvem o mesmo objeto. Por isso um módulo que exporta uma instância funciona como [[wiki/concepts/singleton-pattern|singleton]].
- **Nativos com prefixo `node:`.** Hoje se escreve `require('node:os')` ou `import os from 'node:os'`: deixa claro que é nativo, não pode ser sequestrado por um pacote do npm com o mesmo nome, e alguns módulos novos (`node:test`, `node:sqlite`) só existem com o prefixo `[skill: lang-dynamic]`. Eles ficam compilados dentro do binário do Node, daí "a gente nem sabe onde estão".
- **`os.type` é função.** `console.log(os.type)` imprime `[Function: type]`; o que imprime `Darwin` é `os.type()` (com D maiúsculo) `[external]` https://nodejs.org/api/os.html#ostype. Pela saída, a chamada provavelmente tinha os parênteses.
- **npm.** Publica *pacotes* (pasta com `package.json`), não arquivos soltos. O próprio npm diz que o nome não é sigla oficial, embora "Node Package Manager" seja a leitura comum. E "operational system" é *operating system*.
- **"Install code command" é coisa do macOS.** No Windows e no Linux o instalador do VS Code já põe o `code` no PATH.

## Entities

- [[wiki/entities/jstack]]: o curso
- [[wiki/entities/mateus-silva]]: instrutor; o exemplo imprime "Mateus Silva"
- [[wiki/entities/nodejs]]: `node index.js`, require, módulos nativos
- [[wiki/entities/vs-code]]: `code .`, terminal integrado, IntelliSense

## Concepts

- [[wiki/concepts/modulos-nodejs]]: CommonJS, require, module.exports, ESM
- [[wiki/concepts/gerenciador-de-pacotes]]: npm
- [[wiki/concepts/desestruturacao-javascript]]: `const { printName } = require(...)`
- [[wiki/concepts/funcoes-javascript]]: arrow function em `exports.printName`
- [[wiki/concepts/singleton-pattern]]: cache de módulos
- [[wiki/concepts/tree-shaking]]: por que ESM e não CJS
- [[wiki/concepts/async-await]]: top-level await só em ESM

## Open Questions

- O curso migra para ESM em algum momento, ou segue em CommonJS?
- A próxima aula (servidor com `http`) vai usar `require('http')` ou `node:http`?

## Raw quotes

> "Módulos são conjuntos de código, ponto. Nem ponto e vírgula, é ponto, tá?"

> "Dentro do Node, todos os arquivos JavaScript são módulos."

> "A gente precisa dizer pro Node quais informações a gente quer que sejam acessíveis de outros módulos."
