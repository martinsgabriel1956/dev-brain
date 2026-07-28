---
type: concept
title: "Checklist do Primeiro Dia de um Projeto Novo"
aliases: ["primeiro dia de projeto", "setup inicial de codebase", "day one checklist", "deploy desde o dia um"]
date_created: 2026-07-07
date_updated: 2026-07-28
source_count: 2
tags: [projetos, deploy, mvp, ci-cd, boas-praticas, setup]
skill: tech-mentor-leadership
status: stable
---

# Checklist do Primeiro Dia de um Projeto Novo

Ordem tática para as primeiras horas de uma codebase nova, **antes de existir qualquer funcionalidade real**. A ideia central: tudo que vai doer em produção mais tarde (deploy quebrado, migrations manuais, ausência de testes, falta de contexto para IA) deve ser resolvido no dia 1, quando o custo de errar ainda é baixíssimo — o projeto ainda não faz nada.

## As Seis Etapas

1. **[[wiki/concepts/escolha-de-stack]]** — baseada no objetivo (aprender vs. monetizar) e na natureza do projeto
2. **Documentar a estrutura inicial** num `.md`, pensando no [[wiki/concepts/mvp]], antes de escrever a primeira linha de código de fato
3. **Deploy do boilerplate/Hello World imediatamente**, com CD automático a cada merge para `main`
4. **[[wiki/concepts/orm]] mínima + migrations automáticas**, com o banco de dev já existindo e o deploy já triggando migrations desde o primeiro commit
5. **Testes (unitário + e2e) na pipeline de CI**, bloqueando merge antes mesmo de haver funcionalidade
6. **Documentação dupla**: README (para humanos) + `AGENTS.md` (para a IA) — ver [[wiki/concepts/rules-agente]]

## Por Que Fazer Isso Antes de Codar Qualquer Feature

É comum construir algo que só roda localmente — sem Docker, sem infraestrutura real — e descobrir na hora do primeiro deploy que nada funciona no provedor de cloud escolhido. Se o deploy é o primeiro passo, cada problema de ambiente é resolvido isoladamente e cedo, em vez de se acumular e aparecer todo de uma vez quando a pressão de lançar já é alta.

O mesmo raciocínio vale para migrations e testes: um projeto "vazio" já em produção, com banco de dev, pipeline de CD e testes rodando, é uma base muito mais barata de evoluir do que descobrir que o setup de infraestrutura não funciona só quando já existem semanas de código em cima dele.

## Relação com Documentação para IA

A etapa de documentação (passo 6) não é cerimonial — é o que torna produtivo codar com IA depois. Um `AGENTS.md` com arquitetura, convenções e comandos do projeto reduz alucinação e retrabalho do agente, no mesmo espírito do que [[wiki/sources/agents-md-vale-a-pena-paper-zurique]] documenta empiricamente.

## Ver Também

- [[wiki/concepts/escolha-de-stack]] — primeira decisão do checklist
- [[wiki/concepts/mvp]] — escopo que a estrutura inicial deve servir
- [[wiki/concepts/ci-cd]] — mecanismo do deploy automático desde o dia 1
- [[wiki/concepts/orm]] — camada de dados mínima com migrations automáticas
- [[wiki/concepts/piramide-de-testes]] — o que testar na pipeline antes de ter features
- [[wiki/concepts/rules-agente]] — `AGENTS.md` como parte da documentação de setup
- [[wiki/concepts/living-documentation]] — contraste: README manual é aceitável neste contexto de MVP/solo dev

## Key Sources

- [[wiki/sources/5-ou-6-dicas-para-projetos-novos]]
- [[wiki/sources/database-migrations-sql-cru-vs-orm-drizzle]] — detalha o mecanismo da etapa 4: [[wiki/concepts/database-migration|migrations]] versionadas e reproduzíveis, com ou sem ORM
