---
type: source
title: "O Que Estudar — Guia para Iniciantes (André Casciotti)"
aliases: ["guia de estudos para iniciante dev", "o que estudar programação", "próximo nível guia iniciante"]
date_created: 2026-09-28
date_updated: 2026-09-28
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/o-que-estudar-guia-para-iniciantes-andre-casciotti.md
source_url: ""
author: "André Casciotti (canal Próximo Nível / Dev que Resolve)"
date_published: ""
date_ingested: 2026-09-28
source_count: 0
tags: [carreira, iniciante, aprendizado, csharp, backend, fundamentos, sql, git, infraestrutura, mentalidade-de-crescimento]
skill: tech-mentor-leadership
status: draft
---

# O Que Estudar — Guia para Iniciantes (André Casciotti)

## TL;DR

Quinta fonte de [[wiki/entities/andre-casciotti]]: um guia do que ele estudaria se estivesse começando hoje. Dois pontos conceituais vêm antes da lista técnica — **aprender com foco no problema, não no "como fazer"** ([[wiki/concepts/aprender-com-foco-no-problema]]), exercitado criando um sistema do zero a partir de um **modelo real existente** e "caçando problemas" para implementar (autenticação real, filtro+índice, permissões via JWT, SLA de resposta); e **escolher rápido um caminho de carreira** ([[wiki/concepts/escolha-rapida-de-caminho-de-carreira]]) em vez de tentar abraçar todas as tecnologias — reforçado por [[wiki/concepts/mentalidade-de-crescimento]] (nada é definitivo; trocar de stack/paradigma é mais fácil sendo experiente). Depois, uma lista técnica concreta com viés pessoal: C# + ASP.NET MVC focado em backend, [[wiki/concepts/testes-como-aprendizado|teste unitário]] desde o início, básico de front-end, [[wiki/concepts/requisitos-funcionais-e-nao-funcionais|SQL ANSI/DML]], [[wiki/concepts/git]] e GitHub, fundamentos de linguagem/compilador/[[wiki/concepts/clr-e-garbage-collector|CLR/GC]], [[wiki/concepts/arquitetura-cliente-servidor|arquitetura cliente-servidor]]/HTTP, básico de redes e infraestrutura superficial. Fecha com [[wiki/concepts/ia-como-amplificador]] (IA acelera o que você já sabe fazer) e as quatro habilidades centrais do canal: requisitos, arquitetura, testes, refatoração ([[wiki/concepts/resolver-problemas-como-habilidade-central]]).

## Key Claims

- **Aprender focado no "como fazer" atrapalha o raciocínio**; todo trabalho de dev nasce de um problema (às vezes ainda não digitalizado), nunca de uma instrução do tipo "conecta no banco". Evidência: experiência do autor e observação de que iniciantes "sabem como fazer" mas não sabem "por onde começar". → [[wiki/concepts/aprender-com-foco-no-problema]]
- **Exercício recomendado**: construir um sistema do zero usando um modelo já existente (SaaS, marketplace) em vez de tentar tirar tudo da própria cabeça, e depois "caçar problemas" reais para implementar — autenticação real (não senha em texto puro), filtro que força aprender índice de banco, menu por permissão (JWT vs. sessão), SLA de resposta (cache, N+1). → [[wiki/concepts/aprender-com-foco-no-problema]], [[wiki/concepts/repertorio]], [[wiki/concepts/requisitos-funcionais-e-nao-funcionais]]
- **Melhoria contínua**: implementar "meia boca" primeiro e melhorar depois, uma coisa de cada vez — mesmo padrão de [[wiki/concepts/refatoracao]] aplicado ao aprendizado, não só ao código em produção.
- **Escolher caminho de carreira rápido** (linguagem, depois stack) evita ficar "moscando" e virando um "mais ou menos" que não domina nada; conseguir emprego rápido acelera o desenvolvimento de carreira mais do que dominar teoricamente uma tecnologia nunca usada no trabalho. Recomendação pessoal: C#, Java ou JavaScript, por terem mais mercado (contesta a percepção de que Python "pega mais"). → [[wiki/concepts/escolha-rapida-de-caminho-de-carreira]], [[wiki/concepts/escolha-de-stack]]
- **Trocar de escolha não é falha**: se não der certo ou não houver vaga, trocar rápido é melhor do que ficar decidindo indefinidamente. → [[wiki/concepts/escolha-rapida-de-caminho-de-carreira]]
- **Mentalidade de crescimento**: nada é definitivo; a barreira para aprender uma nova linguagem cai muito depois da primeira; recomenda a devs plenos/sêniors experimentar outro paradigma (Java→Clojure, C#→F#) mesmo sem intenção de trocar de carreira. → [[wiki/concepts/mentalidade-de-crescimento]]
- **Curadoria de informação vale cada vez mais** num cenário de excesso de estímulo/opinião; é um processo pessoal e iterativo (aumentar e diminuir a lista de fontes seguidas com o tempo), não uma escolha única. → [[wiki/concepts/curadoria-de-informacao]]
- **Recomendação técnica de stack**: C# + ASP.NET MVC (cobre API e view no mesmo framework, útil porque times pequenos/médios raramente deixam alguém mexer só numa ponta); mercado corporativo grande prefere C#/Java por confiabilidade de suporte e contratos com vendors (SQL Server, Oracle), enquanto startups tendem a open source por restrição de orçamento. → [[wiki/concepts/escolha-de-stack]]
- **Teste unitário desde o início da carreira é diferencial** porque a barreira mental é menor para quem nunca lidou com métodos gigantes (ao contrário do sênior, que resiste a testar código legado complexo). → [[wiki/concepts/testes-como-aprendizado]]
- **Git ≠ GitHub**: Git é o versionamento (funciona só localmente); GitHub é o repositório descentralizado — mas o mecanismo por trás pode ser GitLab, Bitbucket, GitHub Enterprise on-premises etc. → [[wiki/concepts/git]]
- **SQL é teoria de conjuntos aplicada**: o join do select é a mesma lógica de interseção de conjuntos da escola; para iniciante, o essencial é o DML (select/insert/update/delete), não DDL. → [[wiki/concepts/requisitos-funcionais-e-nao-funcionais]]
- **Fundamentos de runtime importam mesmo sem aprofundar**: entender CLR/CTS/Garbage Collector explica boa parte dos problemas de performance em produção que, sem esse conhecimento, parecem inexplicáveis. → [[wiki/concepts/clr-e-garbage-collector]]
- **Arquitetura cliente-servidor/HTTP e infraestrutura básica (SO, VM, container, cloud, DNS, load balancer)** devem ser estudadas superficialmente e em paralelo — muito dev experiente nunca aprendeu isso por só "entregar código" sem entender onde ele roda. → [[wiki/concepts/arquitetura-cliente-servidor]]
- **IA acelera o que você já faz, não substitui saber resolver problemas**: quem programa bem entrega mais rápido com IA; quem só faz "código porcaria" põe bug em produção mais rápido. → [[wiki/concepts/ia-como-amplificador]]
- **Quatro habilidades centrais do canal**: análise de requisitos, arquitetura, teste unitário, melhoria contínua/refatoração — mesma tese de [[wiki/sources/como-ser-dev-essencial-e-ganhar-mais-andre-casciotti]]. → [[wiki/concepts/resolver-problemas-como-habilidade-central]]

## Entities

[[wiki/entities/andre-casciotti]]

## Concepts

Novos: [[wiki/concepts/aprender-com-foco-no-problema]] · [[wiki/concepts/escolha-rapida-de-caminho-de-carreira]] · [[wiki/concepts/mentalidade-de-crescimento]] · [[wiki/concepts/curadoria-de-informacao]] · [[wiki/concepts/arquitetura-cliente-servidor]] · [[wiki/concepts/clr-e-garbage-collector]]

Existentes: [[wiki/concepts/repertorio]] · [[wiki/concepts/escolha-de-stack]] · [[wiki/concepts/resolver-problemas-como-habilidade-central]] · [[wiki/concepts/requisitos-funcionais-e-nao-funcionais]] · [[wiki/concepts/testes-como-aprendizado]] · [[wiki/concepts/refatoracao]] · [[wiki/concepts/git]] · [[wiki/concepts/compilador]] · [[wiki/concepts/ia-como-amplificador]] · [[wiki/concepts/sql-alem-do-basico]]

## Open Questions

- Todas as recomendações técnicas (C#/Java/JavaScript "têm mais mercado" que Python; SQL Server é mais comum em empresas C#) são experiência pessoal do autor, sem dado de mercado citado — tensão leve com a narrativa comum de que Python domina em vagas de dados/IA.
- O autor recomenda ASP.NET MVC especificamente por versatilidade (API + view), mas não discute a tendência do próprio ecossistema .NET de separar API (ASP.NET Core Web API) de frontend (SPA) — pode estar descrevendo um cenário de empresas com sistemas mais legados/monolíticos.
- "Recomendo C#, Java ou JavaScript" conflita em ênfase (não em conteúdo) com [[wiki/concepts/escolha-de-stack]], que trata a escolha de stack como função de objetivo (aprender vs. monetizar) e não de "qual tem mais mercado" — aqui o critério é quase puramente mercado de trabalho para quem ainda não tem repertório para decidir por objetivo.
- Título original, data de publicação e URL desconhecidos; vídeo transcrito por colagem do usuário, com vários termos técnicos corrompidos pela transcrição automática (listados no cabeçalho do raw) e corrigidos por contexto.

## Raw Quotes

> "Todo o trabalho do dev surge a partir de um problema. Nosso trabalho não surge a partir do como fazer as coisas."

> "A solução nasce do problema."

> "Se você ficar esperando para definir [seu caminho], você se perde."

> "Você não é do jeito que você é agora. Você está como você está agora — você pode ser diferente."

> "A IA acelera aquilo que você já faz. [...] Se você só sabe fazer código porcaria, a IA vai te ajudar a fazer isso mais rápido."
