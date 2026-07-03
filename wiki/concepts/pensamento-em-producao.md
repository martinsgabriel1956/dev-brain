---
type: concept
title: "Pensamento em Produção"
aliases: ["production mindset", "pensar em producao"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 3
tags: [carreira, arquitetura, observabilidade]
skill: tech-mentor-leadership
status: draft
---

# Pensamento em Produção

Preocupação com o comportamento do sistema depois que o código está rodando com usuários reais, em condições não previstas — em oposição a considerar o trabalho terminado quando o código compila e os testes passam.

## A diferença de mentalidade

> "O programador comemora quando o código compila e o teste passa. O engenheiro comemora quando o sistema sobrevive ao pico da Black Friday."

O código escrito é ~10% do trabalho. Os outros 90% são o sistema rodando em produção, com tráfego real, dados reais e falhas que não apareceram em nenhum teste.

## O que compõe

- Observabilidade: logs, métricas, rastreamento de requisições
- Indicadores de qualidade de serviço (SLIs/SLOs)
- Plano para quando as coisas derem errado — não apenas para quando derem certo

## Relação com outros conceitos

- [[wiki/concepts/engenheiro-vs-programador]] — é um dos componentes do "eixo horizontal" que separa quem executa de quem governa o sistema
- [[wiki/concepts/governanca-de-codigo-gerado-por-ia]] — código gerado por IA que nunca foi pensado para produção carrega esse risco de forma ampliada
- [[wiki/concepts/sintaxe-vs-conhecimento-perene]] — exemplos concretos de pensamento em produção (causas de 401/500, debugging só-em-prod, propagação de exceções) são o que [[wiki/sources/atrofia-cognitiva-ia-programacao]] chama de "conhecimento perene", em contraste com sintaxe memorizada

## Exemplos concretos de conhecimento perene

[[wiki/sources/atrofia-cognitiva-ia-programacao]] concretiza o que entra nesse "10%" que não é escrever código: saber as causas comuns de um erro 401 vs. 500, saber debugar uma falha que só acontece em produção (não no ambiente de dev), e saber desenhar a propagação de uma exceção — da camada de domínio até uma mensagem legível na interface, via hierarquia de classes de exceção e stack de chamadas. A fonte argumenta que esse é exatamente o tipo de conhecimento que continua relevante com ou sem IA, ao contrário de sintaxe memorizada.

## Validar em produção antes de fechar a tarefa

Uma aplicação prática e concreta desse mindset: depois do deploy, testar manualmente a funcionalidade em produção (não só em ambientes internos) antes de marcar a tarefa como concluída. Reportar um bug encontrado nessa checagem é sinal de comprometimento com o resultado final, não uma falha — ver [[wiki/concepts/code-review]].

## Key Sources

- [[wiki/sources/engenheiro-vs-programador-mercado-ia]]
- [[wiki/sources/atrofia-cognitiva-ia-programacao]] — exemplos concretos de conhecimento perene: erros 401/500, debugging só-em-produção, propagação de exceções
- [[wiki/sources/como-nao-ser-humilhado-no-primeiro-code-review]] — testar manualmente em produção após o deploy, antes de fechar a tarefa
