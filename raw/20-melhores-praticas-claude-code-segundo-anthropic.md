# 20 melhores práticas de Claude Code segundo a própria Anthropic

## Introdução

A Anthropic tem, dentro da própria documentação do Claude Code, uma biblioteca inteira de prompts prontos para copiar e colar, além de explicações sobre workflows comuns que funcionam para diferentes tipos de tarefa. Após ler toda essa documentação — que é extensa, páginas e mais páginas — foram extraídas de 20 a 30 melhores práticas. Todas elas, de uma forma ou de outra, vêm dessa documentação oficial do Claude Code, mesmo quando não citada diretamente a cada ponto.

## 1. Coloque o método de verificação no próprio prompt

Ao pedir para o Claude Code executar uma tarefa, inclua também como ele deve verificar se o resultado está correto — por exemplo, rodar testes, ou comparar screenshots. A própria documentação da Anthropic dá exemplos: uma função `validateEmail` com casos de teste (`user@mail.com` deve ser verdadeiro, `user@.com` deve ser falso), ou fornecer um print e pedir: "Implemente esse design, tire um print do resultado, compare com o original, liste as diferenças e corrija-as."

## 2. Descreva o estado desejado, não os passos

Em vez de prescrever a sequência de ações que o Claude Code deve tomar, descreva o resultado final que você quer. Isso está na própria biblioteca de prompts do Claude Code: diga o que você quer e deixe o Claude Code encontrar os arquivos e o caminho. Um bom prompt funciona sem nomear um único caminho de arquivo.

## 3. Faça refatorações em pequenos incrementos testáveis

Dentro da documentação, na seção de fluxos de trabalho comuns, a recomendação é sempre trabalhar em pequenos incrementos que possam ser testados a cada passo, em vez de tentar uma refatoração grande de uma vez só. A documentação também aborda receitas de prompt, como retomar conversas anteriores, executar sessões paralelas com worktrees, e separar planejamento de edição.

## 4. Interrompa o Claude Code se ele estiver no caminho errado

Se o Claude Code estiver com premissas erradas ou fazendo algo do jeito errado, quanto antes você interromper e redirecionar, melhor.

## 5. Prefira regras concretas e pequenas a regras genéricas

É melhor referenciar comandos específicos, documentações específicas, specs específicas, e bordas entre serviços específicos, da maneira mais sucinta possível. Isso funciona muito melhor do que instruções vagas como "utilize Clean Code". Uma regra de projeto específica (por exemplo, "sempre que for acessar uma URL, faça de tal maneira, utilize tal lib ou tal classe") gera outputs mais precisos.

## 6. Use contexto novo para tarefas não relacionadas

Dentro da shell interativa do Claude Code existe o comando `/clear`. Quando uma nova tarefa não tem relação com o restante da conversa, é recomendado limpar o contexto (ou usar um subagent) para que essa tarefa tenha um contexto específico, sem poluição de assuntos anteriores não relacionados. A própria Anthropic recomenda contexto novo para tarefas não relacionadas com a tarefa anterior.

## 7. Fique no menor diretório possível

Inicie a shell interativa do Claude Code no menor diretório possível que resolva a tarefa. Em um monorepo com frontend e backend, se a tarefa é só de backend, é melhor instanciar o Claude Code diretamente na pasta do backend, em vez do monorepo inteiro — isso também reduz o contexto necessário. Quando a tarefa realmente cruza fronteiras (por exemplo, frontend que acessa uma API do backend), aí sim inicia no monorepo como um todo.

## 8. Em modelos mais fortes, foque em resultado, limitações e evidências

Nos modelos mais pesados (como o Fable), é mais interessante concentrar o prompt no resultado desejado, nas limitações e nas evidências de sucesso do que prescrever uma sequência de ações. É o mesmo princípio do item 2, mas reforçado: quanto mais poderoso o modelo, melhor essa abordagem funciona — a documentação menciona isso especificamente para o Fable 5.

## 9. Use modelos mais fortes para tarefas de maior alavancagem

A recomendação da Anthropic é usar os modelos mais poderosos (como o Fable) para tarefas de planejamento e arquitetura — tarefas de alta alavancagem (leverage). Para tarefas mais rotineiras e simples, modelos mais leves bastam. Um workflow possível: usar um modelo forte para criar uma spec, um modelo intermediário para quebrar isso em tarefas menores, e o Sonnet (ou vários subagents de Sonnet) para implementar as tarefas.

## 10. Use checkpoints e o comando rewind

A documentação do Claude Code explica sobre checkpoints e o comando `rewind`, que permite voltar a um ponto anterior de uma conversa. Se a conversa foi por um caminho ruim a partir de determinado momento, dá para voltar para o ponto anterior sem descartar tudo — diferente de depender só do Git para reverter para um commit específico, o rewind permite voltar a um ponto no meio de uma conversa.

## 11. Gerencie sessões e retomada de sessões

O Claude Code salva sessões localmente e oferece comandos para nomeá-las, continuar a partir delas, ou trocar entre elas. Se uma tarefa está no meio do caminho e será retomada depois, vale usar `/rename` para renomear a sessão e facilitar encontrá-la depois. Para retomar, usa-se `claude --resume` (ou equivalente) com o nome da sessão, recuperando todo o histórico e contexto. Isso evita o problema comum de, ao voltar para um commit no Git, perder todo o contexto da conversa que levou até aquele commit — simplesmente conversar de novo com o Claude Code não garante que ele "lembre" de onde vocês pararam.

## 12. Use `/go` para objetivos verificáveis de longo prazo

Quando há um objetivo grande e verificável (por exemplo, "crie um PR até zero erros nos testes" ou "faça todos os testes passarem"), o comando `/go` pode manter o Claude Code trabalhando em prol desse objetivo. A documentação, na seção de automação, explica como manter o Claude Code focado nisso.

## 13. Tenha um arquivo dedicado a code review

Existe um arquivo (`review`) que deve conter somente informações pertinentes a fazer code reviews — não informações gerais do projeto (essas ficam no `CLAUDE.md`). Isso mantém o arquivo de review focado. O Claude Code também tem o comando `/code-review`, útil para requests complexos; para código substancial e complexo, a documentação recomenda o effort "ultra".

## 14. Monitore o contexto com `/context`

O comando `/context` permite ver o que está dentro do contexto atual, avaliar se faz sentido, e remover o que não é mais relevante. Administrar o contexto ativamente é uma recomendação recorrente da Anthropic.

## 15. Comite o `.claude` do projeto (não o pessoal)

Existem configurações pessoais do usuário (fora do projeto) e configurações específicas de cada projeto em `.claude/`. As configurações pessoais não devem ser comitadas, mas as do projeto sim — isso permite que toda a equipe trabalhe com as mesmas especificações do Claude Code e possa evoluir esse comportamento em conjunto, fazendo o Claude Code agir do jeito que a equipe quer.

## 16. Configure o modo automático (auto mode) com cuidado

Existe um mecanismo nas configurações de permissões do Claude Code que usa a tecla ESC: certas ações (como um `git push`) podem ser configuradas para exigir permissão explícita mesmo em auto mode. Quem usa bastante o auto mode deve configurar isso deliberadamente.

## 17. Use sandbox para loops não interrompidos

Para rodar o Claude Code em um loop não interrompido (como em "half loops"), a própria Anthropic recomenda ter algum mecanismo de sandbox — geralmente uma VM, container ou dev container — para isolar a execução com segurança.

## 18. Não é preciso nomear ferramentas explicitamente

As ferramentas do Claude Code têm descrições que entram no contexto do modelo, então ele sabe quando deve usar qual ferramenta para atingir um objetivo. Não é necessário, por exemplo, dizer explicitamente "use o Playwright para testar isso" — basta pedir "testa aí no navegador" que o Claude Code infere a ferramenta certa (embora nomear explicitamente também funcione).

## 19. Saiba onde ficam os dados de sessão e por quanto tempo

O Claude Code retém sessões localmente em `~/.claude/projects` por padrão, por 30 dias. Esse período de retenção pode ser alterado. É possível deletar sessões individuais, mas por padrão elas ficam disponíveis nessa pasta por 30 dias para consulta, leitura ou análise.

## Observação final

O criador do vídeo reforça que quase todo o conteúdo apresentado está documentado oficialmente pela Anthropic, e incentiva o espectador a consultar a documentação diretamente em vez de depender só de terceiros (YouTubers, opiniões de outras pessoas) para aprender a usar a ferramenta.
