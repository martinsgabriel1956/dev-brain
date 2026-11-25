---
type: concept
title: "Módulo Profundo (Deep Module)"
aliases: ["deep module", "shallow module", "módulo raso", "caixa cinza"]
date_created: 2026-07-09
date_updated: 2026-11-25
source_count: 9
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

## Por que a `java.io` ficou rasa: ausência de retorno múltiplo e over-otimização

[[wiki/sources/filosofia-design-software-podcast-eduardo-matos-otavio-santana-mauricio-linhares]] complementa o exemplo de classitis do Java I/O já registrado acima com uma explicação estrutural do motivo: a API foi desenhada para maximizar opções de otimização, não facilidade de uso, e algumas de suas falhas nascem de limitações da própria linguagem (ausência de retorno múltiplo, forçando o uso de uma constante especial para sinalizar fim de arquivo em vez de um resultado explícito). Só no Java 9 — quase duas décadas depois — apareceu um método simples para ler um arquivo inteiro em bytes; até lá, praticamente todo projeto Java reescrevia essa mesma classe utilitária, sinal de que a abstração pública estava errada ou incompleta. É citado como exemplo simultâneo de duas coisas: o melhor exemplo didático do padrão [[wiki/concepts/decorator-pattern|Decorator]] e o pior exemplo de design de API — ver a mesma fonte em [[wiki/concepts/decorator-pattern]].

O antídoto discutido não é eliminar as opções de baixo nível, mas empilhar camadas: oferecer uma interface simples de alto nível para o caso comum, com acesso de baixo nível disponível só para quem precisa. Exemplos citados na mesma fonte, complementares ao Unix I/O já registrado acima: o cliente HTTP padrão do Go (implementa três versões do protocolo HTTP e o handshake TLS por baixo, mas expõe request/response simples) e a função `file_get_contents` do PHP (aceita tanto caminho de arquivo local quanto URL, sem exigir do usuário nenhum conhecimento sobre a diferença).

## Mais linhas pode ser mais simples (cap. 2)

Antes de falar em módulos, o cap. 2 já recusa linhas de código como medida de complexidade: "às vezes, uma abordagem que exige mais linhas de código é, na verdade, mais simples, porque reduz a carga cognitiva". A fórmula do mesmo capítulo ($C = \sum_p c_p t_p$) explica por que a profundidade compensa: o que fica escondido atrás de uma interface simples quase não consome o tempo de quem só usa o módulo ([[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]]).

## Cap. 4 em primeira mão (2026-11-25)

[[wiki/sources/filosofia-do-design-de-software-cap-04-modulos-devem-ser-profundos]] traz o texto do capítulo que dá nome ao conceito. Quatro pontos que a página não tinha:

- **Custo e benefício.** A Figura 4.1 desenha cada módulo como um retângulo: a área é a funcionalidade e a borda superior é a interface. A interface é o **custo** (menos é melhor) e a funcionalidade é o **benefício** (mais é melhor). "Interfaces são boas, mas interfaces em maior quantidade ou mais extensas não são necessariamente melhores!"
- **Módulo é qualquer unidade com interface e implementação**, inclusive um método. A regra vale para funções, não só para classes e serviços.
- **A interface inclui a parte informal**: comportamento e restrições de uso que só cabem em comentário, e que costumam ser a maior parte ([[wiki/concepts/interface-formal-e-informal]]). Uma assinatura curta com regras de uso escondidas não faz um módulo profundo.
- **Exemplos rasos do próprio livro**: a classe de [[wiki/concepts/lista-encadeada]] e o método `addNullValueForAttribute`, cujo corpo é `data.put(attribute, null)`. "Módulos pequenos tendem a ser rasos." O excesso de classes pequenas tem página própria: [[wiki/concepts/classite]].

A regra que sai da 4.7 é **tornar o caso comum simples**: se a maioria só usa alguns recursos de uma interface, a complexidade efetiva dela é a desses recursos. Por isso o `lseek` não pesa para quem lê arquivos em sequência, e o buffer opcional do Java pesa para todo mundo.

## Cap. 5: ocultar é como se aprofunda (2026-11-25)

[[wiki/sources/filosofia-do-design-de-software-cap-05-ocultacao-de-informacao-e-vazamento]] liga as duas ideias: um módulo que esconde muito oferece mais funcionalidade com interface menor, e um que esconde pouco é raso de qualquer jeito, por ter pouca funcionalidade ou interface complexa (5.10). Dois casos novos de raso: duas classes para ler e analisar uma requisição HTTP, fundidas numa classe "mais profunda do que as originais" (5.5); e `getParams()` devolvendo o `Map` interno, trocado por `getParameter(name)` (5.6). Regra que sai da 5.5: o ocultamento muitas vezes melhora com uma classe **um pouco maior**, que junta todo o código de uma capacidade ou sobe o nível da interface (um método para o processamento inteiro em vez de um por etapa). Ver [[wiki/concepts/ocultamento-de-informacao]] e [[wiki/concepts/decomposicao-temporal]].

## Key Sources

- [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]]
- [[wiki/sources/filosofia-do-design-de-software-introducao]]
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]] — generalidade moderada (Cap. 6), Unix I/O e classitis do Java I/O (Cap. 4)
- [[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] — primeiro estudo controlado medindo o debate com Uncle Bob, e a distinção entre profundidade e grepability
- [[wiki/sources/filosofia-design-software-podcast-eduardo-matos-otavio-santana-mauricio-linhares]] — motivo estrutural da rasura do `java.io` (sem retorno múltiplo, otimização em vez de usabilidade); camadas simples sobre complexidade escondida no cliente HTTP do Go e em `file_get_contents` do PHP
- [[wiki/sources/filosofia-do-design-de-software-cap-01-traducao-revisada]] — tradução revisada do cap. 1: "as classes devem ser profundas" como exemplo de princípio quase filosófico
- [[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]] — LOC não mede complexidade; fórmula explica o ganho da profundidade
- [[wiki/sources/filosofia-do-design-de-software-cap-04-modulos-devem-ser-profundos]] — texto do cap. 4: Figura 4.1 como custo-benefício, módulo inclui método, parte informal da interface, lista encadeada e `addNullValueForAttribute` como rasos, caso comum simples
- [[wiki/sources/filosofia-do-design-de-software-cap-05-ocultacao-de-informacao-e-vazamento]] — ocultar como técnica de profundidade; classes um pouco maiores; HTTP leitura+análise e `getParams` como rasos
