---
type: concept
title: "Context API"
aliases: ["React Context", "useContext", "createContext"]
date_created: 2026-04-22
date_updated: 2026-08-03
source_count: 3
tags: [react, context, estado-global, prop-drilling]
skill: tech-mentor-frontend
status: stable
---

# Context API

Mecanismo do React para **compartilhar estado entre componentes sem prop drilling**. Ideal para dados de **baixa frequência de mudança**: tema, locale, usuário autenticado.

## Estrutura padrão

```typescript
type ThemeContextValue = {
  theme: "light" | "dark";
  toggleTheme: () => void;
};

const ThemeContext = createContext<ThemeContextValue | null>(null);

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<"light" | "dark">("light");
  const toggleTheme = useCallback(() => setTheme(prev => prev === "light" ? "dark" : "light"), []);

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

## Problema de performance

**Todo consumidor re-renderiza quando o `value` muda.** Para estado que muda frequentemente (carrinho, filtros), use Zustand/Jotai.

## Decisão de quando usar

| Frequência de mudança | Solução |
|---|---|
| Baixa (tema, auth, locale) | Context API |
| Alta (carrinho, UI state complexo) | Zustand / Jotai |
| Dados do servidor | TanStack Query |

## Provider composition

Para evitar "pyramid of doom" de providers aninhados:

```typescript
const AppProviders = composeProviders(ThemeProvider, AuthProvider, CartProvider);
<AppProviders><App /></AppProviders>
```

## Alternativa sem Provider: estado externo à árvore

Nem toda solução de estado global do React passa por `Provider`. [[wiki/concepts/zustand]] mantém o estado num módulo fora da árvore e usa um Hook (`useStore`) para cada componente se inscrever diretamente nele — sem precisar estar dentro de nenhum ancestral `<Provider>`. O mecanismo central (um [[wiki/concepts/observer-pattern|Observer]] com `subscribe`/`emit` + `useState`/`useEffect` para sincronizar) pode ser recriado em ~40 linhas de JavaScript puro; ver [[wiki/sources/recriando-zustand-javascript-puro-sem-provider]].

## O problema que motiva isso, fora do React

Prop drilling — passar uma prop por componentes intermediários que não a usam, só para alcançar um componente profundo na árvore — é um problema que todo framework de UI precisa resolver de algum jeito, não só o React. A solução muda de nome (Context API no React, `provide`/`inject` no Vue, dependency injection no Angular), mas a ideia é sempre a mesma: um canal direto entre quem produz o dado e quem consome, sem passar por ninguém no meio.

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
- [[wiki/sources/10-conceitos-internos-frameworks-frontend]]
- [[wiki/sources/recriando-zustand-javascript-puro-sem-provider]] — alternativa de estado global sem Provider (Zustand-style)
