---
type: source
title: "Desestruturação: objetos, parâmetros e arrays com mousemove (FrontPUSH)"
aliases: ["FrontPUSH desestruturação", "módulo de JavaScript ES6, aula 18", "Desestruturação"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [javascript, desestruturacao, destructuring, objeto, array, parametro, mousemove, clientx, clienty, event-listener, react, curso, frontend]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/dev-brain/raw/frontpush-desestruturacao-objetos-arrays-mousemove.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Desestruturação (FrontPUSH)

## TL;DR

Aula 18 do módulo de JavaScript ES6 do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]] (pela sequência; não diz o nome). Cerca de 10 min sobre [[wiki/concepts/desestruturacao-javascript|desestruturação]], "muitíssimo utilizad[a]" em [[wiki/entities/react|React]] e [[wiki/entities/vue|Vue]]: "bater o olho e identificar, poxa, isso aqui é uma desestruturação".

- **Exemplo:** `document.documentElement.addEventListener("mousemove", mouseMove)`, e o `console.log(event)` mostra "o tanto de características" (`clientX`, `clientY`, `detail`, `layerX`, `offsetX`, `pageX`...). Ver [[wiki/concepts/event-listener-javascript]].
- **Sem desestruturar:** uma `const` por propriedade (`const clientX = event.clientX`); "10 características [...] 10 linhas".
- **Objeto:** `const { clientX, clientY } = event` "tira um pouco da verbosidade". Os nomes precisam ser os da propriedade.
- **Parâmetro:** como o `event` "passa aqui automático, porque é uma função de callback", dá para desestruturar "diretamente no argumento": `function mouseMove({ clientX, clientY })`.
- **Array:** `const [marca1, marca2, marca3, marca4] = carros` pega por posição (Volks, Fiat, BMW, Audi). "Objeto chaves, array, colchetes."
- Fecha dizendo que vale "não só para variáveis, mas também para funções", ligando a [[wiki/concepts/arrow-functions]].

## Key Claims

### Por que

- "Esse recurso aqui [...] é muito similar a quando a gente [...] escreve um código de maneira tradicional e quer reescrever ele de maneira mais simples ou mais direta."
- "Esse recurso aqui é muitíssimo utilizado quando a gente parte para frameworks como React ou Vue." Ver [[wiki/concepts/framework-web]].
- "É um conceito bem simples, mas é importante a gente vir aqui e trabalhar."

### O evento

- "Mostrar aqui no console a posição Y e X do meu mouse, quando eu estou movendo."
- "Um document e um documentElement, que é para poder ele executar sem ser em cima de algum outro elemento, a própria página." Ver [[wiki/concepts/dom]].
- "Vou colocar o evento de mousemove, e aí ele vai disparar uma função que eu vou chamar essa função de mouseMove." `function mouseMove(event)` recebe "o próprio evento para eu obter [...] as informações do evento". Remete às [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown|aulas de DOM]].
- `console.log(event)`: "ele está disparando um monte de números aqui do lado [...] aqui são todas as propriedades, métodos que estão inerentes a esse evento, só que eu quero dois específicos, que é o clientX e o clientY". Ver [[wiki/concepts/objetos-javascript]].
- Listagem do objeto: "clientX, [...] clientY, [...] detail, [...] layerX, o layerY, [...] offsetX, o offsetY, [...] pageX, o pageY".

### Sem e com desestruturação

- "Criar uma constante chamada clientX, onde eu vou pegar lá no evento e justamente pegar a informação clientX [...] posso colocar minúscula também." O mesmo para o Y, "e ao invés de plotar o evento, eu vou plotar apenas o x, o y".
- "Se eu extrair muitas características e ficar declarando, o meu código fica muito grande [...] eu teria 10 linhas só para poder extrair essas características."
- "Basicamente eu faço const, abro e fecho chaves e aí eu coloco o nome das características aqui direto."
- "Não são constantes, eu poderia muito bem colocar aqui eixoX [...] eixoY [...] aqui eu coloco o nome que eu quiser, nesse caso aqui, se eu for desestruturar, eu tenho que utilizar a propriedade, então no caso eu tenho que colocar clientX, clientY e aí ele recebe o evento."
- "Isso aqui é a chamada desestruturação, que tira um pouco da verbosidade nessas declarações."

### No parâmetro

- "Eu estou criando uma constante com essas variáveis que estão recebendo exatamente o mesmo nome da propriedade que existe no objeto event."
- "O event passa aqui automático, porque é uma função de callback, lembre-se disso [...] eu posso muito bem desestruturar isso aqui de maneira direta [...] diretamente no argumento." Ver [[wiki/concepts/callback-javascript]] e [[wiki/concepts/funcoes-javascript]].

### Array

- `const carros` com "Volks [...] Fiat, [...] BMW, [...] Audi". Ver [[wiki/concepts/array]].
- "Lembre-se, eu desestruturei um objeto utilizando chaves, sempre objeto chaves, array, colchetes."
- "Pegando aqui o array carros, passando o primeiro aqui para marca 1, criando uma constante chamada marca 1, pegando esse primeiro valor, marca 2 esse segundo valor." `marca1` dá Volks, `marca3` BMW, `marca4` Audi.

### Com funções

- "Vai ser comum vocês verem essa questão de [...] desestruturação, não só para variáveis, mas também para funções, lembre-se que quando a gente declara arrow functions [...] ao invés de receber um valor, um string [...] você pode muito bem declarar uma função."
- "Quando a gente estiver trabalhando com algumas frameworks, isso vai ser comum."

## Código reconstruído

Pela fala (a legenda não mostra a tela):

```javascript
document.documentElement.addEventListener("mousemove", mouseMove)

// 1. sem desestruturar
function mouseMove(event) {
  const clientX = event.clientX
  const clientY = event.clientY
  console.log(clientX, clientY)
}

// 2. desestruturando no corpo
function mouseMove(event) {
  const { clientX, clientY } = event
  console.log(clientX, clientY)
}

// 3. desestruturando no parâmetro
function mouseMove({ clientX, clientY }) {
  console.log(clientX, clientY)
}

// array
const carros = ["Volks", "Fiat", "BMW", "Audi"]
const [marca1, marca2, marca3, marca4] = carros
console.log(marca3) // BMW
```

## Entities

- [[wiki/entities/nasser]]: instrutor (pela sequência do módulo).
- [[wiki/entities/frontpush]]: curso; módulo de JavaScript ES6, aula 18.
- [[wiki/entities/react]], [[wiki/entities/vue]]: frameworks citados como motivo.
- [[wiki/entities/javascript]]: assunto da aula.

## Concepts

- [[wiki/concepts/desestruturacao-javascript]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/array]]
- [[wiki/concepts/event-listener-javascript]]
- [[wiki/concepts/callback-javascript]]
- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/arrow-functions]]
- [[wiki/concepts/dom]]
- [[wiki/concepts/propagacao-de-eventos-dom]]
- [[wiki/concepts/framework-web]]

## Precisões e tensões com a wiki

`⚠️` Sem arquivo de referência na skill lang-dynamic para desestruturação ou eventos de mouse; as precisões vêm do MDN (`[external]`, sem fetch nesta sessão, confiança alta).

- **Renomear exige dois-pontos.** "Não são constantes, eu poderia muito bem colocar aqui eixoX" vale para o nome da variável, mas na desestruturação de objeto ela só aceita outro nome com `const { clientX: eixoX, clientY: eixoY } = event`. `const { eixoX } = event` dá `undefined`, porque `event` não tem `eixoX`. A própria aula corrige em seguida ("eu tenho que utilizar a propriedade"), mas não mostra a sintaxe de renomear. Ver [[wiki/concepts/desestruturacao-javascript]].
- **"Desestruturação para funções" tem um exemplo melhor que o da aula.** A fala sobre arrow function ("ao invés de receber um valor [...] declarar uma função") descreve função atribuída a variável, não desestruturação. O caso que vai aparecer no React é `const [count, setCount] = useState(0)`: desestruturação de array em que o segundo item é uma função. E `const { useState } = React` tira uma função de um objeto. Ver [[wiki/entities/react]].
- **O nome do evento é `"mousemove"`, tudo minúsculo.** Nomes de evento diferenciam maiúsculas; `"mouseMove"` nunca dispararia. A função pode se chamar `mouseMove`. A legenda não mostra como ficou na tela.
- **As coordenadas têm referências diferentes.** `clientX/Y`: relativo à janela visível. `pageX/Y`: relativo ao documento, somando a rolagem. `offsetX/Y`: relativo ao elemento alvo. `screenX/Y`: relativo ao monitor. `layerX/Y` não é padrão. Copiar `pageX` "copia, cola" como se fosse o mesmo valor esconde isso.
- **`document.documentElement` é o `<html>`.** Para a página toda também servem `document` ou `window`; como o `mousemove` sobe por *bubbling*, qualquer um dos três recebe o evento de qualquer ponto ([[wiki/concepts/propagacao-de-eventos-dom]]).
- **`mousemove` dispara dezenas de vezes por segundo.** Para algo além de `console.log`, use `requestAnimationFrame` ou *throttle*, como já foi notado na [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown|aula 10]].
- **Array: posição, pulos, resto e padrão.** `const [primeira, , terceira] = carros` pula itens; `const [primeira, ...resto] = carros` junta o resto; `const [a = "nenhuma"] = []` usa valor padrão. "Marca 3 esse segundo valor" é lapso: `marca3` é o terceiro.
- **Desestruturar `undefined` lança erro.** `function mouseMove({ clientX })` chamada sem argumento dá `TypeError`; num callback de evento isso não acontece, porque o navegador sempre passa o evento.
- **Nomes sem espaço.** "Marca 1" no código é `marca1`.
- **Coincide com o resto da wiki:** a NLW #2 (Mayk e Diego) e o JStack usam as mesmas três formas (objeto, array, parâmetro); a NLW #2, dia 3, já mostrava rest e spread.
- **Positivos:** partir do jeito verboso para mostrar o ganho, o evento real como objeto a desestruturar, e "objeto chaves, array colchetes".

## Open Questions

- "Mais simples ou mais direta, mais escrevendo e tendo a mesma funcionalidade": provavelmente "menos escrevendo" (ficou literal no raw).
- O evento foi registrado como `"mousemove"` ou `"mouseMove"`? Como funcionou, deve ser o primeiro.
- A aula 17 (módulos) e esta usam `import { a } from` e `const { a } = obj` com a mesma cara: o curso vai explicar que o `import` não é desestruturação?

## Raw quotes

- "isso aqui é uma desestruturação, eu já sei o que está acontecendo"
- "sempre objeto chaves, array, colchetes"
- "tira um pouco da verbosidade nessas declarações"
