---
type: source
title: "Promises: resolve, reject, then e catch com XMLHttpRequest (FrontPUSH)"
aliases: ["FrontPUSH Promises", "módulo de JavaScript ES6, aula 15", "Promises"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [javascript, promise, resolve, reject, then, catch, pending, xmlhttprequest, assincrono, status-code, github-api, curso, frontend]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/dev-brain/raw/frontpush-promises-resolve-reject-then-catch.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Promises (FrontPUSH)

## TL;DR

Aula 15 do módulo de JavaScript ES6 do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]] (pela sequência; não diz o nome). Refaz o exemplo da [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate|aula 14]] (XHR contra a API do [[wiki/entities/github|GitHub]]) embrulhado numa [[wiki/concepts/promise-javascript|Promise]].

- **Ideia:** uma promessa "pode dar certo ou pode dar errado", e você faz uma coisa em cada caso: "essas duas bifurcações". `readyState` 4 "não significa que deu certo"; é preciso conferir o status 200.
- **Código:** `minhaPromise` é uma função que faz `return new Promise(function (resolve, reject) {...})`. Dentro, o XHR; se `status == 200`, `resolve(JSON.parse(XHR.responseText))`, senão `reject("erro")`.
- **Pending:** `const result = minhaPromise(); console.log(result)` mostra `Promise {<pending>}`, porque o log roda "imediatamente depois", antes de a requisição voltar. "Com esse exercício [...] a gente consegue entender um pouco mais da diferença de JavaScript síncrono e assíncrono." Ver [[wiki/concepts/javascript-assincrono]].
- **then/catch:** "uma cascata de possibilidades". O `resolve` levanta "uma bandeirinha verde" que "aciona o then"; o `reject`, "uma bandeirinha vermelha", e "será executado o catch".
- **Teste:** com a URL certa, o objeto aparece (Network: 200, 340 ms); com "uns caracteres a mais" na URL, cai no `catch`. Próxima aula: [[wiki/entities/axios|Axios]], "um pouquinho mais fácil".

## Key Claims

### Promessa e status

- "Quando a gente fala de promessas, ela pode dar certo ou pode dar errado [...] você faz alguma coisa quando uma promessa dá certo e [...] uma outra coisa quando a promessa dá errado."
- A requisição "demora um tempo, 200 milissegundos, 300 milissegundos".
- "Ready state, ou seja, estado de pronto, quando ele me volta 4 significa que ele está pronto para poder me devolver alguma resposta se deu certo ou se deu errado [...] lembre-se que o estado de pronto não significa que deu certo." Ver [[wiki/concepts/xmlhttprequest]].
- "Status de 200 é o status code de que deu tudo certo." Ver [[wiki/concepts/http-status-code]].
- No erro, "plotar o erro para você descobrir, para você debugar, ou simplesmente vai fazer outra requisição"; no sucesso, "emitir uma mensagem que deu certo".
- "Basicamente são funções que a gente vai encadear, vai cascatear [...] é uma cascata de possibilidades."

### new Promise, resolve e reject

- "Uma variável chamada minhaPromise [...] vou atribuir ela uma função [...] return new, onde ele vai devolver um objeto que é a própria promise, que é uma classe, onde dentro da promise eu tenho uma função."
- "Estou passando como parâmetro dela uma função básica que essa função tem duas variáveis, que é a resolve, e reject [...] isso aqui parece uma variável, mas também é uma função [...] é uma função que declara outra função, que declara outra função." Ver [[wiki/concepts/funcoes-javascript]] e [[wiki/concepts/callback-javascript]].
- "Resolver as coisas, ou seja, quando der certo, e reject quando der errado."
- Dentro: o XHR, `open`, `send`, `onreadystatechange`, e "mais um if onde eu vou acessar o objeto XHR, e ele vai me dar o status, se o status for igual a 200 [...] else, deu errado".
- "Aí sim agora que eu vou colocar a função resolve [...] o parse [...] do XHR.responseText." No `else`, `reject` com "uma mensagem de erro".
- "Você está vendo como é muito importante o entendimento de objetos, porque a gente está lidando aqui com uma função dentro da outra, com instanciamento de classes." Ver [[wiki/concepts/programacao-orientada-a-objetos]].

### Pending

- `result` recebe a chamada de `minhaPromise`, e o `console.log(result)` mostra `Promise {<pending>}`.
- "Nós inicializamos no background do navegador um JavaScript assíncrono, onde ele foi lá fazer a requisição [...] tem uma série de processos que acontecem no background."
- "Como aqui fora temos o JavaScript síncrono, a partir do momento que ele [...] mandou executar essa função aqui, ela foi para background [...] e imediatamente depois apresentou o result [...] o pending, então como foi instantaneamente, ele não deu tempo de literalmente retornar a promise o resultado." Ver [[wiki/concepts/event-loop-performance-js]].
- "Com o síncrono eu não sei quando vai dar certo, não sei exatamente qual o tempo que vai demorar essa requisição."

### then e catch

- "Dois métodos muito legais, que é o chamado then, onde eu posso escrever assim de forma de cascata [...] ele tem como argumento, o response [...] e nós temos aqui o .catch [...] onde ele recebe, por exemplo, o erro."
- "Se ela der resolve, imagine que ela vai estar tipo levantando uma bandeirinha para o sistema [...] uma bandeirinha verde [...] ela no sistema aciona o then."
- "Quando o status code, por exemplo, não for o 200 [...] ela vai levantar como se fosse uma bandeirinha vermelha [...] e automaticamente será executado o catch de maneira assíncrona."
- "Esse response é a resposta desse resolve, ou seja, ele vai devolver o JSON com o objeto."

### Teste

- Sucesso: "na nossa requisição já está voltando o objeto". Na Network: "status code 200 [...] o preview, o response [...] timing, foram 340 milissegundos de resposta". Ver [[wiki/concepts/debug-de-requisicao-http]].
- Erro: "trocar a URL do GitHub para algo que não existe [...] coloquei aqui uns caracteres a mais", e o `catch` mostra "erro na requisição tal, tal, tal".
- "A gente vai verificar, por exemplo, o axios [...] que é um pouquinho mais fácil de tratar tudo isso aqui."

## Código reconstruído

Pela fala (a legenda não mostra a tela; o usuário do GitHub não é dito):

```javascript
const minhaPromise = function () {
  return new Promise(function (resolve, reject) {
    const XHR = new XMLHttpRequest()
    XHR.open("GET", "https://api.github.com/users/<usuario>")
    XHR.send(null)

    XHR.onreadystatechange = function () {
      if (XHR.readyState == 4) {
        if (XHR.status == 200) {
          resolve(JSON.parse(XHR.responseText))
        } else {
          reject("erro na requisição")
        }
      }
    }
  })
}

const result = minhaPromise()
console.log(result) // Promise {<pending>}

minhaPromise()
  .then(function (response) {
    console.log(response)
  })
  .catch(function (erro) {
    console.log(erro)
  })
```

## Entities

- [[wiki/entities/nasser]]: instrutor (pela sequência do módulo).
- [[wiki/entities/frontpush]]: curso; módulo de JavaScript ES6, aula 15.
- [[wiki/entities/github]]: a API consultada.
- [[wiki/entities/axios]]: anunciado para a próxima aula.
- [[wiki/entities/javascript]]: assunto da aula.

## Concepts

- [[wiki/concepts/promise-javascript]]
- [[wiki/concepts/xmlhttprequest]]
- [[wiki/concepts/javascript-assincrono]]
- [[wiki/concepts/event-loop-performance-js]]
- [[wiki/concepts/callback-javascript]]
- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/http-status-code]]
- [[wiki/concepts/debug-de-requisicao-http]]
- [[wiki/concepts/json]]
- [[wiki/concepts/fetch-api]]
- [[wiki/concepts/async-await]]
- [[wiki/concepts/programacao-orientada-a-objetos]]

## Precisões e tensões com a wiki

`[skill: lang-dynamic]` Referência: `nodejs-core.md` (microtasks: os callbacks de Promise rodam antes dos timers e do I/O). Resto do MDN como `[external]`, sem fetch nesta sessão (confiança alta).

- **O executor não vai "para o background".** A função passada a `new Promise` roda na hora, de forma síncrona: cria o XHR, chama `open` e `send` e registra o handler. O que fica no fundo é só a requisição de rede, a cargo do navegador. O `resolve` é chamado depois, quando o `onreadystatechange` dispara. Ver [[wiki/concepts/javascript-assincrono]].
- **`resolve` e `reject` não são "uma função que declara outra função".** São funções que o próprio `Promise` cria e passa como argumentos para o executor: callbacks prontos, que você só chama. Ver [[wiki/concepts/callback-javascript]].
- **`console.log(result)` nunca mostra o valor.** Mesmo se o log rodasse depois da resposta, apareceria `Promise {<fulfilled>: {...}}`, o objeto Promise, e não o usuário. O valor só sai por `then` ou `await`; não é só que "não deu tempo". Coincide com o `Promise {<pending>}` da [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta|NLW #1, dia 2]].
- **Três estados, e uma promessa só termina uma vez.** *pending* → *fulfilled* ou *rejected*. Depois de assentada, chamadas seguintes de `resolve`/`reject` são ignoradas. Por isso o `if (status == 200)` precisa ficar dentro do `readyState == 4`; um `reject` nos estados 1 a 3 rejeitaria a promessa antes da resposta. Pela fala, o código está aninhado e certo.
- **A "cascata" real é o encadeamento de `then`.** Cada `then` devolve uma nova Promise com o valor que o callback retornar, e o próximo `then` recebe esse valor. O `catch` no fim pega erros de qualquer elo, inclusive exceções lançadas dentro de um `then`. A aula só mostra um `then` e um `catch`. Há ainda `finally`, e o `then` aceita um segundo argumento para a rejeição. Ver [[wiki/concepts/promise-javascript]].
- **A "bandeirinha" é uma boa imagem para a microtask.** `[skill: lang-dynamic]` Ao `resolve`, o callback do `then` entra na fila de microtasks e roda assim que a pilha esvazia, antes de timers e de novos eventos (`nodejs-core.md`: `nextTick → promise → timeout → immediate`).
- **Rejeite com `Error`.** `` reject(new Error(`HTTP ${XHR.status}`)) `` dá stack trace e a mensagem com o status (404 para o usuário inexistente). Uma string funciona, mas perde contexto. Falha de rede chega com `status` 0 e também cai no `else`.
- **Nome confuso: `response` × `Response`.** No `then` da aula, `response` já é o objeto do usuário, porque o `resolve` passou o JSON parseado. Com [[wiki/concepts/fetch-api|fetch]], o `then` recebe um objeto `Response`, e o JSON vem de `response.json()`, outra Promise.
- **O padrão tem nome: *promisificar*.** Embrulhar uma API de callback (XHR) numa Promise. O `fetch` já nasce devolvendo Promise, e o [[wiki/entities/axios|Axios]] faz esse embrulho por dentro.
- **Sem `catch`, a rejeição fica sem tratamento** (*unhandled rejection*) e o navegador mostra um erro no console. A aula põe o `catch`, que é o certo.
- **`async`/`await` é a mesma coisa com outra sintaxe**: `const user = await minhaPromise()` com `try/catch` ([[wiki/concepts/async-await]]).
- **Lapsos ficaram literais no raw.** "Do HTML, HTTP request" e "a classe do XHTML, HTTP request" são o `XMLHttpRequest`. "Cheito", entre response e timing na lista de abas, deve ser *Initiator* (inferência pela ordem das abas do Chrome).
- **Positivos:** `readyState` 4 ≠ sucesso, com o status conferido (corrige o atalho da aula 14); o `pending` como demonstração de síncrono × assíncrono; o teste do caminho de erro com uma URL quebrada.

## Open Questions

- Ele usa `==` ou `===` no `status`? A legenda diz "for igual a 200".
- A mensagem do `reject` era só "erro" e depois virou "erro na requisição tal, tal, tal"? A fala sugere que ele editou a string durante o teste.
- A aula de Axios vai reusar o `then`/`catch` daqui ou já passar para `async/await`?

## Raw quotes

- "o estado de pronto não significa que deu certo"
- "é uma cascata de possibilidades"
- "como se fosse uma bandeirinha verde [...] ela no sistema aciona o then"
