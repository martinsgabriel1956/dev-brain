# Loop Engineering: Por Que Você Deveria Estar Desenhando Loops, Não Prompts

## Introdução

O criador do OpenCode falou o seguinte: "Você deveria estar desenhando loops que fazem prompts no seu agente." E o criador do Claude Code também falou o seguinte: "Eu não faço mais prompts no Claude. Eu tenho loops que descobrem o que tem que ser feito, e o meu trabalho é criar loops."

O que eles estão falando aqui é exatamente do que se trata esse vídeo. Nesse vídeo eu vou abrir a caixa do loop. Você vai entender o que é hype e o que de fato é útil, e vai conseguir tirar proveito disso a partir de hoje.

Eu sou o Hulk, eu ajudo indivíduos e empresas a colocarem soluções de IA em produção e lucrarem com isso. Comunidade Hulk e Hulk Empresas, ambos os links estão na descrição. Bora pro trabalho, vamos lá.

## O que tá acontecendo

Se você não conhece esses dois caras, como eu disse aí na introdução: um trabalha hoje na OpenAI e outro trabalha na Anthropic. Ambos trabalham em empresas que vendem tokens. E o que eles têm que você não tem — provavelmente você não tem tokens infinitos, guarda essa mensagem aí, tá.

E a segunda coisa: ambos aqui tão falando sobre criar soluções. O que seria — não importa o que você tá criando, de software, de SaaS, etc, etc. Eles estão falando nesse perfil aqui, tá. Então guarda essa informação pra gente prosseguir aqui.

No vídeo passado eu falei como eu recriei o padrão de dynamic workflows usando LangGraph, tá, e é basicamente esses padrões aqui — a gente viu no vídeo lá. Você tem interesse, vai no vídeo, você não viu ainda, é um vídeo que provavelmente tá à frente do tempo.

E o padrão que eu percebi ao longo do caminho é: quem cria a própria harness é um vibe coder superior a quem não cria harness. E o que que seria criar harness? Seria criar soluções de IA. Eu já mostrei diversas aqui, por exemplo aquela renda do WhatsApp ao público que eu botei aqui, eu expliquei o método, expliquei tudo o que tá feito.

E por que que você fica melhor quando você aprende a fazer harness? Você fica melhor no vibe code porque você entende intrinsecamente esses padrões e você resolve problemas. Então você cria em cima desses padrões e usa esses padrões implementados por outras pessoas — muitas vezes o Claude, muitas vezes o Codex — para resolver o teu problema de gerar o código. Então é um ganha-ganha: você aprende a fazer harness, você obviamente aprende a fazer vibe code.

E pensando nisso, muita gente me perguntou — a gente lançou um curso de vibe coding para os membros da comunidade baseado exatamente nessas ideias. O curso não é voltado para Claude Code nem Codex, a gente na verdade lá usa OpenCode, mas você pode usar qualquer ferramenta. E a ideia é mostrar um workflow.

E por que eu tô mostrando isso tudo que eu vou mostrar a partir de agora sobre loop? Na verdade ele é uma espécie de workflow, só que de maneira automática. E o nosso curso lá ele percorre exatamente esse caminho do workflow, e você vai poder eventualmente automatizá-lo. E essa é a ideia do loop, tá. Então você tem um workflow de desenvolvimento que você pode automatizar, e é isso que eles falam sobre o loop. Eu vou mostrar exemplos práticos para você a partir de agora.

## Quebrando o termo: Prompt → Context → Harness → Loop Engineering

Muito bem, vamos quebrar o termo em pequenos pedacinhos aqui, tá. Vamos pegar o histórico, né, pra gente não se perder.

**Prompt engineering**: você melhora uma chamada. Então você já sabe, tá, engenharia de contexto, né, você já sabe que melhora o contexto. Isso é muito importante, isso a gente continua fazendo, isso é importante, assim como prompt engineering é importante ainda — você precisa fazer um prompt aqui, ali, tá.

**Harness engineering**: você melhora o ambiente como um todo. Tem muitos vídeos meus aqui sobre como fazer, e todos esses subtópicos relacionados. Esse por si só é uma indústria enorme. E aqui na internet, pelo que eu noto, é diferente do mundo real: as pessoas associam apenas harness engineering a vibe coding, mas harness engineering é muito maior do que vibe coding. Se você aprende a criar uma harness, como eu disse, você de fato consegue fazer um bom vibe coding, porque você entende os padrões. Então você consegue usar harness dos outros sem precisar reinventar a roda. Você sabe como o modelo funciona, como ele chama as ferramentas, qual o limite de contexto, para que a compactação serve, o que que é uma skill, etc, etc. Isso é um conhecimento que vira parte da sua natureza, tá.

E aí os caras vieram com essa ideia do **loop engineering**, que é basicamente melhorar o ciclo todo da harness, digamos assim — todo o ciclo que acontece desde a primeira chamada até a resposta final que você recebe, tá.

E essa ideia de "você não faz o prompt no agente, você desenha o sistema que faz" é exatamente o que eu mostrei semana passada. Talvez vocês não entenderam, talvez vocês não tiveram oportunidade de ver o vídeo e não viram a fundo. E eu quero mostrar exatamente ele para vocês, tá.

## Anatomia de um loop na prática

Esse aqui é um loop, tá. Como que é um loop? O que que tá acontecendo aqui, tá? Eu tenho uma estrutura, tá — o loop não acontece milagrosamente, né, tá, você tem uma estrutura, e dentro dessa estrutura você vai ter um ou mais loops, tá.

E o que que eu faço aqui, o que que acontece: eu dou uma pergunta para ele, tá, pro meu agente. E é exatamente isso que esses caras estão falando. Eles estão falando o seguinte: "O meu agente descobre o que tem que ser feito, cria os prompts." Só que tem um detalhe ali que eles não falaram: não adianta, por exemplo, usar um agente para criar um código ou para fazer uma tarefa e não verificar se essa tarefa foi bem executada, correto?

Então se você tá fazendo vibe code — se você fizer o curso lá, por exemplo, você vai ver que a gente tem uma fase de verificação do código gerado. Show de bola. Só que o que a gente faz nesse loop é: a gente cria um prompt dinamicamente. Então eu não vou mais criar o prompt para todas as tarefas, eu vou criar uma estrutura capaz de gerar prompts infinitos para diferentes agentes/subagentes, infinitamente. Só que ele também vai gerar uma **rúbrica**. E esse é um tópico muito importante — o que seria a rúbrica, você vai ver já, tá, vem comigo aqui.

Então o que que eu fiz: eu fiz uma pergunta, o meu agente vai descobrir o que é, tá, ele tá fazendo um racional aqui, o plano. Você tá vendo tudo exatamente como o meu loop pensa. É exatamente isso aqui: é uma harness que tem um loop. E esse aqui é o curioso, tá: ela tá sendo acionada à medida que eu mando uma pergunta, mas nada impede de eu fazer essa harness aqui rodar a cada uma hora, verificar alguma coisa automaticamente, e fazer alguma coisa por mim.

É isso que tá acontecendo na indústria lá fora, e é isso que a gente tem o poder de fazer hoje. O futuro já é agora. Só que a distância, né, entre a informação útil de fato e o mercado é lenta, muito porque vários desses conteúdos são em inglês — são de origem inglesa, né, da língua — requer conhecimento técnico alto, e existe um gap entre uma coisa e outra, obviamente aqui no Brasil, você sabe disso, tá.

## O Planner

Então beleza, ele entende a entrada, e o que que ele vai fazer: ele vai criar subtarefas, tá. No meu caso aqui, eu mostrei lá que o meu agente poderia fazer até 160 subtarefas ao mesmo tempo, tá. E aí, mais uma vez que eu te digo, não precisaria ser eu promptando ali a entrada — já tá, ele poderia ler dados, por exemplo, do meu banco de dados todo dia lá à meia-noite, e verificar se a venda diminuiu, por exemplo, tá.

Ele verificou que a venda diminuiu, ele aciona, ele vai mandar esses dados aqui pro meu workflow. O meu workflow vai olhar aquele dado e falar assim: "Ah tá, de repente eu tenho que fazer X coisa." E ele vai montar a própria harness dinamicamente para resolver aquele problema.

Nós estamos saindo da ideia de "eu crio código para resolver um problema" para "eu crio código para resolver uma série de problemas nesta categoria". Você consegue entender? Esse é o nível de abstração — nós estamos mudando de abstração, nós estamos resolvendo o problema em outro nível. OK, é isso que a engenharia está se ocupando agora.

Show de bola. Então o que que meu planner faz — e se você lembra lá no meu vídeo anterior, eu usei o GPT 5.5 para fazer o planner. Por quê? Porque essa é uma atividade que requer um modelo melhor, correto? Então beleza.

E o que que esse planner faz: ele vai gerar o meu prompt, tá, para este subagente. Então ele vai gerar o prompt para todas as subtarefas que ele acredita que sejam necessárias. Tudo isso aqui que você tá vendo — objetivo, papel, resultado esperado e fontes sugeridas — vai entrar no prompt do meu subagente. Então, ao invés de eu fazer essa requisição ao subagente, existe uma LLM entendendo o problema e mandando essa tarefa para um subagente.

E aí o que tem aqui de interessante também é que ele cria uma rúbrica. E o que seria essa rúbrica: ele vai dizer "tá, faça isso", mas vai dizer "essa tarefa só tá cumprida se você cumprir essa, essa, essa, essa exigência". Show de bola, show de bola, OK.

## O Subagente e o Verificador

Então você já viu como é que o planner funciona e o que que ele fez. Agora a gente vai ver o subagente, como que isso funciona na prática. O que que o subagente faz: o subagente vai fazer o que ele tem que fazer lá, vai achar a resposta.

E a parte interessante aqui é exatamente essa dinâmica do subagente e um **verificador** do subagente. O que seria isso: é uma outra LLM. E quando eu digo "outra" é literalmente outra, é um outro modelo. Por que que você tem que fazer isso com um outro modelo? Porque você não pode ter um bias, né, o mesmo viés. Então você usa um modelo para gerar resposta e um outro modelo para verificar a resposta gerada.

Esse segundo modelo aqui recebe exatamente aquela rúbrica, ele sabe qual é a rúbrica, e ele vai olhar a saída desse agente anterior, correto, e vai falar: "Ah tá bom, a saída está legal, pode passar" ou "não, a saída está ruim". E quando a saída estiver ruim, olha o que ele vai fazer: ele vai fazer um follow-up, tá, que seria "reescreva o relatório incluindo uma tabela markdown com colunas".

Você entende o que a gente tá fazendo: a gente cria uma estrutura que vai delegar as subtarefas e vai definir qual é o critério de aprovação. Obviamente isso é excelente para fazer código. Eu acredito que — já existe o AutoGPT/AFF Loop há um tempo e não foi pra frente exatamente porque tinha esse problema de você criar um monstrinho, né, você deixava lá rodando. Isso aqui é muito mais sofisticado do que AFF Loop, obviamente, tá. Só que, se você não tem token infinito e você preza pela qualidade do seu codebase, você vai querer um engenheiro por perto sempre no momento de decisão.

Mas para trabalhos corporativos isso aqui é maravilhoso. Para pesquisas internas, para entendimento do cliente, isso aqui é fantástico, tá. Então você pode criar estruturas assim hoje sem depender da Anthropic, sem depender da OpenAI, sem depender de ninguém, desde que você tenha conhecimento.

Beleza, show de bola, tá. E você vê aqui que ele fez o follow-up, e ele fez três tentativas, tá. O que aconteceu: ele veio aqui uma vez, pediu de novo, pediu de novo, pediu de novo, e ele não aprovou, tá. E o que ele fez foi não aprovar — "qual condição de saída é essa?", essa condição fui eu que criei. Mais uma vez, a escolha é minha e eu defino qual é o critério de decisão.

Eu poderia fazer aqui, por exemplo: se ele manda um follow-up que o primeiro modelo não gerou direito, eu poderia — já que a solução é minha — falar assim: "não, troca o modelo e gera essa resposta com outro modelo, e vamos ver a resposta", tá. Tudo isso é possível, desde que você saiba o que você tá fazendo.

Show de bola, show de bola, tá. Vamos ver um outro exemplo aqui do resultado do subagente que não aconteceu isso, tá. Então ele fez o que ele tinha que fazer, deu a resposta dele lá, e você vê que a verificação rodou, a confiança tá alta, e nesse caso não teve follow-up. Então o meu agente gerou a resposta, ou fez a tarefa que ele tinha que fazer, o meu verificador olhou e falou assim: "não, isso aqui passou na rúbrica, tá tudo certo", e ele aprovou.

E é basicamente isso, tá. Então você vê o nível de detalhe que a gente tem: você vê aqui que o meu subagente verificador verifica o problema, diz qual o problema, e cria o follow-up. Nós estamos criando máquinas automatizadoras — é essa a beleza da coisa, é esse o novo nível de abstração, tá.

## O grafo como nível de abstração

E só para você fixar essa ideia, o que que é, qual é o espírito dessa abstração: estrutura com aqueles padrões que eu falei no vídeo anterior e que eu acabei de demonstrar aqui no meu gráfico, tá, tem vários daqueles padrões implementados ali. Você vai ter um prompt gerado automaticamente, um ou mais, né — então eu tenho quatro prompts sendo gerados automaticamente ali para os meus subagentes, e eu tenho rúbricas geradas dinamicamente. E eu criei uma máquina de estado que verifica o estado de todas essas coisas e roda automaticamente, principalmente trabalhos que são de conhecimento, né, os knowledge workers, o trabalho de colarinho branco — vários deles a gente pode fazer isso, desde que a gente entenda o problema. E é importante a gente entender o problema, senão você nem vibe code vai conseguir fazer, correto, correto.

Show de bola. Então a minha defesa é que o **grafo é um novo nível de abstração**. Se você fez computação, você já viu o grafo, já viu esse G = (V, E), tá, então o gráfico é igual a vértices e arestas, o E, tá.

Então você pode pensar no seguinte: os nós, né, o nosso bonequinho aqui — vamos lá, esse carinha aqui — são a computação, é onde algo acontece computacionalmente, tem um custo computacional aqui, tá. E aqui são as arestas, de condição de fluxo, e você é quem define essas condições de fluxo.

Então, quando fala lá, o cara fala "o meu trabalho é construir loops", ele tá construindo ou um nó de computação, ou uma camada de abstração de condição de fluxo. Por quê? Você não quer deixar que a LLM decida tudo. Existem decisões que são determinísticas, e você precisa entender do problema para você fazer essas condições. Então você muitas vezes vai usar computação que é LLM para resolver um problema no nó, e o controle das arestas é feito de maneira determinística. E assim a gente tem o melhor dos dois mundos usando essas abstrações com grafo.

Aí você vai falar assim: "mas os caras não usam LangGraph e você usa?" Obviamente você pode fazer grafo do jeito que você quiser. Você pode fazer num papel, escrever um grafo, você pode fazer uma conta matemática — inclusive, quando a gente aprende grafo, a gente só aprende assim, o grafo não depende de um framework. O grafo é uma ideia, é uma abstração.

Então, se você quer se dar bem nesse novo mundo da tecnologia — sempre foi assim, na verdade, mas agora é a hora de entender o novo nível de abstração — o grafo é um nível de abstração. Quando eu decidi começar a usar LangGraph, eu tinha entendido essa abstração, já tinha muita familiaridade com o grafo, e é por isso que eu adotei a ferramenta. E parece que eu acertei na direção do mercado quando eu decidi isso, porque é um nível de abstração que a gente precisa ter o controle da estrutura e deixar a LLM trabalhar onde ela trabalha muito bem.

## Fechamento

Então, se você pretende de fato construir soluções para o novo mundo, para o novo mercado, quer se juntar aos construtores — Comunidade Hulk, precisa de ajuda na tua empresa para entender esse processo, ou quer treinamento corporativo, também Hulk Empresas. Nós temos ajudado diferentes pessoas, e tem sido um prazer trabalhar com a galera que de fato tem se movido além do hype e tem buscado construir.

Quem consegue entender boa parte do que eu falei aqui entende que a gente tá saindo de uma fase da computação e de uma fase da tecnologia computacional em geral para outra. Obviamente LLMs têm seus riscos, têm seus problemas, as empresas que fornecem tokens têm suas próprias agendas, mas a tecnologia tá aí, ela não vai embora. Adapte-se ou saia do jogo.
