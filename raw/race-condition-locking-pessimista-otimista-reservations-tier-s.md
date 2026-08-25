# Race Condition: Locking Pessimista, Controle de Concorrência Otimista e Reservations (System Design para Entrevistas Tier S)

## Abertura — o exemplo do Vingadores Ultimato

Em meados de abril de 2019 a Marvel finalmente lança Vingadores Ultimato nos cinemas, um dos filmes mais esperados pelos fãs da franquia. Foram simplesmente milhares de pessoas só esperando o momento, passando os segundos, para poderem ser as primeiras a comprar os ingressos dos melhores lugares nos cinemas.

Agora imagina que você é uma dessas pessoas: assim que o site libera, você vai lá o mais rápido que consegue, escolhe o melhor lugar no cinema, e na hora de pagar você recebe uma mensagem de erro falando que alguém já reservou aquele lugar. Seria uma experiência extremamente frustrante, não seria?

Pois é, isso tem um nome: **race condition** — quando muitas pessoas estão tentando fazer a mesma ação ao mesmo tempo e o nosso servidor, o nosso banco de dados, não está preparado para lidar com isso.

E pior ainda seria se você conseguisse de fato comprar o seu ingresso, só que, chegando lá no cinema, você descobre que outras cinco pessoas compraram o mesmo lugar que você — e está lá certinho no bilhete delas o nome do lugar, o código, tudo certinho. Pois é, isso já aconteceu e acontece até hoje em sistemas que não estão preparados para lidar com race condition.

É exatamente sobre isso que vamos falar hoje: como sites gigantes de cinema, de show, lidam com isso, e as estratégias exatas que eles usam para garantir uma experiência perfeita na hora da compra para os usuários. Até o fim desse vídeo você vai aprender o que é locking pessimista, controle de concorrência otimista, as estratégias exatas que sites de companhias aéreas, de e-commerces ou de venda de ingressos usam para garantir que nenhum usuário vai comprar o mesmo lugar/o mesmo ingresso. E no final, os principais erros que as pessoas cometem quando estão trabalhando com race condition e não podem cometer durante uma entrevista.

Muito prazer, meu nome é Pedro Camaforte, sou desenvolvedor sênior, trabalho há quase dois anos para empresas do exterior. Esse é o sexto vídeo da nossa série sobre os principais conceitos de system design que caem nas entrevistas para empresas tier S — empresas que vão te pagar de R$20.000 a R$40.000 para cima. A playlist completa da série está na descrição.

## O que é race condition e por que ela acontece

### Exemplo 1 — duas pessoas comprando a mesma cadeira de cinema

Sistema de venda de ingressos de um cinema, onde dois usuários (Ana e Bruno) estão tentando comprar um ingresso para a cadeira A3. Os dois fazem uma solicitação ao servidor praticamente ao mesmo tempo — o usuário 2 demora 1 milissegundo a mais que o usuário 1.

1. Ambos verificam se a cadeira está livre (`SELECT` simples pelo código da cadeira). O banco responde que o status está disponível — para os dois.
2. Ambos avançam para pagamento e pagam.
3. O usuário 1, que está 1 milissegundo mais adiantado, marca a cadeira como indisponível. Só que, nesse meio tempo, o usuário 2 já pagou também — ou seja, duas pessoas pagaram pela mesma cadeira, porque quando verificaram ela estava livre.

Nesses milissegundos de diferença, o sistema deu um falso positivo: falou que a cadeira estava livre porque, de fato, estava — só que o usuário 1 já tinha pagado por ela e o usuário 2 acabou ficando sem. Ou ele recebe um erro dizendo que não conseguiu comprar, ou pior: os dois chegam no dia do cinema com o mesmo ingresso para a mesma cadeira, com os mesmos códigos, e um baita problema de suporte/confusão no balcão.

### Exemplo 2 — estoque de e-commerce sobrevendido

Dois usuários comprando de um e-commerce: usuário 1 quer comprar 17 itens, usuário 2 quer comprar apenas 2. Os dois fazem a solicitação de compra e o sistema verifica quantos itens há em estoque — vamos supor que há 20, e os dois leem esse valor **ao mesmo tempo**.

1. O sistema libera a venda para ambos (simplificando os outros passos que existiriam num sistema real).
2. O sistema atualiza o estoque: `estoque atual - quantidade comprada = novo estoque`. O usuário 1 atualiza primeiro: 20 - 17 = 3.
3. Dois milissegundos depois, o usuário 2 faz a mesma operação — só que ele tinha armazenado em memória o valor que buscou antes (20, não o 3 já atualizado pelo usuário 1). Ele calcula 20 - 2 = 18 e grava por cima: o estoque final marcado no sistema é 18.

O resultado real (17 + 2 comprados, partindo de 20) deveria ser 1 item em estoque, mas o sistema está marcando 18 — porque a segunda escrita simplesmente sobrescreveu a primeira, sem saber que ela existiu.

O problema aparece quando um terceiro usuário chega e quer comprar 8 itens: o sistema verifica o estoque, vê 18, libera a venda, o usuário paga — e depois recebe um e-mail dizendo que o item não está mais disponível. Dor de cabeça: desculpas ao cliente, estorno, ajuste de estoque. E imagine que não foi um usuário, foram 100 comprando desse "estoque fantasma".

Esse é o segundo padrão de problema causado por race condition: uma solicitação sobrescrevendo o que a solicitação anterior tinha feito, porque a operação foi feita de forma separada (ler em memória, depois escrever) em vez de forma atômica/indivisível.

Esses dois exemplos cobrem uns 90% dos casos de race condition mais comuns. Existem outros casos, mas o vídeo foca nesses dois para entender as estratégias de resolução.

## Estratégia 1 — Locking pessimista (Pessimistic Locking)

A primeira estratégia usa uma **transação** no banco: tudo que roda dentro dela acontece de forma atômica/indivisível — ou tudo roda perfeitamente, ou nada acontece (`ROLLBACK` desfaz tudo se algo falhar no meio; `COMMIT` confirma quando tudo deu certo).

Exemplo: Ana e Bruno querem comprar um ingresso para um show do Linkin Park. Ana chegou 1 milissegundo antes e inicia a transação primeiro:

```sql
BEGIN;

SELECT ingressos_disponiveis
FROM shows
WHERE show = 'Linkin Park'
FOR UPDATE;
```

O `FOR UPDATE` é a keyword que implementa o lock pessimista: ela diz ao banco "não deixe ninguém modificar essa linha enquanto eu estiver mexendo nela — só quando eu terminar e liberar é que a próxima pessoa poderá mexer". Até lá, qualquer outra transação que tente tocar essa linha fica esperando numa fila.

```sql
UPDATE shows
SET ingressos_disponiveis = ingressos_disponiveis - 1
WHERE show = 'Linkin Park'
  AND ingressos_disponiveis > 0;

COMMIT;
```

Quando Ana finaliza, ela conseguiu o ingresso. Bruno é liberado para tentar em seguida, mas se Ana pegou o último, o `UPDATE` de Bruno não afeta nenhuma linha (`ingressos_disponiveis > 0` falha) e ele não consegue comprar. É frustrante para Bruno, mas o sistema nunca cobra o pagamento dele por um ingresso que não existe mais — o que é bem melhor do que cobrar errado.

**Quando usar locking pessimista:** sob alta contenção (muitas pessoas/processos/automações disputando o mesmo recurso ao mesmo tempo) e principalmente quando a mera possibilidade de conflito sai muito cara (ex.: dano financeiro grande). O tradeoff é que travar a linha pode criar um gargalo/fila quando há muita gente batendo no mesmo recurso — vale avaliar se essa latência extra é aceitável em troca da segurança.

*(Observação do autor: os exemplos são simplificados para fins didáticos — num caso real existiriam muitas outras tabelas e verificações, mas o `FOR UPDATE` se aplica da mesma forma.)*

## Estratégia 2 — Controle de Concorrência Otimista (Optimistic Concurrency Control / OCC)

Mesma situação: Ana e Bruno leem no `SELECT` que há um ingresso disponível e seguem para pagamento — só que agora sem transação/lock explícito. Ana, 1 milissegundo à frente, faz o update primeiro:

```sql
UPDATE shows
SET ingressos_disponiveis = ingressos_disponiveis - 1
WHERE show_id = 'linkin-park'
  AND ingressos_disponiveis = 1; -- valor que ela leu no SELECT anterior
```

A Ana só consegue fazer o update porque a quantidade de ingressos disponíveis no banco ainda é exatamente igual ao que ela leu antes. Alguns milissegundos depois, Bruno tenta o mesmo update — só que a Ana já rodou a operação e zerou o estoque, então a condição `ingressos_disponiveis = 1` não é mais verdadeira: o update de Bruno afeta **zero linhas**, e ele não consegue comprar. Mesmo as duas operações acontecendo "ao mesmo tempo", só a Ana consegue — e o Bruno nunca chega a ter o pagamento processado.

Se essa mesma estratégia (um pequeno `AND estoque = <valor lido>` na query) tivesse sido aplicada no exemplo do e-commerce, a segunda escrita (usuário 2) teria falhado, porque o estoque já não seria mais 20 quando ele tentasse gravar — evitando toda a venda fantasma.

### A coluna `version`

Quando o cenário não é um contador simples como "ingressos disponíveis", mas qualquer linha de uma tabela com várias colunas que pode sofrer conflito, o padrão de mercado é adicionar uma coluna `version`, incrementada a cada modificação:

```sql
-- Ana leu version = 1
UPDATE shows
SET ingressos_disponiveis = ingressos_disponiveis - 1,
    version = version + 1
WHERE show_id = 'linkin-park'
  AND version = 1;
-- Bruno leu version = 1 também, mas quando tenta fazer o update
-- a version já está em 2 (Ana terminou primeiro) → 0 linhas afetadas → falha
```

Uma variação: em vez de checar `version = 1` (igualdade exata), checar `ingressos_disponiveis > 0`. Isso dá mais flexibilidade quando a regra de negócio permite — por exemplo, se ainda existiam 10 ingressos e cada um quer comprar 1, Bruno não falha só porque Ana comprou antes dele; ele falha só quando o contador realmente chegar a zero.

**Quando usar OCC:** quando os conflitos causados por race condition são **raros**. Como bônus, não há criação de filas (menor latência) — mas o tradeoff é que sob **alta contenção** (muita gente disputando o mesmo recurso), a maioria das tentativas falha e precisa de retry, o que pode ser ineficiente (ex.: 100 pessoas disputando, 99% precisam tentar de novo a cada rodada). Nesses casos de alta contenção, locking pessimista costuma ser melhor.

## Demonstração prática em código (PostgreSQL)

Setup: tabela `shows` (show do Linkin Park) e tabela `tickets` (cadeira A3). Simulação com 5 pessoas (via pool de conexões) tentando reservar a mesma cadeira simultaneamente.

**Sem `FOR UPDATE`:**
```sql
BEGIN;
SELECT reserved FROM tickets WHERE ...; -- verifica se já tem reserva
-- se reserved for diferente de null, ROLLBACK e retorna falso
UPDATE tickets SET reserved = true WHERE show_id = 'linkin-park' AND codigo = 'A3';
COMMIT;
```
Resultado: as cinco pessoas conseguem reservar a cadeira A3. No banco, quem "ganhou" foi simplesmente a última pessoa a escrever (Diego, no exemplo) — mas se houvesse lógica de e-mail de confirmação já disparada nesse meio tempo, todas as cinco pessoas (Ana, Bruno, Carla, Diego, Helena) teriam recebido ingresso para o mesmo lugar. Overbooking confirmado na prática.

**Com `SELECT ... FOR UPDATE`:**
Mesmo código, travando a linha no primeiro `SELECT`. Resultado: Helena foi a primeira a travar a transação, viu que ninguém tinha reservado ainda, e reservou para ela. Assim que ela dá commit, os próximos da fila fazem a verificação inicial, veem que Helena já reservou, retornam falso e nem chegam ao `UPDATE`. Lock pessimista funcionando como esperado — o mesmo valeria com 100 pessoas, não só 5.

**Controle de concorrência otimista, sem validação nenhuma:**
Mesmo problema do exemplo sem `FOR UPDATE`: todo mundo (Ana, Bruno, Carla, Diego, Helena) consegue "reservar" — overbooking.

**Controle de concorrência otimista, com coluna `version` e checagem no `WHERE`:**
Sem usar transaction (para provar que a técnica funciona também fora de uma transação — embora usar uma não atrapalhe). Todas as pessoas fazem o `SELECT`, leem a `version` em paralelo, guardam em memória, e no `UPDATE` checam show, código do assento **e** a `version` lida. Resultado: só Helena consegue reservar — foi a primeira a rodar o `UPDATE` de fato (o Postgres sempre serializa escritas concorrentes na mesma linha, nunca duas ao mesmo tempo), incrementando a `version` de 0 para 1. Todos os outros, ao tentar o update, descobrem que a `version` que leram não bate mais com a atual — `rowCount = 0` → tratado na aplicação como "alguém já reservou antes de você". Confirma que o OCC também funciona na prática.

## Estratégia 3 — Reservations (a mais recomendada para fluxos de usuário)

Com locking pessimista e OCC dá para corrigir os dois problemas de race condition, mas sempre alguém sai frustrado **depois de já ter preenchido todos os dados de pagamento** — a pior hora possível para descobrir que perdeu o lugar. Como melhorar essa experiência?

A resposta é a estratégia de **reservations**: mais conceitual que as anteriores (não é algo travado diretamente no banco), mas resolve exatamente esse problema. Ao clicar no assento, o usuário dispara uma chamada reservando aquele assento/ingresso por um tempo limitado (ex.: 5, 10 ou 15 minutos, com timer visível na tela). O status do ingresso passa de "disponível" para "reservado" nesse momento — e só quando o usuário de fato finaliza a compra (paga) é que o status vira "comprado" e o e-mail/PDF são enviados.

A diferença crucial: o momento de possível conflito passa a ser o clique no assento (reserva), não o pagamento. É muito melhor ter um conflito de reserva de assento (resolvido com um feedback instantâneo, "escolha outro") do que um conflito depois que o usuário já preencheu cartão de crédito e clicou em pagar.

### Desafio: o que acontece se o usuário desistir?

Se o usuário fecha o navegador sem finalizar, como o status volta de "reservado" para "disponível"?

**Solução simples (cron job):** um job que roda a cada X minutos (ex.: 5 ou 10) verificando reservas expiradas e revertendo o status para "disponível". Solução aceitável em entrevista para vaga júnior/pleno, mas com um problema: se a reserva foi feita às 14:00 e o cron rodou 1 segundo depois de expirar (14:09:59 num ciclo de 10 em 10 minutos), a próxima execução só acontece às 14:19:59 — ou seja, a reserva "de 10 minutos" pode durar quase 20 minutos na prática. Reduzir o intervalo do cron ajuda, mas tem limite: rodar de 5 em 5 segundos, por exemplo, pode disputar recurso demais com o banco em alta escala (ex.: plataformas do porte de Ticketmaster ou companhias aéreas globais).

**Solução mais elegante (locking distribuído com Redis):** o status do ticket no banco fica só "disponível" ou "ocupado" — quem controla o estado "reservado" é o próprio Redis, via:

```
SET show:{showId}:seat:{seatId} {userId} NX EX 600
```

- `NX` ("not exists") — só seta a chave se ela ainda não existir. Se Ana e Bruno tentam reservar ao mesmo tempo, quem conseguir rodar o `SET` primeiro trava a chave; o outro recebe erro/falha porque a chave já existe.
- `EX 600` — expira automaticamente em 600 segundos (10 minutos). O Redis expira a reserva nativamente, sem cron job e sem atraso — não é preciso se preocupar com isso manualmente.

Para exibir ao usuário quais assentos ainda estão disponíveis, o servidor cruza os dados do banco (disponível/ocupado) com as chaves ativas no Redis (reservado), excluindo os reservados da lista — operação tranquila em memória, já que um show nunca tem centenas de milhares de assentos simultâneos.

### E se o Redis cair?

Pergunta citada como recorrente em entrevistas (relato do autor aprendendo essa mesma estratégia com um ex-step engineer da Meta): não é preciso depender só do Redis — pode-se adicionar uma segunda camada de garantia no banco. Fluxo: o lock distribuído via Redis cuida das reservas no caminho feliz (ninguém mais participa da compra enquanto o Redis está de pé). Se o Redis cair e voltar depois de, digamos, 60 segundos (tempo de subir uma nova instância), aplica-se um **locking pessimista** (`FOR UPDATE`) no banco para esses 60 segundos de janela — garantindo que, mesmo nesse intervalo, só uma pessoa consiga de fato completar a compra. A experiência do usuário piora um pouco nesse intervalo excepcional, mas isso é aceitável na prática (o autor sugere que esse tipo de trade-off, "acontecer uma vez por ano por 60 segundos", normalmente é validado com o time de produto) — e mencionar esse edge case numa entrevista é visto como sinal de profundidade.

**Tradeoff da estratégia de reservations:** mais complexidade de implementação (cron job ou Redis como componente adicional) do que simplesmente colocar um `FOR UPDATE` no banco. Mas para fluxos que dependem fortemente da experiência do usuário (e-commerce com estoque limitado, passagens aéreas, compra de ingressos online), o ganho de experiência compensa a complexidade extra — o custo de usuários frustrados/perdidos pode sair muito mais caro.

## Framework de decisão

- Conflitos muito frequentes / alta contenção → **locking pessimista**; senão → **controle de concorrência otimista**.
- É um fluxo de usuário (não só back-end/automação) → considerar e preferir **reservations** na quase totalidade dos cenários.

## Erros comuns que eliminam candidatos em entrevista

1. **Não perceber que existe risco de race condition.** Diante de um cenário com potencial de concorrência, dizer simplesmente "eu faço um update direto" já é red flag — o entrevistador não vai apontar o problema para você; é preciso ter a sensibilidade de identificá-lo sozinho.
2. **Sair "tacando Redis" para tudo**, criando lock distribuído onde um simples `FOR UPDATE` ou uma checagem otimista já resolveria — aumentar complexidade onde não é necessário também é red flag.
3. **Nunca abrir uma transação, travar uma linha do banco, e no meio da transação fazer chamadas para APIs externas** (ex.: gateway de pagamento). Isso trava a linha por segundos, forma fila enorme de espera. A ordem correta: abrir a conexão/transação, fazer o que precisa ser feito no banco, fechar a transação — e só depois conversar com APIs externas/operações lentas. Cometer esse erro é motivo de eliminação imediata em entrevista.

## Teaser do próximo vídeo

Cenário: o usuário faz uma solicitação que dispara várias operações — verificar estoque, verificar cartão de crédito, verificar fraude, processar pagamento, entre outras (ex.: 10 etapas) — e uma dessas etapas críticas falha **depois** que o cartão do usuário já foi cobrado. Como desfazer o que já aconteceu? Esse é o tema do próximo vídeo da série.
