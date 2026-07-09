# Como Evitar o Over-Engineering

E aí galera, beleza? Eu tava vendo um vídeo do David Farley que saiu esses dias sobre esse assunto — como evitar o over-engineering — e aí quis fazer um comentário aqui, meus cinco centavos sobre esse assunto, que é muito importante e que a gente de fato tem que tomar cuidado.

## O mito do triângulo de ferro

A primeira coisa que eu queria falar aqui para vocês é o seguinte: existe um mito que é a ideia do triângulo de ferro. Aquela ideia de que quando você quer, por exemplo, uma coisa boa, barata, e que seja entregue rápido, você não consegue ter essas três qualidades — você tem que escolher duas das três.

No que diz respeito a software, isso não é verdade. É um mito — por exemplo, que a velocidade de entrega briga com a qualidade, então, se a gente for fazer algo de qualidade, vai demorar mais para entregar.

Estudos como o DORA — o DevOps Research and Assessment, que é aquele grande projeto de pesquisa que tá rolando há muitos anos e cujos resultados foram publicados no livro *Accelerate* — esses estudos têm mostrado que, na verdade, as equipes que entregam mais rápido também entregam com mais qualidade. Então, na verdade, essas coisas se correlacionam: quanto mais qualidade, mais rápido você consegue entregar; quanto mais rápido você consegue entregar, maior a qualidade daquilo que você entrega.

Isso obviamente é para software. Pode ser que para outros tipos de produto, outros tipos de coisa que a humanidade faz, de fato você não consiga entregar algo com qualidade e rapidamente. Mas com software, pela natureza do software, na verdade o que a gente precisa fazer é entregar rápido, em pequenos incrementos, para de fato colocar aquilo em produção, para já ir testando, para já ir vendo se aquilo é realmente o que os seus clientes estavam querendo.

E com isso você não tem medo de fazer deploy — você faz o deploy contínuo, ou pelo menos você faz a entrega contínua (continuous delivery), você deixa sempre o seu sistema no estado em que ele pode ser implantado.

Então o pessoal do DORA tem descoberto isso: que a qualidade correlaciona com a velocidade. Em software, na verdade, quem entrega mais rápido em geral também entrega com mais qualidade. Isso parece um pouco contraintuitivo, porque quando a gente entrega, a gente tem medo de entregar as coisas, a gente tem medo de colocar as coisas em produção porque a gente tem medo de quebrar.

## Por que colocamos portões demais no deploy

Às vezes a gente fica colocando vários portões para o deploy — faz PR, faz code review, tem um monte de aprovações que têm que ser feitas para que você coloque algo em produção. Em geral, como é uma coisa que tem que ser aprovada, você vai ter que fazer uma coisa grande, um PR grande, por exemplo — e isso, na verdade, causa mais problemas do que ajuda.

Em geral, as equipes que são mais eficientes e mais efetivas em entregar software trabalham em incrementos pequenos, entregam com bastante frequência, e o software que elas entregam tende a dar menos problemas.

Então a gente já chega com essa ideia: não é que, se eu for fazer teste, se eu for fazer TDD, então eu vou entregar mais devagar, vai demorar mais — isso não é verdade. Em geral, quando você aplica boas práticas, na verdade você entrega mais rápido.

## A origem do ágil

Essa é a própria ideia do ágil. Acho que eu já contei para vocês aqui uma história lá da ThoughtWorks: um projeto que estava atrasado por um ano, e chamaram o Martin Fowler para ajudá-los. E a ideia do ágil, desde o princípio — que não se confunda com Scrum, que de fato essa palavra ficou confundida com esses processos que às vezes não levam à agilidade por si só — mas no começo a ideia do ágil era essa: vamos entregar pequenos incrementos rapidamente, já criar testes automatizados para aquilo, para que a gente consiga mudar o software rapidamente.

Então aquela ideia do inglês *change* do Extreme Programming: nós não teremos medo de mudar o software. A gente já tem por hipótese que o software vai ter que mudar, então a gente não tem medo da mudança.

## Qualidade interna e facilidade de mudança

E aí entra uma ideia muito boa que o próprio David Farley comenta, que é o seguinte: a qualidade, principalmente interna, do software está muito relacionada com a facilidade de mudar. Então, quanto mais fácil de mudar o software, melhor a qualidade — porque você consegue colocar mais features naquele sistema com mais rapidez e consegue colocar em produção logo, gerando valor de negócio.

Porque, olha, vamos pensar numa coisa muito importante: o software é um meio, ele não é um fim em si mesmo. O software está servindo para gerar um valor de negócio. Se você não está entregando o valor de negócio, o software não serve para nada. Então todas essas coisas que a gente fala aqui — de TDD, de arquitetura — tudo isso tem que ajudar você a entregar software com mais qualidade, mais rápido, e software que seja fácil de ser mudado.

Então o primeiro comentário é esse: não há contradição entre qualidade e rapidez de entrega em software.

*(Conversei sobre isso também com o Guilherme Fróes, que é um cara com muita experiência, que trabalhou na Thoughtworks e hoje trabalha no Google — se você não viu esse bate-papo, dá uma olhada, foi muito legal, a gente conversa também sobre essa questão do deploy, de não ter medo de fazer deploy, e que isso de fato vai melhorar a qualidade do software.)*

## O maior problema não é over-engineering, é under-engineering

Mas o over-engineering de fato existe, e é algo que você tem que tomar cuidado. Mas antes de falar de over-engineering e dos cuidados que você tem que ter para não cometer, eu só queria dizer o seguinte: o problema maior da nossa indústria não é over-engineering, mas sim under-engineering.

Tem esse comentário lá no vídeo do Farley — alguém falou exatamente isso, que a nossa indústria sofre por falta de engenharia mais do que por excesso de engenharia. Eu fiz essa pergunta para vários desenvolvedores lá no [comunidade/curso], e todo mundo foi unânime em dizer exatamente isso: que o maior problema não é o over-engineering, mas sim o under-engineering.

Porém o over-engineering existe. Então vamos falar aqui um pouquinho sobre como não cometer over-engineering.

## Problema 1: Perfeccionismo

Um dos primeiros problemas é o perfeccionismo — é você querer construir uma torre de marfim que nunca tem fim. Isso tem muito a ver com aquilo que eu falei de não ter medo de entregar.

Em geral, o que causa esse over-engineering no sentido de perfeccionismo é a falta de um objetivo — é a falta de você ter uma feature que você sabe que tem que entregar, e você ir lá e desenvolver uma solução que vai ser suficiente para o contexto que você tem agora, para o conhecimento que você tem agora do sistema, e entregar.

Engenharia é resolução de problemas. Então, quando a gente está desenvolvendo software, a gente está resolvendo um problema. Então é bom que a gente tenha na cabeça exatamente o problema que a gente está — pelo menos até onde a gente conseguiu entender esse problema. Mais uma vez: o software é um meio para resolver um problema que vai gerar um valor de negócio. Se você não tem bem claro qual é esse valor que você tá criando, você se perde em purismo de engenharia.

O pessoal do Clean Code, o pessoal do Clean Architecture — em vez de usar esses princípios para te ajudar a ter um software que é mais fácil de mudar, mas que você consegue entregar alguma coisa — fica perdido no processo, em vez de entregar logo.

Isso acontece muitas vezes por falta de conhecimento. Já falei aqui do "gamer" — aquela pessoa que não estudou direito, só tem algumas ideias vagas do que é o Clean Code, o que é o Clean Architecture, e aí tenta aplicar essas ideias sem saber muito bem por que está usando aqueles princípios, qual é o objetivo que quer chegar com aquilo. E aí a pessoa fica perdida nisso e não entrega.

Então, mais uma vez: falta de objetivo e muitas vezes falta de conhecimento. Engenharia de software não é perfeccionismo — engenharia de software é resolver um problema e entregar. A gente quer gerar valor de negócio o quanto antes, claro, de uma maneira sustentável, como eu já comentei aqui de acordo com a definição do DORA — a gente quer entregar valor de negócio rapidamente, mas de uma maneira sustentável, que a gente quer continuar entregando valor de negócio.

Então esse é um dos motivos de over-engineering: o perfeccionismo, a falta de conhecimento, a falta de objetivo.

## Problema 2: Falta de confiança

O segundo problema relacionado com o over-engineering é a falta de confiança — é aquela equipe que quer construir algo que é à prova de qualquer problema. Então, logo de início, a pessoa já pensa que o software tem que ser escalável, tem que ter performance ótima, e aí tem que usar Kubernetes, tem que usar microsserviços, tem que usar Clean [Architecture], tudo junto — aquele Frankenstein logo de início, que não vai te entregar valor de negócio.

### O exemplo do LMAX

O David Farley dá um exemplo muito legal do sistema que eles desenvolveram, o LMAX, que é um sistema financeiro. Logo de início eles já sabiam que o desempenho tinha que ser muito bom, o software tinha que ser capaz de aguentar muitas requisições e processar muitos dados.

Só que aí, o que eles fizeram, na verdade, no início: eles focaram num problema que era um problema essencial deles, e desenvolveram o mínimo possível para começar a rodar algo. Eu gosto muito daquela ideia do **esqueleto ambulante** ("walking skeleton") — aquela ideia é a seguinte: logo que você começa um projeto, em vez de você desenvolver um monte de coisa para colocar em produção só depois que você tiver uma feature completa, você desenvolve uma coisa pequena, que talvez não vai entregar muito valor, mas que é algo essencial para o projeto, e coloca para rodar — já coloca em produção. Aí você já vai ter que tomar cuidado com a infra que você vai precisar usar para colocar aquilo em produção, e aí logo você já tem algo rodando.

Foi isso que eles fizeram: fizeram um mínimo de arquitetura possível. Eles pensaram em serviços — havia dois serviços que tinham que se comunicar por meio de mensageria. E aí, por exemplo, eles usaram uma tecnologia de mensageria que não tinha uma performance muito boa. Eles sabiam que iam ter que trocar aquilo depois, mas pensaram: "vamos colocar para rodar, a gente sabe que isso aqui não vai ser produção [final], mas como a gente criou aqui uma abstração na qual a gente consegue trocar essa tecnologia de mensageria, então mais para frente, quando a gente for de fato colocar esse negócio para rodar, a gente pode trocar."

E foi de fato o que aconteceu: eles foram lá e mudaram para uma tecnologia super rápida na época, que usava uma comunicação binária. A solução inicial deles usava XML com HTTP, mas eles sabiam que não ia aguentar — mas a postura era: "vamos colocar aqui para rodar isso, e depois, quando a gente souber qual tecnologia de fato vai atender melhor a demanda, a gente troca."

Então esse é o segundo problema: você querer, de cara, desenvolver algo que é à prova de qualquer falha — você já faz algo que tem desempenho perfeito, que tem o banco mais rápido, que escala em total segurança. Você já lida com todos esses requisitos não funcionais de cara. Esse é um problema que vai gerar over-engineering.

## Recapitulando

Esse era o meu comentário para te ajudar a não cometer over-engineering. Recapitulando os principais pontos:

1. **Velocidade e qualidade andam juntas** — não há contradição entre entregar rápido e entregar com qualidade. Na verdade, em geral essas coisas estão atreladas, correlacionadas uma com a outra.
2. **Foco no problema** — cuidado com o perfeccionismo, cuidado com já tentar resolver todo o problema de cara, isso vai gerar over-engineering.

E, claro, tomando cuidado com isso, utilizando bons princípios de design, de modularização, de separação de responsabilidades, cuidando da coesão do seu sistema — tudo isso vai te ajudar a ter um sistema fácil de mudar. Porque se você não tomar o mínimo de cuidado com essas coisas, "a cobra vai te picar" ali na frente.

Então isso não é desenvolver pensando lá no futuro — é desenvolver pensando agora mesmo: "daqui a pouco eu vou me dar mal se eu fizer uma bagunça aqui, se eu não tomar cuidado com a separação de interesses, se eu não tomar cuidado com a coesão e com o acoplamento."

Então: usar o mínimo desses princípios de design, com foco em resolver o problema e entregar valor de negócio — porque, mais uma vez, o software é um meio, e não um fim em si mesmo.

Fiquem com Deus, e até o próximo vídeo.
