---
date: 2026-07-19
tags: [tech-mentor-testing, quality-gate, ratchet, ci-cd, code-review, ia, babysitting-de-agentes]
skill: tech-mentor-testing
level: pratico
---

# Qualidade de Código na Era dos Agentes de IA — Quality Gate e Ratchet

## Contexto

Vídeo em formato de reflexão pessoal (sem roteiro fechado), de um criador de conteúdo/desenvolvedor individual não identificado com confiança na transcrição, sobre como ele garante qualidade de código quando a maior parte (ou totalidade) do código do seu projeto pessoal é escrita por agentes de IA. O autor menciona ser membro/palestrante de uma comunidade paga chamada "Stubborn Club" (grafia incerta na transcrição — soa como "stupid button club"), que já aparece referenciada em outra fonte da wiki. O projeto de exemplo é um app de desktop chamado "Strawberry" (nome parcialmente cortado na transcrição — "strawberry h..."), um cliente local de LLM feito com Electron + React, com scripts de baixo nível para rodar modelos via llama.cpp (Metal no macOS, CUDA no Windows com GPU NVIDIA).

---

## Introdução — o que é qualidade de código

Eu quero falar sobre qualidade de código hoje. Vai ser um vídeo um pouco diferente porque não tem roteiro, não é sobre um assunto novo, não é sobre inteligência artificial — é sobre qualidade de código. Vamos voltar um pouco e falar sobre engenharia de software.

Primeiro: o que é qualidade de código? Quando a gente coloca isso no Google, a definição que aparece é que *code quality* é uma forma de medir o quão bem estruturado está o teu código e o quanto ele segue alguns padrões. Tem muita coisa na nossa área de engenharia de software que foi estabelecida há décadas e que são padrões de formas de criar projeto: arquitetura hexagonal, design patterns, esse tipo de coisa. Tudo isso vira e se torna algo que a gente chama de qualidade de código. Se você trabalha na área há bastante tempo, provavelmente já conhece essas palavras-chave.

E hoje, no nosso mundo atual, quem é que gera o código? É a inteligência artificial. Então como é que a gente garante que a IA está gerando código de qualidade para nós?

No início, a gente usava a IA como um copiloto — revisava tudo que ela criava. Atualmente, o que a gente anda fazendo é basicamente spawnar diferentes agentes, múltiplos agentes fazendo múltiplas tarefas ao mesmo tempo, e isso gera, no fim, um pull request — ou simplesmente modificações que você vai ter que revisar, seja pelas ferramentas que você usa para interagir com a IA, seja no próprio GitHub.

## Um pull request real como exemplo

Peguei um pull request que estou desenvolvendo há uns dois dias, desde o final de semana. Comprei um PC Asus (como devem ter visto no meu Instagram), e esse Asus vem com uma RTX 5060, o que vai me permitir fazer otimizações para uso de modelos de IA locais rodando em computadores Windows com GPU. No macOS eu já uso Metal para algumas otimizações, mas no Windows, se você tem uma placa NVIDIA, precisa usar CUDA junto com o llama.cpp.

Esse pull request está modificando 16 arquivos — parte é documentação, outra parte é da arquitetura de client (estamos falando de apps de PC): como um script de baixo nível interage com Electron, depois com o React, com o renderer do aplicativo; tem testes, scripts de tuning, e por aí vai. A grande questão é: como fazer um PR desse tamanho, totalizando quase 800 linhas modificadas, e garantir a qualidade desse código que vai para produção?

Isso é uma tarefa que estou trabalhando agora — se eu abrir o Cursor, tenho três tarefas pendentes rodando ao mesmo tempo, tirando essa. É muito código para vir aqui fazer a revisão de qualidade manualmente.

## O ponto de partida: Uncle Bob e análise estática no PR

Recentemente trouxe uma citação do Uncle Bob, que postou no Twitter dizendo que nós, programadores, somos péssimos em escrever código — somos muito lentos e tudo mais — mas que a gente não precisa abrir mão da qualidade por causa disso. Ele trouxe um ponto: colocar análise estática, colocar análise de qualidade de código no seu pull request.

Fazia tempo que eu queria montar esse setup, e acabei fazendo há umas duas semanas. Já compartilhei isso numa palestra exclusiva para membros do Stubborn Club, onde temos treinamentos a cada duas semanas (já são mais de 12 aulas gravadas), com acesso a vários desenvolvedores e desenvolvedoras de SaaS que estão na mesma vibe de criar produto e se desenvolver.

## O quality gate e o "babysitting" de agentes

O que eu mostrei lá foi o seguinte: hoje, todo pull request que eu abro passa por um **quality gate** — um portão de qualidade — que faz a IA corrigir problemas que eu teria que revisar manualmente e pedir para ela refazer. Normalmente, o que peço para os meus agentes é que, ao abrirem um pull request, eles façam **babysitting** dele.

Vou explicar com mais detalhes qual ferramenta estou usando num vídeo na quarta-feira — todo mês a gente muda de preferência de ferramenta. Mas, de forma mais abstrata: normalmente tenho um agente com todo o AI harness (também vou explicar isso no vídeo de quarta), que gera o código, cria uma branch, e dessa branch cria o pull request. No fim, peço para ele abrir o PR — esse é o resultado final dele — e fazer babysitting: ele vira uma babá do próprio PR, monitorando.

Os modelos top de linha já entendem bem o que você quer dizer com isso. Normalmente é: o CI está verde? Os revisores deixaram comentários? Os revisores podem ser o Copilot, uma ferramenta externa, ou um colega seu. E dentro do CI também rodam os testes e o quality gate. O modelo fica em loop fazendo isso: abre o PR, verifica se o CI passou, verifica se os revisores deixaram comentários, e se deixaram, vai lá e endereça os comentários.

Se você ainda não criou uma skill para isso, recomendo muito criar uma skill de babysit e customizá-la. Uma das coisas que gosto de fazer é pedir para a IA resolver todas as conversas depois de endereçar os comentários, para que no GitHub você consiga acompanhar quais comentários ela já implementou.

## Baseline e o padrão ratchet

Foi nesse processo que criei o quality gate, e a IA fica automaticamente corrigindo, corrigindo, corrigindo. Deixa eu descrever o que é isso: eu tenho um **baseline**, que é a base que o gate usa como referência para medir melhorias.

No momento em que você coloca um quality gate num projeto que nunca teve controle de qualidade, o projeto vai ficar "vermelho" se você comparar com uma baseline zerada — não dá para mergear um PR com quality gate contra uma baseline ideal, porque tudo vai falhar. Então o quality gate funciona assim: você define uma baseline — por exemplo, cobertura de código não coberto em 7%, e o PR está levando isso para 10% (regressão); duplicação de código com baseline em 2,2%, e o PR está levando para 2,04% (melhora); violações de regras de lint aumentando (regressão).

Um exemplo real de regressão: o arquivo `local-llm-service.js` cresceu de 1000 para 1140 linhas nesse PR — cresceu 140 linhas, pouca coisa, mas o arquivo já estava acima do limite estipulado. Antes de eu poder mergear esse código, a IA fica no babysitting tentando corrigir isso: refatorar o que fez, aplicar um DRY (não exatamente por causa do DRY, mas porque um arquivo está crescendo demais), modularizar. A IA já é capaz de fazer isso — se você entregar esse problema para um Claude Opus 4.7 ou um GPT-5.5, esses modelos conseguem enxergar a situação e pensar numa solução que combine com uma boa arquitetura. Antigamente a gente tinha que descrever tudo isso para os modelos; hoje não precisa mais — eles já foram treinados com os livros de como escrever bom código.

### Por que os modelos não corrigem tudo de primeira

Os modelos não fazem isso de cara porque são "preguiçosos" — mas não por acidente. Se eles fizessem o código certo desde o início, você gastaria menos tokens. O que as empresas de IA descobriram é que, deixando os modelos "preguiçosos", elas queimam mais tokens: você recebe um output que não está perfeito, dá um novo input para gerar um novo output, e fica nesse ciclo. Toda vez que o modelo passa pelo babysitting, gasto mais token, mais token, mais token — mesmo que o modelo, tecnicamente, já tivesse capacidade de acertar de primeira. Não seria mais vantajoso comercialmente para as empresas de IA se o modelo acertasse de primeira.

### O custo do Ultra Review / Ultra Plan da Anthropic

Quanto custa isso? Teste o Ultra Review / Ultra Plan da Anthropic para ver quanto custa. Quando eles lançaram, foi interessante porque, num bate-papo no canal do Fernando, alguém estava lançando um produto/solução que por trás rodaria um modelo muito melhor (algo como "Mitos" — nome incerto na transcrição), e dois dias depois a Anthropic lançou o Ultra Review e o Ultra Plan. Fui testar e gastei uns 150 (moeda não especificada) só de teste: rodava o Ultra Review, ele gastava 30, e tinha um bug no Claude — eu ficava sem limite e o Ultra Review simplesmente crashava, já tendo consumido o saldo. Para ele terminar e eu ver o resultado, eu tinha que colocar mais crédito, e mais crédito. É muito caro — mas esse é o mundo em que a gente está agora.

## Visão geral do projeto Strawberry

Deixa eu trazer uma visão geral do meu projeto, que chamo de Strawberry: atualmente ele está com 483 violações de ESLint, espalhadas em 120 arquivos; 2,2% de duplicação de código (relativamente baixo); 7% de cobertura de testes; e 19 arquivos acima do limite de tamanho definido — o maior deles é o `app.js`, com 4600 linhas.

Mesmo assim, já consigo dormir um pouco mais tranquilo abrindo PR todo dia com meu agente de IA escrevendo a maior parte do código — na real, ele escreve praticamente 100% do código, porque o quality gate que montei tem uma **regra de ouro**: cada PR pode adicionar código, mas não pode aumentar nenhuma das métricas — nem uma violação, nem uma linha, nem 0,1 ponto percentual. Esse é o meu baseline: não pode ficar pior do que isso. Aos poucos vou começar a colocar PRs de refatoração para melhorar esse baseline.

Isso normalmente se chama de **ratchet** — "catraca": você só anda num sentido. Uma vez que você congela o baseline, o repositório só pode melhorar a partir dali, ou empatar. Antes de fechar o vídeo achando que isso é burocracia que vai atrasar o trabalho: essa catraca é o que torna possível deixar a IA escrevendo 100% do código sem o codebase virar um "slop" (bagunça) em seis meses. E não é só o quality gate que resolve isso sozinho.

## O pipeline de CI/CD por trás do quality gate

Pedi para o próprio Claude fazer um resumo do que tenho no meu pipeline. Quando um PR é aberto:

1. `npm ci` — instalação determinística.
2. `npm audit --audit-level critical` — bloqueia o PR se houver qualquer vulnerabilidade crítica.
3. `npm audit --audit-level high` — avisa, mas não bloqueia.
4. `npm run lint` — o padrão do projeto React.
5. `npm run test:coverage` — Jest rodando com coverage (`c8`/coverage).
6. Um script Node de **quality gate**, que faz o check central — o coração da catraca de baseline.
7. A partir disso, comentários automáticos no PR, alguns steps no sumário do PR, e upload dos artefatos (coverage e relatórios) — para que o próprio agente de IA tenha acesso a eles depois. Não adianta só deixar isso visível no PR; o agente precisa ter acesso aos artefatos para entender o que está dando errado.

### O script de quality gate

O arquivo `quality-gate` tem 581 linhas. Ele importa um `baseline.json` — o arquivo com o baseline que descrevi. Também define um arquivo de métricas (`metrics-summary.json`), roda um coletor de métricas, e depois um script que compara as métricas coletadas com o baseline. Isso gera as falhas, e a partir delas é escrito um sumário em Markdown com métricas, baseline e falhas.

Para coletar as métricas, o script lê os arquivos de coverage, o resultado do ESLint, e as duplicações. Por exemplo, para duplicação existe uma função `collectDuplicationMatrix`, que roda a biblioteca **jscpd** (qualquer biblioteca de detecção de duplicação de código serve) — monta os argumentos do comando do jscpd, roda o comando, pega o output, e constrói o sumário a partir dele. Tudo isso que estou coletando já tem biblioteca pronta para fazer — não é nada excepcional que estou inventando, só estou colando um monte de ferramentas e chamando isso de quality gate.

## Redefinindo qualidade de código para a era dos agentes

Se voltarmos à definição de qualidade de código do Google, diríamos que um projeto precisa ter boa manutenibilidade — e acho que isso tem mudado bastante na nossa área. O que significa um projeto de boa manutenção? Sempre falamos que o melhor código é aquele que um ser humano entende — você escreve para que, daqui a um ano, você mesmo entenda o que escreveu. Isso sempre foi resolvido via *readability*.

Hoje em dia, precisamos pensar nisso também para agentes. Uma das coisas que vejo a galera errando é remover comentários que os agentes deixam no código. Acho que um comentário perto do código, explicando o que aquele trecho está fazendo e por que está sendo feito daquela forma, é muito melhor do que ter um README gigante — porque hoje os AI harness vão buscar, via grep ou qualquer ferramenta que estejam usando, o arquivo específico que precisam alterar, e conseguem ler aquele arquivo, o código, e os comentários que trazem informação que não está explícita no código. Isso torna o código muito mais legível. Eu sempre fui a favor de não escrever comentários porque o código é a própria documentação — mas, no mundo de agentes de IA, estou voltando um pouco atrás nisso.

Além da manutenibilidade, tem a **confiabilidade** (o quanto uma função faz o que é prevista para fazer, com o mínimo de bugs), o quanto ela é **testável**, e o quanto é **eficiente**. Há formas de medir isso — uma muito usada é o SonarQube. O que estou mostrando aqui é o mínimo do mínimo: um script simples, mas você poderia usar algo como SonarQube no seu projeto. O próprio GitHub Code Quality também tem métricas de complexidade, duplicação e coverage. Tem também code review — pedir para uma IA revisar, ou para um colega humano.

## Reflexão final: o humano vira o gargalo

Tudo isso reduz débito técnico e por aí vai — mas, ao meu ver, não é sobre isso que estou falando. Estou falando porque eu acabei virando o gargalo da IA. Fazer o babysitting das coisas básicas do PR é o gargalo: não consigo entregar quatro tarefas ao mesmo tempo se precisar ler 10.000 linhas de código por dia. Então tenho que começar a me blindar dos meus próprios erros como revisor de código — e é uma coisa curiosa de se pensar: a IA está escrevendo o código, a IA está revisando o código. Então o que a gente faz é a parte da engenharia: o controle de qualidade, entendendo que, como qualquer controle de qualidade, o humano é falho. Por isso é preciso colocar catracas, colocar portões, para barrar automaticamente quando a qualidade cair.

Ainda essa semana vou falar mais sobre como estou usando inteligência artificial.
