# Estado global: por que evitar, side effects e reprodutibilidade de bugs

Fonte: transcrição de vídeo, colada pelo usuário em 2026-10-06. Já em português — sem tradução. Autor: Augusto Galego (inferido: o locutor se chama "galego", cita "cupom galego" e um curso completo de System Design). Adicionados apenas pontuação, parágrafos e títulos; erros de reconhecimento corrigidos por contexto.

Termos corrigidos (reconhecimento automático): "arisca / a pace Rest" → REST; "stat" → stateless; "Heads / headges" → Redis; "login / Login" (na classe de checkout) → logger; "porte" → port; "rono" → Hono; "SOF Elements" mantido como no áudio (patrocinador, cadeira); "um monte de a sem noção" → provável "um monte de IA sem noção" (não confirmado); "achar pelo novo" → "procurar pelo em ovo" (provável).

---

## Abertura (patrocínio)

Antes de comprar o próximo mouse ou teclado: "a sua cadeira é boa?". O patrocinador (SOF Elements) vende a cadeira como peça central do setup, com cupom "galego". O autor comenta que é um tipo de vídeo que provavelmente "flopa" e que não há muito como fazer bait com o tema: **estado global**. Mistura de código e system design.

## Estado global e o HTTP stateless

O objetivo do HTTP/REST é ser **stateless**: cada requisição carrega tudo que é necessário para executar a ação, e o servidor não precisa estar em nenhum estado específico. Como o servidor sabe que você é você ao navegar de uma página do YouTube para outra? Como as requisições são independentes, cada uma precisa conter um identificador provando quem você é.

Intuitivamente sabemos que não faz sentido escrever no servidor `currentUser = galego` e supor que o "usuário atual" é o último que fez login. As requisições chegam em paralelo e cada uma precisa responder com o conteúdo do **seu** usuário (o autor e o espectador acessam o YouTube ao mesmo tempo e cada um recebe suas recomendações).

## Formas menos óbvias de estado global

- **Cache dentro do servidor:** muito comum inicializar um cache (Redis é associado a cache; é um banco in-memory) ou um cache ingênuo como um `Map` dentro do servidor. Esse cache representa estado global.
- **Variáveis de módulo (JavaScript):** uma variável no topo de um arquivo, como `port = 3000`, faz o arquivo se comportar como um **singleton** e a variável como global. Se alguma requisição de algum usuário alterar essa variável, ela muda para o sistema inteiro. Muitas linguagens têm algo similar.
- **Configurações e coisas exportadas de módulos** também podem ser estado global.
- **Erro típico:** uma `currency` (moeda) instanciada fora de um método ou numa classe compartilhada; depois `setCurrency` e `formatCurrency` para imprimir bonitinho. Ou um `discount` global com uma função que altera o desconto e `calculatePrice` que calcula o preço com base nele. Os exemplos são óbvios, mas na prática os bugs são **sutis** e aparecem em diversos tipos de aplicação.

## Duas boas práticas violadas

Uma função **não deve depender de algo externo** e **não deve gerar side effects**: deve receber as variáveis de que precisa e não alterar nada fora dela. O exemplo do desconto viola as duas:

1. `calculatePrice` depende de um `discount` instanciado fora dela.
2. `enableBlackFriday` altera o desconto e **não retorna nada**; a única coisa que faz é gerar um side effect.

Efeitos colaterais alteram o estado do servidor, e **a ordem em que você invoca os métodos altera o resultado final** — contra o princípio de ser stateless. Se o desconto não é passado para dentro da função, ele é compartilhado entre a aplicação inteira, entre todos os usuários; qualquer coisa que o altere muda para sempre o funcionamento de `calculatePrice`.

Linguagens funcionais têm ganhado tração em parte por valorizarem isso: não gerar side effects e funções autocontidas que recebem tudo de que precisam. Detalhes da programação funcional aparecem cada vez mais em Python e TypeScript.

Esse tipo de coisa cria **contaminação**: uma requisição contamina a outra, e o **momento** em que as coisas são chamadas passa a importar.

## Reprodutibilidade de bugs

Não dá para reproduzir um bug causado numa função sem reproduzir todo o estado externo de que ela depende. Se chamo `calculatePrice(30)`, não consigo saber o retorno sem saber o valor do desconto setado fora. Então, quando um bug acontece, muitas vezes não é possível reproduzi-lo apenas chamando a função com os mesmos parâmetros — "terrivelmente péssimo".

Em produção o cenário típico: o usuário chama `calculatePrice` com 30, a função gera um erro; você pega os parâmetros dos logs e, na máquina local, **não consegue reproduzir**. Por quê? Porque o erro só ocorria para um usuário com condição especial (por exemplo, um usuário *retail* e um produto cujo estoque era zero). Isso é sinal de que a função depende de **estado externo** (provavelmente um banco de dados): para causar o erro ela precisa identificar que o usuário é retail e que o produto está zerado, e se isso não é parâmetro, veio de outro lugar. Aqui já se foge um pouco de "estado global" para "funções dependendo de coisas externas", mas o problema é a **dificuldade de reprodutibilidade**: as condições do erro não são visíveis nos logs.

O estado global também pode criar **race conditions**: dois requests em paralelo acessando e alterando o mesmo estado.

## Dependência externa x não externa

Contraste: uma função que vai adicionando valores a um `subtotal` externo depende de algo externo; uma função `calculateSubtotal` que simplesmente recebe uma lista e roda um `reduce` não depende.

## Nem todo estado global é ruim

Se nada altera o `port`, não há problema. Uma constante como `MAX_UPLOAD_SIZE = 10 * 1MB * 1GB` também está OK.

## Soluções

### 1. Estado local, passado explicitamente

Cada função tem o seu estado. Objeção: "mas eu preciso saber qual user tem cada coisa" — o exemplo `currentUser = user` é "muito tosco". Provavelmente o usuário será buscado num banco em algum momento; a questão é que, ao buscar, você o **passe explicitamente** para dentro da função, porque a mesma função, dado o mesmo input, deve retornar o mesmo output. A única exceção são funções que acessam explicitamente o banco de dados ou uma API externa. Se a função é puramente código, deve retornar o mesmo output. Passando o usuário na chamada, o bug fica **mais reproduzível**: se você consegue ver como o objeto de usuário foi construído, consegue passar o mesmo objeto e reproduzir os mesmos bugs.

Ainda pode haver um "bugzinho": tudo que conecta ao banco interage com algo fora do código que nem sempre dá para controlar. O autor acha que não há como evitar isso.

### 2. Request context

Muito popular: cada requisição agrupa uma quantidade de **contexto**, e esse contexto vai sendo passado adiante para todo mundo saber o que entrou de input. Ao logar, depurar ou reproduzir, entender o que aconteceu fica muito mais fácil. Muitos frameworks, empresas e codebases adotam esse padrão.

### 3. Injeção de dependência

Uma dependência externa **invisível**: uma função que cobra o valor de uma `order` usando um `paymentProvider`, instanciado fora da função. Parece que está tudo certo, mas o provedor de pagamento também é estado externo — não se sabe como foi instanciado nem o que estava acontecendo quando a função foi chamada.

A forma de não depender de algo externo dentro da função e ainda usá-lo é a **injeção de dependência**: uma interface `PaymentProvider`, uma interface `Logger`, e um `CheckoutService` (classe) que recebe as duas no construtor. Dentro da função específica não há todo o contexto, mas, considerando a classe instanciada e seu estado atual, **é possível saber qual era o provedor de pagamento naquele momento**. DI ajuda a lidar com o contexto compartilhado e o estado global.

### 4. Configuração

Exportar uma configuração não é, para o autor, um grande problema; está "perfeitamente OK". O único risco é algum outro lugar do código alterar esses valores. Quem quiser programar de forma extensivamente defensiva pode **carregar a configuração uma única vez** (função que roda só quando o servidor inicia) e transformá-la num objeto **read-only** que nunca mais será alterado. Opinião pessoal: geralmente não precisa; talvez se o time tiver "um monte de IA sem noção" causando problemas.

## Frameworks

Você pode dizer "eu não tenho esses problemas, meu framework resolve". Provavelmente o framework usa o **contexto da requisição**. Frameworks de request/response (FastAPI, Hono, Express) te **induzem a não compartilhar contexto**. Não garante que você sempre agirá certo, mas induz a não errar — e, seguindo o tutorial, você segue os bons princípios. Quando precisar de algo externo (banco, API), é inevitável depender disso.

## Fechamento

O autor admite que "não tem como fazer esse vídeo ser muito impactante". Promove o curso completo de System Design (link na descrição; 30 dias para pedir reembolso integral).
