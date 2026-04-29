---
date: 2026-04-23
tags: [tech-mentor, mobile, navegação, react-native, flutter, android, ios]
skill: tech-mentor-mobile/references/navegacao
level: fundamento
---

# Navegação Mobile

## Contexto
Navegação é o esqueleto de qualquer app. A escolha da lib e do modelo de navegação impacta diretamente a DX, performance de transições e o suporte a deep links. Cada plataforma tem seu paradigma nativo — entender as abstrações é o que separa quem usa de quem decide.

## Como Funciona

### React Native — React Navigation vs Expo Router

**React Navigation** é orientado a configuração imperativa: você define uma stack/tab/drawer e navega programaticamente.

```typescript
// Stack navigator típico
import { createNativeStackNavigator } from "@react-navigation/native-stack";

type RootStack = {
  Home: undefined;
  Profile: { userId: string };
};

const Stack = createNativeStackNavigator<RootStack>();

export function RootNavigator() {
  return (
    <Stack.Navigator initialRouteName="Home">
      <Stack.Screen name="Home" component={HomeScreen} />
      <Stack.Screen name="Profile" component={ProfileScreen} />
    </Stack.Navigator>
  );
}

// Navegação tipada
navigation.navigate("Profile", { userId: "abc123" });
```

**Expo Router** é file-based (como Next.js App Router): a estrutura de pastas define as rotas. Nativamente integrado a deep links e URL-based navigation.

```
app/
├── index.tsx          → /
├── profile/
│   └── [id].tsx       → /profile/:id
└── (tabs)/
    ├── feed.tsx       → tab 1
    └── explore.tsx    → tab 2
```

```typescript
// Expo Router — navegar
import { router } from "expo-router";
router.push("/profile/abc123");

// Ler params
import { useLocalSearchParams } from "expo-router";
const { id } = useLocalSearchParams<{ id: string }>();
```

### Flutter — GoRouter vs Navigator 2.0

**GoRouter** é o padrão recomendado pelo Flutter team. URL-based, suporta deep links nativamente.

```dart
final router = GoRouter(
  routes: [
    GoRoute(path: "/", builder: (ctx, state) => const HomeScreen()),
    GoRoute(
      path: "/profile/:id",
      builder: (ctx, state) => ProfileScreen(id: state.pathParameters["id"]!),
    ),
  ],
);

// Navegar
context.go("/profile/abc123");
context.push("/profile/abc123"); // empilha, pode voltar
```

### Android — Navigation Compose

```kotlin
@Composable
fun AppNavHost(navController: NavHostController) {
  NavHost(navController, startDestination = "home") {
    composable("home") { HomeScreen(navController) }
    composable("profile/{userId}") { backStack ->
      val userId = backStack.arguments?.getString("userId")!!
      ProfileScreen(userId)
    }
  }
}

// Navegar
navController.navigate("profile/abc123")
```

### iOS — NavigationStack (SwiftUI)

```swift
@State private var path = NavigationPath()

NavigationStack(path: $path) {
  HomeView()
    .navigationDestination(for: String.self) { userId in
      ProfileView(userId: userId)
    }
}

// Navegar programaticamente
path.append("abc123")
```

## Trade-offs

| Aspecto | React Navigation | Expo Router | GoRouter | Navigation Compose | NavigationStack |
|---|---|---|---|---|---|
| Curva de aprendizado | Média | Baixa (file-based) | Baixa | Média | Baixa |
| Deep links | Manual | Automático | Automático | Manual | Manual |
| Type-safety | Com generics | Parcial | Fraco | Com sealed classes | Fraco |
| Controle fino | Alto | Médio | Alto | Alto | Alto |
| Tela modal/bottom sheet | Plugin externo | Nativo | Nativo | Nativo | Nativo |

## Quando Usar / Quando Evitar

**Use Expo Router se:** novo projeto RN, quer zero config de deep links, equipe web vindo do Next.js.

**Use React Navigation se:** projeto existente, precisa de controle fino sobre animações, app sem URL-based routing.

**Use GoRouter se:** Flutter — sempre. Navigator 2.0 puro é verboso demais sem benefício real.

**Navigation Compose se:** Android nativo com Jetpack Compose — é o padrão atual.

**NavigationStack se:** SwiftUI iOS 16+. Para projetos legados, usar UINavigationController.

## Conceitos Relacionados
[[mobile-deep-links]] · [[mobile-state-management-global]] · [[mobile-offline-first-basico]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
