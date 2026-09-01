# Event Sourcing — Conceito, Prós, Contras e Cases de Mercado

> Transcrição de vídeo (canal focado em arquitetura de software, apresentador se dirige ao público como "ARQ" — abreviação de "arquiteto"). Tema: Event Sourcing.

## Introdução

Hoje a gente vai falar de um tema que é simplesmente obrigatório para qualquer arquiteto de soluções ou de software: Event Sourcing. A gente vai falar de uma maneira extremamente simples, com exemplos na lousa, e você vai sair desse conteúdo sabendo exatamente o que é, os pontos fortes e fracos desse padrão, e também com cases reais de mercado — quando aplicar, quando não aplicar.

## O que é Event Sourcing

Event Sourcing é um padrão de projeto que visa, ao invés de você persistir diretamente no banco de dados o estado atual de cada objeto/dado de cada domínio da sua aplicação, persistir toda a trajetória que levou aquele objeto a chegar àquele estado. Nesse contexto, cada evento que é executado você vai persistindo no banco, para você conseguir obter depois todo esse histórico de informações — tudo que aconteceu até o objeto chegar àquele estado.

Estado de objeto pode ser N coisas. Por exemplo: um cliente que no primeiro momento é prospect, depois vira cliente, e tem diversos estados dentro da base durante o tempo em que é cliente daquela empresa. Pensando em um sistema de telecomunicações/telefonia, o cliente pode estar em vários estados: ativo (pode receber e fazer ligações), inativo, inadimplente (só pode receber, não pode fazer ligações), etc. Vários sistemas podem ter necessidade de tratar estados de formas diferentes.

## O que é um evento

Um evento é a ação que levou um dado objeto do sistema a receber aquele estado. Por exemplo: um comando foi executado e registrou o cliente na base — a ação de cadastrar o cliente na base é um evento. A ação de obter informações desse cliente, a ação de transformar o estado desse cliente de A para B — tudo isso são eventos: as ações que acontecem e mudam o estado do objeto final.

Em um sistema financeiro onde há saldo e extrato, a mudança do valor do saldo do cliente varia com os lançamentos na conta corrente. Essas alterações feitas diretamente na tabela de lançamentos são as que refletem no saldo — e ter todo esse histórico registrado, em vez de atualizado, é fundamental, uma das chaves do padrão Event Sourcing.

### Regra fundamental: só inserts

Para Event Sourcing funcionar, ele precisa trabalhar somente com **inserts** — nunca com updates, nunca com deletes. É sempre inserção. Eventualmente o registro antigo muda para o estado inativo, e um novo registro passa a receber o status de ativo. É assim que funciona.

## Para que serve o Event Sourcing

Serve basicamente para duas coisas:

1. **Capacidade de desfazer** — em qualquer momento, você consegue voltar a um estado anterior e reprocessar aquele objeto a partir daquele momento, não importa quando isso aconteceu. A ideia e o conceito por trás do Event Sourcing é que você seja capaz de reprocessar.
2. **Histórico** — para auditoria, para log, ou para qualquer outra finalidade de troubleshooting: você consegue olhar para tudo que aconteceu até o momento que levou o objeto ao estado em que está atualmente.

## Exemplo prático — tabelas de extrato e saldo

Esse padrão (segundo os posts do Martin Fowler, um dos fundadores desse padrão) funciona assim, num exemplo bem comum no mercado:

**Tabela de extrato**: tem a data em que foi inserido o registro, o tipo (débito/crédito, ou uma ação de desfazimento), o valor do lançamento (10, 20, 30, 40 reais), uma descrição, um campo `enabled` (ligado/desligado), a data em que o estado foi alterado (`state_date`), e um `account_id` que liga com a tabela `account`.

**Tabela `account`**: é a tabela de conta corrente, a ligação entre tudo no sistema — tem o id do cliente e o id da própria conta corrente, desacoplando cliente de conta corrente/extrato. Isso, inclusive, é ótimo para LGPD: se precisar apagar tudo do cliente, na tabela de extrato só existe o id da conta, o que já resolve boa parte do problema.

**Tabela de saldo**: tem ligação com `account`, tem o `state_date`, o `enabled`, o valor do saldo daquele momento, e o id da própria tabela.

Tanto a tabela de extrato quanto a de saldo não sofrem update nem delete — só insert.

- Na tabela de **extrato**, os registros normalmente são sempre válidos: um lançamento de algo que deu certo (uma compra bem-sucedida vira um débito, um salário pago vira um crédito) é sempre um insert. O que pode acontecer é um lançamento negativo — alguém fez um depósito errado, um pagamento errado, uma fraude — e aí se lança embaixo um outro registro de estorno/desfazimento. Ainda assim, não se muda o estado do registro anterior; por isso existem `state_date` e `enabled`: pode haver uma ação manual, por motivo legal (ex.: um lançamento que não pode nem aparecer na fatura), onde se faz uma deleção lógica mudando `enabled` para falso.
- Na tabela de **saldo**, diferente do extrato, você tem um registro por vez com o valor consolidado — nunca se faz update, sempre inserts, e a única coisa que se atualiza é o `enabled` do registro anterior para falso, mantendo só um registro com `enabled = true`. Assim você tem sempre o último valor atualizado e todo o histórico por trás.

Muitas vezes, se você só precisa de histórico das alterações, ao invés de aplicar Event Sourcing na sua plenitude, você pode simplesmente alterar seu modelo de dados para trabalhar só com insert e update do estado anterior para desligado — conseguindo rastro de todas as alterações sem aplicar o padrão como um todo.

## Aplicando o padrão como um todo — arquitetura com streaming

Para aplicar o padrão por completo, você precisa registrar o evento como um todo — a ação que fez a alteração acontecer.

Arquitetura típica: APIs públicas (às vezes front-ends acessam direto) orquestram chamadas a microsserviços. Esses microsserviços lançam dados/eventos numa ferramenta de streaming (pode ser tratada como black box — filas, streaming de eventos; MQ serve para isso também). À medida que as ações vão sendo lançadas na streaming, outros microsserviços que estão ouvindo a fila pegam o objeto, tratam/enriquecem ele, e devolvem para a fila em um outro estado. É o padrão de microsserviços coreografados ouvindo a fila, pegando o objeto, trabalhando nele e passando o bastão adiante (ou persistindo).

É aqui que entra o Event Sourcing: um microsserviço (ou "Betty", como o apresentador chama) fica responsável por registrar tanto no Kafka (ou outra ferramenta de streaming de grandes volumes de dados não transacionais — não precisa ser Kafka necessariamente) quanto num banco SQL transacional (SQL Server, Postgres, Oracle, etc.) — pegando cada mudança/alteração de estado e registrando tanto no banco de eventos quanto no SQL. Tipicamente isso é o próprio objeto de domínio serializado, que depois pode ser desserializado para reproduzir exatamente o evento que aconteceu.

Um outro componente faz o caminho inverso: pega o evento do banco e lança de volta na fila, no estado daquele momento passado, reproduzindo exatamente o que aconteceu — os microsserviços then executam as ações para levar o objeto ao novo estado, exatamente como tinha acontecido no passado. Isso permite reproduzir um problema, entender por que aconteceu, para fins de auditoria ou troubleshooting.

## Prós

1. **Reprodutibilidade** — se aplicado corretamente (testado, evento serializável e desserializável), você consegue reproduzir exatamente o que aconteceu com o objeto, a ponto de poder dropar o banco de dados inteiro e reconstruir tudo a partir dos eventos lançados na fila.
2. **Auditoria** — auxilia (e muito) em processos de auditoria, como CMMI, onde é preciso ter todos os registros de tudo que aconteceu, quando e por quê, detalhadamente.
3. **Troubleshooting** — ajuda bastante a rever o que aconteceu no código, encontrar o momento exato do erro e reproduzi-lo.

## Contras

1. **Volume de dados** — eleva muito o volume de dados armazenado no banco/Kafka/banco transacional, o que traz mais consumo de infraestrutura: mais capacidade de backup (mais caro), mais processamento do banco (mais registros para percorrer até o registro exato).
2. **Complexidade de código** — exige mais componentes arquiteturais, que podem falhar em vários pontos, tornando o troubleshooting mais complicado. É preciso muito log de tudo que acontece (não só dos eventos, mas de qualquer tipo de exceção/erro), tratamento de exceção robusto, para garantir que não haja impacto operacional.
3. **Maior tempo de desenvolvimento e manutenção** — código mais complexo, mais coisas com que se preocupar, portanto mais caro e mais lento de manter.

## Cases reais de mercado onde Event Sourcing foi aplicado

1. **Padrão Saga** — ao trabalhar com microsserviços e precisar garantir um contexto transacional sem ter uma transação garantida de banco, aplica-se o padrão Saga, que tem tudo a ver com Event Sourcing. Independente do case, para aplicar Saga é preciso aplicar Event Sourcing (na totalidade ou o conceito dele) para as transações, de forma a poder desfazer caso haja algum problema no fluxo.
2. **Opt-in / LGPD** — ter histórico de quando o cliente deu ou retirou consentimento (ex.: "não quero mais notificações de parceiros") é fundamental. Também é necessário propagar esse estado para parceiros (cobrança, marketing etc.), que precisam seguir o ativado/desativado do opt-in — Event Sourcing é perfeito para broadcast dessas mudanças com garantia de que o pedido foi registrado, quando e como aconteceu. Isso tende a ficar cada vez mais relevante com problemas legais relacionados à LGPD.
3. **Auditoria de segurança em operações críticas** — operações que envolvem financiamento, transferência de dinheiro etc. O apresentador relata ter precisado aplicar Event Sourcing depois de uma empresa sofrer uma auditoria sem ter os dados necessários; a solução sugerida foi Event Sourcing para operações financeiras.
4. **Faturas e extratos** — faturas de cartão de crédito, extratos bancários, faturas de operadoras de telecomunicações/TV a cabo (controle de consumo, pay-per-view, dados, voz, pacotes de telefone). Empresas de telecomunicações sofrem fiscalização da Anatel e precisam justificar rapidamente o porquê de cada estado/lançamento do cliente. O apresentador afirma que, apesar de raríssimas empresas de telecom aplicarem esse padrão corretamente, as duas que aplicaram conseguiram justificar facilmente à Anatel o porquê de cada lançamento e estado do cliente.

## Conclusão — não existe bala de prata

Não existe bala de prata em arquitetura — a resposta padrão de arquiteto é "depende". É preciso colocar na balança os prós e os contras, considerar o trade-off todo antes de decidir usar Event Sourcing, porque escolher errado custa caro: mais esforço de desenvolvimento, mais componentes arquiteturais. Não é para aplicar em tudo dentro de uma solução — aplicar onde faz sentido, como na parte financeira/transacional onde é realmente necessário.

O vídeo também recomenda assistir a um conteúdo anterior do canal sobre CQRS (um hangout feito com outros arquitetos do mercado), por ter tudo a ver com Event Sourcing.
