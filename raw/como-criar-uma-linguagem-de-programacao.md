---
title: "Como Criar uma Linguagem de Programação"
source_url: ""
author: "desconhecido (canal YouTube)"
date_published: "desconhecido"
date_ingested: 2026-07-09
type: transcript
language: pt-BR
tags: [linguagens-de-programacao, compiladores, interpretadores, parsers, sistema-de-tipos, runtime, garbage-collector, bytecode, llvm]
---

# Como Criar uma Linguagem de Programação

Imagina abrir um arquivo vazio, escrever duas linhas e o computador entender: ele cria uma variável, monta a frase e printa "Hello World". Não parece muita coisa, mas se isso rodar de verdade, você acabou de inventar uma mini linguagem de programação. Porque por trás dessas duas linhas tem um monte de perguntas escondidas: quais keywords existem, que ordem elas podem ter, o que é erro, o que é número, o que é texto, como isso vira execução.

Criar uma linguagem é responder essas perguntas uma por uma.

## 1. Propósito

Toda linguagem nasce tentando resolver um problema. O C dá controle total sobre o hardware. Python prioriza a produtividade. SQL existe para consultar dados. Antes de escrever uma linha de código, você precisa responder uma pergunta: qual problema a minha linguagem resolve melhor do que as opções que já existem?

A partir dessa resposta surgem as decisões de design:

- Vai priorizar controle total ou facilidade de uso?
- Tipagem estática ou dinâmica?
- Compilada ou interpretada?
- Gerenciamento de memória manual ou com garbage collector?

Cada escolha tem consequências. Se você quer performance máxima, tipagem estática e compilação antecipada costumam ajudar. Se quer prototipagem rápida, tipagem dinâmica e interpretação podem fazer mais sentido.

Olha algumas linguagens mais recentes: o Rust colocou segurança de memória como core da linguagem sem depender de garbage collector. O Go simplificou a concorrência. O Elixir trouxe a tolerância a falhas da máquina virtual do Erlang para uma sintaxe mais moderna. Nenhuma começou tentando ser boa em tudo — cada uma escolheu um nicho e focou nele.

## 2. Gramática

Com o problema definido, você precisa definir as regras da linguagem. Toda linguagem tem uma gramática. No português, uma frase pode seguir uma estrutura como sujeito, verbo e objeto. Numa linguagem de programação, uma declaração de variável também precisa seguir uma forma esperada: uma palavra-chave, um nome e um valor.

Essas regras podem ser definidas formalmente usando o **EBNF** (Extended Backus-Naur Form), uma notação para descrever a estrutura da linguagem. Funciona assim:

- Um *statement* (instrução) pode ser uma atribuição ou um "mostre".
- Uma atribuição é a palavra-chave `variável`, seguida de um identificador, depois um sinal de igual e depois uma expressão.
- Uma expressão pode ser um número, uma string, um identificador ou uma expressão com operador.

Isso pode parecer simples, mas essas poucas regras já permitem coisas como `variável x = 1 + 2` ou `variável nome = "João"`.

A gramática funciona como uma receita: para saber se um trecho de código é válido, o parser tenta derivar esse código a partir das regras. Se ele conseguir, a estrutura faz sentido; se não, é erro de sintaxe.

Aqui entra um problema importante: a **ambiguidade**. `1 + 2 * 3` pode ter duas leituras possíveis se a gramática não for cuidadosa. A linguagem precisa definir sem ambiguidade qual leitura vale — para isso existem as regras de **precedência** e **associatividade**. A multiplicação tem precedência maior que a soma, então `2 * 3` agrupa primeiro. Essas decisões parecem pequenas, mas definem como todo código na sua linguagem vai ser interpretado.

## 3. Lexer e Parser (Front End)

Com a gramática definida, agora você precisa de algo que leia o código e aplique essas regras.

O primeiro passo é o **lexer**, também chamado de analisador léxico. Ele lê o texto caractere por caractere e agrupa tudo em *tokens*: `variável` vira uma palavra-chave, `nome` vira um identificador, `=` vira um operador.

Em seguida, o **parser** (analisador sintático) pega esses tokens e monta uma árvore: a **AST** (Abstract Syntax Tree, ou árvore de sintaxe abstrata). O nó raiz pode ser uma atribuição, o lado esquerdo é o nome `x`, o lado direito é uma expressão de soma com `10` e `20`.

Na prática, você tem duas opções para construir o parser:

1. **Escrever à mão, usando descida recursiva** — você cria uma função para cada regra da gramática. Isso te dá mais controle, mas também dá mais trabalho.
2. **Usar um gerador de parser**, como uma gramática **PEG** (Parsing Expression Grammar) — você descreve as regras e a ferramenta gera boa parte do parser automaticamente.

Por isso muitos compiladores importantes acabam usando parsers escritos à mão: o Go tem um parser próprio, o Rust também, e o TypeScript faz a mesma coisa, porque a sintaxe dele precisa lidar com JavaScript, tipos, JSX e mensagens de erro úteis pro editor.

## 4. Sistema de Tipos

Com o front end pronto, a AST vai representar a estrutura do código — mas a estrutura não é tudo. `x` é um número, `y` é uma string. O que acontece quando você soma os dois depende da linguagem:

- O JavaScript, por exemplo, converte o número pra string e concatena.
- O Python lança um erro em tempo de execução.
- Numa linguagem estaticamente tipada como Rust, algo equivalente nem passa pela compilação.

Quem decide isso é o **sistema de tipos**. A primeira decisão é *quando* verificar os tipos:

- **Tipagem estática** verifica em tempo de compilação, ou seja, antes do código rodar — o compilador consegue avisar se você tá somando tipos incompatíveis.
- **Tipagem dinâmica** verifica em tempo de execução — o código roda e, se encontrar uma operação inválida, lança um erro na hora.

O estático pega muitos erros mais cedo e ajuda o editor a oferecer um autocomplete melhor. O custo é que às vezes você precisa escrever mais informação no código: declarar o tipo de um parâmetro, explicar um genérico, ou tratar um valor nulo antes de usar. O dinâmico é mais flexível e costuma ser mais rápido para escrever, mas certos erros só aparecem quando o código passa por aquele caminho — e às vezes isso acontece em produção.

Existe um meio-termo importante: **inferência de tipos**. Linguagens como TypeScript e Rust deduzem muitos tipos sem você declarar tudo manualmente — `let x = 42` e o compilador já sabe que é número. Você mantém boa parte da segurança da tipagem estática com menos verbosidade.

O sistema de tipos é muito mais do que número ou string: uma função pode retornar valores de tipos diferentes, variáveis podem mudar de tipo, como genéricos funcionam, como a linguagem representa a ausência de valor. Cada uma dessas decisões muda bastante como a linguagem funciona na prática.

## 5. Execução

Com a estrutura e os tipos validados, falta a parte mais concreta: como executar o código. Você tem a AST, o sistema de tipos validou tudo — agora como transformar essa árvore em ação? Existem três caminhos comuns.

### Interpretador direto

Você percorre a AST nó por nó e executa na hora. Encontrou um nó de soma, faz a soma; encontrou um nó de print, imprime. É um dos jeitos mais simples de implementar — muitas linguagens começam com uma versão assim porque ela deixa o foco na semântica da linguagem. O problema é que percorrer uma árvore costuma ser lento: cada nó pode estar em um lugar diferente da memória, e pular entre objetos atrapalha bastante o cache do processador.

### Compilar para código de máquina nativo

A AST vira **IR** (representação intermediária), que facilita a otimização. Algumas linguagens, como C, C++ e Rust, fazem isso — o código roda direto no processador, sem uma VM no meio. Esse costuma ser o caminho mais rápido, mas também é o mais difícil de implementar: você precisa lidar com registradores, alocação de memória e gerar instruções para cada arquitetura de CPU.

### Bytecode + máquina virtual (meio-termo)

Aparece em muitas linguagens modernas. Você compila a AST para **bytecode**, uma lista de instruções simples para uma máquina virtual. Exemplo de bytecode para `mostre 10 + 20`:

```
LOAD_CONST 10
LOAD_CONST 20
ADD
PRINT
```

Geralmente é mais rápido que percorrer a AST, porque o bytecode é sequencial e compacto, e é mais fácil de implementar do que um compilador nativo completo. O Java compila para bytecode da JVM, o Python compila para bytecode do CPython, o Lua compila para bytecode da Lua VM.

Muitas VMs modernas adicionam **JIT** (just-in-time compilation, ou compilação em tempo de execução): a VM identifica as partes do código que mais executam e compila essas partes para código nativo enquanto o programa roda.

## 6. Gerenciamento de Memória

Com o modelo de execução definido, resta a próxima questão: quem gerencia a memória? Toda variável que você cria ocupa memória, e essa memória precisa ser liberada quando não é mais necessária.

- **Abordagem manual**: o programador aloca e libera memória explicitamente. É o que o C faz, com `malloc`/`free`. Dá controle total pra pessoa, mas um erro pode causar vazamento de memória ou acesso à memória já liberada.
- **Garbage Collector**: o runtime monitora quais objetos ainda estão sendo usados e libera os que não estão. Linguagens como Java, Go, Python e JavaScript fazem isso. É mais seguro pra maioria dos programas, mas tem custo — dependendo do coletor, o garbage collector pode pausar o programa por um tempo para limpar a memória.
- **Ownership (Rust)**: cada valor tem um dono. Quando o dono sai do escopo, a memória é liberada. Não tem garbage collector e não tem `free` manual espalhado pelo código — o compilador verifica essas regras em tempo de compilação.

Além da memória, o runtime também define como a linguagem lida com **concorrência**: threads (Java), event loop (JavaScript), goroutines (Go). Cada modelo tem tradeoffs de complexidade, performance e segurança — e essa decisão é difícil de mudar depois, porque o código que os usuários escrevem vai se apoiar nela.

## 7. Standard Library e Ecossistema

O runtime é como se fosse o motor invisível da linguagem, mas sem boas ferramentas fica difícil convencer alguém a usar. Ninguém vai querer escrever uma função para ler arquivo do zero toda vez que começa um projeto.

A **standard library** é o que vem incluído na linguagem, e o que você escolhe incluir define como as pessoas vão usar a sua linguagem:

- O Python tem uma standard library grande — por isso chamam de "batteries included": requisição HTTP, regex, parsing de CSV, tá tudo lá.
- O Go também tem uma standard library enxuta e prática: servidor HTTP, JSON, crypto, testes — tudo que você precisa para construir um serviço web sem dependência externa.

Essa decisão afeta um ponto importante: o **ecossistema** da linguagem. A linguagem pode ser muito boa, mas se não tem como instalar bibliotecas, pouca gente vai apostar nela. O *package manager* hoje em dia é quase obrigatório: npm (JavaScript), pip ou uv (Python), Cargo (Rust).

Além do gerenciador de pacotes, ferramentas como formatter, linter e debugger fazem diferença enorme na experiência do dia a dia. O Go, por exemplo, acertou nisso desde o começo: `gofmt` formata todo o código Go do mesmo jeito, `go test` roda testes sem framework externo, `go build` compila sem makefile.

Uma das ferramentas mais importantes hoje é o **LSP** (Language Server Protocol), criado pela Microsoft, que permite que vários editores se conectem ao servidor da sua linguagem. É por ele que você ganha autocomplete, erros inline, "ir para definição" e refatoração. Com LSP, sua linguagem pode funcionar bem no VS Code, no Neovim, no IntelliJ e em vários outros editores.

Mas nenhuma ferramenta vai substituir a **comunidade**: pessoas escrevendo bibliotecas, respondendo perguntas, reportando bugs. Uma linguagem só vai sobreviver quando existe gente suficiente usando, ensinando e melhorando o ecossistema.

## Próximos Passos para Quem Quer Aprender

Todos esses passos já dão uma linguagem funcional. Talvez ainda não seja uma linguagem para usar em produção, mas já é uma linguagem que roda código de verdade. Para quem quer aprender, não precisa começar do zero:

- **Crafting Interpreters**, de Robert Nystrom — gratuito e online. Guia passo a passo a construção de duas implementações completas de uma linguagem chamada **Lox**: primeiro um interpretador em Java, depois uma VM com bytecode em C.
- **Dragon Book** — o livro mais famoso de compiladores, para quem quer ir mais a fundo na teoria.
- **LLVM** como backend, para quem quer construir um compilador mais robusto: você gera IR para o LLVM e ele cuida de muita parte da otimização e da geração de código para várias arquiteturas. Rust, Swift e várias outras linguagens fazem algo nessa linha.

Mesmo que você nunca crie uma linguagem de verdade, esse processo te obriga a entender como o código vira execução — e isso muda como você programa em qualquer linguagem.
