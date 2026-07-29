---
type: concept
title: "Ocultamento de Informação (Information Hiding)"
aliases: ["information hiding", "information leakage", "vazamento de informação", "decomposição temporal", "temporal decomposition"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 1
tags: [arquitetura, complexidade, design, ousterhout, information-hiding, parnas]
skill: tech-mentor-backend
status: draft
---

# Ocultamento de Informação (Information Hiding)

## TL;DR

Técnica central (David Parnas, 1972) para produzir [[wiki/concepts/modulo-profundo|módulos profundos]]: cada módulo deve encapsular uma ou poucas decisões de design (algoritmo, estrutura de dados, formato de arquivo, suposição sobre o domínio), de forma que essa informação fique invisível para o resto do sistema. O oposto — **vazamento de informação** — ocorre quando a mesma decisão se reflete em múltiplos módulos, criando uma dependência entre eles mesmo que nenhum dos dois a exponha publicamente na interface ("back-door leakage").

## Como reduz complexidade

Duas vias, segundo [[wiki/entities/john-ousterhout]] (*A Philosophy of Software Design*, Cap. 5): (1) simplifica a interface — quem usa uma árvore-B não precisa saber o fanout ideal dos nós; (2) facilita evolução — se uma informação está escondida, não há dependências fora do módulo que a contém, então uma mudança de design relacionada a ela afeta só aquele módulo.

**Importante:** declarar uma variável/método como `private` não é a mesma coisa que ocultar informação. Getters e setters expõem a natureza e o uso da variável tão publicamente quanto se ela fosse `public` — o encapsulamento sintático (privado) não implica encapsulamento semântico (informação escondida).

## Vazamento de informação (Information Leakage)

Ocorre quando uma decisão de design se reflete em mais de um módulo. Exemplo do livro: duas classes que ambas entendem o formato de um mesmo tipo de arquivo (uma lê, outra escreve) — mesmo que nenhuma exponha isso na interface pública, mudar o formato exige mudar as duas. Esse tipo de vazamento "por trás" é mais perigoso que vazamento via interface porque não é óbvio.

## Decomposição temporal — a causa mais comum de vazamento

**Decomposição temporal** é estruturar módulos pela ordem em que operações ocorrem em tempo de execução ("primeiro lemos o arquivo, depois parseamos, depois escrevemos"), em vez de pelo conhecimento necessário para cada tarefa. Exemplo canônico do livro: um servidor HTTP dividido em uma classe para *ler* a requisição da rede e outra para *parsear* a string lida — como o cabeçalho `Content-Length` precisa ser parseado para saber onde a requisição termina, a classe de leitura já precisa entender boa parte do formato HTTP, duplicando conhecimento com a classe de parsing. A correção foi fundir as duas em uma única classe.

Regra prática: a ordem de execução quase sempre importa e vai aparecer em algum lugar do código — mas não precisa (e geralmente não deveria) determinar a estrutura de módulos.

## Relação com outros conceitos

- [[wiki/concepts/modulo-profundo]] — ocultamento de informação é a técnica-mãe para produzir módulos profundos; quanto mais se esconde, mais funcional e mais simples a interface tende a ficar.
- [[wiki/concepts/red-flags-de-design]] — Information Leakage e Temporal Decomposition são dois dos 14 red flags catalogados no livro.
- [[wiki/concepts/complexidade-acidental]] — vazamento de informação é uma forma estrutural (não do domínio) de complexidade acidental.
- [[wiki/concepts/arquitetura-de-software]] — decisão de onde uma informação deveria "morar" é, em essência, uma decisão de arquitetura.

## Key Sources

- [[wiki/sources/filosofia-do-design-de-software-livro-completo]] — Cap. 5, exemplos de servidor HTTP (leitura+parsing, parâmetros, defaults em respostas)
