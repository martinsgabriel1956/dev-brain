---
type: concept
title: "Acoplamento"
aliases: ["coupling", "baixo acoplamento", "alto acoplamento"]
date_created: 2026-04-25
date_updated: 2026-08-18
source_count: 8
tags: [acoplamento, software-design, clean-code, arquitetura, under-engineering]
skill: tech-mentor-backend
status: stable
---

# Acoplamento

Acoplamento mede o **grau de dependência entre partes de um sistema**. Não é sobre estar fisicamente junto — é sobre quanto uma mudança em A força uma mudança em B.

## Alto acoplamento (problema)

Uma função que busca dados, valida, transforma, envia e loga tem todas as etapas interdependentes. Mudar o schema do banco obriga a alterar a validação. Mudar o formato da API obriga a alterar a transformação.

```typescript
// alto acoplamento — tudo numa função
function processarPedido(pedidoId: string) {
  const pedido = db.query(`SELECT * FROM pedidos WHERE id = '${pedidoId}'`);
  if (!pedido || pedido.status !== "pendente") throw new Error("Inválido");
  const payload = { id: pedido.id, total: pedido.valor * 1.1 };
  await api.post("/pedidos", payload);
  console.log({ message: "Pedido processado", pedidoId });
}
```

Analogia: quebra-cabeça com peças coladas. Não dá para tirar uma sem destruir as vizinhas.

## Baixo acoplamento (solução)

Cada função tem uma responsabilidade. Mudanças ficam locais.

```typescript
async function buscarPedido(pedidoId: string) { ... }
function validarPedido(pedido: Pedido) { ... }
function transformarPedido(pedido: Pedido) { ... }
async function enviarPedido(payload: PedidoPayload) { ... }
```

Mudança no banco → só `buscarPedido`. Mudança na API → só `enviarPedido`.

## Por que importa

Sistemas altamente acoplados congelam: uma mudança pequena quebra coisas inesperadas, o time tem medo de mexer, o código para de evoluir. O próximo passo é sempre "precisamos refatorar tudo".

## Acoplamento como sinal de under-engineering, não só de over-engineering

[[wiki/sources/underengineering-overengineering-mario-souto]] traz acoplamento (tight coupling) como um dos sintomas do lado oposto do espectro descrito em [[wiki/concepts/under-engineering]] — não é uma abstração excessiva, é a ausência de qualquer separação. O exemplo dado é concreto e reconhecidamente parcial: lógica de login e de criação de conta no mesmo arquivo de autenticação, porque o autor "colocou todos os tipos de autenticação num arquivo só" e reconhece que "poderia quebrar isso um pouco mais". O critério prático que ele usa para decidir onde cortar é funcional, não teórico: "se esse arquivo é o arquivo de login, eu evito colocar coisas de criar conta junto" — a separação de responsabilidades sendo descoberta durante o trabalho ("é um pouco filosófico... conforme você vai trabalhando nos projetos, você vai vendo que existe uma separação natural"), não definida a priori.

## Analogia Médica: Limites de Órgãos Furando Uns aos Outros

[[wiki/sources/7-habitos-programador-altamente-eficaz]] reaproveita a mesma analogia de órgãos usada em [[wiki/concepts/abstracao]] para explicar acoplamento pelo ângulo inverso: assim como problemas graves de saúde surgem quando o limite de um órgão começa a "furar" o limite de outro (ex.: um problema cardíaco afetando o funcionamento renal), um software sofre os mesmos sintomas quando abstrações e responsabilidades mal definidas deixam tudo acoplado e misturado. A fonte não detalha técnica de identificação de limites (bounded contexts, DDD) — fica no nível de intuição desenvolvida com experiência, reconhecendo explicitamente que no início da carreira é difícil enxergar esses limites.

## Heurística prática: "De quem é essa linha?"

[[wiki/sources/tres-estagios-de-acoplamento-observer-pattern-na-pratica]] propõe uma pergunta simples para treinar a percepção de acoplamento linha a linha: **de quem é essa linha de código?** Se a resposta é sempre "do mesmo componente" (a mesma camada onde a linha está fisicamente), o software é uma "ameba total" — não existem divisórias reais entre responsabilidades. Se não é possível responder com clareza a quem uma linha pertence, é sinal de que não há compreensão da própria modelagem do código, não só um problema de organização de arquivos.

A fonte formaliza isso em **três estágios de acoplamento**, exemplificados via refatoração de um jogo em JavaScript, e argumenta que nenhum estágio é objetivamente superior — cada um tem seu uso:

1. **Tudo misturado** — camada de input com regra de negócio do jogo dentro do mesmo handler de evento. Ruim para manutenção, mas ótimo para prototipar rápido e descobrir falhas na própria ideia.
2. **Componentes isolados com chamada estática/explícita** — a camada de input chama `game.multiplayer(command)` de um módulo separado (via [[wiki/concepts/factory-pattern]]). Ainda é acoplamento — a camada de input conhece o método concreto — mas já tem responsabilidades separadas. A fonte nota que é assim que a maioria do software profissional é construído, mesmo com [[wiki/concepts/dependency-injection]]: DI torna a dependência flexível/testável, não a remove.
3. **Componentes que não se conhecem nem estaticamente** — via [[wiki/concepts/observer-pattern]]: o subject notifica quem estiver inscrito, sem saber quem é ou se alguém está ouvindo. É o único estágio onde adicionar um novo consumidor (ex.: uma camada de rede escutando os mesmos comandos) tem impacto quase zero no código já existente.

## Dependency Structure Analysis: Detectando Acoplamento Indevido Entre Módulos Automaticamente

[[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]] descreve uma técnica de gate de CI voltada especificamente a detectar acoplamento indevido *entre módulos* (não dentro de uma função, como complexidade ciclomática, nem dentro de um arquivo, como tamanho de módulo) — três padrões citados como alvo dessa análise:

- **Import circular**: arquivo A importa arquivo B que importa arquivo A de volta.
- **Camadas invertidas**: um controller chamando um model diretamente, pulando a camada de serviço que deveria mediar essa chamada.
- **Módulo de implementação acessando a implementação interna de outro módulo diretamente**, em vez de passar por um **módulo de API** que aquele módulo expõe propositalmente para consumo externo.

Esse terceiro padrão generaliza o próprio problema já descrito nesta página em "Alto acoplamento (problema)" e nos "três estágios de acoplamento" — a diferença é que aqui a fronteira é entre módulos/pacotes inteiros, não entre funções dentro do mesmo arquivo, e a fonte propõe capturar a violação automaticamente no CI (ferramenta de análise de estrutura de dependências), não só via revisão humana ou heurística de design.

## Feature Envy: Acoplamento Via Acesso a Dados Internos de Outra Classe

[[wiki/sources/9-code-smells-como-identificar-codigo-ruim]] descreve [[wiki/concepts/feature-envy]] como uma forma de acoplamento "content" (na taxonomia acima) especialmente severa: uma classe (`OrderPrinter`) acessando atributos internos de outra classe (`Order.items`) que por sua vez expõe atributos internos de uma terceira (`Product.price`, `Product.discount`), para fazer um cálculo que não é responsabilidade de nenhuma das duas classes acessadas. A fonte descreve o resultado como "mais acoplado que espaguete" — renomear um único campo interno de `Product` quebra uma classe a duas camadas de distância, sem nenhuma dependência declarada e visível entre elas. É o mesmo padrão do "Alto acoplamento (problema)" descrito acima, mas atravessando fronteiras de classe em vez de ficar dentro de uma única função.

## Tipos, Categorias e Métricas: Tornando o Acoplamento Mensurável

[[wiki/sources/medindo-e-entendendo-acoplamento-matheus-castiglioni]] complementa toda a discussão qualitativa acima com uma **taxonomia formal e fórmulas**. Distingue seis *tipos* de acoplamento em ordem crescente de força/indesejabilidade — **data** (só informação passa, mais fraco), **stamp** (estruturas inteiras), **control** (parâmetros que ativam comportamentos), **external** (dependência de partes externas), **common** (dependência de estado global) e **content** (uma parte modifica dados/fluxo interno de outra, mais forte) — e duas *categorias* qualitativas: acoplamento **apropriado** (você sabe que existe e deveria existir) vs. **não apropriado** (não sabe que existe, ou sabe e não deveria).

Sobre medição, apresenta as métricas de [[wiki/entities/uncle-bob|Robert C. Martin]]: acoplamento **aferente** (Ca, conexões que entram) e **eferente** (Ce, conexões que saem), abstração `A = ma/(ma+mc)`, instabilidade `I = Ce/(Ca+Ce)` e distância da sequência principal `D = |A + I − 1|`, além das duas regiões-armadilha do gráfico A×I — a **zona de dor** (concreto e rígido demais → frágil) e a **zona de inutilidade** (abstrato demais → ninguém usa). A página [[wiki/concepts/metricas-de-acoplamento]] consolida essas fórmulas e sua interpretação.

## Relações

- [[metricas-de-acoplamento]] — como medir acoplamento por componente: aferente/eferente, abstração, instabilidade, distância da sequência principal
- [[abstracao]] — abstração é o mecanismo que permite baixo acoplamento entre módulos
- [[single-responsibility]] — SRP é a diretriz que orienta como separar responsabilidades
- [[coesao]] — conceito complementar: coesão alta dentro de um módulo + acoplamento baixo entre módulos é o alvo
- [[efeito-colateral]] — funções com efeitos colaterais ocultos aumentam o acoplamento implícito

## Key sources

- [[wiki/sources/medindo-e-entendendo-acoplamento-matheus-castiglioni]] — taxonomia (6 tipos + 2 categorias) e as métricas de Uncle Bob (aferente/eferente, abstração A, instabilidade I, distância D, zonas de dor/inutilidade)
- [[wiki/sources/acoplamento-abstracao-estado]]
- [[sources/ports-and-adapters-codebase-para-ia]] — forte acoplamento em god class quebra três módulos por uma mudança
- [[wiki/sources/design-pattern-adapter]] — `new` de uma classe concreta de baixo nível (lib externa) dentro de uma classe de alto nível é a manifestação de acoplamento que o [[wiki/concepts/adapter-pattern]] resolve
- [[wiki/sources/underengineering-overengineering-mario-souto]] — exemplo real de login e criação de conta acoplados no mesmo arquivo; separação tratada como algo que se aprende na prática, não como regra fixa
- [[wiki/sources/7-habitos-programador-altamente-eficaz]] — analogia médica dos órgãos aplicada ao acoplamento: limites mal definidos entre componentes causam os mesmos sintomas que órgãos ferindo os limites uns dos outros
- [[wiki/sources/tres-estagios-de-acoplamento-observer-pattern-na-pratica]] — heurística "de quem é essa linha?"; três estágios de acoplamento exemplificados via refatoração de um jogo em JavaScript (misturado → Factory com chamada estática → Observer sem conhecimento estático)
- [[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]] — dependency structure analysis como gate de CI: import circular, camadas invertidas, módulo de implementação acessando outro sem passar por módulo de API
- [[wiki/sources/9-code-smells-como-identificar-codigo-ruim]] — feature envy como acoplamento "content" atravessando classes; god object como acoplamento resolvido via composição
