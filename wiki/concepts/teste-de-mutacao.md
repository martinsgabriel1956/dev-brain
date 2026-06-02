---
type: concept
title: "Teste de Mutação"
aliases: ["mutation testing", "testes de mutação", "mutation test"]
date_created: 2026-05-31
date_updated: 2026-05-31
source_count: 1
tags: [teste-de-mutacao, qualidade, testes, harness, cobertura]
skill: tech-mentor-backend
status: stable
---

# Teste de Mutação

## TL;DR

Técnica de validação de testes que modifica automaticamente o código de produção (introduz "mutantes" — pequenas alterações como trocar `>` por `>=`, inverter condições) e verifica se os testes existentes detectam essas mudanças. Se um mutante sobrevive, os testes não estão testando aquele comportamento de verdade.

## O Problema que Resolve

Code coverage alto não garante testes bons — garante apenas que as linhas foram executadas. É possível ter 90% de coverage e testes que não detectam bugs reais.

```python
# Código com bug
def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)  # deveria ser / 100

# Teste que "passa" mas não testa o bug
def test_desconto():
    resultado = calcular_desconto(100, 10)
    assert resultado is not None  # ← passa, mas não valida o valor correto
```

Mutation testing introduz o mutante `preco - (preco * percentual / 10)` e verifica se o teste detecta a diferença. Se o teste continua passando com o mutante, ele não está testando o valor calculado.

## Como Funciona

```
1. Ferramenta cria variações do código (mutantes)
   - Troca operador: > → >=
   - Inverte condição: if x → if !x
   - Remove linha de código
   - Troca constante: 0 → 1

2. Executa a suite de testes contra cada mutante

3. Resultado:
   - Mutante "morto" = testes detectaram a mudança ✅
   - Mutante "sobrevivente" = testes não cobrem aquele comportamento ❌

4. Mutation score = mortos / total de mutantes
```

## Ferramentas

| Linguagem | Ferramenta |
|-----------|-----------|
| JavaScript/TypeScript | Stryker |
| Python | Mutmut, Cosmic Ray |
| Java | PIT (Pitest) |
| Go | go-mutesting |
| Ruby | Mutant |

## Na Era da IA

Com a IA gerando testes em grande volume, mutation testing virou ainda mais importante: a IA consegue criar centenas de testes rapidamente, mas tende a criar testes que executam o código sem validar o comportamento. Mutation testing detecta essa superficialidade de forma automatizada.

> *"Você consegue com a harness ter um ferramental que roda de maneira determinística — não é o que a IA acha, é a ferramenta passou ou não passou."*

## Parte do [[harness-de-qualidade]]

Mutation testing é um componente do [[harness-de-qualidade]] e da [[pipeline-de-qualidade]]. Não substitui coverage — complementa: coverage diz "essa linha foi executada", mutation testing diz "essa linha foi testada de verdade".

## Key Sources

- [[wiki/sources/conteudo-tecnico-ia-robustez-sistemas]]
- [[wiki/sources/conteudo-tecnico-ia-hype-sistemas-robustos]]
