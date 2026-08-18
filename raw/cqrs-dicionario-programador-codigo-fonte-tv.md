# CQRS — Dicionário do Programador, Código Fonte TV (transcrição)

> Transcrição de vídeo em português (segmento "Dicionário do Programador" do canal Código Fonte TV). Texto bruto de reconhecimento de fala, sem pontuação, com termos deformados pelo ASR (ex.: "que RS", "Seca RS", "essa qrs" por "CQRS"; "Pater"/"Pátia"/"Pátio" por "padrão"; "de dois" por "void"; "e Ventos fortes"/"eventos force" por "Event Sourcing"; "macoratti" por José Carlos Macoratti, autor referenciado). Limpa, pontuada e organizada em seções abaixo, preservando a estrutura original: introdução → cenários de motivação → definição de Command/Query → diagrama → estratégias de sincronização → quatro aspectos de implementação → menção a Event Sourcing → encerramento.

## Introdução

CQRS é a sigla para Command and Query Responsibility Segregation — em português, "segregação de responsabilidade de comando e consulta". É um padrão (pattern), ou seja, um modelo para operações de leitura e gravação de dados. Importante não confundir: é um padrão arquitetural, não uma arquitetura em si.

Quando você precisa gravar informações em um banco de dados, mas ele trava porque tem muita consulta sendo executada ao mesmo tempo, o CQRS trouxe a solução para esse e outros problemas parecidos.

## Por que separar comando e consulta?

Para explicar CQRS, primeiro é preciso entender por que inventaram essa separação entre escrita e consulta de dados. Alguns cenários ajudam a ilustrar:

**Cenário 1 — consultório médico, uso único.** Uma aplicação desktop para agendamento de consultas, instalada na máquina do usuário, com o banco de dados também na própria máquina. Se der pau, é o problema do próprio usuário, mas o que importa é que, como só existe um usuário, ele realiza consultas e alterações na agenda de forma não concorrente. Esse sistema não tem problema de concorrência no enfileiramento de tarefas.

**Cenário 2 — clínica com 10 atendentes.** O sistema agora é uma aplicação que roda na rede local, em um servidor dentro da clínica, com o banco de dados também em servidor próprio. Nessa situação já é possível que consultas e alterações no banco tenham uma certa concorrência, já que existem mais usuários utilizando o sistema simultaneamente.

**Cenário 3 — SaaS multi-clínica.** A solução cresce e passa a ser usada por diversas clínicas e consultórios, onde quem marca a consulta é o próprio paciente, via aplicação web ou aplicativo. Agora, em vez de 10 atendentes atualizando e consultando uma base de dados, pode haver 100 mil ou muito mais usuários simultâneos realizando tarefas no sistema.

Nesse último cenário, o uso de CQRS passa a fazer muito mais sentido.

## Command e Query

- **Query** (consulta): modelo responsável por recuperar informações dos dados. Nunca faz qualquer alteração neles.
- **Command** (comando): modelo responsável por fazer modificações no estado dos dados — criação, atualização e remoção.

É importante frisar que esse modelo deve ser baseado em **tarefas**, e não centrado nos dados em si. Parece bobo explicar isso, mas em determinadas abordagens de CQRS é possível utilizar duas ou mais bases de dados diferentes para realizar essas tarefas.

Outro ponto importante: CQRS deve ou pode ser usado apenas em partes específicas de um sistema — o que se chama de **bounded context** (contexto delimitado) — e não no sistema como um todo. Pensando dessa forma, cada contexto precisa de suas próprias decisões sobre como deve ser modelado. Aí entram os microsserviços, que não deixam mentir: a ideia é fazer com que não haja lock de acesso ao banco de dados, seja a nível de linha, de documento (no caso do NoSQL) ou de tabela.

## Diagrama do fluxo

Exemplo de implementação de CQRS:

```
Aplicação
   │
   ├── Modelo Command → INSERT / DELETE / UPDATE → Banco de dados relacional (escrita)
   │
   └── Modelo Query → SELECT → Base de dados de leitura (pode ser qualquer tecnologia:
                                Redis, repositório de cache, ou qualquer outro tipo de
                                repositório usado para consulta — inclusive, em alguns
                                casos, o mesmo banco de dados)
```

O importante aqui é que se está falando de um **padrão**, não de uma tecnologia específica. A tecnologia usada nos dois lados depende do que for necessário.

Por último, entra a **estratégia de sincronização**: a partir do momento em que os dados são alterados no lado de escrita, é preciso, em algum momento, sincronizar a base de dados de leitura. É aí que a complexidade começa a aumentar — não existe uma resposta pronta para todos os cenários, é preciso escolher a melhor estratégia para cada caso.

### Estratégias de sincronização mais comuns

- **Automática**: cada mudança de estado dispara um processo síncrono no banco de dados de leitura. Não é uma solução mágica.
- **Eventual**: a atualização é feita de forma assíncrona.
- **Controlada**: um disparo periódico (geralmente agendado) atualiza a base de leitura.
- **Sob demanda**: para cada consulta, a consistência das bases é verificada.

A consistência eventual costuma fazer mais sentido do ponto de vista de performance. Por isso, a implementação de um serviço de mensageria pode ajudar nesse processo — não é obrigatório, mas pode ajudar.

Em resumo, o padrão consiste em dividir a aplicação em modelos de leitura e gravação, distribuindo a responsabilidade entre objetos dedicados: o modelo de gravação não precisa se preocupar com o retorno de dados, e o modelo de leitura pode ser especificamente escrito para retornar os dados corretos que satisfaçam os requisitos da aplicação.

## Como o CQRS é implementado: quatro aspectos

### 1. UI baseada em tarefas (task-based UI)

CQRS deve ser focada na intenção do usuário, e não em aplicações CRUD. Numa interface CRUD típica, a tela é apenas uma camada fina sobre o banco de dados, permitindo ao usuário criar, ler, atualizar e excluir. Ao obedecer só a esses quatro métodos básicos, perde-se a intenção do usuário — uma aplicação não deve ser apenas uma camada fina sobre um banco de dados, ela deve ajudar o usuário a atingir um objetivo.

CQRS não está focado em ser um CRUD: ele permite escrever uma UI baseada em tarefas que atravessa a aplicação para oferecer uma interface rica e baseada em intenção. Ou seja, em vez de uma interface que tenta se adequar à estrutura do banco de dados, uma UI orientada a CQRS é ajustada para resolver as necessidades reais do usuário. É sutil, mas faz toda a diferença.

### 2. Command bus (barramento de comando)

Ao implementar o modelo de Command, o ideal é que ele **não retorne nenhum valor** (void). Isso significa que, por exemplo, um novo registro, quando adicionado, não retorna um ID. Um Command nunca deve retornar dados, porque isso quebraria a separação entre os modelos de leitura e gravação. Se a aplicação realmente precisa desse tipo de funcionalidade, provavelmente não deveria usar CQRS para essa parte específica — ou talvez não devesse usar CQRS para o aplicativo inteiro.

### 3. Consistência de sincronização

Aqui entra a decisão entre processamento síncrono ou assíncrono das tarefas:

- **Síncrono**: retorna uma resposta imediata ao usuário. Importante quando a interface exige um resultado instantâneo.
- **Assíncrono**: nem sempre é necessária uma resposta imediata — por exemplo, quando os dados precisam passar por um processamento complexo ou intenso. CQRS permite gravar os dados numa fonte, processá-los de forma assíncrona e depois transferi-los para o banco de leitura.

Exemplo do mundo real: a contagem de visualizações de vídeos no YouTube. A interface não atualiza a contagem a cada visualização — ela vai sendo atualizada de tempos em tempos, de forma assíncrona. Esse processo é conhecido como **consistência eventual**. Se a aplicação não requer resultados imediatos, usar consistência eventual pode evitar muitas dores de cabeça.

### 4. Domain events (eventos de domínio)

Eventos de domínio são muito importantes para aplicações que implementam CQRS, pois detectam determinados eventos durante a execução da aplicação para acionar outras ações. Isso permite desacoplar a consequência de uma ação da própria ação.

## Menção a Event Sourcing

O vídeo também cita, brevemente, o padrão **Event Sourcing**, comumente utilizado em conjunto com CQRS, citando o autor José Carlos Macoratti: a ideia fundamental do Event Sourcing é garantir que todas as alterações no estado de uma aplicação sejam capturadas em um objeto de evento, e que esses objetos de evento sejam armazenados na sequência em que foram aplicados, pelo mesmo tempo de vida útil do estado da aplicação.

## Encerramento

O vídeo reconhece que cobriu apenas o "basicão" sobre CQRS — há muito assunto relacionado, já que se trata de um padrão que, dependendo da situação, agrega diversas abordagens tecnológicas diferentes.
