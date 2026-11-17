---
type: source
title: "Introdução ao módulo de JavaScript ES6+: o que é JavaScript e o que é ES6 (FrontPUSH)"
aliases: ["FrontPUSH introdução JavaScript", "módulo de JavaScript ES6, aula 01", "O que é JavaScript e ES6+"]
date_created: 2026-11-16
date_updated: 2026-11-17
source_count: 0
tags: [javascript, ecmascript, es6, es2015, jquery, babel, webpack, front-end, back-end, react, react-native, curso, frontend]
skill: lang-dynamic
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-introducao-javascript-es6-ecmascript.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Introdução ao módulo de JavaScript ES6+ (FrontPUSH)

## TL;DR

Aula 01 do módulo de JavaScript ES6 do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]] (ele se chama pelo nome: "Násser, como assim"). Aula sem código: para quem é o módulo, o que ele cobre, o que é ES6+ e o que é [[wiki/entities/javascript|JavaScript]].

- **Para quem:** iniciante absoluto ou quem quer "dar uma repaginada". Serve para "nivelar" antes de um framework, como o [[wiki/entities/react]]. Não é um curso "completaço": cobre o básico, "um basicinho ali", que ele acha "super necessário".
- **Pré-requisito:** HTML e CSS já praticados, porque o JavaScript "vai justamente manipular esses dois".
- **Próxima aula:** instalar [[wiki/entities/vs-code]], [[wiki/entities/nodejs|Node]] e [[wiki/concepts/git|Git]].
- **Conteúdo:** variáveis, condicionais, repetição, funções, objetos, arrays e loops ([[wiki/concepts/logica-de-programacao]]); [[wiki/concepts/dom]] e eventos; JavaScript assíncrono e a conversa do front-end com o back-end ([[wiki/concepts/async-await]]).
- **ES6+:** ES vem de [[wiki/concepts/ecmascript|ECMAScript]], a "organização" que "gerencia" o JavaScript; as versões seguem o ano: ES6 = 2015, ES7 = 2016, ES8 = 2017. Antes do ES6 o JavaScript era "um pouco arcaico", e por isso o [[wiki/concepts/jquery|jQuery]] fazia sucesso; hoje o JS nativo "já faz o que ele fazia".
- **O que vem:** Webpack, Babel ([[wiki/concepts/transpilador]]), arrow functions ([[wiki/concepts/funcoes-javascript]]) e async/await, "a partir do ES6".
- **O que é JavaScript:** linguagem de programação, ao contrário do HTML (marcação, conteúdo; [[wiki/concepts/html-hipertexto]]) e do [[wiki/concepts/css]] (estilo), que "não têm muita inteligência". É o que torna a página "dinâmica". Exemplo: no e-commerce, clicar num produto abre a página dele com preço, parcelas e fotos maiores.
- **Front-end × back-end:** front é a parte em contato com o usuário; back é "aquele que vai lá no banco de dados" ([[wiki/concepts/arquitetura-cliente-servidor]]).
- **Por que cresce:** a mesma linguagem no front, no back e no mobile ([[wiki/entities/react-native]]).

## Key Claims

### Escopo do módulo

- "Esse módulo aqui é voltado para quem quer aprender JavaScript iniciante [...] se você quiser, por exemplo, dar uma repaginada no JavaScript, esse módulo também é para você."
- O objetivo é "nivelar os principais pontos que eu acho de suma importância antes de a gente passar para alguma framework, como, por exemplo, o React".
- "Esse módulo não é aquele curso completaço de JavaScript [...] até acredito que isso é impossível." Ele vai "bater nas principais", nos conceitos "primordiais".
- "Você precisa saber, sim, o básico [...] para poder você não se sentir completamente perdido, mas de fato você não precisa saber de tudo antes de iniciar qualquer coisa."
- Pré-requisito: "é altamente recomendável que você já saiba, que você já tenha praticado HTML e CSS, por quê? O JavaScript a gente vai justamente manipular esses dois."
- Roteiro: variáveis, estruturas condicionais e de repetição, funções, objetos, arrays e loops; "DOM e os seus principais eventos"; algo "que interaja com o usuário"; "o que significa o JavaScript assíncrono [...] com relação a comunicação com o back-end".

### ES, ECMAScript e as versões

- "O JavaScript [...] detém de uma organização, então esse ES vem de ECMAScript, então essa organização gerencia o JavaScript". Gerenciar é "atualizar o JavaScript, organizar o JavaScript".
- A pergunta "qual foi a forma de organizar as atualizações?" tem 5,5 s sem legenda antes da resposta: "O ano, só que mais um, ou seja, o ES6 é uma atualização do JavaScript em 2015, o ES7 de 2016, o ES8 de 2017 e assim vai". Leitura provável: o último dígito do ano mais um (2015 → 6).
- "Antes dessa atualização do ES6, o JavaScript era um pouco arcaico." O jQuery "basicamente faz o que o JavaScript nativo já faz hoje em dia, por isso que o jQuery tem caído com relação a procura", mas "na época ele era muito, muito popular justamente porque ele implementava essas questões que o JavaScript ainda não tinha".
- "A partir do ES6, o ES7, o ES8 tiveram boas atualizações do JavaScript tornando-o mais completo nativamente." Cita Webpack, Babel, arrow functions e async/await: "esses conceitos vieram mais nessas versões".

### O que é JavaScript

- "O JavaScript [...] é uma linguagem de programação em si, diferente, por exemplo, do HTML e do CSS, o HTML é uma linguagem de marcação, onde você insere o conteúdo da página, o CSS é mais voltado para estilização, então esses dois não têm muita inteligência, apesar de que o CSS tenha evoluído tanto."
- "O JavaScript é a linguagem de programação que torna, por exemplo, uma página web dinâmica, é uma tecnologia que implementa funcionalidade naquela página."
- E-commerce: a listagem tem foto pequena e descrição curta. Clicando, aparece a página do produto com descrições, códigos, preço, "quantas vezes você pode dividir", botão de compra, fotos maiores, observações e fórum. "Essa dinamicidade, quem faz por trás dela é o JavaScript."
- "Quem a parte de frente de usuário está em contato direto com o usuário, quem é o responsável é o front-end e aquele que vai lá no banco de dados, que constrói as funcionalidades e tudo mais, quem faz isso é o back-end."
- "Para a web não existe só o JavaScript, existem outras tecnologias", mas ele cresce porque "você aprende uma tecnologia [...] tanto no front-end como no back-end", e em bibliotecas "como o React Native, que é mais voltado para mobile".

## Entities

- [[wiki/entities/nasser]]: instrutor (diz o nome).
- [[wiki/entities/frontpush]]: curso; abertura do módulo de JavaScript ES6.
- [[wiki/entities/javascript]]: assunto da aula (página criada neste ingest).
- [[wiki/entities/react]]: o framework para o qual o módulo prepara.
- [[wiki/entities/react-native]]: JavaScript no mobile.
- [[wiki/entities/nodejs]]: instalado na próxima aula; implícito no "JavaScript no back-end".
- [[wiki/entities/vs-code]]: instalado na próxima aula.

## Concepts

- [[wiki/concepts/ecmascript]] (criado neste ingest)
- [[wiki/concepts/jquery]]
- [[wiki/concepts/biblioteca-javascript-de-compatibilidade]]
- [[wiki/concepts/transpilador]]
- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/async-await]]
- [[wiki/concepts/dom]]
- [[wiki/concepts/html-hipertexto]]
- [[wiki/concepts/css]]
- [[wiki/concepts/logica-de-programacao]]
- [[wiki/concepts/framework-web]]
- [[wiki/concepts/historia-do-front-end]]
- [[wiki/concepts/arquitetura-cliente-servidor]]
- [[wiki/concepts/single-page-application]]
- [[wiki/concepts/renderizacao-ssr-vs-csr]]
- [[wiki/concepts/git]]

## Precisões e tensões com a wiki

- **ECMAScript é a especificação, não a organização.** `[external]` A organização é a Ecma International. Quem evolui a linguagem é o comitê TC39, e o documento é o ECMA-262, cujo nome é ECMAScript (https://tc39.es/ecma262/, https://ecma-international.org/technical-committees/tc39/). "JavaScript" é a marca usada para as implementações (marca registrada da Oracle). Ver [[wiki/concepts/ecmascript]]. Confiança alta.
- **ES6 e ES2015 são o mesmo.** `[external]` A 6ª edição saiu em junho de 2015. A partir dela o nome oficial passou a ser o ano (ES2015, ES2016...), e "ES6", "ES7" ficaram como apelidos. Daí a regra "o ano, só que mais um", que só funciona de 2015 a 2019 (ES10 = ES2019). Antes do ES6 vinha o ES5 (2009), e o ES4 foi abandonado (https://262.ecma-international.org/6.0/). Confiança alta.
- **Webpack e Babel não "vieram nessas versões".** Não são recursos do ECMAScript, são ferramentas. O Babel (lançado como 6to5 em 2014) traduz JS novo para JS que navegador antigo entende; o Webpack (2012) é um *bundler* que junta módulos ([[wiki/concepts/transpilador]], [[wiki/concepts/pipeline-de-assets]]). Ficaram populares porque o ES6 saiu antes de os navegadores o suportarem. Arrow functions (ES2015) e async/await (ES2017) são da linguagem; aí a frase está certa. `[skill: lang-dynamic]` Hoje Vite, esbuild e Rspack (substituto do Webpack escrito em Rust) dominam projetos novos; o Webpack segue como linha de base de ecossistema.
- **O que tirou o espaço do jQuery foi mais o DOM do que o ES6.** `querySelectorAll`, `classList`, `fetch` e `addEventListener` padronizado são APIs da web (W3C/WHATWG), não do ECMAScript. O ES6 trouxe a sintaxe (classes, módulos, promises); o fim da fragmentação entre navegadores trouxe o resto. A página [[wiki/concepts/jquery]] já registra os dois movimentos ([[wiki/sources/historia-do-front-end-akita-ep4]]).
- **O exemplo do e-commerce não exige JavaScript.** Uma listagem com links para páginas de produto geradas pelo servidor funciona com JS desligado, e as lojas costumam ser assim, por SEO ([[wiki/concepts/renderizacao-ssr-vs-csr]]). O JavaScript entra quando a troca acontece sem recarregar a página ([[wiki/concepts/single-page-application]]) ou no carrinho, galeria e simulador de parcelas. A aula mistura "dinâmico no servidor" com "dinâmico no navegador".
- **Front-end não é "a parte visual" só.** Na mesma frase, a lógica de funcionalidade fica no back-end ("que constrói as funcionalidades"), mas o JavaScript do front também é lógica. A divisão correta é onde o código roda: navegador ou servidor ([[wiki/concepts/arquitetura-cliente-servidor]]).
- **React como "framework".** A documentação do React o chama de biblioteca; na prática a palavra é usada para os dois ([[wiki/concepts/framework-web]]). O módulo também diz "uma framework", no feminino. Na abertura do módulo de React ele já diz "biblioteca JavaScript" ([[wiki/sources/frontpush-intro-modulo-reactjs]]).
- **Novidades depois da gravação.** `[skill: lang-dynamic]` O TC39 continua lançando uma edição por ano. A API Temporal (datas) chegou ao Stage 4 em março de 2026 e vem ligada no Node 26.
- **Data da gravação.** "jQuery tem caído" e ES8 como exemplo mais novo apontam para o período 2020–2021, coerente com as outras aulas do FrontPUSH (inferência).

## Open Questions

- Há 5,5 s sem legenda (00:04:35–00:04:41) entre a pergunta e "O ano, só que mais um". Ele provavelmente mostrou um slide com a tabela de versões.
- "Muitas funcionalidades que são pedidas": "pedidas" pela comunidade (propostas ao TC39)? A frase fica solta na legenda.
- O cenário novo ("estamos meio aqui de cenário novo") sugere que o módulo foi gravado depois dos de CSS e Sass; a ordem real dos módulos no curso não é dita.

## Raw quotes

- "esse módulo não é aquele curso completaço de JavaScript"
- "o JavaScript a gente vai justamente manipular esses dois"
- "o JavaScript é a linguagem de programação que torna [...] uma página web dinâmica"
