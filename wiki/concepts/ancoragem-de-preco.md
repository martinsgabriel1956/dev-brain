---
type: concept
title: "Ancoragem de Preço"
aliases: ["price anchoring", "ancoragem de valor", "efeito de ancoragem", "anchoring", "decoy premium"]
date_created: 2026-08-11
date_updated: 2026-08-11
source_count: 1
tags: [precificacao, negocio, psicologia-de-preco, posicionamento, mercado-de-ia, freelance]
skill: tech-mentor-ai
status: stub
---

# Ancoragem de Preço

**Ancoragem de preço** (*price anchoring*) é o viés cognitivo de usar um primeiro número (a "âncora") como referência para julgar todos os preços seguintes. Na prática de vendas, você apresenta deliberadamente uma **oferta premium cara** — que não precisa vender em volume — para fazer o produto que você **realmente quer vender** parecer barato por comparação.

## O caso Anthropic (Opus 5)

[[wiki/sources/precificacao-ancoragem-anthropic-opus-5-lancamento]] usa o lançamento do **Opus 5** da [[wiki/entities/anthropic]] como estudo de caso:

- O **Fable** é a âncora premium (percepção de valor altíssima, preço altíssimo).
- Ao **ancorar o Opus ao Fable** — e não ao Sonnet — o Opus "parece barato" (uma pechincha), mesmo custando mais que o dobro do Sonnet.
- Preços de saída narrados no vídeo: Fable ~10,50 e Opus ~5,25 por milhão de tokens (aproximação, sem link primário).
- A tese: **a Anthropic não quer vender o Fable — quer vender o Opus.** O Fable existe para reposicionar o Opus como "o novo [[wiki/concepts/modelo-frontier|Sonnet]]" (o modelo do dia a dia).

## A analogia do iPhone Pro Max

O mecanismo é o mesmo do topo de linha da Apple: a maioria não precisa do iPhone Pro Max, e poucos o compram — mas sua existência faz o cliente pagar **confortavelmente** um valor mais alto no modelo do meio. O item premium é um *decoy* (isca de comparação), não a meta de volume.

## Por que a ancoragem foi necessária: pressão competitiva

A ancoragem não teria função sem [[wiki/concepts/corrida-preco-qualidade-llm|concorrência de preço]]. O mid-tier vinha sendo pressionado por baixo pelo [[wiki/entities/moonshot-ai|Kimi K3]] (US$ 0,92 vs US$ 2,13 do Fable numa mesma task do Cline) e pelo [[wiki/entities/xai|Grok 4.5]] — ambos mais baratos que o Opus. Ancorar o Opus ao Fable defende a margem do mid sem entrar numa guerra direta de preço.

## Como aplicar em serviços/produtos (a lição para o dev)

1. Defina o que você **realmente quer vender** (o "Opus").
2. Crie uma **oferta premium** acima dela (o "Fable") — cara, completa, que não precisa vender muito.
3. Apresente as duas juntas: a âncora reposiciona a oferta-alvo como escolha "razoável".

**Ressalva da fonte:** a ancoragem só funciona porque há **produto e competência técnica reais** por trás. Vender por percepção de valor sem entregar resultado ("só com lábia") deixou de funcionar — o mercado cobra resultado. Ver [[wiki/concepts/visao-de-negocio-do-desenvolvedor]] e [[wiki/concepts/dev-e-negocio]].

## Conceitos relacionados

- [[wiki/concepts/corrida-preco-qualidade-llm]] — o contexto de mercado que motiva a jogada.
- [[wiki/concepts/surge-pricing]] — outro padrão de precificação (por demanda dinâmica).
- [[wiki/concepts/ltv-cac]] — quando a decisão de preço precisa fechar unit economics.
- [[wiki/concepts/freelance-como-alavanca-de-renda]] — o público que a fonte quer ensinar a precificar.

## Key Sources

- [[wiki/sources/precificacao-ancoragem-anthropic-opus-5-lancamento]] — único source até o momento.
