# Hard-to-Test Code

> Tradução para português do test smell **"Hard-to-Test Code"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/Hard%20to%20Test%20Code.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Test smell do livro *xUnit Test Patterns: Refactoring Test Code* (2007), categoria "Test Smells" (subcategoria de code smell, sob "Test Smells" — irmão de Obscure Test, Conditional Test Logic, Test Code Duplication e Test Logic in Production).
> Tradução feita para fins de estudo.

*Nota do site original: o livro já foi publicado e o conteúdo deste capítulo provavelmente mudou substancialmente. Ver página 209 de xUnit Test Patterns para a informação mais atual.*

**Código é difícil de testar.**

Testes automatizados são uma ferramenta poderosa que nos ajuda a desenvolver software rapidamente mesmo depois de termos uma grande base de código para manter, mas isso só traz esses benefícios se a maior parte do nosso código tiver **Fully Automated Test** (ver Goals of Test Automation, página X). O esforço de escrever esses testes é adicional ao esforço de escrever o código de produção que eles verificam, então gostaríamos de facilitar a escrita dos testes automatizados[^1].

*Hard-to-Test Code* (código difícil de testar) é um fator que dificulta escrever testes automatizados completos e corretos de forma economicamente eficiente.

## Sintomas

Alguns tipos de código são difíceis de testar. Componentes de GUI, código multi-thread e código de teste vêm imediatamente à mente como *Hard-to-Test Code*. Pode ser difícil acessar o código a ser testado porque ele não é visível para um teste. Pode ser difícil fazer um teste compilar porque o código está muito acoplado a outras classes, ou pode ser difícil criar uma instância do objeto porque os construtores não existem, são privados, ou recebem parâmetros demais.

## Impacto

Sempre que temos *Hard-to-Test Code*, temos código cuja qualidade não conseguimos verificar facilmente de forma automatizada. Embora a avaliação manual de qualidade muitas vezes seja possível, ela não escala bem, porque o esforço de fazê-la depois de cada mudança de código geralmente significa que ela não é feita. Também não é muito repetível sem um custo grande de documentação de teste.

## Padrões de Solução

Uma solução melhor é tornar o código mais propenso a ser testado. Esse é um tópico grande o suficiente para merecer um capítulo inteiro próprio, mas vou cobrir alguns destaques aqui.

## Causas

Há uma série de razões para *Hard-to-Test Code*, mas as causas mais comuns são:

### Causa: Código Altamente Acoplado

**Também conhecido como:** Hard-Coded Dependency (Dependência Fixa no Código)

#### Sintomas

Uma classe não pode ser testada sem também testar várias outras classes.

#### Impacto

Código que está altamente acoplado a outro código é muito difícil de testar unitariamente, porque não executa isoladamente.

#### Causa Raiz

*Highly Coupled Code* (código altamente acoplado) pode ser causado por muitos fatores, incluindo design ruim, falta de experiência em design orientado a objetos, ou falta de uma estrutura de incentivo que encoraje o desacoplamento.

#### Possível Solução

A chave para testar código excessivamente acoplado é quebrar o acoplamento. Isso acontece naturalmente ao fazer **test-driven development**.

Uma técnica que costumamos usar para desacoplar código com o propósito de testar é o **Test Double** (página X) ou, mais especificamente, **Test Stubs** (página X) ou **Mock Objects** (página X). Esse tópico é coberto em muito mais detalhe no capítulo narrativo **Using Test Doubles**.

É mais desafiador quando estamos retrofitando testes em código já existente, especialmente quando lidamos com uma base de código legada. Esse é um tópico grande o suficiente para que Michael Feathers tenha escrito um livro inteiro sobre técnicas para fazer isso. Chama-se "Working Effectively with Legacy Code" [WEwLC].

### Causa: Código Assíncrono

#### Sintomas

Uma classe não pode ser testada via chamadas diretas de método. O teste precisa iniciar um executável (como uma thread, processo ou aplicação) e esperar até que ele termine de inicializar antes de interagir com ele.

#### Impacto

Código que tem uma interface assíncrona é difícil de testar porque os testes precisam coordenar sua execução com a do **system under test (SUT)**. Isso pode adicionar muita complexidade aos testes e também fazer com que demorem muito, muito mais para rodar. Isso é uma questão importante para testes unitários, que precisam rodar muito rapidamente para garantir que os desenvolvedores os executem com frequência.

#### Causa Raiz

Essa é uma forma específica de acoplamento, na qual o código que implementa o algoritmo que queremos testar está altamente acoplado ao objeto ativo no qual ele normalmente executa.

#### Possível Solução

A chave para testar código assíncrono é separar a lógica do mecanismo de acesso assíncrono. O padrão de design-for-testability **Humble Object** (página X) (incluindo **Humble Dialog** e **Humble Executable**) é um bom exemplo de forma de reestruturar código que seria assíncrono para que possa ser testado de maneira síncrona.

### Causa: Código de Teste Não Testável

#### Sintomas

O corpo de um **Test Method** (página X) é obscuro o suficiente (**Obscure Test**, página X) ou contém **Conditional Test Logic** (página X) suficiente para nos fazer questionar se o teste está correto.

#### Impacto

Qualquer **Conditional Test Logic** dentro de um **Test Method** tem probabilidade maior de resultar em **Buggy Tests** (página X) e provavelmente resultará em **High Test Maintenance Cost** (página X). Código demais no corpo do teste pode torná-lo difícil de entender e difícil de acertar.

#### Causa Raiz

O código dentro do corpo do **Test Method** é inerentemente difícil de testar usando um **Self-Checking Test** (ver Goals of Test Automation). Teríamos que substituir o **SUT** por um **Test Double** que injeta o erro que estamos testando, e então rodar o test method dentro de outro método **Expected Exception Test** (ver Test Method) — muito trabalho para se dar ao luxo, exceto nas circunstâncias mais incomuns.

#### Possível Solução

Podemos remover a necessidade de testar o corpo de um **Test Method** tornando-o extremamente simples e removendo qualquer **Conditional Test Logic** dele para **Test Utility Methods** (página X), para os quais podemos facilmente escrever **Self-Checking Tests**.

---

*Página gerada originalmente em: Wed Feb 09 16:39:51 +1100 2011*
*Copyright © 2003-2008 Gerard Meszaros, todos os direitos reservados.*

[^1]: Nota de rodapé do original: "Também gostaríamos de recuperar esse custo reduzindo esforço em outro lugar. A melhor forma de conseguir isso é evitar *Frequent Debugging* (página X) escrevendo os testes primeiro e alcançando *Defect Localization* (ver Goals of Test Automation)."
