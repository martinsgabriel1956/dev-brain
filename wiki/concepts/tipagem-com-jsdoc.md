---
type: concept
title: "Tipagem com JSDoc"
aliases: ["JSDoc types", "typescript sem typescript", "@typedef", "tipagem forte em javascript puro"]
date_created: 2026-07-21
date_updated: 2026-07-21
source_count: 1
tags: [javascript, jsdoc, tipagem, node-js, ferramental]
skill: tech-mentor-testing
status: draft
---

# Tipagem com JSDoc

Forma de ter autocomplete e alguma validação de tipos em **JavaScript puro**, sem precisar de TypeScript, usando comentários `@typedef`/`@param`/`@returns` que o TS Language Server (embutido em editores como o VS Code) já entende e valida.

## Definindo tipos

```js
/**
 * @typedef {Object} IncomingUser
 * @property {string} name
 * @property {string} email
 * @property {string} password
 */

/**
 * @typedef {Object} OutcomingUser
 * @property {string} name
 * @property {string} email
 */
```

## Anotando função

```js
/**
 * @param {IncomingUser} user
 * @returns {OutcomingUser}
 */
function parseUser(user) {
  return {
    name: user.name.toUpperCase(),
    email: user.email,
  };
}
```

Com o `@param` anotado, o editor oferece autocomplete de propriedades ao digitar `user.`. Com o `@returns` anotado, o editor sinaliza incompatibilidade se o valor retornado não bater com o formato declarado — mesmo sem nenhum passo de compilação de TypeScript.

## Onde usar

Funciona igual em arquivos de teste: importar os mesmos tipos e anotar a variável de entrada com `@type {IncomingUser}` dá autocomplete ao montar o objeto de teste, sem duplicar a definição do tipo.

## Trade-off frente a TypeScript

- **Ganha**: zero configuração de build/transpilação, funciona em qualquer projeto Node.js puro, tipos vivem como documentação inline.
- **Perde**: validação só em tempo de edição (via language server), não em tempo de build/CI — nada impede rodar código com tipo incompatível em produção se ninguém rodar um `tsc --checkJs` no pipeline.

## Relação com o resto do setup

Faz parte do mesmo pacote de ferramental descrito em [[wiki/concepts/setup-live-reload-debug-testes]] — o objetivo comum é reduzir o tempo entre escrever código e obter feedback, sem sair do editor.

## Key Sources

- [[wiki/sources/3-pilares-testes-automatizados-produtividade]]
