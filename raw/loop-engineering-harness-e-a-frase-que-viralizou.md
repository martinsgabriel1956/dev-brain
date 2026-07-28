# Loop Engineering, Harness e a Frase Que Viralizou

> Transcrição bruta em bloco único, sem pontuação/seções — reestruturada em markdown (contexto, definição de loop em 4 peças, ganhos concretos sobre prompt a prompt, origem histórica no padrão ReAct, os três fatores que destravaram loop engineering em 2026, e a correção da frase "loop engineering matou harness engineering"). Vídeo do Pedro Nauke (criador do Compose), primeiro de uma série de três sobre loop engineering.

## Contexto

Todo mundo no YouTube de dev está falando sobre loop engineering — "parei de dar prompt, agora só uso loop". A afirmação não está errada, mas a maioria dos vídeos manda parar de dar prompt sem explicar duas coisas: por que loop engineering só se tornou possível agora, em 2026, e não no passado; e para que serve na prática, no dia a dia. Este é o primeiro de três vídeos aprofundando o tema. O Compose, ferramenta criada pelo autor, já trabalha o conceito de loop engineering desde julho do ano anterior — antes de virar palavra da moda.

## O Que é Loop Engineering: as Quatro Peças

Loop engineering é parar de operar a IA prompt a prompt e passar a desenhar um sistema — determinístico ou não — que opera a IA por você. Um loop tem quatro peças-base:

1. **Objetivo definido de forma checável** — dá para verificar se foi cumprido ou não.
2. **Ação** — o próprio agente executando o trabalho.
3. **Feedback** — o sistema observa o resultado e avalia se aquilo foi feito de fato.
4. **Condição de parada** — o ponto em que o sistema sabe se terminou ou se precisa rodar mais uma iteração.

Essas quatro peças rodando em repetição formam um loop.

### Exemplo Concreto: o Compose

O Compose pega uma ideia (uma feature, por exemplo) e conduz desde a idealização — o PRD — até a implementação, em processo spec-driven executado em loop: escreve o documento de especificação, quebra em tarefas, executa uma a uma, revisa o próprio trabalho, guarda o que aprendeu em memória e segue para a próxima tarefa, até o objetivo final ser cumprido. Não é necessário dar prompt tarefa por tarefa manualmente — um sistema determinístico por trás roda esse ciclo.

**Resumo:** um prompt dá uma instrução; um loop dá um trabalho inteiro.

## Quatro Ganhos Concretos de Loop Engineering sobre Prompt a Prompt

Operar prompt a prompt entrega só o que a atenção do humano consegue captar, um prompt de cada vez. O loop rompe esse teto de quatro formas:

1. **Autonomia** — o loop roda sem que alguém precise visualizar cada etapa; dá para deixá-lo rodando de madrugada ou durante o almoço, em momentos que normalmente seriam gastos olhando a IA trabalhar.
2. **Paralelização** — dá para colocar vários loops rodando ao mesmo tempo, cada um numa worktree isolada, como se fossem features ou bugs diferentes trabalhando em paralelo (existe depois o trabalho de merge). O autor relata gerenciar no máximo 4-5 loops simultâneos antes de perder controle.
3. **Velocidade da máquina** — tarefas repetitivas e chatas (ex.: migrar 200 arquivos de uma biblioteca para outra, subir cobertura de teste de módulos inteiros) o loop executa uma por uma, testando cada passo, sem o cansaço de fazer manualmente módulo a módulo.
4. **Composição** — a cada rodada, o loop guarda o que funcionou em memória e não recomeça do zero; melhora a cada iteração (isso varia de harness para harness).

**Aviso:** loop só compensa quando a tarefa é repetitiva, revisável e valiosa. Usar loop numa tarefa única, sem processo repetitivo, é "usar uma bazuca para matar uma mosca".

## Por Que a Ideia do Loop Não é Nova

A ideia central do loop não é nova — é antiga. Existe desde 2022/2023 um padrão chamado **ReAct** (agir e observar em ciclo): um `while` que pega a resposta anterior e a joga para a próxima iteração, repetindo até que algo seja concluído, sempre compondo o próximo contexto. Essa é a base de todo agent loop e de todo sistema agêntico por trás dos harnesses atuais — toda ferramenta agêntica precisa acumular tool calls e respostas para que o agente saiba o próximo passo e o que já foi feito.

## O Que Destravou Loop Engineering em 2026 (Não é a Ideia do Loop)

Se a ideia é antiga, o que mudou foram três fatores que destravaram a execução eficiente de loops — nenhum dos três é a ideia do loop em si:

1. **Capacidade dos modelos para long tasks** — modelos frontier atuais (GPT-5.x, Opus etc.) aguentam executar por horas ou dias sem se perder, graças ao nível de reasoning atual, que permite planejar e decidir o próximo passo por muito mais tempo sem intervenção humana constante. Modelos menores/open source com menos parâmetros ainda se perdem depois de poucos passos.
2. **Evolução do harness** — compactação de contexto deixou de ser um grande problema; os próprios logs e tool calls gerados pelos harnesses viram dado de treinamento para versões futuras dos modelos, num ciclo que se retroalimenta (mais execução → mais log de falha → melhor treinamento → modelos que fazem mais com menos informação).
3. **Estado persistente** — um bom harness não carrega a tarefa inteira "na cabeça"; ele escreve o progresso num arquivo ou board (o que foi feito, o que falta). Isso permite que a conversa estoure o contexto sem problema, porque o modelo sabe onde parou através desse estado persistente, normalmente em arquivos markdown no filesystem.

O que mudou em 2026 não foi a ideia de loop — foi o motor (modelo) e o chão (harness + estado persistente) ficarem bons o suficiente para aguentar o loop rodando sem parar no meio do caminho.

## A Correção Mais Importante do Vídeo: "Loop Engineering > Harness Engineering" é Falso

A frase que viralizou — "loop engineering é maior que harness engineering" ou "loop engineering matou harness engineering" — está errada. Harness e loop não competem: **o loop contém o harness**. Tudo que sustenta um loop rodando por horas sem errar — compactação de contexto, estado persistente, modelo aguentando long tasks — é harness, não loop. O loop é só o ciclo que roda por cima. Sem um bom harness por baixo, nem o modelo mais inteligente do mundo sustenta esse ciclo. Por isso o Compose funciona bem: é loop determinístico por cima de um harness que gerencia runs, contexto, persistência e revisão por baixo.

**Frase-resumo do vídeo:** um prompt dá uma instrução; o loop dá um trabalho inteiro; mas o loop só entrega esse trabalho se houver um harness por baixo aguentando o tranco. Primeiro se constrói o chão (harness), depois se roda o loop.
