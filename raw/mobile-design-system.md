---
date: 2026-04-23
tags: [tech-mentor, mobile, design-system, tokens, componentes, figma-to-code, react-native, flutter]
skill: tech-mentor-mobile/references/design-system
level: arquiteto
---

# Design System Mobile — Tokens, Componentes Agnósticos, Figma-to-Code

## Contexto
Design system mobile não é uma biblioteca de componentes — é a única fonte de verdade que conecta design (Figma) ao código (iOS/Android/RN/Flutter). Sem ele, cada desenvolvedor reinventa padding, cores e tipografia, criando inconsistência visual que usuários percebem subconscientemente. A arquitetura correta é: tokens no centro, componentes primitivos em cima, componentes compostos no topo.

## Como Funciona

### Arquitetura em camadas

```
Figma (fonte de verdade)
  ↓ (tokens exportados via Style Dictionary)
Design Tokens (JSON agnóstico de plataforma)
  ↓
Tokens de plataforma (RN StyleSheet / Flutter ThemeData / Swift Color assets)
  ↓
Primitivos (Button, Text, Input, Icon) — agnósticos de domínio
  ↓
Compostos (ProductCard, CheckoutForm, ProfileHeader) — contexto de negócio
```

### Design Tokens — Style Dictionary

```json
// tokens/base.json — fonte única de verdade
{
  "color": {
    "brand": {
      "primary": { "value": "#007AFF", "type": "color" },
      "secondary": { "value": "#34C759", "type": "color" }
    },
    "neutral": {
      "100": { "value": "#F2F2F7", "type": "color" },
      "900": { "value": "#1C1C1E", "type": "color" }
    },
    "semantic": {
      "background": { "value": "{color.neutral.100}", "type": "color" },
      "surface": { "value": "#FFFFFF", "type": "color" },
      "error": { "value": "#FF3B30", "type": "color" },
      "success": { "value": "{color.brand.secondary}", "type": "color" }
    }
  },
  "spacing": {
    "xs": { "value": "4", "type": "dimension" },
    "sm": { "value": "8", "type": "dimension" },
    "md": { "value": "16", "type": "dimension" },
    "lg": { "value": "24", "type": "dimension" },
    "xl": { "value": "32", "type": "dimension" }
  },
  "typography": {
    "size": {
      "xs": { "value": "12", "type": "fontSizes" },
      "sm": { "value": "14", "type": "fontSizes" },
      "md": { "value": "16", "type": "fontSizes" },
      "lg": { "value": "20", "type": "fontSizes" },
      "xl": { "value": "24", "type": "fontSizes" },
      "2xl": { "value": "32", "type": "fontSizes" }
    },
    "weight": {
      "regular": { "value": "400", "type": "fontWeights" },
      "medium": { "value": "500", "type": "fontWeights" },
      "semibold": { "value": "600", "type": "fontWeights" },
      "bold": { "value": "700", "type": "fontWeights" }
    }
  },
  "radius": {
    "sm": { "value": "4", "type": "borderRadius" },
    "md": { "value": "8", "type": "borderRadius" },
    "lg": { "value": "16", "type": "borderRadius" },
    "full": { "value": "9999", "type": "borderRadius" }
  }
}
```

```javascript
// style-dictionary.config.js
const StyleDictionary = require("style-dictionary");

module.exports = {
  source: ["tokens/**/*.json"],
  platforms: {
    // React Native
    reactNative: {
      transformGroup: "js",
      buildPath: "src/design-system/tokens/",
      files: [{ destination: "index.ts", format: "javascript/es6" }]
    },
    // Flutter
    flutter: {
      transformGroup: "flutter",
      buildPath: "lib/design_system/",
      files: [{ destination: "tokens.dart", format: "flutter/class.dart" }]
    },
    // iOS — Swift
    ios: {
      transformGroup: "ios-swift",
      buildPath: "ios/DesignSystem/",
      files: [
        { destination: "ColorTokens.swift", format: "ios-swift/enum.swift" }
      ]
    }
  }
};

// Gerar tokens: npx style-dictionary build
```

### React Native — Design System

```typescript
// src/design-system/tokens/index.ts (gerado pelo Style Dictionary)
export const tokens = {
  color: {
    brandPrimary: "#007AFF",
    brandSecondary: "#34C759",
    semanticBackground: "#F2F2F7",
    semanticError: "#FF3B30",
    semanticSuccess: "#34C759"
  },
  spacing: { xs: 4, sm: 8, md: 16, lg: 24, xl: 32 },
  typography: {
    size: { xs: 12, sm: 14, md: 16, lg: 20, xl: 24, "2xl": 32 },
    weight: { regular: "400", medium: "500", semibold: "600", bold: "700" }
  },
  radius: { sm: 4, md: 8, lg: 16, full: 9999 }
} as const;

// Dark mode
export const darkTokens = {
  ...tokens,
  color: {
    ...tokens.color,
    semanticBackground: "#1C1C1E",
    semanticSurface: "#2C2C2E"
  }
} as const;

// Theme context
type Theme = typeof tokens;
const ThemeContext = createContext<Theme>(tokens);

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const colorScheme = useColorScheme();
  const theme = colorScheme === "dark" ? darkTokens : tokens;

  return <ThemeContext.Provider value={theme}>{children}</ThemeContext.Provider>;
}

export const useTheme = () => useContext(ThemeContext);
```

```typescript
// Componente primitivo — Button
type ButtonVariant = "primary" | "secondary" | "ghost" | "destructive";
type ButtonSize = "sm" | "md" | "lg";

type ButtonProps = {
  label: string;
  onPress: () => void;
  variant?: ButtonVariant;
  size?: ButtonSize;
  disabled?: boolean;
  loading?: boolean;
  leftIcon?: React.ReactElement;
};

export function Button({
  label,
  onPress,
  variant = "primary",
  size = "md",
  disabled = false,
  loading = false,
  leftIcon
}: ButtonProps) {
  const theme = useTheme();

  const containerStyle = [
    styles.base,
    styles[variant],
    styles[`size_${size}`],
    disabled && styles.disabled
  ];

  const labelStyle = [
    styles.label,
    styles[`label_${variant}`],
    styles[`labelSize_${size}`]
  ];

  return (
    <Pressable
      style={({ pressed }) => [containerStyle, pressed && !disabled && styles.pressed]}
      onPress={onPress}
      disabled={disabled || loading}
      accessibilityRole="button"
      accessibilityLabel={label}
      accessibilityState={{ disabled }}
    >
      {loading ? (
        <ActivityIndicator color={variant === "primary" ? "#fff" : theme.color.brandPrimary} />
      ) : (
        <>
          {leftIcon}
          <Text style={labelStyle}>{label}</Text>
        </>
      )}
    </Pressable>
  );
}

const styles = StyleSheet.create({
  base: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    borderRadius: tokens.radius.md,
    gap: tokens.spacing.sm
  },
  primary: { backgroundColor: tokens.color.brandPrimary },
  secondary: { backgroundColor: "transparent", borderWidth: 1, borderColor: tokens.color.brandPrimary },
  ghost: { backgroundColor: "transparent" },
  destructive: { backgroundColor: tokens.color.semanticError },
  size_sm: { paddingHorizontal: tokens.spacing.md, paddingVertical: tokens.spacing.xs, minHeight: 36 },
  size_md: { paddingHorizontal: tokens.spacing.lg, paddingVertical: tokens.spacing.sm, minHeight: 44 },
  size_lg: { paddingHorizontal: tokens.spacing.xl, paddingVertical: tokens.spacing.md, minHeight: 56 },
  disabled: { opacity: 0.4 },
  pressed: { opacity: 0.85 },
  label: { fontWeight: tokens.typography.weight.semibold },
  label_primary: { color: "#FFFFFF" },
  label_secondary: { color: tokens.color.brandPrimary },
  label_ghost: { color: tokens.color.brandPrimary },
  label_destructive: { color: "#FFFFFF" },
  labelSize_sm: { fontSize: tokens.typography.size.sm },
  labelSize_md: { fontSize: tokens.typography.size.md },
  labelSize_lg: { fontSize: tokens.typography.size.lg }
});
```

### Flutter — ThemeData como design system

```dart
// lib/design_system/app_theme.dart
class AppTheme {
  static ThemeData get light => ThemeData(
    useMaterial3: true,
    colorScheme: ColorScheme.fromSeed(
      seedColor: const Color(0xFF007AFF),
      brightness: Brightness.light,
    ),
    textTheme: _textTheme,
    elevatedButtonTheme: _buttonTheme,
    inputDecorationTheme: _inputTheme,
    cardTheme: _cardTheme,
  );

  static ThemeData get dark => ThemeData(
    useMaterial3: true,
    colorScheme: ColorScheme.fromSeed(
      seedColor: const Color(0xFF007AFF),
      brightness: Brightness.dark,
    ),
    textTheme: _textTheme,
  );

  static const _textTheme = TextTheme(
    displayLarge: TextStyle(fontSize: 32, fontWeight: FontWeight.bold),
    titleLarge: TextStyle(fontSize: 20, fontWeight: FontWeight.w600),
    bodyLarge: TextStyle(fontSize: 16, fontWeight: FontWeight.w400),
    bodyMedium: TextStyle(fontSize: 14, fontWeight: FontWeight.w400),
    labelSmall: TextStyle(fontSize: 12, fontWeight: FontWeight.w500),
  );

  static final _buttonTheme = ElevatedButtonThemeData(
    style: ElevatedButton.styleFrom(
      padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
      minimumSize: const Size(0, 44),
    ),
  );
}

// Uso nos widgets — acessar via Theme.of(context)
class PrimaryButton extends StatelessWidget {
  final String label;
  final VoidCallback onPressed;
  
  const PrimaryButton({required this.label, required this.onPressed, super.key});

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: onPressed,
      child: Text(label),
    );
  }
}
```

### Figma-to-Code — Tokens sincronizados

```
Fluxo Figma → Código:
1. Designer cria/atualiza tokens no Figma (Variables API ou Tokens Studio plugin)
2. CI exporta tokens via Figma REST API → atualiza base.json
3. Style Dictionary regenera os arquivos de plataforma
4. PR automático com diff dos tokens

# Script de exportação
curl -H "X-Figma-Token: $FIGMA_TOKEN" \
  "https://api.figma.com/v1/files/$FILE_ID/variables/local" \
  | jq ".meta.variables" > tokens/figma-export.json
```

## Trade-offs

| Aspecto | Design system | Sem design system |
|---|---|---|
| Consistência visual | Alta | Baixa |
| Velocidade inicial | Mais lenta (setup) | Mais rápida |
| Manutenção de UI | Fácil (mudar token = mudar tudo) | Cara (busca e troca manual) |
| Onboarding de devs | Fácil | Difícil |
| Dark mode | Trivial (trocar tokens) | Trabalhoso |

## Quando Usar / Quando Evitar

**Investir em design system** quando o produto está crescendo e múltiplos devs/designers trabalham simultaneamente — o custo de inconsistência supera o custo de setup.

**Não crie design system no MVP** — use Tailwind, shadcn, ou os componentes padrão da plataforma. Design system é para produtos que vão durar anos.

**Token-first:** mude o design mudando tokens, não buscando componentes. Um rebrand deve ser uma mudança de 10 tokens, não 300 arquivos.

## Conceitos Relacionados
[[mobile-feature-flags]] · [[mobile-cross-platform-decision]] · [[mobile-platform-engineering]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
