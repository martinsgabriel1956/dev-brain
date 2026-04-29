---
date: 2026-04-17
tags: [tech-mentor, linguagens, typescript, generics, conditional-types, template-literal, decorators, type-system]
skill: tech-mentor-backend/references/typescript
level: avançado
---

# TypeScript Avançado — Generics, Conditional Types, Template Literal Types e Decorators

## Contexto

TypeScript avançado não é sobre "usar mais tipos" — é sobre usar o sistema de tipos como ferramenta de design. Generics permitem escrever código que funciona para qualquer tipo mantendo type safety. Conditional types e template literal types permitem criar tipos que computam em função de outros tipos — transformando o type system em uma linguagem de programação em si.

---

## Generics — Além do Básico

```typescript
// Generic com constraint
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const user = { id: "123", name: "Alice", age: 30 };
const name = getProperty(user, "name");  // type: string
const age = getProperty(user, "age");   // type: number
// getProperty(user, "email");          // ❌ compile error

// Generic com multiple constraints
type Repository<T extends { id: string }, CreateDTO, UpdateDTO> = {
  findById: (id: string) => Promise<T | null>;
  create: (data: CreateDTO) => Promise<T>;
  update: (id: string, data: UpdateDTO) => Promise<T>;
  delete: (id: string) => Promise<void>;
};

// Generic condicional — tipo depende do input
type Awaited<T> = T extends Promise<infer U> ? Awaited<U> : T;

type A = Awaited<Promise<string>>;           // string
type B = Awaited<Promise<Promise<number>>>;  // number
type C = Awaited<string>;                    // string (não é Promise)

// Infer — extrair tipos de dentro de outros tipos
type ReturnType<T extends (...args: unknown[]) => unknown> =
  T extends (...args: unknown[]) => infer R ? R : never;

type FirstParam<T extends (first: unknown, ...rest: unknown[]) => unknown> =
  T extends (first: infer F, ...rest: unknown[]) => unknown ? F : never;

async function fetchUser(id: string): Promise<{ id: string; name: string }> {
  return { id, name: "Alice" };
}

type UserResult = Awaited<ReturnType<typeof fetchUser>>;  // { id: string; name: string }
type FetchParam = FirstParam<typeof fetchUser>;            // string
```

---

## Conditional Types — Tipos que Computam

```typescript
// Conditional type básico
type IsString<T> = T extends string ? true : false;
type A = IsString<string>;  // true
type B = IsString<number>;  // false

// Distributive conditional types — distribui sobre unions
type ToArray<T> = T extends unknown ? T[] : never;
type C = ToArray<string | number>;  // string[] | number[]
// (não ToArray é aplicado a cada membro da union separadamente)

// Evitar distribuição: wrap em tuple
type ToArrayNonDist<T> = [T] extends [unknown] ? T[] : never;
type D = ToArrayNonDist<string | number>;  // (string | number)[]

// NonNullable implementado com conditional types
type MyNonNullable<T> = T extends null | undefined ? never : T;
type E = MyNonNullable<string | null | undefined>;  // string

// Flatten recursivo
type Flatten<T> = T extends Array<infer U> ? Flatten<U> : T;
type F = Flatten<number[][][]>;  // number

// Deep Partial — tornar todas as propriedades opcionais recursivamente
type DeepPartial<T> = T extends object
  ? { [K in keyof T]?: DeepPartial<T[K]> }
  : T;

type Config = {
  server: { host: string; port: number };
  db: { url: string; pool: { min: number; max: number } };
};

type PartialConfig = DeepPartial<Config>;
// { server?: { host?: string; port?: number }; db?: { url?: string; pool?: { min?: number; max?: number } } }

// Readonly Deep
type DeepReadonly<T> = T extends object
  ? { readonly [K in keyof T]: DeepReadonly<T[K]> }
  : T;

// Extract apenas as chaves cujo valor é de um tipo específico
type KeysOfType<T, ValueType> = {
  [K in keyof T]: T[K] extends ValueType ? K : never;
}[keyof T];

type User = { id: string; name: string; age: number; active: boolean };
type StringKeys = KeysOfType<User, string>;   // "id" | "name"
type NumberKeys = KeysOfType<User, number>;   // "age"
```

---

## Template Literal Types — Tipos Baseados em Strings

```typescript
// Combinação de string literals
type HttpMethod = "GET" | "POST" | "PUT" | "DELETE" | "PATCH";
type ApiVersion = "v1" | "v2";
type Endpoint = `/${ApiVersion}/${string}`;

const validEndpoint: Endpoint = "/v1/users";      // ✅
// const bad: Endpoint = "/v3/users";             // ❌

// Gerar variantes de eventos
type EventName = "user" | "order" | "payment";
type EventVerb = "created" | "updated" | "deleted";
type DomainEvent = `${EventName}.${EventVerb}`;
// "user.created" | "user.updated" | "user.deleted" | "order.created" | ...

// CSS-like property names
type CSSProperty = "margin" | "padding" | "border";
type CSSDirection = "top" | "right" | "bottom" | "left";
type CSSLonghand = `${CSSProperty}-${CSSDirection}`;
// "margin-top" | "margin-right" | ... | "border-left"

// Manipulação de strings em tipos
type CamelToSnake<S extends string> =
  S extends `${infer Head}${infer Tail}`
    ? Head extends Uppercase<Head>
      ? `_${Lowercase<Head>}${CamelToSnake<Tail>}`
      : `${Head}${CamelToSnake<Tail>}`
    : S;

type Snaked = CamelToSnake<"getUserById">;  // "get_user_by_id"

// Event emitter type-safe
type EventMap = {
  "user.created": { userId: string; email: string };
  "order.created": { orderId: string; total: number };
  "payment.failed": { paymentId: string; reason: string };
};

type TypedEmitter<Events extends Record<string, unknown>> = {
  emit<K extends keyof Events>(event: K, data: Events[K]): void;
  on<K extends keyof Events>(event: K, handler: (data: Events[K]) => void): void;
};

declare const emitter: TypedEmitter<EventMap>;

emitter.emit("user.created", { userId: "123", email: "a@b.com" });  // ✅
// emitter.emit("user.created", { userId: "123" });                  // ❌ falta email
// emitter.emit("unknown.event", {});                                 // ❌ evento não existe
```

---

## Mapped Types — Transformar Tipos

```typescript
// Mapped type básico
type Optional<T> = { [K in keyof T]?: T[K] };
type Required<T> = { [K in keyof T]-?: T[K] };    // -? remove opcionalidade
type Readonly<T> = { readonly [K in keyof T]: T[K] };
type Mutable<T> = { -readonly [K in keyof T]: T[K] };  // remove readonly

// Remapear chaves com as
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};

type UserGetters = Getters<{ id: string; name: string; age: number }>;
// { getId: () => string; getName: () => string; getAge: () => number }

// Filtrar propriedades
type OmitNever<T> = { [K in keyof T as T[K] extends never ? never : K]: T[K] };

// Pick por tipo de valor
type PickByValue<T, V> = {
  [K in keyof T as T[K] extends V ? K : never]: T[K];
};

type StringProps = PickByValue<User, string>;  // { id: string; name: string }

// Criar union de tuplas de [key, value]
type Entries<T> = { [K in keyof T]: [K, T[K]] }[keyof T];
type UserEntries = Entries<{ id: string; age: number }>;
// ["id", string] | ["age", number]
```

---

## Decorators — Metadata e AOP

```typescript
// TypeScript 5.0+ decorators (stage 3, sem experimentalDecorators)

// Class decorator
function Singleton<T extends { new(...args: unknown[]): object }>(Base: T) {
  let instance: InstanceType<T> | null = null;
  return class extends Base {
    constructor(...args: unknown[]) {
      if (instance) return instance as InstanceType<T>;
      super(...args);
      instance = this as unknown as InstanceType<T>;
    }
  };
}

@Singleton
class DatabaseConnection {
  constructor(private url: string) {}
}

// Method decorator — logging automático
function Log(target: unknown, context: ClassMethodDecoratorContext) {
  const methodName = String(context.name);
  return function(this: unknown, ...args: unknown[]) {
    console.log({ message: `Calling ${methodName}`, args });
    const result = (target as (...a: unknown[]) => unknown).apply(this, args);
    console.log({ message: `${methodName} returned`, result });
    return result;
  };
}

class OrderService {
  @Log
  createOrder(userId: string, items: string[]): string {
    return `order-${userId}-${Date.now()}`;
  }
}

// Accessor decorator — validação
function Positive(target: unknown, context: ClassAccessorDecoratorContext) {
  return {
    set(this: unknown, value: number) {
      if (value <= 0) throw new Error(`${String(context.name)} must be positive`);
      (context as unknown as { set: (v: number) => void }).set.call(this, value);
    }
  };
}

class Product {
  @Positive
  accessor price: number = 0;
}
```

---

## Utility Types Avançados

```typescript
// Parameters<T> — tipos dos parâmetros de uma função
type Params = Parameters<typeof fetch>;  // [input: RequestInfo | URL, init?: RequestInit]

// ConstructorParameters<T> — parâmetros do constructor
class MyService {
  constructor(private db: string, private redis: string, private timeout: number) {}
}
type ServiceParams = ConstructorParameters<typeof MyService>;  // [string, string, number]

// InstanceType<T> — tipo da instância de uma classe
type ServiceInstance = InstanceType<typeof MyService>;  // MyService

// Satisfies — valida sem alterar o tipo inferido
const config = {
  host: "localhost",
  port: 5432,
  database: "mydb"
} satisfies Record<string, string | number>;

// config.host é string (não string | number)
// sem satisfies seria Record<string, string | number> e perderia a especificidade

// NoInfer — previne que TypeScript infira um tipo de uma posição específica (TS 5.4)
function createState<T>(initial: T, validator: (value: NoInfer<T>) => boolean): T {
  if (!validator(initial)) throw new Error("Invalid initial state");
  return initial;
}
// sem NoInfer, TypeScript inferira T a partir de validator também
```

---

## Trade-offs

| Feature | Poder | Complexidade | Quando Usar |
|---|---|---|---|
| **Generics básicos** | Alto | Baixa | Sempre que a forma é reutilizável |
| **Conditional types** | Muito alto | Alta | Tipos que computam em função de outros |
| **Template literals** | Alto | Média | APIs type-safe, event systems |
| **Decorators** | Alto | Média | Cross-cutting concerns (logging, auth, cache) |
| **Mapped types** | Alto | Média | Transformações de forma (Partial, Required, Pick) |

## Quando Usar / Quando Evitar

**Generics:** usar sempre que uma função ou classe opera sobre tipos que o caller deve determinar. Evitar generics desnecessários — se o tipo não varia, use o tipo concreto.

**Conditional types:** usar para utilitários de biblioteca (como os built-ins do TS). Evitar em código de aplicação cotidiano — torna o código difícil de ler e depurar.

**Template literal types:** excelente para APIs de eventos, roteamento type-safe, CSS-in-TS. Evitar para strings arbitrárias sem semântica.

**Decorators:** adequados para frameworks (NestJS, TypeORM). Evitar em código de domínio — decorators adicionam acoplamento implícito e tornam o fluxo difícil de rastrear.

## Conceitos Relacionados

[[node-internals]] · [[typescript-patterns]] · [[zod-validation]] · [[fastify-typescript]]

---
*Fonte: tech-mentor skill · lang-dynamic · 2026-04-17*
