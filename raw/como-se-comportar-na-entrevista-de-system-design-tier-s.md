Mesmo que você conheça 500 estratégias/conceitos de system design, tenha estudado cada uma delas e tenha tudo na ponta da língua para falar na hora da entrevista, infelizmente isso não é suficiente. Existe um pequeno detalhe, uma pequena maneira de pensar, que é o que diferencia quem passa e quem não passa na entrevista — porque para uma vaga de R$50.000/mês existem muitas centenas de pessoas concorrendo, que também estudaram meses de System Design (ainda mais numa vaga remota, com gente do mundo inteiro concorrendo). O que diferencia as duas ou três pessoas que avançam de fase e são efetivamente contratadas é exatamente sobre isso que este vídeo fala.

Quando chegamos nesse ponto de participar de processos seletivos para vagas desse nível, que pagam salários muito altos, onde as empresas procuram desenvolvedores realmente bons que agreguem ao time, não dá para considerar que simplesmente estudar/sistematizar os conceitos vai ser suficiente para passar na entrevista. O entrevistador está procurando algo além — ele não quer entender se você decorou a técnica certa de system design para usar no processo seletivo, ele quer entender a sua maneira de pensar e como você comunica o seu pensamento. Simplesmente decorar conceitos e falar "vou usar Redis aqui, vou usar Elasticsearch aqui" qualquer um pode fazer. Comunicar a ideia, o processo de raciocínio, o quão bem você explica o porquê de cada decisão que está tomando — isso é o que diferencia.

Até o fim deste vídeo você vai entender exatamente como se posicionar para se destacar dos outros candidatos. Isso não é só experiência pessoal do autor — é baseado também na experiência de outros desenvolvedores que já participaram de diversos processos seletivos e hoje chegaram no patamar de R$40.000 para cima, e que concordam que isso é um diferencial gigantesco na hora da entrevista.

Autor: Pedro Camaforte, desenvolvedor sênior, trabalha há quase dois anos para empresa do exterior recebendo em moeda forte. Este vídeo fecha a série de System Design do canal sobre os principais conceitos que mais caem em entrevistas de empresas Tier S — empresas que pagam salários muito maiores do que a média dos brasileiros, em moeda forte. É um fechamento: entender os conceitos é uma coisa, mas como aplicar tudo isso na hora real da entrevista — como começar, como desenvolver, como finalizar o processo seletivo ao vivo com o entrevistador — é o tema deste vídeo.

## Os 7 conceitos da série se encaixam nas features de qualquer sistema

Se formos propostos a desenhar o Instagram, por exemplo, e quebrarmos as features envolvidas, percebemos que:
- Upload de vídeo/foto → URL pré-assinada (vídeo 5 da série)
- Carregamento do feed → escalando leituras (vídeo 1)
- Contador de likes → escalando leituras (vídeo 2)
- Notificações → real-time updates

As features do sistema proposto vão se encaixando dentro dos sete principais conceitos cobertos ao longo da série. Claro que sempre vai ter alguma feature com um sisteminha específico não coberto — o autor pretende gravar vídeos sobre estratégias menos conhecidas, mas igualmente importantes.

Outros exemplos:
- WhatsApp: trocas de mensagens real-time, persistência de mensagens, escalando escritas
- Upload de arquivos: URLs pré-assinadas
- YouTube: upload de vídeos gigantes (URLs pré-assinadas), contador de views (escalando escritas), vídeo viral (escalando leituras), coletar métricas (escalando escritas)

Tendo a base das principais estratégias da série fixada, já se tem uma base muito sólida para começar a desenhar o sistema na entrevista. O que falta é identificar o desafio central do que foi proposto (ex.: YouTube é conhecido por upload de vídeo → pensar em URLs pré-assinadas de cara) e manter isso em mente. Como você desenvolve esse desafio a partir daí é onde o jogo muda — é o motivo deste vídeo.

## O erro clássico: sair desenhando sem entender o problema

Exemplo: o entrevistador pede para desenhar um encurtador de URL. O candidato já sai desenhando no whiteboard: "vou ter um servidor, um client fazendo as chamadas, para escalar a longo prazo vou precisar de vários servidores, um load balancer distribuindo a carga..." — só que ele nunca entendeu o problema de fato, nunca fez perguntas, nunca entendeu os requisitos do sistema. Presumiu e já saiu tacando informações no whiteboard.

Se o entrevistador quisesse um sistema para 100 usuários, por que colocar três servidores e um load balancer para um sistema de 100 usuários? Isso é queimar a largada. Mesmo que o sistema esteja correto e escale para milhões de usuários, esse comportamento provavelmente desclassifica o candidato — porque existem outras centenas de pessoas concorrendo pela mesma vaga, e algumas delas vão procurar entender o problema e se comunicar melhor, e serão essas que avançam.

Antes de sair desenhando qualquer coisa, é preciso comunicar ao entrevistador a linha de raciocínio e primeiro deixá-lo falar. **Isso não é um monólogo, é uma conversa.** O entrevistador não está ali só para observar enquanto o candidato desenha — é algo participativo, e ele espera que o candidato aja assim.

## O passo a passo que funciona para 99% das entrevistas

### 1. Entender os requisitos (funcionais e não funcionais)

- **Requisitos funcionais**: as features do sistema. Ex.: encurtador de URL → criar link encurtado, ler/redirecionar do link encurtado para o original.
- **Requisitos não funcionais**: as qualidades do sistema. Ex.: suportar 100 milhões de usuários simultâneos, latência baixa (responder/redirecionar em menos de 100ms), durabilidade (não pode cair, precisa funcionar 24h).

Você não precisa saber esses números de antemão — você pergunta ao entrevistador. Literalmente: "quantos usuários simultâneos a gente está considerando aqui?". Se ele responder, você anota. Se ele não quiser definir, você propõe: "que tal a gente considerar 1 milhão de usuários simultâneos?" — ele confirma ou não, e vocês ajustam juntos. Pode até propor um número menor: "vou fazer um sistema para 5.000 usuários simultâneos e a gente evolui isso ao longo da entrevista, o que você acha?". É literalmente uma conversa.

O mesmo vale para as features: se as duas principais (criar link, redirecionar) não forem suficientes, você pergunta o que mais adicionar (ex.: coletar métricas) e negocia prioridade com o entrevistador — inclusive dizendo algo como "vamos começar com esses dois principais e, se der tempo, falamos de métricas".

### 2. Discutir as entidades principais

Para o encurtador de URL: URL, usuário. Pode haver mais, mas isso não é definitivo — pode evoluir ao longo da entrevista. Essa etapa não deve tomar mais que ~2 minutos da conversa.

### 3. Discutir as APIs/interfaces

Ex.: `POST /urls` recebendo a URL original e um tempo de expiração opcional, retornando a URL encurtada. `GET /{código encurtado}` redirecionando para a URL original. Deve ser rápido e dinâmico.

Só depois de passar por essas três etapas (requisitos → entidades → APIs) é que se parte para o design. Conversar sobre isso antes ajuda a digerir o problema — fica visualmente claro tanto para o entrevistador (para onde a entrevista está indo) quanto para o próprio candidato (como modelar o sistema mentalmente).

### 4. Aprofundamento (opcional, escolha do entrevistador)

Só depois do design, se o entrevistador achar interessante, ele aprofunda em algum tópico (ex.: por que Cassandra e não Postgres). Esses aprofundamentos são mais comuns em vagas de staff engineer, mas podem acontecer também em pleno/sênior.

## A etapa de design: sempre explicar o porquê e os tradeoffs

O design é desenvolvido em paralelo com o entrevistador, fazendo perguntas, sempre atendendo aos requisitos funcionais e não funcionais levantados antes — que agora servem de base objetiva para as decisões (ex.: 100 milhões de usuários ativos → óbvio que serão necessários múltiplos servidores e um load balancer).

O ponto indispensável, que mais diferencia candidatos: **sempre explicar o porquê de cada decisão e o tradeoff que ela traz.** Não basta dizer "vou usar Postgres aqui", "vou usar Redis aqui", "vou colocar um load balancer de nível 4 aqui" — é preciso explicar o porquê (ex.: "vou usar Postgres porque para esse cenário ele é adequado por X, Y, Z, é um banco relacional que lida bem com esse tipo de aplicação"; "vou usar Redis porque vamos precisar de uma camada de cache"). Se houver um tradeoff, também deve ser explicitado ("temos um tradeoff aqui por causa dessa camada, mas com base nos nossos requisitos isso é aceitável porque conseguimos lidar com isso de boa maneira").

Sempre fazer pausas, comentar o que está sendo feito, pedir feedback do entrevistador ("você acha que isso faz sentido? Tem alguma decisão que poderia ser mais eficiente?"). O entrevistador não é um professor observando em silêncio até dar uma nota no final — ele espera participação, pode inclusive interromper e questionar a performance de uma escolha, pedindo para pensar em outra alternativa. Ele já sabe a solução mais adequada; o que está sendo avaliado é como o candidato se comunica, se comporta, como recebe e responde a feedback, se se adapta ou se fica na defensiva.

**O comportamental pesa mais do que o quanto você sabe de uma ferramenta específica.** Saber tecnologia é um pré-requisito — praticamente todos os outros 200 candidatos também sabem. O que mais será avaliado é o comportamental: como se posicionar, como se comportar. A recomendação é focar nisso e praticar — fazer várias entrevistas, ser rejeitado, e ir aprimorando aos poucos.

## Dois perfis de desenvolvedor

| Desenvolvedor 1 (reprova) | Desenvolvedor 2 (passa) |
|---|---|
| Assume o que precisa ser feito e já sai fazendo | Faz perguntas para entender o problema primeiro |
| Fica defensivo ao receber feedback | Recebe feedback de forma aberta e se adapta |
| Só cita tecnologias que vai usar | Explica o raciocínio por trás de cada tomada de decisão |
| A entrevista é um monólogo dele | Colabora com o entrevistador — é uma conversa |

O objetivo é se parecer com o Desenvolvedor 2 — é esse perfil que mais se destaca, mais passa nas entrevistas e consegue os salários de R$20-50k+.

## Como praticar

- Organizar "design meetings" no trabalho atual: propor junto com manager/colegas o desenho de uma nova arquitetura de sistema, se pronunciar e liderar esse tipo de discussão.
- Pegar desafios do canal (Uber, YouTube, WhatsApp — citados na série mas não aprofundados), se gravar resolvendo, depois assistir a própria gravação e identificar o que melhorar.
- Pedir para um amigo (de preferência mais sênior) fazer uma mock interview, fazendo perguntas como um entrevistador faria. Gravar, assistir, identificar acertos e erros, repetir.

Um salário desses não se alcança de uma semana para outra — o autor levou 4 anos para conseguir seu primeiro trabalho no exterior. É normal não se sentir sobrecarregado; aprendendo uma coisa de cada vez, o resultado vem.

O autor menciona planejar um vídeo futuro no canal aplicando esse framework completo sobre um sistema real (Uber), destrinchando cada feature na prática.
