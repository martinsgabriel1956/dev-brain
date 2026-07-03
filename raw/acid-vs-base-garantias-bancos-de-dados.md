# ACID vs. BASE: As Garantias que os Bancos de Dados Nos Dão

**Tema:** Comparação entre as garantias ACID (bancos relacionais/SQL) e BASE (bancos não relacionais/NoSQL) — o que cada uma significa, o tradeoff entre corretude e escalabilidade, e quando usar cada abordagem
**Data de captura:** 2026-07-03

---

## Transcrição

Vamos lá: garantias ACID são garantias que os bancos de dados dão pra gente, né — bancos de dados SQL, no SQL. Vamos discutir aqui um pouco os tradeoffs, vamos discutir o que que é isso.

Por favor, eu não quero ter que te convencer que isso aqui é importante, tá. Eu espero que você saiba que isso aqui é mais importante do que qualquer conteúdo de IA que você tá vendo agora. Eu espero que eu não precise fazer o trabalho de convencer as pessoas de que é importante elas entenderem como os sistemas que elas fazem funcionam, né — tipo, não deve ser importante precisar convencer um engenheiro de que ele tem que entender o que faz uma ponte ficar em pé. Eu acho que isso é meio básico.

## O que é ACID

Vamos entender os nomes primeiro, e depois a gente explica um por um.

- **A — Atomicidade** (*atomicity*)
- **C — Consistência** (*consistency*)
- **I — Isolamento** (*isolation*)
- **D — Durabilidade** (*durability*)

### Atomicidade

Uma transação é atômica — átomo, indivisível, aquela unidade que não pode ser dividida (na verdade o ser humano já dividiu o átomo, mas enfim). Isso significa que não tem como acontecer meia transação: precisa acontecer a transação inteira.

Imagina o seguinte: eu vou transferir R$100 para alguém. Na minha conta vai ter menos 100, e na conta da outra pessoa vai ter mais 100. O que a atomicidade diz é: vai ser subtraído 100 da minha conta e adicionado 100 na conta da outra pessoa; caso alguma dessas operações não funcione, a operação inteira vai ser cancelada. Ela precisa passar por inteiro, ou ela não vai passar. Isso é atomicidade — uma das garantias do banco de dados relacional. Você pode confiar que, a não ser que ocorra uma falha gravíssima de hardware, não vai existir o caso em que uma transação passa pela metade, que uma transação é comitada pela metade sem que isso seja o seu intuito explícito.

### Consistência

Consistência significa que o banco de dados vai passar de um estado válido para outro estado válido.

Quando a gente tem um banco de dados SQL, a gente pode criar restrições (*constraints*) — garantias como "meu estoque não pode ser negativo". Isso seria traduzido numa regra na criação da tabela de estoque: um *constraint* que determina que o estoque não pode ser negativo.

Consistência significa que em todos os momentos o banco de dados vai estar internamente consistente — as regras que eu defini não vão ser quebradas. Se eu tenho a obrigação de que uma loja tenha pelo menos um usuário dono dela, e um usuário pode ter N lojas, nunca vai existir no meu banco de dados o caso de uma loja sem usuário. Isso não vai acontecer, porque não seria internamente consistente. Essa é uma garantia que os bancos de dados nos dão.

### Isolamento

Uma transação não vai afetar a outra transação. Imagina duas pessoas tentando comprar o último produto em estoque: essas transações não vão afetar uma a outra, mas como as duas estão tentando comprar o último produto, uma deve passar e a outra deve falhar. Não deve haver interferência de uma transação em outra transação que não tem nada a ver com ela.

Atenção: isso não significa que, se eu rodar `UPDATE accounts SET balance = 0 WHERE id = 123` e, em paralelo, rodar outra transação que altera esse mesmo saldo para 15, uma vai "esperar" a outra de forma amigável. As duas rodam; uma não interfere tecnicamente na outra, mas o valor final do saldo vai ser ou 0 ou 15 — não os dois. Isolamento não significa que operações concorrentes sobre o mesmo dado não competem; significa que o resultado final é consistente com uma ordem serial válida das transações.

### Durabilidade

Se o banco de dados disse que algo foi executado com sucesso, foi salvo com sucesso, e está feito. Se eu tirar o hardware do banco de dados da tomada (e não aconteça nenhuma falha física), quando eu ligar de novo os dados vão estar lá, armazenados. Se o seu sistema der crash, você não vai perder o que já foi salvo.

Essas são as garantias ACID.

## O que é BASE

BASE é a alternativa — as garantias mais comuns em bancos de dados não relacionais. Importante: bancos NoSQL não *sempre* vão te oferecer exatamente essas garantias — é que é comum a gente esperar, e comum tentar montar um sistema que tende a isso. Exemplos: Cassandra, MongoDB, DynamoDB.

- **BA — Basically Available** (basicamente/geralmente disponível)
- **S — Soft State** (estado fluido)
- **E — Eventual Consistency** (consistência eventual)

### Basically Available

O sistema vai tentar responder mesmo se partes dele estiverem falhando. Um banco relacional não pode te oferecer isso da mesma forma, porque se parte dele estiver falhando, ele não consegue garantir atomicidade nem as outras garantias ACID.

### Soft State (estado fluido)

O estado interno do banco de dados pode ser alterado mesmo sem que haja um novo input explícito, porque existe uma sincronização entre réplicas diferentes — pode existir um tempo de propagação entre elas. Não existe a mesma garantia de estado interno fixo que o ACID oferece.

### Eventual Consistency (consistência eventual)

Você vai ter cópias (réplicas) dos dados em vários lugares. Por exemplo, o DynamoDB permite escalar para o mundo inteiro do zero — isso significa necessariamente ter réplicas dos dados.

Imagina três réplicas. Eu atualizo meu saldo para 150 numa delas, mas nas outras réplicas o saldo ainda está em 80. Existe um breve período em que esses dados ainda não foram propagados para as outras réplicas — ou seja, é possível (não comum, mas possível) que eu atualize meu saldo para 150, faça um `GET` logo em seguida, e leia 80 mesmo já tendo atualizado para 150, porque nem todas as réplicas foram atualizadas ao mesmo tempo.

Isso é um problema dependendo do sistema que você está montando. Se a gente tá falando do número de likes no seu post do LinkedIn, não tem o menor problema esse tempo de propagação.

## ACID vs. BASE: o tradeoff

Bancos de dados relacionais entregam **corretude** e **consistência forte** — não consistência eventual. Usando de novo o exemplo do saldo bancário: você pode forçar a garantia de que, a partir do momento que você escreveu ali, toda vez que esse saldo for lido ele já vai estar consistente (embora, como já foi falado várias vezes no canal, você não deveria armazenar saldo direto no banco de dados, a não ser que seja um banco só de leitura — mas isso é outro assunto).

Essas garantias ACID forçam o banco a seguir regras rígidas. Pensa da perspectiva do banco de dados: imagina que eu quero garantir que não posso ter e-mail duplicado. Um usuário cria a conta com `augusto@mail.com`; outro tenta criar a conta com o mesmo e-mail. Como o banco garante essa regra? Ou ele olha usuário por usuário para garantir que o e-mail não está duplicado antes de escrever a linha nova, ou ele precisa construir um índice (provavelmente um *hash index*) e consultar esse índice para saber se o e-mail já existe. Ou seja: essa garantia de consistência tem uma contrapartida de **performance** — mais dificuldade para escalar para milhões de usuários com a mesma facilidade.

As garantias BASE, por sua vez, nos dão muito mais **disponibilidade** (*availability*). Se eu quero escrever um e-mail novo e uma das partições, *shards* ou réplicas não estiver funcionando, num banco ACID eu talvez tenha que recusar a transação porque não consigo garantir as outras propriedades. No BASE, tanto faz: você pode aceitar a transação e sincronizar internamente depois. Se rolar um problema de consistência temporário nessa regra de e-mail único, ninguém te garantiu que aquilo seria sempre consistente. Isso nos dá escalabilidade e flexibilidade melhores no geral.

Naturalmente, tem coisas mais adequadas para corretude forte, e coisas em que dá para "dar aquele jeitinho" — não faz tanta diferença se não estiver perfeitamente correto o tempo todo.

### Um disclaimer da prática

Na prática já vi bancos relacionais sendo usados para coisas que não precisavam disso, e bancos não relacionais sendo usados até em instituições de pagamento. O que foi descrito acima é o "academicamente bonito" de se falar, não necessariamente o que sempre acontece na prática — principalmente quando você começa a escalar muito, faz otimizações "bizarras" e larga mão de um Postgres porque o sistema passa a funcionar de um jeito totalmente diferente de um sistema pequeno (por exemplo, sincronizando DynamoDBs em regiões diferentes). Nesse ponto, essas regras de bolso já não se aplicam tanto — o foco vira disponibilidade e escalabilidade, e o resto "se ajeita depois".

## Quando usar cada abordagem

**Quando você geralmente quer consistência forte (ACID):**
- Pagamentos e bancos
- Compras, lojas, estoque
- Tickets (ex.: assentos de avião) — coisas que se traduzem em algo físico/palpável no mundo real e que precisam estar corretas (não posso vender um assento a mais no avião que não existe — embora companhias aéreas já tenham feito isso)

**Quando você geralmente quer escalabilidade gigantesca (BASE):**
- Rede social — se o número de likes ficar um pouco inconsistente, não faz diferença nenhuma
- Analytics no geral
- Logs — perder um log ou ele ficar um pouco fora de ordem geralmente não é problema; cada requisição logada é independente das outras
- Cache — é naturalmente algo efêmero, tanto faz, vai ser limpo/deletado de qualquer forma
- Sistemas de recomendação — não faz diferença se o sistema não contabilizou "agora" que você deu like num filme; ele vai contabilizar daqui a pouco

## Conclusão

Esses são os conceitos de ACID e BASE — as garantias que bancos de dados relacionais e não relacionais nos dão, e o tradeoff central entre corretude/consistência forte de um lado e disponibilidade/escalabilidade do outro.

---

## Notas de contexto (para ingestão na wiki)

- **Origem:** transcrição de vídeo patrocinado (menção a "Abacus.ai" como patrocinador — ferramental de IA com assinatura mensal, geração de vídeo, IDE e CLI incluídos) sobre as garantias ACID vs. BASE em bancos de dados.
- **Autor:** aparenta ser o mesmo criador de conteúdo por trás de outras transcrições já ingeridas no wiki sobre bancos de dados e system design (menciona um curso de System Design com lançamento previsto para junho de 2026, mirado em devs pleno–sênior).
- **Temas centrais:** ACID (Atomicidade, Consistência, Isolamento, Durabilidade) em bancos relacionais (Postgres, MySQL, Oracle, SQL Server, SQLite); BASE (Basically Available, Soft State, Eventual Consistency) em bancos não relacionais (Cassandra, MongoDB, DynamoDB); tradeoff entre corretude/consistência forte e performance/disponibilidade/escalabilidade; exemplo do e-mail único via índice hash como custo de garantir consistência; exemplo de saldo bancário e réplicas para ilustrar consistência eventual; disclaimer de que a escolha na prática nem sempre segue a regra "acadêmica" (bancos relacionais usados onde não precisava, NoSQL usado em pagamentos).
- **Menções de produtos/tecnologias:** PostgreSQL, MySQL, Oracle, SQL Server, SQLite, Cassandra, MongoDB, DynamoDB, Abacus.ai (patrocinador).
- **Promoção:** menção a curso de System Design do próprio autor, com lista de espera, lançamento em junho de 2026, mirado em desenvolvedores pleno para sênior — não essencial ao conteúdo técnico do vídeo.
