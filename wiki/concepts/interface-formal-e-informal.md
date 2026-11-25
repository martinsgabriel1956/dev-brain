---
type: concept
title: "Interface Formal e Informal (Ousterhout)"
aliases: ["interface formal", "interface informal", "formal and informal interface", "interface vs implementação", "interface e implementação"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_count: 1
tags: [design, ousterhout, interface, modulo-profundo, documentacao, contrato]
skill: tech-mentor-backend
status: stub
---

# Interface Formal e Informal (Ousterhout)

## TL;DR

Para [[wiki/entities/john-ousterhout]], a interface de um módulo é **tudo o que um desenvolvedor de outro módulo precisa saber para usá-lo** ([[wiki/sources/filosofia-do-design-de-software-cap-04-modulos-devem-ser-profundos]], seções 4.1 e 4.2). Ela tem parte **formal**, escrita no código e parcialmente verificada pela linguagem, e parte **informal**, que só se descreve em comentários. Para a maioria das interfaces, a informal é maior e mais complexa.

## Interface e implementação

Todo módulo tem duas partes. A interface descreve **o que** o módulo faz, não **como**. A implementação é o código que cumpre as promessas da interface. Quem trabalha num módulo precisa entender a interface e a implementação dele, mais as interfaces dos módulos que ele chama. Não deveria precisar entender as implementações dos outros. Módulo, aqui, é qualquer unidade com interface e implementação: classe, método, função, subsistema ou serviço.

## As duas partes

| | Formal | Informal |
|---|---|---|
| Onde está | No código | Em comentários |
| Quem verifica | A linguagem, em parte | Ninguém |
| Método | Assinatura: nomes e tipos dos parâmetros, retorno, exceções | Comportamento de alto nível (ex.: a função apaga o arquivo passado) |
| Classe | Assinaturas dos métodos públicos, variáveis públicas | Restrições de uso (ex.: chamar um método antes de outro) |
| Tamanho típico | Menor | Maior e mais complexa |

A regra que decide o que entra: "se um desenvolvedor precisa saber de uma informação específica para conseguir usar um módulo, então essa informação faz parte da interface do módulo". Uma dependência de ordem entre métodos, que a linguagem não vê, faz parte da interface tanto quanto a assinatura.

## Por que importa

- **Elimina incógnitas desconhecidas.** Uma interface claramente especificada diz exatamente o que é preciso saber. Ver [[wiki/concepts/sintomas-de-complexidade-ousterhout]].
- **Mede o custo do módulo.** A complexidade de interface que conta para a [[wiki/concepts/modulo-profundo|profundidade]] inclui a parte informal. Um método com assinatura curta e restrições de uso escondidas tem interface larga.
- **Justifica o comentário de interface.** Se a parte maior da interface só existe em comentário, o comentário é parte do design, não enfeite. Ver [[wiki/concepts/comentarios-como-ferramenta-de-design]].
- **Especificação formal não substitui.** Em nota de rodapé, o autor diz que linguagens de especificação formal existem, quase todas em pesquisa, mas que uma interface em linguagem natural tende a ser mais compreensível. É opinião dele.

## Relação com outros conceitos

- [[wiki/concepts/abstracao]]: a interface é a abstração que o módulo oferece; detalhe importante fora da interface vira falsa abstração.
- [[wiki/concepts/causas-de-complexidade-ousterhout]]: a assinatura de um método é uma dependência; a parte informal mal documentada é obscuridade.
- [[wiki/concepts/contrato-de-api]]: o mesmo par formal/informal aparece em APIs (schema vs. semântica).
- [[wiki/concepts/classite]]: cada classe nova soma interface para aprender.

## Key Sources

- [[wiki/sources/filosofia-do-design-de-software-cap-04-modulos-devem-ser-profundos]]: definição de interface e implementação (4.1), parte formal e informal (4.2), nota de rodapé sobre especificação formal
