# Shopify Trocou Redis por MySQL e Segurou US$ 5,1 Milhões por Minuto na Black Friday

**Fonte:** Transcrição de vídeo (YouTube) — canal de tecnologia, análise de artigo de engenharia da Shopify
**Idioma original:** Português

---

## Introdução

A Shopify jogou o Redis fora e substituiu por MySQL — e mesmo assim escalou. Não é sistema de startup nem de empresa pequena brincando de arquitetura: é o e-commerce que segurou **US$ 5,1 milhões por minuto** na Black Friday de 2025. A Shopify processa mais transações por segundo do que a maioria dos sistemas processa na vida inteira.

Este vídeo é uma análise de um artigo de engenharia da Shopify sobre o redesenho do sistema de reserva de estoque em cima do MySQL.

---

## O Problema Clássico de Concorrência

O problema é antigo: dois compradores entram no e-commerce, querem o mesmo tênis, só tem uma unidade em estoque, e os dois clicam em "finalizar compra" ao mesmo tempo (mais comum do que parece).

Se o sistema errar para um lado:
- **Os dois pagam pelo mesmo item** → a loja cancela um pedido → cliente furioso → reclamação pública, possível disputa judicial.
- **O sistema recusa a venda por engano** (falso esgotado) → venda perdida → o dono da loja fica insatisfeito com a Shopify.

Escala do problema: **14% dos e-commerces americanos** rodam na Shopify. Qualquer bug bobo de concorrência se multiplica de forma absurda nesse volume.

---

## Arquitetura Antiga: Redis + MySQL

A arquitetura anterior resolvia concorrência com **Redis** como camada de reserva rápida — pensa nele como um caixa expresso: ótimo para operações simples e rápidas, mas trava quando você precisa fazer qualquer ação fora do fluxo padrão (trocar item, cancelar, etc.).

Fluxo:
1. O item era **reservado no cache (Redis)**.
2. O **estoque de verdade** vivia no **MySQL**, que era a fonte única de verdade.
3. Na hora do pagamento, o sistema precisava **atualizar o MySQL** e **limpar o Redis** — duas escritas em dois sistemas diferentes, sem garantia atômica entre elas.

É como fazer um Pix: você transfere, debita da sua conta, mas o outro lado não confirma o recebimento na hora — fica uma janela de incerteza. Aqui, dependendo da ordem de execução, o sistema ou vendia sem dar baixa no estoque, ou dava baixa e o item ficava "fantasma", bloqueado no banco sem motivo aparente.

---

## Primeira Solução: SKIP LOCKED

A Shopify usou uma feature do MySQL 8+ (existe desde 2018) que pouca gente usa: **`SELECT ... FOR UPDATE SKIP LOCKED`**.

### Modelo antigo vs. novo

- **Modelo antigo:** uma coluna `estoque` numa tabela, tipo uma "placa" que é atualizada: "10 unidades" → compra 1 → "9 unidades".
- **Modelo novo:** cada unidade de estoque vira **uma linha real na tabela**. 10 unidades em estoque = 10 linhas no banco. Reservar 3 = pegar 3 linhas específicas e movê-las para o carrinho, tudo na mesma transação — ou tudo acontece, ou nada acontece.

`SKIP LOCKED` funciona como um funcionário de estoque desenrolado: ele olha a prateleira, se uma caixa já foi pega por outro processo ele **pula** para a próxima disponível, sem fila, sem espera, sem travamento.

### Escalando o modelo por linha

Para produtos com estoque muito grande (ex: 1 milhão de unidades, múltiplos locais), a Shopify não criou 1 milhão de linhas de uma vez. Em vez disso:

- Criaram um **pool limitado a 1.000 linhas por produto/local**.
- Conforme o pool esvazia, o sistema **reabastece automaticamente** (útil em picos como Black Friday).
- Adicionaram uma **trava que executa um processo de reposição por vez**, evitando que múltiplos "repositores" dupliquem linhas no pool simultaneamente.

---

## Os Três Problemas de Banco que Precisaram Corrigir

Antes de chegar na solução estável, a equipe bateu de frente com três problemas clássicos de banco relacional:

1. **Chave primária mal desenhada** — gerava travamento duplo (deadlock) desnecessário.
2. **Configuração padrão do MySQL bloqueando "gaps"** — por padrão, o MySQL trava até os espaços vazios ao redor da linha sendo lida (gap locking), como um segurança de condomínio que fecha o corredor inteiro em vez de só o apartamento.
3. **Operações executando em ordens diferentes entre si**, gerando contenção cruzada.

Corrigidos os três, o `SKIP LOCKED` passou a funcionar como esperado.

---

## O Gargalo Real Não Era a Query

Mesmo com as travas otimizadas e as operações agrupadas, o sistema bateu num teto: CPU baixa, latência ok, mas **não escalava**. Sintoma de "motor bom, mas o carro não passa de 80 km/h" — o problema não estava numa query isolada, estava em algum lugar do caminho inteiro da requisição.

Esse é o tipo de problema que uma IA não resolve otimizando uma query individual: ela pode deixar a query "bonitinha", mas o sistema continua travado, porque o gargalo não é sintático, é sistêmico.

### O que a equipe fez

Em vez de otimizar queries isoladas, **etiquetaram cada operação SQL** por origem (ex: "esta é do checkout", "esta é da reserva") e mediram **quanto tempo cada parte segurava a conexão do banco** — não qual query era lenta, mas **quem estava monopolizando conexões**.

Essa é uma abordagem de engenharia, não de ferramenta: alguém precisa saber que pergunta fazer. Uma IA sozinha não faz essa pergunta porque não tem o contexto de negócio/arquitetura para formulá-la.

### A descoberta contraintuitiva

As reservas de estoque **não eram** o gargalo. O problema real estava em **partes mais antigas do checkout**, que seguravam conexões abertas por tempo desproporcional — como um vizinho sem noção que estaciona na sua vaga. As reservas foram só o gatilho que expôs o problema, não a causa.

---

## Resultados

Depois de limpar o caminho do checkout e revisar a configuração padrão do MySQL (que "ninguém mexia há anos"):

- **50% menos leituras**
- **33% menos transações**
- **CPU do banco abaixo de 50%** nos picos de Black Friday, com folga para escalar

---

## O "Grande Rollback"

O vídeo conecta o case da Shopify a uma teoria recorrente do canal: o **"Grande Rollback"** — a observação de que empresas estão voltando para tecnologias que a indústria havia decretado "ultrapassadas". Em processos seletivos, sugerir abandonar o Redis em favor do MySQL puro ainda pode te desclassificar na hora, dependendo de quem entrevista — mas a prática de mercado está indo na direção oposta ao dogma.

O artigo da Shopify referencia o case da **37signals** (Basecamp) — empresa que saiu do cloud para hardware próprio e passou um ano provando que "você provavelmente não precisa do que acha que precisa". O produto mencionado é o **Solid Queue**: uma fila de processamento deles que roda inteiramente sobre banco relacional — sem Redis, sem Kafka, sem broker externo.

A Shopify, operando em escala de US$ 5,1 milhões por minuto, chegou à mesma conclusão.

### A crítica não é ao Redis

O ponto não é que Redis seja ruim — ele resolve problemas reais. O ponto é que Redis virou uma **resposta automática**: "tem problema de concorrência? Bota Redis". O `SKIP LOCKED` existe desde 2018; a Shopify só o usou quando alguém internamente parou para questionar por que a empresa não usava a solução que já tinha disponível no próprio banco. Não foi uma IA que sugeriu isso — foi uma pessoa questionando uma decisão aceita e normalizada havia anos.

### O custo real de manter dois sistemas

Manter Redis e MySQL em paralelo, sincronizados, tem um custo que vai além de infraestrutura ("Redis é barato"): custo de depuração de bugs entre sistemas que não compartilham transação, custo de operar/monitorar/replicar um cluster Redis separado, e custo mental/cognitivo da equipe. Quando a Shopify foi forçada a repensar, descobriu que o MySQL, bem desenhado, fazia o serviço tão bem ou melhor — porque reserva e estoque passam a viver no mesmo banco, na mesma transação.

---

## Conclusão Prática

Para quem lida com concorrência no dia a dia (filas de job, reserva de recursos, etc.), o conselho do vídeo é: **questionar decisões de stack aceitas por inércia**, sem ser inconveniente sobre isso. Perguntar "por que estamos usando X aqui?" antes de assumir que a resposta padrão (Redis, fila externa, etc.) é a única opção.

`SKIP LOCKED` também funciona no **PostgreSQL desde a versão 9.5** — quem já usa Postgres pode não precisar adicionar nada à stack para resolver o mesmo tipo de problema de concorrência.
