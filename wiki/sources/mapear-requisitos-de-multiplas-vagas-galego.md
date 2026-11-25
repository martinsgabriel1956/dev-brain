---
type: source
title: "Mapear requisitos de múltiplas vagas (módulo Mapeando Vagas)"
aliases: ["mapear requisitos de múltiplas vagas", "planilha de requisitos de vagas", "template Notion de requisitos"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mapear-requisitos-de-multiplas-vagas-galego.md
source_url: ""
author: "Augusto Galego (inferido: pasta 'galego' da transcrição, módulo Mapeando Vagas do curso de carreira dele; o nome não é dito)"
date_published: ""
date_ingested: 2026-11-25
source_count: 0
tags: [carreira, busca-de-vagas, curriculo, plano-de-estudo, fintech, portfolio, kafka, java, aws]
skill: tech-mentor-leadership
status: draft
---

# Mapear requisitos de múltiplas vagas

## TL;DR

Aula curta (~7:35) do módulo Mapeando Vagas de [[wiki/entities/augusto-galego]] (autoria inferida), a lição de [[wiki/concepts/mapeamento-de-requisitos-de-vagas]] prometida em [[wiki/sources/introducao-mapeando-vagas]]. Em vez de perguntar "o que devo aprender?", ele propõe o caminho inverso: abrir as vagas das empresas onde se quer entrar e **contar** o que elas pedem numa tabela (template no Notion, mas "no papel" também serve). Cada linha é uma tecnologia ou técnica, com **categoria**, **prioridade**, **contagem** de vagas que pediram, **sua proficiência** e **notas**. A demo passa por três vagas de banco/fintech: [[wiki/entities/nubank]] ([[wiki/entities/clojure]], Java, [[wiki/concepts/kafka]], [[wiki/entities/aws]], Dynamo Database, [[wiki/entities/prometheus]], [[wiki/concepts/kubernetes]]), Brex (full stack puxado para React, descartada por pouco overlap) e [[wiki/entities/itau]] (Java, AWS, [[wiki/entities/terraform]], [[wiki/entities/spring-boot]], Kafka, observabilidade, Dynamo Database). Com 10 a 15 vagas do mesmo perfil, a contagem ("8 pedem Java, 6 AWS, 4 Kafka") diz o que pôr em evidência no currículo, o que estudar e qual projeto fazer, ou que tecnologia levar para a empresa atual para ter experiência "validada".

## Key Claims

| Claim | Evidência (no vídeo) | Confiança |
|---|---|---|
| "O que aprender para entrar nas empresas" é o caminho inverso; comece pelos requisitos das vagas-alvo | Opinião do autor, motivada pelas perguntas que recebe | Alta como método: é a mesma lógica de [[wiki/concepts/cacar-a-empresa-nao-a-vaga]] |
| Ler 10 vagas de cabeça confunde; contar em números deixa a análise objetiva | Raciocínio ("é muita informação") | Alta para o argumento; a contagem mede frequência, não peso de cada requisito |
| A tabela tem: item, categoria, prioridade (alta/média/baixa), contagem, proficiência e notas | Demo no template do Notion | Alta (é o que a demo mostra) |
| A prioridade depende do papel: numa vaga de dev, Kubernetes é "legal saber", AWS "sempre precisa", Java "com certeza absoluta" | Julgamento do autor sobre a vaga do Nubank | Média: opinião, sem critério explícito |
| A nota registra o plano ou o nível exigido ("fiz projeto pessoal X com Java", "preciso fazer Y com Clojure", "necessário entender, mas não dominar 100%") | Exemplos inventados na demo ("não são meus dados reais") | Alta como uso da coluna |
| Agile não vale estudo ("ninguém vai implementar Agile da maneira correta"); entra como Soft Skills | Opinião do autor | Baixa: hipérbole |
| Vagas com pouco overlap (Brex full stack focado em front-end) atrapalham a amostra | Demo: troca de vaga para não "ficar adicionando mais e mais requerimentos" | Média: reduz ruído, mas também enviesa a amostra para o que você já conhece |
| A amostra deve ser de 10 a 15 vagas de empresas de tamanho, nível e perfil parecidos (ex.: só fintech) | Recomendação do autor; ele diz ter viés pró-fintech | Média: tamanho de amostra sem justificativa |
| O mapa não ajuda na candidatura em si; ajuda a decidir o que destacar no currículo, o que estudar e que projeto fazer | Afirmação explícita | Alta |
| Se a stack dominante não aparece no currículo, faça um projeto com ela ou leve-a para a empresa atual (se for a ferramenta certa para o problema) | Exemplo hipotético com Kafka | Média: conselho prático; a ressalva "se for a ferramenta adequada" é dele |

## Entidades

[[wiki/entities/augusto-galego]], [[wiki/entities/nubank]], [[wiki/entities/itau]], [[wiki/entities/clojure]], [[wiki/entities/aws]], [[wiki/entities/prometheus]], [[wiki/entities/terraform]], [[wiki/entities/spring-boot]]. Brex e Notion são citados, sem página própria.

## Conceitos

[[wiki/concepts/mapeamento-de-requisitos-de-vagas]], [[wiki/concepts/cacar-a-empresa-nao-a-vaga]], [[wiki/concepts/otimizacao-ats-curriculo]], [[wiki/concepts/curriculo-vs-portfolio]], [[wiki/concepts/demonstrar-experiencia-na-primeira-vaga]], [[wiki/concepts/acompanhamento-de-candidaturas]], [[wiki/concepts/kafka]], [[wiki/concepts/dynamodb]], [[wiki/concepts/kubernetes]].

## Open Questions

- **"Dynamo Database" no Nubank.** O autor lê "Dynamo Database" na vaga do Nubank e soma com a do Itaú. O banco transacional conhecido do Nubank é o [[wiki/concepts/datomic]] ([[wiki/sources/nubank-clojure-datomic-event-sourcing]]); a vaga pode citar DynamoDB de fato, ou pode ser Datomic lido como Dynamo. Não dá para conferir sem a vaga.
- **"Finable".** Item da vaga do Nubank que o autor diz não conhecer; a legenda não permite identificar. Ficou literal.
- **Pesos.** A contagem trata "8 de 10 pedem Java" igual seja requisito obrigatório ou "bônus" (como o Kotlin da Brex). A aula não separa obrigatório de desejável.
- **Viés de amostra.** Descartar vagas de pouco overlap faz o mapa confirmar a stack que você já mira. Para quem quer mudar de área, isso esconde exatamente as lacunas.
- **Viés comercial:** aula de um curso pago do autor.

## Raw Quotes

- "eu acho que esse é o caminho inverso, certo?"
- "A gente só quer contar o número de vezes que a gente viu em diferentes empresas tais coisas sendo pedidas"
- "isso aqui não vai te ajudar na aplicação, isso aqui vai te ajudar a identificar o que é importante pras empresas"
