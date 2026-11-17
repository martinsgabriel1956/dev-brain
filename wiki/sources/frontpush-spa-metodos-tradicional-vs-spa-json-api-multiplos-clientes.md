---
type: source
title: "SPA: o método tradicional e o método SPA (FrontPUSH)"
aliases: ["FrontPUSH SPA Métodos", "módulo de ReactJS, aula 04", "método tradicional vs. SPA"]
date_created: 2026-11-17
date_updated: 2026-11-17
source_count: 0
tags: [spa, ssr, mpa, json, api, endpoint, php, dao, query-string, metodo-get, escalabilidade, multiplos-clientes, front-end, back-end, react, curso, frontend]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-spa-metodos-tradicional-vs-spa-json-api-multiplos-clientes.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-17
---

# SPA: o método tradicional e o método SPA (FrontPUSH)

## TL;DR

Aula 04 do módulo de ReactJS do [[wiki/entities/frontpush|FrontPUSH]], cerca de 20 min. É a primeira de duas sobre [[wiki/concepts/single-page-application|SPA]]; a componentização fica para a próxima. [[wiki/entities/nasser|Násser]] (diz o nome: "ó, Násser, quando você for requisitar produtos") conta que veio do PHP e compara dois fluxogramas.

- **Método tradicional** (slide): browser pede `/products?id=10` → servidor faz a query SQL → banco devolve o registro → servidor monta HTML e CSS e devolve "o pacote já pronto", ~50 KB. Demonstração na KaBuM (`?codigo=` na URL, Ctrl+U mostra HTML, CSS, Swiper.js, jQuery, masked inputs) e código PHP com `$_GET`, `new Produto`, `setID`, um `ProdutoDAO` e `echo` de `<li>` ([[wiki/concepts/renderizacao-ssr-vs-csr]], [[wiki/concepts/template-engine]]).
- **Consequências:** front e back "muito atrelados" no mesmo arquivo; "na época" não havia as duas profissões, só o webmaster ([[wiki/concepts/historia-do-front-end]]); o servidor "fica sobrecarregado", e a saída é servidor mais potente ou "servidor espelhado" ([[wiki/concepts/escalabilidade-vertical]], [[wiki/concepts/failover]]).
- **Método SPA** (slide): mesma requisição, mas o servidor devolve só a informação, em [[wiki/concepts/json|JSON]], ~5 KB; o front interpreta e mostra.
- **Vantagens** (slide): "melhor divisão de tarefas" (back cuida de autenticação, segurança, banco e regra de negócio; front, de "mostrar isso na tela"), "uma API, múltiplos clientes" (web, Swift iOS, Kotlin Android), "+ flexibilidade, + aproveitamento, + interatividade, + organização".
- **API e endpoints:** o back documenta endereços por recurso; `api.github.com` como exemplo ([[wiki/concepts/api]], [[wiki/concepts/contrato-de-api]], [[wiki/entities/github]]).
- **Back-end agnóstico:** "pode ser PHP, pode ser Node, pode ser Ruby, pode ser C Sharp [...] não interessa porque ele comunica em JSON" ([[wiki/concepts/arquitetura-cliente-servidor]]).

## Key Claims

### Por que comparar

- "Eu sou desenvolvedor PHP e lógico que eu meio que parei, estou estudando mais front-end." Quer mostrar "o que acontece debaixo dos panos" e "por que as bibliotecas JavaScript estão com vantagens com relação a esse método tradicional, com relação à produtividade, à flexibilidade".
- "Não entenda tradicional como algo ruim ou como algo antigo, porque tem muitos websites que ainda são feitos dessa forma."
- "Sempre tem que ter um motivo" para usar um framework.

### O método tradicional

- Na KaBuM, o produto vai na URL: "é o método GET [...] eu passo a interrogação, código é o nome da variável, igual, ele passa o valor" ([[wiki/concepts/query-string]], [[wiki/concepts/metodos-http]]).
- O servidor faz "uma query SQL [...] onde tiver o ID igual a 10, me traz esse registro", recebe nome, descrição, especificação, endereço das imagens, preço, e "vai vincular com o HTML".
- Outro produto (um processador): "é a mesma página [...] o que vai mudar é [...] essa sidebar aqui do lado e as informações do próprio produto [...] muda o miolo aqui da página".
- Ctrl+U: "é isso aqui que o servidor vai devolver para o front-end, ele faz tudo": CSS, JavaScript, Swiper.js nos sliders, jQuery no zoom, masked inputs, conteúdo e imagens. "Ele manda o pacote já pronto, sei lá, pesando 50kb."
- Código PHP no VS Code ("você está ensinando PHP no negócio de JavaScript, calma"): pegar o ID "via get", `objetoProduto = new Produto`, `setID`, um `ProdutoDAO` com um método inventado "pesquisa ID produto" que devolve um array, um `forEach` e `echo` com `<li>` para nome e preço. "O echo é como se fosse um print, não, é de fato um print."
- "Essa parte aqui de cima [...] quem faz é o back-end [...] pegar o ID, instanciar, fazer a pesquisa e devolver o array, a parte do front-end, a competência do front-end é essa competência aqui."
- "Back-end e front-end são muito atrelados [...] porque a renderização é toda feita no servidor." "Na época não fosse muito bem definido as profissões [...] é simplesmente o cara que faz o site, que é o chamado webmaster", e eles "precisariam trabalhar muitíssimo juntos no mesmo arquivo".
- Num e-commerce famoso, "o servidor tem que dar conta de tudo, ele que renderiza tudo, meio que ele fica sobrecarregado", e a saída é "servidores mais potentes, mais robustos" ou "um servidor espelhado para quando um cair o outro subir na frente dele".
- Há 8 s sem legenda (00:08:55–00:09:03) entre o `setID` e "Dentro de uma função para poder ele fazer a requisição lá para o banco".

### O método SPA

- "Agora o servidor não vai renderizar o HTML, o CSS, o JavaScript e vai me entregar esse pacote completo, ele vai me entregar somente a informação do produto [...] em um arquivo chamado JSON [...] meio que uma forma universal de todas as linguagens se comunicarem." O slide traz `{"nome": "Notebook DELL 15.7' Full HD", "marca": "DELL", "preco": "R$ 4.999,99"}` e ~5 KB.
- "Ele me manda o que de fato importa [...] que eu posso [...] pegar no meu front-end o JSON, interpretar ele e aí sim eu consigo tratar e mostrar essas informações visualmente."
- Divisão: back-end "responsável por autenticação, por segurança, por comunicação com o banco de dados, por regra de negócios, enquanto o front-end fica literalmente responsável por mostrar isso na tela" ([[wiki/concepts/separation-of-concerns]]).
- Endpoints como documentação: "quando você for requisitar produtos, requisite nesse endereço [...] você quer adicionar um novo usuário, vai no endereço de usuário e aí a gente começa a falar sobre API". Em `api.github.com`, "cada endereço desse aqui, a gente fala que é um endpoint". A API informa "todos os JSONs que eu preciso para [...] atualizar [...] criar [...] listar [...] deletar registros" ([[wiki/concepts/crud]]).

### Uma API, múltiplos clientes

- "Da forma tradicional ele vai devolver um pacote de HTML, CSS e JavaScript e quem disse que se eu for fazer um aplicativo [...] o front dele vai entender o que é HTML [...] porém o JSON todos entendem."
- "Com o mesmo back-end, com a mesma API, eu consigo servir vários clientes": web, "Swift com o iOS", "Kotlin de Android".
- "A gente agora delimitou muito bem duas profissões, o cara do back-end e o cara do front-end."
- "A interatividade quando a gente utiliza o React, o Vue, você vai ver que ela melhora muito porque ele utiliza componentes", tema da próxima aula ([[wiki/concepts/componentizacao]]).

## Entities

- [[wiki/entities/nasser]]: instrutor (diz o nome); veio do PHP.
- [[wiki/entities/frontpush]]: curso; módulo de ReactJS.
- [[wiki/entities/react]], [[wiki/entities/vue]]: bibliotecas que usam o método SPA.
- [[wiki/entities/github]]: `api.github.com` como exemplo de endpoints.
- [[wiki/entities/vs-code]]: editor da demonstração.
- KaBuM, Swiper.js, PHP, Swift, Kotlin: citados, sem página.

## Concepts

- [[wiki/concepts/single-page-application]]
- [[wiki/concepts/renderizacao-ssr-vs-csr]]
- [[wiki/concepts/site-estatico-vs-dinamico]]
- [[wiki/concepts/template-engine]]
- [[wiki/concepts/json]]
- [[wiki/concepts/api]]
- [[wiki/concepts/api-rest]]
- [[wiki/concepts/contrato-de-api]]
- [[wiki/concepts/query-string]]
- [[wiki/concepts/metodos-http]]
- [[wiki/concepts/repository-pattern]] (DAO)
- [[wiki/concepts/arquitetura-cliente-servidor]]
- [[wiki/concepts/separation-of-concerns]]
- [[wiki/concepts/bff-pattern]]
- [[wiki/concepts/escalabilidade-vertical]]
- [[wiki/concepts/escalabilidade-horizontal]]
- [[wiki/concepts/failover]]
- [[wiki/concepts/historia-do-front-end]]
- [[wiki/concepts/jquery]]
- [[wiki/concepts/componentizacao]]

## Precisões e tensões com a wiki

- **A comparação é entre renderizar no servidor e renderizar no cliente; "SPA" é só um lado.** O método tradicional é uma MPA com SSR; o "método SPA" é CSR com API JSON. O que a aula mostra (servidor devolve dados, front monta) pode existir sem SPA: uma página multi-página que busca JSON com [[wiki/concepts/ajax|AJAX]]. E o contrário: Next.js, Remix e o próprio React com Server Components voltaram a renderizar no servidor, com hidratação ([[wiki/concepts/renderizacao-ssr-vs-csr]], [[wiki/concepts/hydration]]). `[skill: tech-mentor-frontend]` Confiança alta.
- **50 KB × 5 KB omite o primeiro carregamento.** Na SPA, a primeira visita baixa o bundle JavaScript (centenas de KB não é raro) e o HTML chega quase vazio; só as navegações seguintes trocam ~5 KB de JSON. Daí o pior LCP e o problema de SEO das SPAs puras, que o SSR resolve. O slide compara a 2ª navegação de uma com a 1ª da outra. `[skill: tech-mentor-frontend]` Confiança alta.
- **"O servidor fica sobrecarregado" vale menos do que parece.** Montar HTML a partir de um template é barato perto da query no banco, que acontece nos dois métodos. Páginas de produto são ótimas para cache (CDN, [[wiki/concepts/http-caching]]), coisa que JSON personalizado nem sempre é. A SPA desloca a renderização para o cliente; não elimina a carga do servidor. Confiança média-alta.
- **"Servidor espelhado" é redundância, não capacidade.** Um espelho que "sobe na frente" quando o outro cai é [[wiki/concepts/failover]] (disponibilidade). Para aguentar mais requisições a saída é [[wiki/concepts/escalabilidade-horizontal]] atrás de um [[wiki/concepts/load-balancer]], o que vale para os dois métodos.
- **DAO: o nome certo é Data Access Object.** Ele diz "Direct Access Database, Database Access Object, aliás". O padrão isola o acesso ao banco atrás de uma classe; é parente do [[wiki/concepts/repository-pattern]]. `[external]` (Core J2EE Patterns). Confiança alta.
- **GET não é "uma forma de inserir a informação no link".** GET é o método HTTP; o `?codigo=154988` é a [[wiki/concepts/query-string]]. Um GET pode não ter query string, e um POST de formulário também pode ter ([[wiki/concepts/metodos-http]]). Em PHP, `$_GET` lê a query string seja qual for o método. Em URLs de produto, o comum hoje é o ID no caminho (`/produto/154988`).
- **"Uma API, múltiplos clientes" tem limite conhecido.** Clientes diferentes querem formatos diferentes (o app quer menos campos, a web quer mais), e a API única tende a servir mal os dois. As respostas são o [[wiki/concepts/bff-pattern]] (um back-end por front) e o GraphQL. O argumento central está certo: JSON desacopla a tecnologia do cliente da do servidor.
- **"Webmaster" e o surgimento das duas profissões.** A divisão front × back nasceu com o AJAX e as SPAs (meados dos anos 2000 e 2010), não só com o JSON; e a separação acabou trazendo de volta o full-stack ([[wiki/concepts/historia-do-front-end]], [[wiki/sources/historia-do-front-end-akita-ep4]]).
- **Preço como string no JSON.** `"preco": "R$ 4.999,99"` mistura dado e formatação; o comum é número (ou centavos inteiros) e formatar no front com `Intl.NumberFormat`. Detalhe de slide, mas é o tipo de coisa que o front vai receber ([[wiki/concepts/json]]).
- **"Da outra forma não tinha como fazer" app.** Havia: apps híbridos (WebView) consomem HTML, e um back-end tradicional pode ter, além das páginas, uma API para o app. O que a API JSON evita é ter dois back-ends.
- **"Página de aplicação"** não traduz *single page application*; a tradução que ele dá em seguida, "aplicação de página única", é a certa.

## Open Questions

- "Porque eu nascia, eu sou desenvolvedor PHP": provável "eu nasci [como] desenvolvedor PHP"; deixado literal.
- "Várias frontes para o aplicativo, para mobile ou para mobile": provável "para web ou para mobile"; deixado literal.
- "Eu tenho, por exemplo, do hub": provável leitura do `hub_url` da raiz de `api.github.com`.
- O que ele disse nos 8 s sem legenda (00:08:55–00:09:03), provavelmente a assinatura da função que chama o DAO.
- ~~A aula 05 deve tratar componentização~~: tratou, e trouxe as rotas no cliente na definição de SPA ([[wiki/sources/frontpush-spa-componentes-estrutura-app-js-componentizacao]]).

## Raw quotes

- "não entenda tradicional como algo ruim ou como algo antigo"
- "meio que ele manda o pacote já pronto, sei lá, pesando 50kb"
- "porém o JSON todos entendem"
