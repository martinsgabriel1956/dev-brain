# Os 8 Tipos de JavaScript

**Fonte:** Transcrição de vídeo (YouTube)
**Tema:** Apesar de JavaScript ser uma linguagem de tipagem fraca, ela contém oito tipos primitivos/fundamentais. O vídeo detalha cada um deles e compara duas formas de checar tipos: `typeof` e `Object.prototype.toString.call()`.

---

## Como checar tipos em JavaScript

Existe uma keyword chamada `typeof` que retorna o tipo de um valor. Exemplo: `typeof null`.

Curiosamente, `typeof null` retorna `"object"` — o que não é muito preciso. Isso acontece porque, internamente em JavaScript, tudo é derivado de `Object`; todos os tipos são, de certa forma, um objeto. Por isso `typeof null === "object"`.

Uma forma alternativa e mais precisa de checar tipos — usada, inclusive, em bibliotecas como o Underscore — é `Object.prototype.toString.call(valor)`. Exemplo: `Object.prototype.toString.call(null)` retorna `"[object Null]"`, um resultado bem mais claro do que `typeof`.

### Sobre `==` (comparação com conversão de tipo)

Quando se usa `==` (dois iguais) em JavaScript, o motor faz uma **conversão de tipo** (type coercion) antes de comparar — o que é chamado de "truthy comparison", não uma comparação 100% estrita.

Exemplo: `null == undefined` retorna `true`, porque o `==` converte os dois valores para um tipo comum antes de comparar.

Já `===` (três iguais / strict equality) não faz nenhuma conversão de tipo — compara os valores diretamente. Por isso a recomendação geral é sempre usar `===`, para evitar resultados inesperados de conversão implícita de tipo.

Entender esses oito tipos primitivos é importante justamente para entender como e por que essas conversões acontecem.

---

## 1. `null`

`null` é um tipo em JavaScript associado a um valor único — ele representa "nenhum valor" de forma explícita e intencional.

- `typeof null` → `"object"` (impreciso, como visto acima)
- `Object.prototype.toString.call(null)` → `"[object Null]"` (mais preciso)

---

## 2. `undefined`

- `typeof undefined` → `"undefined"`
- `Object.prototype.toString.call(undefined)` → `"[object Undefined]"`

`undefined` é o valor padrão (default) de toda variável declarada sem valor atribuído. Exemplo: `let fulou;` → `fulou` é `undefined`.

### `undefined` em parâmetros default de função

```js
function bar(a = [1, 2, 3]) {
  return a;
}

bar();        // retorna [1, 2, 3] — parâmetro não veio, usa o default
bar(null);    // retorna null — null É um valor, então o default não é aplicado
```

O valor default de um parâmetro só é usado quando o argumento é `undefined` — `null` é considerado um valor "de verdade" e não aciona o default.

### Diferença para expressões booleanas com `||`

```js
function bar(a) {
  a = a || [1, 2, 3];
  return a;
}

bar(null);   // retorna [1, 2, 3]
bar(0);      // retorna [1, 2, 3]
```

Isso acontece porque expressões booleanas com `||` fazem conversão de tipo (type coercion): qualquer valor "falsy" (`0`, `null`, `false`, `""`, etc.) é tratado como falso e ativa o valor à direita do `||`. Isso é diferente do parâmetro default de função, que só reage a `undefined` — todos os demais valores (incluindo `null` e `0`) são aceitos como estão.

---

## 3. `boolean`

- `typeof false` → `"boolean"`
- `Object.prototype.toString.call(false)` → `"[object Boolean]"`

`boolean` só pode assumir dois valores: `true` ou `false`. Nenhum outro valor é, em si, um boolean — mas JavaScript converte livremente qualquer valor para boolean em contextos booleanos (`if`, `||`, `&&`, `Boolean(valor)`).

Qualquer valor que não seja "vazio" (0, `""`, `null`, `undefined`, `NaN`, `false`) é convertido para `true` nesses contextos.

---

## 4. `number`

- `typeof 1` → `"number"`
- `Object.prototype.toString.call(1)` → `"[object Number]"`

Um número é sempre um valor sem aspas. Se o mesmo dígito estiver entre aspas (`"1"`), ele é uma `string`, não um `number`.

### Cuidado com concatenação

```js
"1" + 2   // "12" — string + number vira concatenação de string
1 + "2"   // "12" — mesma coisa, independente da ordem
```

Sempre que uma `string` é somada a um `number` com `+`, o `number` é convertido para `string` e o resultado é uma concatenação — não uma soma matemática. Por isso é importante garantir que os dois operandos sejam realmente do tipo `number` antes de somar, para evitar resultados inesperados.

---

## 5. `bigint`

Tipo pouco comum no dia a dia — usado para representar números muito grandes, além do limite seguro de `number`.

```js
typeof 1n   // "bigint"
```

A notação `1n` (sufixo `n`) indica um literal `bigint`.

- `Object.prototype.toString.call(1n)` → `"[object BigInt]"`

---

## 6. `string`

`string` é tudo que está entre aspas — simples (`'...'`), duplas (`"..."`) ou crase/template literals (`` `...` ``).

A diferença das crases (template literals) é permitir interpolação de variáveis dentro da string:

```js
const nome = "Sou Elder";
const mensagem = `Olá, ${nome}`; // interpola a variável, convertendo-a para string
```

Quando uma variável é interpolada dentro de um template literal, JavaScript chama internamente o equivalente a `toString()` sobre ela para converter o valor em string. Isso vale até para funções: converter uma função para string retorna a própria definição/código-fonte dela.

- `typeof "texto"` → `"string"`
- `Object.prototype.toString.call("texto")` → `"[object String]"`

---

## 7. `symbol`

Tipo pouco utilizado no dia a dia. Um `Symbol` representa um valor único e imutável — usado, por exemplo, para definir identificadores/constantes que nunca colidem com outros.

```js
Symbol("asd") === Symbol("asd")  // false
```

Mesmo com a mesma descrição (`"asd"`), cada `Symbol` criado é uma alocação distinta — como se cada chamada de `Symbol()` reservasse um espaço de memória único, diferente de comparar duas strings iguais.

- `typeof Symbol()` → `"symbol"`
- `Object.prototype.toString.call(Symbol())` → `"[object Symbol]"`

---

## 8. `object`

No fim das contas, praticamente tudo em JavaScript deriva de `object`.

```js
typeof {}              // "object"
typeof []              // "object"
typeof new Date()      // "object"
typeof Date            // "function" (a classe/construtor em si é uma function)
typeof null            // "object" (peculiaridade já vista acima)
typeof NaN             // "number" — curioso, já que NaN significa "Not a Number"
```

`Object.prototype.toString.call()` costuma ser mais preciso e detalhado que `typeof` para esse tipo — por exemplo, para um array:

```js
Object.prototype.toString.call([])   // "[object Array]"
```

`Array` não é, em si, um tipo primitivo nativo separado em JavaScript — é uma estrutura baseada em `object`. Mas a assinatura retornada por `toString.call()` ajuda a distinguir esse caso com mais precisão do que `typeof` sozinho (que retornaria apenas `"object"` para um array).

É até possível escrever assinaturas customizadas (`Symbol.toStringTag`) que alteram o que `Object.prototype.toString.call()` retorna para objetos próprios.

---

## Resumo — Os 8 Tipos

| # | Tipo | `typeof` | `Object.prototype.toString.call()` |
|---|---|---|---|
| 1 | `null` | `"object"` (impreciso) | `"[object Null]"` |
| 2 | `undefined` | `"undefined"` | `"[object Undefined]"` |
| 3 | `boolean` | `"boolean"` | `"[object Boolean]"` |
| 4 | `number` | `"number"` | `"[object Number]"` |
| 5 | `bigint` | `"bigint"` | `"[object BigInt]"` |
| 6 | `string` | `"string"` | `"[object String]"` |
| 7 | `symbol` | `"symbol"` | `"[object Symbol]"` |
| 8 | `object` | `"object"` | `"[object Object]"` (varia por subtipo, ex: `[object Array]`) |

## Referências

- `typeof` — operador nativo de checagem de tipo
- `Object.prototype.toString.call()` — forma mais precisa de checagem de tipo, usada historicamente em bibliotecas como Underscore
- `==` vs `===` — conversão de tipo implícita vs. comparação estrita
