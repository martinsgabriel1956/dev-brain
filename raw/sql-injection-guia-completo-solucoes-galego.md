# SQL Injection: o que é e como se proteger (guia completo de soluções)

## Patrocínio (Sfia)

Você já ficou sentado horas numa cadeira horrível, tudo doendo nas costas, pescoço emperrado? Trabalhar muito tempo na cadeira correta é completamente diferente disso. A Sfia Elements reclina até 150º, tem apoio lombar ajustável, braço 3D e malha respirável. Clica no link na descrição, usa o cupom Galego e vem sentir a diferença. Cansei de falar disso.

## Introdução

No nosso canal hoje a gente vai voltar um pouco às origens: o tópico é SQL Injection, um tema que você precisa dominar se você for um desenvolvedor profissional que trabalha em empresas. SQL Injection é, digamos assim, um tipo de vulnerabilidade muito comum encontrada em vários tipos de aplicação, e existem várias soluções para ela. A gente vai explorar o que é essa vulnerabilidade, como construir aplicações imunes a ela, e os diferentes tipos de solução.

## O que é SQL Injection

SQL Injection é uma injeção de SQL. No limite, ela significa o seguinte: um usuário malicioso vai tentar passar pro seu servidor um código que vai injetar algo via SQL no seu banco de dados, e o seu servidor, caso não esteja preparado para isso, vai repassar essa instrução para o banco de dados.

Vamos supor o seguinte: lá no seu frontend existe um campo para o usuário digitar o e-mail dele. O usuário digita `augusto@mail.com`. Vamos supor que no seu servidor exista um código que faça uma substituição — você tem um SQL pré-programado e, dentro desse SQL, substitui a string do e-mail.

O que um usuário malicioso pode fazer? Ele pode imaginar que você está fazendo isso e enviar o "e-mail" dele como:

```
' ; DROP TABLE users;--
```

Se ele enviar isso como e-mail, a sua query passa a ser algo tipo:

```sql
SELECT * FROM users WHERE email = '';
DROP TABLE users;
```

Ou seja: ele encerrou a consulta anterior no banco de dados e executou um segundo comando que foi injetado — `DROP TABLE users`. E não precisa ser esse comando específico: pode ser qualquer outro. Ele pode tentar um `SELECT` em todas as tabelas, pode tentar alterar o próprio saldo, pode tentar alterar os próprios tokens. Como invasor, eu ganho um controle sobre o SQL — um controle sobre o seu banco de dados que eu não deveria ter.

Essa é a versão vulnerável, e é assim que o SQL Injection é explorado — assim que a vulnerabilidade é utilizada para me dar um determinado poder que eu não deveria ter sobre o seu banco de dados.

Agora existem vários e vários níveis de fix — coisas que ajudam isso a não acontecer.

## Nível 1 — Query parametrizada (nível de banco de dados)

O fix mais ingênuo, o mais inocente de todos, é utilizar uma **query parametrizada** no banco de dados. Numa query parametrizada, o banco recebe a query em si separada do campo. O campo e-mail vem separado da query. Dessa maneira, o "e-mail" do usuário seria de fato tratado literalmente como a string `'; DROP TABLE users;--`, sem nenhum efeito de comando.

Esse é o primeiro nível de solução — eu não diria que é o mais utilizado, mas ele já consegue prevenir esse bug, a não ser que exista algum *work around* que eu não conheça.

## Nível 2 — Prepared statements (nível de banco de dados)

Parecido com o anterior: os **prepared statements**. Bancos de dados como o Postgres — que é o que eu tenho mais experiência, trabalhei mais de 5 anos usando essa ferramenta — dão essa mesma lógica de separar o que é o statement (a consulta em si) do que é o campo. É muito parecido com uma query parametrizada, só que a nível de banco de dados.

## Nível 3 — Menor privilégio na conexão com o banco

É interessante notar o seguinte: o `DROP TABLE users` não deveria nem ser possível da aplicação executar. A conexão entre o servidor e o banco de dados deve ter o **menor privilégio possível** para fazer aquilo que precisa ser feito.

O seu banco de dados pode ter múltiplos usuários. Um desses usuários, por exemplo, pode ser: "esse usuário vai ser o servidor, especificamente a aplicação de e-mails", e essa aplicação de e-mails tem permissão apenas de fazer `SELECT`, `INSERT` e `DELETE` em algumas tabelas específicas. Isso, claro, não vai prevenir um SQL Injection — mas vai minimizar a superfície de ataque.

Existe também a possibilidade de usar **stored procedures** a nível de banco de dados, mas acho que vocês já pegaram a ideia — vai na mesma linha de uma query parametrizada ou de um prepared statement.

Então, a nível de banco e acesso a banco, essas são as soluções — mas note que ainda tem bastante superfície de trabalho, e quanto mais a gente trabalhar, melhor.

## Nível 4 — Solução nativa do seu backend

Dentro do seu servidor você vai estar rodando algum código no backend — escrito em Node, em Rust, em Django, em Ruby — e todas essas ferramentas vão ter algum tipo de solução nativa para prevenir SQL Injection. Não dá para eu ir uma por uma aqui porque cada uma tem a sua própria solução, mas olhe a solução nativa do seu backend.

## Nível 5 — ORM ou query builder

Existe também a possibilidade de você estar utilizando alguma **ORM**, como um Drizzle, um Prisma — o Django, por exemplo, já vem com uma ORM própria embutida. A sua ORM, ou ela vai prevenir SQL Injection por padrão, ou vai ter uma solução para isso. Então, se você estiver usando uma ORM, olhe dentro da ORM.

O mesmo vale para um **query builder** — supondo que você não use uma ORM, mas use um query builder para acessar o banco. Pesquise, naquele query builder específico, como se coíbe SQL Injection. Todas essas soluções estão a nível de código dentro do seu servidor.

Note que já temos dois lugares onde a gente pode parar isso: a nível de banco de dados, e a nível de servidor/código em si.

## Nível 6 — Validação de input (camada complementar, não suficiente sozinha)

Existe outro lugar que não é o ideal, mas você pode tentar ter uma camada de validação de input. Por exemplo, se você utilizar um **Zod**, você pode garantir que um e-mail é de fato um e-mail, usando o Zod ou algum outro tipo de validador de input que, internamente, pode usar uma regex ou uma máquina de estados para validar que o input é aquilo que você acha que é.

Dessa maneira de coibir SQL Injection eu, pessoalmente, acho fraca. Não é em todos os casos que vai pegar tudo, até porque você não sabe qual regex o Zod está utilizando por baixo, não sabe como ele valida internamente que algo é válido — e até existem e-mails válidos que são bem estranhos (já fiz um vídeo falando sobre validação de e-mail, com vários exemplos de e-mails bizarros que são tecnicamente válidos). Então tome cuidado se usar só essa solução, porque eu não acredito que ela seja suficiente sozinha.

Muitas vezes você vai validar, por exemplo: "ah, um usuário vai enviar a descrição de um produto, então eu valido que essa descrição é um texto". Mas você pode ter um SQL Injection dentro desse texto mesmo assim. Ou seja: validação de input não é necessariamente o caminho.

## Nível 7 — Web Application Firewall (WAF)

Por último, antes do seu servidor, existe algo que eu tenho recomendado bastante — praticamente todos os projetos reais que têm usuários expostos à internet de alguma maneira, a gente tem recomendado o uso de um **Web Application Firewall (WAF)**. Um WAF, dentre outras coisas, pode coibir requests suspeitos.

Note: de maneira alguma eu digo que o WAF vai prevenir 100% dos SQL Injections — não é esse o objetivo de um WAF. Mas o WAF é um firewall, e como firewall é bom para proteção geral da sua aplicação, de quebra ele acaba pegando SQL Injection aqui e ali no corpo de alguns requests.

## O que fazer imediatamente ao encontrar um SQL Injection

Se você olhou sua aplicação e percebeu "eu tenho um SQL Injection aqui", o que você deve fazer de imediato — o mais simples e mais fácil — é olhar como você está acessando esse banco de dados a nível de código. No seu backend — Node, Ruby, Django, Python — procure a solução nativa que vai dentro do seu backend. Essa costuma funcionar 100% e já corta o mal pela raiz.

Adicionalmente, eu também cuidaria dos privilégios do usuário do servidor, porque isso vai te prevenir de outros problemas além do SQL Injection. Por exemplo: caso alguém consiga tomar controle do seu servidor, consiga fazer um SSH pra sua máquina, consiga executar algum tipo de código que coloque o usuário malicioso lá dentro e consiga fazer requests a partir desse servidor — é bom que esse servidor tenha poucos privilégios com relação ao banco de dados.

## Encerramento / CTA

Fechou, galera — dá uma força aqui, dá um like, dá um subscribe, me ajuda com essa série nova que eu quero ensinar computação. Caso você queira aprender mais comigo, temos diversos cursos no canal (links na descrição): um curso completo de estrutura de dados e algoritmos mais LeetCode para preparar para entrevistas de emprego; o curso "Mapa Pro Seu Próximo Emprego", que também prepara para entrevistas, ajuda a ter um bom currículo, um bom LinkedIn, e ser encontrado por recrutadores (preciso atualizar meu site); e o curso de System Design, já lançado, no qual passei mais de um ano trabalhando — é o curso mais extenso e mais trabalhoso que já fiz. Se você comprar qualquer curso meu, tem um mês de acesso em que pode pedir reembolso integral, sem precisar de nenhuma justificativa, porque confio que o trabalho é muito bom e só quero o seu dinheiro se valer a pena pra você também. Fechou, beijão.
