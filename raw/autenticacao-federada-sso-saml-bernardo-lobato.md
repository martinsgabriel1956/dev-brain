# Autenticação Federada e SSO: de LDAP e Kerberos ao SAML (Bernardo Lobato)

> Transcrição de vídeo do canal de Bernardo Lobato, parte da série sobre APIs/autenticação. Original em pt-BR (transcrição ASR bruta, sem pontuação); limpa e organizada em seções abaixo. Sem necessidade de tradução.

## Abertura — o problema

Você já se deparou com aquele cenário onde o usuário entra em cinco sistemas da mesma empresa mas não precisou inserir login e senha cinco vezes? Isso é autenticação federada. Neste vídeo vamos ver o que realmente permite isso acontecer: autenticação federada e Single Sign-On (SSO).

Imagine uma empresa com 10 sistemas diferentes — RH, financeiro, ponto eletrônico, chamados, intranet etc. Cada sistema possui seu próprio login e senha, com suas próprias regras de definição e rotacionamento de senha, seu próprio formato de username (pode ser o e-mail da empresa, pode não ser), e sua própria base de usuários.

A princípio isso não parece um problema tão grande — você cuida da sua vida, faz login em cada portal. Mas 10 logins, 10 senhas, 10 post-its no monitor, ou a mesma senha repetida em tudo (quando o sistema permite). Cada sistema pode ter regras de senha diferentes: no sistema A troca a cada 10 dias, no sistema B a cada 45 dias — e o usuário esquece a senha toda semana.

Do outro lado, o time de suporte/sustentação de cada sistema lida com uma enxurrada de chamados de reset de senha o dia inteiro. Pior: quando alguém se desliga da empresa (ou tem o equipamento roubado), é preciso um processo muito bem azeitado de revogação de acesso em todos os 10 sistemas — qualquer falha nesse processo é um risco de segurança real (acesso residual após desligamento).

Do lado do time de desenvolvimento: cada time em cada projeto precisaria implementar seu próprio módulo de gestão de autenticação e autorização, com regras específicas e controle de perfis — consumindo tempo relevante de desenvolvimento, e esse domínio precisaria ser retestado e revalidado constantemente. O problema não é autenticação e autorização em si — é cada sistema tratar disso do seu próprio jeito, gerando complexidade sem ganho real, já que as regras de autenticação/autorização são maduras e mudam pouco de um sistema para outro.

## Identity Management: base única de usuários

E se existisse uma base única de usuários, e toda autenticação/autorização passasse **somente** por essa base para validar o acesso? Esse é o conceito de **Identity Management** (gestão de identidades).

### LDAP

Historicamente, uma base LDAP cadastra todos os usuários de uma organização e vira um provedor de autenticação. Pense no LDAP como um "chmod corporativo": assim como o `chmod` dá permissões em diretórios numa máquina Linux, o LDAP dá permissões dentro de diretórios corporativos. Ainda hoje é muito utilizado como base de autenticação corporativa — inclusive integrado a ferramentas como o Microsoft Active Directory — além de uso em VPNs, proxies, acesso a e-mail, etc. O LDAP moderno (versão 3) é definido em um conjunto de RFCs.

O uso do LDAP já foi um grande ganho, principalmente entre o final dos anos 90 e meados dos anos 2000, época da explosão de sistemas web internos (intranets, portais corporativos). Mas mesmo com login/senha únicos para todos os sistemas, a **autenticação ainda precisava ser feita em cada sistema individualmente** — o desafio de múltiplas autenticações persistia.

## Kerberos — anos 80, MIT

Para dar o próximo passo, é preciso voltar aos anos 80, no MIT. Conforme o uso de computadores pessoais crescia, surgiu a necessidade de que qualquer aluno pudesse sentar em qualquer máquina da universidade e, com seu login de rede, acessar seus próprios arquivos naquela máquina. Nesse contexto nasce o projeto **Kerberos**, com o objetivo adicional de nunca expor a senha do usuário na rede.

Funcionamento, em essência: em vez de provar quem você é para cada servidor individualmente (o que exigiria múltiplas senhas), você prova quem é para uma espécie de "cão de guarda" e recebe um **ticket** (algo como um token), que apresenta aos outros servidores. Esses servidores confiam no cão de guarda e deixam você passar sem autenticar de novo.

O nome Kerberos (Cérberos em português) vem do cão de três cabeças da mitologia grega que guardava a entrada do mundo dos mortos. No protocolo, as três cabeças representam os três pilares da autenticação: o cliente, o servidor, e o centro de distribuição de chaves (KDC).

O momento divisor de águas do Kerberos ocorreu no final dos anos 90/início dos anos 2000, quando a Microsoft adotou o **Kerberos V5** como protocolo de autenticação padrão do Windows 2000 e do Active Directory. É utilizado até hoje para autenticação em redes locais, definido pela **RFC 4120**.

## A transição do Kerberos para o SSO moderno

A grande transição ocorreu quando a autenticação precisou sair das redes locais fechadas (intranets) e atravessar a fronteira da internet. Enquanto o Kerberos reinava em intranets corporativas baseadas em tickets e sessões persistentes, a ascensão de aplicações online corporativas exigiu protocolos que não dependessem de uma conexão direta com o servidor da empresa — levando ao surgimento de padrões baseados em **tokens e claims**.

Essa evolução manteve o princípio central do Kerberos — confiar em um terceiro elemento (o "cão de guarda", que hoje chamamos de **provedor de identidade** / Identity Provider) — mas trocou a complexidade de chaves simétricas e tickets temporais pela flexibilidade de **assinaturas digitais** e comunicação via HTTPS, permitindo que um único login identifique o usuário em múltiplos serviços globais, de forma leve e segura. Isso é o **SSO** como conhecemos hoje: a capacidade de o usuário autenticar uma vez e acessar vários sistemas com essa mesma autenticação, sem inserir login/senha de novo.

## O que é autenticar, de verdade

Antes de seguir para o SAML, vale conceituar: autenticar alguém é o processo de provar uma identidade, transformando uma afirmação subjetiva ("eu sou fulano") em evidência objetiva e verificável. Não se resume a conferir se a senha está correta — é reduzir a incerteza de que a pessoa do outro lado da tela é de fato quem ela diz ser.

Três pilares clássicos (fatores de autenticação):

1. **Algo que você sabe** — o fator mais comum e, isoladamente, o mais frágil: senhas, PINs, respostas a perguntas de segurança.
2. **Algo que você tem** — posse física: token de hardware, cartão magnético, crachá, dispositivo que recebe um OTP (os famosos TOTP), ou um app no celular.
3. **Algo que você é** — biometria: digitais, reconhecimento facial, padrão de íris, ritmo de digitação/fala. É o mais difícil de ser roubado, mas apresenta desafios de privacidade, precisão e implementação técnica, especialmente em sistemas web.

O grande desafio de autenticar alguém no ambiente digital é que, tecnicamente, o sistema não autentica o ser humano — autentica **credenciais**. Se um atacante sabe a senha e tem acesso ao celular que recebe o OTP, para o sistema ele "é" o usuário.

## Autenticação Federada

Autenticação federada é, em essência, um modelo de **terceirização de confiança**: permite que uma organização aceite a identidade de um usuário validada por outra organização, sem que ambas precisem compartilhar o mesmo banco de dados de senhas. Enquanto o gerenciamento de identidade tradicional exige criar uma conta por serviço, a federação estabelece uma ponte — uma relação de confiança onde a prova de identidade emitida por uma entidade confiável é aceita por terceiros.

Exemplos do dia a dia: entrar no Trello com a conta do Google, acessar o Slack com a conta Microsoft Entra ID da empresa, logar num e-commerce usando o Facebook.

## SAML (Security Assertion Markup Language)

O **SAML** surgiu no início dos anos 2000 para resolver o desafio de estender a identidade do usuário além das fronteiras de uma rede local — foi projetado para a era da web, permitindo que empresas compartilhassem autenticação com parceiros externos (fornecedores de software). A versão **2.0**, lançada em 2005, consolidou o padrão, unificando diferentes bibliotecas e abordagens, e tornou-se a espinha dorsal do SSO corporativo moderno até a ascensão de outros protocolos como o OpenID Connect.

O SAML introduziu uma linguagem baseada em **XML** que permite afirmar fatos sobre o usuário de forma segura. Permitiu que o login ocorresse em um local (o portal da empresa) e o acesso fosse concedido em outro totalmente diferente, sem que a senha do usuário jamais saísse do domínio original do provedor de identidade.

### As três partes do protocolo

- **Identity Provider (IdP)** — responsável por autenticar de fato o usuário.
- **Service Provider (SP)** — o sistema que o usuário quer acessar.
- **Usuário / navegador (browser)** — quem faz as requisições. O uso do browser é fundamental no protocolo — os redirecionamentos acontecem no cliente.

### Troca de metadados (setup prévio)

Antes de qualquer login, o IdP e o SP precisam ser apresentados um ao outro — processo geralmente chamado de troca de metadados. O IdP entrega ao SP seu **certificado X.509**, que contém a chave pública do IdP. O SP salva essa chave e suas configurações e passa a confiar no IdP. A **chave privada** nunca sai dos servidores do IdP — é o segredo usado para assinar os documentos.

### Fluxo de autenticação

1. **Acesso inicial e redirecionamento**: o usuário tenta acessar uma aplicação protegida (o SP). Como ainda não está autenticado nessa aplicação, o SP gera uma mensagem chamada **SAMLRequest** e instrui o navegador a redirecionar esse pedido ao IdP.
2. **Autenticação isolada no IdP**: o usuário chega na tela de login do IdP (Okta, Google Workspace etc.) e insere suas credenciais (usuário/senha, possivelmente um segundo fator). Detalhe crucial: o SP nunca tem acesso nem visualiza a senha digitada — isso acontece inteiramente na tela do IdP.
3. **Geração da SAMLResponse**: após confirmar a identidade, o IdP cria uma **SAMLResponse** — um documento XML contendo as *assertions* (dados como e-mail, grupos de acesso, validade daquele login) — e envia esse documento assinado digitalmente de volta ao SP, novamente através de um redirecionamento passando pelo navegador do usuário.
4. **Validação no SP**: o SP recebe o XML, valida a assinatura criptográfica para garantir que ninguém adulterou o pacote no caminho, e concede o acesso à plataforma.

Em detalhe, quando o navegador entrega a resposta ao SP: o SP enxerga o conteúdo XML em texto claro (quem é o usuário, grupos, data de expiração etc.) e a assinatura digital anexada. Se a chave pública do IdP consegue validar a assinatura, o SP tem certeza de que a mensagem veio do IdP — só o dono da chave privada poderia ter gerado aquele hash/assinatura.

### Considerações sobre o protocolo

- O uso do navegador é essencial: são os redirecionamentos 302 no cliente que permitem manter a autenticação transparente, sem a senha passar pelo SP.
- O protocolo é extremamente dependente de XML — mais verboso que o JSON usado hoje em dia. Funciona bem em sistemas web tradicionais, mas é bastante complicado de usar em APIs ou Single Page Applications, justamente por depender do browser e desses redirecionamentos entre componentes diferentes. Nesses casos costuma-se recomendar outros protocolos, como o OpenID Connect.
- Apesar disso, o SAML ainda reina em sistemas corporativos — grandes empresas o usam para login/SSO de funcionários em ferramentas como Salesforce, entre outras — porque oferece controle de segurança centralizado rígido, já integrado a tecnologias legadas como o Active Directory.

### SAML e OAuth interoperando

SAML (e outros protocolos de autenticação federada) é interoperável com o OAuth, que é um protocolo de autorização. Nesse cenário, a assertion SAML é apresentada a um servidor de autorização OAuth como uma credencial; o servidor valida a assinatura do XML e, em troca, emite um **access token** — podendo ser um JWT leve e moderno. Essa ponte permite que aplicações modernas e APIs REST consumam identidades vindas de diretórios legados de forma transparente, unindo a robustez da federação empresarial com a agilidade necessária ao ecossistema de microsserviços.

A versão 2.0 do SAML, lançada em 2005, permanece o padrão-ouro para federação de identidades em ambientes corporativos e governamentais até hoje (2026). Ferramentas self-hosted como o Keycloak estão prontas para uso com esse protocolo, além de grandes provedores de identidade como Okta, Microsoft Entra ID e Google Workspace. Para implementar suporte via código, existem bibliotecas maduras e consagradas, dependendo da linguagem de programação.

## Fechamento

O que parece apenas um "login automático" é, na verdade, o resultado de décadas de evolução — dos primeiros tickets do Kerberos no MIT até as assertions XML robustas do SAML 2.0 e protocolos como o OpenID Connect. Entender a diferença entre autenticação local e autenticação federada, e principalmente seus conceitos e funcionamento, é o que separa um desenvolvedor que "apenas aperta o botão" de quem se preocupa de verdade com segurança e escalabilidade.

O SAML pode parecer verboso e antigo com seu XML, mas ainda é o "porteiro" das maiores corporações do mundo — conhecer o protocolo é um diferencial para quem deseja trabalhar em empresas nesse modelo mais tradicional. A grande sacada da engenharia moderna não foi descartar o protocolo, mas criar pontes — transformando assertions pesadas em XML em tokens JWT leves que APIs conseguem consumir com boa performance. No fim das contas, identidade federada significa delegar a prova de "quem o usuário é" para quem realmente entende do assunto, permitindo focar no que importa: as funcionalidades do próprio negócio.
