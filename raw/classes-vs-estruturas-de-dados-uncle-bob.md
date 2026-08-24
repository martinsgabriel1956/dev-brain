# Classes vs. Estruturas de Dados

> Tradução de "Classes vs. Data Structures", de Robert C. Martin (Uncle Bob), publicado em 16 de junho de 2019 no blog Clean Coder.
> Fonte original: https://blog.cleancoder.com/uncle-bob/2019/06/16/ObjectsAndDataStructures.html

---

*O que é uma classe?*

Uma classe é a especificação de um conjunto de objetos similares.

*O que é um objeto?*

Um objeto é um conjunto de funções que operam sobre elementos de dados encapsulados.

*Ou melhor, um objeto é um conjunto de funções que operam sobre elementos de dados implícitos.*

O que você quer dizer com elementos de dados "implícitos"?

*As funções de um objeto implicam a existência de alguns elementos de dados; mas esses dados não são diretamente acessíveis nem visíveis fora do objeto.*

Os dados não estão dentro do objeto?

*Poderiam estar; mas não há nenhuma regra que diga que precisam estar. Do ponto de vista de quem usa, um objeto não é nada mais do que um conjunto de funções. Os dados sobre os quais essas funções operam precisam existir, mas a localização desses dados é desconhecida para quem os usa.*

Hmmm. OK, vou aceitar isso por enquanto.

*Ótimo. Agora, o que é uma estrutura de dados?*

Uma estrutura de dados é um conjunto coeso de elementos de dados.

*Ou, em outras palavras, uma estrutura de dados é um conjunto de elementos de dados operados por funções implícitas.*

OK, OK. Entendi. As funções que operam sobre a estrutura de dados não são especificadas pela estrutura de dados, mas a existência da estrutura de dados implica que algumas operações precisam existir.

*Certo. Agora, o que você percebe sobre essas duas definições?*

Elas são meio que opostas uma à outra.

*De fato. Elas são complementares uma à outra. Encaixam como mão e luva.*

- *Um Objeto é um conjunto de funções que operam sobre elementos de dados implícitos.*
- *Uma Estrutura de Dados é um conjunto de elementos de dados operados por funções implícitas.*

Uau, então objetos não são estruturas de dados.

*Correto. Objetos são o oposto de estruturas de dados.*

Então um DTO – um Data Transfer Object – não é um objeto?

*Correto. DTOs são estruturas de dados.*

E então tabelas de banco de dados também não são objetos, são?

*Correto de novo. Bancos de dados contêm estruturas de dados, não objetos.*

Mas espera. Um ORM – um Object Relational Mapper – não mapeia tabelas de banco de dados para objetos?

*Claro que não. Não existe mapeamento entre tabelas de banco de dados e objetos. Tabelas de banco de dados são estruturas de dados, não objetos.*

Então o que os ORMs fazem?

*Eles transferem dados entre estruturas de dados.*

Então eles não têm nada a ver com Objetos?

*Absolutamente nada. Não existe tal coisa como um Object Relational Mapper; porque não existe mapeamento entre tabelas de banco de dados e objetos.*

Mas eu pensava que ORMs construíam nossos objetos de negócio para nós.

*Não, ORMs extraem os dados sobre os quais nossos objetos de negócio operam. Esses dados ficam contidos numa estrutura de dados carregada pelo ORM.*

Mas então o objeto de negócio não contém essa estrutura de dados?

*Pode ser que sim. Pode ser que não. Isso não é problema do ORM.*

Isso parece um detalhe semântico menor.

*De jeito nenhum. Essa distinção tem implicações significativas.*

Tipo o quê?

*Tipo o design do schema do banco de dados versus o design dos objetos de negócio. Objetos de negócio definem a estrutura do* comportamento *do negócio. Schemas de banco de dados definem a estrutura dos* dados *do negócio. Essas duas estruturas são restringidas por forças muito diferentes. A estrutura dos dados de negócio não é necessariamente a melhor estrutura para o comportamento de negócio.*

Hmmm. Isso é confuso.

*Pense desta forma. O schema do banco de dados não é ajustado para uma única aplicação; ele precisa servir a empresa inteira. Então a estrutura desses dados é um compromisso entre muitas aplicações diferentes.*

OK, entendi isso.

*Bom. Mas agora considere cada aplicação individualmente. O modelo de objetos de cada aplicação descreve como o comportamento daquelas aplicações está estruturado. Cada aplicação terá um modelo de objetos diferente, ajustado ao comportamento daquela aplicação.*

Ah, entendi. Como o schema do banco de dados é um compromisso entre as várias aplicações, esse schema não vai corresponder ao modelo de objetos de nenhuma aplicação em particular.

*Isso! Objetos e Estruturas de Dados são restringidos por forças muito diferentes. Eles raramente se alinham de forma perfeita. As pessoas costumavam chamar isso de "impedância objeto-relacional" (object/relational impedance mismatch).*

Já ouvi falar disso. Mas eu pensava que essa impedância era resolvida pelos ORMs.

*E agora você sabe que não é. Não existe impedância porque objetos e estruturas de dados são complementares, não isomórficos.*

Como assim?

*Eles são opostos, não entidades similares.*

Opostos?

*Sim, de uma forma bem interessante. Veja, objetos e estruturas de dados implicam estruturas de controle diametralmente opostas.*

Espera, o quê?

*Considere um conjunto de classes de objetos que seguem uma interface comum. Por exemplo, imagine classes que representam formas geométricas bidimensionais, todas com funções para calcular a* área *e o* perímetro *da forma.*

Por que todo exemplo de software sempre envolve formas geométricas?

*Vamos considerar apenas dois tipos diferentes: `Quadrado`s e `Círculo`s. Deve ficar claro que as funções `area` e `perimetro` dessas duas classes operam sobre estruturas de dados implícitas diferentes. Também deve ficar claro que a forma como essas operações são chamadas é via polimorfismo dinâmico.*

Espera. Devagar. O quê?

*Existem duas funções `area` diferentes; uma para `Quadrado`, outra para `Círculo`. Quando quem chama invoca a função `area` num objeto específico, é aquele objeto que sabe qual função chamar. Chamamos isso de polimorfismo dinâmico.*

OK. Certo. O objeto conhece a implementação dos seus métodos. Certo.

*Agora vamos transformar esses objetos em estruturas de dados. Vamos usar Uniões Discriminadas (Discriminated Unions).*

Uniões discri... o quê?

*Uniões Discriminadas. No nosso caso, são só duas estruturas de dados diferentes. Uma para `Quadrado` e outra para `Círculo`. A estrutura de dados `Círculo` tem um ponto central e um raio como elementos de dados. Ela também tem um código de tipo que a identifica como `Círculo`.*

Você quer dizer tipo um enum?

*Claro. A estrutura de dados `Quadrado` tem o ponto superior esquerdo e o comprimento do lado. Ela também tem o discriminador de tipo – o enum.*

OK. Duas estruturas de dados com um código de tipo.

*Certo. Agora considere a função `area`. Ela vai ter um switch dentro dela, não vai?*

Hmm. Claro, para os dois casos diferentes. Um para `Quadrado` e outro para `Círculo`. E a função `perimetro` vai precisar de um switch parecido.

*De novo certo. Agora pense na estrutura desses dois cenários. No cenário de objetos, as duas implementações da função `area` são independentes uma da outra e pertencem (em algum sentido da palavra) ao tipo. A função `area` do `Quadrado` pertence ao `Quadrado`, e a função `area` do `Círculo` pertence ao `Círculo`.*

OK, já vejo aonde você quer chegar. No cenário de estrutura de dados, as duas implementações da função `area` estão juntas na mesma função, elas não "pertencem" (seja lá o que você quiser dizer com isso) ao tipo.

*Fica ainda melhor. Se você quiser adicionar o tipo `Triângulo` ao cenário de objetos, que código precisa mudar?*

Nenhum código muda. Você só cria a nova classe `Triângulo`. Ah, suponho que o criador da instância precise mudar.

*Certo. Então quando você adiciona um novo tipo, muito pouco muda. Agora suponha que você queira adicionar uma nova função – digamos, a função `centro`.*

Bom, aí você teria que adicionar isso aos três tipos, `Círculo`, `Quadrado` e `Triângulo`.

*Bom. Então adicionar novas funções é difícil, você tem que mudar cada classe.*

Mas com estruturas de dados é diferente. Para adicionar `Triângulo` você tem que mudar cada função para adicionar o caso `Triângulo` nos switches.

*Certo. Adicionar novos tipos é difícil, você tem que mudar cada função.*

Mas quando você adiciona a nova função `centro`, nada precisa mudar.

*Isso mesmo. Adicionar novas funções é fácil.*

Uau. É exatamente o oposto.

*É mesmo. Vamos revisar:*

- *Adicionar novas funções a um conjunto de classes é difícil, você tem que mudar cada classe.*
- *Adicionar novas funções a um conjunto de estruturas de dados é fácil, você só adiciona a função, nada mais muda.*
- *Adicionar novos tipos a um conjunto de classes é fácil, você só adiciona a nova classe.*
- *Adicionar novos tipos a um conjunto de estruturas de dados é difícil, você tem que mudar cada função.*

É. Opostos. Opostos de uma forma interessante. Quer dizer, se você sabe que vai adicionar novas funções a um conjunto de tipos, você vai querer usar estruturas de dados. Mas se você sabe que vai adicionar novos tipos, então você quer usar classes.

*Boa observação! Mas ainda tem uma última coisa para a gente considerar hoje. Existe ainda uma outra forma pela qual estruturas de dados e classes são opostas. Tem a ver com dependências.*

Dependências?

*Sim, a direção das dependências no código-fonte.*

OK, vou nessa. Qual é a diferença?

*Considere o caso da estrutura de dados. Cada função tem um switch que seleciona a implementação apropriada com base no código de tipo dentro da união discriminada.*

OK, isso é verdade. Mas e daí?

*Considere uma chamada à função `area`. Quem chama depende da função `area`, e a função `area` depende de cada implementação específica.*

O que você quer dizer com "depende"?

*Imagine que cada uma das implementações de `area` está escrita na sua própria função. Então tem `areaCirculo`, `areaQuadrado` e `areaTriangulo`.*

OK, então o switch só chama essas funções.

*Imagine que essas funções estão em arquivos-fonte diferentes.*

Então o arquivo-fonte com o switch teria que importar, ou usar, ou incluir, todos esses arquivos-fonte.

*Certo. Essa é uma dependência de código-fonte. Um arquivo-fonte depende de outro arquivo-fonte. Qual é a direção dessa dependência?*

O arquivo-fonte com o switch depende dos arquivos-fonte que contêm todas as implementações.

*E quanto a quem chama a função `area`?*

Quem chama a função `area` depende do arquivo-fonte com o switch, que depende de todas as implementações.

*Correto. Todas as dependências de arquivo-fonte apontam na direção da chamada, de quem chama para a implementação. Então, se você fizer uma pequena mudança em uma das implementações...*

OK, já vejo aonde você quer chegar com isso. Uma mudança em qualquer uma das implementações vai fazer com que o arquivo-fonte com o switch precise ser recompilado, o que vai fazer com que todo mundo que chama esse switch – a função `area`, no nosso caso – também precise ser recompilado.

*Correto. Pelo menos isso é verdade para sistemas de linguagem que dependem das datas dos arquivos-fonte para decidir quais módulos precisam ser compilados.*

Isso é basicamente todos os que usam tipagem estática, certo?

*Sim, e alguns que não usam.*

Isso é muita recompilação.

*E muito redeploy.*

OK, mas isso é invertido no caso das classes?

*Sim, porque quem chama a função `area` depende de uma interface, e as funções de implementação também dependem dessa interface.*

Entendi o que você quer dizer. O arquivo-fonte da classe `Quadrado` importa, ou usa, ou inclui o arquivo-fonte da interface `Forma`.

*Certo. Os arquivos-fonte da implementação apontam na direção oposta à da chamada. Eles apontam da implementação para quem chama. Pelo menos isso é verdade para linguagens com tipagem estática. Para linguagens com tipagem dinâmica, quem chama a função `area` não depende de nada. As ligações são resolvidas em tempo de execução.*

Certo. OK. Então se você fizer uma mudança em uma das implementações...

*Só o arquivo alterado precisa ser recompilado ou redeployado.*

E isso é porque as dependências entre os arquivos-fonte apontam contra a direção da chamada.

*Certo. Chamamos isso de Inversão de Dependência (Dependency Inversion).*

OK, então deixa eu ver se consigo resumir isso. Classes e Estruturas de Dados são opostas em pelo menos três formas diferentes.

- Classes tornam as funções visíveis mantendo os dados implícitos. Estruturas de dados tornam os dados visíveis mantendo as funções implícitas.
- Classes tornam fácil adicionar tipos, mas difícil adicionar funções. Estruturas de dados tornam fácil adicionar funções, mas difícil adicionar tipos.
- Estruturas de Dados expõem quem chama à recompilação e ao redeploy. Classes isolam quem chama da recompilação e do redeploy.

*Exatamente isso. Essas são questões que todo bom designer e arquiteto de software precisa ter em mente.*
