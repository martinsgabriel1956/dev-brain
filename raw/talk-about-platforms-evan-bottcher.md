---
title: "Do que eu falo quando falo de plataformas"
original_title: "What I Talk About When I Talk About Platforms"
author: "Evan Bottcher"
site: "martinfowler.com"
url: "https://martinfowler.com/articles/talk-about-platforms.html"
date_published: 2018-03-05
lang_original: en
lang: pt-BR
nota: "Tradução/adaptação livre em português para estudo. Citações curtas entre aspas preservam o original. Texto integral e figuras: ver URL."
---

# Do que eu falo quando falo de plataformas

> Evan Bottcher — 5 de março de 2018 — publicado no site de Martin Fowler.

Plataformas digitais bem construídas escalam a capacidade de entrega de software de uma organização. Mas muita gente falha ao tentar construí-las porque trata "plataforma" como um problema puramente técnico, ignorando que o problema de fundo é **organizacional**. Este artigo tenta definir com precisão o que é uma plataforma que vale a pena e o que é preciso mudar na organização para tê-la.

## O que é uma "plataforma", afinal?

"Plataforma" é um termo carregado e ambíguo. No nível organizacional, uma plataforma fornece um ambiente operacional no qual os times de produto conseguem construir e entregar funcionalidades mais rápido, com menos coordenação entre times.

A definição que o autor propõe:

> Uma plataforma digital é "uma fundação de APIs, ferramentas, serviços, conhecimento e suporte self-service, organizados como um produto interno atraente" ("a compelling internal product").

A Thoughtworks identifica que "plataforma" pode se referir a coisas bem diferentes — infraestrutura de entrega, APIs de negócio, remediação arquitetural, dados self-service, infraestrutura experimental, tecnologias de ponto de contato com o cliente. Este artigo foca especificamente na **plataforma de infraestrutura de entrega** (hospedagem em cloud, ferramental de DevOps, deploy).

## Primeiro, uma "não-plataforma": o caso BigCo

Para entender o que é uma boa plataforma, comece pelo oposto. A "BigCo" é uma grande empresa australiana de serviços financeiros. A área de infraestrutura/operações era organizada por **especialização técnica**: times separados de middleware, midrange, DBA, redes, serviço gerenciado de load balancer, serviço gerenciado de firewall, automação, monitoração, segurança, gestão de mudança/release.

Cada time:
- era gerido de forma independente, com estruturas de gestão e formas de trabalho diferentes;
- otimizava para a **eficiência interna do próprio silo**, não para a eficácia da entrega ponta a ponta.

Consequências observadas:
- mudanças simples de infraestrutura levavam **de semanas a meses**;
- um processo de mudança lento induz o comportamento de **minimizar mudanças**;
- falhas somam atrasos e geram aversão a risco;
- a qualidade se deteriora, porque manutenção e refatoração são adiadas;
- ciclo auto-reforçante: qualidade baixa → previsibilidade baixa → mais cautela → melhorias ficam ainda mais difíceis.

## O impacto do "acoplamento de backlog" (backlog coupling)

O conceito-chave: quando um item de backlog de um time de produto exige um item de trabalho correspondente **no backlog de outro time**, a produtividade despenca.

Exemplo citado: um estudo em uma empresa australiana de telecomunicações acompanhou centenas de tarefas. Tarefas concluídas por um único time serviam de linha de base; tarefas que dependiam de outro time eram **"10-12x mais lentas em tempo decorrido"** ("10-12x slower in elapsed time").

Problemas gerados pelo acoplamento de backlog:
- reduz throughput e capacidade de resposta ao cliente;
- força planejamento de longo prazo só para administrar dependências;
- corrói a responsabilização (accountability) do time pelo resultado — dano de motivação;
- estimula terceirização de culpa e reduz o impulso de melhoria contínua;
- sobrecarrega os times de serviço compartilhado, que atendem vários clientes exigentes;
- abordagens de "Agile em escala" acabam trocando autonomia/responsividade por alinhamento.

Requisito que emerge para a plataforma: **reduzir o acoplamento de backlog via self-service**. Isso significa self-service de:
- provisionamento;
- configuração;
- gestão e operação.

## A "private cloud superficial e feita pela metade" (half-arsed)

Na BigCo, reconheceu-se a necessidade de self-service, mas não se quis reestruturar a organização de infraestrutura. A tentativa de solução: uma ferramenta self-service para instâncias de computação.

- os times podiam requisitar VMs a partir de templates fixos;
- mas as instâncias continuavam travadas ("locked down"): mudar configuração ainda exigia ticket;
- capacidades reais de self-service (instalar pacotes, redes, storage, load balancers, monitoração) continuavam bloqueadas;
- o time de infraestrutura não quis quebrar os silos nem transferir responsabilidade/acesso.

Resultado: **nenhuma melhoria significativa** no ritmo de entrega. Era controle central maquiado de self-service.

A alternativa que os times acabaram adotando: **AWS**, por ser completamente self-service e ter fronteiras de responsabilidade claras. Os times de entrega "estouraram a boiada" ("stampeded") em direção à AWS como fuga das restrições internas — trazendo junto o mantra **"you build it, you run it"**.

## Autonomia acelera o time-to-market e aumenta a inovação: o caso WebBiz

O padrão organizacional default é o mandato centralizado de "construir para reúso" (build for reuse). A "WebBiz" (grande empresa de tecnologia australiana/global, com centenas de engenheiros, vários desafios de legado) fez o caminho inverso durante uma migração de vários anos de virtualização on-premises para a AWS.

Abordagem da WebBiz: **"Team Managed Infrastructure"** (infraestrutura gerida pelo time).
- autonomia completa dos times de produto sobre a configuração da própria stack;
- mandatos centrais mínimos;
- decisões de tecnologia tomadas de forma independente;
- inverteu o default: favoreceu diversificação em vez de consolidação.

Benefícios observados:
- maior engajamento das pessoas;
- engenheiros com experiência mais profunda na stack;
- responsabilização pelos deploys estabelecida rapidamente;
- eliminou a maior parte das dependências entre times;
- atraiu engenheiros que valorizam autonomia e ownership.

## Diversificação tecnológica aumenta o arrasto (drag)

Eliminar o acoplamento de backlog não é de graça: a autonomia total cria um novo custo. Agora **cada time precisa decidir cada aspecto** de como constrói e opera sua infraestrutura, avaliando e escolhendo ferramentas continuamente.

Recurso citado como ilustração: o **Cloud Native Landscape** — um mapa lotado de opções open-source e comerciais, e que ainda por cima só mostra as opções já bem estabelecidas. Cada time teria que avaliar, escolher, integrar e operar cada uma.

Tipos de arrasto:
- **manutenção duplicada** de infraestrutura entre times;
- **overhead contínuo** de pesquisa/avaliação de escolhas de infra;
- **atrito na transferência de habilidades** entre times que rodam stacks diferentes.

Resposta da WebBiz: começar a estabelecer uma plataforma de infraestrutura de entrega mais clara, com **"sensible defaults"** (padrões sensatos). Tensão levantada: como fazer isso sem perder os benefícios da autonomia via novos mandatos?

## A plataforma como produto interno

Encontrar o equilíbrio entre autonomia e consolidação é difícil. A saída não é o mandato — é tornar a plataforma **atraente o suficiente** para que os times a escolham voluntariamente.

Por que só mandato falha: a infraestrutura compartilhada existente já tem um **monopólio**; pensamento de produto de verdade exige competição viável. Se o time é obrigado a usar, não há sinal de que a plataforma é boa.

Características de uma plataforma atraente:
- **self-service** para a esmagadora maioria dos casos de uso;
- **componível**: serviços discretos, usáveis de forma independente;
- formas de trabalhar **não engessadas**;
- onboarding **rápido e barato** (quick start, documentação, exemplos de código);
- comunidade interna de usuários rica, que compartilha conhecimento;
- **segura e em conformidade por padrão** (secure and compliant by default);
- **atualizada**.

Teste central: deve ser **mais fácil consumir a capacidade da plataforma do que construir e manter a sua própria coisa**.

Referência citada: a Netflix chama seu ferramental centralizado de **"the paved road"** (a estrada pavimentada). Os times não são obrigados a usá-la, mas se saírem dela assumem **todos os custos** de manter a alternativa — o que cria um incentivo natural em direção à plataforma.

Escopo da plataforma é maior que software/APIs: inclui **documentação, consultoria, suporte, evangelização, templates e guidelines**.

## "Espera aí… isso não é um 'time de DevOps'?"

Feito de forma ruim, sim — vira só um novo silo. Mas DevOps não deveria significar um time, um cargo ou uma categoria de ferramentas.

Citação de **Phil Calçado**: "perdemos totalmente a batalha do 'DevOps não é um cargo/time/ferramentas'" ("We totally lost the whole 'DevOps' isn't a role/team/tools' battle").

Se você for montar um time dedicado, defina o escopo claramente:
- **Times de aplicação**: constroem, fazem deploy, monitoram e ficam de plantão (on-call) pelos componentes de aplicação e pela infra de aplicação que eles provisionam;
- **Times de plataforma**: constroem, fazem deploy, monitoram e ficam on-call pelos componentes da plataforma e pela infra subjacente. Idealmente o time de plataforma **nem sabe** quais aplicações rodam em cima — só responde pela disponibilidade do serviço de plataforma.

O princípio **"you build it, you run it"** se aplica aos dois.

## Por onde eu começo?

Pré-requisitos para dar certo:
1. estar já saindo do funding por **"projeto"** rumo a **produto** como mecanismo primário (ver "products over projects");
2. a plataforma tem que ser um **produto**, com um time estável e de vida longa responsável por construir E operar;
3. disposição para transferir a responsabilidade de operar a aplicação da operação centralizada para os **times de aplicação**;
4. disposição para trocar consistência estrita de implementação por **autonomia e responsabilidade** dos times.

Armadilhas (gotchas) críticas:

1. **Plataforma incompleta**: infra/ferramentas/APIs não bastam. É preciso responder às dúvidas de adoção — exige consultoria interna, treinamento, evangelização e gestão de mudança.
2. **Requisitos desconhecidos**: você não consegue prever de antemão o que a plataforma precisa. Comece pequeno, a partir de necessidades reais e comprovadas; "colha" (harvest) soluções já provadas dos times de aplicação; crie capacidades em regime de joint-venture com times usuários; teste antes de escalar.
3. **Rótulo superficial**: não basta re-rotular a infraestrutura centralizada e travada existente como "plataforma". Colocar a etiqueta "platform" numa hospedagem virtualizada e engessada não muda nada.

---

## Frases-chave (originais preservadas)

- Definição: *"a foundation of self-service APIs, tools, services, knowledge and support which are arranged as a compelling internal product"*.
- *"backlog coupling"* — tarefas dependentes de outro time foram *"10-12x slower in elapsed time"*.
- *"sensible defaults"* — padrões sensatos que o time pode sobrescrever.
- Netflix: *"the paved road"* — usar é opcional, mas quem sai paga o custo da alternativa.
- Mantra: *"you build it, you run it"*.
- Phil Calçado: *"We totally lost the whole 'DevOps' isn't a role/team/tools' battle"*.
