---
type: concept
title: "State Management Local — Mobile"
aliases: ["viewmodel android compose", "stateful widget flutter", "usestate react native local"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [mobile, state-local, viewmodel, stateful-widget, useState, stateflow]
skill: tech-mentor-mobile
status: stable
---

# State Management Local — Mobile

Estado local primeiro — elevar para global apenas quando necessário.

## React Native — useState / useReducer

```ts
// Estado simples
const [isExpanded, setIsExpanded] = useState(false);

// Estado complexo — múltiplas ações relacionadas
type FormState = { name: string; email: string; error: string | null };
type FormAction = { type: 'SET_NAME'; value: string } | { type: 'SUBMIT_ERROR'; error: string };

const [form, dispatch] = useReducer((state: FormState, action: FormAction): FormState => {
    switch (action.type) {
        case 'SET_NAME': return { ...state, name: action.value };
        case 'SUBMIT_ERROR': return { ...state, error: action.error };
    }
}, { name: '', email: '', error: null });
```

## Android — ViewModel + StateFlow

```kotlin
class ProductViewModel(private val repo: ProductRepository) : ViewModel() {
    private val _uiState = MutableStateFlow<UiState>(UiState.Loading)
    val uiState: StateFlow<UiState> = _uiState.asStateFlow()

    fun loadProduct(id: String) = viewModelScope.launch {
        _uiState.value = UiState.Loading
        _uiState.value = repo.getProduct(id)
            .fold(UiState::Error, UiState::Success)
    }
}

// ViewModel sobrevive a rotação de tela
val viewModel: ProductViewModel by viewModels()
val uiState by viewModel.uiState.collectAsStateWithLifecycle()
```

`rememberSaveable` para estado que deve sobreviver ao process kill (ex: scroll position, texto digitado).

## Flutter — StatefulWidget / ValueNotifier

```dart
class CounterWidget extends StatefulWidget {
    @override
    State<CounterWidget> createState() => _CounterWidgetState();
}

class _CounterWidgetState extends State<CounterWidget> {
    int _count = 0;

    @override
    Widget build(BuildContext context) {
        return Column(children: [
            Text('$_count'),
            ElevatedButton(
                onPressed: () => setState(() => _count++),
                child: Text('Incrementar'),
            ),
        ]);
    }
}
```

`ValueNotifier` para estado sem reconstruir toda a árvore — `ValueListenableBuilder` consome.

## Ver também

- [[mobile-state-management-global]] — quando elevar para global
- [[mobile-layouts-responsivos]] — estado de layout (breakpoints) é local

## Key Sources

- [[wiki/sources/mobile-state-management-local]]
