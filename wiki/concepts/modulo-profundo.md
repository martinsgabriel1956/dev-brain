---
type: concept
title: "Módulo Profundo (Deep Module)"
aliases: ["deep module", "shallow module", "módulo raso", "caixa cinza"]
date_created: 2026-07-09
date_updated: 2026-08-04
source_count: 4
tags: [arquitetura, complexidade, design, ousterhout, interface, encapsulamento]
skill: tech-mentor-backend
status: draft
---

# Módulo Profundo (Deep Module)

## TL;DR

Conceito de [[wiki/entities/john-ousterhout]] (*A Philosophy of Software Design*): um **módulo profundo** esconde muita funcionalidade atrás de uma interface simples — a complexidade fica encapsulada dentro. Um **módulo raso** faz o oposto: expõe pouca funcionalidade atrás de uma interface relativamente complexa, multiplicando o número de peças que quem lê o código precisa rastrear ao mesmo tempo.

## Profundo vs. raso

| | Módulo Profundo | Módulo Raso |
|---|---|---|
| Funcionalidade | Muita, escondida | Pouca, exposta |
| Interface | Simples | Complexa |
| Consumidor precisa olhar por dentro? | Não (mas pode) | Praticamente sim |
| Custo cognitivo de leitura | Baixo — poucos blocos grandes | Alto — muitos blocos pequenos para navegar |

Poucos módulos grandes e profundos, com interfaces bem projetadas, tendem a produzir bases de código mais fáceis de entender do que muitos módulos pequenos que só delegam uns aos outros.

## Por que importa na era da IA

Agentes de IA são bons em produzir módulos rasos por padrão — muitas funções pequenas, cada uma fazendo pouco. Isso é ruim para a própria IA: ao explorar a base de código depois, ela precisa navegar por um número maior de peças, tem mais chance de não encontrar a dependência certa a tempo, e frequentemente falha em entender o sistema como um todo.

Módulos profundos, por outro lado, permitem tratar a implementação como **caixa cinza**: o humano projeta e revisa cuidadosamente a **interface** (que deve ter alto controle humano, pois um erro de design aí se propaga), mas pode delegar a **implementação** por trás dela à IA sem revisar linha a linha — desde que a fronteira seja testável e o propósito do módulo esteja claro. Ver [[wiki/concepts/tdd]] — módulos profundos são o que torna uma base de código genuinamente testável, porque a fronteira de teste é a própria interface, simples por definição.

Existe uma skill de refatoração citada na fonte ("improve codebase architecture") cujo objetivo é migrar uma base de código de módulos rasos para módulos profundos: explorar o código em busca de blocos relacionados e envolvê-los dentro de uma fronteira única com interface simples.

## Origem no enquadramento geral do livro

[[wiki/sources/filosofia-do-design-de-software-introducao]] (fonte primária, capítulo 1) enquadra módulos profundos como a elaboração da segunda das duas estratégias gerais contra complexidade que abrem o livro: **eliminar** complexidade (código mais simples/óbvio) vs. **encapsular** complexidade (design modular). Módulo profundo é a forma de fazer um módulo encapsular bem — módulo raso é encapsulamento malfeito. O texto também cita "classes devem ser profundas" como exemplo do tipo de princípio filosófico (não receita mecânica) que o livro inteiro oferece — reforçando que é uma heurística de comparação entre alternativas, não uma regra absoluta. Ver também [[wiki/concepts/red-flags-de-design]]: módulo raso é um dos red flags mais citados no livro.

## Relação com outros conceitos

- [[wiki/concepts/complexidade-acidental]] — módulos rasos são uma forma comum de complexidade acidental: a estrutura, não o problema em si, é o que dificulta entender o sistema.
- [[wiki/concepts/arquitetura-de-software]] — decisão de estrutura que escala bem (poucos módulos profundos) vs. que gera bola de neve (muitos módulos rasos).
- [[wiki/concepts/tdd]] — interfaces simples de módulos profundos são o que torna o ciclo RED-GREEN-REFACTOR sustentável.
- [[wiki/concepts/modelo-cascata-vs-desenvolvimento-incremental]] — módulos profundos como estratégia de encapsulamento se aplicam melhor sob design incremental, onde a interface pode ser revisada e ajustada a cada iteração.
- [[wiki/concepts/red-flags-de-design]] — módulo raso é o red flag concreto correspondente a este conceito.

## Generalidade moderada torna módulos mais profundos

[[wiki/sources/filosofia-do-design-de-software-livro-completo]] (Cap. 6) mostra que módulos de propósito **ligeiramente** geral ("somewhat general-purpose" — funcionalidade reflete a necessidade atual, mas a interface não) tendem a ser mais profundos que módulos especializados, mesmo quando o único uso real é especializado. Exemplo canônico: uma classe de texto de editor com métodos `backspace(cursor)` e `deleteSelection(selection)` (espelhando a UI) vaza conhecimento da interface entre UI e classe de texto; a versão com apenas `insert(position, text)` e `delete(start, end)` elimina o vazamento, tem menos código no total, e ainda serve sem alteração para um caso de uso totalmente diferente (busca-e-substituição em arquivo). A regra prática: empurrar especialização para cima (código de UI) ou para baixo (device drivers), nunca deixá-la contaminar o módulo genérico central. Ver também [[wiki/concepts/ocultamento-de-informacao]] — generalidade e ocultamento de informação se reforçam mutuamente.

## Deep module como exemplo de interface deep vs. shallow no mundo real

A mesma fonte cita a interface de I/O do Unix (cinco chamadas de sistema — `open`, `read`, `write`, `lseek`, `close` — escondendo centenas de milhares de linhas de implementação) e o coletor de lixo de linguagens como Go/Java (que não tem interface nenhuma — na verdade encolhe a interface do sistema, já que elimina a necessidade de liberar objetos manualmente) como os dois exemplos mais extremos de módulo profundo do livro. Em contraste, a família de classes do Java I/O (`FileInputStream` → `BufferedInputStream` → `ObjectInputStream`, precisando de três construtores encadeados só para abrir um arquivo com buffer) é o contra-exemplo citado repetidamente no livro como **classitis**: a crença de que "classes são boas, logo mais classes são melhores".

## Primeiro Dado Empírico no Debate com Uncle Bob

[[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] traz o primeiro dado empírico (ainda que direcional, sem nome ou link do estudo) para o debate histórico entre Ousterhout e [[wiki/entities/uncle-bob]] sobre função pequena vs. módulo profundo. Num estudo controlado com agentes de IA como "leitor" mensurável: quebrar métodos e classes densos em helpers pequenos deu **empate** de resultado — a explicação apontada foi que a extração redistribui a complexidade em vez de eliminá-la, e o agente, que lê o arquivo inteiro de qualquer forma, não se beneficia da quebra em si. Isso reforça diretamente o argumento de Ousterhout: o que importa não é o tamanho da função, é se a complexidade foi genuinamente encapsulada atrás de uma interface, ou só redistribuída em mais lugares.

A exceção notável do mesmo estudo (-35% tokens num caso) não veio de profundidade — veio de [[wiki/concepts/codigo-grepavel|grepability]]: funções menores e nomeadas ficaram mais fáceis de localizar por busca textual em tarefas futuras. Isso é ortogonal ao debate módulo-profundo-vs-função-pequena — uma vantagem específica de agentes que navegam por busca, não de leitores sequenciais.

## Key Sources

- [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]]
- [[wiki/sources/filosofia-do-design-de-software-introducao]]
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]] — generalidade moderada (Cap. 6), Unix I/O e classitis do Java I/O (Cap. 4)
- [[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] — primeiro estudo controlado medindo o debate com Uncle Bob, e a distinção entre profundidade e grepability
