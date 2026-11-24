---
type: concept
title: "Programação Orientada a Objetos"
aliases: ["POO", "OOP", "object-oriented programming", "orientação a objetos"]
date_created: 2026-11-03
date_updated: 2026-11-24
source_count: 7
tags: [poo, oop, paradigma, historia-do-software, encapsulamento, polimorfismo, heranca]
skill: tech-mentor-backend
status: draft
---

# Programação Orientada a Objetos

## TL;DR

Paradigma que junta dados e o comportamento relacionado a eles numa mesma abstração. Segundo [[wiki/sources/onde-foi-parar-programacao-orientada-a-objetos-bernardo-lobato]], dominou a indústria nas décadas de 1990 e 2000 e hoje perdeu centralidade: continua boa para modelar domínio dentro de um serviço, mas não organiza mais o sistema inteiro.

## Origem

- **Simula** (Dahl e Nygaard, Norwegian Computing Center): introduziu classes, objetos e herança. [external] [Wikipedia](https://en.wikipedia.org/wiki/Simula)
- **[[wiki/entities/alan-kay|Alan Kay]] e Smalltalk** (Xerox, anos 70): objetos com estado próprio que se comunicam por mensagens.

As duas linhagens não coincidem. Kay define POO por mensagens, ocultação de estado e *late binding*, e deixou herança de fora como recurso embutido. [external] [e-mail de 2003](https://userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en) O ensino popular fixou outra lista: classes, objetos, herança, encapsulamento e polimorfismo.

## O que ela tentava resolver

Na leitura de [[wiki/sources/onde-foi-parar-programacao-orientada-a-objetos-bernardo-lobato]], a pressão vinha de sistemas corporativos maiores, com mais pessoas no mesmo código, e do custo crescente de mudar uma parte ligada a todas as outras ([[wiki/concepts/acoplamento]]). Os mecanismos:

| Mecanismo | Papel |
|---|---|
| [[wiki/concepts/encapsulamento]] | Esconder detalhes internos |
| [[wiki/concepts/abstracao]] | Expor os conceitos do domínio, não a implementação |
| [[wiki/concepts/polimorfismo]] | Desacoplar quem usa da implementação concreta |
| Composição | Montar estruturas complexas com partes menores |
| Herança | Reutilizar e especializar; papel depois questionado em [[wiki/concepts/heranca-vs-composicao]] |

## "Desceu um degrau"

Tese de [[wiki/entities/bernardo-lobato|Bernardo Lobato]], sem dados que a meçam: com [[wiki/concepts/arquitetura-distribuida]] e [[wiki/concepts/microsservicos]], as abstrações de topo passaram a ser serviços, contratos, eventos e filas. A POO fica dentro de cada serviço. Parte dela também foi absorvida por frameworks, como [[wiki/concepts/dependency-injection]] no Spring e no NestJS.

Onde segue fazendo sentido: estado, comportamento, invariantes, relações e responsabilidades dentro de um domínio, inclusive em [[wiki/concepts/ddd]] e na [[wiki/concepts/modelagem-orientada-a-objetos]].

Questionamentos abertos estão em [[wiki/sources/onde-foi-parar-programacao-orientada-a-objetos-bernardo-lobato]]: a visão de Kay lembra serviços que trocam mensagens, e o polimorfismo pode ter saído da conversa sem sair da prática.

Ver também [[wiki/concepts/programacao-procedural]], [[wiki/concepts/programacao-funcional]], [[wiki/concepts/design-patterns]] e [[wiki/concepts/objeto-vs-estrutura-de-dados]].

Em [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]], um objeto JavaScript é "basicamente uma classe gigante, uma caixa muito grande" com variáveis e funções (`console` é a caixa, `.log` a função). Objeto é instância, conjunto de propriedades; classe é o molde, e em JS `class` é sintaxe sobre protótipos.

Em [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]], a distinção sai certa: "console é um objeto em que quando eu aperto o ponto, eu tenho como acessar tanto os métodos, que são as funções, tanto as propriedades" (`log` é método, `memory` propriedade).

## No FrontPUSH, módulo de JavaScript, aula 05 (Násser)

Em [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]], a orientação a objetos é apresentada como abstração do mundo real: a caneta tem características (cor, comprimento, ponta) e funções (rabiscar, traço fino ou grosso), que viram atributos e métodos. A aula fica em objetos literais; a pergunta "está muito fixo" é respondida com mutação, quando a resposta de OO seria um molde (`class` ou função fábrica) para criar vários retângulos ([[wiki/concepts/objetos-javascript]]).

Em [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]], a primeira classe do FrontPUSH: `new XMLHttpRequest()`. "Uma classe [...] tem um conceito muito parecido com um objeto [...] quando você instancia ela em alguma variável, automaticamente essa variável vira um objeto [...] que herda todas essas propriedades." Em JavaScript a herança é por protótipo, e `new` chama um construtor ([[wiki/concepts/xmlhttprequest]]).

Em [[wiki/sources/frontpush-promises-resolve-reject-then-catch]], `new Promise(...)` é a segunda "classe" do curso: "eu estou instanciando uma classe, porque eu tenho new". Ele insiste que entender objetos é chave para "uma função dentro da outra, com instanciamento de classes".

## No JavaScript Ninja, aula 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]], o objeto JavaScript é explicado pela OO: "se você já trabalhou com uma linguagem orientada a objetos, você sabe que um objeto, ele tem propriedades e métodos". O exemplo (`pessoa` com `altura` e `peso`) é objeto literal, sem classe.

## Key sources

- [[wiki/sources/onde-foi-parar-programacao-orientada-a-objetos-bernardo-lobato]] — história do paradigma e tese de que ele mudou de lugar na arquitetura
- [[wiki/sources/frontpush-variaveis-tipos-de-dados-operadores-javascript]]: FrontPUSH, JavaScript aula 02: objeto como "classe gigante" (impreciso)
- [[wiki/sources/frontpush-functions-e-arrow-functions-javascript]]: FrontPUSH, JavaScript aula 04: método × propriedade no console
- [[wiki/sources/frontpush-objetos-javascript-atributos-metodos-this]]: FrontPUSH, JavaScript aula 05: caneta como objeto, atributos e métodos
- [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]]: FrontPUSH, JavaScript aula 14: classe e instância com XMLHttpRequest
- [[wiki/sources/frontpush-promises-resolve-reject-then-catch]]: FrontPUSH, JavaScript aula 15: Promise como classe instanciada
- [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]]: JavaScript Ninja, aula 01: objeto com propriedades e métodos, exemplo pessoa
