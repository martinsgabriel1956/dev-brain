# Arquitetura Orientada a Eventos — Eduardo Macris e Otávio Santana com Luiz Carlos Faria ("Gago")

> Transcrição colada pelo usuário, já em português (sem tradução). Limpeza de erros de reconhecimento automático de fala (ASR) e de pontuação; conteúdo preservado. Trechos ininteligíveis do original foram resumidos ou marcados com `[?]`. Falas sem atribuição segura de quem falou; as explicações longas são do convidado, Luiz Carlos Faria (Gago), e as perguntas dos apresentadores Eduardo Macris e Otávio Santana.

**Participantes:** Eduardo Macris (apresentador), Otávio Santana (co-apresentador), Luiz Carlos Faria, "Gago" (convidado; Solutions Architect / arquiteto de soluções e software).

---

## 1. O que é uma arquitetura orientada a eventos

O grande conceito está ligado a **como o acoplamento é realizado no código e na aplicação**. Quando uma aplicação conecta várias pontas (serviço que chama serviço, serviços externos, serviços internos), existe sempre a dinâmica de acoplamento: **quem chama precisa conhecer quem é chamado**. Isso gera dependência entre as duas partes, e **acoplamento é sempre custo, sempre um problema a ser tratado**.

A arquitetura orientada a eventos entra no meio dessa jornada para **desacoplar** esses pontos e simplificar a operação. As conexões existem porque o negócio as demanda (especialmente em microsserviços), mas dá para perguntar: "há um jeito melhor de fazer isso, reaproveitando mais, com menos complexidade?". Olhando para o mundo real, só se encontram eventos: a arquitetura de eventos é uma representação do mundo real no código, no dia a dia do projeto e da arquitetura.

## 2. Trade-offs: o que se perde

Toda escolha tem trade-off. Ganha-se desacoplamento entre serviços. Perde-se:

- **Complexidade**, em vários momentos: na modelagem e nas discussões. Em DDD e eventos, as discussões são enormes sobre "o que é um evento". Deixa de ser algo orgânico e passa a ser **planejado e estruturado**: separação entre comandos e eventos, tipos de mensagem que se propagam.
- **Discussão evento gordo vs. evento enxuto** (ver seção 5): quase um "sexo dos anjos".
- **Risco de a complexidade ficar grande demais** e a equipe não conseguir gerenciar, ainda mais com time jovem, sem gente experiente, com ausência de liderança técnica. Há um nível de segurança necessário.
- **Rastreabilidade**: é difícil saber de onde o evento saiu (pode ser consumido de vários lugares), para onde foi e o que aconteceu no meio. Quando há um problema, descobrir onde ocorreu e qual a origem costuma ser complexo. É natural em qualquer arquitetura distribuída (serviços entre si também são complicados), e há ferramentas de tracing que ajudam; mas, por exemplo, o RabbitMQ não propaga rastreio automaticamente `[ASR ambíguo: "Rabbit não tem interesse automáticos"; lido como "não tem tracing automático"]`. Depende da responsabilidade e do time.

## 3. Mensageria não é arquitetura orientada a eventos

Há uma diferença real entre usar mensageria no dia a dia e ter de fato uma arquitetura orientada a eventos. O convidado menciona **quatro padrões distintos** (lembra três explicitamente):

1. **Transferência de estado** (*event-carried state transfer*): pega todo o estado do que aconteceu no modelo e o transporta inteiro; quem tem interesse consome.
2. **CQRS**: separação de comando e consulta.
3. **Notificação de evento** (*event notification*): o emissor só avisa "aconteceu", sem passar o evento inteiro, e isso faz muita diferença.
4. Um quarto padrão, que ele não lembra no momento.

**Mensageria** é a forma de baixo nível, "rudimentar": há um mediador (broker), mas não necessariamente uma arquitetura pautada nele. Exemplo: um webhook recebe uma chamada HTTP; em vez de gravar direto no banco e consumir depois, coloca numa fila para garantir resiliência — com o consumidor offline, quando ele volta a ingestão continua. Isso é mensageria, **não** um evento: é pegar uma coisa, pôr numa fila e consumir depois.

Pensar em **eventos** é planejar a intercomunicação entre os pontos da aplicação: a publicação de um evento e o seu consumo. A relação com o mundo real: **aconteceu algo, há interessados, e os interessados passam a seguir o fluxo de negócio a partir do entendimento daquele evento**, em vez de receber um comando "faça isso agora".

Ligação com princípios de design: a palavra-chave é **encapsulamento**; um componente A quer enviar informação ao componente B e, a médio e longo prazo, não quer que haja conhecimento entre eles. Os apresentadores brincam que talvez "arquitetura orientada a eventos seja, no fundo, Open/Closed ou Dependency Inversion em escala" ("viajando bastante aqui"). O convidado diz que faz sentido em diversos pontos.

## 4. Evento vs. comando: quem é dono da informação

A virada de chave: de fora, olhamos e pensamos "Fulano tem que mandar mensagem para Ciclano". No modelo de eventos, **Fulano não manda mensagem para Ciclano; Fulano só diz que algo aconteceu**, e diz **pela ótica dele próprio**, não pela ótica de quem vai receber. Ele deixa de depender de quem consome e **não se importa quem consome**.

- A relação produtor→consumidores pode ser **de 1 para N ou de 1 para 0**. Pode-se publicar mensagem que ninguém consome por um mês, uma semana, um ano; se depois alguém se interessar, o dado já está sendo publicado e o consumidor está pronto para entrar.
- Em microsserviços busca-se independência (de roadmap, de deploy). A arquitetura de eventos mantém essa independência: "meu projeto publica um evento dizendo que aconteceu; quem se interessar, não me traga esse problema; eu não tenho que saber, não tenho que chamar você".
- **Comando é acoplamento direto**: quem manda o comando precisa saber o que e para quem mandar. Quem publica evento é o **dono da informação** (é ele, não o outro lado). Por isso o esforço é evitar, o máximo possível, enviar comandos.
- Exemplo da comunicação tradicional: se você só aceita receber mensagem em um formato seu, o outro lado precisa dessa carga cognitiva para produzir aquilo; se você mudar a forma de receber, o produtor é impactado. Com evento, **o produtor é autônomo**: pode mudar quando quiser e publicar um evento diferente sem precisar avisar todo mundo (até lançar nova versão e deixar os consumidores migrarem).

## 5. Evolução e versionamento de eventos; eventos gordos vs. enxutos

**Pergunta (apresentador):** mesmo com autonomia para mudar eventos, há consumidores dependendo; por retrocompatibilidade mantêm-se pelo menos duas versões rodando. Como convencer as pessoas a migrar, sem manter legado enorme?

**Resposta:**

- Esse problema é **mais comum com eventos gordos** (muitos dados). Evento gordo = **transferência de dados completa** para outra parte; isso gera **acoplamento alto** porque o formato do evento espelha os dados do banco: se você muda os dados do banco, provavelmente muda o evento. O evento **enxuto** (só identificadores, "uma troca de IDs") reduz o problema substancialmente, porque a evolução do banco não implica mudança no evento.
- Sobre gestão de versões de eventos: "nunca vi isso funcionar bem" quando chega o ponto de **não conseguir atualizar a dependência**: o que era para ser independente virou gargalo e trouxe dependência. Já viu **diretoria cair** e gerências de TI mudarem por causa desse cenário: é um tiro no pé, pois se vendeu a ideia de um benefício e ninguém prioriza os upgrades.
- Recomendação: **definir uma linha de tempo de fim de vida (*end of life*)** — um ano, dois anos, qualquer prazo arbitrado — e ela precisa ser respeitada. Arquitetura orientada a eventos não é para projeto pequeno ou amador, é para projetos maiores e com mais carga de engenharia, onde há mais chance de isso ser menos problemático.
- Se a frequência de mudança é alta, o problema provavelmente está no **design** da arquitetura / na escolha do tipo de evento.

**Tipos de evento e consequências:**

- **Evento enxuto** (só o identificador/raiz): muita gente reclama no primeiro contato ("o evento não está completo; preciso fazer uma chamada HTTP para obter o resto"). Questão: carga de rede. O contra-argumento: se o fluxo é com mensageria, **a resiliência do HTTP é assegurada pela mensageria** — se o serviço consultado estiver fora do ar, a mensagem não é processada, volta, é retentada em um ciclo, vai para uma fila de espera e, quando tudo se restabelece, é processada de fato. Vantagem adicional: **toda a história de gestão de API** (autenticação, autorização, credenciais, *rate limiting*, gateway) é reaproveitada: sabe-se **quem consome cada tipo de dado** (um serviço consome o perfil completo, outro só o nome, outro nome e e-mail).
- **Evento gordo/complexo**: o produtor não sabe quem consome, talvez nem tenha mapeamento; **dado pessoal/LGPD** passa a ser preocupação. Já no evento enxuto, qualquer um pode consumir porque o ID não é relevante; o dado completo é buscado via API, onde se consegue **gerenciar quem consome e quem não**.
- Trade-off prático: se rede é um problema (construir muita rede para consultas), talvez seja melhor um evento mais gordo; o risco é a mudança frequente e o acoplamento. Neste caso é preciso um combinado muito maior.
- Preferência do convidado: **começar pensando em evento enxuto como primeiro pensamento**; o evento gordo é possibilidade e fica no jogo, mas **é a segunda opção — é preciso provar que a primeira não é boa**. Há muitos casos (sincronização, por exemplo) em que enviar o evento inteiro faz sentido.
- Sobre empresas grandes vs. pequenas: depende do projeto e da cultura, mais do que do porte. Em projetos mais estruturados, a equipe de TI se preocupa mais com o volume/tamanho do evento.

## 6. Hype e adoção sem necessidade

**Pergunta:** a arquitetura orientada a eventos ganhou tração; sempre existe o risco de adotar por puro hype. Já viu uma aplicação que usava e claramente não era boa opção?

- É o "CRUD de DDD, CRUD de eventos, CRUD de microsserviço": sempre assim. Em projetos de GitHub/teste em casa é natural encontrar essas "bizarrices". Em empresas também: não há as condições necessárias para a arquitetura, então se faz "só para inglês ver" (de fachada) e **não se tem benefício nenhum**.
- Exemplo de fachada: fala-se de eventos e separação de comandos, mas o resto é **hiperacoplado**, e os serviços **compartilham o mesmo banco**. É o acoplamento máximo: não há roadmap independente. Mesmo cenário de microsserviços que não fazem sentido porque, na prática, são uma coisa só.
- Muitos desses projetos partem do **banco de dados** e não de um modelo de domínio: não há camada intermediária. Boa parte vem de **portes de código procedural** (a "arquitetura de 2002", procedural e ligada ao banco), que ainda se encontra hoje em alguns projetos (hoje, graças a Deus, não é a maioria).
- Falta frequente: **discussão mais profunda sobre domínio** (o que faz parte do que) antes de pensar a arquitetura.
- Um dos apresentadores cita o **paradoxo da escolha**: hoje há muito mais ferramentas e soluções que deveriam gerar produtividade, mas geram complexidade, porque, havendo muitas opções, tendemos a seguir o hype.
- Caso extremo citado por um apresentador: uma startup que parou **três meses sem entregar nenhuma funcionalidade** porque decidiu fazer tudo orientado a eventos e contratou três squads (times) `[ASR confuso: "contratou Três Fronteiras"; lido como "três times/squads"]`.
- **Papel do arquiteto**: técnico comunicador, com experiência e "sentido de aranha" para saber se é o caso. O convidado admite ter **viés**: sabe que defenderia por seu viés, então precisa se conhecer e pôr isso como **última opção** na mesa, para ser justo.

## 7. Como adotar uma tecnologia nova pela primeira vez

Opinião própria do convidado, que ele mesmo diz ser **controversa**: a **primeira adoção** de uma solução/ferramenta na empresa deve ser **com o pé nas costas** — com conforto, não com o caso de uso mais crítico.

- A lógica: o primeiro projeto precisa dar segurança política ao projeto, à equipe e à diretoria. Escolher um caso de uso que se sabe que vai funcionar, para que, no segundo, haja confiança. Pensar "onde posso aplicar isso agora com segurança" e "como faço isso agora para usar mais no projeto daqui a dois meses (talvez uma nova fase do mesmo projeto)".
- Exemplo "bobo": mensageria — primeiro caso de uso é **envio de e-mail**. Não traz grande benefício de negócio, mas tira carga da aplicação e dá conforto ao time com o comportamento da ferramenta, reduzindo a carga cognitiva de entendimento.
- Risco de não fazer assim: **trazer risco demais para a primeira implantação**.
- Contraponto de um apresentador: como saber que não se está dando "dez passos além"? E se o futuro imaginado não chegar, a complexidade foi criada na expectativa de um futuro que era ilusão; depois que o tempo passa, é fácil ver isso, mas no começo não é. Também há risco de se antecipar demais.
- Convidado: existe um nível de projeto em que DDD não faz sentido (projeto pequeno), mas a maioria dos projetos passa um pouco desse limite. É questão de experiência e expertise; "você não joga com a sorte nem com o dinheiro do cliente". Algumas soluções ajudam quase qualquer projeto — **mensageria e cache** — "é muito difícil não tirar proveito".
- Cenários clássicos de benefício claro: **Uber, iFood, e-commerce** (muito volume de eventos, muitos sistemas internos/externos a notificar). Para esses, é como "isto é um carro, então precisa de quatro rodas".

## 8. Dores que indicam que a arquitetura se aplica

Ao pegar times que ainda não usam eventos e para quem faria sentido, as dores mais comuns:

- Acoplamento: a API de um time muda e os outros quebram; "tenho que esperar o outro time subir a versão"; "o serviço do outro lado caiu e capotou o meu também".
- São dores que aparecem principalmente em **mensageria**; quando se entra no conceito de eventos, observa-se que, mesmo trocando por mensageria, **o acoplamento continua**: o componente que deveria ser autônomo ainda olha o fluxo como um todo para saber quem é o próximo passo, e precisa saber para quem enviar e o que o outro precisa receber (a "escada" em que cada um manda mensagem ao próximo).
- Roadmap que não destrava; dependências das quais não se consegue desvencilhar.
- **Complexidade**: "nunca vi isso ser simples; se alguém esbarrar num cenário simples, me avisa". Com time mais jovem é mais complexo; com time mais antigo, há o risco de sobre-engenharia — também complexo.
- Esses ganhos de desacoplamento têm de vir com **interação de equipes**: se é preciso abrir solicitação a outra equipe para ter acesso a um serviço (ex.: chaves), está complicado demais. Toda a infraestrutura de API existente (gestão de chaves, gateway) continua sendo usada, só que **mais para consulta**.

## 9. Maturidade da empresa e do projeto

O que mais faz diferença é a **maturidade** da empresa e do projeto:

- **Pessoas**: como a empresa contrata? Se só contrata júnior, quanto mais complexa a arquitetura, maior o desafio de aceitar pessoas novas e formar quem chega; é preciso frear nas novidades porque isso é disruptivo. Com distribuição razoável de níveis, há quem ajude os novatos e é mais fácil absorver.
- **Projeto**: é um projeto pequeno, um microsserviço, um e-commerce, um novo iFood? Para onde vai?
- **Papel estratégico do arquiteto**: entender a visão de futuro do projeto (2, 5, 10 anos) dá um norte do que desenhar e facilita transpor o MVP para a "fase 2" quando for reconstruído.

## 10. Encerramento

O convidado divulga seu blog (cerca de dez anos na versão atual; 13 contando o anterior), sobre ciclos de software e arquitetura de soluções. Os apresentadores agradecem.
