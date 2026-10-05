# 3 Tipos de Acoplamento que Atrapalham o Teste Unitário (André Casciotti)

Fonte: transcrição de vídeo do YouTube, quadro de André Casciotti (canal Próximo Nível / curso "Dev que Resolve"). Já em português — sem necessidade de tradução. Transcrição automática colada pelo usuário; foram adicionados apenas pontuação, parágrafos e títulos de seção, e o texto foi limpo de erros de reconhecimento. Os exemplos de código são em C#/.NET.

Termos corrigidos por contexto (transcrição automática): "André Casac" → André Casciotti; "Coda para subir o quadro" → nome do quadro, grafia incerta (mantido como falado); "Dnet" → .NET; "Devoss" → devs; "Mong DB / Mongo Deb" → MongoDB; "cliente mongo repository / client Mongo Repositor" → `ClienteMongoRepository`; "validar cliente" → `ValidarCliente`; "cliente service errado / servrada" → `ClienteServiceErrado` (classe de exemplo, nome propositalmente ruim); "base service" → `BaseService`; "promoção service" → `PromocaoService`; "API Helper / P helper" → `ApiHelper`; "chamar API" → `ChamarApi`; "I collection" → `ICollection`; "moque / mocar" → mock / mockar; "cash" → cache; "refaturação / refaturar" → refatoração / refatorar; "threads / trads" → threads; "Value cannot be new collection" → provável "Value cannot be null (collection)"; "o Dnet / .net" mantidos como .NET; "Devil" → dev; "ASP 3 / VB6" → ASP clássico e VB6; "C#ARP" → C#.

---

## Abertura

Se você já tentou fazer teste unitário de um método e não conseguiu, um dos motivos possíveis é que ele tinha algum tipo de **acoplamento**. O vídeo mostra **três tipos de acoplamento que atrapalham o teste unitário**.

Teste unitário é uma das coisas mais frustrantes da programação: nos estudos tudo parece simples, e quando o dev pega o código de produção o teste dá erro, não passa, não funciona no build. Boa parte disso vem da falta de compreensão de conceitos de arquitetura. O acoplamento é uma das coisas que **de fato impedem o teste**, e uma das grandes dificuldades é **identificar** que ele é um problema — falta conhecimento de arquitetura para reconhecê-lo. O objetivo do vídeo é ensinar a identificar: são poucas situações, mas muitas vezes estão tão embrenhadas no dia a dia que passam despercebidas. Os exemplos são simples; o importante é o conceito.

## Tipo 1 — Usar `new` dentro do método

O mais comum. O método `ValidarCliente` tem um `new ClienteMongoRepository()` e, mais abaixo, um `new List<string>()`.

Cada `new` instancia uma classe física, gerando um objeto a partir dela. Isso cria **acoplamento**: o método depende especificamente de `ClienteMongoRepository` — se a classe não existir, nem compila. É muito comum, principalmente no início da carreira: aprende-se que objeto é instância de classe e que é preciso dar `new` para instanciar.

### A demonstração no debugger

O teste unitário chama `ClienteServiceErrado.ValidarCliente`. Com breakpoint e F11, o fluxo entra no método, instancia o repositório e chama `Obter`. O teste **quebra antes de continuar** — o erro é algo como "Value cannot be null (collection)".

Entrando no `Obter`: ele usa o driver do MongoDB e tenta um `Find`, mas o campo `clienteCollection` (um `IMongoCollection`) **nunca foi preenchido**. Dentro da aplicação, o contexto já carrega tudo (outras classes do projeto montam a conexão, o arquivo de configuração fornece a connection string). No teste unitário **nada disso foi carregado**: só se deu `new ClienteMongoRepository()`. A classe tentou resolver dependências que não tem; e, mesmo que tivesse, o `Find` precisaria ir ao servidor do MongoDB pela rede — servidor que nem está rodando na máquina.

### Por que isso é um problema

- Na máquina do dev talvez funcione (banco rodando, dados lá). Mas num **servidor de build** (GitHub etc.) muitas vezes não há acesso à rede interna; mesmo apontando para um banco de desenvolvimento, não se chega a ele.
- Por isso uma **premissa do teste unitário é não fazer I/O — nem de rede, nem de disco**: o teste deve rodar em qualquer lugar, dependendo só da máquina onde roda (sem depender de rede nem de caminhos de disco iguais).
- Exemplo: o dev roda local com `localhost` na configuração; o colega não tem o MongoDB local (usa o servidor de desenvolvimento) — o teste dele falha.
- O F12 no `new` leva direto à classe: o teste depende **especificamente** dela. O teste quer verificar só a validação do cliente, mas assuntos se misturam: aparecem dependências (MongoDB, configuração, rede) que não deveriam aparecer. **Quanto mais acoplamento, mais coisa é preciso conhecer e montar no teste** — "acoplamento mata teste unitário".
- A reação comum — "então mocko o `IMongoCollection`" — está errada: o teste não depende do `IMongoCollection`, essa dependência nem está visível para ele.

### Solução

A mais fácil das três: em vez de `new`, usar **injeção de dependência**. Aqui já existe uma interface implementada; basta injetá-la, e no teste unitário a dependência pode ser **mockada**. Para identificar o acoplamento: procurar os `new`.

### Nem todo `new` é problema

O `new List<string>()` também é acoplamento, mas **existem dependências desejáveis e indesejáveis**:

- **Desejáveis:** coisas do próprio runtime/framework (`List` do .NET — não é preciso testar se o `List` funciona, e não é necessário trocar por `ICollection` e mockar); e **classes de domínio / de negócio** — quem cria os objetos de domínio é o próprio sistema (mesmo que o input venha de uma tela ou sistema externo, a construção do objeto de domínio é interna ao sistema).
- **Indesejáveis:** acessos externos — as classes de **serviço, utilitárias ou de infraestrutura**, que não dependem do core nem das regras de negócio. Essas devem ficar do lado de fora, atrás de uma **interface**, que reduz o acoplamento.

## Tipo 2 — Acoplamento por herança

Muito comum em sistemas em produção, e a maioria dos devs não percebe que é acoplamento por falta de conhecimento de arquitetura.

Exemplo: `ClienteServiceErrado` herda de `BaseService`. Na `BaseService` há um método `ChamarApi` que instancia `HttpClient`, faz o `Get`, verifica sucesso e desserializa o retorno; também há `ObterDescontoPadraoComHeranca`, que preenche a URL da API de desconto e chama `ChamarApi`. A ideia de quem escreve: "para não repetir o código de chamada HTTP em toda service, crio uma classe base e herdo onde preciso fazer chamadas". Outra classe, `PromocaoService` (um domain service), também herda de `BaseService` e usa `ChamarApi` para buscar valores de outra API externa em `AplicarDescontoPadrao`. Ganha-se reaproveitamento e manutenção em um só lugar — parece elegante.

### A demonstração

O teste de `ObterDescontoPadraoComHeranca` com breakpoint: seta a URL, entra em `ChamarApi`, instancia `HttpClient` e dá `Get` em um endereço que não existe. O teste quebra: **"esse host não é conhecido"** — o teste tentou sair pela rede para chamar a API. Mesmo conceito do tipo 1, só que no lugar do banco de dados é uma API em endereço de rede da empresa; de novo haverá problema na máquina do colega ou no servidor de build.

### Por que é perigoso

A galera acha que está fazendo a melhor coisa ("é herança, é OOP, reaproveito código"). Mas, do ponto de vista do teste, **não há controle sobre o que a classe herdada faz**: não dá para trocar a chamada, não dá para colocar mock, não dá para substituir nada.

Contexto histórico dado pelo autor: no ASP clássico e no VB6 não havia herança (o conceito era quase nulo, misturado com procedural); quando chegou o .NET, a galera "pirou" com polimorfismo e herança e passou a usar indiscriminadamente. Por isso devs mais antigos têm o hábito de usar herança "para não duplicar código", e devs mais novos também acabam achando que é assim que se faz.

### Solução

Quando as chamadas **não dependem do contexto de negócio** (aqui, das services), **não usar herança**: criar uma classe externa, em **outra camada** (infraestrutura / "a parte mais tecnológica"), que implementa a chamada; do lado da service, criar uma **interface** e **injetar** a interface na classe, chamando `ChamarApi` por ela. Ou seja: **composição injetando dependências em vez de herança**.

Não é que não se possa usar herança — pode, dentro do **contexto onde as classes estão**. O erro é herdar de uma classe que embute tecnologia (HTTP, banco, disco): não misturar contextos. "Parece que você está economizando código, mas está prejudicando a aplicação, porque gera acoplamento."

## Tipo 3 — Classes e métodos estáticos

Consequência do segundo. O dev pensa: "então não uso herança; jogo isso em outra classe e chamo dentro do método". Cria então um `ApiHelper` — classe estática com método estático `ChamarApi` — copiando o método da base e trocando a dinâmica; e ainda usa o nome genérico "Helper", que pode ser qualquer coisa.

### A demonstração

O teste "deveria obter desconto padrão cliente com static": F11 entra, constrói a URL, chama direto `ApiHelper.ChamarApi` e quebra **pelo mesmo motivo** ("esse host não é conhecido"). O acoplamento continua lá; só foi movido de `BaseService` para `ApiHelper`.

### Por que gera acoplamento

Quem consome um método estático (mesmo que a classe não seja estática) depende **diretamente** dessa classe e desse método — **não dá para substituir a chamada nem criar mock** no teste. Vale a mesma recomendação do tipo anterior: misturar contexto de tecnologia com contexto de negócio impede o teste, porque ele tenta sair pela rede ou acessar disco, rodando na máquina do dev mas não no servidor de build.

### Estático não é proibido, mas exige critério

- Sempre que houver classe estática, questionar se **deveria ser estática de verdade**. Muita gente abusa: cria "helpers" e uma camada *cross* (projeto que todo mundo referencia).
- Não é modelagem ruim — depende do contexto; um projeto pode cruzar várias camadas. O que **não pode é furar limites**.
- **O que é estático vale para a aplicação toda e é iniciado junto com ela**: se gravar uma variável estática (como um cache), ela fica no ar enquanto a aplicação estiver; se apagar, apaga para todo mundo. Há discussões sobre threads, mas "de forma geral o estático vale para a aplicação toda" — por isso não se instancia a classe. É conceito de programação que funciona assim em qualquer linguagem (o autor mostra .NET, e afirma que JavaScript, Java e C# funcionam do mesmo jeito; não afirma para todas as linguagens por não conhecê-las).
- Solução: a mesma da herança — **criar uma classe que se instancia e injetá-la como dependência no construtor**; no teste cria-se um mock para ela.

## Conclusão

- O objetivo do vídeo **não é mostrar as soluções**, e sim fazer entender como o acoplamento funciona e por que é um problema para o teste unitário.
- Círculo vicioso (gato e rato / ovo e galinha): quem não faz teste unitário usa e abusa de recursos que impedem o teste (principalmente herança); quando tenta testar, não consegue porque o código já foi feito assim; precisa refatorar, não sabe ou não tem tempo, deixa quieto, e continua alimentando o acoplamento.
- Inversamente, **quando se faz teste unitário o problema vai sumindo naturalmente**: como acoplamento impede o teste, o dev se vê forçado a aprender a escrever código com acoplamento mais baixo. O essencial é ter o **gatilho de enxergar o problema** — o autor apresenta as três situações mais comuns e não sabe dizer se há outras; cita um **quarto tipo, acoplamento por processo**, mais difícil e que às vezes não impede o teste. Estes três **impedem** o teste unitário.
- Conselho prático: observar no código do dia a dia onde esses três pontos aparecem (principalmente herança, "tenho certeza que você tem alguma coisa aí"), tentar escrever teste unitário nesses casos e ver na prática; **antes de corrigir, aprender a identificar** — "isso vem de conhecimento de base, por isso eu falo sempre que conhecer os fundamentos é muito importante". Entender o runtime da linguagem para evitar o problema.
- Fecho promocional: curso "Dev que Resolve" (arquitetura para devs, não para arquitetos, e teste unitário na prática); pedidos de like, comentário e inscrição.
