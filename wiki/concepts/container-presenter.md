---
type: concept
title: "Container/Presenter Pattern"
aliases: ["smart/dumb components", "container presenter", "separação lógica visual React"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [react, padrões, arquitetura, testabilidade, separação-de-responsabilidades]
skill: tech-mentor-frontend
status: stable
---

# Container/Presenter Pattern

Separa **lógica** (fetch, estado, mutações) de **apresentação** (JSX puro). O Presenter não tem efeitos — recebe dados e callbacks via props.

## Estrutura

```typescript
// Container — lógica, fetch, efeitos
function OrderListContainer() {
  const { data: orders, isLoading, error } = useQuery({ queryKey: ["orders"], queryFn: fetchOrders });
  const { mutate: deleteOrder } = useMutation({ mutationFn: deleteOrderAPI });

  if (isLoading) return <OrderListPresenter orders={[]} loading />;
  if (error) return <ErrorMessage error={error} />;
  return <OrderListPresenter orders={orders} onDelete={deleteOrder} />;
}

// Presenter — só JSX, sem efeitos
function OrderListPresenter({ orders, loading = false, onDelete }) {
  if (loading) return <Skeleton count={5} />;
  return (
    <ul>
      {orders.map(o => (
        <li key={o.id}>
          {o.id}
          <button onClick={() => onDelete?.(o.id)}>Deletar</button>
        </li>
      ))}
    </ul>
  );
}
```

## Por que usar

- **Presenter é trivialmente testável** — sem mocks de fetch, sem setup de providers
- Lógica pode ser movida/reutilizada sem arrastar JSX
- Storybook para Presenter funciona sem API real

## Quando não usar

Componentes simples sem lógica pesada — over-engineering desnecessário.

## Ver também

- [[custom-hooks]] — alternativa moderna: extrair lógica em hook, componente consome o hook
- [[useEffect]] — onde os efeitos vivem no Container

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
