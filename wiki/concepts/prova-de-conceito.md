---
type: concept
title: "Prova de Conceito (PoC)"
aliases: ["proof of concept", "PoC", "protótipo técnico", "spike"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [processo, tecnologia, inovação, risco, protótipo]
skill: tech-mentor-leadership
status: stable
---

# Prova de Conceito (PoC)

Projeto pequeno e isolado para **testar uma tecnologia ou abordagem nova antes de adotá-la em produção**. Mata a ansiedade de "quero usar isso" sem colocar sistemas consolidados em risco.

## O problema que resolve

Devs tendem a querer usar tecnologias novas por ansiedade, não por necessidade do cliente. Adotar tecnologia em beta ou recém-lançada em projetos grandes e consolidados é amadorismo — o produto tem muito a perder.

```
❌ Usar tecnologia nova diretamente em produção consolidada
   Motivo real: ansiedade de usar algo novo
   Resultado: instabilidade, bugs de borda, legado difícil de manter

✅ PoC isolada primeiro
   Resultado: ansiedade saciada, aprendizado real, decisão informada
```

## Quando uma tecnologia vai de PoC para produção

- PoC funcionou e os trade-offs são aceitáveis
- A tecnologia saiu de beta / tem histórico de estabilidade
- O ganho para o cliente/produto é claro e mensurável
- O time tem capacidade de manter

## Formato de uma boa PoC

1. **Escopo mínimo** — problema específico, não reescrever tudo
2. **Timeboxed** — 1-3 dias, não semanas
3. **Critérios de sucesso definidos antes** — o que você quer validar?
4. **Descartável por padrão** — código de PoC raramente vai para produção diretamente

## Conexão com flexibilidade técnica

Fazer PoCs regularmente evita virar o dev que "sempre usa X" porque nunca experimentou alternativas — ver [[flexibilidade-tecnica]].

## Key Sources

- [[wiki/sources/desenvolvedor-acima-da-media-10-itens]]
