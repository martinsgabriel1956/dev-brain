---
type: entity
title: "Google Fonts"
aliases: ["fonts.google.com", "Google Web Fonts"]
date_created: 2026-11-15
date_updated: 2026-11-16
source_count: 9
tags: [ferramenta, produto, google, tipografia, fonte, fontes, gratuito, css, frontend]
skill: ux-ui-mentor
status: stub
---

# Google Fonts

Catálogo gratuito de fontes do [[wiki/entities/google]] em fonts.google.com, com código pronto para usar no site. Ver [[wiki/concepts/tipografia]].

## Principal referência do autor

- **Ao lado do Adobe Fonts:** para [[wiki/entities/nasser|Násser]], é "a principal referência que eu tenho" para baixar fontes ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]); na aula de classificações, é um dos "dois principais sites" de fontes, junto com o [[wiki/entities/adobe-fonts]] ([[wiki/sources/classificacoes-tipograficas-serifa-sem-serifa-script-monoespacada-display]]).
- **Gratuito:** "a grande maioria ou senão a total maioria, todas as fontes aqui são gratuitas" ([[wiki/sources/classificacoes-tipograficas-serifa-sem-serifa-script-monoespacada-display]]). Na aula de combinações, a gratuidade é um dos motivos para escolher a Mukta ([[wiki/sources/escolhendo-e-combinando-tipografias-pesquisa-contraste-duas-typefaces]]); ver [[wiki/concepts/licenca-de-fontes]].
- **Espelhado no [[wiki/entities/figma]]:** fonte nova "automaticamente vai aparecer no Figma sem precisar você baixar, sem precisar você instalar". Por isso ele presta "bem mais atenção" nesse catálogo ([[wiki/sources/classificacoes-tipograficas-serifa-sem-serifa-script-monoespacada-display]]).

`[external]` As fontes do Google Fonts vêm disponíveis no Figma por padrão, mas a lista é atualizada pelo Figma, não em tempo real. No Linux, onde o Figma não lê fontes locais, é praticamente o único catálogo à mão (https://help.figma.com/hc/articles/360039956894). Confiança média.

## Filtros e pesos

- **Filtros por [[wiki/concepts/classificacao-tipografica|classificação]]:** serif, sans serif, display, handwriting, monospace ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]). A categoria de cursivas (script) aparece com o nome handwriting ([[wiki/sources/classificacoes-tipograficas-serifa-sem-serifa-script-monoespacada-display]]).
- **Escolha de pesos:** no exemplo da Lato, light, normal e bold ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]). Na aula de combinações, a página da Mukta mostra pesos de Extra Light a Extra Bold ([[wiki/sources/escolhendo-e-combinando-tipografias-pesquisa-contraste-duas-typefaces]]).

## Código para o site

Um `<link>` para o HTML ou um `@import` para o CSS; ele prefere o `<link>`, "mais performático" ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]). Ver [[wiki/concepts/webfonts]].

`[external]` As fontes são de licença aberta, a maioria sob a SIL Open Font License, e podem ser baixadas e hospedadas no próprio servidor em vez de carregadas da CDN do Google (https://fonts.google.com/about). São de código aberto e liberadas para uso comercial (https://developers.google.com/fonts/faq).

## Fonte dos pares da aula de combinações

Em [[wiki/sources/escolhendo-e-combinando-tipografias-pesquisa-contraste-duas-typefaces]], todos os oito pares sugeridos estão no Google Fonts ([[wiki/concepts/combinacao-de-fontes]]).

## Na aula de CSS

Em [[wiki/sources/principais-propriedades-css-color-background-font]], [[wiki/entities/nasser|Násser]] contrasta "download family" (zip para instalar) com "select style" + `<link>` para o site. `[external]` São botões da interface antiga; hoje o fluxo é "Get font" → "Get embed code".

## Na NLW #1 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] escolhe Roboto 300/700 para o texto e Ubuntu 700 para os títulos, copiando o `<link>` e a regra `font-family` sugerida. Fonte de nome único dispensa aspas.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]], Roboto 400 e Ubuntu 700 são carregadas por `<link>` no `index.html` do React; Diego chama o serviço de "o repositório de fontes mais confiável".

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]], o Expo Google Fonts (`@expo-google-fonts/roboto` e `/ubuntu`, `useFonts`) carrega Roboto 400/500 e Ubuntu 700 no app. Para Diego, "pergunta para qualquer desenvolvedor o trabalho que dá" fazer isso à mão.

## Na NLW #2, dia 1 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]], a Poppins entra por um `<link>` do Google Fonts colado antes de fechar o head, e a regra `font: 500 1.6rem Poppins` vai em `body, input, button, textarea`, porque o botão não herda a fonte do body.

## Na NLW #2, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]], os botões e títulos usam Archivo, importada só nos pesos 400 e 700. Pedir 600 sem importar muda pouco; importar o 600 é possível, mas "não vale a pena" pelo peso extra.

## Key Sources

- [[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]: principal referência de fontes; filtros, pesos, `<link>` x `@import`
- [[wiki/sources/classificacoes-tipograficas-serifa-sem-serifa-script-monoespacada-display]]: catálogo gratuito espelhado no Figma; script como handwriting
- [[wiki/sources/escolhendo-e-combinando-tipografias-pesquisa-contraste-duas-typefaces]]: origem dos oito pares; Mukta como exemplo de família ampla e gratuita
- [[wiki/sources/principais-propriedades-css-color-background-font]]: download family x select style + link; font-family no H1
- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: Roboto e Ubuntu na NLW #1
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: Roboto e Ubuntu no Ecoleta web
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: Expo Google Fonts no app
- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: NLW #2, dia 1: Poppins no Proffy
- [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]: NLW #2, dia 2: Archivo 400 e 700
