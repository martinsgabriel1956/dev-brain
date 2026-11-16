---
type: entity
title: "React Navigation"
aliases: ["@react-navigation/native", "react-navigation", "createStackNavigator", "NavigationContainer"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 3
tags: [react-native, navegacao, mobile, biblioteca]
skill: tech-mentor-mobile
status: stub
---

# React Navigation

Biblioteca de navegação mais usada no [[wiki/entities/react-native]]. Um `NavigationContainer` guarda o estado de navegação, e dentro dele vão navegadores em pilha (stack), abas (bottom tabs) ou drawer.

Na NLW #1 com [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]), na versão 5:

- **Estrutura:** `createStackNavigator()`, `<AppStack.Navigator headerMode="none" screenOptions={{ cardStyle }}>` e `<AppStack.Screen name component />`. Ver [[wiki/concepts/navegacao-em-pilha]].
- **Navegar:** `useNavigation()` dá `navigate('Points')`, `navigate('Detail', { point_id })` e `goBack()`. `useRoute().params` lê os parâmetros.
- **Comparação com a web:** o `NavigationContainer` faz o papel do `BrowserRouter` do [[wiki/entities/react-router]]. A diferença é que as telas têm nome, não URL.
- **Dependências nativas:** gesture-handler, reanimated, screens, safe-area-context e masked-view.

**Depois de 2020:**

- **v6/v7:** `headerMode` virou `screenOptions={{ headerShown: false }}`, e o *native stack* (`@react-navigation/native-stack`), com transições nativas, é o recomendado.
- **Tipagem:** `RootStackParamList` tipa as rotas e dispensa o `as Params` da aula.
- **Expo Router:** o template padrão do Expo hoje é o Expo Router, roteamento por arquivos construído sobre o React Navigation. `[skill: tech-mentor-mobile]`

Relacionado: [[wiki/concepts/mobile-navegacao]], [[wiki/concepts/client-side-routing]].

## Na NLW #2, dia 4 (Diego Fernandes)

v5: `createStackNavigator` + `createBottomTabNavigator` encadeados, `screenOptions={{ headerShown: false }}`, `tabBarOptions` (removido no v6), `useNavigation`, `navigate`/`goBack`; traz o `react-native-gesture-handler` (RectButton, BorderlessButton). Ver [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]].

## Na NLW #2, dia 5 (Diego Fernandes)

`useFocusEffect` para recarregar a aba Favoritos (as abas não remontam); a documentação pede `useCallback`. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: stack navigator do Ecoleta mobile
- [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]]: NLW #2, Diego, dia 4: stack + tabs encadeados no Proffy
- [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]]: NLW #2, Diego, dia 5: useFocusEffect
