---
type: source
title: "Graceful Degradation"
aliases: ["degradação graciosa", "fallback", "fail-open", "fail-closed"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 0
tags: [graceful-degradation, fallback, fail-open, fail-closed, resiliencia, system-design]
skill: tech-mentor-system-design
status: draft
source_file: /home/nemomartins/Documentos/new/dev-study/raw/graceful-degradation.md
source_url:
author:
date_published:
date_ingested: 2026-04-23
---

# Graceful Degradation

## TL;DR

Graceful Degradation é o princípio de continuar operando com capacidade reduzida quando um componente falha, ao invés de falhar completamente. Hierarquia de fallbacks: dado em cache stale → resposta genérica degradada → feature desabilitada → erro. Fail-closed (rejeita quando não sabe) vs Fail-open (permite quando não sabe) — a escolha depende do contexto de segurança. Promise.allSettled é o padrão correto para múltiplos serviços opcionais.

## Key Claims

| Claim | Evidência |
|---|---|
| Cache stale é melhor que erro — usuário prefere dado desatualizado a página quebrada | Padrão de resiliência amplamente documentado |
| Fail-closed para segurança (autenticação, pagamento) — rejeitar se dúvida | Erro de segurança é irreversível |
| Fail-open para disponibilidade (recomendações, anúncios) — permitir se dúvida | Serviço não-crítico não deve derrubar o core |
| Promise.allSettled não propaga falha de serviços opcionais | Ao contrário de Promise.all que falha no primeiro erro |
| Feature flag como terceiro tipo de fallback | Desabilitar feature inteira via toggle |

## Conceitos

- [[concepts/graceful-degradation]] — já existe no index
- [[concepts/circuit-breaker]] — detecta falha e aciona fallback automaticamente
- [[concepts/bulkhead]] — isolamento previne cascata
- [[concepts/feature-flags]] — mecanismo de disable programático
- [[concepts/falha-em-cascata]] — o que graceful degradation previne

## Key Sources

_Este é o documento primário._
