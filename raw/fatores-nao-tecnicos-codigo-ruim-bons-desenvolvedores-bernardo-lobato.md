# Fatores Não Técnicos que Explicam Código Ruim de Bons Desenvolvedores

Se você pegar um dev muito bom, ainda iniciante, e colocar em um projeto, provavelmente não vai saber o melhor código do mundo de primeira, concorda? Mas se eu te disser que bons desenvolvedores também escrevem código ruim — não por falta de conhecimento, não por não saber programar — muitas vezes não é isso, e é isso que a gente vai mostrar aqui no vídeo de hoje. Então já abre o seu backlog com as tarefas que deveriam ter sido feitas há três meses atrás, que o vídeo já vai começar.

Olá devs, eu sou Bernardo Lobato, e o vídeo de hoje é um pouquinho mais curto, com pouca edição, mais reflexivo — ainda tô me recuperando aqui de alguns problemas pessoais, e pensando nesse material para não deixar o canal parado mais tempo, mas claro, sempre tentando trazer conteúdo relevante para cá. Mas, sem mais delongas: que fatores podem influenciar o julgamento de um código escrito por um profissional experiente?

Me peguei pensando nisso quando vi um grupo de colegas criticando o código de um projeto legado, sendo que eu sabia que os profissionais responsáveis por aquele projeto eram excelentes profissionais. É comum, principalmente em quem ainda não tem uma experiência muito grande com desenvolvimento, ter uma visão parecida com: código ruim é igual a desenvolvedor ruim; arquitetura ruim é igual a arquiteto ruim; muito débito técnico é igual a uma equipe negligente. Mas eu entendo isso como uma simplificação, e uma simplificação grosseira.

Código-fonte, tudo referente ao projeto, não é produzido no vácuo — ele é resultado das condições em que esse desenvolvimento acontece. Como assim, você me pergunta? Eu separei aqui quatro fatores que podem tornar o trabalho de um profissional experiente em uma entrega não tão boa assim, ok? Então vamos passar por esses quatro fatores. Mas antes, eu já peço que deixe seu like, checa a sua inscrição, e se esse tipo de conteúdo é relevante para você eu gostaria de contar com a sua colaboração. Fechado?

## 1. Pressão na entrega de um módulo ou funcionalidade

O primeiro dos fatores que eu queria elencar aqui é a pressão na entrega de um módulo ou uma nova funcionalidade. Você tem uma nova funcionalidade que deveria levar duas semanas para entregar, mas o negócio precisa dela em dois dias. O desenvolvedor experiente sabe que a solução mais próxima do ideal seria outra, mas acaba precisando ceder a esse fator externo: implementa uma solução mais simples, com menos testes, talvez uma abstração ali inadequada, um control-C control-V aqui, outro ali.

Enfim, o que eu quero dizer aqui é que essa pode ser uma decisão completamente racional daquele profissional, dadas as condições que ele tinha para trabalhar. Nesse caso, a solução ideal deveria virar dívida técnica e ser tratada posteriormente com o devido rigor. Mas será que isso sempre acontece?

## 2. Contexto do projeto

O segundo ponto que eu trago aqui é referente ao contexto do projeto. Aquele código, aquela funcionalidade, pode parecer ruim ou mal feita isoladamente, mas dentro de um sistema maior acaba fazendo sentido. Como assim? Explico: por exemplo, código legado, dependências externas, decisões anteriores erradas no projeto, limitação de infraestrutura, contratos com APIs legadas que não podem ser quebradas, etc, etc e etc.

Muitas vezes não se tem todo o controle de todo esse contexto de projeto assim de cara — ainda mais se você for um profissional que trabalha com sustentação, por exemplo, e caiu ali de paraquedas dentro daquele ambiente. Às vezes a gente acaba entregando o que dá para entregar nesse contexto, porque é só aquilo que o sistema permite. Imagine que, para eu entregar uma funcionalidade nova bonitinha do jeito que tem que ser, eu tinha que refatorar o sistema inteiro — e é um sistema legado, sem testes, complicado. Impraticável, não é?

E existe essa armadilha que eu acho que 100% dos devs já caíram: olhar código fora de contexto, comparar aquele código com o código que a gente escreveria se tivesse começando o projeto hoje do zero. E aí, meu amigo, sair dessa armadilha pode ser complicado.

## 3. Conhecimento incompleto e o fator tempo

O terceiro fator que eu quero trazer aqui é o bom e velho conhecimento daquelas tecnologias. Mesmo os bons e excelentes profissionais têm conhecimento incompleto, principalmente quando envolve algo fora da sua área de atuação mais prioritária. E isso é particularmente fácil de acontecer quando você tá trabalhando ali com outra linguagem de programação — por exemplo, profissionais especialistas em uma determinada linguagem podem transportar padrões dessa linguagem, como nomes de variáveis, nomes de métodos, estruturas de classes, que podem soar inadequadas em outras linguagens.

Além disso, eu queria citar aqui também o fator tempo: o mesmo código, se eu mesmo, de 5 anos atrás, pode não ser tão bom, porque você simplesmente não era um desenvolvedor tão bom 5 anos atrás — não conhecia tanto aquela tecnologia e todo aquele ecossistema como conhece hoje. E, ao contrário do que parece, isso pode ser bom de se ver, né — isso demonstra evolução do seu aprendizado, demonstra que você não parou de aprender em todo esse período.

## 4. Incentivos organizacionais

E o quarto e último ponto que eu trago aqui são o que eu estou chamando de incentivos. Se a sua organização recompensa aquele profissional que fecha ticket, cumpre deadline, entrega valor, sem necessariamente avaliar a qualidade daquele trabalho — e ao mesmo tempo também não recompensa redução de complexidade, melhorias contínuas de arquitetura, boa gestão de dívida técnica, melhor cobertura de testes, etc — então, nessa situação, até bons profissionais vão querer otimizar seu trabalho para se adequar àquilo que é medido pela empresa.

Se eu sou avaliado pela quantidade de tarefas que eu entrego, eu naturalmente vou tentar entregar mais tarefas. Se eu sou avaliado também pela redução da complexidade, qualidade de código e sustentabilidade do sistema, minhas decisões aí podem começar a mudar no meu dia a dia como desenvolvedor. Se só a liderança técnica não dá muita importância pra parte técnica do trabalho, é nesse ponto que vamos parar — e no futuro é ter todos aqueles problemas que a gente já conhece, que estudamos aqui no canal quando falamos de problemas de evolução de software através de engenharia de software, tá bom?

## Mas o que fazer, então?

Eu particularmente não acho que seja o caso de normalizar esse tipo de comportamento como algo rotineiro do dev, dizer alguma coisa como: "Ah, então podemos escrever alguma coisa mal escrito porque a culpa é do contexto." Acredito que isso aí já começa a fazer parte do problema, e não da solução.

Acho que aqui o ponto crucial é saber aprender a reconhecer quando a gente tá criando um débito técnico conscientemente, porque sim, existe uma diferença enorme entre assumir uma dívida técnica conscientemente e simplesmente deixar aquilo para ser um problema do futuro. Se possível, descrever esse débito no backlog, e sempre que possível explicar qual o tradeoff que levou aquela decisão — isso é importantíssimo para que a gente possa ter uma gestão desse backlog.

O principal ponto desse material é a gente, na qualidade de bons profissionais, entender que nem sempre temos as condições ideais de desenvolvimento daquele projeto. Entender que um software ruim não é ruim necessariamente porque profissionais ruins trabalharam nele — é entender que existem tradeoffs, e muitos deles não são técnicos, são algo que vem mais de cima. Decisões complicadas já foram tomadas dentro de um projeto que já era complicado.

Mas entender o contexto não significa aceitar qualquer coisa. Quando uma decisão cria uma dívida técnica conscientemente, precisamos torná-la visível, registrar o tradeoff, e, quando houver oportunidade, pagar esse boleto.

Você concorda? Já pegou alguma situação em algum projeto e quis abençoar o dev anterior que colocou a mão naquele código? Conta aqui pra gente nos comentários. Ok, mais uma vez peço o seu like, a sua inscrição, e agradeço sempre a sua audiência. E a gente se vê no próximo vídeo.
