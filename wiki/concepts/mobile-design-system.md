---
type: concept
title: "Design System Mobile"
aliases: ["mobile design tokens", "figma to code mobile", "mobile component library"]
date_created: 2026-04-24
date_updated: 2026-07-03
source_count: 2
tags: [mobile, design-system, tokens, componentes, figma, dark-mode, theming]
skill: tech-mentor-mobile
status: stable
---

# Design System Mobile

## Arquitetura de Camadas

```
Tokens (cores, espaçamento, tipografia, raios)
    ↓
Componentes Primitivos (Button, Input, Text, Icon)
    ↓
Componentes Compostos (ProductCard, CheckoutForm, Header)
    ↓
Telas
```

Tokens são a única fonte de verdade — dark mode é troca de token, não de componente.

## Tokens

```json
{
  "color": {
    "primary": { "500": "#3B82F6" },
    "surface": { "default": "#FFFFFF", "dark": "#0F172A" }
  },
  "spacing": { "sm": 8, "md": 16, "lg": 24 },
  "radius": { "sm": 4, "md": 8, "lg": 16 }
}
```

Style Dictionary converte JSON → Kotlin/Swift/TypeScript. Figma Variables sincronizam com tokens.

## React Native

```ts
const theme = {
    colors: { primary: tokens.color.primary[500] },
    spacing: tokens.spacing,
};

// ThemeProvider envolve o app
<ThemeProvider theme={isDark ? darkTheme : lightTheme}>
    <App />
</ThemeProvider>
```

## Componentes Primitivos

```ts
type ButtonProps = {
    label: string;
    variant: 'primary' | 'secondary' | 'ghost';
    onPress: () => void;
    disabled?: boolean;
};

export function Button({ label, variant, onPress, disabled }: ButtonProps) {
    return (
        <Pressable style={[styles.base, styles[variant], disabled && styles.disabled]} onPress={onPress}>
            <Text style={styles.label}>{label}</Text>
        </Pressable>
    );
}
```

## Ver também

- [[mobile-cross-platform-decision]] — design system unificado entre plataformas
- [[mobile-feature-flags]] — flags para rollout de novos componentes

## Key Sources

- [[wiki/sources/mobile-design-system]]
- [[wiki/sources/operador-de-crud-vs-engenheiro-repertorio]] — citado como exemplo de que "design system, mesmo no front, não é empilhar componente" — é consistência e acessibilidade que escalam para um time inteiro sem virar caos
