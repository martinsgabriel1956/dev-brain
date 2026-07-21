---
title: "Hermes Agent: o novo Open Claw? Learning loop, skill auto-gerada e o bug de detecção que torrou 200 dólares no Claude Max 20"
source_type: video-transcript
language: pt-BR
translated: false
---

## Abertura — o bug do commit "Hermes"

Se o Claude encontrasse um arquivo `hermes.md` dentro do seu Git History, ele ia torrar os 200 dólares do plano Claude Max 20. É isso mesmo que você ouviu — e sim, a Anthropic já pediu desculpas, porque era só um bug.

Hoje eu quero explicar por que muita gente está dizendo que o Hermes Agent é o novo Open Claw e como a arquitetura dele funciona.

## Por que todo mundo está falando do Hermes

Para entender isso, precisamos nos questionar: quantas vezes essa semana você teve que explicar a mesma coisa para o Claude? Quais são essas coisas?

- O nosso projeto usa PNPM ao invés de NPM.
- A gente roda Postgres com schema `public`, e não como default.
- Sempre escreve teste antes de mudar algo na pasta `resource`.
- Nunca toca no Prisma Migrations sem rodar a migration no ambiente de desenvolvimento.

Esse tipo de coisa está ligado ao seu projeto, e o Claude tem que estar sempre lembrando disso. Aí surge a pergunta: será que eu deveria ter um `init.md` maior? Por que essa repetição acontece? Porque cada nova sessão com o agente é uma nova janela de contexto — o setup dela já pode vir com muita informação, e manter essa informação atualizada é muito importante.

Basicamente, o que o Hermes Agent está fazendo é implementar um **learning loop com skill auto-gerada**. Você tem uma memória persistente em três camadas, e um gateway que pluga ele no Telegram, Discord, Slack.

Isso não é o Open Claw? É — é igual ao Open Claw: open source, licença MIT, roda na sua máquina ou na sua VPS. Essa abordagem parece promissora porque até a Anthropic está lançando algo semelhante: o **Dreaming in Claude**, anunciado há poucos dias, que permite revisar sessões passadas dos agentes Claude, extrair padrões e curar memórias ao longo do tempo.

Por que a gente acredita que o Hermes Agent é uma boa ideia? Porque o Open Claw foi uma ótima ideia — senão a OpenAI não teria adquirido eles — e até a Anthropic está copiando. Fico me perguntando: será que a Anthropic joga pesado mesmo, ou foi só coincidência?

## O bug: perder 200 dólares por causa da palavra "Hermes"

Alguns dias antes da Anthropic anunciar o Dreaming in Claude, alguém expôs na internet que perdeu 200 dólares em um dia porque a string "Hermes" estava nos commits do Git dele. `hermes.md` é uma convenção real usada em projetos de agentes de IA — um arquivo de especificação de prompts do sistema, não um caso obscuro. Ele usava o Claude Max 20 (200 dólares/mês), e o Claude Code notificou do nada que o uso extra tinha acabado.

Tinha um bug. Foi o que um representante da Anthropic (citado como "Tarik" no relato) respondeu no tweet: desculpou-se, disse que foi um bug na detecção de ferramentas de terceiros e na forma como incluíam o status do Git no prompt do sistema, e que estavam entrando em contato com os usuários afetados oferecendo reembolso.

Ou seja: a Anthropic tem sistemas de detecção para ferramentas de terceiros que poderiam estar usando a assinatura dos usuários indevidamente. É por isso que esse tipo de análise não foi feita anteriormente com a Anthropic (diferente do que já vem sendo feito há tempos com a OpenAI, que nunca comentou nada sobre o assunto).

## A mudança de formato do canal

Antes de entrar na parte técnica: o canal vai passar por mudanças. A primeira é o lembrete recorrente para o espectador se hidratar durante o vídeo. A segunda é que a intenção agora é que o espectador saia aprendendo algo técnico, e não simplesmente reagindo a novidades, ao que a Anthropic lança ou ao que a comunidade comenta no Twitter.

*(Bloco patrocinado: menção à Hostinger como provedora de VPS, com liberdade de configurar o próprio servidor virtual — instanciar com Debian, Open Claw, Paperclip, Claude Code, com ou sem painel — enquanto o servidor físico é gerenciado pela Hostinger, incluindo proteção DDoS, firewall com IA, snapshots e backups semanais gratuitos, servidores globais. Cupom de desconto citado: "Lucas Montano". Tratado aqui como conteúdo patrocinado, não como parte da tese técnica central.)*

## Como funciona o learning loop do Hermes Agent

O Hermes não é "o Claude Code com mais memória". O que ele tem por dentro é um **closed-loop skill learning system** que funciona em cerca de cinco a seis etapas:

1. **Task completion** — acontece quando o agente termina uma tarefa. É o primeiro passo do loop de aprendizado.
2. **Pattern extraction** — o agente analisa os passos que deu e identifica o que pode se repetir em tarefas parecidas. Várias empresas já usam hooks para isso: um hook no final da sessão pega tudo que se repetiu, alimenta uma IA que gera esses padrões, e esses padrões alimentam o arquivo `.md` do projeto.
3. **Skill creation** — uma etapa que muitas empresas já fazem manualmente, mas que no Hermes já é automatizada como o terceiro passo do loop.
4. **Skill refinement** — o quarto passo. É o passo em que o autor do vídeo diz já atuar manualmente com hooks, mas reconhece como um problema pessoal: às vezes quer criar uma nova skill, mas já tem tantas skills parecidas que fica difícil organizar esse banco de arquivos `.md` — quando mesclar, quando simplificar, etc. O Hermes automatiza esse refinamento.
5. **Periodic audit** — a cada ~15 tarefas, o agente se autoavalia e escolhe o que deve persistir e por quanto tempo (um TTL configurado). O arquivo `agents.md` do projeto documenta essas referências. Como é open source, nada aqui é informação proprietária — é tudo público e legível.

Isso não é prompt engineering, e não é o agente "ficando mais inteligente" magicamente — é o agente reescrevendo a própria base de conhecimento dele, sempre com a permissão do usuário.

Semana passada, o Hermes Agent chegou ao primeiro lugar do ranking global de uso de tokens pela OpenRouter, ultrapassando Open Claw, Kilo Code, Claude Code e Descript. Mas isso não deve ser tratado como hype sem ressalvas.

## Ressalva: ganho específico de domínio

Quando o Hermes (ou qualquer agente parecido) gera uma skill, essa skill nasce super específica — por exemplo, "sumarizar uma PR do GitHub". Ela não generaliza para algo como "planejar uma migração de banco de dados conforme os últimos pull requests". Tentar fazer isso vai comprometer o projeto. Esses agentes são ótimos para os ~80% do trabalho repetitivo do dia a dia — planejar uma migração de banco de dados não é um desses casos.

## Construir por conta própria vs. usar o Hermes pronto

Dá para construir um agente equivalente por conta própria, mas é preciso prestar atenção em como organizar a memória. Esses agentes normalmente têm três camadas de memória:

1. **Memória de sessão** — a conversa atual, igual à memória do Codex ou do Claude Code.
2. **Persistent memory** — um `memory.md` que armazena e cura dados entre agentes e sessões (quem já usa alguma orquestração de agentes já tem isso).
3. **Skill memory** — os padrões identificados e extraídos como skills, indexados por um `.md` próprio.

Tudo, no final, é um arquivo `.md` — até a Anthropic "nos convencer que devemos usar HTML para torrar mais token" (ressalva irônica do autor, assunto para outro vídeo). Mas é preciso indexar esses arquivos. O Hermes, por exemplo, usa **FTS5** do SQLite (citado como "o banco de dados que eu mais amo") para fazer busca full-text sobre a sumarização feita por LLM quando o contexto começa a crescer.

O resultado prático: o agente aos poucos passa a lembrar, por exemplo, que você odeia NPM, depois de três sessões.

## Messaging gateway: onde a confusão com o Open Claw aumenta

Para competir com o Open Claw, o Hermes também adicionou um messaging gateway — e é aqui que mora a confusão entre duas coisas diferentes: usar algo para facilitar o processo de desenvolvimento de software versus usar algo para organizar a vida da pessoa. Nessa segunda frente (organização de vida), a Anthropic tem ganhado força — o app da Anthropic já ofereceu conectar o Apple Health para monitorar saúde pelo Claude. A leitura do autor: as empresas não conseguem mais focar só em eficiência de trabalho — todo mundo está competindo para ser o próximo "Jarvis".

Assim como o Open Claw, o Hermes permite conectar várias plataformas de mensagem — o que não é trivial de implementar manualmente. Uma arquitetura de referência para isso, na visão do autor:

- Múltiplos apps de origem (Telegram, Discord, Slack, WhatsApp) mandam mensagens para um **gateway/middleware** único.
- Esse gateway armazena cada sessão por chat (uma sessão por conversa/canal).
- A partir do gateway, **controllers** fazem a escrita nas três camadas de memória (sessão, persistente, skill).

Não é um código-fonte complexo, segundo o autor — a complexidade está na organização, não na implementação.

## A grande pergunta em aberto

Vale a pena construir tudo isso manualmente, ou é melhor usar o que a Anthropic está lançando (Dreaming with Claude)? O maior problema de depender de uma solução da Anthropic é o lock-in a um único fornecedor. A vantagem de montar (ou usar um fork do) Hermes é não ficar preso a um único provedor — dá para usar com GPT, Claude, Gemini etc., hospedando você mesmo na sua VPS.

## Fechamento

O autor reage a um tweet que dizia que "o prazer de criar software tinha acabado" — a pessoa relatava que o sentimento de estar sempre aprendendo algo novo havia desaparecido. Discorda: nunca se aprendeu tanta coisa nova todos os dias como agora, com essa nova era de agentes deixando de ser "burros", deixando de esquecer tudo ao final de uma sessão, aprendendo a se autotunar, acumular conhecimento e gerar arquivos sob controle do usuário.

Reforça um ponto já defendido antes no canal: documentação desatualizada é pior do que ausência de documentação. No mundo de agentes de IA, tudo é documentação — tudo é `.md`. As técnicas que estão surgindo para o agente entender onde parou, criar guard rails para não "fazer cagada" sozinho, são importantes.

Encerra pedindo comentários sobre o uso de Hermes vs. Open Claw e lembrando, mais uma vez, o espectador de se hidratar.
