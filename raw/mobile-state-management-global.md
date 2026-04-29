---
date: 2026-04-23
tags: [tech-mentor, mobile, state-management, zustand, redux, riverpod, bloc, viewmodel]
skill: tech-mentor-mobile/references/state-management
level: fundamento
---

# State Management Global — Mobile

## Contexto
Estado global gerencia dados que cruzam telas: usuário autenticado, carrinho, tema, cache de lista. A escolha da solução impacta testabilidade, DX e performance. O erro mais comum é usar estado global para tudo — o custo de re-renders/reconstruções desnecessárias é real em mobile.

## Como Funciona

### React Native — Zustand (recomendado para novos projetos)

Zustand é minimalista: store como hook, sem boilerplate, sem Provider obrigatório.

```typescript
import { create } from "zustand";
import { persist, createJSONStorage } from "zustand/middleware";
import AsyncStorage from "@react-native-async-storage/async-storage";

type AuthState = {
  user: User | null;
  token: string | null;
  login: (user: User, token: string) => void;
  logout: () => void;
};

export const useAuthStore = create<AuthState>()(
  persist(
    set => ({
      user: null,
      token: null,
      login: (user, token) => set({ user, token }),
      logout: () => set({ user: null, token: null })
    }),
    {
      name: "auth-storage",
      storage: createJSONStorage(() => AsyncStorage)
    }
  )
);

// Uso no componente — só selecionar o que precisa (evita re-renders)
export function Header() {
  const user = useAuthStore(state => state.user);
  return <Text>{user?.name}</Text>;
}
```

### React Native — Redux Toolkit (projetos enterprise com estado complexo)

```typescript
// slice
import { createSlice, PayloadAction } from "@reduxjs/toolkit";

const cartSlice = createSlice({
  name: "cart",
  initialState: { items: [] as CartItem[], total: 0 },
  reducers: {
    addItem(state, action: PayloadAction<CartItem>) {
      state.items.push(action.payload);
      state.total += action.payload.price;
    },
    removeItem(state, action: PayloadAction<string>) {
      state.items = state.items.filter(i => i.id !== action.payload);
    }
  }
});

export const { addItem, removeItem } = cartSlice.actions;

// Uso
const items = useAppSelector(state => state.cart.items);
dispatch(addItem({ id: "1", name: "Produto", price: 99.9 }));
```

### Flutter — Riverpod (padrão atual)

Riverpod substitui Provider com type-safety e sem BuildContext obrigatório para ler providers.

```dart
// Provider de autenticação
final authProvider = NotifierProvider<AuthNotifier, AuthState>(() {
  return AuthNotifier();
});

class AuthNotifier extends Notifier<AuthState> {
  @override
  AuthState build() => const AuthState.unauthenticated();

  Future<void> login(String email, String password) async {
    state = const AuthState.loading();
    try {
      final user = await ref.read(authRepositoryProvider).login(email, password);
      state = AuthState.authenticated(user);
    } catch (e) {
      state = AuthState.error(e.toString());
    }
  }
}

// Uso no widget
class ProfileScreen extends ConsumerWidget {
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final auth = ref.watch(authProvider);
    return auth.when(
      authenticated: (user) => Text(user.name),
      unauthenticated: () => const LoginScreen(),
      loading: () => const CircularProgressIndicator(),
      error: (msg) => Text(msg),
    );
  }
}
```

### Flutter — Bloc/Cubit (mais verboso, melhor para fluxos complexos)

```dart
// Cubit é um Bloc simplificado — sem eventos, só métodos
class CartCubit extends Cubit<CartState> {
  CartCubit() : super(CartState.empty());

  void addItem(Product product) {
    emit(state.copyWith(items: [...state.items, product]));
  }
}

// No widget
BlocBuilder<CartCubit, CartState>(
  builder: (context, state) => Text("${state.items.length} itens"),
)
```

### Android — ViewModel + StateFlow

```kotlin
class ProfileViewModel(
  private val userRepository: UserRepository
) : ViewModel() {

  private val _uiState = MutableStateFlow<ProfileUiState>(ProfileUiState.Loading)
  val uiState: StateFlow<ProfileUiState> = _uiState.asStateFlow()

  fun loadProfile(userId: String) {
    viewModelScope.launch {
      _uiState.value = ProfileUiState.Loading
      userRepository.getUser(userId)
        .onSuccess { user -> _uiState.value = ProfileUiState.Success(user) }
        .onFailure { e -> _uiState.value = ProfileUiState.Error(e.message ?: "Erro") }
    }
  }
}

// Composable
@Composable
fun ProfileScreen(viewModel: ProfileViewModel = hiltViewModel()) {
  val uiState by viewModel.uiState.collectAsStateWithLifecycle()
  when (uiState) {
    is ProfileUiState.Loading -> CircularProgressIndicator()
    is ProfileUiState.Success -> ProfileContent((uiState as ProfileUiState.Success).user)
    is ProfileUiState.Error -> ErrorView((uiState as ProfileUiState.Error).message)
  }
}
```

### iOS — ObservableObject + @Published / @Observable (iOS 17+)

```swift
// iOS 17+ com macro @Observable
@Observable
class AuthViewModel {
  var user: User? = nil
  var isLoading = false

  func login(email: String, password: String) async {
    isLoading = true
    defer { isLoading = false }
    user = try? await AuthService.shared.login(email: email, password: password)
  }
}

// Uso — sem @StateObject, @ObservedObject
struct ProfileView: View {
  @Environment(AuthViewModel.self) private var auth

  var body: some View {
    Text(auth.user?.name ?? "Sem usuário")
  }
}
```

## Trade-offs

| Solução | Boilerplate | Performance | Testabilidade | Persistência | Ideal para |
|---|---|---|---|---|---|
| Zustand | Mínimo | Alta (seletores) | Boa | Plugin persist | RN novos projetos |
| Redux Toolkit | Médio | Alta (selector memoization) | Excelente | Redux Persist | Enterprise/time grande |
| Riverpod | Baixo | Alta | Excelente | Hive/SharedPrefs | Flutter padrão |
| Bloc | Alto | Alta | Excelente | Hydrated Bloc | Flows complexos |
| ViewModel+StateFlow | Médio | Alta | Excelente | DataStore | Android nativo |
| @Observable | Mínimo | Alta | Boa | UserDefaults | iOS 17+ |

## Quando Usar / Quando Evitar

**Use global quando:** dados compartilhados entre 2+ telas, autenticação, carrinho, preferências de usuário, feature flags.

**Evite global quando:** estado efêmero de UI (loading de botão, texto de campo), estado derivado (prefira seletores/computed).

**Anti-pattern crítico:** colocar todo o estado da aplicação em um único store monolítico sem seletores — resulta em re-renders em cascata.

## Conceitos Relacionados
[[mobile-state-management-local]] · [[mobile-chamadas-http]] · [[mobile-armazenamento-local]] · [[mobile-offline-first-basico]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
