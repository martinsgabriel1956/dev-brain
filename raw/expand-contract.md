---
date: 2026-04-17
tags: [tech-mentor, arquitetura, principios, migracao, compatibilidade, banco]
skill: tech-mentor-backend/references/migration-patterns
level: intermediário
---

# Expand-Contract

## Contexto
Padrão para fazer mudanças de contrato (API, schema de banco, evento) **sem downtime e sem coordenação simultânea** entre todos os serviços consumidores. Também chamado de *parallel change* ou *versioned contract migration*.

O problema central: você não pode mudar uma coluna de banco ou um campo de API no deploy de uma única versão — consumidores e produtores sempre rodam em versões diferentes durante um rolling update.

## As Três Fases

### Fase 1 — Expand (adicionar)
Adicione o novo campo/coluna **sem remover o antigo**. Ambos coexistem. O novo campo começa a ser preenchido; consumidores ainda leem o antigo.

### Fase 2 — Migrate (mover)
Consumidores migram gradualmente para usar o novo campo. O antigo ainda existe para compatibilidade retroativa.

### Fase 3 — Contract (remover)
Quando todos os consumidores migraram, o campo antigo é removido.

## Exemplos Concretos

### Banco de Dados — renomear coluna sem lock

```sql
-- FASE 1: adicionar nova coluna
ALTER TABLE users ADD COLUMN full_name TEXT;

-- Backfill dos dados existentes (em batch para não travar)
UPDATE users
SET full_name = first_name || ' ' || last_name
WHERE full_name IS NULL
  AND id BETWEEN $offset AND $offset + 1000;

-- FASE 2: aplicação escreve em AMBAS colunas
-- Código: user.first_name, user.last_name, user.full_name = ...
-- Leitura: lê full_name com fallback para first_name

-- FASE 3: remover colunas antigas (após todos deployarem a Fase 2)
ALTER TABLE users DROP COLUMN first_name;
ALTER TABLE users DROP COLUMN last_name;
```

### API REST — mover campo de resposta

```typescript
// FASE 1: resposta com AMBOS os campos
// GET /users/:id
{
  "id": "123",
  "name": "Alice",           // campo antigo — mantido
  "displayName": "Alice M."  // campo novo — adicionado
}

// FASE 2: consumidores migram para usar displayName

// FASE 3: remove o campo "name" da resposta
// Anunciar Sunset Policy com data: Sunset: Sat, 01 Jun 2026 00:00:00 GMT
```

### Kafka — evolução de schema de evento

```typescript
// Schema V1 (evento antigo, ainda no tópico)
type UserCreatedV1 = { userId: string; email: string };

// Schema V2 (novo formato)
type UserCreatedV2 = { userId: string; email: string; phoneNumber?: string };

// Consumer Tolerant Reader — lida com ambas as versões
const userCreatedSchema = z.object({
  userId: z.string(),
  email: z.string(),
  phoneNumber: z.string().optional()  // opcional para compatibilidade retroativa
}).passthrough();

// FASE 1: produtor começa a enviar V2 (com phoneNumber quando disponível)
// FASE 2: consumidores leem phoneNumber quando presente
// FASE 3: campo antigo seria removido se houvesse um
```

## Expand-Contract em Banco com Zero Downtime

```
Deploy A (app v1):           app lê: first_name, last_name
  ↓
Migration 001: ADD COLUMN full_name TEXT  ← sem downtime, nullable
  ↓
Deploy B (app v2):           app lê: full_name ?? first_name
                             app escreve: ambas as colunas
  ↓
Background job: backfill full_name para registros antigos
  ↓
Migration 002: ALTER COLUMN full_name SET NOT NULL  ← após backfill
  ↓
Deploy C (app v3):           app lê apenas: full_name
  ↓
Migration 003: DROP COLUMN first_name, last_name  ← sem risco agora
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Downtime | Zero downtime em mudanças de schema | Mais deploys e migrations para uma única mudança |
| Segurança | Rollback possível em qualquer fase | Período de duplicação aumenta tamanho do banco |
| Velocidade | Times não precisam sincronizar deploy | Processo é lento — dias ou semanas entre fases |
| Complexidade | Mudança gradual e reversível | Código temporário com dual-write precisa ser removido |

## Quando Usar / Quando Evitar

**Usar quando:**
- Qualquer mudança de schema em produção com usuários reais
- APIs consumidas por clientes móveis (impossível forçar update simultâneo)
- Microsserviços com contratos entre times diferentes

**Evitar quando:**
- Ambiente de desenvolvimento ou staging sem usuários — DROP direto é mais rápido
- Sistema offline com janela de manutenção aceitável

## Conceitos Relacionados
[[tolerant-reader]] · [[zero-downtime-deploy]] · [[blue-green-canary-rolling]] · [[cdc-debezium]] · [[kafka]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-17*
