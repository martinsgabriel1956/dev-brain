---
type: concept
title: "COBOL"
aliases: ["Common Business-Oriented Language"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 1
tags: [cobol, mainframe, legado, sistema-financeiro, linguagem-de-programacao]
skill: tech-mentor-backend
status: stub
---

# COBOL

Uma das linguagens de programação mais antigas ainda em uso ativo. Desenvolvimento iniciado em 1959 por um consórcio de indústria e governo dos Estados Unidos, num momento em que computadores deixavam de servir só a cálculo científico e passavam a automatizar atividades administrativas de grandes empresas. O objetivo era representar regras de negócio, processamento de registros, operações financeiras e relatórios de forma legível e — algo incomum na época — relativamente independente do fabricante do hardware.

## Auge (1960–1980)

Bancos, seguradoras, telecomunicações, companhias aéreas e órgãos governamentais construíram seus sistemas centrais em COBOL, sustentados por mainframes como o IBM System/360 e compiladores como IBM Enterprise COBOL e Micro Focus COBOL.

## Por que perdeu espaço em projetos novos

A partir dos anos 1990, Java, C# e C++ passaram a dominar novas aplicações corporativas; a expansão de internet, interfaces gráficas e computação distribuída deslocou a maior parte do desenvolvimento novo para essas plataformas.

## Por que ainda sustenta o sistema financeiro mundial

Grande parte do sistema financeiro global roda sobre aplicações COBOL, processando milhões de transações por dia. Em vez de reescrever esses sistemas por inteiro, organizações tendem a modernizar a borda — expondo funcionalidades via API, filas de mensagens e novos serviços — mantendo o núcleo de regra de negócio em COBOL (ver padrões de integração com legado no [[wiki/concepts/esb-enterprise-service-bus|ESB]] e no [[wiki/concepts/strangler-fig-pattern]]). No Brasil, boa parte da infraestrutura do sistema financeiro — incluindo os sistemas que sustentam o Pix — depende de aplicações em COBOL.

A linguagem continua evoluindo: a versão mais recente do padrão oficial foi publicada em 2023, mais de 60 anos após sua criação, já com orientação a objetos, tipos de dados definidos pelo usuário e suporte a Unicode.

## Cuidados práticos na integração com sistemas COBOL

- Campos de tamanho fixo (`CHAR(10)`) retornam com espaços à direita — sempre fazer `.trim()`.
- Encodings inesperados são comuns (EBCDIC, ISO-8859-1, Windows-1252) — especificar encoding explicitamente.
- Datas costumam ser armazenadas sem timezone — documentar a timezone assumida.
- Nunca gerar código a partir do schema do legado diretamente; usar uma camada de anti-corrupção (anti-corruption layer) para traduzir entre o modelo legado e o modelo moderno.

## Key Sources

- [[wiki/sources/tecnologias-hype-passado-soap-xml-esb-jquery-cobol]]
