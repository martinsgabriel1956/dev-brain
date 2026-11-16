---
type: entity
title: "Next Level Week (NLW)"
aliases: ["NLW", "Next Level Week", "NLW #1", "Ecoleta", "NLW #2", "Proffy"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 14
tags: [evento, educacao, rocketseat, frontend, ecoleta, proffy]
skill: tech-mentor-frontend
status: stub
---

# Next Level Week (NLW)

Semana de aulas gratuitas da [[wiki/entities/rocketseat]] em que se constrói um projeto do zero. Na primeira edição, o projeto é o **Ecoleta**, "uma brincadeira com ecologia e coletas de resíduos", feito na "semana do meio ambiente": empresas cadastram pontos de coleta e o tipo de resíduo que aceitam (pilhas e baterias, eletrônicos, lâmpadas, papelão, óleo de cozinha), e quem quer descartar busca os pontos da cidade. O layout é de Thiago, da Rocketseat ([[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]).

O dia 1 cobre só a página inicial; "a gente vai fazer durante essa semana". A edição é de junho de 2020, pela semana do meio ambiente `[external, não verificado]`.

## Na NLW #1, dia 2 (Mayk Brito)

No dia 2 ([[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]) o Ecoleta ganha a página `create-point.html`, com o formulário de cadastro de pontos e os selects de estado e cidade preenchidos pela API do [[wiki/entities/ibge]]. O envio fica para depois.

## Na NLW #1, dia 3 (Mayk Brito)

Dia 3 da NLW #1 ([[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]): abre explicando a escolha do JavaScript e o método ("foco, grupo e muita prática"). Termina o front-end do Ecoleta: itens de coleta, modal de busca e página de resultados, com feedback na "comunidade exclusiva do NLW".

## Na NLW #1, dia 4 (Mayk Brito)

Dia 4 da NLW #1 ([[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]): o Ecoleta ganha back-end com Node.js, [[wiki/entities/express]] e [[wiki/entities/nunjucks]], e o projeto se reorganiza em `public/` e `src/`. A aula termina anunciando a turma seguinte do Launchbase.

## Na NLW #1, dia 5 (Mayk Brito)

Dia 5 da NLW #1 ([[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]]): o Ecoleta fica completo, com SQLite, cadastro por POST e busca por cidade. A semana termina com um encontro ao vivo no domingo e a abertura das inscrições do Launchbase.

## Na NLW #1, trilha de Diego Fernandes

A mesma edição tem uma segunda trilha, com [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]): o Ecoleta vira uma API REST em Node com [[wiki/entities/typescript]], consumida por uma web em [[wiki/entities/react]] (cadastro de pontos) e por um app em [[wiki/entities/react-native]] com [[wiki/entities/expo]] (mapa, filtro por item, WhatsApp e e-mail). No dia 1, Diego descreve a semana como a "Semana Internacional do Meio Ambiente".

No dia 2 da trilha de [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]), a API do Ecoleta fica pronta com Express, [[wiki/entities/knex]] e SQLite: itens por seed, cadastro de ponto em transação, filtros por UF, cidade e itens, e CORS. Só o upload de imagens fica para depois.

No dia 3 da trilha de [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]), o Ecoleta ganha o front-end web em React: Home, cadastro com mapa Leaflet, itens da API, UF e cidade do IBGE, e envio para `POST /points`.

No dia 4 da trilha de [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]), o Ecoleta ganha o app Android/iOS em React Native com Expo: Home com UF e cidade, mapa filtrado por itens e detalhe com WhatsApp e e-mail.

No dia 5 da trilha de [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]), o Ecoleta ganha upload de imagens (Multer + react-dropzone), validação com celebrate/Joi, repositório no GitHub e um panorama de deploy. Com isso, as duas trilhas da NLW #1 estão completas na wiki.

Comparação das duas trilhas: [[wiki/questions/nlw-1-duas-trilhas-ecoleta-comparacao]].

## Na NLW #2, dia 1 (Mayk Brito)

A segunda edição (NLW #2) tem como projeto o **Proffy**, "nossa plataforma de estudos online", na "versão 1.0": quem dá aula preenche nome, foto, WhatsApp, biografia, matéria e horários; quem estuda busca a matéria e vê os professores disponíveis. A semana coincide com o "dia 6, que é o dia dos profissionais da educação", e o layout é de Thiago, da Rocketseat ([[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]). A transcrição só diz "NLW"; a edição foi confirmada pelo usuário, e a data (agosto de 2020) segue inferida `[external, não verificado]`. O dia 1, com [[wiki/entities/mayk-brito|Mayk]], termina com o esqueleto da página inicial e manda o feedback para a "comunidade exclusiva do NLW", onde também rolam os desafios.

## Na NLW #2, dia 2 (Mayk Brito)

No dia 2 da NLW #2 ([[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]), o Proffy ganha a landing page responsiva (celular e desktop com grid) e a página `study.html`, com filtros de matéria, dia e hora e o card do professor. O envio do formulário e a página de dar aulas ficam para os dias seguintes.

## Na NLW #2, dia 3 (Mayk Brito)

No dia 3 da NLW #2 ([[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]), o Proffy ganha `give-classes.html`, com o formulário de cadastro do professor, e o primeiro JavaScript: o botão "Novo horário" clona o bloco de horários. O front-end fica completo; back-end e banco ficam para os dias 4 e 5.

## Na NLW #2, dia 4 (Mayk Brito)

No dia 4 da NLW #2 ([[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]), o Proffy ganha servidor Express, rotas, Nunjucks, filtros que voltam preenchidos e cadastro em memória. O banco de dados (SQLite) fica para o dia 5.

## Key sources

- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: dia 1, apresentação do Ecoleta e página inicial em HTML e CSS ([[wiki/entities/mayk-brito]])
- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: dia 2: página de cadastro
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: dia 3: fim do front-end do Ecoleta
- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: dia 4: Node, Express, Nunjucks
- [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]]: dia 5: Ecoleta completo
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: dia 1 da trilha de Diego Fernandes: layout web e mobile, API REST, TypeScript, React e Expo
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: dia 2 da trilha de Diego: a API completa do Ecoleta
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: dia 3 da trilha de Diego: front-end web em React
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: dia 4 da trilha de Diego: app mobile
- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: dia 5 da trilha de Diego: fechamento
- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: NLW #2, dia 1: apresentação do Proffy e página inicial em HTML e CSS
- [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]: NLW #2, dia 2: landing page e página study do Proffy
- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: NLW #2, dia 3: give-classes e JavaScript
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: back-end do Proffy
