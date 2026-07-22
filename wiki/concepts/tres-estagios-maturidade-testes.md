---
type: concept
title: "Três Estágios de Maturidade Para Testar Código"
aliases: ["estágios de maturidade em testes", "de postman a jest watch mode", "iniciante intermediário experiente testar código"]
date_created: 2026-07-22
date_updated: 2026-07-22
source_count: 1
tags: [testes, maturidade-tecnica, jest, postman, api-first, dogfooding, carreira]
skill: tech-mentor-testing
status: draft
---

# Três Estágios de Maturidade Para Testar Código

Modelo de progressão pessoal (não uma taxonomia formal da indústria) para descrever como a forma de **validar e depurar código** evolui com a maturidade técnica — cada estágio muda o cliente HTTP usado contra o mesmo servidor, mas o que realmente muda é se o resultado da verificação vira uma especificação permanente ou uma checagem descartável.

## Estágio 1 — Clicar na interface manualmente

Testar uma funcionalidade repetindo sempre a mesma ação na própria interface web (front-end), navegando constantemente entre front-end e back-end para investigar, mudar e reverificar. Sensação de avanço a cada iteração — mas um avanço enganoso: cada mudança feita dessa forma reduz a mobilidade dentro do código, porque nada documenta ou trava o comportamento esperado. O sistema fica exponencialmente mais difícil de mexer conforme cresce, e uma alteração isolada no back-end, sem nenhuma relação com o front-end, ainda exige passar por ele só para conseguir "rodar" o código.

## Estágio 2 — Cliente HTTP dedicado contra uma API pensada API-first

Trocar a interface web por um cliente HTTP especializado (Postman, Thunder Client) contra uma API desenhada para múltiplos clientes — geralmente sustentada por uma cultura de **dogfooding**, onde a mesma API oferecida a clientes externos é a que a própria empresa usa para construir seus produtos internos (ver caso [[wiki/entities/pagar-me]]). Isso força pensar em termos de cliente/servidor desacoplados, onde o servidor não conhece o cliente. Ganhos reais: endpoints organizados, variáveis de ambiente trocadas automaticamente, nenhuma dependência de UI para "cutucar" o back-end.

**O limite desse estágio:** escala. À medida que o sistema cresce (dezenas ou centenas de funcionalidades, com um número grande de combinações de parâmetros), verificar manualmente que uma mudança não quebrou nada em outro lugar deixa de ser viável — cada alteração exigiria retestar manualmente cada endpoint e cada combinação relevante.

## Estágio 3 — Testes automatizados em modo watch

O mesmo cliente HTTP usado no Postman (ex.: `fetch`) passa a rodar dentro de um teste automatizado, com o test runner (ex.: Jest) em **modo watch**: qualquer alteração salva no arquivo reroda o teste sozinho, sem ação manual. A virada de chave dupla:

1. **O resultado da requisição vira uma expectativa executável** (`expect(response.status).toBe(...)`), não apenas uma inspeção visual — a especificação do comportamento esperado passa a existir como código, permanentemente.
2. **O teste se torna uma rede de segurança contra regressão futura**: uma alteração completamente não relacionada, feita meses depois em outro canto do código, pode reintroduzir o mesmo bug — e o teste antigo falha instantaneamente, sem qualquer verificação manual, apontando exatamente o que quebrou. Ver [[wiki/concepts/tdd]] e [[wiki/concepts/setup-live-reload-debug-testes]] para o ferramental que sustenta esse loop.

## Por que a expectativa "quebrando" é o sinal certo

No exemplo demonstrado (rota de migrations retornando `200` para usuário anônimo em vez de `403`), o teste falhar não significa que o teste está errado — significa que o código está exposto. A expectativa correta expõe o bug real; corrigir o código (não a expectativa) é o próximo passo. Esse é o mesmo princípio central por trás de por que a IA não deve deletar testes que falham, discutido em [[wiki/concepts/tdd]].

## Ver também

- [[wiki/concepts/setup-live-reload-debug-testes]] — o ferramental (live reload + debug + testes integrados) que viabiliza o modo watch em velocidade de `Ctrl+S`
- [[wiki/concepts/tdd]] — ciclo RED-GREEN-REFACTOR e por que testes não devem ser enfraquecidos para "passar"
- [[wiki/concepts/piramide-de-testes]] — onde testes de API/integração como o do exemplo vivem na estratégia de testes

## Key Sources

- [[wiki/sources/os-3-estagios-de-maturidade-para-testar-codigo]]
