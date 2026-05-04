# Como Múltiplas Linguagens Vivem Num Único Binário

**Canal:** Core Dumped (George)  
**Patrocinador:** Let's Get Rusty  
**Tema:** Conceitos de baixo nível — compilação, linking, ABI, FFI

---

## Introdução

Por que alguns projetos envolvem múltiplas linguagens de programação? A resposta depende do tipo de projeto.

Em um framework fullstack como o Django, Python cuida do backend (servidor) e HTML/CSS/JavaScript constroem a interface (cliente). São dois processos separados que se comunicam remotamente em tempo de execução via IPC — fácil de entender.

Mas existem projetos onde componentes escritos em linguagens diferentes rodam juntos como **um único processo**. Como isso é possível?

---

## O Pipeline de Compilação do GCC

Para simplificar, vamos considerar apenas linguagens que compilam para código de máquina.

Cada linguagem tem seu próprio compilador dedicado — não dá para compilar um arquivo Rust com o compilador Go. Mas compiladores não são apenas ferramentas que transformam código-fonte direto em executável. Esse é um equívoco comum.

### As 4 fases do GCC

Tomando um programa C simples como exemplo (que imprime uma mensagem diferente dependendo do sistema operacional):

**1. Pré-processamento**
- Remove comentários
- Expande macros
- Resolve compilação condicional
- Resolve `#include` — substitui a linha pelo conteúdo do header file

O output ainda é código C, mas pré-processado.

**2. Compilação**
- O código pré-processado é traduzido para **linguagem assembly** (instruções legíveis por humanos, não código de máquina ainda)
- **Mito derrubado:** um compilador não converte necessariamente código-fonte direto para código de máquina. Muitos compiladores geram uma representação intermediária — assembly ou até outra linguagem de programação.

**3. Montagem (Assembly)**
- O assembler (que tecnicamente é outro compilador) traduz o assembly para **código de máquina** (zeros e uns que a CPU entende)
- O resultado é chamado de **object file** (`.o`)
- Esse arquivo ainda não é executável — as posições das funções no binário final ainda não foram resolvidas

**4. Linking**
- Combina múltiplos object files (do nosso código + bibliotecas externas) em um único executável

---

## Static Linking vs Dynamic Linking

### Static Linking
O código de máquina de cada função necessária é copiado diretamente para o executável final. Tudo autocontido e pronto para rodar.

### Dynamic Linking
Bibliotecas são pré-compiladas em arquivos especiais chamados **dynamic shared libraries**:
- Unix/Linux: extensão `.so`
- Windows: extensão `.dll`

Essas bibliotecas contêm código executável mas **não têm entry point** (sem `main`) — fazem sentido pois bibliotecas não iniciam execução por conta própria.

Com dynamic linking, o linker insere apenas uma **referência** à biblioteca no executável. Em tempo de execução, o sistema operacional carrega a função necessária no address space do programa sob demanda.

**Vantagens:**
- Economiza espaço em disco e memória (uma cópia compartilhada por todos os programas)
- Permite atualizar/corrigir uma biblioteca sem recompilar cada programa que a usa

---

## Misturando Linguagens — Como Funciona

### Com Assembly

O GCC pode receber um arquivo assembly e simplesmente montá-lo e linká-lo. Isso significa que podemos:

1. Escrever parte do código em assembly
2. Passar ao compilador em diferentes fases
3. O linker mistura tudo num único executável

**Exemplo prático:** Um programa que calcula primos entre 0 e N. A função pesada é escrita em assembly para máxima performance, e chamada a partir de C. O GCC compila o C, monta o assembly, e linka ambos os object files.

Isso é usado por sistemas reais: **Linux kernel**, **ffmpeg**, **OpenSSL**, projetos embarcados — C para a lógica geral, assembly quando performance é crítica.

### GCC não é "o compilador C"

O que chamamos casualmente de "compilador C" é na verdade uma **toolchain** — um pipeline de ferramentas executadas em sequência. Cada etapa consome o output da anterior, e cada ferramenta é plugável.

Por isso o GCC suporta: C, C++, Objective-C, Fortran, Ada, D, e até Go dependendo da configuração.

- **GCC original:** GNU C Compiler
- **GCC hoje:** GNU Compiler Collection

Entender isso é crucial para não pensar no GCC como uma caixa preta que transforma C em executável.

### Com Linguagens de Alto Nível (ex: Fortran)

1. Compilar e montar o arquivo Fortran
2. Compilar e montar o arquivo C
3. Linkar ambos os object files em um único executável

O Fortran tem seu próprio pipeline, seu próprio compilador e às vezes suas próprias dependências de runtime.

### Com Rust

Rust tem uma toolchain completamente diferente do C — compilador diferente, build system diferente, filosofia diferente. Mas na hora de produzir o binário final, o Rust também usa um **linker**.

Para chamar uma função Rust a partir de C:
1. Implementar a função em Rust
2. Compilar o código Rust em uma biblioteca (estática ou dinâmica)
3. Declarar e usar a função no código C
4. Compilar o C e linkar com a biblioteca compilada do Rust

O contrário também funciona — chamar C a partir de Rust. De fato, isso é mais comum: C é mais antigo e muitas bibliotecas maduras e APIs de sistema estão escritas em C. Desenvolvedores Rust frequentemente precisam acessar esse ecossistema (gráficos, criptografia, APIs do SO).

---

## ABI — Application Binary Interface

Só porque duas linguagens têm uma fase de linking não significa que podem ser linkadas corretamente.

### Problema 1 — Calling Conventions

**Exemplo:** Linguagem A passa dois parâmetros nos registradores 0 e 1. Linguagem B espera os parâmetros nos registradores 1 e 2. Ambas produzem código de máquina válido para a mesma arquitetura, mas ao serem linkadas juntas o resultado é **comportamento indefinido**.

### Problema 2 — Pass by Reference vs Pass by Value

**Exemplo:** Linguagem X passa todos os argumentos por referência (coloca os endereços de memória nos registradores). Linguagem Y passa por valor (espera os valores diretos). Em tempo de execução, linguagem Y interpreta endereços de memória como valores reais, causando resultados completamente errados ou crash.

### O que é ABI

Assim como uma API define funções no nível da aplicação, uma **ABI** define como diferentes componentes de código binário interagem entre si através do hardware.

Ao misturar linguagens, pelo menos um dos lados (ou a parte que interage com o outro) deve **conformar com as expectativas de ABI do outro lado**.

---

## Ferramentas para Interoperabilidade

Designers de linguagem conhecem esses problemas. Linguagens modernas oferecem palavras-chave e flags para facilitar o processo:

| Linguagem | Mecanismo |
|-----------|-----------|
| C | `extern` |
| Rust | `extern` + atributo `#[no_mangle]` |
| Fortran | atributo `bind` |
| Go | bloco de comentários especial acima de `import "C"` (CGo) — permite inclusive código C inline no arquivo Go |

Em tempo de compilação, essas declarações servem ao mesmo propósito: dizem ao compilador *"esta função vai interagir com código escrito em outra linguagem — gere assembly que siga a ABI esperada"*.

---

## Resumo

A resposta para "como diferentes linguagens vivem num único executável" se resume ao **linker**:

1. Compiladores transformam código-fonte em object files
2. O linker combina esses object files em um único executável
3. As linguagens não precisam nem vir da mesma compiler suite
4. O que importa é que os componentes que interagem entre si **concordem na ABI**

---

## Próxima Parte

Como misturar linguagens compiladas com linguagens interpretadas.
