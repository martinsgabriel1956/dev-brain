---
type: concept
title: "Parâmetro de Configuração (Ousterhout)"
aliases: ["configuration parameter", "parâmetros de configuração", "knob de configuração", "parâmetro de ajuste"]
date_created: 2026-11-27
date_updated: 2026-11-27
source_count: 1
tags: [design, ousterhout, configuracao, complexidade, interface]
skill: tech-mentor-backend
status: stub
---

# Parâmetro de Configuração

## TL;DR

Valor que uma classe exporta para o usuário escolher em vez de decidir o comportamento por dentro (tamanho de cache, número de retentativas, intervalo de retentativa). Para Ousterhout, é o exemplo típico de mover a complexidade **para cima**, o oposto de [[wiki/concepts/puxar-complexidade-para-baixo]]. Regra: evitar o máximo possível e, quando inevitável, dar um padrão razoável. Fonte: [[wiki/sources/filosofia-do-design-de-software-cap-08-puxe-a-complexidade-para-baixo]] (8.2).

## A favor e contra

- **A favor:** às vezes o código de baixo nível não sabe a melhor política e o usuário conhece o domínio (quais requisições são mais sensíveis ao tempo e merecem prioridade). O parâmetro melhora o desempenho em vários domínios.
- **Contra:** é "uma desculpa fácil" para não resolver o problema. Muitas vezes o usuário não sabe o valor certo; outras vezes o sistema poderia calculá-lo. O valor configurado fica desatualizado quando as condições mudam; o calculado se ajusta.

## O teste antes de exportar

"Os usuários (ou módulos de nível superior) serão capazes de determinar um valor melhor do que nós podemos determinar aqui?" Se não, calcule (o intervalo de retentativa a partir do tempo medido das respostas, como no RTO do TCP [external: RFC 6298, https://www.rfc-editor.org/rfc/rfc6298]). Se sim, exporte com padrão razoável, para que só se mexa em condições excepcionais ([[wiki/concepts/sensible-defaults-paved-road]]).

## O que não é

O alvo do capítulo são botões de ajuste de comportamento. Configuração que depende do ambiente (endereço do banco, credencial), tratada em [[wiki/concepts/configuracao-vs-regra-de-negocio]] e no fator 3 do Twelve-Factor [skill: tech-mentor-backend, `references/architecture-evolutionary.md`], passa no teste: o módulo não tem como descobrir sozinho. Distinção da wiki, não do livro.

## Relação com outros conceitos

- [[wiki/concepts/retry-backoff]]: a tabela de parâmetros práticos da página é o tipo de valor que a 8.2 sugere calcular.
- [[wiki/concepts/interface-formal-e-informal]]: cada parâmetro aumenta a interface que o usuário precisa aprender.
- [[wiki/concepts/modulo-profundo]]: menos parâmetros, interface menor para a mesma função.

## Key sources

- [[wiki/sources/filosofia-do-design-de-software-cap-08-puxe-a-complexidade-para-baixo]] — 8.2: argumentos a favor e contra, intervalo de retentativa medido, pergunta antes de exportar, padrões razoáveis
