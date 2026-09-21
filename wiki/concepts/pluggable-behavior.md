---
type: concept
title: "Pluggable Behavior"
aliases: ["pluggable behavior", "SBPP pluggable behavior", "pluggable method selector", "pluggable block"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 4
tags: [design-patterns, testes, xunit, smalltalk, kent-beck, reflection, sbpp]
skill: tech-mentor-testing
status: stub
---

# Pluggable Behavior

Padrão de Kent Beck (*Smalltalk Best Practice Patterns* [SBPP]) descrito em [[wiki/sources/pluggable-behavior-xunitpatterns]]: adicionar uma variável a um objeto para disparar um comportamento diferente **em tempo de execução**, sem precisar criar uma subclasse para cada variação. A motivação explícita do próprio Beck: é "uma solução muito melhor do que criar uma centena de subclasses diferentes, cada uma diferindo das outras em apenas um ou dois métodos".

## As duas variações

- **Pluggable (Method) Selector** — o objeto guarda o *nome* de um método já existente na classe, e o escolhe/invoca dinamicamente (tipicamente via [[wiki/concepts/reflection|reflection]]). É esta variação que [[wiki/concepts/testcase-object|Testcase Object]] usa.
- **Pluggable Block** — em vez de escolher entre métodos já existentes, quem cria o objeto injeta um [[wiki/sources/block-xunitpatterns|block]] de código arbitrário a ser executado depois. Mais próximo em espírito do [[wiki/concepts/command-pattern|Command Pattern]] — um pedaço de comportamento tratado como valor. Fonte primária isolada para o termo "block" (Smalltalk/Ruby: código passado a um método, executado em seu próprio contexto; equivalentes sem suporte nativo: anonymous inner class em Java, delegate em C#).

## Aplicação concreta: como o Testcase Object sabe qual Test Method rodar

[[wiki/sources/testcase-object-xunitpatterns]] já citava "Pluggable Behavior [SBPP]" de passagem, sem fonte primária dedicada — esta página fecha essa lacuna. O mecanismo: o construtor da Testcase Class recebe o **nome** do [[wiki/concepts/test-method|Test Method]] a executar como parâmetro (Pluggable Method Selector, não Pluggable Block — nenhum bloco de código é passado, apenas um nome), armazenado numa [[wiki/concepts/instance-variable|instance variable]]; o método `run` usa **reflection** para localizar e invocar esse método pelo nome guardado. É essa técnica que permite um único Testcase Object por Test Method sem exigir uma subclasse por teste.

## Distinção de padrões vizinhos

| | Pluggable Behavior | [[wiki/concepts/strategy-pattern|Strategy]] | [[wiki/concepts/command-pattern|Command]] |
|---|---|---|---|
| O que varia | Método/bloco escolhido em runtime | Algoritmo inteiro, injetado como objeto | Uma solicitação, objetificada |
| Mecanismo típico | Nome de método + reflection, ou bloco de código | Composição (objeto Strategy trocável) | Encapsular parâmetros de uma operação num objeto |
| Origem citada | Kent Beck, *Smalltalk Best Practice Patterns* | GOF | GOF |
| Uso em xUnit | Despacho do Test Method certo no Testcase Object | — | Testcase Object em si é um Command |

O **Pluggable Method Selector** tem a mesma motivação do Strategy (evitar `if/else`/subclasses para escolher comportamento), mas é mais leve: em vez de um objeto Strategy completo, basta um nome resolvido por reflection. O **Pluggable Block** é a variação mais próxima do Command — a diferença é que o Command formal (GOF) enfatiza parametrizar/enfileirar/desfazer, enquanto o Pluggable Block enfatiza apenas "deixe quem cria o objeto definir o que ele faz depois".

## Key Sources

- [[wiki/sources/pluggable-behavior-xunitpatterns]] — fonte primária dedicada, xUnitPatterns.com (Meszaros, citando Beck/SBPP): define as duas variações (Pluggable Method Selector, Pluggable Block)
- [[wiki/sources/testcase-object-xunitpatterns]] — aplicação concreta do Pluggable Method Selector ao despacho do Test Method dentro do Testcase Object
- [[wiki/sources/block-xunitpatterns]] — fonte primária isolada para o termo "block" usado na variação Pluggable Block: origem em Smalltalk/Ruby, equivalentes em Java (anonymous inner class) e C# (delegate)
- [[wiki/sources/reflection-xunitpatterns]] — fonte primária isolada do mecanismo que o Pluggable Method Selector usa para resolver o nome do método em runtime
