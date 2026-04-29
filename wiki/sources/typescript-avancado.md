---
type: source
title: "TypeScript Avançado — Generics, Conditional Types, Template Literal Types e Decorators"
aliases: ["typescript avancado", "generics typescript", "conditional types", "template literal types", "mapped types", "decorators typescript", "utility types avancados"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/typescript-avancado.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [typescript, generics, conditional-types, template-literal-types, mapped-types, decorators, utility-types]
skill: lang-dynamic
status: stable
---

## TL;DR

TypeScript avançado: Generics com constraints e `infer` extraem tipos de dentro de outros tipos. Conditional Types permitem lógica de tipo em tempo de compilação. Template Literal Types geram unions de strings automaticamente. Mapped Types transformam shapes de objetos. Decorators (Stage 3) adicionam metaprogramação. Utility Types avançados: `Parameters`, `ConstructorParameters`, `InstanceType`, `satisfies` (preserva tipo inferido), `NoInfer` (TS 5.4).

## Key Claims

**Claim:** `infer` dentro de Conditional Types extrai partes de tipos compostos — base para criar utilitários de tipo reutilizáveis.
**Evidence:** `type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never` — extrai o tipo de retorno de qualquer função. `type UnpackPromise<T> = T extends Promise<infer U> ? U : T` — extrai o tipo dentro de uma Promise. Sem `infer`, seria impossível expressar "o tipo que está dentro disso" de forma genérica.
**Confidence:** alta

**Claim:** Template Literal Types geram unions de string automaticamente — elimina manutenção de listas de strings duplicadas.
**Evidence:** `type EventName = `on${Capitalize<"click" | "focus" | "blur">}`` → `"onClick" | "onFocus" | "onBlur"`. `type CSSProperty = `${"-webkit-" | ""}${"transform" | "transition"}`` gera todas as combinações. Qualquer adição na union base é automaticamente propagada para todos os tipos derivados.
**Confidence:** alta

**Claim:** `satisfies` preserva o tipo inferido mais específico enquanto valida contra um tipo mais geral — resolve o dilema entre type annotation e type inference.
**Evidence:** `const config = { host: "localhost", port: 5432 } satisfies Record<string, string | number>` — `config.host` é `string` (não `string | number`). Com annotation explícita `const config: Record<string, string | number>` perderíamos a especificidade e autocompletion falharia. `satisfies` valida o shape sem destruir a informação de tipo da inferência.
**Confidence:** alta

**Claim:** `NoInfer<T>` (TS 5.4) previne que TypeScript infira um tipo de uma posição específica — útil quando uma posição deve ser verificada, não influenciar a inferência.
**Evidence:** `function createState<T>(initial: T, validator: (value: NoInfer<T>) => boolean): T` — sem `NoInfer`, o tipo `T` seria inferido tanto de `initial` quanto de `validator`, podendo causar inferências incorretas. Com `NoInfer`, apenas `initial` participa da inferência de `T`; `validator` é verificado contra o `T` já inferido.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/generics-typescript]]
- [[concepts/conditional-types]]
- [[concepts/template-literal-types]]
- [[concepts/mapped-types]]
- [[concepts/decorators-typescript]]
- [[concepts/utility-types]]
- [[concepts/satisfies-operator]]

## Open Questions

- Decorators Stage 3 vs experimentalDecorators legado — quando migrar projetos existentes (NestJS, TypeORM)?
- Branded types vs `satisfies` para validação de primitivos — qual approach é mais ergonômico?
