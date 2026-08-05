---
type: concept
title: "ESB (Enterprise Service Bus)"
aliases: ["Enterprise Service Bus", "barramento de serviços", "iPaaS"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 1
tags: [esb, integracao, legado, arquitetura, mensageria, ipaas]
skill: tech-mentor-backend
status: stub
---

# ESB (Enterprise Service Bus)

Camada de middleware centralizada para integração corporativa, surgida no início dos anos 2000 sob forte influência do livro *Enterprise Integration Patterns* (Gregor Hohpe e Bobby Woolf). Resolvia um problema estrutural: grandes empresas acumulavam dezenas ou centenas de sistemas diferentes (ERP, CRM, legados, bancos de dados, soluções de terceiros), e fazer cada sistema conversar diretamente com todos os outros criava uma malha de integrações ponto-a-ponto praticamente impossível de manter.

O ESB centraliza transformação de mensagens, roteamento, orquestração de serviços, monitoramento e adaptação entre protocolos. Muitos serviços [[wiki/concepts/soap|SOAP]] da época eram publicados e orquestrados dentro de um ESB, que funcionava como barramento único conectando dezenas de sistemas.

## Auge (2004–2015)

Plataformas como MuleSoft, IBM Integration Bus e Oracle Service Bus tornaram-se referência em bancos, seguradoras, telecomunicações e governo.

## Por que perdeu espaço em projetos novos

Com a consolidação da nuvem, da arquitetura orientada a eventos e da economia das APIs, equipes passaram a preferir integração distribuída — API REST, mensageria ponto-a-ponto, plataformas como Kafka — em vez de concentrar lógica de integração num barramento central. [[wiki/concepts/microsservicos]] nasceu em parte como reação a isso: Jim Webber resumiu a filosofia de microsserviços como "smart endpoints, dumb pipes", em oposição direta ao ESB, que ele chamava de "Erroneous Spaghetti Box".

## Por que ainda sustenta empresas com grande legado

Organizações que passaram décadas construindo sistemas dificilmente substituem toda a infraestrutura de integração de uma vez. Nesses ambientes, ESB/iPaaS (MuleSoft, IBM Integration Bus) continua conectando aplicações de épocas diferentes, preservando investimento acumulado ao longo de anos — ver também os padrões de integração com legado ([[wiki/concepts/strangler-fig-pattern]], anti-corruption layer) usados para migrar gradualmente esses ambientes sem reescrita total.

## Key Sources

- [[wiki/sources/tecnologias-hype-passado-soap-xml-esb-jquery-cobol]]
