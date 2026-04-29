---
type: concept
title: "Decomposição de Problemas"
aliases: ["problem decomposition", "quebrar problemas", "dividir para conquistar", "passos menores"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [logica, algoritmos, solid, iniciante, pensamento-computacional]
skill: tech-mentor-leadership
status: stable
---

# Decomposição de Problemas

Técnica central de lógica de programação: dividir um problema complexo em passos menores e sequenciais, depois implementar cada passo isoladamente. É o oposto de tentar resolver tudo de uma vez.

## Processo

```
1. Identificar o objetivo final
2. Perguntar: quais são as etapas necessárias para chegar lá?
3. Escrever os passos em linguagem natural antes de codificar
4. Implementar passo a passo — validar cada um antes do próximo
```

## Exemplo — Caixa Eletrônico (Java)

**Problema:** dado valor de saque, retornar quantidade de notas por denominação.

```java
// Passo 1: entrada
Scanner scanner = new Scanner(System.in);
int valor = scanner.nextInt();

// Passo 2: denominações
int[] notas = {100, 50, 20, 5, 2};

// Passo 3: cálculo (divisão inteira + módulo)
int[] qtd = new int[notas.length];
for (int i = 0; i < notas.length; i++) {
    if (valor >= notas[i]) {
        qtd[i] = valor / notas[i];
        valor = valor % notas[i];
    }
}

// Passo 4: exibição
for (int i = 0; i < notas.length; i++) {
    if (qtd[i] > 0)
        System.out.println(qtd[i] + " nota(s) de " + notas[i]);
}
```

## Aplicar SRP Após Decomposição

Depois de identificar os passos, cada passo vira um método com responsabilidade única:

```java
public static int obterValorSaque(Scanner scanner) { ... }
public static int[] calcularNotas(int valor, int[] notas) { ... }
public static void exibirNotas(int[] notas, int[] qtd) { ... }
```

**Benefício:** quando algo falha, o stack trace aponta para o método responsável — não para um main monolítico de 80 linhas.

## Relação com Outros Conceitos

- Aplica [[concepts/aprendizado-deliberado]] na prática: cada passo é um exercício isolado
- Prepara terreno para OO/DDD: métodos → classes → use cases
- Matemática necessária é básica — divisão inteira e módulo, não cálculo

## Key Sources

- [[sources/logica-programacao-sem-matematica]]
