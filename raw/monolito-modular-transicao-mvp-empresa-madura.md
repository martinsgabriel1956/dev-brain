# Monolito Modular: a etapa entre o MVP simples e a empresa madura

> Transcrição de vídeo (limpa e organizada; conteúdo original em português).

## O problema: o monolito virou espaguete

Fiquei muito tempo sem entender o conceito de **monolito modular**. Vamos falar um pouco sobre isso.

Imagine que você está construindo o seu software, o seu serviço — um "servição". Embaixo dele você tem o banco de dados tradicional. Aí você começa a criar uma classe de **produtos**. Em algum momento aparece uma parte do código responsável por **users** (usuários) — juntos ou separados de **autenticação**, sei lá, fica junto. Depois vêm **pagamentos**, **hotéis**, **modelos** de alguma coisa...

Conforme o monolito cresce, uma coisa chama outra, que chama funções de outra, que chama funções de outra — uma função chamando a outra sem muita organização, sem muito critério. De repente, no meio disso, o que você tem se parece com um **espaguete**: código espaguete.

Qual a saída dessa situação em que a gente se colocou conforme o serviço foi crescendo de maneira desorganizada e virou um projeto legado?

- Será que a solução é melhorar esse monolito?
- Será que é transformá-lo em um **monolito modular**?
- Será que é ir para um **monolito distribuído** ou para **microsserviços**?

Vamos debater quais opções temos para escalar um serviço cujo monolito ficou muito bagunçado.

## A saída "óbvia": quebrar em microsserviços

Muita gente, ao ver a gambiarra e o espaguete, pensa: "era tão mais fácil quando esse monolito era pequeno". Se era mais fácil quando era pequeno, então esquece essa história de monolito e vamos transformar isso em vários serviços pequenos. Aí teríamos a simplicidade em cada um dos serviços.

Cada um desses serviços pequenos é, em si, um monolito — e o conjunto de vários pequenos monolitos a gente chama de **microsserviços**.

Antes o código era completamente espaguete, uma coisa chamando as funções da outra de maneira desorganizada. Agora isso não é mais possível: o microsserviço de **produtos** não tem acesso às funções de **usuário**. Ele não consegue mais se comunicar através de chamada de função. Microsserviços **impossibilitam** que um serviço chame funções de outro. Eles têm que se comunicar por **protocolos de rede**, com **APIs expostas e documentadas**.

Ao forçar isso, tornou-se impossível transformar o código num espaguete gigante — porque um serviço simplesmente não consegue chamar o outro diretamente. A comunicação precisa passar por uma API (REST, GraphQL) sobre HTTP, ou por algo como **gRPC**.

A troca que fizemos foi: **substituímos uma chamada de função por uma chamada via rede**. Isso "algemou" a gente — travou nossas mãos e preveniu que o código virasse uma sopa. Mas nem tudo são flores.

## Comparação honesta: monolito × microsserviços

Não é tão simples quanto "fui escalando e do nada virei microsserviços", nem "microsserviços são melhores e monolitos são piores".

**Vantagens tradicionais do monolito:**

- **Um único deploy** — o código vai todo junto; você não se preocupa com versões diferentes (ex.: `user` na V2 e `hotel` na V3 podem gerar problemas — dor de cabeça extra para o time/DevOps).
- Tradicionalmente: **uma equipe, uma versão, um repositório** (há exceções a quase tudo isso — talvez menos à "uma versão").
- **Simplicidade** enorme: sem APIs entre serviços, sem comunicação por protocolos de rede (que adicionam latência e complexidade), sem orquestração mirabolante de deploys.

**Do lado dos microsserviços:**

- Vários **deploys**.
- Comunicação **via protocolos** em vez de via funções.
- **Overhead de DevOps** maior.
- **Melhor isolamento**.

Imagine 200 desenvolvedores fazendo commits, deploys e rollbacks em uma **única** code base — é complicado. Por isso o isolamento importa: se a equipe de **pagamentos** lançou uma versão com problema, ela faz o rollback só do serviço de pagamentos. Num monolito, com todas as equipes atualizando o mesmo software, não é tão simples: com boa observabilidade você até remove só o commit que deu problema, mas ainda tem que fazer deploy de tudo de novo (a não ser que use algo como **hot code swap** no Elixir — dizem que funciona).

Conforme a empresa escala, ter tudo separado fica interessante:

- Geralmente cada serviço tem o **seu próprio banco de dados** (tenho ressalvas, mas deixa quieto).
- Cada equipe é **dona** do seu serviço: um squad de seis pessoas para pagamentos, outro para users, outro para produtos, outro para hotéis, e três pessoas para DevOps. É quase como se cada serviço fosse **uma empresa diferente** que se comunica com APIs externas — e cada uma é uma empresa pequena, com produto conciso, simples de rodar.

Vimos essa migração nos últimos ~10 anos: praticamente toda big tech quebrou monolitos tradicionais (Facebook, etc.) — ou já nasceu distribuída (muito venture capital) ou ficou distribuída ao longo do tempo. Isso foi popularizado em blogs, artigos e palestras. Quando você escala o time para 100, 200, 1.000, 10.000 pessoas, esse tipo de solução faz cada vez mais sentido — não é realista esperar que 200 devs façam commits na mesma code base sem virar caos.

## O problema do "pulo" para empresas médias e pequenas

Mas: e quando não tenho vários squads de seis pessoas, e sim uma **empresa inteira de seis pessoas**? Cada um faz o seu serviço, o seu DevOps, o seu banco de dados — cada pessoa tendo que agir como uma empresa completa.

Para empresas médias (10, 20, 50 pessoas), quando o monolito começa a ficar pesado e difícil de todo mundo trabalhar junto, o pulo para microsserviços parece **muito doloroso** também. Ao mesmo tempo em que carregar o monolito fica trabalhoso, lidar com todo o overhead de DevOps e de comunicação entre serviços é difícil: você passa a pensar em **logging distribuído**, **falhas distribuídas**, e a otimizar performance (a chamada via API/rede demora **muito mais** que uma chamada de função). Se cada serviço tem seu banco, um único request do usuário pode exigir consultar **quatro bancos diferentes**.

Tem que existir um meio-termo. Monolitos são perfeitos para **MVPs** em muitíssimos casos. O Pieter Levels, sozinho, tem vários produtos de software — todos monolitos — e fatura milhões de dólares por ano. Dá para ir muito longe só com monolito. Seria idiotice sugerir que ele migre para microsserviços sendo um único dev, com produto simples (ele não está recriando a Netflix): com ~1 milhão de usuários, bota o monolito para rodar em três ou quatro máquinas para redundância, um load balancer na frente, uma réplica do banco, e acabou.

No outro extremo, quem sou eu para criticar Uber, Google, iFood, que fazem microsserviços — eles têm problemas e números que a maioria nunca viu. Mas trabalhei bastante em empresas de **médio porte** que esbarravam nas limitações dos monolitos.

## O monolito modular

O monolito modular surge da pergunta: **será que conseguimos aproveitar alguns prós dos microsserviços sem alguns dos contras?**

**Prós que queremos aproveitar:**

- **Melhor isolamento**.
- **Coibir o espaguete** — acabar com o código-sopa desorganizado.

**Contras que NÃO queremos:**

- **Comunicação via protocolos de rede** não é necessariamente desejável. Estamos num monolito e nosso problema, provavelmente, **não é de hardware**. Um problema de hardware seria: 80% da aplicação é minúscula (cabe numa maquininha) e 20% é um cluster de IA que precisa rodar em hardware totalmente diferente, escalando para várias GPUs — aí faz sentido comunicação via rede, porque rodam em hardwares distintos. Sem esse tipo de problema, comunicação via protocolo **não é vantagem**: é mais lenta. Chamada de função é mais rápida que chamada via rede entre máquinas diferentes.
- **Complexidade no DevOps** — se a empresa não é grande (às vezes nem tem alguém dedicado a DevOps), quero DevOps simples.

O que estou buscando, na verdade, é que **meus desenvolvedores tropecem menos uns nos outros** e que a code base seja razoável de manter.

Então esqueça a chamada via API. Pense que tudo isso é Java (ou qualquer linguagem): cada parte é um **módulo** — daí o nome monolito **modular**. E você **não** chama as funções do outro módulo diretamente: você se comunica através de **interfaces**, usando, por exemplo, o design pattern **Ports & Adapters** / **arquitetura hexagonal**.

O monolito modular é uma aplicação com **um banco de dados**, **um runtime**, dividida em **módulos**. Uma equipe (ou uma pessoa) pode ser dona de um módulo. Esses módulos têm **contratos** — que podemos chamar de **interfaces** —, expondo maneiras específicas de comunicação.

> Não leve para o mau caminho: pense em **getters e setters**. Você define como os outros módulos podem interagir com o seu módulo, do mesmo jeito que uma classe define como o mundo externo interage com ela via getters/setters.

Contrato é nome bonito para interface; o importante é entender que o módulo `user` define os modos de interagir com ele: o que tem de **input** e o que tem de **output**. Isso garante **separation of concerns** e **encapsulamento**.

Como continua sendo um monolito, temos **um único artefato grande** — mas, dentro dele, é como se houvesse vários microsserviços.

## Por que isso facilita a transição

Se o monolito virou monolito modular, transformar depois cada módulo no seu próprio microsserviço (quando necessário) fica **mais simples**.

Se você quiser extrair, por exemplo, o **módulo de IA** — para rodar em GPUs próprias, comunicando via rede, saindo de dentro do monolito — as **interfaces já estavam expostas**. Só precisa trocar **como** ele se comunica: antes era uma chamada de função nas interfaces; agora é uma chamada via **gRPC**. É a mesma coisa. Não havia espaguete antes, não há espaguete agora — só um módulo que foi retirado de dentro do monolito e virou um serviço.

## Conclusão

O monolito modular é uma **etapa** que facilita a transição de um **MVP super simples** (empresa pequena, poucos usuários, serviço simples) para uma **empresa madura** (número considerável de usuários, serviço crescendo em complexidade). É a boa arquitetura ajudando nessa passagem — sem obrigar o salto direto e doloroso para microsserviços.

---

*Nota: o vídeo original inclui um bloco de patrocínio (escola de investimentos UVP) não relacionado ao conteúdo técnico, omitido desta transcrição.*
