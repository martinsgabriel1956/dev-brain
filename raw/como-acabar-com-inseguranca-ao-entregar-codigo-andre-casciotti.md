# Como acabar com a insegurança ao entregar código (André Casciotti — Próximo Nível)

> Transcrição de vídeo (YouTube, quadro "Próximo Nível", canal Dev que Resolve). Já em PT-BR; sem tradução. Limpeza de ASR: "André Casac" → André Casciotti; "sior" → sênior; "Selenum/Cypers/Playwght" → Selenium/Cypress/Playwright; "Jao" omitido/ambíguo mantido como no original; "senner" → sênior; "devs/deves" → devs. Pontuação e parágrafos adicionados.

## Abertura

Sabe quando você escreve o código, ele roda, até parece que funciona, mas sempre bate aquela sensação: "pô, será que isso aqui tá certo? Será que eu fiz tudo que precisava fazer?" Não importa se você é júnior ou sênior, todo dev sofre com insegurança. Hoje eu quero te mostrar por que isso acontece e o que você pode fazer para resolver esse problema.

Fala, dev! Beleza? Vamos para mais um Próximo Nível, aquele quadro onde eu compartilho dicas e estratégias para você evoluir na sua carreira. Eu sou o André Casciotti e ajudo devs a subirem de nível com código que resolve e que não volta com bugs. Se você anda meio perdido na carreira, me acompanha por aqui que toda semana tem bastante conteúdo para te ajudar.

## Insegurança é normal — desde que não seja constante

Antes de entrar no assunto, um esclarecimento importante, principalmente para quem está começando: insegurança é uma coisa super normal de sentir durante a carreira. Ela aparece em formas e tamanhos diferentes, em todos os níveis, principalmente para devs. Nosso ambiente é muito instável, tem muita coisa nova surgindo todos os dias. Então você vai se sentir inseguro em vários momentos.

O que não pode acontecer é a insegurança ser **constante**. Você não pode trabalhar todos os dias, semanas e meses da carreira sentindo insegurança, porque isso sim vai te prejudicar. São coisas que aparecem no caminho; você aprende a lidar, supera, e aí vêm novas inseguranças.

O foco de hoje são as inseguranças na hora de **entregar o código, entregar as tarefas**: fazer o código funcionar, cumprir aquilo que ele precisa cumprir. Não vou abordar inseguranças técnicas (isso é tema de outro vídeo). No começo da carreira você tem vários pontos de insegurança técnica; como pleno também; como sênior também aparece com frequência. Mas hoje é sobre cumprir tarefas.

## "Funcionar" é relativo

O termo "funcionar" é relativo — não no sentido de que certo e errado dependam do contexto, mas pela diferença entre o que **o dev** enxerga como código que funciona e o que **o usuário** enxerga como sistema que funciona.

Ao longo da carreira aprendemos que sistema que funciona é aquele que não fica dando exception, não trava, não cai em produção, e quando o usuário aperta os botões aparece uma mensagem de sucesso — ou seja, chegou até o final e fez o que deveria. Na nossa cabeça, isso é "funcionar".

Do ponto de vista do usuário, **funcionar é resolver problemas**. Ele usa um software porque tem um problema e o software resolve. Se não resolve, ele simplesmente não usa e troca de software — como você faz quando procura um app de finanças e o que achou não atende.

E, para o usuário, não dar exception, não travar, não mostrar erro genérico é **óbvio e natural**. Você não espera que o celular (Android ou iPhone) trave enquanto usa, nem que um jogo online dê crash e você perca tudo. Seria um absurdo. O software que você entrega é a mesma coisa: ele nem usaria "essa porcaria" se não funcionasse assim.

Para nós, devs, isso não é tão óbvio: quando entregamos código, pensamos em não dar exception, chegar até o final e mostrar mensagem de sucesso. Esse pensamento está encrustado porque foi o que aprendemos desde o início — talvez seja um conceito bom para estudar, mas não para trabalhar com programação. Essa diferença entre o que aprendemos e o que o usuário considera um software bom gera conflito. No trabalho, você leva bronca ("chinelada"), dizem que você entrega coisa errada. **São essas chineladas do dia a dia que geram a insegurança.**

Funcionava muito bem na faculdade e nos projetos pessoais; num ambiente corporativo, no mundo real, quando você é a pessoa por trás do software, não funciona exatamente assim. Levamos pancada e ficamos inseguros ("será que estou fazendo direito?"), e ficamos tão focados no medo da próxima chinelada que não procuramos os meios corretos de superar a insegurança.

Essa insegurança — "será que estou entregando algo bom, será que vão gostar do meu trabalho?" — atinge júnior, pleno e sênior, porque ninguém aprende a trabalhar da forma correta: só é ensinado a entregar e a achar que software que funciona é o que não dá exception. Os mecanismos a seguir ajudam a superar isso.

## Dica 1 — Antes de abrir o editor, descubra o que é o certo

Desde o começo aprendemos a **seguir ordens**. Na faculdade e nos cursos: "faça o que o usuário pede; ele sabe o que precisa". Ao chegar na empresa, passam um bug para corrigir: "isso está errado, corrige desse jeito; o sistema faz assim, mas deveria fazer assado". Você só traduz a ordem em código.

A segunda coisa que aprendemos é **reclamar**: que o usuário não sabe pedir, muda de ideia toda hora, pede uma coisa e depois diz que está tudo errado. "Foi você que pediu assim, eu só fiz o que você pediu." Ficamos presos nesse ciclo de "as pessoas têm que me dizer exatamente como fazer para eu fazer meu trabalho direito".

No final quem sofre é você, que entrega e fica pensando "será que está certo mesmo?... deve estar, acho que tudo bem". Às vezes é até excesso de confiança: "isso aqui está certo", vai para produção, está tudo bugado, porque você não sabe o que é certo. Aí vem a chinelada e a bronca, que alimentam a insegurança.

Talvez por isso glorifiquemos tanto o arquiteto (que diz como fazer) e os papéis executivos de tech (coordenador, gerente): não queremos só executar, queremos dizer o que executar. O autor não critica os modelos de empresa — faz parte do jogo — mas quer que se entenda como isso vira bloqueio. Uma mudança de olhar muitas vezes melhora mais a carreira do que 300 cursos, promoção ou virar chefe.

Se você só escuta e obedece, sem questionar nem querer o porquê, como vai entregar algo que funciona sem saber como deve funcionar? E ainda tem o conforto de culpar quem pediu se estiver errado. O dev fica na base da cadeia alimentar e é quem sofre.

### O que é "o certo"

"O certo" não é opinião nem verdade absoluta do universo (como pessoas veem cores diferentes numa loja de tintas, cada um tem experiências diferentes). **O certo, no nosso trabalho de dev, é um combinado**: a convergência entre o que o usuário precisa e o que você, dev, entendeu que precisa ser feito. Se está combinado, está certo.

Analogia do **arquiteto/decorador**: ele pergunta do que você gosta, porque quem vai morar na casa é você. Mas se só perguntar e depois entregar tudo pronto, grande chance de você dizer "não era isso que eu imaginava". Faltou combinar: desenhar, mostrar como fica, materializar o que foi falado. No software é igual: sentamos para ler requisito, tirar dúvida, e no final o usuário espera enquanto você escreve o que **você** entendeu. Ou até se combinou, mas só falando; no dia da entrega, ele imaginava uma coisa e você fez outra. Isso não significa que o que você fez esteja errado — só não combina com o que o usuário precisa.

Se você combina com o usuário, nunca tem problema. A clareza sobre o que fazer traz confiança e segurança: você olha e diz "é isso aqui que é para fazer?" — "é" — e executa. Mesmo que o usuário diga depois "não era bem isso", vocês combinaram; ele entende o ponto.

### Como descobrir o certo e fazer o combinado

1. **Seja curioso** sobre o que você entrega — requisito de negócio, de arquitetura, de segurança. Entenda os porquês e os para quês. Muita gente na empresa faz "biquinho" quando você pergunta ("só faz logo"); vai haver resistência, mas não se importe: quanto mais clareza, melhor o trabalho. Largue o hábito de seguir ordens puramente. "Isso é problema de segurança" — por quê? "O software tem que funcionar assim" — por quê? Pergunte, fale com o usuário, tire as dúvidas, **não obedeça cegamente**.
2. **Faça o combinado e formalize.** Sente com o usuário formalmente: "temos que fazer isso e aquilo". Se precisar, **desenhe** (num papel de pão; se for remoto, desenhe no papel e mostre na câmera ou tire foto e mande por mensagem/e-mail). A combinação precisa ser formalizada: **não faça as coisas na empresa no boca a boca**. É um dos grandes erros do dev iniciante, que acha que pode confiar em todo mundo em todas as situações. Infelizmente, se algo der errado e a pessoa puder tirar o dela da reta, ela vai tirar e colocar você na frente — amigo, chefe ou subordinado, porque todo mundo quer proteger o emprego, e isso faz parte do jogo. Formalização não se aprende na faculdade nem em curso; aprende-se tomando pancada. A dica vale também para relações pessoais (namorado/a, cônjuge, filhos, pais, parceiros comerciais). "Combinar o que é o certo e formalizar" faz diferença no trabalho e na vida.

## Dica 2 — Crie o hábito de testar suas entregas

"De novo você vai falar de teste?" — Falo porque a galera não testa. Recebo muitas dúvidas sobre teste justamente porque as pessoas não fazem. Na correria e nos atrasos, **a primeira coisa que se deixa de lado é o teste**. Isso mostra que, na prática, não é importante para nós: se fosse, você poderia deixar de entregar, mas não deixaria de testar. (Não é crítica; o autor entende o lado do dev.)

Por que não testamos: teste é chato, repetitivo (altera código, repete o teste); automatizar é difícil — o código é uma "desgraça" que não dá para testar unitariamente; aí tenta teste funcional com Selenium, Cypress ou Playwright, não anda, é complicado, e acaba deixado de lado.

Grande motivo: **devs não aprendem a testar**. Cursos, faculdades e escolas ensinam a escrever código; ninguém ensina a testar de verdade. "Testar" virou apertar botão, cadastrar, consultar, preencher campo, ver se aparece mensagem — assistir ao sistema. (Até num curso de Arduino, a pessoa liga o código na plaquinha e vê o que acontece.) Compare: piloto de avião aprende num simulador, não voando; ninguém dá um carro a quem não sabe dirigir. Por que fazemos isso ao aprender a programar?

**Testar de verdade é validar o que é o certo** — verificar se está certo ou não. Como testar sem saber o que é o certo? Por isso a Dica 1 vem primeiro.

### O efeito sobre a insegurança

Quando você executa seu teste e vê que acontece o que você espera (o certo), **a insegurança evapora**. É uma sensação indescritível entregar pensando "já testei tudo que precisava". Não é que vá acertar 100% das vezes — você vai deixar de testar coisas. Mas quando nunca testa, sempre deixa de testar alguma coisa. Se chegar em produção e der problema, você olha seus testes e diz: "testei, mas **essa situação específica eu não testei**" — e basta incluir esse cenário. Sabe que fez tudo ao seu alcance e aquilo escapou. Isso muda o jeito como você trabalha.

### Como criar o hábito

1. **Descubra o que é o certo** (sem isso, não existe teste; o autor passou ~13 anos "rateando" com testes porque não sabia o que era o certo, e fazia "testes idiotas, testes inúteis").
2. **Escreva roteiros / um plano de testes** com o passo a passo (como o manual de um eletrônico: aperte o botão X, veja se a luz Y acendeu). Sem roteiro, quando bate a pressa ou a preguiça você faz meio teste e solta, pensando "isso aqui está tudo certo". Com roteiro, você só segue o que está escrito; escreve uma vez e executa depois. Pode ser cansativo (teste manual repetido), mas dá a segurança de ter uma **prova** de que o código faz o certo. Se aparecer um caso que você não testou, ele entra no plano.
3. **Execute o plano.** Parece idiota, mas se você só fala que testar é importante e não testa, então não é importante. Manual ou automatizado, do jeito que for — comece, para desenvolver o hábito. Senão você fica no zero.

## Dica 3 — Faça escolhas conscientes

O mundo real nas empresas é muito diferente de livros, cursos e faculdade (que têm foco didático; colocar o caos do dia a dia atrapalharia o ensino). No mundo real: o projeto atrasa, o requisito muda toda hora, você mexe em código ruim, legado, sistema velho, tem restrições que impedem usar certas tecnologias. É assim em praticamente todas as empresas (o desafio nos comentários: "minha empresa não tem isso" é uma grande exceção).

O problema: quando aperta, a maioria **escolhe a pressa** ("entrega logo, depois a gente arruma"). Faz parte do jogo — a pressa é uma forma de aprender a lidar, mas também é a opção mais fácil: encher o sistema de gambiarra, sem gastar tempo pensando. **Pressa gera gambiarra; gambiarra gera problema; problema gera insegurança**: quando dá problema em produção você toma chinelada — às vezes nem foi você quem fez, mas "a bomba estoura na sua mão" ("agora você é o dono do sistema, por que não arrumou?"). Daí vem o receio de colocar software em produção e a agonia de não conseguir fazer as coisas. A insegurança de hoje pode ter sido causada pela pressa de ontem.

### Como fazer escolhas conscientes

1. **Esteja por dentro do contexto.** Peça informação: se você sabe o que é crítico e o que é urgente, toma decisões melhores. Quem vive na própria bolha esperando a próxima "chicotadinha" sempre escolhe a pressa e alimenta a gambiarra. Não precisa participar de todas as reuniões (isso é papel de gerente/gestor), mas saber "como a banda está tocando": onde está pegando, por que é urgente, por que não é. Não fique só seguindo ordens; pergunte.
2. **Aceite o cenário em vez de combatê-lo** (erro comum de sêniores e alguns plenos): ver a urgência e ficar brigando — "devíamos mudar a forma de fazer, mudar o cronograma, usar tal coisa". Você pode fazer zilhões de coisas, mas no momento atual não dá mais. Aceitar **não é abaixar a cabeça**; é entender o porquê. Às vezes você vai tomar decisões ruins por causa do contexto (escolher a pressa) e tudo bem, **desde que seja uma decisão consciente**: saber que fazer a gambiarra em vez de corrigi-la pode gerar problema no futuro.
3. **Reporte o risco.** Se você sabe que pode dar problema e não tem poder de mudar, diga: "podemos fazer assim, mas talvez dê problema depois". Você tirou o problema do seu ombro e o dividiu com todos; se der problema, "lembra que eu comentei? Agora é hora de arrumar" — ninguém consegue te bater porque já sabia. Comunicação e entendimento fora da esfera dev tornam as decisões conscientes.
4. **Melhore na próxima.** Faça o melhor com o tempo que tem; se não tem tempo, faz do jeito que dá. Mas se **toda vez** é só "do jeito que dá", você roda em círculos. Ative o outro lado: "eu entendo e aceito, mas não fico alheio — o que podemos mudar na próxima entrega para que isso não aconteça de novo?". **A pior coisa é cometer o mesmo erro duas vezes.** Isso fortalece a confiança: você antecipa o problema, ataca antes que aconteça e, se não conseguir arrumar, já sabia e divulgou. Você não tem insegurança de entregar algo "não tão bom" porque antecipou e dividiu. Isso é trabalhar com programação: fazer o organismo como um todo funcionar para entregar o que precisa **e melhorar as próximas entregas**.

## Conclusão

A insegurança vem da **falta de clareza**. Toda vez que você pega uma demanda, sai fazendo e se sente perdido (não sabe direito o que fazer, como começar ou como termina) é falta de clareza. Você foca muito no **como** (linguagem, tecnologia, comando, ferramenta) e não no **o quê**, no **porquê** e, tão importante quanto, no **quando**. Aprendemos desde o começo que é para entregar código, buildar, subir em produção — e perdemos de vista o que importa. O "como" importa, mas não adianta fazer sem saber para quê. Isso gera insegurança e a dúvida se está certo ou não.

Para ganhar clareza (entender o certo, criar o hábito de testar, tomar decisões conscientes) existem técnicas em **análise de requisitos, testes unitários e conceitos de arquitetura de software**. Parece básico e você provavelmente já ouviu falar, mas provavelmente não coloca em prática: consumimos conteúdo e, no dia a dia, esquecemos, não achamos brecha ou não conseguimos aplicar.

O autor indica seu curso online (link na descrição, "Dev que Resolve"), que dá base em análise de requisitos, teste, arquitetura e mais. Encerramento padrão: curta o vídeo, comente o que ajudou você a ter menos insegurança no trabalho e inscreva-se no canal.
