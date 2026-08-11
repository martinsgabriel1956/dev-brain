---
type: concept
title: "Strangler Fig Pattern"
aliases: ["strangler pattern", "figueira mata-pau", "migração incremental"]
date_created: 2026-08-03
date_updated: 2026-08-10
source_count: 3
tags: [strangler-fig, migração, legado, proxy, cdc, feature-flags, arquitetura]
skill: tech-mentor-system-design
status: stub
---

# Strangler Fig Pattern

## TL;DR

Substitui um sistema legado de forma incremental, em vez de reescrita "big bang", em três estágios:

```
1. Transform (Intercept) → novo sistema construído em paralelo; proxy/gateway
                            colocado na frente do legado, tráfego ainda vai 100% para ele
2. Coexist   (Migrate)   → tráfego roteado gradualmente para o novo sistema
                            (por path, feature flag, ou percentual/canary),
                            enquanto o resto ainda vai para o legado
3. Eliminate             → quando 100% das funcionalidades estão no novo sistema,
                            o legado é desligado
```

Durante a fase de coexistência, dados compartilhados entre os dois sistemas são o ponto mais arriscado — a mitigação recomendada é CDC (ex.: Debezium) para sincronização, em vez de dual-write direto no mesmo banco.

## É a alternativa ao ciclo de "reescrever tudo do zero"

O [[wiki/concepts/ciclo-da-desgraca-software]] descreve o padrão de falha: reescrita completa que reproduz, na nova codebase, as mesmas pressões que geraram a antiga. Strangler Fig quebra esse ciclo porque a nova arquitetura recebe funcionalidade nova desde o primeiro dia, sem exigir que o legado pare de evoluir enquanto isso — os dois convivem sob um proxy de roteamento até o legado poder ser desligado com segurança.

Esse mesmo padrão de coexistência é o mecanismo concreto por trás da etapa "Migração" do [[wiki/concepts/ciclo-de-mudanca-de-arquitetura]]: depois que a POC valida o TO-BE na escala real, a transição do AS-IS para o TO-BE quase nunca é instantânea — é aqui que Strangler Fig entra.

## Armadilhas

- **Dados compartilhados**: legado e novo sistema acessando o mesmo banco ao mesmo tempo cria acoplamento oculto. Preferir Event-carried State Transfer ou réplica via CDC.
- **Funcionalidades entrelaçadas**: lógica de negócio espalhada por triggers, stored procedures e jobs no legado precisa ser mapeada antes de começar — senão a fase "Coexist" nunca termina.

## Relacionado

[[wiki/concepts/ciclo-de-mudanca-de-arquitetura]] · [[wiki/concepts/ciclo-da-desgraca-software]] · [[wiki/concepts/refactor-vs-rewrite-matrix]] · [[wiki/concepts/outbox-pattern]] · [[wiki/concepts/esb-enterprise-service-bus]] · [[wiki/concepts/cobol]]

## Por que sistemas em COBOL raramente são reescritos por inteiro

O caso mais extremo de "legado que não se reescreve" é justamente sistemas [[wiki/concepts/cobol|COBOL]] em bancos e no sistema financeiro: em vez de reescrita, a estratégia dominante é expor funcionalidades por API/filas de mensagens enquanto o núcleo de regra de negócio permanece intacto — o mesmo espírito do Strangler Fig, mesmo quando o time não usa esse nome para o processo.

## Key Sources

- [[wiki/sources/arquitetura-de-sacrificio]] — o "introduzir microsserviços depois para desmontar o monolito gradualmente" de Fowler é, na prática, este padrão
- [[wiki/sources/strangler-fig]]
- [[wiki/sources/ciclo-de-mudanca-de-arquitetura]]
- [[wiki/sources/tecnologias-hype-passado-soap-xml-esb-jquery-cobol]] — COBOL e SOAP como exemplos reais de "modernizar a borda, manter o núcleo legado" em vez de reescrita total
