---
type: entity
title: "Código Fonte TV"
aliases: ["Codigo Fonte TV", "CDF"]
date_created: 2026-07-10
date_updated: 2026-08-18
source_count: 6
tags: [canal, youtube, mercado-de-trabalho, pesquisa-salarial, brasil, design-patterns, typescript]
skill: tech-mentor-leadership
status: stub
---

# Código Fonte TV

Canal brasileiro de YouTube com quase 9 anos de produção de conteúdo sobre programação e mercado de trabalho em tecnologia. Mantém a "pesquisa.codefonte.com.br", uma pesquisa salarial própria filtrável por linguagem principal, nível, modelo de contratação (CLT/PJ) e estado — usada como fonte recorrente de dados de mercado no canal.

## Perfil

- Produz a série "Dicionário do Programador", cobrindo linguagens e tecnologias em formato de referência — ex.: episódio sobre [[wiki/concepts/cqrs]]
- Cruza dados da própria pesquisa salarial com pesquisas oficiais de fabricantes de linguagem (ex.: Go Developer Survey do Google) para dar mais robustez às conclusões sobre mercado
- Mantém o segmento **CDF Café**, formato de conversa mais livre sobre temas diversos da indústria (carreira, mercado, IA) regado a café
- Também produz uma série de "mão no código" sobre design patterns GoF em TypeScript/Deno — já cobriu [[wiki/concepts/strategy-pattern]], [[wiki/concepts/facade-pattern]] e [[wiki/concepts/singleton-pattern]] antes do episódio sobre [[wiki/concepts/observer-pattern]]

## Nota de identificação

O texto do vídeo sobre Observer se autorreferencia como "Código Fonte TV" ao convidar para seguir o canal no Instagram, o que motivou atribuir esta fonte a esta entidade. Diferente das fontes anteriores (pesquisa salarial, CDF Café), este episódio é conteúdo hands-on de programação — mostra que o canal cobre tanto mercado/carreira quanto design patterns com código. Sem evidência de conflito com outra entidade (diferente do caso [[wiki/entities/eric-lenda]]/[[wiki/entities/erick-wendel]]).

## Key Sources

- [[wiki/sources/golang-mercado-salarios-pesquisa-2024]]
- [[wiki/sources/custo-real-ia-tokens-produtividade-demissoes]] — episódio do CDF Café sobre custo real de IA, token economics e demissões
- [[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] — episódio do CDF Café sobre RFCs, skill Grill Me e quality gates contra a perda de entendimento no vibe coding
- [[wiki/sources/design-pattern-observer-codigo-fonte-tv]] — episódio "mão no código" sobre o padrão Observer em TypeScript/Deno, com exemplo genérico e exemplo de notificação de vídeo do YouTube
- [[wiki/sources/cqrs-dicionario-programador-codigo-fonte-tv]] — episódio "Dicionário do Programador" sobre CQRS: progressão de cenários de motivação, task-based UI, command bus, estratégias de sincronização e menção a Event Sourcing
- [[wiki/sources/design-pattern-facade-codigo-fonte-tv]] — segundo episódio "mão no código" da minissérie de design patterns (depois de Strategy): Facade via exemplo de remoção de conta sob LGPD, com posição própria (diverge de Renato Augusto) de que a implementação fere o SRP
