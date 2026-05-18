---
date: 2026-05-17
tags: [tech-mentor, system-design, decisoes-tecnicas, colaboracao]
skill: tech-mentor-system-design/references/rfc
level: intermediário
---

# Request for Comments (RFC)

## Contexto
Algumas mudanças são grandes demais para decidir sozinho ou em silêncio. Breaking changes, migrações de infraestrutura, novos padrões que afetam múltiplos times — essas decisões precisam de input antes de serem implementadas.

RFC é o mecanismo para isso: um documento que **propõe uma mudança ainda não decidida** e abre um período formal de revisão. O objetivo não é convencer — é coletar objeções, alternativas e contexto que o autor não tem.

## Como Funciona

O autor escreve a proposta, define um prazo de feedback e abre para revisão (PR, Notion, Confluence — onde o time trabalha). Ao fim do período, o responsável pela decisão aceita, rejeita ou revisa com base no feedback consolidado.

**Fluxo:**
```
Draft → Comment Period (ex: 1 semana) → Accepted / Rejected / Withdrawn
```

Após aceito, o RFC normalmente origina um [[architecture-decision-record]] que registra a decisão final.

### Estrutura padrão

```markdown
# RFC-0034: Migrar autenticação de JWT stateless para sessions com Redis

## Status
Draft

## Problema
Não conseguimos invalidar tokens antes do TTL. Em casos de comprometimento
de conta, o usuário permanece autenticado por até 15 minutos após logout forçado.
Isso é inaceitável para o nível de segurança exigido pelo produto.

## Proposta
Substituir JWT por session ID opaque armazenado no Redis com TTL de 1h.
Sliding window renova o TTL a cada request autenticado.
Logout invalida imediatamente a sessão no Redis.

## Alternativas Consideradas
1. **JWT Blacklist no Redis** — descartado: mesma dependência operacional,
   complexidade maior, lookups extras no caminho quente
2. **Rotation com TTL de 5min** — descartado: UX degradado, muitos edge cases
   em mobile com conexão instável

## Impacto
- Todos os clients precisam atualizar o header de auth (breaking change)
- Adiciona dependência operacional crítica no Redis
- Redis já existe no stack para cache — não é nova infra
- Equipe mobile precisa de 2 semanas para adaptar

## Perguntas em Aberto
- Qual o plano de fallback se o Redis ficar indisponível?
- Sessões devem ter device fingerprint para detecção de hijacking?

## Prazo para Feedback
2026-05-24

## Autor
@gabriel-martins
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Colaboração assíncrona | Coleta input de quem não está na reunião | Processo mais lento que decidir sozinho |
| Registro de alternativas | Evita re-debater opções já descartadas | Exige disciplina para documentar bem |
| Período formal de revisão | Cria urgência e deadline claro | Pode ser ignorado sem cultura estabelecida |
| Separação proposta/decisão | Reduz viés de ancoragem do autor | Responsabilidade de decidir precisa ser clara |

## Quando Usar / Quando Evitar

**Usar quando:**
- A mudança é breaking change para outros times ou clients
- Envolve escolha de tecnologia com impacto operacional longo
- O autor genuinamente não tem todo o contexto necessário
- A decisão vai afetar como outros times trabalham

**Evitar quando:**
- Você já sabe a resposta — RFC vira teatro burocrático
- A mudança é local e reversível (refactoring interno, renomear variável)
- Urgência não permite período de revisão — decida e registre num ADR
- Time tem menos de 4 pessoas e fala todo dia — conversa é mais eficiente

## Relação com ADR

RFC e ADR são complementares, não substitutos:

```
RFC (proposta + debate) → decisão tomada → ADR (registro permanente)
```

Nem todo ADR precisa de RFC (decisões menores). Mas todo RFC aceito deve gerar um ADR.

## Conceitos Relacionados
[[architecture-decision-record]] · [[tech-debt]] · [[system-design]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-05-17*
