---
type: concept
title: "Optimistic Updates"
aliases: ["atualização otimista", "optimistic UI"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [tanstack-query, ux, mutations, optimistic-updates]
skill: tech-mentor-frontend
status: stable
---

# Optimistic Updates

Técnica de UX que **atualiza a UI imediatamente** antes da resposta do servidor. Se a requisição falhar, reverte para o estado anterior.

## Implementação com TanStack Query

```typescript
const updateOrder = useMutation({
  mutationFn: (update: { id: string; status: string }) => api.updateOrder(update),

  onMutate: async update => {
    // 1. Cancela queries em voo — evita sobrescrever o update otimista
    await queryClient.cancelQueries({ queryKey: orderKeys.lists() });

    // 2. Salva snapshot para rollback
    const previousOrders = queryClient.getQueryData(orderKeys.lists());

    // 3. Aplica update otimista no cache
    queryClient.setQueryData(orderKeys.lists(), (old: Order[]) =>
      old.map(o => o.id === update.id ? { ...o, status: update.status } : o)
    );

    return { previousOrders };
  },

  onError: (err, update, context) => {
    // 4. Reverte em caso de erro
    queryClient.setQueryData(orderKeys.lists(), context?.previousOrders);
  },

  onSettled: () => {
    // 5. Sempre revalida após sucesso ou erro
    queryClient.invalidateQueries({ queryKey: orderKeys.lists() });
  }
});
```

## Fluxo

```
Usuário clica → UI atualiza imediatamente (otimista)
             → Request dispara em background
             → Sucesso: onSettled revalida (confirma)
             → Erro: onError reverte (rollback)
```

## Quando usar

✅ Ações de toggle (like, favorito, marcar como lido)
✅ Reordenação drag-and-drop
✅ Atualização de status com UX fluida

❌ Criação de entidades com ID gerado no servidor (você não sabe o ID antes da resposta)
❌ Operações financeiras críticas — prefira feedback explícito de loading

## Key Sources

- [[wiki/sources/tanstack-query-tudo-que-voce-precisa-saber]]
