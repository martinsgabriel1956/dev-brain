---
type: source
title: "Modules JS: import, export, type module e export default (FrontPUSH)"
aliases: ["FrontPUSH Modules JS", "módulo de JavaScript ES6, aula 17", "Modules JS"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [javascript, es-modules, esm, import, export, export-default, type-module, live-server, modularizacao, curso, frontend]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/dev-brain/raw/frontpush-modules-js-import-export-default.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Modules JS (FrontPUSH)

## TL;DR

Aula 17 do módulo de JavaScript ES6 do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]] (diz o nome: "Ah, Násser, para que você está exportando ele como default?"; a legenda escreve "Nárcio"). Sai da sequência de requisições para os ES Modules: "importar e exportar arquivos JavaScript", base da "dinâmica que acontece muitíssimo em frameworks". Ver [[wiki/concepts/modulos-nodejs]].

- **Motivo:** `areaRetangulo` e `upperName` no mesmo arquivo "não é muito organizad[o]"; cada assunto vai para o seu arquivo (`retângulo.js`, `string.js`). Ver [[wiki/concepts/separation-of-concerns]].
- **Requisitos:** `<script type="module">` e o código "rodando em um servidorzinho", o Live Server do [[wiki/entities/vs-code|VS Code]].
- **Export nomeado:** `export` na frente das funções; `import { areaRetangulo } from './retângulo.js'`. Sem importar, `ReferenceError` ("a área retângulo não está definida"). Cada função nova precisa entrar nas chaves.
- **Objeto com export default:** como numa "biblioteca gigantesca" "você não vai adivinhar o nome da função", ele junta as funções num objeto `retangulo` e faz `export default retangulo`. No `import`, o nome é livre ("teste" funciona), mas "é bom que você tenha semântica".

## Key Claims

### Por que módulos

- "Basicamente é o conceito de importar e exportar arquivos JavaScript, onde suponha que você queira criar um arquivo só de string, de funções e tudo relacionado a string [...] e outro só de números."
- "Eu dou o export em cada um desses e dou o import nesse principal, onde eu posso utilizar todas as funções."
- "Tópico importantíssimo para a gente entender a dinâmica de frameworks." Ver [[wiki/concepts/framework-web]].
- `areaRetangulo(a, b)` com `return a * b` ("mais voltado para números ou então polígonos") e `upperName`, que devolve a string "com a função upperCase [...] em caixa alta". `areaRetangulo(2, 2)` dá 4. Ver [[wiki/concepts/funcoes-javascript]] e [[wiki/concepts/string]].
- "Em um mesmo arquivo eu estou tratando de funções que são respectivas ao retângulo, outra de string, então eu não consigo organizar da melhor forma o meu código." Ver [[wiki/concepts/coesao]].

### type="module" e servidor

- "Primeira coisa que a gente precisa saber para poder isso funcionar de fato é você colocar o atributo aqui chamado type="module"." Ver [[wiki/concepts/carregamento-de-scripts]].
- "O seu código precisa estar rodando em um servidorzinho [...] instalar o Live Server, que ele cria um servidorzinho [...] que é chamado Live Reload, onde quando a gente salva [...] ele automaticamente atualiza a nossa página." Ver [[wiki/concepts/cors]].

### Export e import nomeados

- `perimetroRetangulo(a, b)` com `(2 * a) + (2 * b)`: "vou até colocar entre parênteses para poder dar ênfase na multiplicação por mais que não seja necessário".
- Sem import, o console acusa "a referência erro, ou seja, a área retângulo não está definida".
- "Export na frente das funções e agora eu consigo dar o import [...] o VS Code já é inteligente que ele já leu o arquivo [...] quando eu aperto enter, ele já completa para mim e eu coloco from e aí o caminho do arquivo [...] eu faço ponto barra." Ver [[wiki/concepts/caminho-relativo]] e [[wiki/entities/vs-code]].
- O perímetro "também não está definido, porque eu não chamei ele aqui, então para poder chamar mais funções, eu preciso colocar aqui perímetro retângulo".

### Objeto e export default

- Com as funções nomeadas, "isso me obriga [...] que eu saiba exatamente o nome da função [...] agora vamos supor que você esteja com uma biblioteca gigantesca, isso aqui é praticamente impossível".
- "É muito comum que essas exportações aqui sejam feitas por objetos." Cria `const retangulo = { areaRetangulo, perimetroRetangulo }` ("eu declaro abrindo e fechando chaves"). Ver [[wiki/concepts/objetos-javascript]].
- "Em vez de dar o export nessas funções [...] dou um export do retângulo [...] e aí eu vou exportar ele como default."
- Uso: `retangulo.perimetro` dá 8 e `area` dá 4.
- "Às vezes eu não vou saber exatamente o nome do objeto [...] eu vou dar um nome totalmente aleatório, teste, e se eu chamar esse mesmo teste aqui, ele vai funcionar do mesmo jeito [...] Porque eu exportei ele como default."
- "É lógico que você não vai colocar teste [...] é bom que você tenha semântica no seu código [...] retângulo, rectangle."
- "Então, é isso aí, modularização de código JavaScript." Ver [[wiki/concepts/arquitetura-modular]].

## Código reconstruído

Pela fala (a legenda não mostra a tela; ver a tensão sobre os nomes das chaves abaixo):

```html
<script type="module" src="app.js"></script>
```

```javascript
// retângulo.js
export function areaRetangulo(a, b) {
  return a * b
}

export function perimetroRetangulo(a, b) {
  return (2 * a) + (2 * b)
}

// versão final: objeto como default
const retangulo = { areaRetangulo, perimetroRetangulo }
export default retangulo

// string.js
export function upperName(nome) {
  return nome.toUpperCase()
}

// app.js
import { upperName } from "./string.js"
import retangulo from "./retângulo.js" // o nome aqui é livre (default)

console.log(upperName("teste")) // TESTE
```

## Entities

- [[wiki/entities/nasser]]: instrutor (diz o nome).
- [[wiki/entities/frontpush]]: curso; módulo de JavaScript ES6, aula 17.
- [[wiki/entities/vs-code]]: autocomplete do import e extensão Live Server.
- [[wiki/entities/javascript]]: assunto da aula.

## Concepts

- [[wiki/concepts/modulos-nodejs]]
- [[wiki/concepts/carregamento-de-scripts]]
- [[wiki/concepts/cors]]
- [[wiki/concepts/caminho-relativo]]
- [[wiki/concepts/tree-shaking]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/string]]
- [[wiki/concepts/separation-of-concerns]]
- [[wiki/concepts/coesao]]
- [[wiki/concepts/arquitetura-modular]]
- [[wiki/concepts/framework-web]]

## Precisões e tensões com a wiki

`[skill: lang-dynamic]` Referência: `typescript-core.md` (ESM × CommonJS, `export default` e `export const`, interop). Comportamento no navegador pelo MDN e pela especificação HTML (`[external]`, sem fetch nesta sessão, confiança alta).

- **Por que precisa de servidor.** Scripts `type="module"` são buscados com as regras de [[wiki/concepts/cors]]. Aberto por `file://`, a página tem origem `null` e o navegador bloqueia o `import`. O Live Server serve por `http://127.0.0.1:5500`. "Live Reload" é o recarregamento automático, um recurso do Live Server, não o nome do servidor.
- **`type="module"` muda mais do que liberar o `import`.** O script fica com escopo próprio (as funções não viram globais no `window`), roda em *strict mode* e é adiado como `defer` por padrão. Um módulo é avaliado uma vez só, mesmo importado por vários arquivos. Ver [[wiki/concepts/carregamento-de-scripts]].
- **"Não sei o nome" se resolve sem default.** `import * as retangulo from "./retângulo.js"` junta todos os exports nomeados num objeto, com autocomplete, e mantém os nomes. O default com um objeto agrupando funções derrota o [[wiki/concepts/tree-shaking]]: o bundler não consegue descartar a função que ninguém usa. E numa biblioteca grande você descobre os nomes pela documentação ou pelo autocomplete do editor, que funciona com os exports nomeados (a própria aula mostra o VS Code completando `areaRetangulo`).
- **O nome livre do default é faca de dois gumes.** Cada arquivo pode chamar o mesmo módulo de um jeito, e renomear no editor não acompanha. Por isso muitos guias de estilo preferem exports nomeados. Os dois convivem: um módulo pode ter um `default` e vários nomeados.
- **`retangulo.perimetro` não existiria com o shorthand.** `{ areaRetangulo, perimetroRetangulo }` cria as chaves `areaRetangulo` e `perimetroRetangulo`; `retangulo.perimetro` daria `undefined` e `retangulo.perimetro(2, 2)` um `TypeError`. Como funcionou (8 e 4), o objeto deve ter chaves renomeadas (`{ area: areaRetangulo, perimetro: perimetroRetangulo }`) ou a fala encurtou os nomes (inferência; a legenda não mostra a tela).
- **O caminho precisa de `./` e da extensão no navegador.** `"./retângulo.js"` está certo; `"retângulo"` sem extensão funciona em bundler e no CommonJS, não no navegador nem no ESM do Node ([[wiki/concepts/modulos-nodejs]]). Nome de arquivo com acento funciona, mas complica URL, terminal e servidores *case-sensitive*; `retangulo.js` evita isso ([[wiki/concepts/caminho-relativo]]).
- **O `ReferenceError` vem da mudança de arquivo, não da falta de `export`.** As funções sumiram do `app.js`; só `export` no outro arquivo não basta, é o `import` que traz o nome para o escopo.
- **Bindings importados são somente leitura e "vivos":** `areaRetangulo = ...` no `app.js` lança erro, e se o módulo de origem mudar a variável exportada, quem importou vê o novo valor.
- **"A função upperCase"** é o método `toUpperCase()` de string.
- **Mesmo mecanismo nos frameworks e no Node.** No React cada componente é `export default function Componente`. No Node, o JStack usou CommonJS (`require`/`module.exports`) na [[wiki/sources/jstack-o-que-sao-modulos|aula de módulos]]; os dois sistemas estão comparados em [[wiki/concepts/modulos-nodejs]]. No CSS, a ideia correspondente foi o `@import` com partials do [[wiki/sources/frontpush-import-e-partials-sass|Sass]].
- **Positivos:** separar por assunto (coesão), o `ReferenceError` mostrando o escopo do módulo, `./` e extensão no caminho, e o recado de dar nomes semânticos ao import default.

## Open Questions

- Há trechos sem legenda: 11 s (00:05:12–00:05:23) antes de "Export na frente das funções", 10 s (00:06:41–00:06:52) antes de "As funções, isso me obriga" e 9 s (00:10:30–00:10:39) antes do fecho. Na segunda, a frase começa no meio; ele provavelmente diz que exportar função por função obriga a saber os nomes.
- As chaves do objeto `retangulo` eram `area`/`perimetro` ou os nomes completos?
- O Axios por CDN da [[wiki/sources/frontpush-axios-cdn-get-then-encapsulamento-xhr|aula 16]] continua global; o curso vai importá-lo como módulo quando chegar ao npm?

## Raw quotes

- "importar e exportar arquivos JavaScript"
- "você não vai adivinhar o nome da função"
- "é bom que você tenha semântica no seu código"
