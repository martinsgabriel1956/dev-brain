---
type: concept
title: "Componente controlado (input controlado)"
aliases: ["controlled component", "input controlado", "formulário controlado", "uncontrolled"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [react, formularios, estado]
skill: tech-mentor-frontend
status: stub
---

# Componente controlado (input controlado)

Campo de formulário cujo valor mora no estado do React: `value={estado}` mais `onChange` que chama o `set`. O estado é a fonte da verdade, e o campo só o reflete. No não controlado, o DOM guarda o valor, lido por `ref` ou por `FormData` no submit.

No Ecoleta ([[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]):

- **Selects:** `value={selectedUf}` e `onChange={handleSelectUf}`, com `ChangeEvent<HTMLSelectElement>` para tipar `event.target.value`. A mudança de UF dispara o [[wiki/concepts/useEffect]] das cidades.
- **Inputs:** um só handler para vários campos, `setFormData({ ...formData, [event.target.name]: event.target.value })`. O spread preserva os outros campos ([[wiki/concepts/imutabilidade]]), e o `[name]` é a chave computada.

**Trade-offs:** o controlado re-renderiza a cada tecla e facilita validação ao vivo e campos dependentes. Em formulários grandes, `[skill: tech-mentor-frontend]` React Hook Form (não controlado por padrão) com Zod reduz renders e centraliza a validação. A aula também não define `value` nos `input`s, então eles ficam meio controlados: só o `onChange` grava no estado.

Relacionado: [[wiki/concepts/formulario-html]], [[wiki/concepts/useState]], [[wiki/concepts/validacao-de-entrada]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]], `TextInput` com `value` e `onChangeText={setUf}`, que "recebe diretamente já o texto digitado", mais `maxLength`, `autoCapitalize` e `autoCorrect`.

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: selects de UF/cidade e formData genérico
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: TextInput controlado no RN
