---
type: concept
title: "Cargo Cult Tecnológico"
aliases: ["copiar stack de big tech", "solução Netflix Google Facebook sem contexto", "cargo cult de arquitetura"]
date_created: 2026-07-03
date_updated: 2026-08-04
source_count: 4
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

## A Variante por Consenso de Mercado ("React é a Forma Certa")

[[wiki/sources/a-insanidade-de-ser-um-programador-hoje]] descreve uma terceira variante, distinta tanto da autoridade de big tech quanto da vaidade pessoal: adoção por **consenso coletivo do mercado**, sem gatilho identificável de uma empresa específica. A fonte descreve React (e, por extensão, TypeScript/Redux/Webpack em volta dele) como algo que "a mente coletiva de programação decidiu" ser "a maneira certa" de desenvolver — convenção que vira padrão de contratação e de vaga sem que cada empresa individualmente tenha avaliado se o próprio contexto (tamanho de time, complexidade real de UI) justifica essa pilha específica. O mecanismo de fundo é o mesmo (decisão técnica desconectada de contexto), mas a fonte da autoridade percebida aqui não é "porque a Netflix faz assim", é "porque é isso que todo mundo espera que se saiba".

## A Variante por Ansiedade de Ficar Para Trás ("FOMO de Framework")

[[wiki/sources/tecnologias-hype-passado-soap-xml-esb-jquery-cobol]] descreve o mecanismo inverso ao cargo cult clássico: não é copiar o que a big tech faz, é a ansiedade de que **não** acompanhar toda nova tecnologia é ficar irrelevante — "vontade de jogar todo o conhecimento fora para aprender o framework da moda". A fonte argumenta que essa ansiedade ignora um dado empírico simples: [[wiki/concepts/soap]], [[wiki/concepts/xml-extensible-markup-language|XML]], [[wiki/concepts/esb-enterprise-service-bus|ESB]], [[wiki/concepts/jquery]] e [[wiki/concepts/cobol]] saíram do mainstream de conferências e redes sociais há anos, mas continuam sustentando sistemas críticos — o ciclo de hype da comunidade não é o mesmo ritmo em que uma tecnologia deixa de ser útil em produção. É o cargo cult visto pelo avesso: em vez de "copiar porque todo mundo grande usa", é "abandonar porque ninguém mais fala disso" — mesmo mecanismo de decisão desconectada de contexto real, motivação inversa.

## Ver também

- [[wiki/concepts/decisao-terceirizada]] — o hábito geral de decisão por procuração
- [[wiki/concepts/antifragilidade]] — apostar com risco calibrado ao próprio contexto, não ao da empresa copiada
- [[wiki/concepts/ciclo-de-mercado-tech]] — por que a tecnologia "quente" muda por década e não é garantia de acerto
- [[wiki/concepts/granularidade-de-mudanca]] — a exigência de "valor real" por trás de qualquer mudança técnica, evitando tanto cargo cult quanto vaidade

## Key Sources

- [[wiki/sources/pare-de-terceirizar-suas-decisoes]]
- [[wiki/sources/3-dicas-colocar-conhecimento-em-pratica]] — a variante por vaidade tecnológica pessoal, não por autoridade de big tech
- [[wiki/sources/a-insanidade-de-ser-um-programador-hoje]] — a variante por consenso coletivo de mercado ("React é a forma certa"), sem autoridade de empresa específica
- [[wiki/sources/tecnologias-hype-passado-soap-xml-esb-jquery-cobol]] — a variante por ansiedade de ficar para trás (FOMO de framework), mecanismo invertido do cargo cult clássico
