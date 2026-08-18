# Facade Pattern — Código Fonte TV (transcrição)

> Transcrição de vídeo em português. Texto bruto de reconhecimento de fala, sem pontuação e com erros de ASR. Limpa, pontuada e organizada em seções abaixo, preservando a estrutura original: introdução conceitual → modelagem do sistema de exemplo → implementação "antes" (sem Facade) → discussão de SOLID → implementação "depois" (com Facade) → variações → conclusão sobre uso/controvérsia.

## Introdução

É mais do que aprender uma linguagem de programação — o importante é saber o que fazer com ela. É nesse terreno escorregadio que os padrões de projeto se encaixam: existem possibilidades praticamente infinitas na solução dos problemas, e os padrões do GoF surgiram justamente para nos ajudar na solução dos mais comuns. Saber quando aplicar é quase uma arte.

Depois do vídeo sobre Strategy, chegou a vez de mostrar na prática mais um design pattern: estamos falando do **Facade** (fachada). A gente perguntou e vocês pediram para repetirmos a dose, então vamos trazer para vocês uma minissérie de aplicação nos principais padrões de projeto, para ninguém nunca mais ter dúvida.

Se você já utilizou Facade nos seus códigos, é bem provável que já tenha visto pessoas dizendo que ele fere os princípios do SOLID e que não passa de um anti-padrão. Pode ser que elas tenham razão — vamos mostrar por que ele é tão controverso, mas mesmo assim é preciso conhecê-lo e saber quando aplicar ou quando não aplicar.

Para este vídeo deixamos de lado o pseudocódigo e vamos utilizar TypeScript. Obviamente não faz diferença qual a linguagem, estamos lidando aqui com orientação a objetos.

## Modelagem do sistema de exemplo

Assim como fizemos no vídeo do Strategy, criamos um pequeno sistema para simular o cenário. O sistema tem alguns models:

- `Cliente` — com atributos `nome`, `usuário`, `email`.
- Alguns outros models que representam, por exemplo, o **Avatar** do cliente, **Documentos** e um **histórico de acesso**.

E tem os `Service`s, que representam integrações — por exemplo, um serviço de banco de dados. O Avatar pode usar um tipo de serviço de armazenamento (S3, Google Drive); um serviço de e-mail para falar com o cliente; o histórico de acesso pode vir de outro serviço; e assim por diante. Cada um desses é um **subsistema**: um conjunto de coisas alinhadas no sistema que, juntas, executam operações complexas — e que a gente quer simplificar para quem for consumir.

O Facade é dividido em dois elementos: o **Facade** propriamente (uma classe que vamos criar) e o **cliente**, que é quem consome essa classe.

## Exemplo de operação: remover um cliente do sistema

Cada serviço tem, por exemplo, um método `remove` próprio. Tudo aqui é simplificado ("fake") para ficar didático, mas a ideia é mostrar o antes e o depois do Facade.

### Antes (sem Facade)

Imagine uma ação de botão dentro do sistema que remove a conta de um cliente. Sem Facade, o código cliente precisaria:

1. Instanciar (ou ter à mão) todos os serviços envolvidos.
2. Chamar o método de remoção de cada um deles, na ordem correta — avatar, documentos, histórico de acesso, etc.

Isso cheira a **LGPD**: a lei diz que, quando o titular solicita a remoção, o responsável pelo sistema tem que retirar as informações dele. Só que isso pode ser estranho em alguns casos — por exemplo, talvez o histórico de acesso não deva ser removido totalmente, porque a lei exige que ele seja mantido por um tempo. Ou seja: a operação de remoção não é um `for` bobo chamando `remove` em tudo — tem regra de negócio no meio.

Por isso a gente precisa de uma camada, uma fachada, que encapsula esse fluxo — mas não necessariamente a ponto de ninguém poder chamar os serviços diretamente. O Facade não encapsula de forma a *impedir* o acesso direto aos serviços; ele só oferece um caminho mais simples. Essa necessidade de usar esse tipo de artifício geralmente aparece quando você está chegando mais perto da camada do cliente.

### Implementando o Facade

Criamos um arquivo `client-facade.ts` (TypeScript). A ideia: a cada método, um `console.log` mostrando o que foi removido — "Avatar do Gabriel foi removido", "Documento foi removido", "Histórico de acesso foi removido" — só para simular que todas as operações foram executadas.

```typescript
// client-facade.ts
import { AvatarService } from "./avatar-service";
import { DocumentService } from "./document-service";
import { AccessHistoryService } from "./access-history-service";

class ClientFacade {
  private cliente: Cliente;
  private avatarService: AvatarService;
  private documentService: DocumentService;
  private accessHistoryService: AccessHistoryService;

  constructor(cliente: Cliente) {
    this.cliente = cliente;
    this.avatarService = new AvatarService();
    this.documentService = new DocumentService();
    this.accessHistoryService = new AccessHistoryService();
  }

  removeConta() {
    this.avatarService.remove(this.cliente);
    this.documentService.remove(this.cliente);
    this.accessHistoryService.remove(this.cliente);
  }
}
```

O construtor recebe o `cliente` e guarda como atributo privado; os outros serviços são instanciados diretamente dentro do construtor (não são injetados). O método `removeConta` executa, em sequência, as operações que antes estavam soltas no código cliente — usamos essa "fachada" para esconder toda aquela complexidade. Essa é a ideia principal do Facade: normalmente a gente até acaba implementando esse padrão sem perceber, sem ter estudado ele antes, justamente porque ele facilita a visualização e utilização do lado do cliente.

Depois de implementado, o código cliente fica assim:

```typescript
const facade = new ClientFacade(cliente);
facade.removeConta();
```

Executa exatamente como antes, mas agora o cliente não precisa saber a ordem nem os detalhes de cada serviço.

## Onde o Facade quebra princípios do SOLID

Ao construir esse exemplo, a implementação acabou quebrando alguns princípios do SOLID:

### Open/Closed Principle (OCP)

Quebrado, porque a gente está trabalhando com implementações concretas e não com interfaces. Isso deixa a manutenção mais complicada. Por exemplo: se eu quiser, além de mandar e-mail, também mandar um SMS, eu tenho que abrir a classe e adicionar mais uma chamada — e cada novo requisito desses é mais uma alteração direto no método. O cliente que chama `removeConta()` fica tranquilo, mas a manutenção por dentro não é trivial.

### Injeção de dependência / acoplamento

No construtor, só o `cliente` é recebido por fora; os outros serviços (`avatarService`, `documentService`, `accessHistoryService`) são instanciados direto dentro da classe. Isso deixa o Facade altamente acoplado às implementações concretas desses serviços — não é uma prática muito interessante. Por outro lado, se a gente fizesse injeção de dependência completa, devolveria a complexidade para quem chama o Facade (teria que passar não só o cliente, mas todos os outros serviços também) — o que anula parte do propósito de simplificação. É por isso que é importante saber quando implementar e como implementar: simplificamos de um lado, mas deixamos pontas soltas de outro.

### Single Responsibility Principle (SRP)

Esse é o mais quebrado, na opinião do autor: o método `removeConta` acaba fazendo muito mais coisa do que deveria. Tem quem defenda que isso não quebra necessariamente o SRP, porque o método em si não sabe *como* cada serviço implementa sua remoção — só orquestra chamadas. Mas, na opinião do autor, quebra sim, "e quebra bonito".

## Variações de implementação

O Facade não tem só essa forma de implementação mostrada. Por exemplo, em vez de instanciar um novo objeto `ClientFacade` toda vez, o método `removeConta` poderia ser **estático** — aí não precisaria de construtor, e o cliente seria passado direto como parâmetro do método estático:

```typescript
class ClientFacade {
  static removeConta(cliente: Cliente) {
    new AvatarService().remove(cliente);
    new DocumentService().remove(cliente);
    new AccessHistoryService().remove(cliente);
  }
}

// uso:
ClientFacade.removeConta(cliente);
```

Isso facilitaria remover múltiplos clientes em sequência (não precisa manter instância), mas continua levando a complexidade para dentro de um método mais simples — e algo vai sofrer na manutenção de qualquer jeito.

Vale lembrar também que o Facade não é só uma ponta client-side. Pode haver mais de uma fachada no meio do caminho — por exemplo, uma `ClienteComunicacao` que por dentro tem um método que decide se envia e-mail ou SMS, e essa fachada por sua vez é chamada por outra fachada mais alta (Facade dentro de Facade).

## Conclusão: usar ou não usar?

A questão de usar ou não Facade é controversa. Na opinião do autor, os princípios do SOLID devem ser respeitados ao máximo, mas há situações em que a complexidade é grande demais para deixar só na camada do cliente — e aí o Facade acaba sendo uma solução possível, ou um "meio-termo" para compensar. Mas nem sempre é viável, por conta da complexidade real que ele introduz por dentro. É um padrão bem controverso — por isso o convite para os espectadores darem sua opinião e dizerem que outros padrões de projeto querem ver na série.

(Encerramento: convite para curtir, comentar, se inscrever no canal, e menção a este ser o segundo vídeo da minissérie de design patterns, após o de Strategy.)
