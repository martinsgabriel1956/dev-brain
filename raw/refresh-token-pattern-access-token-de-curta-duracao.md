# Refresh Token: como manter o access token curto e o usuário logado com segurança

## Introdução

Você já passou pela frustração de estar preenchendo um formulário longo e gigantesco na hora de salvar, e ser jogado pra tela de login porque sua sessão expirou? Ou então, como deve já ter feito, apelou para criar aquele token que vale 30 dias, que vale 1 ano, que vale 100 anos, só pro seu usuário não reclamar — e acabou abrindo uma brecha de segurança enorme mesmo sem perceber?

Aliás, se o seu sistema usa JWT com validade longa, você provavelmente tem uma falha de segurança em produção. Então esse vídeo é para você.

No vídeo de hoje vamos entender o padrão de refresh token: como criar um fluxo onde o seu access token é curto e seguro, mas o usuário continua logado de forma transparente por um tempo bem mais coerente com a rotina que ele usa naquele sistema.

Olá devs, eu sou Bernardo Lobato e hoje vamos seguir no nosso caminho de autenticação e, especialmente, autorização, falando sobre um pattern muito conhecido para quem já deu suas voltas ali pelo mundo do AuthN/AuthZ: o refresh token. Esses são padrões ou componentes que permitem que um access token seja renovado, e dessa forma possa manter uma vida curta de maneira mais segura.

Só lembrando brevemente: o access token é um tipo de string que permite que tenhamos acesso a recursos protegidos, e existem diversas formas de criar e validá-los.

## Por que não usar um token de longa duração?

Para começo de conversa: por que eu quero um token de curta duração? Não seria mais fácil ter meu token com a maior duração possível pro meu usuário ficar o tempo inteiro logado?

Resposta curta e simples: não.

Vamos a um exemplo. Imaginemos um token JWT que tem a validade de um ano completo. Esse modelo de token, conforme já vimos, é um token auto-contido que deve ser enviado em todas as requisições que precisam ser autorizadas no endpoint protegido. Isso significa que ele vai passear por logs de servidores, pode ficar armazenado no navegador dependendo da estratégia de armazenamento, ser exposto em algum console.log por aí. Além disso, se o usuário estiver numa rede corporativa, numa VPN, esse token vai trafegar por servidores que a gente nem imagina, desde load balancer até serviços de nuvem.

Se o seu token dura um ano, e ele vai sendo exibido por todas essas etapas, por todos esses lugares, e alguém mal-intencionado tem acesso a esses servidores, a esses logs, em qualquer uma dessas etapas, essa pessoa vai ter um ano para usar esse token tranquilamente dentro de requisições mal-intencionadas — pois a gente não pode revogá-lo, já que o JWT é stateless.

Uma analogia interessante: é mais seguro pensar no access token como um crachá de visitante — daqueles que a gente recebe quando vai num prédio comercial — do que de fato como uma chave real de uma fechadura. O crachá precisa expirar no fim do dia, e no dia seguinte eu não posso mais usá-lo, a não ser que eu seja revalidado, que eu passe na recepção e revalide aquele crachá. A ideia com os tokens é muito parecida com isso.

## O problema da revogação em tokens stateless

Antes de prosseguir, precisamos falar sobre revogação do token — uma das grandes limitações do token JWT, que é por natureza stateless. Isso significa que o servidor não precisa olhar no banco de dados ou no authorization server para saber se aquele token é válido; ele só precisa checar a assinatura.

Esse mecanismo acaba trazendo alguns problemas. Se o usuário fez logout, por exemplo, ou pior, foi demitido, ou teve o equipamento roubado, você não pode esperar um ano para o token expirar e cortar o acesso dele. A gente quer esperar o menor tempo possível, por questões óbvias de segurança.

É claro que existem estratégias que invalidam de fato o token JWT, mas isso foge um pouco do escopo desse vídeo, pois qualquer alternativa nesse sentido faz a arquitetura perder a característica de ser stateless — ela passa a ser stateful.

## Refresh token: o ingrediente a mais

É aqui que a gente coloca um ingrediente a mais no nosso processo de autenticação e autorização: o refresh token.

Você provavelmente já esbarrou com um retorno parecido com esse ao fazer login numa API, seja ela sua ou de terceiros, uma que utilize OAuth por exemplo:

```json
{
  "user": { "...": "..." },
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "8xLOxBtZp8...",
  "expires_in": 900,
  "token_type": "Bearer"
}
```

Cada campo tem uma função estratégica dentro do processo de autorização:

- **user**: dados básicos do usuário. Serve pro frontend saber quem é esse usuário logado sem precisar fazer outras chamadas de API. Completamente opcional.
- **access_token**: o crachá, o token que a gente já vem trabalhando — um JWT com duração curta, enviado no header `Authorization` em cada requisição.
- **refresh_token**: o campo novo — a chave de renovação.
- **expires_in**: o tempo exato em segundos que o access token vai durar. Ajuda o frontend a se programar internamente para a renovação, mas não é obrigatório.
- **token_type**: define o esquema de autenticação. No caso, o padrão `Bearer`, que indica que quem porta o token tem autorização — ou seja, se alguém capturar esse token por algum motivo, essa pessoa herda todos os poderes fornecidos por ele, podendo usá-lo inclusive em ferramentas como o Postman.

Você tem dois tokens: o access token, que já vimos, deve ter duração curta e ser enviado em toda requisição. Já o refresh token tem duração muito maior e não vai em todas as requisições — só quando necessário, ou seja, quando o access token já não vale mais.

## O fluxo de renovação

1. Você faz login e recebe as duas chaves. A vida segue normal, você vai utilizando a aplicação normalmente.
2. O access token expira. A API retorna um erro `401 Unauthorized`.
3. O frontend entra em ação de forma silenciosa: percebe o erro 401, pega o refresh token guardado e pede um novo access token pra API, num endpoint diferente do da autenticação original. Se o refresh token for válido, a API entrega um novo access token.
4. A requisição original, que tinha falhado com 401, é refeita com o novo token e dá sucesso.

Tudo isso sem que o usuário perceba que a sessão dele quase caiu.

Aqui vemos a importância do backend mapear os erros direitinho — é fundamental que o erro 401 seja retornado da maneira correta para que o frontend possa interceptar essas requisições e dar o tratamento adequado. É também aqui que vemos a importância do cliente implementar uma camada de interceptação de requisições HTTP, seja via interceptors, middlewares ou wrappers de client, dependendo da API que está sendo utilizada (ex.: interceptors do Axios).

## Onde armazenar o refresh token

Se eu recebo dois tokens, em algum momento vou precisar enviar ambos — será que os mesmos problemas de armazenamento e interceptação (logs, servidores etc.) mencionados para o access token não se repetem no refresh token? Sim, podem se repetir, mas existem estratégias para evitar isso.

O refresh token é ainda mais sensível que o access token, porque através dele conseguimos novos access tokens. As alternativas comuns, principalmente no frontend, são as mesmas do access token:

- **`localStorage`**: a mais fácil, mas também a mais perigosa. Fica disponível pra aplicação e qualquer script, o que significa que um ataque XSS pode roubar o refresh token facilmente. Melhor evitar.
- **Em memória / estado da aplicação** (ex.: Redux, um service do Angular): mais seguro contra roubo via scripts, mas se o usuário der F5 na página ele é deslogado na hora, pois a variável é reiniciada. Bom em algum sentido pro access token, péssimo pro refresh token.
- **Cookie `HttpOnly`**: o padrão profissional. O token é guardado pelo navegador, mas o JavaScript não consegue ler o que está escrito nele, por definição do próprio tipo de cookie. Isso blinda o refresh token contra roubo via scripts maliciosos — porém nem a própria aplicação tem acesso a ele, o que resolve vários problemas de armazenamento. E no caso do refresh token, a gente realmente não precisa de acesso ao conteúdo — só precisamos que ele esteja lá e seja válido.

A recomendação é taxativa: armazenar o refresh token no formato de um cookie `HttpOnly`. No caso do access token ainda existe a possibilidade de acessar alguma informação relevante autocontida nele (tipo de perfil, nome do usuário etc.) para uso na própria aplicação — no caso do refresh token, em nenhum momento devemos acessar os dados internos pelo lado do cliente. Ele só serve para gerar novos tokens de autenticação.

### Por que não guardar o refresh token só no backend?

Se você guardar o refresh token só no backend, o cliente/frontend não tem como provar quem ele é na próxima requisição, e você se perde no fluxo completo de autenticação. Para ter algum tipo de identidade, algum vínculo com o backend, você precisaria de uma sessão no servidor — o que anula todo o sentido dessa forma de autenticação.

## Refresh token deve ser stateless ou stateful?

Ele pode ser os dois, mas o padrão da indústria hoje é que ele seja **stateful**.

Se o refresh token for stateless, caímos nos mesmos problemas de um access token stateless (um JWT tradicional). Portanto, precisamos de algo — de forma bem genérica, não necessariamente um banco de dados real — para validar e/ou revogar esse token quando necessário. No OAuth, esse papel é executado pelo chamado authorization server.

### Por que não tornar o access token stateful também?

Se você fizer o access token stateful também, cria um gargalo de performance gigante. No papel parece mais seguro, mas na prática mata a escalabilidade da API. Se o cliente faz 1000 requisições por segundo, seriam 1000 requisições validadas no banco ou no servidor de autenticação a cada segundo. Usando o access token stateless, só validamos no banco/servidor de autorização nos momentos em que o access token expira e precisamos renovar com o refresh token.

## Janela de exposição

A gente aceita que o access token seja stateless porque ele deve durar muito pouco — por exemplo, 5, 10, até uns 15 minutos. Se você banir um usuário agora, no pior caso ele continua acessando o sistema por mais 5 ou 10 minutos, até aquele token específico expirar. A partir daí, como o refresh token estará revogado/invalidado no servidor, ele não vai mais poder renovar.

Pra maioria das aplicações — rede social, e-commerce, backoffice — esse risco é aceitável em troca de uma performance muito maior e de mais escalabilidade. Agora, se você trabalha em um sistema que não aceita esse tipo de risco — operações financeiras de alto valor ou alta criticidade, sistemas de tempo real, operações PIX, sistemas do Banco Central, operações sensíveis — nem mesmo essa janela curta pode ser aceita, e aí provavelmente é preciso rever o modelo de autenticação e autorização do backend.

## Duas camadas extras de segurança

### Refresh token rotation (anti-replay)

Em vez de um refresh token durar, digamos, 7 dias e ser usado várias vezes, ele se torna descartável. Toda vez que o cliente usa um refresh token específico para ganhar um novo access token, a API invalida esse refresh token que acabou de ser utilizado e entrega um novo refresh token junto com o novo access token.

Por quê? Se um invasor rouba o refresh token e tenta usá-lo, e o usuário legítimo usa logo em seguida (ou vice-versa), a API detecta que um token antigo foi reapresentado — isso pode ser entendido como fraude. Nesse momento, pode-se tomar a decisão de deslogar o usuário de todos os lugares possíveis, de forma preventiva — como um sistema de alarme automático. O usuário legítimo, que tem as credenciais, autentica novamente, recebe novos tokens e segue seu fluxo normalmente.

### Fingerprinting / vinculação de dispositivo

Além do token ser válido, ele precisa estar nas mãos de quem o solicitou. Quando o usuário faz login, você pode capturar elementos como o user agent daquela requisição, ou um hash do dispositivo (em caso de mobile), e guardar isso atrelado ao refresh token no banco de dados ou no servidor de autorização. Se o refresh token for apresentado por um navegador ou dispositivo completamente diferente e suspeito, bloqueia-se a renovação — como no caso da rotation. Também é possível fazer logout em todos os dispositivos, se for interessante para a aplicação.

## Conclusão

Embora entender esse fluxo seja vital, você não precisa — e muitas vezes não deve — implementar cada linha dessa lógica do zero. Hoje ferramentas de IAM como Keycloak, Auth0 ou o próprio Spring Authorization Server já entregam esses padrões prontos e validados pelo mercado. No entanto, ferramenta nenhuma substitui o critério técnico: dominar os conceitos de stateful/stateless e as camadas de segurança por cima do refresh token é o que evita configurar o ambiente de autenticação e autorização no chute, criando brechas de segurança mesmo sem saber. Esse conhecimento é o que dá controle para usar a ferramenta do jeito certo.
