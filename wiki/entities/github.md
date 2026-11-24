---
type: entity
title: "GitHub"
aliases: ["github.com"]
date_created: 2026-09-23
date_updated: 2026-11-24
source_count: 19
tags: [plataforma, git, incidente, sistemas-distribuidos, security]
skill: tech-mentor-system-design
status: stub
---

# GitHub

Plataforma de hospedagem de código. Na wiki aparece como estudo de caso de falha distribuída (o incidente de outubro de 2018, [[wiki/concepts/github-incidente-2018-particao-de-rede]]) e, mais recentemente, como alvo e ferramenta de segurança: a API de busca de código tem limites de indexação relevantes para secret scanning ([[wiki/concepts/github-search-api-limites]]), e a plataforma oferece defesas nativas contra vazamento de credenciais (push protection, GitHub Advanced Security — ver [[wiki/concepts/secret-scanning]]).

## Logo nos ícones do FrontPUSH

Em [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]], o gato do GitHub ("bem arredondado, tem as orelhinhas") é redesenhado "totalmente reto" para a família de ícones do [[wiki/entities/frontpush]]. `[external]` As diretrizes de logo do GitHub pedem para não modificá-lo (https://github.com/logos).

## GitHub x GitLab no FrontPUSH

Em [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]], [[wiki/entities/nasser|Násser]] apresenta GitHub e GitLab como "repositórios online que a gente utiliza o Git", cita o Bitbucket e diz que o GitHub "está na frente": todo dev que conhece usa. A frase "o GitHub já foi muito utilizado porque ele tinha melhores planos gratuitos" provavelmente queria dizer GitLab. `[external]` O GitHub liberou repositórios privados no plano gratuito em janeiro de 2019: https://github.blog/news-insights/product-news/new-year-new-github/.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: o repositório `nlw-01` com `server/`, `web/` e `mobile/`, a remoção dos `.git` aninhados, o `git push origin master` e o conselho de um README com imagens para o portfólio. Desde então, o padrão é `main` e o HTTPS exige token.

## Na NLW #2, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]], [[wiki/entities/mayk-brito|Mayk]] mostra como pegar o link do avatar de um perfil (botão direito, Copy Image Link) para usar no `src` do card de professor do Proffy.

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], os avatares dos professores de exemplo (Diego, Mayk, Clayton Souza) vêm do Copy Image Link nos perfis do GitHub.

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], o avatar do professor de exemplo é o link da imagem de perfil do GitHub de [[wiki/entities/mayk-brito|Mayk]] (Copy Image Link).

Em [[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete]], [[wiki/entities/nasser|Násser]] usa a API pública do GitHub ("muitíssimo utilizada nesses casos") como exemplo de GET: `/users/<usuário>` devolve login, ID e node ID. Promete usá-la nas próximas aulas. O repositório Public APIs, hospedado no GitHub, lista APIs de vários provedores, não só as do GitHub.

Em [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]], a API `/users/<usuário>` do GitHub é consultada com `XMLHttpRequest`; o objeto traz avatar, bio, blog, company e URLs de outros recursos ([[wiki/concepts/xmlhttprequest]]).

Em [[wiki/sources/frontpush-promises-resolve-reject-then-catch]], a API `/users` do GitHub é consultada de novo, agora via Promise; com a URL alterada de propósito, o 404 cai no `catch`.

Em [[wiki/sources/frontpush-axios-cdn-get-then-encapsulamento-xhr]], a mesma API `/users` do GitHub, agora com `axios.get`; o usuário fica em `response.data`.

## Key sources

- [[wiki/sources/github-2018-cap-pacelc-particao-video]] — incidente de 2018 usado para explicar CAP/PACELC
- [[wiki/sources/dev-na-era-da-ia-qualidade-esteira-e-novas-preocupacoes]] — citado como ferramenta a aprender junto com a IA
- [[wiki/sources/secrets-vazadas-no-github-conceitos-e-riscos]] — limites técnicos da API de busca de código (indexação, teto de resultados) relevantes para a descoberta de secrets vazadas
- [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]: NLW #2, dia 2: link do avatar para o card
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: avatares do array
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: NLW #2, dia 5: avatar de exemplo

## GitHub Pages no FrontPUSH (hospedagem, aula 01)

Em [[wiki/sources/frontpush-introducao-hospedagem-de-websites-url-localhost-porta]], GitHub Pages é a "maneira bem simples de você hospedar o seu website"; o módulo fará o deploy nele. Serve só arquivos estáticos ([[wiki/concepts/hospedagem-de-sites]]).

## No JavaScript Ninja, semana 3, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-metodos-de-objeto-continuacao]], o curso vive no GitHub: repositório `da2k/curso-javascript-ninja`, um fork por aluno, desafios entregues por pull request e dúvidas por issue, "que pode ajudar outras pessoas". O software desktop do GitHub da época "não suporta mais de um remote", segundo o instrutor; por isso a linha de comando ([[wiki/concepts/fork-e-upstream]]).

## Key sources (adição 2026-10-30)

- [[wiki/sources/spec2cobolrot-envelhecer-cobol-com-ia-complexidade-vs-entropia-historica]] — hospeda os samples públicos do Spec2COBOLRot (jbespi/spec2cobolrot-samples)
- [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]] — Invertocat redesenhado reto em ícone do FrontPUSH
- [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]: GitHub x GitLab x Bitbucket
- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: repositório da NLW; master → main; token
- [[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete]]: FrontPUSH, JavaScript aula 13: API pública do GitHub como exemplo
- [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]]: FrontPUSH, JavaScript aula 14: /users consultado via XHR
- [[wiki/sources/frontpush-promises-resolve-reject-then-catch]]: FrontPUSH, JavaScript aula 15: /users via Promise, e o 404
- [[wiki/sources/frontpush-axios-cdn-get-then-encapsulamento-xhr]]: FrontPUSH, JavaScript aula 16: /users via Axios
- [[wiki/sources/frontpush-spa-metodos-tradicional-vs-spa-json-api-multiplos-clientes]]: FrontPUSH, React aula 04: api.github.com como exemplo de endpoints
- [[wiki/sources/frontpush-introducao-hospedagem-de-websites-url-localhost-porta]]: FrontPUSH, hospedagem aula 01: GitHub Pages para site estático
- [[wiki/sources/frontpush-monetizacao-freelancer-como-construir-um-portfolio]]: FrontPUSH, Monetização e Freelancer aula 05: README como portfólio mínimo ([[wiki/concepts/estrutura-de-readme]])
- [[wiki/sources/frontpush-monetizacao-freelancer-como-descobrir-o-nicho-ideal]]: FrontPUSH, Monetização e Freelancer aulas 06 e 07: basta para vaga, sem site
- [[wiki/sources/javascript-ninja-metodos-de-objeto-continuacao]]: JavaScript Ninja, semana 3, vídeo 03: fork, pull request e issues como estrutura do curso
