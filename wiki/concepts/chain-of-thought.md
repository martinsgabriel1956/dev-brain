---
type: concept
title: "Chain-of-Thought"
aliases: ["CoT", "chain of thought", "raciocínio passo a passo"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_count: 2
tags: [llm, prompt-engineering, raciocínio, chain-of-thought, cot, emergent-ability]
skill: tech-mentor-ai
status: stable
---

# Chain-of-Thought (CoT)

## Definição

Técnica de [[prompt-engineering]] que induz o modelo a externalizar o raciocínio intermediário antes de produzir a resposta final. Formalizada em [[wiki/sources/chain-of-thought-prompting]] (Wei et al., 2022), é uma [[emergent-ability]] de modelos com ~100B+ parâmetros: não beneficia modelos menores e pode até piorar a performance deles.

## Como Ativar

**Implícito:** adicionar "Pense passo a passo" / "Let's think step by step" ao final do prompt. Funciona em modelos capazes (GPT-3.5+).

**Explícito:** estruturar os passos de raciocínio esperados diretamente no prompt:

```
Resolva o problema abaixo.

Pense passo a passo:
1. Identifique os dados disponíveis
2. Determine a operação necessária
3. Execute o cálculo
4. Verifique a resposta

Problema: [...]
```

**Few-shot CoT (mais poderoso):** fornecer exemplares completos `input → passos de raciocínio → output` no prompt. Wei et al. usaram 8 exemplares e superaram GPT-3 fine-tuned com verificador no GSM8K.

## Resultados Empíricos (Wei et al., 2022)

| Domínio | Resultado com PaLM 540B + CoT |
|---|---|
| Aritmético (GSM8K) | ~57% — supera fine-tuned GPT-3 (~35%) |
| Senso comum | Melhora ou iguala SOTA em 5 benchmarks |
| Simbólico (OOD) | Única técnica que generaliza para sequências mais longas |

## Quando Usar

- Problemas de matemática ou lógica multi-step
- Raciocínio causal ou contrafactual
- Tarefas onde "adivinhar" a resposta diretamente falha sistematicamente
- **Apenas com modelos ~100B+** — em modelos menores, CoT gera cadeias fluentes mas ilógicas

## Quando CoT Gera Maior Ganho

1. Tarefa desafiadora com múltiplos passos
2. Curva de escala do standard prompting é plana (pouca melhora com mais parâmetros)
3. Modelo grande disponível

## Limites

- **Propriedade emergente:** não funciona em modelos pequenos
- Aumenta tokens gerados (custo e latência maiores)
- Não garante raciocínio correto — "hallucinated reasoning" (cadeias plausíveis mas erradas)
- Para tarefas simples (1–2 etapas), CoT é overhead desnecessário

## O que NÃO Funciona (ablações)

- **Só a equação:** gerar equação matemática sem linguagem natural não ajuda em problemas complexos
- **Tokens extras vazios:** mais tokens sem conteúdo não produz melhora — é o conteúdo que importa
- **Raciocínio depois da resposta:** a cadeia de pensamento deve preceder a resposta final

## Relação com Técnicas Avançadas

- **Self-Consistency** — gerar múltiplas chains e agregar pelo voto majoritário
- **Tree of Thoughts** — explorar múltiplos caminhos de raciocínio em paralelo
- **Reasoning Models (o1/o3)** — CoT internalizado no próprio treinamento do modelo

## Fontes

- [[wiki/sources/chain-of-thought-prompting]]
- [[wiki/sources/microsoft-prompt-engineering-guide]]
