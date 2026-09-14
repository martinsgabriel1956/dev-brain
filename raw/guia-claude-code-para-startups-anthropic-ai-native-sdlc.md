# Guia do Claude Code para Startups (Reação da Anthropic sobre Startups Nativas de IA)

> Transcrição de vídeo do YouTube, em português, de um criador de conteúdo focado em startups/tech founders (menciona o "Stupid Button Club", uma comunidade fechada para tech founders). Reação/comentário sobre um relatório/playbook publicado pela Anthropic com entrevistas a mais de uma dúzia de startups de rápido crescimento sobre como elas operam usando Claude Code. Colada diretamente pelo usuário no prompt, sem arquivo de origem preexistente.

## Abertura

Deixa eu te ouvir um pouco sobre o que você imagina do futuro do trabalho — não precisa nem pagar uma consultoria, você pode simplesmente ir lá e escutar o que a Anthropic tem a dizer. Na verdade, eles fizeram uma pesquisa de como funcionam os princípios operacionais de dezenas de empresas que estão crescendo absurdamente usando o Claude Code. Vamos dar uma olhada nesse relatório de entrevistas que a Anthropic fez com startups de crescimento.

**Título do relatório (paráfrase):** "AI natives working at the frontier" — se você quiser dar uma espiada no futuro do trabalho, pergunte às startups como elas estão operando hoje. Foi o que a Anthropic fez: conversaram com mais de uma dúzia de startups de rápido crescimento.

## Resultados citados no relatório

- Empresas realizando entregas (envios de código) como organizações **10x maiores** do que elas realmente são.
- **ClickHouse**: 30% a mais de funcionalidades avançadas entregues.
- **Clay**: 100% de triagem de bugs automatizada.

### Paralelo pessoal do autor: triagem automática de bugs na Persoa

O autor relata que já implementou algo parecido na própria empresa (Persoa). Quando um usuário manda e-mail para `help@persoa.com`, um "Grockbot" (bot próprio) lê o e-mail, cruza com o código para checar se é uma falha real do produto, troca e-mails com o usuário (inclusive analisando anexos), analisa o código-fonte e cria issues automaticamente para implementação futura. O bot também consulta o **Sentry** para verificar se já existe registro do erro reportado. Resultado: a triagem de bugs é feita de forma automática. O gargalo passou a ser outro: o autor relata ter ~12 issues criadas e falta de tempo para implementar e testar todas.

- **Artemis Security**: mais de 6.000 PRs (pull requests) por semana.

## A pergunta central do vídeo

Pergunta levantada no relatório: *"Como seria uma organização que montou o ciclo de produto com Claude Code desde o zero?"*

Resposta do autor: seria uma organização fadada a ficar fora do ar quando a Anthropic tiver um *outage*. Ele cita que nos últimos 30 dias a Anthropic teve mais de 20 *outages* — o Claude (a versão comercial, não a versão para o governo) ficou indisponível em algum grau quase uma vez por dia. Conclusão do autor: quem monta o ciclo de produto 100% em cima do Claude Code sem plano de contingência "está ferrado" (*"you are fucked"*) se a Anthropic tiver problema.

## As regras do playbook da Anthropic

O autor enfatiza que o material **não é um tutorial de prompt** — é um playbook construído com base em quem está de fato construindo empresas hoje.

### Regra 1 — Everyone ships (todo mundo entrega código)

A barreira para colocar código em produção caiu: quem entende o problema consegue modificar e colocar um fix, não necessariamente quem entende profundamente o código. O autor chama isso de "o terror de muitos devs".

**Depoimentos citados no relatório:**

- Co-founder da **Paraelp** (nome citado como "Parael"/"Paraelp" na fala — grafia incerta): não é só engenheiro fazendo *commit*; pessoas não técnicas também, por exemplo em mudanças de UI e melhorias de produto.
- **Ryan**, da **Crossby**: "Claude Code mudou o que significa ser advogado" — o advogado da empresa tem o melhor insight de produto porque ele é o usuário. Frase citada: *"it's been amazing to watch them cook"*.
- **Thomas**, do **Heid** (CEO): *"For us, Claude Code solved the broken telephone problem"* — o "telefone sem fio" morreu. Antes, a ideia de quem pensou (PM, designer, engenheiro) levava semanas para chegar no ar e chegava diferente do que foi pensado. Agora quem entende o problema abre o pull request; designers e engenheiros entram onde a expertise deles realmente importa.

**Opinião do autor sobre o risco:** o perigo está em CEOs/co-founders não técnicos entrando na "vibe" de shipping direto. Contraponto citado: **Tobi Lütke**, CEO da Shopify (um dos homens mais ricos do Canadá, segundo o autor) — ele vem de background técnico, então quando ele mexe em código (ex.: reescreveu partes do GitHub Actions/GitHub num fim de semana e colocou para rodar dentro da empresa, substituindo o GitHub) isso é diferente de um CEO não técnico mexendo em código de produção. O autor observa que **Sam Altman**, em entrevista recente de podcast, passou os primeiros cinco minutos elogiando Tobi Lütke. O autor lembra que a Shopify foi uma das primeiras empresas a adotar agentes de IA pesadamente dentro da empresa e fechou contrato com a OpenAI antes da adoção em massa dessas ferramentas em corporações.

**Comentário do autor sobre "expertise do engenheiro":** se agora PMs, advogados e outras funções não técnicas escrevem código, a expertise do engenheiro passa a ser **revisar código** — o que o autor descreve como algo que ele "sempre amou" fazer, e por isso critica quem só aprova pull requests com "Looking Good To Me" (LGTM) sem revisão de fato.

**Ressalva sobre marketing:** o relatório menciona que ainda existe divisão de trabalho — marketing faz marketing, dev é dev. O que abriu para todo mundo foi o "tweet de zero a um": a ideia virar um protótipo funcional. O autor destaca que o próprio relatório reconhece que dizer "everyone ships" no LinkedIn é bonito, mas na prática não é bem assim em todas as empresas.

### Compartilhamento de skills — ponto de crítica do autor à Anthropic

O relatório também aborda o compartilhamento de "prompts"/configurações entre equipes como uma dor recorrente dentro das empresas entrevistadas. O autor usa isso para criticar diretamente a Anthropic: a empresa insiste que os times usem o `CLAUDE.md`, e o Claude Code não lê o `AGENTS.md` (formato compartilhado que outros agentes de IA — como o Codex, da OpenAI — usam). Isso obriga muitos projetos a manterem os dois arquivos em paralelo.

**Controvérsia no Twitter/X citada pelo autor:** durante a semana do vídeo, **Tobi Lütke** (CEO da Shopify) declarou publicamente que está considerando banir o Claude Code dentro da Shopify até a Anthropic mudar sua posição sobre o `AGENTS.md` e passar a usar o formato compartilhado por outros agentes.

Em resposta, um funcionário da Anthropic identificado como **Tarik** (grafia incerta na fala) se posicionou publicamente agradecendo o feedback e justificando que o modelo Claude é "muito diferente", e que por isso o Claude Code lê apenas o `CLAUDE.md`, não os `AGENTS.md` de outros agentes.

**Contra-argumento do autor:** ele considera essa justificativa "uma balela" (algo sem sentido) — segundo ele, se a lógica fosse essa, cada família de modelo precisaria de um arquivo de configuração próprio, já que modelos diferentes (ex.: Sonnet vs. "Fable", na fala do autor) não são intercambiáveis e um *system prompt* tem impacto grande na performance. Ou seja, a mesma lógica que a Anthropic usa para justificar não ler `AGENTS.md` deveria, por consistência, implicar que nem um único `CLAUDE.md` deveria servir para todos os modelos da própria Anthropic. Conclusão do autor: skill compartilhada de fato é um problema real, e sem ela — segundo o que o próprio estudo mostrou — cada pessoa acaba fazendo do seu próprio jeito, criando bagunça organizacional.

### Regra 2 — Automate the tedium (automatizar o tédio)

Automatizar etapas mecânicas e repetitivas do processo.

**Opinião do autor (risco de automatizar cedo demais):** como empreendedor, ele alerta para o perigo de automatizar com IA um processo que ainda não se sabe se é o processo certo para a empresa. Segundo ele, empresas estão demorando mais para atualizar seus próprios processos justamente porque esses processos já foram automatizados — antes, um processo manual era revisado e evoluía organicamente (etapas deixavam de ser necessárias, o trabalho mudava de forma), mas quando o processo é automatizado cedo demais com IA, a empresa passa a "deixar rodar" sem refletir sobre ele. O autor descreve um cenário em que há tantos *schedulers* e agendamentos automatizados rodando que a própria empresa perde de vista quais processos estão automatizados e o que exatamente a IA está fazendo. O risco citado: se a Anthropic subir os preços ou os créditos da empresa acabarem, a operação para e ninguém sabe exatamente por quê — o que, segundo o autor, é do interesse comercial da própria Anthropic.

*(Segue, no vídeo, um convite comercial do autor para um formulário de feedback sobre estágio de startups e para a comunidade "Stupid Button Club" — conteúdo promocional, não normativo, registrado apenas como contexto do canal.)*

### SDLCs nativos de IA — onboarding acelerado

O relatório descreve que muitas dessas startups em destaque implementaram formas de acelerar a integração ("onboarding") de novos funcionários aos processos de codificação ágeis.

**Exemplo citado: Emergent (menção a "Bookhund"/nome de pessoa incerto na fala)** — no primeiro dia, um novo funcionário configura todo o seu ambiente de desenvolvimento apenas indicando ao Claude o arquivo Markdown correto (equivalente a um `CLAUDE.md` de onboarding).

**Comentário do autor:** antigamente havia um grande trabalho humano de "onboarding buddy" — a pessoa responsável por acompanhar o novo colaborador, montar o ambiente e explicar as ferramentas. Hoje isso já é possível fazer via agente de IA, o que segundo ele facilitou muito o processo.

### Regra 3 — Trust but verify (confie, mas verifique)

Segundo o autor, essa verificação existe justamente para suprir o risco da Regra 2 (automatizar sem saber validar): não é possível automatizar algo que não se consegue verificar. Por isso, antes de automatizar qualquer etapa de um processo, é preciso primeiro definir os **evals** — como validar se a qualidade do output está correta. O autor descreve que isso mudou sua forma de desenvolver produtos: primeiro pensar em como validar se algo tem qualidade, para só depois automatizar o processo.

**Framework citado (paráfrase de um diagrama do relatório):** ao definir um objetivo para a IA, pensa-se em termos de um *evaluator* que verifica as condições; um "Claude Worker" executa a tarefa e testa; o processo fica em loop até que a verificação passe — só então o loop termina. A recomendação prática é pensar em como formular o objetivo (e a condição de verificação) antes de colocar a IA para rodar em loop.

### Regra 4 — Build for rebuilding (construir para reconstruir)

Segundo o autor, nunca se reescreveu tanto código quanto agora — o padrão observado é construir, reconstruir, e reconstruir de novo. Na quarta iteração de reconstrução, o time acaba aprendendo de fato o que precisa ser feito. O custo de escrever código e descartá-lo caiu bastante, o que tornou esse padrão de reconstrução iterativa cada vez mais comum, segundo o autor.

### Regra 5 — Prototype, dog food, productionize (prototipar, testar internamente, colocar em produção)

O relatório descreve a forma como essas empresas constroem: testar o produto primeiro em ambiente de *dogfooding* local com o Claude Code, integrando com outras ferramentas como um "SQL Console" ou um agente citado como "AISRI" (grafia incerta na fala) que têm acesso a outras ferramentas.

**Checklist citado do guia (paráfrase):** "O Claude Code não consegue entender o que não vê." Recomendações:

1. Conectar fontes confiáveis às ferramentas do time diário via **MCP** e CLI.
2. Criar um **marketplace de plugins corporativos**.

**Experiência própria do autor:** ele relata ter feito exatamente isso dentro da própria empresa — com um clique, conectar todas as ferramentas corporativas. Cita como exemplo a conexão entre **Jira** e **Figma**, que mudou bastante a forma de trabalhar; junto com **Google Drive**, tudo integrado via login corporativo (**SSO**). O autor menciona que hoje já existem "plugins próprios" para fazer essa autenticação de forma segura.

## Resumo das 5 regras (conforme citadas pelo autor)

1. Everyone ships.
2. Automate the tedium.
3. Trust but verify.
4. Build for rebuilding.
5. Prototype, dog food, productionize.

Frase de fechamento citada do relatório: *"Startups na vanguarda constroem na vanguarda."*

## Encerramento

Chamada padrão de engajamento do canal (like, comentários) e reforço do convite ao formulário de feedback para startups mencionado anteriormente — conteúdo promocional, registrado apenas como contexto, não como conteúdo técnico do vídeo.
