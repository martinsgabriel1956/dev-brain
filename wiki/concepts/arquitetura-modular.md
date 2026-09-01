---
type: concept
title: "Arquitetura Modular (vs. Monolito Modular)"
aliases: ["arquitetura modular", "modular architecture", "10 princípios da arquitetura modular"]
date_created: 2026-09-01
date_updated: 2026-09-01
source_count: 2
tags: [arquitetura-modular, monolito-modular, monorepo, nx, microsservicos, backend]
skill: tech-mentor-backend
status: draft
---

# Arquitetura Modular (vs. Monolito Modular)

Termo cunhado por [[wiki/entities/valdemar-neto]] para nomear o nível acima do [[wiki/concepts/monolito-modular|monolito modular]] clássico. A distinção:

- **Monolito modular**: um único artefato/deploy carrega **todos** os módulos de domínio. Mesmo permitindo `main.ts` alternativos que inicializam só um submódulo isoladamente (ver [[wiki/concepts/monolito-modular]], seção "Monolito é uma Escolha de Deploy"), ainda existe só **uma** forma fixa de agrupar os módulos por padrão.
- **Arquitetura modular**: existem **múltiplos monolitos/apps**, cada um compondo um subconjunto arbitrário dos mesmos módulos de domínio a partir de um único codebase (monorepo). Não há mais "o" monolito — há infinitas combinações possíveis de app.

Essa distinção nomeia, de forma mais hierárquica e explícita, o mesmo mecanismo que [[wiki/sources/evoluir-software-sem-pagar-preco-de-microsservicos]] já havia registrado na wiki como [[wiki/concepts/composicao-de-modulos|module composition]] — tratados aqui como sinônimos do mesmo padrão técnico, vindos de fontes/autores independentes.

## A Vantagem sobre Microsserviços: Componibilidade

O argumento central para a existência do termo: **microsserviços não compõem**. Não é possível colocar vários microsserviços dentro de uma mesma app/processo, porque cada um vive em codebase/repositório/pipeline próprios. Módulos de domínio num monorepo, ao contrário, podem ser recombinados em "infinitas" apps diferentes — um app pode carregar só `billing`, outro pode carregar `content` + `identity` juntos, sem duplicar código nem criar repositórios novos.

## Os 10 Princípios

Taxonomia numerada do autor (parte de um livro em produção) para escalar uma arquitetura modular:

1. **Limites bem definidos** — cada módulo isola o que é seu e não expõe internals; pertence a um domínio (design estratégico de DDD), não a uma feature. Na dúvida, comece com módulos grandes e deixe a coesão aparecer antes de quebrar em módulos menores.
2. **Componibilidade** — módulo não depende diretamente de outro módulo; é isolado o suficiente para ser composto livremente em diferentes apps.
3. **Independência** — módulo carrega tudo que precisa para rodar sozinho (testes end-to-end e de unidade, migrations, conexão de banco) — deveria ser possível só "pegar e mover" para outro repositório.
4. **Isolamento de estado** — cada módulo tem sua própria conexão de banco, roda as próprias migrations, só vê as próprias tabelas (idealmente banco próprio); conexões de Redis/filas também isoladas por módulo.
5. **Comunicação explícita** — nunca chamada direta a service de outro módulo; sempre via API HTTP (localhost) ou façade injetada por interface. Ver exemplo concreto em [[wiki/concepts/monolito-modular]] (Ports & Adapters).
6. **Substituibilidade** — módulo pode ser removido/trocado de uma app via configuração, sem afetar o resto da app.
7. **Deploy independente** — o módulo não faz deploy (quem faz é a app); mas o módulo é configurado para não saber do ambiente/app em que roda, pronto para qualquer combinação.
8. **Escala independente** — toda a configuração de escala (banco, serviços dependentes) fica dentro do módulo, nada externo.
9. **Monitoramento e observabilidade** — cada módulo com seu próprio setup, para que o time dono receba os alertas/métricas certos.
10. **Falhas isoladas** — circuit breakers e shutdown gracioso por módulo, para não propagar falha a outros módulos na mesma app.

## Por que Isso é Difícil num Monolito Modular Único

Aplicar os 10 princípios inteiramente dentro de **um só** monolito modular esbarra em três deles: deploy independente (exige ferramental próprio construído na mão), escala independente (tudo no mesmo processo/codebase) e falhas isoladas (mesmo processo compartilhado) — os três exigem sair do monolito único para múltiplas apps.

## Ferramental Habilitador

Resolvido via monorepo com detecção de "affected" — NX no exemplo demonstrado (NestJS), mas o autor cita Bazel e Maven como alternativas usadas em ecossistema Java. Ver [[wiki/concepts/monorepo-backend]] e [[wiki/concepts/composicao-de-modulos]] para o mecanismo `packages/`+`apps/` em detalhe.

## Por que Nem Clean/Hexagonal Nem DDD Cobrem Isso

[[wiki/sources/tres-tipos-de-modulos-arquitetura-modular-valdemar-neto]] posiciona a arquitetura modular como o nível seguinte a [[wiki/concepts/clean-architecture]] e [[wiki/concepts/hexagonal-architecture]]: ambas isolam domínio do mundo externo, mas nenhuma trata explicitamente de reuso de infraestrutura entre contextos nem de rodar módulos em processos separados — nem o Shared Kernel de [[wiki/concepts/ddd]] cobre isso. Nem a transição para microsserviços resolveu essa lacuna: cada microsserviço continua sendo, internamente, um codebase singular — mesma limitação do monolito tradicional, só que menor. A arquitetura modular é o que parte esse mesmo codebase em módulos com tipos e responsabilidades explícitos. Ver taxonomia completa em [[wiki/concepts/tipos-de-modulos]] (módulos de domínio, de infraestrutura pura e de feature).

## Key Sources

- [[wiki/sources/os-10-principios-arquitetura-modular-valdemar-neto]] — origem do termo e dos 10 princípios nesta wiki; exemplo de sistema de streaming (billing/streaming/identity/shared-infra) em NestJS/NX
- [[wiki/sources/tres-tipos-de-modulos-arquitetura-modular-valdemar-neto]] — posiciona arquitetura modular acima de Clean/Hexagonal/DDD; taxonomia de [[wiki/concepts/tipos-de-modulos|três tipos de módulo]] (domínio, infraestrutura pura, feature)
