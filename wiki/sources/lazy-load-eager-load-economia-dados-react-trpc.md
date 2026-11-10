---
type: source
title: "Lazy load e eager load: como economizar leituras no banco combinando backend e front-end"
aliases: ["lazy load tulio faria", "lazy load tabuada trpc", "modo fominha eager load"]
date_created: 2026-11-10
date_updated: 2026-11-10
source_count: 0
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/lazy-load-eager-load-economia-dados-react-trpc.md"
source_url: ""
author: "Tulio Faria (DevPleno; nome reconstruído da legenda automática)"
date_published:
date_ingested: 2026-11-10
tags: [lazy-loading, eager-loading, n-plus-one, orm, prisma, trpc, react, tanstack-query, serverless, custo, backend, frontend]
skill: tech-mentor-backend
status: draft
---

# Lazy load e eager load: como economizar leituras no banco combinando backend e front-end

**Formato:** transcrição de vídeo do YouTube (legenda automática, PT-BR), limpa sem alteração de conteúdo. Parte do vídeo é codificação ao vivo, então a transcrição não mostra o código na tela.

## TL;DR

[[wiki/entities/tulio-faria]] explica por que o banco serverless do SaaS dele continua dentro do plano gratuito: as relações 1:N só são carregadas quando a tela precisa delas. Com 10 autores de 10 posts, o modo "fominha" ([[wiki/concepts/lazy-vs-eager-loading|eager]]) traz 100 posts a cada listagem, enquanto o lazy traz só os posts do autor aberto. Numa demonstração com [[wiki/entities/react]] e tRPC, ele mostra que o ganho depende de onde a busca está: um componente de lista que busca seus próprios dados gera 1 + 10 requisições, e um botão de expandir só resolve se a busca ficar num componente filho que nasce ao expandir. A listagem precisa vir enxuta, com o detalhe no `get by id`. O mesmo princípio vale para assets, como trocar o embed do YouTube por uma imagem até o clique.

## Key Claims

1. **Lazy é carregar à medida que precisa; eager carrega a relação inteira, mesmo sem uso.** Evidência: definição do autor com o exemplo autor e posts. Confiança: alta. Ver [[wiki/concepts/lazy-vs-eager-loading]].
2. **Relação 1:N em listagem multiplica os registros, e essa multiplicação é o "cheirinho" de que cabe lazy.** Com 10 autores e 10 posts cada, o eager traz 100 posts a mais em toda listagem. Evidência: aritmética correta (10 + 100 = 110 registros, contra 10, 20 ou 30 conforme se abrem 0, 1 ou 2 autores). Confiança: alta.
3. **Mudar de eager para lazy reduz a leitura "para 1 décimo".** Confiança: média, porque vale só no melhor caso. Sem nenhum autor aberto a razão é 10/110 (cerca de 9%); com um aberto, 20/110 (cerca de 18%). Se o usuário abrir todos, volta a 110 registros, agora em 11 requisições. O ganho depende de quão pouco o usuário expande.
4. **Regra de negócio pesada fica fora da listagem.** No SaaS do autor, checar colisão de horário exige várias buscas em modelos diferentes pelo [[wiki/concepts/orm|Prisma]], e fazer isso por item da lista multiplicaria a carga. Evidência: relato de produção, sem números por query. Confiança: média.
5. **Desenhar a tela para limitar a lista protege a leitura.** Todas as telas do SaaS são listadas por data, o que põe um teto no número de itens, mesmo com lazy. Evidência: relato do autor. Confiança: alta como heurística. Ver [[wiki/concepts/cursor-pagination]].
6. **Um componente de lista que busca o próprio detalhe gera 1 + 10 requisições.** O autor chama isso de eager, porque o dado trafega mesmo sem estar visível. Evidência: aba Network na demonstração. Confiança: alta para o fato. A nomenclatura pede cuidado: na wiki esse formato é o [[wiki/concepts/n-plus-one|N+1 entre front-end e backend]]. Um eager com JOIN traria os mesmos dados em uma só query.
7. **Botão de expandir não basta se a busca continuar no mesmo componente.** O estado `expanded` só esconde o resultado, e os dados seguem sendo carregados. A correção é manter o botão no componente da linha e renderizar o componente com a query só quando expandido. Evidência: demonstração, em que o F5 passa a fazer só o `get all`. Confiança: alta. Ver [[wiki/concepts/useQuery]].
8. **Se a tela precisa de tudo aberto, lazy não ajuda.** É preciso mudar a consulta da listagem para não buscar um a um. O autor sugere algo como um "soft count", termo ambíguo na legenda. Confiança: alta para o princípio. JOIN com agregação e batching são as saídas usuais `[skill: tech-mentor-backend]`.
9. **A recarga ao abrir e fechar acontece "porque o componente renderiza novamente".** Confiança: média, a explicação é imprecisa. Pelos padrões do TanStack Query, o refetch vem quando uma nova instância da query é montada com dado stale, e a página não lista re-render simples como gatilho ([external](https://tanstack.com/query/latest/docs/framework/react/guides/important-defaults)). Aqui o componente desmonta e remonta. O autor diz que "tá tudo bem", mas cada novo clique pode voltar ao banco, o que reduz a economia; um `staleTime` adequado evita isso. Ver [[wiki/concepts/tanstack-query]].
10. **Lazy no front-end não economiza nada se o `get all` já fizer eager no backend.** A listagem deve trazer só o necessário, e o `get by id` traz o expandido. Evidência: argumento, coerente com o Prisma, em que relações vêm por `include` explícito ([external](https://www.prisma.io/docs/orm/prisma-client/queries/relation-queries)). Confiança: alta.
11. **Hibernate escolhe lazy ou eager no ORM; em JavaScript é preciso antecipar, por causa do assincronismo.** Confiança: alta para o Hibernate, média para JavaScript. O guia do Hibernate define LAZY para `@OneToMany` e `@ManyToMany`, EAGER para `@ManyToOne`, e recomenda que quase toda associação seja lazy ([external](https://docs.hibernate.org/orm/current/introduction/html_single/)). Em JavaScript um getter síncrono não pode esperar o banco, mas o TypeORM contorna isso com relações lazy tipadas como `Promise`, ainda marcadas como experimentais ([external](https://typeorm.io/docs/relations/eager-and-lazy-relations/)). A generalização vale para o Prisma, não para todo ORM em JS.
12. **O termo também vale para assets: JavaScript pesado e embeds de vídeo.** Carrega-se uma imagem e troca-se pelo vídeo real do YouTube só no clique. Evidência: a técnica é a "facade" documentada pelo Chrome, que avisa que ela não tem toda a funcionalidade do embed real ([external](https://developer.chrome.com/docs/lighthouse/performance/third-party-facades)); a MDN documenta `loading="lazy"` e divisão de código ([external](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Lazy_loading)). Confiança: alta. Ver [[wiki/concepts/code-splitting]].
13. **O SaaS, já com faturamento e funcionário, usa de 5% a 10% da leitura gratuita mensal do CockroachDB.** Evidência: relato do autor, não auditável. Confiança: baixa para o número. As condições também mudaram: a página legada lista o Basic com 50 milhões de RUs e 10 GiB grátis por mês para clusters criados antes de 15 de setembro de 2026, e a página atual oferece um trial de 30 dias com US$ 400 em crédito ([legada](https://www.cockroachlabs.com/cockroachdb/pricing/), [atual](https://www.cockroachlabs.com/pricing/), `[external]`). Ver [[wiki/entities/cockroachdb]] e [[wiki/concepts/finops]].

> "Geralmente, quando você tem essa multiplicação, tem um cheirinho que você pode usar lazy load." (Tulio Faria)

## Entidades

- [[wiki/entities/tulio-faria]]: autor. O site do DevPleno o lista como fundador ([external](https://devpleno.com/)).
- [[wiki/entities/cockroachdb]]: banco serverless do SaaS.
- [[wiki/entities/react]]: camada da demonstração.
- Sem página própria: Prisma, tRPC, T3 App, Zod, GitHub Copilot, YouTube. Hibernate só aparece em [[wiki/concepts/hibernate-ddl-auto-validate]].

## Conceitos

- [[wiki/concepts/lazy-vs-eager-loading]]: página criada neste ingest.
- [[wiki/concepts/n-plus-one]]: o custo do lazy e o formato real da demonstração.
- [[wiki/concepts/orm]]
- [[wiki/concepts/lazy-initialization]]: o mesmo adiamento aplicado à criação de objetos.
- [[wiki/concepts/tanstack-query]], [[wiki/concepts/useQuery]]: base do `useQuery` do tRPC.
- [[wiki/concepts/code-splitting]]: lazy para JavaScript.
- [[wiki/concepts/database-index]]: a maioria das queries complexas do autor é indexada.
- [[wiki/concepts/cursor-pagination]]: teto de itens na listagem.
- [[wiki/concepts/finops]]: leitura como custo direto.
- [[wiki/concepts/tradeoff-arquitetural]]: lazy troca volume por requisições.

## Relação com fontes anteriores

- [[wiki/sources/problema-n-mais-1-graphql-orm-solucoes]] trata lazy como a causa do N+1 e recomenda eager/prefetch. Esta fonte recomenda o inverso. As duas se conciliam pelo padrão de acesso: quando quase todo item vai ser lido, eager em uma query vence; quando poucos são abertos, lazy vence.
- **Tensão:** [[wiki/concepts/n-plus-one]] dizia que "ORMs lazy-load relacionamentos por padrão", com exemplo em Prisma. O Prisma não descreve lazy transparente por acesso à propriedade, e a frase ganhou ressalva naquela página.

## Open Questions

- O que é o "soft count" citado no vídeo? Pode ser uma contagem agregada na listagem, mas é inferência.
- RUs do CockroachDB custam o mesmo em leitura e escrita? As páginas de preço lidas não dizem.
- A partir de que taxa de expansão o custo de N requisições supera o de uma query eager? A fonte não mede latência, só volume.
- Trechos ambíguos da transcrição estão no log e não mudam os claims técnicos.
