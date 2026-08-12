# Test Double (Dublê de Teste)

> Fonte original: Gerard Meszaros — xUnitPatterns.com
> URL: http://xunitpatterns.com/Test%20Double.html
> Capítulo de referência do livro *xUnit Test Patterns: Refactoring Test Code* (2007), p. 522.
> Também conhecido como: **Imposter** (Impostor)
> Copyright © 2003–2008 Gerard Meszaros. Tradução livre para PT-BR do conteúdo do site (que é uma versão preliminar do capítulo do livro).

**Pergunta que o padrão resolve:** Como verificar a lógica de forma independente quando o código do qual ela depende está inutilizável? Como evitar Testes Lentos (*Slow Tests*)?

**Solução em uma frase:** Substituímos um componente do qual o SUT (*System Under Test* — sistema sob teste) depende por um "equivalente específico para teste".

---

## Contexto / Motivação

Às vezes é simplesmente difícil testar o sistema sob teste (SUT) porque ele depende de outros componentes que não podem ser usados no ambiente de teste. Isso pode acontecer porque:

- eles não estão disponíveis;
- eles não retornam os resultados necessários para o teste; ou
- executá-los teria efeitos colaterais indesejáveis.

Em outros casos, nossa estratégia de teste exige que tenhamos mais **controle** ou **visibilidade** do comportamento interno do SUT.

Quando estamos escrevendo um teste em que **não podemos** (ou **escolhemos não**) usar um componente-dependência real (DOC — *Depended-On Component*), podemos substituí-lo por um **Test Double**. O Test Double não precisa se comportar exatamente como o DOC real; ele apenas precisa fornecer a **mesma API** que o real, de modo que o SUT pense que está falando com o componente verdadeiro.

---

## Como Funciona

Quando a indústria do cinema quer filmar algo potencialmente arriscado ou perigoso para o ator principal executar, ela contrata um "dublê" (*stunt double*) para tomar o lugar do ator na cena. O dublê é um indivíduo altamente treinado, capaz de atender aos requisitos específicos da cena. Ele pode não saber atuar, mas sabe como cair de grandes alturas, bater um carro, ou o que a cena exigir. O quão parecido o dublê precisa ser com o ator depende da natureza da cena — geralmente basta alguém com estatura vagamente semelhante.

Para fins de teste, podemos substituir o **DOC real** (não o SUT!) pelo nosso equivalente ao dublê: o **Test Double**. Durante a fase de *fixture setup* do nosso [Four-Phase Test](teste-de-quatro-fases), substituímos o DOC real pelo nosso Test Double. Dependendo do tipo de teste que estamos executando, podemos deixar o comportamento do Test Double *hard-coded* (fixo no código) ou configurá-lo durante a fase de setup. Quando o SUT interage com o Test Double, ele não perceberá que não está falando com o componente real — mas teremos alcançado nosso objetivo de tornar testes impossíveis em testes possíveis.

Independentemente de qual variação de Test Double escolhermos, precisamos ter em mente que **não é necessário implementar toda a interface do DOC**. Fornecemos apenas a funcionalidade necessária para o nosso teste específico. Podemos até construir Test Doubles diferentes para testes diferentes que envolvam o mesmo DOC.

---

## Quando Usar

Há várias circunstâncias em que podemos querer usar algum tipo de Test Double:

1. **Requisito não testado** (*Untested Requirement*) — quando não conseguimos verificar algo porque nem o SUT nem seus DOCs fornecem um **ponto de observação** (*observation point*) para a **saída indireta** (*indirect output*) do SUT que precisamos verificar.
2. **Código não testado** (*Untested Code*) — quando um DOC não fornece o **ponto de controle** (*control point*) que permitiria exercitar o SUT com as **entradas indiretas** (*indirect inputs*) necessárias.
3. **Testes lentos** (*Slow Tests*) — quando queremos rodar os testes mais rápido e, portanto, com mais frequência.

**Cuidados:** Cada um desses casos pode ser resolvido por um Test Double, mas é preciso cautela, pois estamos testando o SUT em uma **configuração diferente** da que será usada em produção. Por isso, devemos ter **pelo menos um teste** que verifique o funcionamento **sem** Test Double. Também é preciso cuidado para **não substituir justamente as partes do SUT que queremos verificar** — isso pode resultar em testes que testam o software errado. E o uso excessivo de Test Doubles pode levar a **Testes Frágeis** (*Fragile Tests*) por conta de *Overspecified Software* (software superespecificado).

---

## As Variações (os tipos de Test Double)

As variações são classificadas segundo **como/por que** usamos o Test Double.

### Variação: Test Stub

Usamos um **Test Stub** para substituir um componente real do qual o SUT depende, de modo que o teste tenha um **ponto de controle** para as **entradas indiretas** do SUT. Isso permite ao teste forçar o SUT por caminhos que ele não executaria de outra forma.

> Algumas pessoas usam o termo "Test Stub" para designar uma implementação temporária, usada apenas até que o objeto ou procedimento real fique disponível. Prefiro chamar isso de **Temporary Test Stub** (Stub Temporário) para evitar confusão.

### Variação: Test Spy

Podemos usar uma versão mais capaz do Test Stub — o **Test Spy** — como **ponto de observação** para as **saídas indiretas** do SUT. Assim como o Test Stub, o Test Spy pode precisar fornecer valores ao SUT em resposta a chamadas de método, mas o Test Spy também **captura** as saídas indiretas do SUT à medida que ele é exercitado e as **salva** para verificação posterior pelo teste. De certa forma, o Test Spy é "apenas um" Test Stub com capacidade de gravação. Embora seja usado com o mesmo propósito fundamental de um Mock Object, o estilo de teste escrito com um Test Spy se parece muito mais com um teste escrito com um Test Stub.

### Variação: Mock Object

Podemos usar um **Mock Object** como **ponto de observação** para verificar as **saídas indiretas** do SUT à medida que ele é exercitado. Normalmente o Mock Object também inclui a funcionalidade de um Test Stub (precisa retornar valores ao SUT caso ainda não tenha reprovado o teste), mas a **ênfase** está na **verificação** das saídas indiretas. Portanto, um Mock Object é muito mais do que "um Test Stub com asserções"; ele é usado de uma forma **fundamentalmente diferente**.

### Variação: Fake Object

Usamos um **Fake Object** para substituir a funcionalidade de um DOC real por razões **diferentes** da verificação de entradas e saídas indiretas do SUT. Tipicamente, ele implementa a **mesma funcionalidade** que o DOC real, mas de forma muito **mais simples**. Embora um Fake Object seja geralmente construído especificamente para teste, ele **não** é usado como ponto de controle nem como ponto de observação pelo teste.

A razão mais comum para usar um Fake Object é que o componente-dependência real ainda não está disponível, é lento demais, ou não pode ser usado no ambiente de teste por causa de efeitos colaterais nocivos. (O *sidebar* "Faster Tests Without Shared Fixtures" descreve como encapsular todo o acesso a banco de dados atrás de uma interface de camada de persistência e substituir o banco por *hash tables* em memória, tornando os testes ~50× mais rápidos.)

### Variação: Dummy Object

Algumas assinaturas de método do SUT podem exigir objetos como parâmetros. Se **nem o teste nem o SUT** se importam com esses objetos, podemos passar um **Dummy Object** — que pode ser tão simples quanto uma referência nula (`null`), uma instância da classe `Object`, ou uma instância de um Pseudo Object. Nesse sentido, um Dummy Object não é realmente um Test Double *per se*, mas sim uma alternativa aos padrões de valor Literal Value, Derived Value e Generated Value.

### Variação: Procedural Test Stub

Um Test Double implementado em uma **linguagem procedural** costuma ser chamado apenas de "Test Stub", mas prefiro chamá-lo de **Procedural Test Stub** para distingui-lo da variação moderna Test Stub. Tipicamente o usamos para permitir testar/depurar enquanto esperamos outro código ficar disponível. É raro que sejam "trocados" (*swapped in*) em tempo de execução, mas às vezes tornamos o código condicional a uma flag de "Debugging" — uma forma de *Test Logic in Production*.

---

## Notas de Implementação

Há várias considerações ao construir o Test Double:

- O Test Double deve ser **específico para um único teste** ou **reutilizável** em vários testes?
- O Test Double deve existir **em código** ou ser **gerado dinamicamente** (*on-the-fly*)?
- **Como** dizemos ao SUT para usar o Test Double? (instalação)

Como as técnicas de construção são praticamente independentes do comportamento (aplicam-se tanto a Test Stubs quanto a Mock Objects), Meszaros separa as descrições em padrões distintos (Hard-Coded Test Double e Configurable Test Double).

### Variação: Unconfigurable Test Doubles (Não Configuráveis)

Nem Dummy Objects nem Fake Objects precisam ser configurados. **Dummies** nunca devem ser usados pelo receptor, então não precisam de implementação. **Fake Objects**, por outro lado, precisam de uma implementação "real", porém muito mais simples/leve que o objeto que substituem. Assim, nem o teste nem o *test automater* precisam configurar respostas "enlatadas" ou expectativas — apenas instalamos o Test Double e deixamos o SUT usá-lo como se fosse real.

### Variação: Hard-Coded Test Double

Quando planejamos usar um Test Double específico em um único teste, geralmente é mais simples deixá-lo *hard-coded* para retornar valores específicos (para Test Stubs) ou esperar chamadas de método específicas (para Mock Objects). São construídos à mão pelo *test automater* e vêm em várias formas:

- **Self Shunt** — a própria Testcase Class atua como o Test Double.
- **Anonymous Inner Test Double** — recursos da linguagem criam o Test Double dentro do próprio Test Method.
- **Test Double Class** — implementado como uma classe separada.

### Variação: Configurable Test Double

Quando queremos usar a mesma implementação de Test Double em muitos testes, tipicamente usamos um **Configurable Test Double**. Também podem ser construídos à mão, mas muitos membros da família xUnit têm *toolkits* reutilizáveis para gerar test doubles.

### Instalando o Test Double

Antes de exercitar o SUT, precisamos dizer a ele para usar o Test Double em vez do objeto que ele substitui. Podemos usar qualquer um dos padrões de **dependência substituível** (*substitutable dependency*) para instalá-lo durante a fase de *fixture setup* do Four-Phase Test. Configurable Test Doubles precisam ser configurados **antes** de exercitar o SUT — tipicamente antes de instalá-los.

---

## Exemplo

Como há uma grande variedade de razões para usar as variações de Test Double, é difícil dar um único exemplo que caracterize a motivação de cada estilo. Meszaros remete aos exemplos de cada um dos padrões mais detalhados (Test Stub, Test Spy, Mock Object, Fake Object).

---

## Vocabulário-chave

- **SUT** (*System Under Test*) — o sistema/código que está sendo testado.
- **DOC** (*Depended-On Component*) — componente do qual o SUT depende (é o que se substitui).
- **Indirect input** (entrada indireta) — valores que o SUT recebe de um DOC (controlados por Stub/Mock).
- **Indirect output** (saída indireta) — chamadas/efeitos que o SUT dispara sobre um DOC (observados por Spy/Mock).
- **Control point** (ponto de controle) — mecanismo para fornecer entradas indiretas ao SUT.
- **Observation point** (ponto de observação) — mecanismo para observar as saídas indiretas do SUT.

---

## Padrões Relacionados

- Test Stub, Test Spy, Mock Object, Fake Object, Dummy Object (as cinco variações principais)
- Hard-Coded Test Double, Configurable Test Double (como construir)
- Four-Phase Test, Substitutable Dependency, Test-Specific Subclass
- Fragile Test, Overspecified Software, Slow Tests (armadilhas relacionadas)
