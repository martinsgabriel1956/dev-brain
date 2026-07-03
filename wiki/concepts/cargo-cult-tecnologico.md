---
type: concept
title: "Cargo Cult Tecnológico"
aliases: ["copiar stack de big tech", "solução Netflix Google Facebook sem contexto", "cargo cult de arquitetura"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 2
tags: [arquitetura, tomada-de-decisao, carreira, escala, contexto]
skill: tech-mentor-leadership
status: draft
---

# Cargo Cult Tecnológico

Adotar uma solução técnica (Kubernetes, microsserviços, squads do Spotify, linguagem X) só porque uma empresa grande (Netflix, Google, Facebook, Nubank) a usa publicamente em palestra ou artigo — sem verificar se o próprio contexto (escala, número de usuários, número de desenvolvedores, maturidade do produto) justifica a mesma escolha.

## O argumento central

Quando um engenheiro de uma empresa com 100 milhões de assinantes explica como resolveu um problema *para aquela escala*, ele está dizendo: "essa solução tem grandes chances de funcionar **se você também tiver aquela escala**". A decisão errada não é a palestra existir — é decidir copiar a solução para um projeto com dois desenvolvedores e zero clientes.

> "Não se compare com eles hoje, se compare com eles no dia um deles, e no seu dia um você vai fazer merda, assuma isso de uma vez." — Fábio Akita

Netflix (fundada em 1997), Google (1998) e Facebook (2004) hoje rodam pouquíssimo código do "dia um" delas. Comparar seu dia um com a versão madura e escalada dessas empresas — em vez de com o dia um delas — é a distorção que sustenta o cargo cult.

## Analogia

Assistir a uma palestra de um ciclista profissional sobre a bicicleta de 8 mil dólares que ele usa não transforma quem ainda está com rodinha em recordista — a bicicleta não é o gargalo.

## O que fazer em vez disso

- No dia um de um produto, a única preocupação relevante é o *fit* com o próprio produto e sobreviver até o dia dois — não a escolha de infraestrutura de quem já sobrevive há décadas em escala massiva.
- Pesquisar, prototipar e testar hipóteses para o **seu** contexto, em vez de assumir que "se funcionou lá, funciona aqui".
- Reconhecer que não existe erro em usar Kubernetes, React, Go ou os squads do Spotify — o erro está no processo de decisão que ignora contexto, não na tecnologia em si.

## Relação com [[wiki/concepts/decisao-terceirizada]]

É a versão técnica do mesmo hábito: terceirizar a decisão de arquitetura para "o que a empresa X faz" em vez de fazer a análise de contexto própria.

## A Variante por Vaidade

[[wiki/sources/3-dicas-colocar-conhecimento-em-pratica]] descreve uma variante do mesmo padrão que não vem de copiar big tech, mas de vaidade tecnológica pessoal: querer trocar uma linguagem ou stack de produção só porque se aprendeu um recurso novo e achou legal ("quero trocar Java por Clojure porque estudei closures"), ou adotar mensageria/eventos assíncronos sem necessidade real, só para "ser o primeiro" a usar. O mecanismo é o mesmo do cargo cult — decisão técnica desconectada do contexto e do valor real — mas a motivação aqui é vaidade individual, não autoridade percebida de uma empresa grande. Ver [[wiki/concepts/granularidade-de-mudanca]] para o critério de "valor real" que deveria filtrar qualquer mudança, pequena ou grande.

## Ver também

- [[wiki/concepts/decisao-terceirizada]] — o hábito geral de decisão por procuração
- [[wiki/concepts/antifragilidade]] — apostar com risco calibrado ao próprio contexto, não ao da empresa copiada
- [[wiki/concepts/ciclo-de-mercado-tech]] — por que a tecnologia "quente" muda por década e não é garantia de acerto
- [[wiki/concepts/granularidade-de-mudanca]] — a exigência de "valor real" por trás de qualquer mudança técnica, evitando tanto cargo cult quanto vaidade

## Key Sources

- [[wiki/sources/pare-de-terceirizar-suas-decisoes]]
- [[wiki/sources/3-dicas-colocar-conhecimento-em-pratica]] — a variante por vaidade tecnológica pessoal, não por autoridade de big tech
