# Como Escalar Leituras de Banco de Dados (System Design para Entrevistas Tier S)

> Transcrição de vídeo de **Pedro Camaforte** — primeiro vídeo da série de System Design sobre como escalar leituras de banco de dados para entrevistas em empresas "Tier S" (faixa salarial ~R$30.000 para cima).
> A série é inspirada em um artigo de **Lucas Faria** sobre os sete conceitos que mais caem em entrevistas de System Design para empresas Tier S.

## Abertura

Você está numa entrevista para uma vaga de R$40.000 e o entrevistador monta um sistema e te fala: "Esse banco de dados está recebendo 50.000 leituras por segundo e começou a travar. O que você faz?"

O programador mediano responde: "Ah, é só adicionar uma camada de cache, réplicas dos bancos de dados, e ele é eliminado na hora."

Este vídeo é o porquê disso. Até o fim você vai entender o que são **índices**, **connection pooling**, **read replicas**, **cache** e **CDN**, os *tradeoffs* de cada um desses pontos, e no final o erro que faz o entrevistador eliminar 90% dos candidatos.

## Como identificar um sistema pesado em leituras

Um post é escrito uma vez e é visto milhares de vezes. Uma URL encurtada é criada uma vez e redireciona milhares de vezes ao longo do dia. Quando há uma aplicação assim — em que para cada 100 leituras existe uma escrita (500 leituras, 1000 leituras por escrita) — possivelmente haverá um gargalo no banco de dados no futuro.

A solução do gargalo depende do **motivo** por trás dele, que nem sempre é o mesmo. O objetivo não é entrar nos detalhes de implementação de cada conceito (na entrevista você não faz isso), mas focar naquilo que o entrevistador quer ouvir para o problema apresentado.

## 1. Índices + Connection Pooling (resolve 80% dos casos)

Antes de pensar em cache ou réplica, a primeira coisa a analisar: a tabela/banco que está com latência alta tem **índices corretos** e está fazendo **connection pooling**?

- Uma tabela sem índice com milhões de dados pode demorar até ~500ms (ou mais, dependendo do volume). Com índice, a resposta pode cair para ~2ms — ganho absurdo de performance.
- Só com índices + connection pooling, uma infraestrutura/hardware moderno consegue trabalhar na ordem de dezenas a centenas de milhares de requisições por segundo. A maioria dos sistemas nem sonha em chegar perto desse número.

**Por que connection pooling?** Sempre que se abre uma nova conexão com o banco há um *delay* de ~5 a 10ms. Sob alta carga de leitura, esses milissegundos fazem diferença e começam a retornar erro para o usuário quando a capacidade máxima de conexões é excedida. Com connection pooling, as conexões ficam abertas e são reutilizadas entre as solicitações de cada usuário.

Combinando índices + connection pooling, nativamente, sem mudar nada no banco, resolve-se ~80% dos casos iniciais.

## 2. Read Replicas (200-300k+ leituras/s)

Quando índices + pooling não bastam (já falando de 200-300-500 mil leituras por segundo), entra o conceito de **read replicas**.

Read replica é pegar um banco que recebia tanto escrita quanto leitura e separá-lo: agora ele só recebe **escrita**, e existem cópias (réplicas) para receber as **leituras**. É como um "load balancer de banco de dados": redistribui a carga de leitura para réplicas com menos carga. Pode-se escalar praticamente de forma infinita — adicionar uma quarta, quinta, sexta réplica conforme o sistema cresce.

**O segredinho (tradeoff) que elimina candidatos:** deixar claro para o entrevistador o *tradeoff* da replicação. Sempre que há uma escrita, até a replicação acontecer, pode haver um *delay* de até **segundos** (não só milissegundos), dependendo da aplicação.

- Para um feed de Instagram, tudo bem: postou, demorou um pouquinho, ok.
- Para uma **conta bancária / fintech**, será que é aceitável? Mostrar o conceito sem explicar isso pode te cortar na hora — mostra que você não tem tanto conhecimento.

Saber falar os tradeoffs é excepcional. Mas há um cenário que as read replicas **não** resolvem, não importa quantas réplicas você coloque.

## 3. Cache (hotspots e queries caras)

Imagine que a aplicação lida com 10-20 mil requisições/s no banco — só índices + pooling já resolveram. Só que um lugar específico (um **hotspot**) recebe carga altíssima, muito acima do normal: o perfil de uma celebridade recebendo 200.000 requisições/s. É aí que o **cache** brilha: reduz a carga nesse ponto específico e responde ao usuário final em menos de 1ms.

Onde mais o cache se aplica: **queries caras** — com muitos joins e muita agregação (leaderboards, dashboards, relatórios em tempo real). Essas queries às vezes recebem pouca carga (ex: 50 req/s), mas se demoram 10 segundos para responder, é péssima experiência. O cache guarda o resultado pré-computado e devolve em menos de 1ms.

**O problema do cache: invalidação.** Se a tabela muda / um dado novo entra, é preciso uma estratégia para o cache servir o dado mais atualizado. Três estratégias principais:

1. **Expiração (TTL)** — o cache expira a cada N segundos (ex: 15s). Simples, mas pode trazer dados desatualizados.
2. **Deletar o cache** — sempre que a tabela muda, deleta o cache; a próxima leitura traz o dado atualizado. Requer coordenação entre os sistemas.
3. **Atualizar o cache** — atualiza o cache junto com o banco quando o dado é inserido/atualizado. Também requer coordenação.

**Padrão mais comum (cache-aside):** a requisição procura no cache; se não tem o dado (miss), bate no banco, guarda no cache e devolve ao usuário. Na próxima vez, busca direto no cache. O cache tira a carga do banco, que fica livre para servir o resto da aplicação.

## 4. CDN (arquivos estáticos)

O último conceito é a **CDN**, principalmente para distribuir arquivos estáticos aos usuários. É uma rede de servidores globais onde os arquivos ficam armazenados mais próximos do usuário final.

Exemplo: o data center está no Brasil e um usuário nos EUA carrega uma página com várias imagens. Se demorar, o site tem má performance no ranqueamento do Google e o usuário provavelmente sai antes de carregar. Com CDN, o tempo de espera cai de ~400-500ms para ~20-50ms. Para esse problema não se usa cache nem réplica de banco — é a CDN que resolve.

## O erro que elimina 90% dos candidatos

O erro mais comum: o candidato **não tenta entender o problema por trás da arquitetura** pedida — o escopo, o contexto. Parece simples, mas com o nervosismo o candidato passa por cima disso e já ataca arquitetura/conceito direto, sem entender o que está acontecendo.

- **Programador pleno** já sairia falando: "Para resolver esse problema de leitura é só tacar um cache e fazer réplicas dos bancos para distribuir as leituras." → Eliminado.
- **Programador sênior** entende que o entrevistador pergunta de forma genérica de propósito, para ver se você entende o contexto. O sênior responde: "Que tipo de aplicação é essa? Quantas requisições por segundo? Existe algum hotspot — algum lugar sobrecarregado enquanto o resto recebe carga razoável? A aplicação precisa de dados extremamente atualizados (é crítico)?"

Ao entender o contexto, a resposta fica muito mais clara e simples, e você mostra senioridade.

Exemplo: o entrevistador diz que o banco está com gargalo. Você pergunta: "Quantas requisições por segundo?" Se ele responder **10.000 req/s**, matou: só otimizando índices + connection pooling você resolve o gargalo. Você ainda pode citar que daria para fazer read replicas, cache e CDN — mas com essa volumetria, só otimizar as tabelas já resolve, reduzindo custos de arquitetura, time e infraestrutura.

Às vezes ficamos com medo porque parece simples demais, mas é exatamente isso que o entrevistador quer. E não é só entregar "é só tacar índice na tabela": primeiro entender o contexto (mostra senioridade), depois mostrar o que você **faria de fato** porque é o que aquele problema específico está pedindo.

## Regra de ouro (resumo)

Perguntas a fazer durante a entrevista:

1. Estamos lidando com **arquivos estáticos**? Se sim → **CDN**.
2. O banco está sobrecarregado de leituras? → **índices + connection pooling** (80% dos casos se resolvem aqui).
3. Ainda não é suficiente, tem muito mais leitura? → **read replicas** (mata bancos com 200-300 mil req/s; só ir adicionando réplicas).
4. Ainda não resolveu porque há **hotspots** e **queries caras**? → só aí entra o **cache**.

Ciladas que eliminam:

- Sair adicionando cache sem antes otimizar tabelas e aplicar connection pooling.
- Mostrar uma implementação sem antes mostrar os **tradeoffs** (cache exige coordenação para os dados não ficarem desatualizados; read replica causa latência de replicação, problemático para aplicação financeira).

## Exemplo prático: encurtador de URL

O entrevistador pergunta como você lidaria com o banco de um **encurtador de URL**. Conversando, chega-se à conclusão: para cada 1 escrita existem ~1000 leituras (um link é criado uma vez e redireciona milhares de vezes), e a aplicação recebe ~60.000 req/s no banco.

- A query de redirecionamento busca pelo `public_code` (a parte visível do link). Esse campo precisa de um **índice**, e todas as conexões usam **connection pooling**.
- Para **URLs virais** (que redirecionam muito mais que a maioria — ex: perfil de um famoso no Instagram), aplica-se **cache com Redis**, tirando a carga dessas queries do banco e deixando-o servir o resto.

Se as 60.000 req/s virarem 200.000+ req/s, então pega-se o banco principal e criam-se **réplicas** conforme a necessidade, distribuindo a carga em bancos de leitura e deixando o banco principal só para escritas.

## Próximo vídeo

Isso resolve escalabilidade de **leituras**. Escalar **escritas** é outro assunto (próximo vídeo da série) — é onde a maioria dos desenvolvedores quebra.
