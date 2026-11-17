---
type: concept
title: "Componentização"
aliases: ["componentes", "component-based UI", "componente React"]
date_created: 2026-11-16
date_updated: 2026-11-17
source_count: 11
tags: [frontend, react, componentes, reuso, organizacao]
skill: tech-mentor-frontend
status: stub
---

# Componentização

Organizar a interface em peças pequenas, isoladas e reutilizáveis, os componentes. Cada um encapsula marcação, estilo e comportamento, e os componentes se compõem uns dentro dos outros.

Na aula de [[wiki/entities/diego-fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]), é a primeira vantagem do [[wiki/entities/react]]. Um botão que se repete na aplicação vira um componente, "e um dia se eu precisar alterar ele, eu altero apenas em um lugar". O diagrama mostra um componente App com a lista de comentários, cada comentário (o mesmo componente com conteúdo diferente) e o formulário. No React, um componente é "uma função que retorna o HTML" ([[wiki/concepts/jsx]]).

Relacionado: [[wiki/concepts/dry]], [[wiki/concepts/component-library]], [[wiki/concepts/compound-components]], [[wiki/concepts/single-page-application]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]], o exemplo é o `Header` reutilizável (nome com maiúscula "para ele não bater com as tags do HTML") e o tweet repetido do Twitter, visto no React DevTools. Cada página vira uma pasta (`pages/Home/index.tsx` + `styles.css`).

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]], o mesmo modelo se aplica no mobile: uma pasta por tela (`pages/Home`, `Points`, `Detail`) com estilos no mesmo arquivo.

## Arquivos Sass como "componentes" (FrontPUSH)

Em [[wiki/sources/frontpush-import-e-partials-sass]], separar cores, tipografia, layout e botões em partials "utiliza mais ou menos o conceito de componentes" no CSS. Ver [[wiki/concepts/import-e-partials-sass]].

## Na NLW #2, dia 1 (Diego Fernandes)

"Componentes [...] são funções que retornam um HTML", com nome em maiúscula. O `PageHeader` é extraído para `components/` e reaproveitado entre listagem e cadastro; o `TeacherItem` vai para lá porque "bem provavelmente vai ser utilizado em mais lugares". Ver [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]].

## Na NLW #2, dia 3 (Diego Fernandes)

`Input`, `Textarea` e `Select` extraídos porque o campo do cadastro "é exatamente igual" ao da busca; o CSS vai junto, menos a cor da label, que só muda na listagem. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]].

## Na NLW #2, dia 4 (Diego Fernandes)

`PageHeader` mobile reaproveitado entre Proffys e Favoritos, com título por prop e `children` previsto para os filtros, "muito semelhante com o que a gente tinha lá na web". Ver [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]].

## Na NLW #2, dia 5 (Diego Fernandes)

`TeacherItem` mobile compartilhado entre Proffys e Favoritos, com a `interface Teacher` copiada da web. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: botão reutilizável, diagrama de comentários
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: Header reutilizável; uma pasta por página
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: telas como componentes no RN
- [[wiki/sources/frontpush-import-e-partials-sass]]: partials do Sass por categoria
- [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]: NLW #2, Diego, dia 1: PageHeader e TeacherItem como componentes compartilhados
- [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]]: NLW #2, Diego, dia 3: Input, Textarea e Select compartilhados
- [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]]: NLW #2, Diego, dia 4: PageHeader no app
- [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]]: NLW #2, Diego, dia 5: TeacherItem no app
- [[wiki/sources/frontpush-conceitos-gerais-react-interface-dinamica-spa-virtual-dom-jsx]]: FrontPUSH, React aula 03: "seccionar a minha página" em componentes
- [[wiki/sources/frontpush-spa-componentes-estrutura-app-js-componentizacao]]: FrontPUSH, React aula 05: App.js > header, sidebar, content, footer; organização, encapsulamento, aninhamento, reuso; performance é da reconciliação, não da divisão
- [[wiki/sources/frontpush-jsx-webpack-babel-react-createelement-create-react-app]]: FrontPUSH, React aula 06: componentes "tripartidos" (HTML, CSS, JS) renderizados pelo JavaScript
