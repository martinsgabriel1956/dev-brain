# Tokens de Autorização: Opacos vs. Autocontidos, e o Padrão JOSE

## Introdução

Você já se perguntou por que alguns sistemas gigantes utilizam tokens que parecem uma string aleatória ilegível, como se fosse algo criptografado, enquanto outros sistemas utilizam aquele JWT enorme e cheio de informações dentro? Por que em alguns sistemas você consegue revogar um token instantaneamente, e em outros precisa esperar ele expirar? Se você não entende bem a diferença arquitetural entre um token opaco e um token autocontido, esse conteúdo é para você.

Olá devs, eu sou Bernardo Lobato e hoje vamos aprofundar a discussão sobre tokens, dando continuidade à série de vídeos sobre APIs. Nos vídeos anteriores falamos sobre APIs stateful e stateless e como funcionam estruturalmente esses tipos de sistemas. Agora o foco é em como as requisições são trafegadas e autorizadas em cada uma dessas escolhas, fazendo uma viagem ao mundo dos tokens — entender a melhor maneira de gerar tokens de autorização para cada propósito e como tirar o melhor proveito dessas estruturas.

## O que é um token de autorização

Um token de autorização é uma credencial que representa identidade ou permissão para acessar um recurso restrito — que não pode ser acessado livremente por qualquer usuário. Esse recurso pode ser um endpoint, uma URL, uma página, uma imagem, um documento privado etc.

Na prática, no contexto de APIs, o token de autorização é uma string — uma cadeia de caracteres — enviada em cada requisição que, uma vez validada e autorizada, permite o acesso a um endpoint ou recurso previamente autorizado. Quando a requisição é feita e o token é enviado, o servidor valida esse token com algum algoritmo, verifica se ele fornece o acesso solicitado e libera (ou não) esse acesso.

Caso o token seja inválido, tenha expirado ou não seja reconhecido, o comum é retornar `401 Unauthorized`. Vale um parêntese sobre a diferença entre `401` e `403`:

- **401**: problema de autenticação — senha inválida, token expirado, ou token que o servidor não reconhece como válido.
- **403**: problema de autorização — a autenticação está correta (senha ok, token válido), mas o recurso/endpoint acessado não é permitido para aquele nível de acesso.

A natureza desses tokens pode ser de dois tipos: **opacos** ou **autocontidos**.

## Tokens opacos

Tokens opacos não carregam informação útil visível dentro da própria string. Funcionam como uma chave de referência: são consultados no backend ou no servidor de autorização, que traz os dados corretos referentes ao objeto autorizado por aquele token. É como se fosse, a grosso modo, uma chave primária de uma tabela cujas linhas são os dados do usuário autenticado — os dados de uma sessão, por exemplo.

Esse modelo traz muito mais controle sobre as informações armazenadas, inclusive de forma dinâmica, assim como sobre sua revogação — o JWT, como veremos, tem um problema grave com revogação, o que não é o caso aqui. Por outro lado, o lado ruim é que diminui a autonomia sobre o token, já que não há informações que possam ser utilizadas diretamente no cliente.

Não existe uma RFC ou padrão formal que defina como um token opaco deve ser estruturado e gerado. Isso não é necessariamente ruim, já que por definição um token opaco é apenas uma string cujo significado — os dados a que ela dá acesso — só o servidor conhece. Por isso, tokens opacos são utilizados com frequência em serviços **stateful**.

### Fluxo típico

1. O cliente autentica passando suas credenciais.
2. O authorization server (ou a própria API) gera um token opaco.
3. O token é armazenado no banco, em cache, ou em outra estrutura — junto com os dados do usuário autenticado.
4. O token opaco é retornado ao cliente.
5. Em requisições posteriores, esse token é reenviado para ser validado e autorizado pelo servidor.

### Como gerar um token opaco com segurança

Tecnicamente, qualquer string pode ser um token opaco, mas algumas opções são fortemente desaconselhadas. O ideal é que a string seja o mais difícil possível de prever.

Exemplo didático do problema: se o primeiro login gera o token `1`, o segundo gera `2`, o terceiro gera `3`... um atacante pode, por força bruta, tentar tokens `4`, `5`, `6` e ganhar acesso a recursos privados. Portanto, mesmo sem padrão formal definido, o token opaco precisa ser imprevisível o suficiente para não permitir nenhum tipo de adivinhação razoável.

Isso implica padrões indiretos de geração, como:

- Geração pseudo-randômica de bytes.
- Um **CSPRNG** (Cryptographically Secure Pseudo-Random Number Generator) — gerador de números pseudoaleatórios criptograficamente seguro, cujas propriedades garantem imprevisibilidade suficiente para criação de chaves e tokens.

Exemplos por linguagem:

- **Node.js**: `crypto.randomBytes`
- **Java**: classe `SecureRandom`
- **Python**: módulo `random`/`secrets` (CSPRNG)

É preferível que o token tenha idealmente **256 bits**, para que ataques de força bruta sejam ineficientes o suficiente para serem desencorajados.

O que evitar: `Math.random()`, qualquer string incremental, hash de timestamp, ou mesmo UUID puro. O UUID v4, forçando um pouco a barra, pode ser aceitável, mas ainda assim tem apenas 122 bits de aleatoriedade, contra os 256 bits de um token bem gerado — uma diferença exponencial em dificuldade de quebra. Não há motivo para não usar algoritmos mais seguros.

### Token não é ID

Um token é categoricamente diferente de um ID. Um ID identifica uma entidade — segurança não é o aspecto principal. Um token autoriza o acesso a um recurso. Embora os conceitos possam se misturar, são bem diferentes: se o ID é o número do CPF, o token é o crachá com o qual você passa na catraca da empresa. Por isso, algoritmos de geração de ID (como Snowflake e variações) não devem ser usados como algoritmo de geração de token.

Tokens opacos também não servem só para autorização de API — são usados em reset de senha por e-mail, validação de links temporários, chaves de idempotência etc. Saber gerá-los com segurança é importante em todos esses contextos.

### Onde tokens opacos são usados

- **Session token / ID de sessão**: armazenado no servidor, revogação simples (do lado do servidor), normalmente enviado via cookie. Para escalar, exige armazenamento distribuído ou estratégias equivalentes.
- **API Keys**: identificam aplicações (não usuários). Funcionam como uma chave secreta enviada em um header da requisição, permitindo à API identificar qual serviço está consumindo aquele recurso. Comuns em integrações sistema-a-sistema, cenários B2B e serviços públicos (mapas, pagamento, envio de e-mail, IA etc.) — também chamadas de chaves de serviço.
  - Vantagem: simplicidade — fáceis de gerar, distribuir e validar, sem fluxo de login, redirecionamento ou emissão de tokens temporários.
  - Risco: se vazada, qualquer pessoa pode usá-la até ser revogada.
  - Boas práticas: armazenar com segurança, nunca expor em frontend público, sempre usar HTTPS, e ter rotação periódica da chave. Em sistemas mais maduros, API keys são combinadas com outras camadas de segurança, como mTLS, para reduzir a superfície de ataque.

## Tokens autocontidos

Tokens autocontidos carregam informação útil dentro da própria string — o próprio token fornece dados que podem ser usados inclusive em regras de negócio. Normalmente usa-se alguma estratégia de assinatura e criptografia para garantir que esses dados não sejam alterados ou corrompidos no caminho.

O JWT é o exemplo clássico: carrega *claims* que podem ser usadas tanto no frontend quanto no backend para determinar propriedades ou características. Por exemplo: um claim com o nome do usuário pode ser exibido diretamente na tela; claims de *roles* podem definir quais itens de menu exibir ou ocultar no frontend. Isso é perfeitamente normal quando o JWT é usado fora do contexto de cookie `HttpOnly`.

### O padrão JOSE

**JOSE** (JavaScript Object Signing and Encryption) é um dos frameworks mais difundidos para geração de tokens autocontidos. Define como o JWT e outros formatos de token são criados e gerenciados. Seu objetivo é transferir *claims* de forma segura entre componentes diferentes da arquitetura — um claim é um par chave-valor que fornece aos sistemas informações suficientes sobre o usuário em questão, e que os backends usam como artifício para tomada de decisão em suas regras de negócio.

Um token gerado via JOSE pode assumir dois formatos:

- **JWS (JSON Web Signature)**: o formato mais comum no dia a dia — payload visível, codificado em Base64. É o JWT tradicional.
  - Ressalva importante: **Base64 não é criptografia**. É apenas uma forma de codificar dados (binários ou não) em caracteres, de modo que possam ser transferidos com segurança entre canais que só aceitam texto.
- **JWE (JSON Web Encryption)**: mais complexo — o payload também é criptografado, exigindo a chave de criptografia para leitura dos dados.

### CWT (CBOR Web Token)

Um formato adicional relevante é o **CWT**, uma versão binária do JWT, baseada no padrão **COSE**. Por ser binária, é extremamente leve, tem RFC própria definida, e é muito utilizada em dispositivos IoT e sistemas onde cada byte trafegado custa caro — comunicação via satélite, sensores e outros equipamentos com restrição de banda.

## Conclusão

A escolha entre um token opaco e um token autocontido não é uma questão de gosto — envolve arquitetura. Se o requisito é controle total e revogação imediata, o modelo opaco é o aliado natural. Se o requisito é escala, e o backend precisa "respirar" sem consultar o banco a todo momento, o JWT (via JOSE) ou formatos equivalentes como PASETO são a escolha adequada.

Ficaram de fora deste tópico, para aprofundamento futuro: fluxos de autenticação com access token e refresh token, e estratégias híbridas que combinam o melhor de APIs stateful e stateless.
