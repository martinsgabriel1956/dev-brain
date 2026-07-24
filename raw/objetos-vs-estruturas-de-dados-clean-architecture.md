# Objetos vs. Estruturas de Dados na Clean Architecture

> Transcrição de vídeo em português sobre a distinção, dentro da Clean Architecture, entre classes/objetos e estruturas de dados — com base num post do blog do Uncle Bob e no diagrama de cenário típico de aplicação web do livro *Clean Architecture*. Transcrição bruta de fala (sem pontuação original) reorganizada em seções e limpa de repetições/hesitações, sem adicionar conteúdo novo.

---

## A distinção central: classes/objetos vs. estruturas de dados

Uma das distinções mais importantes que aparece na Clean Architecture é entre **classes/objetos** e **estruturas de dados**.

Uncle Bob tem um blog no qual publicou um post especificamente sobre essa diferença entre classes e estruturas de dados. Nesse post ele constrói o argumento como se fosse um diálogo entre duas pessoas — uma pergunta "o que é uma classe?", a outra responde, depois pergunta "o que é um objeto?", e assim por diante. Em determinado ponto da discussão, os dois personagens chegam à conclusão de que **objetos são o oposto de estruturas de dados**.

As definições a que eles chegam:

- **Objeto**: um conjunto de funções que operam sobre elementos de dados **implícitos** (escondidos).
- **Estrutura de dados**: um conjunto de elementos de dados que são operados por funções **implícitas** (externas).

Em outras palavras:

- Nos **objetos**, os dados em geral são **encapsulados** — não são visíveis, são os atributos/membros privados — e o que fica público são os **métodos**, funções explícitas.
- Nas **estruturas de dados**, é exatamente o oposto: elas contêm **campos** que geralmente são **visíveis**/públicos, mas as **funções que operam sobre esses campos ficam externas** à estrutura — não pertencem a ela.

Um exemplo simples: quando você cria uma `struct` (por exemplo em C), os dados daquela struct são completamente acessíveis de fora. Isso é diferente de um objeto, no qual os atributos não são acessíveis diretamente — o acesso é mediado por métodos.

---

## Implicação 1: não existe mapeamento direto entre objetos e relações de banco de dados

Uma das implicações de objetos serem o oposto de estruturas de dados é que **não há um mapeamento direto entre um objeto e uma relação (tabela) de banco de dados**. Uncle Bob inclusive sugere que o nome correto para essas ferramentas não deveria ser *Object-Relational Mapper* (ORM) — talvez algo como *Relational Datastructure Mapper* seria mais adequado.

O raciocínio: o banco de dados contém **relações**, e essas relações na verdade contêm **estruturas de dados**, não objetos. O que uma ferramenta de mapeamento faz é pegar os dados que estão na estrutura de dados do banco e **transferir** esses dados para um objeto — o objeto passa a conter dados que estavam nas estruturas de dados do banco.

Por que não pode haver mapeamento direto entre relações e objetos:

- Objetos contêm **comportamento**.
- As linhas de uma tabela de banco de dados não são nada mais do que **dados estruturados** — ou seja, estruturas de dados. Não há comportamento dentro do banco de dados.

Então não existe mapeamento direto entre relação e objeto — o que pode existir é uma **transferência de dados**. Você tem uma tabela `usuario` com os dados de usuários, e tem um objeto `Usuario` que pode carregar esses dados para dentro de si — mas o objeto contém mais coisas do que só os dados: ele contém comportamento, coisa que a tabela do banco não tem.

---

## Implicação 2: onde entram estruturas de dados e onde entram objetos numa aplicação web com Clean Architecture

O livro *Clean Architecture*, do Uncle Bob, mostra um diagrama de um cenário típico de uso da Clean Architecture numa aplicação web. Nesse diagrama existem tanto classes/objetos quanto estruturas de dados — algumas caixas do diagrama têm a marcação **"DS"** (Data Structure), indicando que aquela caixa representa uma estrutura de dados, não um objeto.

A regra geral: **estruturas de dados são usadas somente para transferir dados entre uma camada e outra**. Essas caixas não têm nenhum comportamento — são dados puros e simples. **Objetos** aparecem onde há comportamento e lógica de negócio.

### O fluxo, passo a passo

1. O **servidor web** recebe os dados de entrada do usuário e os envia para o **Controller**.
2. O **Controller** empacota esses dados em uma **estrutura de dados** (Input Data) — aqui só existem dados simples, por exemplo strings representando e-mail e nome do usuário.
3. Esse dado é passado através de uma **interface** (o **Input Boundary**) para o **caso de uso (Use Case)**. Essa interface existe para fazer **inversão de dependência**: o caso de uso não depende do controller — é o controller que depende dessa abstração, e o caso de uso também depende da mesma abstração. Essa interface também é chamada de **protocolo**.
4. O **caso de uso** interpreta os dados recebidos e os usa para **orquestrar as entidades**. As **entidades** aqui, em geral, são **objetos** de verdade — porque têm comportamento e implementam a lógica de negócio do domínio.
5. O caso de uso também usa uma **interface de acesso a dados** (Data Access interface) para trazer dados do banco de dados. Esses dados vêm do banco e são transferidos para as entidades por meio de um **Data Mapper** — o mapeador que faz essa transferência dos dados do banco de dados para dentro das entidades.
6. Quando a operação do caso de uso é concluída, ele constrói um **Output Data** — também uma **estrutura de dados simples**. Esse Output Data é passado para o **Presenter** através de uma interface de saída (**Output Boundary**) — novamente, uma interface para evitar que o caso de uso dependa diretamente de algo que está em outra camada da aplicação.
7. O trabalho do **Presenter** é reempacotar os dados que vêm do Output Data em um **ViewModel** — outra **estrutura de dados**, bem simples, geralmente contendo apenas strings e flags que a **View** utiliza para apresentar os dados.

A diferença entre o Output Data e o ViewModel: no Output Data você ainda pode ter tipos do domínio de negócio — por exemplo um tipo `Data`/`Date`, ou objetos/Value Objects que representam valores em dinheiro. Tudo isso é transformado em **strings simples** no ViewModel, que é o que a View vai usar para apresentar os dados ao usuário. Dessa forma a View fica muito simples — ela praticamente não faz nada além de jogar os dados do ViewModel para dentro de uma página HTML.

### Resumo do papel de cada peça

| Peça | Tipo | Papel |
|---|---|---|
| Input Data | Estrutura de dados | Dados de entrada empacotados pelo Controller |
| Input Boundary | Interface (protocolo) | Inversão de dependência entre Controller e Use Case |
| Use Case | Objeto | Orquestra as entidades, contém lógica de aplicação |
| Entities | Objeto | Comportamento e regra de negócio do domínio |
| Data Access interface | Interface (protocolo) | Inversão de dependência entre Use Case e banco de dados |
| Data Mapper | — | Transfere dados do banco para as Entities |
| Output Data | Estrutura de dados | Dados de saída construídos pelo Use Case, pode conter tipos de domínio |
| Output Boundary | Interface (protocolo) | Inversão de dependência entre Use Case e Presenter |
| Presenter | Objeto | Reempacota Output Data em ViewModel |
| ViewModel | Estrutura de dados | Apenas strings e flags, pronto para a View exibir |
| View | — | Só transfere os dados do ViewModel para o HTML |

---

## Fechamento

A ideia central das estruturas de dados na Clean Architecture é simplesmente **transferir dados entre uma camada e outra**, enquanto os **objetos** realmente carregam **comportamento**. As classes/objetos também são usadas para permitir **inversão de dependência via polimorfismo** (as interfaces de Input/Output Boundary e Data Access). Esse é o cenário típico de como a Clean Architecture funciona numa aplicação web, e onde entram estruturas de dados e onde entram objetos.
