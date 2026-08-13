---
type: concept
title: "Modelo de Domínio Anêmico"
aliases: ["anemic domain model", "domínio anêmico", "entidade anêmica", "classe anêmica", "anemic model"]
date_created: 2026-08-13
date_updated: 2026-08-13
source_count: 1
tags: [oop, ddd, encapsulamento, invariante, regra-de-negocio, anti-pattern, backend]
skill: tech-mentor-backend
status: stub
---

# Modelo de Domínio Anêmico

Anti-padrão em que uma classe de domínio carrega **dados sem comportamento**: só atributos com
getters e setters de atribuição pura, enquanto as regras de negócio ficam **fora** dela — em
"services", controllers ou espalhadas pelo sistema. O objeto vira um saco de dados (na prática,
uma [[wiki/concepts/objeto-vs-estrutura-de-dados|estrutura de dados]] disfarçada de objeto), e
qualquer parte do código pode colocá-lo num estado inválido sem passar por validação.

## Anêmico vs. rico

[[wiki/sources/encapsulamento-proteger-estado-invalido]] contrasta os dois na prática com uma
classe `Product`:

- **Anêmico** — atributos `public` (ou `private` com setters que só atribuem). Aceita
  `name = ""`, `price = -500`, `stock = -20` sem reclamar. As regras, se existirem, vivem fora
  do objeto e podem ser esquecidas.
- **Rico (não anêmico)** — atributos `private`; a mutação só acontece por métodos de comando
  (`changePrice`, `decreaseStock`…) que validam as **invariantes** antes de aplicar a mudança.
  O objeto **nunca** entra em estado inválido.

A chave: substituir setters de atribuição por **métodos que carregam comportamento e regra de
negócio**. Um `setPrice(x)` que só faz `this.price = x` não protege nada; um `changePrice(x)`
que rejeita `x <= 0` protege a invariante.

## Relação com outros conceitos

- [[wiki/concepts/encapsulamento]] — o modelo rico é o que o encapsulamento de verdade produz;
  `private` é a ferramenta, a invariante protegida é o fim
- [[wiki/concepts/objeto-vs-estrutura-de-dados]] — o modelo anêmico é tratar um objeto como se
  fosse estrutura de dados; entidade anêmica é o sintoma clássico dessa confusão
- [[wiki/concepts/ddd]] — no DDD, o agregado é responsável por proteger suas próprias
  invariantes; o modelo anêmico é o oposto disso
- [[wiki/concepts/modelagem-orientada-a-objetos]] — modelar o domínio é pôr as regras dentro dos
  objetos que as possuem, não fora deles

## Key sources

- [[wiki/sources/encapsulamento-proteger-estado-invalido]] — a classe "não anêmica" como fim do
  encapsulamento: toda mutação passa pelas regras de negócio do próprio objeto
