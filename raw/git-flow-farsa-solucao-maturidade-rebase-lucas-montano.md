# Git Flow é uma Farsa? A "Solução", Maturidade e o Processo com Rebase (Lucas Montano)

> Transcrição de vídeo (auto-gerada, limpa e organizada). O autor se identifica na fala como "Lucas Badico TV" — atribuição a Lucas Montano pelo conjunto de sinais (o famoso vídeo anterior "Git Flow é uma farsa", ensino de Golang, membership do canal, ter fechado a própria empresa ~3 anos antes). Continuação do vídeo anterior sobre Git Flow.

## Introdução: acabou a Copa

Copa acabou, a gente tá aqui de novo para falar de Git. A gente deu uma pausa porque não adiantaria lançar nada no meio da Copa — não faria sentido nenhum, porque até eu mesmo estava assistindo mais à Copa do que aos meus vídeos de tecnologia (tenho que admitir). Mas encerramos esse ciclo só daqui a 4 anos de novo, e até lá vamos ver se em 4 anos a gente te torna um dev profissional e maduro — porque é sobre maturidade que vamos conversar hoje.

## O vídeo anterior: "Git Flow é uma farsa"

Há muito tempo atrás eu fiz um vídeo falando que **Git Flow é uma farsa**, que Git Flow não é essa solução que todo mundo pinta. Tanto se fala sobre Git Flow que parece que Git Flow é padrão em toda a indústria. Mas eu começo esse vídeo te fazendo a seguinte pergunta: **me diga uma grande empresa que está usando Git Flow.**

Não sei se é intencional ou não, mas para mim Git Flow é uma das maiores falácias que a gente tem na nossa bolha dev. Parecido com aquela ideia do vídeo do Clean Code, onde a gente discutiu que **influenciadores são modificadores de cultura**: o Git Flow foi uma parada elevada à estátua de "padrão industrial" pelos influenciadores, sem que de fato a indústria usasse isso.

E, enfim, meti o pau no Git Flow mesmo, fiz um "hunch" (aquele hunch gostoso). De vez em quando esse vídeo sobe, desce, sobe e desce. Este vídeo aqui é a continuação daquele outro — só que nele você vai entender não só a minha resposta, a minha solução, mas também **por que eu demorei tanto**. Porque não é assim, a + b. Não existe uma resposta.

Para ouvir a minha solução — que não é tão boa assim, já admito, vou baixar as expectativas — você primeiro tem que ouvir por que eu demorei a fazer esse vídeo. Qual é a lógica? Por que o Lucas não soltou o segredo? Por que o Lucas está guardando esse segredo? Você vai entender.

## Por que demorei: comunicar maturidade é mais difícil que comunicar sensacionalismo

Diferente daqueles criadores de conteúdo que eu critico no vídeo de Git Flow — que pegam uma ideia, pegam um post, e a comunidade Tech abraça aquela solução como se fosse um gospel, um evangelho, a nova verdade.

Isso aconteceu com o movimento ágil, isso aconteceu com orientação a objetos, isso aconteceu com squads. Para você ter noção: a ideia de você criar squads nasceu no Spotify. Alguém do Spotify fez um post, fez uma palestra sobre isso, o pessoal começou a falar, outras empresas começaram a reproduzir, reproduzir, reproduzir. Ficou tão famoso, e usaram tanto o Spotify como âncora, que **a própria pessoa e o time original que falaram sobre squads vieram a público dizer que o Spotify não usava exatamente daquela maneira**. Um movimento que tinha iniciado usando como justificativa a importância daquilo dentro do Spotify era tão megalomaníaco e tão fora da realidade que não tinha relação com o que acontecia dentro do Spotify.

Quer dizer que squads não funcionam? Não, não é essa a minha defesa. Meu ponto é que **é muito mais fácil comunicar uma verdade sensacionalista ou um argumento sensacionalista** ("ah, o Spotify usa", "esse é o jeito certo") **do que comunicar maturidade**. E, no caso do Git Flow, esse é o ponto: comunicar maturidade.

## O que quero dizer com "maturidade"

Quero dizer que uma solução de Git vai muito além de você ter uma forma para encaixar todas as empresas.

Passando um pouco do que eu vivi nos últimos anos: desde que fechei a minha empresa, quase 3 anos atrás, eu já passei por pelo menos três outras empresas. **Em nenhuma empresa eles usavam Git da mesma maneira, e em nenhuma empresa o processo estava quebrado.** Existiam prós e contras do processo, mas o processo funcionava.

Então, ao invés de procurar uma solução certeira para tudo, o que você, como profissional, tem que buscar são os **princípios**.

## O ponto central: cada empresa compra um processo com prós e contras

Cada empresa vai ter um processo. Cada empresa vai colocar na mesa, vai se expor, e vai comprar um processo que tem prós e contras que fazem sentido para aquela empresa.

E é por isso que Git é muito doido: **Git é muito mais do que só uma ferramenta. Git é parte do processo e da natureza da empresa.**

Estou agora numa empresa bem grande (não vou falar o nome — quebraria todo o meu argumento de você buscar maturidade). Nessa empresa, o processo de levar uma tarefa para produção é a coisa mais maluca que eu já vi na vida. Nunca imaginei que uma empresa tão grande teria um processo tão trabalhoso. Só que **funciona**. Eles estão estudando como fazer algo mais automático, estão buscando melhorar esse processo, mas o processo de hoje funciona. E isso é o que importa: o processo funcionar.

## A minha solução (que funcionou por 4 anos, em times pequenos)

Dito tudo isso, para não te deixar na mão e não me eximir da minha opinião, vou falar qual acho que é um processo que **por um tempo** funcionou na minha empresa. Percebe? Não é o que eu acho que funcionaria na empresa X ou Y — é um processo que funcionou na minha empresa, com prós e contras.

Mesmo o meu processo — que eu acho uma solução muito melhor do que o Git Flow — tem prós e contras. Não existe nenhum processo, nenhuma solução, que seja só prós. Mas ainda sustento que o Git Flow tem muito mais contras do que prós, ainda mais para empresinha pequena.

O meu processo mira exatamente em **times pequenos**. E para times pequenos, **burocracia é um problema.**

### 1. CI / single command deploy (frictionless)

A primeira coisa que você tem que ter pronta em qualquer time pequeno é o seu **CI**: um processo em que, quando você faz deploy na `main`, você entrega e testa o seu projeto — seja um ambiente de teste, seja um ambiente produtivo (produtivo não quer dizer exatamente produção, mas um ambiente *como* produção).

Por exemplo, hoje no meu projetinho pessoal eu tenho um ambiente de **staging** — o que a gente brinca de "deve e testa" — idêntico ao de produção, só muda a URL. São idênticos (tem diferença de capacidade: máquinas menores em staging), mas é um ambiente produtivo. Quando testo algo, quero saber se funciona em produção, então subo para esse ambiente produtivo.

Então a primeira coisa é ter um CI. E aqui, entenda: **CI não necessariamente é algo configurado no GitHub ou GitLab** (seria bom que fosse). Aqui eu considero **single command deploy**. Por quê? Somos empresas pequenas. Empresas pequenas às vezes não têm capacidade de pagar um CI. Então você pode usar a máquina do dev para fazer parte do processo — mas o ponto é: **a entrega tem que ser em um comando.**

Isso é legal porque, dessa forma, você tira problemas de entrega e você tira aquele problema de "o código está pronto, mas não está em produção" — isso tem que acabar. Tem que ser um negócio **frictionless**: pode ser automático no CI, pode ser manual num single command, mas tem que ser frictionless. Isso é necessário.

### 2. Um dono para cada entrega (ownership)

Segundo passo: tem que ter um **dono para a entrega**. Para cada entrega tem que haver um dev responsável, que vai cuidar daquela entrega — garantir que ela chega em produção e orquestrar as dependências. Normalmente é um dev pleno, um dev responsável.

Por quê? No flow que criei na minha empresa, a gente usava **rebase**. E qual é o problema do rebase? Os conflitos têm que ser gerenciados com ownership, porque o conflito é gerenciado de forma diferente. O rebase resolve os conflitos **commit a commit**, e isso é muito oneroso — precisa de alguém com muita atenção.

Hoje em dia, IA ajuda bastante nisso (seria uma coisa diferente hoje). Mas na época em que a gente usava (2020 a 2023/2024, foram 4 anos), era custoso, mas importante. E, mais importante: a gente tentava colocar o dev numa situação em que ele **não** fizesse rebase só antes de fazer o merge, mas que fizesse rebase continuamente — sei lá, uma ou duas vezes por semana — para que, quando fossem mergear, o conflito fosse menor.

### 3. Só existe a `main` (sem branch dev de vida longa)

Outra coisa: **não tinha `dev` e `main`.** A `main` era a verdade. Todo o trabalho, toda feature concluída, era entregue na `main`. O que acontecia era que, às vezes, a versão que você está entregando não vai para produção — fica em staging, fica em desenvolvimento — mas pode ir para produção sim. E é aquela **fonte de verdade** (source of truth).

Porque, pensa comigo: você já teve o trabalho de pegar a sua branch de feature, resolver conflito para levar para a branch de desenvolvimento, e essa branch de desenvolvimento está atrás da branch de produção — e você tem que resolver bug em produção? Em vários momentos, manter os conflitos entre a branch de desenvolvimento e a de produção é um trabalho extra.

No meu sistema **só existe `main`. Não existe outra branch de vida longa.** Você entende que não existe aquele `main`/`dev` — só `main`.

### 4. Rebase, não merge (evitar o "subway train from hell")

E a gente não usa **merge** para levar feature para a `main`, a gente usa **rebase**. Por quê? Quando a gente usa merge, começa a criar o que eu chamo de **"subway train from hell"** — aquelas linhas malucas de branching que ninguém entende. Quando você usa rebase, você entende claramente os trechos da entrega, a ordem.

Para mim, que tinha consultoria, isso era muito importante: ficava claro para o meu cliente o que eu tinha entregado e em qual ordem.

Por muito tempo eu achei — e nos 4 anos confirmei — que trabalhar com rebase, ter a **disciplina** de fazer rebase uma ou duas vezes por semana (recorrentemente, não só na hora de mergear) e usar o rebase para o merge, **evitava aqueles problemas muito comuns**: aquele "consertei uma coisa, e aí essa coisa consertada deixa de estar consertada". Na minha empresa isso nunca aconteceu. (Aconteceu em projetos que não usavam esse processo — projetos que a gente pegava no meio do caminho, com processo já existente. A gente nunca disruptou o time nem o processo que já existia; sempre respeitou e, passo a passo, transformava naquele processo melhor.)

### Por que rebase exige mais atenção que merge

Quando a gente fazia os commits, era **um arquivo, um commit** (tínhamos múltiplos arquivos só em criação — criação de projeto, de pasta; mas se era edição, um arquivo, um commit). Então, quando dava conflito, era em um arquivo, e você ia lá **intencionalmente** corrigir aquele conflito naquele arquivo. Isso fazia com que aqueles "retornos de erro" nunca acontecessem de novo.

Precisa de muita disciplina. Rebase é feito com responsabilidade e com atenção muito maior do que um merge.

## Por que NÃO é uma solução universal (mudei de ideia)

Por muito tempo — e aqui coloco minha culpa — eu achei que esse processo era **o** processo que revolucionaria a indústria, que todo dev deveria passar pelo rebase. Hoje eu não acho mais. Por quê?

Porque funcionava, mas funcionava para **ativos pequenos**, para times que poderiam ter **uma pessoa** prestando atenção no merge, uma pessoa mexendo na branch de feature.

Qual é o "BO" (problema) do rebase? O rebase **modifica a branch da feature** de forma que, se der ruim, você quase perdeu o projeto original — você perdeu a versão original daquela feature. A responsabilidade é muito grande. Para um time onde você pode ter centralização, é perfeito. Mas, por exemplo, na empresa onde trabalho hoje não existe essa possibilidade: se for centralizar isso, o trabalho da pessoa que cuida do merge vira uma loucura.

Então **é um processo que só serve para empresa pequena. Não escala** — hoje eu entendo isso. Mas para empresa pequena eu vou defender que é um bom processo até o fim. Ainda mais hoje em dia com IA, que consegue ser mais automático ainda e diminui muito esse "BO" do rebase.

No meu processo (uma solução para times pequenos): uma branch de feature mergeia na `main` depois de fazer rebase com ela — e aí você só tem **fast-forward merge**, que são bloquinhos de merge bem definidos.

## Encerramento: você se adapta ao processo da empresa, não o contrário

Outra vez: não acho que essa solução seja para você aplicar em todos os seus projetos, ou para todas as empresas. É necessário ter alguém **responsável, maduro, e que conheça Git**.

Se você fizer o curso que vamos propor nos próximos meses, e acompanhar nossa série de Git, talvez você consiga assumir um projeto e usar esse método. Quer dizer que vamos ensinar Git só para isso? Não. Vamos ensinar Git para que você **ganhe maturidade** e possa definir seus próprios processos e se adaptar aos processos de outras empresas.

Para encerrar: **não ache que você vai chegar numa empresa que tem um processo estruturado e funcionando com um "super método master", e que a empresa vai adotar o método que você trouxe. É você que tem que se adaptar ao método da empresa, ao processo da empresa.** Está entendendo por que digo que precisa de maturidade?

Espero que tenham entendido por que enrolei tanto para falar de Git: **porque não existe uma resposta final, uma resposta matadora.** E é muito doido, porque quanto mais sênior a pessoa, mais ela vai concordar comigo. Se isso é uma verdade, deixa aí nos comentários.

Foi por isso que demorei tanto para fazer esse vídeo explicando qual é o bom processo — porque não existe. Existe o meu, que achei que funcionava, e funcionou por 4 anos. Mas ele não é o processo final, não funcionaria em todas as empresas. Na verdade, funciona em pouquíssimas empresas.

## Jabá (menções ao canal / cursos)

Sobre ser dev maduro, profissional responsável: o primeiro passo é se educar. O canal tem recursos gratuitos — na aba "cursos" há três cursos gratuitos (um de Postman, outro de Golang básico, e um extra que ensina a criar seu próprio blog com Docusaurus). A cereja do bolo é o **curso avançado de Golang** (carro-chefe da área de membros, 17 aulas já disponíveis). As novas aulas de Golang seguem depois de terminar a série de Git. Agradecimento aos membros do canal.
