---
type: concept
title: "Módulos no Node.js (CommonJS e ESM)"
aliases: ["CommonJS", "CJS", "require", "module.exports", "ES Modules", "ESM", "import/export", "módulos do Node"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 4
tags: [nodejs, javascript, modulos, commonjs, esm, require, import, lang-dynamic]
skill: lang-dynamic
status: stub
---

# Módulos no Node.js (CommonJS e ESM)

Cada arquivo é um módulo com escopo próprio: o que ele não exporta, os outros não veem. Há três origens: arquivos do projeto (caminho relativo, `./util`), módulos nativos (`node:fs`, `node:http`, `node:os`) e pacotes instalados pelo npm (`express`). Ver [[wiki/concepts/gerenciador-de-pacotes]].

## Dois sistemas

| | CommonJS (CJS) | ES Modules (ESM) |
|---|---|---|
| Importar | `const x = require('./x')` | `import x from './x.js'` |
| Exportar | `module.exports = ...` / `exports.y = ...` | `export default ...` / `export const y` |
| Quando ativa | padrão em `.js` sem `"type"`; `.cjs` | `"type": "module"` no `package.json`; `.mjs` |
| Carregamento | síncrono, em tempo de execução | estático (analisável), assíncrono |
| Extensão | opcional (`.js`, `.json`, `.node`, `index.js`) | obrigatória em caminhos relativos |
| Extras | `__dirname`, `__filename` | `import.meta.dirname`, top-level `await` |

`[external]` https://nodejs.org/api/modules.html e https://nodejs.org/api/esm.html.

ESM é o padrão da linguagem e o que navegadores, Deno e bundlers entendem; habilita [[wiki/concepts/tree-shaking]] e `await` no topo ([[wiki/concepts/async-await]]). CJS ainda domina código legado e tutoriais antigos. Desde o Node 22.12/20.19, `require()` carrega ESM síncrono sem flag, o que facilita a migração `[skill: lang-dynamic]`.

## Como o CJS funciona por dentro

- **Module wrapper.** O Node embrulha cada arquivo em `function (exports, require, module, __filename, __dirname) { ... }`. Daí o escopo por arquivo e as variáveis "mágicas".
- **`exports` é atalho.** Começa apontando para `module.exports`. `exports.x = 1` funciona; `exports = {...}` não exporta nada; `module.exports = {...}` depois de `exports.x` descarta o `x`.
- **Cache.** O arquivo roda uma vez; outros `require` recebem o mesmo objeto (`require.cache`). Um módulo que exporta uma instância vira [[wiki/concepts/singleton-pattern|singleton]] de fato.
- **Ordem de resolução.** Nativo → caminho relativo/absoluto (tenta extensões e `index.js`) → `node_modules` subindo pelas pastas.

## Nativos com `node:`

`require('node:os')` / `import os from 'node:os'` deixa explícito que é nativo e impede que um pacote do npm com o mesmo nome seja carregado no lugar. Alguns módulos novos só existem com o prefixo (`node:test`, `node:sqlite`) `[skill: lang-dynamic]`.

## No JStack (aula 03)

Em [[wiki/sources/jstack-o-que-sao-modulos]], [[wiki/entities/mateus-silva]] apresenta os três tipos ("todos os arquivos JavaScript são módulos"), o erro `printName is not defined` → `is not a function` → funciona com `module.exports`, as duas formas de exportar vários valores (objeto com shorthand e `exports.x = ...`) e `require('os')`. É CommonJS, sem o nome e sem citar ESM.

Também em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: `module.exports` de uma promise e de objetos de funções.

## Aula 04: require('http')

Em [[wiki/sources/jstack-criando-o-servidor-http]], o primeiro módulo nativo em uso real: `const http = require('http')`, "é só passar o require e o nome do pacote, do módulo". Com prefixo, `require('node:http')`.

## Aula 06: require relativo ao arquivo

Em [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]], mover o código para `controllers/` quebra `require('./mocks/users')`; vira `../mocks/users`. O caminho do `require` é relativo ao arquivo que importa, não ao terminal. O `require('./controllers/userController')` para o arquivo `UserController.js` só funciona em sistemas de arquivos que ignoram maiúsculas.

## ES Modules no navegador (FrontPUSH, JavaScript aula 17)

Em [[wiki/sources/frontpush-modules-js-import-export-default]], [[wiki/entities/nasser|Násser]] usa ESM direto no navegador: `<script type="module">`, `export function` e `import { areaRetangulo } from "./retângulo.js"`, e depois um objeto como `export default` importado com nome livre. Diferenças em relação ao Node: o navegador exige servidor (o `file://` tem origem `null` e o `import` cai no CORS), `./` e extensão no caminho; o módulo tem escopo próprio, *strict mode* e `defer` implícito. `import * as nome` resolve o "não sei o nome da função" sem agrupar tudo num default, que atrapalha o [[wiki/concepts/tree-shaking]].

## Key sources

- [[wiki/sources/jstack-o-que-sao-modulos]]: três tipos de módulo; require, module.exports e exports; require('os')
- [[wiki/sources/jstack-criando-o-servidor-http]]: require('http') na prática
- [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]]: require relativo ao arquivo; maiúsculas no nome
- [[wiki/sources/frontpush-modules-js-import-export-default]]: FrontPUSH, JavaScript aula 17: ESM no navegador, type=module, named × default
