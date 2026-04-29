---
date: 2026-04-22
tags: [tech-mentor, carreira, logica, algoritmos, solid, java, iniciante]
skill: tech-mentor-leadership
level: iniciante
source: transcrição de vídeo (speaker brasileiro, canal de programação — Java/Eclipse)
---

# Lógica de Programação Sem Ser Gênio da Matemática

## Contexto

Vídeo direcionado a iniciantes que acreditam que programação exige habilidade matemática avançada. Duas dicas práticas demonstradas com código Java: (1) quebrar problemas em partes menores e (2) desenvolver pensamento algorítmico.

---

## Dica 1 — Quebrar Problemas em Partes Menores

O segredo é se perguntar: **qual é o objetivo final e como posso chegar lá passo a passo?**

### Exercício prático: Caixa Eletrônico

Dado um valor de saque, mostrar quantas notas de cada denominação serão entregues.

**Decomposição em passos:**

```
Passo 1: Receber o valor do saque (Scanner)
Passo 2: Definir as notas disponíveis (ex: 100, 50, 20, 5, 2)
Passo 3: Calcular a quantidade de cada nota
Passo 4: Exibir o resultado
```

**Código inicial (tudo no main):**

```java
Scanner scanner = new Scanner(System.in);
System.out.println("Digite o valor do saque:");
int valor = scanner.nextInt();

int[] notas = {100, 50, 20, 5, 2};
int[] quantidadeNotas = new int[notas.length];

for (int i = 0; i < notas.length; i++) {
    if (valor >= notas[i]) {
        quantidadeNotas[i] = valor / notas[i];
        valor = valor % notas[i];
    }
}

System.out.println("Notas fornecidas:");
for (int i = 0; i < notas.length; i++) {
    if (quantidadeNotas[i] > 0) {
        System.out.println(quantidadeNotas[i] + " nota(s) de " + notas[i]);
    }
}

scanner.close();
```

**Exemplos:**
- Saque 200 → 2 notas de 100
- Saque 320 → 3 notas de 100, 1 nota de 20

---

## Dica 2 — Aplicar Single Responsibility (SOLID) nos Métodos

Após quebrar em passos, transformar cada passo em um método com responsabilidade única. Benefício: quando algo falha, você sabe exatamente onde está o problema.

**Refatoração com métodos:**

```java
public static int obterValorSaque(Scanner scanner) {
    System.out.println("Digite o valor do saque:");
    return scanner.nextInt();
}

public static int[] calcularNotas(int valor, int[] notas) {
    int[] quantidadeNotas = new int[notas.length];
    for (int i = 0; i < notas.length; i++) {
        if (valor >= notas[i]) {
            quantidadeNotas[i] = valor / notas[i];
            valor = valor % notas[i];
        }
    }
    return quantidadeNotas;
}

public static void exibirNotas(int[] notas, int[] quantidadeNotas) {
    System.out.println("Notas fornecidas:");
    for (int i = 0; i < notas.length; i++) {
        if (quantidadeNotas[i] > 0) {
            System.out.println(quantidadeNotas[i] + " nota(s) de " + notas[i]);
        }
    }
}

// main:
int valor = obterValorSaque(scanner);
int[] notas = {100, 50, 20, 5, 2};
int[] quantidadeNotas = calcularNotas(valor, notas);
exibirNotas(notas, quantidadeNotas);
```

**Vantagem do Outline (IDE):** com métodos separados, o outline da IDE lista todos os métodos — em classes com centenas de linhas, isso é essencial para navegar.

---

## Dica 3 — Desenvolver Pensamento Algorítmico

Bons programadores não decoram código — entendem a lógica por trás do problema e criam a própria solução.

**Como desenvolver:**
- Praticar e exercitar constantemente — "programação é igual à matemática: quanto mais você exercita, melhor fica"
- **Explicar o código para outra pessoa** (amigo, cônjuge, filho) — explicar em voz alta melhora o raciocínio lógico mais do que ler código sozinho
- Resolver exercícios novos sem copiar solução pronta — desenvolver a solução a partir do entendimento do problema

---

## Sobre Matemática e Programação

Programação exige:
- Raciocínio lógico
- Pensamento estruturado
- Matemática básica (divisão inteira, resto — como no exercício acima)

**Não exige** resolver equações complexas no dia a dia — exceto em domínios específicos (ex: software fiscal/contábil, onde cálculos de ICMS, SPED, nota fiscal exigem conhecimento do domínio contábil).

---

## Conceitos Relacionados

[[aprendizado-deliberado]] · [[postura-de-programador]] · [[atomic-commits]] · [[definicao-de-pronto]]
