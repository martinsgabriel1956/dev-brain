---
type: concept
title: "State Management Global — Mobile"
aliases: ["zustand mobile", "redux toolkit mobile", "riverpod flutter", "bloc flutter"]
date_created: 2026-04-24
date_updated: 2026-11-16
source_count: 2
tags: [mobile, state-management, zustand, redux, riverpod, bloc, global-state]
skill: tech-mentor-mobile
status: stable
---

# State Management Global — Mobile

## Quando Usar Estado Global

- Dados de autenticação (usuário logado, tokens)
- Carrinho de compras (compartilhado entre telas)
- Tema / configurações do app
- Notificações não lidas (badge count)

**Nunca:** server state (dados do servidor), estado de navegação, estado de formulário.

## React Native — Zustand

```ts
type AuthStore = {
    user: User | null;
    isLoggedIn: boolean;
    login: (user: User) => void;
    logout: () => void;
};

const useAuthStore = create<AuthStore>()(
    persist(
        set => ({
            user: null,
            isLoggedIn: false,
            login: user => set({ user, isLoggedIn: true }),
            logout: () => set({ user: null, isLoggedIn: false }),
        }),
        { name: 'auth-storage', storage: createJSONStorage(() => mmkvStorage) }
    )
);
```

## Flutter — Riverpod

```dart
final authProvider = StateNotifierProvider<AuthNotifier, AuthState>((ref) {
    return AuthNotifier(ref.watch(authRepositoryProvider));
});

// Consumir
final auth = ref.watch(authProvider);
if (auth.isLoggedIn) return HomeScreen();
return LoginScreen();
```

## Flutter — Bloc

```dart
// Events e States explícitos — rastreável, testável
class AuthBloc extends Bloc<AuthEvent, AuthState> {
    AuthBloc() : super(AuthInitial()) {
        on<LoginRequested>((event, emit) async {
            emit(AuthLoading());
            final result = await authRepo.login(event.credentials);
            result.fold(
                (error) => emit(AuthFailure(error)),
                (user) => emit(AuthSuccess(user)),
            );
        });
    }
}
```

Bloc para fluxos com eventos complexos e muitos estados — maior verbosidade, maior rastreabilidade.

## Ver também

- [[wiki/concepts/mobile-state-management-local]] — estado local primeiro
- [[wiki/concepts/mobile-chamadas-http]] — TanStack Query / Riverpod para server state

## Na NLW #2, dia 5 (Diego Fernandes)

O favorito removido numa aba continua marcado na outra; Diego aponta Context API ou Redux como saída. Parte do problema é local: `useState(favorited)` não acompanha a prop. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]].

## Key Sources

- [[wiki/sources/mobile-state-management-global]]
- [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]]: NLW #2, Diego, dia 5: favoritos entre abas
