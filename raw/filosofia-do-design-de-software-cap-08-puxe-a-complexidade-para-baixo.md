# Capítulo 8 — Puxe a Complexidade para Baixo

Este capítulo apresenta outra maneira de pensar sobre como criar classes mais profundas. Suponha que você esteja desenvolvendo um novo módulo e descubra um elemento de complexidade inevitável. O que é melhor: você deve deixar que os usuários do módulo lidem com a complexidade, ou você mesmo deve tratá-la internamente dentro do módulo? Se a complexidade estiver relacionada à funcionalidade oferecida pelo módulo, então a segunda resposta geralmente é a correta. A maioria dos módulos tem mais usuários do que desenvolvedores, então é melhor que os desenvolvedores sofram do que os usuários. Como desenvolvedor de um módulo, você deve se esforçar para facilitar ao máximo a vida dos usuários do seu módulo, mesmo que isso signifique trabalho extra para você. Outra forma de expressar essa ideia é que **é mais importante para um módulo ter uma interface simples do que uma implementação simples.**

Como desenvolvedor, é tentador agir de maneira oposta: resolver os problemas fáceis e empurrar os difíceis para outra pessoa. Se surgir uma condição com a qual você não tem certeza de como lidar, a coisa mais fácil a fazer é lançar uma exceção e deixar que o chamador resolva. Se você não tem certeza de qual política implementar, pode definir alguns parâmetros de configuração para controlá-la e deixar para o administrador de sistemas descobrir os melhores valores para eles.

Abordagens como essas facilitarão a sua vida a curto prazo, mas elas amplificam a complexidade, fazendo com que várias pessoas tenham que lidar com um problema, em vez de apenas uma. Por exemplo, se uma classe lança uma exceção, todos os chamadores dessa classe terão que lidar com ela. Se uma classe exporta parâmetros de configuração, todo administrador de sistemas em cada instalação terá que aprender a configurá-los.

---

**Notas do Tradutor (N.T.):**

- **"Puxe a Complexidade para Baixo" (Pull Complexity Downwards):** Refere-se ao conceito de arquitetura de software de "absorver" ou "empurrar" a complexidade para as camadas mais profundas (internas e privadas) do código, mantendo a superfície (a interface pública) o mais simples possível para quem a consome.
- **"Chamador" (Caller):** Termo técnico padrão no Brasil para designar o código, método ou objeto que invoca (chama) uma determinada função ou classe.

## 8.1 Exemplo: classe de texto do editor

Considere a classe que gerencia o texto de um arquivo para um editor de texto com interface gráfica (GUI), a qual foi discutida nos Capítulos 6 e 7. A classe fornece métodos para ler um arquivo do disco para a memória, consultar e modificar a cópia do arquivo em memória e gravar a versão modificada de volta no disco. Quando os alunos precisaram implementar essa classe, muitos deles escolheram uma interface orientada a linhas, com métodos para ler, inserir e excluir linhas inteiras de texto. Isso resultou em uma implementação simples para a classe, mas criou complexidade para o software de nível superior. No nível da interface de usuário, as operações raramente envolvem linhas inteiras. Por exemplo, o pressionamento de teclas faz com que caracteres individuais sejam inseridos dentro de uma linha existente; copiar ou excluir a seleção pode modificar partes de várias linhas diferentes. Com a interface de texto orientada a linhas, o software de nível superior precisava dividir e unir linhas para conseguir implementar a interface de usuário.

Uma interface orientada a caracteres, como a descrita na Seção 6.3, puxa a complexidade para as camadas inferiores. O software da interface de usuário agora pode inserir e excluir intervalos arbitrários de texto sem precisar dividir e mesclar linhas, tornando-se, assim, mais simples. A implementação da classe de texto provavelmente se torna mais complexa: se ela representar o texto internamente como uma coleção de linhas, terá que dividir e mesclar essas linhas para implementar as operações orientadas a caracteres. Essa abordagem é melhor porque encapsula a complexidade de divisão e mesclagem dentro da própria classe de texto, o que reduz a complexidade geral do sistema.

## 8.2 Exemplo: parâmetros de configuração

Os parâmetros de configuração são um exemplo de mover a complexidade para cima, em vez de para baixo. Em vez de determinar um comportamento específico internamente, uma classe pode exportar alguns parâmetros que controlam seu comportamento, como o tamanho de um cache ou o número de vezes para tentar novamente uma requisição antes de desistir. Os usuários da classe devem, então, especificar os valores adequados para os parâmetros. Os parâmetros de configuração se tornaram muito populares nos sistemas atuais; alguns sistemas possuem centenas deles.

Os defensores argumentam que os parâmetros de configuração são bons porque permitem aos usuários ajustar o sistema para seus requisitos e cargas de trabalho específicos. Em algumas situações, é difícil para o código de infraestrutura de baixo nível saber a melhor política a ser aplicada, enquanto os usuários estão muito mais familiarizados com seus domínios. Por exemplo, um usuário pode saber que algumas requisições são mais sensíveis ao tempo do que outras, então faz sentido que ele especifique uma prioridade maior para essas requisições. Em situações como essa, os parâmetros de configuração podem resultar em um melhor desempenho em uma ampla variedade de domínios.

No entanto, os parâmetros de configuração também fornecem uma desculpa fácil para evitar lidar com problemas importantes e repassá-los para outra pessoa. Em muitos casos, é difícil ou impossível para os usuários ou administradores determinarem os valores corretos para os parâmetros. Em outros casos, os valores corretos poderiam ter sido determinados automaticamente com um pouco de trabalho extra na implementação do sistema. Considere um protocolo de rede que precisa lidar com pacotes perdidos. Se ele envia uma requisição, mas não recebe uma resposta dentro de um determinado período, ele reenvia a requisição. Uma maneira de determinar o intervalo de retentativa é introduzir um parâmetro de configuração. No entanto, o protocolo de transporte poderia calcular um valor razoável por conta própria, medindo o tempo de resposta das requisições bem-sucedidas e, em seguida, usando um múltiplo disso para o intervalo de retentativa. Essa abordagem puxa a complexidade para baixo e poupa os usuários de terem que descobrir o intervalo de retentativa correto. Ela tem a vantagem adicional de calcular esse intervalo dinamicamente, de modo que ele se ajustará automaticamente se as condições de operação mudarem. Em contrapartida, os parâmetros de configuração podem facilmente ficar desatualizados.

Portanto, você deve evitar parâmetros de configuração o máximo possível. Antes de exportar um parâmetro de configuração, pergunte a si mesmo: "os usuários (ou módulos de nível superior) serão capazes de determinar um valor melhor do que nós podemos determinar aqui?". Quando você realmente criar parâmetros de configuração, veja se pode fornecer valores padrão razoáveis, para que os usuários só precisem fornecer valores em condições excepcionais. Idealmente, cada módulo deveria resolver um problema por completo; os parâmetros de configuração resultam em uma solução incompleta, o que aumenta a complexidade do sistema.

## 8.3 Indo longe demais

Tenha cautela ao puxar a complexidade para baixo; essa é uma ideia que pode facilmente passar do ponto. Uma abordagem extrema seria puxar toda a funcionalidade da aplicação inteira para uma única classe, o que claramente não faz sentido. Puxar a complexidade para baixo faz mais sentido se:

- (a) a complexidade que está sendo movida estiver intimamente relacionada à funcionalidade existente da classe;
- (b) puxar a complexidade para baixo resultar em simplificações em outras partes da aplicação;
- (c) puxar a complexidade para baixo simplificar a interface da classe.

Lembre-se de que o objetivo é minimizar a complexidade geral do sistema.

O Capítulo 6 descreveu como alguns alunos definiram métodos na classe de texto que refletiam a interface de usuário, a exemplo de um método que implementa a funcionalidade da tecla de retrocesso (backspace). Pode parecer que isso é bom, já que puxa a complexidade para as camadas inferiores. No entanto, adicionar conhecimento da interface de usuário à classe de texto não simplifica muito o código de alto nível, e o conhecimento da interface de usuário não se relaciona com as funções centrais da classe de texto. Neste caso, puxar a complexidade para baixo resultou apenas em vazamento de informação.

> **Nota do Tradutor (N.T.):** O termo original "information leakage" (vazamento de informação) é usado aqui no contexto de engenharia de software para descrever a quebra de encapsulamento — quando detalhes de implementação de um módulo "vazam" e afetam outros lugares do código —, e não no sentido de falha de segurança de dados.

## 8.4 Conclusão

Ao desenvolver um módulo, procure oportunidades para assumir um pouco de sofrimento extra com o objetivo de reduzir o sofrimento dos seus usuários.
