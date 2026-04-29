# React — Tudo que você precisa saber

## O que é React

React é uma **biblioteca JavaScript para construir interfaces de usuário** (não um framework completo). Criado pelo Facebook em 2013, seu modelo mental central é simples: **UI = f(state)** — dado um estado, a UI é uma função determinística dele.

---

## Conceitos Fundamentais

### 1. Componentes

A unidade básica do React. Um componente é uma função que recebe **props** e retorna JSX.

```typescript
type UserCardProps = {
  name: string;
  email: string;
  isAdmin: boolean;
};

export function UserCard({ name, email, isAdmin }: UserCardProps) {
  return (
    <div>
      <h2>{name}</h2>
      <p>{email}</p>
      {isAdmin && <span>Admin</span>}
    </div>
  );
}
```

**Regras de ouro:**
- Sempre `function declaration`, nunca arrow function ou `React.FC`
- Componentes reutilizáveis: `named export`. Páginas Next.js: `default export`
- Um componente = uma responsabilidade. Mais de 3 → quebre

---

### 2. JSX

Sintaxe que parece HTML mas é JavaScript. Compilado para `React.createElement(...)`.

```typescript
// JSX
const el = <h1 className="title">Olá</h1>;

// O que o compilador gera
const el = React.createElement("h1", { className: "title" }, "Olá");
```

**Detalhes importantes:**
- `class` → `className`, `for` → `htmlFor`
- Expressões JS dentro de `{}`
- Elementos JSX precisam de uma raiz única — use `<>...</>` (Fragment)

---

### 3. Estado — `useState`

Estado é **memória local do componente**. Quando muda, o componente re-renderiza.

```typescript
function Counter() {
  const [count, setCount] = useState(0);

  return (
    <button onClick={() => setCount(prev => prev + 1)}>
      Cliques: {count}
    </button>
  );
}
```

**Regra crítica:** sempre use callback quando o novo estado depende do anterior:
```typescript
// ✅ Correto — sem risco de stale closure
setCount(prev => prev + 1);

// ❌ Errado — pode capturar valor antigo
setCount(count + 1);
```

---

### 4. Efeitos — `useEffect`

Sincroniza o componente com sistemas externos (API, DOM, timer, WebSocket).

```typescript
function UserProfile({ userId }: { userId: string }) {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    const controller = new AbortController();

    fetchUser(userId, { signal: controller.signal }).then(setUser);

    return () => controller.abort(); // cleanup — evita memory leak
  }, [userId]); // roda toda vez que userId mudar

  if (!user) return <Spinner />;
  return <div>{user.name}</div>;
}
```

**Array de dependências:**
- `[]` → roda só uma vez (mount)
- `[dep1, dep2]` → roda quando dep1 ou dep2 mudar
- Sem array → roda em todo render (raramente o que você quer)

**⚠️ Nunca ignore warnings de dependências.** O linter está certo.

---

### 5. Refs — `useRef`

Dois usos principais: **acessar o DOM** e **guardar valores sem causar re-render**.

```typescript
// Acessar DOM
function AutoFocusInput() {
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  return <input ref={inputRef} />;
}

// Guardar valor sem re-render (ex: ID de timer)
function Timer() {
  const intervalRef = useRef<NodeJS.Timeout | null>(null);

  function start() {
    intervalRef.current = setInterval(() => console.log({ message: "tick" }), 1000);
  }

  function stop() {
    if (intervalRef.current) clearInterval(intervalRef.current);
  }

  return <><button onClick={start}>Start</button><button onClick={stop}>Stop</button></>;
}
```

---

### 6. Context API

Compartilha estado entre componentes sem prop drilling. **Use para dados de baixa frequência de mudança** (tema, locale, usuário autenticado).

```typescript
type ThemeContextValue = {
  theme: "light" | "dark";
  toggleTheme: () => void;
};

const ThemeContext = createContext<ThemeContextValue | null>(null);

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<"light" | "dark">("light");

  const toggleTheme = useCallback(() => {
    setTheme(prev => prev === "light" ? "dark" : "light");
  }, []);

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme() {
  const ctx = useContext(ThemeContext);
  if (!ctx) throw new Error("useTheme must be used inside ThemeProvider");
  return ctx;
}
```

**⚠️ Problema:** todo consumidor re-renderiza quando o valor muda. Para estado que muda frequente, use Zustand.

---

### 7. `useReducer`

Alternativa ao `useState` para estado complexo com múltiplas ações relacionadas.

```typescript
type CartState = { items: CartItem[]; total: number };
type CartAction =
  | { type: "ADD_ITEM"; payload: CartItem }
  | { type: "REMOVE_ITEM"; payload: string }
  | { type: "CLEAR" };

function cartReducer(state: CartState, action: CartAction): CartState {
  switch (action.type) {
    case "ADD_ITEM":
      return {
        items: [...state.items, action.payload],
        total: state.total + action.payload.price
      };
    case "REMOVE_ITEM":
      const item = state.items.find(i => i.id === action.payload)!;
      return {
        items: state.items.filter(i => i.id !== action.payload),
        total: state.total - item.price
      };
    case "CLEAR":
      return { items: [], total: 0 };
  }
}

function Cart() {
  const [state, dispatch] = useReducer(cartReducer, { items: [], total: 0 });

  return (
    <div>
      {state.items.map(item => (
        <div key={item.id}>
          {item.name}
          <button onClick={() => dispatch({ type: "REMOVE_ITEM", payload: item.id })}>
            Remover
          </button>
        </div>
      ))}
      <p>Total: R$ {state.total}</p>
    </div>
  );
}
```

**Quando usar `useReducer` vs `useState`:**
- Mais de 2-3 estados relacionados que mudam juntos → `useReducer`
- Estado simples isolado → `useState`

---

### 8. Performance — `useMemo` e `useCallback`

Memoizam valores e funções para evitar recálculos desnecessários.

```typescript
function OrderList({ orders, filter }: { orders: Order[]; filter: string }) {
  const filteredOrders = useMemo(
    () => orders.filter(o => o.status === filter),
    [orders, filter]
  );

  const handleDelete = useCallback((id: string) => {
    deleteOrder(id);
  }, []);

  return <List items={filteredOrders} onDelete={handleDelete} />;
}
```

**Quando usar:**
- `useMemo`: cálculos caros (sort/filter de listas grandes, transformações complexas)
- `useCallback`: funções passadas como prop para componentes memoizados com `React.memo`

**⚠️ Não use em tudo** — tem custo de overhead. Meça antes.

---

## Ciclo de Vida (simplificado)

```
Mount     → componente aparece no DOM  → useEffect(fn, []) executa
Update    → estado/props muda          → useEffect(fn, [dep]) executa (se dep mudou)
Unmount   → componente sai do DOM      → cleanup function do useEffect executa
```

---

## Padrões de Componentes

### Compound Components
Componentes que compartilham estado implicitamente via Context — API estilo `<Select.Trigger>`.

### Container/Presenter
Separa lógica (fetch, state) do visual (JSX puro). Presenter é facilmente testável sem mocks.

### Custom Hooks
Extrai lógica stateful reutilizável para fora do componente:
```typescript
function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => setDebouncedValue(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);

  return debouncedValue;
}
```

---

## Quando usar o quê — Estado

| Situação | Solução |
|---|---|
| Estado local do componente | `useState` / `useReducer` |
| 2-3 componentes próximos | Lifting state + props |
| Tema, locale, auth | Context API |
| Estado global que muda frequente | Zustand / Jotai |
| Dados do servidor | TanStack Query / SWR |
| Estado na URL | nuqs |

---

## React 18/19 — Novidades Importantes

**Concurrent Mode (React 18):** React pode pausar e retomar renders para não travar a UI.

- `useTransition` — marca update como não urgente
- `useDeferredValue` — adia o uso de um valor em um filho

**React 19:**
- `use()` hook — consume Promises e Context de forma mais flexível
- `useActionState` — gerencia estado de forms com Server Actions
- **React Compiler** (beta) — elimina necessidade de `useMemo`/`useCallback` manual

---

## Error Boundaries

```typescript
import { ErrorBoundary } from "react-error-boundary";

<ErrorBoundary
  FallbackComponent={({ error, resetErrorBoundary }) => (
    <div>
      <p>Algo deu errado: {error.message}</p>
      <button onClick={resetErrorBoundary}>Tentar novamente</button>
    </div>
  )}
>
  <OrdersList />
</ErrorBoundary>
```

**Não capturam:** erros em event handlers, código async fora do render, SSR.

---

## Arquitetura de Projeto (feature-based)

```
src/
  features/
    orders/
      components/   # OrderList, OrderCard
      hooks/        # useOrders, useOrderMutation
      api/          # queries TanStack Query
      types/        # order.types.ts
      index.ts      # barrel — API pública da feature
  shared/
    components/     # Button, Modal, Input
    hooks/          # useDebounce, useLocalStorage
    lib/            # queryClient, axios instance
  app/              # routing, providers, layout
```

---

## O que estudar em seguida

1. **Next.js / App Router** — Server Components, SSR, RSC
2. **TanStack Query** — server state, cache, mutations
3. **Zustand** — client state global
4. **React Hook Form + Zod** — formulários
5. **Performance** — `React.memo`, Code Splitting, Virtualização
6. **Testing** — React Testing Library + Vitest
