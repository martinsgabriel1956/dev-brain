# O que sobrou pro Dev Júnior? (Eric Wendel)

Transcrição de vídeo em português (fala espontânea, transcrição automática/ASR). Limpo de repetições, cacoetes de fala e pontuação corrigida, mantendo o conteúdo e a estrutura de raciocínio do apresentador. Sem tradução — conteúdo original em português.

**Apresentador:** Eric Wendel — trabalha na área de software desde 2014, atua com educação em tecnologia, tem experiência trabalhando remotamente em inglês para empresas dos Estados Unidos.

## Gancho / pergunta central

O que sobrou pro Dev Júnior? A posição de júnior é realmente substituível por inteligência artificial? E, se pessoas não passarem mais pela etapa de júnior da forma tradicional, como serão os devs seniores e especialistas do futuro?

Eric já havia feito um vídeo anterior sobre "se a IA vai substituir os devs", onde relata ter "caído no hype" e se corrigido depois — esse vídeo é uma continuação dessa reflexão, com mais tópicos.

## Contexto: o clima de apreensão atual

Eric trabalha com educação em tecnologia há bastante tempo e já viu várias "ondas" passarem: a promessa de que todo mundo precisava aprender a programar, o boom dos bootcamps, a explosão dos cursos online, a chegada do low-code/no-code, e agora os agentes de IA.

Ele diz nunca ter visto tanta gente preocupada com o futuro de quem está começando como agora — inclusive entre profissionais de educação em tecnologia, que estão inseguros sobre qual será a nova forma de iniciantes aprenderem (vídeo? blog post? exercícios?).

Sintoma do problema: ferramentas de chat de IA entregam respostas mais rápido do que a pessoa consegue formular a pergunta, criando a ilusão de que "qualquer pessoa pode ser programadora sem o mínimo de esforço ou especialidade — está tudo a um prompt de distância". Circulam afirmações de que não há mais necessidade de contratar devs iniciantes, que uma pessoa de produto os substituiria, ou que não vale mais a pena estudar código porque virou "banal".

## Por que o medo é compreensível, mas a conclusão está errada

Eric reconhece a origem do medo: se a IA consegue gerar código, criar telas, explicar erros, escrever SQL, subir arquitetura e montar um CRUD completo, parece natural concluir que empresas não precisariam mais contratar alguém iniciante. Ele discorda dessa conclusão — a área não morreu, ela mudou, e tecnologia é uma área que muda o tempo inteiro; adaptação é requisito, não exceção.

A pergunta certa, para ele, não é "o que sobrou pro Dev Júnior" e sim "o que mudou na forma de começar".

## Comparação: como as grades curriculares mudaram

Eric usa os dois irmãos, que começaram a estudar programação neste ano, como ponto de comparação direta com sua própria trajetória (início por volta de 2014).

### Como Eric aprendeu (grade "tradicional")

- Caminho: algoritmos, estrutura de dados, C, C++, Java, PHP, terminal, muita teoria e abstração.
- Estudava história da computação, modelagem de banco de dados com SQL, lógica booleana, matrizes, ponteiros, listas, filas, pilhas, engenharia/gestão de software.
- Demorava muito para entender como aquilo se conectava ao mundo real — queria saber como se faz um site, como uma tela conversa com uma API.
- Só via a construção de um sistema real e completo lá pelo segundo ano da faculdade.
- Resultado: grande quebra de expectativa. Na disciplina de algoritmos e estrutura de dados, cerca de 80% das pessoas desistiam do curso, por acharem difícil demais ou por não verem aplicação prática imediata.
- Eric encontrou um caminho alternativo: fez um curso à parte (formação em C#/ASP), sem esperar pela faculdade, inspirado por outro estudante que conseguiu emprego em menos de duas semanas após esse tipo de formação. Chegou a faltar aula para estudar por conta própria, alinhando o estudo aos requisitos reais de vagas — construía um projeto aplicando os temas pedidos na vaga, para ter repertório de entrevista.
- Dica prática que ele destaca: demonstrar vontade de aprender, não depender de terceiros, ser solucionador de problemas — projetos no GitHub (mesmo não-profissionais) ajudam a contar essa história em entrevista.

Eric é explícito: fundamentos importam, sim — inclusive ele recomenda que devs experientes voltem a estudá-los, porque ajudam a otimizar software e entender projetos em profundidade. O ponto não é que fundamentos sejam dispensáveis, mas que havia uma distância enorme entre o que se aprendia no início e o trabalho real. Muito do que aprendeu logo no início só foi usar/entender de fato bem depois, já em nível avançado — e algumas coisas nunca chegou a usar na prática. Isso não invalida o conteúdo, mas sugere que estava no momento errado da jornada de aprendizado.

### Como os irmãos de Eric estão aprendendo agora

- Aprendem Flutterflow, N8N, modelagem de banco de dados via interface, já no primeiro semestre, criando um app real e funcional.
- A ordem se inverteu: começam pelo alto nível (o que é um sistema, do que ele é composto) e vão afunilando para os fundamentos ao longo do curso, em vez do caminho inverso.
- Eric avalia isso como uma melhoria: ter algo funcional desde cedo, para visualizar problemas, e só então cair na especialização.

## A tese central de Eric: a ordem se inverteu, não os fundamentos

Fundamentos continuam importando. O que mudou é a ordem em que são adquiridos:

- Antes: baixo nível primeiro (sintaxe, algoritmos, estrutura de dados) → alto nível depois (produto funcional).
- Agora, cada vez mais: alto nível primeiro (telas, apps, automações, fluxos, integrações, protótipos) → aprofundamento em fundamentos conforme as dores reais aparecem.

Eric relata ter vivido essa segunda ordem antes mesmo da IA: aprendeu jQuery antes de JavaScript "puro", o que não o impediu de aprofundar em JavaScript depois — pelo contrário, foi o caminho que o levou a isso. Ele foi da API/CRUD/site funcional para, com a experiência, descer a camadas mais profundas: sintaxe e otimizações de linguagem, certificações, o que significa "escala" e otimizar para centenas de milhares de usuários simultâneos, arquitetura, ciclo de vida de aplicações, funcionamento do Node.js, infraestrutura, custo, observabilidade.

Padrão que ele identifica: aprofundamento e especialização surgem naturalmente quando a dor aparece —

- performance importa quando a aplicação fica lenta;
- modelagem importa quando o banco de dados vira bagunça;
- arquitetura importa quando o sistema começa a crescer;
- otimização de custo importa quando a infraestrutura fica cara;
- boas práticas importam quando o código fica difícil de manter;
- senso crítico importa quando a IA gera algo errado;
- responsabilidade técnica importa quando a empresa depende daquele software.

Ressalva de nível: um dev experiente é cobrado a planejar problemas possíveis desde o início e desenhar para estabilidade/resiliência desde o dia 1 — o júnior não precisa disso desde o dia zero, e "tá tudo bem" que não precise.

## "Quem começa por ferramenta X não aprende de verdade" — um medo recorrente, não novo

Eric argumenta que a crítica "se a pessoa começar por no-code/low-code/IA, ela não vai aprender de verdade" não é um medo novo — é uma variação de críticas que já existiam:

- quem aprendia pela web não sabia programar "de verdade" (segundo os críticos da época);
- quem começava por PHP não entendia de computação;
- quem usava jQuery não sabia JavaScript;
- quem usava framework não sabia o básico;
- quem usava Stack Overflow só copiava código sem entender;
- agora: quem usa IA não vai aprender, ou será "inferior" à geração anterior.

Conclusão de Eric: "a tecnologia muda, mas o medo é sempre o mesmo".

## O que a IA muda de fato (segundo Eric)

A IA acelerou o acesso: iniciantes conseguem pedir ajuda para entender erros, gerar exemplos, criar uma primeira versão de código, revisar ideias, explicar conceitos, montar caminhos de estudo. Isso também gera atrito para profissionais experientes, porque donos de empresa sem nenhuma experiência de código conseguem criar sistemas inteiros em minutos e questionam por que a equipe "demora tanto".

Risco apontado: essa acessibilidade cria a ilusão perigosa de que **gerar código é a mesma coisa que saber construir software**. Ser programador não se resume a escrever código — envolve considerar dezenas de complexidades e variáveis, desde o dia zero, algo que exige experiência.

Exemplo de risco concreto citado: criar um CRUD com IA pode ser fácil; saber se aquele CRUD está bem modelado, seguro, otimizado, barato de manter e adequado ao problema é outra história. Ele cita o cenário de um sistema criado sem consultoria especializada que "no outro dia" tem dados vazados por falta do mínimo de segurança da informação.

Formulação central de Eric: a IA ajuda muito no primeiro passo, mas não elimina a necessidade de **julgamento** — e julgamento vem de experiência, repertório e estudo.

## O que muda no perfil do "bom júnior"

Segundo Eric, a IA não acabou com o espaço dos juniores — mudou o tipo de júnior que se destaca.

- Antes: o diferencial era decorar sintaxe, montar tudo manualmente, copiar o mínimo possível.
- Agora: o diferencial passa a ser fazer boas perguntas, entender o problema, validar se a solução faz sentido, testar, ajustar, ter curiosidade, aprender rápido, e **não terceirizar completamente o raciocínio** para a IA.

Formulação de Eric: a IA deve ser "copiloto", não um "download do seu cérebro" — se você não sabe o que pedir, ela sempre vai te entregar um falso positivo. O júnior que só copia e cola sem entender vai ter dificuldade — mas isso já era verdade antes da IA. A diferença agora é que a ferramenta é mais poderosa e a ilusão de produtividade também é maior.

## Evidência de mercado (pesquisa informal do apresentador no LinkedIn)

### Brasil

- No momento da gravação, Eric relata ainda haver muitas vagas abertas para programador júnior no Brasil no LinkedIn — "milhares e milhares de vagas".
- Ele nota que mudanças de mercado costumam acontecer primeiro nos Estados Unidos e chegar depois ao Brasil — logo, o mercado brasileiro, no momento do vídeo, ainda não mudou a ponto de dispensar fundamentos ou a escrita de código por parte de juniores.
- Consenso nas vagas que ele checou: um júnior atual deve saber criar um CRUD de ponta a ponta, usar uma linguagem como TypeScript, saber um pouco de SQL, modelar e conectar a um banco de dados, trabalhar com Git, saber o que é uma API e integrá-la a um site, ter lógica de programação e estrutura de dados (recomendação de treinar em HackerRank / LeetCode).
- Não é exigida maestria total, mas um CRUD completo é, na visão dele, o que costuma abrir a primeira oportunidade.
- Nas vagas brasileiras que ele checou, saber ferramentas de IA aparecia como diferencial adicional, não como critério eliminatório.

### Estados Unidos

- Eric trabalha remotamente em inglês para empresas americanas há bastante tempo e usa o mercado dos EUA como referência do que deve chegar ao Brasil.
- Nas vagas americanas de nível iniciante que checou, já é esperado que o candidato tenha, além dos fundamentos, experiência usando ferramentas de IA para gerar código, acelerar desenvolvimento e criar projetos.
- Detalhe que ele destaca: essas vagas pedem "familiaridade" com alguma linguagem de programação, não necessariamente conhecimento profundo de todas as ferramentas — ao contrário de vagas brasileiras que, segundo ele, ainda listam exigências mais extensas/rígidas.
- Sua expectativa: esse padrão americano deve chegar ao Brasil em breve.

## Conclusão de Eric sobre o mercado

O Dev Júnior não acabou, mas está sendo remodelado. Algumas tarefas antes manuais de um iniciante podem hoje ser aceleradas com IA e ferramentas visuais/automações — mas empresas ainda precisam de pessoas capazes de construir, adaptar, operar, entender contexto e evoluir sistemas.

- No Brasil: fundamentos continuam essenciais para quem está recém-formado ou com pouca experiência.
- Nos EUA: já se espera que essas pessoas usem IA a favor para entregar mais rápido, aprendendo no dia a dia — não necessariamente decorando sintaxe, mas entregando produtos partindo de um nível mais alto, se especializando conforme os problemas aparecem, antes de "concluir a parada toda" (isto é, aprofundando sob demanda em vez de dominar tudo antes de começar).

## Mensagem final / recomendações

**Para quem está começando:**
- Construa algo: um app, site, CRUD, automação, bot, jogo — qualquer coisa. Use IA, ferramenta visual, framework, template — o que te colocar em movimento.
- Preencha o GitHub com projetos de portfólio — é o que diferencia entre concorrentes.
- Não pare no "funcionou": pergunte-se por que funcionou, o que está acontecendo por trás, onde pode quebrar, como você testaria, como explicaria a solução para outra pessoa. É assim que o alto nível "puxa" o fundamento.
- Não é preciso saber tudo antes de começar, mas isso não é desculpa para nunca se aprofundar.

**Para quem já é experiente:**
- A nova geração não está perdida — só está começando por outro lugar.
- Cuidado para não transformar a própria trajetória (tela preta, algoritmo, estrutura de dados primeiro) em régua universal. Sofrer para aprender não é pré-requisito de validação para a próxima geração.
- A área, as ferramentas e a forma de aprender mudaram — e isso pode ser uma melhoria: descobrir mais cedo do que se gosta (produto, automação, dados, interface) é preferível a anos de conceitos sem saber onde se encaixam.

**Reformulação da pergunta-título:** para Eric, a pergunta não é "a IA acabou com os juniores?", e sim "como preparar melhor quem está começando para construir com ferramentas modernas sem abandonar o pensamento crítico?" — porque nenhuma ferramenta substitui uma pessoa curiosa, capaz de aprender, questionar e evoluir.

## Encerramento

Pedido de engajamento (like, comentários, inscrição no canal) e convite para ver as playlists do canal.
