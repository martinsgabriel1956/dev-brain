---
date: 2026-07-27
tags: [carreira, historia-da-computacao, complexidade, especializacao, unix, react, devops]
skill: tech-mentor-leadership
type: transcript
---

# A Insanidade de Ser um Programador Hoje

> Transcrição de vídeo de reação (canal não identificado no áudio) ao artigo ["The Insanity of Being a Software Engineer"](https://0x1.pt/2025/04/06/the-insanity-of-being-a-software-engineer/) de Vitor Sousa Pereira, publicado em 06/04/2025 no blog 0x1.pt. Transcrição bruta já estava em português (narrador lê/parafraseia trechos do artigo original em inglês e reage a eles) — limpa e estruturada em markdown, sem necessidade de tradução do áudio em si; trechos citados do artigo original foram mantidos como o narrador os leu/traduziu.

---

## Introdução

A insanidade de ser um programador hoje — vamos ver esse artigo aqui do Vitor Sousa Pereira sobre a insanidade [de ser engenheiro de software]. É algo que eu penso frequentemente, porque não consigo deixar de me perguntar se a maioria dos outros empregos são assim. Cara, tem muita coisa que eu questiono sobre a nossa área.

## Senso de comunidade: o caso do Ken Thompson e do grep

Qual que é a primeira diferença da área de programação/TI com outros empregos? O senso de comunidade. Vamos pegar o caso do Ken Thompson: o `grep` — provavelmente já usaram. Dá para fazer uma busca recursiva por todos os arquivos que têm, por exemplo, "GitHub" como conteúdo dentro deles (`grep` recursivo, excluindo algum diretório tipo `node_modules`). Isso traz de volta todos os arquivos com aquele conteúdo e as linhas correspondentes.

Isso foi criado pelo Ken Thompson, porém era um comando privado dele — algo que ele criou para si antes de abrir ao público. Esse senso de comunidade se repete: quem criou o Unix? A motivação por trás do Unix, se eu não me engano, era para fazer um jogo. O Thompson estava lá, criou um ambiente melhor para trabalhar no seu jogo, o *Space Travel*, e nesse processo criou o Unix. Depois de criar, o que ele fez? Guardou para ele? Não — depois de um tempo isso foi absorvido pela comunidade e muita coisa foi criada em cima do Unix.

Isso sem falar de bibliotecas — várias libs que vocês usam no dia a dia. Quando você desenvolve um software, você é capaz de montar seu software com pedaços de outros softwares, de motivações diferentes, de várias pessoas que, sem receber dinheiro por isso, foram lá e compartilharam seu trabalho. Isso, para mim, é simplesmente incrível e diz muito sobre a nossa área.

## Sistemas complexos como Lego

Tem um trecho legal no artigo sobre "GL complicated programs building out of..." — basicamente ele fala que, às vezes, você quer criar um sistema complexo e faz isso encaixando sistemas mais simples e menores, como se fosse um Lego. Isso deve existir em outras áreas também, mas será que, por exemplo, um time de arquitetos ou a comunidade de advogados tem esse quebra-cabeça, essas peças compartilhadas onde um constrói em cima do outro numa finesse surpreendente?

## A curva de aprendizado é brutal desde o início

Ser engenheiro de software é difícil: você precisa conhecer algumas linguagens de programação e ferramentas desde o início — é assim que você conversa com os computadores. Mas isso não é suficiente. Você entra no *rabbit hole*: as empresas esperam que você conheça qualquer framework específico que elas usem — pode ser Rails, Django, Laravel ou qualquer outro. Você também precisará de CSS — levará uma vida inteira para aprender, e você ainda não vai saber por que o layout está quebrado, mas saber o suficiente para se virar já é viável.

Isso é especificamente difícil no início por causa de uma coisa muito peculiar da nossa área: a curva de aprendizagem. Se a gente desenhasse dois eixos — eixo Y = o que você consegue criar, eixo X = o que você precisa saber (conhecimento) — no início você precisa adquirir muito conhecimento para conseguir criar alguma coisa, e essa curva não é contínua: tem várias barreiras.

**Exemplo pessoal do narrador — como enviar um e-mail.** A primeira barreira dele foi algo simples: como enviar um e-mail. Já sabia HTML e CSS, já tinha colocado até um JavaScript no meio, mas no site que estava desenvolvendo queria um formulário de contato que enviasse e-mail. Descobriu num fórum da época que, para enviar o e-mail, precisaria de algo chamado *back end*. Por quê? Não interessa — mas precisava. Aprendeu PHP. Antes de conseguir enviar o e-mail, teve que aprender várias coisas: como rodar um Apache, o que é um Apache, a diferença entre um HTML/JavaScript rodando no browser e algo rodando na máquina fora do browser, como o browser se comunica com esse outro pedaço de código rodando em outro lugar. Pode ser Node, pode ser Nginx — várias coisas. No final, ainda descobriu que, para enviar o e-mail, não é uma requisição HTTP — é outro protocolo, o **SMTP** (Simple Mail Transfer Protocol).

E isso se repete a cada novo objetivo. É improvável que você não precise lidar com JavaScript — talvez tenha sorte e precise só de um pouco de jQuery de vez em quando num app legado. Antes do jQuery, tinha o Ajax (como as coisas vão pro servidor e voltam sem recarregar a página — antes disso, dava pra usar um iframe). Antes do Ajax, já dava pra fazer isso de outro jeito. Mas as coisas mudam: o pessoal do Facebook criou o React.

## A falsa história do "sempre existiu front-end e back-end"

Aquela empresa, com dezenas de milhares de engenheiros, sempre teve duas especialidades, front-end e back-end? **Não** — isso está errado. Não é verdade que "sempre existiram" essas duas especialidades. A distinção front-end/back-end é algo muito novo, de **2006-2007**. Antes disso, o que existia era basicamente um dev desktop e um dev web — você era um *web master*, um dev web, fazia tudo, era o "full cycle" do negócio. Não tinha essa distinção. Foi quando o front-end começou a ficar mais complexo que surgiu a distinção — e se essa complexidade era necessária é debatível, mas ficou mais complexo mesmo.

Piada do narrador: todo dev que diz que é "backend specialized" na verdade é um front-end frustrado, e todo front-end é um designer que aprendeu a codar. Esses conceitos não existiam quando o narrador aprendeu PHP para mandar e-mail — essa distinção veio lá por volta de 2005-2006, e é quase certo que quando Mark Zuckerberg começou o Facebook, todo mundo fazia tudo. Não é "sempre teve duas especialidades" — isso veio depois.

## O nascimento do "fullstack" como corte de custos

A mente coletiva de programação decidiu que React agora é "a maneira certa" de desenvolver front-end. Mas ao mesmo tempo as empresas decidiram que não podem mais contratar dois engenheiros separados — e assim nasce o engenheiro *fullstack*. "Aprenda React e crie APIs REST com base na tecnologia de back-end" — só falta abrir um ticket pro time de back-end pra implementar sua API. Daí vem o BFF (*backend for frontend*), o GraphQL como "solução" — e não para por aí.

## Tipos, estado, tooling: a pilha de exigências

Você precisa de tipos (o narrador sempre teve tipos, começou com VB e Java antes do PHP — para ele, não ter tipos é o mais bizarro possível: "como assim um dado não tem tipo, pode ser qualquer coisa?").

O artigo continua ironizando: "adicione TypeScript" — "vai gerenciar estado no React como um plebeu? Adicione Redux" — "está se sentindo esperto por ter evitado os dois? Divirta-se descobrindo como configurar Webpack, esbuild, Rollup, além do Prettier e do ESLint". O narrador concorda: toda essa responsabilidade, tudo isso que precisamos aprender antes de criar alguma coisa (ou antes de conseguir um emprego), é real.

Contraponto irônico do artigo: "você pode continuar fazendo do jeito que sempre fez, funcionou perfeitamente, não precisa de React" — claro que pode, vai fazendo — mas aí você se desvia completamente da maneira como as coisas são feitas em toda startup que "queima dinheiro" rápido, e vai ter que ensinar os novos contratados (que só ouviram falar de React) sobre as vantagens de server-side rendering. "E descobrimos que estávamos apenas começando."

## De sysadmin a DevOps a SRE: infraestrutura também virou responsabilidade do dev

Antigamente existia um profissional chamado **administrador de sistemas**, cujo trabalho era garantir que o back-end estivesse funcionando: mudanças de infraestrutura, atualização de banco de dados, atualização de sistema, manutenção de daemon em execução, reinicializações. Hoje o SRE faz isso. Depois veio o DevOps: empresas com dificuldades financeiras decidiram que isso tudo passaria a ser feito pelos próprios engenheiros — e todo mundo concordou. Isso, para o narrador, também é parte do grande hack: quando ele começou, literalmente programava dentro da sala do servidor, e parte de debugar era olhar pra trás pra ver se a luz do HD ainda estava piscando.

Agora, aprenderam Docker — "ah, seu aplicativo inteiro é um único binário estaticamente vinculado, você não precisa de Docker" — aprenda Ansible. E espero que se divirta descobrindo as opções que precisa passar para o `systemd`, porque você nem chegou na metade do caminho: agora precisa aprender AWS, e não vai configurar sua infraestrutura numa interface gráfica "como um camponês" — é melhor aprender Terraform, Pulumi ou qualquer outro.

## A "recompensa": virar gestor (e depois voltar a codar)

Você faz um bom trabalho, é promovido a gerente — precisa aprender uma nova função, mas tudo bem, é o "objetivo final". Aqui estão algumas coisas que você precisa fazer: estimar prazos, atribuir tarefas aos colegas de equipe, participar de revisões anuais, dar feedback valioso em reuniões de produto. É melhor torcer para sua empresa ter quadruplicado o número de funcionários até agora, ou você vai estar fazendo tudo isso junto (gestão + código). Observação do narrador: depois dos *layoffs*, a grande maioria dos engineering managers voltou a codar — isso mudou não só pela quantidade de funcionários, mas porque as empresas estão pressionando, e sempre pode piorar.

## O anúncio de vaga absurdo

Um recrutador entrou em contato com o narrador sobre uma vaga de engenharia para uma "empresa secreta": queriam habilidades sênior em **Rails**, **Hotwire**, desenvolvimento **mobile nativo** — por que não adicionar desenvolvimento de kernel e de compilador também, só para garantir?

## Complexidade cresceu, especialização diminuiu

O software fica mais complicado — toda essa complexidade existe por um motivo — mas o que aconteceu com a especialização? O narrador acha que isso anda junto: construir software ficou **menos especializado** porque o nível de abstração aumentou, e o nível de complexidade das várias peças que você precisa encaixar também aumentou — isso levou a você não ser tão especialista quanto antes. Não que antes não existisse alguém especializado em front-end ou back-end, mas você sabia, por debaixo dos panos, os protocolos.

Exemplo: o narrador duvida muito que alguém em 2025 que queira enviar um e-mail vá parar pra aprender o que é SMTP, ou se deveria usar POP3 ou IMAP. Esse tipo de questionamento não é mais feito — normalmente as pessoas vão perguntar "qual API eu uso pra enviar e-mail" (Resend, do Zeno Rocha; Vercel; etc.). Parece mais complicado porque há muitas opções, porque muita abstração foi criada em cima de um SMTP simples, de um POP3, de um IMAP simples. Antigamente se aprendia essas coisas de base — você era mais especializado, mas ao mesmo tempo mais generalista, porque conseguia entender tudo profundamente; e era mais simples, porque não tinha tanta abstração.

## Analogia com a construção civil

Quando uma casa está sendo construída, há toneladas de pessoas envolvidas: arquitetos, engenheiros civis, encanadores, eletricistas, pedreiros, designers de interior, agrimensores, pavimentadores, entre outros. Comentário do narrador: no Brasil a galera pega os projetos "da cabeça", faz reforma em casa e chama o "pedreiro conhecido" que vira mestre de obra — o cara faz tudo. Mas, de modo geral, você não espera que uma única pessoa (ou mesmo uma única empresa) seja capaz de fazer tudo sozinha.

## Fechamento

Talvez um futuro em que se possa criar um aplicativo inteiro com apenas alguns prompts não seja tão ruim. O narrador diz que já é a favor de voltar: parar de tentar aprender tudo que é novo o tempo todo, e voltar ao "vanilla JS, HTML, CSS — escreve teu SMTP e manda o e-mail". E nunca esqueça de se hidratar.
