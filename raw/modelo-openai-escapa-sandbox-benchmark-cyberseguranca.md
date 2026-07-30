# O Modelo da OpenAI que Escapou do Sandbox Durante um Benchmark de Cybersegurança

Transcrição de vídeo em português (canal de notícias/mercado de tecnologia), sem necessidade de tradução. Fala corrida/coloquial reestruturada em markdown com uma seção por etapa do incidente, mantendo o conteúdo original sem sumarização.

---

Quando você vê esse tipo de notícia pode pensar que é hype, ou então entrar em completo desespero e achar que o mundo vai acabar amanhã. Mas na verdade você deveria olhar por uma outra perspectiva: não deveria ficar tão emocionado, e sim olhar de fato para os fatos, entender o que aconteceu e tirar proveito disso. É exatamente o que a gente vai fazer nesse vídeo. Mas antes de mostrar como você vai fazer isso, deixa eu explicar o que de fato aconteceu.

## O Contexto: um benchmark interno de cybersegurança

A OpenAI estava rodando um benchmark interno para testar cybersegurança — esse é o contexto. Não aconteceu do nada; o modelo não "acordou um dia" e falou "não vou invadir um outro lugar". Não foi assim.

Ao longo desse teste, dá pra ver o primeiro fato interessante — e tem vários fatos interessantes aqui que você precisa prestar atenção se você quer de fato se destacar nessa área, tirar proveito, empreender, arrumar o emprego etc. Tem coisas importantes acontecendo na indústria.

Primeira coisa: eles usaram uma combinação do GPT 5.6, Sol, e um modelo que ainda não foi lançado ao público, que está só dentro do laboratório. Primeiro ponto: a gente não sabe que modelo é esse. Segundo: como está sendo usada uma combinação de modelos, dá pra chutar que tá rolando aqui um subagente, uma run, etc. — o modelo está sendo usado dentro de um sistema para chamar API, gerenciar contexto e toda essa coisa. Isso só prova o que eu falo aqui há mais de um ano e meio: que essas coisas de fato são muito importantes.

A segunda coisa nesse teste é que esses modelos — diferente do modelo que você usa via API ou o modelo que você usa aí no Codex e tal — tiveram os guardrails removidos. O que são esses guardrails? Esses modelos podem ser usados, por exemplo, para ataque, como foi aqui. Só que, para fornecer ao mundo inteiro, os laboratórios fazem camadas de segurança para que o modelo se negue a fazer coisas que não são seguras. É basicamente isso. Então eles removeram tudo isso e foram rodar esse benchmark.

## A arquitetura: modelo, proxy e a internet

Existe uma explicação muito boa no blog do incidente, e eu poderia ficar lendo ele, mas eu vou fazer melhor: vou mostrar o desenho da arquitetura que eles explicam ali, para você entender de fato o que aconteceu.

A gente tem o modelo. E aqui tinha um **proxy**. Qual a função desse proxy? Evitar que esse modelo acesse a internet. Esse proxy tem um **cache**. E tem um outro elemento no nosso proxy: o **middleware**, responsável por gerenciar o proxy. E aqui a gente tem a internet.

Como o teste era desenhado: eles vão rodar esse benchmark de cybersegurança, e o modelo deve acessar apenas o cache. O que ele pega do cache? Pacotes. Por exemplo, imagina que o modelo queira analisar dados — sei lá, ele queria o Pandas — e aí ele vinha no cache e pegava o Pandas. Se não tivesse no cache, o proxy ia na internet, pegava o que tinha que pegar, e fornecia para o modelo. Então o modelo estava isolado da internet.

A primeira falácia que você tem que tomar cuidado é falar assim: "o modelo escapou para a internet e agora ele é o Ultron". Não é isso que aconteceu — tecnicamente é isso que estava acontecendo, mas aqui começa a ficar muito interessante.

## O zero-day: o modelo descobriu a falha no proxy

O modelo percebeu que estava sendo "proxado", digamos assim, e descobriu uma falha nesse controle. Por que essa falha é importante? Se a gente olhar o artigo, eles vão falar em **zero-day**. É uma falha que ninguém nunca identificou antes, nem o provedor do serviço, ninguém — uma falha que era desconhecida.

O modelo foi capaz de verificar que estava em um ambiente controlado, explorou (exploitou) esse problema e aí sim conseguiu alcançar a internet. Ele basicamente falou: "proxy, você não serve de nada, eu vou falar direto com a internet, você tá me atrapalhando" — e foi isso que ele fez.

Aqui está a segunda falácia que você tem que tomar cuidado, se você quer amadurecer seu entendimento na área: o modelo é guiado ao seguinte instinto — **chegue à solução que você tem que chegar por qualquer meio necessário, sem nenhum guardrail** — e ele leva isso ao pé da letra. Foi exatamente o que aconteceu: "por qualquer meio necessário" virou "eu posso dar um jeito de ir pra internet". Você pode pensar isso extrapolado para qualquer solução da vida. Isso prova que guardrails são importantes, apesar de todo o discurso do Amodei, da Anthropic, quando for lançar o próximo modelo e tudo mais — essa discussão é relevante, e existem oportunidades aqui.

## Na internet: a Hugging Face e as senhas vazadas

Chegou na internet — e aqui acontece a segunda coisa muito, muito interessante. O modelo estava na internet e foi procurar o que era relevante para resolver aquele problema, e achou a **Hugging Face**. O que tem lá? Um monte de modelo, e tem benchmark — show de bola. Até aí tudo bem, se ele consultasse o site como qualquer um de nós, estaria de boa.

Só que ele descobriu **senhas vazadas do servidor** na internet, usou essa senha para acessar o servidor, e fizeram um ataque com uma mudança de mais ou menos **17.000 linhas de eventos** (registros de eventos). O artigo da Hugging Face também vem falando sobre o incidente.

Isso já seria extraordinário: prova que o modelo não age sozinho, não tem consciência, não tem vontade própria — ele recebeu uma instrução e foi fazer o que tinha que fazer por qualquer meio necessário, e conseguiu fazer, inclusive por meios que a gente não espera. Isso é muito importante para a indústria porque, como eu falei em vídeo anterior, esses modelos mais modernos são um novo tipo de modelo que consegue ficar rodando por muito tempo, segurar contexto, e com um harness consegue fazer isso de maneira muito mais longa ainda. Essa é uma mudança interessante na indústria: como o modelo consegue encontrar caminhos que o humano não consegue encontrar tão facilmente, ele consegue fazer isso em volume e em velocidade muito rápida — a gente tem que achar um jeito de se defender, e aí tem um monte de oportunidade.

## A investigação: guardrails atrapalhando o próprio time de defesa

Se a gente vier no artigo, eles vão falar como fizeram isso, e tem um fato aqui muito, muito interessante que você, a partir de agora, não pode mais relevar: o time viu que estava sendo invadido. E aí, "tudo bem, estamos sendo invadidos, o que a gente faz agora?" E o que eles decidiram? Vamos usar IA para investigar o que está acontecendo. Eles viram os 17.000 tracings ali — estava acontecendo muita coisa mais rápido do que eles conseguiam dar conta no olho humano. Então: vamos usar IA para investigar o problema.

E aí o interessante: eles começaram a usar, seja o Fable, seja o GPT etc., na API, igual nós, mortais — e **o modelo se negou a ajudar**. Essa é uma simetria muito importante, uma notícia boa e ruim ao mesmo tempo. A boa: se esses modelos não vazarem sem guardrails, dificilmente a gente vai ter esse problema no curtíssimo prazo — não é para entrar em desespero, isso é um sinal de mercado. Um sinal de mercado porque: qualquer um, exceto quem tem acesso a esses modelos de maneira privilegiada, não consegue, por exemplo, debugar um ataque nesse nível com o próprio modelo.

E o que eles fizeram — esse aqui é um sinal de alerta muito legal: eles usaram o **GLM 5.2** (não o GPT), na própria infraestrutura, hospedado por eles — pegaram o peso do modelo, botaram lá, e aí sim, sem nenhum desses guardrails, conseguiram reverter o problema e investigar com o modelo controlado por eles.

## As lições e as oportunidades de mercado

De repente a gente vai chegar num ponto em que empresas precisam controlar os próprios modelos para ter soberania digital, digamos assim. E outra coisa muito importante: o mesmo modelo que pode atacar é o mesmo modelo que pode defender — e isso gera muita oportunidade.

Lembra quando o vibe coding surgiu e as pessoas falavam "o dev vai morrer, não existe mais"? Obviamente o dev evolui, assim como qualquer profissão — e esse aqui é uma prova disso. Por exemplo: eles usaram o GLM 5.2 sem guardrail e conseguiram reverter o ataque; nada impede de alguém usar esse mesmo GLM para atacar. O que acontece hoje se você colocar uma solução para ter um GLM na sua própria infraestrutura? Hoje é um preço absurdo, e pouquíssima gente tem essa oportunidade. Só que alguém vai tentar te atacar usando algum modelo, e você tem que usar alguma defesa que também é com algum modelo. Isso gera uma demanda muito grande, tanto por profissionais que saibam segurança e saibam aplicar, quanto pelas chamadas GPUs, modelos etc., para empresas como a Anthropic e a OpenAI — isso é ótimo para elas, porque mostra a demanda, mostra "nós somos muito importantes, vocês não conseguem viver sem o nosso serviço". Para elas é um golaço, porque fica esse jogo meio que de ameaça, meio que assim: "cara, se eu quiser, eu derrubo metade da internet aqui com o meu modelo".

Por outro lado, existe uma tremenda oportunidade — seja se você presta serviço, seja porque as pessoas falam "ganhar dinheiro com IA, cara, existe uma infinidade de meios de você ganhar dinheiro com IA, desde que você entenda o meio, entenda o mercado, entenda as oportunidades". Não precisa fazer o mesmo aplicativo que todo mundo tá fazendo. Se você, por exemplo, se tornar uma pessoa que entende de cybersegurança e entende que vai fazer uma combinação única, você vai ser importante no mercado onde você estiver, seja prestando serviço para empresa, seja arrumando emprego. Se você vai botar alguém de cybersegurança no seu time e ninguém sabe de IA, você tem um problema. IA hoje, em termos de conhecimento, eu costumo dizer que é como banco de dados: todo mundo que está na indústria tem que saber o mínimo, nem que seja para fazer um `SELECT`, nem que seja para montar uma tabela — todos na indústria precisam ter o entendimento de IA.

É exatamente disso que esse canal se ocupa: falar de mercado, trazer as oportunidades de fato. Isso aqui é uma oportunidade — se você hoje está me vendo, comece a estudar isso, comece a acompanhar isso, comece a olhar mais de perto: você vai ser um destaque daqui a alguns meses ou um ano, isso é fato.

Eu estudo IA e ensino IA para criar aplicações — não vibe coding necessariamente, mas para criar harness. Mas você pode se especializar em cybersegurança, outro pode se especializar em outra coisa — é assim que a indústria funciona: não é feita só de uma pessoa, é feita de um conjunto de coisas, e é por isso que fazer software não é tão simples quanto parece para quem é de primeira viagem — e é por isso que essa indústria é maravilhosa, tem bastante espaço para as pessoas boas que estão dispostas a fazer.

Espero que esse vídeo tenha sido útil. Esse canal traz mais notícias, é mais voltado ao mercado; meu canal técnico é o outro, provavelmente o melhor do Brasil no tema. Se você não está inscrito em nenhum dos dois, se inscreva — tem sempre vídeo de muita qualidade. Te vejo na próxima, abraço.
