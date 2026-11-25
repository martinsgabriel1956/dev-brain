---
type: concept
title: "Classite (Classitis)"
aliases: ["classitis", "classite", "excesso de classes", "classes pequenas demais"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_count: 3
tags: [design, ousterhout, modulo-profundo, classes, java, orientacao-a-objetos]
skill: tech-mentor-backend
status: stub
---

# Classite (Classitis)

## TL;DR

Nome que [[wiki/entities/john-ousterhout]] dá à visão de que "classes são boas, então quanto mais classes, melhor" ([[wiki/sources/filosofia-do-design-de-software-cap-04-modulos-devem-ser-profundos]], seção 4.6). Num sistema com classite, cada classe nova recebe o mínimo de funcionalidade e, para ter mais funcionalidade, cria-se mais classe. Cada classe fica simples, mas as interfaces se somam e o sistema fica mais complexo. É a forma mais comum de produzir [[wiki/concepts/modulo-profundo|módulos rasos]]. O nome vem do sufixo médico "-ite", de inflamação, segundo a N.T.

## Como ela nasce

O senso comum ensina que classes devem ser pequenas e que métodos com mais de N linhas devem ser divididos, com N às vezes igual a 10. Seguida sem critério, a regra gera muitas classes e métodos rasos. A classite é o extremo dessa abordagem. Ousterhout aponta três custos:

1. **Interfaces acumuladas.** Classes pequenas contribuem pouca funcionalidade, então é preciso muitas, e cada uma tem sua interface para aprender.
2. **Boilerplate.** Cada classe traz sua estrutura repetida, e o código fica prolixo.
3. **Complexidade no nível do sistema.** O que parece simples classe a classe vira complexidade "tremenda" no todo.

## Caso típico: I/O do Java

Na seção 4.7, a biblioteca do Java é "um dos exemplos mais visíveis". Para ler objetos serializados de um arquivo era preciso criar `FileInputStream`, `BufferedInputStream` e `ObjectInputStream`, e os dois primeiros nunca mais eram usados. O pior é o buffer ser opcional: quem esquece o `BufferedInputStream` fica com I/O lento sem perceber. A correção que o livro propõe é tornar o caso comum simples: buffer por padrão e um mecanismo separado para desligá-lo. O ângulo de design pattern do mesmo caso está em [[wiki/concepts/decorator-pattern]], e o motivo histórico da API, segundo o podcast, em [[wiki/concepts/modulo-profundo]].

## Tensões na wiki

- **Responsabilidade única.** [[wiki/concepts/single-responsibility]] costuma ser ensinada como "classes pequenas, um motivo para mudar". Ousterhout não ataca o princípio pelo nome, mas o efeito prático da regra mal aplicada é a classite. Ver também [[wiki/concepts/ravioli-code]], o equivalente de código partido em peças pequenas demais.
- **Tamanho de função.** [[wiki/concepts/comprimento-de-funcao]] recusa o limite fixo de linhas por outro critério (aninhamento). Ousterhout recusa pelo critério de profundidade.
- **Classite não é culpa da linguagem.** O livro diz que o Java não exige classes pequenas: o problema é a cultura da comunidade.

## Relação com outros conceitos

- [[wiki/concepts/modulo-profundo]]: a classite é o caminho mais curto para módulos rasos.
- [[wiki/concepts/red-flags-de-design]]: "módulos pequenos tendem a ser rasos", no quadro de Módulo Raso.
- [[wiki/concepts/decorator-pattern]]: o `java.io` é o exemplo didático do padrão e o exemplo de classite.
- [[wiki/concepts/interface-formal-e-informal]]: cada classe nova soma interface formal e informal para aprender.

## Key Sources

- [[wiki/sources/filosofia-do-design-de-software-cap-04-modulos-devem-ser-profundos]]: definição (4.6) e o caso do I/O do Java (4.7), em primeira mão
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]]: primeira menção na wiki, no resumo do cap. 4
- [[wiki/sources/filosofia-design-software-podcast-eduardo-matos-otavio-santana-mauricio-linhares]]: por que o `java.io` ficou assim (otimização antes de usabilidade, sem retorno múltiplo)
