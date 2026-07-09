# 10 Conceitos Fundamentais do Backend

Você clica em "entrar". Em menos de um segundo o sistema valida a requisição, checa a senha, cria sessão, consulta banco, escreve logs e devolve uma resposta. Parece uma chamada simples, mas por trás desse clique existe um backend inteiro tomando decisões — e quase todo backend profissional se apoia nas mesmas 10 ideias. Não importa a linguagem ou framework usado, esses conceitos vão aparecer em qualquer sistema.

## 10. Requisição e Resposta

Todo backend começa com uma mensagem chegando: um app pede alguma coisa, o servidor processa e uma resposta volta. Isso parece óbvio, mas essa é a base de quase tudo.

Uma requisição normalmente tem:

- Um **método**: GET para buscar, POST para criar, PUT/PATCH para atualizar, DELETE para remover.
- Uma **rota**, tipo `/api/orders`.
- **Headers**, que carregam metadados como token, idioma, tipo de conteúdo.
- Às vezes um **body**, que é o corpo da mensagem.

A resposta também tem estrutura. O **status** vai dizer o que aconteceu: 200 quer dizer que deu certo, 401 faltou autenticação, 404 não foi encontrado, 500 quebrou alguma coisa no servidor.

Requisição e resposta são o idioma básico do backend — mas as duas partes também precisam combinar o formato dessas mensagens.

## 9. Contrato de API

A API é um contrato entre quem pede e quem responde. O frontend não deveria precisar saber como a tabela do banco foi montada ou qual framework o servidor usa — ele só precisa saber qual rota chamar, quais dados mandar e qual resposta esperar.

É isso que facilita o backend mudar internamente sem quebrar os clientes. Se você trocar o banco, dividir o serviço, mudar a regra interna — e o contrato continuar estável, o cliente continua funcionando.

Se o contrato for bem feito, ele vai deixar claro o que pode entrar, o que pode sair, e como o sistema se comporta quando algo dá errado.

Mas antes de executar qualquer regra, o backend precisa decidir se a mensagem recebida faz sentido.

## 8. Validação e Regra de Negócio

O backend nunca pode confiar no que está vindo. Se a quantidade é negativa, não pode passar. Se o e-mail não é e-mail, não pode passar. Se o preço veio do cliente, talvez o backend precise ignorar e calcular de novo — isso acontece para proteger a regra de negócio do sistema.

Uma forma comum de organizar isso é separar em camadas:

- O **controller** entende de HTTP.
- O **service** entende de regra de negócio.
- O **banco** guarda os dados.

Essa separação ajuda a não espalhar a regra crítica em qualquer lugar. Quando essa regra fica espalhada, o sistema pode começar a se contradizer.

Depois de validar o que a requisição quer fazer, vem a próxima pergunta: quem está fazendo esse pedido?

## 7. Autenticação e Autorização

São duas coisas diferentes. A **autenticação** responde "quem é você". A **autorização** responde "o que você pode fazer". Você pode estar logado e mesmo assim não ter permissão para, por exemplo, aprovar um pagamento.

Na prática, o backend costuma receber algum tipo de credencial — cookie de sessão, JWT, token — que mostra se veio de alguém conhecido e também se essa pessoa tem permissão para acessar aquele recurso.

Isso é importante porque muita falha de segurança nasce quando o sistema não trata autenticação e autorização como coisas separadas. Qualquer backend profissional checa essas duas coisas o tempo todo.

Mas saber quem pediu e o que pode fazer ainda não resolve a parte mais importante: onde esses dados ficam.

## 6. Banco de Dados e Modelagem

Guardar o dado é decidir como o mundo real vira estrutura no seu backend. Por exemplo: um pedido tem usuário, tem itens, pagamento, endereço, status.

Se você modela mal, a regra fica confusa. Se você normaliza demais, toda consulta pode envolver vários joins e ficar complexa.

Banco também é performance. Uma query simples pode virar um full scan gigante, ou pode usar um índice e encontrar o dado em poucos passos. Por isso, quando algo está lento, uma das primeiras coisas que se olha é se o problema está numa consulta ruim — se existe algum índice faltando, ou se as tabelas foram organizadas de um jeito que obriga o banco a ler dado de vários lugares.

Mas o banco não serve só para guardar os dados — ele também precisa manter esse dado correto quando várias coisas acontecem ao mesmo tempo.

## 5. Transações e Consistência

Imagine uma transferência: tirar R$ 100 de uma conta é uma operação, adicionar R$ 100 em outra é outra operação. Mas para o sistema isso precisa ser uma coisa só — ou as duas acontecem, ou nenhuma acontece. Esse é o motivo de existir transação: ela cria um isolamento onde tudo dentro dele ou confirma, ou dá errado junto. Sem isso, erros de rede, bugs ou queda de algum processo podem deixar o sistema num estado impossível.

Consistência também aparece com concorrência. Imagine duas pessoas comprando o último produto ao mesmo tempo: as duas lêem estoque igual a 1, as duas tentam confirmar. Se o backend não protege essa parte crítica, ele vai vender mais do que realmente tem. Por isso transação é essencial — ela impede dados reais de ficarem errados.

Mas consistência tem um tradeoff de tempo, e quando esse tempo vira um problema, muita gente usa o próximo conceito.

## 4. Cache

Cache é guardar uma resposta perto de onde ela vai ser usada de novo, para não ter que calcular tudo ou consultar o banco toda vez. Quando o dado está no cache, é o chamado **cache hit** — e isso gera uma resposta rápida. Quando não está, é o chamado **cache miss**: o sistema busca a informação original, guarda uma cópia e usa essa cópia nas próximas vezes.

Mas o cache tem um problema: se o dado muda, a cópia pode ficar velha, e dado velho pode gerar problema dependendo do seu domínio. O cache ajuda a acelerar a leitura, mas cria a pergunta: e quando essa resposta deixa de ser verdade? Um backend bem feito não usa cache só porque é rápido — ele também precisa saber como e quando invalidar.

Mas nem todo o trabalho precisa acontecer na hora da requisição — algumas coisas podem esperar.

## 3. Filas e Workers

Nem tudo precisa acontecer enquanto o usuário espera. Se você faz o checkout, o sistema precisa responder rápido, mas pode depois mandar o e-mail, gerar nota fiscal — tudo isso é um job, mas não precisam travar a resposta principal.

As filas separam o pedido do processamento mais pesado: a API coloca uma mensagem que o worker vai pegar depois. Se tiver muitos jobs, a fila vai crescendo; se precisar processar mais rápido, você consegue subir mais workers.

Mas usar filas também traz novos problemas: e se o job falhar? E se ele processar duas vezes? E se a fila crescer mais rápido do que os workers conseguem consumir? Por isso, ao usar fila, é bom pensar em estratégias de retry, idempotência, ordem e monitoramento.

Quando tudo isso começa a crescer, aparece o próximo conceito.

## 2. Escala e Disponibilidade

Escala é a capacidade do sistema continuar respondendo quando o volume aumenta. No começo, só um servidor costuma resolver: ele recebe a requisição, processa a regra, consulta o banco e devolve a resposta. Mas conforme o produto cresce, esse mesmo servidor passa a receber mais usuários, mais chamadas de API, mais consultas ao banco, mais jobs assíncronos e mais picos inesperados.

**Disponibilidade** é outra parte: o sistema tem que continuar rodando mesmo quando acontecem falhas.

Existem dois caminhos básicos:

- **Escalar verticalmente**: colocar uma máquina mais potente, com mais CPU e memória, na mesma instância.
- **Escalar horizontalmente**: colocar mais máquinas para dividir o tráfego.

O segundo caminho é o mais usado em sistemas atuais, mas exige pensar em estratégia de estado. Se cada servidor guarda informação importante só na própria memória, o usuário pode cair numa outra instância e perder todo o contexto — uma sessão que existia na máquina A não existe na máquina B, um job em andamento pode sumir se a instância cair.

Por isso muitos backends tentam ser **stateless**: a instância que processa a requisição não guarda estado importante, que fica em lugares compartilhados como Redis, cache, fila ou algum serviço externo. Assim, qualquer instância consegue responder à próxima requisição.

A disponibilidade também depende de saber quais partes do sistema estão saudáveis — é aí que entram conceitos como **load balancer**, **deploy gradual**, **rollback** e **redundância**. O load balancer não deveria mandar tráfego para uma instância que travou; um deploy não deveria derrubar todas as máquinas ao mesmo tempo.

Escala não é só colocar mais servidor — o backend precisa ser desenhado para dividir carga mesmo quando algo dá errado. E para saber que alguma parte falhou, você precisa conseguir enxergar o sistema por dentro.

## 1. Observabilidade

Observabilidade é a capacidade de entender o que está acontecendo dentro do sistema coletando os sinais que ele emite. Quando o backend quebra, você precisa saber mais do que "está dando erro" — precisa saber qual rota falhou, em qual horário, com qual usuário, depois de qual deploy, em qual parte do fluxo a requisição ficou lenta ou parou. Sem isso, você nem sabe por onde começar a procurar.

Os três sinais mais comuns são **logs**, **métricas** e **traces**:

- **Logs** detalham eventos específicos: uma requisição foi feita, uma validação falhou, um pagamento foi recusado, um worker processou um job.
- **Métricas** mostram o comportamento do sistema ao longo do tempo: taxa de erro, latência, uso de CPU, tamanho da fila, requisições por minuto.
- **Traces** mostram o caminho de uma requisição por dentro do sistema — a chamada passou pela API, depois autenticação, depois service, depois cache, depois banco. Se só o banco gastou 800ms, o trace deixa isso claro.

Cada sinal ajuda a responder uma pergunta diferente: o log ajuda a entender o que aconteceu, a métrica ajuda a entender se o problema está crescendo, o trace ajuda a entender onde o tempo está sendo gasto. Depois de um deploy, dá para ver se a taxa de erro subiu; quando uma fila começa a acumular jobs, dá para perceber antes do usuário; quando uma query fica lenta, dá para encontrar qual rota está chamando essa query e em quais condições.

Observabilidade não substitui banco, cache, fila ou autenticação — nenhuma parte da stack do backend. Ela ajuda a amarrar todos esses conceitos no mundo real. Sem ela, você pode até construir um backend, mas não consegue mantê-lo com confiança.
