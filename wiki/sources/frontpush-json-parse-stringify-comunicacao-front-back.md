---
type: source
title: "JSON: linguagem unificada entre front-end e back-end, parse e stringify (FrontPUSH)"
aliases: ["FrontPUSH JSON", "módulo de JavaScript ES6, aula 11", "JSON"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [javascript, json, json-parse, json-stringify, serializacao, api, front-end, back-end, cliente-servidor, javascript-assincrono, curso, frontend]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/dev-brain/raw/frontpush-json-parse-stringify-comunicacao-front-back.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# JSON (FrontPUSH)

## TL;DR

Aula 11 do módulo de JavaScript ES6 do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]] (pela sequência; não diz o nome). Abre a parte de "JavaScript assíncrono" com um "pequeno e importante parênteses": o [[wiki/concepts/json|JSON]] e o papel dele entre front-end e back-end.

- **Front × back:** o back-end cuida das "regras de negócio para com o banco de dados"; o front-end "requisita ou passa os valores". Exemplos: a página de produto do e-commerce (o ID vai na URL, o back consulta o banco e devolve) e o cadastro de usuário (o front "empacota" o formulário e manda). Ver [[wiki/concepts/arquitetura-cliente-servidor]].
- **Linguagem unificada:** a troca é "por meio de uma API" e de JSON. Analogia: se o mundo todo aprendesse inglês, todos se comunicariam; o JSON faz isso entre front e back, "independente da linguagem" (Node, PHP).
- **Sintaxe** (`produto.json`): array de objetos; chaves e strings "sempre" com aspas duplas (aspas simples dão erro no VS Code); sem vírgula no último item; vírgula entre objetos.
- **Valores:** número, string, booleano (`USB-C: true`), objeto aninhado (`fabricante: { cidade, país }`) e array. Chave repetida gera warning.
- **`JSON.parse`** transforma "o texto JSON em objeto" manipulável; **`JSON.stringify`** faz o contrário. Demo: colar o JSON numa linha dentro do `parse` e `console.log`; depois `stringify` de um objeto `caneta`.
- Próximas aulas: API e requisição HTTP, para buscar o JSON "via HTTP" em vez de copiar e colar.

## Key Claims

### Front-end, back-end e a troca de dados

- "O back-end é aquela parte do código onde faz as requisições, organização das regras de negócio para com o banco de dados, e o front-end é quem requisita ou passa os valores para o back-end conversar com o banco de dados." Ver [[wiki/concepts/regra-de-negocio]].
- E-commerce: "lá na URL [...] passa um monte de informações lá, inclusive, por exemplo, o ID do produto [...] o serial number", para que a página "requisite aquele produto específico para o back-end", que consulta o banco e "joga para o front-end na tela". Ver [[wiki/concepts/query-string]].
- Cadastro: "eu pego as informações que você colocou naquele formulário, empacoto e mando para o back-end".
- "Por meio de uma API e por meio do quê? Por meio de arquivos de linguagem unificada [...] que é o JSON." Ver [[wiki/concepts/api-rest]] e [[wiki/concepts/requisicao-http]].

### A analogia do inglês e o nome

- "Vamos supor que em todo o mundo seja obrigado todos a aprender inglês [...] todos conseguem se comunicar, independente de qual país ele seja, a mesma coisa é o JSON nesse papel."
- "Por mais que o nome seja JSON e o J seja de JavaScript, ele é uma linguagem unificada que pode ser utilizada em qualquer linguagem." O back-end "pode ser Node, que é JavaScript, ou pode ser, por exemplo, PHP". Ver [[wiki/entities/nodejs]].
- "JavaScript Object Notation, ou seja, uma anotação de objeto [...] ele se assemelha muito" a um objeto: "um formato de organização de dados composto por um conjunto de chave e valor [...] como se fosse um atributo e um determinado valor". Ver [[wiki/concepts/objetos-javascript]].

### Sintaxe

- "Você pode abrir um colchete [...] muito parecida com arrays e eu posso colocar [...] objetos aqui dentro, lembrando que objeto é sempre com chaves."
- "As propriedades, mais uma vez, precisam ser em aspas duplas, se colocar em aspas simples, vai dar erro [...] o próprio VS Code já mostra." O mesmo vale para valores string. Ver [[wiki/entities/vs-code]].
- "O último item [...] dentro do JSON, ele nunca pode ter vírgula." A vírgula separa um objeto do outro: Notebook Dell (ID 1, gamer, 5 no estoque) e Notebook Acer (ID 2, gamer, 10).
- "Aqui eu posso colocar as descrições que eu quiser, seja uma configuração de input, uma configuração de socket, de API."

### Tipos de valor

- Numéricos, string e "valores booleanos, então eu posso colocar se ele tem USB-C [...] true ou false". Ver [[wiki/concepts/tipos-primitivos-javascript]].
- "Ele também pode carregar um objeto dentro do outro": `fabricante` com cidade (Brasília) e país (Brasil).
- Array: copiou para `fabricante 2` "porque você viu que ele deu um warning, quando eu tenho a mesma característica", trocou chaves por colchetes, e "o array é direto no valor, um array de valores", sem par atributo/valor. "Isso aqui é só porque eu não tive um exemplo melhor."

### O objeto JSON

- "O objeto é simplesmente JSON em maiúsculo, onde nós temos [...] dois métodos principais."
- `parse`: "transforma o texto, isso aqui é uma string, por mais que ela tenha um formato [...] em objeto [...] manipulável para poder acessar os atributos, adicionar métodos".
- `stringify`: "justamente ao contrário, é quando eu quero transformar um objeto que eu tenho aqui dentro do JavaScript [...] em JSON".
- Demo do `parse`: copia o JSON para dentro das aspas; "é muito importante que ele esteja [...] em uma linha, ele não vai pegar essas quebras de linha". O console mostra o objeto com id 1, modelo gamer, Notebook Dell, quantidade 5.
- "A gente não vai utilizar esse método aqui, copiando e colando, porque geralmente os arquivos JSON são muito grandes." A próxima etapa é "API e requisição HTTP". Ver [[wiki/concepts/fetch-api]].
- Demo do `stringify`: objeto `caneta` (cor azul, formato triangular, tipo "caneta de desenho"), `JSON.stringify(caneta)` e `console.log` da "string JSON".

## Entities

- [[wiki/entities/nasser]]: instrutor (pela sequência do módulo).
- [[wiki/entities/frontpush]]: curso; módulo de JavaScript ES6, aula 11.
- [[wiki/entities/javascript]]: assunto da aula.
- [[wiki/entities/nodejs]]: exemplo de back-end em JavaScript.
- [[wiki/entities/vs-code]]: o editor que acusa o erro de aspas simples.

## Concepts

- [[wiki/concepts/json]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/tipos-primitivos-javascript]]
- [[wiki/concepts/arquitetura-cliente-servidor]]
- [[wiki/concepts/api-rest]]
- [[wiki/concepts/requisicao-http]]
- [[wiki/concepts/fetch-api]]
- [[wiki/concepts/query-string]]
- [[wiki/concepts/regra-de-negocio]]
- [[wiki/concepts/xml-extensible-markup-language]]
- [[wiki/concepts/promise-javascript]]

## Precisões e tensões com a wiki

`[skill: lang-dynamic]` A referência `nodejs-patterns-runtime.md` cobre serialização (BigInt, Date, Decimal); o resto vem da RFC 8259 e do MDN (`[external]`, sem fetch nesta sessão, confiança alta).

- **JSON não é "linguagem de marcação".** É um formato de dados em texto (RFC 8259, ECMA-404). Marcação é o que HTML e [[wiki/concepts/xml-extensible-markup-language|XML]] fazem: anotar um texto com tags. "Linguagem unificada" também exagera: é um formato de intercâmbio que quase toda linguagem lê por biblioteca, não uma linguagem que "todas entendem" nativamente.
- **Lapsos de fala ficaram literais no raw.** "Tem que ser colocado por chaves duplas" e "não funciona com aspas duplas" querem dizer o contrário (aspas duplas obrigatórias, aspas simples proibidas); o resto da aula confirma. Mais adiante, "como é um objeto, eu tenho que simplesmente passar o valor" fala do array.
- **Os seis tipos de valor:** string, número, booleano, `null`, objeto e array. A aula esquece o `null`. `[external]` Não entram `undefined`, funções, `Symbol`, `NaN`/`Infinity` (viram `null`) nem comentários. `Date` vira string ISO, e `BigInt` lança `TypeError` (`[skill: lang-dynamic]`, `nodejs-patterns-runtime.md`). Ver [[wiki/concepts/tipos-primitivos-javascript]].
- **O `parse` não "adiciona métodos".** O resultado é um objeto de dados puro; `stringify` descarta funções. Para métodos, passa-se o resultado a uma classe ou fábrica.
- **"Em uma linha" não é regra do JSON.** Quebras de linha entre tokens são espaço em branco válido e o `JSON.parse` aceita. O erro do vídeo é do JavaScript: uma string com aspas `'...'` ou `"..."` não pode quebrar linha. Uma template literal (`` `...` ``) aceita o JSON formatado. Ver [[wiki/concepts/template-literals]].
- **`const JSON = JSON.parse(...)` quebraria.** A legenda diz "constante chamada JSON", mas não mostra maiúsculas. Com esse nome a linha lançaria `ReferenceError` (a constante sombreia o global e ainda está na TDZ), e o `JSON.stringify` seguinte também falharia. Como a demo funciona, o nome na tela é quase certamente `json` minúsculo (inferência; ficou literal no raw).
- **Chave duplicada é só warning.** A RFC diz que os nomes "SHOULD be unique"; o `JSON.parse` aceita e fica com o último valor. O VS Code avisa, não bloqueia.
- **O exemplo do e-commerce mistura URL e corpo.** O ID do produto na URL é path ou [[wiki/concepts/query-string]]; o JSON aparece na resposta do back-end e no corpo do cadastro (`POST` com `Content-Type: application/json`). Ver [[wiki/concepts/requisicao-http]].
- **Arquivo `.json` × texto JSON.** O `produto.json` serve de exemplo, mas numa API o JSON trafega como corpo HTTP, sem arquivo. "Transformar esse objeto em JSON [...] em um arquivo JSON" quer dizer em texto; gravar arquivo seria outra etapa (`fs.writeFile` no Node).
- **Ainda não é assíncrono.** `parse` e `stringify` são síncronos. A ligação com "JavaScript assíncrono" vem na próxima aula: `fetch` devolve uma [[wiki/concepts/promise-javascript|Promise]], e `response.json()` faz o parse do corpo ([[wiki/concepts/fetch-api]]).
- **Sem vírgula final e chaves com aspas** coincide com a [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy|NLW #2, dia 2]] e a [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy|NLW #2, dia 4]]. No objeto literal do JavaScript, as duas coisas são permitidas ([[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this|aula 05]]).
- **Positivos:** `parse`/`stringify` como par inverso, o formato independente da linguagem do back-end, aninhamento de objeto e array, e a promessa de buscar por HTTP em vez de colar à mão.

## Open Questions

- "Arquivos de linguagem unificada a nascer" não faz sentido; pode ser "nascida" (do JavaScript) ou ruído. Ficou literal.
- O `stringify` sem `null, 2` sai numa linha só; a aula não mostra a indentação (`JSON.stringify(caneta, null, 2)`).
- "Configuração de input, [...] socket, [...] API" fica sem exemplo real; o caso mais próximo na wiki é o [[wiki/concepts/package-json]].
- Na demo do `stringify` ele "comenta esse outro console", mas a legenda não diz se o `console.log` do `parse` volta depois.

## Raw quotes

- "a mesma coisa é o JSON nesse papel"
- "o último item não pode ter vírgula"
- "ele transforma o texto JSON em objeto"
