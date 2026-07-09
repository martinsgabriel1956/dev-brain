---
title: "Como um Compilador Transforma Código em Instruções de Máquina"
source_url: ""
author: "desconhecido (canal YouTube)"
date_published: "desconhecido"
date_ingested: 2026-07-09
type: transcript
language: pt-BR
tags: [compiladores, lexing, parsing, ast, analise-semantica, ir, otimizacao, geracao-de-codigo, interpretadores, jit]
---

# Como um Compilador Transforma Código em Instruções de Máquina

Seis tokens de código, duas instruções de máquina: algo transformou um no outro, e não foi uma tradução simples. Foram seis etapas. Isso é o que um compilador faz, e este texto mostra cada uma dessas etapas.

Um compilador é um pipeline: cada estágio pega a saída do anterior, transforma e passa pro próximo. As seis etapas principais são: análise léxica, análise sintática, análise semântica, representação intermediária, otimização e geração de código. Parece muita coisa, mas cada etapa resolve um problema bem definido.

## 1. Análise léxica (lexing)

O compilador recebe um arquivo de texto e a primeira coisa que ele faz é quebrar esse texto em pedaços. Análise léxica, ou *lexing*, é o primeiro estágio: o compilador lê o texto caractere por caractere e agrupa em **tokens**.

Não confunda esses tokens com tokens de inteligência artificial. Aqui, token é cada pedaço de código que o compilador reconhece. Por exemplo, em `int result = a + b * 2;`:

- `int` é uma *keyword*
- `result` é um identificador
- `=` é um operador
- `a` e `b` são identificadores
- `+` e `*` são operadores
- `2` é um literal numérico
- `;` encerra a declaração

Pensa no *lexer* como alguém lendo uma frase e separando cada palavra e pontuação: não precisa entender o significado, só precisa saber onde começa e termina cada pedaço e de que tipo é. Algumas coisas são descartadas, como espaços em branco e comentários. O lexer produz uma lista limpa de tokens.

Mas uma lista de tokens não diz nada sobre a estrutura do programa: `a + b * 2` é "a + b, tudo entre parênteses, vezes 2" ou "a + (b * 2)"? Para resolver isso, precisamos da próxima etapa.

## 2. Análise sintática (parsing)

A análise sintática, ou *parsing*, transforma a lista de tokens numa árvore — uma estrutura de dados hierárquica chamada **AST** (Abstract Syntax Tree).

Esse padrão não é exclusivo de compiladores: bancos de dados fazem a mesma coisa com SQL. O texto vira tokens, tokens viram árvore, e a árvore é otimizada num plano de execução.

No exemplo `a + b * 2`, o *parser* sabe que multiplicação tem precedência sobre soma, então `b * 2` fica agrupado primeiro. A árvore mostra isso claramente: o nó `+` tem dois filhos, `a` de um lado e `b * 2` do outro.

Cada estrutura da linguagem tem uma forma na árvore: um `if` vira um nó com condição e corpo; um laço de repetição vira um nó com condição e corpo de repetição; uma chamada de função vira um nó com nome e argumentos.

Quando a estrutura está errada — por exemplo `x = ;` — não faz sentido: tem o `=` mas não tem valor. O *parser* não vai conseguir montar a árvore e vai reportar um **erro de sintaxe**. Esse é aquele erro vermelho no editor antes mesmo de compilar: o parser já sabe que a estrutura está quebrada.

Mas a árvore só garante que a estrutura está correta, não garante que faz sentido.

## 3. Análise semântica

`int x = "hello";` tem sintaxe perfeita — declaração de variável com tipo, nome e valor — mas faz sentido atribuir uma string a um inteiro? A análise semântica é o estágio que verifica se o programa tem significado válido:

- Tipos são compatíveis
- Variáveis foram declaradas antes de usar
- Funções que você chama existem
- O número de argumentos está correto

Uma das tarefas mais importantes é a **resolução de nomes**. Quando o compilador vê `a` numa segunda linha, ele precisa saber qual `a`, onde foi declarada, qual o tipo. Ele consulta uma **tabela de símbolos**, uma estrutura que mapeia cada nome ao que ele representa: nome `a`, tipo `int`, escopo local, posição na *stack*.

Essa tabela é construída conforme o compilador percorre a AST: cada declaração adiciona uma entrada, cada uso busca na tabela.

Depois da análise semântica, o compilador tem certeza de que o programa é válido: a estrutura está correta, os tipos batem, os nomes existem. Agora ele precisa transformar isso em algo mais perto da máquina, mas ainda não em código de máquina direto.

## 4. Representação intermediária (IR)

Antes de gerar o código de máquina, o compilador converte a AST numa **representação intermediária**, ou **IR**.

Por que não ir direto para código de máquina? Porque existem muitas linguagens e muitas arquiteturas de processador. Com IR, cada linguagem traduz para IR e cada arquitetura traduz do IR — evitando combinações N×M.

A IR é mais simples que o código original: cada instrução faz uma operação. `a + b * 2` vira três instruções:

1. multiplica `b` por `2`, guarda no temporário
2. soma `a` com esse temporário
3. guarda no resultado

Sem precedência de operadores, sem expressões compostas — cada passo é explícito. É nessa forma simples que o compilador consegue fazer algo muito importante: a otimização.

## 5. Otimização

O compilador olha pro código e encontra formas de torná-lo mais rápido sem mudar o resultado.

- **Constant folding**: se o compilador vê `2 + 3`, ele sabe que o resultado é sempre `5`. Por que calcular em tempo de execução algo que já se sabe em tempo de compilação? Então `2 + 3` é substituído por `5` direto.
- **Dead code elimination**: código que nunca executa é removido. Um `if false` com um bloco inteiro dentro — o compilador descarta tudo e nada vai pro binário.
- **Loop unrolling**: se um loop tem quatro iterações, o compilador pode desenrolar e escrever as quatro operações em sequência, sem o overhead de checar a condição e incrementar o contador a cada volta.
- **Function inlining**: para funções pequenas que são chamadas muitas vezes, o compilador copia o corpo da função direto no ponto de chamada, eliminando o custo de empilhar e desempilhar o *stack frame*.

Esses são só alguns exemplos — compiladores modernos fazem centenas de otimizações. O resultado é que o código legível que você escreveu roda tão rápido quanto código otimizado à mão, às vezes até mais rápido, porque o compilador enxerga otimizações que humanos não enxergam.

Mas o código otimizado ainda é IR. Falta o último passo.

## 6. Geração de código

O último estágio é a geração de código: cada instrução da IR é traduzida para instruções de máquina da arquitetura alvo.

- `t1 = b * 2` vira um `imul` no x86
- `t2 = a + t1` vira um `add`
- `result = t2` vira um `move` para um registrador ou posição de memória

Aqui entra um dos problemas mais difíceis: a **alocação de registradores**. A CPU tem um número limitado de registradores — são poucos, mas muito rápidos. O compilador precisa decidir quais variáveis ficam em registradores e quais vão para a memória. Se uma variável é usada em loop, ela fica no registrador; se é usada uma vez e nunca mais, pode ir para a *stack*.

O assembly passa pelo *assembler*, que traduz cada instrução para bytes. Depois o *linker* junta o código com bibliotecas externas, resolve referências e gera o executável final — o arquivo que você clica duas vezes para rodar.

## Resumo do pipeline (exemplo completo)

Para a função `int square(int x) { return x * x; }`:

1. **Análise léxica**: quebra em tokens — `int`, `square`, `(`, `int`, `x`, `)`, `{`, `return`, `x`, `*`, `x`, `;`, `}`
2. **Análise sintática**: monta a árvore — nó *function declaration* com nome `square`, parâmetro `x` do tipo `int`, corpo com `return x * x`
3. **Análise semântica**: verifica os tipos — `x` é `int`, `x` é `int`, o retorno bate com a declaração, tudo certo
4. **IR**: `t1 = x * x`; `return t1`
5. **Otimização**: como a função é pequena, provavelmente é *inlined* nos pontos de chamada
6. **Geração de código**: assembly — `imul`, instruções de máquina

De seis tokens de código, saíram duas instruções de máquina. Esse é o trabalho do compilador. Mas esse não é o único jeito de transformar código em execução.

## Compilador vs. interpretador

A diferença é que o compilador traduz o programa inteiro antes de executar — você compila uma vez e roda quantas vezes quiser. O interpretador traduz e executa junto, linha por linha, em tempo real.

Comparação: o compilado demora para compilar, mas executa rápido. O interpretado começa instantaneamente, mas cada execução é mais lenta.

Também existe o meio-termo. O Java, por exemplo, compila para *bytecode* que roda na JVM. A JVM interpreta, mas quando detecta código que roda muitas vezes, ela compila para código nativo — isso é o **JIT** (*just-in-time compilation*). O JavaScript faz algo parecido: o V8 começa interpretando e, quando detecta um *hot path*, compila para nativo em tempo de execução.

A diferença entre compilador e interpretador é cada vez mais difícil de traçar — a maioria das linguagens modernas usa os dois.

## Por que isso importa no dia a dia

Entender o pipeline de um compilador muda como você lê os erros:

- **Erro de sintaxe**: o parser não conseguiu montar a árvore — faltou um parêntese, um ponto e vírgula, uma chave.
- **Erro de tipo**: a análise semântica encontrou incompatibilidade — você pode ter passado uma string onde era esperado um número.
- **Variável undefined**: a tabela de símbolos não encontrou o nome.

E se você trabalha com JavaScript, você usa compiladores o tempo todo sem perceber:

- O **TypeScript** compila para JavaScript.
- O **Babel** transpila sintaxe nova para navegadores antigos.
- O **Webpack** resolve módulos e gera *bundles*.

São todos compiladores: fazem análise léxica, sintática, semântica, transformação e geram um output. O pipeline é o mesmo.

## Resumo

- **Análise léxica**: quebra o texto em tokens — keywords, identificadores, operadores, literais.
- **Análise sintática**: monta uma árvore (AST) que representa a estrutura do programa.
- **Análise semântica**: verifica se o programa faz sentido — tipos, nomes e escopos.
- **Representação intermediária (IR)**: simplifica a árvore em instruções básicas, independentes de arquitetura.
- **Otimização**: transforma código legível em código rápido — *constant folding*, *dead code elimination*, *inlining*, entre outras.
- **Geração de código**: traduz para instruções de máquina da arquitetura alvo.

Esse processo, que muitas vezes leva milissegundos, é uma das criações mais interessantes da ciência da computação.
