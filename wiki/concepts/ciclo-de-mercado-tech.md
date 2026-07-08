---
type: concept
title: "Ciclo de Mercado Tech"
aliases: ["ciclo de abundância e depressão", "lei da oferta e procura em tech", "ciclo de contratação tech"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 3
tags: [carreira, mercado-de-trabalho, oferta-e-procura, ciclo-economico]
skill: tech-mentor-leadership
status: draft
---

## Definição

O mercado de trabalho em programação segue a lei de oferta e procura em ciclos alternados de **abundância** (alta demanda, contratação fácil, salários subindo) e **depressão** (demanda cai, oferta de profissionais supera vagas, seletividade aumenta). Nenhum ciclo de abundância dura para sempre.

## O Mecanismo

Quando a demanda por desenvolvedores excede a oferta, o mercado fica "aquecido": empresas contratam com critérios mais frouxos, salários sobem, e cursos rápidos (semanas a poucos meses) parecem suficientes para conseguir emprego. Esse próprio aquecimento, porém, atrai um volume enorme de gente nova para a profissão via cursos de formação rápida — o que aumenta a oferta de profissionais mais rápido do que a demanda cresce, empurrando o mercado de volta para um ciclo de depressão.

## Exemplo Histórico — Ondas de Tecnologia

[[wiki/entities/fabio-akita]] ilustra o ciclo com a evolução das linguagens mais demandadas por década:

| Época | Linguagens/tecnologias mais quentes |
|---|---|
| Anos 90 | Visual Basic, Delphi, Java |
| Virada do século | PHP, ASP, Flash |
| ~10 anos depois | Objective-C, Ruby, JavaScript |
| 2020s | Python, Go, Rust (segundo o autor) |

Quem ficou preso à ferramenta de uma onda perdeu, sequencialmente, as ondas seguintes: a primeira onda da web, a onda das redes sociais, a onda mobile, a onda dos e-commerces. Ver [[apego-a-ferramentas]] para o mecanismo psicológico por trás disso.

[[wiki/entities/lucas-badico]] reforça a onda 2020s do Go com um contra-exemplo de "onda que não emplacou": Ruby on Rails teve forte influência histórica no ecossistema mas nunca gerou volume relevante de vagas no Brasil além de algumas consultorias — ao contrário do Go, hoje consolidado em Mercado Livre, Mercado Pago e Stone. A diferença, segundo o autor, é que Go foi desenhado como linguagem *cloud native* (ver [[wiki/concepts/go-fundamentos]]), o que amplia sua adoção além de qualquer moda passageira.

## O que Não Muda entre Ciclos

O autor argumenta que tentar prever qual será a próxima linguagem/framework "quente" é perda de tempo — o que não perde valor entre ciclos é [[raciocinio-matematico-aplicado|raciocínio fundamental]] (matemática, lógica, capacidade de aprender rápido), porque essas habilidades transferem entre qualquer ferramenta específica.

## Implicação Prática

Em ciclo de depressão, a prioridade das empresas deixa de ser "produzir funcionalidade nova rápido" e passa a ser **otimizar e extrair mais valor do que já existe** — o que favorece quem sabe raciocinar sobre trade-offs, não só seguir padrões prontos. Mercados em depressão filtram naturalmente quem tem [[fundacao-tecnica|fundação técnica]] real de quem só teve sorte de entrar durante a abundância.

## Cada onda como curva de adoção

Cada onda de tecnologia listada acima é, individualmente, uma [[wiki/concepts/curva-de-adocao-tecnologica|curva de adoção em S]]: começa devagar, cresce exponencialmente, desacelera. O próprio autor descreve ter apostado cedo em Ruby on Rails (2005), na fase inicial daquela curva — ilustrando a estratégia de [[wiki/concepts/antifragilidade|apostar em várias tecnologias ao longo de ~10 anos]] em vez de tentar prever com certeza qual onda vai vencer.

## Conexões

- [[apego-a-ferramentas]] — por que ficar preso a uma ferramenta específica amplia o dano de cada virada de ciclo
- [[raciocinio-matematico-aplicado]] — a habilidade que não perde valor entre ciclos
- [[fundacao-tecnica]] — o que sobrevive quando o mercado esfria e filtra profissionais
- [[autodidata]] — quem aprendeu a aprender sozinho consegue "nadar" tanto em ciclos de abundância quanto de depressão
- [[wiki/concepts/curva-de-adocao-tecnologica]] — o padrão em S por trás de cada onda individual
- [[wiki/concepts/antifragilidade]] — a estratégia de aposta que lida com a incerteza sobre qual onda vai vencer

## Key Sources

- [[wiki/sources/akita-oferta-procura-matematica-carreira]]
- [[wiki/sources/golang-mercado-trabalho-frontend-para-backend]]
- [[wiki/sources/pare-de-terceirizar-suas-decisoes]]
