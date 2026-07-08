---
type: source
title: "5 (ou 6) Dicas Para Projetos Novos"
aliases: ["dicas para começar projeto novo", "checklist primeiro dia de projeto", "setup inicial de codebase"]
date_created: 2026-07-07
date_updated: 2026-07-07
source_count: 0
tags: [projetos, stack, deploy, orm, migrations, testes, documentacao, ci-cd, mvp, carreira]
skill: tech-mentor-leadership
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/5-ou-6-dicas-para-projetos-novos.md
source_url: ""
author: "desconhecido (canal YouTube, patrocínio HostGator)"
date_published: "desconhecido"
date_ingested: 2026-07-07
---

# 5 (ou 6) Dicas Para Projetos Novos

## TL;DR

Checklist tático para o primeiro dia de uma codebase nova, antes de qualquer feature real existir: (1) escolher a stack com base no objetivo — aprender vs. monetizar —, preferindo frameworks "batteries included" para SaaS solo; (2) documentar a estrutura inicial rumo ao [[wiki/concepts/mvp]] antes de codar; (3) fazer deploy do boilerplate/Hello World imediatamente, com CD automático a cada merge; (4) usar uma [[wiki/concepts/orm]] mínima com migrations automáticas e já triggar essas migrations no deploy; (5) rodar testes (unitário + e2e) na pipeline antes mesmo de existir funcionalidade; (6) documentar tudo em README + `AGENTS.md` para consumo humano e de IA.

## Key Claims

| Claim | Evidência | Confiança |
|---|---|---|
| Escolha de stack se correlaciona com o objetivo do projeto: para aprender, escolhe-se tecnologia nova (Elixir, Go, Rust); para monetizar, escolhe-se o que já se domina (na prática, majoritariamente JavaScript) | Distinção explícita da fonte entre "projeto para aprender" e "projeto para ganhar dinheiro" | Alta |
| Frameworks "batteries included" (Django, Rails, Laravel) tiram um SaaS solo do zero mais rápido do que setups mais nus (Node + Express), que exigem agregar plugins manualmente | Comparação direta feita na fonte | Alta |
| A escolha de stack também deve considerar a natureza do projeto — SPA favorece Next.js; backend pesado computacionalmente pode não favorecer Python/JavaScript | Exemplos citados na fonte | Média (não aprofunda critério de "pesado computacionalmente") |
| Documentar a estrutura inicial do projeto num `.md` antes de codar evita "gambiarra macarrônica" difícil de evoluir, e ajuda a codar com IA dentro do escopo certo | Argumento central da fonte para o passo 2 | Alta |
| Fazer deploy do boilerplate (Hello World) imediatamente, antes de qualquer funcionalidade, expõe cedo problemas de ambiente/infra que só apareceriam depois, quando já são mais caros de debugar | Analogia da fonte: projetos que rodam só localmente, não dockerizados, falham no primeiro deploy horas a fio | Alta |
| Deploy contínuo (CD automático a cada merge para `main`) deve ser configurado desde o primeiro dia, não adicionado depois | Fluxo descrito: GitHub Actions apontando para VPS, deploy a cada merge | Alta |
| ORMs devem ser mínimas — o valor está em gerar migrations automáticas, schema explícito e type safety, mantendo a API o mais próxima possível de SQL puro | Preferência explícita da fonte por Drizzle no ecossistema JS | Média (comparação com Prisma/TypeORM não é feita na fonte) |
| O banco de dev e o gatilho de migrations automáticas no deploy devem existir desde o primeiro dia, mesmo com o projeto ainda vazio | Exemplo da fonte: primeira migração para armazenar usuários, sem nenhuma feature ainda | Alta |
| Testes (unitário com Vitest, e2e com Cypress) devem rodar na pipeline de CI antes mesmo de existir qualquer funcionalidade real | Afirmação direta da fonte sobre a ordem de setup | Alta |
| Documentação de setup deve existir em dois artefatos com públicos diferentes: README (humanos — instalação, comandos, decisões, convenções) e `AGENTS.md` (IA — como rodar testes, se seguir TDD, padrões de tipagem, arquitetura, objetivo do projeto) | Distinção explícita feita na fonte entre os dois arquivos | Alta |
| Recomendação comercial de HostGator (VPS a partir de ~R$21/mês, servidores em São Paulo) como provedor para o fluxo de deploy contínuo | Conteúdo patrocinado do vídeo | Baixa (é publicidade, não claim técnica independente) |

## Concepts & Entities Touched

[[wiki/concepts/checklist-primeiro-dia-projeto]] · [[wiki/concepts/escolha-de-stack]] · [[wiki/concepts/mvp]] · [[wiki/concepts/orm]] · [[wiki/concepts/ci-cd]] · [[wiki/concepts/piramide-de-testes]] · [[wiki/concepts/rules-agente]] · [[wiki/concepts/living-documentation]]

## Open Questions

- O nome do canal/autor não foi identificado na transcrição — não há URL de origem fornecida.
- O vídeo promete um projeto futuro (\"SaaS do zero\") mostrando esse passo a passo na prática — fora do escopo desta ingestão, mas candidato a fonte futura para acompanhar a mesma metodologia aplicada de fato.
- A fonte não compara Drizzle com alternativas mais completas (Prisma, TypeORM) além de citar preferência pessoal — vale checar `references/architecture-foundations.md` (tech-mentor-backend) se o tema for aprofundado depois.
- Complementa [[wiki/sources/por-que-devs-nao-terminam-projetos]]: aquela fonte identifica "ausência de estrutura" como uma das quatro causas de projetos inacabados; esta fonte propõe o antídoto tático direto (estrutura documentada + deploy dia 1) para esse ponto específico.
