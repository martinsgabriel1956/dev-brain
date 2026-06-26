---
type: concept
title: "Modelo Mental de Fluxo de Dados"
aliases: ["mental model", "modelo mental de codebase", "fluxo de dados mental"]
date_created: 2026-06-20
date_updated: 2026-06-20
source_count: 1
tags: [onboarding, codebase, aprendizado, arquitetura]
skill: tech-mentor-leadership
status: stable
---

# Modelo Mental de Fluxo de Dados

Representação interna e navegável de como os dados se movem dentro de uma codebase — quais eventos disparam quais funções, onde o estado é mutado, quais componentes re-renderizam. É o objetivo final da [[wiki/concepts/exploracao-com-intencao]].

## Como se forma

Não é construído lendo a estrutura de arquivos. Emerge de seguir ações concretas do ponto de entrada (evento do usuário) até o efeito final (estado atualizado, UI re-renderizada, dado persistido). Cada fio seguido adiciona uma rota ao mapa mental.

## Sinal de que o modelo está formado

Você usa o app e consegue antecipar mentalmente qual código está executando — qual função processa o clique, qual reducer atualiza o estado, qual componente recebe o novo prop. O app se torna uma janela transparente para o código.

## Relação com [[wiki/concepts/aprendizado-por-impressoes]]

Cada vez que você revisa a documentação, usa o app ou lê o código com mais contexto, o modelo mental fica mais rico. As primeiras passadas criam estrutura grosseira; as seguintes adicionam detalhes e conectam partes que antes pareciam isoladas.

## Key sources

- [[wiki/sources/como-aprender-novas-codebases]]
