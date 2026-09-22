# Developers Not Writing Tests

> Tradução para português do artigo/test smell **"Developers Not Writing Tests"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/Developers%20Not%20Writing%20Tests.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Test smell do livro *xUnit Test Patterns: Refactoring Test Code* (2007), categoria "Project Smells".
> Tradução feita para fins de estudo.

*Nota do site original: o livro já foi publicado e o conteúdo deste capítulo provavelmente mudou substancialmente. Ver página 263 de xUnit Test Patterns para a informação mais atual.*

**Desenvolvedores não estão escrevendo testes automatizados.**

## Sintomas

Ouvimos dizer que nossos desenvolvedores não estão escrevendo testes. Ou talvez tenhamos observado **Production Bugs** (página X) e perguntado "Por que tantos bugs estão passando" e recebido como resposta "Porque não estamos escrevendo testes que cubram aquela parte do software."

## Impacto

Se o time não está escrevendo testes automatizados para cada pedaço de software "que poderia quebrar", ele está hipotecando seu futuro. O ritmo atual não será sustentável no longo prazo, porque o sistema estará em **test debt** (dívida de teste). Vai levar cada vez mais tempo para adicionar novas funcionalidades, e refatorar o código para melhorar o design será cheio de riscos (por isso, isso vai acontecer com cada vez menos frequência). Esse é o começo de uma descida pela proverbial "ladeira escorregadia" rumo ao desenvolvimento tradicional, paranoico e não ágil. Se é para lá que aspiramos ir, devemos manter o curso. Caso contrário, é hora de agir.

## Causas

### Causa: Falta de Tempo

Uma causa provável é que os desenvolvedores estão tendo dificuldade em escrever testes no tempo que lhes é dado para o desenvolvimento. Isso pode ser causado por um cronograma de desenvolvimento agressivo demais, ou por terem sido instruídos por seus supervisores ou líderes de time a "não perder tempo escrevendo testes". Também pode ser causado por eles não terem as habilidades para escrever testes de forma eficiente e não terem recebido tempo para subir a curva de aprendizado.

Se tempo é o que eles precisam, será necessário ajustar o cronograma do projeto para dar a eles esse tempo. Isso deveria ser apenas um ajuste temporário, enquanto desenvolvem as habilidades e a infraestrutura de automação de testes que os permitirá escrever os testes mais rapidamente. Em nossa experiência, uma vez que os desenvolvedores internalizaram o processo, eles conseguem escrever os testes e o código no mesmo tempo que costumava levar para escrever e depurar apenas o código. O tempo gasto escrevendo os testes é mais do que compensado pelo tempo não gasto no debugger.

### Causa: Código Difícil de Testar

Outra causa comum, especialmente com "software legado" (definido, para nossos propósitos, como qualquer software que não tenha uma suíte completa de testes automatizados) é que o design do software não é propício à automação de testes. Essa situação é descrita em mais detalhes em sua própria seção de smell, **Hard-to-Test Code** (página X).

### Causa: Estratégia Errada de Automação de Testes

A causa também pode ser um ambiente de teste ou estratégia de automação de testes que está levando a **Fragile Tests** (página X) ou **Obscure Tests** (página X) que demoram demais para escrever. Precisamos perguntar os "cinco porquês" [TPS] para encontrar as causas raiz. Então podemos endereçar essas causas e começar a colocar o navio de volta no rumo.

## Conselhos para Investigação (Trouble-Shooting Advice)

Smells de nível de projeto como *Developers Not Writing Tests* têm mais chance de serem detectados por um gerente de projeto, Scrum master ou líder de time do que por um desenvolvedor. Como gestores, podemos não saber como resolver o problema, mas nossa consciência e reconhecimento dele é o que importa. Isso nos permite perguntar ao time de desenvolvimento por que eles não estão escrevendo testes, em quais circunstâncias, e quanto tempo está levando para escrever testes quando eles o fazem. Então podemos encorajá-los e capacitá-los a criar formas de endereçar as causas raiz, de modo que passem a escrever todos os testes necessários.

Teremos que dar a eles nosso apoio total na execução de qualquer plano de melhoria que eles criarem. Esse apoio terá que incluir o tempo para aprender as habilidades necessárias e construir ou montar a infraestrutura de teste necessária. E não devemos esperar que as coisas se resolvam da noite para o dia. Podemos definir metas de melhoria de processo para cada iteração, como "redução de 20% no código não testado" ou "melhoria de 20% na cobertura de código". As metas devem ser razoáveis e de nível alto o suficiente para encorajar o comportamento certo, em vez de apenas fazer os números parecerem bons. (Uma meta de "205 testes a mais escritos" poderia ser alcançada sem aumentar a cobertura de testes em nada, simplesmente dividindo testes em pedaços menores ou clonando testes.)

---

*Página gerada originalmente em: Wed Feb 09 16:39:51 +1100 2011*
*Copyright © 2003-2008 Gerard Meszaros, todos os direitos reservados.*
