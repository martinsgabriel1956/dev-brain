# Código Gerado por IA Tem 2,77x Mais Falhas de Segurança — e Piora a Cada Refinamento

Você pediu para a IA escrever um código. O código gerado por IA tem 2,77 vezes mais falhas de segurança do que código escrito por humanos — quase o triplo. Isso não é o pior. O pior é que quase ninguém te conta: cada vez que você pede para melhorar o seu código, a segurança na verdade piora. E quanto mais você refina, mais inseguro ele fica. Tem um paper medindo isso. Hoje eu vou te mostrar os números que se sustentam, por que isso acontece de forma sistêmica — quase automática — e o que mudar no processo antes que isso vire um incidente e te dê dor de cabeça.

## Os números

Antes de tudo eu fui atrás de dados para poder comprovar isso, porque tem bastante dado circulando sobre esse assunto que não tem fonte, que não tem pesquisa por trás. Então eu não queria trazer isso sem embasamento para o canal.

### 2,77x mais falhas — CodeRabbit e Veracode

Esse número vem do CodeRabbit: eles analisaram PRs (pull requests) reais — 320 escritos por IA, 150 escritos por humanos. E não foi só eles: o relatório da Veracode, também de 2025, testando mais de 100 modelos diferentes, chegou no mesmo número. Dois estudos independentes, a mesma conclusão.

### O relatório da Black Duck

Esse segundo número é do Black Duck, um relatório de segurança de open source deles. Eles analisaram 947 codebases. O que eles descobriram:

- **107% de aumento de vulnerabilidades por codebase em um ano** — dobrou.
- A média hoje é de **581 vulnerabilidades por codebase**.
- **87% dos codebases têm pelo menos uma vulnerabilidade conhecida.**

Isso tem muito a ver com o boom da IA e o boom das pessoas usando IA e aumentando a produtividade. Nesse mesmo relatório também mostra que, de todas as empresas, **85% já usam IA para gerar código**. Só que o número que mais pegou sobre isso é algo que eu não esperava, e acho que você também não: é o que a gente **não** faz com esse código.

Só **24% das empresas fazem uma avaliação completa** do código gerado por IA — segurança, licença, qualidade, tudo. **76% checam alguma coisinha** ali (tem algum lint para ver), mas só um quarto olha o pacote inteiro. Ou seja: a IA está gerando código quase três vezes mais vulnerável, na velocidade em que ela produz código, e três a cada quatro times não estão nem sabendo o que está acontecendo.

## Por que isso acontece — o mecanismo

Antes de eu falar da solução, quero que a gente entenda o mecanismo. Se você não entende por que isso acontece, você vai achar que é um bug e que a próxima versão do modelo vai corrigir. Só que não é isso.

A IA generativa treina em código que existe — todo o código da internet, incluindo código inseguro:

- Stack Overflow cheio de snippet com SQL Injection.
- GitHub cheio de projeto com XSS.
- Tutorial de 10 anos atrás que nunca foi atualizado.

O modelo aprendeu com esses padrões, e quando você pede código, ele gera o padrão que aprendeu. E é engraçado, porque ele vai te passar a mesma confiança quando gera código seguro e quando gera código inseguro. Esse é justamente o coração do problema.

Um dev experiente, quando começa a concatenar string com input de usuário numa query SQL, tem um alerta interno — ele já aprendeu na marra que ali mora um perigo. O modelo não tem esse alerta: ele completa o padrão. Se o padrão tem vulnerabilidade, ele vai achar que está certo.

O mais estressante — o pior — é que a confiança que ele gera no texto não é sinal de segurança, é só fluência, é só a "oratória" dele. A fluência com que o modelo escreve código inseguro é a mesma fluência com que ele escreve código seguro. Parece certo, compila, os testes passam, e mesmo assim tem um buraco, tem vulnerabilidade.

Isso é diferente de um colega — júnior, pleno ou sênior — quando ele está inseguro: ele hesita, ele vai perguntar, vai avisar, vai verificar. O modelo não faz isso, porque ele entrega tudo, entrega todos os padrões que conhece com a mesma cara lavada, seja o padrão bom ou ruim.

## O paper: degradação de segurança em geração iterativa

O dado que deu o título para esse vídeo — e que me fez querer gravar — é que eu não vejo muita gente falando sobre isso. Tem bastante gente falando sobre código inseguro gerado por IA, mas tem um paper no arXiv, de autoria de Shivani Chukala, Rimanchu Joshi e Romília Sid — os nomes podem estar com grafia imprecisa, ouvidos foneticamente da fala. O título do paper é **"Security Degradation in Iterative AI Code Generation"** (degradação de segurança na geração iterativa de código por IA).

A premissa do estudo é testar uma coisa que todo mundo assume: que mais rodadas de refinamento deixam o código melhor. Eles foram medir se isso vale também para segurança.

**Metodologia:**
- 400 amostras.
- 40 rodadas de refinamento.
- 4 estratégias de prompt diferentes.
- Vulnerabilidade medida a cada passo com análise estática — o mesmo tipo de ferramenta que roda no seu CI, aplicada da mesma forma para todos os prompts.

**Resultado:** 37,6% de aumento de vulnerabilidades **críticas** depois de cinco interações. Crítica não é warning de lint — é o tipo de coisa que passa em pentest, que vira CVE, que vira notícia. Cinco rodadas de "melhora" e você já tem quase 40% mais buracos críticos do que quando começou.

O detalhe que mata qualquer esperança de resolver isso só com prompt: das quatro estratégias de prompt testadas, uma pedia explicitamente para focar em segurança a cada rodada. Mesmo assim, degradou — melhora nas primeiras interações e volta a piorar depois. O modelo corrige o que ele consegue ver e introduz o que ele não consegue ver. Não existe uma estratégia de prompt que impeça essa degradação — o problema é mais fundo do que o prompt.

## Por que isso é automático, e não só azar

Três razões:

1. **O modelo não tem memória do contexto de segurança das rodadas anteriores.** Ele não sabe que, na interação dois, introduziu um SQL Injection, e que na três corrigiu — ele trabalha no código presente, sem esse histórico.
2. **Cada refactor para "deixar mais limpo" move a lógica de validação de lugar.** Ela sai do ponto certo, some, ou muda de comportamento sem parecer diferente.
3. **Os testes funcionais continuam passando** — porque quase todo mundo testa o happy path, não o edge case de alguém mal-intencionado usando o sistema. A regressão de segurança passa por baixo dos panos, e as vulnerabilidades passam junto. É como se cada review fosse feito por um dev diferente, e nenhum deles tivesse lido o review anterior — a inconsistência vai se acumulando.

## O que fazer — não é largar a IA

A resposta não é parar de usar IA — eu continuo usando, mesmo sabendo disso. É ajustar o processo, com disciplina.

O jeito errado, que é o que quase todo time faz hoje: gerar e iterar várias vezes, e o review de segurança vem no final — se vem. Nesse ponto você já acumulou degradação por quatro rodadas antes de alguém olhar.

O jeito certo: o security review deixa de ser a fase final e vira um **checkpoint entre cada rodada de iteração**. Cinco mudanças concretas:

1. **Rodar SAST antes e depois de cada modificação.** O que você revisa é o *delta* — a diferença no relatório — não o código todo de novo. É rápido.
2. **Ter um limite de número de iterações antes de parar e revisar na mão.** O paper mostra que cinco rodadas já dão 37% a mais de vulnerabilidades críticas — não deixe chegar na vigésima interação para fazer a primeira revisão manual.
3. **Escrever os testes de segurança antes de começar a iterar.** Se você sabe que um endpoint precisa limpar o input ou ter alguma validação, escreve um teste que verifica isso antes de pedir para mexer — assim, qualquer iteração que quebre isso é pega automaticamente.
4. **Usar um contexto limpo quando for pedir para a IA revisar segurança** — não o mesmo chat que gerou o código. Cola o código, ou passa o link do PR, num chat/contexto novo. Um modelo sem histórico de quem escreveu o código é bem mais crítico do que um modelo que acabou de escrever aquele mesmo código.
5. **Mudar a expectativa mental:** você não está iterando só para melhorar, está iterando para *mudar* — e toda mudança tem custo, inclusive custo de segurança. Reconhecer isso muda quando você decide parar e fazer na mão.

## Para quem trabalha em time

Se você adotou IA no desenvolvimento e não atualizou os processos de segurança de code review, você está acumulando débito técnico — dívida de segurança — na mesma velocidade em que está produzindo código, que é muito rápido. Security review que era uma vez por sprint, ou uma vez por mês, tem que passar a ser **por feature, por iteração significativa**. Óbvio que isso tem custo, vai ter tempo — mas o custo de não fazer isso, de expor dados de usuário e ter uma vulnerabilidade explorada, é muito maior.

Um amigo meu, no trabalho dele, já caiu nisso: eles iteraram um endpoint e ele passou a logar, na response, o nome e telefone do usuário — dado PII (personally identifiable information). Não foi o fim do mundo, mas podia ser dado de cartão, dado de pagamento. Foi um bom lembrete de que a gente não pode delegar segurança para a IA sem testar e sem se atentar — tem que ter um checklist do que se está defendendo.

## Fechamento

Quero saber de você: você faz security review? Se preocupa com isso no seu trabalho, ou é só o review padrão (quando faz)? Se você quer aprender a trabalhar com IA de um jeito que já embuta isso — spec antes de código, testes antes de código, contrato de segurança, verificação a cada passo em vez de só no final — é exatamente o que passo no meu treinamento de programar com IA. Link na descrição para a lista de e-mails de quando estiver disponível.
