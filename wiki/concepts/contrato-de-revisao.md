---
type: concept
title: "Contrato de Revisão"
aliases: ["contrato de revisão auditável", "review contract", "contrato implementador-revisor"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [contrato-de-revisao, spec-driven-development, revisao-por-ia, verificabilidade, quality-gate, acceptance-criteria]
skill: tech-mentor-ai
status: draft
---

# Contrato de Revisão

Documento **verificável** que liga implementador e revisor: o implementador desenvolve garantindo cumpri-lo; o revisor o lê e confere item por item, **sem precisar entender o contexto do projeto**. É a peça que, segundo [[wiki/sources/pilares-desenvolvimento-com-ia-contrato-de-revisao-waves]], falta no workflow básico e nas ferramentas de [[wiki/concepts/spec-driven-development|SDD]] ("você já viu o contrato de revisão que essas ferramentas têm umas com as outras?") — afirmação do autor, não verificada.

## Conteúdo (exemplo da fonte)

- **Pré-requisitos de runtime:** backend, framework, banco, diretório gravável, **browser real** (Playwright CLI).
- **Estado inicial do teste:** usuários/dados que devem existir (ex.: Alice admin suspensa, usuário em branco, Bob para UI, arquivos de mídia com formato definido).
- **Gates de qualidade:** scripts de linter, dependências, arquitetura e camadas (regra de negócio no controller falha; repositório instanciado na camada errada falha), código slop/morto (Knip), dependência circular, organização de arquivos = [[wiki/concepts/fitness-functions]] / [[wiki/concepts/quality-gate]].
- **Rastreabilidade:** cada item deriva de um **critério de aceitação** do produto e aponta os testes que o cobrem.
- **Superfícies:** onde verificar (API HTTP, UI, protocolos). Qualquer agente deve conseguir rodar e bater **cada item**.

## Por que importa

Habilita a [[wiki/concepts/revisao-por-agente-independente]]: revisar algo que não está claro para ser revisado "não é uma revisão completa". Também suporta [[wiki/concepts/waves-de-desenvolvimento]], pois cada tarefa paralela carrega o próprio critério de "pronto".

## Notas / limites

- Relação com [[wiki/concepts/contrato-de-api]] é só de nome (aquele descreve interface entre serviços); aqui o contrato é de **verificação de entrega**. Próximo de [[wiki/concepts/criterios-de-uma-boa-spec]] e do padrão "condição de parada verificável" de [[wiki/concepts/loop-engineering]] [inferência].
- Sem dados sobre o custo de escrever/manter o contrato para features pequenas.

## Key sources

- [[wiki/sources/pilares-desenvolvimento-com-ia-contrato-de-revisao-waves]]
