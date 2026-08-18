# Spec Writer: Skill para Gerar Specs a Partir do PRD e os 7 Critérios de uma Boa Spec

Toda vez que a gente tem um projeto pessoal independente — se ele é um projeto legado, com codebase existente, ou não — a primeira coisa que a gente tem que fazer é entender o que vamos utilizar a nível de tecnologia. Por quê? Porque quando a gente tem isso, a gente consegue montar o contexto necessário para que a LLM produza aquilo que a gente quer.

O primeiro passo é: beleza, sei o que eu quero desenvolver, vou gerar um PRD. Lembrando, isso aqui é uma das formas — existem várias outras. O que é esse PRD? Basicamente é o que eu quero desenvolver da forma mais high-level possível. A ideia é que a gente não especifica tecnologia e tudo mais.

## O PRD de Exemplo

Vou apresentar esse PRD de forma bem rápida. Basicamente: sumário executivo, os problemas, a audiência, métricas de sucesso, e aqui começa a parte que a gente realmente vai utilizar, que são as histórias de usuário. Aqui dentro eu tenho a landing page, o sistema de autenticação, a parte de upload, a biblioteca de vídeos, a forma de organização, as tags para organizar os vídeos, o processamento em background — enfim, todas as features que este produto requer para que a gente consiga desenvolvê-lo.

A partir deste PRD, o que eu já ganho? Independente se você tem um produto já criado, código legado ou não, o primeiro ganho aqui é: OK, eu sei o que eu preciso resolver. E note que não tem nada aqui técnico — é basicamente "olha, tem essas features aqui" e pronto: camada de contexto fechada.

Quais são as outras camadas de contexto que eu poderia ter dentro de um Harness Engineering design? Eu posso, por exemplo, montar como eu quero o meu contexto visual — todos os design tokens, como vai ser utilizado, etc. Isso é mais contexto. Por enquanto a LLM pode inferenciar qualquer coisa que ela quiser, porque a gente só está falando de contexto.

## Da Feature à Spec

O que mais eu posso trazer para melhorar ainda mais? Eu posso começar a trabalhar com uma coisa que se chama spec. A partir daquele PRD, que tem diversas features, eu posso pegar uma feature em específico e falar: "pega esse carinha em específico e gere para mim um contexto específico num formato de especificação, para que, baseado nessa especificação, eu consiga começar o meu processo de desenvolvimento." É aí que entram metodologias como BMAD, SDD, e diversas outras metodologias que hoje a gente tem no mercado.

Na prática, como a gente faz isso? Através do uso de skills. Essas skills estão espalhadas na internet, mas uma coisa que a gente já reparou é que vocês vão, em dado momento, precisar criar as próprias skills para gerar essas specs.

Então, o que eu fiz: comecei apresentando o que é o meu projeto, depois fui granularizando isso, pegando uma feature e dizendo o que eu espero que essa feature seja desenvolvida através de specs.

## Exemplo: Spec de Autenticação

Vou mostrar uma spec para vocês — a de autenticação, por exemplo. Peguei aquela feature de autenticação do PRD e aqui eu já começo a ser um pouco mais voltado para o técnico, mas ainda no modelo high-level — não estou a nível de especificação de implementação, estou montando o que eu desejo.

Passo um overview técnico, passo o que eu espero desta feature, passo quais são os componentes que serão afetados — ou seja, a nível de arquitetura, o que eu espero que aconteça. Tenho aqui todas as roles. Depois tenho itens que podem ser ignorados e tudo mais. Tenho as minhas decisões técnicas de tudo que eu vou fazer: para autenticação, eu sei que tenho um processo de hashing, vou usar a biblioteca Argon2; ORM eu vou utilizar Prisma com Postgres. Note que não tem nível de implementação — tem basicamente o que eu espero dessa feature e como eu espero trabalhar nela.

Depois tenho os componentes que eu vou precisar criar e a descrição de cada componente. Tenho os contratos de API — o que eu espero de cada endpoint. Tenho uma parte de migration, uma parte de estratégia de teste, e por fim toda a feature agora descrita, aquilo que eu espero.

## A Skill "Spec Writer"

Como é que eu gerei isso? Simples — lembra que eu falei que existem metodologias para isso, eu utilizei SDD, só que eu criei uma skill que faz isso na prática, e essa skill inclusive eu disponibilizo para os nossos alunos. Essa skill se chama **Spec Writer**.

Eu tenho a minha skill de prompt pessoal — o "babá" — e eu espero que ela siga tudo isso. Para ela seguir tudo isso, eu utilizo uma execução por steps. A skill é dividida em seis etapas:

1. **Validar os inputs** do usuário.
2. **Processo de entrevista** — porque aí o que vai acontecer: "beleza, você quer criar um processo de autenticação, me diz como ela vai começar" — toda hora fazendo perguntas para inferir de fato como eu desejo fazer isso.
3. **Sumarizar** tudo aquilo que eu ajudei ela a levantar.
4. **Geração do documento** — que é a minha spec.
5. **Validar a minha spec** — e para validar, ela tem que cumprir todos os critérios (ver seção seguinte).
6. **Escrever o output.**

Com isso eu consigo gerar aquele documento de spec que mostrei para vocês.

## Por Que Contexto Passo a Passo Importa (Gates Determinísticos e Contexto)

Mas eu não posso gerar isso de outra forma? Você pode gerar da forma que quiser — pode usar Codex, o ponto aqui não é a ferramenta, não é a forma como você gera. O ponto é: lembra da primeira coisa que eu falei? Primeiro são gates determinísticos, e a segunda é contexto. O que a gente está fazendo aqui é basicamente alimentando o contexto.

Pensa o seguinte: a IA é inferência, ela não sabe o que você quer criar, ela não sabe como você quer criar, ela não sabe a melhor maneira de criar. A gente acha que ela sabe — ela não sabe. Então a gente precisa dizer passo a passo tudo que ela precisa fazer, explicar passo a passo, dar o contexto passo a passo, para assim a gente ter o resultado que a gente quer.

Quando vocês não dão contexto suficiente, sabe o que a IA vai fazer? Ela vai fazer o login para você do jeito que ela achar que é bom. E aí, quando ela faz o login, o que a gente tem que fazer? Fez o login, autenticou, faz o redirect para onde? Pro dashboard, não é? Exatamente aí ela não vai entender que você tem que fazer pro dashboard, sabe por quê? Porque faltou contexto. A gente só falou "implemente um login", mas como é o login, qual é a ação por trás desse login, o que vai acontecer depois que você implementou, em caso de sucesso, em caso de erro? Quando a gente passa o contexto, a gente está reforçando para chegar aquilo que a gente quer.

Então a ideia que a gente está fazendo aqui é: beleza, eu tenho o meu PRD, tenho o contexto do meu projeto, tenho a minha feature, e tenho uma skill que gera o destrinchar desta feature através do Spec Writer, que produz aquela primeira documentação, destrinchando o passo a passo daquilo que deve ser feito.

## Demonstração Prática

Na prática isso vai funcionar assim: vou chamar o Spec Writer, vou lá no meu PRD, pego a minha feature e só colo ela aqui. O que vai acontecer? Ele vai carregar a minha skill e vai começar a fazer todo o meu processo. Aqui, o que aconteceu: ele fez algumas buscas — primeiro leu o meu PRD, foi lá e leu as minhas documentações que já existiam dentro do projeto, e aí agora começou de fato a escrever. Isso é basicamente o Claude Code trabalhando. No final das contas o que aparece é o arquivo sendo criado.

## Os 7 Critérios de uma Boa Spec

Outra coisa que vocês têm que entender é: OK, entendi que eu tenho que trabalhar com specs — o que eu preciso gerar, o que eu classifico como uma spec boa, uma spec ruim, e tudo mais, para vocês criarem a própria skill de vocês. Eu costumo separar isso em sete itens:

1. **Falseabilidade.** Cada afirmação tem que ser verificável contra o output real. Exemplo: "o sistema deve ser performático" — performance é muito vago. Agora, quando eu coloco que o meu P99 de latência tem que ser menor que 200 milissegundos sobre 1000 requisições por segundo, por exemplo, eu já tenho algo que é real — a performance passa a ser latência P99 menor que 200ms sob 1000 req/s.

2. **Comportamento, não implementação.** Eu tenho que dizer o comportamento, eu não preciso especificar o processo de implementação. A spec vai dizer o que é verdade, não o como fazer. Eu não vou dizer "eu vou criar uma classe X.Y.Z com o método apply para aplicar um valor de desconto em um cupom" — isso é implementação. Eu posso dizer "aplicar desconto sobre um valor proporcionado", por exemplo.

3. **Invariantes.** A gente tem que deixar mais claras as invariantes — os cases que nunca podem ser violados. Exemplo: o preço final nunca é negativo; a soma dos créditos distribuídos, por exemplo, nunca excede o crédito original numa transação.

4. **Edge cases (casos de borda).** Precisam ser nomeados: vazio, negativo, limite, quando se trabalha de forma simultânea, o que não existir. Eu tenho que deixar isso claro — é sinal de spec madura.

5. **Fronteira (escopo).** Eu tenho que dizer o que é minha barreira, o que está fora do escopo ou não. Por exemplo, num caso de cupom: eu não vou tratar moedas estrangeiras, vou tratar só BRL; o reembolso vai ser uma tratativa totalmente diferente, um fluxo diferente — deixei explícito que está fora do meu escopo.

6. **Entradas e restrições.** Como eu espero receber isso.

7. **Decisões de negócio.** Tem que mostrar isso claramente.

Se vocês repararem bem na nossa spec, a gente faz exatamente isso: começa com technical overview, depois a parte de inputs, parte de arquitetura, depois os cases, a infraestrutura, como vou integrar coisas, o que está fora do escopo ou não, quais são os critérios de verificação de aceite ou não. Se vocês usarem esse método de sete etapas que passei para vocês, conseguem gerar uma skill exatamente com tudo que precisa uma spec para ser boa.

## Fechamento da Demonstração

Depois de chamar a nossa spec, o que aconteceu: ele fez o carregamento do contexto, subdividiu em dois arquivos — spec e plan. Por fim gerou somente um contrato aqui que vai organizar tanto o plano de implementação quanto a spec, e já me deu o próximo passo.
