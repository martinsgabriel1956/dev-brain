# Autenticação Moderna: Senhas, Sessões, JWT, OAuth, MFA e Passkeys

> Transcrição de vídeo (português). Limpa de erros de ASR e formatada em Markdown a partir do texto bruto fornecido pelo usuário. Conteúdo já em português, sem necessidade de tradução.

Você clica em entrar e em 200 milissegundos logou. Mas como o servidor sabe que você é quem diz que é? Hoje eu vou te mostrar como funciona cada etapa da autenticação moderna e os erros de segurança que podem te causar muitos problemas em produção.

## Autenticação vs. Autorização

Antes de tudo, vou explicar um conceito que muita gente confunde. A **autenticação** prova quem você é. A **autorização** define o que você pode fazer.

Pensa numa portaria de um prédio comercial: você mostra o seu documento, quando a portaria confirma que você é você, ela faz a autenticação. Depois, quando te dá um crachá dizendo qual andar você pode acessar, é autorização. São coisas diferentes, mas que trabalham juntas: primeiro você prova a identidade, depois o sistema decide o que vai liberar.

## Senhas: hashing, work factor e salt

Tudo começa com a forma mais antiga de autenticação, que é a senha. Quando você cria uma conta, o servidor nunca guarda a senha em texto — ou pelo menos não deveria. Se o banco de dados vazar, o atacante teria todas as senhas de forma muito fácil.

Para prevenir isso, o servidor passa a senha digitada por uma função de **hash**. O hash transforma qualquer texto numa string fixa e o processo é irreversível — você consegue ir do texto pro hash, mas nunca do hash pro texto. Mas isso não funciona com qualquer hash: o SHA-256 é muito rápido, 1 bilhão de hashes por segundo numa GPU moderna. Isso significa que um atacante consegue testar bilhões de senhas em segundos.

O **bcrypt** e o **Argon2** são lentos de propósito. Eles usam um **work factor**, que é o número de rodadas de processamento que cada hash exige. Com o valor certo, cada hash demora centenas de milissegundos. Isso pode parecer pouco, mas transforma um ataque de segundos em anos.

Tem também o **salt**, que é um valor aleatório colocado antes do hash. Duas pessoas com a mesma senha geram hashes completamente diferentes. Sem isso, um atacante pode usar **rainbow tables**, que são tabelas pré-computadas com milhões de hashes de senhas comuns. Usando salt, cada hash é único e as tabelas ficam inúteis.

Na hora do login, o servidor pega a senha digitada, aplica o hash usando o salt salvo junto, e compara com o hash armazenado. Se bater, a senha está certa.

### Erros comuns no login

- **Mensagens de erro diferentes para e-mail e senha.** Se o servidor diz "usuário não encontrado", o atacante sabe que o e-mail não está cadastrado. Se diz "senha incorreta", sabe que o e-mail existe e só precisa adivinhar a senha. A mensagem correta tem que ser sempre genérica — "e-mail ou senha incorretos" — sem dar nenhuma informação ao atacante.
- **Falta de rate limiting.** Sem limite de tentativas, um atacante pode rodar um script que testa 100.000 senhas por minuto, ou testar uma lista de e-mails/senhas vazados de outro site (credential stuffing). A proteção ideal é limitar tentativas por IP e por conta, com bloqueio temporário após X falhas consecutivas.
- **SQL Injection no login**, a vulnerabilidade mais clássica e famosa. Se a query concatena o input direto na string, o atacante pode digitar `' or 1=1` no campo de e-mail e a query retorna todos os usuários. A solução é sempre usar queries parametrizadas — nunca concatenar input do usuário direto na query.

## Sessões

Agora temos a senha verificada. Mas como o servidor lembra que você já fez login? A abordagem mais comum é a **sessão**. Você digita e-mail e senha, o servidor valida, cria um registro de sessão e devolve um identificador. Esse identificador vai para um cookie, que o browser guarda e envia automaticamente em toda requisição. O servidor recebe o cookie, confere na memória (ou storage) e sabe que é você.

O cookie também precisa de proteção:

- **`HttpOnly`** impede que o JavaScript acesse o cookie — protege contra XSS (cross-site scripting).
- **`Secure`** garante que só trafega via HTTPS.
- **`SameSite`** bloqueia o envio em requisições vindas de outros domínios — protege contra CSRF (cross-site request forgery).

### Session fixation

Perigo escondido: o atacante cria uma sessão, planta um session ID no browser da vítima e espera ela fazer login. Se esse session ID não muda após o login, o atacante consegue usá-lo. A solução é sempre gerar de novo o session ID depois do login, limpando o antigo e criando um novo. A maioria dos frameworks faz isso automaticamente, mas vale confirmar.

### Invalidação ao trocar senha

Outro erro comum: não invalidar sessões antigas quando o usuário troca a senha. Se o atacante já roubou a sessão, trocar a senha não resolve nada, porque a sessão antiga continua ativa. Sempre que o usuário trocar a senha, é preciso invalidar todas as sessões existentes e forçar um novo login.

### Onde a sessão fica armazenada

Em memória é rápido, mas se o servidor reiniciar, todo mundo perde a sessão. No banco de dados há persistência, mas cada requisição vira uma consulta extra. A solução mais comum em produção é algo como **Redis**: rápido, compartilhado entre servidores, feito para exatamente esse tipo de coisa.

Sem Redis, cai no problema clássico: com três servidores atrás de um load balancer, a sessão só existe em um deles. A próxima requisição pode ir para outro servidor, que não vai te reconhecer — porque sessões são *stateful*, guardam estado, e estado é difícil de escalar.

## JWT

Existe uma forma de autenticar sem guardar estado: o **JWT** (JSON Web Token). Tem três partes separadas por ponto:

- **Header**: qual algoritmo de assinatura foi usado.
- **Payload**: dados como ID do usuário, data de expiração e escopos de acesso. Codificado em Base64 — **não criptografado**. Qualquer pessoa com o token consegue ler o conteúdo, por isso nunca colocar dados sensíveis ali.
- **Signature**: garante que ninguém forjou o conteúdo.

Dois tipos de algoritmo de assinatura:

- **HMAC** usa chave simétrica — a mesma chave assina e verifica. Funciona bem quando um único servidor faz tudo.
- **RSA/ECDSA** usam chaves assimétricas — a chave privada assina, a chave pública verifica. Importante para microsserviços: os outros serviços só precisam da chave pública para validar o token, e a chave privada nunca sai do servidor de autenticação.

### Erros comuns com JWT

- **Chave secreta fraca** (ex.: `secret`, `password123`). Um atacante testa um dicionário de chaves comuns e, se acertar, forja qualquer token. A chave precisa ter pelo menos 256 bits de entropia, gerada aleatoriamente, nunca exposta no código — sempre em variável de ambiente.
- **Verificar só a assinatura, ignorando `issuer` e `audience`.** Sem isso, um token emitido para o serviço A pode ser reutilizado no serviço B. Cada API deve validar que o token foi emitido pela fonte esperada e é direcionado para ela.

### Fluxo

Login → servidor gera o token → devolve para o cliente → a cada requisição, o cliente manda no header `Authorization: Bearer <token>`. A diferença mais importante em relação à sessão: o servidor não precisa guardar nada, só verifica a assinatura com a chave.

### Onde guardar o token no cliente

**LocalStorage** é simples — JavaScript lê e manda no header — mas qualquer script malicioso na página (XSS) também consegue ler, e o token vaza. A opção mais segura para aplicações web é o **cookie `HttpOnly`**: JavaScript não acessa, e o browser manda automaticamente. Regra simples: em aplicação web, use cookies.

### Revogação e rotação

Um token stateless, se roubado, funciona até expirar. Por isso existe um tempo limite curto: o **Access Token** dura ~15 minutos. Quando expira, o cliente usa o **Refresh Token**, com validade de dias/semanas, para pedir um novo par. Boa prática: **rotação** — cada vez que o refresh token é usado, ele é invalidado e um novo é gerado. Mesmo que alguém roube o antigo, ele já não funciona.

### Sessão ou JWT?

- Aplicação web tradicional, servidor único, poucos serviços → **sessão**: simples, fácil de revogar, servidor tem controle total.
- API consumida por vários clientes/microsserviços que precisam validar identidade → **JWT**: cada serviço valida sozinho com a chave pública, escala melhor.
- É possível combinar os dois: sessão para o usuário final, JWT para comunicação entre serviços internos.

## OAuth

E quando o login é com outra conta, tipo "Entrar com Google"? Aí entra o **OAuth**, um protocolo de autorização delegada: você autoriza um aplicativo a acessar seus dados em outro serviço sem dar sua senha para ele. O site nunca vê sua senha do Google — só recebe permissão para acessar nome e e-mail, por exemplo.

Quatro papéis:

- **Resource Owner**: você.
- **Client**: o aplicativo que quer acesso.
- **Authorization Server**: quem autentica e autoriza (ex.: Google).
- **Resource Server**: a API que tem os dados.

### Authorization Code Flow

1. O app redireciona você pro Google, passando `client_id`, a URL de retorno, os escopos necessários e um parâmetro `state` aleatório (proteção contra CSRF).
2. Você faz login no Google, vê a tela de permissões e aceita.
3. O Google redireciona de volta pro app com um **código de autorização** na URL. Esse código só pode ser usado uma única vez e tem vida curta.
4. O app manda esse código pro Google direto do back-end, junto com o `client_secret`, e recebe os tokens de volta. Tudo servidor-para-servidor — o token nunca passa pelo browser.

### PKCE

Exceção: apps de celular não têm como guardar o `client_secret` de forma segura (qualquer um pode inspecionar o código). Para isso existe o **PKCE** (Proof Key for Code Exchange):

1. O app gera uma string aleatória, o `code_verifier`.
2. Calcula o hash dela — o `code_challenge` — e manda esse hash na primeira requisição pro Google.
3. Na hora de trocar o código por tokens, o app manda o `code_verifier`.
4. O Google aplica o hash e compara com o `code_challenge` recebido antes. Se bater, prova que quem está trocando o código é quem iniciou o fluxo. Mesmo que alguém intercepte o código de autorização, sem o `code_verifier` não consegue trocar por tokens.

### Open redirect

Erro que já causou vazamentos reais: se o authorization server não valida exatamente a `redirect_uri`, o atacante pode mudar para um domínio dele e o código de autorização vai parar no servidor dele. A validação precisa ser exata — não pode usar wildcard (comparação parcial). A URL de callback tem que bater caractere por caractere.

### O parâmetro `state`

Sem ele, o fluxo fica vulnerável a CSRF: o atacante inicia um fluxo OAuth com a conta dele e manda o link de callback pra vítima. Se a pessoa não percebe, pode vincular a conta do atacante ao próprio perfil. `state` precisa ser sempre um valor aleatório vinculado à sessão do usuário e verificado no retorno.

## OpenID Connect

O OAuth diz o que o app pode acessar, mas não diz quem é o usuário. Para identidade existe o **OpenID Connect (OIDC)**, uma camada em cima do OAuth que adiciona o **ID Token** — um JWT com dados de identidade (nome, e-mail, foto de perfil). "Entrar com Google" na prática usa OIDC.

O campo **`nonce`** protege contra ataques de replay: se alguém escuta o tráfego de rede e copia o token, sem o nonce esse atacante pode reenviar o mesmo token e entrar como se fosse você. O nonce é um valor único gerado pelo servidor a cada login — se o token for reenviado, o servidor vê que aquele nonce já foi usado e rejeita.

### Escopos

Controlam o nível de acesso. Cada escopo define exatamente o que o app pode fazer — ex.: ler e-mails mas não deletar, ver contatos mas não editar. Princípio do menor privilégio: o app recebe só o menor escopo necessário. Os escopos ficam dentro do token, e a API checa se o token tem o escopo necessário antes de responder — sem o escopo certo, a requisição é negada mesmo com token válido.

## MFA (Autenticação Multifator)

Com a identidade provada e os acessos limitados, ainda existe o problema de a senha ser roubada por phishing, vazamento ou adivinhação. O **MFA** resolve isso adicionando camadas. Três tipos de fatores: algo que você sabe (senha/PIN), algo que você tem (celular, chave física), algo que você é (biometria). O MFA exige pelo menos dois fatores diferentes.

### TOTP

Método mais comum: **TOTP** (Time-based One-Time Password). Ao ativar 2FA, o servidor gera uma chave secreta e compartilha com o app (Google Authenticator, 1Password). Para gerar o código, o app pega a chave, combina com o horário atual dividido por 30, e aplica um HMAC — gera um código de 6 dígitos que muda a cada 30 segundos. O servidor faz a mesma conta e, se bater, valida — sem precisar de internet.

- **SMS** é a opção mais fraca — o número pode ser clonado por SIM swap.
- **TOTP** é bom, mas vulnerável a phishing — o código pode ser digitado num site falso.
- **Chaves físicas** (ex.: YubiKey) são ideais — não são vulneráveis a phishing.

### Step-up authentication

Erro comum: colocar MFA só no login e achar que é suficiente. Se o atacante já tem uma sessão ativa, pode trocar o e-mail, resetar a senha e tomar a conta. Por isso, operações sensíveis (trocar e-mail, mudar senha, desativar MFA, transferir dinheiro) precisam de **step-up authentication** — o sistema pede o segundo fator de novo antes de liberar a ação sensível.

## Passkeys

A evolução mais relevante da autenticação nos últimos anos: elimina senhas usando criptografia de chave pública. Ao criar uma passkey, o dispositivo gera um par de chaves — a privada fica no dispositivo, protegida por biometria/PIN, e nunca sai dele; a pública vai para o servidor.

No login, o servidor manda um *challenge* aleatório, o dispositivo pede a biometria, assina o challenge com a chave privada e devolve a assinatura. O servidor verifica com a chave pública — sem senha, sem código, nada que possa ser roubado por phishing.

A passkey **não é vulnerável a phishing** porque a chave é vinculada ao domínio do site: se o atacante cria um site falso, a chave não funciona (o dispositivo sabe que "Google" com dois zeros não é o Google real). Nenhum outro método tem essa proteção.

Passkeys podem ser sincronizadas entre dispositivos (iCloud Keychain, Google Password Manager) — resolve o problema de perder o celular, mas adiciona uma camada de confiança na nuvem. Para cenários de alta segurança existem passkeys não sincronizadas, vinculadas a hardware físico (ex.: YubiKey), que nunca saem do dispositivo.

## Ataques comuns contra autenticação

- **XSS**: o atacante injeta JavaScript malicioso na página. Se o token está no localStorage, o script lê e envia para um servidor externo. Defesa em camadas: cookie `HttpOnly` (impede acesso via JS), Content Security Policy (bloqueia scripts não autorizados), sanitização de input (previne a injeção).
- **CSRF**: o atacante cria um site que dispara uma requisição pro seu banco; como os cookies são enviados automaticamente, o banco acha que é você. `SameSite=Strict` no cookie resolve a maioria dos casos; para formulários, um token CSRF único por sessão garante que a requisição veio do seu site.
- **CORS mal configurado**: se a API responde com `Access-Control-Allow-Origin: *` junto de `Allow-Credentials: true`, qualquer site na internet pode fazer requisições autenticadas para sua API. A correção é definir exatamente quais origens são permitidas.
- **Token de reset de senha previsível**: se o token é previsível (ex.: base64 do ID do usuário), o atacante gera tokens para qualquer conta. O token precisa ser aleatório, expirar em poucos minutos e ser de uso único. Depois de resetar, ainda é preciso invalidar todas as sessões atuais.

## Fluxo completo, resumido

1. Usuário digita e-mail e senha.
2. Servidor compara o hash (bcrypt), confere o salt, pede o segundo fator.
3. TOTP é validado, ou a passkey assina o challenge.
4. Servidor gera um access token JWT de 15 minutos, assina com a chave privada, e um refresh token com rotação.
5. A cada requisição, a API verifica a assinatura, checa os escopos, responde.
6. Quando o access token expira, o refresh token renova nos bastidores.
7. Se for login social, o OAuth cuida do redirecionamento com PKCE, e o OpenID Connect traz a identidade no ID token.
