---
type: source
title: "5 Boas Práticas de UI/UX (com Cursor e UX Pilot)"
aliases: ["5 boas praticas uiux", "hierarquia visual gestalt affordance", "boas praticas ux pilot"]
date_created: 2026-07-21
date_updated: 2026-07-21
source_count: 0
tags: [ui, ux, design, frontend, ux-pilot, figma, prompt-engineering, gestalt, affordance]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/5-boas-praticas-uiux-ux-pilot.md"
source_url: ""
author: ""
date_published: "2026"
date_ingested: 2026-07-21
---

# 5 Boas Práticas de UI/UX (com Cursor e UX Pilot)

## TL;DR

Vídeo (transcrição colada diretamente no chat, sem arquivo pré-existente) comparando duas versões de uma mesma landing page: uma gerada com um prompt padrão no Cursor, e outra refinada no UX Pilot (ferramenta de geração de UI/UX que exporta para Figma, de onde se conecta via MCP a uma IA de código). A diferença entre as duas não é sorte nem "vibe" — é a aplicação de quatro conceitos clássicos de design (mais um bônus sobre wireframes): hierarquia visual, lei da proximidade (Gestalt), affordance e a interface como máquina de estados. Tese central: desenvolvedores (especialmente back-end) raramente conhecem esses conceitos, e aplicá-los explicitamente nos prompts de ferramentas de geração de UI (ou no código direto) já produz interfaces sensivelmente mais amigáveis e conversivas.

## Key Claims

- **Hierarquia visual**: fontes, pesos, cores e posicionamento devem ser desenhados para que o olho siga uma ordem de importância. Dois CTAs com o mesmo peso visual competem pela atenção do usuário e reduzem a conversão do CTA principal (o mais fácil de executar "vence"). Evidência: comparação direta entre as duas versões da landing page e exemplos do Google sobre hierarquia tipográfica.
- **Padrões de leitura em tela**: padrão Z (menos texto, mais elementos — apps, landing pages) vs. padrão F (muito texto — blogs). Escolher o padrão errado para o tipo de conteúdo desalinha o fluxo visual pretendido com o real. Evidência: artigo externo citado no vídeo sobre padrões de visualização (não linkado na transcrição).
- **Lei da proximidade (Gestalt)**: elementos próximos são percebidos como um grupo único; elementos distantes ou de cores/formas diferentes são percebidos como grupos distintos — independentemente do conteúdo. Exemplo citado: o logo da Unilever, onde ícones isolados (cenoura, flor, peixes) formam a letra U apenas quando vistos em conjunto. Aplicação prática: aproximar prova social (número de cursos, horas de conteúdo) do título da promessa, e distanciar esse bloco do formulário, para separar visualmente "promessa" de "ação".
- **Affordance**: propriedade visual/interativa de um elemento que sugere, por si só, como deve ser usado (botão sugere clique, switch sugere puxar, slider sugere arrastar, microfone sugere fala) — reduzindo a curva de aprendizado da interface. Erro recorrente em UI gerada por IA: ausência de `cursor: pointer`, hover/glow em botões, e sublinhado em links — pequenos detalhes cuja falta causa confusão sobre o que é clicável.
- **Interface como máquina de estados**: todo componente interativo deveria ter seus estados (idle, preenchendo, loading, erro, sucesso) mapeados explicitamente antes da implementação — a ausência de estado de loading em telas que buscam dados é o sintoma mais comum de não ter feito esse mapeamento. Um mesmo componente nunca deveria conseguir ocupar dois estados mutuamente exclusivos ao mesmo tempo (ex.: erro e sucesso simultâneos).
- **Fluxo de ferramentas**: UX Pilot (geração de conceito UI/UX, inclusive wireframes) → Figma (exportação) → MCP do Figma → IA de código (Cursor/Claude Code) para implementação. Selecionar apenas a seção da tela que se quer alterar (em vez do design inteiro) permite iterar sem perder o que já funcionou em outras seções.
- **Meta-técnica de prompting**: usar um LLM de texto para ajudar a redigir o prompt de design (a partir de um print + explicação da lei que se quer aplicar) antes de colar na ferramenta de geração de UI, e evitar usar a versão anterior como referência de imagem quando o objetivo é fugir do estilo visual dela (a IA tende a herdar cores/fontes do print de referência).

## Entities

Nenhuma entidade com página própria na wiki é o foco central deste vídeo. UX Pilot é citado como ferramenta central — ver stub criado em [[wiki/entities/ux-pilot]]. [[wiki/entities/figma]] e Cursor (sem página dedicada na wiki) aparecem como parte do fluxo de trabalho.

## Concepts

- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/lei-da-proximidade-gestalt]]
- [[wiki/concepts/affordance]]
- [[wiki/concepts/maquina-de-estados-ui]]
- [[wiki/concepts/design-como-interacao]]
- [[wiki/concepts/design-engineer]]
- [[wiki/concepts/design-first]]
- [[wiki/concepts/estado]]

## Open Questions

- Autor do vídeo não identificado no texto transcrito — atualizar `author`/`source_url` se a origem for encontrada depois.
- O artigo citado sobre padrões Z/F não foi linkado na transcrição — se encontrado, vale registrar como fonte externa `[external]` na página de [[wiki/concepts/hierarquia-visual]].

## Raw Quotes

> "A hierarquia visual dos elementos não tá pensada da melhor forma pra explicar o que o usuário tem que fazer na tela."

> "Como a ação de ver cursos disponíveis é mais fácil do que preencher o formulário, muito provavelmente eu vou ter um número menor de inscrições — esse CTA vai acabar tirando o número de pessoas que vão preencher o formulário."

> "Affordance em UX é uma propriedade visual ou interativa de um elemento que sugere como ele deve ser utilizado, guiando o usuário através das ações de forma intuitiva."

> "É muito comum a gente acessar frontends que buscam dados e não têm um loading na tela — esse estado teria sido mapeado caso a pessoa tivesse pensado um pouquinho sobre como uma máquina de estados funciona."
