# Por Que Pull Requests Falham (e Alternativas Sem PR)

> Transcrição de vídeo em português, reorganizada em seções e limpa de repetições de fala. Autor não se identifica nominalmente na transcrição. Bloco de patrocínio (AUVP, escola de investimentos) removido por não ser conteúdo técnico — mesmo critério já aplicado em ingestões anteriores de vídeos com o mesmo patrocinador.

## Introdução

Por que pull requests (PRs) falham, por que às vezes não funcionam, e por que algumas empresas optam por sequer utilizá-los. O vídeo tem duas partes: primeiro, como fazer PRs que de fato funcionam e agregam valor rapidamente com a menor quantidade de defeitos possível; depois, alternativas adotadas por empresas que não utilizam PRs.

Como base, o autor traz sua experiência como desenvolvedor de software em várias empresas — todas trabalhavam com PRs — além de conversas com quatro empresários antes de preparar o vídeo, sobre os processos das empresas deles. Todos os quatro utilizam PRs de uma maneira ou de outra. Quase toda empresa aplica a regra: "nada vai ser mergeado sem pelo menos uma aprovação" — com a única exceção observada sendo o MVP de uma única pessoa.

## Parte 1 — Por Que Pull Requests Existem e Como Fazê-los Funcionar

### De onde vem o valor do PR

Existe um corpo de evidências apontando que PRs são uma maneira razoável e rápida de reduzir defeitos no código. O valor vem do fato de, numa equipe distribuída — trabalhando de maneira assíncrona ou mesmo síncrona, cada um na sua máquina — revisar código um do outro, compartilhar informações, e detectar problemas antes deles chegarem à `main` e afetarem os usuários. Também serve para evitar que o time caminhe numa direção errada e gere retrabalho: um código pode não ter bugs, mas estar mal escrito ou difícil de manter — e o PR é o ponto onde alguém pode pegar isso antes de virar dívida.

Dois critérios definem se um PR cumpre seu propósito: precisa ser **razoavelmente rápido** (para evitar retrabalho e acelerar entrega) e precisa **reduzir defeitos no código**. Se não fizer as duas coisas, não serve o propósito de existir.

### O problema do tamanho do PR

Um PR de 200 linhas de código razoavelmente complexo leva de 20 a 30 minutos para ser bem revisado — tempo suficiente para uma análise de verdade, não só "passar o olho".

Um PR de 2.000 linhas de código, na prática, também recebe de 20 a 30 minutos de atenção — porque quem revisa tem uma jornada de trabalho cheia de outras tarefas e não tem tempo (nem disposição) para dedicar proporcionalmente mais tempo. Resultado: a mesma quantidade de bugs encontrados (5 a 10, por exemplo) representa uma fração muito menor do PR grande — o review não escala com o tamanho do PR, então PRs grandes não recebem a atenção que precisariam para reduzir defeitos de forma efetiva.

Duas alternativas hipotéticas também falham: (1) se alguém dedicasse 5 horas para revisar um PR gigante, isso deixaria de ser rápido — seria quase um dia inteiro de trabalho perdido, e o ciclo de idas e voltas (revisar → devolver → ajustar → revisar de novo) faria um PR levar semanas para chegar a produção; (2) um PR de 20.000 linhas simplesmente não vai ser revisado — 0 minutos de atenção real.

### O meme do tamanho ideal

Existe uma dinâmica social conhecida: um PR de 10 linhas de código faz quem revisa "querer sentir que contribuiu", gerando um monte de sugestões de *bikeshedding* (nome de variável, comentário a mais ou a menos, `for` vs. `while`). Um PR de 1.000 linhas de código, por outro lado, tende a receber um "looks good to me" superficial — ninguém vai de fato revisar aquilo. Isso não é o ideal, é como as pessoas realmente trabalham no mundo real.

Daí a existência de um **tamanho ótimo de PR**: não tão pequeno que vire só fricção e bikeshedding (exceção: correções de uma linha, que fazem sentido como PR próprio), nem tão grande que ninguém preste atenção de verdade. Contagem de linhas não é uma métrica perfeita (10 linhas cognitivamente densas podem ser mais complexas que 1.000 linhas repetitivas), mas como referência grosseira: 100–300 linhas é um bom alvo, podendo ser menor (~50) para código mais complexo. Cada PR aberto adiciona fricção ao dia de trabalho de quem revisa (parar, abrir o site, revisar, comentar, aprovar) — e revisão de PR normalmente acontece em lotes (início do dia, final do dia, depois do almoço, depois da daily), não continuamente.

### Inventário é custo (Reinertsen)

Uma das fontes consultadas na preparação do vídeo recomendou o livro *Principles of Product Development Flow*, que traz uma ideia vinda do toyotismo: **inventário é custo**. Ao invés de operar num estilo fordista, o ideal é manter inventário pequeno e processar as coisas de forma rápida e ágil.

Um PR aberto por uma semana é uma semana em que aquele código não está gerando dinheiro — o propósito do código para uma empresa é gerar valor/dinheiro; código parado é dinheiro parado. Exemplo: um dev que ganha R$ 10.000/mês custa ~R$ 2.500 por semana de trabalho — se o PR dele fica uma semana parado, há R$ 2.500 "parados" nesse PR.

Recomendação prática: revisar PRs abertos **todos os dias**, no mínimo — de preferência **duas vezes por dia** (início e final do dia). Assim dá para pedir ajustes de manhã, a pessoa ajusta ao longo do dia, e o código é mergeado no fim do dia — sem perder uma noite inteira com o PR parado. Demorar mais de um dia para revisar impõe um custo adicional de troca de contexto (*context switching*) sobre quem abriu o PR.

Quanto mais rápido no processo um defeito, uma feature inútil, ou um caminho de implementação errado for identificado, menos trabalho (dias, semanas, às vezes meses) é jogado fora depois. Isso é o motivo de se buscar feedback o mais rápido possível durante o desenvolvimento, não só no final.

### Boas práticas para PRs rápidos e claros

- **Concisão** — PR pequeno e com uma única razão de existir facilita revisão, acelera o processo e, se algo der errado depois do merge, permite reverter só aquele PR isoladamente.
- **Clareza proporcional ao contexto do revisor** — se quem revisa já tem contexto absoluto da tarefa, menos explicação é necessária no PR. Se não tem, título claro, descrição, e screenshots de antes/depois (quando aplicável) fazem diferença real na qualidade da revisão.
- **Fast follow** — em vez de negar um PR funcional que só precisa de pequenos ajustes (o que reabriria o ciclo de idas e vindas, aumentando o "inventário parado"), aprovar e mergear o PR, e abrir um segundo PR menor só com as correções. Isso limpa o inventário mais rápido e o segundo PR, sendo menor, é mais rápido e fácil de revisar, com menos carga cognitiva.
- **Conhecimento de contexto** — tanto quem escreve quanto quem revisa precisam entender o domínio (ex.: as regras de negócio de desconto de uma loja) para conseguir detectar bugs reais, não só sintaxe.
- **Draft PRs** — abrir um PR ainda não pronto, mas encaminhado, permite que outra pessoa dê uma olhada e confirme se o caminho está certo antes de terminar — evitando retrabalho por seguir um caminho errado até o fim.
- **Checklists de PR** — algumas empresas usam um checklist que quem abre o PR precisa preencher (ex.: "criei os testes de integração necessários", "testei localmente", "testei em staging"). Pode ser bastante valioso.

### O custo da troca de contexto

O ciclo de idas e vindas de um PR (enviar para revisão → revisor comenta → volta para o autor → autor ajusta → volta para revisão) implica trocas de contexto reais no dia a dia de trabalho — um custo que existe mesmo que algumas pessoas neguem ou subestimem seu impacto.

## Parte 2 — Alternativas Ao Modelo de Pull Request

Seria ideal se o código fosse continuamente integrado à codebase sem a necessidade de parar para criar e revisar PRs — isso reduziria o tempo que código fica parado, as idas e vindas, e as trocas de contexto. O desafio: como reduzir defeitos no código sem depender da revisão via PR?

Processo de revisão de código nunca é livre de falhas — PRs não previnem a existência de bugs, apenas diminuem sua quantidade. Algumas empresas (e alguns estudos) têm tido êxito ao trazer a revisão de código para dentro do próprio processo de criação — enquanto o código está sendo escrito, alguém já está revisando ao mesmo tempo, sem depender de um PR separado. O autor é transparente: nunca trabalhou numa empresa que aplica esse modelo à risca, apenas ouviu relatos — o que segue é uma descrição de como, segundo esses relatos, essas empresas costumam operar.

### 1. Pair programming / mob programming

Dois desenvolvedores (pair) ou mais (mob) trabalhando constantemente juntos, criando e revisando o código ao mesmo tempo, na mesma máquina. Um gestor pode achar isso menos eficiente (duas pessoas fazendo o trabalho de uma), mas estudos demonstram que pair programming não dobra o tempo — a velocidade de produção fica em torno de **1,6x** a de uma pessoa sozinha, não 1x nem 2x. Ou seja: há uma perda de velocidade bruta de escrita, mas o código sai com mais qualidade, o que tende a compensar o tempo perdido — menos tempo de revisão depois, menos retrabalho quando bugs aparecem.

Pair/mob programming demanda mais atenção, sincronização de agenda, e é mais difícil em ambiente assíncrono/remoto — mas a literatura (e a opinião do autor) aponta que é uma prática útil, inclusive para compartilhar conhecimento dentro da empresa. Não é uma prática exclusiva: pode ser combinada com PRs, não precisa substituí-los por completo.

### 2. Trunk-based development

Empresas que não usam PR costumam fazer commit direto na `main` (trunk-based development), com uma review por commit (mais curta que um PR completo, já que o código foi programado e revisado em pool durante o pairing). Para isso funcionar sem aumentar o risco, depende de uma pipeline de testes que decide se o commit pode ou não ir direto pra `main` — geralmente com testes de integração, que pegam o grosso dos problemas e previnem regressões de comportamento.

Isso reduz o tempo em que o "inventário" (código) fica parado, já que não há espera por aprovação de PR.

### 3. Feature flags

Enquanto uma feature complexa está sendo desenvolvida e ainda não está pronta para o usuário, ela fica escondida atrás de uma feature flag mesmo estando commitada direto na `main`. Quando a feature é validada, a flag é liberada aos poucos: primeiro para pessoas dentro da empresa, depois para um pequeno grupo de usuários, e por fim para toda a base — removendo a flag ao final desse processo.

### Opinião pessoal do autor

Mesmo reconhecendo validade em todo esse fluxo (pairing, pipeline de testes, feature flags), o autor pessoalmente ainda criaria um PR — mesmo tendo feito tudo em pair programming e tendo uma pipeline de testes robusta. Reconhece que essa é uma opinião pessoal sujeita a discordância, inclusive de pessoas "muito mais inteligentes" que ele, dos dois lados.

## Fechamento

Esse fluxo (PRs pequenos e rápidos, revisados com frequência; ou, alternativamente, pairing + trunk-based + feature flags) é o que, segundo o autor, faz o código se mover com mais agilidade e faz as revisões de fato funcionarem.
