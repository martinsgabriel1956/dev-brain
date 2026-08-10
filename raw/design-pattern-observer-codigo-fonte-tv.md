# Observer Pattern — Código Fonte TV (transcrição)

> Transcrição de vídeo em português. Texto bruto de reconhecimento de fala, sem pontuação e com nomes deformados pelo ASR (ex.: "gang of War" por "Gang of Four", "PTS" por ".ts"). Limpa, pontuada e organizada em seções abaixo, preservando a estrutura original: introdução conceitual → diagrama → exemplo 1 (genérico, com Deno) → exemplo 2 (YouTube, mais próximo do mundo real) → encerramento.

## Introdução

Quem nos acompanha sabe que aqui no canal nós colocamos a mão no código para mostrar alguns conceitos e exemplos práticos de patterns, como o Strategy, o Facade e o Singleton. Agora chegou a vez de falarmos do padrão Observer, que a propósito pode ser conhecido por vários nomes: Event Subscriber, Listener, Publish-Subscribe, ou apenas Pub/Sub pros mais íntimos.

Ele é um padrão de comunicação entre objetos, por isso é usado justamente quando você precisa estar ciente das alterações de um outro objeto.

Para te ajudar a entender, podemos também recorrer à famosa Gang of Four, que diz que o Observer define uma dependência um-para-muitos entre objetos, para que, quando um objeto mudar de estado, todos os seus dependentes sejam notificados e atualizados automaticamente.

Qualquer rede social pode ser um bom exemplo de Observer na vida real: se você nos segue lá no Código Fonte TV, no Instagram, isso quer dizer que você quer receber as atualizações da nossa conta, ou seja, receber os conteúdos que postamos por lá.

## Diagrama e estrutura geral

Para poder mostrar um pouco melhor visualmente o que vamos fazer aqui, criamos um diagrama através do draw.io (que tem até uma extensão pro VS Code). Vamos criar duas interfaces: uma que representa o `Subject` e outra que representa o `Observer`. E vamos implementar classes através dessas interfaces, implementando os métodos `subscribe`, `unsubscribe`, `unsubscribeAll`, `notify` e `notifyAll`. Eles são responsáveis por colocar os observers dentro do subject, e depois vamos implementar isso de forma a criar os observers e ver como seria isso na prática.

Para isso vamos utilizar TypeScript, então é necessário ter conhecimento de orientação a objetos. E para rodar esse código todo vamos usar o Deno. Vale lembrar que separamos isso em pastas para ficar mais simples de entender: para as interfaces, `i-observer.ts` e `i-subject.ts`; nas classes, `Observer` e `Subject`. Para a gente ver isso tudo rodando, vamos criar na raiz um arquivo chamado `index.ts`.

Antes de implementar tudo, a ideia geral do `index.ts`: com o subject na mão, adicionamos observers a ele (`subscribe`) e depois fazemos a notificação chamando `subject.notifyAll()`.

## Exemplo 1 — implementação genérica (Deno)

### Interface `IObserver`

De acordo com o diagrama, o Observer só tem um método:

```typescript
// i-observer.ts
export interface IObserver {
  update(): void;
}
```

### Interface `ISubject`

```typescript
// i-subject.ts
import { IObserver } from "./i-observer.ts";

export interface ISubject {
  subscribe(observer: IObserver): void;
  unsubscribe(observer: IObserver): void;
  unsubscribeAll(): void;
  notify(observer: IObserver): void;
  notifyAll(): void;
}
```

### Classe `Observer`

```typescript
// observer.ts
import { IObserver } from "./i-observer.ts";

export class Observer implements IObserver {
  constructor(public readonly id: string) {}

  update(): void {
    console.log(`Observer ${this.id} foi atualizado`);
  }
}
```

No mundo real, esse `update` pode ser algo muito mais complexo do que um `console.log`.

### Classe `Subject`

```typescript
// subject.ts
import { IObserver } from "./i-observer.ts";
import { ISubject } from "./i-subject.ts";

export class Subject implements ISubject {
  private observers: IObserver[] = [];

  subscribe(observer: IObserver): void {
    this.observers.push(observer);
  }

  unsubscribe(observer: IObserver): void {
    this.observers = this.observers.filter((o) => o !== observer);
  }

  unsubscribeAll(): void {
    this.observers = [];
  }

  notify(observer: IObserver): void {
    observer.update();
  }

  notifyAll(): void {
    this.observers.forEach((observer) => this.notify(observer));
  }
}
```

`subscribe` insere no array; `unsubscribeAll` zera o array (o autor considerou usar `filter` também para tirar todo mundo, mas zerar é mais direto); `notify` chama `update` de um único observer; `notifyAll` itera o array chamando `notify` para cada um.

### `index.ts` — rodando o exemplo

```typescript
// index.ts
import { Observer } from "./classes/observer.ts";
import { Subject } from "./classes/subject.ts";

const observer1 = new Observer("1");
const observer2 = new Observer("2");
const observer3 = new Observer("3");

const subject = new Subject();

subject.subscribe(observer1);
subject.subscribe(observer2);
subject.subscribe(observer3);

console.log("notifyAll");
subject.notifyAll();

subject.unsubscribe(observer2);

console.log("notifyAll again");
subject.notifyAll();
```

Rodando com `deno run index.ts`: no primeiro `notifyAll`, os observers 1, 2 e 3 são notificados (cada um faz seu `console.log`). Depois o observer 2 é desinscrito (`unsubscribe`), e no segundo `notifyAll` só os observers 1 e 3 são notificados.

Esse primeiro exemplo foi um aquecimento, para fixar o conceito antes de ir para um exemplo mais próximo do mundo real.

## Exemplo 2 — notificação de vídeo do YouTube

Vamos implementar novamente as duas interfaces, com a diferença de que agora o `update` recebe um `Video` por parâmetro — como se fosse uma notificação de vídeo novo do próprio YouTube.

Existem vários tipos de implementação possíveis para esse cenário; o autor escolheu a que achou mais didática. A partir da interface `IObserver` teremos duas implementações: `Subscriber` (o papel do inscrito de um canal) e `Feed` (o YouTube também gera um feed que é atualizado a cada vídeo novo publicado). Ou seja: para cada notificação de vídeo novo, existe mais de um tipo de observer — não existe só um tipo de observer quando se está lidando com esse design pattern.

Estrutura de pastas: criada uma pasta `youtube/`, novamente separada em `interfaces/` e `classes/`.

### Interfaces (variante com `Video`)

```typescript
// youtube/interfaces/i-observer.ts
import { Video } from "../classes/video.ts";

export interface IObserver {
  update(video: Video): void;
}
```

```typescript
// youtube/interfaces/i-subject.ts
import { IObserver } from "./i-observer.ts";

export interface ISubject {
  subscribe(observer: IObserver): void;
  unsubscribe(observer: IObserver): void;
  unsubscribeAll(): void;
  notify(observer: IObserver, video: Video): void;
  notifyAll(video: Video): void;
}
```

### Classe `Video`

A classe mais independente — só tem atributos, sem depender de nada. No mundo real seria maior e provavelmente dividida em outras classes; aqui é só um exemplo didático. Graças ao suporte do TypeScript a parâmetros de construtor como atributos públicos (recurso presente também em outras linguagens, como Dart), não é necessário atribuir campo a campo manualmente.

```typescript
// youtube/classes/video.ts
export class Video {
  constructor(
    public readonly id: string,
    public readonly title: string,
    public readonly thumbnail: string,
    public readonly link: string,
  ) {}
}
```

### Classe `Subscriber`

Um observer que representa o inscrito no canal. Poderia receber várias informações do inscrito; aqui só `id` e `nome`.

```typescript
// youtube/classes/subscriber.ts
import { IObserver } from "../interfaces/i-observer.ts";
import { Video } from "./video.ts";

export class Subscriber implements IObserver {
  constructor(
    public readonly id: string,
    public readonly name: string,
  ) {}

  update(video: Video): void {
    console.log(`${this.name} foi notificado sobre o vídeo: ${video.title}`);
  }
}
```

Esse `update` é uma rotina que provavelmente faria muito mais coisa no mundo real — aqui só registra o nome do observer e o nome do vídeo em que ele está sendo notificado.

### Classe `Feed`

Outro tipo de observer, com atributos diferentes: o feed do YouTube usa o `channelId` do canal, e monta uma URL própria a partir dele.

```typescript
// youtube/classes/feed.ts
import { IObserver } from "../interfaces/i-observer.ts";
import { Video } from "./video.ts";

export class Feed implements IObserver {
  public url: string;

  constructor(public readonly channelId: string) {
    this.url = `https://youtube.com/feed/${channelId}`;
  }

  update(video: Video): void {
    console.log(`O feed foi atualizado sobre o novo vídeo: ${video.title}. Nova URL: ${this.url}`);
  }
}
```

Cada observer tem seu próprio `update` personalizado — o `Subscriber` recebe uma notificação pessoal, o `Feed` atualiza sua URL e registra a atualização.

### Classe `VideoNotification` (o Subject)

Implementação idêntica ao `Subject` do primeiro exemplo, com a diferença de que aqui a classe `Video` é importada e passada para os observers no momento da notificação.

```typescript
// youtube/classes/video-notification.ts
import { IObserver } from "../interfaces/i-observer.ts";
import { Video } from "./video.ts";

export class VideoNotification {
  private observers: IObserver[] = [];

  subscribe(observer: IObserver): void {
    this.observers.push(observer);
  }

  unsubscribe(observer: IObserver): void {
    this.observers = this.observers.filter((o) => o !== observer);
  }

  unsubscribeAll(): void {
    this.observers = [];
  }

  notify(observer: IObserver, video: Video): void {
    observer.update(video);
  }

  notifyAll(video: Video): void {
    this.observers.forEach((observer) => this.notify(observer, video));
  }
}
```

### `youtube/index.ts` — rodando o exemplo

```typescript
// youtube/index.ts
import { Video } from "./classes/video.ts";
import { VideoNotification } from "./classes/video-notification.ts";
import { Subscriber } from "./classes/subscriber.ts";
import { Feed } from "./classes/feed.ts";

const video = new Video(
  "abc123",
  "Aprenda a criar um Observer do zero",
  "thumbnail.jpg",
  "https://youtube.com/watch?v=abc123",
);

const videoNotification = new VideoNotification();

const gabriel = new Subscriber("1", "Gabriel");
const vanessa = new Subscriber("2", "Vanessa");
const juliana = new Subscriber("3", "Juliana Silva");
const feedYoutube = new Feed("codigofontetv");

videoNotification.subscribe(gabriel);
videoNotification.subscribe(vanessa);
videoNotification.subscribe(juliana);
videoNotification.subscribe(feedYoutube);

console.log("Notificando os observers");
videoNotification.notifyAll(video);

videoNotification.unsubscribe(juliana);

console.log("Notificando os observers novamente");
videoNotification.notifyAll(video);
```

Rodando com `deno run youtube/index.ts`: na primeira notificação, Gabriel, Vanessa e Juliana são notificados sobre o vídeo, e o feed do YouTube também é notificado (mostrando a nova URL). Depois Juliana é desinscrita; na segunda notificação, só Gabriel, Vanessa e o feed são notificados.

Durante a gravação, o autor usa o GitHub Copilot como autocomplete e comenta em vários pontos os acertos e erros das sugestões (ex.: sugestão de implementar `Video` com métodos em vez de atributos públicos; nome de variável sugerido incorretamente; import com nome de arquivo errado por causa de sugestão automática) — esses detalhes são de produção do vídeo, não fazem parte do design do pattern em si, e foram omitidos desta transcrição limpa.

## Encerramento

O padrão Observer, um design pattern comportamental, é empregado amplamente — não só em event handlers, mas em sistemas bem mais complexos que utilizam Pub/Sub, como o Kafka, por exemplo.
