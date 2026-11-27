---
type: concept
title: "Objeto de Contexto (e Variável de Passagem)"
aliases: ["context object", "contexto (ousterhout)", "variável de passagem", "pass-through variable", "argumento de repasse", "pass-through argument"]
date_created: 2026-11-27
date_updated: 2026-11-27
source_count: 2
tags: [design, ousterhout, estado-global, pass-through, configuracao, testabilidade]
skill: tech-mentor-backend
status: draft
---

# Objeto de Contexto (e Variável de Passagem)

## TL;DR

**Variável de passagem** é a que desce por uma cadeia de métodos que não a usam, só para chegar a quem precisa. **Objeto de contexto** é a saída que [[wiki/entities/john-ousterhout]] mais usa: um objeto por instância do sistema com todo o estado global (configuração, subsistemas compartilhados, contadores), referenciado pelos objetos principais ([[wiki/sources/filosofia-do-design-de-software-cap-07-camada-diferente-abstracao-diferente]], 7.5). O próprio autor diz que contextos "estão longe de ser uma solução ideal", mas não achou nada melhor.

## O problema

`main` lê um argumento de linha de comando com certificados. Só `m3`, que abre o *socket*, usa `cert`, mas a variável aparece na assinatura de `m1` e `m2`. Todos os intermediários ficam cientes dela, e adicionar uma variável nova depois obriga a mudar muitas interfaces.

## As quatro opções (Figura 7.2)

| Opção | Como | Custo |
|---|---|---|
| (a) Passar | `cert` em toda assinatura | todo método intermediário conhece a variável |
| (b) Objeto já compartilhado | `obj.cert` | o objeto pode virar ele mesmo variável de passagem |
| (c) Global | `cert` global | impede duas instâncias no mesmo processo, o que atrapalha testes ([[wiki/concepts/estado-global-em-servidor]]) |
| (d) Contexto | `context.cert`, com `timeout` e `metrics` | desvantagens de global, se usado sem disciplina |

## Como o contexto circula

Os objetos principais guardam uma referência ao contexto como variável de instância. Quem cria um objeto novo pega a referência do próprio objeto e passa ao construtor. O contexto aparece explícito só nos construtores. Isso é injeção pelo construtor ([[wiki/concepts/dependency-injection]]) de um único objeto; o livro não usa o termo (leitura da wiki).

## Vantagens segundo o livro

- Variável nova entra no contexto sem mexer em código existente, exceto construtor e destrutor do contexto.
- O estado global fica num lugar só, fácil de achar.
- Testes mudam a configuração global alterando campos do contexto.
- Várias instâncias do sistema convivem no mesmo processo, cada uma com o seu contexto.

## Riscos

- Não fica óbvio por que uma variável está no contexto nem onde é usada.
- Sem disciplina, vira um "amontoado desorganizado de dados" (*grab-bag*, na N.T.) com dependências não óbvias.
- *Thread-safety*: a melhor defesa é manter as variáveis do contexto imutáveis, o que o aproxima do [[wiki/concepts/estado-global-inofensivo]].

## Relação com outros conceitos

- [[wiki/concepts/request-context]]: agrupa o contexto **por requisição** e o passa adiante; o objeto de contexto agrupa **por instância do sistema** e fica guardado nos objetos. Os dois rejeitam o global.
- [[wiki/concepts/metodo-de-repasse]]: a mesma duplicação entre camadas, com métodos em vez de variáveis.
- [[wiki/concepts/dependency-lookup]]: um contexto com subsistemas dentro funciona como registro onde o código busca dependências. Paralelo da wiki, não do livro.

## Key sources

- [[wiki/sources/filosofia-do-design-de-software-cap-07-camada-diferente-abstracao-diferente]]: texto da 7.5, Figura 7.2, vantagens e riscos
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]]: primeira menção na wiki (contexto como campo de instância)
