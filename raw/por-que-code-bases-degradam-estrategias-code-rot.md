# Por que sua code base degrada — e como conter a entropia

> Transcrição de vídeo (pt-BR), limpa e estruturada em markdown. Conteúdo original já em português — sem tradução. Os trechos de publicidade (patrocínio no início e divulgação de cursos no fim) foram mantidos ao final, marcados como tal.

---

Essa é uma pergunta que eu tenho feito consistentemente há muitos anos da minha carreira, porque em todo lugar que eu passo eu vejo uma code base que vai aos poucos se degradando. Por que que a code base se degrada, e como que a gente pode tomar medidas para evitar que isso aconteça?

O natural, na verdade, é que ela se degrade mesmo — isso é o que é observado.

## Por que a code base se degrada

Você tem uma série de fatores. Acredito que o principal deles seja que **os requerimentos evoluem** e as demandas vão evoluir em cima de uma arquitetura estática. Muitas vezes não é planejado que a sua arquitetura evolua tão rapidamente quanto as demandas do sistema, porque a gente tá carregando conosco uma code base inteira de, sei lá, 5 anos de história. Não dá pra gente só refatorar tudo cada vez que mudar um pouco os requerimentos.

A gente tem também muitas **mudanças de contexto**. De repente eu fiz pensando que eu vou implementar algo no futuro, então eu fiz de alguma forma. Vamos supor: eu comecei a code base dando prioridade para funções puras, quis implementar um negócio mais funcional, e de repente a próxima pessoa que chegou na code base não tinha esse contexto, não tinha esse conhecimento, isso não estava documentado em nenhum lugar, e a pessoa foi para um lado muito mais orientação a objetos, que era o que ela sabia fazer. Meio que não dá para culpar ninguém. Quem que você vai culpar? A pessoa que começou a code base de uma maneira e não documentou, não explicou para as próximas? A pessoa que pegou uma code base e trabalhou da melhor maneira que ela conseguia? É difícil.

Um dos fatores terríveis, onde você consegue ver a code base degradando muito rápido, é **apagar incêndio**. Você precisa fazer um hotfix, você não tem tempo para fazer um fix decente, então você sobe qualquer coisa para corrigir o problema e joga a bola pra frente — leva nas coxas, empurrando o problema mais pra frente.

E você tem **cases não previstos**. De repente você fez a sua arquitetura, estruturou a sua base de código de maneira que você pensava que tinha visto todos os problemas que iam aparecer, mas surgiram problemas novos, não previstos, e aí a gente tem que fazer aquela gambiarrinha para nos adequar àqueles problemas novos. E essa gambiarrinha começa a degradar a code base. É assim que começa.

## Como a degradação evolui

Quando a code base começa a degradar, quando você tá apagando incêndio toda sprint e parece que tá toda sprint atrasado, o problema vai se agravando até você chegar num momento em que nada é feito — ao longo de uma sprint tudo que você consegue fazer é corrigir dois bugs e implementar meia feature. E aí surge a necessidade de criar uma code base do zero, uma **V2 do zero**, para tentar corrigir isso. E logicamente, por algum momento essa V2 vai funcionar, até que a V2 passe a ser antiga e apresente todos esses mesmos problemas.

## Sinais de que a code base está degradando

- **Você e sua equipe estão sempre atrasados.** Nenhum prazo nunca é cumprido, tudo tá demorando mais do que o esperado.
- **A velocidade cai.** A velocidade para tudo — para aprovar PR, para criar coisas novas. Parece que a code base não evolui.
- **Testes deixam de ser confiáveis.** Para compensar a perda de velocidade, a equipe começa a negligenciar testes: testes mais flaky, menos testes de integração, mais testes unitários. Uma code base muito complexa é muito difícil de testar, então a suíte de testes vai aos poucos sendo abandonada e negligenciada.
- **Monolitos distribuídos e "classes super-homem".** O código vai ter hotspots que fazem tudo — uma classe que faz absolutamente tudo, porque a gente foi só empilhando coisas ali naquela parte do código que a gente sabia rodar, que sabia instanciar. Uma classe que orquestra tudo e manda em todo mundo.
- **Os "Devs Gandalf" do código.** É aquele cara que tá na empresa há 10 anos e é a única pessoa que sabe como tal coisa funciona. O Gandalf é extremamente valioso — você não quer demitir o seu Gandalf, mas ele é **sintoma** de um problema: um código que não pode ser modificado facilmente. Ele agrega consigo todo o conhecimento necessário para continuar evoluindo uma code base extremamente caótica.

## Estratégias organizacionais / de projeto

### Nunca alocar 100% do tempo da equipe

Apresentada no livro *Principles of Product Development Flow* (não tem tradução em português). É óbvio para quem já trabalhou: no meio da sprint vão surgir bugs críticos imprevistos, o deploy vai falhar. Se você alocou 100% do tempo da equipe para tasks novas ou bugs que você sabe que existem, vão surgir bugs que você não sabe que existem e não vão ter tempo de ser resolvidos. Como você já gastou 100% do recurso, para corrigir emite dívida técnica — faz a gambiarra rápida.

**A estratégia:** aloque na faixa de **80% do tempo**. Os outros 20% ficam para bug fixes, refatorações e melhorias do que já existe.

### A regra do escoteiro

Tem que ser seguida e enforçada durante os PRs: você não pode pegar um código e deixá-lo pior do que estava. Ele sempre tem que estar igual ou melhor. A regra se refere aos escoteiros não deixarem lixo nos acampamentos — você sempre deixa o local onde acampou melhor do que estava. Você sempre deixa sua code base melhor do que ela estava.

Uma pequena margem de erro é aceitável **apenas em hotfix**, por causa da urgência. "Minha feature prometida pro cliente vai atrasar" não é justificativa para fazer gambiarra — ela vai atrasar de qualquer forma.

### A falácia do planejamento

Quanto tempo demora para implementar um sistema de upload de vídeos? Se você respondeu 1, 2, 3 dias ou uma semana **considerando que nenhum erro vai ocorrer**, tá errado — tem tipo 50% de chance de acontecer algum problema não previsto. E você considerou o tempo do PR? Alguém pede mudanças, você faz, envia de novo, pedem de novo, você faz de novo — já é pelo menos mais um ou dois dias.

Isso ocorre em todas as empresas. Se a sua empresa **não mensura o erro de planejamento** (planejou 40 story points, entregou 30; de novo 40/30; de novo 40/30), ela está vivendo num mundo que não é real: não faz ideia do quanto consegue produzir num dado tempo, nem de quando uma feature vai estar pronta. Estimativas costumam não funcionar muito bem — mas se você estima e nem mensura o erro da estimativa, aí não faz o menor sentido.

## Estratégias de código (e meio organizacionais)

### Code owners e arquitetura modular

Você pode ter pessoas responsáveis por um módulo / conjunto de responsabilidades, que documentam todas as partes externas desse módulo: quais são as APIs, quais são as partes que conectam com outro módulo, como ele funciona. E priorizar uma **arquitetura modular** com separações claras entre o que é responsabilidade de quem.

Isso entra no planejamento. Se a partir de hoje a empresa vai lidar com pagamentos, antes de implementar o primeiro botãozinho de checkout da Stripe ou da Abacate Pay, crie um **módulo de pagamentos**. O primeiro gateway vai demorar 2-3-4 semanas; o segundo vem rápido, porque a estrutura já está pronta.

### Um padrão bem definido, enforçado pela liderança

"Nessa code base a gente aplica DDD (domain-driven design)" — só um exemplo, não precisa ser DDD. Não importa qual padrão; importa escolher um que se adeque ao que a empresa faz e segui-lo majoritariamente (não necessariamente à risca). Se a sua empresa só tem staff engineers da Meta, não precisa de padrão. Numa empresa comum, com júniors, plenos e sêniores de capacidades bem diferentes, é bom ter um padrão. (Idealmente enforçado pela liderança — honestamente, ninguém escuta o júnior da equipe.)

### Testes de integração como critério de aceitação

Conversando com empresários e outros CTOs: algumas empresas acham teste unitário inútil, algumas acham end-to-end muito caro, mas **a maioria concorda que testes de integração têm bom custo-benefício**. Todo tipo de módulo que entra no sistema é legal ter algum teste de integração — dá pra usar isso como critério de aceitação da task. Teste de integração ajuda a prevenir um pouco o code rot. Não é bala de prata: é um trabalho contínuo de luta contra a entropia, que a gente geralmente perde, mas dá pra ir empurrando pra frente.

> "As pessoas não necessariamente odeiam Java. Elas odeiam trabalhar em code base de Java que começou 10 anos atrás e cresceu de maneira desorganizada." (Vale para PHP, Python, e daqui a um tempo, Next.js.)

**A maior parte disso é organizacional, não de código:** entender que a equipe tem uma certa capacidade — se você usa 100% dela, está criando dívida. Não planejar pro crescimento saudável de uma code base é, efetivamente, dizer que tanto faz: deixar a entropia crescer indefinidamente.

## Estratégias adicionais (secundárias)

- **Code freeze** — parar de fazer código e testar o sistema por um tempo. O autor não vê muito valor, mas alguma empresa pode ver.
- **Feature freeze** — por uma semana você não desenvolve features ativamente; só faz fixes em bugs críticos e dá uma repaginada na arquitetura: corrige TODOs, refatora gambiarras, implementa testes mais compreensíveis, conserta os flaky tests. Dá um respiro pra equipe.
- **Ferramental de apoio** — não é autossuficiente. Pode medir complexidade ciclomática, cobertura de testes (análise estática). Cuidado: **no momento em que uma métrica vira objetivo, ela deixa de ser útil** (Lei de Goodhart). "Quero 100% de cobertura" cria cultura de testes inúteis; mas 5% de cobertura pode ser sinal de que você não testa o suficiente.
- **Linters e tipagem gradual** — em linguagens não tipadas, tipar gradualmente. "Nessa code base de TypeScript, usar `any` é proibido" — ou você anota explicitamente, com comentário, o porquê. Na empresa do autor, o código não builda se não passar dessas regras.
- **Documentação** — testes como documentação: o título do teste "garante que um usuário não pode criar mais do que quatro produtos" enforça uma regra de negócio *e* a documenta. **ADRs** e documentos que explicam a tomada de decisão (por que algo foi feito de tal maneira). O problema da documentação fora do código é que às vezes o código muda e a documentação não — mas é melhor ter do que nada. Vale até via comentário: se um módulo faz algo de um jeito estranho, comente o porquê da decisão não usual. Assim o Dev Gandalf não precisa manter tudo na cabeça.

## Fecho

Nada disso é uma bala de prata que resolve os problemas da noite pro dia. É um trabalho contínuo de luta contra a entropia. Não vai prevenir o aumento de entropia, mas vai controlá-lo — permitindo que a equipe mantenha um bom pace na maratona que é o desenvolvimento de software por um longo período, em vez de um código que evolui rápido por três meses e vira legado em três meses.

> **Qualidade é uma prática, não é uma feature que você implementa.** Precisa estar acontecendo ativamente, semana após semana, sprint após sprint.

---

## [Publicidade — patrocínio de abertura]

"Tu já tá numa das melhores carreiras da atualidade, agora só falta começar a investir. Vem aprender a investir de verdade com a AVP, a maior e melhor escola de investimentos do Brasil."

## [Publicidade — cursos do canal, no fim do vídeo]

Curso de **estrutura de dados e algoritmos** (link na descrição): acesso a aulas antigas e novas; foco em DSA e LeetCode para passar entrevistas (Brasil, EUA, Europa); o próprio autor dá todas as aulas no Excalidraw; 2 meses para pedir reembolso.

Curso **"Roadmap pro seu próximo emprego"**: não foca na parte técnica, e sim em como se vender — currículo, LinkedIn, mapear e encontrar vagas (Brasil e "gringa"), cover letter e ir bem nas entrevistas. Descontinho especial para quem viu até o fim.
