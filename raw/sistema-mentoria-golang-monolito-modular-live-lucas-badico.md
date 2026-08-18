# Sistema de Mentoria em Golang — Monolito Modular Construído em Live (Lucas Badico)

> Transcrição de vídeo colada pelo usuário no chat (ASR bruto, sem pontuação, já em pt-BR — sem necessidade de tradução). Limpa e organizada em seções abaixo; código/estrutura de pastas extraídos da fala corrida.

## Quem fala e por que o vídeo existe

Eu tenho trabalhado em um projeto durante as minhas lives, e nesse vídeo eu quero mostrar o que é esse projeto e compartilhar dois aspectos: primeiro, como tem sido a experiência de construir algo em público; segundo, como as lives são "puro suco da realidade" de um programador. Eu sou Lucas Badico, dev mentor e apaixonado por programação, aqui no YouTube construindo uma comunidade de desenvolvedores que estão sempre em busca de evoluir. Nesse vídeo eu vou falar sobre o sistema que estou construindo em Golang — não poderia ser outra linguagem.

## Por que construir algo em live

1. **Exposição e criação de conteúdo.** Antes eu operava em quatro funções; atualmente só opero como criador de conteúdo e procurador de emprego. Construir em live é uma forma de estar com vocês, me expor, criar conteúdo, falar com a audiência.
2. **Testar um novo conceito de arquitetura mais modular.** Passei um bom tempo "lutando contra microsserviços" — não porque discordo do que eles trazem de bom (pensar em verticais independentes, crescer de forma saudável), mas porque uma série de microsserviços para um time pequeno cuidar vira uma loucura. Eu queria pegar a ideia de **monolito modular**, que vi em muitos projetos (inclusive no Nest, que eu não gosto tanto, mas que implementa essa ideia muito bem) e aplicar em Go.
3. **Prática de Go em si.** Quando perguntam qual linguagem eu trabalho, sempre digo três: Go, Elixir/Erlang ("leng"), Python e JavaScript. Dessas, Go é a linguagem em que tive muito mais contato na liderança do que na parte de codar. Desenhei muita arquitetura em Go, resolvi muito problema em Go, mas codar em Go eu fiz muito pouco — e, nas poucas vezes que fiz, criei alguns bugs que meu time teve que cuidar. Verdade feia sobre mim, mas estamos mudando isso. Tem uns dois meses que faço esse projeto — um mês praticamente no "Calendly" (o clone de agenda) e agora indo para a segunda/terceira semana no "bot". A evolução na linguagem está sendo incrível — o Lucas de agora é praticamente outro desenvolvedor comparado ao Lucas que começou.

## O que construir: o motor da escola

A aplicação escolhida é o motor da minha escola/mentoria. Ela precisa atender dores de agora e dores futuras (essas, conforme forem aparecendo). Duas dores atuais concretas:

- **Visibilidade de sessões de mentoria**: o mentorado não tem visibilidade das sessões que já teve nem do processo de marcar novas mentorias.
- **Integração de pagamento**: para cada mentoria, quase R$50 ficam retidos na plataforma de pagamento atual, usada apenas como link de pagamento — ou seja, praticamente nada do valor que a plataforma cobra está sendo aproveitado.

Decisão: construir o próprio sistema — o "veleiro" que vai operar a escola (referência a um vídeo anterior sobre low-code/no-code).

## Verticais do sistema (monolito modular)

- **Payment**: vai precisar ser implementado em algum momento, para resolver a dor de integração de pagamento citada acima.
- **Chatbot**: pivotou de "atendimento" para "monitor de live" — ajuda durante as lives a coletar informação, enviar perguntas etc. A ideia de chatbot de atendimento (para facilitar a jornada em geral) continua no radar.
- **Journey (Jornada)**: módulo que cuida do aprendizado — a ideia é que aprendizado é uma jornada, então tudo relacionado a isso (a "aventura de aprender") fica dentro desse módulo.
- **Appointment (Agendamento)**: primeira vertical implementada. Nasceu como um clone do Calendly — sistema em que você emite um link e a pessoa agenda um evento na sua agenda (no caso, mentorados agendam mentoria).

### Por que não usar o Calendly puro

O Calendly tem limitações no plano gratuito: só um tipo de evento (não daria pra ter múltiplos tipos de mentoria) e sincronização com um único calendário. Hoje já existem pelo menos dois calendários ativos (pessoal e comercial/mentorias) e um terceiro viria quando houver vínculo profissional (calendário de trabalho). O sistema próprio precisa juntar os três calendários e permitir outros tipos de agenda. Bônus desejado: um dashboard para o mentorado ver não só as agendas, mas o que aprendeu em cada mentoria e como está evoluindo — a ideia de jornada de novo.

## Stack tecnológica

- **Go** no core do sistema — escolha óbvia.
- **AWS / LocalStack**: uso intenso de ferramentas cloud, principalmente AWS. Exemplo de funcionalidade que vai usar cloud: notificação uma hora antes da mentoria ("você tá preparado para começar?"). Para desenvolvimento, montada uma versão local da AWS com LocalStack — configurar essa stack levou 6 horas (praticamente o primeiro vídeo do projeto).
- **Banco de dados**: PostgreSQL (Postgis) para o banco principal, além do DynamoDB (dentro das ferramentas AWS/LocalStack). No futuro, uso pontual de Redis em módulos específicos — a intenção é ir além de cache, já que Redis é muito mais poderoso do que "só cache".
- **APIs**: o core expõe tanto HTTP quanto gRPC — HTTP para integrações externas e frontend (ainda não existe solução muito boa de gRPC para frontend) e gRPC para comunicação interna entre módulos/serviços. A experiência com gRPC em outro projeto ("a saga do bot") mostrou o quanto isso ajuda a facilitar integrações internas.
- **Poucas libs externas**: Go levou a não depender de muita coisa de fora. Três libs citadas: **Gorilla Mux** (roteamento HTTP), o **pacote de RPC do próprio Google** (gRPC) e **GORM**. No "bot" precisou de mais coisas externas, mas no core o stdlib/ecossistema pequeno atendeu muito bem.

## Estrutura de pastas do projeto

```
scripts/         # scripts de inicializar, logar, rodar; toda a lógica do LocalStack
                  # (versão local da AWS para desenvolvimento)
lambdas/          # encapsulamento da lógica das Lambdas (usadas conforme necessário)
app/              # o "Core" — o monolito modular em si
  cmd/            # entry points: servidor HTTP e servidor gRPC (cada um roda como
                  # um "servidorzinho")
  internal/       # recursos compartilhados entre módulos, ou usados na camada de
                  # comando (entry points)
  modules/
    appointment/  # único módulo implementado até o momento nesta versão de dev
      handler/    # handler gRPC e handler HTTP
      model/      # modelagem: dado de negócio (Postgres) e DTO (transferência)
      *.pb.go     # arquivos gerados pelo protobuf
      *.proto     # definições protobuf
      repository/ # camada que conversa com o banco e recebe inputs do serviço
      service/    # lógica de negócio, usada pelos handlers
```

### Fluxo dentro do módulo `appointment`

O handler traduz os inputs que vêm de fora, usa o `service` para mandar esses dados pro domínio, pega a resposta e traduz de volta para a camada que chamou (no handler HTTP, um utilitário auxiliar só escreve o JSON de resposta). O handler expõe uma função `register` que recebe o router HTTP (implementação: Gorila Mux, usado via interface) e registra as rotas.

No `main` (entry point / `cmd`): instancia a `Database`, roda migração, instancia o servidor HTTP, puxa o `http handler` do módulo `appointment`, injeta esse handler dentro do servidor HTTP, e então dá `start` no servidor. Toda essa lógica é interna ao projeto.

## A tese do monolito modular: extração futura para microsserviços

A ideia central: hoje existe `appointment`; no futuro existirão `payment`, `journey` e outros módulos — um "monolito grande" com vários módulos internos. Se em algum momento `payment` precisar ser delegado a um time específico que quer controle isolado, basta remover a injeção/importação de `payment` do entry point atual e criar um novo entry point só para `payment`. A partir daí, um time cuida do módulo isolado e outro cuida do "monolitão".

Sobre dados: hoje é um único banco de dados. Se o projeto "explodir" em microsserviços, cada time pode clonar o banco atual, rodar uma migração e a partir daí ter um banco isolado por projeto/entrypoint. No início, o monolito será fácil de manter; num futuro próximo, a evolução para microsserviços — quando o projeto escalar — se torna natural a partir dessa mesma base modular.

## Sobre construir em público

Praticamente tudo está sendo feito em live stream — só coisas muito repetitivas ou sem importância são feitas fora da live. As gravações ficam abertas por uma ou duas semanas para o clube de membros; o histórico completo fica disponível para assinantes. Não é conteúdo pré-produzido "fora das telas" e depois mostrado pronto: é código sendo escrito ao vivo, com erros, aprendizado, e perguntas da audiência respondidas em tempo real.

## Desafios em aberto (mencionados como próximos passos)

A arquitetura modular ainda está "embrionária". Desafios explicitamente citados como não resolvidos ainda:

- Como lidar com **logs**.
- Como lidar com **observabilidade**.
- Como lidar com **autorização e autenticação**.

Convite: acompanhar as próximas lives para ver como esses desafios serão resolvidos junto com a audiência.
