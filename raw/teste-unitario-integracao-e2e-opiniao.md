# Testes Unitários, Integração e E2E — uma conversa opinativa

> Transcrição de vídeo. Formatada em Markdown para ingest na wiki, sem alteração de conteúdo ou opinião do autor. Trecho publicitário (patrocínio) preservado no fim, isolado do conteúdo técnico.

O vídeo de hoje tá diferente. Ele foi escrito, reescrito, eu tentei gravar e eu tinha uma ideia do que eu queria trazer para vocês: eu queria mostrar como funciona o teste unitário, qual o propósito dele, como encaixa na prática, depois mostrar um teste de integração, depois um end-to-end, numa pegada meio tutorial.

Enquanto eu tava produzindo o script desse vídeo eu achei que não funcionou muito bem. Achei que, para um tutorial, ficou muito raso. E se eu fizesse ele muito seco, sem ser opinativo, eu não sentia que eu tava falando o que eu realmente penso. Você que tá vendo esse vídeo vai ter que aceitar o fato de que é um vídeo altamente opinativo — tem muita controvérsia com teste. Eu vou falar o que eu acho baseado na minha experiência, baseado no que eu vi. E você tem que ter o discernimento de entender que diferentes tipos de teste vão ser mais adequados para diferentes contextos e diferentes capacidades de diferentes equipes.

A minha opinião sobre testes é enviesada pelo fato de que: primeiro, eu sou muito ruim em fazer eles; segundo, eu não gosto de fazer eles; terceiro, eu não sou front também, o que vai influenciar na minha capacidade de fazer end-to-end — uma das pontas do end-to-end é o front-end, a interface.

O que a gente vai tentar fazer: eu vou tentar te explicar de uma maneira didática qual é a ideia e o propósito de unit tests, qual é a ideia e o propósito de teste de integração, qual é a ideia de end-to-end e por que se fala dessa pirâmide. Depois que eu explicar dessa maneira, tentando ser um pouco imparcial, a gente vai desconstruir isso. Eu vou te falar como eu vi isso na vida real, como eu aplico na empresa que eu trabalho e como eu vejo essas coisas fazendo sentido e encaixando.

A gente tem que se lembrar que a gente não tem recursos infinitos. O problema é sempre o mesmo: é um problema de alocação de recursos. Como que a gente vai alocar os nossos recursos? Eu poderia muito bem falar "você faz todo tipo de teste, o mais compreensivo possível" — isso existe, existem benefícios, mas existe um custo muito grande também. É um problema de alocação de recursos.

*(Segue, neste ponto do vídeo original, um bloco publicitário do patrocinador — reproduzido ao final deste documento, separado do conteúdo técnico.)*

## Testes unitários

Na base da pirâmide a gente tem os testes unitários. Eles testam unidades de código — geralmente uma unidade é uma função. Às vezes testam uma classe inteira, ou funções dentro de classes, mas uma unidade acaba sendo geralmente uma função, um método.

Exemplo em Python: uma função `add` que soma dois números, e um teste que usa `assert` para aferir se os valores somados estão corretos. É recomendado que um teste unitário teste apenas uma única coisa — por exemplo, testar a adição de números positivos, depois um teste separado para números negativos, outro para adicionar zero (testando os *boundaries*).

**O problema:** e se existe um bug que eu não pensei no meu teste unitário? Não importa quantas vezes eu teste a mesma linha de código — 100% de cobertura não garante ausência de bug. No exemplo do Python não tem bug, porque a função só soma. Mas supondo uma função mais complexa: eu poderia esquecer de testar com número fracionado, ou, em Java, esquecer de testar *integer overflow*.

Teste não previne bug 100%. Cobertura de teste não previne bug — pelo menos não existe maneira de prevenir um bug que a gente não sabe que pode existir. Se você não sabe o que é integer overflow, você não vai criar um caso de teste para isso; se você não pensa que um bug pode existir, você não consegue preveni-lo. O objetivo de um teste unitário é ver que uma função funciona para os casos de uso que a gente imagina que ela deve funcionar.

### O que faz um bom teste (na minha visão)

- **Determinístico.** Se o teste não é determinístico, para mim ele não vale nada — pode simplesmente ser deletado. Existem *flaky tests* que às vezes passam, às vezes falham; determinismo é extremamente importante.
- **Conciso.** Um teste deve testar uma coisa, um comportamento. Se ele testa várias coisas e uma quebra, fica chato de corrigir — você tem que refatorar o teste inteiro por algo minúsculo que quebrou.
- **Relevante.** Em muitos exemplos "de livro" (como testar `add(2,3) == 5`), o teste não é muito útil. Testes unitários têm esse problema com frequência: não testam muita coisa relevante.
- **Compreensível.** Eu preciso entender o teste.
- **Durável.** Se um teste só vai durar uma semana, para que escrevê-lo?

### Testando código que fala com o banco: mocks

Se a função, além de somar, também salva o resultado num banco de dados, academicamente é recomendado mockar esse banco — para não salvar dados de teste no banco de verdade. Isso normalmente exige que o banco seja injetado como dependência (dependency injection), permitindo passar um `mock_db` no teste.

O problema: eu consigo testar que `db.save` foi chamado (uma asserção sobre a chamada), mas não consigo verificar se o dado realmente foi persistido. O que muita gente faz para resolver isso é usar, por exemplo, SQLite no lugar do mock, com um setup de teste um pouco maior — e isso já deixa de ser um teste unitário puro, porque não estamos mais testando uma unidade isolada. Isso encaminha para o segundo tipo de teste: o teste de integração.

Numa abordagem puramente unitária, o ideal seria dois testes separados: um testando que a função soma corretamente, outro testando (isoladamente) que a função de salvar no banco de fato persiste e permite buscar os dados depois.

## Testes de integração

Aqui a gente testa que componentes trabalhando juntos resultam no que a gente espera — por exemplo, que a soma feita em conjunto com o `save` resulta em um número salvo no banco de dados. Usa-se menos mock (não necessariamente zero). Um teste de integração pode testar duas funções, ou um fluxo inteiro, desde o request do usuário até o dado chegar no banco.

Teste de integração é mais devagar que unitário — está testando mais código, e geralmente é mais devagar justamente porque se moca menos coisa.

**Exemplo:** uma aplicação FastAPI com endpoints de criar e buscar usuário. O teste de integração faz um POST para `/users`, verifica o status 201 e o nome retornado, e depois usa o ID retornado para fazer um GET, garantindo que o dado foi de fato salvo no banco. Isso não é mais um teste unitário — é um teste de integração testando que o POST funciona e que, dado que o POST funcionou, o GET consegue buscar a informação.

É possível também mockar o banco num teste de integração, mas geralmente é melhor ter um banco de dados dedicado a testes (não o de staging/dev), podendo ser o mesmo motor (ex.: Postgres em produção e Postgres nos testes), só que sem os dados de produção. Isso adiciona tempo — o banco precisa ser criado no CI. Se você não cria um banco de teste real, na prática você não está testando o banco: está testando um mock que você mesmo escreveu, e se você não pensou nos problemas que o banco real poderia ter, esses problemas não estão no mock. Nesse caso, é um teste de integração que não integrou muito bem.

## Testes end-to-end (E2E)

Acima da integração, em teoria, temos em menor quantidade os testes end-to-end. Aqui o negócio fica mais "doido": nunca vi duas empresas fazendo E2E da mesma maneira. Teste E2E testa um fluxo inteiro da perspectiva do usuário — geralmente simulando um browser (às vezes headless, às vezes visível), executando as ações que o usuário faria e conferindo o resultado que o usuário teria.

**Exemplo:** uma FastAPI com endpoint de signup e um front-end em React que faz um POST de formulário. Com ferramentas como Playwright, Cypress ou Selenium, o teste abre uma página local, preenche campos (ex.: e-mail, senha) usando seletores como IDs, clica em "submit" e verifica se a página resulta no que se espera.

Testes E2E tendem a ser mais lentos e mais complicados na vida real do que um exemplo simplório sugere — porque são requests de verdade, geralmente rodando em ambiente de staging (ou um ambiente efêmero criado e destruído no CI/CD, o que adiciona custo de infraestrutura e tempo). Por isso são o topo — e a ponta mais cara — da pirâmide: mais caros em tempo de desenvolvedor, em infraestrutura e em tempo de execução.

### O problema de "ponta a ponta" em sistemas com dependências externas

Num sistema com um "Provedor de Pagamentos" (PSP) e um fornecedor externo, o que é de fato "ponta a ponta"? Testar o fluxo completo batendo no ambiente de staging real do PSP? Ou mockar o sistema nas pontas (input mockado, output mockado) e testar só o sistema próprio no meio?

Se você moca as pontas, pode não estar testando adequadamente se o PSP responde como você espera — então é possível fazer, separadamente, uma suíte que testa o PSP e outra que testa o fornecedor, mockando ambos nos testes do sistema principal. Fica caro, complexo — mas, dependendo do caso, principalmente em fluxos cruciais (signup, login: "se isso não funcionar, não pode ter deploy"), pode valer a pena.

**Fragilidade de UI:** um teste E2E que depende de um seletor de campo (ex.: id do campo de e-mail) quebra se a UI mudar, mesmo que o site continue funcionando normalmente. Coisas de UI/UX tendem a mudar bastante, e isso tende a quebrar esses testes com frequência.

Avaliando os critérios de bom teste para cada camada:
- **Determinístico:** na medida do possível.
- **Conciso:** difícil dizer que sim para os três tipos, e especialmente para E2E.
- **Relevante:** dos três tipos, E2E é o mais relevante de todos, quando bem aplicado.
- **Compreensível:** deveria ser, mas em casos reais é complicado.
- **Durável:** não — a durabilidade do teste E2E dura na mesma medida em que os fluxos do sistema permanecem os mesmos.

## Desconstruindo a pirâmide: minha opinião

Não é toda empresa que precisa de tudo. Não faz sentido, num MVP sem nenhum cliente, investir em testes E2E — o custo não se justifica.

Testes unitários são legais, mas o problema é que eles são mais úteis para reforçar um bom padrão de código e prevenir regressão de bugs do que para outras coisas. Muitas vezes o código é tão pequeno e conciso que quase nem precisa ser testado.

No tamanho de empresa e nos ambientes em que trabalhei, o custo-benefício que eu mais valorizo fica entre o unitário e o de integração — talvez mais para o lado do teste de integração. Entendo que a UI varia muito, entendo que existem coisas fora do meu controle (ex.: o provedor de pagamentos pode quebrar) e aceito esse risco. O caso médio que considero ideal é um teste de integração que moca algumas coisas em alguns momentos, mas não tudo — ainda testando o banco de dados especificamente, e testando mais pesadamente o back-end. (Vale notar que um teste de integração também acaba testando um pouco da infraestrutura: às vezes o teste passa mesmo que a infra não esteja de fato funcionando, o que é uma limitação.)

Não vejo isso como uma pirâmide estrita, mas como um balanço que depende de entender o contexto:

- **Código legado, mal compreendido, sem donos claros:** aqui um teste E2E ("usuário clicou nesse botão, fez isso, isso, resultou naquilo") é extremamente valioso — ele dá a liberdade de refatorar um monolito espaguete legado com confiança. Existe um valor gigantesco em E2E nesses contextos.
- **Startups que pivotam a cada poucos meses, mudam a interface inteira com frequência:** nesses casos, não vejo que valha tanto a pena investir pesado em E2E, porque a durabilidade desses testes tende a ser baixa.
- Quanto mais maduro (e mais frágil) o produto, mais valiosos os testes E2E se tornam — mas se o produto é muito frágil, os testes tampouco vão ser muito duráveis.

É possível ter 500% de "testagem" (cada linha executada cinco vezes nos testes) e não existir um único teste relevante. Para mim, o teste mais relevante é aquele que observa que um caso de uso segue a regra de negócio esperada — por exemplo: um POST em `/users` seguido de um GET que busca esse mesmo usuário no banco. Esse é o *sweet spot* dos testes: testar o caso de uso, não a implementação isolada.

Esse padrão pode ser generalizado: aplicar um desconto num produto e depois ver que o preço reflete o desconto; criar um usuário administrador via setup e verificar que ele pode criar um produto novo, enquanto um usuário não-administrador não pode; um usuário dono de uma loja consegue acessar todos os dados dela, mas um usuário que não é dono só acessa um subconjunto. O mais importante de um teste, nesse sentido, é garantir que a regra de negócio está sendo seguida e não vai regredir.

De novo: o teste não garante ausência de bug, porque não dá para testar para um bug que você não conhece. Um teste garante que, se eu enviar "Alice" hoje, eu consigo recuperar "Alice" depois — mas não garante proteção contra um caso que eu nunca imaginei que pudesse existir (ex.: uma tentativa de SQL injection que eu não pensei em testar).

## Fechamento

Este não foi um tutorial profundo de testes — não era o objetivo. Foi uma conversa opinativa sobre como pensar a respeito de testes: relevância acima de tudo (vejo muito teste irrelevante e alguns incompreensíveis); concisão importa menos do que se costuma dizer. E lembrando sempre que tudo isso tem um custo — é um problema de alocação de recursos. Se você gasta uma semana fazendo testes E2E, foi uma semana que você não gastou fazendo outra coisa; isso precisa ser mensurado. Se a produção está sempre quebrando, vale a pena investir mais em testes; se nunca quebrou e vocês nunca gastaram tempo testando manualmente, talvez não valha. As perguntas a se fazer: qual custo você quer prevenir, qual erro você quer que não aconteça, qual benefício você visualiza, quanto tempo seria poupado garantindo que um bug não vai voltar depois de um merge. Respondendo essas perguntas, fica mais claro qual teste é mais adequado para a situação.

---

## Bloco publicitário (patrocínio, fora do escopo técnico)

Trecho de patrocínio de uma escola de investimentos (curso para organizar finanças pessoais, renda fixa e variável no Brasil e exterior, questões tributárias de imposto de renda sobre ações, cartão de crédito com cashback e acesso a sala VIP em aeroporto, e plataforma de investimentos). Preservado aqui apenas por integridade da transcrição — sem relação com o conteúdo técnico sobre testes.
