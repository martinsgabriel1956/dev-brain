---
type: concept
title: "Agente de PRD"
aliases: ["agente prd", "prd agent", "gerador de prd", "agente de requisitos"]
date_created: 2026-06-02
date_updated: 2026-08-18
source_count: 2
tags: [agente, prd, spec-driven, planejamento, human-in-the-loop]
skill: tech-mentor-ai
status: stub
---

# Agente de PRD

## TL;DR

Agente especializado na primeira etapa do [[wiki/concepts/spec-driven-development|Spec Driven Development]]: converte uma ideia ou problema descrito em linguagem natural em um [[wiki/concepts/prd-product-requirements-document|PRD]] estruturado, por meio de perguntas iterativas ao usuário.

## Funcionamento

O agente de PRD não gera o documento de uma vez. Ele conduz uma sessão interativa:

1. Recebe a descrição inicial do problema/feature
2. Faz perguntas para esclarecer requisitos ambíguos
3. Propõe estrutura do PRD para validação
4. Itera até o usuário aprovar
5. Persiste o PRD em arquivo para uso nas etapas seguintes

## O PRD Resultante

O PRD gerado é um documento **para a IA**, não para a empresa. Seu propósito é:
- Fornecer contexto suficiente para o agente de Tech Spec gerar as decisões corretas
- Eliminar ambiguidade antes da fase técnica
- Servir como referência durante a execução das tarefas

> "PRD não é um documento feito para a empresa, é um documento feito para a IA." — [[wiki/entities/pedro-nauke]]

## Conteúdo Típico do PRD

- Problema a resolver e usuários afetados
- Funcionalidades esperadas (lista não técnica)
- Comportamentos explícitos ("faça / nunca faça")
- Critérios de aceite funcionais
- Restrições de negócio (prazo, escopo, integrações)

## Relação com HITL

O [[wiki/concepts/human-in-the-loop|human-in-the-loop]] é obrigatório ao final da geração do PRD. A aprovação humana garante que o contexto capturado está correto antes de investir tempo na Tech Spec.

## Skill Análoga um Nível Abaixo: Geração de Spec por Feature

[[wiki/sources/spec-writer-skill-criterios-de-boa-spec]] descreve uma skill do mesmo formato interativo aplicada uma etapa depois: em vez de gerar o PRD, a skill "Spec Writer" pega uma feature *já definida* no PRD e conduz uma entrevista para gerar a tech spec dessa feature especificamente — mesmo padrão de "validar inputs → entrevistar → sumarizar → gerar documento" do agente de PRD, mas aplicado à granularidade de spec, com uma etapa extra de validação contra os [[wiki/concepts/criterios-de-uma-boa-spec|7 critérios de qualidade de spec]] antes do output.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-04-agentes-planejamento]]
- [[wiki/sources/spec-writer-skill-criterios-de-boa-spec]] — skill análoga um nível abaixo (spec por feature, não PRD), mesmo padrão de entrevista iterativa
