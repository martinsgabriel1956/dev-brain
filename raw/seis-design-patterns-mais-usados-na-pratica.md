# Seis Design Patterns Mais Usados na Prática

**Fonte:** Vídeo do YouTube (transcrição de áudio, PT-BR)
**Tema:** Design Patterns — os seis mais usados no mundo real, segundo a experiência do autor
**Data de adição:** 2026-08-06

---

## Introdução

Mesmo código, mesmo problema, mesmo resultado — mas manter um deles é horrível, enquanto o outro é muito mais simples de manter e evoluir. A diferença entre os dois é o uso de design patterns. O vídeo mostra os seis mais usados no mundo real, na experiência do autor.

Antes de entrar nos patterns, uma explicação do que eles são: pensa na planta de uma casa. Você não inventa do zero como construir uma cozinha toda vez que projeta uma casa — existem soluções já testadas milhões de vezes, que todo arquiteto e empreiteiro conhece. Design Patterns funcionam do mesmo jeito, só que para código: são soluções reutilizáveis para problemas que aparecem toda hora na construção de software.

O termo ficou famoso em 1994, quando quatro autores (o **Gang of Four**) publicaram um livro descrevendo 23 padrões. Mas não precisa decorar os 23 — na prática, uns seis são mais usados que os outros.

---

## 1. Observer

Imagina que você se inscreve num canal do YouTube e ativa o sino. Toda vez que o canal posta um vídeo novo, você recebe uma notificação — não precisa ficar entrando no canal toda hora para ver se tem coisa nova, o YouTube te avisa. Esse é o padrão **Observer**.

Tem um objeto que é o **subject** (nesse caso, o canal) e tem os **observers** (os inscritos). Quando o estado do subject muda, todos os observers são notificados automaticamente. Na prática, o subject mantém uma lista de observers; quando algo muda, ele percorre essa lista e chama um método de cada observer, tipo um `update` ou `notify`:

```javascript
// subject
const channel = {
  observers: [],
  on(event, observer) {
    this.observers.push({ event, observer });
  },
  emit(event, data) {
    this.observers
      .filter(o => o.event === event)
      .forEach(o => o.observer(data));
  }
};
```

O `on` registra um observer, o `emit` notifica todos os observers daquele evento.

Você provavelmente já usa isso todo dia sem perceber: `addEventListener` é um observer, o `EventEmitter` do Node.js é um observer, e até o `useEffect` do React segue essa ideia — ele reage quando uma dependência muda.

**Quando usar:** em vez de só chamar uma função direto, a resposta está no desacoplamento. O subject não precisa saber quem tá escutando nem quantos observers existem. É bem útil quando módulos diferentes do sistema precisam reagir ao mesmo evento.

---

## 2. Factory

Quando o problema não é reagir a mudanças, mas sim criar objetos de forma flexível: imagina que você vai numa pizzaria e pede uma marguerita. Você não entra na cozinha para escolher a massa, preparar o molho e montar a pizza — você só diz o que quer e a cozinha entrega pronto. Esse é o **Factory Pattern**.

Você delega a criação de objetos para um método ou classe especializada. Quem pede o objeto não precisa saber os detalhes de como ele é construído ou implementado.

Exemplo: um sistema de pagamentos onde, dependendo do tipo (Pix, cartão, boleto), você precisa usar um processamento diferente — cada um com sua lógica específica. Sem a factory, toda vez que você precisasse de um pagamento teria que colocar esse switch no meio do código. Com a factory, fica tudo centralizado e isolado — se amanhã aparecer um novo tipo de pagamento, você muda num lugar só.

A diferença fica clara quando a codebase vai crescendo: sem factory, a lógica de criação vai ficando espalhada; com factory, fica num lugar só, e o resto do código nem sabe qual classe está sendo usada.

No mundo real: `document.createElement` no browser é uma factory. Frameworks de teste como Jest usam factories para criar mocks. É um dos padrões mais comuns porque criar objetos é algo que quase todo sistema faz.

---

## 3. Singleton

Quando você precisa garantir que um objeto só exista uma vez no sistema inteiro: pensa num prédio com vários andares que tem um elevador — todo mundo usa o mesmo elevador, não faz sentido ter um diferente para cada andar. Esse é o padrão **Singleton**.

Ele garante que uma classe tem apenas uma instância e oferece um ponto global de acesso a ela. O constructor é privado — ninguém consegue dar `new Database()` direto. A única forma de obter a instância é pelo `getInstance()`: na primeira vez que chamar, ele cria; nas próximas vezes, retorna a mesma instância. Não importa se é o módulo de usuários, de pedidos ou de relatórios chamando — todos recebem a mesma conexão com o banco.

**Ressalva:** o Singleton é um pouco polêmico. Muita gente considera um anti-pattern, e faz sentido em alguns casos — o maior problema é que ele cria um estado global que dificulta fazer testes e esconde dependências. Por isso, em muitos frameworks atuais o Singleton é implementado pelo contêiner de injeção de dependências, em vez de ser feito na mão — o framework garante que só existe uma instância sem acoplar o código.

Recomendado só para recursos que realmente precisam ser únicos: pool de conexão com o banco, configuração da aplicação, sistema de logs.

---

## 4. Decorator

Quando você quer adicionar comportamento a um objeto sem modificá-lo: pensa nos filtros de fotos do Instagram. Você tira uma foto e aplica um filtro, depois aplica contraste, depois brilho. Cada filtro recebe a imagem anterior e devolve uma nova versão com o efeito aplicado — a foto original continua intacta. O mais importante é que a entrada e a saída são sempre a mesma coisa (uma imagem), então você pode empilhar quantos filtros quiser, na ordem que quiser. Esse é o padrão **Decorator**.

Ele permite adicionar responsabilidades a um objeto de forma dinâmica, envolvendo-o em outro objeto que tem a mesma interface.

Exemplo: um sistema de notificações que começa com e-mail, mas depois também precisa mandar por Slack e por SMS. Em vez de criar uma classe "Deus" gigante que faz tudo, você cria decorators — o `SlackDecorator` recebe um `notifier` no constructor, chama o `send` do objeto original e adiciona a lógica do Slack. Para usar, você vai encadeando; cada camada adiciona comportamento sem mudar as anteriores. E você pode combinar os decorators como quiser: quer só e-mail e SMS, sem Slack? É só não adicionar o `SlackDecorator`.

No JavaScript moderno, os decorators do TypeScript (aqueles com `@`) seguem exatamente esse princípio. O `@Injectable` do Angular, o `@Component` do NestJS — todos são decorators que adicionam comportamento a uma classe sem modificá-la diretamente.

---

## 5. Strategy

Quando você tem um problema que pode ser resolvido de várias formas diferentes e quer trocar a solução sem mudar o resto do código: pensa no GPS. Você quer ir de um lugar para outro, e o app oferece várias opções — carro, bicicleta, transporte público. Cada opção usa um algoritmo diferente para calcular a rota, mas a interface é a mesma — você só escolhe qual estratégia quer. Esse é o **Strategy Pattern**.

Ele define uma família de algoritmos, encapsula cada um e permite a troca entre eles em tempo de execução. A classe `Sorter`, por exemplo, não sabe qual algoritmo está usando — ela só sabe que tem um objeto com o método `sort`. Você pode trocar a estratégia a qualquer momento com o `setStrategy`.

Um caso real que todo mundo já viu: validação de formulários. Cada campo tem uma regra diferente — CPF tem uma lógica, telefone tem outra, senha tem outra. Em vez de colocar tudo isso num `if/else` gigante, cada regra vira uma strategy que o validador pode usar.

No dia a dia, esse pattern está em todo lugar: middleware do Express escolhe qual handler processar; existem estratégias de autenticação no Passport.js; o comparador (`compareFn`) do `Array.sort` do JavaScript é basicamente um strategy.

**Regra prática:** quando a estratégia tem estado ou precisa de vários métodos trabalhando juntos, uma classe faz mais sentido que uma função isolada. Se for só uma operação simples, uma função já resolve.

---

## 6. Adapter

O último pattern do vídeo é usado quando aparece um problema recorrente em projetos reais: você precisa usar uma biblioteca ou uma API externa, mas a interface dela não encaixa no seu código. Como resolver isso sem ter que refatorar tudo?

Imagina que você viaja para o exterior e leva seu carregador. Chega no hotel e a tomada é diferente — o carregador continua funcionando, a tomada também funciona, mas os dois não são compatíveis. Aí você usa um adaptador de tomada: ele não muda o carregador nem a tomada, só faz a conexão entre eles. Esse é o padrão **Adapter**.

Ele converte a interface de uma classe para outra que o código espera, fazendo com que classes que não poderiam trabalhar juntas funcionem sem problemas.

Exemplo: você está integrando com uma API externa que retorna dados de usuário com `first_name` e `last_name`, mas o seu sistema inteiro usa `nome` e `sobrenome`. Você não vai mudar a API externa, mas também não quer mudar todo o seu sistema — a solução é criar um adapter. Os dados entram num formato, passam pelo adapter e saem no formato que o sistema espera.

Isso não serve só para trocar nomes de campo. Digamos que o sistema todo usa o Axios, mas agora você quer usar o `fetch` nativo. Em vez de mudar centenas de arquivos, você cria um adapter que implementa a mesma interface do Axios, mas usa `fetch` por baixo — o resto do código nem percebe que o Axios não está mais sendo usado. A interface continua a mesma, só a implementação por baixo mudou.

No mundo real, o Adapter está em todo lugar: ORMs como Prisma e TypeORM são adapters entre o seu código e o banco de dados; até drivers de banco de dados são adapters — eles traduzem chamadas genéricas para o protocolo específico de cada banco.

---

## Resumo

- **Observer** — vários objetos precisam reagir a uma mudança (eventos do DOM, webhooks, qualquer sistema reativo).
- **Factory** — a criação de objetos é complexa ou varia conforme o contexto (APIs que retornam tipos diferentes, frameworks que instanciam componentes).
- **Singleton** — você precisa de uma instância compartilhada: pool de conexão, configuração ou cache global — mas pense bem antes de usar.
- **Decorator** — adicionar comportamento sem alterar o objeto original: middleware, interceptors, os próprios decorators do TypeScript.
- **Strategy** — trocar algoritmos em tempo de execução: validação, ordenação, ou qualquer lógica que pode variar.
- **Adapter** — conectar interfaces incompatíveis: integração com API externa, migração de bibliotecas, tradução entre formatos de dados.

## Interação entre os patterns

Os patterns podem interagir entre si: uma factory pode criar singletons; um observer pode usar strategy para decidir como notificar; um adapter pode envolver um objeto criado por uma factory. Conforme você vai conhecendo os padrões, começa a enxergar as combinações.

## Ponto mais importante

Não sair enfiando design pattern em tudo. Eles existem para resolver problemas reais, não para deixar o código bonito — se o problema não existe, o pattern também não precisa ser usado.
