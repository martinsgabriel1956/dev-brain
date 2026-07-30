# Índice do Banco de Dados

> Transcrição de vídeo em português. Início com propaganda de patrocinador (cadeira ergonômica Sfia) preservada por completude, sem relação com o conteúdo técnico.

## Abertura / Patrocínio

Você já ficou sentado horas numa cadeira horrível, tudo nas costas e no pescoço emperrado? Trabalhar muito tempo na cadeira correta é completamente diferente disso. A Sfia Elementos reclina até 150º, tem apoio no lombar ajustável, braço 3D e mesh respirável. Clica no link na descrição, usa o cupom Galego e vem sentir a diferença.

Série nova no canal: vamos falar sobre conceitos importantes da programação em pouco tempo.

## O que é um índice

Conceito de hoje é o índice do banco de dados. Quando você cria uma tabela no seu banco de dados, geralmente é criado um índice na sua chave primária. No caso do Postgres isso sempre vai acontecer: sua chave primária geralmente é um ID, então já existe um índice criado no ID no seu banco de dados — você não precisa criar um índice para isso.

Mas fica a pergunta: o que é um índice, para que ele serve, por que a gente cria ele?

Um índice é uma estrutura de dados subjacente no seu banco de dados que vai ajudar a acessar esses dados de maneira mais rápida. SQL é tradicionalmente estruturado e orientado a linhas e colunas. Então, imaginando uma tabela que você tem — ID, nome, e-mail — de repente você faz um `CREATE`, e o seu banco de dados vai armazenar estes dados internamente. Ele vai armazenar o ID 1, o nome Augusto, o e-mail, e o timestamp do `CREATE`.

Para além dessa estrutura de base, um índice vai criar uma estrutura adicional. Por quê? Vamos supor que você queira encontrar o ID 300. Caso não existisse um índice, o banco de dados precisaria checar todas as linhas, linha por linha, uma atrás da outra, até encontrar o ID 300. Se, por exemplo, você tá buscando pelo nome "Fernando" e não existe um índice na tabela de nome, o seu banco de dados precisa escanear a tabela inteira e olhar linha por linha até achar o nome Fernando. Como você pode estar imaginando, isso é custoso e lento. Então a gente cria um índice — o índice faz com que essa busca seja muito mais rápida.

## Como o índice é criado (B-tree)

Existem diferentes estruturas de dados que o seu banco de dados pode criar para serem utilizadas como índice. O índice padrão do Postgres é um índice de B-tree — um dos índices mais comuns.

Vamos adicionar alguns números de ID, imaginando um número de ID sequencial: inserir o ID 1, inserir o ID 2, o três, o quatro. Nota: essas inserções estão alterando a estrutura da minha B-tree. O cinco também entra. Aqui temos a nossa B-tree.

Essa estrutura de dados adicional vai ser armazenada em conjunto com os nossos dados — então a gente tá tomando mais espaço. Como você viu na criação, essa B-tree vai se reordenando conforme os elementos entram. Essa reordenação também tem um custo computacional.

Então o que a gente pode inferir daqui: os índices vão tornar as suas tabelas no banco de dados necessariamente mais pesadas, e as suas inserções — as criações de novos usuários, as criações de novos IDs — mais lentas. Porém a busca vai ser muito mais rápida.

Antes, se eu quisesse buscar o ID 7, eu teria que percorrer 1, 2, 3, 4, 5, 6, 7 até encontrar o sete. Agora, se eu quero buscar o ID 7, eu vou vir na minha B-tree, nessa estrutura de dados, e vou olhar: o cinco é maior ou menor do que quatro? É maior. Vou para a direita. O sete é maior ou menor do que seis? É maior. Então vou para cá, e encontrei o meu sete. Eu encontrei ele em três etapas, escaneando apenas três coisas, ao invés de ter que escanear sete linhas na minha tabela. Por isso um índice torna a busca mais rápida.

## Quando criar (e quando não criar) um índice

Como ele torna a escrita mais lenta e a busca mais rápida, a gente só vai querer criar um índice quando fizer sentido. Isso responde a pergunta comum de: "por que não criamos índices em tudo?" É porque, se a gente não executar muitas buscas em cima daquele índice, não vale a pena criar um índice naquilo.

## B-tree e range queries

Uma das vantagens do índice de B-tree é que ele é muito bom para fazer *range*. O que é range? "Encontra para mim todos os IDs entre 1 e 3." Note que na imagem, todos os IDs entre um e três ficam juntinhos, por causa de como uma B-tree funciona. Isso vai funcionar para `created_at` também: se a gente criar um índice no `created_at`, a gente vai conseguir encontrar com facilidade todas aquelas linhas que foram criadas entre determinado momento no tempo e determinado momento no tempo. Então, para buscas em range, B-tree é um tipo de índice muito bom.

Agora, B-tree não é o único tipo. Ele é o padrão, ele é o mais comum, mas não é o único.

## Índice Hash

Existe também o índice hash. O que é o índice hash? Se você já estudou o que é um hash map, um dicionário, ou key-value, é a mesma coisa: você vai ter uma chave — que vai ser um hash — e ela vai apontar para um valor. O nome "Augusto", se eu passar por uma função hash, vai cuspir sempre o mesmo hash. Então vai existir uma tabelinha onde eu tenho a chave e o valor, e essa tabelinha vai ter todos os pares de chave e valor. Existe a possibilidade de conflito de hash, mas não vou falar sobre isso agora.

O índice hash não funciona para range, não funciona para ordenação, não funciona para prefixo. Ele só funciona com match exato. Então ele não vai ser bom caso eu queira procurar por nomes que começam com "Augus" — não funciona, tem que ser match exato, tem que ser exatamente igual.

Dito isso, se for para match exatamente igual, o hash tem uma vantagem muito boa de velocidade. A velocidade dele é muito boa porque a complexidade média de busca num hash é O(1). Claro, existe conflito e tal, mas vamos ignorar isso — hash é bom para esse caso de uso.

## Índice composto

Um índice muito comum também é o índice composto — composto de duas colunas diferentes. Então, de repente, eu vou criar um índice composto em cima de `name` e `email`. O índice composto, por padrão, também vai ser um índice de B-tree — ele também vai utilizar uma B-tree. São conceitos que não entram em conflito: o índice composto diz respeito apenas àquilo que vai ser indexado — a gente vai juntar essas duas colunas — mas a estrutura de dados subjacente vai continuar sendo uma B-tree.

## Índice único vs. não único

Ainda falando sobre índices, você pode criar índices que são únicos ou índices que não são únicos. Novamente, isso não entra em conflito com o fato de ser composto ou não, de ser uma B-tree ou não. O índice único diz respeito apenas a se aquele campo vai ser único ou não, para prevenir valores duplicados. Por exemplo, o ID, por padrão, é um identificador único — senão não tem propósito. Porém, se eu criar um índice no nome, eu posso muito bem criar um índice que não é único, já que muitas pessoas podem ter o nome Augusto.

## Índice parcial (partial/filtered)

Existe também a possibilidade de criar um índice parcial, *partial* ou *filtered*, em que a gente vai criar um índice apenas em parte da tabela, onde vai existir uma condição — os elementos que preenchem essa condição entram no índice, os que não preenchem não entram. É bom quando a gente quer acessar um subset de dados que é muito comumente acessado.

## Full-text index

Temos também, entrando um pouco mais em complexidade, o full-text index. Isso vai trazer um índice invertido para a gente poder fazer buscas dentro de um texto completo. Funciona muito bem em documentos. O armazenamento dele acaba sendo muito pesado, porque ele vai mapear tokens ou palavras individuais — ele vai fazer um mapa de qual palavra aparece em qual texto. É um caso de uso bastante específico, mas se você tem esse caso de uso, um full-text index é muito bom.

## Índice espacial (spatial)

Temos o spatial index — espacial, para geolocalização, coordenadas. Funciona muito bem se você tem esse caso de uso: por exemplo, "quero encontrar restaurantes que estão a 2 km dessa posição geográfica". Se você não tem esse caso de uso, ele é perfeitamente inútil.

## Outros tipos (mencionados, não aprofundados)

Existem outros tipos também, a gente poderia ficar citando muitos — covering index, clustered index — mas para manter o vídeo mais simples, a ideia aqui é trazer o que é um índice, como ele funciona, como ele é armazenado de fato dentro do seu banco de dados, e quais os tradeoffs.

## Regra de ouro: padrão de acesso

Eu espero que você tenha entendido isso, e que utilize dessa informação para entender quando vale a pena criar um índice e quando não vale a pena. Regra de ouro: o índice que você vai criar deve ser guiado pelo padrão de acesso — com que frequência você acessa esses dados e como essas buscas são feitas.

Por exemplo, numa rede social eu frequentemente busco por usernames — busco por "@augusto", por exemplo. Como essa busca é muito mais frequente do que a inserção de um username novo (a criação de um usuário novo), é muito interessante eu criar um índice em cima desse username.

Agora depende: eu quero que a minha feature seja boa em dar match parcial? Se eu quiser, B-tree vai ser interessante. Se eu quiser apenas matches exatos, hash pode ser uma opção legal. Então índice é sempre criado baseado no padrão de acesso e na necessidade da sua aplicação.

## Encerramento

Curtiu esse vídeo? Estamos a cinco dias sem falar sobre... deixa um like, dá um subscribe se você quiser aprender sobre computação de verdade, de uma maneira simples, sem firula, e eu espero que didática. Se você quiser aprender mais comigo, temos cursos aqui na descrição — a gente tem um curso de system design onde eu falo bastante sobre índices em bancos de dados, e sobre diversas coisas para te preparar para uma entrevista de system design. E beijão por hoje, é isso.
