---
type: source
title: "Estado global: stateless, side effects e reprodutibilidade de bugs (Galego)"
aliases: ["estado global galego", "por que evitar estado global", "estado global servidor"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/estado-global-stateless-side-effects-reprodutibilidade-galego.md
source_url: ""
author: "Augusto Galego (inferido: locutor se chama \"galego\", cita \"cupom galego\" e curso de System Design)"
date_published: ""
date_ingested: 2026-10-06
source_count: 0
tags: [estado-global, stateless, side-effects, reprodutibilidade, injecao-de-dependencia, request-context, system-design, backend]
skill: tech-mentor-backend
status: draft
---

# Estado global: stateless, side effects e reprodutibilidade de bugs (Galego)

## TL;DR

[[wiki/entities/augusto-galego]] argumenta que o objetivo do HTTP/REST é ser [[wiki/concepts/stateless]] e que o servidor vira stateful sem querer por **estado global** (caches in-process, variáveis de módulo, configs mutáveis). Isso viola duas boas práticas — função não deve depender de algo externo nem gerar [[wiki/concepts/efeito-colateral]] — e produz contaminação entre requests, dependência da **ordem das chamadas**, [[wiki/concepts/race-condition]] e bugs **não reproduzíveis** ([[wiki/concepts/reprodutibilidade-de-bugs]]). Remédios: passar estado explicitamente, [[wiki/concepts/request-context]], [[wiki/concepts/dependency-injection]] e config read-only. Nem todo estado global é ruim ([[wiki/concepts/estado-global-inofensivo]]).

## Key claims

1. **HTTP stateless:** cada requisição carrega o necessário (inclusive identificação do usuário); `currentUser = x` no servidor não funciona com requests paralelos. Ver [[wiki/concepts/stateless]], [[wiki/concepts/estado-global-em-servidor]].
2. **Estado global tem formas sutis:** cache in-memory (`Map`, Redis local), variável no topo de módulo JS (módulo = singleton), config exportada, `currency`/`discount` fora da função. Ver [[wiki/concepts/estado-global-em-servidor]], [[wiki/concepts/singleton-pattern]], [[wiki/concepts/cache]].
3. **Função com dependência oculta + side effect** (`calculatePrice` lê `discount` global; `enableBlackFriday` só muta) torna a ordem de chamada relevante. Ver [[wiki/concepts/dependencia-externa-oculta]], [[wiki/concepts/estado-compartilhado]], [[wiki/concepts/programacao-funcional]].
4. **Bug não reproduzível:** parâmetro 30 nos logs não basta; o erro dependia de usuário *retail* com estoque zero vindo de fora. Ver [[wiki/concepts/reprodutibilidade-de-bugs]].
5. **Estado global gera race condition** com requests paralelos. Ver [[wiki/concepts/race-condition]].
6. **Mesmo input → mesmo output**, exceto funções que acessam banco/API; passe o objeto de usuário explicitamente. Ver [[wiki/concepts/dependencia-externa-oculta]].
7. **Request context** agrupa o contexto por requisição e facilita log/debug/reprodução. Ver [[wiki/concepts/request-context]].
8. **DI** expõe a dependência (ex.: `PaymentProvider`, `Logger` no construtor do `CheckoutService`), tornando possível saber qual era no momento. Ver [[wiki/concepts/dependency-injection]], [[wiki/concepts/composition-root]].
9. **Config:** exportar é OK; opcionalmente carregar uma vez e congelar (read-only), mas "geralmente não precisa". Ver [[wiki/concepts/estado-global-inofensivo]], [[wiki/concepts/imutabilidade]].
10. **Frameworks request/response** (FastAPI, Hono, Express) induzem a não compartilhar contexto, mas não garantem. Ver [[wiki/concepts/request-context]].

## Entities

[[wiki/entities/augusto-galego]]

## Concepts

[[wiki/concepts/estado-global-em-servidor]], [[wiki/concepts/dependencia-externa-oculta]], [[wiki/concepts/reprodutibilidade-de-bugs]], [[wiki/concepts/request-context]], [[wiki/concepts/estado-global-inofensivo]], [[wiki/concepts/stateless]], [[wiki/concepts/estado-compartilhado]], [[wiki/concepts/efeito-colateral]], [[wiki/concepts/race-condition]], [[wiki/concepts/dependency-injection]], [[wiki/concepts/singleton-pattern]], [[wiki/concepts/cache]], [[wiki/concepts/programacao-funcional]], [[wiki/concepts/imutabilidade]], [[wiki/concepts/requisicao-http]]

## Open questions / lacunas

- Request context na prática (ex.: `AsyncLocalStorage` em Node) não é mostrado; só o conceito.
- Cache in-process vs. distribuído: o vídeo não diz quando o cache local é aceitável (ver [[wiki/concepts/cache]]).
- O que fazer com estado externo inevitável (banco) para reproduzir bugs — sugestão de logar o estado lido não aparece; é **inferência minha**.
- Número/autoria: autor inferido, não confirmado.

## Contradições / tensões com a wiki

- Sem contradição. Nuance: [[wiki/concepts/singleton-pattern]] lista "cache compartilhado em processo único" e pool de conexão como usos legítimos; o vídeo trata cache in-process como estado global. Resolução (**inferência minha**): vale para estado imutável/idempotente por design, e para infra stateless-friendly (pool); o risco está em estado **de negócio mutável por request**.

## Quotes

> "A ordem com que você invoca esses métodos vai alterar o resultado final. Isso vai contra o nosso princípio de tentar fazer um negócio stateless."

> "Uma mesma função, dado que ela tem o mesmo input, deve retornar o mesmo output."
