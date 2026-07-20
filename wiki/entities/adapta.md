---
type: entity
title: "Adapta"
aliases: ["Adapta.org", "Adapta ONE", "Adapta ONE Pro"]
date_created: 2026-07-19
date_updated: 2026-07-19
source_count: 1
tags: [ia, agregador-de-modelos, produto, brasil, produtividade]
skill: tech-mentor-ai
status: draft
---

# Adapta

Plataforma brasileira de IA (`adapta.org`) que agrega múltiplos modelos de linguagem de terceiros (GPT, Claude, Gemini, DeepSeek e outros — mais de 15 segundo a documentação pública) em uma única interface de chat, com [[wiki/concepts/skills-agente|skills]] configuráveis para dar contexto pessoal/de projeto ao modelo, e um recurso de [[wiki/concepts/roteamento-automatico-de-modelo|roteamento automático de modelo]] chamado "ONE".

**[external]** Confirmado via `adapta.org` e `docs.adapta.org`: a Adapta se descreve como o maior ecossistema de IA generativa do Brasil, oferece cursos e newsletter além da ferramenta, e tem apps nativos nas lojas Android/iOS. Não foi feita verificação independente de métricas de uso, satisfação ou das alegações de qualidade de resposta — as fontes primárias disponíveis (site e documentação do próprio produto) são material do fabricante, não avaliação de terceiros.

## Modelo ONE

Tecnologia própria descrita como "maestro" que escolhe automaticamente, para cada prompt, qual modelo do ecossistema deve respondê-lo (GPT, Claude, Gemini etc.), eliminando a necessidade de o usuário decidir manualmente qual IA usar para cada tarefa. Ver [[wiki/concepts/roteamento-automatico-de-modelo]] para o padrão técnico geral e o grau de confiança sobre esse mecanismo específico.

## Modelo ONE Pro

**[external]** Segundo a documentação do produto, evolução voltada a tarefas que exigem raciocínio mais profundo: em vez de rotear para um único modelo, alterna entre modelos de raciocínio (citado: DeepSeek Reasoner) e passa o mesmo prompt por múltiplos modelos para compor uma resposta mais completa, com busca web nativa, interpretação de arquivo (Vision) e contexto pessoal de biblioteca. Na fonte que introduziu a Adapta nesta wiki, esse comportamento é descrito de forma consistente com a documentação: "passa o prompt por três IAs diferentes" para reduzir lacunas e alucinações — claim de marketing do fabricante, não verificado de forma independente.

## Skills como contexto pessoal

Na fonte, skills da Adapta são usadas para dois fins: (1) dar à IA contexto de rotina persistente (tipo de trabalho, horário de CLT, hábito de criar conteúdo) para gerar planejamentos mais calibrados sem repetir esse contexto a cada prompt; (2) configurar um "assistente de rotina" personalizado com forma de pensar e prioridades do usuário, usado para apoiar decisões de carreira. Ver [[wiki/concepts/skills-agente]] para o padrão geral de skills como harness, do qual esse é um uso de produto (não de codificação).

## Garantia comercial

A fonte cita garantia de reembolso de 30 dias como parte da oferta comercial — não verificado além da menção na fonte (a página comercial do produto não foi consultada para confirmar termos exatos).

## Ver também

- [[wiki/concepts/roteamento-automatico-de-modelo]]
- [[wiki/concepts/skills-agente]]

## Key Sources

- [[wiki/sources/sistema-produtividade-ia-adapta]]
