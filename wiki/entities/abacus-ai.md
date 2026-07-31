---
type: entity
title: "Abacus.AI"
aliases: ["Abacus", "Abacus AI"]
date_created: 2026-07-31
date_updated: 2026-07-31
source_count: 1
tags: [abacus, model-routing, ai-gateway, ferramenta]
skill: tech-mentor-ai
status: stub
---

# Abacus.AI

Plataforma de IA por assinatura mensal que, entre outras features, oferece um recurso de "Custom Router": permite criar um roteador de modelos próprio, escolhendo um template inicial (ex.: "Frontier") e configurando categorias de tarefa (ex.: Frontier/problem solving, Complexo, Velocidade, Balanceado, Fallback) mapeadas para modelos específicos de diferentes provedores.

## Duas Formas de Roteamento

Segundo [[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]]:

- **RouteLL** — roteamento próprio da Abacus, em que a plataforma decide automaticamente qual modelo é mais adequado para cada prompt (mecanismo de decisão não detalhado na fonte).
- **Custom Router** — o usuário define manualmente as categorias e o modelo associado a cada uma; roteamento por categoria estática configurada pelo humano, não por classificador aprendido. Ver [[wiki/concepts/roteamento-automatico-de-modelo]].

O router gerado expõe uma chave de API que pode ser conectada a outros harnesses de codificação (ex.: [[wiki/entities/opencode]]) como se fosse qualquer outro provider.

**Confiança:** a fonte é um vídeo com bloco de patrocínio explícito da Abacus — a demonstração é tratada como exemplo de um padrão genérico (roteamento configurável por categoria), não como avaliação independente da qualidade ou dos preços da ferramenta.

## Key Sources

- [[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]]
