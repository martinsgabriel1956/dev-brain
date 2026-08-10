# O Paradoxo da Aceleração: por que 93% dos devs usam IA e a produtividade só sobe 10%

> Transcrição de vídeo (pt-BR), transformada em Markdown. Fonte original: transcrição de áudio;
> nomes e números limpos para leitura, mantendo o conteúdo fiel ao original.

93% dos devs usam IA para escrever código. A produtividade real das empresas aumentou 10%.
Essas duas coisas são verdade ao mesmo tempo — só que tem alguma coisa errada com essa conta,
ou tem algo errado com a forma como a gente está medindo esses dados.

Hoje eu vou mostrar os dados que ninguém está colocando no mesmo parágrafo e o que eles vão
revelar sobre como você está usando IA no trabalho.

## Os dados da pesquisa da Faros AI

A Faros AI analisou times de engenharia de verdade — não é uma pesquisa de satisfação, é dado
real de produção.

- **93%** — quase todo mundo usa IA. A adoção já está consolidada.

O que você esperaria ver no lado da produtividade da empresa? Um número parecido. Só que na
realidade não é tão parecido assim, porque o **ganho real de produtividade é 10%**. É pouco,
vai um pouco contra o que a gente esperava, e é decepcionante para um número tão alto de adoção
— e também pelo preço.

Mas vamos olhar os números individuais:

- Os devs fazem **21% mais tarefas**.
- Fazem merge de **quase o dobro de PRs**.

Isso acontece na prática: o time entrega cada vez mais PRs, e o gargalo agora está na hora de
revisar. Quando você usa Claude Code ou Copilot, você realmente entrega mais rápido — o
autocomplete funciona, o código gerado funciona, o boilerplate sai na hora.

Então, como é que individualmente você está entregando quase o dobro de PRs, e o time cresce só
10%? Alguma coisa não fecha.

## O gargalo migrou da escrita para a revisão

- **Tempo de code review aumentou 91%.**

Você produz o dobro de PRs, e alguém precisa revisar esses PRs — só que a revisão **não escalou
junto**.

Antes da IA existia um equilíbrio: o dev escrevia um PR, alguém revisava, mergeava — o ritmo era
compatível. Com IA você acelerou muito a produção, mas o gargalo não é mais a escrita. **O
gargalo agora está na revisão.**

A revisão é uma tarefa que exige atenção humana, contexto do sistema e julgamento. A IA não
resolve isso ainda — na verdade, ela vai criar **mais código para você revisar**.

Detalhe sutil e importante: **código gerado por IA não é mais simples de revisar** — às vezes é
até mais difícil.

Parece que a gente otimizou a parte errada do sistema. É exatamente o que a Faros AI chama de
**paradoxo da aceleração**: mais velocidade individual, mas mais atrito no sistema.

## Percepção vs. realidade

Um número que incomoda:

- **95% dos devs se sentem mais produtivos com IA.**

Só que, objetivamente, na mesma pesquisa, eles estão produzindo **código de qualidade menor**.
Há uma **dissociação entre percepção e realidade** — a sensação de produtividade não está
calibrada pela qualidade do que é entregue.

Isso é perigoso não porque a sensação seja "ruim", mas porque **métricas erradas geram decisões
e feedback errados**.

## O dado mais revelador: sêniors em legado

O Pragmatic Engineer fez uma survey com mais de 90 desenvolvedores em 2026:

- **Juniores em tarefas simples:** ganham entre **26% e 56%** mais produtividade com IA.
- **Sêniors trabalhando em codebases legados:** ganho **zero ou negativo**.

Como isso é possível? A ferramenta supostamente ajuda todo mundo, mas está prejudicando os devs
mais experientes no contexto mais crítico.

A explicação mais convincente: **a IA funciona como amplificador do que já existe**.

- Um sênior bom, num codebase legado, sabe que aquele sistema tem nuances — decisões de design
  tomadas 10 anos atrás por razões não documentadas. A IA trata o código existente como se fosse
  a verdade. Quando o sênior verifica o que foi gerado, está comparando contra um código que não
  é bom.
- Um sênior mediano, no mesmo contexto, começa a delegar mais e a aceitar sugestões sem verificar
  o contexto histórico — especialmente se não conhece esse histórico. Geralmente existe um sênior
  que é "o pai do sistema", que sabe tudo, mas essa informação está na cabeça dele. (Dá para
  discutir se isso deveria ser documentado — hoje, na maioria dos casos, não é.)

O código gerado é **tecnicamente válido** (segue os padrões), mas **arquiteturalmente errado**.
Você tem um PR que **passa nos testes e quebra a lógica de negócio**.

> Frase da pesquisa que ficou: "Sêniors bons ficam melhores; sêniors medíocres ficam mais
> difíceis de gerenciar."

Isso é diferente de dizer que a IA é ruim para sêniors. Ela é um **amplificador — e amplificador
não tem julgamento**.

## O problema é o que a gente mede

As métricas que os times usam para medir produtividade com IA são **métricas de output**:
quantidade, velocidade, volume. E a IA é exatamente o tipo de ferramenta que faz essas métricas
subirem, **independente da qualidade**.

As métricas que realmente importam são outras:

- Quantos bugs chegaram em produção depois que você começou a usar IA?
- O tempo de code review aumentou?
- Os incidentes ficaram mais frequentes?

Um dado honesto que a Faros AI incluiu:

- **30% dos devs já bateram nos limites de uso das ferramentas de IA.**

Isso não parece uma adoção sustentável — é receita para **burnout**.

A pergunta que ninguém está fazendo: **você está usando IA para escrever mais código ou para
escrever código melhor?** São escolhas diferentes, com resultados diferentes.

## Três perguntas concretas para levar ao seu time

1. **Bug rate.** Se a IA está te tornando mais produtivo e a qualidade está aumentando, o número
   de bugs depois do deploy tinha que cair. Se está subindo, você tem um problema.
2. **Ciclo de code review.** Se o último PR levou mais de uma semana para mergear, o gargalo não é
   você — é o processo. Adicionar mais PRs só piora.
3. **Facilidade de mudar o codebase.** O sistema como um todo (não só o último módulo que você
   tocou) está ficando mais fácil ou mais difícil de mudar?

## A mudança de papel: engenheiro → tech lead

Nos próximos dois anos, os papéis de **engenheiro** e **manager** vão convergir. O engenheiro
vira cada vez mais um **tech lead**: quando a IA gera o código, o trabalho passa a ser
**decisão, revisão e direcionamento** — gerenciamento do sistema, não escrever código.

Nessa nova era, o dev que vai prosperar **não é o que escreve mais rápido — é o que consegue
julgar o que foi gerado com critério.**

## Fechamento (relato pessoal)

"Eu já caí nessa armadilha. Tinha a sensação de estar entregando muito, e quando ia revisar — uma
semana depois — a arquitetura estava bagunçada, mexendo em coisas que não deveriam, sem respeitar
as boas práticas que o time aceitou e que não estavam bem documentadas. Talvez esse seja o ponto:
começar a tirar o contexto que está na cabeça do engenheiro e colocar no papel."
