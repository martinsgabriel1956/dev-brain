---
type: concept
title: "Ciclo da Desgraça do Software"
aliases: ["software doom cycle", "reescrita do zero", "big rewrite", "ciclo de reescrita"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [arquitetura, legado, gestão, reescrita, anti-pattern]
skill: tech-mentor-leadership
status: stable
---

# Ciclo da Desgraça do Software

Espiral recorrente que começa com produtividade alta, cai progressivamente e culmina em uma reescrita que reproduz as mesmas condições do início.

## O Ciclo

```
1. Time pequeno, codebase jovem → alta produtividade
2. Velocidade cai com complexidade acumulada
3. Gerência contrata mais devs para acelerar
4. Novos devs desconhecem o design original
5. Cada commit pode afastar ou aproximar da intenção original — ninguém sabe
6. Mais pessoas = mais pressão = mais bagunça
7. Time exige reescrita do zero
8. Gerência cede (produtividade visível caindo)
9. Sistema antigo não pode ser descontinuado imediatamente
10. Dois sistemas em paralelo: legado com novas features + novo acelerando ao máximo
11. Nova codebase acumula as mesmas pressões → volta ao passo 1
```

## Por que a reescrita falha

- O sistema legado continua recebendo features durante a reescrita — "correr atrás do próprio rabo"
- Quem ficou no sistema antigo fica desmotivado
- O novo sistema, sob pressão de entregar rápido, reproduz as mesmas decisões ruins
- O conhecimento implícito no sistema legado (edge cases, regras de negócio não documentadas) demora anos para ser redescoberto

## Alternativa

[[concepts/strangler-fig-pattern]] — migra incrementalmente, sem reescrita big bang. Nova funcionalidade sempre na arquitetura correta; legado migra aos poucos.

## O "Engenheiro de Obra Pronta"

Quem entra numa empresa nova e imediatamente critica a codebase e propõe reescrever tudo. É fácil criticar *depois* que o problema se revelou — muito mais difícil é entender as restrições que produziram aquelas decisões.

> "Código legado é código que funciona e paga as contas."

## Ver também

- [[concepts/tech-debt]] — dívida técnica como causa raiz do ciclo
- [[concepts/principio-da-inversao]] — hábito ruim nº 3: propor reescrita ao entrar numa empresa
- [[concepts/strangler-fig-pattern]] — alternativa à reescrita big bang

## Key Sources

- [[sources/principio-da-inversao-programador]]
