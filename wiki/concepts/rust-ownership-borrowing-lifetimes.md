---
type: concept
title: "Rust — Ownership, Borrowing e Lifetimes"
aliases: ["ownership rust", "borrow checker", "lifetimes rust", "fearless concurrency", "move semantics rust", "&mut vs &"]
date_created: 2026-07-16
date_updated: 2026-07-28
source_count: 4
tags: [rust, ownership, borrowing, lifetimes, borrow-checker, memory-safety, data-race, raii]
skill: lang-systems
status: stable
---

# Rust — Ownership, Borrowing e Lifetimes

O trio de regras que permite Rust ter desempenho de linguagem de sistema, memory safety e ausência de data races, sem garbage collector — tudo verificado em compile-time. Ver [[wiki/concepts/gerenciamento-de-memoria]] para a comparação com as outras duas abordagens (manual e GC).

## Ownership

Regra central: **todo valor tem exatamente um dono**; quando o dono sai de escopo, o valor é liberado automaticamente (`drop`).

```rust
let s1 = String::from("hello");
let s2 = s1; // move — s1 não pode mais ser usado
// println!("{}", s1); // erro de compilação
```

Atribuição em Rust **move** a propriedade por padrão (não copia referência como em Java/Python, nem faz cópia profunda automática como um `struct` por valor em C++). Tipos primitivos que implementam o trait `Copy` (inteiros, bool, char) são exceção — são copiados, não movidos.

Sem essa regra, duas variáveis apontando pro mesmo endereço abrem três bugs clássicos de memória manual:
- **double free** — ambas tentam liberar
- **memory leak** — nenhuma libera
- **use-after-free** — uma libera enquanto a outra ainda usa

Ownership corta o problema estruturalmente: só existe um caminho de código autorizado a liberar aquele valor.

A ideia central — liberação atrelada ao fim do escopo, verificada automaticamente, sem chamada manual espalhada pelo código — não nasce em Rust: é o mesmo princípio do padrão **RAII** de C++ (um `std::unique_ptr` libera seu recurso no destrutor quando sai de escopo). A diferença é que Rust formaliza isso como regra do compilador (borrow checker), enquanto em C++ é convenção de biblioteca — nada impede alguém de voltar para `new`/`delete` cru e reintroduzir os mesmos bugs que ownership elimina estruturalmente. Ver [[wiki/concepts/ponteiros-cpp-stack-heap-raii]] para RAII e `unique_ptr`/`std::move` em detalhe.

## Borrowing

Passar o valor inteiro para toda função destruiria o dado no caminho. **Borrowing** resolve isso com referências (`&`) — acesso sem transferência de propriedade.

```rust
fn tamanho(s: &String) -> usize { s.len() }

let nome = String::from("Ana");
let n = tamanho(&nome); // empresta, não move
// nome continua válido aqui
```

Regra de exclusividade: **várias referências imutáveis (`&`) podem coexistir, mas uma referência mutável (`&mut`) precisa estar sozinha** — ou N leitores, ou 1 escritor, nunca os dois ao mesmo tempo.

```rust
let mut texto = String::from("oi");
let a = &texto;
let b = &mut texto; // erro de compilação: a ainda está viva
```

Essa regra é o que elimina **data races** em compile-time: duas threads não conseguem ter, simultaneamente, uma referência mutável e qualquer outra referência ao mesmo dado — o cenário que causaria corrupção de memória em C/C++ não compila em Rust. É a base do que a comunidade chama de *fearless concurrency*: paralelizar código sem o medo usual de condição de corrida, porque a classe de bug inteira é rejeitada antes do programa rodar (ver [[wiki/concepts/concorrencia]]).

Quem fiscaliza essas regras é o **borrow checker**, parte do compilador (`rustc`) que analisa cada empréstimo e recusa compilar código que viole exclusividade ou ownership. "Brigar com o borrow checker" é a fricção mais citada por quem aprende Rust — não é um bug do compilador, é o mecanismo funcionando como projetado.

## Lifetimes

Pergunta que ownership e borrowing sozinhos não respondem: uma referência pode sobreviver mais tempo que o valor que ela aponta? **Lifetime** é a relação entre uma referência e a validade do valor apontado — não é um timer, é uma garantia estrutural verificada em compile-time.

```rust
let r;
{
    let texto = String::from("temporário");
    r = &texto; // texto morre no fim do bloco
} // erro de compilação: r não pode outlive texto
```

Na maioria do código, o compilador infere lifetimes sozinho (*lifetime elision*). Anotação explícita (`'a`) só é exigida quando há ambiguidade — tipicamente em funções com múltiplas referências de entrada e uma referência de saída, ou em `struct`s que guardam referências:

```rust
fn maior<'a>(s1: &'a str, s2: &'a str) -> &'a str {
    if s1.len() > s2.len() { s1 } else { s2 }
}

struct Excerpt<'a> {
    texto: &'a str, // não pode outlive o dono do texto original
}
```

`'a` aqui só nomeia uma relação: a referência devolvida vive, no mínimo, enquanto o menor dos lifetimes de entrada viver.

## Por que isso é "zero-cost"

Ownership, borrowing e lifetimes são checados inteiramente em compile-time — não sobra nenhuma estrutura de runtime (contador de referência, coletor de lixo, lock implícito) rodando junto com o programa por causa dessas garantias. O preço é pago no tempo de compilação e na curva de aprendizado, não na execução. Isso é o que torna Rust viável para embarcados e sistemas onde overhead de runtime não é opção — ver [[wiki/concepts/rust-fundamentos]] para os casos de uso reais que exploram exatamente essa propriedade.

## Relação com outros conceitos

- [[wiki/concepts/gerenciamento-de-memoria]] — ownership é a terceira abordagem (além de manual e GC) para decidir quem libera memória
- [[wiki/concepts/sistema-de-tipos]] — o borrow checker opera em conjunto com o type checker; ownership é, em parte, verificação de tipos em compile-time
- [[wiki/concepts/concorrencia]] — a regra de exclusividade do borrowing (N leitores OU 1 escritor) é o que torna data races impossíveis sem locks em runtime
- [[wiki/concepts/rust-fundamentos]] — traits, `Option`/`Result`, `enum` exaustivo e cargo, que se apoiam nessas garantias de memória para formar o resto da linguagem

## Borrow Checker como Harness para Loops Agênticos

[[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]] cita a migração do Ban (>500.000 linhas) para Rust como motivada, em parte, por essa garantia de memory safety em tempo de compilação servir como [[wiki/concepts/harness|harness]] objetivo para um agente rodando em [[wiki/concepts/loop-engineering|loop]]: em vez de o modelo "interpretar" se um trecho é memory-safe, o compilador rejeita o código diretamente — um sensor determinístico, ao contrário da linguagem anterior citada (Zig), que compila código que só quebra em produção.

## Transferência de Aprendizado para Outras Linguagens

[[wiki/sources/aprenda-a-programar-do-jeito-dificil]] cita (via comentário de espectador, não estudo controlado) o relato de que estudar "só um pouco" de Rust já melhorou a escrita de código em outras linguagens de mais alto nível — usado no vídeo como argumento de que o benefício de estudar ownership/borrowing não se limita ao uso direto de Rust em produção, mas se manifesta transferido para o código escrito em qualquer linguagem depois.

## Key Sources

- [[wiki/sources/rust-por-que-tanto-hype-ownership-borrowing-lifetimes]]
- [[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]] — borrow checker como harness/sensor objetivo na migração do Ban para Rust via loop criador
- [[wiki/sources/aprenda-a-programar-do-jeito-dificil]] — relato de comentário de espectador: estudar um pouco de Rust já melhora código em outras linguagens
- [[wiki/sources/ponteiros-cpp-go-csharp]] — RAII em C++ (`unique_ptr`, escopo, destrutor automático) como precursor conceitual do ownership em Rust
