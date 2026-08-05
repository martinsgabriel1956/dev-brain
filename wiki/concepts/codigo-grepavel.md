---
type: concept
title: "Código Grepável"
aliases: ["grepability", "código buscável", "greppable code"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 1
tags: [ia-engineering, codebase-quality, agentes, tool-call, refatoracao]
skill: tech-mentor-ai
status: stub
---

# Código Grepável

Propriedade de um código-fonte onde funções e blocos relevantes têm nomes distintos o suficiente para serem localizados por busca textual (grep) — uma qualidade que importa especificamente para agentes de IA, não apenas para leitores humanos.

## Por Que é um Critério Diferente de Legibilidade

Legibilidade tradicional avalia se um humano, lendo sequencialmente, entende o código. Grepability avalia algo diferente: se um agente, que descobre o codebase por busca em vez de leitura sequencial, consegue **encontrar** o trecho relevante antes mesmo de precisar entendê-lo.

[[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] descreve um estudo controlado onde quebrar um bloco de código denso em funções menores não melhorou a tarefa em si (a lógica só foi redistribuída, não simplificada — ver [[wiki/concepts/modulo-profundo]]), mas em um caso gerou 35% menos tokens consumidos. A causa apontada não foi a função individual ficar mais clara — foi o código ter ficado buscável: ao planejar uma tarefa e precisar localizar algo relacionado em outros arquivos, o agente consegue fazer grep e achar a função pelo nome, em vez de precisar ler arquivos inteiros para descobrir onde algo está implementado.

## Relação com Comentários Como Sinal de Recuperação

[[wiki/concepts/codebase-legibilidade-ia]] já registra uma observação complementar da mesma família: comentários próximos ao código são informação que o agente efetivamente recupera no momento da busca (via grep), diferente de documentação externa que pode nunca ser encontrada. Grepability e comentários-como-sinal-de-recuperação são a mesma lógica aplicada a duas coisas diferentes — nome de função buscável vs. texto de comentário buscável.

## Implicação Prática

A justificativa para quebrar um bloco grande em funções menores nomeadas, na era dos agentes, não é mais só "cada função faz uma coisa" (regra clássica de [[wiki/entities/uncle-bob|Uncle Bob]]) — é tornar aquele bloco **achável de fora**, algo que um leitor humano sequencial não precisava tanto porque já estava com o arquivo inteiro aberto.

## Key Sources

- [[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]]
