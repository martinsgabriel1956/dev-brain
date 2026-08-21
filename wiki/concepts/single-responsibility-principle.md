---
type: concept
title: "Single Responsibility Principle (SRP)"
aliases: ["SRP", "single responsibility", "responsabilidade única"]
date_created: 2026-05-01
date_updated: 2026-08-18
source_count: 5
tags: [solid, oop, architecture]
skill: tech-mentor-backend
status: stub
---

## Definição

Uma classe deve ter apenas uma razão para mudar — ou seja, uma única responsabilidade.

## Relação com Proxy

No exemplo do [[proxy-pattern]]: o Controller não deve carregar lógica de cache (sua responsabilidade é orquestrar a requisição HTTP). A classe `ReportGenerator` não deve carregar lógica de cache (sua responsabilidade é gerar relatórios). O proxy assume a responsabilidade de cache isoladamente.

## "Razão para mudar" vs. "faz só uma coisa"

Via [[wiki/sources/design-pattern-facade-renato-augusto]]: SRP é frequentemente mal interpretado como "cada trecho de código deve fazer literalmente uma única ação". A formulação correta é sobre **motivo único de mudança**. Uma [[facade-pattern|Facade]] que orquestra pagamento, notificação e estoque num pedido não fere SRP se o único motivo dela mudar for o *processo de pedido* mudar — mesmo orquestrando múltiplas chamadas, ela opera num nível de abstração diferente das classes que chama, cada uma delas com SRP estrito.

## Posição contrária: nem toda orquestração escapa do SRP

[[wiki/sources/design-pattern-facade-codigo-fonte-tv]] discorda diretamente do parágrafo acima: para essa fonte, um método de [[facade-pattern|Facade]] que coordena avatar, documentos e histórico de acesso "faz muito mais coisa do que deveria estar fazendo" — SRP quebrado, na opinião do autor, mesmo reconhecendo que a orquestração em si não conhece os detalhes de implementação de cada serviço. Ver a comparação completa das duas posições em [[wiki/questions/facade-fere-srp-video-comparison]].

## Analogia da Máquina de Lavar

Via [[wiki/sources/principios-solid-ilustrados]]: numa máquina de lavar, basta uma meia vermelha para manchar todas as roupas claras. Em software acoplado, basta um componente no lugar errado para "manchar" o comportamento de todos os outros — ex.: cadastro e login numa mesma entidade "usuário", onde mudar o fluxo de cadastro quebra o login de quem já está cadastrado. Dica prática para achar o limite de uma responsabilidade: tente nomear a função/componente com tudo que ele faz — se o nome fica bizarro (`registrationAndImagingConfirmationAndAuthentication`), a entidade provavelmente acumulou responsabilidade demais.

## Definição Formal (Fonte Primária)

Via [[wiki/sources/solid-principles-in-pictures-ugonna-thelma]]: "uma classe deve ter uma única responsabilidade" — quando uma classe acumula responsabilidades, o risco de bug aumenta porque uma mudança numa delas pode afetar as outras sem querer.

## Key Sources

- [[wiki/sources/design-pattern-proxy]]
- [[wiki/sources/design-pattern-facade-renato-augusto]]
- [[wiki/sources/principios-solid-ilustrados]]
- [[wiki/sources/solid-principles-in-pictures-ugonna-thelma]]
- [[wiki/sources/design-pattern-facade-codigo-fonte-tv]] — posição contrária: Facade que orquestra múltiplos serviços fere SRP, mesmo sem lógica de negócio própria
