---
type: concept
title: "Módulo de Propósito Geral (Um Tanto de Uso Geral)"
aliases: ["somewhat general-purpose", "um tanto de uso geral", "general-purpose module", "módulo de uso geral", "generalidade moderada", "empurrar especialização para cima", "push specialization up", "push specialization down"]
date_created: 2026-11-26
date_updated: 2026-11-27
source_count: 3
tags: [design, ousterhout, general-purpose, especializacao, api-design, modulo-profundo]
skill: tech-mentor-backend
status: draft
---

# Módulo de Propósito Geral (Um Tanto de Uso Geral)

## TL;DR

Heurística de [[wiki/entities/john-ousterhout]] (*A Philosophy of Software Design*, cap. 6): construa módulos **um tanto de uso geral**. A funcionalidade atende às necessidades de hoje; a interface não fica presa a elas. Para o autor, a interface geral sai mais simples e [[wiki/concepts/modulo-profundo|mais profunda]] que a especializada, com menos código, e é melhor mesmo que o módulo nunca seja reutilizado ([[wiki/sources/filosofia-do-design-de-software-cap-06-modulos-de-proposito-geral-sao-mais-profundos]]).

## O exemplo do editor

| | Especializada | Um tanto geral |
|---|---|---|
| Métodos | `backspace(Cursor)`, `delete(Cursor)`, `deleteSelection(Selection)` | `insert(Position, String)`, `delete(Position, Position)`, `changePosition(Position, int)` |
| Tipo de posição | `Cursor` (conceito da UI) | `Position` (conceito do texto) |
| Operação nova da UI | método novo na classe de texto | código só na UI |
| Backspace | escondido na classe de texto | `text.delete(text.changePosition(cursor, -1), cursor)`, visível na UI |

A versão especializada vazou conceitos da UI para a classe de texto ([[wiki/concepts/ocultamento-de-informacao]]) e amarrou as duas classes ([[wiki/concepts/acoplamento]]). O `backspace` era uma falsa abstração ([[wiki/concepts/abstracao]]): a UI precisa saber quais caracteres ele apaga.

## As três perguntas

1. **Qual é a interface mais simples que cobre todas as necessidades atuais?** Menos métodos sem perder capacidade indica generalidade. Não vale se cada método ganhar muitos argumentos.
2. **Em quantas situações o método será usado?** Método feito para um único uso é sinal de alerta.
3. **A API é fácil de usar para as necessidades atuais?** Se o chamador precisa de muito código extra, foi longe demais. Uma classe de texto de um caractere por vez é geral e simples, mas obriga a UI a escrever laços e fica lenta em operações grandes.

## Empurrar a especialização para cima ou para baixo

A especialização não some; ela fica separada do código geral.

- **Para cima:** as classes de topo são específicas da aplicação (a UI sabe o que o backspace faz); as de baixo, que implementam os recursos, ficam gerais.
- **Para baixo:** o sistema operacional define "ler um bloco" e "escrever um bloco", e cada driver de dispositivo implementa isso com seus comandos. O núcleo não conhece nenhum dispositivo, e um dispositivo novo entra sem mudar o núcleo.
- **Desfazer:** a classe `History` gerencia ações e barreiras sem saber o que elas fazem; cada módulo implementa as suas `History.Action`; a UI decide como agrupar. Ver [[wiki/concepts/command-pattern]].

A separação vale dentro de cada mecanismo. A classe de texto é geral para texto e pode conter o desfazer específico de texto, porque esse código está ligado às outras funções de texto.

## Tensões

- **[[wiki/concepts/yagni]].** O YAGNI manda não construir o que não se precisa hoje, e a página registra a regra "extrair só depois do segundo caso de uso". Ousterhout concorda na funcionalidade e discorda na interface: ela já nasce um tanto geral, com um único uso. O capítulo apresenta o argumento do uso específico (6.1) e diz que mudou de ideia depois de revisar projetos de alunos.
- **[[wiki/concepts/interface-segregation-principle]].** O ISP quebra interfaces gordas por cliente; o cap. 6 junta métodos específicos em poucos gerais. São eixos diferentes (leitura da wiki), e a classe de texto especializada viola os dois.
- **Generalidade demais.** "Um tanto" é parte da regra. A abordagem de um caractere por vez é o exemplo do livro de quando parar.

## Relação com outros conceitos

- [[wiki/concepts/modulo-profundo]]: o capítulo existe para mostrar que generalidade produz profundidade.
- [[wiki/concepts/eliminar-casos-especiais]]: a mesma ideia dentro do corpo dos métodos.
- [[wiki/concepts/programacao-tatica-vs-estrategica]]: a 6.1 compara o uso geral com a mentalidade de investimento do cap. 3.
- [[wiki/concepts/carga-cognitiva]]: poucos métodos gerais, reaproveitáveis, em vez de muitos métodos rasos para aprender.
- [[wiki/concepts/red-flags-de-design]]: a mistura de código geral e específico é o quadro *Special-General Mixture* (cap. 9).

## Drivers de novo no cap. 7

[[wiki/sources/filosofia-do-design-de-software-cap-07-camada-diferente-abstracao-diferente]] (7.2) volta aos drivers de disco: várias implementações da mesma interface, na mesma camada, são duplicação aceitável e reduzem a carga cognitiva. A 7.4 também retoma a classe de texto: a API por caracteres sobre armazenamento por linhas. Ver [[wiki/concepts/camada-diferente-abstracao-diferente]].

## Key Sources

- [[wiki/sources/filosofia-do-design-de-software-cap-06-modulos-de-proposito-geral-sao-mais-profundos]]: texto do cap. 6 em primeira mão: definição, editor, três perguntas, para cima e para baixo, `History`
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]]: resumo do cap. 6 e o cap. 11, que compara interfaces por linha, caractere e intervalo
- [[wiki/sources/filosofia-do-design-de-software-cap-07-camada-diferente-abstracao-diferente]] — drivers e classe de texto retomados (7.2 e 7.4)
