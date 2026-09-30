# CQRS — Desbalanço entre Leitura e Escrita, Banco de Leitura e Sincronização por Eventos

Fonte: transcrição de vídeo (autor/canal não identificados na transcrição), já em português — sem necessidade de tradução. Transcrição automática colada pelo usuário; foram adicionados apenas pontuação, parágrafos e títulos de seção, e o texto foi limpo de erros de reconhecimento de fala. O vídeo usa um diagrama na tela (cliente → comandos → command bus → banco de escrita; fila/broker → consumidor assíncrono → banco de leitura) que não está na transcrição.

Termos corrigidos por contexto (transcrição automática): "blog da tabela" → lock da tabela; "colegas"/"consegue" → queries/consultas (provável "queries"); "tutorial tensão" → alta contenção; "Command Drag Race o segregation" → Command Query Responsibility Segregation; "como de render" → command handler (provável); "SQL serve" → SQL Server; "postos" → Postgres (provável); "novo ciclo"/"não ciclo" → NoSQL; "Jason" → JSON; "Inner join"/"energyon" → joins; "Rebite mico" → RabbitMQ; "com ciúmes" → consumer (provável); "Yu hai" → UI; "atualização A5" → atualização assíncrona (provável); "event handler The King" → event handler; "dormem eventos" → domain events (provável); "consistência eventual" mantido. Trechos ambíguos: "formulário lagero cadastro com três tabelas" (provável "formulário largo de cadastro com três tabelas"); "você paga as cores com banco de dados leitura" (provável "você paga as consultas com o banco de dados de leitura"). Marcados abaixo com [?] onde a interpretação é incerta.

---

## O problema

Situação recorrente: um sistema com volume de carga muito divergente entre **consulta** e **alteração**. Faz-se muito mais consulta do que alteração. Em termos de banco de dados, as consultas ficam presas por **locks** de tabela (transações abertas) em determinados períodos do dia ou do mês, em que há mais alteração ou mais consulta. Esse desbalanço, com alta contenção no banco, acaba onerando o banco de dados e, por consequência, a aplicação.

Qual seria a solução proposta? Um desbalanço muito grande entre consulta e alteração, com consultas presas por transação aberta, é uma relação muito desigual. Obviamente é preciso analisar vários pontos, mas uma estratégia que pode ser usada é **CQRS**.

## O que é CQRS

**Command Query Responsibility Segregation**: segregar a responsabilidade entre **alteração** e **consulta** na aplicação. Quando a diferença entre alteração e consulta é muito grande e existe uma solução só que trata as duas tarefas de forma unificada, não se consegue escalar uma ou outra individualmente. Não dá, por exemplo, para deixar as consultas mais rápidas destinando recursos só a elas, porque se usa o mesmo banco e a mesma estrutura — para escalar é preciso escalar **como um todo**.

## Lado de escrita (alteração)

O cliente (UI) faz requisições que alteram o comportamento de alguma entidade do sistema. Isso é representado por **comandos**. Os comandos são construídos e, através de um **bus**, chegam a ser executados em um **command handler** — a estrutura que manipula os comandos. Ali se faz tudo o que for necessário: chamar um repositório, trabalhar o domínio, as entidades e as regras de negócio, e persistir no banco usando o repositório.

Suponha que esse repositório seja um banco de dados relacional (ex.: SQL Server, Postgres). O comando por si só é persistido no **banco relacional**.

## Lado de leitura (consulta)

Num modelo convencional, a consulta iria simplesmente ao mesmo banco SQL. Mas aqui se quer **segregar tanto na aplicação quanto no banco**: separar até o banco de escrita do banco de leitura. O banco de escrita é o relacional; o banco de leitura é outro, a escolher.

A leitura é feita por **queries** — há uma camada de dados que sabe conversar com o banco de leitura e vai direto nele, sem passar pelo domínio.

Qual banco de leitura? Depende, mas geralmente usam-se bancos **não normalizados** (desnormalizados). **NoSQL** é uma escolha frequente para leitura porque, ao consultar, o objetivo é deixar os dados no banco de leitura **o mais próximo possível do que precisa ser consumido**. Se a tela precisa de cinco informações, carrega-se um documento com elas — geralmente em **JSON**, num formato muito próximo do que será consumido na UI. Isso dá muita agilidade: num banco SQL muitas vezes é preciso fazer vários **joins**, consultar várias tabelas ao mesmo tempo para chegar à informação desejada na UI. Desnormalizando, os dados ficam mais "prontos": uma linha que se quer consultar é basicamente uma linha (documento) no banco de leitura, enquanto no SQL muitas vezes seriam necessários inner joins com duas ou três tabelas para trazer a descrição de códigos e assim por diante. O banco de leitura é preparado para ter dados mais próximos do que precisa ser consumido.

## Como o dado chega ao banco de leitura

Pergunta: persisti os dados no SQL Server (por exemplo, um formulário largo de cadastro com três tabelas [?]). Como faço para que esse dado, que só existe no banco de escrita até então, seja salvo também no banco de leitura?

Estratégia: trabalhar com **eventos**. Toda vez que se salva um dado na escrita, dispara-se um **evento** (por exemplo, "formulário cadastrado" — o vídeo não especifica se a comunicação é interna à aplicação ou não; comenta esse detalhe mais adiante). Uma parte da aplicação recebe o evento — um **event handler** — e processa: sabe que tal dado foi cadastrado na base, **transforma** o dado de alguma forma e o persiste na base de leitura no formato já especificado, muito mais próximo do que será consumido.

Geralmente essa comunicação é feita por **eventos** e transportada por **mensagens**. As mensagens caem numa **fila**, gerenciada por um **message broker** — por exemplo **RabbitMQ**. Em algum lugar há um **consumer** que roda de forma **assíncrona**, lendo as mensagens das filas do RabbitMQ, **apartado da aplicação de escrita**. Ele faz o processamento dos eventos e a inserção dos dados no banco de leitura.

Perceba que **não se onera a aplicação de escrita**: ela apenas insere, gera um evento que cai numa fila, e a relação acaba ali. Esse trecho não trabalha ativamente para atualizar a base de leitura. Além disso, o consumer é outro componente que pode ser **escalado independentemente** se houver muito volume de eventos. Os dados vão sendo inseridos no banco de leitura, com a atualização de forma assíncrona do que foi cadastrado.

## Separação lógica e física

Dessa forma há separação **lógica** da aplicação e separação **física** dos bancos de dados: a parte de alteração passa pelos comandos e por toda a lógica de negócio e insere os dados; as consultas vão ao banco de leitura, que já oferece os dados num formato muito mais próximo, mais fácil e rápido de consumir, e está separado em outro banco.

## Consistência e estratégias de atualização

Detalhe importante: cadastrei o dado — em quanto tempo ele estará disponível no banco de leitura? Existem várias estratégias de atualização do read model: **atualização imediata** ou **atualização assíncrona** (o modelo descrito acima [?]). Na atualização assíncrona há um **pequeno delay**, dependendo de como o processamento é feito, entre a existência do cadastro no banco de escrita e sua existência no banco de leitura. Isso é a **consistência eventual**.
