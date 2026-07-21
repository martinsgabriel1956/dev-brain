---
type: concept
title: "Mapear Entrada/Processamento/Saída"
aliases: ["input processing output", "entrada processamento saída", "dividir tarefa em casos de teste"]
date_created: 2026-07-21
date_updated: 2026-07-21
source_count: 1
tags: [testes, decomposicao, tdd, given-when-then, planejamento]
skill: tech-mentor-testing
status: draft
---

# Mapear Entrada/Processamento/Saída

Técnica de decomposição de tarefa em casos de teste concretos, usando três campos-guia preenchidos progressivamente conforme a especificação e as regras de negócio ficam claras:

- **Entrada** — o que chega (endpoint, payload, parâmetros)
- **Processamento** — a regra de negócio aplicada (deixado em branco de propósito enquanto ainda não está claro — isso sinaliza exatamente o que falta perguntar)
- **Saída** — o resultado esperado (status code, corpo de resposta, efeito colateral)

## Combinação com Given/When/Then

Cada caso mapeado ganha também uma sentença no formato **dado/quando/então**, por exemplo:

> Dado um cliente com saldo atual de 1000 e limite de 1000, quando receber o pedido de saque de R$ 2.000, então retorna status code 422 sem processar a transação.

Isso é a mesma estrutura sintática do Given/When/Then usado em [[wiki/concepts/bdd]] — mas aqui como ferramenta **pessoal de planejamento e tradução direta para teste**, não como especificação formal em Gherkin compartilhada com o negócio. Não exige `.feature` files, step definitions ou engajamento de PO/QA — é uma anotação de texto livre que qualquer dev pode usar sozinho antes de codificar.

## Fluxo completo

```
1. Ler a especificação → extrair entrada e saída conhecidas
2. Ler as regras de negócio → extrair o processamento
3. Para cada regra/caso de erro → criar uma linha
   entrada / processamento / saída + "dado/quando/então"
4. Para cada linha → criar um teste anotado (it() pendente, ainda sem implementação)
5. Só depois de mapear todos os casos → implementar
6. Escrever o código do teste = transcrever exatamente a anotação
```

## Por que o campo "processamento em branco" importa

Deixar o processamento deliberadamente vazio quando a regra ainda não está clara é um sinalizador de risco explícito — evita a armadilha de assumir uma regra de negócio e só descobrir o engano na implementação ou, pior, em produção. Conecta com o pilar anterior de [[wiki/concepts/loop-de-confirmacao-de-entendimento]]: o campo vazio é literalmente a lista do que ainda precisa ser confirmado com quem passou a tarefa.

## Exemplo usado: Rinha de Backend

Demonstrado sobre a especificação pública do desafio [[wiki/entities/rinha-de-backend]] — uma API de transações de crédito/débito com validação de limite de cliente. A especificação pública descrevia o formato de entrada e saída, mas não deixava explícita toda a regra de negócio (o que já era, em si, informação a anotar); as regras de erro (débito que deixa saldo inconsistente → 422; cliente inexistente → 404) só apareciam lendo a documentação de regras separadamente.

## Relação com [[wiki/concepts/tdd]]

Esse mapeamento é o passo que precede o ciclo RED-GREEN-REFACTOR: cada linha da tabela entrada/processamento/saída vira o teste que vai falhar primeiro (RED). A técnica resolve um problema prático comum do TDD — saber *o que* testar antes de escrever o primeiro teste — ao forçar a decomposição da especificação em casos discretos antes de qualquer código.

## Key Sources

- [[wiki/sources/3-pilares-testes-automatizados-produtividade]]
