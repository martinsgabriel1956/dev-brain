# O Que Esperam de um Pleno na Programação — Revisão com 4 Anos de IA

Transcrição de vídeo em português (fala espontânea, transcrição automática/ASR). Limpo de repetições, cacoetes de fala, trecho publicitário do patrocinador e pontuação corrigida, mantendo o conteúdo e a estrutura de raciocínio do apresentador. Sem tradução — conteúdo original em português.

**Apresentador:** não identificado com certeza a partir do próprio texto (ver observações no source page da wiki). Canal com pelo menos 4 anos de atividade no momento da gravação, evidências no texto: vídeo original "o que esperam de pleno na programação" postado há 4 anos, com mais de 51.000 visualizações; canal derivado de vlogs citado como "AI the Internet" (transcrição possivelmente imprecisa do nome real); menção a uma pessoa chamada Sara aparecendo em vlogs de sexta-feira/fim de semana.

## Gancho / contexto

Erick tuitou marcando o apresentador, avisando que achou um vídeo dele de 4 anos atrás sobre os requisitos para virar programador pleno. O vídeo original, "O Que Esperam de Pleno na Programação", foi um dos primeiros vídeos a viralizar no canal, trazendo bastante audiência nova — cerca de 51 mil visualizações.

Em vez de reagir ao vídeo completo (16 minutos), o apresentador revisita os 13 pontos listados no vídeo original e os reavalia com base em ~4 anos e meio de agentes de IA escrevendo código. Conclusão adiantada: o resultado foi pior do que esperava — 6 dos 13 requisitos hoje são "commodity" (a IA faz melhor, mais rápido e mais barato que um humano). Um item, classificado por engano como baixa prioridade no vídeo original, hoje é reclassificado como o único que de fato justifica o salário de um pleno.

## Sobre as etiquetas júnior/pleno/sênior/staff

Antes da lista, o apresentador questiona o valor das etiquetas de nível (júnior, pleno/mid-level, sênior, staff): na opinião dele, são rótulos que o mercado usa para dar aos profissionais um motivo para continuar subindo a escada de carreira — não necessariamente uma medida objetiva de conhecimento ou de salário. Argumento: existe disparidade salarial enorme entre empresas para o mesmo nível (pleno de uma empresa pode ganhar mais que sênior de outra); isso depende de quanto a empresa compete por talento (local, regional, nacional, internacional, ou em subnichos como laboratórios de IA, onde os salários chegam à casa de milhões de dólares/ano). Por isso, as etiquetas não seriam usadas para equilibrar remuneração de mercado, mas sim como uma "cenourinha" motivacional de progressão de carreira.

## Os 13 itens do vídeo original, revisados um a um

### 1. Git (versionamento de código) — commodity, já caiu
Antes: resolver conflitos de merge manualmente, stash, patch, escolher entre trunk-based development ou git flow, cortar tags de release. Hoje: o apresentador diz não resolver um merge conflict manualmente há muitos meses — tudo isso já é feito via IA. Menciona também o conceito de **worktree**, que não estava na lista original mas foi crucial no início do uso de agentes (muita gente não conseguia paralelizar tarefas por não conhecer esse conceito) — hoje as próprias interfaces de agentes (Cursor, Claude Desktop, Codex, Claude Code) já criam worktrees automaticamente ou perguntam se você quer rodar local, em worktree, ou na nuvem, então o conceito importa menos explicitamente.

### 2. Comandos básicos de terminal — commodity, já caiu
Antes: aprender pipes, grep, formatação de saída para buscar/filtrar/mover/copiar arquivos manualmente. Hoje: os agentes já operam dentro do terminal — você pede em linguagem natural e o agente busca, filtra e roda os comandos por conta própria. Considerado hoje algo "para exibir para os amigos", não mais uma competência prática necessária no dia a dia.

### 3. Estrutura de dados e algoritmos — rebaixado de pleno para júnior, mas continua importante
Antes: conhecer pilha (stack/LIFO), fila (queue/FIFO), hash table, lista encadeada, array, e as variações (hashset, hashmap). Hoje: o apresentador ainda considera esse conhecimento fundamental — mas rebaixa a exigência de "pleno" para "júnior". Justificativa: mesmo que a IA tome decisões de implementação, entender o conceito de LIFO/FIFO continua relevante no dia a dia (ex.: entender que um Redis pode ser usado como fila/queue de processamento).

### 4. Tooling (SSH, proxy, VPN, mock de API) — ficou mais importante
Item que ganhou peso na revisão. Inclui: usar SSH, configurar um proxy (ex.: Charles Proxy) para reescrever/interceptar requisições, debugar tráfego, e mockar respostas de uma API que ainda não está pronta. Avaliação: a IA facilitou parte disso (ex.: adicionar/remover IP de proxy nos dispositivos), mas o apresentador ainda relata precisar configurar esse tipo de ferramenta manualmente, porque a IA frequentemente erra ou não consegue configurar corretamente dispositivos/proxies.

### 5. Consumir/criar REST API, WebSocket vs. polling, GraphQL — ficou atemporal
Avaliado como um dos itens que "envelheceu bem": ainda é necessário entender a diferença entre WebSocket, short polling, long polling, Socket.IO e quando usar GraphQL. O apresentador considera que isso continua sendo conhecimento que cabe ao pleno revisar quando a IA sugere uma solução de transporte/infra para a aplicação — cabe à pessoa validar se a IA escolheu a abordagem correta. Ressalva: isso depende do stack de cada empresa (não é obrigatório saber GraphQL se a empresa não usa), mas espera-se que um pleno consiga se preparar sozinho em cerca de uma semana antes de uma entrevista, se necessário — inclusive comparando com conceitos já dominados de sockets/polling para acelerar esse aprendizado.

### 6. Dominar uma linguagem/paradigma de programação — rebaixado de pleno para júnior (paradigma, não "linguagem 100%")
Antes: dominar 100% uma linguagem de programação e seu paradigma; eventualmente duas linguagens (ex.: Kotlin/Java em Android). Hoje: o apresentador está em dúvida se ainda é necessário "dominar" uma linguagem no sentido antigo — mas considera que dominar o **paradigma** ao redor da linguagem continua essencial, porque não dá para revisar código gerado por IA sem entender os padrões da linguagem. Reclassificado como requisito de júnior, não de pleno. A necessidade de uma segunda linguagem ainda depende do contexto (ex.: times Android multiplataforma).

### 7. SQL e bancos de dados — mantido em pleno, mas o foco muda
Antes: criar banco, usar joins (left/inner), GROUP BY, triggers, cuidado com DELETE sem WHERE, conhecer bancos não-relacionais (Redis, MongoDB, MariaDB), e saber escrever testes com mocks. Hoje: o apresentador separa esse item em dois. Sobre banco de dados: mantém como pleno, mas desloca o foco de "escrever a query na mão" para os conceitos por trás — estratégia de sharding, roteamento, indexação, chaves primárias/secundárias/estrangeiras. Justificativa: quando a IA está mapeando o banco de dados, o pleno precisa ter esse repertório conceitual para revisar as decisões da IA, mesmo que não escreva mais o JOIN/GROUP BY manualmente (isso a IA já faz bem, bastando descrever a intenção em linguagem natural).

### 8. Testes automatizados — ficou mais importante
Reforçado na revisão. Justificativa central: como a IA gera milhares de linhas de código por dia, é humanamente impossível revisar tudo linha a linha — nem só um humano revisando, nem só uma IA revisando outra IA, é suficiente. A resposta é ter validação determinística via testes automatizados e CI. O apresentador relata escrever mais testes do que nunca, e delegar cada vez menos a escrita dos próprios testes à IA de forma automática — prefere planejar quais testes escrever e como rodá-los no CI. Aponta esse conhecimento como cada vez mais crítico para quem quer evoluir de pleno para sênior.

### 9. Gerenciamento de dependências — mantido, com novo foco em segurança
Antes: saber usar Maven/Gradle e organizar catálogos de dependência. Hoje: a IA facilita a parte operacional (organizar o catálogo do Gradle deixou de ser um "bicho de sete cabeças"), mas o item ganhou uma dimensão nova de segurança — modelos recentes já vêm com skills de varredura de segurança em pacotes, mas ainda cometem erros; o apresentador cita o crescimento de ataques de supply chain como motivo para esse conhecimento continuar relevante, mesmo com apoio de IA.

### 10. Design patterns e arquitetura — rebaixado de pleno para júnior
Antes: dominar padrões como Singleton (incluindo detalhes como `synchronized` para múltiplas threads acessando a mesma instância). Hoje: a IA facilitou bastante a implementação (ex.: pedir para refatorar três implementações distintas para um Abstract Factory), mas o conhecimento conceitual continua essencial — porque é isso que orienta o prompt dado à IA sobre como o projeto deve ser organizado. Reclassificado como requisito de júnior, não mais de pleno.

### 11. Dominar um framework (2-3 anos de vivência) — se transformou em "múltiplos frameworks"
Antes: ter 2-3 anos de experiência em um framework específico usado pela empresa contratante (Spring, Symfony, .NET/C#, React etc.), não apenas na linguagem "vanilla". Hoje: essa exigência está caindo — cada vez mais se espera trânsito entre múltiplos frameworks/stacks. Exemplo citado: devs de Android nativo tendo que contribuir também no projeto iOS nativo (não Flutter/React Native — nativo mesmo); devs de backend tendo que contribuir do início ao fim em frameworks de frontend e de backend diferentes. Avaliação: um pleno hoje deveria se sentir confortável navegando entre frameworks — e isso exige uma base sólida de arquitetura, já que um framework é essencialmente um "template" de padrões (injeção de dependência, inversão de dependência etc.) que elimina boilerplate.

### 12. System design (desenhar solução no quadro branco) — mantido, sem mudança
Único item, junto com o item 5 (protocolos de transporte), citado como tendo "envelhecido bem": a capacidade de desenhar uma funcionalidade/sistema continua um conhecimento valioso para pleno, sem redução de importância na revisão.

### 13. Soft skills (code review, feedback, documentação, metodologias ágeis) — reclassificado como o item mais importante
Este foi o item que, segundo o apresentador, foi classificado incorretamente no vídeo original — colocado por último, como se fosse menos importante. Hoje ele reavalia esse item como **o único que de fato justifica o salário de um pleno**. Detalhamento:
- **Code review** passou a consumir boa parte do tempo de trabalho, embora essa onda já esteja arrefecendo à medida que o foco migra para formas mais determinísticas de verificar qualidade de PR.
- **Escrever feedback** também já está sendo parcialmente delegado à IA.
- **Documentação**: segundo o apresentador, "ninguém mais escreve documentação, ninguém mais lê documentação".
- **Metodologias ágeis**: estão mudando rápido, migrando para algo mais próximo de um "go horse organizado" — sprints de duas semanas viraram sprints de uma semana, viraram simplesmente um Kanban, mas ainda sem um nome formal para esse novo modelo. O apresentador especula que, nos próximos 6-12 meses, deve surgir algum autor nomeando formalmente essa nova metodologia.
- Conclusão do apresentador sobre soft skills: a regra mais importante continua sendo "não seja um idiota" — ser uma pessoa agradável de se trabalhar.

## Resumo da reclassificação (2026 vs. vídeo original)

- **Caíram para "commodity" (a IA faz melhor/mais rápido/mais barato):** Git avançado, comandos de terminal.
- **Rebaixados de pleno para júnior (conceito ainda importa, mas é piso, não diferencial):** estrutura de dados e algoritmos, dominar uma linguagem/paradigma, design patterns e arquitetura.
- **Mantidos como pleno, com foco realocado (menos "mão na massa", mais "revisar a decisão da IA"):** SQL/bancos de dados, gerenciamento de dependências (com camada nova de segurança).
- **Ficaram mais importantes:** tooling (proxy, SSH, mock de API), testes automatizados.
- **Ficaram atemporais, sem mudança relevante:** protocolos de transporte (REST/WebSocket/polling/GraphQL), system design.
- **Se transformou:** dominar um framework → transitar entre múltiplos frameworks/stacks.
- **Reclassificado como o item mais importante (antes subestimado):** soft skills — especialmente a capacidade de não ser "um idiota" para trabalhar junto.
