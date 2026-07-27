# Você Realmente Sabe Como Projetar Arquitetura Frontend de Grande Porte?

> Transcrição de vídeo (autor não identificado no áudio). Já em português — sem necessidade de tradução. Limpa e estruturada em markdown por seções a partir da transcrição bruta fornecida pelo usuário.

## Introdução

Vamos falar um pouco sobre arquitetura de frontend. Esse é um dos temas que mais sentimos falta quando o assunto é frontend, e é uma das perguntas que mais derruba pessoas em processo seletivo. Por quê? Porque as pessoas não olham para isso como decisão arquitetural, mas sim numa situação de "ah, é uma telinha, eu vou fazer, e é isso" — sem entender quais são as nuances dos tradeoffs dessas arquiteturas.

## Demo: Microfrontends Parciais

De cara, peguei uma arquitetura bem conhecida e bem cobrada: microfrontends. Especificamente, microfrontends parciais que representam partes da tela.

Nesse card específico, se a gente inspecionar, vamos ver que tem um Shadow DOM — que é basicamente esse microfrontend. Tenho outros ali: um em React, um em Angular e um em Solid.js. Cada um deles é um projeto rodando em porta separada, host separado. No `localhost:5001` está o React, no `5004` o Angular, e também o Solid.js. Esse Shell incorpora todos eles.

Como ele sabe qual microfrontend exibir? Ele começa pelo view e dispara um evento, e ele troca o card. Consigo disparar um evento pelo console e ele muda — por exemplo, mudo para o do Angular, emito o evento, ele escuta e faz a mudança. Mudo agora para o do React — ele muda também.

**Qual a vantagem desse modelo?** Temos projetos rodando em portas separadas, hosts separados. Eles não se conhecem e se comunicam via eventos — o projeto React não conhece o Angular, mas ao clicar na tech Angular ele emite um evento que mostra o projeto Angular. Temos um grau de desacoplamento alto, e é isso que vendem quando querem que você aprenda microfrontends ou tome uma decisão desse tipo: "a gente pode criar polirrepos, cada projeto é um repositório, como são 100% independentes podem ter CI/CDs totalmente independentes, e a gente só se comunica por eventos — cada um cuida da sua parte, o ownership de cada repo é de um time."

## O Que Fica Escondido Nessa Venda

Essa é a imagem que todo mundo já viu 300 vezes no LinkedIn quando o assunto é microfrontends: uma UI composta por vários frameworks, com versatilidade alta. Mas isso não se mostra verdade no dia a dia.

**Primeiro — performance.** Você não quer quatro frameworks na sua tela. Um dos maiores oneradores de performance é JavaScript. Você não quer gerar quatro componentes com quatro frameworks diferentes e fazer eles coexistirem na mesma tela — isso estraga a performance brutalmente.

**Segundo — CI/CD.** Será que você realmente quer repositórios separados com CD 100% separado? Se eu tenho seis microfrontends, são seis "disses" diferentes, seis para dar manutenção. Será que você realmente quer repositórios 100% independentes?

**Exemplo de versionamento.** Supondo que todos os microfrontends tivessem React: se eu fizer um bump de versão, isso gera quantas atualizações? Seis projetos para atualizar. Será que isso é prático para o dia a dia?

**Exemplo de mudança num Design System.** Tenho um microfrontend parcial e um DS, e preciso mudar um componente do DS. Tenho que: modificar o componente, fazer um bump, ir no microfrontend, atualizar para a nova versão, conferir em tela, abrir um PR, fazer o deploy em produção e só então ver se ele foi substituído. Olha o tamanho do fluxo — isso atende o seu caso de uso?

Quando falamos em microfrontends distribuídos, geralmente temos uma complexidade muito alta que não atende a maioria das empresas. Isso traz uma complexidade muito além do que você precisa.

## Visualizando a Complexidade (Excalidraw)

Essa é a tela: `localhost:5000` é o Shell, que incorpora os cards View React, Angular e Solid.js, além dos eventos. Esses eventos, quando disparados, decidem qual card mostrar. Já dá para ver que ganhamos uma complexidade bem alta para fazer algo tão simples. Pensa no seu caso de uso real e complexo: quão viável é isso? Quanto de eventos você teria? Como ficaria a observabilidade disso? Como ficaria a governança se surgisse, por exemplo, uma vulnerabilidade como a que surgiu no Axios ou no Next? Quanto tempo levaria para atualizar em todos os locais?

Por que eu bato nessa tecla? Porque essas estratégias de microfrontends e polirrepos são muito vendidas em bigtechs, que têm ferramental, controle e capacidade de tolerar esse tipo de complexidade porque automatizaram parte do processo. Mas a maioria das empresas de pequeno e médio porte não tem esse ferramental. Essa decisão pode parecer muito madura em termos de escalabilidade, mas está bem longe disso.

## Panorama de Arquiteturas de Alto Nível

### 1. Arquitetura Baseada em Layers (Camadas)

É a primeira arquitetura que você aprende: `pages`, `components`, `services`, separados por etapa/tipo técnico.

**Problema:** de cara, se você abre a pasta de componentes e tem 80 componentes lá dentro, você não tem contexto, não sabe quantos locais aquilo afeta, não sabe se é de um módulo específico ou de um caso de uso que aquilo atende. Isso naturalmente vira um problema bem rápido.

### 2. Arquitetura Modular

Em vez de ter tudo centralizado num único local, você começa a quebrar em módulos. Um módulo de "Alfa" tem componentes que só dizem respeito a ele — se eu alterar ali, sei que a alteração só afeta aquele escopo. Obviamente existem componentes compartilhados (pode ser uma pasta `core`, o nome é irrelevante — há nomenclaturas similares na indústria).

O principal dessa abordagem é criar **fronteiras entre módulos** — garantir uma atuação clara de escopo. Isso importa muito quando você quer escalar times: por exemplo, "o time A cuida de Alfa e de Pagamentos" — eles estão dentro dessa fronteira. Qualquer coisa compartilhada pode ficar sob responsabilidade de um time de plataforma, e quando é preciso fazer um "in-house" (mudança compartilhada), há um review obrigatório para garantir que nada existente vai quebrar.

### 3. Vertical Slice (dentro de um módulo)

Não é necessariamente uma arquitetura de alto nível por si só, mas um modelo de organização dentro do módulo. Quase sempre as pessoas associam vertical slice a arquitetura de grande porte, mas isso não é necessariamente verdade — é fácil entrar num terreno filosófico sobre "onde as coisas deveriam ficar".

Pensa numa funcionalidade dentro do módulo de Alfa que já nasce mais complexa, com aquelas ideias de "por que a gente não desacopla, cria um projeto separado?". Esse não é o momento — antes de qualquer coisa, isola a funcionalidade dentro do próprio módulo, cria um vertical slice ali para garantir que ela faça sentido naquele contexto. Se depois ela realmente precisar ser desacoplada, é só "arrancar" dali e colocar em outro local.

Essa abordagem é excelente quando, dentro do módulo, existem funcionalidades muito grandes — mas é importante que o time não fique 100% preso à filosofia de "isso deveria ficar dentro do módulo" ou "deveria ficar dentro da feature". Isso deve **facilitar, não complicar** — um ponto que já gerou bastante conflito em alguns lugares onde trabalhei ao ser tratado como regra rígida em vez de ferramenta prática.

### 4. Microfrontend Baseado em Rotas

Uma das arquiteturas favoritas do autor. Basicamente um proxy reverso: o que antes eram módulos com um único build passam a ser módulos com builds separados.

Pensa no monolito modular com build único: naturalmente você bate num tempo de CI/CD máximo, num tempo de teste máximo, e um deploy começa a esbarrar no outro — isso vira conflito. A partir disso, você consegue desmembrar a arquitetura para ter build separado: agora cada time faz seu deploy separado, com controle tranquilo.

O que antes era um pacote compartilhado passa a ser lib num monorepo — usando, por exemplo, Nx, que já dá ferramental para criar libs instaláveis no seu pacote, acessadas como se fossem uma biblioteca de fato.

Essa arquitetura entrega a maior parte dos benefícios com a menor taxa de complexidade: você tem uma estrutura similar à do monolito modular, gestão de libs (com um mono onde libs são instaladas), autonomia para deploy, autonomia para gerar build separado, autonomia para rodar só os testes do seu escopo — e não cobra uma complexidade absurda em observabilidade e governança, porque você consegue estruturar isso como um grafo de dependências: "atualizei um pacote, atualizem todos os locais que dependem disso" — simples, direto e efetivo.

### 5. Microfrontends Parciais (Orquestrados/Distribuídos)

A arquitetura demonstrada no início — partes da tela representadas por microfrontends independentes. Cada um depende de um host, todos levam mais JavaScript para o cliente, têm grau de complexidade alto, e qualquer coisa como observabilidade tende a virar um problema bem rápido.

## Escala de Complexidade

Transicionando de um **monolito modular com build único** para um **microfrontend baseado em rotas**, o aumento de complexidade é relativamente baixo — porque você consegue manter a estrutura que já tinha, só transicionando pacotes: o que era pasta compartilhada vira pacotes instaláveis (ex.: libs Nx), e o que eram módulos que serviam como fronteiras agora são módulos que representam builds separados de fato.

Já quando olhamos para **microfrontends parciais**, isso não é mais verdade — trazemos realmente bastante complexidade adicional.

## Conclusão: Onde Fica a Maior Parte das Boas Decisões

Ao olhar para arquitetura, a pergunta certa não é "isso aqui é uma arquitetura distribuída, então atende" — é olhar para todos os pontos: governança, observabilidade, caso de uso, evolução.

Uma arquitetura modular com um único build tem espaço muito grande para transicionar para builds separados sem muita dor de cabeça, porque você não se apoia de cara num modelo extremo. A maior parte das arquiteturas que você quer está **entre microfrontend baseado em rotas e monolito modular** — você não quer nenhum dos dois extremos (nem monolito de camadas único sem fronteiras, nem microfrontends distribuídos parciais).

## Fechamento

Os microfrontends de demonstração estarão no repositório do GitHub para quem quiser rodar — há comandos prontos para rodar um `dev` que já sobe todos os microfrontends juntos, para teste e comentários. Pedido de vídeo futuro sobre monolito modular.
