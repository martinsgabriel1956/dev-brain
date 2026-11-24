---
type: concept
title: "Imutabilidade"
aliases: ["immutability", "dados imutáveis", "readonly"]
date_created: 2026-04-25
date_updated: 2026-11-24
source_count: 12
tags: [imutabilidade, software-design, estado, clean-code, programacao-funcional, datomic, event-sourcing, strings, encoding]
skill: tech-mentor-backend
status: stable
---

# Imutabilidade

Imutabilidade significa que um valor **não pode ser alterado após ser criado**. Em vez de mutar, você cria um novo valor com a mudança aplicada.

## Por que importa

Dados mutáveis compartilhados são a principal fonte de bugs difíceis de rastrear (ver [[estado-compartilhado]]). Se os dados não podem ser mutados, múltiplas partes do sistema podem acessá-los com segurança.

## No TypeScript

```typescript
// readonly — sinaliza intenção no tipo
type Config = {
  readonly baseUrl: string;
  readonly timeout: number;
};

// Object.freeze — impede mutação em runtime
const CONFIG = Object.freeze({ baseUrl: "https://api.exemplo.com", timeout: 5000 });

// spread para criar novo objeto com mudança
const updatedConfig = { ...CONFIG, timeout: 10000 };
```

## Padrão funcional

Em vez de mutar, retornar novo estado:

```typescript
// mutável (problemático)
function addItem(cart: Cart, item: Item) {
  cart.items.push(item); // muta o original
}

// imutável (correto)
function addItem(cart: Cart, item: Item): Cart {
  return { ...cart, items: [...cart.items, item] };
}
```

## Relações

- [[estado-compartilhado]] — imutabilidade é a solução para os problemas de estado compartilhado
- [[efeito-colateral]] — funções imutáveis não têm efeitos colaterais
- [[acoplamento]] — dados imutáveis reduzem acoplamento implícito

## Em Sistemas Financeiros

[[ledger-imutavel]]: em bancos, saldo nunca é um campo que se atualiza — é a soma de todas as transações. Entradas no ledger são imutáveis; erros se corrigem com estornos.

[[datomic]] implementa imutabilidade no nível do banco de dados: acumula fatos (datoms) em um log append-only. Histórico completo sempre preservado com time-travel nativo.

[[wiki/concepts/event-sourcing]] aplica o mesmo princípio ao nível do domínio: eventos são fatos imutáveis, estado é derivado por replay.

## Por que Resolve Complexidade

Bugs de mutabilidade são difíceis de reproduzir, explodem em runtime, e surgem de código distante que modificou estado que você esperava inalterado. Eliminar mutabilidade elimina toda essa classe de bugs — esse é o argumento central do paper *"Out of the Tar Pit"* que influenciou as decisões técnicas do [[nubank]].

## Conexão com Programação Funcional

[[programacao-funcional]] torna imutabilidade o padrão estrutural do paradigma. Em [[clojure]], todas as estruturas de dados são imutáveis por default.

## Imutabilidade de Strings

Em quase todas as linguagens (Go, Java, Python, JavaScript, C#, Rust), [[string|strings]] são imutáveis. O motivo não é apenas evitar aliasing — é proteger o **encoding**. Uma string [[utf-8]] é um slice de bytes onde caracteres podem ocupar 1–4 bytes. Alterar 1 byte arbitrário pode fragmentar um caractere multi-byte, corrompendo silenciosamente o encoding.

Exemplo: o caractere chinês `世` ocupa 3 bytes em UTF-8. Sobrescrever apenas o primeiro byte resultaria em uma sequência inválida — o computador não saberia interpretar os bytes restantes. Por isso, ao invés de mutar, linguagens como Go forçam criar uma nova string.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]], Diego explica a imutabilidade do estado React ("criar um novo valor [...] com as modificações"), o spread em `formData` e `[...selectedItems, id]` em vez de `push`. A justificação é "performance", mas o motivo primário é que o React detecta mudança comparando referências.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]], o `handleSelectItem` com `filter` e spread é copiado da web sem mudança, e os estilos em array (`[styles.item, cond ? styles.selectedItem : {}]`) seguem a mesma lógica.

Em [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]], o `const` do JavaScript é "uma variável que não é para alterar o conteúdo". `const` impede reatribuir o nome; o objeto guardado continua mutável (`Object.freeze` para congelar). Ver [[wiki/concepts/var-let-const]].

Em [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]], `retangulo.a = 2` e `retangulo.border = 1` mudam e acrescentam propriedades depois de criado o objeto, a mutação comum em JavaScript. `Object.freeze` impediria as duas.

Em [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]], `map` e `forEach` não mudam o array original: o `map` devolve um array novo (a aula diz "modificado") e o `forEach` só executa o callback. Ver [[wiki/concepts/metodos-de-array-javascript]] para quais métodos mutam (`push`, `sort`) e quais copiam.

## Key sources

- [[wiki/sources/acoplamento-abstracao-estado]]
- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
- [[wiki/sources/como-strings-realmente-funcionam]] — motivação técnica para imutabilidade de strings: proteger encoding UTF-8 de corrupção por indexação de bytes

## Na NLW #2, dia 3 (Diego Fernandes)

"As variáveis [...] não são modificáveis" e "o React não fica observando variáveis comuns": na prática o JS permite mutar e o React re-renderiza quando o `set` é chamado com outra referência. Cópia com spread no `addNewScheduleItem` e `map` + `{ ...item, [field]: value }` no `setScheduleItemValue`. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]].

## Na NLW #2, dia 5 (Diego Fernandes)

O toggle de favorito usa `push` e `splice` no array lido do storage; como é uma cópia vinda do `JSON.parse`, funciona, mas `splice(-1, 1)` apaga o último se o id não existir. `filter` seria mais seguro. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]].

## No JavaScript Ninja, semana 3, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-metodos-de-objeto]], as duas operações que a imutabilidade separa aparecem juntas: reatribuir a variável (`pessoa = {...}`, objeto novo) e mutar o objeto (`pessoa.cor = ...`, `pessoa.idade++`). A aula usa a mutação como forma normal de acrescentar dados.

## Key sources (adição 2026-10-06)

- [[wiki/sources/estado-global-stateless-side-effects-reprodutibilidade-galego]] — config carregada uma vez e exposta read-only: [[wiki/concepts/estado-global-inofensivo]].
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: estado React: spread em vez de push
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: mesma seleção imutável no mobile
- [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]]: NLW #2, Diego, dia 3: spread e map nos horários
- [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]]: FrontPUSH, JavaScript aula 02: const ≠ imutável
- [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]]: NLW #2, Diego, dia 5: push/splice no array de favoritos
- [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]]: FrontPUSH, JavaScript aula 05: objeto mutável por padrão
- [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]]: FrontPUSH, JavaScript aula 07: map devolve array novo
- [[wiki/sources/javascript-ninja-metodos-de-objeto]]: JavaScript Ninja, semana 3, vídeo 02: reatribuir × mutar objeto
