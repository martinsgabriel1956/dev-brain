# Code Review Morreu? Uncle Bob Não Lê Mais Código, Push Force pra Prod e "Business Manda em TI"

> Transcrição de vídeo (Lucas Montano). Reação à repercussão no X/Twitter do post de Uncle Bob dizendo que não lê mais o código escrito pelos seus agentes de IA. Limpa e organizada a partir do áudio original em português; conteúdo preservado, sem tradução (fonte já em PT-BR).

## O post de Uncle Bob e a treta com o Fernando

Uncle Bob (Robert C. Martin), semana passada, voltou a dizer que não revisa mais o código — na verdade que ele nem olha mais o código que a inteligência artificial está escrevendo. Isso gerou muita repercussão no Twitter/X.

O Fernando de novo estava envolvido numa dessas tretas com o Uncle Bob (o Uncle Bob responde se você o marcar). O Fernando cutucou: "Uncle Bob, tu sabe o que é estar *on call*, ou tu só sabe escrever livros legais?"

O Bob respondeu: "Fui o líder técnico em muitos projetos diferentes, passei muitos anos de plantão — provavelmente mais anos que você está vivo." E completou:

> "Sou consideravelmente mais velho que você, comecei a programar no final dos anos 60. Minha estratégia atual é não ler nenhum código escrito por meus agentes. Essa é a única maneira de aproveitar a produtividade deles. Em vez disso, submeto os agentes a restrições extremas: testes unitários, testes Gherkin, procedimentos de controle de qualidade, métricas de qualidade, teste de mutação, cobertura de testes e uma infinidade de outros. No fim, tenho muita confiança no código que eles produzem, porque tiveram que passar por todas as minhas restrições e testes."

Eu até perguntei pro Uncle Bob o que ele está construindo — porque ele fala que usa todos esses quality gates e tudo mais, e fiquei interessado. "Não ter medo de ler o código, se você não está mandando nada pra produção, é fácil." Ele não me respondeu, mas, dando uma olhada no GitHub dele, ele tem alguns projetos rodando quality procedures e testes end-to-end. Um dos projetos é o "Missile Command dual platform" — acho que é um *play project* mesmo.

Ele está vivendo o que eu espero viver no futuro: não me importar com nada, só programar as coisas que estou a fim de programar. Acho bem massa: alguém com no mínimo 60 anos de experiência (programa desde os anos 60), ainda programando, é uma inspiração.

## Eu estou alinhado com o Uncle Bob (e faço push direto em prod)

Confesso que estou um pouco alinhado com o Uncle Bob. Tenho revisado cada vez menos código. Estou num novo patamar de *push force* pra mim: às vezes modifico coisa direto em produção — logo por SSH na minha VPS, rodo o Claude Code lá dentro e faço as modificações. Estou fazendo isso nesse exato momento, uma modificação direto em Prod no servidor do Persoa.

A única questão é dar um *downtime* no Stupid Button Club. Mas, no meu caso, downtime não importa tanto, desde que rode e teste tudo funcionando em Prod.

### Bloco patrocinado — Hostinger

A VPS que uso nos meus projetos é a Hostinger. O plano que uso é o **KVM2**: dois núcleos de vCPU, 8 GB de RAM, armazenamento SSD, backups semanais grátis, gerenciamento de firewall, e servidores no mundo todo. Ao contratar VPS da Hostinger dá pra fazer implantação com um clique de coisas como Claude Code, Codex CLI, N8N, Docker — então, se você muda o projeto de uma infra pra outra e usa Docker, é só subir. Dá também pra instalar só o sistema operacional (eu uso Debian; tem Ubuntu, Alma Linux, Arch Linux e outros). Também dá pra testar com um clique coisas como o Odysseus (do PewDiePie) e o Hermes. Usa o cupom **Lucas Montano** pra garantir desconto (link na descrição).

## O argumento central do Uncle Bob: o que fazer com o tempo economizado

No X, o Uncle Bob complementou (ele ficou meio mordido com a galera comentando):

> "A IA escreve código muitas vezes mais rápido que você — talvez 20 vezes."

O ponto: a IA escreve código 20x mais rápido que você, e esse tempo economizado, o que você faz com ele? Você vai escrever unit tests, testes de aceitação, testes de QA (quality assurance). Aí você tem 10.000 linhas de código — e esse é o ponto: se você tem tudo isso, como é que você vai revisar? Você não revisa mais o código. Essa é a questão.

É muito legal ver um cara com experiência estar na fronteira, usando os agentes, *spawnando* um monte de agente.

## A reação da comunidade (e a defesa do Uncle Bob)

A galera comentou: "Não consigo acreditar que o Senhor Código Limpo não se importa mais com a qualidade do código. Arquitetura limpa e atenção aos detalhes são de suma importância em todos os domínios sérios."

O que essas pessoas esquecem é que o Uncle Bob nunca falou sobre *código* — ele falou justamente sobre **código limpo** e **qualidade de código**. E a grande questão é que essa qualidade é **mensurável** — não depende de algo subjetivo/humano. Isso tem regra. Você tem as regras, e consegue medir isso com um processo de quality gate no seu CD. Ou seja, ele escrevia sobre *regras*, não sobre você escrever código. Foi o que ele respondeu:

> "Code quality still matters. It matters a lot. I verify it by using tools that measure."

## Gergely Orosz: o conceito de code review desaparecendo

O Gergely (Pragmatic Engineer) postou:

> "Não consigo deixar de notar o conceito de revisão de código desaparecendo. Conversei com um engenheiro extremamente experiente e competente que, até recentemente, revisava todo o código gerado por sua IA. Até o lançamento do Fable, ele concluiu que não faz sentido continuar revisando — então está parando de fazê-lo, a menos que seja para partes essenciais do produto. Isso vindo de alguém que sempre revisou o próprio código e o de todos os outros ao longo de toda a sua carreira. Ainda não sei o que substituirá a revisão de código, pois algo precisa surgir no lugar dela."

Minha opinião: já surgiu. Todos esses processos que o Uncle Bob citou já surgiram. A revisão de código morreu quando começamos a produzir 10.000 linhas de código por dia.

## "Território desconhecido" e a inversão TI × Business

Outro perfil que viralizou:

> "Estamos em território desconhecido. Não existe nenhum livro que ensine como desenvolver software em 2026. Todos estão aprendendo a partir dos princípios básicos."

Não me surpreenderia se o Uncle Bob lançasse um "Clean Code com IA".

O Felipe Regazio comentou quatro opiniões:
1. Estamos em território desconhecido — sim.
2. Estamos tentando usar serrote pra apertar parafuso em muitos contextos.
3. TI não manda mais em TI. **Business agora manda em TI**, porque acha que a IA sabe mais de TI do que o pessoal de TI.
4. Vai piorar muito antes de melhorar.

Isso me lembra de uma mentoria no Stupid Button Club: numa empresa com seis devs, demitiram metade porque alguém do time comercial *vibe codou* uma solução com Claude, o CEO ficou deslumbrado e decidiu demitir metade do time pra usar IA. Ainda temos um hype absurdo acontecendo, e esses CEOs que tomam essas decisões estão equivocados.

## O sketch do freelancer (e por que o dev não some)

Vi um sketch que é muito real: um freelancer passa orçamento pro cliente ("vou cobrar X pra construir esse sistema"), e o lead responde que não — "por esse valor eu faço com IA mesmo". Resposta do freelancer (que serve de argumento de venda):

> "Vamos fazer o seguinte: você faz com a IA e eu faço com a IA, e depois a gente vê qual ficou melhor."

O cliente começou a falar e, no meio, percebeu: "Não, mas você tem anos de experiência, é óbvio que o teu sistema vai ficar melhor que o meu."

Esse é o ponto. Se você bota o time comercial pra vibe codar dentro da empresa, tudo que for vibe codado vai precisar de melhorias. Aí você reúne os três melhores do comercial que sabem vibe codar, e é tanto software gerado, tanta automação, que esses três viram um **time de TI**. Ou seja: se você pode produzir mais software, por que usaria alguém que não é da área? Você vai acabar especializando alguém que não é de TI em vibe codar um produto de TI — não faz sentido. Só faz sentido demitir alguém e substituir por IA se o seu *supply* já foi suprido (você automatizou tudo e o problema passou a ser vender, não produzir).

## Minha opinião sincera sobre code review

- **Projeto de um homem só:** revisar cada linha que a IA escreveu é uma **red flag** — significa que você não colocou nenhum teste de qualidade no seu pipeline. Eu, sozinho (ex.: codando no Persoa), não faço mais code review: peço pra IA revisar o código, penso em testes automatizados end-to-end, em orquestração de testes — mas não perco mais tempo revisando linha por linha. Você já tem o *accountability* total do projeto; é só você quem vai resolver os problemas. Aqui concordo com o Uncle Bob.
- **No emprego (time grande):** ainda reviso por pull request. Não porque eu não confie no código (que já é escrito por IA), mas porque pra mim é importante ter **contexto** do que está sendo feito. Não reviso linha por linha: reviso a **arquitetura**, se os **padrões do projeto** estão sendo seguidos, se todos os **requisitos** foram implementados, e **testo localmente** cada pull request. O code review vira cada vez mais o **QA dos próprios devs** num time grande.

## Accountability × substituibilidade: por que o review sobrevive em time grande

Uma vertente que pode virar padrão: o dev ser responsabilizado ainda mais pelo que coloca em produção sozinho. "Você fez o merge, colocou em prod, deu merda, o culpado é você." Isso funciona em empresas de **médio porte**. Em empresa de **grande porte**, a empresa não quer isso — ela quer que você seja **substituível**. Responsabilizar cada dev individualmente aumenta o *bus factor* (o sistema fica na mão de um dev que é o único que entende o que colocou em prod). Uma grande empresa quer **processos**, não heróis.

Por isso acho que vai ter várias verdades na nossa área:
- **Time grande:** code review segue muito bem-vindo (contraintuitivo, mas importante).
- **Time médio:** recursos menos substituíveis; talvez o review do *código* possa ser substituível.
- **Projeto de um homem só:** não faz sentido ler linha por linha o que a IA gera — no máximo ler por cima, sem nem abrir o pull request.

Antigamente eu rodava na minha IDE e revisava linha por linha; isso não faz mais sentido num projeto solo, porque o accountability já é totalmente meu.

## A história do Jira interno vibe-codado (com update)

Um funcionário de uma startup onde a irmã de alguém trabalha criou o próprio Jira. Descartaram completamente Jira, Linear e Trello e passaram a usar uma ferramenta própria — "muitíssimo melhor que o Jira e tão detalhada quanto". E a pessoa nem é desenvolvedora: é responsável pelo controle de qualidade. Isso foi em março de 2026.

**Update (~4 meses depois):** eles voltaram ao Linear/Jira, porque a manutenção da ferramenta interna que desenvolveram com Vibe Code estava consumindo a capacidade de trabalho deles.

É exatamente isso: se você bota alguém não técnico pra vibe codar algo, e esse algo fica bom, ele sempre vai precisar de melhorias — e essa pessoa vai gastar cada vez mais tempo nisso do que no que de fato faz. O dev ainda vai ser o cara que vai vibe codar.

## Fecho

Não esqueça de se hidratar. Comenta como você faz seu processo de code review — se faz, se não faz mais. Forte abraço.
