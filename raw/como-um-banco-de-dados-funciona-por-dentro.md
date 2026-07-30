# Como um banco de dados funciona por dentro

Você confirma um Pix em poucos milissegundos: o banco muda bytes na memória e grava um log no disco. Aí ele promete que esse dado não vai sumir, mesmo se o processo cair no meio — ele precisa subir de novo sem perder uma transferência confirmada.

Hoje eu vou abrir essa caixa preta para mostrar como um banco funciona por dentro. E uma novidade: a partir de hoje, todo vídeo do canal vai ter uma aula grátis relacionada na minha plataforma. Espero que gostem.

Para não ficar abstrato, vou seguir pelo caminho de um banco relacional. Cada banco organiza as peças de um jeito, mas a pergunta principal vai ser sempre a mesma: como uma mensagem que veio do back-end se transforma em dado persistido?

Para isso acontecer, o banco roda como processo ou serviço que recebe comandos por uma conexão. Essa conexão carrega uma sessão com usuário, permissões, configurações e talvez uma transação aberta. Um SELECT, por exemplo, vai querer ler; um INSERT, UPDATE ou DELETE quer mudar um estado. E por fora vai tudo parecer uma chamada simples, mas por dentro o banco vai precisar combinar essas três coisas ao mesmo tempo: ele precisa encontrar os dados, controlar quem pode enxergar ou mudar cada linha, e garantir que o resultado vai sobreviver a falhas.

## Onde o dado mora

Para entender isso, a gente precisa começar explicando onde o dado mora. Quando você imagina uma tabela, é normal pensar em linhas soltas, mas o banco não costuma buscar uma linha isolada no armazenamento. Ele organiza o dado em páginas. Uma página é um bloco com várias linhas dentro.

Então, se uma query precisa buscar o débito de R$ 100 dessa transferência, o banco vai atrás da página onde essa linha está. Se uma consulta lê 1000 linhas espalhadas em muitas páginas, ela vai ser lenta. Se ler 1000 linhas que estão próximas, o caminho vai ser bem mais barato. Por isso que modelagem e índices importam: o banco vai pagar duas contas — as linhas que entram no resultado, e o caminho para chegar até as páginas onde elas estão.

## Buffer pool: a memória interna do banco

Mas buscar página direto no disco demora muito mais do que ler da memória. E se o banco fizesse isso para cada consulta, ele gastaria tempo trazendo páginas que talvez já foram lidas um segundo atrás, por exemplo. Por isso o banco mantém um cache interno de páginas na memória: o buffer pool.

O buffer pool é a memória interna do banco para páginas de dados. Quando uma query precisa de uma página, o banco primeiro procura nessa memória. Se a página já está lá, é um *buffer hit*. Se não está, ele precisa buscar no disco e colocar a página no buffer. Por isso uma query pode ficar mais rápida depois da primeira execução — isso porque as páginas necessárias já estavam carregadas na memória.

Mas a memória é limitada. Quando o buffer pool encher, o banco vai precisar escolher quais páginas ficam e quais vão sair. Se uma página foi só lida, ela pode sair sem problema. Mas se uma página foi modificada, ela vira uma *dirty page* (página suja). Isso significa que a cópia em memória já mudou, mas a página definitiva no disco talvez ainda não.

## Write-Ahead Log (WAL)

Mas se a página alterada ainda não foi gravada no arquivo final, como o banco pode prometer durabilidade na escrita?

O banco geralmente não reescreve o arquivo inteiro na hora. Ele encontra a página relevante, carrega essa página na memória (se ela ainda não estava lá) e aplica a mudança. Nesse exemplo, o saldo da conta muda de 100.000 para 90.000 — a página em memória agora tem a versão nova. Só que gravar a página final no disco pode acontecer depois, e esse atraso tem um motivo: se o banco gravasse cada página final imediatamente, ele perderia muita performance. O disco funciona melhor com escrita mais organizada em lotes, no momento certo.

Só que o banco não pode simplesmente confiar na memória, porque se o processo cair, o que estava na memória vai sumir. Então, antes de dizer que a transação confirmou, ele vai precisar gravar um registro dessa mudança em um lugar mais seguro — e isso é um log chamado de *write-ahead log* (WAL). Write-ahead log literalmente significa "log escrito antes": antes de gravar a página final no arquivo de dados, o banco vai gravar no log.

Depois que o log estiver pronto, o banco pode responder com commit. A página modificada pode ser gravada no arquivo de dados depois. Por isso o banco pode responder "commit OK" antes de gravar a página modificada no arquivo de dados.

Se o processo cair depois do commit, o banco vai lá e lê o log na inicialização. Aí ele vai reaplicar o que estava confirmado. Se alguma mudança começou mas não foi confirmada, o banco vai descartar ou desfazer aquela parte, dependendo de como aquele banco implementa recuperação especificamente. E esse é o conceito de durabilidade: ele promete que tem informação suficiente para reconstruir o estado confirmado.

## Transações e atomicidade

O problema é que algumas mudanças precisam andar juntas, e é aí que entram as transações. Uma transação existe porque algumas mudanças só fazem sentido juntas. Vamos pensar no mesmo exemplo do Pix: o banco precisa tirar R$ 100 de uma conta e colocar R$ 100 em outra. Se só a primeira parte acontecer, o dado vai ficar errado. Por isso a transação agrupa as mudanças: ou todas as mudanças da transação são salvas, ou nenhuma delas vale.

Esse bloco tem três partes: BEGIN abre a transação, os dois UPDATEs entram no mesmo grupo, e COMMIT confirma o grupo inteiro. Se alguma coisa dá errado antes disso, o ROLLBACK cancela o grupo inteiro. É assim que o banco entrega a chamada atomicidade: a ideia de tudo acontecer junto, ou nada acontecer.

## Controle de concorrência: locks e MVCC

Em produção, várias transações rodam ao mesmo tempo, e é aí que o banco precisa controlar a concorrência. Banco de dados quase nunca executa uma transação por vez. Enquanto um Pix debita uma conta, outro Pix pode tentar debitar a mesma conta. Se os dois leem o mesmo saldo antes de atualizar, uma transferência pode passar por cima da outra. Para evitar isso, o banco usa locks nos dados que não podem mudar ao mesmo tempo. Um lock é uma trava temporária: ele faz uma transação esperar até a outra terminar.

Mas o banco também não quer fazer toda leitura esperar toda escrita. Para isso, muitos bancos usam MVCC — controle de concorrência por múltiplas versões. Quando uma transação altera uma linha, o banco pode manter a versão antiga por um tempo e criar uma versão nova. A leitura que começou antes continua vendo a versão antiga; a escrita segue criando a versão nova. Assim, uma consulta de extrato não precisa travar só porque tem outro Pix que acabou de mudar o saldo.

## Níveis de isolamento

Mas isso não significa que toda transação enxerga os mesmos dados. O que cada transação pode enxergar depende do nível de isolamento. Isolamento responde uma pergunta muito prática: qual versão dos dados essa transação pode enxergar?

No Read Committed, cada comando costuma enxergar o que já foi confirmado antes dele rodar. Então duas leituras dentro da mesma transação podem ver saldos diferentes, se o outro Pix confirmou uma mudança no meio do caminho. No Repeatable Read, a transação mantém uma visão mais estável — por isso a segunda leitura pode ver o mesmo saldo que a primeira.

Mas esse controle tem um trade-off: mais isolamento vai reduzir a surpresa, mas também pode aumentar a espera de lock, ou a chance de uma transação falhar e precisar tentar de novo. Por isso o banco não escolhe sempre o isolamento mais rígido — ele oferece níveis diferentes, e a aplicação escolhe conforme o risco do fluxo. Debitar dinheiro de uma conta, por exemplo, é algo arriscado; consultar um extrato antigo pode aceitar uma visão menos rígida.

## Índices também são dados

Agora que a transação confirmou, ainda existe uma peça importante: os índices também são dados, e eles também precisam ser mantidos. Índice é uma estrutura auxiliar: ele ajuda o banco a encontrar linha sem testar página por página. O exemplo mais comum é uma B-tree, uma árvore ordenada que guia a busca até uma faixa pequena do dado.

Para uma tela de extrato, por exemplo, o índice por `account_id` e `created_at` ajuda o banco a chegar nas linhas daquela conta ordenadas por data. Só que o índice também precisa estar correto depois de cada escrita: se você insere um lançamento novo, a tabela muda e o índice também vai mudar; se você estorna uma transação e muda o status dela, o índice daquele status também pode precisar mudar. É por isso que índice demais pesa na performance.

O problema é criar índice sem olhar o acesso real: cada índice criado ocupa espaço, entra no log, participa da escrita e precisa de manutenção. Então a pergunta vem do produto: qual tela precisa responder rápido? O extrato por conta? A busca por ID externo da transação? A conciliação por data? O índice bom vai reduzir páginas lidas sem transformar toda escrita num trabalho extra desnecessário.

## Manutenção: vacuum, compaction, checkpoints

E quando muita escrita e muita leitura acontecem juntas, o banco ainda precisa fazer manutenção. O trabalho do banco não acaba quando a query responde. Depois de várias escritas, as páginas ficam sujas, as versões ficam antigas, os índices maiores, e as estatísticas desatualizadas.

Alguns bancos chamam parte disso de *vacuum*; outros usam nomes como *compaction*, *purge* ou *analyze*. O nome vai mudar, mas esse conceito aparece em vários bancos: ele precisa limpar versões antigas que nenhuma transação pode enxergar mais, e também precisa atualizar estatísticas para estimar melhor quantas linhas uma query vai encontrar.

Isso explica por que performance pode piorar com o tempo mesmo com a query não mudando — a tabela mudou e o volume cresceu. E quando isso acontece, a resposta nem sempre é mexer na query; às vezes o banco precisa fazer trabalho de bastidor, como limpar sessões antigas, organizar as páginas, criar os checkpoints. Esse trabalho é uma manutenção comum, mas ele muda o tamanho do estrago quando tudo para de repente.

## Checkpoints e recovery

Depois de uma queda, o banco vai precisar responder uma pergunta: quais transações já tinham sido confirmadas? E os checkpoints são esses pontos de controle: de vez em quando, o banco grava a parte das páginas sujas no arquivo de dados e registra até onde chegou no log. Ele reduz quanto o log precisa ser lido depois de uma queda. Se o último checkpoint foi recente, o recovery tem menos coisa para refazer. Se o último checkpoint ficou muito para trás, o banco vai precisar reler mais logs antes de aceitar conexões de novo.

Quando o banco volta depois de cair, ele vai ler o log desde o checkpoint necessário. As transações confirmadas vão ser refeitas, se a página modificada ainda não tinha sido gravada no arquivo de dados; as incompletas são descartadas ou desfeitas. Esse processo é o chamado *recovery*. É por isso que o "commit OK" precisa significar alguma coisa real: se o banco respondeu que confirmou, ele precisa conseguir reconstruir aquilo depois de uma falha.

## Por que um banco não é só um arquivo

Agora dá para juntar tudo isso e responder uma pergunta: por que um banco não é só um arquivo? Um arquivo guarda bytes; essencialmente, um banco também guarda bytes, mas ele coloca regras em volta desses bytes.

Ele vai carregar as páginas na memória. Ele mantém índice. Ele grava log antes de responder "commit OK". Ele agrupa operações em transações. Ele controla concorrência com locks e snapshots. Ele valida regras do banco, como chave única e chave estrangeira. E ele consegue se recuperar quando alguma coisa cai no meio.

Então, quando uma aplicação chama, por exemplo, `db.save()`, ela está fazendo algo muito mais complexo do que jogar uma linha num arquivo: ela está pedindo pro banco seguir esse acordo entre memória, disco, log e regra de concorrência. E na maior parte do tempo o banco vai esconder essa complexidade de você — até que uma query fique lenta, ou um commit precise sobreviver a uma queda, por exemplo. São esses conceitos que explicam o problema.

É isso. Se curtiu, se inscreve e deixa um like — ajuda bastante o canal. Valeu.
