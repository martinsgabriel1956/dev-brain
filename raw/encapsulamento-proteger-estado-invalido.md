# Encapsulamento: o verdadeiro sentido de proteger o estado do objeto

> Transcrição de vídeo (canal brasileiro de programação/OOP, autor não identificado no áudio).
> Formato: resposta a uma dúvida de um espectador (Alexandre Medeiros) sobre um vídeo anterior
> ("Encapsulamento como você nunca viu"). Texto limpo e organizado a partir da transcrição
> automática — conteúdo original em português, preservado.

---

No vídeo de hoje eu vou te mostrar qual o verdadeiro sentido de usar encapsulamento na
programação orientada a objetos.

Eu fiz um vídeo há algum tempo atrás — não me lembro, acho que há um ano — chamado
"Encapsulamento como você nunca viu". E desse vídeo surgiram algumas dúvidas. Uma delas foi
do Alexandre Medeiros:

> "Olá, saudações. Você falou que encapsular é proteger atributos, mas ninguém explica o
> proteger de quê. O que pode acontecer de ruim se deixar público? Qual o objetivo real dessa
> proteção? Fica mais fácil se você explicar diretamente no objeto — para um leigo fica mais
> difícil de entender."

Então, Alexandre, eu entendi de fato a tua dor, entendi a tua dúvida, e nesse vídeo eu vou
tentar responder os teus questionamentos.

## O encapsulamento não serve para "esconder atributos"

O encapsulamento, na verdade, não serve simplesmente para você esconder os atributos. O
principal objetivo é **proteger o estado do teu objeto contra alterações inválidas**.

## Demonstração: a classe totalmente aberta

Vou criar uma classe em Java, chamada `Product` (poderia ser em português também). Vou colocar
os atributos todos públicos:

```java
public class Product {
    public String name;
    public double price; // poderia usar BigDecimal, mas double facilita o exemplo
    public int stock;
}
```

Tenho uma classe totalmente aberta, com todos os atributos públicos. Agora, na `main`, eu vou
ser um desenvolvedor do time que usa esse `Product` e vou declarar algumas situações inválidas:

```java
Product p = new Product();
p.name = "";       // nome vazio
p.price = -500;    // preço negativo
p.stock = -20;     // estoque negativo

System.out.println(p.name);
System.out.println(p.price);
System.out.println(p.stock);
```

Se eu rodar esse programa, ele imprime informações errôneas: não estipulei o nome do produto,
tenho um preço negativo (que não faz sentido) e um estoque negativo (que também não faz
sentido). **O objeto entrou num estado inválido e ninguém impediu.**

## A correção: o próprio objeto protege seus dados

Agora eu vou usar o encapsulamento que, na minha visão, é o mais correto: **este próprio objeto
vai ser responsável por proteger os seus dados.** Eu transformo tudo em `private`.

Atenção: tornar os atributos `private` **é** o encapsulamento. A forma como você programa depois
(getters, setters, métodos) não diz respeito ao encapsulamento em si — diz respeito ao *acesso*
a esses atributos. O encapsulamento são as formas de proteção.

Em vez de criar `setName` / `setPrice` simples (que só atribuem), eu crio métodos explícitos
que carregam as regras de negócio — deixando a classe **não anêmica**:

```java
public class Product {
    private String name;
    private double price;
    private int stock;

    public Product(String name, double price, int stock) {
        changeName(name);
        changePrice(price);
        increaseStock(stock);
    }

    public void changeName(String name) {
        if (name == null || name.isBlank()) {
            throw new IllegalArgumentException("product name is required");
        }
        this.name = name;
    }

    public void changePrice(double price) {
        if (price <= 0) {
            throw new IllegalArgumentException("product price must be greater than zero");
        }
        this.price = price;
    }

    public void increaseStock(int quantity) {
        if (quantity < 0) { // pode ser zero, então só negativo é inválido
            throw new IllegalArgumentException("quantity cannot be negative");
        }
        this.stock += quantity;
    }

    public void decreaseStock(int quantity) {
        if (quantity <= 0) {
            throw new IllegalArgumentException("quantity must be greater than zero");
        }
        if (quantity > stock) {
            throw new IllegalArgumentException("insufficient stock");
        }
        this.stock -= quantity;
    }

    public String getName()  { return name; }
    public double getPrice() { return price; }
    public int getStock()    { return stock; }
}
```

Perceba que eu não estou criando setters só para atribuição — os métodos `changeName`,
`changePrice`, `increaseStock` e `decreaseStock` carregam comportamento. Os getters existem
apenas para leitura.

## O uso da classe encapsulada

```java
Product notebook = new Product("Notebook Dell", 4500, 10);
notebook.changePrice(4300);   // troca de preço válido
notebook.decreaseStock(2);    // comprei dois

System.out.println(notebook.getName());  // Notebook Dell
System.out.println(notebook.getPrice()); // 4300
System.out.println(notebook.getStock()); // 8
```

Agora, se eu tentar as operações inválidas de antes:

```java
notebook.changePrice(-500);   // IllegalArgumentException: product price must be greater than zero
notebook.decreaseStock(100);  // IllegalArgumentException: insufficient stock
```

O objeto **nunca entra num estado inválido**. E esse sim é o principal objetivo do
encapsulamento.

## A lição

Encapsular significa **impedir que qualquer parte do sistema coloque um objeto em um estado
inválido**. Os atributos `private` são apenas uma *ferramenta* para alcançar esse objetivo — o
importante não é esconder os dados, é **garantir que todas as alterações passem pelas regras de
negócio do próprio objeto**.

Por isso, em sistemas grandes, com dezenas de desenvolvedores, o encapsulamento evita bugs —
inclusive os mais difíceis de encontrar. Ninguém consegue alterar um `Product` de uma forma que
viole as regras definidas pela própria classe, justamente porque a classe **não é anêmica**.
