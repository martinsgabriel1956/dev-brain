---
date: 2026-05-17
tags: [tech-mentor, system-design, decisoes-tecnicas, documentacao]
skill: tech-mentor-system-design/references/adr
level: intermediário
---

# Architecture Decision Record (ADR)

## Contexto
Projetos de longa duração acumulam decisões técnicas invisíveis. Sem registro, o time futuro herda consequências sem entender causas — o que gera retrabalho, debates recorrentes e medo de mexer em partes críticas do sistema.

ADR resolve isso: é um documento curto, imutável e datado que captura **uma decisão arquitetural já tomada**, o contexto que a motivou e os trade-offs conscientemente aceitos.

## Como Funciona

Cada ADR cobre uma única decisão. O arquivo fica no repositório junto ao código (`docs/decisions/` ou `adr/`), versionado com git. Nunca é editado — se a decisão mudar, cria-se um novo ADR que supersede o anterior.

**Status possíveis:** `Proposed` → `Accepted` → `Deprecated` → `Superseded by ADR-XXXX`

### Estrutura padrão (MADR)

```markdown
# ADR-0012: Usar PostgreSQL como banco principal

## Status
Accepted

## Contexto
Precisamos de ACID, suporte a JSON semi-estruturado e full-text search.
O time já tem expertise em SQL relacional. Escala de escrita não é gargalo hoje.

## Decisão
Adotar PostgreSQL 16 com Prisma como ORM.

## Consequências
+ Transações ACID nativas, sem workaround
+ jsonb + GIN index resolve 90% dos casos NoSQL que tínhamos
+ Prisma migrations garantem histórico de schema
- Horizontal write scaling exige Citus ou sharding manual
- Operação mais complexa que managed NoSQL (RDS mitiga parcialmente)
```

### Exemplo real — decisão de autenticação

```markdown
# ADR-0023: JWT stateless com refresh token rotation

## Status
Accepted

## Contexto
Sistema SPA + mobile. Precisamos de auth sem estado no servidor para
escalar horizontalmente sem sessão centralizada. Time tem familiaridade com JWT.

## Decisão
Access token JWT (15min) + refresh token opaque armazenado em httpOnly cookie (7d).
Rotation a cada uso do refresh token. Blacklist mínima só para logout explícito.

## Consequências
+ Stateless no caminho quente — sem roundtrip ao Redis por request
+ Rotation limita janela de comprometimento do refresh token
- Revogação de access token antes de 15min não é possível sem blacklist
- Aceito: para o threat model atual, 15min é risco tolerável
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Imutabilidade | Preserva contexto histórico fiel | Não corrige erros — precisa de novo ADR |
| Proximidade ao código | Versionado com git, visível no PR | Fácil de esquecer de criar |
| Formato curto | Baixo custo de escrita | Pode faltar detalhe em decisões complexas |
| Escopo por decisão | Fácil de buscar e referenciar | Proliferação de arquivos em times ativos |

## Quando Usar / Quando Evitar

**Usar quando:**
- A decisão afeta estrutura, tecnologia, contrato de API ou schema de DB
- É difícil ou cara de reverter
- Vai aparecer em code review recorrentemente ("por que usamos X?")
- Há alternativas razoáveis que foram descartadas conscientemente

**Evitar quando:**
- Decisão é trivial ou completamente reversível
- É uma convenção de estilo (vai para CLAUDE.md ou contributing guide)
- A decisão ainda não foi tomada — use [[request-for-comments]] para isso

## Conceitos Relacionados
[[request-for-comments]] · [[system-design]] · [[tech-debt]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-05-17*
