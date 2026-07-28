# Connection Pooling — Pool vs. Polling, Vazamento de Conexão e Serverless

Transcrição de vídeo (autor não identificado no material fornecido). Já em português, sem necessidade de tradução — apenas reestruturada em markdown a partir de transcrição bruta sem pontuação/seções.

---

## Pool vs. Polling — desambiguação

É um fato muito triste que, para nós programadores, as palavras em inglês *poll* e *pool* são muito parecidas — por favor, não confunda essas palavras.

- **Poll** (polling): uma pesquisa. Quando você está fazendo *polling*, está tentando o mesmo recurso algumas vezes para ver se ele está disponível.
- **Pool** (piscina): um grupo grande — hoje o assunto é *connection pooling*, um grupo grande de conexões, uma *pool* de conexões.

## O problema: uma conexão por cliente

Quando você tem um servidor, ele está rodando código e provavelmente se conectando com algum banco de dados. Se cada cliente que faz um request abre uma nova conexão com o banco, e você tem 50 clientes, você vai ter 50 conexões. Existe um limite físico de quantas conexões dá para manter.

A estratégia é ter um **pool de conexões** — por exemplo, uma piscina de 20 conexões entre o servidor e o banco de dados — e as que estiverem disponíveis são reutilizadas.

A solução resolve dois problemas:
- Usar eficientemente os recursos.
- Aumentar a quantidade de clientes que dá para servir — se cada cliente precisasse de uma conexão dedicada, o número máximo de clientes seria limitado pelo número máximo de conexões que o banco aceita.

Assim, 1000 clientes fazendo requisições podem compartilhar 20 conexões com o banco de dados. Isso **não causa problema de conflito** — tudo é devidamente abstraído e isolado.

## Por que criar uma conexão é caro

Criar uma conexão é caro a nível computacional, porque envolve vários passos:

- Handshake da network.
- Autenticação.
- Processos de ambos os lados (banco de dados e servidor).
- TLS, se habilitado — overhead adicional.

## O jeito errado

Imagine uma rota de backend (Express ou qualquer framework equivalente) em que, a cada requisição do usuário, o código instancia um client novo (uma conexão nova) e depois encerra essa conexão. Isso é uma conexão por usuário.

Isso **funciona**, mas só até certo ponto — até uns 20-30 usuários simultâneos, aí começa a falhar. 20-30 usuários simultâneos é bastante coisa, então é perfeitamente possível que, em partes de uma aplicação em produção, isso esteja acontecendo sem nunca ter dado problema visível ainda.

## O jeito certo: pool reutilizada fora da rota

A própria lib do Postgres (ex.: `pg` no Node) fornece uma pool. Você consegue:

- Setar um número máximo de conexões.
- Combinar isso com o limite do banco de dados — ex.: o banco aceita 250 conexões, mas você quer reservar apenas 10 para essa parte específica da aplicação, deixando o resto para outras partes/serviços.

A pool deve ser instanciada **fora** da rota. Em Node.js, um arquivo é, na prática, um singleton — então a pool é instanciada uma única vez, e a rota (chamada quantas vezes for, por quantos usuários for) reutiliza essa mesma pool entre todos os requests. Isso depende da linguagem: é preciso entender como cada linguagem lida com isso.

```js
// pool instanciada uma única vez, fora da rota (arquivo é singleton em Node.js)
const pool = new Pool({ max: 10 });

app.get('/users', async (req, res) => {
  const client = await pool.connect();
  try {
    const result = await client.query('SELECT * FROM users');
    res.json(result.rows);
  } finally {
    client.release(); // sempre libera, mesmo se houver erro
  }
});
```

## O bug do `client.release()` esquecido

Um problema recorrente e fácil de identificar (porque estoura a aplicação rapidamente): cada request cria uma conexão, dá `pool.connect()`, mas esquece de dar o `client.release()`.

Ao esquecer o release, a conexão não é liberada de volta para a pool. Uma pool que tinha 10 conexões passa a ter 9, depois 8, 7, 6... até dar problema.

**Solução:** sempre usar `finally` (ou equivalente na linguagem) para garantir que `client.release()` rode mesmo em caso de erro. Se não houver um `finally`, um erro na linha da query pode desviar o fluxo da aplicação e pular a linha do release, vazando a conexão. O autor já viu isso acontecer em produção.

## Ambientes serverless

Em ambientes serverless (ex.: Lambda), não existe memória compartilhada por padrão — cada Lambda é autossuficiente, instancia quando a requisição chega e morre quando a requisição sai. Se 20 requests chegarem, 20 Lambdas são instanciadas.

Num servidor tradicional, a pool fica em memória compartilhada do processo. Lambdas não têm isso, então não dá para simplesmente ter uma pool "normal" dentro do código de negócio — isso cria o mesmo problema de excesso de conexões.

A solução depende exatamente de como o ambiente serverless está montado:

- **AWS**: uma das soluções mais utilizadas é o **RDS Proxy** — um servidor intermediário que mantém estado e mantém a pool. Cada Lambda faz um request para esse proxy, que é onde a pool realmente vive.
- **Vercel**: a Vercel tenta automatizar isso. A documentação da Vercel Functions especifica o uso de **"attach database pool"**. É necessário ler a documentação específica da Vercel para usar — é o *lock-in* da plataforma (toda plataforma tem o seu).
- **ORMs**: a ORM usada (em vez da lib crua do Postgres) provavelmente tem solução nativa equivalente — vale pesquisar na documentação da própria ORM.
- **PgBouncer**: apareceu na pesquisa para o vídeo. Funciona como um proxy — a aplicação faz requests para o PgBouncer, que mantém a pool de conexões com o banco. **Disclaimer do autor: nunca utilizou isso na prática**, citado por completude, mas recomenda usar com cautela.

## Resumo

- *Poll* = pesquisa/tentativa repetida (polling). *Pool* = piscina/grupo de conexões.
- Pool de conexões resolve o limite físico de conexões simultâneas com o banco e reduz o custo de criar/destruir conexões.
- Instancie a pool uma única vez, fora do handler de rota (aproveitando o singleton natural do módulo/arquivo).
- Sempre libere a conexão (`client.release()`) num `finally`, para não vazar conexões da pool aos poucos.
- Em serverless, não há memória compartilhada entre invocações — a solução (RDS Proxy, attach database pool da Vercel, suporte nativo da ORM, ou PgBouncer) depende do ambiente específico.
