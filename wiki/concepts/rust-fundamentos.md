---
type: concept
title: "Rust — Fundamentos, Tooling e Adoção"
aliases: ["rust option result", "rust enum exaustivo", "cargo", "crates.io", "rust traits", "quando usar rust"]
date_created: 2026-07-16
date_updated: 2026-07-16
source_count: 1
tags: [rust, traits, option, result, pattern-matching, cargo, enum, adocao-de-linguagem]
skill: lang-systems
status: stable
---

# Rust — Fundamentos, Tooling e Adoção

Além de ownership/borrowing/lifetimes (ver [[wiki/concepts/rust-ownership-borrowing-lifetimes]]), Rust tem um conjunto de decisões de design que aparecem no dia a dia de quem escreve a linguagem: como representar ausência de valor e erro, como modelar estado, e uma toolchain padronizada via Cargo.

## `Option<T>` e `Result<T, E>` — sem `null` implícito

Rust não tem `null` no sentido tradicional. Ausência de valor é um tipo: `Option<T>` é `Some(valor)` ou `None`. Erro recuperável é outro tipo: `Result<T, E>` é `Ok(valor)` ou `Err(erro)`. Ambos empurram a checagem para o sistema de tipos — ver [[wiki/concepts/sistema-de-tipos]].

```rust
match usuario {
    Some(u) => println!("{}", u.nome),
    None => println!("sem usuário"),
}

fn ler_config() -> Result<String, std::io::Error> {
    let texto = std::fs::read_to_string("config.toml")?; // propaga erro
    Ok(texto)
}
```

O operador `?` propaga `Err` automaticamente, mantendo o caminho feliz legível sem esconder que o erro existe — diferente de uma exception que pode ser esquecida ou de um `null` que só quebra quando alguém tenta usá-lo.

## `match` exaustivo e estado inválido irrepresentável

Rust incentiva modelar estado de forma que combinações inválidas **não compilem**, em vez de existirem como bug latente:

```rust
enum Status {
    Aberto,
    Pago { pago_em: String },
    Cancelado { motivo: String },
}
```

Cada variante carrega só os dados que fazem sentido para aquele estado — nada de campos soltos (`pago_em: Option<String>`, `motivo: Option<String>`) que permitiriam um pedido pago com motivo de cancelamento. O `match` sobre um `enum` é **exaustivo**: o compilador exige tratar todas as variantes. Se alguém adicionar uma quarta variante depois, todo `match` que não trata o novo caso vira erro de compilação, apontando exatamente onde o código precisa mudar — o tradeoff é modelar exigindo mais intenção e tempo no começo.

## Traits — polimorfismo sem overhead implícito

`trait` é um contrato de comportamento, análogo a interface, mas mais integrado ao sistema de tipos: aparece em genéricos, no operador `?`, em conversões e em iterators.

```rust
trait Repository<T> {
    fn find_by_id(&self, id: &str) -> Option<T>;
}
```

Genéricos com trait bound (`fn process<R: Repository<T>>(...)`) usam *static dispatch* — o compilador gera uma versão especializada por tipo concreto (monomorphization), sem overhead de vtable em runtime.

## Cargo — toolchain padronizada

**Cargo** é o gerenciador de projeto: build, dependências, testes e publicação. Ver [[wiki/concepts/toolchain]] para o papel do `rustc`+`cargo` frente a outras toolchains (GCC, Clang).

| Comando | Faz |
|---|---|
| `cargo new` | Cria projeto |
| `cargo run` | Compila e executa |
| `cargo test` | Roda testes |
| `cargo fmt` | Formata código |

Dependências (**crates**) ficam declaradas em `Cargo.toml`; o repositório público é o [crates.io](https://crates.io). Um formatador e gerenciador únicos e padronizados no ecossistema eliminam boa parte da discussão de estilo/tooling que outras comunidades gastam tempo resolvendo por conta própria.

## Quando Rust compensa o custo

Três tradeoffs frente a outras linguagens:

1. **Aprendizado** — ownership/borrowing/lifetimes são exigidos desde o primeiro programa, não algo que dá pra adiar.
2. **Velocidade de compilação** — tende a ser mais lenta que Go em projetos grandes (varia com dependências e máquina).
3. **Verbosidade em casos específicos** — genéricos podem gerar mensagens de erro longas; estruturas com referências internas (árvores com ponteiro pro pai, grafos) são difíceis de escrever de forma idiomática sem `Rc`/`RefCell`.

Rust compensa esse custo quando: o custo de falha é alto, controle e desempenho importam, segurança de memória é crítica, uso de CPU/latência importam, e distribuir um binário único nativo é vantagem (sem runtime externo, início rápido — útil pra CLIs). Não compensa tanto para validar uma ideia em poucos dias, ou para um CRUD comum de tela+formulário+banco, onde TypeScript, Ruby, Python ou Go entregam com muito menos atrito. Ver [[wiki/concepts/escolha-de-stack]].

## Adoção real: motor por baixo, não substituto do produto

Rust nem sempre substitui a linguagem do produto — frequentemente entra como peça de infra crítica dentro de um sistema maior escrito em outra stack:

- **Linux** — suporte a Rust para escrever abstrações e drivers dentro do kernel (não o kernel inteiro).
- **Android** — Google usa Rust em componentes nativos do sistema para reduzir vulnerabilidades de memória que historicamente vinham de C/C++.
- **AWS Firecracker** — microVMs usadas por Lambda e Fargate; ambientes isolados com pouco overhead.
- **Cloudflare Pingora** — proxy HTTP para tráfego de alto volume, onde performance e previsibilidade de memória importam.
- **Deno** — runtime que executa JS/TS/WASM, com base em V8 + Rust + Tokio; quem escreve TypeScript pode estar rodando Rust por baixo sem perceber.
- **uv** — gerenciador de pacotes Python escrito em Rust.

Nenhum desses exemplos foi verificado contra fonte primária nesta ingestão — ver Open Questions em [[wiki/sources/rust-por-que-tanto-hype-ownership-borrowing-lifetimes]].

## Relação com outros conceitos

- [[wiki/concepts/rust-ownership-borrowing-lifetimes]] — as garantias de memória que tornam esse resto da linguagem seguro
- [[wiki/concepts/sistema-de-tipos]] — `Option`/`Result`/`enum` exaustivo são o sistema de tipos carregando o comportamento possível
- [[wiki/concepts/compilador]] — monomorphization de genéricos acontece na fase de geração de código
- [[wiki/concepts/toolchain]] — Cargo como camada acima do `rustc`
- [[wiki/concepts/go-fundamentos]] — contraste de filosofia: Go busca poucas formas de fazer cada coisa; Rust oferece mais expressividade ao custo de mais decisões explícitas

## Key Sources

- [[wiki/sources/rust-por-que-tanto-hype-ownership-borrowing-lifetimes]]
