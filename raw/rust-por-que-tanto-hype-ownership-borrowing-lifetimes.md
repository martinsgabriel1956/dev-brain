# Rust: por que tanto hype (e por que irrita tanta gente)

> Transcrição de vídeo em português, limpa e reestruturada em seções a partir de um áudio corrido sem pontuação. Erros óbvios de ASR corrigidos por contexto (ex.: "Rush"/"Rush" → Rust, "INAM" → `enum`, "OM" → `impl`, "vc exclamação" → `vec!`, "e-comercial" → `&`). Sem necessidade de tradução — fonte já em PT-BR.

## Abertura

Você escreve um bug que, em C, talvez compile, rode e explode só depois. Em Rust, o programa nem chega a rodar — o compilador barra o erro antes da primeira linha executar. A aposta do Rust é pagar mais na compilação para levar menos susto em produção. Hoje vou mostrar por que Rust é tão exaltado e também por que irrita tanta gente, e quais foram as motivações para ele ser criado.

## O problema que o Rust quer resolver

Todo programa precisa lidar com memória. Em C e C++ você ganha controle fino, mas também pode liberar memória cedo demais, esquecer de liberar, ou usar um ponteiro depois que ele ficou inválido. Em Java, Go, JavaScript e várias outras linguagens, o garbage collector cuida de boa parte disso — deixa o código mais confortável de escrever, mas adiciona um runtime rodando junto com o programa.

Rust tenta ir por outro caminho: desempenho de linguagem de sistema, sem garbage collector, com segurança de memória checada antes do programa rodar. Rust troca uma parte da liberdade imediata por regras mais fortes no compilador. Na prática, você passa mais tempo negociando com o compilador, mas quando o código compila, boa parte dos erros de memória e de acesso concorrente já foram descartados.

Para fazer isso, o Rust precisa de uma ideia que quase nenhuma linguagem mainstream colocou no centro: **ownership**.

## Ownership

Ownership quer dizer propriedade, posse. Em Rust, todo valor tem um dono. Quando esse dono sai de escopo, o valor é liberado automaticamente, e na maior parte dos casos só existe um dono por vez.

```rust
let nome = String::from("Ana");
let saudacao = nome; // a propriedade se move para saudacao
// nome não pode mais ser usado a partir daqui
```

Na primeira linha, `nome` é dono da string. Na segunda, a propriedade se *move* para `saudacao`. A partir daí, `nome` não pode mais ser usado.

Isso pode parecer estranho no começo, porque em várias linguagens a atribuição só copia uma referência. Mas isso evita um problema real: se duas variáveis apontassem para o mesmo endereço de memória, quem liberaria essa memória no final?

- Se as duas liberam, você tem **double free** (liberar duas vezes).
- Se nenhuma libera, você tem **memory leak**.
- Se uma libera enquanto a outra ainda usa, você tem **use after free** (usar a memória depois dela morrer).

O ownership corta esse problema com uma regra rígida: quem é dono responde pelo valor; quando o dono muda, a variável antiga perde acesso.

## Borrowing

Mas se todo valor só pode ter um dono, como passar dados para funções sem destruir tudo no caminho? Para isso existe o **borrowing** — literalmente, emprestar. Em vez de passar o valor inteiro para uma função, você passa uma referência, feita com `&`. Ela permite acessar o valor sem tomar a propriedade.

```rust
fn tamanho(s: &String) -> usize {
    s.len()
}

let nome = String::from("Ana");
let n = tamanho(&nome);
// nome continua existindo normalmente depois da chamada
```

A função `tamanho` recebe `&String` — ela pode ler a string, mas não vira dona dela.

Agora vem a parte que costuma confundir: Rust deixa você ter várias referências **imutáveis** ao mesmo tempo — várias partes do código podem ler o mesmo valor. Mas se alguém quiser mudar esse valor, a referência **mutável** precisa ficar sozinha: ou vários leitores, ou um único escritor. Essa regra evita **data races** — disputas em que duas threads acessam a mesma memória sem coordenação e pelo menos uma delas escreve.

```rust
let mut texto = String::from("oi");
let a = &texto;
let b = &mut texto; // o compilador reclama aqui
```

O compilador reclama porque `a` e `b` poderiam tentar mudar o mesmo texto ao mesmo tempo. Quem faz essa fiscalização é o **borrow checker** — a parte do compilador que confere se esses "empréstimos" são válidos. Se você já ouviu falar que "brigar com o borrow checker" faz parte de aprender Rust, é disso que as pessoas estão falando.

## Lifetimes

Falta uma pergunta: como o compilador sabe se uma referência fica viva tempo demais? Para isso existe o **lifetime**. Lifetime não é um timer — é a relação entre uma referência e o valor apontado por ela. O compilador garante que a referência nunca vai viver mais do que o próprio valor.

```rust
let r;
{
    let texto = String::from("temporário");
    r = &texto; // texto morre no fim do bloco, r ficaria apontando pro nada
}
// Rust não deixa esse código compilar
```

`texto` nasce dentro do bloco; a referência `r` tenta sobreviver fora dele. Quando o bloco termina, `texto` morre, então `r` ficaria apontando para nada — e Rust não deixa esse código compilar. O fix é fazer o valor viver tempo suficiente.

Na maior parte do código normal você não precisa anotar lifetimes na mão — o compilador infere. Mas quando você cria structs que guardam referências, ou funções com várias referências entrando e saindo, ele precisa de ajuda:

```rust
fn maior<'a>(s1: &'a str, s2: &'a str) -> &'a str {
    if s1.len() > s2.len() { s1 } else { s2 }
}
```

O apóstrofo `'a` só nomeia uma relação: a função está dizendo que a referência devolvida vive pelo menos enquanto as entradas compartilharem um tempo de vida válido. A sintaxe é estranha, mas a ideia é essa: uma função que devolve referência precisa dizer de onde essa referência veio.

## Ausência de valor e erros: `Option` e `Result`

Com ownership, borrowing e lifetimes explicados, dá para entender por que Rust parece diferente das linguagens mais usadas. Rust não tem `null` no jeito tradicional para representar ausência de valor — ele usa `Option`: ou você tem `Some(valor)`, ou você tem `None`. Isso força o código a lidar com os dois casos, via **pattern matching** (`match`), que compara o valor com cada formato possível:

```rust
match usuario {
    Some(u) => println!("Usuário: {}", u.nome),
    None => println!("Sem usuário"),
}
```

Isso é positivo porque o erro não fica escondido atrás de um valor mágico — ele aparece no tipo.

Para erro recuperável, Rust usa `Result<T, E>`: `Ok` significa sucesso, `Err` significa erro. O operador `?` é um atalho muito usado:

```rust
fn ler_config() -> Result<String, std::io::Error> {
    let texto = std::fs::read_to_string("config.toml")?; // propaga erro se der errado
    Ok(texto)
}
```

Se `read_to_string` der erro, a função retorna esse erro; se der certo, o código continua com `texto`. Esse estilo deixa o caminho feliz legível sem esconder que erro não existe — e esse design aparece de novo na sintaxe, porque Rust gosta de colocar o comportamento possível no tipo e deixar o compilador cobrar que você trate.

## Sintaxe: structs, enums, mutabilidade

Rust parece uma mistura estranha no começo: tem cara de C em alguns pontos, e em outros tem coisas como `match` e tipos que lembram linguagem funcional.

```rust
struct Pedido {
    id: u64,
    total_centavos: u64,
    status: Status,
}

enum Status {
    Aberto,
    Pago,
    Cancelado(String), // motivo do cancelamento
}
```

`struct` define dados — aqui o pedido tem id, total em centavos e status. `enum` define alternativas — o status pode ser aberto, pago ou cancelado, com uma string carregando o motivo. Isso é mais forte do que usar uma string solta: se alguém escrever um status inválido, o código nem compila.

```rust
impl Pedido {
    fn cancelar(&mut self, motivo: String) {
        self.status = Status::Cancelado(motivo);
    }
}
```

`impl` coloca funções associadas a um tipo dentro dele. `self` é o próprio pedido, e `&mut self` diz que esse método pega uma referência mutável do pedido.

Outro ponto importante: em Rust, a variável **não é mutável por padrão**. Se você quer alterar, precisa usar `mut`. Em vez de tudo poder mudar a qualquer momento, a mutação fica claramente marcada. E quando você junta isso com borrowing e tipos como `Option`/`Result`, o compilador tem bastante contexto para te proteger.

## Traits, iterators, macros, closures

Até aqui o foco foi restrição, mas Rust também tem bastante ferramenta para escrever código expressivo.

**Trait** é um contrato de comportamento: se uma função precisa de algo que sabe realizar uma ação, ela não precisa saber o tipo exato — só que aquele tipo implementa o trait certo. Parece com interface em outras linguagens, mas os traits são bem mais integrados ao sistema de tipos: aparecem em genéricos, no operador `?`, em conversões, em iterators e em várias APIs do dia a dia.

**Iterator** é um objeto que produz valores em sequência, e o compilador costuma otimizar pipelines de iterators de forma bem agressiva.

```rust
let dobrados: Vec<i32> = vec![1, 2, 3].iter().map(|n| n * 2).collect();
```

Duas coisas assustam um pouco aqui: `vec!` é uma **macro** (macros em Rust usam `!` no nome, como `println!`, `format!`, `vec!`), e `|n| n * 2` é uma **closure** — uma função criada ali mesmo. Rust deixa você escrever código bem alto nível, mas sempre tenta compilar isso para algo eficiente, sem depender de garbage collector.

## Cargo e tooling

Uma parte forte de Rust é o tooling. **Cargo** é o gerenciador de projeto: build, dependências, testes e publicação de pacotes. Em vez de escolher ferramentas uma a uma, você já tem um fluxo padrão:

- `cargo new` — cria projeto
- `cargo run` — compila e executa
- `cargo test` — roda os testes
- `cargo fmt` — formata o código

Essa padronização ajuda na adoção: quando o time inteiro usa o mesmo formatador e o mesmo gerenciador, muita discussão pequena nem tem como acontecer. As dependências ficam no `Cargo.toml`; os pacotes são chamados de **crates**, e o repositório público principal é o [crates.io](https://crates.io).

## Modelagem de dados: estado inválido irrepresentável

Rust incentiva modelar estado inválido como algo impossível de representar. Se você guarda `status`, `pago_em` e `motivo` como campos soltos, dá para ter combinações sem sentido — um pedido pago com motivo de cancelamento, ou um pedido cancelado com data de pagamento em vez de `None`.

Com `enum`, cada estado carrega só os dados que fazem sentido: `Pago` carrega `pago_em`, `Cancelado` carrega `motivo`, `Aberto` não precisa de campos vazios.

O `match` em Rust é **exaustivo**: se o `enum` tem três alternativas, você precisa tratar as três. Se amanhã alguém adicionar um quarto estado, o compilador aponta exatamente onde o código precisa mudar — uma mudança futura não exige caçar todos os lugares que precisam ser atualizados. O tradeoff: modelar bem em Rust exige mais intenção e tempo no começo.

## Onde Rust faz sentido

Rust faz mais sentido quando você quer controle, desempenho e previsibilidade — por isso é forte em software de sistema: drivers, runtimes, bancos de dados, proxies, ferramentas de linha de comando. Compila para binário nativo, o que é ótimo para CLIs que precisam iniciar rápido e para serviços que precisam controlar bem o uso de memória — e para sistemas onde o garbage collector atrapalharia a previsibilidade.

No backend, Rust aparece bastante em infraestrutura: proxies, gateways, workers, processamento de dados, ferramentas que rodam dentro do pipeline de desenvolvimento. Também é usado em embarcados, onde há pouca memória e é preciso controlar bem cada alocação.

## Tradeoffs

1. **Aprendizado** — ownership, borrowing, lifetimes etc. são exigidos desde o começo; o compilador não deixa empurrar as dúvidas para depois.
2. **Velocidade de compilação** — por causa de como compila, Rust pode demorar mais que linguagens como Go em projetos grandes (varia com projeto, dependências e máquina).
3. **Complexidade em certos tipos de código** — a sintaxe pode ficar verbosa, tipos genéricos podem gerar mensagens de erro longas, e algumas estruturas de dados com referências internas são difíceis de escrever de forma idiomática.

Por isso Rust costuma ser melhor decisão quando o problema justifica o custo. Um CRUD com prazo curto: TypeScript, Ruby, Python ou Go resolvem com muito menos atrito. Uma peça de infraestrutura que vai rodar muito e processar dados pesados: Rust começa a fazer sentido.

## Adoção no mundo real

A adoção de Rust segue esse padrão: aparece onde o custo de falha é muito alto. Nem todo projeto que usa Rust é um projeto inteiro em Rust — muitas vezes ele entra só em partes específicas, justamente onde segurança e desempenho importam mais.

- **Linux**: Rust entrou como suporte para código dentro do kernel — não significa que o kernel é feito em Rust, mas existe uma frente para escrever abstrações e drivers em Rust, com cuidado extra porque o kernel é um ambiente bem restrito.
- **Android**: o Google usa Rust em componentes nativos do sistema, porque bugs de memória em C/C++ costumam virar vulnerabilidades graves, e Rust reduz esse risco quando o código fica dentro do subconjunto seguro da linguagem.
- **AWS Firecracker**: tecnologia de microVMs usada em Lambda e Fargate — o objetivo é subir rápido ambientes isolados com pouco overhead.
- **Cloudflare Pingora**: framework em Rust para serviços de rede e proxies HTTP — quando se processa uma quantidade absurda de tráfego, memória, performance e previsibilidade importam muito.
- **Deno**: runtime que executa JavaScript, TypeScript e WebAssembly, mas cuja base inclui V8, Rust e Tokio — quem escreve TypeScript pode estar usando Rust por baixo sem perceber.
- **uv** (Python): gerenciador de pacotes escrito em Rust, ganhando bastante popularidade recentemente.

Rust nem sempre substitui a linguagem que você usa no produto, mas muitas vezes vira o motor por baixo das ferramentas que você já usa.

## Quando vale escolher Rust

Faz sentido quando: o custo de falhar é alto, a necessidade de controle é alta, segurança de memória importa muito, uso de CPU importa, latência importa, e distribuir um binário único importa.

Não serve tão bem quando: você quer validar uma ideia em poucos dias, ou o app é basicamente tela + formulário + banco + regra de negócio comum — aí outras linguagens entregam mais rápido.

Isso não quer dizer que Rust é pior que as outras. Rust obriga você a responder perguntas que outras linguagens deixam implícitas: quem é dono desse valor, quem pode mudar esse dado, essa referência está viva tempo suficiente, esse erro foi tratado, esse estado inválido pode existir? No começo parecem burocracia; depois de um tempo, viram design.

Rust também não resolve tudo — o compilador não impede um deadlock, e não transforma uma arquitetura ruim em uma arquitetura boa. Mas tira um conjunto grande de erros que, em outras linguagens, aconteceriam de forma mais silenciosa.

## Fechamento

O objetivo da linguagem não é ter sintaxe parecida com outras — é forçar que as decisões fiquem explícitas antes do programa rodar.
