---
type: concept
title: "Navegação em pilha (stack navigation)"
aliases: ["stack navigation", "stack navigator", "pilha de telas"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [mobile, navegacao, react-native, ux]
skill: tech-mentor-mobile
status: stub
---

# Navegação em pilha (stack navigation)

Modelo de navegação em que cada tela nova é empilhada sobre a anterior. A anterior continua montada; o "voltar" (botão, gesto de borda no iOS, botão físico no Android) desempilha. É o padrão para fluxos de detalhe: lista → item → subitem.

Na explicação de [[wiki/entities/diego-fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]), as telas anteriores "não deixam de existir, o usuário consegue voltar". No Ecoleta, a pilha é Home → Points (mapa) → Detail, com o [[wiki/entities/react-navigation]] (`createStackNavigator`, `navigate`, `goBack`). Os outros modelos citados são abas (seções paralelas) e drawer (menu lateral).

**Consequências práticas:**

- **Telas montadas consomem memória,** e seus efeitos (timers, assinaturas) continuam rodando. Para reagir ao foco, usa-se `useFocusEffect`.
- **`navigate` x `push`:** `navigate` para uma tela já na pilha volta até ela; `push` empilha outra cópia.
- **Botão de voltar no Android:** a tela precisa de um "voltar" visível (como o `arrow-left` da aula), além do botão físico ou do gesto.

Relacionado: [[wiki/concepts/mobile-navegacao]], [[wiki/concepts/client-side-routing]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: Home → Points → Detail
