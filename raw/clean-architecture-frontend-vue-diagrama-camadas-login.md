# Clean Architecture no Frontend — Diagrama de Camadas Aplicado a uma Tela de Login (Vue.js)

Transcrição de aula em vídeo (pt-BR, sem necessidade de tradução), limpa e organizada em seções. O áudio original veio de reconhecimento de fala automático com diversos erros de transcrição — em especial o nome do framework **Vue** foi capturado foneticamente como "iate", "iett", "yakult" e "vert", e a sigla **API** como "pel", "ap", "apehit". Esses termos foram corrigidos no texto abaixo com base no contexto (o instrutor menciona explicitamente "hooks", Vue Router, axios e uma API feita em Node desenvolvida em outro curso do mesmo autor).

## Abertura — por que falar de arquitetura antes de escrever código

Antes de começar a escrever o código do projeto, a aula é dedicada a discutir arquitetura e como dividir a responsabilidade dos componentes. O primeiro exemplo do projeto vai ser uma tela de login — algo muito comum em projetos atuais.

Frameworks como Vue dão muita facilidade através dos **hooks** e da simplicidade de fazer requisições com axios. Isso facilita fazer tudo dentro do próprio componente Vue: validação de campo, gravação de dados em cache, navegação, regra de negócio, comunicação com API, tratamento de resposta e de erros da API, toda a parte de renderização de UI, e ainda o controle de estado (a chamada **programação reativa** — toda vez que se altera o input, isso reflete numa variável da tela e vice-versa, sem precisar mapear manualmente).

Essa sincronização automática entre componente e variável de estado é o motivo pelo qual o Vue foi criado — evitar que o desenvolvedor precise mapear manualmente cada componente para uma variável. Essa deveria ser a única responsabilidade do componente Vue, mas na prática se acaba colocando muito mais coisa nele, justamente por ser fácil e rápido programar assim.

## Os contras de colocar tudo no componente

Com essa abordagem sem arquitetura:

- Fica muito mais difícil dar manutenção no código.
- Fica difícil reaproveitar código.
- Fica praticamente impossível criar testes unitários — um componente acoplado a tudo isso só permite, no máximo, testes de integração, que são mais lentos e se comunicam com a API de verdade, tornando os testes pouco confiáveis.

Para quem quer trabalhar com uma boa arquitetura, o objetivo principal é conseguir reaproveitar código — e isso simplesmente não é possível nesse modelo. É para resolver isso que existem conceitos de arquitetura como DDD e Clean Architecture, que são parecidos em muitos pontos.

## A ideia central: frameworks são passageiros, a arquitetura deve sobreviver a eles

Hoje o projeto é feito com Vue, e no momento ninguém pensa em trocá-lo — é o framework do momento, usado (segundo o instrutor) por mais de 50% dos desenvolvedores. Mas ninguém sabe o que vai acontecer daqui a um ou dois anos. Anos atrás ninguém cogitava a hipótese de o jQuery deixar de ser usado — era usado por todo mundo, e hoje é usado por quase ninguém, só em código legado.

Essa é a ideia por trás de uma arquitetura bem feita: conseguir reaproveitar 70-80% do código caso o projeto precise trocar de framework — seja porque o Vue não é mais o "framework do momento", seja por trocar o Axios por outra biblioteca de requisição — com o menor custo possível. É para isso que serve a Clean Architecture.

## Camada de Domínio — a regra de negócio

A primeira camada é a **camada de domínio**, onde ficam as regras de negócio. No caso do login, a regra de negócio é **autenticação** — um componente chamado `Authentication`.

Essa camada não é uma classe, e sim uma **interface** (representada no diagrama com uma linha tracejada e arredondada — a convenção do diagrama é que todo elemento tracejado é uma interface). A ideia da camada de domínio é que as regras de negócio sejam definidas como interfaces: a classe de autenticação só declara que precisa de um e-mail e uma senha para autenticar, e que isso retorna um token de acesso.

Como e onde essa autenticação de fato acontece — banco de dados, API, local storage, biblioteca de terceiros — não importa para a regra de negócio. Ela não fica acoplada a nenhum tipo específico de implementação. Esse é o principal ponto da Clean Architecture (e também do DDD).

## Camada de Data — implementação concreta do protocolo

Como implementar essa interface? A camada seguinte é a **Data**, onde ficam as implementações concretas dos casos de uso, usando algum tipo de tecnologia. No exemplo, a autenticação se comunica com uma API externa (desenvolvida em Node em outro curso do mesmo autor).

Essa é uma implementação concreta da interface `Authentication` — usa linha normal (não tracejada) para diferenciar classe de interface. Por convenção, o nome da classe carrega o tipo de implementação: como aqui a implementação busca dados de uma API, ao invés de nomear como `HttpAuthentication`, o instrutor prefere o termo **Remote** — `RemoteAuthentication`.

`RemoteAuthentication` é uma classe que implementa o protocolo do domínio — logo, a camada Data depende do domínio (fluxo de dependência apontando para dentro). O que essa classe faz é basicamente tratar a resposta da API e tratar os erros da API.

### Desacoplando a Data da biblioteca HTTP

Dentro da Data, o `RemoteAuthentication` precisa fazer uma chamada HTTP — mas não deve ficar acoplado diretamente ao Axios (ou fetch, ou qualquer outra biblioteca de requisição). Se amanhã for preciso trocar de biblioteca, seria necessário alterar todos os casos de uso que dependem diretamente dela.

Para desacoplar isso, cria-se **outra interface**, dessa vez pertencente à própria camada Data: um `HttpClient` (ou `HttpPostClient`). Essa interface define a regra de como fazer a requisição — por exemplo, `HttpPostClient` sabe fazer um POST, sem se importar com quem faz esse post ou como ele é feito internamente.

## Camada de Infraestrutura — implementações com bibliotecas externas

A camada de infraestrutura contém implementações que usam frameworks/bibliotecas externas. Aqui entra o `AxiosHttpClient` (ou `AxiosPostClient`) — uma implementação concreta do `HttpPostClient` usando a biblioteca Axios.

Qualquer caso de uso que precise fazer um POST depende apenas da interface `HttpPostClient` — a abstração. A implementação concreta fica isolada na infraestrutura, que depende de uma biblioteca externa (Axios). Nem sempre é obrigatório depender de terceiros nessa camada — poderia, por exemplo, usar `fetch` nativo sem depender de nada externo — mas é aqui que se toma essa decisão.

A infraestrutura implementa o protocolo definido na Data (o `HttpPostClient`) — ou seja, a seta de dependência aponta da infraestrutura para a Data. A infraestrutura só conhece a Data; a Data depende do domínio; e o domínio não depende de ninguém.

Com isso, a comunicação HTTP com a API vira responsabilidade da infraestrutura, e mais uma responsabilidade sai do componente de login.

## Camada de Presentation — o que sobra no componente Vue

A camada de **Presentation** é onde fica de fato o componente de login. Em projetos mais desacoplados que não usam Vue, costuma existir uma camada de Presentation separada da camada de UI — o Presenter pega a resposta vinda da API e converte os dados para o formato que a tela precisa (exemplo clássico: formatar uma data antes de exibi-la), produzindo um **ViewModel** pronto para a View simplesmente renderizar.

Com Vue isso fica mais difícil de separar totalmente — não por ser difícil, mas porque seria "demais": por causa do sistema de reatividade do Vue (um recurso novo e poderoso), separar Presentation de UI significaria abrir mão dos hooks. Por isso o instrutor usa o termo "Presentation" cobrindo tanto a parte de UI quanto a parte de conversão/tratamento de dados — já que o forte do Vue é justamente a reatividade, vale a pena aproveitar esse poder.

O componente de login, na camada de Presentation, depende apenas da interface `Authentication` do domínio — nunca de uma implementação concreta. O domínio é a camada principal da Clean Architecture: as setas de dependência sempre entram para dentro dele, nunca saem. Do Presentation, só se conhece a abstração `Authentication`; alguém precisa fornecer uma classe concreta que implemente esse protocolo (poderia ser uma implementação alternativa vindo de banco de dados, ou uma implementação de teste).

### O que realmente fica no componente de login

As funções que de fato pertencem ao componente Vue de login:

- Renderizar a UI.
- Controlar o estado (o próprio objetivo do Vue — o bind automático dos campos).
- Navegação — usando o sistema de rotas do Vue Router, o componente de login não precisa conhecer nenhum outro componente/página diretamente; ele aponta para uma rota (um `path`), e é o Vue Router quem sabe qual componente/tela de fato renderizar. Isso evita acoplar uma página a outra diretamente.
- (Nesta aula, por simplicidade) Gravar/ler dados do local storage — como salvar o token de acesso recebido da autenticação. O instrutor reconhece que isso também poderia virar um caso de uso isolado (ex.: um caso de uso `SaveAccessToken`, implementado por algo como `LocalSaveAccessToken`, dependendo de um protocolo de armazenamento na camada de domínio, com a implementação concreta na infraestrutura — trocável por cookies, por exemplo). Para não sobrecarregar a aula logo de início, essa refatoração fica para depois; a solução mais simples (acessar o local storage direto no componente) é usada por ora.

Vale notar: nem local storage nem cookies são garantia de solução definitiva — anos atrás cookies eram a solução universal e hoje quase não são mais cogitados para esse tipo de uso; local storage pode um dia ser substituído por outra abordagem mais moderna.

## Camada de Validation — desacoplando a validação de formulário

Ainda falta tratar a **validação**. Apesar de ser tentador usar diretamente uma lib de formulários do Vue (ex.: VeeValidate, Vue Hook Forms) definindo o esquema de validação (campo obrigatório, campo do tipo e-mail) direto na tela, isso torna o componente menos reutilizável — trocar de framework (Angular, React) exigiria reescrever toda a validação.

A solução é criar uma camada própria de **Validation**, com validadores específicos — por exemplo, `RequiredFieldValidation` e `EmailFieldValidation`. O componente de login depende apenas de uma interface (`Validation`), definida na própria camada de Presentation: o protocolo diz que o campo recebe parâmetros X e Y e retorna Z. Quem faz a validação de fato precisa se adaptar a esse protocolo.

Todos os validadores concretos (`RequiredFieldValidation`, `EmailFieldValidation`, validação de senha com mínimo de caracteres, etc.) implementam essa mesma interface. Isso permite aplicar o design pattern **Composite**: como é preciso injetar vários validadores ao mesmo tempo no formulário, cria-se um `ValidationComposite`, que agrupa (compõe) todas as regras de validação que o login precisa.

Com essa camada de Validation isolada, mais duas responsabilidades saem do componente de login.

## Resumo das responsabilidades tiradas do componente

O componente de login começou com aproximadamente dez responsabilidades — talvez mais. Depois da separação em camadas, restam quatro no componente Vue (renderizar UI, controlar estado, navegação e, por ora, cache/local storage). O local storage é um forte candidato a também sair do componente no futuro, seguindo o mesmo padrão aplicado ao `RemoteAuthentication`.

Se amanhã o Vue for trocado por outro framework, permanecem reutilizáveis: toda a validação, toda a regra de negócio (domínio), todo o acesso à API (Data + Infraestrutura). Também são reaproveitáveis os estilos (CSS/SASS) e boa parte do template HTML. O que muda radicalmente de um framework para outro é justamente a parte de controle de estado (cada framework tem sua própria forma de fazer programação reativa) e a parte de ligação (binding) — essas precisariam ser reescritas. Os testes de UI também seriam perdidos nessa troca, mas os testes das camadas isoladas (domínio, data, validation) sobreviveriam intactos — um ganho "de brinde" ao isolar essas camadas.

## A camada Main — o ponto de composição

Por fim, a camada **Main**. No diagrama, não vale a pena desenhar todas as setas de dependência apontando para o Main, porque ele depende de tudo — diferente de todas as outras camadas, que respeitam uma dependência única entre si (infraestrutura → Data → domínio; Validation → Presentation), o domínio não depende de ninguém.

Mas como fazer o login funcionar de fato, se ele depende só de interfaces (`Authentication`, `Validation`)? É preciso de alguém que forneça as implementações concretas — e é essa a função do Main: montar o "quebra-cabeça" usando o design pattern **Factory**. Por exemplo, um `LoginFactory` tem acesso a todos os componentes do sistema — instancia `EmailValidation`, `RequiredFieldValidation`, `RemoteAuthentication`, `AxiosHttpClient` — e monta o componente de login já construído com todas as dependências que ele precisa.

Esse design pattern é chamado de **composição grude** (composition root): o Main é o ponto de entrada da aplicação, e é a única camada que se acopla a todas as outras para permitir que as demais fiquem desacopladas entre si — é preciso "sacrificar" alguém para que o sistema funcione como um todo.

No diagrama, ao invés de apontar o Main para cada componente individual (o que poluiria o diagrama), aponta-se apenas para as camadas (infraestrutura, Data, Validation). O arquivo `index` é o ponto de entrada real da aplicação, que aponta para um componente inicial — o Router, que mapeia toda a aplicação.

## Design patterns e princípios SOLID mencionados

- **Dependency Injection**: a classe não deve criar suas próprias dependências — ela depende de uma abstração, e alguém (o Main, via Factory) injeta a implementação concreta.
- **Single Responsibility Principle (SRP)**: o login começou com múltiplas responsabilidades; a divisão em camadas as quebra em responsabilidades únicas.
- **Dependency Inversion Principle (DIP)**: ao invés do componente de login importar diretamente uma implementação (o que o acoplaria à camada de baixo), cria-se uma interface na própria camada de Presentation — chamada de fronteira (**boundary**) da camada — e a implementação concreta é quem aponta para essa interface, invertendo a direção normal da dependência. É o mesmo mecanismo usado para desacoplar Data de infraestrutura via `HttpClient`.
- **Open/Closed Principle (OCP)**: (mencionado brevemente, com promessa de exemplos práticos ao longo do curso) a ideia de poder adicionar funcionalidade a um componente sem alterá-lo — citado o design pattern **Decorator** como forma de incluir funcionalidade na instância de um objeto sem precisar alterar o próprio objeto.
- **Interface Segregation Principle (ISP)**: (com promessa de aprofundamento numa aula futura sobre o cliente Axios) o exemplo dado é o de um cliente HTTP genérico com métodos `get`, `post`, `put`, `delete` — se `RemoteAuthentication` só precisa de `post`, criar uma interface só com `post` evita ter que implementar (ou mockar em teste) métodos desnecessários. Daí o nome do princípio: segregar (dividir) interfaces grandes em interfaces menores, o que facilita tanto a composição de objetos quanto a criação de testes.

O instrutor promete que, ao longo do curso, todos esses princípios SOLID e diversos design patterns serão aplicados na prática com código, e que a parte de Interface Segregation será aprofundada quando o cliente Axios for implementado.

## Fechamento

O diagrama completo foi feito na ferramenta gratuita draw.io (Google), com um link disponibilizado para os alunos (acesso somente leitura, com possibilidade de download). O instrutor recomenda se acostumar com esse tipo de diagrama de dependências antes de começar a programar, especialmente para quem está começando com arquitetura — desenhar e rascunhar ajuda a esclarecer dúvidas antes da implementação em código.

Todo o conteúdo apresentado aqui é só sobre a tela de login — o curso implementará tudo isso do zero, em código, mostrando a forma mais clara possível de atingir esses objetivos.
