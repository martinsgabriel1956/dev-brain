# História da Autenticação: de Senha a Tokens, Criptografia Assimétrica e Identidade Federada

**Formato:** Transcrição de vídeo (YouTube)
**Idioma original:** Português (BR)
**Data de transcrição:** 2026-07-27
**Tema:** Evolução histórica e técnica da autenticação de usuários — de user ID único, passando por senha, MFA, tokens de hardware, biometria, até OAuth, OpenID Connect e JWT.

---

## Introdução

Imagina que você chega na porta de um clube exclusivo. O segurança te olha e pergunta: "Quem é você?" Parece simples, mas essa pergunta esconde uma das questões mais difíceis da computação, e a forma como a gente responde ela evoluiu muito nos últimos 70 anos.

Hoje vamos falar de autenticação: por que ela existe, como surgiu, quais protocolos e algoritmos estão por baixo, e como chegamos ao modelo de tokens, criptografia assimétrica e identidade federada.

## Anos 40-60: do computador de sala única ao time-sharing

Lá no início da computação, nos anos 40, um computador era uma máquina gigante que ocupava uma sala inteira e era dedicada principalmente a uma única tarefa por vez. Não tinha múltiplos usuários, então não tinha por que identificar ninguém.

Mas nos anos 60 uma pequena coisa mudou tudo: o *time sharing*. Vários usuários acessando o mesmo computador ao mesmo tempo. Agora o computador tinha que saber com quem ele estava falando, para isolar dados, contabilizar tempo de CPU e também controlar permissão de acesso a arquivos.

Para resolver isso, criaram um identificador de usuário digitado no terminal. Sim, você só tinha que digitar o seu usuário. Isso fazia sentido na época: eram sistemas fechados que ficavam dentro de universidades e laboratórios, ou seja, era um ambiente de confiança absoluta. Mas, ao longo do tempo, à medida que mais pessoas ganharam acesso, esse modelo de confiança absoluta não era tão confiável assim. E se alguém digitasse o nome de outra pessoa? Aí entra a senha.

## A senha e o problema do texto puro

A senha é muito, muito antiga. Ela vem da ideia de segredos compartilhados, que existem desde sempre na espionagem, no exército e em sociedades secretas. No computador, você tem um identificador público — o seu nome de usuário, que diz quem você afirma ser — e uma prova secreta — a sua senha, que confirma a sua afirmação.

Nessa época, a senha era armazenada em texto puro, em um arquivo supostamente protegido. E isso já tinha um problema enorme: o sistema conhece a sua senha. Se o arquivo vazar, todas as senhas vazam juntas.

## 1976: Unix, hash e salt

Alguns anos depois, por volta de 1976, o Unix melhorou esse sistema. Em vez de armazenar a senha, armazena só a sua impressão digital matemática — no caso, um *hash*. Só que essa função de hash é determinística, então a solução foi usar um *salt*, que era armazenado junto com o hash no arquivo de senhas. O salt não precisa ser secreto, ele só tem que ser único.

Essa combinação de usuário e senha virou um padrão universal por décadas, e ainda é o método mais usado no mundo. Só tem um problema: senha é pena de sigilo, e a gente sabe que sigilo é frágil, principalmente porque as pessoas escolhem senhas fáceis, como o nome do cachorro, e ainda ficam reutilizando elas em vários sites diferentes. O problema principal é que as senhas podem ser roubadas. E, com a chegada da internet, esses problemas explodiram muito mais: não era mais 50 usuários em uma universidade, eram milhões de pessoas em e-commerce, bancos, e-mails. Esse modelo de usuário-senha estava chegando no limite.

## Perguntas de segurança

O que acontece se um usuário esqueceu a senha? A confirmação por e-mail não era muito comum no início. Na época existiam perguntas de segurança, como o nome do seu primeiro animal de estimação, cidade onde nasceu, nome da mãe — e a resposta servia como uma segunda camada de verificação. A ideia era que só você sabia dessas coisas. Isso fazia sentido na época, mas hoje esse modelo é completamente obsoleto.

As perguntas de segurança, na prática, eram uma senha mais fraca. Mas elas abriram uma ideia muito importante: a autenticação não precisa se limitar ao que você sabe.

## Os três fatores de autenticação

A segurança chegou a um consenso muito interessante: autenticação robusta precisa de múltiplos fatores, e os fatores têm que ser de categorias diferentes. Já ouviu falar de 2FA (Two-Factor Authentication) ou MFA (Multi-Factor Authentication)? Os fatores são:

- **Algo que você sabe** — uma senha, um PIN, resposta de uma pergunta.
- **Algo que você tem** — um cartão físico, um celular, token de hardware.
- **Algo que você é** — impressão digital, reconhecimento facial.

A lógica por trás é bem simples: para comprometer dois fatores de categorias diferentes, o atacante precisaria de dois vetores de ataque simultâneos e completamente independentes, o que é muito mais difícil.

## Anos 90: tokens de hardware (RSA SecurID)

A primeira aparição comercial em grande escala do segundo fator foram os tokens de hardware, lá nos anos 90, principalmente o Secure ID da RSA Security. Cada token tinha gravado de fábrica uma *seed* secreta e um relógio interno, e o servidor da empresa tinha uma cópia dessa mesma seed. A cada 30 ou 60 segundos, o token calculava um código de seis dígitos a partir da seed e do tempo atual.

Nessa geração tinha dois pequenos problemas: primeiro, se alguém roubasse a seed, poderia clonar o token; segundo, o dispositivo e o servidor tinham que ter um relógio sincronizado, o que pode não parecer, mas é bem difícil.

## 2005: HOTP (IETF)

Em 2005, a IETF padronizou o HOTP — HMAC-based One-Time Password —, que tirou a dependência do relógio. Agora a fórmula era baseada em um contador: toda vez que você usava o token, o seu dispositivo incrementava o contador, e o servidor também.

## TOTP: o padrão dos apps autenticadores

Depois apareceu o TOTP — Time-based One-Time Password —, que é o padrão usado pelos aplicativos autenticadores que você tem no seu celular. Ele também usa o relógio, bem parecido com a primeira geração — a diferença é que agora ele é padronizado e a especificação é pública.

Quando você escaneia o QR Code em um serviço, o que está sendo transferido é a seed secreta, e, a partir daí, o seu app e o servidor geram o mesmo código de seis dígitos usando essa função. Eles nem se comunicam: só têm que concordar sobre a hora atual e a seed com que o código é calculado nos dois lados.

## 2014: U2F (Universal Second Factor)

Em 2014, o Universal Second Factor foi lançado, implementado em dispositivos físicos, tipo a YubiKey. Agora a ideia era baseada em criptografia de chave pública. No registro, o dispositivo gerava um par de chaves exclusivo para aquele serviço, e a chave pública era enviada para o servidor. No login, o servidor envia um *challenge* — um valor aleatório —, e o dispositivo assina esse challenge com a chave privada. Assim, o servidor conseguia verificar a assinatura com a chave pública armazenada e te liberava.

Olha como: a chave privada nunca sai do dispositivo, o challenge é diferente a cada autenticação, e o protocolo vincula o challenge à origem do site — então phishing é praticamente impossível, porque o dispositivo verifica o domínio.

## O terceiro fator: biometria

O terceiro fator tenta responder "você é fisicamente quem diz ser?"

**Primeira geração**: basicamente a impressão digital. O sistema capturava uma imagem do dedo e extraía pequenos detalhes chamados de minúcias — como, por exemplo, quando uma linha terminava ou quando uma linha se dividia. O *template* era basicamente uma lista dessas características, com posição e ângulo. Para comparar com a sua digital, o sistema tinha que alinhar as duas impressões, porque o dedo nunca é colocado exatamente na mesma posição, e depois contava só quantos detalhes coincidiam — se o número passasse um certo threshold, era match. Só que esse método é muito frágil: o dedo é um tecido mole, então a pressão que você faz pode mudar o padrão.

**Segunda geração**: em vez de analisar só esses pequenos detalhes, começaram a ver também a direção das linhas, densidade e textura, juntando tudo isso em um único vetor numérico. Quando você encosta o dedo de novo, ele gera um outro vetor e mede o quão perto eles são. Agora imagina o que acontece se a sua impressão digital vazar: você não consegue só trocar ela, como você troca de senha.

**Terceira geração**: o que mudou foi a arquitetura. O fluxo antes era sensor → sistema operacional → app, que fazia a comparação. Mas, se o sistema tivesse comprometido, um malware poderia interceptar tudo. A solução foi mover para um processador isolado, como o Secure Enclave da Apple ou o TEE do Android. Na web, o fluxo do terceiro fator é bem parecido com o do segundo: o site te manda um challenge, o seu navegador pede a biometria para o dispositivo, o hardware verifica localmente e, se aprovar, ele libera uma chave privada que vai assinar o challenge, e o site verifica a assinatura. Olha como: o site nunca vai ver o seu rosto ou a sua digital, ele só vê uma prova criptográfica.

## Removendo a senha: Magic Links e Passkeys

Olhando agora esses fatores, você deve estar pensando: definitivamente senha em si é uma ideia bem ruim. E muita gente está chegando nessa mesma conclusão, e com isso estão começando a remover senhas da forma que a gente conhece. Por exemplo:

- **Magic Links**: você só digita o seu e-mail, e o sistema manda um link temporário que você clica e está dentro.
- **Passkeys**: o seu dispositivo gera um par de chaves criptográficas — uma pública, que fica no servidor, e uma privada, que fica no seu dispositivo, protegida por biometria ou um PIN local. Quando você faz login, o seu dispositivo assina um challenge, e o servidor verifica.

## SSO corporativo

Nos últimos anos, a internet explodiu de serviços, e cada serviço quer o seu cadastro, o seu e-mail, sua senha. Uma única pessoa passou a ter contas em dezenas de sistemas, e gerenciar isso tudo é muito ruim.

A solução apareceu no mundo corporativo: o SSO. A ideia era você autenticar uma única vez em uma fonte confiável, chamada de Identity Provider ou IdP, e a partir daí todos os sistemas dessa organização confiam nessa autenticação. Um funcionário entra no escritório e faz login uma vez, e tem acesso ao e-mail, CRM, internet, sistema de RH — tudo sem digitar senha de novo.

## 2006: OAuth

Em 2006, o Twitter — tecnicamente foram várias empresas da web, incluindo o Twitter — criou o OAuth, para resolver um problema diferente: como deixar um aplicativo acessar dados de outro sem compartilhar a senha.

Pensa assim: você quer que um app de agendamento acesse o seu Google Agenda. Antes do OAuth, a única forma seria dar sua senha do Google para esse aplicativo, o que é péssimo, porque ele teria acesso a tudo, e você não ia conseguir revogar o acesso sem trocar a senha.

O OAuth introduziu o conceito de delegação de acesso com escopo limitado. Funciona assim:

1. Você clica em "Conectar via Google" no seu aplicativo de agendamento.
2. O app te redireciona para o Google, passando o seu ID de cliente e quais permissões quer.
3. Você faz login e aprova as permissões.
4. Você é redirecionado de volta para o aplicativo com um código de autorização.
5. O aplicativo pega esse código e troca por um Access Token diretamente com o Google.
6. O app pode usar esse token para acessar sua agenda.

A sua senha nunca foi exposta, e você pode revogar o acesso a hora que você quiser.

## 2014: OpenID Connect e identidade federada

Em 2014, em cima do OAuth, surgiu o OpenID Connect — o protocolo verdadeiro por trás do botão de "Entrar com Google", Facebook, GitHub e por aí vai. Isso tem o nome de identidade federada: a sua identidade existe em um domínio, como por exemplo Google, e outros domínios confiam 100% nela.

Mas, para entender o que o OpenID Connect resolve, você tem que entender o limite do OAuth: ele foi criado para autorização — definir o que um app pode fazer — mas não foi projetado para autenticação, para responder "quem é você".

Então agora o servidor também retorna um ID Token, que é um JWT assinado, com uma estrutura bem definida. O payload dele é padronizado, com:

- **issuer**: quem emitiu o token.
- **subject**: seu identificador único do usuário naquele provedor.
- **audience**: para qual aplicação esse token foi emitido.

O site que recebe esse token não tem que confiar na palavra de ninguém: ele mesmo pega a assinatura e busca a chave pública do emissor em um endpoint chamado JWKS (JSON Web Key Set), que retorna as chaves públicas do provedor. Com isso, ele verifica a assinatura criptograficamente e, em milissegundos, sabe exatamente quem você é.

Essa é a identidade federada: você existe em um lugar confiável, e a criptografia garante esse fato para o resto do mundo.

## Sessões: como o servidor lembra quem você é

Mas tem uma pergunta que a gente não respondeu ainda: depois que meu usuário autentica, como o sistema lembra quem ele é nas próximas requisições? O HTTP é um protocolo sem estado — cada requisição é independente, o servidor não guarda o contexto entre elas. Então como ele sabe que a próxima requisição é sua?

A solução clássica são as sessões. No login, o servidor verifica suas credenciais, cria uma entrada no banco de dados — a sessão — com ID único e os seus dados, como usuário e permissões, e envia esse ID de volta para o cliente guardar, geralmente em um cookie. A partir daí, em toda requisição, o navegador envia o cookie automaticamente, o servidor pega a sessão, consulta o banco e descobre quem você é.

Só que imagina uma arquitetura com muitos servidores: todos teriam que acessar o mesmo armazenamento de sessões, tipo um Redis. Isso funciona, mas olha como ele cria uma dependência central: se o Redis cair, tudo cai.

## JWT: tokens stateless

A alternativa foram os tokens stateless, como o JWT. Em vez de guardar a sessão no servidor, toda a informação fica no próprio token, e o token fica com o cliente. Ele é composto por header, payload e signature, todos separados por ponto.

- O **header** define o tipo de token e o algoritmo de assinatura, tipo HS256.
- No **payload** estão os dados: o user ID, as permissões, quando o token expira.
- Tanto o payload quanto o header são codificados em Base64, não criptografados — qualquer um pode ler e, em tese, tentar mudar o conteúdo. O que garante a integridade é a **signature**: se alguém alterar o payload, a assinatura fica invalidada e o servidor rejeita o token.

No login, o servidor gera e assina o JWT e envia para o cliente. Nas próximas requisições, o cliente envia o token no header, e o servidor só verifica a assinatura, sem precisar consultar banco de dados. Isso escala muito melhor: qualquer servidor com a chave de verificação pode validar um JWT.

## Access Token e Refresh Token

Mas surge um outro problema: como o JWT também é stateless, como você invalida um token antes dele expirar? Se o usuário fizer logout ou tiver a conta comprometida, o token continua válido até expirar.

A solução é trabalhar com tokens de curta duração, tipo um Access Token que expira em minutos. Mas aí o usuário teria que fazer login a cada 15 minutos, o que seria insuportável. Então também usamos o Refresh Token.

A ideia é que o Access Token tem uma curta duração — 15 minutos, 1 hora — e é usado em cada requisição. O Refresh Token tem uma duração maior — dias ou até semanas. Quando o Access Token expira, o cliente envia o Refresh Token para um endpoint específico, o servidor valida e emite um novo Access Token.

O Refresh Token também pode ser invalidado: se o usuário fizer logout ou a conta for comprometida, o servidor marca aquele Refresh Token como revogado, e na próxima tentativa de renovação o servidor recusa, e o usuário tem que autenticar de novo.

É o melhor dos dois mundos: requisições rápidas e stateless com Access Tokens curtos, e controle de revogação centralizado com Refresh Tokens.

## Conclusão: voltando ao segurança da porta

Então vamos voltar e responder o segurança que está esperando. Até os anos 60, eu era o que eu digitava, e ninguém me questionava. Mas depois veio a senha, e eu sei de um segredo. Só que segredos podem vazar, então vieram os fatores: eu sei, eu tenho e eu sou — múltiplas provas ao mesmo tempo.

Para eu não ter que ficar me identificando toda hora em todos os lugares, eu tenho essa identidade federada aqui, que você pode ver que alguém confiável já me verificou. E para você ter a garantia de que eu ainda sou eu no meio do caminho, eu ainda tenho esse Access Token, e, se precisar, um Refresh Token também.

Só que nada disso é uma garantia de que eu sou eu. A gente ainda está aprendendo a responder isso.
