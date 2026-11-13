---
type: concept
title: "Lazy Loading vs. Eager Loading"
aliases: ["lazy load", "eager load", "carregamento preguiçoso", "carregamento antecipado", "modo fominha"]
date_created: 2026-11-10
date_updated: 2026-11-13
source_count: 2
tags: [lazy-loading, eager-loading, orm, performance, banco-de-dados, frontend, custo]
skill: tech-mentor-backend
status: draft
---

# Lazy Loading vs. Eager Loading

Duas estratégias para decidir **quando** dados relacionados são carregados. **Eager** traz a relação junto com o item principal, mesmo sem uso. **Lazy** adia a busca até o momento em que o dado é necessário. Ver [[wiki/sources/lazy-load-eager-load-economia-dados-react-trpc]].

## O trade-off

| | Eager | Lazy |
|---|---|---|
| Volume lido | Tudo, sempre | Só o que foi aberto |
| Número de requisições | Pode ser uma, com JOIN | Uma por item aberto |
| Melhor quando | Quase todo item será lido | Poucos itens serão abertos |
| Risco | Multiplicar registros sem uso | [[wiki/concepts/n-plus-one]] |

Com 10 autores de 10 posts, eager lê 110 registros por listagem. Lazy lê 10, mais 10 por autor aberto. Se o usuário abrir todos, lazy volta aos 110, agora em 11 requisições. A decisão depende do padrão de acesso, como todo [[wiki/concepts/tradeoff-arquitetural|trade-off]].

## Lazy na interface

Esconder o resultado não adia a busca. A query precisa estar num componente que só é montado ao expandir (reconstrução da demonstração da fonte):

```tsx
function Tabuada({ id, title }: Props) {
  const [expanded, setExpanded] = useState(false);
  return (
    <div>
      <h2>{title}</h2>
      <button onClick={() => setExpanded((v) => !v)}>Mostrar/ocultar</button>
      {expanded && <TabuadaCompleta id={id} />}
    </div>
  );
}
```

Duas condições para o ganho ser real: o endpoint de listagem não pode já trazer a relação, e o cache precisa evitar nova ida ao servidor a cada abertura. O [[wiki/concepts/tanstack-query|TanStack Query]] refaz a busca quando uma nova instância monta com dado stale ([external](https://tanstack.com/query/latest/docs/framework/react/guides/important-defaults)).

## Nos ORMs

- **Hibernate:** LAZY para `@OneToMany` e `@ManyToMany`, EAGER para `@ManyToOne`; o guia recomenda que quase toda associação seja lazy ([external](https://docs.hibernate.org/orm/current/introduction/html_single/)).
- **Prisma:** relações vêm por `include` explícito, e as páginas lidas não descrevem carregamento lazy por acesso à propriedade ([external](https://www.prisma.io/docs/orm/prisma-client/queries/relation-queries)). O dataloader agrupa `findUnique()` no mesmo tick, mas não `findMany()` ([external](https://www.prisma.io/docs/orm/prisma-client/queries/query-optimization-performance)).
- **TypeORM:** relações lazy tipadas como `Promise`, marcadas como experimentais ([external](https://typeorm.io/docs/relations/eager-and-lazy-relations/)).

Ver [[wiki/concepts/orm]].

## Em assets

O mesmo princípio vale para `loading="lazy"` em imagens e iframes ([external](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Lazy_loading)), para [[wiki/concepts/code-splitting]] e para a "facade", que mostra uma imagem no lugar do embed até o clique ([external](https://developer.chrome.com/docs/lighthouse/performance/third-party-facades)).

## Ver também

- [[wiki/concepts/lazy-initialization]]: o adiamento aplicado à criação de objetos.
- [[wiki/concepts/finops]]: em banco cobrado por uso, cada leitura evitada é custo evitado.

## Key Sources

- [[wiki/sources/lazy-load-eager-load-economia-dados-react-trpc]]
- [[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]] — "carregamento sob demanda" citado como otimização de imagem do lado do código, sem detalhe
