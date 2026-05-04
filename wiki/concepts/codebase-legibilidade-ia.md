---
type: concept
title: "Codebase Legibilidade para IA"
aliases: ["codebase para ia", "código legível ia", "qualidade código ia"]
date_created: 2026-05-04
date_updated: 2026-05-04
source_count: 2
tags: [ia-engineering, codebase-quality, acoplamento, context-engineering, coding-agents]
skill: tech-mentor-backend
status: stable
---

# Codebase Legibilidade para IA

A qualidade do código que a IA vai interagir importa mais do que o prompt, o modelo ou a ferramenta utilizada. As mesmas técnicas que sempre tornaram código mais manutenível para humanos são as que tornam código mais legível para agentes.

> "Uma codebase boa legível para seres humanos também é uma codebase boa e legível para IAs."

## Por Que Isso Importa

Agentes de código trabalham com context window limitada. Cada arquivo aberto é tokens consumidos. Cada dependência escondida é uma chance de o agente perder contexto crítico.

Código fortemente acoplado numa god class de 20.000 linhas:
- Obriga o agente a manter muito mais contexto
- Torna impossível isolar a tarefa num módulo específico
- Aumenta a chance de o agente quebrar partes não relacionadas ao fazer uma mudança
- Dificulta o [[concepts/mental-alignment]] do dev sobre o que foi gerado

Ver [[concepts/navigation-paradox]] — agentes perdem ~25% dos arquivos críticos em arquiteturas com forte acoplamento via DI containers.

## O Que Torna Código Legível Para IA

| Característica | Bom para IA | Ruim para IA |
|---|---|---|
| Estrutura | Módulos com responsabilidade clara | God class que faz tudo |
| Acoplamento | Baixo — mudanças localizadas | Alto — mudança em A quebra B e C |
| Interfaces | Contratos explícitos (ports) | Dependências diretas e implícitas |
| Funções | Explícitas e nomeadas | Lógica inline repetida |
| Contexto por tarefa | 2–3 arquivos | 7–13 arquivos ou mais |

## Escala do Problema

Com 200 linhas, a IA entende qualquer estrutura. O problema começa quando:
- O projeto cresce para 10.000+ linhas
- Há múltiplos colaboradores (e agentes) fazendo PRs em paralelo
- Partes do sistema precisam ser substituídas
- O dev precisa voltar ao código dois meses depois

Para 200 linhas, uma god class é perfeitamente adequada. Para 20.000 linhas e quatro colaboradores, torna-se um problema real tanto para humanos quanto para modelos.

## Relação com Comprehension Debt

[[concepts/comprehension-debt]] é causado em parte por código de difícil leitura gerado por agentes. O ciclo:
1. Codebase ruim → agente gera código de baixa qualidade
2. Dev aprova sem entender completamente
3. Codebase piora
4. Próximo agente tem ainda mais dificuldade

Manter código legível quebra o ciclo na origem.

## Padrões que Ajudam

- [[concepts/hexagonal-architecture]] — ports e adapters localizam mudanças e reduzem contexto necessário por tarefa
- [[concepts/vertical-slice-architecture]] — feature-first em vez de camada-first reduz número de arquivos por feature
- [[concepts/single-responsibility-principle]] — uma razão para mudar = contexto mínimo para a IA

## Key Sources

- [[sources/ports-and-adapters-codebase-para-ia]]
- [[sources/navigation-paradox-2026]]
