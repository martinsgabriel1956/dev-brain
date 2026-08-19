# Arquitetura Limpa: Por Que Ela É Tão Popular

Transcrição de vídeo (pt-BR, sem necessidade de tradução), limpa e organizada em seções.

## Abertura

A ideia do vídeo é falar sobre arquitetura limpa (Clean Architecture) e, principalmente, sobre por que ela é tão popular. O vídeo vai:

- Contrastar Clean Architecture com algumas alternativas (outras arquiteturas populares).
- Mostrar um exemplo na prática de como ela se tornou tão popular e por que é tão adorada.
- Mostrar pontos negativos, para entender quando faz sentido usar e quando não faz.

(Bloco de patrocínio de ferramenta de IA/IDE — omitido, sem relevância técnica para a wiki.)

## O nome é tendencioso

O nome "Arquitetura Limpa" é um pouco tendencioso, porque o oposto disso deixa implícito que todas as outras são "sujas" — o que não é bem o caso. Toda codebase, se começada sem nenhum tipo de padrão ou estrutura a ser seguida, vai crescer para virar um caos: lógica de negócio nos controllers, lógica que deveria estar no banco de dados espalhada pela aplicação inteira, mudança na UI quebrando a lógica de negócios, e adicionar uma feature simples se torna arriscado porque pode quebrar tudo.

Isso é basicamente código legado. E código legado muitas vezes chega nesse estado porque ou nenhum padrão foi seguido, ou o padrão foi se deteriorando ao longo dos anos — conforme o código passa de mão em mão, é natural que a intenção de algumas coisas criadas seja mal compreendida, e vai havendo uma deterioração natural. Não é necessariamente culpa da empresa nem dos funcionários — é difícil segurar a entropia de uma codebase, é difícil passar a informação de mão em mão sem que nada se perca.

## O que a Arquitetura Limpa resolve

A Arquitetura Limpa vem para resolver:

1. **Acoplamento** — o principal ponto: desacoplar o código.
2. **Instabilidade que vem do acoplamento.**
3. **Lentidão natural de desenvolvimento** — uma codebase no início desenvolve rápido; quanto mais tempo passa, mais devagar fica desenvolver nela, porque qualquer mudança arrisca quebrar tudo e exige testar muito mais. Se algum tipo de arquitetura limpa for seguido, dá para prevenir que a codebase fique lenta de se trabalhar (lentidão de desenvolvimento, não de execução do código).

A ideia central: **a regra de negócio não depende de detalhes externos**. Se isso for seguido à risca, o banco de dados fica separado, e em algum lugar da aplicação — geralmente chamado de "entidades"/"domínio" (às vezes "use cases") — ficam concentradas as regras de negócio. Essas regras não dependem se você está usando Postgres, MongoDB, ou até uma API externa/Supabase.

## Estrutura de pastas típica

Arquitetura de software não é estrutura de pastas — mas a estrutura de pastas geralmente reflete a arquitetura. Uma simplificação comum (sem contar DTOs, Mappers etc.):

- **Entidades** (ou algo parecido)
- **Use Cases** (casos de uso)
- **Interfaces / Adapters** (ports and adapters: adapters em cima, ports embaixo — ou simplesmente "interfaces")
- **Infraestrutura**

A árvore de dependência é de cima para baixo: infra pode depender de interface, use case pode depender de entidade — nunca o inverso. Cuidado especial com dependências circulares.

## Exemplo prático: `create-user`

- **Entidade `User`**: sem nenhuma dependência externa. Só um `init` que recebe e-mail, por exemplo — algo simples.
- **Use case `CreateUser`**: depende da entidade `User` e depende da **interface** `UserRepository` (não da implementação concreta) — porque para criar um usuário é preciso do modelo de usuário e é preciso salvar isso em algum repositório.
- Ao clicar em `UserRepository`, cai-se na abstração: uma interface, uma declaração de como algo vai ser feito, sem implementação nenhuma.

### Por que separar interface de implementação (ex.: Postgres)

Se o use case dependesse diretamente do adapter concreto (ex.: `PostgresUserRepository`), toda vez que o caso de uso mudasse, ou que se quisesse trocar de banco de dados, seria necessário alterar **todos** os casos de uso que usam esse repositório. Numa aplicação real com, por exemplo, 150 casos de uso, isso geraria um trabalho gigantesco.

Outro problema: se o repositório for instanciado diretamente dentro do use case (`self.repository = PostgresUserRepository()`), fica impossível testar com um repositório mockado ou um banco de dados diferente sem gambiarra.

**Solução — injeção de dependência**: passar o repositório como parâmetro do use case. Isso é, na prática, injeção de dependência: o use case é agnóstico em relação ao Postgres, e o Postgres (adapter) é agnóstico em relação ao use case. Ambos dependem em conjunto apenas da interface `UserRepository`. Como não há dependência direta, qualquer implementação que satisfaça essa interface pode ser usada — seja Postgres, MongoDB, uma API externa, Supabase etc. A interface diz apenas: "você precisa ter um método `save` que recebe um `user` e salva, retornando `void`."

Essa prática de programar contra interfaces, não contra implementações, é a grande força da Arquitetura Limpa — e é aplicada em quase todas as camadas.

## Pontos fortes

- **Testabilidade** — um dos maiores motivos de a arquitetura ser tão usada. Injeção de dependência via interfaces permite trocar implementações reais por mocks nos testes.
- **Independência de frameworks** — a lógica é agnóstica em relação ao framework usado.
- **Manutenibilidade.**
- **A lógica de negócio fica no centro de tudo**, como um cidadão de primeira classe: uma camada protegida e isolada, não dispersa pela aplicação inteira.

## Pontos negativos

- **Verbosidade e boilerplate**: no exemplo, quatro arquivos/pastas para implementar algo que poderia ter sido feito em quatro ou cinco linhas de código. Um exemplo mínimo de Arquitetura Limpa já gera uma quantidade grande de abstrações.
- **Risco de abstrações ruins**: uma das partes mais difíceis do trabalho de desenvolvedor é criar boas abstrações. Quanto mais abstrações se cria, maior a chance de que algumas sejam ruins.
- **Setup inicial mais complexo.**
- **Dificuldade de debugar**: o `CreateUser` é instanciado em algum lugar distante da aplicação; para descobrir onde a implementação real de `save` está rodando, é preciso rastrear onde o use case foi instanciado e qual repositório concreto foi passado como parâmetro — a implementação não está visível diretamente na interface.
- **Trade-off de tempo de vida do projeto**: o investimento inicial precisa se pagar ao longo do tempo. Para uma aplicação que dura poucos meses, pode não valer a pena. Para uma aplicação que dura anos, tende a se pagar com manutenibilidade — desde que a regra de negócio não vaze para outras partes do sistema.
- **Pode brigar com convenções de frameworks opinativos** (Rails, Django, Laravel). Frameworks mais MVC podem exigir "lutar contra" os padrões do próprio framework para impor Clean Architecture.

## Comparação com arquiteturas alternativas

- **Hexagonal (Ports and Adapters)**: muito parecida com Clean Architecture na opinião do autor. A diferença é que a Hexagonal fala em "domain" ao invés de "entidades e use cases", mas na prática as implementações ficam muito similares.
- **Onion / Arquitetura em Camadas (Layers)**: popular também no ecossistema NestJS. Não muito diferente de Hexagonal nem de Clean Architecture — círculos concêntricos em que as dependências sempre apontam para dentro, para a lógica de domínio. Em comum entre essas arquiteturas: o domínio não depende de nada, e as implementações concretas ficam nas folhas da árvore, não no centro.
- **Layered (Presentation / Business / Data Access)**: separação em camadas — apresentação, lógica de negócio, acesso a dados. Tem um pouco menos de abstrações, é um pouco mais simples e mais rápido para aplicações CRUD. No geral, a lógica de negócio fica isolada do acesso a dados, e a apresentação costuma estar isolada de ambos — tem relação com MVC.
- **DDD (Domain-Driven Design)**: nem chega a ser uma "arquitetura" no mesmo sentido, porque não é tão prescritivo. Tema grande demais para cobrir neste vídeo — fica para um vídeo dedicado.
- **MVC, CQRS**: citados brevemente. CQRS é bastante usado por quem trabalha com ledger/fintech.

## Conclusão

Esses conceitos de arquitetura são valiosos, mas a Arquitetura Limpa não é necessariamente melhor ou pior que as outras nos méritos técnicos — ela é adequada para alguns tipos de projeto, assim como as demais. Na visão do autor, ela ficou tão popular principalmente por causa do livro de Robert C. Martin (Uncle Bob), que é uma figura muito popular e ajudou a popularizar ainda mais essa arquitetura.
