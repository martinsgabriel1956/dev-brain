---
type: concept
title: "Error Boundary"
aliases: ["error boundaries", "boundary de erro React"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [react, error-handling, resiliência, error-boundary]
skill: tech-mentor-frontend
status: stable
---

# Error Boundary

Componente que **captura erros JavaScript na árvore de componentes filhos** e exibe uma UI de fallback em vez de quebrar a tela inteira.

## Implementação (via react-error-boundary)

```typescript
import { ErrorBoundary } from "react-error-boundary";

<ErrorBoundary
  FallbackComponent={({ error, resetErrorBoundary }) => (
    <div role="alert">
      <p>Algo deu errado: {error.message}</p>
      <button onClick={resetErrorBoundary}>Tentar novamente</button>
    </div>
  )}
  onError={(error, info) => captureException(error, { extra: info })}
  onReset={() => queryClient.resetQueries({ queryKey: ["orders"] })}
>
  <OrdersList />
</ErrorBoundary>
```

## O que captura vs não captura

| Captura ✅ | Não captura ❌ |
|---|---|
| Erros em render | Erros em event handlers |
| Erros em lifecycle methods | Código async fora do render |
| Erros em toda a árvore filha | Erros no próprio boundary |
| | Erros em SSR |

## Integração com TanStack Query

```typescript
import { QueryErrorResetBoundary } from "@tanstack/react-query";

<QueryErrorResetBoundary>
  {({ reset }) => (
    <ErrorBoundary onReset={reset} FallbackComponent={ErrorFallback}>
      <Suspense fallback={<Spinner />}>
        <OrdersList />
      </Suspense>
    </ErrorBoundary>
  )}
</QueryErrorResetBoundary>
```

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
- [[wiki/sources/tanstack-query-tudo-que-voce-precisa-saber]]
