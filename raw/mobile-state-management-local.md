---
date: 2026-04-23
tags: [tech-mentor, mobile, state-management, react-native, flutter, android, ios]
skill: tech-mentor-mobile/references/state-management
level: fundamento
---

# State Management Local — Mobile

## Contexto
State local é o estado que vive dentro de um componente/widget e não precisa ser compartilhado. É a primeira ferramenta a dominar — quem usa estado global para tudo paga o custo de complexidade sem necessidade. O princípio: coloque o estado o mais próximo possível de onde ele é usado.

## Como Funciona

### React Native — useState + useReducer

```typescript
// Estado simples — formulário
export function LoginForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  async function handleSubmit() {
    setIsLoading(true);
    try {
      await login({ email, password });
    } finally {
      setIsLoading(false);
    }
  }

  return (/* ... */);
}
```

```typescript
// Estado complexo com transições — useReducer
type State = {
  status: "idle" | "loading" | "success" | "error";
  data: User | null;
  error: string | null;
};

type Action =
  | { type: "FETCH_START" }
  | { type: "FETCH_SUCCESS"; payload: User }
  | { type: "FETCH_ERROR"; payload: string };

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case "FETCH_START":
      return { status: "loading", data: null, error: null };
    case "FETCH_SUCCESS":
      return { status: "success", data: action.payload, error: null };
    case "FETCH_ERROR":
      return { status: "error", data: null, error: action.payload };
    default:
      return state;
  }
}

export function UserProfile({ userId }: { userId: string }) {
  const [state, dispatch] = useReducer(reducer, {
    status: "idle",
    data: null,
    error: null
  });

  useEffect(() => {
    dispatch({ type: "FETCH_START" });
    fetchUser(userId)
      .then(user => dispatch({ type: "FETCH_SUCCESS", payload: user }))
      .catch(err => dispatch({ type: "FETCH_ERROR", payload: err.message }));
  }, [userId]);

  if (state.status === "loading") return <ActivityIndicator />;
  if (state.status === "error") return <ErrorView message={state.error!} />;
  if (!state.data) return null;
  return <UserCard user={state.data} />;
}
```

### Flutter — setState + StatefulWidget

```dart
class CounterWidget extends StatefulWidget {
  const CounterWidget({super.key});

  @override
  State<CounterWidget> createState() => _CounterWidgetState();
}

class _CounterWidgetState extends State<CounterWidget> {
  int _count = 0;
  bool _isLoading = false;

  void _increment() {
    setState(() => _count++);
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text("$_count"),
        ElevatedButton(onPressed: _increment, child: const Text("+")),
      ],
    );
  }
}
```

```dart
// Flutter moderno — hooks_riverpod ou flutter_hooks para estado funcional
// Alternativa sem StatefulWidget: ValueNotifier
class CounterPage extends StatelessWidget {
  final _count = ValueNotifier<int>(0);

  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder<int>(
      valueListenable: _count,
      builder: (ctx, value, _) => Text("$value"),
    );
  }
}
```

### Android Compose — remember + rememberSaveable

```kotlin
@Composable
fun Counter() {
  // remember: sobrevive à recomposição, mas NÃO a mudanças de configuração
  var count by remember { mutableStateOf(0) }

  // rememberSaveable: sobrevive a rotação de tela e process death
  var savedCount by rememberSaveable { mutableStateOf(0) }

  Button(onClick = { count++ }) {
    Text("Count: $count")
  }
}
```

### iOS SwiftUI — @State + @StateObject

```swift
struct CounterView: View {
  @State private var count = 0          // primitivos e structs
  @StateObject private var vm = CounterViewModel()  // classes/ObservableObject

  var body: some View {
    VStack {
      Text("\(count)")
      Button("Increment") { count += 1 }
    }
  }
}
```

## Trade-offs

| Aspecto | useState/setState | useReducer/Bloc | remember | @State |
|---|---|---|---|---|
| Complexidade | Baixa | Média | Baixa | Baixa |
| Testabilidade | Difícil (isolado) | Alta (lógica separada) | Difícil | Difícil |
| Debug | Console.log | State máquina clara | Recomposition inspector | Xcode debugger |
| Quando usar | Formulários simples | Fluxos com múltiplos estados | Qualquer UI local | Primitivos SwiftUI |

## Quando Usar / Quando Evitar

**Use estado local quando:** o estado não é compartilhado entre telas, é efêmero (loading, form input, toggle), ou é derivável de props/params.

**Evite estado local quando:** múltiplos componentes precisam ler/escrever, o estado precisa persistir entre navegações, ou ele afeta lógica de negócio fora da UI.

**Regra prática:** se você está passando estado por mais de 2 níveis de props (prop drilling), mova para estado global ou Context.

## Conceitos Relacionados
[[mobile-state-management-global]] · [[mobile-navegacao]] · [[mobile-chamadas-http]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
