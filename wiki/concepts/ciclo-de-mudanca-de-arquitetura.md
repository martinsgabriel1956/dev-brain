---
type: concept
title: "Ciclo de Mudança de Arquitetura (AS-IS → TO-BE → POC → Coexistência)"
aliases: ["ciclo de migração arquitetural", "AS-IS TO-BE", "ciclo de vida de mudança arquitetural"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
tags: [arquitetura, migração, as-is, to-be, poc, ciclo-de-vida]
skill: tech-mentor-system-design
status: stub
---

# Ciclo de Mudança de Arquitetura

## TL;DR

Toda mudança arquitetural significativa (trocar padrão de mensageria, adotar Event Sourcing, migrar de banco, decompor um monolito) segue um ciclo com 5 etapas, e pular ou encurtar qualquer uma delas é a causa mais comum de retrabalho caro:

```
1. AS-IS      → entender 100% o estado atual: tecnologia + regras de negócio
2. TO-BE      → desenhar o estado futuro desejado
3. POC        → validar tecnicamente na escala real esperada (não numa fração dela)
4. Migração   → coexistência entre legado (A) e novo (B), com padrões de transição
5. Novo AS-IS → migração concluída = ponto de partida do próximo ciclo
```

## Por que a ordem importa

**AS-IS antes de TO-BE**: escolher um padrão de arquitetura (Event Sourcing, CDC, Transaction Outbox, coreografia vs. orquestração) sem primeiro mapear 100% as regras de negócio do sistema atual é decidir tecnologia antes de entender o problema. O erro típico é ir direto para "vamos usar X" sem levantar o que já funciona, o que não funciona, e por quê.

**POC antes de migração**: uma POC não é uma versão simplificada do TO-BE — é um teste de hipótese técnica sob as condições reais em que o sistema vai operar. Testar a 5% da carga esperada e considerar validado é o erro mais citado: se o volume real é 10.000 transações por segundo, a POC precisa se aproximar desse número, não de uma fração conveniente. Isso é uma extensão específica do conceito geral de [[wiki/concepts/prova-de-conceito]] (que trata POC como "escopo mínimo, timeboxed, descartável") — para migrações de infraestrutura/banco de dados, "mínimo" não pode significar "escala irrealista", porque o comportamento sob carga é frequentemente o próprio objeto do teste.

**Migração não é reescrita "big bang"**: o período de coexistência entre sistema legado e novo sistema exige padrões específicos de roteamento e sincronização de dados — ver [[wiki/concepts/strangler-fig-pattern]]. É o mesmo argumento estrutural por trás de por que o [[wiki/concepts/ciclo-da-desgraca-software]] falha: reescrita completa sem convivência incremental deixa o time correndo atrás do próprio rabo.

**O ciclo não termina** — ele se reinicia. A migração concluída vira o próximo AS-IS. Arquitetura não é uma decisão que se "congela" — é um processo contínuo, o mesmo argumento (em outro nível) já registrado em [[wiki/concepts/arquitetura-de-software]] via [[wiki/sources/filosofia-do-design-de-software-introducao]] contra o modelo cascata.

## Custo de errar a assertividade

O risco central que a fonte aponta não é "escolher a arquitetura errada" isoladamente — é descobrir isso **no meio do ciclo**, depois de tempo já investido. Trocar de rumo é sempre válido quando a informação nova justifica, mas cada etapa pulada ou mal executada (AS-IS incompleto, POC subdimensionada) aumenta a chance de descobrir o erro tarde, quando o custo de corrigir já é alto. Ver [[wiki/concepts/refactor-vs-rewrite-matrix]] para o framework de decisão equivalente quando o "erro" já está em produção, não em planejamento.

## Relacionado

[[wiki/concepts/prova-de-conceito]] · [[wiki/concepts/strangler-fig-pattern]] · [[wiki/concepts/ciclo-da-desgraca-software]] · [[wiki/concepts/refactor-vs-rewrite-matrix]] · [[wiki/concepts/arquitetura-de-software]] · [[wiki/concepts/event-sourcing]] · [[wiki/concepts/outbox-pattern]] · [[wiki/concepts/saga-pattern]]

## Key Sources

- [[wiki/sources/ciclo-de-mudanca-de-arquitetura]]
