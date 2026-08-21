# IA em 2026 Não É Mais Só Sobre Prompts ou Agentes (Código Fonte TV)

> Transcrição bruta em português, sem tradução necessária. Reformatada em parágrafos/seções para leitura — conteúdo e ordem das falas preservados o mais fielmente possível a partir do áudio transcrito automaticamente (ASR), incluindo prováveis erros de reconhecimento sinalizados entre colchetes `[sic?]` onde identificáveis.

## Abertura: da adesão de 2024 à adesão de 2026

Passaram os quase 3 anos de lançamento do Cloud [Claude?] e quase quatro do ChatGPT — ninguém vai dizer que o uso de inteligência artificial generativa não está evoluindo. Na pesquisa salarial de 2024, o canal já perguntava sobre isso: 83% dos devs já estavam utilizando IA para programar. Em 2026, a pesquisa mostra 98,5% usando inteligência artificial para programar no dia a dia — um salto grande frente a uma adesão que já era muito grande em 2024. Não tem mais como fugir disso.

Do lançamento do GitHub Copilot, em junho de 2021, parece que vivemos em outro mundo. O ponto do vídeo: IA para desenvolvimento sério em 2026 não é mais só sobre prompts ou só sobre agentes — é um assunto extremamente técnico, e não dá para ignorar isso.

## Linha do tempo 2021–2023

- **2021** — GitHub Copilot. Uso típico: extensão instalada como autocomplete, ou comentário no código pedindo para ele completar a função. Dava a sensação de "adivinhar o pensamento" do dev, mas nem de perto o que existe hoje.
- **2022** — ChatGPT (OpenAI).
- **2023** (março, segundo o vídeo) — Claude (Anthropic), lançado "devagarzinho", pouco conhecido no início. O canal já tinha um vídeo especulando que a Anthropic poderia virar a "próxima OpenAI".

No modelo de "chat", o dev ia até o chat, pedia o que queria, esperava a resposta, e voltava. Foi ficando claro que não bastava pedir tudo do zero sempre — surgiu a necessidade de o sistema já trazer contexto (do GitHub, do projeto) sem precisar reexplicar tudo a cada pedido. Daí vieram o Claude Code, o Codex (OpenAI), o Open Code, o Cursor e outras ferramentas com abordagens diferentes — cada uma com uma aposta própria. O Devin, mais atrás na linha do tempo, apareceu prometendo algo que hoje muitas outras ferramentas já entregam.

## A era dos agentes e o vocabulário novo

Depois vem a "era dos agentes". O vídeo lista uma série de termos/técnicas novas — alguns já consolidados (ex.: MCP), outros ainda pouco conhecidos — e destaca que, mesmo "sendo tudo prompt no fim", a forma como você estrutura isso faz diferença, principalmente quando o uso é agêntico e automatizado: você quer deixar o agente rodando e ter alguma garantia de que o que foi pedido — inclusive quando um agente pede algo a outro agente — está de fato funcionando.

Termos citados como parte desse vocabulário novo (lista aberta, "dicionário do programador"): Harness Engineering, MCP, agentes de IA, RAG, e outros — pedido explícito aos espectadores para comentar quais termos dessa lista eles querem ver como vídeo dedicado.

## Loop Engineering

Todo agente, na essência, trabalha num loop: observa o estado atual, decide o que fazer, usa uma ferramenta, observa o resultado, e repete até concluir a tarefa. Tanto a Anthropic quanto a OpenAI descrevem esse comportamento explicitamente. Em 2026, a LangChain passou a usar o termo "loop engineering" para discutir como esses ciclos devem ser projetados — o que traz problemas clássicos de engenharia:

- Quando os loops devem terminar?
- Quantas tentativas são aceitáveis?
- Quando o agente deve pedir ajuda humana?
- O que acontece se uma ferramenta falhar?
- Como evitar que o agente fique repetindo uma ação e consumindo milhares de tokens?

Projetar esses loops corretamente está ficando tão importante quanto escolher um modelo. O consumo de milhares de tokens é hoje um tema muito discutido — a ideia de "token maxing" já caiu por terra; a tendência atual é consumir o menor número possível de tokens.

## Graph Engineering

Quando os agentes ficam mais complexos, um loop simples pode não bastar — daí a ideia de modelar o fluxo como um grafo: cada nó representa uma operação (chamada de modelo, ferramenta, ou até outro agente), e as arestas determinam qual é o próximo passo. Quem batizou o termo também foi a LangChain, em 2026.

A vantagem: parte do sistema pode continuar determinística (como software tradicional), enquanto outras decisões ficam a cargo da IA — permitindo caminhos diferentes para sucesso, erro, revisão humana, nova tentativa ou execução de ferramentas. É essencialmente uma volta aos conceitos clássicos de máquinas de estado e grafos, agora aplicados a sistemas probabilísticos.

Blueprint descrito no vídeo (visão geral, a partir de uma imagem mostrada): define-se um objetivo → quebra-se o trabalho em partes → execução em paralelo de "workers" (cada um fazendo uma parte diferente) → passa por um verificador → combina tudo numa síntese única → revisão final.

Boris (criador do Claude Code) é citado como alguém que já falou bastante sobre graph engineering. A leitura do vídeo: muita gente dizia "não faço mais prompt, faço loop" — e agora está percebendo que o melhor é gerenciar esses loops através de graph engineering, ou seja, "loops observando outros loops".

## Memory Layers (memória de agente)

Memória de agente não é simplesmente guardar todo o chat. Sistemas modernos podem ter memória de curto prazo, informações persistentes, resumos, artefatos produzidos durante a execução, e mecanismos que recuperam apenas o que é relevante para a tarefa atual. A [Anthropic? transcrito como "OPA"] diferencia: contexto de trabalho, memória para execuções futuras, e artefatos revisados que servem como fonte confiável.

Isso cria um problema de arquitetura: o que deve ser lembrado? Por quanto tempo? Quem pode acessar essa memória? Quando uma informação fica desatualizada? Uma aplicação de IA com memória rapidamente começa a se parecer com um sistema de armazenamento e gerenciamento de estado.

No Claude Code, o `CLAUDE.md` já tem uma hierarquia (máquina → usuário → projeto → pasta) — isso também é memória. Prática relatada pelos apresentadores: ao final de uma tarefa no Claude Code, pedem para ele gerar documentação do que foi feito dentro de uma pasta `docs/` do próprio projeto — assim, sempre que precisam retomar ou gerenciar contexto (context engineering), essa documentação já está pronta para consulta prévia.

### Mensagens cruzadas entre subagentes ("list agents")

Novidade citada do Claude Code: quando ele usa subagentes para resolver problemas, um subagente agora consegue "promptar" outro agente — eles conversam entre si. Isso funciona através de um recurso chamado **list agents**, que lista todos os agentes disponíveis naquele contexto; o agente sabe qual é o melhor para executar uma determinada tarefa, prompta esse agente, ele resolve o problema, e depois a execução continua (podendo ficar rodando em paralelo e retomar depois). Isso está diretamente ligado à memória e ao gerenciamento de estado — e também ao trabalho em equipe: sem acessar a memória do que já foi feito, não dá para compartilhar isso entre máquinas diferentes nem entre membros de uma equipe.

## Spec-Driven Development (SDD)

Ganhando bastante atenção por causa dos agentes de IA na programação. A ideia central: a especificação deixa de ser apenas documentação auxiliar e passa a funcionar como a fonte de verdade que orienta a implementação.

O GitHub criou o **Spec Kit**, especificamente para esse fluxo com agentes de código (documentação completa disponível no GitHub, buscando por "Spec Kit"). Em vez de simplesmente pedir "crie um sistema de login", primeiro se definem requisitos, regras, arquitetura e critérios (e até tarefas) — depois o agente implementa com base nessa especificação. Justificativa: quanto mais autonomia se entrega à IA, mais importante é que ela saiba formalmente o que deve ser feito e construído antes de tomar todas as decisões.

## "E mais": lista aberta de temas correlatos

Citados em sequência, sem aprofundar, como temas que "ainda cabem nessa lista": sandboxing, autenticação de agente, permissões granulares, human in the loop, roteamento entre modelos, caching, rate limiting, segurança (prompt injection), gerenciamento de secrets, e — destacado à parte como algo que "a galera tá meio que esquecendo" — governança, especialmente no uso de IA.

## A virada de 2023 → 2026 (imagem-síntese do vídeo)

Em 2023, "saber usar inteligência artificial" normalmente queria dizer saber usar o ChatGPT e um pouco de prompt engineering. Em 2026, o vocabulário mudou para: protocolo, arquitetura de memória, observabilidade, avaliação, segurança, bancos de dados, sistemas distribuídos, otimização de custos.

Conclusão central do vídeo: a inteligência artificial não está eliminando a parte técnica do desenvolvimento — em muitos casos, ela está criando uma camada completamente nova em cima do que já era preciso saber. Saber programar continua importante; entender de arquitetura, banco de dados, API, segurança e infraestrutura continua importantíssimo. Quanto mais código a IA consegue produzir sozinha, mais importante fica saber projetar o sistema em que essa IA vai (ou não vai) conseguir trabalhar bem. A nova skill do desenvolvedor não é "eu sei usar IA" — é "engenharia de software com IA".

## Bloco patrocinado (Hostinger)

Segmento publicitário do vídeo, resumido (não é conteúdo técnico central, preservado por registrar contexto/produto citado): a Hostinger é apresentada como parceira do canal, com serviços além de hosting/VPS tradicional — Horizons (criação de MVP com IA, já usado pelo canal em um hackathon, incluindo banco de dados e dashboards), serviço de e-mail marketing, agentes de IA (citam "openla" [nome provavelmente mal transcrito] e "Hermes Agent"), suporte a n8n, e uma lista de espera para um futuro serviço de GPU (treino de modelos, inferência). A Hostinger já tem servidor no Brasil. Deploy de ferramentas de dev com um clique no VPS é destacado — ex.: rodar Claude Code 24x7, Codex, n8n, Docker. Citam também o **Dokploy** como ferramenta usada pelo próprio canal para gerenciar containers, com deploy direto do GitHub, controle de versionamento e backups.

## Fechamento

Convite para os espectadores comentarem se o conteúdo fez sentido (ou não) e reforço da tese central: a nova competência não é "saber usar IA" isoladamente, e sim engenharia de software com IA.
