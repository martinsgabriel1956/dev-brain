# Mainframe as a Service: Casas Bahia, SulAmérica e o zCloud da Kyndryl

Transcrição de vídeo em PT-BR (canal e autor desconhecidos; o autor menciona ser autor do livro *Introdução à Plataforma Mainframe*). Já em português — sem tradução. Título original desconhecido; título descritivo derivado do conteúdo.

> **Nota de limpeza:** a transcrição automática corrompeu vários termos, corrigidos por contexto: "Benfame/Menframe/mainfame" → mainframe; "Kindrew/Kindre/Kinder/Kindro" → Kyndryl; "Zloud/ZCloud" → zCloud; "Acer" → Azure; "Incobol" → em COBOL; "Prisma" → PR/SM (Processor Resource/System Manager); "Lipar/L par/Lippar" → LPAR; "MAS/GMAS/NAS/MAS" → MaaS (Mainframe as a Service); "multitênne" → multitenant/multitenância; "Six" → CICS; "ZOS" → z/OS; "STF" → staff (equipe); "ox" → OPEX; "J2E" → J2EE; "hyper scaler" → hyperscaler. Pontuação e pausas de fala foram reorganizadas em parágrafos; o conteúdo não foi alterado.

## Abertura: a pergunta sobre as Casas Bahia

Há uns dias um espectador deixou um comentário perguntando se o autor sabia algo sobre a migração das Casas Bahia para o serviço de zCloud da Kyndryl. O caso ajuda a desmontar uma associação automática: quando se diz que uma empresa "levou sistemas para a nuvem", pensa-se em AWS, Azure, Google Cloud, instâncias x86, contêineres, microsserviços, um sistema em COBOL reescrito em Java. Nem sempre é assim.

O grupo Casas Bahia migrou seus sistemas do mainframe para um serviço da Kyndryl chamado zCloud. A SulAmérica já tinha feito o mesmo um ano antes: migrou sistemas de saúde, vida e previdência para o serviço de cloud da Kyndryl. Ou seja: as empresas foram para um **modelo de nuvem sem abandonar o mainframe**.

## Dois conceitos que costumam vir misturados

Ao falar de modernização, é preciso separar: **onde** a aplicação é executada e **como** a infraestrutura onde ela roda está sendo **consumida**.

### O modelo tradicional

Durante décadas: a empresa grande comprava ou alugava um mainframe e o colocava no próprio data center, mantendo toda a estrutura: processamento, conectividade, segurança, recuperação de desastre, backup, e uma equipe de especialistas para administrar o ambiente. O maior desafio era estabelecer uma **capacidade** suficiente para rodar os sistemas.

O exemplo: uma rede de varejo precisa de uma capacidade numa terça-feira qualquer de agosto completamente diferente da que precisa na semana da Black Friday. Para não perder venda no pico, tradicionalmente **superestimava-se** a capacidade; no resto do tempo essa capacidade extra ficava **subutilizada** — e "capacidade subutilizada é dinheiro parado". Esse dilema (capacidade para o pico × capacidade ociosa) é o grande apelo dos serviços em nuvem.

### A virtualização nasceu no mainframe

O curioso, segundo o autor, e que pouca gente comenta: a virtualização não nasceu com a AWS; **nasceu no mainframe**. Compartilhamento de recursos e aumento/diminuição de capacidade conforme a necessidade já existiam no mainframe há décadas. (O autor não entra nos detalhes de PR/SM e LPAR — diz que daria um vídeo próprio e que explica isso no livro.)

O princípio: um grande equipamento físico pode ter seus recursos particionados e compartilhados entre ambientes diferentes. O PR/SM permite criar **partições lógicas (LPAR)** numa mesma máquina, que podem rodar sistemas operacionais diferentes, isolados e independentes.

### Multitenância

Se é possível compartilhar recursos de uma máquina entre sistemas diferentes com isolamento e segurança, é natural compartilhar entre **empresas diferentes**, oferecendo a cada uma só a capacidade de que precisa em cada momento. Esse é o conceito de **multitenant**: um provedor como a Kyndryl mantém toda a infraestrutura de mainframe e oferece parte da capacidade a clientes diferentes, mantendo os ambientes segregados.

É o que já se conhece da cloud pública: ao criar uma instância num hyperscaler, não se sabe em que servidor físico ela roda, e nem precisa — compra-se **capacidade computacional, não hardware**. O hardware, seja qual for a plataforma, é problema do provedor.

## MaaS: o que a Kyndryl ofereceu

É exatamente isso que a Kyndryl ofereceu às Casas Bahia e à SulAmérica: eles contratam um **MaaS — Mainframe as a Service**. O mainframe continua lá; os sistemas críticos, com milhares de programas e milhões de linhas de COBOL, DB2, CICS, JCL, seguem rodando. A empresa não corre o risco nem arca com o custo de reconstruir sistemas que existem há muitos anos só porque mudou a forma de **consumir** a plataforma.

Antes: mainframe próprio em data center próprio. Agora: um serviço da Kyndryl que entrega uma ou mais LPARs de um mesmo equipamento físico para ela e para outros clientes. O cliente não sabe em que mainframe seu workload roda — como com uma instância x86 na AWS.

## Vantagens econômicas

Quando a empresa mantém infraestrutura própria, ela **imobiliza capital** para manter capacidade, principalmente para o pico: isso é **CAPEX**. Ao terceirizar em modelo MaaS, o que era capital imobilizado passa a ser **custo operacional (OPEX)**.

Gráfico hipotético do autor: histórico de consumo de MIPS numa instalação. Com máquina própria, é preciso dimensioná-la para o **pico**, e sempre sobra uma "zona cinzenta" de **capacidade ociosa** — dinheiro parado em capital imobilizado sem necessidade. No modelo MaaS, contrata-se uma **capacidade elástica**, com margem de segurança sobre o histórico de movimentação; a área que antes era capacidade imobilizada vira **ociosidade eliminada**, economia de custo operacional.

### Equipe de especialistas

Não é só hardware: antes era preciso uma "tropa" de especialistas — suporte de CICS, DB2, z/OS, storage, performance. Ao contratar MaaS, o provedor assume boa parte desses especialistas e os **compartilha entre vários clientes**. Para algumas empresas, essa terceirização da equipe (que era própria) é **mais importante do que a economia** com a infraestrutura.

## Conclusão: mainframe × nuvem não é oposição

O mercado confunde "modernização" e "migração para a nuvem" como se houvesse uma oposição artificial: "se vou para a nuvem, tenho que matar o mainframe; se fico no mainframe, não fui para a nuvem". Mas os sistemas corporativos não evoluem assim. O que se vê é um sistema crítico legado no mainframe que conversa com um software-as-a-service, que também fala com um sistema de microsserviços numa nuvem híbrida, que também fala com um sistema Java departamental desenvolvido anos atrás em J2EE, e assim por diante. Apesar de chamado de legado, o sistema **evolui na forma como se integra** com o resto — e, nos exemplos das Casas Bahia e da SulAmérica, evolui também na **infraestrutura onde executa**.

Quando se ouve que "a empresa migrou para a nuvem", não necessariamente o mainframe foi desligado: no caso das Casas Bahia e da SulAmérica, **a empresa foi para a nuvem e o mainframe foi junto**.

## Encerramento

O autor diz que neste mês quer falar de projetos de modernização que **não necessariamente mataram o mainframe ou o COBOL**, pede sugestões de tema nos comentários e avisa que a conversa continua na semana seguinte.

## Trechos

> "As empresas foram para um modelo de nuvem sem que isso significasse necessariamente abandonar o mainframe."

> "Uma coisa é onde a aplicação é executada, outra coisa é como a infraestrutura onde ela é executada está sendo consumida."

> "Capacidade subutilizada é dinheiro parado."

> "A virtualização não nasceu com a AWS; ela nasceu no mainframe."

> "A empresa foi para a nuvem e o mainframe foi junto."
