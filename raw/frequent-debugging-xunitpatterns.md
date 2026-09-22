# Frequent Debugging

> Tradução para português do test smell **"Frequent Debugging"** (também conhecido como "Manual Debugging"), do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/Frequent%20Debugging.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Test smell do livro *xUnit Test Patterns: Refactoring Test Code* (2007), categoria "Test Smells" → subcategoria "Behavior Smells" (irmão de Assertion Roulette, Erratic Test, Manual Intervention e Slow Tests).
> Tradução feita para fins de estudo.

*Nota do site original: o livro já foi publicado e o conteúdo deste capítulo provavelmente mudou substancialmente. Ver página 248 de xUnit Test Patterns para a informação mais atual.*

**Também conhecido como:** Manual Debugging (Depuração Manual)

**A depuração manual é necessária para determinar a causa da maioria das falhas de teste.**

## Sintomas

Uma execução de testes resulta em uma **test failure** (falha de teste) ou um **test error** (erro de teste). A saída do **Test Runner** (página X) é insuficiente para determinarmos o problema, então precisamos usar um debugger interativo (ou instruções de print espalhadas pelo código) para descobrir onde as coisas estão dando errado.

Se esse for um caso isolado, não precisamos nos preocupar com ele, mas se a maioria das falhas de teste exige esse tipo de depuração, então temos um caso de *Frequent Debugging*.

## Causas

*Frequent Debugging* é causado pela falta de **Defect Localization** (ver Goals of Test Automation, página X) em nossa suíte de testes automatizados. Os testes que falham deveriam nos dizer o que deu errado, seja através de suas mensagens de falha individuais (ver **Assertion Message**, página X) ou através do padrão de falhas dos testes. Se não o fazem:

- Podemos estar sem os **unit tests** detalhados que apontariam um erro de lógica dentro de uma classe individual.
- Podemos estar sem os **component tests** para um cluster de classes (ou seja, um **component**) que apontariam um erro de integração entre as classes individuais. Isso pode acontecer quando usamos **Mock Objects** (página X) extensivamente para substituir objetos dependentes, mas os unit tests dos objetos dependentes não correspondem ao modo como os Mock Objects estão programados para se comportar.

Esse problema costuma aparecer com mais frequência quando os testes de nível mais alto (funcionais ou de componente) foram escritos, mas nem todos os unit tests dos métodos individuais. (Algumas pessoas chamariam essa abordagem de **test-first development**, para distingui-la de **test-driven development**, onde cada pequeno pedaço de código é trazido à existência por um unit test que falha.)

*Frequent Debugging* também pode ser causado por **Infrequently Run Tests** (ver Production Bugs, página X). Se rodarmos nossos testes a cada pequena mudança feita no software, conseguimos lembrar o que mudamos desde a última vez que os testes rodaram. Isso significa que, quando um teste falha, não precisamos gastar muito tempo investigando o software para descobrir onde está o bug — sabemos onde ele está porque lembramos de tê-lo colocado ali!

## Impacto

A depuração manual é um processo lento e tedioso. É fácil deixar passar indícios sutis do problema e gastar muitas horas rastreando um único erro de lógica. Isso reduz a produtividade e torna os cronogramas de desenvolvimento muito menos previsíveis, porque uma única sessão de depuração manual pode estender o tempo necessário para desenvolver o software em meio dia ou mais.

## Padrões de Solução

Se estamos sem os **customer tests** para uma funcionalidade e o teste manual do usuário revelou um problema não exposto por nenhum teste automatizado, provavelmente temos um caso de **Untested Requirement** (ver Production Bugs). Podemos nos perguntar que tipo de teste automatizado teria evitado a sessão de depuração manual. Melhor ainda, uma vez identificado o problema, podemos escrever o teste que o expõe. Aí podemos usar o teste que falha para fazer **test-driven bug fixing**! Se suspeitamos que esse seja um problema generalizado, podemos criar uma tarefa de desenvolvimento para identificar e escrever quaisquer testes adicionais necessários para preencher a lacuna que acabamos de expor.

Fazer verdadeiro **test-driven development** é a melhor forma de evitar as circunstâncias que levam a *Frequent Debugging*. Devemos começar o mais próximo possível da "pele" da aplicação e fazer **storytest-driven development**, escrevendo unit tests para classes individuais assim como component tests para as coleções de classes relacionadas, para garantir que tenhamos boa **Defect Localization**.

---

*Página gerada originalmente em: Wed Feb 09 16:39:50 +1100 2011*
*Copyright © 2003-2008 Gerard Meszaros, todos os direitos reservados.*
