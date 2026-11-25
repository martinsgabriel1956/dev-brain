# Capítulo 4 — Módulos Devem Ser Profundos

Uma das técnicas mais importantes para gerenciar a complexidade de software é projetar sistemas de forma que os desenvolvedores precisem lidar apenas com uma pequena fração da complexidade total a qualquer momento. Essa abordagem é chamada de design modular, e este capítulo apresenta seus princípios básicos.

## 4.1 Design modular

No design modular, um sistema de software é decomposto em uma coleção de módulos que são relativamente independentes. Os módulos podem assumir diversas formas, como classes, subsistemas ou serviços. Em um mundo ideal, cada módulo seria completamente independente dos demais: um desenvolvedor poderia trabalhar em qualquer um dos módulos sem saber nada sobre nenhum dos outros. Nesse mundo, a complexidade de um sistema seria a complexidade de seu pior módulo.

Infelizmente, esse ideal é inatingível. Os módulos precisam trabalhar juntos chamando as funções ou métodos uns dos outros. Como resultado, os módulos precisam saber algo uns sobre os outros. Haverá dependências entre os módulos: se um módulo mudar, outros módulos podem precisar mudar para se adequarem. Por exemplo, os argumentos de um método criam uma dependência entre o método e qualquer código que o invoque. Se os argumentos exigidos mudarem, todas as invocações do método devem ser modificadas para se conformarem à nova assinatura. As dependências podem assumir muitas outras formas e podem ser bastante sutis; como exemplo, um método pode não funcionar corretamente a menos que algum outro método tenha sido invocado primeiro. O objetivo do design modular é minimizar as dependências entre os módulos.

A fim de identificar e gerenciar dependências, pensamos em cada módulo em duas partes: uma interface e uma implementação. A interface consiste em tudo o que um desenvolvedor trabalhando em um módulo diferente precisa saber para usar o módulo em questão. Normalmente, a interface descreve o que o módulo faz, mas não como ele faz isso. A implementação consiste no código que cumpre as promessas feitas pela interface. Um desenvolvedor trabalhando em um módulo específico deve entender a interface e a implementação desse módulo, além das interfaces de quaisquer outros módulos invocados por ele. Um desenvolvedor não deveria precisar entender as implementações de outros módulos além daquele em que está trabalhando.

Considere um módulo que implementa árvores balanceadas. O módulo provavelmente contém um código sofisticado para garantir que a árvore permaneça balanceada. No entanto, essa complexidade não é visível para os usuários do módulo. Os usuários veem uma interface relativamente simples para invocar operações de inserção, remoção e busca de nós na árvore. Para invocar uma operação de inserção, quem faz a chamada precisa fornecer apenas a chave e o valor do novo nó; os mecanismos para percorrer a árvore e dividir os nós não são visíveis na interface.

Para os fins deste livro, um módulo é qualquer unidade de código que tenha uma interface e uma implementação. Cada classe em uma linguagem de programação orientada a objetos é um módulo. Métodos dentro de uma classe, ou funções em uma linguagem que não seja orientada a objetos, também podem ser pensados como módulos: cada um deles possui uma interface e uma implementação, e técnicas de design modular podem ser aplicadas a eles. Subsistemas e serviços de nível mais alto também são módulos; suas interfaces podem assumir formas diferentes, como chamadas de kernel ou requisições HTTP. Grande parte da discussão sobre design modular neste livro se concentra no design de classes, mas as técnicas e os conceitos também se aplicam a outros tipos de módulos.

Os melhores módulos são aqueles cujas interfaces são muito mais simples do que suas implementações. Tais módulos têm duas vantagens. Primeiro, uma interface simples minimiza a complexidade que um módulo impõe ao resto do sistema. Segundo, se um módulo for modificado de uma forma que não altere sua interface, nenhum outro módulo será afetado pela modificação. Se a interface de um módulo for muito mais simples do que sua implementação, haverá muitos aspectos do módulo que poderão ser alterados sem afetar outros módulos.

## 4.2 O que há em uma interface?

A interface de um módulo contém dois tipos de informação: formal e informal. As partes formais de uma interface são especificadas explicitamente no código, e a corretude de algumas delas pode ser verificada pela linguagem de programação. Por exemplo, a interface formal de um método é a sua assinatura, que inclui os nomes e os tipos de seus parâmetros, o tipo do seu valor de retorno e informações sobre as exceções lançadas pelo método. A maioria das linguagens de programação garante que cada invocação de um método forneça o número certo e os tipos corretos de argumentos para corresponder à sua assinatura. A interface formal de uma classe consiste nas assinaturas de todos os seus métodos públicos, além dos nomes e tipos de quaisquer variáveis públicas.

Cada interface também inclui elementos informais. Estes não são especificados de uma forma que possa ser compreendida ou imposta pela linguagem de programação. As partes informais de uma interface incluem seu comportamento de alto nível, como o fato de que uma função exclui o arquivo nomeado por um de seus argumentos. Se houver restrições no uso de uma classe (talvez um método deva ser chamado antes de outro), estas também fazem parte da interface da classe. Em geral, se um desenvolvedor precisa saber de uma informação específica para conseguir usar um módulo, então essa informação faz parte da interface do módulo. Os aspectos informais de uma interface só podem ser descritos usando comentários, e a linguagem de programação não pode garantir que a descrição seja completa ou precisa¹. Para a maioria das interfaces, os aspectos informais são maiores e mais complexos do que os aspectos formais.

Um dos benefícios de uma interface claramente especificada é que ela indica exatamente o que os desenvolvedores precisam saber para usar o módulo associado. Isso ajuda a eliminar o problema das "incógnitas desconhecidas" descrito na Seção 2.2.

> N.T.: O termo "incógnitas desconhecidas" (do original "unknown unknowns") é um conceito clássico na gestão de projetos e engenharia de software que se refere a riscos, cenários ou informações que a equipe não apenas desconhece, mas que sequer tem consciência de que desconhece.

## 4.3 Abstrações

O termo abstração está intimamente relacionado à ideia de design modular. Uma abstração é uma visão simplificada de uma entidade, que omite detalhes sem importância. As abstrações são úteis porque facilitam a nossa capacidade de pensar sobre coisas complexas e manipulá-las.

Na programação modular, cada módulo fornece uma abstração na forma de sua interface. A interface apresenta uma visão simplificada da funcionalidade do módulo; os detalhes da implementação não são importantes do ponto de vista da abstração do módulo, portanto, são omitidos da interface.

Na definição de abstração, a palavra "sem importância" é crucial. Quanto mais detalhes sem importância forem omitidos de uma abstração, melhor. No entanto, um detalhe só pode ser omitido de uma abstração se ele for realmente irrelevante. Uma abstração pode dar errado de duas maneiras. Primeiro, ela pode incluir detalhes que não são realmente importantes; quando isso acontece, a abstração se torna mais complicada do que o necessário, o que aumenta a carga cognitiva dos desenvolvedores que a utilizam. O segundo erro ocorre quando uma abstração omite detalhes que são, de fato, importantes. Isso resulta em obscuridade: os desenvolvedores que olham apenas para a abstração não terão todas as informações necessárias para usá-la corretamente. Uma abstração que omite detalhes importantes é uma falsa abstração: ela pode parecer simples, mas na realidade não é. A chave para projetar abstrações é entender o que é importante e buscar designs que minimizem a quantidade de informações que são de fato essenciais.

Como exemplo, considere um sistema de arquivos. A abstração fornecida por um sistema de arquivos omite muitos detalhes, como o mecanismo de escolha de quais blocos em um dispositivo de armazenamento usar para os dados de um determinado arquivo. Esses detalhes não são importantes para os usuários do sistema de arquivos (desde que o sistema forneça um desempenho adequado). No entanto, alguns dos detalhes da implementação de um sistema de arquivos são importantes para os usuários. A maioria dos sistemas de arquivos armazena dados em cache na memória principal e pode atrasar a gravação de novos dados no dispositivo de armazenamento a fim de melhorar o desempenho. Algumas aplicações, como bancos de dados, precisam saber exatamente quando os dados são efetivamente gravados no armazenamento, para que possam garantir que eles serão preservados após falhas no sistema. Assim, as regras para o descarregamento (flushing) de dados para o armazenamento secundário devem ser visíveis na interface do sistema de arquivos.

Nós dependemos de abstrações para gerenciar a complexidade não apenas na programação, mas de forma onipresente no nosso dia a dia. Um forno de micro-ondas contém componentes eletrônicos complexos para converter corrente alternada em radiação de micro-ondas e distribuir essa radiação por toda a cavidade de cozimento. Felizmente, os usuários veem uma abstração muito mais simples, consistindo em alguns botões para controlar o tempo e a intensidade das micro-ondas. Os carros fornecem uma abstração simples que nos permite dirigi-los sem entender os mecanismos dos motores elétricos, o gerenciamento de energia da bateria, os freios ABS, o controle de cruzeiro, e assim por diante.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 511 336"
     font-family="Arial, Helvetica, sans-serif" font-size="15">

  <!-- Ponta de seta reutilizável -->
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5"
            markerWidth="7" markerHeight="7" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#000"/>
    </marker>
  </defs>

  <rect width="511" height="336" fill="#fff"/>

  <!-- Rótulos -->
  <text x="160" y="36" text-anchor="middle">Interface (custo:</text>
  <text x="160" y="56" text-anchor="middle">menos é melhor)</text>
  <text x="352" y="100" text-anchor="middle">Funcionalidade (benefício:</text>
  <text x="352" y="120" text-anchor="middle">mais é melhor)</text>

  <!-- Setas: custo de interface -->
  <line x1="130" y1="62" x2="112" y2="102" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="200" y1="62" x2="287" y2="238" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Setas: benefício (funcionalidade) -->
  <line x1="320" y1="132" x2="106" y2="190" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="372" y1="132" x2="352" y2="262" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Módulo profundo: interface pequena, corpo grande -->
  <rect x="45" y="110" width="86" height="175" fill="#e6e6e6"
        stroke="#666" stroke-width="1" stroke-dasharray="6 4"/>
  <line x1="45" y1="110" x2="131" y2="110" stroke="#000" stroke-width="5"/>
  <text x="88" y="308" text-anchor="middle">Módulo Profundo</text>

  <!-- Módulo raso: interface larga, corpo pequeno -->
  <rect x="217" y="245" width="256" height="40" fill="#e6e6e6"
        stroke="#666" stroke-width="1" stroke-dasharray="6 4"/>
  <line x1="217" y1="245" x2="473" y2="245" stroke="#000" stroke-width="5"/>
  <text x="345" y="308" text-anchor="middle">Módulo Raso</text>

</svg>
```

*Figura 4.1: Módulos profundos e rasos. Os melhores módulos são profundos: eles permitem que muita funcionalidade seja acessada por meio de uma interface simples. Um módulo raso é aquele que possui uma interface relativamente complexa, mas com pouca funcionalidade: ele não oculta muita complexidade.*

## 4.4 Módulos profundos

Os melhores módulos são aqueles que oferecem funcionalidades poderosas, mas possuem interfaces simples. Eu uso o termo *profundo* para descrever tais módulos. Para visualizar a noção de profundidade, imagine que cada módulo seja representado por um retângulo, conforme mostrado na Figura 4.1. A área de cada retângulo é proporcional à funcionalidade implementada pelo módulo. A borda superior de um retângulo representa a interface do módulo; o comprimento dessa borda indica a complexidade da interface. Os melhores módulos são profundos: eles têm muita funcionalidade escondida atrás de uma interface simples. Um módulo profundo é uma boa abstração porque apenas uma pequena fração de sua complexidade interna é visível para seus usuários.

A profundidade do módulo é uma forma de pensar sobre a relação custo-benefício. O benefício proporcionado por um módulo é a sua funcionalidade. O custo de um módulo (em termos de complexidade do sistema) é a sua interface. A interface de um módulo representa a complexidade que o módulo impõe ao restante do sistema: quanto menor e mais simples for a interface, menos complexidade ele introduz. Os melhores módulos são aqueles com o maior benefício e o menor custo. Interfaces são boas, mas interfaces em maior quantidade ou mais extensas não são necessariamente melhores!

O mecanismo de E/S de arquivos (I/O) fornecido pelo sistema operacional Unix e seus descendentes, como o Linux, é um belo exemplo de uma interface profunda. Existem apenas cinco chamadas de sistema básicas para E/S, com assinaturas simples:

```c
int open(const char* path, int flags, mode_t permissions);
ssize_t read(int fd, void* buffer, size_t count);
ssize_t write(int fd, const void* buffer, size_t count);
off_t lseek(int fd, off_t offset, int referencePosition);
int close(int fd);
```

A chamada de sistema `open` recebe um nome de arquivo hierárquico, como `/a/b/c`, e retorna um inteiro chamado *descritor de arquivo*, que é usado para referenciar o arquivo aberto. Os outros argumentos de `open` fornecem informações opcionais, como se o arquivo está sendo aberto para leitura ou escrita, se um novo arquivo deve ser criado caso não exista, e as permissões de acesso ao arquivo, caso um novo seja criado. As chamadas de sistema `read` e `write` transferem informações entre áreas de buffer na memória da aplicação e o arquivo; `close` encerra o acesso ao arquivo. A maioria dos arquivos é acessada sequencialmente, de modo que esse é o padrão; no entanto, o acesso aleatório pode ser realizado invocando a chamada de sistema `lseek` para alterar a posição de acesso atual.

Uma implementação moderna da interface de E/S do Unix exige centenas de milhares de linhas de código, que resolvem questões complexas, tais como:

* Como os arquivos são representados no disco para permitir um acesso eficiente?
* Como os diretórios são armazenados e como os nomes de caminhos hierárquicos são processados para encontrar os arquivos aos quais se referem?
* Como as permissões são aplicadas, para que um usuário não possa modificar ou excluir os arquivos de outro usuário?
* Como os acessos aos arquivos são implementados? Por exemplo, como a funcionalidade é dividida entre os tratadores de interrupção (interrupt handlers) e o código em segundo plano, e como esses dois elementos se comunicam com segurança?
* Quais políticas de escalonamento são usadas quando há acessos simultâneos a vários arquivos?
* Como os dados de arquivos acessados recentemente podem ser armazenados em cache na memória para reduzir o número de acessos ao disco?
* Como uma variedade de dispositivos de armazenamento secundário diferentes, como discos e pen drives, pode ser incorporada a um único sistema de arquivos?

Todas essas questões, e muitas outras, são tratadas pela implementação do sistema de arquivos Unix; elas são invisíveis para os programadores que invocam as chamadas de sistema. As implementações da interface de E/S do Unix evoluíram radicalmente ao longo dos anos, mas as cinco chamadas básicas do kernel não mudaram.

Outro exemplo de um módulo profundo é o coletor de lixo (garbage collector) em uma linguagem como Go ou Java. Este módulo não possui interface alguma; ele trabalha de forma invisível nos bastidores para recuperar a memória não utilizada. Adicionar a coleta de lixo a um sistema, na verdade, reduz a sua interface geral, uma vez que elimina a interface para a liberação de objetos. A implementação de um coletor de lixo é bastante complexa, mas essa complexidade fica oculta dos programadores.

Módulos profundos, como a E/S do Unix e os coletores de lixo, fornecem abstrações poderosas porque são fáceis de usar e, ao mesmo tempo, escondem uma complexidade de implementação significativa.

## 4.5 Módulos rasos

Por outro lado, um módulo raso é aquele cuja interface é relativamente complexa em comparação com a funcionalidade que ele fornece. Por exemplo, uma classe que implementa listas encadeadas é rasa. Não é preciso muito código para manipular uma lista encadeada (inserir ou excluir um elemento leva apenas algumas linhas), portanto, a abstração da lista encadeada não oculta muitos detalhes. A complexidade da interface de uma lista encadeada é quase tão grande quanto a complexidade de sua implementação. Classes rasas, como listas encadeadas, às vezes são inevitáveis e ainda podem ser úteis, mas não oferecem muita vantagem contra a complexidade.

Aqui está um exemplo extremo de um método raso, retirado de um projeto em uma aula de design de software:

```java
private void addNullValueForAttribute(String attribute) {
    data.put(attribute, null);
}
```

Do ponto de vista do gerenciamento da complexidade, esse método piora as coisas, em vez de melhorar. O método não oferece nenhuma abstração, já que toda a sua funcionalidade é visível através da sua interface. Por exemplo, quem o chama provavelmente precisa saber que o atributo será armazenado na variável `data`. Não é mais simples pensar na interface do que pensar na implementação completa. Se o método for documentado adequadamente, a documentação será mais longa que o código do método. Exige até mais toques no teclado para invocar o método do que seria necessário para manipular a variável `data` diretamente. O método adiciona complexidade (na forma de uma nova interface para os desenvolvedores aprenderem), mas não fornece nenhum benefício compensatório.

> **🚩 Sinal de Alerta: Módulo Raso 🚩**
>
> Um módulo raso é aquele cuja interface é complicada em relação à funcionalidade que ele fornece. Módulos rasos não ajudam muito na batalha contra a complexidade, porque o benefício que eles fornecem (não ter que aprender como eles funcionam internamente) é anulado pelo custo de aprender e usar suas interfaces. Módulos pequenos tendem a ser rasos.

## 4.6 Classite

Infelizmente, o valor das classes profundas não é amplamente reconhecido hoje em dia. O senso comum na programação é que as classes devem ser pequenas, não profundas. Muitas vezes, ensina-se aos estudantes que a coisa mais importante no design de classes é dividir as classes maiores em menores. O mesmo conselho é frequentemente dado sobre métodos: "Qualquer método com mais de N linhas deve ser dividido em múltiplos métodos" (N pode ser tão baixo quanto 10). Essa abordagem resulta em um grande número de classes e métodos rasos, que aumentam a complexidade geral do sistema.

O extremo da abordagem "as classes devem ser pequenas" é uma síndrome que chamo de classite, que deriva da visão equivocada de que "classes são boas, então quanto mais classes, melhor". Em sistemas que sofrem de classite, os desenvolvedores são encorajados a minimizar a quantidade de funcionalidade em cada nova classe: se você quiser mais funcionalidade, introduza mais classes. A classite pode resultar em classes que são individualmente simples, mas ela aumenta a complexidade de todo o sistema. Classes pequenas não contribuem com muita funcionalidade, então é necessário que existam muitas delas, cada uma com sua própria interface. Essas interfaces se acumulam para criar uma complexidade tremenda no nível do sistema. Classes pequenas também resultam em um estilo de programação prolixo, devido ao boilerplate necessário para cada classe.

> **Nota do Tradutor (N.T.):**
>
> * **Classite:** Adaptação do termo original "classitis", criado pelo autor como um trocadilho utilizando o sufixo médico "-ite" (indicativo de inflamação/doença) para descrever a "doença" do excesso de classes.
> * **Boilerplate:** O termo foi mantido no jargão original em inglês, pois é amplamente utilizado e consagrado pela comunidade de desenvolvimento de software no Brasil para se referir a blocos de código estruturais, padronizados e repetitivos que precisam ser incluídos em vários lugares com pouca ou nenhuma alteração.

## 4.7 Exemplos: I/O no Java e no Unix

Um dos exemplos mais visíveis de "classite" hoje em dia é a biblioteca de classes do Java. A linguagem Java não exige um monte de classes pequenas, mas uma cultura de "classite" parece ter se enraizado na comunidade de programação Java. Por exemplo, por muitos anos os desenvolvedores Java tiveram que criar três objetos diferentes para abrir um arquivo e ler objetos serializados dele:

```java
FileInputStream fileStream =
    new FileInputStream(fileName);
BufferedInputStream bufferedStream =
    new BufferedInputStream(fileStream);
ObjectInputStream objectStream =
    new ObjectInputStream(bufferedStream);
```

Um objeto `FileInputStream` fornece apenas I/O rudimentar: ele não é capaz de executar I/O com buffer, nem pode ler ou gravar objetos serializados. O objeto `BufferedInputStream` adiciona o uso de buffer a um `FileInputStream`, e o `ObjectInputStream` adiciona a capacidade de ler e gravar objetos serializados. Os dois primeiros objetos no código acima, `fileStream` e `bufferedStream`, nunca mais são usados depois que o arquivo é aberto; todas as operações futuras usam o `objectStream`.

É particularmente irritante (e propenso a erros) que o uso de buffer precise ser solicitado explicitamente por meio da criação de um objeto `BufferedInputStream` separado; se um desenvolvedor esquecer de criar esse objeto, não haverá buffer e as operações de I/O serão lentas. Talvez os desenvolvedores do Java argumentassem que nem todo mundo quer usar buffer para I/O de arquivos, então isso não deveria ser embutido no mecanismo base. Eles poderiam argumentar que é melhor manter o uso de buffer separado, para que as pessoas possam escolher se querem ou não usá-lo. Oferecer escolha é bom, mas as interfaces devem ser projetadas para tornar o caso comum o mais simples possível (veja a fórmula na página 6). Quase todo usuário de I/O de arquivos vai querer usar buffer, então isso deveria ser fornecido por padrão. Para aquelas poucas situações em que o buffer não é desejável, a biblioteca pode fornecer um mecanismo para desativá-lo. Qualquer mecanismo para desativar o buffer deve ser separado de forma limpa na interface (por exemplo, fornecendo um construtor diferente para `FileInputStream`, ou por meio de um método que desative ou substitua o mecanismo de buffer), para que a maioria dos desenvolvedores nem precise saber da sua existência.

Em contrapartida, os projetistas das chamadas de sistema (system calls) do Unix tornaram o caso comum simples. Por exemplo, eles reconheceram que a I/O sequencial é a mais comum, então tornaram esse o comportamento padrão. O acesso aleatório ainda é relativamente fácil de se fazer, usando a chamada de sistema `lseek`, mas um desenvolvedor que faz apenas acesso sequencial não precisa estar ciente desse mecanismo. Se uma interface tem muitos recursos, mas a maioria dos desenvolvedores só precisa conhecer alguns deles, a complexidade efetiva dessa interface é apenas a complexidade dos recursos comumente usados.

> **Notas do Tradutor (N.T.):**
>
> 1. **"Classite" (do original *classitis*):** Termo informal cunhado na área de engenharia de software (usando o sufixo "-ite", que denota inflamação ou doença) para descrever a tendência exagerada e desnecessária de criar uma quantidade excessiva de classes pequenas em um projeto orientado a objetos, fragmentando demais a lógica e dificultando a usabilidade.

## 4.8 Conclusão

Ao separar a interface de um módulo da sua implementação, podemos ocultar a complexidade da implementação do restante do sistema. Os usuários de um módulo precisam entender apenas a abstração fornecida por sua interface. A questão mais importante no projeto de classes e de outros módulos é torná-los profundos (deep), para que possuam interfaces simples para os casos de uso comuns, mas ainda assim forneçam uma funcionalidade significativa. Isso maximiza a quantidade de complexidade que é ocultada.

¹ Existem linguagens, principalmente na comunidade de pesquisa, onde o comportamento geral de um método ou função pode ser descrito formalmente utilizando uma linguagem de especificação. A especificação pode ser verificada automaticamente para garantir que corresponda à implementação. Uma questão interessante é se tal especificação formal poderia substituir as partes informais de uma interface. Minha opinião atual é que uma interface descrita em inglês provavelmente será mais intuitiva e compreensível para os desenvolvedores do que uma interface escrita em uma linguagem de especificação formal.

> **Nota do Tradutor (N.T.):** A expressão "módulos profundos" (deep modules) é um termo técnico consagrado neste contexto de arquitetura de software (frequentemente associado ao livro *A Philosophy of Software Design*). Ele descreve componentes que expõem uma interface extremamente simples e enxuta, mas que encapsulam e executam uma lógica altamente complexa e poderosa internamente. Na nota de rodapé, o autor usa a palavra "inglês" como sinônimo para idioma natural humano (em oposição às linguagens matemáticas de especificação), conceito que na prática se aplicaria da mesma forma ao português.
