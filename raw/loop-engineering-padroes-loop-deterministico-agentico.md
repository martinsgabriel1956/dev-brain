# Loop Engineering: Padrões para o Loop Trabalhar Sozinho (Determinístico vs. Agêntico, Judge, Orquestrador, Estado, Skills)

> Transcrição de vídeo em português, colada pelo usuário no chat e reorganizada em seções/parágrafos para leitura (removidas repetições e hesitações de fala; conteúdo não traduzido — já em português). Segundo vídeo da série de três vídeos de **Pedro Nauke** (criador do Compose) sobre Loop Engineering — o primeiro é [[wiki/sources/loop-engineering-harness-e-a-frase-que-viralizou]], que já registrava a promessa de dois vídeos seguintes na série. Identificação do autor por inferência: o falante se refere ao Compose como "a ferramenta que eu criei" e retoma explicitamente o conteúdo do vídeo 1 (quatro peças do loop, origem em ReAct) — mesma pessoa já documentada em [[wiki/entities/pedro-nauke]]. Não é a mesma série do vídeo "Loop Engineering: Por Que Você Deveria Estar Desenhando Loops, Não Prompts" (autor "Hulk", série separada).

## Abertura

No primeiro vídeo dessa série eu te falei o que é loop engineering: aonde você basicamente para de operar a IA no braço, prompt a prompt, e passa a desenhar um loop que opera ela por você. Só que aí a pergunta de quem realmente vai usar isso no dia a dia é: "Beleza, mas como eu rodo esse loop? Que tipo de loop, com qual modelo, e como eu não deixo ele se perder no meio do caminho?"

Porque existe uma diferença gigante entre um loop que trabalha sozinho e te devolve o serviço pronto, e um loop que roda por horas, gasta um monte de token e te devolve uma bagunça. E na maioria das vezes essa diferença nem é o modelo especificamente — é mais o tipo de loop que você escolheu e como você gerencia ele por baixo dos panos.

Nesse vídeo eu vou te mostrar os padrões que eu de fato uso para fazer um loop trabalhar sozinho.

## Recapitulando o Vídeo 1

No primeiro vídeo a ideia foi entender o que é o loop e por que ele só ficou possível agora. Nesse segundo vídeo a gente vai pro lado prático: os tipos de loop e como rodar cada um da maneira certa.

## A Divisão Mais Importante: Determinístico vs. Agêntico

A primeira grande divisão, a mais importante de todas: existe um loop que é **determinístico** — feito via algoritmo — e um loop que é **100% agêntico**. Parece um detalhe técnico, mas é essa diferença que decide qual modelo você usa e quanto você vai gastar.

## Loop Determinístico

No loop determinístico você cria um script e, a cada novo round, ele abre uma sessão nova — todo o contexto antigo é jogado fora e um novo contexto é iniciado. É assim que o Compose, a ferramenta que o autor criou, atua hoje.

Como cada round começa do zero, sem lembrar de nada do round anterior, esse modelo de loop precisa que um **arquivo de memória transitória** esteja sempre sendo gravado pelo modelo. Isso deve ser configurado via system prompt: ao fechar uma run ou antes de compactar, o modelo grava tudo que aconteceu naquela memória transitória, num lugar em disco, para ajudar a próxima run a lembrar do que aconteceu.

### O Detalhe de Custo que Quase Ninguém Comenta

Em modelos com característica de "long" reasoning muito alto — como GPT 5.6, Fable ou qualquer outro com reasoning muito alto (pensa muito antes de executar) — o mais custoso é o **contexto inicial**. Toda vez que você inicia uma run nova, você perde muito tempo de reasoning só na formulação inicial de contexto.

No modelo determinístico, quanto maior o modelo em termos de "long", pior — porque você acaba pagando aquele reasoning inicial caro, run atrás de run, e sempre jogando tudo fora no round seguinte.

**Recomendação**: se o loop já tem um bom aparato de artefatos de estado salvo, o melhor é usar um modelo não tão focado em long reasoning — baixar um pouco o reasoning para não pagar caro por algo que vai ser descartado depois.

### Aplicação ao Spec Driven

No processo de spec driven, onde se pega uma spec e quebra em tarefas: para cada tarefa, um modelo com muito long reasoning vai pensar muito até executar aquela tarefa. Como no spec driven já existem artefatos bem definidos, é preciso que a execução seja mais rápida — colocar muito reasoning nos modelos frontier (GPT 5.6, Fable) nesse contexto pode fazer com que uma tarefa leve muito tempo, porque o modelo sempre vai fazer um reasoning muito alto. Existe uma maneira de uso melhor para esse tipo de loop determinístico (reasoning mais baixo).

## Loop Agêntico

O loop agêntico normalmente roda usando um comando que a maioria dos harness tem, o `/go` (barra go) — cada harness implementa de uma forma, mas por baixo dos panos é muito parecido com um half loop. Hoje já é comum: a maioria dos harness, como Claude Code, Codex, Hermes, implementam esse comando.

Nesse tipo de loop, o agente nunca faz uma run nova — ele fica iterando sempre na mesma run, compactando o contexto conforme ela vai enchendo. Esse tipo de loop depende não só do modelo, mas também do harness.

### Codex como o Harness que Melhor Entrega o Loop Agêntico

Para o autor, hoje o harness que mais consegue entregar esse tipo de loop com `/go` é de longe o **Codex** — evoluiu muito em relação à compactação de contexto, a ponto de a compactação quase não fazer mais efeito perceptível de tão eficiente que está.

Combinando essa função do harness com um modelo novo como o **GPT 5.6**, que tem treinamento na própria base de conhecimento do harness — todo Jason (JSON) de log do Codex depois é usado como base de treinamento do modelo — existe um processo de retroalimentação: o modelo vai ficando melhor conforme o Codex vai sendo mais usado em long-running tasks. Cada próximo modelo GPT fica melhor em long-running tasks por causa desse treinamento com os próprios dados do Codex.

### Quem Julga se Terminou é o Próprio Modelo

Como nesse modelo de loop você depende da compactação, e quem julga se aquilo acabou de fato ou não é o próprio modelo, é interessante sempre ter bons **gates de verificação** para garantir que o modelo não vai acabar se perdendo no meio do caminho.

## Spec Driven Morre nos Loops Agênticos? Teste do Autor

Muita gente fala que spec driven meio que morre quando se entra em loops agênticos de long-running tasks. Nos testes do autor (honestamente reportados): testou spec driven quebrando em tasks tradicional em loop determinístico, testou spec driven quebrando em tasks em loop agêntico, e testou também sem quebrar em tasks.

**Resultado**: quando não há quebra de tarefas específica — quando se pega uma spec inteira e simplesmente dá pro modelo executar em loop — o resultado deixa a desejar tanto na definição das tarefas em runtime quanto na execução; pareceu pior e mais demorado.

Quando se define previamente os artefatos que vão ser usados como estado, já se faz a quebra das tasks, e se deixa o modelo preencher critérios de sucesso (lista de testes, descrição mínima, tudo certinho por task) — o resultado melhorou bastante. **Conclusão do autor**: definir o estado antes traz um resultado melhor, mesmo quando o loop não era determinístico.

## Padrão Judge

Um dos padrões mais úteis em loop engineering: o **agente juiz** — julga o que aconteceu no final de cada run.

A ideia: toda vez que uma run termina (o agente diz que terminou aquela tarefa), sobe um segundo agente que roda em background e cujo trabalho é julgar se de fato aquilo que foi proposto foi feito ou não. Ele é o **dono da verdade** — o outro modelo disse que terminou, mas é o judge que vai rodar em background e julgar se de fato terminou.

### Implementação via Stop Hook

Isso pode ser feito através de um `stop hook`, que a maioria dos harness hoje também tem: toda vez que a run acaba (o modelo diz que acabou e faz um stop), esse hook é disparado. O que ele faz: executa o agente juiz (via comando ou integrado no próprio harness — há n maneiras). Isso é determinístico de fato. O judge revisa o que foi feito naquela run e diz se acabou ou não; se não acabou, ele mesmo retorna um novo prompt dizendo que a execução precisa continuar, já contendo o que não foi feito. Assim se tem de fato um ciclo de loop com outro agente julgando se terminou ou não.

### Quando o Padrão Judge é Mais Útil

O padrão judge é muito bom principalmente quando se está usando modelos que não são tão densos e não são tão focados em long-running tasks — modelos frontier "menos densos" como Opus, Grok, Sonnet — que acabam encerrando o loop cedo demais. Se algo precisa rodar durante horas e horas, esses modelos não conseguem executar — acabam parando muito cedo, e é aí que o padrão judge ajuda bastante a mitigar esse erro.

Dá para colocar um judge em modelos maiores também, como Fable ou GPT 5.6, mas o autor não vê tanta necessidade — considera um gasto desnecessário, já que esses modelos conseguem segurar o loop sozinho por muito tempo.

## Modelos Focados em Long-Running Tasks: Fable e GPT 5.6

Na visão do autor, Fable e GPT 5.6 estão muito acima de todos os outros nesse quesito — conseguem ficar muito tempo executando algo mesmo com compactação; guardam o resultado da compactação de uma maneira impressionante. Podem rodar por dias — o autor relata exemplos que rodaram mais de dois dias seguidos.

Enquanto isso, outros modelos menos densos e sem essa capacidade acabam encerrando o trabalho cedo — e é aí que o padrão judge ajuda bastante.

Só que usar só modelo frontier como GPT 5.6 ou Fable tem um custo maior, e nem todo mundo pode rodar esses modelos sempre com reasoning alto, porque não é barato. Por isso é preciso ter outras abordagens para conseguir usar modelos menores dentro de loop engineering — modelos mais baratos que consigam rodar por mais tempo sem ter que ser os modelos mais caros.

## Padrão Orquestrador (Modelo Caro Orquestra Modelos Baratos)

Abordagem interessante: usar os modelos mais densos, focados em long tasks, como **orquestradores**. O modelo caro não faz o trabalho de implementação — ele orquestra outros modelos menores, mais baratos, para fazer a parte de implementação e até de review.

### Exemplo do Dia a Dia do Autor

Com uma spec bem grande, executando algumas tarefas dela num loop agêntico: usar um modelo para back-end e outro modelo para front-end.

No **Compose** (loop determinístico), isso é fácil: basta definir qual modelo em qual tarefa, e na hora de iniciar a nova run ele usa aquele modelo.

Quando o loop **não é determinístico**, isso precisa ser passado via prompt, deixando o modelo orquestrador orquestrar para cada tipo de tarefa. O autor tem um agente orquestrador que segura a run, pode fazer o review, e orquestra outros agentes na hora de executar determinada tarefa. Exemplo de prompt: para back-end, orquestrar um GPT 5.6 (reasoning medium/"terra high" — modelo mais barato); para front-end, usar um Opus 4.8 ou um Grok 4.5, que entregam um front-end muito bom, mais rápido e com preço menor. O próprio modelo orquestrador, na hora de executar uma das tarefas, escolhe qual usar.

Isso é possível fazer via Claude Code, Codex, ou de inúmeras outras maneiras — o harness executa/orquestra outro harness. O autor gosta bastante dessa abordagem e afirma que funciona muito bem: bom para gasto de token e para velocidade de execução (win-win).

## Gerenciamento de Estado Durante o Loop

Penúltimo ponto: a necessidade de uma abordagem de gerenciamento de estado durante o loop — uma maneira de trackear tudo que está acontecendo durante cada run, dentro de um loop agêntico.

Isso não precisa ser algo determinístico — pode ser feito via prompt mesmo, ou até via skill. Instrução ao agente: escrever um arquivo (`.md`) que vai trackear tudo que está sendo feito durante cada run — mapeando qual tarefa foi feita, qual é a próxima, qual é a lista de tarefas, as decisões que foram tomadas, os erros, os arquivos que foram modificados. Os modelos atuais são inteligentes o suficiente para fazer esse próprio tracking bem, só passando via prompt ou skill.

O autor costuma usar `.md` para isso — gosta de ter um arquivo `state.md` (ou "state spec") que guarda o estado daquela run. Exemplo: numa spec com 10 tasks, o agente cria esse arquivo de estado, contendo todas as informações para que aquelas 10 tasks sejam executadas uma por uma, seguindo um padrão formalizado.

## Skills para Gerar Loops Não Determinísticos

Último ponto: criar skills para gerar os loops que não são determinísticos.

### Exemplo: a Skill "C Loop Tests" do Autor

O autor tem uma skill que usa bastante, chamada (foneticamente) **"C Loop Tests"**, que ajuda a fazer loop engineering em cima de spec driven. Ela dá todo o aparato e estrutura organizacional para que o loop aconteça da melhor maneira:

- Já tem um padrão de gerenciamento de estado (o `state.md` descrito acima).
- Define como o modelo deve olhar a spec, o que tem que ser feito, quais são os gates de verificação, quais são as verificações finais de review.
- Define o que tem que acontecer depois de cada task finalizada.
- Define como é o output final e o que precisa ser escrito em termos de memória.

A skill consegue ainda habilitar outras skills durante a leitura, gerando um link entre skills — um processo eficiente de loop engineering.

### Fluxo Completo dentro da Skill

Ao final da implementação, dentro dessa skill, o autor faz com que o modelo sempre execute um processo de **report** e de **execution** (outras skills que ele já tem). Quando termina todas as tasks da spec, o modelo faz o report e o execution daquele "Qwaya" (trecho de pronúncia incerta — possivelmente nome próprio de ferramenta/processo não identificado claramente na fala).

Depois desses passos, o autor ainda pede para executar uma skill de **deep review**, que faz um review de tudo que foi feito e gera issues — que o próprio agente já pode trabalhar e resolver, tudo numa run só. Fluxo: task a task terminando → QA faz o deep review → resolve o deep review. Indo além: depois do deep review, o agente pode abrir um pull request com uma description e fazer um squash merge.

Esse processo funciona muito bem, segundo o autor, com modelos como GPT 5.6 ou Fable, ou com o padrão judge quando usando modelos não tão densos.

## Loop Agêntico Substituindo o Determinístico

O autor relata que muitas vezes acaba substituindo o próprio Compose (sua ferramenta de loop determinístico) por essa abordagem agêntica, porque vê cada vez mais o loop agêntico substituindo, de certa forma, parte da abordagem determinística — já que, com um modelo de reasoning alto como GPT 5.6, isolar o contexto no loop determinístico traz um resultado pior por causa do autoconsumo e da formulação repetida de contexto. Deixar o modelo se autogerenciar, deixar ele decidir como o loop vai acontecer, tem trazido — pelos testes do autor — um resultado melhor.

## Fechamento

Esse foi o segundo vídeo da série de Loop Engineering: a diferença entre loop determinístico e agêntico, e os padrões — padrão judge, arquitetura de orquestração de modelos, gerenciamento de estado e skills para gerar o loop.
