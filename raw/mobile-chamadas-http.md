---
date: 2026-04-23
tags: [tech-mentor, mobile, http, api, loading-states, error-handling, react-native, flutter]
skill: tech-mentor-mobile/references/chamadas-http
level: fundamento
---

# Chamadas HTTP + Loading States + Error Handling — Mobile

## Contexto
HTTP é a fronteira mais crítica de um app mobile: latência variável, conexão instável, erros de servidor, timeouts. Um app robusto trata os três estados (loading, success, error) de forma explícita em cada chamada — e nunca deixa o usuário em tela branca sem feedback.

## Como Funciona

### React Native — TanStack Query (padrão recomendado)

TanStack Query gerencia cache, refetch, loading e error automaticamente.

```typescript
// query client no root
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: 2,
      staleTime: 5 * 60 * 1000, // 5 min
      gcTime: 10 * 60 * 1000
    }
  }
});

export function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <RootNavigator />
    </QueryClientProvider>
  );
}
```

```typescript
// Serviço HTTP centralizado com Axios
import axios from "axios";

const http = axios.create({
  baseURL: process.env.EXPO_PUBLIC_API_URL,
  timeout: 10_000
});

http.interceptors.request.use(config => {
  const token = useAuthStore.getState().token;
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

http.interceptors.response.use(
  res => res,
  err => {
    if (err.response?.status === 401) useAuthStore.getState().logout();
    return Promise.reject(err);
  }
);
```

```typescript
// Hook de query tipado
type User = { id: string; name: string; email: string };

async function fetchUser(id: string): Promise<User> {
  const { data } = await http.get<User>(`/users/${id}`);
  return data;
}

export function useUser(id: string) {
  return useQuery({
    queryKey: ["user", id],
    queryFn: () => fetchUser(id),
    enabled: !!id
  });
}

// Mutation com invalidação de cache
export function useUpdateUser() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (data: Partial<User>) => http.patch("/users/me", data),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ["user"] })
  });
}
```

```typescript
// Componente com os 3 estados explícitos
export function UserProfile({ userId }: { userId: string }) {
  const { data: user, isLoading, isError, error } = useUser(userId);

  if (isLoading) return <ActivityIndicator size="large" />;

  if (isError) {
    return (
      <ErrorView
        message={error instanceof Error ? error.message : "Erro ao carregar"}
      />
    );
  }

  return <UserCard user={user!} />;
}
```

### React Native — Fetch nativo (sem TanStack Query)

```typescript
// Custom hook com os 3 estados
export function useUserFetch(userId: string) {
  const [status, setStatus] = useState<"idle" | "loading" | "success" | "error">("idle");
  const [user, setUser] = useState<User | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const controller = new AbortController();

    async function load() {
      setStatus("loading");
      try {
        const res = await fetch(`${API_URL}/users/${userId}`, {
          signal: controller.signal
        });
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const data: User = await res.json();
        setUser(data);
        setStatus("success");
      } catch (err) {
        if ((err as Error).name === "AbortError") return;
        setError((err as Error).message);
        setStatus("error");
      }
    }

    load();
    return () => controller.abort();
  }, [userId]);

  return { status, user, error };
}
```

### Flutter — Dio + Riverpod

```dart
// Configuração do Dio
final dioProvider = Provider<Dio>(ref => {
  final dio = Dio(BaseOptions(
    baseUrl: Env.apiUrl,
    connectTimeout: const Duration(seconds: 10),
    receiveTimeout: const Duration(seconds: 10),
  ));

  dio.interceptors.add(InterceptorsWrapper(
    onRequest: (options, handler) {
      final token = ref.read(authProvider).token;
      if (token != null) options.headers["Authorization"] = "Bearer $token";
      handler.next(options);
    },
    onError: (error, handler) {
      if (error.response?.statusCode == 401) {
        ref.read(authProvider.notifier).logout();
      }
      handler.next(error);
    },
  ));

  return dio;
});

// Repository
class UserRepository {
  UserRepository(this._dio);
  final Dio _dio;

  Future<User> getUser(String id) async {
    final response = await _dio.get("/users/$id");
    return User.fromJson(response.data as Map<String, dynamic>);
  }
}

// Provider com AsyncValue (loading/data/error automático)
final userProvider = FutureProvider.family<User, String>((ref, id) async {
  return ref.watch(userRepositoryProvider).getUser(id);
});

// Widget
class UserProfileWidget extends ConsumerWidget {
  final String userId;
  const UserProfileWidget({required this.userId, super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final userAsync = ref.watch(userProvider(userId));
    return userAsync.when(
      loading: () => const CircularProgressIndicator(),
      error: (err, _) => ErrorWidget(err.toString()),
      data: (user) => UserCard(user: user),
    );
  }
}
```

### Android — Retrofit + Coroutines

```kotlin
// Interface do serviço
interface UserService {
  @GET("users/{id}")
  suspend fun getUser(@Path("id") id: String): UserResponse
}

// ViewModel
class UserViewModel(private val repository: UserRepository) : ViewModel() {
  private val _state = MutableStateFlow<UiState<User>>(UiState.Idle)
  val state = _state.asStateFlow()

  fun loadUser(id: String) {
    viewModelScope.launch {
      _state.value = UiState.Loading
      repository.getUser(id)
        .fold(
          onSuccess = { _state.value = UiState.Success(it) },
          onFailure = { _state.value = UiState.Error(it.message ?: "Erro") }
        )
    }
  }
}
```

## Trade-offs

| Abordagem | Cache | Retry | Boilerplate | Offline support |
|---|---|---|---|---|
| TanStack Query | Automático | Configurável | Baixo | Com persist plugin |
| Fetch/useEffect manual | Nenhum | Manual | Médio | Manual |
| Riverpod FutureProvider | Por widget | Manual | Baixo | Com Hive |
| Retrofit + Coroutines | Nenhum | OkHttp interceptor | Médio | Manual |

## Quando Usar / Quando Evitar

**Use TanStack Query/Riverpod** para qualquer GET que precise de cache, refetch em foco, ou deduplicação de requests.

**Use fetch/useEffect manual** apenas para POSTs simples sem necessidade de cache ou para prototipar.

**Sempre:** implementar timeout (10s), tratar 4xx/5xx separado de erros de rede, cancelar requests no cleanup do efeito (AbortController/CancelToken).

**Nunca:** deixar o usuário em tela branca sem loader, mostrar stack trace de erro para o usuário, fazer retry infinito sem backoff.

## Conceitos Relacionados
[[mobile-state-management-global]] · [[mobile-offline-first-basico]] · [[cache]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
