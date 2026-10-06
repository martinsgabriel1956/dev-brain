---
type: concept
title: "Dependência Externa Oculta"
aliases: ["hidden dependency", "função impura por dependência", "mesmo input mesmo output"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [funcoes-puras, side-effects, injecao-de-dependencia, reprodutibilidade]
skill: tech-mentor-backend
status: draft
---

# Dependência Externa Oculta

Função cujo resultado depende de algo que **não está nos parâmetros**: `calculatePrice(30)` lendo um `discount` global, ou `charge(order)` usando um `paymentProvider` instanciado fora. Olhando só a assinatura (ou o log da chamada), não se sabe o resultado.

## Regra

Mesmo input → mesmo output, salvo funções que acessam **explicitamente** banco ou API. Função puramente de código não deve depender de nada fora nem alterar nada fora ([[wiki/concepts/efeito-colateral]]). Contraste do vídeo: `calculateSubtotal(lista)` com `reduce` é autocontida; acumular num `subtotal` externo não é.

## Como tornar explícita

- Passar o objeto (ex.: o `user`) como argumento — reproduzir o bug vira reconstruir o objeto.
- [[wiki/concepts/dependency-injection]] para serviços (`PaymentProvider`, `Logger` no construtor) — o estado da instância revela qual era a dependência.
- [[wiki/concepts/request-context]] para contexto por requisição.

Limite admitido: o acesso a banco continua sendo externo e incontrolável. Base: [[wiki/concepts/programacao-funcional]], [[wiki/concepts/reprodutibilidade-de-bugs]].

## Key sources

- [[wiki/sources/estado-global-stateless-side-effects-reprodutibilidade-galego]]
