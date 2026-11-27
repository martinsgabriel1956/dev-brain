---
type: concept
title: "Método de Repasse (Pass-Through Method)"
aliases: ["pass-through method", "método pass-through", "métodos de repasse", "método passa-através"]
date_created: 2026-11-27
date_updated: 2026-11-27
source_count: 2
tags: [design, ousterhout, red-flag, pass-through, modulo-profundo, refatoracao]
skill: tech-mentor-backend
status: draft
---

# Método de Repasse (Pass-Through Method)

## TL;DR

Red flag de [[wiki/entities/john-ousterhout]] (cap. 7): um método que não faz nada além de passar os argumentos para outro método, geralmente com a mesma API. Indica que não há divisão clara de responsabilidade entre as classes ([[wiki/sources/filosofia-do-design-de-software-cap-07-camada-diferente-abstracao-diferente]]). É a forma mais comum de [[wiki/concepts/camada-diferente-abstracao-diferente|camadas adjacentes com a mesma abstração]].

## O exemplo do livro

```java
public Character getLastTypedCharacter() {
    return textArea.getLastTypedCharacter();
}
public void insertString(String textToInsert, int offset) {
    textArea.insertString(textToInsert, offset);
}
```

Num editor de alunos, 13 dos 15 métodos públicos de `TextDocument` eram assim, repassando para `TextArea`.

## Por que é ruim

- **Deixa a classe rasa**: a interface cresce e a funcionalidade do sistema não ([[wiki/concepts/modulo-profundo]]).
- **Cria dependência**: mudou a assinatura em `TextArea`, muda em `TextDocument` ([[wiki/concepts/acoplamento]]).
- **Separa interface de implementação em classes diferentes**: "a interface de uma funcionalidade deve estar na mesma classe que implementa a funcionalidade".

## Como corrigir (Figura 7.1)

1. Expor a classe de baixo nível direto aos chamadores.
2. Redistribuir a funcionalidade para que as classes não precisem chamar uma à outra.
3. Juntar as classes, se não der para separar. O aluno juntou `TextDocument`, `TextArea` e `TextDocumentListener` em duas.

A pergunta-guia: por quais recursos e abstrações cada uma das classes é responsável?

## Não é repasse

- *Dispatcher*: mesma assinatura, mas escolhe quem executa.
- Várias implementações da mesma interface (drivers), na mesma camada.
- Wrapper que traduz uma interface externa imutável para a da aplicação, o que a wiki chama de [[wiki/concepts/adapter-pattern]] (o livro não usa o nome).

## Relação com outros conceitos

- [[wiki/concepts/decorator-pattern]]: decorators "costumam conter muitos métodos de repasse".
- [[wiki/concepts/architecture-sinkhole]]: o mesmo problema em camadas inteiras (leitura da wiki).
- [[wiki/concepts/objeto-de-contexto]]: a versão do problema com variáveis, em vez de métodos.
- [[wiki/concepts/red-flags-de-design]]: *Pass-Through Method* no catálogo do apêndice.

## Key sources

- [[wiki/sources/filosofia-do-design-de-software-cap-07-camada-diferente-abstracao-diferente]]: quadro do red flag, `TextDocument`, Figura 7.1 e casos aceitáveis (7.1 e 7.2)
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]]: primeira menção na wiki (13 de 15 métodos)
