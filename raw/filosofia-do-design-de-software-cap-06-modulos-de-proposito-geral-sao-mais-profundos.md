# Capítulo 6 — Módulos de Propósito Geral são Mais Profundos
O processo de lecionar meu curso de design de software, no qual estou constantemente tentando identificar as causas da complexidade no código dos alunos, mudou minha forma de pensar sobre o design de software de várias maneiras. A mais importante delas tem a ver com generalidade versus especialização. Tenho notado repetidas vezes que a especialização leva à complexidade; agora acredito que a superespecialização talvez seja a maior causa isolada de complexidade em software. Por outro lado, um código de propósito mais geral é mais simples, mais limpo e mais fácil de entender.

Esse princípio se aplica a muitos níveis diferentes no design de software. Ao projetar módulos como classes ou métodos, uma das melhores maneiras de produzir uma API profunda é torná-la de propósito geral (APIs de uso geral resultam em maior ocultação de informações). Ao escrever o código detalhado, uma das formas mais eficazes de simplificá-lo é eliminando casos especiais, de modo que o código voltado para o caso comum lide também com as exceções. Eliminar casos especiais também pode tornar o código mais eficiente, como veremos no Capítulo 20.

Este capítulo discute os problemas causados pela especialização e os benefícios da generalidade. A especialização não pode ser completamente eliminada, portanto, o capítulo também oferece diretrizes sobre como separar o código de propósito específico do código de propósito geral.

## 6.1 Torne as classes um tanto de uso geral

Uma das decisões mais comuns que você enfrentará ao projetar uma nova classe é se deve implementá-la de forma a ter um propósito geral ou um propósito específico. Alguns podem argumentar que você deve adotar uma abordagem de uso geral, na qual você implementa um mecanismo que pode ser usado para resolver uma ampla gama de problemas, não apenas aqueles que são importantes hoje. Nesse caso, o novo mecanismo pode encontrar usos imprevistos no futuro, economizando tempo assim. A abordagem de uso geral parece consistente com a mentalidade de investimento discutida no Capítulo 3, em que você gasta um pouco mais de tempo logo de cara para economizar tempo depois.

Por outro lado, sabemos que é difícil prever as necessidades futuras de um sistema de software, então uma solução de uso geral pode incluir recursos que nunca serão realmente necessários. Além disso, se você implementar algo que seja genérico até demais, pode ser que ele não resolva muito bem o problema específico que você tem hoje. Como resultado, alguns podem argumentar que é melhor focar nas necessidades de hoje, construindo apenas o que você sabe que precisa e especializando a solução para a forma como planeja usá-la atualmente. Se você adotar a abordagem de uso específico e descobrir usos adicionais mais tarde, sempre poderá refatorar o código para torná-lo de uso geral. A abordagem de uso específico parece consistente com uma abordagem incremental para o desenvolvimento de software.

Quando comecei a dar minhas aulas de design de software, eu tendia mais para a segunda abordagem (fazer algo de uso específico para começar), mas depois de ministrar o curso algumas vezes, mudei de ideia. Ao revisar os projetos dos alunos, notei que as classes de uso geral eram quase sempre melhores do que as alternativas de uso específico. O que me surpreendeu particularmente é que as interfaces de uso geral são mais simples e mais profundas do que as de uso específico, e resultam em menos código na implementação. Acontece que, mesmo que você use uma classe com um propósito específico, dá menos trabalho construí-la como algo de uso geral. E a abordagem de uso geral pode economizar ainda mais tempo no futuro, se você reutilizar a classe para outros fins. Mas a abordagem de uso geral continua sendo melhor mesmo que você não reutilize a classe.

Na minha experiência, o ponto ideal é implementar novos módulos de uma forma um tanto de uso geral. A expressão "um tanto de uso geral" significa que a funcionalidade do módulo deve refletir suas necessidades atuais, mas sua interface não. Em vez disso, a interface deve ser geral o suficiente para dar suporte a múltiplos usos. A interface deve ser fácil de usar para as necessidades de hoje sem estar especificamente atrelada a elas. O termo "um tanto" é importante: não se empolgue a ponto de construir algo tão genérico que fique difícil de usar para as suas necessidades atuais.

## 6.2 Exemplo: armazenando texto para um editor

Vamos considerar um exemplo de uma aula de design de software em que os alunos foram solicitados a construir um editor de texto simples com interface gráfica (GUI). O editor precisava exibir um arquivo e permitir que os usuários apontassem, clicassem e digitassem para editar o arquivo. Ele também precisava suportar múltiplas visualizações simultâneas do mesmo arquivo em janelas diferentes, e tinha que suportar desfazer e refazer em vários níveis para as modificações no arquivo.

Cada um dos projetos dos alunos incluía uma classe que gerenciava o texto subjacente do arquivo. As classes de texto normalmente forneciam métodos para carregar um arquivo na memória, ler e modificar o texto do arquivo, e gravar o texto modificado de volta em um arquivo. Muitas das equipes de alunos implementaram APIs de propósito específico para a classe de texto.

Eles sabiam que a classe seria usada em um editor interativo, então pensaram nos recursos que o editor precisava fornecer e adaptaram a API da classe de texto a esses recursos específicos. Por exemplo, se um usuário do editor digitasse a tecla backspace, o editor deletava o caractere imediatamente à esquerda do cursor; se o usuário digitasse a tecla delete, o editor deletava o caractere imediatamente à direita do cursor. Sabendo disso, algumas das equipes criaram um método na classe de texto para suportar cada um desses recursos específicos:

```java
void backspace(Cursor cursor);
void delete(Cursor cursor);
```

Cada um desses métodos recebe a posição do cursor como argumento; um tipo especial `Cursor` representa essa posição. O editor também precisava suportar uma seleção que pudesse ser copiada ou deletada. Os alunos lidaram com isso definindo uma classe `Selection` e passando um objeto dessa classe para a classe de texto durante as exclusões:

```java
void deleteSelection(Selection selection);
```

Os alunos provavelmente pensaram que seria mais fácil implementar a interface de usuário se os métodos da classe de texto correspondessem aos recursos visíveis aos usuários. Na realidade, no entanto, essa especialização trouxe pouco benefício para o código da interface de usuário e criou uma alta carga cognitiva para os desenvolvedores que trabalhavam tanto na interface de usuário quanto na classe de texto. A classe de texto acabou com um grande número de métodos rasos, cada um dos quais era adequado apenas para uma operação da interface de usuário. Muitos dos métodos, como o `delete`, eram invocados em apenas um único lugar. Como resultado, um desenvolvedor trabalhando na interface de usuário tinha que aprender sobre um grande número de métodos para a classe de texto.

Essa abordagem criou um vazamento de informações entre a interface de usuário e a classe de texto. Abstrações relacionadas à interface de usuário, como a seleção ou a tecla backspace, foram refletidas na classe de texto; isso aumentou a carga cognitiva para os desenvolvedores trabalhando na classe de texto. Cada nova operação da interface de usuário exigia a definição de um novo método na classe de texto, de modo que um desenvolvedor trabalhando na interface de usuário provavelmente acabaria trabalhando na classe de texto também. Um dos objetivos no design de classes é permitir que cada classe seja desenvolvida de forma independente, mas a abordagem especializada amarrou as classes de interface de usuário e de texto juntas.

## 6.3 Uma API de uso mais geral

Uma abordagem melhor é tornar a classe de texto mais genérica. Sua API deve ser definida apenas em termos de recursos básicos de texto, sem refletir as operações de alto nível que serão implementadas com ela. Por exemplo, apenas dois métodos são necessários para modificar o texto:

```java
void insert(Position position, String newText);
void delete(Position start, Position end);
```

O primeiro método insere uma string arbitrária em uma posição arbitrária dentro do texto, e o segundo método exclui todos os caracteres em posições maiores ou iguais a `start`, mas menores que `end`. Essa API também usa um tipo mais genérico `Position` em vez de `Cursor`, que reflete uma interface de usuário específica. A classe de texto também deve fornecer recursos de uso geral para manipular posições dentro do texto, como o seguinte:

```java
Position changePosition(Position position, int numChars);
```

Este método retorna uma nova posição que está a um determinado número de caracteres de distância de uma posição fornecida. Se o argumento `numChars` for positivo, a nova posição será mais adiante no arquivo do que `position`; se `numChars` for negativo, a nova posição será anterior a `position`. O método pula automaticamente para a linha seguinte ou anterior quando necessário. Com esses métodos, a tecla delete pode ser implementada com o seguinte código (presumindo que a variável `cursor` mantenha a posição atual do cursor):

```java
text.delete(cursor, text.changePosition(cursor, 1));
```

De forma semelhante, a tecla backspace pode ser implementada da seguinte maneira:

```java
text.delete(text.changePosition(cursor, -1), cursor);
```

Com a API de texto de uso geral, o código para implementar funções da interface de usuário, como delete e backspace, é um pouco mais longo do que com a abordagem original usando uma API de texto especializada. No entanto, o novo código é mais óbvio que o código antigo. Um desenvolvedor trabalhando no módulo de interface de usuário provavelmente se importa com quais caracteres são excluídos pela tecla backspace. Com o novo código, isso é óbvio. Com o código antigo, o desenvolvedor teria que ir até a classe de texto e ler a documentação e/ou o código do método `backspace` para verificar o comportamento. Além disso, a abordagem de uso geral tem menos código no total do que a abordagem especializada, uma vez que substitui um grande número de métodos de propósito específico na classe de texto por um número menor de métodos de uso geral.

Uma classe de texto implementada com a interface de uso geral poderia, potencialmente, ser usada para outros propósitos além de um editor interativo. Como exemplo, suponha que você estivesse construindo uma aplicação que modificasse um arquivo especificado substituindo todas as ocorrências de uma string em particular por outra string. Métodos da classe de texto especializada, como `backspace` e `delete`, teriam pouco valor para essa aplicação. No entanto, a classe de texto de uso geral já teria a maior parte da funcionalidade necessária para a nova aplicação. Tudo o que falta é um método para buscar a próxima ocorrência de uma determinada string, como este:

```java
Position findNext(Position start, String string);
```

Naturalmente, é provável que um editor de texto interativo tenha um mecanismo de busca e substituição, caso em que a classe de texto já incluiria este método.

> **Nota do Tradutor (N.T.):** O termo "string" foi mantido no original, pois é o jargão técnico consagrado na comunidade de desenvolvimento de software no Brasil. Da mesma forma, delete e backspace foram mantidos para se referirem inequivocamente às teclas correspondentes na interface e aos métodos do código.

## 6.4 A generalidade leva a um melhor ocultamento de informação

A abordagem de uso geral fornece uma separação mais limpa entre as classes de texto e de interface de usuário, o que resulta em um melhor ocultamento de informação. A classe de texto não precisa ter conhecimento das especificidades da interface de usuário, como a forma em que a tecla backspace é tratada; esses detalhes agora estão encapsulados na classe de interface de usuário. Novos recursos de interface de usuário podem ser adicionados sem a necessidade de criar novas funções de suporte na classe de texto. A interface de uso geral também reduz a carga cognitiva: um desenvolvedor trabalhando na interface de usuário só precisa aprender alguns métodos simples, que podem ser reutilizados para diversas finalidades.

O método `backspace` na versão original da classe de texto era uma falsa abstração. Ele supostamente ocultava informações sobre quais caracteres são excluídos, mas o módulo de interface de usuário realmente precisa saber disso; os desenvolvedores de interface de usuário provavelmente lerão o código do método `backspace` para confirmar seu comportamento exato. Colocar o método na classe de texto apenas torna mais difícil para os desenvolvedores de interface de usuário obterem as informações de que precisam. Um dos elementos mais importantes do design de software é determinar quem precisa saber o quê, e quando. Quando os detalhes são importantes, é melhor torná-los explícitos e o mais óbvios possível, a exemplo da implementação revisada da operação de backspace. Ocultar essas informações por trás de uma interface apenas cria obscuridade.

## 6.5 Perguntas para se fazer

É mais fácil reconhecer o design de uma classe limpa de uso geral do que criar uma. Aqui estão algumas perguntas que você pode se fazer, que o ajudarão a encontrar o equilíbrio certo entre o uso geral e o uso específico para uma interface.

Qual é a interface mais simples que cobrirá todas as minhas necessidades atuais? Se você reduzir o número de métodos em uma API sem reduzir suas capacidades gerais, então você provavelmente está criando métodos de uso mais geral. A API de texto de uso específico tinha pelo menos três métodos para deletar texto: `backspace`, `delete` e `deleteSelection`. A API de uso mais geral tinha apenas um método para deletar texto, que servia aos três propósitos. Reduzir o número de métodos só faz sentido enquanto a API para cada método individual permanecer simples; se você tiver que introduzir muitos argumentos adicionais para reduzir o número de métodos, talvez você não esteja realmente simplificando as coisas.

Em quantas situações esse método será usado? Se um método é projetado para um uso particular, como o método `backspace`, isso é um sinal de alerta de que ele pode ser de uso muito específico. Veja se você consegue substituir vários métodos de uso específico por um único método de uso geral.

Esta API é fácil de usar para as minhas necessidades atuais? Essa pergunta pode ajudá-lo a determinar quando você foi longe demais ao tornar uma API simples e de uso geral. Se você tiver que escrever muito código adicional para usar uma classe para seu propósito atual, isso é um sinal de alerta de que a interface não fornece a funcionalidade certa. Por exemplo, uma abordagem para a classe de texto seria projetá-la em torno de operações de caractere único: `insert` insere um único caractere e `delete` exclui um único caractere. Esta API é ao mesmo tempo simples e de uso geral. No entanto, ela não seria particularmente fácil de usar para um editor de texto: o código de nível mais alto conteria muitos loops para inserir ou excluir intervalos de caracteres. A abordagem de caractere único também seria ineficiente para grandes operações.

Portanto, é melhor que a classe de texto tenha suporte nativo para operações em intervalos de caracteres.

## 6.6 Empurre a especialização para cima (e para baixo!)

A maioria dos sistemas de software inevitavelmente deve ter algum código que seja especializado. Por exemplo, as aplicações fornecem recursos específicos para seus usuários; estes são frequentemente muito especializados. Portanto, geralmente não é possível eliminar a especialização por completo. No entanto, o código especializado deve ser claramente separado do código de uso geral. Isso pode ser feito empurrando o código especializado para cima ou para baixo na pilha de software.

Uma forma de separar o código especializado é empurrá-lo para cima. As classes de nível superior de uma aplicação, que fornecem recursos específicos, serão necessariamente especializadas para esses recursos. Mas essa especialização não precisa se propagar para as classes de nível inferior que são usadas para implementar os recursos. Vimos isso no exemplo do editor no início deste capítulo. A implementação original do aluno vazava detalhes especializados da interface do usuário, como o comportamento da tecla backspace, para a implementação da classe de texto. A API de texto aprimorada empurrou toda a especialização para cima, para o código da interface do usuário, deixando apenas o código de uso geral na classe de texto.

Às vezes, a melhor abordagem é empurrar a especialização para baixo. Um exemplo disso são os drivers de dispositivo. Um sistema operacional geralmente precisa suportar centenas ou milhares de tipos diferentes de dispositivos, como diferentes tipos de dispositivos de armazenamento secundário. Cada um desses tipos de dispositivos possui seu próprio conjunto de comandos especializado. Para evitar que características especializadas dos dispositivos vazem para o código principal do sistema operacional, os sistemas operacionais definem uma interface com operações de uso geral que qualquer dispositivo de armazenamento secundário deve implementar, como “ler um bloco” e “escrever um bloco”. Para cada dispositivo diferente, um módulo de driver de dispositivo implementa a interface de uso geral usando os recursos especializados daquele dispositivo específico. Essa abordagem empurra a especialização para baixo, para os drivers de dispositivo, de modo que o núcleo do sistema operacional possa ser escrito sem nenhum conhecimento das características específicas do dispositivo. Essa abordagem também facilita a adição de novos dispositivos: se um dispositivo tiver recursos suficientes para implementar a interface do driver de dispositivo, ele poderá ser adicionado ao sistema sem nenhuma alteração no sistema operacional principal.

## 6.7 Exemplo: mecanismo de desfazer do editor

No projeto do editor com interface gráfica (GUI), um dos requisitos era suportar múltiplos níveis de desfazer/refazer, não apenas para alterações no próprio texto, mas também para mudanças na seleção, no cursor de inserção e na visualização. Por exemplo, se um usuário seleciona um texto, o exclui, rola para um lugar diferente no arquivo e então aciona o comando para desfazer, o editor deve restaurar seu estado para o que era exatamente antes da exclusão. Isso inclui restaurar o texto excluído, selecioná-lo novamente e também tornar o texto selecionado visível na janela.

Alguns dos projetos dos alunos implementaram todo o mecanismo de desfazer como parte da classe de texto. A classe de texto mantinha uma lista de todas as alterações que podiam ser desfeitas. Ela adicionava entradas a essa lista automaticamente sempre que o texto era alterado. Para alterações na seleção, no cursor de inserção e na visualização, o código da interface do usuário invocava métodos adicionais na classe de texto, que então adicionava entradas referentes a essas alterações à lista de desfazer. Quando o usuário solicitava desfazer ou refazer, o código da interface do usuário invocava um método na classe de texto, que então processava as entradas na lista de desfazer. Para entradas relacionadas ao texto, ela atualizava os componentes internos da classe de texto; para entradas relacionadas a outras coisas, como a seleção, a classe de texto fazia uma chamada de retorno (callback) ao código da interface do usuário para executar o desfazer ou refazer.

Essa abordagem resultou em um conjunto estranho de funcionalidades na classe de texto. O núcleo do desfazer/refazer consiste em um mecanismo de propósito geral para gerenciar uma lista de ações que foram executadas e percorrer essas ações durante as operações de desfazer e refazer. O núcleo estava localizado na classe de texto junto com manipuladores de propósito específico que implementavam o desfazer e refazer para coisas específicas, como o texto e a seleção. Os manipuladores de desfazer de propósito específico para a seleção e para o cursor não tinham relação com mais nada na classe de texto; eles resultaram em vazamento de informações entre a classe de texto e a interface do usuário, bem como em métodos extras em cada módulo para passar informações de desfazer de um lado para o outro. Se um novo tipo de entidade que pudesse ser desfeita fosse adicionada ao sistema no futuro, isso exigiria mudanças na classe de texto, incluindo novos métodos específicos para essa entidade. Além disso, o núcleo de desfazer de propósito geral tinha pouca relação com os recursos de texto de propósito geral da classe.

Esses problemas podem ser resolvidos extraindo o núcleo de propósito geral do mecanismo de desfazer/refazer e colocando-o em uma classe separada:

```java
public class History {
    public interface Action {
        public void redo();
        public void undo();
    }

    History() {...}

    void addAction(Action action) {...}
    void addFence() {...}

    void undo() {...}
    void redo() {...}
}
```

Neste design, a classe `History` gerencia uma coleção de objetos que implementam a interface `History.Action`. Cada `History.Action` descreve uma única operação, como uma inserção de texto ou uma mudança na localização do cursor, e fornece métodos que podem desfazer ou refazer a operação. A classe `History` não sabe nada sobre as informações armazenadas nas ações ou como elas implementam seus métodos `undo` e `redo`. `History` mantém uma lista de histórico que descreve todas as ações executadas ao longo da vida útil de um aplicativo, e fornece métodos `undo` e `redo` que caminham para trás e para frente através da lista em resposta aos pedidos de desfazer e refazer do usuário, chamando os métodos `undo` e `redo` nas `History.Action`s.

As `History.Action`s são objetos de propósito específico: cada uma entende um tipo particular de operação que pode ser desfeita. Elas são implementadas fora da classe `History`, em módulos que entendem tipos específicos de ações que podem ser desfeitas. A classe de texto poderia implementar objetos `UndoableInsert` e `UndoableDelete` para descrever inserções e exclusões de texto. Sempre que insere texto, a classe de texto cria um novo objeto `UndoableInsert` descrevendo a inserção e invoca `History.addAction` para adicioná-lo à lista de histórico. O código da interface do usuário do editor poderia criar objetos `UndoableSelection` e `UndoableCursor` que descrevem mudanças na seleção e no cursor de inserção.

A classe `History` também permite que as ações sejam agrupadas para que, por exemplo, uma única solicitação de desfazer do usuário possa restaurar um texto excluído, selecionar novamente o texto excluído e reposicionar o cursor de inserção. Para implementar o agrupamento, a classe `History` usa *fences* (cercas/barreiras), que são marcadores colocados na lista de histórico para separar grupos de ações relacionadas. Cada chamada para `History.redo` caminha para trás na lista de histórico, desfazendo ações até atingir a próxima barreira. O posicionamento das barreiras é determinado por código de nível mais alto, invocando `History.addFence`.

Essa abordagem divide a funcionalidade de desfazer em três categorias, cada uma implementada em um lugar diferente:

- Um mecanismo de propósito geral para gerenciar e agrupar ações e invocar as operações de desfazer/refazer (implementado pela classe `History`).
- As especificidades de ações particulares (implementadas por uma variedade de classes, cada uma compreendendo um pequeno número de tipos de ação).
- A política de agrupamento de ações (implementada por código de interface de usuário de alto nível para fornecer o comportamento geral correto da aplicação).

Cada uma dessas categorias pode ser implementada sem nenhum conhecimento das outras categorias. A classe `History` não sabe que tipo de ações estão sendo desfeitas; ela poderia ser usada em uma variedade de aplicações. Cada classe de ação entende apenas um único tipo de ação, e nem a classe `History` nem as classes de ação precisam estar cientes da política para agrupar ações.

A decisão de design fundamental foi a de separar a parte de propósito geral do mecanismo de desfazer das partes de propósito específico, criando uma classe separada para a parte de propósito geral e empurrando as partes de propósito específico para subclasses de `History.Action`. Uma vez feito isso, o restante do design surgiu naturalmente.

**Nota:** a sugestão de separar código de propósito geral de código de propósito específico refere-se a código relacionado a um mecanismo particular. Por exemplo, o código de desfazer de propósito específico (como o código para desfazer uma inserção de texto) deve ser separado do código de desfazer de propósito geral (como o código para gerenciar a lista de histórico). No entanto, pode fazer sentido combinar o código de propósito específico para um mecanismo com o código de propósito geral para outro. A classe de texto é um exemplo disso: ela implementa um mecanismo de propósito geral para o gerenciamento de texto, mas inclui código de propósito específico relacionado a desfazer. O código de desfazer é de propósito específico porque lida apenas com operações de desfazer para modificações de texto. Não faz sentido combinar esse código com a infraestrutura de desfazer de propósito geral na classe `History`, mas faz sentido colocá-lo na classe de texto, já que ele está intimamente relacionado a outras funções de texto.

> **N.T. (Nota do Tradutor):** No texto original da imagem, há a menção "Each call to `History.redo` walks backwards through the history list, undoing actions...". Em termos de lógica de software, caminhar para trás desfazendo ações seria a função do método `undo`, e não `redo`. Contudo, a tradução manteve a literalidade do termo impresso no original para fidelidade ao documento. A palavra "fences" foi traduzida contextualmente como "barreiras" ou "cercas", mantendo o conceito técnico de demarcação de limite na estrutura de dados.

## 6.8 Elimine casos especiais no código

Até este ponto, venho discutindo a especialização no contexto do design de classes e métodos. Outra forma de especialização ocorre no código dos corpos dos métodos, na forma de casos especiais. Casos especiais podem resultar em um código repleto de instruções `if`, o que torna o código difícil de entender e propenso a bugs. Portanto, os casos especiais devem ser eliminados sempre que possível. A melhor maneira de fazer isso é projetando o caso normal de forma que ele lide automaticamente com as condições de contorno sem nenhum código extra.

No projeto do editor de texto, os alunos tiveram que implementar um mecanismo para selecionar texto e copiar ou excluir a seleção. A maioria dos alunos introduziu uma variável de estado em sua implementação de seleção para indicar se a seleção existe ou não. Eles provavelmente escolheram essa abordagem porque há momentos em que nenhuma seleção é visível na tela, então pareceu natural representar essa noção na implementação. No entanto, essa abordagem resultou em inúmeras verificações para detectar a condição de "nenhuma seleção" e lidar com ela de forma especial.

O código de manipulação da seleção pode ser simplificado eliminando o caso especial de "nenhuma seleção", de modo que a seleção sempre exista. Quando não há nenhuma seleção visível na tela, isso pode ser representado internamente com uma seleção vazia, cujas posições inicial e final são as mesmas. Com essa abordagem, o código de gerenciamento de seleção pode ser escrito sem nenhuma verificação para "nenhuma seleção". Ao copiar a seleção, se a seleção estiver vazia, então 0 bytes serão inseridos no novo local; se implementado corretamente, não haverá necessidade de verificar os 0 bytes como um caso especial. Da mesma forma, deve ser possível projetar o código para excluir a seleção de forma que o caso vazio seja tratado sem nenhuma verificação de caso especial. Considere uma seleção inteira em uma única linha. Para excluir a seleção, extraia a parte da linha que precede a seleção e concatene-a com a parte da linha que a sucede para formar a nova linha. Se a seleção estiver vazia, essa abordagem irá regenerar a linha original.

O Capítulo 10 discutirá as exceções, que criam muito mais casos especiais, e como reduzir o número de locais onde elas devem ser tratadas.

## 6.9 Conclusão

A especialização desnecessária, seja na forma de classes e métodos de propósito específico ou de casos especiais no código, é um fator que contribui significativamente para a complexidade do software. A especialização não pode ser eliminada completamente, mas, com um bom design, você deve ser capaz de reduzi-la consideravelmente e separar o código especializado do código de uso geral. Isso resultará em classes mais profundas, em um melhor ocultamento de informações e em um código mais simples e evidente.
