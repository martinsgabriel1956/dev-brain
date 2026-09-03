# Anatomia de um Token 2: JOSE, JWS, JWE, JWK, JWA, Algorithm Confusion e PASETO

Você sabe o que tá trafegando no seu header `Authorization: Bearer` quando usa JWT, ou você só deu um `npm install` na biblioteca da moda e seguiu com a vida? Se eu te perguntar agora, você saberia dizer, sem olhar, qual o algoritmo que tá criptografando seu token que autoriza o seu usuário? Saberia explicar como ele funciona? Sabia que o cliente pode trocar esse algoritmo, e se quem tiver implementado o back end tiver mal configurado ou não otimizado a validação do token, pode passar como se fosse válido?

Então esse vídeo aqui é para você. Hoje a gente vai continuar falando sobre tokens, e um pouco mais a fundo sobre o ecossistema JOSE como um todo — e entender que às vezes ele pode ser uma péssima ideia. Então já cria seu token aí com validade de 100 anos, para não ter que ficar trocando enquanto testa sua PoC.

Olá Devs, eu sou Bernardo Lobato, e hoje a gente continua a nossa jornada no mundo dos tokens — dessa vez bem mais específica, nos tokens autocontidos. Esse vídeo é uma continuação direta do "Anatomia de um Token 1", onde eu falo de uma maneira um pouco mais genérica sobre os tipos de token e suas características. Então, se você ainda não viu, link aqui no card, e já deixa aberto no mapinho aí do lado para começar a assistir quando esse aqui terminar. Fechou.

## Recapitulando

Em resumo, caso você ainda não tenha visto o anterior: tokens autocontidos são credenciais que carregam toda a informação e autoridade necessárias dentro de si mesmas, permitindo que o servidor valide quem é o usuário e o que ele pode fazer sem precisar consultar um banco de dados a cada requisição. E aí na tela temos o exemplo de um token autocontido, codificado como base64.

## O Ecossistema JOSE

Para a gente começar a nossa discussão desse vídeo, temos que entrar obrigatoriamente no ecossistema **JOSE**, ou **JSON Object Signing and Encryption**. Esse ecossistema é quem define as especificações criptográficas utilizadas por esses tokens JWT. Ele, resumidamente, possui quatro pilares: o **JWS**, **JWE**, **JWA** e **JWK**. Vamos falar um pouquinho sobre cada um deles.

Mas antes, você pode se perguntar: qual é a relação entre o JWT e o ecossistema JOSE? JWT é o **formato** do token, enquanto JOSE é o **conjunto das especificações** que define como esse token vai ser assinado e criptografado. O JWT pode ser entendido, a grosso modo, como uma instância de um token do JOSE.

## JWS — JSON Web Signature

Vamos começar falando do JWS. O JWS, ou **JSON Web Signature**, é a especificação dentro do ecossistema JOSE responsável por garantir **integridade e autenticidade** de um dado, assegurando que a informação não foi alterada desde que foi criada pelo emissor do token. Ou seja, uma vez que o token é criado, ele nunca mais pode ser alterado sem se tornar inválido — o que nos dá a segurança de que aquela informação foi passada e que, uma vez validada, a gente pode confiar nela.

Ele funciona através de uma assinatura digital — atenção aqui para a palavra "assinatura", que vai ser útil — que vincula um cabeçalho (onde a gente coloca o algoritmo de criptografia utilizado) e um conjunto de dados que a gente chama de **payload**, utilizando uma chave secreta simétrica ou um par de chaves pública e privada, no caso de criptografia assimétrica.

O resultado final é a famosa estrutura de três partes separadas por pontos e codificadas em base64 que a gente já conhece, e permite ao receptor desse token validar matematicamente se o emissor é confiável e se o conteúdo permanece intacto — embora, por padrão, os dados continuem visíveis para qualquer um que consiga decodificar essa string base64.

**É extremamente importante entender esse funcionamento específico do JWS**, pois ele é a base para todos os outros conceitos que a gente vai falar nesse vídeo.

### JWS com chave simétrica

No processo simétrico, emissor e receptor compartilham a mesma chave. O emissor usa essa chave secreta para gerar um hash da assinatura, e o receptor usa a mesma chave para gerar o hash novamente e comparar com o token que ele recebe — é como um aperto de mão combinado previamente no escuro.

É importante ressaltar que o authorization server do exemplo não precisa ser necessariamente um serviço à parte — pode ser a própria API ou o próprio back end que também faça esse papel. E o cliente (nesse caso, um front end) não tem acesso a essa chave de criptografia.

### JWS com chave assimétrica

Aqui usa-se o par de chaves público e privada — o jogo muda um pouquinho. O emissor usa uma chave privada, que só ele tem acesso, para assinar esse token. O receptor usa uma chave pública, que pode ser divulgada, que qualquer um pode ter, apenas para validar essa string. Basicamente o funcionamento normal de uma criptografia assimétrica: a chave privada assina o hash, e a chave pública valida.

### Como o receptor sabe qual algoritmo foi usado?

Existe uma infinidade de algoritmos de criptografia — como o emissor e o receptor sabem qual deles está sendo utilizado dentro do token, para poder decodificar, e como sabem quem gerou esse token? A resposta está no **header**. Esse componente é o metadado que instrui o servidor sobre qual algoritmo e qual chave devem ser utilizados para validar essa assinatura do token. Portanto, todas as informações relevantes a respeito da validação estão nele.

Mas será que isso não é um problema? Não é inseguro expor tanta informação assim? Sim, podemos ter um baita de um problema — mas calma, a gente chega lá.

### Registered claims (RFC 7519)

Além do header, o payload também tem algumas claims de chave-valor pré-definidas — o que a gente chama de **registered claims**. Elas são campos padronizados definidos pela **RFC 7519**, que ajudam a tratar de interoperabilidade entre sistemas. Essas claims são todas opcionais, porém bastante recomendadas:

- **`iss`** (issuer): identifica quem emitiu o token, com uma URL do seu sistema de autenticação.
- **`sub`** (subject): identifica o sujeito do token, geralmente o ID único do usuário.
- **`aud`** (audience): define quais destinatários ou APIs podem aceitar esse token.
- **`exp`** (expiration time): define quando o token deixa de ser válido.
- **`nbf`** (not before): timestamp que define o momento exato antes do qual o token não deve ser aceito.
- **`iat`** (issued at): quando o token foi gerado.
- **`jti`** (JWT ID): identificador único para esse token — essencial para implementar listas de revogação ou detectar alguns tipos de ataque.

Além desses campos, você pode usar seu próprio objeto JSON dentro do payload, que vai trafegar nas requisições — o que é bastante comum, colocando dados de autorização (quais roles o usuário tem acesso, qual o perfil dele, etc).

### Dois pontos importantes sobre o payload

1. **Nada de dados sensíveis.** Como esse objeto trafega livremente nas suas requisições através do `Authorization`, não coloque CPF, e-mail, endereço, nome completo. Sempre trafegue o mínimo de informação possível, só o necessário para autorizar aquele usuário a acessar algum recurso definido. Isso é um ponto bem importante quando se fala de LGPD e pentests — quem já passou por esse tipo de auditoria sabe muito bem do que eu tô falando.

2. **Atenção ao tamanho do objeto.** Esse payload trafega em toda requisição autenticada — se for muito grande, aumenta bastante a latência. Já vi, em mais de uma ocasião, tokens de mais de 1 MB sendo trafegados na rede interna, o que deixava a aplicação inteira extremamente lenta. Imagina um GET qualquer que deveria retornar só um ID, e você ter que trafegar informações gigantes de token — isso pode prejudicar bastante os seus endpoints.

## JWE — JSON Web Encryption

O segundo pilar da especificação JOSE é o **JWE**, regido pela **RFC 7516** (2015). O JWE, ou **JSON Web Encryption**, é a especificação voltada para **confidencialidade**, garantindo que o conteúdo do token não seja legível para qualquer pessoa que não possua a chave de decriptação — diferente do JWS, que apenas assina os dados para garantir integridade, mas expõe o payload.

O JWE utiliza algoritmos de criptografia autenticada para transformar o payload em texto cifrado. Ou seja, agora não temos mais acesso aos dados do token sem a chave de criptografia utilizada. Sua estrutura é um pouco mais complexa que a do JWS: composta por **cinco partes**, em vez das três que a gente viu anteriormente — o cabeçalho, a chave de criptografia, o vetor de inicialização, o texto cifrado e a tag de autenticação.

É o padrão ideal quando o token precisa carregar informações sensíveis que não podem ser expostas via base64, como dados pessoais ou qualquer tipo de segredo de negócio.

### Fluxo de criação de um JWE

1. Cria-se o header com os algoritmos especificados.
2. Codifica-se esse header em base64.
3. Gera-se a **Content Encryption Key (CEK)** — uma chave simétrica e aleatória.
4. Gera-se um **Initialization Vector (IV)** aleatório.
5. Criptografa-se o payload usando a CEK e o IV, com um algoritmo de criptografia autenticada (ex.: AES-GCM). O resultado é um **cipher text** e uma **tag**, artefatos próprios desse tipo de criptografia.
6. Criptografa-se a CEK usando a chave pública do destinatário (algoritmo definido no header).
7. Codifica-se em base64 a chave de criptografia, o vetor de inicialização, o cipher text e a tag — e concatenam-se as cinco partes para formar o JWE.

### Fluxo de decodificação de um JWE

1. Separa-se o token nas cinco partes.
2. Decodifica-se o header (base64).
3. Descriptografa-se a chave de criptografia usando a chave **privada** do destinatário (o destinatário precisa ter essa chave — atenção: destinatário é diferente de cliente).
4. Usa-se essa chave, o IV e a tag para descriptografar o cipher text (o payload).
5. Valida-se a authentication tag durante a descriptografia e recupera-se o payload original.

Esse tipo de token merece um vídeo específico. Felizmente as bibliotecas de JWE de hoje em dia normalmente abstraem bem o funcionamento interno, a ponto de você quase nunca precisar lidar diretamente com os detalhes criptográficos de baixo nível — uma implementação simples seria um `encrypt` recebendo um payload e a chave pública.

## JWK — JSON Web Key

O **JWK**, ou **JSON Web Key**, regido pela **RFC 7517**, é a especificação que padroniza como chaves criptográficas devem ser representadas e transportadas no formato JSON — eliminando a necessidade de lidar com formatos complexos ou binários, como os famosos arquivos `.pem`.

Ele permite que um servidor de autorização publique suas chaves públicas em um endpoint — normalmente algo como `/.well-known/jwks.json` — e a partir daí as APIs possam baixar essas chaves dinamicamente e validar as assinaturas dos tokens gerados com a chave privada correspondente, sem precisar de chaves hardcoded no código ou em variáveis de ambiente. Através de campos como o **`kid`** (Key ID), o JWK facilita a rotação dessas chaves e o suporte a múltiplos algoritmos simultaneamente, evitando o erro de chave fixa no código. O servidor de autenticação expõe o JSON com suas chaves públicas; a API baixa esse JSON, procura o ID da chave que veio no header do token, e faz a validação.

## JWA — JSON Web Algorithms

De acordo com essa especificação, o **JSON Web Algorithms**, regido pela **RFC 7518**, é o conjunto de algoritmos criptográficos padronizados usados pelos tokens da família JOSE. Ele define quais algoritmos podem ser usados para assinar, criptografar ou proteger esses tokens (JWT, JWS, JWE). Em palavras simples: o JWA é a lista de algoritmos credenciados que esses tokens podem usar sem fugir da especificação.

**É aqui que começamos a encontrar os grandes potenciais problemas com essa abordagem do JOSE no geral.** O ponto crítico é que o JWA é a fonte da **cipher agility** — ao oferecer tantas opções, algumas hoje consideradas fracas ou obsoletas, ela acaba delegando ao desenvolvedor a responsabilidade de escolher o que é seguro, o que abre margem para vulnerabilidade.

## Cipher Agility: a faca de dois gumes

**Cipher agility** é uma filosofia de design de sistemas de segurança — como a utilização do ecossistema JOSE — que permite que o protocolo suporte múltiplos algoritmos de criptografia e mude entre eles sem necessidade de reescrever ou, em alguns casos, até refazer o deploy da aplicação. Na prática, isso significa que o token carrega no seu cabeçalho a instrução de qual algoritmo o servidor deve usar para validar aquele token, oferecendo flexibilidade para atualizar esse algoritmo caso o que está sendo utilizado atualmente fique obsoleto.

Muito bom, certo? Na teoria, sim. Mas por que isso seria um problema para o desenvolvedor? Essa liberdade acaba sendo uma faca de dois gumes: ela introduz uma complexidade perigosa, onde o servidor pode ser enganado a aceitar algoritmos mais fracos ou inexistentes, transferindo a responsabilidade da segurança da especificação para quem está implementando — e muitas vezes o desenvolvedor não é versado em segurança, e vai implementando tudo no default conforme chega na API que acabou de instalar. A partir daí, a API fica muito vulnerável a um ataque chamado **algorithm confusion**.

## O Ataque de Algorithm Confusion

Funciona assim: esse ataque explora uma falha de implementação onde o servidor confia cegamente no cabeçalho do token — como o padrão permite que o algoritmo seja definido como `none`, previsto originalmente para cenários onde a segurança já é garantida por outros meios (normalmente numa rede interna, por exemplo).

Um atacante pode pegar um token legítimo, alterar seu conteúdo (como mudar os roles de um usuário para admin, por exemplo), modificar o header para excluir o algoritmo atual, e remover completamente a assinatura final. Se o back end estiver usando uma biblioteca vulnerável ou simplesmente mal configurada, que aceita esse tipo de parâmetro, ele lerá o header, verá que nenhum algoritmo é necessário, e processará o payload alterado como se fosse válido — ignorando a ausência de uma assinatura digital. É a versão digital do "É verdade, esse bilhete."

Essa que expliquei é uma variação mais simples desse tipo de ataque. Existem outras variações — não é simplesmente remover o algoritmo, mas trocar de um algoritmo A para um algoritmo B, o que também permite algumas liberdades até se conseguir obter o token de outros usuários.

### O caso Tim McLean (2015)

Em 2015, um pesquisador chamado Tim McLean revelou que bibliotecas extremamente populares em diversas linguagens — como Node.js, Python, Ruby, PHP — aceitavam essa inexistência de algoritmo (`alg: none`) por padrão. Como essas bibliotecas eram a base de autenticação e autorização para milhões de aplicações, sistemas inteiros gigantescos ficaram expostos da noite para o dia: qualquer um podia pegar um token de usuário comum, mudar para admin, trocar o header para `none`, e entrar no sistema. Existem vários casos documentados de problemas similares com empresas grandes, como a Shopify ou a própria Microsoft.

O ponto central: o header do token pode ser controlado pelo cliente — logo, o back end não pode confiar nele para escolher o algoritmo. Isso é um erro de design. A regra é: **jamais aceitar o algoritmo que vem do cliente**, e manter no servidor uma whitelist com os algoritmos permitidos. As melhores libs de JOSE já atendem esse requisito de maneira facilitada.

## PASETO — Platform Agnostic Security Token

Com tudo isso exposto, vamos finalmente falar sobre o **PASETO** (**Platform Agnostic Security Token**), uma especificação de token de segurança projetada para ser uma alternativa inerentemente segura ao JWT e ao ecossistema JOSE, ao adotar o padrão de filosofia **cipher rigidity** (rigidez de cifra) — o oposto da cipher agility.

Diferente do JWT, onde o cliente pode escolher o algoritmo no header, o PASETO utiliza versões fixas e imutáveis — V1, V2, V3 ou V4 — que implementam apenas algoritmos criptográficos modernos e de alta performance, como **Ed25519** e **AES-256-GCM**, impedindo completamente ataques de algorithm confusion ou a falta de algoritmo no header.

No PASETO, você escolhe entre assinar ou criptografar o token: assinar seria semelhante ao que vimos no JWT/JWS, em que os dados ficam expostos porém imutáveis (com as mesmas restrições que se aplicam ao JWS); os tokens criptografados seriam semelhantes ao JWE, com dados criptografados e não podendo mais ser expostos para quem não tem a chave de criptografia.

A estrutura de um token PASETO é um pouco diferente: ainda tem três partes, mas a primeira parte não tem mais aquele header completo — tem a versão do algoritmo utilizado, o **purpose** (propósito, que pode ser `local` ou `public`), e o payload, com os dados configurados de maneira semelhante aos outros tokens.

## JWT vale a pena?

Depois de passar pelo JWS, JWE, entender o perigo da cipher agility e ver como gigantes de mercado ficaram expostos pelo simples `alg: none`, a pergunta que fica é: JWT vale realmente a pena? A resposta curta é um retumbante **sim**. O JWT é padrão da indústria, é regido por RFC, e se você configurar sua biblioteca corretamente — desativar algoritmos fracos e ser rígido na validação — ele funciona muito bem. O problema não é a ferramenta, é a liberdade excessiva que o ecossistema JOSE dá, e quando o desenvolvedor não é tão ligado nessas questões de segurança, pode dar problema.

Por outro lado, se você está começando um projeto novo hoje e quer dormir tranquilo sem se preocupar se a próxima vulnerabilidade de algorithm confusion vai derrubar o seu sistema, dê uma chance ao PASETO: ele troca a flexibilidade perigosa pela segurança por design — o famoso "menos é mais": menos opções de erro para você, mais segurança para o seu usuário.

---

*Transcrição de vídeo do canal de Bernardo Lobato, continuação direta da série "Anatomia de um Token". Formatada e organizada em Markdown a partir de fala bruta transcrita, sem necessidade de tradução (conteúdo original em português). Trechos de engajamento de canal (like, inscrição, comentários, indicação do próximo vídeo) omitidos ou resumidos onde não agregam valor técnico.*
