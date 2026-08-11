---
type: concept
title: "Teste de Mutação"
aliases: ["mutation testing", "testes de mutação", "mutation test"]
date_created: 2026-05-31
date_updated: 2026-08-11
source_count: 4
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

## Mutation Testing na Lista de Uncle Bob Para "Não Precisar Ler Código"

[[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] cita mutation testing como um dos itens concretos que [[wiki/entities/uncle-bob]] usa no lugar de ler código gerado por agentes. O papel específico que a fonte atribui a essa técnica na lista (junto com teste unitário, cobertura, Gherkin/BDD e métrica de qualidade): pega a variação — se o código está otimizado só para um caminho feliz (RPF — "requisito, parâmetro, formato" citado pela fonte) ou se de fato suporta mudanças de parâmetro. É o item que cobertura sozinha não pega, reforçando a distinção já registrada acima entre "linha executada" e "linha testada de verdade".

## Exemplo Numérico Concreto com `mutmut` e Metas de Gate

[[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]] dá um exemplo numérico do ciclo descrito acima: de 400 mutações geradas pela ferramenta `mutmut` (Python, `pip install mutmut`), 50 sobrevivem — essas 50 sobreviventes são, na prática, o próximo sprint de testes a escrever, não um relatório para arquivar. A fonte cita como meta de exemplo para gate de CI 85% de cobertura combinado com 60% de mutation score — os dois números juntos, não isolados, ecoando a mesma razão pela qual [[wiki/entities/uncle-bob]] cita cobertura e mutation testing lado a lado: cobertura sozinha não distingue "linha executada" de "linha testada de verdade".

## Key Sources

- [[wiki/sources/conteudo-tecnico-ia-robustez-sistemas]]
- [[wiki/sources/conteudo-tecnico-ia-hype-sistemas-robustos]]
- [[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] — mutation testing como um dos cinco pilares do harness que Uncle Bob usa em vez de ler código
- [[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]] — exemplo numérico com `mutmut` (400 mutações, 50 sobreviventes) e meta de gate combinando cobertura + mutation score
- [[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]] — mutation testing entre as métricas objetivas que sustentam não ler o código, com a ressalva de que métrica verde dá probabilidade, não garantia
