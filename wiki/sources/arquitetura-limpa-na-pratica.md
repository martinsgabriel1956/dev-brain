---
type: source
title: "Arquitetura Limpa na Prática — Livro Completo"
aliases: ["arquitetura limpa na prática", "clean architecture na prática otávio lemos", "thewisepad"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/arquitetura-limpa-na-pratica.md
source_url: ""
author: "Otávio Lemos"
date_published: "2022"
date_ingested: 2026-08-03
source_count: 0
tags: [clean-architecture, arquitetura-de-software, hexagonal-architecture, dci, bce, typescript, ddd, solid, design-patterns, either-monad, repository-pattern, mvc, humble-object, dependency-inversion]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Livro-tutorial em português que ensina Arquitetura Limpa (Robert C. Martin) por meio de um estudo de caso completo — uma API REST de bloco de notas ("theWisePad") em TypeScript/Node.js/MongoDB/Express, construída camada por camada: Entidades → Casos de Uso → Adaptadores de Interface → Frameworks & Drivers → Principal & Configuração. O livro situa a Arquitetura Limpa como síntese prática de três arquiteturas anteriores — Hexagonal (Cockburn), DCI (Reenskaug/Coplien) e BCE (Jacobson) — todas construídas em torno da mesma ideia central: separar regras de negócio de detalhes de infraestrutura via a **Regra de Dependência** (dependências de código-fonte só apontam para dentro). O diferencial do livro frente à obra original de Robert Martin é justamente o exemplo de código completo e didático, algo que os leitores do livro original sentiam falta.

**Nota sobre direitos autorais:** por instrução do usuário, este ingest **não reproduz o texto do livro na íntegra** (o próprio epub traz o aviso "Copyright © 2021-2022 - Otávio Lemos | Todos os direitos reservados"). Este documento é resumo e paráfrase com citações curtas pontuais, seguindo o mesmo padrão adotado em [[wiki/sources/filosofia-do-design-de-software-livro-completo]].

## Key Claims

**Claim:** Arquitetura de software é, na definição adotada pelo livro (seguindo Robert Martin), "a forma dada ao sistema por aqueles que o constroem" — a divisão do sistema em componentes, seu arranjo, e como esses componentes se comunicam; seu propósito é minimizar os recursos humanos necessários para construir e manter o sistema, mantendo o máximo de opções em aberto pelo máximo de tempo possível.
**Evidence:** Cap. 1 ("Arquitetura de Software"). O autor contrasta três abordagens de definição — a de Mark Richards/Neal Ford (estrutura + características + decisões de projeto + princípios), a acadêmica de Taylor/Medvidovic/Dashofy, e a "essencial" de Robert Martin (arquitetura = design de software) — e adota a última como referência do livro. Cita também Dan North: o propósito do desenvolvimento de software é gerar impacto positivo de negócio, minimizando o *lead time* de forma **sustentável**.
**Confidence:** alta — capítulo fundacional que define o vocabulário usado no resto do livro.

**Claim:** Toda arquitetura de software deveria separar "regras de negócio do domínio" (dados e políticas que existiriam mesmo sem um sistema — ex.: as regras de um empréstimo) de "regras de negócio da aplicação" (como o sistema automatiza essas regras — os casos de uso); essa distinção é o que motiva a separação em camadas Entidades vs. Casos de Uso.
**Evidence:** Cap. 1, usando o exemplo de empréstimo do próprio livro de Robert Martin (principal, taxa, período como dados críticos; realizarPagamento, aplicarTaxa, cobrarMultaDeAtraso como regras críticas — juntos formam uma Entidade). No estudo de caso do livro, essa distinção se manifesta em User/Note (Entidades) vs. SignUp/CreateNote/etc. (Casos de Uso).
**Confidence:** alta.

**Claim:** A Arquitetura Limpa é uma síntese prática de três arquiteturas anteriores — Hexagonal/Portas e Adaptadores (Cockburn 2005), DCI/Dados-Contexto-Interação (Reenskaug e Coplien) e BCE/Fronteira-Controle-Entidade (Jacobson) — todas convergindo para o mesmo objetivo de separação de interesses via divisão em camadas.
**Evidence:** Cap. 2. Hexagonal: isola o cerne da aplicação de quem a executa (via portas/interfaces) e de quem ela conversa (via adaptadores). DCI: three perspectivas — Dados (estado/domínio), Contexto (redes de objetos em runtime, "Roles"), Interação (como objetos colaboram — mapeia para casos de uso; o próprio Robert Martin usa o termo "interactors"). BCE: Entidade (objetos de domínio persistidos), Fronteira (interações com atores externos), Controle (lógica de casos de uso e coordenação).
**Confidence:** alta — o autor documenta a genealogia explicitamente, com citação de cada arquitetura original.

**Claim:** A Regra de Dependência — "dependências de código-fonte só podem apontar para dentro, em direção às políticas de alto nível" — é o conceito mais importante da Arquitetura Limpa; nenhum código de um círculo mais interno pode mencionar nome de algo declarado em um círculo mais externo (função, classe, variável, estrutura de dados).
**Evidence:** Cap. 2, seção "Arquitetura Limpa: Uma Ideia Prática". As quatro características resultantes: independência de frameworks, testabilidade (cada camada testável isoladamente), independência de UI, independência de banco de dados. As cinco camadas descritas: Entidades (regras de domínio, menor probabilidade de mudar), Casos de Uso (regras de negócio da aplicação — "a dança das entidades"), Adaptadores de Interface (MVC — controllers/presenters/views —, conversão de dados para o formato de repositórios), Frameworks & Drivers (banco, framework Web, bibliotecas — "detalhes sujos"), e uma quinta camada que o autor adiciona por conta própria: Principal & Configuração (módulo `Main`, factories, injeção de dependência, ponto de entrada).
**Confidence:** alta — é o núcleo conceitual do livro e da arquitetura descrita.

**Claim:** Empresas de grande escala (iFood, Netflix, Uber, e — por relatos de terceiros do autor — Amazon, Mercado Livre e Nubank) usam, na prática, ideias de Arquitetura Limpa/Hexagonal em produção, contrariando a visão de que essas arquiteturas são apenas acadêmicas ou inviáveis em escala.
**Evidence:** Cap. 2. Caso citado com mais detalhe: post do blog de engenharia da Netflix relatando troca de fonte de dados de API JSON para GraphQL em ~2 horas graças a repositórios abstraídos por interface (Arquitetura Hexagonal). Uber: "Domain-Oriented Microservices Architecture" (DOMA), declarado pelos próprios autores do post como baseado em DDD e Arquitetura Limpa. iFood: relato pessoal do autor após conversa de duas horas com um desenvolvedor do iFood ("Braca"), observando jargão de Arquitetura Limpa/Hexagonal em microsserviços.
**Confidence:** média — Netflix e Uber citam fontes primárias (posts de engenharia linkados); iFood, Amazon, Mercado Livre e Nubank são relatos pessoais/anedóticos do autor, sem fonte publicada verificável.

**Claim:** No frontend, não faz sentido replicar rigorosamente todas as camadas da Arquitetura Limpa (o frontend já é, por definição, uma camada externa/de baixo nível); o padrão recomendado é o *Humble Object*, dividindo em *Presenter* (lógica de formatação, testável) e *View* (apenas exibição, difícil de testar, mantida "humilde"/simples).
**Evidence:** Cap. 2, seção "E o frontend?". O autor cita o trabalho de Khalil Stemmler sobre MVP com "zoom in" no Model como uma camada própria para lidar com dados globais e recuperação de dados no cliente. SOLID e boas práticas de design continuam válidas no frontend, mas regras de negócio de domínio não deveriam morar lá.
**Confidence:** alta quanto à posição do autor; é opinião declarada, não uma regra formal da Arquitetura Limpa original de Robert Martin.

**Claim:** TypeScript foi escolhido para o exemplo por ser superconjunto tipado do JavaScript com sistema de tipos estrutural (não nominal, ao contrário de Java/C#) — um valor pode pertencer a múltiplos "conjuntos"/tipos simultaneamente, o que torna uniões de tipo (`string | number`) naturais.
**Evidence:** Cap. 3. Descreve o pipeline de compilação: AST TypeScript → checagem de tipos → transpilação para JS → AST JavaScript → bytecode → runtime (V8/Node.js).
**Confidence:** alta — descrição técnica direta, não uma claim polêmica.

**Claim:** O tratamento de erros do estudo de caso é feito com a monad **Either** (não `try-catch`) por toda a aplicação, para reservar exceções apenas a cenários verdadeiramente inesperados (estouro de memória, perda de conexão); o padrão é inspirado em recomendações de *Object Design* (Wirfs-Brock et al. 2002) e *Programming TypeScript* (Cherny 2019).
**Evidence:** Cap. 3. Either é implementado com classes `Left` (erro) e `Right` (sucesso), com propriedade `value` e métodos `isLeft`/`isRight`; usado, por exemplo, no factory method de criação de `User`, que pode retornar `InvalidEmailError`, `InvalidPasswordError` ou a instância de `User`. No estudo de caso completo há apenas dois `try-catch`: na classe `WebController` e no middleware de autenticação.
**Confidence:** alta — padrão central e recorrente em todo o exemplo de código do livro.

**Claim:** No modelo de domínio do estudo de caso (theWisePad), `User` e `Note` usam Value Objects auto-validados (`Email`, `Password`, `Title`) em vez de tipos primitivos, para evitar a *obsessão por tipos primitivos* (primitive obsession) e tornar impossível instanciar um objeto de domínio inválido ("make illegal states irrepresentable" — citação de Yaron Minsky via Scott Wlaschin).
**Evidence:** Cap. 6. Value Objects são criados via *factory method* `create` (construtor privado), retornam `Either<ErroEspecífico, ValueObject>`, e são congelados (`Object.freeze`) para imutabilidade. Identificadores artificiais (`id`) deliberadamente NÃO aparecem na camada de Entidades — só surgem na camada de Casos de Uso, ao lidar com repositórios.
**Confidence:** alta.

**Claim:** A fronteira entre "regra de negócio do domínio" (camada de Entidades) e "regra de negócio da aplicação" (camada de Casos de Uso) é uma decisão de projeto subjetiva, não uma classificação objetiva — o mesmo requisito (ex.: "usuário não pode ter duas notas com o mesmo título") pode legitimamente morar em qualquer uma das duas camadas dependendo de quão "fechada"/estável se considera a regra.
**Evidence:** Cap. 7 (Casos de Uso, seção *Create note*). O autor implementa a checagem de título duplicado no caso de uso `CreateNote`, mas explicitamente argumenta que ela poderia estar na Entidade `User` se fosse considerada uma regra fechada do domínio, mudando a estrutura do modelo (a lista de notas do usuário precisaria estar na própria Entidade `User`).
**Confidence:** alta — é uma reflexão metodológica explícita do autor sobre os limites da própria arquitetura que está ensinando.

**Claim:** O padrão *Interface Segregation Principle* (o "I" do SOLID) é deliberadamente relaxado no exemplo: em vez de uma interface por conjunto mínimo de operações, o autor usa interfaces mais "gordas" (ex.: `UserRepository` único com `findByEmail`, `add`, `findAll`) por simplicidade, com plano de quebrá-las apenas se realmente incharem — postura que o autor atribui ao próprio Robert Martin em cursos na cleancoders.com.
**Evidence:** Cap. 7 (nota de rodapé 1). Mesma lógica se aplica à interface `UseCase`, genérica para qualquer caso de uso, em vez de uma interface por caso de uso — trade-off explícito entre simplicidade de teste (fácil criar stubs genéricos) e segurança de tipos (risco de injetar o caso de uso errado em um `ControllerOperation`).
**Confidence:** alta — decisão de projeto documentada com justificativa e trade-off explícito.

**Claim:** Na camada de Adaptadores de Interface, adaptadores que se comunicam *diretamente* com serviços externos (ex.: driver do MongoDB) NÃO pertencem a essa camada, mesmo sendo "adapters" no sentido do design pattern — pertencem à camada de Frameworks & Drivers, porque dependem diretamente de infraestrutura, o que violaria a Regra de Dependência se ficassem na camada de Adaptadores de Interface.
**Evidence:** Cap. 8. A camada de Adaptadores de Interface contém, no exemplo, apenas `WebController` (implementado com uma variação do padrão Template Method via composição, não herança — decisão explicitamente alinhada com a recomendação "favoreça composição sobre herança" do livro GoF) e o middleware de autenticação/autorização baseado em JWT.
**Confidence:** alta — distinção arquitetural fina, explicada com justificativa direta pela Regra de Dependência.

**Claim:** ORMs que exigem anotação direta das entidades de domínio (ex.: decorators de classe) violam a Regra de Dependência; o padrão *Active Record* aplicado a entidades de domínio é considerado "impossível" dentro da Arquitetura Limpa, mas aceitável se aplicado a estruturas de dados (DTOs) na camada externa.
**Evidence:** Cap. 9 (Frameworks & Drivers, seção sobre ORMs). O autor argumenta que objetos e estruturas de dados são conceitualmente opostos (citando o post "Classes vs. Data Structures" de Robert Martin/Uncle Bob): objeto = funções operando sobre dados implícitos; estrutura de dados = dados explícitos operados por funções implícitas. Alternativa viável: ORMs com definição de schema separada das entidades, mantendo o schema na camada de Frameworks & Drivers.
**Confidence:** alta — posição doutrinária clara, com fonte primária citada (Robert Martin) e alternativa prática oferecida.

**Claim:** O repositório de usuários do estudo de caso usa MongoDB (schemaless) por simplicidade; o autor reconhece explicitamente que a implementação não trata de concorrência (ex.: edição simultânea da mesma nota em dois dispositivos) e propõe como alternativas mais robustas o padrão *Unit of Work* combinado com *Repository* (Fowler), ou operações atômicas em nível de repositório/caso de uso/controlador.
**Evidence:** Cap. 9. Também reconhece uma decisão técnica imperfeita mantida deliberadamente: `findByEmail` retorna `null` quando o usuário não é encontrado, em vez de usar `Either<NotFoundError, UserData>` — o autor relata ter começado a refatorar isso e desistido no meio do caminho, usando o próprio livro como exemplo de que sistemas reais nunca estão em estado "perfeito".
**Confidence:** alta — autocrítica documentada explicitamente pelo autor, útil como estudo de caso de decisão de projeto imperfeita mas consciente.

## Entidades e Conceitos Mencionados

- **Pessoas/entidades:** Robert C. Martin (Uncle Bob), Alistair Cockburn, Trygve Reenskaug, James Coplien, Ivar Jacobson, Martin Fowler, Eric Evans, Mark Richards, Neal Ford, Dan North, Maurício Aniche (autor do prefácio), Khalil Stemmler, Scott Wlaschin, Chris Kiehl, David Parnas.
- **Empresas citadas com uso de arquitetura desacoplada:** iFood, Netflix, Uber, Amazon, Mercado Livre, Nubank.
- **Conceitos centrais:** [[wiki/concepts/clean-architecture]], Arquitetura Hexagonal (Ports & Adapters), DCI (Data, Context, Interaction), BCE (Boundary, Control, Entity), Regra de Dependência, Value Object, Either monad, Repository pattern, Template Method (via composição), Humble Object, MVP (Model-View-Presenter), Domain-Driven Design (regras de domínio vs. aplicação), Inversão de Dependência (SOLID), Conway's Law / Inverse Conway Maneuver.

## Open Questions

- O livro não trata de estratégias de concorrência/locking em repositórios (reconhecido explicitamente pelo autor como fora de escopo) — fica em aberto como a Arquitetura Limpa se combina formalmente com Unit of Work em TypeScript/Node.js.
- As afirmações sobre uso de Arquitetura Limpa em iFood, Amazon, Mercado Livre e Nubank são anedóticas (conversas pessoais do autor), sem fonte publicada verificável — tratar com confiança média, ao contrário dos casos Netflix/Uber que citam posts de engenharia públicos.
