---
type: concept
title: "Componentização"
aliases: ["componentes", "component-based UI", "componente React"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 3
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

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: botão reutilizável, diagrama de comentários
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: Header reutilizável; uma pasta por página
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: telas como componentes no RN
