# ORM vs. SQL Puro: Organização de Regras de Negócio e Escolha de Banco de Dados

**Tema:** Respostas a perguntas do chat de uma live sobre as limitações do ORM em sistemas com relacionamentos profundos, como organizar regras de negócio em SQL (stored procedures, functions, triggers), o que faz sentido mover para o banco de dados vs. manter na aplicação, e como escolher entre banco relacional e não relacional.
**Data de captura:** 2026-07-03
**Nota:** transcrição de áudio limpa e reorganizada a partir de um texto gerado por transcrição automática (com diversos erros de reconhecimento de fala, ex.: "história possível" → "stored procedure", "trilhas" → "triggers", "cores"/"correr" → "queries"/"query", "curva" → "cursor", "banco no circo" → "banco NoSQL"). Trechos ambíguos foram reconstruídos pelo contexto e podem conter imprecisões.

---

## Transcrição

### ORM e relacionamentos complexos

Então tá bom. Olha só, o [pessoa do chat] falou assim: "Ah, você fala muito sobre o ORM, e eu percebo que algumas lógicas ficam quase impossíveis de usar com o ORM." Isso acontece principalmente em sistemas que têm muito relacionamento, né — quando você tem uma profundidade de relacionamento muito grande, muita chave composta, isso vai acontecer, tá.

Ele complementa: "E isso vai nos obrigar a usar muito o SQL diretamente." Beleza, é isso mesmo, tá — é isso que acontece.

### Como organizar regras de negócio em SQL

Vamos lá: como você organiza o SQL quando chega um ponto em que você tem muita regra de negócio? Nesse caso a gente acaba criando uma **stored procedure** pra determinar a regra. Gostei da pergunta, vamos lá.

Olha só, respondendo: é melhor a gente escrever queries mais curtas e mais específicas, porque eu não gosto tanto de ORM, exatamente pelo que a gente acabou de falar em relação à escalabilidade. Quando você usa muito o ORM, a tendência é que essas queries não sejam otimizadas. Já quando você escreve a query diretamente, você sabe quais tabelas vai relacionar — tô falando de banco SQL, se for NoSQL é outra história.

Quer dizer: você sabe exatamente como vai relacionar essas tabelas, quais colunas vai retornar, que tipo de cláusulas vai usar, se está batendo o índice ou não. Então você tem muita precisão naquilo que está fazendo.

### O que faz sentido mover para o banco de dados

Agora, sobre essa questão de mover coisas mais para o banco: como eu estruturo isso, que foi o que ele perguntou? É assim: em termos de responsabilidade, o que é da aplicação e o que é do banco?

Um exemplo: imagine que você tem, como é o nosso caso, um milhão de faturas — fatura de cartão de crédito, fatura de conta de luz, fatura de conta de água — e você precisa saber, por exemplo, qual é o volume de inadimplência que você tem em um determinado mês, junto com os pagamentos que você já recebeu, em termos de volume.

Então, pra mim, não faz sentido você usar um cursor e tirar um milhão de faturas do banco de dados, trazer pra memória da aplicação, pra executar uma regra e fazer uma apuração até chegar no total. Faz sentido você mandar o banco fazer isso — nessa escala, não há servidor de aplicação que aguente. Se você fizer isso na aplicação, fica muito pesado, fica muito difícil, principalmente com um volume grande de dados.

Então algumas coisas você invariavelmente vai acabar levando pro seu banco. Agora, eu tento me manter fora das stored procedures, fora das functions, fora das triggers — é bom até certo ponto, mas eu já acho que você está passando de um ponto que eu considero saudável, apesar de reconhecer que existem casos e casos.

Por exemplo: acho que muitas vezes a criação de uma **view** pode ser muito legal — uma materialized view, em que você tem um nível de cache. Então pensa nisso: nem sempre vale a pena você extrair metade do banco de dados pra aplicação pra obter um valor. Às vezes vale a pena, sim, compartilhar responsabilidades até onde faça sentido pra você reduzir, principalmente, essa carga que você coloca no banco.

É por isso que eu sempre digo: relatório sempre tem que bater num banco réplica. Você não deve colocar relatório pra bater no banco de produção, porque, se você bate no banco de produção, você está concorrendo com uma série de outros processos mais importantes que esse — pensa comigo, é uma parte do sistema que está tirando espaço do sistema de rastreamento de veículos, do sistema de chamada telefônica...

Mas boa parte dos sistemas: você escreve muito menos do que você lê — você escreve uns 10% do tempo. Então você pode, sim, obter muita escala tendo réplicas e economizando um pouco naquilo que você está extraindo do banco. Show de bola, galera, tá falando um monte de coisa aqui no chat.

### Banco relacional ou não relacional?

Pergunta da Bruna: "Qual o melhor tipo de banco pra você — relacional ou não relacional?" O Renan Mateus perguntou algo parecido: "Depende do cenário."

Assim, eu acho que a característica da aplicação é que vai te fazer entender a moral do banco relacional. Em geral, no banco relacional você tem um esquema, você tem uma formalização das suas tabelas e dos seus relacionamentos. Isso te dá a habilidade de chegar num dado por vários caminhos, fazendo diferentes tipos de junções — essencialmente, teoria dos conjuntos.

Se o teu sistema tem essa característica, essa necessidade, não tenha dúvida: você precisa de um banco relacional.

Agora, se você vai fazer machine learning, se vai montar um data lake, se é simplesmente pegar um bocado de dado não estruturado pra jogar em algum lugar e fazer alguma coisa com ele — de repente um banco não relacional te ocorre. Lembrando que não é só um: existem várias estratégias de banco não relacional, tem banco orientado a grafo, tem orientado a documento. Então você tem que ver qual é a sua necessidade e, assim, achar a melhor ferramenta pra ela, tá bom.

Só que é muito bom também lembrar que existem bancos relacionais que têm características de bancos não relacionais — por exemplo, possuem coluna JSON, inclusive com indexação. Então isso pode te ajudar bastante a não precisar ter uma infra muito complexa, tá bom.

Mas essa discussão é maravilhosa, é maravilhosa mesmo, não tem dúvida. Foi bom.
