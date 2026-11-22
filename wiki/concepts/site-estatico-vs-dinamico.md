---
type: concept
title: "Site estático vs. dinâmico (e interface dinâmica)"
aliases: ["interface dinâmica", "interface estática", "site estático", "site dinâmico", "página dinâmica"]
date_created: 2026-11-17
date_updated: 2026-11-22
source_count: 6
tags: [frontend, backend, renderizacao, spa, ssr, ssg, site-estatico]
skill: tech-mentor-frontend
status: stub
---

# Site estático vs. dinâmico

"Dinâmico" tem pelo menos três sentidos na web, que costumam se misturar:

| Sentido | Estático | Dinâmico |
|---|---|---|
| **Geração no servidor** | arquivos prontos servidos como estão (HTML de um build, SSG) | HTML gerado a cada requisição a partir de um modelo e do banco (PHP, Rails, SSR) ([[wiki/concepts/template-engine]]) |
| **Interatividade no navegador** | só HTML e CSS | JavaScript muda a página sem recarregar ([[wiki/concepts/ajax]], [[wiki/concepts/single-page-application]]) |
| **Movimento** (uso informal) | sem animação | com motion (GSAP, transições) |

Os eixos são independentes: um build de React é estático no 1º sentido e dinâmico no 2º; um site PHP sem JavaScript é dinâmico no 1º e estático no 2º. `[skill: tech-mentor-frontend]` Ver [[wiki/concepts/renderizacao-ssr-vs-csr]].

## No FrontPUSH

Em [[wiki/sources/frontpush-conceitos-gerais-react-interface-dinamica-spa-virtual-dom-jsx]], [[wiki/entities/nasser]] descarta o 3º sentido ("não é isso") e define interface dinâmica como a página "reconstruída de maneira diferente dependendo da rota", com "JavaScript ou uma linguagem de programação por trás"; estática é "um site com HTML e CSS só". O exemplo é a página de produto da KaBuM: mesma estrutura, dados de cada produto, em vez de "milhões de páginas" em HTML puro.

A definição junta os sentidos 1 e 2. O exemplo é do sentido 1 (ele mesmo diz que a página "vai recarregar"), que o template no servidor resolve sem React; o React entra no sentido 2. Na aula 04 ([[wiki/sources/frontpush-spa-metodos-tradicional-vs-spa-json-api-multiplos-clientes]]) ele mesmo usa a KaBuM como exemplo do "método tradicional", renderizado no servidor. A aula 01 de JS tinha a mesma mistura com o e-commerce ([[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]]).

## Related

- [[wiki/concepts/renderizacao-ssr-vs-csr]]
- [[wiki/concepts/single-page-application]]
- [[wiki/concepts/template-engine]]
- [[wiki/concepts/historia-do-front-end]]

## FrontPUSH, hospedagem aula 01

Em [[wiki/sources/frontpush-introducao-hospedagem-de-websites-url-localhost-porta]], hospedagem serve "um site ou aplicação web", "e olha que tem diferença": a aplicação "necessita de mais configurações". Na escolha do host isso pesa: GitHub Pages só estático, Heroku roda processos ([[wiki/concepts/hospedagem-de-sites]]).

## FrontPUSH, hospedagem aula 03

Em [[wiki/sources/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react]], estático é "HTML, CSS e JS puros", "denominado estático porque ele não consegue construir funcionalidades complexas" (to-do list que some no F5), e React não caberia nele. A aula mistura os eixos da tabela acima: estático é o servidor entregar arquivos prontos; um build de React é estático e navega entre telas. O critério que sobra, e que importa para hospedar, é o do servidor: PHP pede interpretador, estático só um servidor de arquivos.

## FrontPUSH, hospedagem aula 06

Em [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]], o critério vira prático: o portfólio (com GSAP por `<script>`, sem npm) e o CreatorPUSH são estáticos porque "qual é a funcionalidade que eu preciso que ele tenha? Nenhuma"; página de vendas também ("texto, imagem e link"), por ser "bem leve", "escalável", "performático". O FrontPUSH é PHP por ter outras páginas (cadastro, lista de espera). Ressalvas: páginas ligadas por link também são estáticas; o build de React também é estático.

## De novo: estático "sem funcionalidade"

A [[wiki/sources/frontpush-monetizacao-freelancer-como-conseguir-a-primeira-vaga|aula 04 do módulo Monetização e Freelancer]] repete a definição pela funcionalidade (estáticas "só têm de HTML e CSS"; dinâmicas têm rotas, e-mail, reatividade, SPA). A ressalva desta página vale: o build de uma SPA também é estático do ponto de vista do servidor.

## Key Sources

- [[wiki/sources/frontpush-monetizacao-freelancer-como-conseguir-a-primeira-vaga]]: definição por funcionalidade repetida
- [[wiki/sources/frontpush-conceitos-gerais-react-interface-dinamica-spa-virtual-dom-jsx]]: FrontPUSH, React aula 03: interface dinâmica × estática pela KaBuM
- [[wiki/sources/frontpush-spa-metodos-tradicional-vs-spa-json-api-multiplos-clientes]]: FrontPUSH, React aula 04: o mesmo e-commerce da KaBuM, agora explicado como HTML montado no servidor
- [[wiki/sources/frontpush-introducao-hospedagem-de-websites-url-localhost-porta]]: FrontPUSH, hospedagem aula 01: site × aplicação web na hora de hospedar
- [[wiki/sources/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react]]: FrontPUSH, hospedagem aula 03: website estático × aplicação web (eixos misturados)
- [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]]: FrontPUSH, hospedagem aula 06: portfólio e vendas estáticos, FrontPUSH em PHP
