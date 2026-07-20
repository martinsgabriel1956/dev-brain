---
type: concept
title: "KISS — Keep It Simple"
aliases: ["kiss", "keep it simple", "pensar simples", "simplicidade intencional"]
date_created: 2026-04-29
date_updated: 2026-07-19
source_count: 3
tags: [kiss, over-engineering, principios, qualidade, design-patterns, testes]
skill: tech-mentor-backend
status: stable
---

## Definição

KISS (Keep It Simple, Stupid / Keep It Simple and Stupid) é o princípio de evitar aumentar a complexidade de uma solução além do necessário para resolver o problema. Não é limitação de conhecimento — é disciplina intencional de suprimir complexidade desnecessária.

## O paradoxo da expertise

Pensar simples é fácil quando você sabe pouco — você está limitado pelo próprio conhecimento.

Pensar simples é difícil quando você sabe muito — você precisa ativamente escolher não aplicar tudo que sabe. O viés de complexidade cresce com a experiência.

> "Lá na frente pensar simples é uma das coisas mais difíceis na programação quando você tem bagagem e conhecimento."
> — Carol (Até Quinta)

## O que KISS não é

- **Não é defender código bagunçado.** Código simples ≠ código feio ≠ gambiarra.
- **Não é ignorar padrões.** É saber quando aplicá-los.
- **Não é anti-escabilidade.** É distinguir escalabilidade real de escalabilidade hipotética.

## Teste KISS

Antes de adicionar uma abstração, padrão ou camada:
1. Qual requisito real justifica isso agora?
2. Qual dev do time consegue manter isso sem o meu contexto?
3. Quantos arquivos preciso alterar para mudar um comportamento?
4. A explicação da solução é mais complexa que o problema?

Se qualquer resposta for "nenhum", "ninguém", ">3" ou "sim" — reavalie.

## Origem: Marinha dos Estados Unidos

O acrônimo é atribuído à Marinha dos EUA (déc. de 1960), embora a atribuição individual mais citada na literatura de engenharia seja Kelly Johnson, da Lockheed Skunk Works — a origem exata segue sem fonte primária consolidada. Ver [[wiki/sources/kiss-yagni-entrega-rapida-qualidade]] para a versão mais comum contada por criadores de conteúdo de programação.

## KISS aplicado a testes

O princípio não se limita a arquitetura e design: testes unitários que não geram valor real (não protegem contra regressão nem documentam comportamento importante) podem — e devem — ser removidos em favor de uma suíte menor e mais focada no coração do problema. Complexidade desnecessária em teste é o mesmo desperdício que complexidade desnecessária em produção. Ver [[criterios-de-bom-teste]].

## Exemplo: simplificar validação de status com early return + lista de permitidos

Padrão comum de refactor KISS: uma cadeia de `if`s aninhados comparando um status contra vários valores possíveis (ex.: decidir se uma transferência pode ser reprocessada, dado seu status atual) vira uma validação inicial com retorno antecipado, seguida de uma checagem de pertencimento a uma lista de status habilitados.

```typescript
// ❌ Cadeia de ifs aninhados
function podeReprocessar(status: string): boolean {
  if (status === "pendente") {
    if (status !== "cancelado") {
      if (status !== "expirado") {
        return true;
      }
    }
  }
  return false;
}

// ✅ KISS — validação inicial + lista de status permitidos
const STATUS_REPROCESSAVEIS = ["pendente", "falhou", "aguardando_retry"];

function podeReprocessar(status: string): boolean {
  return STATUS_REPROCESSAVEIS.includes(status);
}
```

O ganho não é só linhas de código — é a legibilidade para quem lê depois: fica óbvio quais status habilitam reprocessamento sem precisar simular mentalmente a árvore de `if`s. Ver [[wiki/concepts/idempotencia]] para o padrão mais amplo de garantir que uma operação pode ser reexecutada com segurança.

## Benefícios do KISS

- **Menos bugs** — código simples é mais fácil de entender, manter e evoluir corretamente.
- **Menor custo de manutenção** e **entregas mais rápidas** — menos tempo para navegar e alterar o código.
- **Mais qualidade** — código simples de entender é mais simples de testar.
- **Maior retenção de usuário** (extensão para UX/front-end) — interfaces mais simples, que o usuário entende de imediato, têm maior propensão a mantê-lo usando o sistema.

## Relação com outros princípios

- **YAGNI** (You Aren't Gonna Need It) — complementar: não adicione o que não é necessário agora.
- **[[concepts/over-engineering]]** — KISS é o antídoto.
- **[[concepts/accidental-complexity]]** — KISS é a prática que previne complexidade acidental.
- **[[wiki/concepts/fazer-a-coisa-mais-simples-que-poderia-funcionar]]** — princípio irmão, de origem em XP: heurística mais específica de "primeira tentativa" ao escrever uma solução nova, enquanto KISS é a disciplina geral que vale em qualquer momento do design.

## Key Sources

- [[sources/overengineering-carol-ate-quinta]]
- [[wiki/sources/5-principios-que-mudaram-como-programador]]
- [[wiki/sources/kiss-yagni-entrega-rapida-qualidade]] — origem na Marinha dos EUA, KISS aplicado a testes, exemplo de refactor de validação de status, benefício de retenção de usuário via UX simples
