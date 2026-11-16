---
type: entity
title: "Metro (bundler)"
aliases: ["Metro Bundler", "Metro", "metro.config.js"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [react-native, bundler, build, javascript]
skill: tech-mentor-mobile
status: stub
---

# Metro (bundler)

Bundler JavaScript do [[wiki/entities/react-native]], mantido pela Meta. Resolve os imports, transforma o código (Babel, TypeScript) e serve o bundle ao app. Em desenvolvimento, faz o *fast refresh* a cada salvamento; em release, gera o bundle minificado (e, com Hermes, o bytecode).

Na NLW #1 com [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]): roda ao dar `npm start` no projeto [[wiki/entities/expo]] e "fica ouvindo [...] todas as alterações". Diego o descreve como gerador de "um código JavaScript totalmente minificado", o que só vale para produção: em desenvolvimento, o bundle não é minificado. Diego também mostra a janela do Expo com os logs de cada aparelho conectado.

**Por que importa:** muitos erros "fantasmas" depois de instalar pacotes nativos vêm de cache do Metro. `npx expo start -c` limpa o cache, e é mais rápido que o reinicia-tudo da aula.

Relacionado: [[wiki/concepts/transpilador]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: hot reload e logs no Expo
