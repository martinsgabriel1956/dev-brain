---
type: concept
title: "Context API"
aliases: ["React Context", "useContext", "createContext"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
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

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
