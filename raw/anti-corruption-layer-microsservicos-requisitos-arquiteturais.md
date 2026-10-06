# Anti-Corruption Layer em Microsserviços: Funcionamento, Problemas e Requisitos Arquiteturais

Transcrição de vídeo/aula (pt-BR, autor não identificado no trecho colado; continuação do vídeo registrado em `raw/anti-corruption-layer-facade-adapter-sistema-legado.md`). ASR bruto limpo, pontuado e organizado em seções; conteúdo técnico preservado, sem tradução (já estava em português). Termos reconhecidos erroneamente pelo ASR foram corrigidos pelo contexto: "Market" = time to market; "ras" = RAs (requisitos arquiteturais); "ten/ten que" = "tem/tenho que"; "lobs" = LOBs (linhas de negócio); "ep gate" = API Gateway; "dnet" = .NET; "skl server" = SQL Server; "microcomponente zado" = microcomponentizado; "RB" = rollback; "ARL" = RAs, "carimbando a notinha" = emitindo nota fiscal.

## Origem e referências

Este é um padrão de projeto cujo conceito foi trazido para o universo de microservices. As referências usadas: o portal microservices.io (pouca coisa, mas com comentários que levam a um portal da Microsoft e ao livro de Chris Richardson). O conteúdo é baseado nessas duas referências, mais um pouco do conhecimento do autor. O foco do vídeo é falar de **requisitos arquiteturais**, que "não é em todo lugar que a gente vê".

## Por que o padrão é aplicável a microsserviços

Quando se fala de "refatoramento" (entre aspas, segundo Chris Richardson), é um padrão que ajuda a diminuir a complexidade e reduz os problemas na hora de migrar para o modelo microcomponentizado. Contribui também para reduzir a dependência do legado em relação à versão nova: as dependências ficam todas nessa camada anticorrupção.

O padrão nasceu com Eric Evans, no DDD. Na época a iniciativa não era para migração para domínios: quem leu o livro vê que Evans já propõe que o projeto nasça usando a abordagem de domínios; ele fala em alguns momentos de uma possível migração/refatoração, mas o ponto aqui era **dependências externas**. Exemplo: existe outro domínio externo, que nem é meu ou que não é mais importante que o meu domínio Core, e que vai demandar alteração no meu domínio principal. Coloca-se uma camada anticorrupção no meio para garantir que a alteração feita no microsserviço principal (ou secundário que demanda alteração no principal) **não altere o principal**, e sim a camada anticorrupção, evitando o impacto. O vídeo não é sobre DDD, e sim sobre a aplicação do padrão na microcomponentização.

## Objetivo (recapitulação)

O objetivo é não estragar o outro código. Há um código novo e um legado; para não haver quebra arquitetural/estrutural grande dos dois lados, um componente faz a tradução de um subsistema para o outro. A substituição é gradativa, e tudo que seria incomum e causaria impacto em uma das duas pontas vai para a camada intermediária. Implementação via Facade ou Adapter (Design Patterns).

## Problemas que resolve

- **Dependência.** Quando se muda um ponto, pode-se quebrar outro; dependências escondidas (URL vinda de configuração em banco, arquivo ou memória/variável de ambiente; reflexão em .NET/Java, ligando componentes em tempo de execução) são difíceis de diagnosticar. O padrão evita dependência forte entre os objetos da versão nova e da anterior: mudança na origem (na requisição feita ao microsserviço novo) quebra o lado de cá; mudança no provedor (resposta ou assinatura da requisição) quebra a outra ponta.
- **Sistemas legados.** Não só um, talvez vários legados que precisavam se falar; a camada reduz a dependência e, com isso, os problemas nos sistemas de origem, "os antigos, que tipicamente são os principais e vão ser por um bom tempo quando você começa esse processo".

## Definição do padrão

### 1. Isolamento dos subsistemas e responsabilidade clara

A primeira coisa é isolar os subsistemas e ter clareza da responsabilidade de cada componente ao segmentar (o Strangler é um bom exemplo, do conteúdo anterior sobre padrões de microservices). Precisa estar bem definido o que fica no sistema novo e no antigo: quem faz a requisição, quem responde, o que há na requisição e na resposta. "É quase como pensar em Bounded Contexts."

Essa é a **grande dor do padrão**: às vezes coloca-se parte de uma única responsabilidade no legado e parte no novo, e fica uma dependência muito forte entre os dois. A camada anticorrupção **não resolve a divisão de responsabilidades**; ela ajuda com alterações no sistema A que não poderiam ser feitas e tiveram de ser levadas ao B (ou vice-versa).

Exemplo do autor: update de uma **pessoa** no legado. O legado atualiza a entidade pessoa; endereço e telefone já estão em microsserviços (talvez vários) e passam pela camada anticorrupção. Em um primeiro momento a pessoa tinha um telefone; depois surgiu o celular e passou a poder ter vários telefones, então cria-se uma entidade telefone. O legado passa a demandar alterações na camada futura; o "salvar" completo fica com um pedaço no legado e um pedaço no novo, e se algo falhar lá é preciso desfazer aqui. A camada anticorrupção resolve isso "de certa maneira", mas continua problemático porque **é a mesma responsabilidade (salvar a pessoa) dividida**. Melhor migrar tudo junto: a pessoa inteira no microsserviço novo, não parte no legado e parte no novo.

### 2. Várias camadas anticorrupção

Se vários sistemas consomem o mesmo microcomponente, é bom ter mais de uma camada anticorrupção, em vez de uma única para tudo.

### 3. Como funciona

A lógica da camada fica dentro de um componente **totalmente isolado**: pode ser um microsserviço, ou estar dentro de um API Gateway separado (várias APIs, cada uma representando uma camada anticorrupção). Poderia ser feita no lado do legado, principalmente se o legado é o grande ponto, **mas com o tempo tende-se a ter mais responsabilidade nos microcomponentes do que no legado**: no começo os microcomponentes são menos importantes que o monólito; depois a coisa vira. Por isso é bom isolar a camada e não enraizá-la. Muitas aplicações, porém, começam com a camada dentro do sistema legado ("cada sistema legado tem a sua"). A comunicação é sempre entre subsistemas, e é preciso ter as **abstrações da outra ponta**; sem abstração a camada não funciona como deveria.

## Cenário ilustrado (o desenho)

Sistema antigo com seu banco; com o tempo, pequenos componentes migram para microsserviços. O ideal é que cada microsserviço tenha seu próprio banco, mas haverá cenários em que é preciso usar dados do banco primário.

**Sem camada anticorrupção**, com o legado chamando o microsserviço direto: para consultar dados do banco legado a partir do microsserviço (ou compor a lógica dele), seria necessário **alterar o sistema legado** (como no exemplo da pessoa com telefone): passar mais informações, fazer segunda consulta etc. Ou seja, mexer no legado só para começar a usar microsserviços, com alteração estrutural e na camada de dados; a resposta do microsserviço impacta o que se salva do lado de cá. Se o microsserviço precisar de mais um campo, altera-se o legado de novo, e a camada que faz a requisição ao microsserviço talvez não tenha esse campo, e assim por diante. Altera-se um método do legado que talvez seja usado por muita coisa: risco de quebrar, de ter que testar todo o legado de novo.

**Com camada anticorrupção** (pode ser um componente apartado, até um microsserviço): o autor a chama de **"patinho feio"** — não é bonita. Quem chama a camada é o legado. No exemplo: para gravar a pessoa, o legado chama a camada, que usa o banco antigo para parte da pessoa e vários microsserviços para o resto; chama o microsserviço 1, "deu bom", faz commit, deixa transação aberta etc. Ou seja, ela tem dependência até do banco legado — a razão de existir é não mexer no legado. Em tese a camada de microsserviços não precisaria desse artifício, por já ser feita de forma atômica com boas práticas. Se a lição de casa foi bem feita, a camada anticorrupção "vai ser feia para caramba, mas é mais para o lado do legado". Em alguns casos pode-se trazê-la para dentro do legado — pode nascer assim, principalmente se há um plano de **tombar todo o legado** (certeza absoluta de que não se quer mantê-lo): coloca-se a parte feia no lado legado e depois puxa-se tudo. **Se começar a haver alterações do lado dos microsserviços (tabelas etc.) a partir da camada anticorrupção, é problema**: perde-se o objetivo da migração; o microsserviço deve ser autônomo e resolver tudo que lhe cabe numa requisição.

### Onde se aplicam Facade e Adapter

- **Facade**, principalmente do lado do legado: tipicamente é o legado que chama a camada, então existe uma interface comum, conhecida e "praticamente imutável" (deveria ser imutável). Toda a complexidade de ajustar/adaptar fica por trás. Exemplo: um legado que talvez seja um mainframe e nem consiga chamar o microsserviço direto; chama-se outro componente em tecnologia mais nova. A camada pode até ir direto ao banco de dados, se não há interface pura.
- **Adapters**, do lado dos microsserviços: talvez seja preciso usar uma versão intermediária de microsserviço num momento e a definitiva em outro; conforme a parametrização recebida, ir para uma versão ou outra; chamar um único microsserviço ou dois, três, quatro; ora modelo **coreografado**, ora **orquestrado**. Toda essa complexidade vai para a camada, evitando levá-la ao legado (desacoplamento).

Evoluções do lado dos microsserviços (mudar a assinatura, o tempo de resposta degradando e exigindo escalar para outra infra, outro protocolo de comunicação — por exemplo HTTP, para evitar latência alta) são resolvidas na camada **sem colocar tecnologias novas no legado**. Exemplo extremo: legado monolítico com comunicação binária que não suporta HTTP; suportá-lo exigiria upgrade do sistema operacional, do compilador/runtime etc., o que pode quebrar muita coisa — "uma cadeia de problemas". A camada anticorrupção **quebra o acoplamento do conhecimento da conexão entre os dois sistemas**.

## Problemas a considerar

- **Escalabilidade.** O legado talvez já esteja em cluster ou escale horizontal/vertical (talvez independente de sessão, com sessão em banco). Ao colocar a camada, é preciso escalá-la também (principalmente se apartada, como serviço adicional), e talvez adicionar um balanceador de carga entre a camada e o legado.
- **Manutenção adicional**, não só da camada, mas dos componentes de infra no meio.
- **Latência.** Uma camada extra: requisição vai e volta, aumentando a latência.
- **Várias camadas anticorrupção**, importante com vários subsistemas. Antes havia um sistema Core e satélites ("monolitinhos") em volta, e muitas aplicações ainda são assim. Na migração é preciso comunicação entre eles; provavelmente uma camada **por subsistema**, pensada de forma isolada — senão o acoplamento de vários subsistemas na mesma camada vira dor de cabeça. **Mesmo com código duplicado, recomenda-se uma camada por subsistema/sistema integrado**, ao custo de mais complexidade de implementação.
- **Gerenciamento.** Se for componente/infra separada, é preciso monitorar tudo; aumenta a complexidade de **observabilidade**; há também a decisão de como lidar com as demais camadas e requisições a cada microsserviço.
- **Permanência da camada.** Ela serve para levar o legado para a versão nova; com o tempo **vira débito técnico**, pesado de manter e evoluir. Em DDD e outras aplicações, a camada durar não é problema ("faz parte da solução"); na migração legado → microsserviços, enquanto os dois sistemas existirem faz sentido, mas passar muito tempo vira problema. Relato do autor: já viu migrar todo o legado, mas ficar uma dependência — um "croninho" que atualizava uma tabela que, na outra ponta, um microsserviço alterava; o único jeito de pegar a informação sem quebrar a responsabilidade de ninguém era pela camada anticorrupção, com volta por mais de um microsserviço (cada um com seu micro database) e duplicidade de dados. Até onde o autor ficou na empresa, a camada não tinha sido retirada. Era uma tabela "monstro", com muitos campos, usada em data warehouse/relatórios.
- **Outras arquiteturas de serviço.** O padrão é aplicável a outras arquiteturas, mas é uma dor: tecnologias diferentes (SOAP, FTP etc.) e manter todo esse catálogo tecnológico de integrações numa única camada intermediária eleva a complexidade.
- **Consistência transacional.** Se há consistência forte (gravar nas tabelas A, B, C para depois fazer commit), é dor: transação aberta por muito mais tempo gera timeout (do banco, por exemplo), e é preciso tratar o estouro e desfazer também no microsserviço. Se há transação aberta no legado e a resposta depende de microsserviços (no exemplo: pessoa, telefone, endereço, e-mail — talvez e-mail e telefone já em microsserviços), o ideal é ter uma transação do lado dos microsserviços também, com **encadeamento de transações**. Nem toda tecnologia suporta **propagação de contexto transacional** de uma camada física para outra. Se houver muito disso, talvez seja melhor a camada anticorrupção **estar dentro do legado**, onde se consegue propagar o objeto de transação, que depois da persistência nos microsserviços é devolvido. O protocolo SOAP permite propagação (principalmente com SQL Server), mas o ponto negativo é a **latência da conexão aberta**: propagar via HTTP, 2–3 segundos "é uma eternidade pro banco". Reusar a mesma transação em outra conexão é suportado, mas são duas conexões abertas; faz-se commit primeiro no lado do legado e, após o "commit geral", o outro lado fecha a comunicação e efetiva o commit; se a comunicação falhar, faz rollback de tudo. Com microsserviço chamando microsserviço, tudo preso num contexto transacional, vira dor. Alternativa: usar padrões de consistência mais fraca, como **Saga**, do lado novo — mas aí se casa transação forte de um lado com consistência mais fraca do outro, "vai ter que dar algumas voltas". "Não tem uma resposta fácil"; com muita dessa dor, o autor iria para trazer a camada para dentro do legado — mas aí, se for preciso evoluir tecnicamente algo para conectar nela, altera-se todo o legado. Avaliar direitinho.

## Requisitos arquiteturais: quando aplicar

**Atendidos (padrão ajuda):**
- **Time to market:** o padrão ajuda a resolver o problema de tempo de entrega.
- **Manutenibilidade:** evita ficar alterando o legado; altera-se tudo dentro da camada. (Embora várias camadas dêem trabalho com o tempo, sem elas a evolução do microsserviço "evolui o legado": a dor.)
- **Integrabilidade:** o padrão ajuda amplamente na integração entre legado e versão nova.
- **Adaptabilidade:** flexibiliza o legado em função das alterações que vêm com os microsserviços.

Racional: se esses quatro são altos (time to market, manutenibilidade, integrabilidade, adaptabilidade são importantes para a empresa), o padrão faz sentido. Se a manutenibilidade não é tão importante (raro; talvez uma aplicação de baixa relevância, onde se continuaria com planilha Excel se o sistema caísse), mas o time to market é (exemplo: alguém "carimbando a nota fiscal" que não se quer pagar parado), ainda pode valer.

**Atendidos parcialmente:**
- **Segurança:** o legado e os serviços novos já têm sua segurança; a camada que faz o parse pode ser uma vulnerabilidade grande, abrindo espaço para invasão dos dois sistemas, inclusive pelo mundo externo se for uma API acessível publicamente (o legado pode ser mainframe, o outro lado web). Mais um ponto de preocupação.
- **Testabilidade:** dá para testar, mas há pontos complexos para teste unitário, principalmente por causa da volta ao legado; um caso de teste pode não refletir a realidade do legado, e uma alteração pode quebrar o legado; não se tem visão ampla integrada. É um componente apartado, mais difícil de testar.

**Inferidos / impactados parcialmente** (o autor diz que "inferido" = é impactado; "parcial" = tem contorno):
- **Disponibilidade:** depende do volume e da forma de escalar; a camada pode não suportar o volume de requisições; operações síncronas lentas, retries e timeouts podem fazer o tempo de resposta do legado subir, acumular conexões e derrubar a aplicação. "Coloquei como parcialmente sendo bonzinho, mas diria que pode ter impacto maior" (disponibilidade amplamente inferida).
- **Observabilidade:** mais difícil monitorar fim a fim e fazer trace completo; há um componente no meio onde pode acontecer muita coisa.
- **Experiência do usuário:** impactada pelo maior tempo de resposta (inclusive na aplicação nova que consome recurso legado).

**Inferidos totalmente (impactados):**
- **Performance:** certamente degradada; é uma camada a mais, no mínimo uma requisição TCP a mais; se há um TPS a atender, ele será degradado.
- **Escalabilidade:** escalar um lado não escala o outro; é preciso escalar a camada também (mais máquina, mais recursos); depende de infra, rede (talvez uma limitação), banco e FTP; "meio de campo que ferra a gente totalmente". Dependência forte de recursos de infraestrutura impacta a escala.
- **Elasticidade:** quase impossível; o modelo sobe e dificilmente desce (principalmente automaticamente), então não se reduz o custo de infra quando o volume cai.

## Quando aplicar / quando não aplicar

Para a maioria das aplicações vale a pena em migração de legado, **principalmente se o legado é pesado, antigo, com muitas funcionalidades**. Com tecnologia muito moderna e amplo suporte (REST etc.) talvez não. Se manutenibilidade não for importante, reconsiderar. Os requisitos norteiam a decisão: se performance, escalabilidade e elasticidade são altos ("não quero ficar pagando à medida que tenho menor volume"; ganho centavos por requisição), pode ficar mais caro. Não é fórmula mágica, mas ajuda: ter os requisitos ponderados, com criticidade clara e o requisito mais importante definido (no ARL/RAs: se o mais importante é performance ou elasticidade, que são inferidos, é para pensar fortemente).

**Quando não usar** (visto mais na literatura): quando há **diferenças semânticas significativas** entre os dois sistemas. Exemplo: o legado é orientado a **LOBs (linhas de negócio)**, modular; o novo é orientado a **jornadas**, com domínios em vez de módulos. Semanticamente é muito diferente, vai doer aplicar o padrão, e nesse caso nem mesmo o Strangler é fácil; vale mais "tombar" o sistema inteiro. Se há uma **versão intermediária** semanticamente mais parecida, o padrão vale a pena: desativa-se o legado primeiro e depois faz-se a mudança semântica final. Também vale quando há vários temas com semânticas diferentes que precisam se comunicar.

Na maioria dos casos de **planejamento de migração para microsserviços** (várias etapas, talvez versão intermediária) vale a pena: é uma camada que traz grande flexibilidade.

## Conclusão do autor

Não é uma escolha simples: parece "Easy" (uma camadinha que faz o parse de um lado pro outro), mas há vários pontos — comunicação, segurança, performance — e é preciso avaliar os requisitos e planejar. "A palavra mágica para todo trabalho de arquitetura é um bom planejamento: desenhar bem, pensar no máximo de situações possíveis." Recomenda orientar-se pelos **requisitos arquiteturais** para chegar nas decisões mais aderentes ao que a empresa mais precisa.
