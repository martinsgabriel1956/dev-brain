---
type: source
title: "The S.O.L.I.D Principles in Pictures"
aliases: ["solid principles in pictures", "solid em imagens ugonna thelma"]
date_created: 2026-08-06
date_updated: 2026-08-06
source_count: 0
tags: [solid, oop, architecture]
skill: tech-mentor-backend
status: stable
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/solid-principles-in-pictures-ugonna-thelma.md"
source_url: "https://medium.com/backticks-tildes/the-s-o-l-i-d-principles-in-pictures-b34ce2f1e898"
author: "Ugonna Thelma"
date_published: "2020-05-18"
date_ingested: "2026-08-06"
---

## TL;DR

Artigo original (Medium, Backticks & Tildes, 2020) que deu origem às ilustrações de robôs usadas no vídeo já ingerido em [[wiki/sources/principios-solid-ilustrados]]. Traz a definição formal de cada um dos cinco princípios SOLID em uma frase, mais uma explicação curta do porquê e do objetivo de cada um — sem o aprofundamento em exemplos de código que o vídeo adiciona por cima.

---

## Reivindicações Principais

**Claim:** SRP reduz risco de bug ao separar comportamentos, para que uma mudança numa responsabilidade não vaze para funcionalidades não relacionadas.
**Evidência:** Definição formal: "uma classe deve ter uma única responsabilidade."
**Confiança:** Alta — formulação direta da autora, consistente com a leitura de Uncle Bob já documentada em [[wiki/concepts/single-responsibility]].

**Claim:** OCP existe porque modificar o comportamento de uma classe já existente impacta todo sistema que depende dela — estender com métodos novos evita quebrar quem já usa a classe.
**Evidência:** Definição formal: "classes devem estar abertas para extensão, mas fechadas para modificação."
**Confiança:** Alta.

**Claim:** LSP exige que uma subclasse execute todas as ações da classe pai e retorne tipos de resultado compatíveis — não apenas "algo parecido".
**Evidência:** Exemplo textual do artigo: se a classe pai retorna `Coffee`, a subclasse pode retornar `Cappuccino` (subtipo compatível), mas não `Water` (tipo não relacionado).
**Confiança:** Alta — é o exemplo mais concreto e verificável do artigo, mais explícito que a ilustração do café descrita de segunda mão no vídeo.

**Claim:** ISP existe para que uma classe não implemente métodos que não usa — dividindo um conjunto grande de ações em subconjuntos menores.
**Evidência:** Definição formal: "clientes não deveriam ser forçados a depender de métodos que não usam."
**Confiança:** Alta.

**Claim:** DIP se apoia em quatro termos definidos explicitamente pela autora: módulo de alto nível (a classe que usa uma ferramenta), módulo de baixo nível (a ferramenta), abstração (a interface que conecta os dois) e detalhes (como a ferramenta funciona por dentro).
**Evidência:** Definição formal: "módulos de alto nível não deveriam depender de módulos de baixo nível — ambos deveriam depender da abstração."
**Confiança:** Alta — vocabulário mais preciso que a ilustração do "soquete" usada no vídeo, útil para desambiguar os termos.

---

## Os 5 Princípios — Definições Formais da Fonte Primária

| Letra | Princípio | Definição (tradução) |
|---|---|---|
| S | [[wiki/concepts/single-responsibility-principle]] | Uma classe deve ter uma única responsabilidade |
| O | [[wiki/concepts/open-closed-principle]] | Classes devem estar abertas para extensão, mas fechadas para modificação |
| L | [[wiki/concepts/liskov-substitution-principle]] | Se S é subtipo de T, objetos do tipo T podem ser substituídos por objetos do tipo S |
| I | [[wiki/concepts/interface-segregation-principle]] | Clientes não deveriam ser forçados a depender de métodos que não usam |
| D | [[wiki/concepts/dependency-inversion-principle]] | Módulos de alto nível não deveriam depender de módulos de baixo nível — ambos deveriam depender da abstração |

## Conceitos

- [[wiki/concepts/single-responsibility-principle]]
- [[wiki/concepts/open-closed-principle]]
- [[wiki/concepts/liskov-substitution-principle]] — exemplo textual `Coffee`/`Cappuccino`/`Water`
- [[wiki/concepts/interface-segregation-principle]]
- [[wiki/concepts/dependency-inversion-principle]] — vocabulário formal (módulo de alto/baixo nível, abstração, detalhes)

## Entidades

- [[wiki/entities/ugonna-thelma]] — autora, identidade confirmada nesta ingestão

## Conexões com Outras Sources

- [[wiki/sources/principios-solid-ilustrados]] — vídeo (PT-BR) que usa as mesmas ilustrações desta fonte primária como fio condutor, com exemplos de código adicionados por cima; a autoria ficou incerta naquela ingestão ("gol na Telma", deformação de ASR) e é resolvida aqui

## Nota sobre Skill Carregada

Skill carregada: `tech-mentor-backend`, lida de `/home/gabriel-martins/Documentos/skills/tech-mentor-backend/SKILL.md` e do arquivo de referência `references/architecture-evolutionary.md` (seção "SOLID na Prática para Arquitetos") — mesmo skill já usado na ingestão do vídeo relacionado, path drift de `CLAUDE.md` já registrado anteriormente.

## Perguntas Abertas

_(nenhuma — esta ingestão resolve a pergunta em aberto de identidade de autoria deixada por [[wiki/sources/principios-solid-ilustrados]])_
