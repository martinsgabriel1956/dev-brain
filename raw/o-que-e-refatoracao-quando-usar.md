# O Que É Refatoração (e Quando Usar) — Bernardo Lobato

Você já separou um tempo para refatorar um código, sabe muito bem como fazer isso e qual deve ser de fato o resultado desse trabalho. Já comentou um bloco de código gigante em vez de deletar, só por garantia. Então esse vídeo é para você.

No vídeo de hoje a gente vai pôr um pezinho no mundo da refatoração: vamos entender o que é, quando utilizar, quando não utilizar, e nesse caminho fazer algumas reflexões. Já duplicou aquele método que é quase 100% igual ao requisito que você vai implementar, só para não correr o risco de quebrar o original? O vídeo já vai começar.

Olá, devs, eu sou Bernardo Lobato, e hoje vamos pedir licença para entrar nesse mundo da refatoração. Planejei uma série sobre esse assunto aqui no canal, caso a comunidade tenha interesse e o YouTube fizer uma boa entrega. E se você acha que sabe tudo sobre esse assunto, acompanha até o final — pode ser que eu tenha uma ou duas surpresinhas para você.

## A historinha do consultor

Você sabe primeiramente o que é refatoração? Antes de qualquer definição, vamos de historinha.

Imagine que você, como um consultor ou desenvolvedor sênior, chega num projeto agora e é o responsável por dar andamento às demandas do dia a dia daquele projeto. Dentro do seu estudo, vai observando que cada funcionalidade leva cada vez mais tempo para ser entregue, e se embrenha no código para tentar entender por quê.

Percebe que, apesar de ter uma estrutura de classes bem definida e uma arquitetura inicial bem implementada, essa estrutura está confusa: muitas classes sendo sobrescritas, muita biblioteca compartilhada sem muita necessidade, várias subclasses com código duplicado, fazendo com que alterações em determinados componentes precisem ser feitas em diversos arquivos diferentes.

Você, como um bom profissional, alerta a liderança que o ideal seria estudar um pouco mais o código e reescrever algumas classes desse sistema, pois o design está sendo degradado conforme novas funcionalidades vão sendo adicionadas. Seu gerente dá pouca importância e diz que isso vai ser colocado como débito técnico, que será feito em algum momento no futuro — afinal, o código funciona bem, e essas alterações seriam só para que o código tivesse um melhor aspecto.

Será mesmo essa história? Lhe parece familiar? De acordo com o que foi apresentado, é justificável dizer que o gerente está errado e que o consultor estava certo? O que o consultor estava sugerindo era uma refatoração em partes do código para que novas alterações pudessem ser feitas com mais eficiência. Mas a gente já chega lá.

## Definição

Refatoração é o processo de modificar um sistema de software de modo que não altere o comportamento externo do código, embora possa alterar — algumas vezes drasticamente — sua estrutura interna. Em suma: você está melhorando o design do código depois que ele já foi escrito.

Dois grandes pilares dessa definição:

1. **Não se altera o comportamento externo do código.** A refatoração não deve, em nenhuma hipótese, ser feita enquanto se adiciona funcionalidades novas no sistema ou se altera uma funcionalidade existente.
2. **Pode e deve alterar sua estrutura interna.** Isso pode ter grandes implicações positivas, como a melhoria contínua do design e da arquitetura do projeto, sem que essa vá se degradando no decorrer do andamento das entregas.

Uma primeira reflexão: um sistema pode começar com design e arquitetura bem feitos e bem implementados, com muita boa vontade. Porém, com o aumento das entregas e a diminuição de cronograma, é muito comum que as entregas passem a atropelar, devagarinho, aquele design bem pensado, diminuindo gradativamente a qualidade do código como um todo.

Disso, dá para inferir que um programa com design ruim é difícil de ser entendido e alterado por humanos. Um compilador não se importa se o código está bonito ou feio, mas o humano sim. Um sistema assim é difícil de manter, difícil de alterar, pois é difícil identificar todas as partes que precisam de alteração — portanto, há uma boa chance de introduzir bugs.

## Exemplo do dia a dia: a God Class

Na Sprint 1, o projeto é um brinco. Você tem uma classe chamada `OrderProcessor` que faz exatamente o que o nome diz: recebe o pedido, cobra no gateway e salva no banco. O design está limpo, coeso e fácil de testar.

Aí o projeto cresce. Na Sprint 5, o negócio precisa de frete internacional urgente, devido a um requisito novo. O desenvolvedor, pressionado pelo prazo, pensa: "é só um if rapidinho aqui dentro, não vai machucar ninguém" — e coloca a regra ali mesmo.

Na Sprint 20, depois de três alterações de escopo, duas trocas de equipe, quatro hotfixes na sexta-feira à noite, aquela classe virou monstro — a chamada **God Class**: ela valida cupom, calcula imposto, checa fraude, dispara evento pro Kafka. O design original foi soterrado por esses puxadinhos.

O desenvolvedor da Sprint 20 não é necessariamente ruim — ele só está tentando sobreviver aos prazos, seguindo o padrão que já estava ali. Mas o resultado é um código que agora todo mundo tem medo de tocar. É aí que a refatoração oportuna deveria ter agido no decorrer do processo de desenvolvimento.

## Como não piorar o código ao refatorar: testes automatizados

Quando o código já está nessa situação, como garantir que a refatoração não vai ser uma piora — algo que, além de não melhorar o código, acaba quebrando alguma funcionalidade que já funcionava perfeitamente?

De longe, a melhor maneira é ter uma boa cobertura de testes automatizados: testes unitários, testes de integração e outros. O importante é que esses testes sejam próximos do desenvolvedor no dia a dia e baratos de rodar. Um teste end-to-end, por exemplo, pode ser mais custoso e demorado — portanto pode não ser a melhor opção na hora de refatorar.

Na pirâmide de testes, os testes na base são os mais simples e rápidos de rodar, por isso devem existir em abundância. No caso da refatoração, o foco é nessa base da pirâmide.

Se o código não tem testes, a melhor maneira é você mesmo criá-los — não precisa criar para o projeto inteiro, mas pelo menos para a funcionalidade específica que está sendo refatorada. Uma vez mapeado o comportamento real daquela funcionalidade, a maturidade da refatoração vai ser muito maior.

## O processo de refatoração deve ser em passos pequenos

Sem discussões: o processo de refatoração deve ser simples e rápido. A refatoração deve ser feita em passos pequenos.

Uma armadilha comum é refatorar um módulo por completo de uma vez só. Nesse caso, a chance de se ter um código incompleto — que não entrega nem refatoração nem nova funcionalidade — é grande. Cria-se uma branch com código sendo refatorado, e na main o projeto vai continuando normalmente. Imagine a loucura do merge dessa refatoração, caso ela algum dia termine.

A refatoração está ligada diretamente à aplicação de pequenos passos que preservam o comportamento atual do sistema. Durante a refatoração, o estado do sistema não pode ficar inconsistente. O processo deve permitir parar a qualquer momento, ou pouquíssimo tempo depois, sem nenhum prejuízo para o comportamento externo do sistema.

Se a refatoração está deixando o sistema quebrado — mesmo que temporariamente — por muitas horas ou dias, cuidado: essa pode ser uma red flag gigante no processo.

### E se eu encontrar um bug durante a refatoração?

No livro *Refatorando: Aperfeiçoando o Design de Códigos Existentes*, Martin Fowler defende que sim: no caso de um bug conhecido e provavelmente já priorizado, você deixa ele lá. A ideia é reproduzir o comportamento externo exato que o sistema tinha no início do processo de refatoração.

Já no caso de um bug ainda não conhecido, encontrado durante a atividade de refatoração, pode ser coerente corrigi-lo nesse momento — mas é preciso ter certeza absoluta de que é um bug real.

## Os dois chapéus de Kent Beck

A refatoração não deve ser feita enquanto se adiciona funcionalidades novas no sistema. Kent Beck criou a metáfora dos **dois chapéus**: ao desenvolver software, o tempo se divide em duas atividades distintas — adicionar funcionalidades e refatorar.

- Quando se está adicionando funcionalidades, não se deve refatorar. Avalia-se o progresso acrescentando testes e fazendo-os passar.
- Quando se está refatorando, não se deve adicionar funcionalidades. O objetivo é somente a reestruturação do código, preferencialmente sem alterar nenhum dos resultados esperados nos testes já existentes.

Essa troca de chapéus pode durar algumas horas ou mesmo alguns minutos. O importante é ter consciência de qual chapéu está sendo usado naquele momento, e da diferença que isso faz.

## Refatoração não é bala de prata

Como tudo que envolve arquitetura, design de software e programação, refatoração não é bala de prata. No geral, é uma excelente ferramenta para manter um bom controle sobre o código.

### Quando refatorar é uma boa ideia

1. **Melhorar o design do software.** Quando novos comportamentos são acrescentados sem o devido cuidado, o design tende a cair em decadência, prejudicando gradativamente o estado interno do código. Com a refatoração constante, essa degradação diminui ativamente.
2. **Aumentar a manutenibilidade.** Código refatorado é mais legível e mais inteligível para o desenvolvedor que vai pegá-lo no futuro — muitas vezes você mesmo.
3. **Ajudar a encontrar problemas.** Ao se embrenhar no código para entender o que ele faz, você acaba entendendo melhor sua estrutura interna e regras de negócio, o que ajuda a encontrar comportamentos inesperados ou bugs.
4. **Entregar o software mais rapidamente.** Parece contraintuitivo — o tempo gasto refatorando não aumentaria o tempo de entrega? Segundo os gráficos do livro de Fowler, quando se coloca esforço num bom design interno, aumenta-se a qualidade do código e, por consequência, diminui-se o tempo que novas features levam para ser acrescentadas. Adicionar funcionalidade a um código com bom design e arquitetura bem definida é sempre mais rápido.

### Quando refatorar

O melhor momento é durante a própria atividade de desenvolvimento, conectado ao fluxo de trabalho. Dois pontos importantes:

- **Imediatamente antes de adicionar uma nova funcionalidade**, quando já existe um comportamento muito próximo ao que deve ser adicionado. A alternativa ruim é simplesmente duplicar o método ou o código e substituir os pontos divergentes — se esse comportamento geral precisar ser alterado num requisito futuro, será necessário alterar em dois (ou mais) lugares, obrigando a procurar todos os pontos que compartilham a funcionalidade.
- **Quando o código está difícil de entender** (lógica confusa, código duplicado), mas com bom senso: não se deve gastar tempo excessivo nessa refatoração. Se exigir muito esforço — mais horas ou dias — o ideal é mapeá-la como débito técnico, para correção num momento mais oportuno.

Esse tipo de refatoração — que se aproveita de atividades que já seriam feitas de qualquer jeito no código, encaixando-se automaticamente no processo — é chamado de **refatoração oportunista**. Existem também as **refatorações planejadas**, envolvendo revisões de código e outros processos mais raros.

### Quando NÃO refatorar

- Quando um algoritmo complicado (muitas vezes proprietário) funciona desde a primeira versão do sistema, e apesar de feio e confuso, não é necessário alterá-lo naquele momento. A refatoração só traz vantagem se for preciso entender internamente como aquele código funciona.
- Quando é mais fácil reescrever o trecho de código completamente do que refatorá-lo. Essa decisão é arriscada, porque para perceber que o código é difícil de refatorar é preciso se debruçar sobre ele por algum tempo — só aí dá para compreender de fato a dificuldade da alteração.

## Gestão e o hábito da refatoração

Um ponto recorrente: como desenvolvedor, devo informar à gestão que uma parte do tempo será usada para refatoração? Se a gestão não tem o pé no técnico, esse tipo de atividade pode ser desencorajado.

Nesses casos, a solução é simplesmente não informar — vá lá e faça, incorporando a refatoração no trabalho normal de adicionar funcionalidades, do mesmo jeito que já se adiciona tempo na estimativa para criar testes unitários.

Se a gestão é mais técnica, a refatoração pode ser discutida mais abertamente — inclusive o ponto de quando uma refatoração deve virar débito técnico e ser priorizada, em vez de incorporada no fluxo normal do dia a dia.

## Mensagem final

Refatoração é sobre manter a capacidade do software de continuar evoluindo sem se degradar. Todo sistema em geral começa organizado; o problema é que, a cada nova feature, a cada hotfix, a cada prazo apertado, esse design vai se degradando um bocadinho. Se ninguém cuidar disso, chega o momento em que qualquer alteração vira sofrimento.

Refatorar não deveria ser visto como um projeto separado — é uma habilidade que faz parte do trabalho de quem desenvolve software profissionalmente. Toda vez que você abre um arquivo para implementar uma nova funcionalidade, está diante de uma escolha: deixar aquele código um pouco melhor, ou um pouco pior, do que encontrou. No longo prazo, são essas pequenas melhorias que fazem toda a diferença.

---

*Nota: este vídeo é anunciado como introdução de uma possível série sobre refatoração no canal, com planos de vídeos futuros cobrindo code smells, técnicas específicas do catálogo de refatoração de Fowler, e como refatorar com segurança usando testes.*
