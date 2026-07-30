# PKCE — Como Proteger Autenticação em SPAs e Apps Mobile

Transcrição de vídeo/áudio em português (canal técnico, apresentador Bernardo Lobato). Já no idioma original — sem necessidade de tradução.

---

Você já se deparou com a missão de implementar autenticação diretamente de uma single page application ou de um app mobile e ficou se perguntando como esconder um client secret de forma segura no lado do cliente? Ou pior: já implementou esse mesmo client secret live do cliente sem se dar conta de que, se um atacante intercepta o seu código de autorização, ele pode se passar por você — e aí o estrago já tá feito. Tá tentando encontrar uma maneira de garantir que os seus tokens de autenticação e autorização sejam disponibilizados exatamente para quem fez a solicitação deles, e que eles não caiam em mãos erradas? Então esse vídeo é para você.

No vídeo de hoje a gente vai ver o que é o fluxo PKCE (Pixi, pros íntimos), como ele ajuda a resolver essa vulnerabilidade, e por que ele se tornou padrão absoluto no OAuth 2.1 — até mesmo para backends robustos. Já abre seu DevTools aí e vasculha o localStorage atrás de um client secret que o vídeo já vai começar.

Olá, dev. Eu sou Bernardo Lobato e hoje a gente vai falar sobre essa dor que passamos sempre que surge uma single page application ou aplicativo mobile que interage com o servidor OAuth: a de garantir que o token repassado pelo Authorization Server não seja interceptado pelo meio do caminho, e que somente quem pede o token é quem pode recebê-lo e de fato usá-lo. Esse aqui é mais um vídeo da nossa série sobre APIs, e uma continuação do vídeo que fala sobre OAuth, OpenID e OpenID Connect — se você ainda não assistiu, tá no card, já deixa preparado numa aba do lado.

## O problema: client secret não tem onde se esconder no cliente

Antes de continuar com a solução, vamos entender o problema que ela visa resolver. A gente já sabe que, para uma aplicação se autenticar com outra usando OAuth com OpenID Connect, ela precisa do fluxo de client credentials: um client ID e um client secret, ou, na informalidade, uma conta de serviço. Esse fluxo já foi detalhado em vídeos anteriores.

O design do OAuth foi pensado originalmente para comunicação entre servidores — back end para back end — onde esse segredo ficava guardado a sete chaves num servidor protegido, muitas vezes criptografado, e sempre bem longe dos olhos do usuário final. E o dev viu que isso era bom, até não ser mais.

Nos anos 2000 era comum a aplicação web "tradicional", que funcionava assim: o cliente recebia o HTML já renderizado, tudo processado, e não tinha nenhuma ou pouquíssima inteligência. Todo o processamento e a renderização eram feitos do lado do servidor. No caso de autenticação, isso era feito por baixo dos panos, sem que o cliente percebesse o que estava acontecendo.

No entanto, por volta de 2012–2013, começou a se popularizar o que hoje conhecemos como single page application, em que — entre outras características — o cliente passou a ter suas próprias responsabilidades, como uma aplicação mais independente, fazendo chamadas diretas à API. Muitos comportamentos como renderização e redirects, que antes eram feitos pelo backend no modelo tradicional, agora são feitos pelo client.

A partir daí começamos a adicionar complexidade do lado do cliente, fazendo com que informações sensíveis que antes eram exclusividade da API ou do back end passassem a ser relevantes também para esse lado. Quando você faz autenticação em uma single page application, todo o código da aplicação roda no navegador do usuário — isso impacta diretamente na segurança. Diferente do modelo anterior, não existe um lado servidor protegendo seus secrets. Tudo que tá ali — JavaScript, variável, chamada HTTP — pode ser inspecionado facilmente por qualquer pessoa com o DevTools aberto. No fluxo tradicional, esses dados sensíveis nunca são disponibilizados ao navegador de maneira nenhuma.

Sem uma forma de garantir que quem pedia o token era a mesma instância que iniciou o processo de login, a gente ficava num beco sem saída: ou aceitava o risco de ter o código de acesso roubado por um aplicativo malicioso, ou usava fluxos paliativos que entregavam o token de acesso diretamente na barra de endereço do navegador — o que também já é um problemão por si só, como veremos agora.

## O Implicit Flow e por que ele falhou

Uma das tentativas mais populares de resolver esse problema foi a implementação do Implicit Flow dentro do OAuth. O fluxo funciona assim:

1. O navegador, com a single page application, pede diretamente ao Authorization Server um token.
2. O usuário faz login e dá consentimento sobre suas informações.
3. O servidor redireciona de volta já com o access token na URL, a partir do fragmento (`#`).
4. A single page application lê esse token via JavaScript.
5. A single page application passa a chamar a API usando esse access token.

Nesse fluxo, tanto o access token quanto os dados de introspecção e controle desse token são devolvidos via URL para o aplicativo de origem. A partir daí o frontend captura esses fragmentos, chama o callback do back end, salva o token na sua própria estrutura e começa a fazer as chamadas autorizadas.

O grande problema dessa abordagem é que os tokens e demais informações sensíveis seguem sendo expostos via URL. Isso é uma baita falha de segurança, porque a partir daí temos:

- **Vazamento no histórico**: como o token passa pela barra de endereço, ele fica salvo no histórico do navegador do usuário.
- **Interceptação fácil**: o velho problema do man-in-the-middle — extensões de navegador maliciosas, proxies, aplicativos espiões do celular podem facilmente interceptar esse redirecionamento e roubar o token em texto claro.
- **Sem refresh token**: justamente por ser um canal inseguro, boas práticas proibiam a emissão de refresh tokens nesse fluxo implícito — o usuário precisava logar de novo com muito mais frequência.
- **Falta de prova de posse**: o servidor de autorização entregava o token via URL, mas não tinha como provar que a aplicação recebendo aquele token era a mesma que iniciou o pedido. Esse é o principal motivador deste vídeo.

Em suma, precisamos garantir que o cliente que recebe o token é o mesmo que solicitou. No backend isso é fácil: dá-se um client ID e um client secret pra ele, que autentica por baixo dos panos diretamente no servidor de autorização. Mas no client, se colocarmos um client secret disponível, ele vai estar vulnerável — qualquer pessoa que saiba usar o DevTools vai conseguir achar. Rapadura é doce, mas não é mole não.

## Alternativas que evoluíram com o tempo

Existem algumas alternativas que evoluíram com foco em clientes mais complexos e independentes do back end:

- **DPoP** (Demonstrating Proof of Possession)
- **mTLS**
- **BFF** (Backend for Frontend) — apesar de ser um padrão arquitetural, pode ser usado como um frontend intermediário, uma ponte para mitigar esse problema (modelo híbrido stateless/stateful, tema de vídeo futuro)
- **PKCE** — o tema deste vídeo

## PKCE: Proof Key for Code Exchange

O PKCE (ou "Pixi") é uma extensão do fluxo de código de autorização (Authorization Code) para prevenir ataques de injeção de código de autorização. Foi criado pela **RFC 7636**, em 2015, quando esse problema do Authorization Code Flow do OAuth/OpenID Connect estava bastante em evidência.

A ideia central: se não podemos ter um client secret estático acoplado no código-fonte, por que não criar um client secret **dinâmico** — um que é descartado a cada tentativa de login? Aqui usa-se uma espécie de handshake entre o client e o Authorization Server, que confirma o secret gerado, em duas etapas.

**Como funciona:**

1. O client gera um secret temporário — uma string randômica suficientemente grande para ser difícil de adivinhar. Esse segredo temporário chamamos de **code_verifier**.
2. O cliente pega essa mesma string e aplica um hash (por exemplo, SHA-256), gerando uma nova string chamada **code_challenge**.
3. O cliente manda para o Authorization Server, na tela de login, essa última string (o `code_challenge`) junto com suas próprias credenciais de login (usuário, senha, MFA).
4. O Authorization Server guarda essa string do lado dele.
5. O usuário é autenticado e recebe o seu authorization code tradicional do OAuth.
6. A partir desse código, o cliente pede o access token — só que agora, ao invés de enviar o `code_challenge`, ele envia o `code_verifier` (a string original, antes do hash).
7. **Validação**: o Authorization Server pega o `code_verifier`, aplica o mesmo hash SHA-256, e compara com o `code_challenge` que já tinha armazenado. Se bater: sucesso, token liberado. Se não bater: `401`.

**Considerações:**

- O Authorization Server precisa estar preparado para armazenar esse `code_challenge` enviado na primeira solicitação — o que significa que ele já precisa ter estrutura para isso. Mas isso não é um problema: grandes players como Keycloak e Auth0, ou frameworks como Spring Security (Java) ou NestJS (TypeScript), já têm essa implementação nativa prontinha.
- É padronizado, tem sua própria RFC — garantia de ampla utilização e implementação.
- O nome completo é **Proof Key for Code Exchange by OAuth Public Clients** — foi criado inicialmente focado em clientes públicos, mas a história mudou desde então.
- No **OAuth 2.1**, o PKCE é padrão absoluto e praticamente obrigatório quando se opta pela sua utilização. A recomendação é usá-lo não só em frontends ou clientes públicos, mas também em backends robustos (ex.: uma API em Java). Apesar de já ser padrão no OAuth 2.1, também é perfeitamente possível utilizá-lo no OAuth 2.0 como extensão.
- O ponto-chave: os códigos (o par `code_verifier`/`code_challenge`, não individualmente) precisam ser completamente descartáveis — mesmo que sejam entregues a um atacante, devem ser altamente voláteis, com duração mínima. Mesmo que alguém intercepte o authorization code, não vai conseguir trocá-lo pelo token, devido à dinamicidade desse padrão.

## Conclusão

O PKCE transforma um canal de comunicação inerentemente inseguro — como um navegador ou um aplicativo de celular — em um meio de transporte robusto, garantindo que o token de acesso só caia nas mãos de quem realmente provou ser o dono daquela sessão. Implementar esse tipo de solução de segurança é entender os vetores de ataque e blindar a arquitetura antes que o problema aconteça.

Se você usa o Implicit Flow até hoje, ou confia em client secrets no frontend, a missão agora é revisar esse código e ver a possibilidade de migrar para o PKCE. As ferramentas que você provavelmente já usa, seja qual for a sua linguagem de programação, já estão prontas para ajudar com isso.
