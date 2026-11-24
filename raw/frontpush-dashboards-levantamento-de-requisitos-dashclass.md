# Levantamento de requisitos do DashClass: atores, entidades e gamificação (FrontPUSH)

## Um levantamento simplificado

Opa, fala pessoal, sejam muito bem-vindos a mais uma aula onde nós vamos agora fazer o levantamento de requisitos do DashClass, tá? Já conversei para vocês que é um levantamento de requisitos bem simplificado, eu fiz justamente para poder demonstrar para vocês como que é mais ou menos o fluxo seguindo os princípios que a gente tinha falado nas aulas anteriores, mas tem poucos atores de propósito porque dá muito trabalho para poder a gente executar cada fluxo desse para poder a gente entender fazer o levantamento de requisitos, né? Cada ator que tem no sistema aumenta drasticamente a quantidade de telas, a quantidade de relacionamentos entre as entidades e tudo mais, então pense que esse aqui é um demonstrativo um pouco mais simplificado para poder você pegar a essência daquilo e conseguir aplicar aí nos seus projetos, tá?

## Os atores: aluno, funcionário e administrador

Então vamos lá, levantamento de requisitos, basicamente pessoal, o que que se trata o DashClass? Como eu já disse, ele é uma plataforma de ensino, então vamos lá, vamos anotar aqui, ele é uma plataforma de ensino, nessa plataforma de ensino eu tenho três principais atores, tá? Que é o aluno, esse aqui é o aluno, eu tenho o funcionário deles, o funcionário, vai trabalhar dentro dessa plataforma, né? E eu tenho os administradores, tá bom?

Então o que acontece? Geralmente os alunos vão com certeza assistir as aulas, eles vão assistir as aulas, opa, assistir as aulas, eles vão interagir, eles vão dar os feedbacks e vão ser os compradores, tá bom? Então vão ser aqui os compradores, beleza? Compradores. Automaticamente se ele é um comprador, esse aqui vai ter venda, a gente já sabe que vai ter a parte de venda, concorda? Beleza.

Esses dois aqui, eles são os funcionários, né? Então a caráter mais administrativo, então eles têm acesso mais administrativo. Então eu já sei mais ou menos qual é o outro fluxo que eu vou desenhar aqui, tá? Então eu vou ter um fluxo que é de alunos e eu vou ter outro fluxo que é do administrativo, entendeu? Em que o administrativo vai ter acesso restrito a determinadas telas, né? Então é isso.

## Entidade user

Eu já sei que pelos atores aqui, eu já tenho uma entidade chamada usuário, né? Eu vou chamar aqui de user. Eu tenho uma entidade chamada de user. Por ela ser uma entidade, eu já tenho que atribuir para ela, né? Eu tenho que perguntar para ela quais são os atributos dessa entidade, quais são as características, né? Então eu já estou fazendo aqui uma abstração.

Qual que são as características de um usuário? Primeiro, ele precisa de um identificador, né? Dentro do meu sistema eu preciso de um identificador. Qual outra coisa que eu posso colocar de usuário aqui? E aqui eu estou chutando, tá bom, pessoal? Ele tem que ter um perfil, né? Ele tem que ter um perfil, porque ele pode ser administrador ou um usuário normal, né? Ele precisa de ter, sei lá, um e-mail, né? Para poder a gente recuperar a senha. Caso ele perca o acesso dele, eu preciso mandar um novo código de acesso para poder recuperar o acesso ao sistema.

Ele precisa, sei lá, de uma data de aniversário? Talvez, não sei. Ah, eu quero que o meu sistema dê parabéns para ele na data de aniversário. Pode ser, né? Data de aniversário. Eu estou inventando aqui alguns atributos só para vocês terem noção, tá bom? O que é interessante também? Lógico, o nome, né? Como é que a gente vai ter? Nome, sobrenome. Outra coisa, CPF, né? Então, se a gente está falando de alunos compradores e vai acontecer uma venda, eu preciso emitir nota fiscal. Se eu preciso emitir nota fiscal, eu preciso do CPF, tá? Que também é uma chave identificadora. E por aí vai. Você vai elencando aqui diversos atributos para o usuário.

Então, eu já sei que eu preciso fazer o quê? Se ele virou uma entidade, eu preciso fazer o famigerado CRUD. Então, eu já sei que eu tenho que ter telas de cadastro de usuário, eu tenho que ter telas para listar e pesquisar o usuário, eu tenho que ter telas para poder atualizar o usuário e eu tenho que ter telas para deletar o usuário. Ponto, tá? Então, você já sabe quais são as telas que vão sair daqui.

## Entidade venda

Segunda coisa, venda. Isso aqui, venda, também é uma entidade, correto? Também é uma entidade, do qual eu tenho o ID da venda. Eu preciso saber qual é a natureza da venda, por exemplo, se foi cartão, se foi boleto. Então, se foi cartão de crédito, se foi boleto, se foi PIX e etc. Preciso da natureza, né? Dessa venda.

Eu preciso saber quem comprou a venda, né? Quer dizer, quem realizou essa venda. Então, eu preciso do ID do funcionário. ID funcionário. Que, porventura, esse ID do funcionário, né? Ele é uma chave que ele vai vir do usuário, né? Então, vai vir para cá. Outra coisa que eu preciso, ID do comprador, né? Ou seja, qual foi o usuário que comprou? Comprador, que também vai vir de usuário, né? Então, a gente coloca aqui ID comprador, que também vai vir daqui de usuário. Então, eu tenho um relacionamento entre vendas e usuário, né?

Outra coisa que eu preciso, saber se foi parcelado ou não, né? Foi parcelado? Foi à vista? Quais foram as características? Está quitado? Já passou o prazo, né? Já emitiu nota fiscal? Então, eu tenho que colocar aqui uma parte de NF-e. Eu tenho que fazer uma parte de data. Eu tenho que ver os itens. O que foi comprado, né? Quais foram os produtos? Opa! Quais foram os produtos que ele comprou? Produtos. Produtos.

## Entidade produtos: os cursos

Quais são os produtos do curso? São o quê? Compradores de conteúdo, né? Da nossa DashClass. Então, o que é o nosso produto? São as aulas, né? São os cursos. Então, os produtos são os cursos. Então, eu acabei de descobrir outra entidade, né? Então, tem os itens. Que, porventura, os produtos vão se relacionar com vendas, né?

E aí, eu já vou lá elencar quais são todos os outros atributos de produtos. Eu tenho o ID do produto. Toda entidade tem o seu ID. Tem que ter o seu identificador, tá? O produto, quem foi que ele comprou, né? Preciso do ID do comprador. Eu preciso da data que ele comprou. Eu preciso da situação, cartão de crédito, parará, parará, parará, parará, parará.

Então, você tá vendo que a gente consegue elencar aqui, pelo menos, o quê? Uma, duas, três. Três principais entidades. Então, eu tenho os cursos e as características deles. Ou seja, eu tenho que ter o nome do curso. Eu tenho que ter a capa do curso. Eu tenho que ter quais são os instrutores do curso. Eu preciso ter, sei lá, quantidade de módulos do curso. Quantidade de aulas, né? Porventura, eu tenho a parte de vendas, para poder ver quem comprou. E eu tenho os usuários.

Então, vamos tentar definir aqui, no primeiro momento, três principais entidades dentro do nosso sistema. Usuário, venda e produtos, cursos, né? Então, eu tenho esses atores, aluno, funcionário e administrador, com três entidades no nosso sisteminha. Concorda? Beleza.

## Requisitos não funcionais: gamificação, notificações e aulas

Qual que é o próximo passo agora? Eu tenho que perguntar quais são os requisitos funcionais e não funcionais. Então, eu fui perguntando. Isso aqui são muitos requisitos funcionais. Mas, quais são os não funcionais, talvez? Quais são as características que ele quer que eu faça, né? Isso. Então, por exemplo, eu quero que tenha alguma estrutura de gamificação.

Quando eu fiz o processo, o projeto do CSV, foi justamente uma das coisas que, assim, mais bateram na tecla, que queriam muito que o usuário, ele fosse colocado em uma estrutura de gamificação, para sempre mostrar o progresso que ele está, sempre mostrar o que está faltando, sempre dar algum tipo de recompensa para o usuário, para poder instigar ele a poder terminar aquele curso que ele comprou, que ele adquiriu, né? E instigar ele a terminar, a se engajar mais, a estar atento e tudo mais. Então, tem essa estrutura de gamificação.

Se você está querendo fazer uma estrutura de gamificação, eu preciso de uma estrutura de informação muito grande. Porque eu preciso estar sempre alertando o usuário, munindo ele de informações com relação a essa gamificação. Porque é um sistema novo, né? Ele não conhece. Então, o sistema de notificação e informações, ele precisa ser bem trabalhado, né? Uma coisa leva a outra.

Então, o usuário, ele só sabe que ele quer uma estrutura de gamificação, mas como que vai fazer isso? Aí já é papel seu, do designer, né? Do cara que está projetando esse dashboard. Então, eu já preciso de uma estrutura de notificação e informações interessantes, né?

Ah, eu tenho uma estrutura de aulas. Eu preciso disponibilizar a estrutura para poder assistir as aulas, que foi o que a gente colocou aqui. Então, eu preciso de materiais de apoio, né? Eu preciso de uma estrutura de cursos, de aulas, de módulos bem definidos, bem hierarquizados, para poder eu mostrar o progresso para ele. Olha só, essa aula aqui você já assistiu, esse módulo aqui você já assistiu, você já, sei lá, fez 70%, para poder ganhar uma nova medalha dentro dessa estrutura de gamificação, complete 80% desse curso, para poder você passar para a próxima fase, tem um pequeno questionário, tem um pequeno teste.

## Como conduzir a conversa com o cliente

Então, isso tudo você já tem que ir anotando, entendeu? Tudo que eu estou falando aqui, você vai abstraindo conforme a gente vai conversando, fazendo levantamento de requisitos, você vai imaginando, abstraindo e anotando. Então, é literalmente esse processo aqui, que eu faço quando eu tenho algum tipo de reunião.

Então, eu vou perguntando, como é que faz isso? Como é que faz aquilo? Como é que vocês pensam de fazer isso? Qual a estrutura que vocês já têm, entendeu? Qual é a experiência de vocês com relação a isso? O que vocês acham que melhor encaixou no modelo de negócio de vocês? Então, é uma conversa franca com o dono do negócio, para poder entender o negócio dele.

Esse é o primeiro passo, é entender o negócio dele e conforme ele for falando as funções que ele quer desempenhar, eu já tenho que ter a expertise de falar, é possível, não é possível? Dou conta, não dou conta? Como é que é a estrutura que eu tenho que projetar isso aí? E aí, você desenha isso tudo, consequentemente, vai aparecer algumas dúvidas nesse processo e aí, em uma segunda oportunidade, você pode chegar na pessoa e conseguir tirar suas dúvidas e partir para cima desse processo.

Então, pessoal, essa aqui é a estrutura simples do levantamento de requisitos que eu costumo fazer, quando eu tenho algum tipo de cliente. E aí, a gente vai começar a traduzir todas essas informações com o tempo, quando a gente for para a estrutura de wireframes e projetar os fluxos. Então, em uma próxima oportunidade, nós já vamos definir os fluxos aqui, com tudo que a gente conversou até agora. Beleza? Então, falou pessoal, até a próxima!
