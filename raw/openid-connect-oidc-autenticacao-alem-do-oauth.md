# OpenID Connect (OIDC): Autenticação Além do OAuth

> Transcrição de vídeo em português, reorganizada em seções e limpa de repetições de fala, calls-to-action de engajamento (like/inscrição) e comentários de transição entre blocos. Autor não se identifica nominalmente na transcrição, mas o estilo, a numeração de série ("nossa jornada no mundo das APIs, autenticação e autorização"), a menção a vídeos anteriores sobre SAML/SSO e OAuth, e o vídeo futuro anunciado sobre PKCE apontam para o mesmo autor de [[wiki/sources/pkce-proof-key-code-exchange-spa-mobile]] — Bernardo Lobato.

## Introdução

Como a autenticação de uma single page application (SPA) pode ser segura se todo o código dela fica exposto no browser? É comum implementar SSO com OpenID Connect fazendo o login passar pela própria API como proxy — e é comum achar que o SAML é o padrão da indústria sem saber que o protocolo original OpenID foi descontinuado em 2014. Este vídeo detalha o protocolo OpenID Connect: por que ele virou padrão de fato em arquiteturas modernas de API e single page application, e qual problema ele resolve.

## Parte 1 — O Protocolo OpenID Original (não confundir com OpenID Connect)

OpenID e OpenID Connect são protocolos diferentes, apesar do nome compartilhado.

### Origem (~2005)

O OpenID original surgiu por volta de 2005 como um dos primeiros padrões abertos de identidade federada na web. A proposta: permitir que uma pessoa usasse uma única identidade para se autenticar em vários sites, sem criar usuário e senha em cada um.

A identidade do usuário não era um e-mail ou username tradicional — era uma **URL controlada por ele**, algo como `https://usuario.myopenid.com`. Essa URL podia até funcionar como uma landing page de perfil se acessada diretamente. O domínio MyOpenID não existe mais hoje.

### Como funcionava o fluxo

Fluxo inteiramente por redirecionamentos do navegador:

1. O usuário informava sua URL OpenID em um campo de texto no site de destino (o Relying Party / Service Provider).
2. O site fazia um `GET` nessa URL. Na resposta HTML havia tags `<link>` ocultas apontando para o provedor OpenID real (`openid.server`) e para o `openid.delegate`/local ID do usuário. O site descobria dinamicamente, a partir da própria URL, quem era o provedor de identidade responsável — não havia conhecimento prévio.
3. O navegador era redirecionado para esse provedor, e o login acontecia diretamente na tela do provedor — o Service Provider nunca tinha acesso a login/senha.
4. Após autenticar, o provedor redirecionava o navegador de volta ao site original com uma mensagem assinada (em geral baseada em XML) confirmando a autenticação.
5. O site verificava a assinatura criptográfica e, se válida, criava a sessão local.

Modelo centralizado no navegador, com descoberta dinâmica de provedores e múltiplos redirecionamentos — flexível e descentralizado, mas complexo de implementar e pouco amigável para desenvolvedores, num momento em que o mundo já começava a migrar para APIs, mobile e JSON.

### OpenID vs. SAML

OpenID e SAML nasceram quase na mesma época tentando resolver o mesmo problema — permitir que um site confiasse na autenticação feita por outro — mas partiram de premissas diferentes sobre quem controla a identidade e quem decide adotar o padrão.

- **SAML**: desenhado para o mundo corporativo. Pressupunha acordos formais entre empresas, infraestrutura controlada, baseado em XML verboso — mas isso não era um grande problema porque quem implementava eram times internos das próprias organizações. Encaixava no modelo de federação corporativa com confiança formal pré-estabelecida entre domínios conhecidos.
- **OpenID**: apostou numa visão aberta e descentralizada — qualquer pessoa com uma URL, qualquer site aceitando qualquer provedor. Elegante na teoria, mas sem governança nem confiança pré-estabelecida entre provedores e sites, aceitar logins de provedores OpenID aleatórios era um risco. Faltava o elemento que o SAML já tinha resolvido: relações de confiança explícitas.

Na prática, o SAML prosperou por resolver um problema real de federação entre organizações que já confiavam umas nas outras. O OpenID tentou um ecossistema de confiança aberto demais, sem incentivo claro para os sites aceitarem a descentralização.

### Descontinuação

O protocolo OpenID original — baseado em URL como identidade e descoberta via HTML — foi descontinuado por volta de 2014 e hoje só aparece em sistemas legados. Quem usou WordPress, Blogger, AOL ou Yahoo nesse período provavelmente tem uma URL OpenID esquecida por aí. Hoje é difícil até implementar o protocolo original para fins didáticos — praticamente só via bibliotecas antigas já descontinuadas; não foi encontrado nenhum serviço atual que ofereça o protocolo original, nem para fins de estudo.

## Parte 2 — Da OpenID Foundation ao OpenID Connect

### A OpenID Foundation (2007)

Diante do crescimento caótico e das implementações incompatíveis do OpenID original, empresas como Google, Yahoo, Facebook e AOL criaram em 2007 a OpenID Foundation, para direcionar o padrão e fornecer uma especificação oficial.

### A ascensão do OAuth e a "autenticação de gambiarra"

Com a explosão das APIs, o mercado viu a ascensão do OAuth 1.0 e depois do OAuth 2. Mas o OAuth foi criado puramente para autorização, não autenticação. Muitas empresas, diante da complexidade do OpenID original, passaram a improvisar autenticação **sobre** o OAuth — protocolos proprietários e ad-hoc, cada provedor de identidade com sua própria forma de entregar os dados do usuário. Resultado: cada grande provedor tinha sua própria integração, forçando desenvolvedores a escrever adaptações diferentes para cada um.

### O nascimento do OpenID Connect (2014)

A OpenID Foundation percebeu que o futuro não estava mais nas URLs como identidade, e sim em tokens JWT, APIs e sistemas mobile. A partir daí liderou a criação do OpenID Connect, reaproveitando o nome mas abandonando a especificação antiga. Lançado oficialmente em 2014, versão 1.0.

A ideia central: em vez de reinventar a roda, usar o OAuth 2 como transporte e adicionar uma camada rígida de identidade em cima, usando o formato JWT (JSON Web Token) já amplamente usado pelo próprio OAuth. Isso uniu a segurança e os fluxos de permissão do OAuth com a padronização de dados de perfil que faltava.

Hoje o OpenID Connect é padrão absoluto da indústria, adotado em massa por Google, Microsoft e Apple — é a base de praticamente todo botão de login social e de aplicações single page modernas.

## Parte 3 — O Que É o OpenID Connect (OIDC)

OpenID Connect (OIDC) é uma **camada de identidade construída sobre o OAuth 2**. Enquanto o OAuth é desenhado apenas para autorização, o OIDC estende essa funcionalidade para permitir autenticação — verificar a identidade do usuário. Transforma o OAuth num sistema completo de identidade, permitindo que aplicações recebam informações básicas do usuário de forma padronizada.

### O ID Token

O grande diferencial do OIDC é o **ID Token** — um JWT contendo informações do usuário, chamadas de **claims** (nome, e-mail, foto de perfil etc.). Diferente do access token do OAuth, que é destinado à autorização na API/Service Provider, o ID Token é destinado à aplicação cliente.

### Fluxo do OIDC

1. O usuário acessa uma rota protegida. O navegador chama a aplicação (Service Provider).
2. A aplicação responde com um redirect para `/authorize` no provedor de identidade.
3. O navegador vai até o provedor de identidade, e o usuário realiza o login (usuário/e-mail, senha, MFA se necessário).
4. O provedor de identidade redireciona de volta para a aplicação, passando um `code`.
5. O navegador chama o endpoint de callback da aplicação.
6. O back-end troca o `code` por tokens no endpoint `/token` do provedor de identidade — essa troca acontece inteiramente no back-end, o usuário não vê.
7. O provedor de identidade valida o `code` e devolve o token para a aplicação.
8. A aplicação valida o token e cria a sessão autenticada conforme a estratégia escolhida.

Esse fluxo se integra diretamente ao fluxo principal do OAuth 2 e é conceitualmente parecido com o do SAML.

### Autenticação sempre via client/navegador

Para de fato usar OpenID Connect (e SAML), a autenticação **sempre** precisa acontecer via client/navegador no provedor de identidade — nunca diretamente pela API. É a única forma de garantir que login, senha e MFA não sejam interceptados pela aplicação cliente (a API). Esse é um conceito fundamental do OIDC: a senha do usuário nunca deve passar pela aplicação. É por isso que "Entrar com Google/Facebook/GitHub" abre uma instância do browser mostrando a URL do provedor de identidade — mesmo em SPA ou app mobile.

### OIDC vs. SAML: JSON vs. XML

O SAML trafega XML pesado tanto no request quanto no response, aumentando a complexidade de implementação — especialmente em single page applications e sistemas mobile. O OIDC trafega apenas JSON, muito mais leve e compatível com o mercado atual.

### Antipadrão: API como proxy de autenticação (ROPC)

É comum ver — inclusive hoje — implementações em que a própria API funciona como proxy entre o usuário e o provedor de identidade: o usuário autentica via API, e a API por baixo dos panos autentica no provedor de identidade e devolve os tokens. Isso funciona, mas do ponto de vista de arquitetura e segurança assume um risco desnecessário: a API passa a manipular a senha do usuário. Nesse caso, **não se está usando SAML nem OpenID Connect de fato** — ambos exigem autenticação via client exatamente para não existir esse vínculo entre dados sensíveis do usuário e a API.

Esse antipadrão tem nome: **Resource Owner Password Credentials (ROPC)**. É completamente desencorajado nas APIs atuais.

## Parte 4 — Interceptação do Code e PKCE

Se alguém interceptar o `code` gerado pelo provedor de identidade no início do fluxo, pode se passar pelo usuário legítimo junto à própria API, receber os tokens e usar como se tivesse sido autenticado de fato. Isso pode acontecer — é preciso que tanto o provedor de identidade quanto o Service Provider validem quem está enviando os tokens; não basta o simples conhecimento do token.

O problema fica mais evidente em single page applications e browsers comuns: não é possível embutir um `client_id`/`client_secret` estático no código do front-end para autenticar o client, porque tudo no cliente está exposto e pode ser inspecionado.

O OpenID Connect resolve isso com **PKCE** (Proof Key for Code Exchange). O mecanismo detalhado de PKCE fica fora do escopo deste vídeo e é tratado em vídeo dedicado — ver [[wiki/sources/pkce-proof-key-code-exchange-spa-mobile]].

## Fechamento

O OpenID Connect é o resultado de quase duas décadas de evolução: do desejo de descentralizar tudo com URLs do OpenID original, passando pelas gambiarras corporativas sobre o OAuth (que ainda existem hoje), até o padrão robusto baseado em JSON e focado em APIs usado atualmente. O OpenID Connect não veio substituir o OAuth — veio completar a peça que faltava: gestão de identidade.

Se uma API está pedindo a senha do usuário para repassar ao provedor de identidade, está no caminho do Resource Owner Password Credentials — um caminho que a indústria está fechando. A recomendação é delegar autenticação para quem entende de autenticação, e deixar a API focada em regras de negócio. Ainda assim, o protocolo de identidade só cumpre metade do trabalho se o client não garantir que o fluxo não pode ser interceptado — daí a relevância do PKCE para quem desenvolve front-end de SPA (React, Angular, Vue ou similares) ou aplicações mobile.
