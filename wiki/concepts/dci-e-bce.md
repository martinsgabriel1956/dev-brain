---
type: concept
title: "DCI e BCE — Precursores da Clean Architecture"
aliases: ["data context interaction", "boundary control entity", "dci", "bce"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
tags: [arquitetura, clean-architecture, dci, bce, uml, jacobson, reenskaug, coplien]
skill: tech-mentor-backend
status: stub
---

# DCI e BCE — Precursores da Clean Architecture

Duas arquiteturas anteriores à [[wiki/concepts/clean-architecture]], citadas por Robert Martin como parte da síntese que deu origem a ela (junto com [[wiki/concepts/hexagonal-architecture]]).

## DCI — Data, Context, Interaction

Criado por Trygve Reenskaug (também criador do MVC) e James Coplien. Parte da tese de que a programação orientada a objetos convencional, centrada em *classes*, esconde como os objetos colaboram em tempo de execução para atingir um comportamento — o código não revela isso, só a estrutura estática. O DCI propõe três perspectivas distintas:

- **Dados** — representação do estado do sistema (mapeia para o modelo de domínio / Entidades)
- **Contexto** — redes de objetos comunicantes em tempo de execução, incluindo o conceito de **Roles** (papéis que um objeto pode representar — ex: uma conta bancária pode ser "conta origem" ou "conta destino" numa transferência)
- **Interação** — como os objetos colaboram para atingir o comportamento do sistema (mapeia para Casos de Uso — o próprio Robert Martin usa o termo "interactors" para casos de uso, evidenciando a relação)

## BCE — Boundary, Control, Entity

Desenvolvido por Ivar Jacobson (também um dos pioneiros da UML), a partir de sua abordagem de engenharia de software orientada a objetos guiada por casos de uso. Estrutura as classes do sistema por responsabilidade na realização de casos de uso:

- **Entidade** — objetos de domínio geralmente persistidos
- **Fronteira** — interações com atores externos (usuários, sistemas externos); nome original era "Interface", trocado para evitar confusão com *interfaces* de código
- **Controle** — lógica de negócio e coordenação necessária para executar um caso de uso

## Por que importam

Ambas convergem para a mesma ideia central que a Clean Architecture formaliza: separar o modelo de domínio (Dados/Entidade), a comunicação com o mundo externo (Fronteira), e a orquestração de casos de uso (Interação/Controle) em responsabilidades distintas — a mesma separação de interesses que aparece, com nomes diferentes, em [[wiki/concepts/hexagonal-architecture]] e em [[wiki/concepts/clean-architecture]].

## Key Sources

- [[wiki/sources/arquitetura-limpa-na-pratica]] — resumo de DCI e BCE como parte da genealogia da Clean Architecture, no capítulo "A Arquitetura Limpa"
