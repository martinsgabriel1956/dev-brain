# A História do OAuth: Do Antipadrão da Senha ao Protocolo de Autorização

Você se imagina fornecendo sua senha do Google ou do GitHub para algum dispositivo terceiro hoje em dia, ou então tendo que criar um usuário em cada sisteminha que você usa em casa ou na empresa, sem poder compartilhar logins e sessões entre eles? Então esse vídeo é para você.

No vídeo de hoje vamos entender um pouco mais sobre o protocolo (ou framework) OAuth: como ele surgiu, todo seu contexto histórico, e por que ele é tão importante no desenvolvimento web atualmente.

Olá, dev. Eu sou Bernardo Lobato, e o vídeo de hoje é mais um passo do nosso tema de APIs, autenticação e autorização.

## Contexto histórico

O ano aqui é 2006. Para você dar permissão a algum serviço terceiro para acessar algum dado seu — como, por exemplo, suas fotos no Flickr — você devia fornecer sua senha para esse serviço, e ele se conectava como se fosse você.

Nesse momento histórico estava surgindo o que hoje conhecemos como **API Economy** (economia das APIs): um período em que as empresas começaram a gerar valor e receita ao expor seus recursos ou capacidades como APIs, consumidas por outros sistemas ou parceiros. Sistemas como Salesforce, Google Maps, Amazon e o próprio Flickr foram pioneiros em disponibilizar seus recursos através de APIs.

Dessa maneira, ter que fornecer dados de login e senha para serviços terceiros passava cada vez mais a ser considerado uma ideia ruim, e novos padrões precisavam ser estabelecidos dentro dessa indústria.

## O antipadrão da senha

Hoje em dia conhecemos esse mecanismo de distribuir senha como um antipadrão chamado **o antipadrão da senha** (password antipattern). Ele acontece quando sistemas ou usuários se autenticam entre si usando usuário e senha — um mecanismo criado quase exclusivamente para ser usado por pessoas —, o que impede a identificação real de um serviço ou aplicação, dificulta a auditoria, inviabiliza a rotação de credenciais, etc.

Além disso, uma vez que você fornece seu usuário e senha para um serviço específico, você fica à mercê do que aquele serviço pode fazer: ele se passa por você, então tudo que você pode fazer, ele também pode.

Se você quisesse ter certeza de que aquele (ou outro) serviço não tivesse mais acesso às suas informações, a maneira mais segura era trocar a senha no serviço original — mas isso também trazia diversos problemas. Imagina que você já compartilhou sua senha com diversos sistemas terceiros. Uma vez trocada a senha, você teria que refazer todas essas conexões nos outros serviços que você não queria perder acesso. Além disso, enquanto o acesso durava, o serviço poderia fazer exatamente tudo que você podia fazer: excluir suas fotos, ler seus e-mails, acessar informações confidenciais, etc.

Num período em que as APIs se tornavam cada vez mais relevantes, esse tipo de compartilhamento de informação tornava tudo muito frágil — e isso já estava incomodando muita gente.

## A origem: Twitter, Magnolia e o grupo de discussão OAuth

A partir desse contexto, um rapaz chamado **Blaine Cook**, que na época atuava no Twitter, já sentia a necessidade de melhorar esse tipo de compartilhamento e estava trabalhando numa implementação do protocolo OpenID para o próprio Twitter.

Enquanto isso, um outro rapaz chamado **Larry Halff**, de um outro serviço chamado **Magnolia** (um tipo de API de favoritos da época), estava procurando uma solução para conectar alguns widgets de macOS às suas próprias APIs, e disponibilizá-las através de um protocolo que fornecesse delegação de acesso.

O destino juntou os dois: em **abril de 2007** iniciou-se o grupo de discussão OAuth, depois que perceberam que não existia nenhum padrão aberto de delegação de acesso em APIs. Pouco tempo depois, outras empresas como o Google já tinham se juntado a essas discussões.

Em **julho de 2007** saiu o primeiro rascunho do que viria a ser a especificação OAuth. E em **abril de 2010** foi publicada a **RFC 5849**, com o protocolo **OAuth 1.0**.

## OAuth 1.0 vs. OAuth 2.0

O OAuth 1.0 hoje em dia é pouco falado, porque era complexo demais de implementar: assinaturas criptográficas em todas as requisições, canonicalização de parâmetros, difícil para desenvolvedores e difícil para provedores manterem a interoperabilidade. Por isso ele não é o foco deste vídeo.

Já o **OAuth 2.0**, publicado oficialmente em **2012** pela **RFC 6749**, trocou essa complexidade por simplicidade operacional: usa HTTPS como base de segurança, introduz o token Bearer, define fluxos mais claros, e é muito mais fácil de adotar em APIs modernas, Single Page Applications e mobile. É essa versão que é amplamente utilizada até hoje na indústria, e é sobre ela que o vídeo vai focar a partir daqui.

## O que é o OAuth

OAuth é um protocolo (ou framework) de **autorização delegada**, ou autorização por procuração, baseado em tokens. Basicamente: o usuário — que é o dono do recurso a ser autorizado — autoriza a utilização daquele recurso; a aplicação (o *client*), que quer usar esses recursos, recebe um token; e a API de destino confia nesse token.

**Autorização delegada / por procuração** significa que, com esse tipo de protocolo, em nenhum momento você precisa compartilhar suas senhas com quaisquer aplicações interoperáveis. Em vez disso, você delega um conjunto específico de permissões para que aquela aplicação acesse uma determinada API em seu nome. Assim como no mundo real você não entrega sua identidade para uma pessoa se passar por você — você assina uma procuração dizendo exatamente o que aquela pessoa pode fazer em seu nome. Ela age em seu nome, mas dentro do limite que você mesmo estabeleceu naquele documento.

**Importante: o OAuth não é um protocolo de autenticação — é um protocolo de autorização.** Ele não define nenhuma maneira de autenticar usuários. A confusão existe porque as ferramentas que implementam o OAuth normalmente também implementam um protocolo de autenticação junto com ele, como o **OpenID Connect** (tema de um próximo vídeo). Resumindo: OAuth é autorização; OpenID Connect é autenticação.

## Os quatro pilares do OAuth

1. **Resource Owner** — o usuário que detém os dados que vão ser compartilhados.
2. **Client** — a aplicação que quer aqueles dados (uma API, um back end, um front end).
3. **Authorization Server** — o motor que valida quem você é e emite os tokens correspondentes.
4. **Resource Server** — a API que guarda as informações reais protegidas pela autorização, no banco de dados ou serviço.

## O fluxo, passo a passo (exemplo: login com Google)

Exemplo: você criou uma API de calendário/agendamento e quer que o usuário importe os contatos do Google.

1. **Redirecionamento.** Quando o usuário clica em "login com Google", a sua aplicação não pede senha — ela diz ao navegador: "leve esse usuário até o Google e diga que o client 123 (minha API) quer ler os contatos dele", passando o *scope* desejado.
2. **Consentimento.** O usuário vê a tela "app deseja acessar seus contatos — permitir?". É aqui que o Google autentica o usuário. Sua aplicação ainda não sabe de nada.
3. **Authorization code.** Se o usuário aceita, o Google devolve o usuário ao seu site com uma senha temporária na URL, o *authorization code*. Esse código sozinho não serve para acessar a API: vale por poucos segundos e só pode ser usado uma única vez.
4. **Troca do código pelo token.** O front end manda esse authorization code para o back end, que junto com o *client secret* (uma senha que não aparece no front end) confirma ao Google: "o código é real, quem está pedindo é realmente o app X". Só então o Google entrega o *access token*.

A partir daí, seu aplicativo não precisa mais da senha do usuário — ele usa o token como a "procuração" mencionada antes para buscar os contatos na API.

## OAuth também dentro de casa (arquitetura interna / microsserviços)

Muita gente acha que o OAuth é só para integrar com Google, Facebook ou GitHub. Mas se você está construindo uma arquitetura de microsserviços (ou qualquer arquitetura um pouco mais moderna), o OAuth é seu melhor amigo mesmo dentro de casa.

Imagina um ecossistema com um app mobile (Android/iOS), um portal web, uma API de pedidos, uma API de pagamentos, etc. Você não quer que cada uma dessas APIs saiba validar a senha do usuário ou consultar um banco de usuários toda hora — isso é ineficiente e inseguro.

A solução: centralizar a identidade em um Authorization Server (pode ser um Keycloak, um Spring Authorization Server, um serviço na nuvem, ou até um módulo dentro do próprio backend, sem microsserviços). O usuário faz login uma vez no servidor de identidade e recebe um access token. O app mobile envia esse token para a API de pedidos; se a API de pedidos precisa chamar a API de pagamentos em nome do usuário, ela repassa esse token ou gera um novo via *client credentials*.

O ganho: as APIs de negócio (pedidos, pagamentos) ficam "burras" em relação a quem é o usuário — só precisam saber que o token é válido e que tem o escopo necessário para acessar aquele endpoint, e executam.

## Formato do token: opaco vs. JWT

No OAuth 2, o access token é **opaco** para o cliente — o padrão não obriga nenhum formato específico, mas na prática muitos provedores usam tokens no padrão JOSE (JWT), embora isso não seja obrigatório.

É fundamental que a API (resource server) saiba validar esse token, normalmente de duas maneiras:

- **Introspecção** — modelo mais *stateful*: a API precisa validar o token no Authorization Server a cada requisição.
- **Validação local** — o token é autoassinado e não precisa de validação a cada request, pois já carrega sua própria assinatura (validação embutida).

## Grant Types

O **Grant Type** define como a aplicação obtém o token. Três principais (deixando de lado outros hoje considerados antipadrões):

- **Authorization Code** — o usado no exemplo do login com Google. Para aplicações web, SPAs, mobile, e qualquer login de usuário comum. Envolve redirecionamento do usuário pelo navegador e consentimento explícito de um humano. Se você precisa autorizar algo sem poder redirecionar o usuário pelo navegador, provavelmente esse não é o grant type certo. Hoje em dia exige o uso de **PKCE** (Proof Key for Code Exchange), camada de proteção contra a interceptação do authorization code — garante que quem iniciou o login é o mesmo componente que recebe o token, impedindo que um invasor intercepte o código no meio do caminho e o use indevidamente.
- **Client Credentials** — não existe usuário humano na tela; é sistema conversando com sistema (integrações entre back ends, jobs agendados). A aplicação se autentica com seu próprio client id e client secret no Authorization Server — como um login/senha, mas para aplicações, não usuários. Fluxo mais simples que o Authorization Code.
- **Refresh Token** — serve para renovar um access token que se tornou inválido/expirado.

## Escopos

Um **escopo** (scope) é um controle fino de permissões: responde à pergunta "o que essa aplicação pode fazer em meu nome?". É basicamente uma lista de permissões — o que aparece quando alguma aplicação pede para logar com seu Gmail, por exemplo — e vai embutido no access token. Cabe à API validar as permissões de acordo com o que o usuário liberou, antes de executar as ações.

## Conclusão

O OAuth nasce para resolver um problema muito específico de um momento histórico muito específico: parar de compartilhar senha para integrar sistemas. A solução é simples e poderosa: em vez de entregar sua identidade, você entrega uma autorização limitada, temporária e controlada. A aplicação não se passa por você em nenhum momento — ela age em seu nome, dentro do que você permitiu, pelo tempo que você permitiu.

É por isso que hoje praticamente toda API moderna, todo login social, toda integração entre serviços, toda arquitetura moderna passa em algum momento por algum serviço OAuth. Conceitualmente: OAuth é autorização, é procuração, é delegação de acesso.

(O próximo vídeo da série trata do OpenID Connect — o protocolo que cuida da parte de autenticação e que, combinado com o OAuth, permite coisas como single sign-on e identidade federada.)
