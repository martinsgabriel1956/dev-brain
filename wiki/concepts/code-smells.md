---
type: concept
title: "Code Smells"
aliases: ["code smell", "cheiro de código", "sinais de código ruim"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 1
tags: [code-smells, clean-code, refactoring, craftsmanship]
skill: tech-mentor-backend
status: draft
---

# Code Smells

Um code smell é um sinal de que um trecho de código **talvez** esteja deteriorando em qualidade — não uma prova determinística de que o código está ruim ou precisa ser refatorado. É o mesmo espírito de [[wiki/concepts/red-flags-de-design]] (Ousterhout): um sintoma a investigar, não uma regra a aplicar cegamente. A diferença é de linhagem — "code smell" é o termo clássico associado a Martin Fowler e ao livro *Refactoring* (ver [[wiki/sources/refatoracao-pragmatic-programmer-martin-fowler-2a-edicao]]), enquanto "red flag" é o vocabulário específico de *A Philosophy of Software Design*. Os catálogos se sobrepõem parcialmente mas não são idênticos.

## Régua para julgar um smell

[[wiki/sources/9-code-smells-como-identificar-codigo-ruim]] propõe seis critérios para decidir se um smell concreto é, de fato, um problema a corrigir: o código é **compreensível**, **testável**, tem **baixo acoplamento** ([[wiki/concepts/acoplamento]]), **alta coesão** ([[wiki/concepts/coesao]]), é **modular** e de **fácil manutenção**? Se um trecho apresenta um smell mas ainda satisfaz essas seis propriedades, não há necessidade de refatorar apenas por reflexo.

## Catálogo (vídeo de origem)

1. **Funções muito longas** — carga cognitiva alta, difíceis de testar; nem sempre um problema real se ainda forem compreensíveis, testáveis e de fácil manutenção.
2. **[[wiki/concepts/god-object|God Objects]]** — classe que concentra responsabilidades não relacionadas (ex.: autenticação + banco + notificação na mesma classe). Corrigido via composição/injeção de serviços especializados.
3. **[[wiki/concepts/dry|DRY]] levado longe demais ou não aplicado o suficiente** — repetição pequena (2 pontos) é tolerável; duplicação em 3+ pontos vira risco real de manutenção.
4. **Condicional gigante** — cadeias longas de `if`/`elif` combinando múltiplas dimensões (ex.: país × peso). Testes de 100% dos branches são a rede de segurança mínima; estruturas de dados (dicionários, polimorfismo) tendem a ser mais legíveis que a cadeia condicional.
5. **Números mágicos** (e "coisas mágicas" em geral — URLs, chaves de API hard-coded) — dificultam busca e manutenção porque um valor cru não é distinguível de coincidências textuais. Ver [[wiki/concepts/naming]].
6. **[[wiki/concepts/feature-envy|Feature Envy]]** — uma classe acessando dados internos de outra para fazer um cálculo que não é sua responsabilidade.
7. **[[wiki/concepts/data-clumps|Grupos de dados (data clumps)]]** — variáveis relacionadas passadas soltas em vez de agrupadas num tipo.
8. **Comentários inúteis** — um comentário que só existe para compensar um nome/estrutura pouco claros é, ele mesmo, sinal de falta de clareza no código. Ver [[wiki/concepts/comentarios-como-ferramenta-de-design]].
9. **[[wiki/concepts/primitive-obsession|Uso exacerbado de tipos primitivos]]** — dados como e-mail ou dinheiro representados como string/int crus, sem tipo dedicado que garanta validação por construção.

## Como usar smells na prática (aviso do vídeo)

Não varrer a code base inteira caçando smells para refatorar sem antes considerar o objetivo real a atingir. Às vezes a melhoria é cara demais para valer a pena, ou a guideline simplesmente não se aplica ao cenário. A recomendação é entender o **conceito por trás** de cada smell (por que ele indica risco de manutenção/compreensão/acoplamento), não seguir os exemplos específicos como regras rígidas — o mesmo espírito de "toda regra de design tem exceções" já registrado em [[wiki/concepts/red-flags-de-design]].

## Relacionado

[[wiki/concepts/red-flags-de-design]] · [[wiki/concepts/refatoracao]] · [[wiki/concepts/god-object]] · [[wiki/concepts/acoplamento]] · [[wiki/concepts/coesao]] · [[wiki/concepts/tech-debt-como-ferramenta]] · [[wiki/concepts/naming]]

## Key Sources

- [[wiki/sources/9-code-smells-como-identificar-codigo-ruim]]
