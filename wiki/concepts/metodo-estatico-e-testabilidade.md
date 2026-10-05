---
type: concept
title: "Método Estático e Testabilidade"
aliases: ["classe estática", "static helper", "ApiHelper"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_count: 1
tags: [static, testabilidade, acoplamento, helper, camada-cross]
skill: tech-mentor-testing
status: draft
---

# Método Estático e Testabilidade

Refatorar o método herdado para um `ApiHelper` estático **só move o acoplamento**: o consumidor chama `ApiHelper.ChamarApi` diretamente e não há ponto para substituir a chamada nem criar mock — o teste sai para a rede de novo ([[wiki/sources/tres-tipos-de-acoplamento-que-impedem-teste-unitario-andre-casciotti]]).

Pontos do autor:

- O estático "vale para a aplicação toda" e vive enquanto a aplicação estiver no ar; uma variável estática funciona como cache global (apagar afeta todos). Questões de threads existem.
- Nome genérico (*Helper*) é sinal de falta de limite de responsabilidade.
- **Não é proibido:** camadas *cross* e classes estáticas são válidas; o que não se pode é furar limites ou ligar o contexto de negócio à tecnologia.
- Cura: classe instanciável + interface, injetada no construtor.

**[inferência]** Estático puro (sem I/O nem estado compartilhado) não atrapalha o teste; o dano vem do estático que embute infraestrutura ou estado. Relaciona-se a [[wiki/concepts/singleton-pattern]] (estado global) e a [[wiki/concepts/acoplamento-que-impede-teste-unitario]].

## Key sources

- [[wiki/sources/tres-tipos-de-acoplamento-que-impedem-teste-unitario-andre-casciotti]]
