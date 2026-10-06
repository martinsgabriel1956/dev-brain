# Senioridade não é só técnica: especialização, negócio, dados e confiança em crise

Fonte: transcrição de vídeo, colada pelo usuário em 2026-10-06. Já em português — sem tradução. Autor: não identificado (o locutor cita um vídeo anterior sobre a visão de IA do Uncle Bob vs. a de Linus Torvalds e relata experiência em consultoria, arquitetura, escalabilidade e observabilidade; nome não aparece). Adicionados apenas pontuação, parágrafos e títulos; erros de reconhecimento corrigidos por contexto.

Termos corrigidos (reconhecimento automático): "Linux" (ao falar da visão de IA) → Linus (Torvalds), provável; "Crude" → CRUD; "sior / primeiro sior" → sênior; "Bassen" → Basileia/Basel (provável; regulação bancária); "Atomic" → Datomic (provável; ferramenta usada pelo Nubank); "Nube" → Nubank; "a hora do negócio" → área de negócio; "delega pro pi" → "delega pra IA" (provável, não confirmado); "deves" → devs; "tradita impacto" → trecho ininteligível, mantido como [trecho incerto]; "Joel" (no meio do vídeo) mantido como no áudio — pode ser nome do locutor ou de um espectador hipotético, não confirmado.

---

## Abertura: o vídeo anterior e a ideia de "senior em quê?"

No vídeo passado o autor falou sobre como o Uncle Bob tem uma visão sobre IA moldada pela carreira dele, e como isso difere da visão de Linus Torvalds. Hoje quer entrar mais na carreira, porque a percepção de como o dev funciona talvez não fique clara para todos: o dev pode escrever código da mesma maneira, mas as **características do que ele desenvolve mudam totalmente a percepção dele sobre várias coisas**.

Hoje o dev que faz CRUD, o programador web, é (na percepção do autor sobre o mercado) a esmagadora maioria — mas isso não quer dizer que só existem esses programadores. O dev pode se tornar muitas coisas ao longo da carreira; não é só uma jornada de júnior a sênior. **Sênior em quê? No que esse cara está se tornando sênior?** Isso é o que ele quer discutir.

## Uncle Bob vs. Linus: perto do dia a dia web vs. perto do processador

Depois que o Uncle Bob começou a falar de TDD e afins, o foco dele foi muito o dia a dia do dev. A visão de Linus mostra algo que a maioria dos devs não vê e que pode ser um caminho de carreira: ele trabalha muito mais perto do **processador e do sistema operacional**, onde rodam inclusive os sistemas web. É um mundo de conhecimento que a maioria dos devs não acessa, porque não é comum hoje um dev falar ou entender de threads ou de Bluetooth.

"Entender" não é usar uma biblioteca — até em JavaScript há bibliotecas prontas para Bluetooth. É saber, por exemplo, **como se desenvolve um driver** para isso. No baixo nível, **recurso é uma coisa extremamente escassa que você controla o tempo todo**, e isso muda totalmente como você programa e pensa. Na programação web não é que não haja preocupação com isso, mas o nível é muito mais baixo.

## Quem sabe baixo nível é mais sênior? Não necessariamente: o especialista de negócio

Saber isso não torna o cara automaticamente mais sênior. Há muito sênior que vira **especialista do negócio ou de uma área específica**: fica em volta da programação, mas o conhecimento dele é valorizado dentro da empresa de outras formas. O autor conhece devs seniores com salário alto que detêm muito conhecimento de negócio: programam (botam a mão na massa) e também conhecem o negócio. Há desenvolvedores especialistas em **mercado financeiro, mercado portuário, logística, saúde**.

Em áreas muito reguladas, conforme o dev entra, ganha um conhecimento notório. Exemplo: poucos devs conhecem bem como funcionam as **implementações de Basileia para o mercado financeiro**; empresas olham de forma diferente para quem conhece. Para quem está começando isso não fica claro, mas conforme se amadurece a visão de negócio da área, dá para ser **muito bem reconhecido e remunerado por isso**.

Perguntam muito sobre diferenciais de carreira: "fale inglês, fale bem" são válidos (abordado em vários vídeos), mas **conhecimento de negócio também pode ser um baita diferencial**. Ser especialista numa área pode fechar algumas oportunidades, mas nas oportunidades em que você se encaixa, você se encaixa muito melhor.

## Mudanças na empresa: o exemplo do Nubank virando banco

Mudanças na vida da empresa podem exigir trocar a equipe inteira; isso não é maldade, é necessidade. Exemplo do autor: o **Nubank**, até hoje (segundo o autor), não é formalmente um banco — é uma mescla; pode trabalhar com dinheiro, mas não é um banco. Isso permite muita **inovação**, liberdade do time para criar ferramentas e experimentar. Em 2015/2016 havia muitas palestras do pessoal do Nubank sobre **Datomic** (na época poucos sabiam o que era), usado em produção.

Agora o Nubank caminha para virar banco. Quando virar, essa parte fica **muito mais restrita**: mais regras, que impactam as ferramentas que pode usar e o processo do dia a dia. O viés de inovação não morre, mas tende a ficar de lado e a ficar mais "chato".

## A realidade dos grandes bancos

Sem citar nomes, o autor conhece alguns grandes bancos por dentro e diz que **é terrível** em alguns aspectos: difícil acessar uma ferramenta de e-mail; difícil acessar uma IA que não seja do banco, e as que existem dentro do banco são extremamente capadas; muitas vezes se trabalha com máquina virtual remota que cai e perde conexão. Ressalva: não são todos assim, mas é comum nos "bancões".

## Régua de carreira em banco: pagar menos no começo, reter depois

Um grande banco no Brasil não paga muito bem, apesar de gigante, mas tem **programa de formação e régua de carreira muito bem definida, com planos agressivos**. Não é bondade: conforme a pessoa cresce lá dentro, ganha muito conhecimento de como funciona um banco — algo extremamente complexo — e constrói carreira forte, ganhando muito bem depois de alguns anos. **O banco não quer te perder**, porque provavelmente logo você vira tomador de decisão. Um dos caminhos é virar líder; mas muita gente que não quer liderança vira **especialista em uma determinada área de negócio**, e o foco é esse. Há vários caminhos que não dependem só de tecnologia.

## Dados: cientista, engenheiro e mais subdivisões

O mesmo vale para quem trabalha com dados: hoje há tanta divisão porque se trabalha com muito dado que nasceram classificações diferentes. **Cientista de dados e engenheiro de dados são coisas muito diferentes** (há vídeo no canal sobre isso), e mesmo dentro de cada ramo há subdivisões.

- **Cientista de dados:** difícil chegar lá sem saber muito de **estatística e matemática** ("achando que programação não precisa de matemática" — há cenários em que precisa e muito). Um bom cientista também é **muito criativo e detém conhecimento do negócio**; se não conhece a área, precisa ser muito **questionador**, entender como a empresa funciona e para onde está construindo o modelo — senão a chance de o modelo não ser assertivo é alta. Quanto mais ele tem o ímpeto de entender a fundo, melhores os modelos; não é só saber estatística.
- **Engenheiro de dados (viés técnico/engenharia):** como acessar dado muito rápido, como montar uma estrutura que serve dados muito rápido, com **alta disponibilidade**, atende muita gente, permite extração em logística sem cair tudo e sem ficar extremamente caro. "É outra cabeça, outra necessidade, outro tipo de inteligência."

Ele poderia fazer vários vídeos sobre isso: a área é muito maior, com muito mais entradas e percepções.

## A experiência do autor: confiança como skill em situações de crise

O autor diz ser muito bom tecnicamente em **arquitetura, escalabilidade, monitoramento e observabilidade**, mas o que teve impacto grande na carreira foi **falar bem e conseguir entender as pessoas** [trecho incerto no áudio: "gosto de lá entrar no nível da tradita impacto na minha carreira eu falar bem"]. Já falou em vídeos sobre filosofia e comunicação.

Entrava em **operações críticas**, em situações em que "todo mundo já estava arrancando os cabelos". Como trabalhou muito tempo em **consultoria**, entrava no meio de times em crise, chamado para atender. Na visão dele, a primeira coisa **não** era ter só bom conhecimento técnico: era **entender o que aquele time está passando**. Numa "vibe impositiva" — questionar todo mundo, achar que ninguém sabe o que faz, ser grosseiro — o time não deixa você trabalhar e te vê como **ameaça**, não como alguém em quem confiar.

A habilidade de entrar e fazer as pessoas **confiarem nele e o enxergarem como parceiro**, não como crítico ou ofensor, foi crucial para o sucesso. Por mais conhecimento técnico que tivesse, **quem sabe por que decisões corretas ou erradas foram tomadas são essas pessoas**; ao ganhar a confiança delas (e por consequência bons amigos até hoje), ganhou destaque: consegue **entrar em crise sem piorá-la**.

O problema nunca é só restabelecer o sistema: é **readaptar, reconquistar e fazer o time recuperar o nível de confiança**, terminando a situação resolvida **com lições aprendidas**. Isso é difícil: é preciso ter um plano, garantir que todos estejam alinhados e "comprados" nele. Até traçar o plano, ter visão clara do que fazer para voltar ao normal e executar, há pressão de diretoria, pessoas pensando em desistir dos cargos, estressadas e cansadas; **é preciso manter todo mundo unido, acreditando no que está sendo construído** até a execução gerar resultado. Foi uma skill que fez muita diferença na carreira dele e que talvez precise ser desenvolvida por quem assiste.

## Fechamento

Foi um vídeo para "soltar" a ideia: começou falando da perspectiva Linus vs. Uncle Bob, e não é difícil perceber por que pessoas tão relevantes, que geraram tanto impacto, têm visões diferentes — **os dois estão certos por causa da diversidade que a nossa área tem**. Pede nos comentários se o espectador tem ou não essa percepção.
