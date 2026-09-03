# XSS Attack — Dicionário do Programador (Código Fonte TV)

> Transcrição de vídeo da série "Dicionário do Programador", do canal Código Fonte TV. Agradecimento no vídeo a Lucas Santos pela ajuda na construção do conteúdo. Patrocínio mencionado: Alura (escola online de tecnologia), com menção à formação de Segurança de Aplicações.

XSS attack, ou Cross-Site Scripting, é uma das principais causas de problemas de segurança em sites modernos e está ligado à falta de validação dos dados fornecidos pelos usuários.

## O que é

XSS attack, ou Cross-Site Scripting, é um dos ataques mais simples de serem executados e um dos que podem trazer muitos problemas. É um ataque do tipo injeção — ou seja, quando um código que originalmente não pertencia a uma aplicação é injetado nela por uma fonte maliciosa e executado. Esse tipo de ataque já existia, mas ficou muito mais comum com a popularização da internet.

A ideia principal do XSS é baixar algum script malicioso de uma outra fonte e executar dentro de um determinado site, de uma forma que seja compartilhável — a pessoa que descobre a vulnerabilidade pode compartilhar o link malicioso com outras vítimas.

## Exemplo: a loja do Bob e a Cecília

Imagine um site que vende produtos para cachorros, de propriedade do Bob, com milhares de usuários. Uma dessas usuárias é a Alice, que fez cadastro no site e armazenou suas informações de pagamento. O site do Bob infelizmente não segue boas práticas para armazenar informações de pagamento e guarda tudo em texto plano.

Além disso, o site tem uma vulnerabilidade de XSS descoberta pela Cecília: sempre que ela digita uma busca de produto que não retorna nenhum resultado, a página mostra o texto "pesquisa X não foi encontrada", onde X é o texto pesquisado na caixa de busca.

Fazendo um teste simples, Cecília coloca na caixa de busca o texto `<script>alert('oi')</script>`. Quando ela realiza a busca, a página mostra "pesquisa não foi encontrado" mas, para surpresa dela, o site também exibe um popup com "oi" — ou seja, o script foi de fato executado. Isso significa que ela pode injetar scripts por ali.

Além disso, ela percebe que sempre que faz uma busca a URL da página muda para algo como `https://lojadobob.com.br/busca?q=<texto de pesquisa>`, e quando faz a busca com o script, a URL passa a conter o script dela. (Uma curiosidade: esse mesmo mecanismo é usado por outro tipo de vulnerabilidade chamada CSRF — já explicada em outro episódio do Dicionário do Programador.)

A maldosa Cecília então cria um pequeno site `https://dominiomalicioso.com.br` que serve um script que rouba o cookie de autenticação do usuário da loja. Ela ofusca o código para dificultar a detecção e cria um link encurtado com o endereço da loja apontando para a busca com o payload. Ela posta esse link em grupos de amantes de cachorros, dizendo que é um produto novo e legal. Muitas pessoas clicam no link, abrindo a página que carrega o script malicioso da Cecília, que rouba as sessões de todos que clicaram. Agora Cecília pode acessar ou usar o site legitimamente como qualquer um desses usuários, incluindo pegar os dados de cartão de crédito deles.

## XSS refletido (não persistente)

O exemplo acima é chamado de **XSS refletido** ou **não persistente**: o script não fica armazenado no servidor de destino (no caso, o site do Bob) e precisa ser entregue manualmente para cada vítima. Ataques refletidos exigem mais engenharia social, porque é preciso induzir alguém (ou muitas pessoas) a clicar em um link ou baixar o script — no geral, é preciso enganar uma vítima humana.

### Por que "cross-site scripting"

O nome vem do fato de que o script que é executado está vindo de outro site ou de outro domínio, e o navegador não tem como saber qual é o domínio válido ou não.

### Curiosidade / estatísticas

De todos os ataques documentados em 2019, cerca de 74% deles estavam de alguma forma relacionados a XSS. Ainda hoje, mais de 60% dos sites existentes são vulneráveis a algum ataque desse tipo. Não é à toa que, ano após ano, XSS esteja consistentemente na lista das dez principais vulnerabilidades divulgadas pela OWASP, a comunidade de segurança da web.

## XSS persistente (armazenado)

O outro tipo é o **XSS persistente ou armazenado**, o oposto do refletido. É muito mais perigoso porque não precisa de nenhum vetor humano — o próprio site hospedeiro se encarrega de entregar o script malicioso para o cliente.

O exemplo mais comum desse tipo de ataque são os fóruns antigos. O grande problema desse tipo de site era que usuários postavam tópicos que podiam conter todo tipo de conteúdo — desde texto até imagens, vídeos e, em determinados tipos de fórum (como fóruns de tecnologia), até scripts e códigos.

Uma das formas mais comuns de disseminar XSS do início dos anos 2000 até por volta de 2015 (e ainda hoje) era criar um tópico com um título chamativo — por exemplo, "como minerar bitcoins sem gastar energia" — e, dentro desse tópico, incluir um script mal-intencionado da mesma forma que a Cecília fez, usando a tag `<script>` dentro do campo de texto, para que o navegador interpretasse aquele texto como HTML em vez de uma string. Se o site não tivesse proteção contra a execução de scripts (o que não era muito comum no início da web), qualquer pessoa que entrasse naquele tópico automaticamente baixaria o script malicioso, continuando a propagá-lo até ser removido.

Foi por conta desse tipo de ataque que o nível de preocupação das pessoas com XSS cresceu bastante, principalmente em um mundo onde os conteúdos gerados pelos usuários são extremamente valorizados — eles incentivam a criação de mais conteúdo e o consumo ainda mais desse conteúdo.

## Como se prevenir

O XSS pode ser perigoso, mas para se prevenir é só validar toda entrada de dados do usuário — é preciso preparar as informações antes de executá-las ou armazená-las no banco de dados, escapando/higienizando todas as informações, independente de virem de uma pessoa ou de outro sistema. A regra principal do front-end é nunca confiar no usuário, e isso serve para o back-end também: sempre validar os dados de entrada, e sempre validar também as sessões.

Voltando ao caso da loja do Bob, ele poderia ter mitigado o problema com passos simples:

- A entrada de dados da busca poderia ter sido escapada e sanitizada.
- O servidor poderia detectar logins múltiplos (mesma sessão usada em locais diferentes) e invalidar a sessão suspeita.
- O site poderia armazenar/exibir apenas os últimos dígitos do cartão de crédito.
- O site poderia pedir confirmação de senha novamente antes de trocar dados de pagamento.
- Poderia implementar uma Content Security Policy (CSP) para evitar que scripts de terceiros fossem executados no domínio.
- O cookie de sessão poderia ter sido marcado como `HttpOnly`, para evitar o uso a partir do JavaScript.

Essas são algumas formas de prevenção do XSS — mas o problema ainda existe e pode ser explorado de várias maneiras.

## Resumo

XSS attack é quando se consegue executar o script de um site malicioso dentro de um site legítimo em que a vítima já está logada. Existem duas formas principais:

- **Refletida**: o script precisa ser enviado manualmente para as vítimas, porque ele não fica armazenado no servidor — muito comum via links maliciosos e conteúdo compartilhável.
- **Persistente (armazenada)**: mais perigosa, porque o próprio usuário consegue incluir de forma persistente um script malicioso no banco de dados do servidor, de forma que ele é servido para todos os usuários que acessarem aquele conteúdo.

Apesar de perigoso, é fácil de mitigar: basta não confiar em nada que é enviado pelo usuário e sempre manter controle rigoroso sobre a validação de dados nas aplicações.

---

O vídeo indica como próximo conteúdo relacionado um episódio sobre SQL Injection, mostrando na prática como esse ataque acontece e como evitá-lo — descrito como, assim como o XSS, um ataque comum mas fácil de evitar.
