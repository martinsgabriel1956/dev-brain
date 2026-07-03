# O mercado não precisa de mais programadores (precisa de engenheiros de software)

Transcrição de vídeo. Fala meu povo, tudo bem? Hoje eu quero falar para vocês porque o mercado não precisa de mais programadores, e eu vou te explicar porquê. A versão resumida é: o mercado precisa de engenheiros de software, ainda mais agora com a inteligência artificial.

Quero falar sobre isso hoje porque a maioria dos desenvolvedores não sabe essa diferença. E se você por acaso é um desses que tem "engenheiro de software" no seu LinkedIn, só quero te lembrar de uma coisa: título no LinkedIn não muda mentalidade. Para ser um engenheiro de software você precisa mudar a sua mentalidade. Talvez você até já tenha isso, mas para aqueles que me mandam mensagem perguntando como ser um engenheiro, o que é estudar a base, o que é esse conceito que eu tô vendendo — já tem alguns vídeos aqui, mas quero trazer uma visão mais aprofundada. Se você tá no início da carreira ou tem anos mas tá se sentindo estagnado, fica comigo até o final que eu quero te explicar como fazer essa transição.

## Programador vs. engenheiro

É bem claro hoje em dia que o programador transforma requisitos em código. Ele recebe um problema já mastigado, faz um CRUD de usuários, integra com uma API, corrige um bug. É uma habilidade valiosa, com certeza — mas é uma **habilidade de execução**. Ele opera dentro de um espaço que outra pessoa definiu. Não que isso seja necessariamente um problema, mas é importante entender que é uma habilidade de execução.

O engenheiro de software opera um nível acima. É o cara que questiona se o problema tá bem formulado antes de sair codando. Coisas do tipo: por que estamos construindo isso? Qual o resultado esperado do negócio? Quais são as restrições reais que a gente tem — tempo, escala, dinheiro, equipe? Quais decisões de hoje vão nos prender amanhã? Isso tem a ver com senioridade, mas principalmente com **mentalidade**.

### A analogia da construção civil

Na construção civil, o pedreiro é o cara que executa: levanta a parede, assenta o tijolo, segue a planta. Ele é essencial, o prédio não sobe sem ele. O engenheiro civil decide onde o prédio vai ficar, calcula a fundação conforme o tipo de solo, projeta a estrutura para aguentar vento e terremoto, define materiais certos para o orçamento disponível.

Se o pedreiro erra, você troca alguns tijolos. Se o engenheiro erra, o prédio cai.

No software é a mesma coisa. Se o programador erra, você refatora. Se o engenheiro toma uma decisão arquitetural errada, você joga fora meses de trabalho — e pior, convive com aquela dívida técnica por anos.

## O paradoxo da IA

A inteligência artificial está comoditizando a execução. Copilot, Cursor, Claude — já escrevem código funcional a partir de uma descrição, e vão ficar cada vez melhores. Muita gente discute isso: "ah, eles ainda vão ficar melhores". Sim, em gerar código — e isso não é o trabalho da engenharia de software.

O trabalho de transformar requisito claro em código funcional, que é o trabalho clássico do programador, é exatamente o tipo de tarefa que a IA faz cada vez melhor — não perfeitamente, mas bem o suficiente para mudar a equação econômica. Já o trabalho do engenheiro — entender se o requisito faz sentido, decidir arquitetura, avaliar trade-offs, governar a complexidade do sistema como um todo — a IA não faz, porque exige contexto, julgamento sobre incerteza e responsabilidade sobre as consequências.

Aqui existe um paradoxo: **quanto mais a IA gera código, mais a gente precisa de engenheiros para governar esse código**. Sem governança, a IA gerando código é como dar uma metralhadora para quem não sabe mirar.

A IA vai tomar o emprego do desenvolvedor que só permanece na camada de execução, que não evolui para a camada de engenharia — porque a IA vai criar mais demanda para o engenheiro que pensa, decide e governa. Isso não é uma verdade universal — depende muito do caso, da linguagem, de quão antigo é o projeto — mas a necessidade de novos engenheiros vai ser crescente nos próximos anos.

## O que estudar (não qual tecnologia aprender)

Uma coisa é perguntar "o que devo estudar", outra é perguntar "qual tecnologia devo aprender". Esses dois conceitos não se misturam. Tem muito roadmap de estudo por aí, tipo roadmap.sh, com diagramas gigantes cheios de caixinhas: React, Kubernetes, Docker, Terraform. Achar que ser engenheiro é preencher todas essas caixinhas é mentalidade de programador — é colecionar ferramentas.

Saber várias ferramentas é legal, mas não pode ser seu foco principal. Ferramentas contribuem para a carreira, mas não são a carreira. **O engenheiro de software não coleciona ferramentas, coleciona modelos mentais.** Ferramentas podem mudar a cada 3 anos — o React de hoje é o jQuery de ontem, o Kubernetes de hoje pode ser outra ferramenta amanhã. Mas os fundamentos não mudam. São os fundamentos que permitem aprender qualquer tecnologia nova em semanas, porque você entende o porquê por trás do como.

O roadmap de fundamentos se divide em dois eixos: profundidade técnica (vertical) e o que coloca você na mesa de decisão (horizontal).

### Eixo vertical — profundidade técnica

**Estrutura de dados e algoritmos.** Vale a pena não só para passar entrevista técnica, mas para entender por que o sistema ficou lento quando passou de 1.000 para 100.000 usuários, ou por que a escolha entre uma lista e uma tabela hash pode ser a diferença entre 50ms e 5 segundos de resposta. Quando você entende complexidade de algoritmos, para de chutar e começa a prever — isso é engenharia. Livro: *Introduction to Algorithms* (Cormen) — não precisa ler inteiro, mas os capítulos sobre complexidade, árvores, grafos e tabelas hash são essenciais. É livro de cabeceira, para consultar ao longo dos anos.

**Arquitetura de software.** Como sistemas são estruturados. Importa porque certas decisões escalam e outras criam bola de neve de problemas. Não existe arquitetura boa para tudo — existe arquitetura certa para o contexto certo. Livros: *Clean Architecture* (Robert Martin) para princípios; *Fundamentals of Software Architecture* (Mark Richards / Neal Ford) para trade-offs de verdade; *Designing Data-Intensive Applications* (Martin Kleppmann) — este separa o júnior do sênior quando o assunto é sistemas distribuídos.

**Design de software e modelagem de domínio.** O objetivo é traduzir um problema do mundo real para código que faz sentido. Não é decorar padrões clássicos (Singleton, Factory, Observer) — isso é como aprender jogadas de xadrez sem saber conectá-las numa estratégia vencedora. O que importa é saber modelar o domínio de negócio, a forma como o código conta a história do problema. Livros: *Domain-Driven Design* (Eric Evans) — denso e desafiador, mas transformador; *A Philosophy of Software Design* (John Ousterhout) — mais curto e direto.

**Sistemas operacionais e redes.** Não precisa ser especialista em kernel do Linux, mas precisa entender o que acontece entre a chamada de rede do seu código e a resposta chegar na tela: TCP/IP, DNS, como o HTTP opera, processos e threads, gerenciamento de memória. Quando o sistema quebra em produção — e ele vai quebrar — o bug provavelmente está na interação entre o código e a infraestrutura. Sem entender essa camada, você fica cego.

**Banco de dados.** A maioria dos devs sêniores entende muito pouco disso, talvez porque hoje em dia se terceiriza a responsabilidade para o ORM. Mas é preciso se preocupar com modelagem relacional, índices, planos de execução de query, a tensão entre consistência e disponibilidade, quando usar banco relacional vs. não relacional. A maioria dos problemas de performance em produção mora no banco de dados. A maioria dos desenvolvedores trata o banco como caixa preta mágica: manda os dados, reza, torce para voltar rápido. Engenheiro não reza, engenheiro entende.

### Eixo horizontal — o que coloca você na mesa de decisão

Não são habilidades técnicas no sentido clássico, mas são o que separa o engenheiro que fica no canto codando do engenheiro que senta na mesa onde as decisões acontecem.

**Comunicação técnica.** Saber escrever um documento de decisão arquitetural (ADR), fazer uma análise pós-incidente que realmente previne o próximo problema, explicar para um diretor não técnico por que um trabalho de refatoração de três sprints vai economizar seis meses depois. O engenheiro que não se comunica bem é invisível — nunca vai ser CTO ou diretor de tecnologia, porque toma decisões que ninguém entende, valoriza ou defende sob pressão de prazo.

**Noções de produto e negócio.** Não precisa virar gerente de produto, mas precisa entender métricas de negócio, como o software gera valor, o que é custo de oportunidade. Quando você entende que cada sprint tem um custo real em reais, suas decisões técnicas mudam completamente. Livros: *The Lean Startup* (Eric Ries) — como os ciclos de valor funcionam; *Inspired* (Marty Cagan) — como a área de produto pensa.

**Gestão de complexidade.** Livro: *The Mythical Man-Month* (Frederick Brooks, 1975) — não é sobre gestão de projetos, é sobre por que software é difícil e como lidar com isso. O ponto central é a separação entre **complexidade essencial** e **complexidade acidental** (a dificuldade que você mesmo criou com suas escolhas de tecnologia, arquitetura e processo). O programador lida com complexidade acidental o dia inteiro — configurando ferramenta, lutando com framework, resolvendo conflito de dependência. O engenheiro foca na complexidade essencial: entender o problema de verdade e tomar decisões que minimizam a complexidade acidental.

**Pensamento em produção.** O programador comemora quando o código compila e o teste passa. O engenheiro comemora quando o sistema sobrevive ao pico da Black Friday. Pensar em produção significa se preocupar com observabilidade (logs, métricas, rastreamento de requisições), definir indicadores de qualidade de serviço, ter um plano para quando as coisas derem errado. O código escrito é 10% do trabalho — os outros 90% são ele rodando em produção, com usuários reais, em condições que você não previu.

## Como estudar isso

Essa meia dúzia de temas e livros pode consumir anos da sua vida — são coisas que você vai amadurecendo, não é algo que se aprende de uma vez. Pegue os tópicos e comece a estudar aos poucos.

Para quem tá no comecinho, sistemas operacionais, redes, TCP/IP e DNS é uma boa parte para começar — os frameworks e linguagens que você vai estudar usam esses conceitos como base. Depois de aprender uma ou duas linguagens, alguns frameworks e redes, os fundamentos de engenharia de software (arquitetura, design) começam a fazer mais sentido.

Não é um tipo de estudo linear — são conceitos que você vai revisitar ao longo de toda a carreira, sempre que precisar tomar uma decisão. Os livros citados não são baratos (o de algoritmos, por exemplo, custa uns R$ 400), mas são de altíssima qualidade.

A diferença entre um programador e um engenheiro não é o título do LinkedIn, não é o salário, não são os anos de experiência — é o que você escolhe estudar. Dá para chegar a dev sênior sem estudar 95% do que foi falado aqui. Mas para ir além — vagas de tech lead em diante — esse conhecimento começa a fazer muita diferença. Se você só estuda a ferramenta da moda, está apostando que ela vai durar. Se estuda os fundamentos dos dois eixos, está apostando em você mesmo — e essa é uma aposta que você nunca vai perder.

Pegue um desses fundamentos que mais faz sentido pra sua carreira agora e comece por ele: uma hora por dia, um capítulo por semana. Em seis meses você vai olhar para trás e não vai acreditar na diferença.
