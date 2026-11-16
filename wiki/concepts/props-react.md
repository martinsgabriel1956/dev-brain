---
type: concept
title: "Props (React)"
aliases: ["props", "propriedades", "propriedades de componente"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [react, componentes, typescript]
skill: tech-mentor-frontend
status: stub
---

# Props (React)

Entradas de um componente React, passadas como atributos JSX: `<Header title="Ecoleta" />`. Para [[wiki/entities/diego-fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]), são "atributos que a gente envia pro componente", como o `type` e o `value` de um `input`.

- **Só leitura:** o componente não altera as próprias props. Para dado que muda, usa-se [[wiki/concepts/useState|estado]] no pai e passa-se para baixo. Quando a prop muda, o filho re-renderiza (o exemplo da aula é `title={`Contador: ${counter}`}`).
- **Tipagem:** `interface HeaderProps { title: string }`, com `title?` para opcional. Sem a prop obrigatória: "Property title is missing". Na aula, `React.FC<HeaderProps>` ([[wiki/concepts/generics-typescript]]). Hoje o padrão é `function Header({ title }: HeaderProps)`, porque o `React.FC` injetava `children` implícito e caiu em desuso.
- **`children`** é a prop do conteúdo entre as tags. Callbacks como props (`onSelect`) fazem o filho avisar o pai.
- **`key` não é prop:** o React a consome para identificar itens de lista e não a repassa ao componente.

Relacionado: [[wiki/concepts/componentizacao]], [[wiki/concepts/jsx]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]], a prop `onFileUploaded` é uma função: o filho chama, o pai atualiza o estado ([[wiki/concepts/levantamento-de-estado]]).

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: Header com title, React.FC e interface
- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: função como prop
