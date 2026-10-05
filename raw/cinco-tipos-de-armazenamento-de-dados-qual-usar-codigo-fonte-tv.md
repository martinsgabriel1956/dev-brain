# Cinco Tipos de Armazenamento de Dados: Qual Usar em Cada Problema (Código Fonte TV)

Fonte: transcrição de vídeo do YouTube, canal Código Fonte TV (série "Dicionário do Programador"). Já em português — sem necessidade de tradução. Transcrição automática colada pelo usuário; foram adicionados apenas pontuação, parágrafos e títulos de seção, e o texto foi limpo de erros de reconhecimento.

Termos corrigidos por contexto (transcrição automática): "rood" → "tá errado/errou, rodou" (provável "ó"/"errou"; mantido como "errou"); "Maria DB ou uma SKL" → MariaDB ou MySQL; "structure carry language" → Structured Query Language; "Postgre SQL" → PostgreSQL; "Docploy" → Dokploy; "Reds" → Redis; "main Cashet" → Memcached; "Mongo DB" → MongoDB; "no se c / no sequel" → NoSQL; "Elastic Search" → Elasticsearch; "Apach Kafkaa / Cafca" → Apache Kafka; "Amazon SKS" → Amazon SQS; "idem potência" → idempotência; "Full Tex" → full-text; "Key Valelue" → key-value; "Cash" → cache; "Iar" → IA; "Jason" → JSON; "Big Table" → Bigtable; "Cassandra" mantido; "Vanessa" = coapresentadora citada no texto.

---

## Abertura

O maior erro ao escolher um banco de dados não é escolher a tecnologia errada (pode ser um pouquinho isso). O maior erro é achar que todos os dados deveriam ir sempre para o mesmo lugar. Em situações diferentes — um pedido, uma sessão, uma busca por descrição, uma mensagem entre serviços — as necessidades são completamente diferentes. O vídeo compara cinco tipos de armazenamento para escolher exatamente pelo problema que se quer resolver. É voltado a júnior, pleno ou sênior; "mais que obrigatório".

O desafio: cinco necessidades de dados de uma mesma aplicação, e encontrar onde cada uma deve ser usada: um pedido pago, a sessão do usuário, a descrição de um produto que precisa aparecer na busca, um cadastro que muda de formato toda hora e um evento que precisa chegar a outro serviço. Quem responde "coloco tudo num banco que já conheço" errou: até pode funcionar, mas arca com efeitos colaterais — lentidão, inconsistência, redundância, despadronização.

## O exemplo: uma loja virtual

Todos os exemplos são de uma loja virtual, para mostrar como um único software tem necessidades bem diferentes. A escolha de armazenamento muitas vezes começa pelo banco mais popular, pelo que apareceu no curso, pelo que "a empresa gigante usa" ou "o que eu sei usar" — o último critério é o mais comum ("não precisa ter vergonha, todo mundo começa assim"). A pergunta certa é sobre o **dado**: precisa durar para sempre? Precisa estar sempre atualizado? Tem relações com outros dados? Pode mudar de formato? Precisa expirar em minutos? Precisa ser encontrado quando alguém digita palavras numa caixa de busca? Precisa ser entregue a outro processo para trabalhar?

A loja tem: cadastro de cliente, catálogo de produtos, carrinhos, sessão de usuário, pedidos, pagamentos, estoque, busca por texto, e-mails, compensação de pagamento, emissão de nota e relatórios. Não são todos o mesmo tipo de dado.

## 1. Banco de dados relacional

Dados "sérios" da loja: clientes, pedidos, itens de pedido, pagamento, estoque. Em comum: (1) estrutura conhecida (todo pedido tem cliente, status, valor); (2) relacionam-se entre si (pedido pertence a cliente, tem itens, pode ter transação de pagamento); (3) precisam permanecer no sistema e estar corretos — um pedido/pagamento não pode sumir nem aparecer pela metade. Algumas regras precisam continuar verdadeiras mesmo quando algo falha no meio do caminho.

Modelo: informação em tabelas; cada tabela com colunas de formato definido; cada linha é um registro com uma chave; uma tabela pode apontar para a chave de outra (assim o pedido se liga ao cliente). Comparável a uma planilha, mas com mais garantias.

**Transação**: confirmar uma compra exige criar o pedido, registrar o pagamento e baixar o estoque, no mínimo. Se o servidor cai depois de registrar o pagamento e antes de baixar o estoque, o cliente foi cobrado por um produto que o sistema acha que ainda está na prateleira. A transação do SGBD agrupa as operações num pacote em que **ou tudo acontece ou nada acontece** — "não existe metade da compra".

**SGBDR (RDBMS)**: o software que valida o formato das tabelas, garante chaves e relacionamentos, controla várias conexões mexendo nos dados ao mesmo tempo e executa as transações. Analogia: a diferença entre uma gaveta de papéis e um cartório — os dois guardam um documento, mas só um garante as regras. Ideia testada há décadas: o modelo relacional amadureceu nos anos 70 e segue firme.

**SQL**: Structured Query Language, a linguagem padrão da indústria para consultar e alterar bancos relacionais; obrigatório saber. É **declarativo**: descreve-se o que se quer ("me traz os pedidos do cliente 42") e o gerenciador descobre a melhor forma de buscar. Conselho de carreira: frameworks vão e vêm, mas o SQL atravessa décadas praticamente igual, com pequenas variações de dialeto. O canal tem um mini-curso de SQL.

Exemplos da família relacional: PostgreSQL, MySQL, MariaDB, SQLite, SQL Server, Oracle Database — todos maduros.

**Armadilha**: por ser natural, tende-se a usá-lo para tudo (sessão, cache, log, fila improvisada — "tudo vira tabela"). Mas começar com relacional não é um erro; para muitos projetos, talvez a maioria, é excelente decisão inicial. A pergunta: esse dado tem relações, regras ou alterações que precisam permanecer consistentes? Se sim, forte candidato.

*(Trecho patrocinado: VPS da Hostinger — custo previsível, qualquer tecnologia, melhor custo-benefício; usam há mais de 10 anos; instalam o Dokploy no VPS para fazer deploy do GitHub direto para contêiner Docker; vários deploys por dia; cupom "códigofonte".)*

## 2. Banco de dados não relacional — documentos (NoSQL)

Cadastrar produtos: notebook tem processador, memória, armazenamento; camiseta tem tecido, cor, tamanho; livro tem autor, editora, número de páginas; amanhã a loja pode vender instrumentos musicais, com formato novo. Dá para modelar no relacional (foi feito por muito tempo, há técnicas, times fazem todos os dias, continua funcionando) — o relacional não é incapaz. Mas dependendo do projeto parece "lutar contra a estrutura": cada tipo novo de produto vira mudança de esquema, coluna inexistente para alguns registros, tabela auxiliar.

O modelo de **documento** (estrutura parecida com JSON): cada registro carrega os campos que fazem sentido para ele. Os três produtos têm nome, preço, categoria e disponibilidade em comum; depois divergem. Isso é **dado semiestruturado**: tem estrutura, mas pode variar de registro para registro. O mais famoso: MongoDB.

"NoSQL" é um guarda-chuva com famílias diferentes: documentos (MongoDB), colunas largas (Cassandra, Bigtable) — não aprofundados.

**Erro clássico**: achar que "sem esquema rígido" significa "sem modelagem". O banco não cobrar formato não significa que o formato deixou de existir: a aplicação continua dependendo da estrutura. Se metade dos produtos tem o campo `preço` e a outra metade `valor`, quem quebra é o código — "o banco aceita tudo sorrindo e a bagunça vira sua". E fugir de migration não é, por si só, motivo para escolher NoSQL; é preciso entender se a estrutura varia o suficiente para justificar o modelo flexível.

## 3. Chave-valor (key-value)

Sessão do usuário autenticado: a cada clique a aplicação pergunta "quem é o usuário da sessão 123?" — milhares ou milhões de vezes por dia. O dado não tem relação complexa, não precisa de tabela nem de documento: é um identificador apontando para uma informação. E pode expirar: sessão parada por meia hora, "tchau"; o mesmo para o código de verificação que vale 10 minutos, o contador de limite de requisições (rate limiting) e, com cuidados, o carrinho temporário.

Uma chave identifica um valor; a busca é pela chave, sem relacionamento e sem consulta sofisticada. Em troca da simplicidade, o acesso pode ser absurdamente rápido, porque várias dessas ferramentas guardam tudo em memória. Demonstração: Redis instanciado via Dokploy (que também cria bancos MongoDB, MySQL/MariaDB e Redis); chaves de sessão com estrutura tipo JSON e tempo de expiração; busca trouxe a sessão do usuário. Tecnologias: Redis e Memcached.

**Cache**: cópia temporária de uma informação, criada para evitar que a aplicação repita uma operação mais cara. Exemplo: a página inicial mostra os produtos mais acessados; a consulta é pesada e o resultado quase não muda de minuto a minuto; em vez de refazer a cada acesso, guarda-se o resultado pronto no key-value por alguns minutos.

**Erro perigoso**: transformar o cache na única fonte de informação importante. Valor em cache pode expirar e ser removido quando falta memória; a aplicação precisa saber reconstruir tudo a partir da fonte original. "Um pedido pago que existe só no cache não é uma arquitetura, é roleta-russa." Key-value serve quando é preciso recuperar rapidamente um valor simples a partir de uma chave, e o valor pode ser temporário ou reconstruído.

## 4. Mecanismo de busca full-text

Até aqui a busca era por identificador ou estrutura. Mas o cliente digita "notebook leve para programação" e espera achar o produto mesmo que as palavras estejam espalhadas entre título e descrição, mesmo que o cadastro diga "ideal para desenvolvedores" em vez de "para programação", e espera o resultado mais útil primeiro — isso se chama **relevância**: não basta achar, tem que ordenar pelo que faz mais sentido.

O banco relacional **consegue** fazer busca em texto: para catálogos pequenos e buscas simples dá conta do recado, e tem recursos de full-text próprios. Não cair na história de que toda caixinha de pesquisa exige ferramenta nova. O problema aparece quando a necessidade cresce: milhares de descrições longas, buscas em vários campos ao mesmo tempo, tolerância a variação de escrita e ordenação por relevância — a consulta genérica do banco começa a engasgar.

Para isso existem os mecanismos de busca full-text. Ideia central: o **índice de busca** — em vez de guardar o texto e varrê-lo toda hora, a ferramenta fatia os textos em termos e monta uma estrutura que responde imediatamente quais documentos contêm a palavra, já com nota de relevância. Analogia: índice remissivo de um livro. Nomes mais conhecidos: Elasticsearch e OpenSearch.

**Ponto importante**: o mecanismo de busca **não pode ser a fonte oficial** dos dados. O produto continua salvo na fonte principal (na loja, provavelmente o relacional ou o de documentos); para o mecanismo de busca vai uma **cópia** do necessário, e o índice tem que poder ser **reconstruído do zero** a qualquer momento. Por ser cópia, pode haver pequeno intervalo (normalmente segundos) entre alterar um produto e a busca refletir a mudança — o sistema precisa conviver com isso (exemplo: anúncios na OLX ou no Mercado Livre).

Pergunta-teste: é realmente necessário localizar palavras, trechos ou resultados relevantes dentro de uma grande quantidade de texto? Se sim, esse tipo de mecanismo entra no radar.

**Aparte sobre IA**: hoje a IA muitas vezes pode substituir essa abordagem — passa-se apenas os dados brutos e o modelo decide o que é relevante. Experiência pessoal: ao procurar uma cadeira de escritório para receber convidados num formato de podcast, a pessoa perguntou a uma IA se a cadeira específica era boa para podcast, e ela deu dicas que não estariam na descrição da loja (braço que abaixa para não bater na mesa; travar o encosto para a pessoa não se afastar do microfone). Esse tipo de dica não está em nenhum banco; a IA personaliza a resposta ao que a pessoa procura.

## 5. Filas / mensageria

O cliente pagou. Agora o sistema precisa baixar o estoque, mandar e-mail de confirmação, emitir nota (com a parte tributária brasileira), avisar a logística, registrar dados para relatório e atualizar outros serviços. Precisa tudo isso acontecer na mesma requisição, com o cliente olhando o botão "processando"? Se o servidor de e-mail ficar lento, faz sentido a confirmação do pedido travar? E-mail atrasar 5 minutos é chato; a compra falhar por causa do e-mail é inaceitável.

Por isso existem filas e sistemas de **mensageria**: de um lado um **produtor** registra uma mensagem ("aconteceu algo"); ela fica guardada numa fila ou num log; do outro lado um ou mais **consumidores** pegam a mensagem e executam o trabalho cada um no seu ritmo. Exemplo cotidiano: SMS de recuperação de senha do banco que demora (às 5 da manhã); o serviço de mensageria é programado para rodar de tempos em tempos e executa uma fila de uma vez; às vezes o usuário gera outro código e depois recebe os três juntos.

Isso é **processamento assíncrono**: a aplicação registra que algo precisa ser feito, mas não precisa concluir todo o trabalho antes de responder ao usuário — o pedido confirma na hora e o resto acontece logo em seguida ou em outro processo. De quebra, **desacoplamento**: o sistema de pedidos não precisa saber quem consome o evento; amanhã entra um serviço novo interessado em "pedido confirmado" e começa a consumir sem mexer no fluxo da compra.

Nomes: RabbitMQ, Amazon SQS e Apache Kafka. Ressalva: o Kafka tecnicamente não é uma fila tradicional, e sim um **log distribuído** (registro ordenado de eventos), muito usado em arquiteturas orientadas a eventos; para o mapa do vídeo cumpre o mesmo papel de transportar mensagens entre processos, por isso entra na mesma família. O canal tem episódio do Dicionário do Programador sobre Apache Kafka.

**Ressalvas**: colocar a tarefa na fila não resolve automaticamente os problemas de integração — pode apenas mudar os problemas de lugar. O consumidor pode falhar no meio do trabalho, a mensagem volta e é processada de novo; se for "cobrar o cliente", cobra duas vezes. O sistema precisa ser esperto: se a mesma mensagem chegar duas vezes, o efeito deve acontecer só uma vez — **idempotência**. Além disso, é preciso pensar em novas tentativas quando algo falha, em ordem quando a ordem importa, e no que fazer com a mensagem que nunca consegue ser processada (travada na fila — comparação com a fila de impressão em que um item emperra os seguintes). "Fila é uma ferramenta poderosa, mas cobra responsabilidade." Pergunta-teste: esse trabalho pode acontecer depois, ou em outro processo, sem bloquear o fluxo principal? Se sim, mensageria é candidata.

## O mapa da loja

- Clientes, pedidos, itens, pagamentos, estoque → **banco relacional**.
- Catálogo com produtos de estrutura muito variada → possivelmente **documento (NoSQL)**.
- Sessões e cache → **key-value**.
- Pesquisa de catálogo → **mecanismo full-text**.
- Eventos depois da compra → **fila / mensageria**.

**A frase mais importante do vídeo**: isso é um *mapa de possibilidades*, não uma lista obrigatória. Uma loja pequena pode conviver muito bem guardando produtos tudo no relacional, usando a busca do próprio banco e processando as tarefas de forma mais simples (o apresentador diz que, no começo, usaria cache). Cada tecnologia nova traz instalação, configuração, monitoramento, backup, segurança, mais uma coisa para aprender e mais um jeito novo de falhar. É tentador colocar tudo na stack, mas **maturidade muitas vezes é começar com o bom e velho banco relacional e adicionar as outras peças quando o problema aparecer de verdade — quando chega "com nome e sobrenome"**. O desenvolvedor mais experiente não é o que decorou nomes de bancos ou palavras pomposas, é o que faz as perguntas certas antes de escolher a tecnologia.

## Fechamento

Convite: contar nos comentários em qual projeto já adicionou uma tecnologia que deu mais trabalho do que a solução. Referência à playlist "Dicionário do Programador" (NoSQL, SQL, Elasticsearch, Kafka etc.).
