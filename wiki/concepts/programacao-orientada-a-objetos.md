---
type: concept
title: "Programação Orientada a Objetos"
aliases: ["POO", "OOP", "object-oriented programming", "orientação a objetos"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_count: 1
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

## Key sources

- [[wiki/sources/onde-foi-parar-programacao-orientada-a-objetos-bernardo-lobato]] — história do paradigma e tese de que ele mudou de lugar na arquitetura
