---
type: concept
title: "Bounded Context"
aliases: ["bounded context", "contexto delimitado"]
date_created: 2026-08-18
date_updated: 2026-10-01
source_count: 6
tags: [ddd, arquitetura, cqrs, microsservicos]
skill: tech-mentor-backend
status: stub
---

# Bounded Context

## TL;DR

Fronteira explícita dentro da qual um modelo de domínio (e sua Ubiquitous Language) é válido e consistente. Fora dessa fronteira, o mesmo termo pode significar outra coisa — é a unidade de escopo do [[wiki/concepts/ddd]]. [[wiki/sources/cqrs-martin-fowler]] usa o conceito para delimitar onde o [[wiki/concepts/cqrs]] deve ser aplicado: nunca ao sistema inteiro, apenas a bounded contexts específicos onde a separação leitura/escrita genuinamente compensa a complexidade adicional.

## Relação com CQRS

Fowler é explícito: aplicar CQRS como estilo arquitetural geral para um sistema inteiro — em vez de restringi-lo a um bounded context específico — é o erro mais comum que ele observou, e a principal causa de complexidade e risco desnecessários em projetos corporativos.

## Módulo de Monolito Modular = Bounded Context

[[wiki/sources/microsservicos-monolito-first-renato-augusto]] usa bounded context como a unidade de módulo dentro de um [[wiki/concepts/monolito-modular]]: cada módulo (ex.: catálogo de produtos, pedidos, carrinho, clientes, pagamentos) tem sua própria linguagem ubíqua, entidades e regras de negócio, mesmo compartilhando processo e conexão de banco com os demais. Só quando esses bounded contexts estão claramente visíveis no código é que faz sentido extrair um deles para [[wiki/concepts/microsservicos]] — ver [[wiki/concepts/monolith-first]].

## Dificuldade de Acertar Fronteiras no Início (Monolith First)

[[wiki/sources/monolith-first-martin-fowler]] traz o segundo argumento central do princípio [[wiki/concepts/monolith-first]]: microsserviços só funcionam bem com bounded contexts bons e estáveis, mas mesmo arquitetos experientes em domínios familiares erram as fronteiras no início de um projeto — refatorar funcionalidade entre serviços já distribuídos é muito mais caro do que dentro de um monolito. Construir o monolito primeiro dá tempo de descobrir as fronteiras certas antes que o design distribuído as trave.

## Base Conceitual dos Serviços em Microsserviços

[[wiki/sources/microsservicos-historia-soa-esb-bernardo-lobato]] reforça que os serviços dentro de uma arquitetura de microsserviços são "fortemente inspirados" em bounded context: cada serviço deve ter uma e somente uma responsabilidade dentro de um contexto delimitado. É a mesma ideia já central nesta página (fronteira do modelo de domínio), aqui aplicada como pré-requisito conceitual — antes mesmo de discutir extração ou maturidade de módulo — para que um serviço seja considerado um "microsserviço" de fato, e não apenas uma divisão técnica arbitrária.

## Limite Linguístico e Semântico: Duas Classes para o Mesmo Conceito

[[wiki/sources/bounded-context-contextos-delimitados-bernardo-lobato]] ([[wiki/entities/bernardo-lobato|Bernardo Lobato]], *Dominando DDD #4*) define o bounded context como **limite linguístico e semântico do domínio da solução**: até onde um termo tem significado consistente. Exemplo (imagem de [[wiki/entities/martin-fowler]]): "Produto" em Vendas (preço, palavras-chave, estoque) vs. Suporte (só ID, nome, descrição curta) → **duas classes**, cada uma só com o que o contexto precisa — menos [[wiki/concepts/acoplamento]] entre times, mais [[wiki/concepts/coesao]] dentro do módulo. Classes separadas podem mapear a **mesma tabela** (mapeamento parcial de colunas) — o autor não discute o acoplamento de dados que isso mantém (inferência).

**Distinções:** ≠ [[wiki/concepts/subdominio]] (divisão do *negócio*; um subdomínio pode ter 1+ contextos) e ≠ [[wiki/concepts/ubiquitous-language]] (o contexto define onde a linguagem vale; analogia país/dialeto). **Como identificar:** conflito de vocabulário entre times em refinamento/discovery. **Integração entre contextos:** [[wiki/concepts/shared-kernel]], [[wiki/concepts/customer-supplier]], [[wiki/concepts/conformist]], [[wiki/concepts/anti-corruption-layer]] — ver [[wiki/concepts/context-map]].

## Key Sources

- [[wiki/sources/monolith-first-martin-fowler]] — fonte primária: dificuldade de acertar bounded contexts no início como segundo argumento contra começar com microsserviços
- [[wiki/sources/microsservicos-monolito-first-renato-augusto]] — bounded context como unidade de módulo do monolito modular, critério de maturidade para extração a microsserviço
- [[wiki/sources/microsservicos-historia-soa-esb-bernardo-lobato]] — bounded context como base conceitual de "uma e somente uma responsabilidade" dentro de um serviço de microsserviços
- [[wiki/sources/cqrs-martin-fowler]]
- [[wiki/sources/bounded-context-contextos-delimitados-bernardo-lobato]] — fonte primária do bounded context como limite linguístico; duas classes "Produto" (Vendas/Suporte); ≠ subdomínio, ≠ linguagem ubíqua
- [[wiki/sources/vertical-slice-organizar-codigo-por-funcionalidade-bernardo-lobato]] — duas representações de Usuário por slice como a mesma lógica de fronteira semântica, em granularidade mais fina; ver [[wiki/concepts/dominio-centralizado-vs-modelo-por-slice]]
