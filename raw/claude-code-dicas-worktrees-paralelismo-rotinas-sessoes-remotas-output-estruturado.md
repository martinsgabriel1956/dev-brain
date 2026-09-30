# Dicas de Claude Code direto da documentação da Anthropic: worktrees, paralelismo, rotinas, sessões remotas, fork e output estruturado

> **Origem:** transcrição de vídeo em português (brasileiro), colada pelo usuário. Terceiro (e "último por um tempo") vídeo do canal com dicas extraídas da documentação oficial do Claude Code. Autor se refere a si mesmo como "Galego"; canal não identificado. Vídeo gravado por volta do fim de julho de 2026 (o autor diz "não sei se é o último ou um dos últimos de julho").
>
> **Tratamento:** o texto original é uma transcrição automática corrida, sem pontuação. Aqui foi limpo e organizado por tópico, sem alterar o conteúdo. Já estava em português; não houve tradução.
>
> **Termos corrompidos pela transcrição, corrigidos por contexto:**
> - "Cloud Code" / "cloud" → Claude Code / Claude
> - "Entropic" → Anthropic
> - "works", "workthr", "gite", "traço traço work" → worktrees / git worktree / flag `--worktree` (provável)
> - "Playgright" → Playwright
> - "Pidentic" → Pydantic; "ódios" → Zod (validação)
> - "Chrome job" → cron job
> - "PI" → API; "gato de pagamento" → gateway de pagamento
> - "harness de A" → harness de IA
> - "IFN P" → não identificável (possivelmente uma flag da CLI; ver Notas)
> - "Amax" → nome do patrocinador (gateway de pagamentos); grafia incerta
> - "Effective hardness for long agents" → "Effective harnesses for long-running agents" (artigo do blog de engenharia da Anthropic; título inferido)

---

## Patrocínio (início do vídeo)

Integrar pagamentos não é só linkar uma API e receber dinheiro: é preciso pensar em antifraude, retentativa (retry), tokenização, recorrência e split. A maioria dos gateways de pagamento não acompanha o produto e não oferece tudo isso de forma completa. O patrocinador ("Amax") é apresentado como construído para quem integra via API: ambiente de testes, webhook configurável, antifraude com machine learning, gestão de recorrência e split de pagamentos nativo, documentação completa "sem pegadinha". Para quem acompanha o canal, há Pix com taxa zero integrando pela API (link na descrição).

## Introdução

O autor já fez dois vídeos com dicas retiradas diretamente da documentação do Claude Code. Parte da audiência pediu mais ("gostei, aprendi bastante"), parte não aguenta mais ouvir falar de IA. Meio-termo: este é o último vídeo de dicas de Claude Code por um tempo, a menos que surja algo imprescindível.

Todas as dicas vêm da documentação do Claude Code da Anthropic (link na descrição). Embora sejam dicas dadas para o Claude Code, a maioria funciona em contextos parecidos: Codex, OpenCode, qualquer outro harness de IA, Cursor — "porque fundamentalmente todos esses sistemas funcionam meio que da mesma maneira".

## Dica 1 — Worktrees

O Claude Code tem uma flag própria para worktrees (`--worktree`, dita "traço traço work"): com ela, a ferramenta cria um git worktree.

A ideia: uma sessão do Claude Code implementa a feature A e outra sessão implementa a feature B. Você não quer que elas entrem em conflito: podem editar o mesmo arquivo, se confundir, ou uma pode fazer um commit e acabar commitando coisas incompletas da outra. Separando em duas worktrees, existem duas versões do código no computador e cada sessão do Claude Code trabalha numa versão diferente; os arquivos não entram em conflito.

## Dica 2 — Paralelismo

Existem várias maneiras de paralelizar trabalho no Claude Code:

- **Dois terminais:** abrir a CLI em dois terminais diferentes; agem de forma paralela.
- **Subagentes:** dentro de uma única sessão, cada subagente trabalha numa tarefa diferente.
- **Agents View:** você entrega tarefas individuais e visualiza os resultados depois.
- **Agent Teams:** o Claude planeja e supervisiona um grupo de trabalhadores; você orquestra times de sessões diferentes do Claude Code que podem interagir entre si. **Feature experimental — cuidado.**
- **Workflows dinâmicos / customizados:** um script com um plano que segue um determinado fluxo de trabalho.

Resumo fácil, segundo o autor: em **subagentes**, o Claude delega e coleta os resultados dentro de uma única conversa; na **Agents View** você entrega tarefas individuais e visualiza depois; em **Agent Teams** o Claude planeja e supervisiona um grupo de trabalhadores; no **workflow customizado** há um script com o plano a seguir. Segundo a Anthropic, cada um tem um objetivo próprio.

Ressalvas importantes:

1. **Custo:** o paralelismo aumenta o custo muito rápido. Rodando em paralelo você produz ~duas vezes mais tokens, e isso custa ~duas vezes mais.
2. **Atenção humana:** você continua sendo uma única pessoa; existe um limite do quanto você consegue prestar atenção em tudo.
3. **Agent Teams e arquivos em comum:** a recomendação é quebrar o trabalho de modo que não existam arquivos em comum entre dois colegas do time. Se um trabalha na feature A e outro na B (ou partes de A e B) e há um arquivo comum, um pode sobrescrever o outro.

## Agendamento de tarefas (número da dica não identificável na transcrição)

- `/loop` faz algo rodar recorrentemente no seu computador.
- Também é possível rodar coisas dentro da cloud da Anthropic: agendar ("a cada uma hora eu quero que você rode os testes…") e automatizar o trabalho com uma rotina recorrente em determinado horário.
- Exemplos de tarefas: health check que alerta se a API tiver erro; revisar os pull requests abertos. "Como se fosse um cron job."
- Se for complicado fazer pela CLI, dá para fazer na web: no Claude Code web, em `/code/routines` você cria uma rotina nova, conecta o GitHub (ou o que for necessário para a tarefa) e a tarefa é executada.

## Dica 7 — Browser

É possível integrar o Claude Code com o Google Chrome. Isso permite testar modificações do aplicativo web e depurar (debug) sem precisar ficar mudando de contexto. Também é possível integrar o MCP do Playwright para o Claude manipular o Playwright; também funciona.

## Dica 8 — Computer Use

Dica "meio estranha", mas o autor diz que muita gente já sabe: dá para deixar o Claude Code manipular o seu computador. Existe uma flag interativa ("IFN P" na transcrição) e outras maneiras de atingir o objetivo. Ativa-se o **MCP Computer Use**, que permite ao Claude Code manipular a tela e o mouse e tomar ações no computador. O autor não tem certeza se já funciona em outros sistemas além do macOS. "Isso aqui é meio loucura, mas existe."

## Dica 9 — Sessões remotas

Ao fazer um refactor muito grande, ou construir algo que vai demorar, as sessões do Claude Code ficam armazenadas na sua máquina (como no vídeo anterior), mas dá para iniciar uma **sessão remota**, disponível de forma mais global. Isso permite rodar tarefas de maneira remota e contínua.

- Segundo a documentação (especificando o desktop app): no aplicativo do Claude Code (não na CLI), em "Local" dá para mandar rodar na cloud ou configurar um **Remote Control**.
- **Remote Control:** executa na sua própria máquina, mas você monitora por outro dispositivo — por exemplo, deixar o PC ligado rodando e monitorar pelo smartphone quando está fora de casa.
- **Disclaimer do autor:** nunca fez isso e não recomenda, porque não acha um hábito saudável monitorar o Claude Code do celular ("você já trabalha 8 horas por dia… não precisa ficar na academia promptando o Claude Code"). "Mas se quiser, tá aí."

## Dica — Fork de sessão

Sessões foram comparadas a branches/commits do GitHub. É possível fazer um **fork** de uma sessão: por exemplo, durante um refactor grande, em determinado ponto não se sabe qual caminho resulta no melhor código; faz-se o fork, dividindo a sessão em duas. O fork cria uma **nova sessão com uma cópia exata da sessão atual**.

Demonstração: na sessão atual, digitar `/fork` (barra fork) e pedir algo na sessão forkeada; ele cria o fork e retorna o ID da sessão. O fork **spawna um subagente** (mostrado embaixo) que trabalha nisso enquanto a sessão original permanece intacta. Assim criam-se dois caminhos diferentes e, em algum momento, pode-se usar só um deles.

## Dica — Output estruturado

Mais útil quando se usa o **SDK** ou se constrói uma aplicação em cima do Claude: o backend manda uma request para a Anthropic e obtém algo de volta, e é possível **especificar exatamente a estrutura** em que isso volta, inclusive usando bibliotecas de validação.

- No exemplo de código da Anthropic usa-se **Zod** (TypeScript) ou **Pydantic** (Python).
- O exemplo define um output estruturado com campos como `feature name`, `summary`, `steps`, etc. Esse `feature plan` do Zod é transformado em **esquema JSON**, enviado à Anthropic; a Anthropic responde nesse formato; depois valida-se com Zod. Dessa forma o output vem estruturado como se quer.
- Opinião do autor: não acha isso super útil ao usar o Claude Code localmente, mas dentro de uma aplicação pode fazer sentido — por exemplo, construir um orquestrador de agentes, ou algo que quebra tarefas muito complexas usando por baixo dos panos o ferramental da Anthropic.

## Referência final — blog de engenharia da Anthropic

Se estiver muito interessado: `anthropic.com/engineering` — o blog de engenharia da Anthropic, com artigos muito interessantes, por exemplo "Effective harnesses for long-running agents" (harnesses efetivas para agentes que rodam por um longo período).

Para quem está avançado nesse mundo e mira trabalhar numa big tech de forma internacional, pode ser útil — não porque vá usar esse conhecimento no dia a dia, mas porque vai conseguir **conversar sobre isso**, o que é valioso em momentos de contratação e ao conhecer pessoas que fundam startups nesse âmbito: "saber conversar com o Vale do Silício é muito bom se você quiser ser contratado pelo Vale do Silício".

## Encerramento

Cursos do canal (links na descrição). "Vamos dar um tempinho de Claude Code."
