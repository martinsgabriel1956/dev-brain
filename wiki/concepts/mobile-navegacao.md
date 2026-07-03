---
type: concept
title: "Navegação Mobile"
aliases: ["react navigation", "navigation compose", "gorouter flutter", "mobile routing"]
date_created: 2026-04-24
date_updated: 2026-07-03
source_count: 2
tags: [mobile, navegacao, react-navigation, navigation-compose, gorouter, stack, tab]
skill: tech-mentor-mobile
status: stable
---

# Navegação Mobile

## Padrão: Tab → Stack

```
TabNavigator (root)
├── HomeTab → Stack(HomeScreen → ProductScreen → CheckoutScreen)
├── SearchTab → Stack(SearchScreen → ResultScreen)
└── ProfileTab → Stack(ProfileScreen → SettingsScreen)
```

Tab no root — Stack dentro de cada tab. Mantém histórico por tab independente.

## React Navigation

```ts
type RootStackParams = {
    Home: undefined;
    Product: { id: string };
    Checkout: { productId: string; quantity: number };
};

const Stack = createNativeStackNavigator<RootStackParams>();

function AppNavigator() {
    return (
        <NavigationContainer linking={linking}>
            <Stack.Navigator>
                <Stack.Screen name="Home" component={HomeScreen} />
                <Stack.Screen name="Product" component={ProductScreen} />
            </Stack.Navigator>
        </NavigationContainer>
    );
}
```

## Android — Navigation Compose

```kotlin
@Serializable data class Product(val id: String)

NavHost(navController, startDestination = Home) {
    composable<Home> { HomeScreen(onNavigate = { navController.navigate(Product(it)) }) }
    composable<Product> { backStackEntry ->
        val product: Product = backStackEntry.toRoute()
        ProductScreen(productId = product.id)
    }
}
```

Rotas tipadas com Kotlin Serializable — sem string magic.

## Flutter — GoRouter

```dart
final router = GoRouter(routes: [
    GoRoute(path: '/', builder: (ctx, state) => HomeScreen()),
    GoRoute(path: '/product/:id', builder: (ctx, state) => ProductScreen(id: state.pathParameters['id']!)),
]);
```

## O Risco Escondido: Memória e Ciclo de Vida

Cada tela empilhada na navigation stack não é "de graça" — ela segura estado, imagens, listeners e a árvore de views inteira na memória. Se o ciclo de vida de cada tela (criada → ativa → pausada → destruída) não é gerenciado corretamente, a memória só sobe: telas que deveriam ter morrido continuam vivas, listeners que ninguém cancelou continuam escutando, imagens que ninguém liberou continuam ocupando RAM. O sintoma final é o sistema operacional matando o app por falta de memória. A diferença entre o app que trava e o que "voa" está exatamente em entender estado e ciclo de vida, não em empilhar mais uma tela. Ver [[wiki/sources/operador-de-crud-vs-engenheiro-repertorio]].

## Ver também

- [[mobile-deep-links]] — integrar deep links com navegação
- [[mobile-state-management-global]] — onde estado de navegação NÃO vai

## Key Sources

- [[wiki/sources/mobile-navegacao]]
- [[wiki/sources/operador-de-crud-vs-engenheiro-repertorio]] — vazamento de memória por navigation stack e ciclo de vida mal gerenciados; OOM kill como sintoma final
