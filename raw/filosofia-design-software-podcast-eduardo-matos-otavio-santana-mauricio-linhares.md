# Filosofia do Design de Software — bate-papo entre Eduardo Matos, Otávio Santana e Maurício Linhares

> Transcrição de podcast/vídeo em português, fornecida pelo usuário como texto corrido (fala transcrita automaticamente, sem pontuação/parágrafos, com hesitações e repetições típicas de fala natural). Reescrita como Markdown estruturado por tópicos, preservando o conteúdo e a ordem original da conversa, removendo apenas repetições de fala, hesitações ("né", "tipo", "então" excessivos) e cacoetes de transcrição automática. Sem necessidade de tradução (fonte já em português). Participantes identificados pelo próprio diálogo: o anfitrião é Eduardo Matos; os convidados são Otávio Santana e Maurício Linhares (mencionado também como "Linhares"), ambos engenheiros de software experientes. O tema é uma conversa sobre o livro **"A Philosophy of Software Design"**, de John Ousterhout (sem tradução para o português até o momento da gravação).

Episódio de podcast em formato de bate-papo entre três engenheiros de software sobre o livro *A Philosophy of Software Design*, de John Ousterhout. Eduardo Matos conduz a conversa, alternando perguntas entre Otávio Santana e Maurício Linhares sobre os principais temas do livro: complexidade, design estratégico vs. tático, TDD, design de APIs, tratamento de erros e comentários no código.

## Abertura

Eduardo Matos recebe Maurício Linhares (chamado de "corrusty" por Otávio) e Otávio Santana para discutir o livro *A Philosophy of Software Design*. Maurício comenta que está bem, apesar de o filho ter voltado doente da escola — "padrão" de quem tem criança pequena.

## Complexidade: os primeiros sinais de que um sistema está ficando complexo

Eduardo pergunta quais são os primeiros sinais de que um sistema/software está se tornando complexo.

**Maurício Linhares** destaca o conceito do livro chamado **change amplification**: você imagina que uma mudança está logicamente localizada em um pedaço do código, mas ao tentar fazê-la descobre que precisa alterar várias outras classes com as quais não sabia que havia dependência. Isso fica muito visível quando alguém chega pela primeira vez numa base de código nova (troca de emprego, nova equipe): a pessoa pensa que a mudança é localizada, mas descobre que precisa alterar vários lugares diferentes, inclusive configuração. Isso indica que o conhecimento que deveria estar encapsulado em um único lugar está espalhado pela base de código.

**Otávio Santana** complementa pelo caminho contrário: quando o conhecimento *não* está devidamente espalhado/documentado, entra o conceito de **cargo cult** — o processo de onboarding, quantas pessoas você precisa consultar para entender o sistema. Cita o meme de "a pessoa nova pergunta onde está a documentação, e alguém responde 'a documentação sou eu'". O número de dias que uma pessoa leva para entender o processo é um sinal importante. Reforça que a indústria segue cometendo o mesmo erro de falta de documentação, independentemente da moda arquitetural do momento (microsserviços, e futuramente "nanoserviços"/"atomic services").

## Modularidade: partir para módulos pequenos ou aceitar classes maiores?

Eduardo questiona como decidir entre uma linha mais modular (muitos módulos pequenos, alterados em várias partes) versus classes/métodos maiores.

**Otávio** relata que, na prática, só percebia se estava no caminho mais adequado conforme via o software evoluir — por exemplo, perceber que uma classe estava ficando grande demais, com muita responsabilidade, e que valia a pena quebrá-la. Não acredita que exista controle total sobre isso: é preciso deixar o software evoluir e entender em que direção ele está indo, para então decidir se as abstrações fazem sentido. Toda decisão tomada é um trade-off (ganha de um lado, perde de outro).

**Maurício** reforça que, no início de um projeto, não adianta se preocupar demais com isso, porque ainda não se entende bem o domínio/modelo — esse conhecimento é construído aos poucos. Cita (apesar de "detestar a maior parte das coisas que o Bob Martin fala") a ideia de que construir software é um processo científico: você constrói conhecimento e traduz isso para o software de forma evolutiva. A exceção é quando se está migrando um monolito existente para microsserviços — nesse caso já se enxerga a estrutura atual. Caso contrário, começando do zero, é natural "quebrar a cara" porque ainda não se sabe quais são os contextos corretos.

Menciona o conceito do livro (capítulos 2–3) de **programação tática vs. programação estratégica**: programação tática é fazer a entrega sem considerar o impacto no software; programação estratégica é pensar em como a mudança deixa a estrutura do software melhor no final. É preciso equilíbrio: reconhecer que o processo é evolutivo, mas também se esforçar para melhorar o software continuamente — senão a dívida técnica cresce até o ponto em que ninguém mais quer mexer no sistema e todos querem reescrevê-lo do zero.

Otávio relata uma situação recorrente: projetos antigos e ninguém entende a solução, e a resposta costuma ser "adicionar mais microsserviços" ou trocar de linguagem/tecnologia, achando que isso resolve o problema real. Cita o termo do livro sobre **"desconhecido"/"unknown unknowns"** como uma das métricas que mais tocou. Recomenda simplicidade como caminho: cita que os capítulos iniciais dos livros de microsserviços da Microsoft (que "todo mundo cita mas ninguém lê") já alertam sobre a dor de cabeça de ir para microsserviços sem necessidade.

**Maurício** reforça: gosta de começar o código/arquitetura propositalmente simples — até um pouco mais simples do que talvez fosse necessário — e só adicionar complexidade quando sentir a dor real. Relata que, olhando para todas as equipes por onde passou, o maior problema recorrente foi complexidade desnecessária no código — cita um exemplo absurdo de um fluxo de "depósito" que, por trás de um botão aparentemente simples, disparava um pipeline complexo entre múltiplos repositórios e times. É importante ficar atento a esse acúmulo de complexidade ao longo do tempo, seja por tecnologias antigas, seja por metodologias que já não fazem mais sentido.

## Momento certo para revisar/melhorar o código

Eduardo pergunta se costuma ser mais produtivo revisar o código periodicamente (ex.: a cada X meses) ou ficar sempre buscando pontos de melhoria no dia a dia.

**Maurício** responde que depende da pressão do momento — nem sempre há tempo. É importante que quem está começando na carreira entenda que refatorar constantemente nem sempre é viável do ponto de vista do negócio: às vezes é preciso entregar algo sob pressão, mesmo sabendo que não é o ideal. O importante é ter consciência do que ficou "para trás" e ter também o momento de voltar a esses pontos. Prática recomendada: ao identificar uma solução que resolve o problema imediato mas cria um problema de arquitetura/design a ser resolvido depois, criar diretamente um card/ticket linkado (ex. no Jira) explicando por que a solução foi feita daquele jeito e o que precisa ser revisitado (repetição de código, entendimento, manutenção, estabilidade). Isso ajuda a equilibrar entrega de funcionalidade com qualidade de código, e melhora a comunicação com o time.

**Otávio** conecta essa prática ao conceito do livro sobre **"tactical tornado"** ("tornado tático") — a pessoa que, por onde passa, deixa o código difícil de entender, manter e evoluir. Relata que errava por dois motivos: pressão (sem documentar) e o vício de aplicar toda funcionalidade nova da linguagem em todo lugar, mesmo sem necessidade, piorando o código para "usar a feature". Menciona o estereótipo do "programador 10x" que depois "desaparece" (vira "programador ninja"), deixando bombas-relógio para o time desarmar depois.

**Maurício** relata um caso real: um colega que saiu da empresa, e dois anos depois ainda surgiam problemas relacionados ao código que essa pessoa havia deixado, porque ela trabalhava sozinha e não explicava nada para ninguém. Considera terrível esse padrão de trabalho isolado, mesmo quando aparentemente mais "produtivo".

**Otávio** conta um caso parecido: um projeto entregue por uma pessoa que saiu da empresa, escrito em uma linguagem que ninguém mais da equipe conhecia — ao quebrar, ninguém sabia nem por onde começar a debugar.

**Eduardo** conecta os pontos: um código ruim/difícil de manter está ligado à colaboração em equipe, e a documentação (bem como um código bem escrito) faz parte do próprio design do software — os dois trabalham em conjunto para comunicar intenção.

## TDD, documentação e design guiado por testes

Eduardo pergunta a opinião de ambos sobre TDD (o autor do livro não é muito entusiasta da prática), e se o importante é só ter testes no final.

**Maurício** discorda parcialmente do livro na parte em que o autor sugere escrever a documentação primeiro e derivar a implementação dela. Prefere partir do teste como o primeiro "usuário" do código: pela facilidade ou dificuldade de testar, avalia se o design imaginado realmente funciona. Ressalva que isso funciona bem para testes unitários e sistemas de backend, mas não necessariamente para interfaces (onde talvez um *sketch*/protótipo de uso seja mais adequado).

**Otávio** concorda parcialmente: usa práticas de linguagem ubíqua (DDD) para desenhar o código, observando se classes e métodos estão alinhados com a nomenclatura do negócio. O teste ajuda nesse primeiro momento (sem se preocupar ainda com implementação) a validar a clareza do código em relação ao negócio. Seu fluxo: cria o teste (às vezes sem nem corrigi-lo ainda), documenta espalhando contexto de negócio nas classes/métodos, e só depois trabalha na implementação/correção dos testes.

Ambos discutem uma citação de DHH (criador do Rails) sobre "TDD is dead": código não deve ser guiado necessariamente por testes nem por arquitetura — a arquitetura deveria resolver o problema de negócio primeiro, e os testes viriam depois como ferramenta de regressão, não necessariamente como ferramenta de design. **Otávio** relata que, atualmente, não é um grande praticante de TDD, mas valoriza muito ter testes — sobretudo quando corrige um bug, prática de criar primeiro um teste que reproduz o bug (TDD aplicado a correções, não ao desenho inicial).

**Maurício** questiona a mistura de conceitos: para ele, arquitetura (estrutura da aplicação) é diferente de design de código (nível de método/classe/pacote, onde entra o DDD). Testes unitários atuam no nível de design/modelagem, não no nível de arquitetura — por mais que a arquitetura influencie o design, ela está "fora" do teste unitário. O que pode acontecer é o teste unitário sinalizar que a arquitetura está complicando demais o design (cita como exemplo negativo a quantidade de anotações/configuração exigida por certas convenções do Spring para tornar uma classe testável).

## Design de APIs: o exemplo negativo do `java.io`

Eduardo puxa o capítulo 4 do livro, sobre módulos e design, onde o autor usa a API de I/O do Java como exemplo de má API.

**Otávio** concorda que a API de I/O do Java é um exemplo ruim — só perde para a de `java.util.logging` como pior. Questiona por que o livro não fala diretamente com o autor sobre isso.

**Maurício** explica o problema central: em vez de otimizar para facilidade de uso, a API do Java foi desenhada para dar muitas opções de otimização — múltiplas formas de fazer a coisa errada, sem um caminho simples óbvio. Até o Java 9 não havia um método simples para ler um arquivo inteiro como bytes; todo mundo escrevia essa mesma classe utilitária repetidamente nos seus projetos — sinal de que a abstração estava errada ou complexa demais. A API é composta por ~20 classes que o usuário precisa conhecer, com heranças do C e limitações da linguagem (ex.: não ter retorno múltiplo, forçando o uso de constantes especiais para sinalizar fim de arquivo). O design não considerou usabilidade do ponto de vista de quem chama a API — só depois de duas décadas o Java ganhou um método simples para ler um arquivo inteiro.

Conectam isso ao conceito do livro de **módulo raso ("shallow module")**: várias classes pequenas, cada uma fazendo pouco — o exemplo clássico do padrão *Decorator* usando streams do Java é um ótimo exemplo do padrão, mas um péssimo exemplo de API bem desenhada.

**Otávio** relaciona ao overengineering: querer expor todas as opções possíveis e esquecer do "caminho feliz". Cita como esse caso é usado até hoje pelo comitê executivo do Java como exemplo de erro cometido pela comunidade.

**Maurício** propõe balancear os dois lados: nada impede oferecer opções de baixo nível avançadas, desde que também exista uma solução simples e de alto nível para o caso comum — dando o exemplo de bibliotecas (como a antiga versão do Feed/RSS parser que usava) que ofereciam tanto um método simples de alto nível quanto acesso de baixo nível para casos avançados.

**Otávio** cita o "paradoxo da escolha" mencionado por um colaborador do Spring: ter muitas opções de API pode atrapalhar mais do que ajudar, mesmo quando as opções parecem boas — analogia com a dificuldade de escolher um filme na Netflix.

Discutem o conceito de **camadas (layering)** do livro, usando o exemplo da API de arquivos do Unix/Linux — seis métodos simples (abrir, ler, escrever, mover, fechar etc.) que abstraem completamente detalhes de hardware (HD, SSD, rede) e do sistema de arquivos. O ideal seria o `java.io` ter feito o mesmo: uma camada de alto nível simples, escondendo a complexidade de baixo nível para quem não precisa dela, mas ainda disponível para quem precisa (cita um caso real de precisar ajustar o tamanho de buffer de leitura do Linux). Cita também a função `file_get_contents` do PHP como exemplo (não necessariamente de melhor prática, mas de simplicidade de uso) — aceita tanto caminho de arquivo local quanto URL.

## Como chegar a um bom design de API na prática

Eduardo pergunta como, na prática, se chega a um design de API realmente bom (não trivial, não é só "simplificar").

**Maurício** responde que o primeiro passo é entender o caso de uso — qual problema realmente precisa ser resolvido. Usa como exemplo positivo o cliente HTTP do Go: apesar de ter alguns problemas de tipagem, é muito bem construído, pois abstrai a negociação entre três versões diferentes do protocolo HTTP e o handshake TLS — o usuário não precisa saber os detalhes, só faz a chamada e recebe a resposta ou o erro. É um cliente HTTP de alto nível, com objetivo claro dentro da biblioteca padrão: simplicidade de uso, com algum grau de customização, sem expor toda a complexidade interna.

**Otávio** compara com a analogia do micro-ondas: o usuário não precisa saber sobre ondas eletromagnéticas e vibração molecular, só aperta o botão. Aponta um erro comum: no padrão **Repository** (DDD), muita gente cria métodos como "inserir", "deletar", "atualizar" e coloca sufixo "Repository" achando que está aplicando DDD, quando na verdade o conceito é abstrair a implementação e usar linguagem próxima do domínio de negócio (ex.: um repositório de carros de uma locadora deveria ser uma "garagem", com métodos como "registrar" ou "estacionar" em vez de "inserir").

## Trechos mais importantes do livro, na opinião de cada um

**Otávio** escolhe o **capítulo 10 ("Define errors out of existence")**: a ideia de eliminar erros de existir, em vez de simplesmente lançar exceções sem necessidade. Critica APIs que lançam erros sem motivo real, exigindo uso exatamente de uma forma específica — contrasta com sua experiência em Ruby, onde a API tenta sempre entender a intenção do usuário e chegar o mais próximo possível do esperado. Reforça que uma API também é uma interface de usuário (o desenvolvedor que a chama é o usuário), e devemos nos preocupar com usabilidade da mesma forma que com UI. Em vez de lançar erro, o ideal é: (1) projetar a solução para que o erro seja impossível de acontecer, ou (2) tentar entender a intenção e entregar o resultado mais próximo do esperado (exemplo: pedir um substring além do tamanho da string deveria retornar o que existe, não lançar exceção).

**Maurício** escolhe o **capítulo 15 (comentários)**: critica a "utopia" de que código bem escrito dispensa comentários — cita que grandes projetos (API do Google, Intel, o kernel Linux, JVM, Spring) usam comentários extensivamente. Recomenda o capítulo como referência para aprender a escrever bons comentários e boa documentação.

**Eduardo** fica com a ideia geral do livro: simplicidade — reforça que, na sua experiência, a complexidade desnecessária foi o maior problema recorrente em todas as equipes por onde passou, dificultando a entrega de funcionalidades.

## Encerramento

Maurício recomenda a leitura do livro *A Philosophy of Software Design*, chamando-o de um dos melhores livros recentes sobre design/modelagem de software. Menciona seu canal com resumos de livros (já cobriram esse título e estão cobrindo também *Fundamentals of Software Architecture*, livro que considera uma futura referência de arquitetura de software). Brinca que o único efeito colateral de todo mundo ler o livro é gerar mais discussões técnicas ("treta"), já que o livro deixa claro que várias decisões de design "dependem" do contexto, sem resposta única certa.
