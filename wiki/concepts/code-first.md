---
type: concept
title: "Code First"
aliases: ["code-first approach", "codar sem layout"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [design, processo, workflow, component-libraries, prototipagem]
skill: tech-mentor-frontend
status: stable
---

# Code First

Abordagem onde o **desenvolvimento começa direto no código**, usando component libraries, templates e estruturas semiprontas — sem criar um layout no Figma antes.

## Exemplos de ferramentas que facilitam code first

- **shadcn/ui** — componentes pré-estilizados copiáveis
- **Headless UI** — componentes sem estilo, só comportamento
- **Vercel AI Elements** — componentes para interfaces de IA
- **Radix UI** — primitivos acessíveis

## Vantagens

✅ Velocidade — sai codando sem fase de design
✅ Não exige habilidade de design para começar
✅ Bom para MVPs, protótipos, validação rápida

## Risco principal: o "Frankenstein"

Componentes de libraries são **isolados e sem contexto da aplicação**. Sem visão de design, o resultado é uma colagem de componentes sem coesão visual — o "Frankenstein".

```
Button do shadcn + Card do MUI + Modal custom + Layout improvisado
= Frankenstein visual
```

O risco aumenta quando:
- Você mistura estilos de múltiplas libraries
- Não tem referências de design próximas ao produto que está construindo
- Não estabelece um sistema de cores/espaçamento consistente antes

## Mitigação

Mesmo indo code first, ter **referências visuais** antes de começar reduz o risco. Ver [[dribbble]] e [[linear-app]] como referências.

## Ver também

- [[design-first]] — abordagem oposta
- [[design-engineer]] — perfil que navega bem em code first com visão de design

## Key Sources

- [[wiki/sources/design-first-vs-code-first-referencias]]
