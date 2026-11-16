---
type: concept
title: "Props (React)"
aliases: ["props", "propriedades", "propriedades de componente"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 6
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

## Na NLW #2, dia 1 (Diego Fernandes)

`PageHeader` recebe `title` tipado por `interface PageHeaderProps` e `React.FC<PageHeaderProps>`, e o formulário de busca entra por `props.children`, "uma propriedade automática do React". Com os tipos do React 18, o `FC` perdeu o `children` implícito: o mesmo código pede `children?: React.ReactNode` na interface. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]].

## Na NLW #2, dia 3 (Diego Fernandes)

`description?` opcional; `Input`/`Textarea`/`Select` com `extends InputHTMLAttributes<HTMLInputElement>` e `({ label, name, ...rest })` + `{...rest}`; `options` como prop no Select; `TeacherItem` recebendo `teacher` tipado por uma `interface Teacher` exportada. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]].

## Na NLW #2, dia 4 (Diego Fernandes)

`PageHeaderProps { title: string }` com `React.FC`; `options` do navigator com `tabBarIcon: ({ color, size, focused }) => ...`, uma função recebida como prop. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]].

## Na NLW #2, dia 5 (Diego Fernandes)

`headerRight?: ReactNode` para passar um ícone-botão ao header ("receber um componente como uma propriedade"); `favorited` booleano, com a frase invertida "é só não passar nada" (o atalho é escrever só o nome). Ver [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: Header com title, React.FC e interface
- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: função como prop
- [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]: NLW #2, Diego, dia 1: title tipado e props.children no PageHeader
- [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]]: NLW #2, Diego, dia 3: HTMLAttributes, rest/spread e teacher
- [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]]: NLW #2, Diego, dia 4: title e tabBarIcon
- [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]]: NLW #2, Diego, dia 5: ReactNode como prop e booleano
