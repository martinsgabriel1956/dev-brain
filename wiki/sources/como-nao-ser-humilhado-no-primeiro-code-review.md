---
type: source
title: "Como Não Ser Humilhado no Primeiro Code Review"
aliases: ["primeiro code review", "code review júnior", "como sobreviver ao code review"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/como-nao-ser-humilhado-no-primeiro-code-review.md
source_url: null
author: null
date_published: null
date_ingested: 2026-07-03
source_count: 0
tags: [carreira, code-review, júnior, inteligência-emocional, síndrome-do-impostor, testes, mentoria]
skill: tech-mentor-leadership
status: stable
---

# Como Não Ser Humilhado no Primeiro Code Review

> Fonte: transcrição de vídeo (canal/autor não identificado na transcrição), resumida em [[raw/como-nao-ser-humilhado-no-primeiro-code-review]] sem reprodução literal do texto original.

## TL;DR

O choque do primeiro code review de um júnior quase nunca é sobre competência — é sobre desconhecimento do padrão da empresa. Cinco passos práticos reduzem a fricção: validar a regra de negócio antes do estilo, revisar o próprio código (com IA ou colega) antes do PR sem virar dependência, testar em ambientes externos antes de produção, não levar comentários de review para o lado pessoal, e validar em produção após o deploy.

## Claims Principais

- A maioria dos comentários no primeiro code review reflete desconhecimento do padrão/framework da empresa, não incompetência — o padrão de escrita de quem revisa raramente coincide com o de quem chega.
- Quem revisa costuma comentar de forma seca não por má intenção, mas por falta de tempo e de prática em dar feedback com tato.
- Prioridade de revisão: primeiro a regra de negócio (o código faz o que o PO pediu?), só depois estilo e formatação — código limpo que não resolve o pedido não serve.
- Revisar o próprio código com apoio de IA antes do PR é útil **se** vier acompanhado de pedir explicação do "porquê" de cada mudança — sem isso vira [[wiki/concepts/dependencia-ia]] disfarçada de boa prática.
- "Funciona na minha máquina" é insuficiente: testar em ambiente de desenvolvimento/homologação antes do PR, nunca validar mudanças direto em produção.
- Comentários de code review são sobre o código, não sobre a pessoa — reagir defensivamente ("não faz sentido") prejudica mais do que ouvir primeiro e questionar depois.
- Nos primeiros meses, alinhar prioridade com o PO antes de abrir PR, e evitar criar tarefas fora do escopo pedido — se a iniciativa não pedida der errado, a responsabilidade recai sobre quem a propôs.
- Validar manualmente em produção após o deploy, antes de fechar a tarefa como concluída; reportar um bug encontrado nessa checagem é sinal de comprometimento, não de falha.

## Conceitos Abordados

- [[wiki/concepts/code-review]]
- [[wiki/concepts/sindrome-do-impostor]]
- [[wiki/concepts/definicao-de-pronto]]
- [[wiki/concepts/paridade-local-producao]]
- [[wiki/concepts/inteligencia-emocional]]
- [[wiki/concepts/mentoria-tecnica]]
- [[wiki/concepts/pensamento-em-producao]]
- [[wiki/concepts/autonomia-responsabilidade]]
- [[wiki/concepts/dependencia-ia]]

## Questões Abertas

- O vídeo não define o que fazer quando o padrão de estilo da empresa é genuinamente ruim/desatualizado — a orientação de "não levar pro pessoal" vale mesmo quando a crítica é discutível?
- Como equilibrar "não criar tarefa que ninguém pediu" com a expectativa de que júniors também demonstrem iniciativa técnica?
