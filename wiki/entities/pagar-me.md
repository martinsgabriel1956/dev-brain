---
type: entity
title: "Pagar.me"
aliases: ["pagarme", "pagar.me"]
date_created: 2026-07-09
date_updated: 2026-07-22
source_count: 2
tags: [fintech, pagamentos, brasil, node-js]
skill: tech-mentor-leadership
status: stub
---

# Pagar.me

Empresa brasileira de meios de pagamento, do mesmo grupo da [[wiki/entities/stone]]. Cofundada por Pedro Franceschi. Escolheu Node.js como stack principal quando o modelo assíncrono single-thread ainda era uma tecnologia hype, apostando na concorrência sem multi-threading complexo — decisão discutida por Pedro Franceschi numa apresentação na RupyIC Conference (~11 anos antes de 2026).

[[wiki/entities/filipe-deschamps]] trabalhou na empresa e participou de entrevistas de contratação nessa época — observando que era mais fácil contratar para Node.js no Pagar.me do que para C# na Stone, apesar de C# ser tecnologia mais estabelecida e com pool de profissionais maior. Ver [[wiki/concepts/avaliar-hype-tecnologico]] para a análise completa desse caso via [[wiki/concepts/triade-retorno-risco-liquidez]].

## Cultura de Dogfooding e API-First

Segundo [[wiki/sources/os-3-estagios-de-maturidade-para-testar-codigo]], o Pagar.me era forte em **dogfooding**: a mesma API oferecida aos clientes para construir suas próprias soluções era a que a própria empresa usava para construir seus produtos internos (ex.: a dashboard). Essa escolha força uma separação clara entre cliente e servidor — o servidor não conhece o cliente —, permitindo conectar múltiplos clientes (dashboard web, app mobile, Postman) contra o mesmo back-end. [[wiki/entities/filipe-deschamps]] usa essa experiência como o segundo dos três estágios de maturidade que descreve para validar código — ver [[wiki/concepts/tres-estagios-maturidade-testes]].

## Key Sources

- [[wiki/sources/como-identificar-o-proximo-hype-tecnologico]]
- [[wiki/sources/os-3-estagios-de-maturidade-para-testar-codigo]] — cultura de dogfooding e API-first como base do segundo estágio de maturidade em testes
