# Requisição HTTP por dentro — Métodos, Headers, Body, Middleware e Status Code

Fonte: transcrição de vídeo (autor/canal não identificados na transcrição; o vídeo divulga a plataforma "Eduni", de planejamento de carreira), já em português — sem necessidade de tradução. Transcrição automática colada pelo usuário; foram adicionados apenas pontuação, parágrafos e títulos de seção, e o texto foi limpo de erros de reconhecimento de fala.

Termos corrigidos por contexto (transcrição automática): "poste"/"pôs" → POST; "o peixe" → PUT; "delite" → DELETE; "Friendo"/"FET"/"Fate"/"F" → fetch (provável); "readers" → headers; "bar"/"bar header" → body; "catch control" → Cache-Control; "cook" → Cookie; "autorization"/"autorizated" → Authorization/Unauthorized; "bear" → Bearer; "midware" → middleware; "course" → CORS; "o for Biden" → 403 Forbidden; "400 request" → 400 Bad Request; "errow" → error; "Becken" → back-end; "David Tool" → DevTools; "Jason" → JSON; "Géini"/"cloud" → Gemini/Claude (provável); "300 e um" → 301; "Edúo"/"Eduni"/"edunio.com.br"/"Idonio" → Eduni (grafia incerta, [?]); "Stake" → stack. Frases de fecho do tipo "deixa o like" foram mantidas de forma resumida.

---

## Abertura

A esmagadora maioria dos desenvolvedores usa API todo dia e não faz ideia do que realmente acontece quando ela funciona. Já fez centenas de requisições HTTP, usou Axios, fetch, GET, POST, talvez PUT e DELETE. A pergunta direta: quando você clica em um botão e uma requisição é enviada, consegue explicar o que está acontecendo? Não é decorar "GET busca, POST cria", é entender o que está viajando pela internet. O autor diz que passou anos sabendo usar e até explicar, até entender de verdade — e aí a API "parou de parecer mágica".

Promessa do vídeo: abrir o capô da requisição HTTP inteira — o que tem dentro, o que headers e body fazem, o que acontece no servidor entre o clique e a resposta, o que 200/404/500 realmente dizem — e juntar tudo numa história do início ao fim.

## Requisição e resposta: uma conversa

Situação simples: um site com o botão "ver meu perfil". Ao clicar, o navegador precisa pedir uma informação a um servidor. Isso é uma **requisição HTTP**; a volta é a **resposta HTTP**. Antes de qualquer framework, linguagem ou biblioteca existe uma conversa: cliente pergunta, servidor responde. Mas o navegador não manda simplesmente "me dá o usuário" — existe uma estrutura, uma quantidade enorme de informação numa mensagem que parece pequena.

## Método HTTP

O primeiro elemento é o **método**, que comunica a intenção da requisição: GET = quero obter algo; POST = quero enviar algo ao servidor; PUT = quero alterar algo; DELETE = quero remover algo. O método não é a operação inteira, é **parte da mensagem**.

**Idempotência** (detalhe "que quase ninguém explica direito"): GET, PUT e DELETE são pensados para serem idempotentes — mandar a mesma requisição várias vezes leva ao mesmo resultado final. GET no mesmo usuário 100 vezes não muda o dado; o mesmo PUT duas vezes deixa o registro igual ao da primeira. POST não tem essa garantia: o mesmo POST duas vezes cria dois registros. Por isso telas de pagamento costumam ter trava extra contra clique duplo — um POST duplicado pode cobrar a pessoa duas vezes. Entender isso muda como se decide qual método usar.

## URL: o recurso

Em `/usuarios/42` o cliente não diz "me dê alguma coisa", diz "quero acessar **esse recurso específico**". Ideia fundamental de uma API: não pensar "qual função chamar", mas "qual recurso estou tentando acessar". Essa mudança de mentalidade torna REST muito mais intuitivo.

## Headers

Muita gente usa sem entender: Authorization, Content-Type, Accept, Cookie. São **metadados da requisição** — informação sobre a comunicação, não o conteúdo em si.
- `Content-Type: application/json` — "o conteúdo que estou mandando está em JSON".
- `Authorization: Bearer <token>` — a requisição carrega informação de autenticação.
- `Accept` — qual formato de resposta o cliente aceita receber.
- `User-Agent` — identifica de onde vem a requisição (navegador, aplicativo, bot).
- `Cache-Control` — se a resposta pode ser guardada e reaproveitada ou não.

Cada header é "uma frase dentro da conversa". O header não é necessariamente o dado que você quer enviar; ele descreve como a comunicação deve ser interpretada.

## Body

Para criar um usuário é preciso mandar nome, e-mail e senha: isso vai no **body**. O header descreve a mensagem; o body carrega o conteúdo. Analogia: uma encomenda — a informação na etiqueta e o conteúdo dentro da caixa não são a mesma coisa.

## O código é só a interface

Quando se escreve `fetch(...)`, vê-se uma linha de código que esconde toda a conversa: o navegador constrói a requisição (método + URL + headers + possivelmente body) e a envia. O código é a interface para produzir essa comunicação.

**HTTPS**: hoje a conversa quase sempre acontece dentro de uma camada criptografada. O "S" significa que, antes da requisição sair, navegador e servidor negociam uma criptografia; quem interceptar o tráfego no meio do caminho não consegue ler o conteúdo. O cadeadinho ao lado do endereço diz "essa conversa está protegida".

**Ferramenta ≠ protocolo**: você não manda um fetch, você manda uma requisição HTTP. fetch, Axios, Postman e o navegador são ferramentas; por baixo a conversa continua sendo HTTP. Quem entende HTTP deixa de ficar preso a uma biblioteca e entende qualquer stack.

## Parêntese: Eduni (divulgação)

Pausa para falar da plataforma **Eduni**, criada pelo autor: planejamento de carreira — você mapeia onde está e para onde quer ir e ela ajuda a montar o caminho "sem achismo". Mesma lógica do vídeo: não decidir tudo no automático/improviso. Link na descrição e no comentário fixado; o plano pago desbloqueia o acompanhamento completo. (Conteúdo promocional; sem valor técnico.)

## No back-end: rota → middleware → controller → service → banco

O servidor recebeu a requisição e precisa decidir o que fazer: existe uma rota; a rota chama um **controller**; o controller chama o **service**; o service conversa com o **banco de dados**. Entre a rota e o controller geralmente há uma etapa pouco comentada: o **middleware**, "um pedágio no meio do caminho". Antes de chegar ao controller, a requisição passa por camadas que verificam: o token de autenticação é válido? o usuário tem permissão para essa rota? o corpo está no formato esperado? Se alguma verificação falha, a requisição nem chega ao controller e o servidor já devolve uma resposta — geralmente **401** ou **403**. Por isso às vezes uma requisição "certinha" nunca chega ao código de regra de negócio: foi barrada no meio do caminho.

## A resposta e os status codes

O usuário foi encontrado, o back-end consultou o banco, o banco devolveu os dados; o servidor monta outra mensagem, a **resposta**, também com estrutura: status, Content-Type e o conteúdo.

"200 é sucesso, 404 é não encontrado, 500 é erro" não está errado, mas é uma simplificação gigantesca. O status code **comunica o resultado da intenção**:
- **200 OK** — requisição processada com sucesso.
- **201 Created** — recurso criado.
- **400 Bad Request** — a requisição não está adequada para ser processada.
- **401 Unauthorized** — autenticação não fornecida ou inválida.
- **403 Forbidden** — o servidor sabe quem você é, mas você não tem permissão.
- **404 Not Found** — o recurso solicitado não existe.
- **500 Internal Server Error** — algo quebrou no lado do servidor.
- **301 Moved Permanently** — o recurso mudou de endereço de forma definitiva.
- **429 Too Many Requests** — você bateu no limite de requisições num período (rate limit).

Não pensar "se não for 200, deu erro", mas "o que o servidor está tentando me comunicar com esse status?". Com isso, `fetch` deixa de ser "mágica que pegou os dados" e passa a ser "iniciei uma comunicação HTTP com um recurso específico e aguardo a resposta".

**HTTP ≠ JSON**: JSON é o formato do conteúdo; HTTP é o protocolo de comunicação.

## DevTools

Ao abrir o DevTools na aba Network, vê-se os pedaços da conversa: URL, método, headers, request payload, status code, response.

## As peças se encaixam

Por que existe CORS? Porque existe uma política sobre comunicação entre origens diferentes. Por que existem cookies? Porque o cliente pode enviar informação associada a uma sessão. Por que Authorization? Para transportar credenciais. Por que JWT? Um token pode fazer parte do mecanismo de autenticação. Por que Content-Type? Para comunicar como o conteúdo deve ser interpretado. Por que status code? Para o servidor comunicar o resultado da interação.

**HTTP vs WebSocket**: HTTP é pergunta e resposta, uma troca pontual. WebSocket é uma conversa que fica aberta: os dois lados podem mandar mensagens a qualquer momento sem abrir uma requisição nova a cada vez. Os dois começam com uma negociação parecida.

## Maturidade: de "estou fazendo uma requisição" a "estou enviando uma requisição HTTP"

Conforme se amadurece, olha-se além do código e perguntam-se: qual método, qual recurso, quais headers, tem Authorization, tem body, qual status voltou, o que veio na response, o que o servidor fez, o banco foi consultado?

**Exemplo 1 — 401.** Quem só decorou: "deu erro de autenticação, vou tentar de novo". Quem entende: mandei o header de autorização? com o nome certo? o token ainda é válido? mandei `Bearer <espaço> token` ou esqueci o "Bearer" e mandei só o token? Às vezes o bug não está na lógica gigantesca do back-end, está numa letra maiúscula errada no nome do header ou num espaço que faltou.

**Exemplo 2 — erro de CORS.** Quem não entende HTTP copia a mensagem, procura solução mágica, abre ChatGPT/Claude/Gemini. Mas CORS não é bug aleatório: é o navegador aplicando uma política de segurança porque a **origem** que fez a requisição é diferente da origem do servidor que respondeu. Entendendo isso, para-se de procurar gambiarra e vai-se ao que resolve: **configurar o servidor para permitir aquela origem específica**. Método: abrir o DevTools na aba Network, olhar a requisição que saiu, comparar com o que o servidor esperava e achar onde a conversa quebrou.

## Fecho

O vídeo cobriu a anatomia completa de uma requisição, o que headers e body fazem, o que rola no servidor e o que os status codes significam — o ciclo do clique até a resposta voltar à tela. Não decorar "GET busca, POST cria, 404 não encontrou, 500 erro": isso é só o começo; enxergar a conversa inteira transforma a API de caixa-preta em algo compreendido. É a diferença entre quem só faz a aplicação funcionar e quem olha uma aplicação quebrada e descobre por que não funciona. Fecha com pedido de like e nova chamada para a Eduni.
