# TanStack Query — Tudo que você precisa saber

## O que é

TanStack Query (antes React Query) é uma biblioteca de **gerenciamento de server state** para React. Resolve o problema de buscar, cachear, sincronizar e atualizar dados do servidor sem boilerplate manual.

Modelo mental central: **dados do servidor não são seu estado** — são um snapshot remoto que precisa de cache, revalidação e sincronização. `useState` + `useEffect` para fetch é um anti-padrão.

---

## Por que não usar useState + useEffect para fetch

```typescript
// ❌ Anti-padrão — boilerplate enorme, sem cache, sem retry, sem devtools
const [orders, setOrders] = useState([]);
const [loading, setLoading] = useState(false);
const [error, setError] = useState(null);

useEffect(() => {
  setLoading(true);
  fetchOrders()
    .then(setOrders)
    .catch(setError)
    .finally(() => setLoading(false));
}, []);

// ✅ TanStack Query — cache, retry, refetch, devtools, tudo grátis
const { data: orders, isLoading, error } = useQuery({
  queryKey: ["orders"],
  queryFn: fetchOrders
});
```

O que você ganha de graça: cache automático, deduplicação de requests, retry em falha, refetch em foco de janela, loading/error states, devtools visuais.

---

## Setup

```typescript
// main.tsx
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 60 * 1000,      // 1 minuto padrão
      retry: 2,                   // 2 retries em falha
      refetchOnWindowFocus: true  // refetch ao focar a aba
    }
  }
});

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router />
      <ReactQueryDevtools initialIsOpen={false} />
    </QueryClientProvider>
  );
}
```

---

## useQuery — Leitura de dados

```typescript
const { data, isLoading, isError, error, isFetching, refetch } = useQuery({
  queryKey: ["orders", { status: "pending" }],
  queryFn: () => fetchOrders({ status: "pending" }),
  staleTime: 5 * 60 * 1000,   // 5 minutos
  gcTime: 10 * 60 * 1000,     // 10 minutos no cache inativo
  enabled: !!userId,           // só executa se userId existir
});
```

### Estados possíveis

| Estado | Significado |
|---|---|
| `isLoading` | Primeira busca, sem dados em cache |
| `isFetching` | Qualquer fetch em andamento (incluindo revalidação) |
| `isError` | Query falhou após todos os retries |
| `isSuccess` | Dados disponíveis |
| `isPending` | Query ainda não executou (disabled ou aguardando) |

---

## queryKey — A chave do cache

O `queryKey` é o **endereço do cache**. Arrays são comparados por valor — estruture hierarquicamente para invalidação granular.

```typescript
// Fábrica de keys — padrão recomendado
const orderKeys = {
  all: ["orders"] as const,
  lists: () => [...orderKeys.all, "list"] as const,
  list: (filters: OrderFilters) => [...orderKeys.lists(), filters] as const,
  details: () => [...orderKeys.all, "detail"] as const,
  detail: (id: string) => [...orderKeys.details(), id] as const
};

// Uso
useQuery({ queryKey: orderKeys.list({ status: "pending" }), queryFn: ... });
useQuery({ queryKey: orderKeys.detail(orderId), queryFn: ... });

// Invalidação granular
queryClient.invalidateQueries({ queryKey: orderKeys.lists() });   // invalida todas as listas
queryClient.invalidateQueries({ queryKey: orderKeys.detail(id) }); // invalida um pedido
```

---

## staleTime vs gcTime

```
staleTime (padrão: 0)
  → Quanto tempo o dado é considerado "fresco"
  → Durante esse período: sem refetch em background
  → staleTime: 0  → refetch sempre que componente monta ou janela foca
  → staleTime: Infinity → nunca refetch automático (dados estáticos)

gcTime (padrão: 5min, antes chamado cacheTime)
  → Quanto tempo o dado fica no cache após não ter mais consumidores
  → Depois desse tempo: dado é descartado da memória
```

---

## useMutation — Escrita de dados

```typescript
const { mutate, mutateAsync, isPending, isError, reset } = useMutation({
  mutationFn: (newOrder: CreateOrderDTO) => api.createOrder(newOrder),
  onSuccess: (data) => {
    queryClient.invalidateQueries({ queryKey: orderKeys.lists() });
    toast.success("Pedido criado!");
  },
  onError: (error) => {
    toast.error(`Erro: ${error.message}`);
  }
});

// Uso
mutate({ productId: "123", quantity: 2 });

// Com async/await — lança exceção em caso de erro
await mutateAsync({ productId: "123", quantity: 2 });
```

---

## Optimistic Updates

Atualiza a UI antes da resposta do servidor. Se falhar, reverte.

```typescript
const updateOrder = useMutation({
  mutationFn: (update: { id: string; status: string }) => api.updateOrder(update),

  onMutate: async (update) => {
    // Cancela queries em voo para não sobrescrever o update otimista
    await queryClient.cancelQueries({ queryKey: orderKeys.lists() });

    // Salva estado anterior para rollback
    const previousOrders = queryClient.getQueryData(orderKeys.lists());

    // Aplica update otimista no cache
    queryClient.setQueryData(orderKeys.lists(), (old: Order[]) =>
      old.map(o => o.id === update.id ? { ...o, status: update.status } : o)
    );

    return { previousOrders };
  },

  onError: (err, update, context) => {
    // Reverte para estado anterior
    queryClient.setQueryData(orderKeys.lists(), context?.previousOrders);
    toast.error("Erro ao atualizar pedido");
  },

  onSettled: () => {
    // Sempre revalida após sucesso ou erro
    queryClient.invalidateQueries({ queryKey: orderKeys.lists() });
  }
});
```

---

## Suspense Mode — useSuspenseQuery

Elimina os estados `isLoading`/`isError` do componente — delega para `<Suspense>` e `<ErrorBoundary>`.

```typescript
// Componente fica limpo — data é sempre definido aqui
function OrdersList() {
  const { data: orders } = useSuspenseQuery({
    queryKey: orderKeys.lists(),
    queryFn: fetchOrders
  });

  return (
    <ul>
      {orders.map(o => <li key={o.id}>{o.status}</li>)}
    </ul>
  );
}

// Wrapper com boundary + suspense
function OrdersPage() {
  return (
    <QueryErrorResetBoundary>
      {({ reset }) => (
        <ErrorBoundary onReset={reset} FallbackComponent={ErrorFallback}>
          <Suspense fallback={<OrdersSkeleton />}>
            <OrdersList />
          </Suspense>
        </ErrorBoundary>
      )}
    </QueryErrorResetBoundary>
  );
}
```

---

## Infinite Scroll — useInfiniteQuery

```typescript
function InfiniteOrderList() {
  const {
    data,
    fetchNextPage,
    hasNextPage,
    isFetchingNextPage
  } = useInfiniteQuery({
    queryKey: ["orders", "infinite"],
    queryFn: ({ pageParam }) => fetchOrders({ cursor: pageParam, limit: 20 }),
    initialPageParam: null,
    getNextPageParam: lastPage => lastPage.nextCursor ?? undefined
  });

  const allOrders = data?.pages.flatMap(page => page.orders) ?? [];

  return (
    <ul>
      {allOrders.map(order => <OrderItem key={order.id} order={order} />)}
      {hasNextPage && (
        <button onClick={() => fetchNextPage()} disabled={isFetchingNextPage}>
          {isFetchingNextPage ? "Carregando..." : "Carregar mais"}
        </button>
      )}
    </ul>
  );
}
```

---

## Polling e WebSocket

```typescript
// Polling — refetch a cada N ms
const { data } = useQuery({
  queryKey: ["order", orderId],
  queryFn: () => fetchOrder(orderId),
  refetchInterval: 5000,              // a cada 5s
  refetchIntervalInBackground: false  // pausa quando aba não está em foco
});

// WebSocket — invalida cache ao receber mensagem
function useOrdersWebSocket() {
  const queryClient = useQueryClient();

  useEffect(() => {
    const ws = new WebSocket("wss://api.exemplo.com/orders");

    ws.onmessage = event => {
      const { type, orderId } = JSON.parse(event.data);

      if (type === "ORDER_UPDATED") {
        queryClient.invalidateQueries({ queryKey: ["order", orderId] });
      }
      if (type === "ORDER_CREATED") {
        queryClient.invalidateQueries({ queryKey: orderKeys.lists() });
      }
    };

    return () => ws.close();
  }, [queryClient]);
}
```

---

## Prefetch — Carregamento antecipado

```typescript
const queryClient = useQueryClient();

// Prefetch no hover de um link
async function handleOrderHover(id: string) {
  await queryClient.prefetchQuery({
    queryKey: orderKeys.detail(id),
    queryFn: () => fetchOrder(id),
    staleTime: 30_000
  });
}

// Prefetch no servidor (Next.js App Router)
import { dehydrate, HydrationBoundary } from "@tanstack/react-query";

export default async function OrdersPage() {
  const queryClient = new QueryClient();
  await queryClient.prefetchQuery({
    queryKey: orderKeys.lists(),
    queryFn: fetchOrders
  });

  return (
    <HydrationBoundary state={dehydrate(queryClient)}>
      <OrdersList />
    </HydrationBoundary>
  );
}
```

---

## Integração com Server Actions (Next.js)

```typescript
// action.ts
"use server";
export async function updateOrderAction(id: string, data: Partial<Order>) {
  return db.order.update({ where: { id }, data });
}

// componente client
"use client";
function OrderEditor({ order }: { order: Order }) {
  const queryClient = useQueryClient();

  const mutation = useMutation({
    mutationFn: (data: Partial<Order>) => updateOrderAction(order.id, data),
    onSuccess: updated => {
      queryClient.setQueryData(orderKeys.detail(order.id), updated);
      queryClient.invalidateQueries({ queryKey: orderKeys.lists() });
    }
  });

  return (
    <button
      disabled={mutation.isPending}
      onClick={() => mutation.mutate({ status: "paid" })}
    >
      {mutation.isPending ? "Salvando..." : "Marcar como pago"}
    </button>
  );
}
```

---

## TanStack Query vs SWR

| | TanStack Query | SWR |
|---|---|---|
| Bundle size | ~13KB | ~4KB |
| Mutations | `useMutation` rico | `mutate` básico |
| Optimistic updates | Nativo | Manual |
| Infinite scroll | `useInfiniteQuery` | `useSWRInfinite` |
| Devtools | Oficial, excelente | Não oficial |
| Suspense | `useSuspenseQuery` | Sim |

**Quando SWR:** projetos simples, bundle crítico.
**Quando TanStack Query:** projetos maiores, mutations complexas, optimistic updates.

---

## Quando NÃO usar TanStack Query

- Estado que não vem do servidor → use `useState`, Zustand ou Jotai
- Dados que nunca mudam após o carregamento inicial → considere buscar no servidor (RSC / SSR) e passar como prop
- Mutations simples sem necessidade de cache → Server Actions direto com `useActionState`

---

## Resumo de decisão — Server State

```
Dados do servidor                → TanStack Query
Estado global de UI               → Zustand / Jotai
Estado local de componente        → useState / useReducer
Estado na URL (filtros, páginas)  → nuqs
```
