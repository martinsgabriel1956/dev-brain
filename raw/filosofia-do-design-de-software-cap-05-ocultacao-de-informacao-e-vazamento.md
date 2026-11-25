# Capítulo 5 — Ocultação de Informação (e Vazamento)
O Capítulo 4 argumentou que os módulos devem ser profundos. Este capítulo, e os próximos que se seguem, discutem técnicas para a criação de módulos profundos.

## 5.1 Ocultação de informação

Uma das técnicas mais importantes para se obter módulos profundos é a *ocultação de informação*. Essa técnica foi descrita pela primeira vez em um artigo clássico de David Parnas¹. A ideia básica é que cada módulo deve encapsular alguns conhecimentos, que representam decisões de design. O conhecimento fica embutido na implementação do módulo, mas não aparece em sua interface, de modo que não fica visível para outros módulos.

As informações ocultadas dentro de um módulo geralmente consistem em detalhes sobre como implementar algum mecanismo. Aqui estão alguns exemplos de informações que podem ser ocultadas em um módulo:

- Como armazenar informações em uma árvore B e como acessá-las de forma eficiente.
- Como identificar o bloco físico do disco correspondente a cada bloco lógico dentro de um arquivo.
- Como implementar o protocolo de rede TCP.
- Como agendar *threads* em um processador *multi-core*.
- Como fazer o *parsing* de documentos JSON.

As informações ocultas incluem estruturas de dados e algoritmos relacionados ao mecanismo. Elas também podem incluir detalhes de baixo nível, como o tamanho de uma página, bem como conceitos de alto nível mais abstratos, como a premissa de que a maioria dos arquivos é pequena.

A ocultação de informação reduz a complexidade de duas maneiras. Primeiro, ela simplifica a interface de um módulo. A interface reflete uma visão mais simples e abstrata da funcionalidade do módulo e esconde os detalhes; isso diminui a carga cognitiva dos desenvolvedores que o utilizam. Por exemplo, um desenvolvedor que usa uma classe de árvore B não precisa se preocupar com o *fanout* ideal para os nós da árvore ou com a forma de mantê-la balanceada. Segundo, a ocultação de informação facilita a evolução do sistema. Se um dado está oculto, não existem dependências sobre ele fora do módulo que o contém; logo, uma mudança de design relacionada a essa informação afetará apenas aquele módulo específico. Por exemplo, se o protocolo TCP sofrer alterações (para introduzir um novo mecanismo de controle de congestionamento, por exemplo), a implementação do protocolo precisará ser modificada, mas nenhuma alteração deverá ser necessária no código de alto nível que usa o TCP para enviar e receber dados.

Ao projetar um novo módulo, você deve pensar cuidadosamente sobre quais informações podem ser ocultadas nele. Se for possível ocultar mais coisas, você também será capaz de simplificar a interface do módulo, o que o torna mais profundo.

> **Nota:** ocultar variáveis e métodos em uma classe declarando-os como *private* não é a mesma coisa que ocultação de informação. Elementos privados podem ajudar na ocultação de informação, pois impossibilitam que os itens sejam acessados diretamente de fora da classe. No entanto, informações sobre os itens privados ainda podem ser expostas por meio de métodos públicos, como *getters* e *setters*. Quando isso acontece, a natureza e o uso das variáveis ficam tão expostos quanto se elas fossem públicas.

A melhor forma de ocultação de informação ocorre quando ela está totalmente escondida dentro de um módulo, de forma que se torne irrelevante e invisível para os usuários daquele módulo. Contudo, a ocultação parcial de informação também tem o seu valor. Por exemplo, se um recurso ou dado específico for necessário apenas para alguns usuários de uma classe e for acessado por métodos separados para não ficar visível nos casos de uso mais comuns, então essa informação estará quase que totalmente oculta. Uma informação desse tipo criará menos dependências do que uma que fique visível para todos os usuários da classe.

---

### Notas do Tradutor (N.T.)

- **Módulos profundos (*deep modules*):** Conceito frequentemente associado à obra *A Philosophy of Software Design* de John Ousterhout, referindo-se a módulos que oferecem funcionalidades poderosas e complexas através de uma interface extremamente simples.
- **_Fanout_:** Mantido no original em inglês por ser o jargão padrão em estruturas de dados no Brasil. Refere-se à taxa de ramificação, ou seja, o número de filhos que um nó de uma árvore B pode conter.
- **_Parsing_, _threads_, _multi-core_, _getters_ e _setters_:** Termos amplamente consagrados em inglês na comunidade brasileira de desenvolvimento de software, traduzi-los de forma literal prejudicaria a naturalidade técnica do texto.

## 5.2 Vazamento de informação

O oposto da ocultação de informação é o vazamento de informação. O vazamento de informação ocorre quando uma decisão de design é refletida em múltiplos módulos. Isso cria uma dependência entre os módulos: qualquer alteração nessa decisão de design exigirá mudanças em todos os módulos envolvidos. Se um pedaço de informação é refletido na interface de um módulo, então, por definição, ele vazou; portanto, interfaces mais simples tendem a se correlacionar com uma melhor ocultação de informação. No entanto, a informação pode vazar mesmo que não apareça na interface de um módulo. Suponha que duas classes tenham conhecimento sobre um formato de arquivo específico (talvez uma classe leia arquivos nesse formato e a outra os escreva). Mesmo que nenhuma das classes exponha essa informação em sua interface, ambas dependem do formato do arquivo: se o formato mudar, as duas classes precisarão ser modificadas. Um vazamento “pela porta dos fundos” como esse é mais pernicioso do que o vazamento por meio de uma interface, porque não é óbvio.

O vazamento de informação é um dos principais sinais de alerta no design de software. Uma das melhores habilidades que você pode aprender como designer de software é ter um alto nível de sensibilidade ao vazamento de informação. Se você encontrar vazamento de informação entre classes, pergunte a si mesmo: “Como posso reorganizar essas classes para que esse conhecimento específico afete apenas uma única classe?”. Se as classes afetadas forem relativamente pequenas e estiverem intimamente ligadas à informação vazada, pode fazer sentido fundi-las em uma única classe. Outra abordagem possível é extrair a informação de todas as classes afetadas e criar uma nova classe que encapsule apenas essa informação. No entanto, essa abordagem só será eficaz se você conseguir encontrar uma interface simples que abstraia os detalhes; se a nova classe expuser a maior parte do conhecimento através de sua interface, ela não trará muito valor (você terá simplesmente substituído o vazamento pela porta dos fundos por um vazamento através de uma interface).

---

### Notas do Tradutor (N.T.)

- **_Information hiding_:** Traduzido literalmente como “ocultação de informação”, conceito clássico cunhado por David Parnas. No dia a dia do desenvolvimento no Brasil, o termo “encapsulamento” também é frequentemente utilizado para descrever o mesmo princípio.
- **_Red flags_:** Adaptado para “sinais de alerta”, jargão amplamente compreendido na área de tecnologia brasileira para descrever indícios (ou “sintomas”) de que há um problema estrutural no código ou na arquitetura (como os *code smells*).
- **_Back-door leakage_:** Traduzido como vazamento “pela porta dos fundos”. A metáfora funciona perfeitamente em PT-BR para indicar algo que acontece de forma oculta, sub-reptícia ou não declarada (fora dos contratos e interfaces públicas das classes).

## 5.3 Decomposição temporal

Uma causa comum do vazamento de informações é um estilo de design que eu chamo de decomposição temporal. Na decomposição temporal, a estrutura de um sistema corresponde à ordem cronológica em que as operações ocorrerão. Considere uma aplicação que lê um arquivo em um formato específico, modifica o conteúdo desse arquivo e, em seguida, o grava novamente. Com a decomposição temporal, essa aplicação poderia ser dividida em três classes: uma para ler o arquivo, outra para realizar as modificações e uma terceira para gravar a nova versão. Tanto a etapa de leitura quanto a de gravação do arquivo possuem conhecimento sobre o formato do arquivo, o que resulta em vazamento de informações. A solução é combinar os mecanismos centrais de leitura e gravação de arquivos em uma única classe. Essa classe será utilizada tanto durante as fases de leitura quanto de gravação da aplicação. É fácil cair na armadilha da decomposição temporal, pois a ordem em que as operações devem ocorrer costuma estar na sua mente na hora de programar. No entanto, a maioria das decisões de design se manifesta em vários momentos diferentes ao longo do ciclo de vida da aplicação; como resultado, a decomposição temporal frequentemente resulta em vazamento de informações.

> **🚩 Sinal de Alerta: Vazamento de Informações 🚩**
>
> O vazamento de informações ocorre quando o mesmo conhecimento é utilizado em múltiplos lugares, como em duas classes diferentes que compreendem o formato de um tipo específico de arquivo.
>
> A ordem geralmente importa, então ela será refletida em algum lugar da aplicação. Contudo, ela não deveria ser refletida na estrutura dos módulos, a menos que essa estrutura seja consistente com o ocultamento de informações (talvez as diferentes etapas usem informações totalmente distintas). Ao projetar módulos, concentre-se no conhecimento necessário para executar cada tarefa, e não na ordem em que as tarefas ocorrem.

---

### Notas do Tradutor (N.T.)

- **_Red Flag_:** O termo original foi traduzido como “Sinal de Alerta” para soar mais natural no jargão técnico e corporativo brasileiro, mantendo o sentido original de um aviso crítico.

## 5.4 Exemplo: Servidor HTTP

Para ilustrar as questões sobre ocultação de informação, vamos considerar as decisões de design tomadas por alunos que implementaram o protocolo HTTP em um curso de design de software. É útil observar tanto o que eles fizeram bem quanto as áreas em que tiveram problemas.

O HTTP é um mecanismo usado pelos navegadores da Web para se comunicarem com os servidores da Web. Quando um usuário clica em um link em um navegador da Web ou envia um formulário, o navegador usa o HTTP para enviar uma requisição pela rede para um servidor da Web. Assim que o servidor processa a requisição, ele envia uma resposta de volta ao navegador; normalmente, a resposta contém uma nova página da Web para ser exibida. O protocolo HTTP especifica o formato das requisições e respostas, ambas representadas textualmente. A Figura 5.1 mostra um exemplo de requisição HTTP descrevendo o envio de um formulário. Foi solicitado aos alunos do curso que implementassem uma ou mais classes para facilitar aos servidores da Web o recebimento de requisições HTTP e o envio de respostas.

> **🚩 Sinal de Alerta: Decomposição Temporal 🚩**
>
> Na decomposição temporal, a ordem de execução reflete-se na estrutura do código: operações que ocorrem em momentos diferentes ficam em métodos ou classes diferentes. Se o mesmo conhecimento é usado em pontos diferentes da execução, ele acaba sendo codificado em vários lugares, resultando em vazamento de informação.

```text
Método      URL                                 Parâmetro(s) Versão do Protocolo
  ↓          ↓                                       ↓            ↓
POST /comments/create?photo_id=246 HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html, */*
Accept-Language: en-us                                              } Cabeçalhos
Accept-Charset: ISO-8859-1,utf-8
Content-Length: 40

comment=What+a+cute+baby%21&priority=low <— Corpo
```

**Figura 5.1:** Uma requisição POST no protocolo HTTP consiste em texto enviado por meio de um socket TCP. Cada requisição contém uma linha inicial, um conjunto de cabeçalhos terminados por uma linha em branco, e um corpo opcional. A linha inicial contém o tipo de requisição (`POST` é usado para enviar dados de formulário), uma URL indicando uma operação (`/comments/create`) e parâmetros opcionais (`photo_id` tem o valor `246`), além da versão do protocolo HTTP usada pelo remetente. Cada linha de cabeçalho consiste em um nome, como `Content-Length`, seguido por seu valor. Para esta requisição, o corpo contém parâmetros adicionais (`comment` e `priority`).

## 5.5 Exemplo: classes demais

O erro mais comum cometido pelos alunos foi dividir seu código em um grande número de classes rasas, o que levou ao vazamento de informações entre as classes. Uma equipe usou duas classes diferentes para receber requisições HTTP; a primeira classe lia a requisição a partir da conexão de rede para uma string, e a segunda classe analisava a string. Este é um exemplo de decomposição temporal (“primeiro lemos a requisição, depois a analisamos”). O vazamento de informações ocorreu porque uma requisição HTTP não pode ser lida sem que se analise grande parte da mensagem; por exemplo, o cabeçalho `Content-Length` especifica o tamanho do corpo da requisição, portanto, os cabeçalhos devem ser analisados para que se possa calcular o tamanho total da requisição. Como resultado, ambas as classes precisavam entender a maior parte da estrutura das requisições HTTP, e o código de análise foi duplicado em ambas. Essa abordagem também criou uma complexidade extra para os chamadores, que precisavam invocar dois métodos em classes diferentes, em uma ordem específica, para receber uma requisição.

Como as classes compartilhavam tanta informação, teria sido melhor mesclá-las em uma única classe que lidasse tanto com a leitura quanto com a análise da requisição. Isso proporciona um melhor ocultamento de informações, pois isola todo o conhecimento sobre o formato da requisição em uma única classe, além de fornecer uma interface mais simples para os chamadores (apenas um método para invocar).

Este exemplo ilustra um tema geral no design de software: o ocultamento de informações muitas vezes pode ser melhorado tornando uma classe um pouco maior. Um dos motivos para fazer isso é reunir todo o código relacionado a uma capacidade específica (como a análise de uma requisição HTTP), de modo que a classe resultante contenha tudo o que diz respeito a essa capacidade. Um segundo motivo para aumentar o tamanho de uma classe é elevar o nível da interface; por exemplo, em vez de ter métodos separados para cada uma das três etapas de um processamento, ter um único método que execute o processamento inteiro. Isso pode resultar em uma interface mais simples. Ambos os benefícios se aplicam ao exemplo do parágrafo anterior: combinar as classes reúne todo o código relacionado à análise de uma requisição HTTP e substitui dois métodos visíveis externamente por apenas um. A classe combinada é mais profunda do que as classes originais.

É claro que é possível levar a noção de classes maiores longe demais (como ter uma única classe para a aplicação inteira). O [Capítulo 9] discutirá as condições sob as quais faz sentido separar o código em várias classes menores.

---

### Notas do Tradutor (N.T.)

- **“Analisava” / “Análise”:** Tradução direta de *parsed* / *parsing*. No cotidiano do desenvolvimento de software no Brasil, é extremamente comum utilizar o anglicismo “fazer o *parsing*” ou “parsear”.
- **“Classes rasas” / “mais profunda”:** Tradução de *shallow classes* e *deeper*. No contexto de design de software (frequentemente associado à filosofia de John Ousterhout), uma classe “profunda” (*deep class*) é aquela que oferece uma interface simples, mas oculta uma grande complexidade interna, enquanto uma classe “rasa” (*shallow class*) tem uma interface complexa para pouca funcionalidade.
- **“Chamadores”:** Tradução de *callers*. Refere-se aos trechos de código ou outras classes que invocam (chamam) os métodos da classe em questão (também frequentemente chamados de “clientes” da classe no Brasil).

## 5.6 Exemplo: Manipulação de parâmetros HTTP

Depois que uma requisição HTTP é recebida por um servidor, o servidor precisa acessar algumas das informações da requisição. O código que lida com a requisição na Figura 5.1 pode precisar saber o valor do parâmetro `photo_id`. Parâmetros podem ser especificados na primeira linha da requisição (`photo_id` na Figura 5.1) ou, às vezes, no corpo (`comment` e `priority` na Figura 5.1). Cada parâmetro tem um nome e um valor. Os valores dos parâmetros usam uma codificação especial chamada *URL encoding* (codificação de URL); por exemplo, no valor de `comment` na Figura 5.1, “+” é usado para representar um caractere de espaço, e “%21” é usado em vez de “!”. Para processar uma requisição, o servidor precisará dos valores para alguns dos parâmetros, e vai querê-los em sua forma não codificada.

A maioria dos projetos dos alunos fez duas boas escolhas com relação à manipulação de parâmetros. Primeiro, eles reconheceram que aplicações de servidor não se importam se um parâmetro é especificado na linha de cabeçalho ou no corpo da requisição, então eles ocultaram essa distinção de quem faz a chamada (*callers*) e mesclaram os parâmetros de ambos os locais. Segundo, eles ocultaram o conhecimento sobre o *URL encoding*: o analisador (*parser*) HTTP decodifica os valores dos parâmetros antes de retorná-los ao servidor Web, de modo que o valor do parâmetro `comment` na Figura 5.1 será retornado como “What a cute baby!”, e não “What+a+cute+baby%21”. Em ambos os casos, a ocultação de informações resultou em APIs mais simples para o código que utiliza o módulo HTTP.

No entanto, a maioria dos alunos usou uma interface para retornar parâmetros que era muito rasa (*shallow*), e isso resultou em oportunidades perdidas de ocultação de informação. A maioria dos projetos usou um objeto do tipo `HTTPRequest` para armazenar a requisição HTTP analisada, e a classe `HTTPRequest` tinha um único método como o seguinte para retornar parâmetros:

```java
public Map<String, String> getParams() {
    return this.params;
}
```

Em vez de retornar um único parâmetro, o método retorna uma referência ao `Map` usado internamente para armazenar todos os parâmetros. Este método é raso, e expõe a representação interna usada pela classe `HTTPRequest` para armazenar parâmetros. Qualquer mudança nessa representação resultará em uma mudança na interface, o que exigirá modificações em todos os chamadores. Quando as implementações são modificadas, as mudanças geralmente envolvem alterações na representação de estruturas de dados essenciais (para melhorar o desempenho, por exemplo). Portanto, é importante evitar expor estruturas de dados internas tanto quanto possível. Essa abordagem também dá mais trabalho para os chamadores: um chamador deve primeiro invocar `getParams`, e depois deve chamar outro método para recuperar um parâmetro específico do `Map`. Por fim, os chamadores devem perceber que não devem modificar o `Map` retornado por `getParams`, já que isso afetará o estado interno de `HTTPRequest`.

Aqui está uma interface melhor para recuperar valores de parâmetros:

```java
public String getParameter(String name) { ... }
public int getIntParameter(String name) { ... }
```

`getParameter` retorna o valor de um parâmetro como uma *string*. Isso fornece uma interface um pouco mais profunda (*deeper*) do que o `getParams` acima; mais importante, ela oculta a representação interna dos parâmetros. `getIntParameter` converte o valor de um parâmetro de sua forma em *string* na requisição HTTP para um número inteiro (por exemplo, o parâmetro `photo_id` na Figura 5.1). Isso poupa o chamador de ter que solicitar a conversão de *string* para inteiro separadamente, e oculta esse mecanismo do chamador. Métodos adicionais para outros tipos de dados, como `getDoubleParameter`, poderiam ser definidos se necessário. (Todos esses métodos lançarão exceções se o parâmetro desejado não existir, ou se não puder ser convertido para o tipo solicitado; as declarações de exceção foram omitidas no código acima).

---

### Notas do Tradutor (N.T.)

- **_Callers_:** Traduzido como “quem faz a chamada” ou “chamadores”, referindo-se aos componentes de código ou métodos que invocam as funções da API.
- **_Parser_ e _URL encoding_:** Mantidos no original, com explicação entre parênteses, por serem amplamente utilizados no mercado de tecnologia brasileiro.

## 5.7 Exemplo: valores padrão em respostas HTTP

Os projetos HTTP também precisavam fornecer suporte para a geração de respostas HTTP. O erro mais comum que os alunos cometeram nessa área foram valores padrão (*defaults*) inadequados. Cada resposta HTTP deve especificar uma versão do protocolo HTTP; uma equipe exigiu que os chamadores especificassem essa versão explicitamente ao criar um objeto de resposta. No entanto, a versão da resposta deve corresponder àquela do objeto de requisição, e a requisição já deve ser passada como argumento ao enviar a resposta (ela indica para onde enviar a resposta). Portanto, faz mais sentido que as classes HTTP forneçam a versão da resposta automaticamente. É improvável que o chamador saiba qual versão especificar, e se o chamador especificar um valor, isso provavelmente resultará em vazamento de informações entre a biblioteca HTTP e o chamador. As respostas HTTP também incluem um cabeçalho `Date` especificando o momento em que a resposta foi enviada; a biblioteca HTTP também deve fornecer um valor padrão sensato para isso.

Valores padrão ilustram o princípio de que as interfaces devem ser projetadas para tornar o caso comum o mais simples possível. Eles também são um exemplo de ocultação parcial de informações: no caso normal, o chamador não precisa estar ciente da existência do item que possui o valor predefinido. Nos raros casos em que um chamador precisa substituir um valor padrão, ele terá que conhecer o valor e poderá invocar um método especial para modificá-lo.

Sempre que possível, as classes devem “fazer a coisa certa” sem que isso lhes seja solicitado explicitamente. Valores padrão são um exemplo disso. O exemplo de E/S (I/O) do Java na página 26 ilustra esse ponto de maneira negativa. O uso de *buffers* em E/S de arquivos é algo tão universalmente desejável que ninguém deveria ter que solicitar explicitamente por isso, ou mesmo estar ciente de sua existência; as classes de E/S devem fazer a coisa certa e fornecer isso automaticamente. As melhores funcionalidades são aquelas que você obtém sem sequer saber que existem.

> **🚩 Bandeira Vermelha: Superexposição 🚩**
>
> Se a API de um recurso muito utilizado obriga os usuários a aprenderem sobre outros recursos que raramente são usados, isso aumenta a carga cognitiva dos usuários que não precisam desses recursos menos frequentes.

## 5.8 Ocultação de informação dentro de uma classe

Os exemplos neste capítulo focaram na ocultação de informação no que se refere às APIs externamente visíveis das classes, mas a ocultação de informação também pode ser aplicada em outros níveis do sistema, como dentro de uma classe. Tente projetar os métodos privados dentro de uma classe de modo que cada método encapsule alguma informação ou funcionalidade e a oculte do restante da classe. Além disso, tente minimizar o número de lugares onde cada variável de instância é usada. Algumas variáveis podem precisar ser acessadas amplamente por toda a classe, mas outras podem ser necessárias em apenas alguns lugares; se você conseguir reduzir o número de lugares onde uma variável é usada, você eliminará dependências dentro da classe e reduzirá sua complexidade.

## 5.9 Indo longe demais

Ocultar informações só faz sentido quando a informação que está sendo ocultada não é necessária fora de seu módulo. Se a informação for necessária fora do módulo, então você não deve ocultá-la. Suponha que o desempenho de um módulo seja afetado por determinados parâmetros de configuração, e que diferentes usos do módulo exigirão ajustes distintos desses parâmetros. Nesse caso, é importante que os parâmetros sejam expostos na interface do módulo, para que possam ser ajustados adequadamente. Como um projetista de software, seu objetivo deve ser minimizar a quantidade de informações necessárias fora de um módulo; por exemplo, se um módulo puder ajustar sua configuração automaticamente, isso é melhor do que expor parâmetros de configuração. Porém, é importante reconhecer quais informações são necessárias fora de um módulo e certificar-se de que elas sejam expostas.

## 5.10 Conclusão

A ocultação de informações e os módulos profundos estão intimamente relacionados. Se um módulo oculta muitas informações, isso tende a aumentar a quantidade de funcionalidades oferecidas por ele e, ao mesmo tempo, reduzir a sua interface. Isso torna o módulo mais profundo. Por outro lado, se um módulo não oculta muitas informações, ou ele não tem muita funcionalidade, ou possui uma interface complexa; de qualquer maneira, o módulo é raso.

Ao decompor um sistema em módulos, tente não se deixar influenciar pela ordem em que as operações ocorrerão em tempo de execução; isso o levará pelo caminho da decomposição temporal, o que resultará em vazamento de informações e módulos rasos. Em vez disso, pense nos diferentes fragmentos de conhecimento necessários para realizar as tarefas da sua aplicação e projete cada módulo para encapsular um ou alguns desses conhecimentos. Isso produzirá um design limpo e simples com módulos profundos.

¹ David Parnas, “On the Criteria to be Used in Decomposing Systems into Modules,” *Communications of the ACM*, dezembro de 1972.

---

### Notas do Tradutor (N.T.)

- **Ocultação de informações (_Information hiding_):** Conceito clássico da engenharia de software cunhado justamente por David Parnas no artigo citado na nota de rodapé. Refere-se à prática de esconder os detalhes internos de implementação de um módulo.
- **Módulos profundos / rasos (_Deep_ / _shallow modules_):** Terminologia frequentemente usada em arquitetura de software (popularizada no livro *A Philosophy of Software Design* de John Ousterhout) para descrever módulos que oferecem muita funcionalidade através de uma interface simples (profundos) versus aqueles que oferecem pouca funcionalidade através de uma interface complexa (rasos).
