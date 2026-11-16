---
type: concept
title: "Renderização condicional (React)"
aliases: ["conditional rendering", "&& no JSX", "ternário no JSX", "early return"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 4
tags: [react, react-native, jsx]
skill: tech-mentor-mobile
status: stub
---

# Renderização condicional (React)

Mostrar ou não um trecho de JSX conforme o estado. As formas comuns: ternário (`cond ? <A /> : <B />`), `&&` quando não há "senão" (`cond && <A />`) e *early return* (`if (!data) return <Loading />`).

Na aula de [[wiki/entities/diego-fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]), o mapa só aparece depois da localização chegar: `initialPosition[0] !== 0 && (<MapView ... />)`. Antes disso, o `initialRegion` em `[0, 0]` abriria no oceano e não se moveria. "Quando eu não tenho o else [...] eu posso botar e-comercial." A tela de detalhe usa *early return*, `if (!data.point) return null`.

**Pegadinhas:**

- **`&&` com número:** `count && <List />` com `count = 0` renderiza o `0`. No React Native, isso quebra com "Text strings must be rendered within a `<Text>` component", o mesmo erro da aula. Use comparações booleanas (`count > 0 &&`) ou `!!count`.
- **Sentinelas como `0`:** "não carregou" e "deu erro" ficam indistinguíveis, porque a posição pode ser legitimamente 0. Um estado explícito (`'loading' | 'ready' | 'denied'`) deixa o fluxo claro, inclusive o caso de permissão negada, que na aula deixa a tela sem mapa para sempre.
- **`return null` não é loading:** a tela fica vazia sem indicação.

Relacionado: [[wiki/concepts/jsx]], [[wiki/concepts/useState]], [[wiki/concepts/maquina-de-estados-ui]].

## Na NLW #2, dia 3 (Diego Fernandes)

`{props.description && <p>...</p>}` no lugar do ternário com `null`, explicado pelo truthy. Funciona com string; com número, o `0` seria renderizado. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]].

## Na NLW #2, dia 4 (Diego Fernandes)

`if (!fontsLoaded) return <AppLoading />` até as fontes do `useFonts` carregarem, para "parecer que o app ainda está carregando". Ver [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]].

## Na NLW #2, dia 5 (Diego Fernandes)

`{isFiltersVisible && (<View>...</View>)}` para mostrar e esconder os filtros, e `{headerRight}` no header; ternário para ícone e estilo do favorito. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: MapView condicionado à posição; early return no detalhe
- [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]]: NLW #2, Diego, dia 3: && para a descrição opcional
- [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]]: NLW #2, Diego, dia 4: AppLoading até as fontes
- [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]]: NLW #2, Diego, dia 5: filtros com && e headerRight
