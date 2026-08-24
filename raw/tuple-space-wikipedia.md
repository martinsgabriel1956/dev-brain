# Tuple Space (Wikipédia, traduzido para pt-BR)

Fonte: https://en.wikipedia.org/wiki/Tuple_space

## Introdução

Um **tuple space** (espaço de tuplas) implementa o paradigma de memória associativa para computação paralela/distribuída. Ele fornece um repositório de tuplas que pode ser acessado concorrentemente. Produtores publicam dados como tuplas no espaço, e consumidores recuperam dados que casam com um determinado padrão. Isso também é conhecido como "metáfora do quadro-negro" (blackboard metaphor) e pode ser pensado como uma forma de memória compartilhada distribuída.

Os tuple spaces foram o embasamento teórico da linguagem Linda, desenvolvida por David Gelernter e Nicholas Carriero na Universidade de Yale em 1986.

Implementações foram desenvolvidas para Java (JavaSpaces), Lisp, Lua, Prolog, Python, Ruby, Smalltalk, Tcl e o .NET Framework.

## Object Spaces (Espaços de Objetos)

**Object Spaces** é um paradigma para desenvolver aplicações de computação distribuída caracterizado por entidades lógicas chamadas _Object Spaces_. Todos os participantes compartilham um Object Space. Um provedor de serviço encapsula o serviço como um Objeto e o coloca no Object Space. Clientes acessam o Object Space, identificam qual objeto provê o serviço necessário, e têm a requisição atendida por esse objeto.

Object Spaces como paradigma de computação foi proposto nos anos 1980 por David Gelernter em Yale. Gelernter desenvolveu Linda para suportar o conceito de coordenação global de objetos.

Um Object Space pode ser pensado como um repositório virtual compartilhado entre provedores e acessadores de serviços de rede, abstraídos como objetos. Processos se comunicam atualizando o estado de objetos compartilhados.

Quando um objeto é depositado em um espaço, ele deve ser registrado em um Object Directory. Qualquer processo pode então identificar o objeto por meio de busca de propriedades (properties lookup). Um processo pode esperar até que um objeto seja colocado no Object Space, se necessário.

Objetos depositados em um Object Space são passivos — seus métodos não podem ser invocados enquanto estão no espaço. Um processo acessador deve recuperá-lo para a memória local, usar o serviço, atualizar seu estado, e colocá-lo de volta.

Esse paradigma fornece exclusão mútua de forma inerente. Uma vez que um objeto é acessado, ele é removido do Object Space e substituído somente após ser liberado (release). Nenhum outro processo pode acessar um objeto enquanto ele está sendo usado por outro.

## JavaSpaces

JavaSpaces é uma especificação de serviço que fornece um mecanismo de troca e coordenação de objetos distribuído para objetos Java. Ele armazena o estado de sistemas distribuídos e implementa algoritmos distribuídos. Todos os parceiros de comunicação (peers) se comunicam e se coordenam compartilhando estado.

JavaSpaces pode alcançar escalabilidade por meio de processamento paralelo e fornecer armazenamento confiável de objetos por meio de replicação distribuída. A distribuição pode se estender a locais remotos, embora JavaSpaces seja usualmente empregado em aplicações de baixa latência e alta performance, em vez de cache confiável de objetos.

O padrão de software mais comum usado em JavaSpaces é o padrão Master-Worker. O Master distribui unidades de trabalho para o "espaço", que são lidas, processadas e escritas de volta pelos workers. Ambientes típicos têm vários espaços, múltiplos masters e muitos workers projetados para serem genéricos.

JavaSpaces é parte da tecnologia Java Jini, que não foi um sucesso comercial. A tecnologia encontrou usuários ao longo do tempo, e alguns fornecedores oferecem produtos baseados em JavaSpaces. JavaSpaces permanece uma tecnologia de nicho, usada principalmente nas indústrias de serviços financeiros e telecomunicações. Bill Joy, cofundador da Sun, observou que esse sonho de sistemas distribuídos exigiria "um salto quântico de pensamento".

### Exemplo de uso

O exemplo a seguir mostra uma aplicação usando JavaSpaces. Um objeto a ser compartilhado no Object Space é chamado de _Entry_. Aqui, a Entry encapsula um serviço que retorna a string "Hello World!" e rastreia a contagem de uso. O servidor cria um Object Space (ou JavaSpace) e escreve a Entry nele. O cliente lê a entry, invoca seu método para acessar o serviço, atualiza a contagem de uso, e escreve a Entry atualizada de volta.

```java
// Uma classe Entry
public class SpaceEntry implements Entry {
     public final String message = "Hello World!";
     public Integer count = 0;
 
     public String service() {
         ++count;
         return message;
     }
 
     public String toString() {
         return "Count: " + count;
     }
}

// Servidor Hello World!
public class Server {
     public static void main(String[] args) throws Exception {
         SpaceEntry entry = new SpaceEntry();            // Cria o objeto Entry
         JavaSpace space = (JavaSpace)space();           // Cria um Object Space
         // Registra e escreve a Entry no Space
         space.write(entry, null, Lease.FOREVER);        
         // Pausa por 10 segundos e então recupera a Entry e checa seu estado.
         Thread.sleep(10 * 1000);
         SpaceEntry e = space.read(entry, null, Long.MAX_VALUE);
         System.out.println(e);
     }
}

// Cliente
public class Client {
     public static void main(String[] args) throws Exception {
         JavaSpace space = (JavaSpace) space();
         SpaceEntry e = space.take(new SpaceEntry(), null, Long.MAX_VALUE);
         System.out.println(e.service());
         space.write(e, null, Lease.FOREVER);
     }
}
```

### Livros

- Eric Freeman, Susanne Hupfer, Ken Arnold: _JavaSpaces Principles, Patterns, and Practice._ Addison-Wesley Professional, 1 de junho de 1999, ISBN 0-201-30955-6
- Phil Bishop, Nigel Warren: _JavaSpaces in Practice._ Addison Wesley, 2002, ISBN 0-321-11231-8
- Max K. Goff: _Network Distributed Computing: Fitscapes and Fallacies_, 2004, Prentice Hall, ISBN 0-13-100152-3
- Sing Li, et al.: _Professional Java Server Programming_, 1999, Wrox Press, ISBN 1-86100-277-7
- Steven Halter: _JavaSpaces Example by Example_, 2002, Prentice Hall PTR, ISBN 0-13-061916-7

### Entrevistas

- Gelernter, David (2009). "Lord of the Cloud". John Brockman, Editor and Publisher; Russell Weinberger, Associate Publisher, Edge Foundation, Inc.
- Heiss, Janice J. (2003). "Computer Visions: A Conversation with David Gelernter". Sun Developer Network (SDN).
- Venners, Bill (2003). "Designing as if Programmers are People (Interview with Ken Arnold)". java.net.

### Artigos

- Brogden, William (2007). "How Web services can use JavaSpaces". SearchWebServices.com.
- Brogden, William (2007). "Grid computing and Web services (Beowulf, BOINC, Javaspaces)". SearchWebServices.com.
- White, Tom (2005). "How To Build a ComputeFarm". java.net.
- Ottinger, Joseph (2007). "Understanding JavaSpaces". theserverside.
- Angerer, Bernhard; Erlacher, Andreas (2005). "Loosely Coupled Communication and Coordination in Next-Generation Java Middleware". java.net.
- Angerer, Bernhard (2003). "Space-Based Programming". onjava.com.
- Sing, Li (2003). "High-impact Web tier clustering, Part 2: Building adaptive, scalable solutions with JavaSpaces". IBM developerworks.
- Mamoud, Qusay H. (2005). "Getting Started With JavaSpaces Technology: Beyond Conventional Distributed Programming Paradigms". Sun Developer Network (SDN).
- Freeman, Eric; Hupfer, Susanne (20 de novembro de 1999). "Make room for Javaspaces, Part 1 (from 5)". _JavaWorld_.
- Löffler, Dr. Gerald (2004). "JavaSpaces und ihr Platz im Enterprise Java Universum, Das Modell zum Objektaustausch: JavaSpaces vorgestellt". Entwickler.com.
- Arango, Mauricio (2009). "Coordination in parallel event-based systems". blogs.sun.com.
- Nemlekar, Milind (2001). "Scalable Distributed Tuplespaces". NCSU, Dept of ECE.

## Ver também

- Space-based architecture
- Linda (coordination language)
- Ken Arnold, engenheiro líder do JavaSpaces na Sun Microsystems

## Referências

1. Lee Gomes: "Sun Microsystems' Predictions For Jxta System Sound Familiar". _The Wall Street Journal_, 4 de junho de 2001.
2. Rob Guth: "More than just another pretty name: Sun's Jini opens up a new world of distributed computer systems". _SunWorld_, agosto de 1998.

## Fontes

- Gelernter, David. "Generative communication in Linda". _ACM Transactions on Programming Languages and Systems_, volume 7, número 1, janeiro de 1985.
- _Distributed Computing_ (primeira reimpressão indiana, 2004), M. L. Liu.
