# 7 Coisas Que Desenvolvedores Estão Fazendo em 2026 Que Pareceriam Loucura Há Três Anos

> Tradução do artigo original em inglês "7 Things Developers Are Doing in 2026 That Would Have Looked Insane Three Years Ago", de Max Lorian (assina como "Maxime", engenheiro de software sênior), publicado em 12 de setembro de 2026 na publicação The Coding Front (Medium).
> Fonte: https://medium.com/@the.coding.front/7-things-developers-are-doing-in-2026-that-would-have-looked-insane-three-years-ago-1c9b46db719c
> Tradução feita para fins de estudo.

---

## O desenvolvimento de software ficou estranho mais rápido do que qualquer um esperava.

Três anos atrás, o GitHub estava lançando o Copilot Chat para que desenvolvedores pudessem fazer perguntas sobre código sem sair do VS Code. Aquilo já parecia bem futurista na época. Em 2026, o GitHub consegue revisar um pull request escrito por um bot e, se o dono do repositório habilitar, o Copilot também pode aprovar a droga do PR. Passamos 2023 nos perguntando se o autocomplete nos deixaria preguiçosos. De alguma forma, enquanto todo mundo discutia isso, o desenvolvimento de software foi parar numa sala muito mais estranha.

Uso agentes de codificação há tempo suficiente para que boa parte disso já pareça normal, o que talvez seja a coisa mais estranha nisso tudo. Esqueça o hype por um minuto, esqueça os lançamentos de modelos, e olhe o que os desenvolvedores estão fazendo hoje. Junte esses comportamentos e "ferramentas de codificação melhores" passa a soar como uma descrição bem pobre do que realmente aconteceu.

## 1. Dar um ticket para o software e ir cuidar de outra coisa

Esse ainda me quebra um pouco a cabeça. Você pode atribuir uma issue ao GitHub Copilot, mencionar o Cursor a partir do Slack ou do Linear, ou passar uma tarefa para o Codex, e então... ir embora. O agente recebe um ambiente de desenvolvimento, edita o repositório, roda comandos, testa o resultado, abre um pull request e espera você voltar — como um terceirizado que de alguma forma mora dentro da AWS.

Pense em como isso soaria bizarro em 2023. IA para codar significava digitar algo, ver o texto aparecer e decidir se você confiava o suficiente nele para colar no editor. Você estava presente durante toda a troca. Agora, ir embora faz parte da funcionalidade, e o momento em que consigo dar uma tarefa a um software, ir tomar café, entrar numa reunião ou trabalhar em outra coisa, é o momento em que estou fazendo algo diferente de usar um assistente de codificação. Eu deleguei trabalho a algo. Chame de agente, de trabalhador, de processo ou de um shell script muito caro com opiniões próprias. Eu fui embora mesmo assim, e ele continuou trabalhando.

Isso cria uma pergunta incômoda para todo o vocabulário de "assistente de codificação com IA". Assistentes, em geral, assistem enquanto você faz algo. Um sistema trabalhando na sua ticket enquanto você discute prioridades de roadmap em outra sala soa mais como delegação. Passamos anos debatendo se a IA pode substituir desenvolvedores enquanto ficávamos cada vez mais confortáveis com a IA fazendo pedaços de trabalho no formato de desenvolvedor sem que ninguém observasse.

## 2. Fazer quatro IAs resolverem o mesmo problema e escolher a vencedora

Por anos, trabalho duplicado de implementação era algo que gerentes de engenharia tentavam eliminar. Aparentemente as máquinas reabriram a negociação. O Cursor agora permite que desenvolvedores enviem o mesmo problema para múltiplos modelos em paralelo, cada um isolado em sua própria worktree, e depois comparem os resultados e fiquem com o melhor. Soa como desperdício até você lembrar o que está sendo desperdiçado no lugar de tempo humano: computação.

Fazer quatro engenheiros implementarem independentemente o mesmo ticket te renderia uma reunião com alguém segurando uma planilha. Dar a tarefa a quatro modelos e, de repente, a conta fecha. O Claude ganha uma branch. O Codex ganha uma branch. Outro alguém ganha uma branch. Brigem entre si, eu confiro depois.

Produzir uma implementação pode ficar barato o suficiente para que escolher se torne mais importante do que produzir. Agora você tem quatro versões da mesma feature e precisa descobrir qual delas entendeu errado a arquitetura, inventou uma abstração que ninguém pediu ou deixou uma granada escondida em algum lugar do tratamento de erros. Três anos atrás, "ser bom em programar" significava ser capaz de produzir a resposta. Estamos construindo fluxos de trabalho em que obter respostas é fácil e saber qual delas merece sobreviver é a habilidade que importa.

## 3. Escrever documentação para funcionários que não existem

Repositórios estão ganhando arquivos com nomes como `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` e `copilot-instructions.md`. Eles explicam a arquitetura, regras de teste, convenções, exceções e como um agente deve se comportar quando entra em um diretório específico. O GitHub consegue até fazer o Copilot gerar instruções que depois vão ensinar o próprio Copilot a trabalhar dentro do repositório, o que dá a sensação de que a documentação finalmente aprendeu a se reproduzir.

Passamos anos escrevendo bases de código para duas audiências: o computador que executa o código e os humanos com o azar de precisar mantê-lo. Agora existe uma terceira audiência. Agentes precisam saber o que pode mudar, como testar, quais fronteiras importam, qual comando realmente funciona (apesar do que o README diz) e onde o Dave escondeu aquele script de build amaldiçoado em 2021.

Um repositório amigável a IA tem regras que máquinas conseguem descobrir e verificações que avisam quando uma regra foi quebrada, em vez de um prompt gigante colado na porta da frente. Um processo de build vivendo inteiramente na cabeça do Dave costumava virar problema quando o Dave saía de férias. Agora vira problema toda vez que um agente toca o sistema. Todo aquele trabalho chato de engenharia que a gente ia adiando porque humanos conseguiam contornar a bagunça ganhou um cliente sem o menor bom senso.

Acho isso bem engraçado. A IA prometia nos deixar escrever software mais rápido escapando de certas responsabilidades, e uma de suas primeiras exigências é basicamente: por favor, arrume seu quarto.

## 4. Dar à IA o seu próprio computador

Um assistente de codificação costumava ficar do lado do seu editor. Agentes na nuvem agora ganham máquinas virtuais com terminais, navegadores, dependências, credenciais, acesso à rede e, no caso do Cursor, um desktop que eles conseguem operar. Eles conseguem abrir a aplicação que acabaram de modificar, clicar dentro dela, coletar screenshots ou vídeo, decidir se o resultado funcionou e continuar corrigindo. Estamos provisionando computadores para software agora, frase que eu provavelmente teria usado para fechar uma piada em 2023.

Uma vez que o agente tem uma máquina, discutir se o Claude ou o Codex tem a melhor pontuação de codificação começa a parecer incompleto. Eu me importo com quais credenciais essa coisa recebe. Eu me importo com onde ela pode se conectar, o que ela pode executar, quanto tempo o ambiente sobrevive, o que fica registrado em log e se alguém consegue reconstruir o que aconteceu depois que ela faz alguma besteira. O modelo mais o ambiente que entregamos a ele é a coisa que de fato colocamos em produção.

Times de segurança passaram anos tentando impedir que software aleatório ganhasse controle sobre máquinas de desenvolvedores. Agora times de engenharia estão construindo software especificamente para que ele inspecione uma máquina, use o terminal, navegue na web, toque em credenciais e escolha sua próxima ação sem perguntar a um humano sobre cada comando. Leia essas duas frases juntas e dá quase para ouvir um engenheiro de segurança abrindo uma garrafa.

E não estou fazendo o ponto barato de "IA é perigosa". Dar mais autonomia a agentes é exatamente o que os torna úteis. Um agente de codificação que pede permissão a cada doze segundos é só um autocomplete carente com um shell. A versão útil precisa de liberdade, e a versão útil, por isso mesmo, cria um problema de permissões muito mais interessante. Parabéns, deixamos o produto melhor e o modelo de ameaça pior ao mesmo tempo.

## 5. Pedir para a IA revisar código escrito por IA

Esse talvez seja meu favorito porque soa como a premissa de uma piada ruim de gestão. O GitHub Copilot consegue revisar pull requests escritos por bots, incluindo o próprio agente na nuvem do Copilot. Ele também consegue produzir uma avaliação de aprovação e, quando administradores do repositório habilitam a funcionalidade, aprovar o pull request. Chegamos ao robô checando o dever de casa do robô, e de alguma forma só fica mais estranho quando você percebe que a ideia faz sentido.

Agente escreve mudança. Outro agente revisa a mudança. CI testa a mudança. Agente lê a falha. Política decide se o resultado pode ser mesclado. Humano é chamado quando algo sai dos trilhos. Claro que alguém ia construir isso. Se código pode ser gerado mais rápido do que humanos conseguem revisar, "vamos inspecionar cuidadosamente cada linha gerada" tem prazo de validade.

A revisão de código então começa a se transformar em outra coisa. Você se importa com o patch, obviamente, mas também se importa com a maquinaria que decide quais patches merecem atenção humana. Quais mudanças um agente pode aprovar? Quais diretórios exigem uma pessoa? Que tipos de falha bloqueiam o pipeline? Quão independente o revisor precisa ser do autor? De repente, as decisões de revisão interessantes estão acontecendo antes de alguém sequer abrir o pull request.

Movemos o humano um andar acima e deixamos duas máquinas no andar de baixo discutindo sobre TypeScript.

## 6. Rodar agentes de codificação como cron jobs

O Cursor Automations consegue rodar a partir de agendamentos ou eventos como uma mensagem no Slack, um ticket no Linear, um pull request mesclado no GitHub ou um incidente no PagerDuty. A Faire diz que roda mais de 2.000 jobs semanais de agentes autônomos para investigação de CI, correção de bugs e revisão de código. A Amplitude diz que roda mais de 1.000 por semana, com 60% a 70% dos pull requests de baixo risco indo direto para produção.

Esqueça a palavra IA por um momento e leia o fluxo de trabalho. Um evento de produção acontece. Software acorda, examina uma base de código, decide o que deveria mudar, escreve a mudança, testa e manda pelo pipeline de desenvolvimento. Empurramos um programador para dentro de um event handler, que talvez seja uma das minhas peças favoritas de arquitetura acidental a sair de toda essa confusão.

Chamar esses sistemas de "assistentes" fica ridículo rapidamente. Assistentes esperam por você. Essas coisas conseguem acordar porque o PagerDuty gritou às 3h12 da manhã, alguém moveu um ticket no Linear ou outro software mesclou um pull request. Nenhum desenvolvedor abriu uma janela de chat. Nada começou com "por favor, me ajude".

Automação de software costumava funcionar lindamente quando conseguíamos descrever a próxima ação com antecedência. Evento acontece, executa operação conhecida. Agora as pessoas estão inserindo algo capaz de escolher a operação. O branch no fluxo de trabalho não é mais `if status === failed`; às vezes é um modelo olhando para a situação e decidindo o que diabos fazer.

Consigo entender por que empresas querem isso em todo lugar. Também já consigo ver o relatório de incidente: um agente reagiu corretamente à interpretação exatamente errada de um evento e depois fez isso 600 vezes antes do café da manhã. Sistemas distribuídos já estavam ficando perigosamente previsíveis mesmo assim.

## 7. Construir software em que humanos não escrevem nenhuma linha de código

A OpenAI passou cinco meses construindo e lançando um produto interno sob uma restrição ridícula: zero código escrito manualmente. Lógica de aplicação, testes, CI, documentação, observabilidade e ferramentas internas foram todos produzidos pelo Codex, chegando eventualmente a um milhão de linhas. Os engenheiros descrevem o próprio trabalho como desenhar ambientes, especificar intenção e construir loops de feedback que permitem aos agentes trabalhar.

IA escrevendo código sempre foi fácil de prever. O Copilot já conseguia gerar código há três anos; fazer os pedaços gerados ficarem maiores não exigia clarividência. Redesenhar todo o processo de desenvolvimento partindo da suposição de que humanos podem nunca escrever a implementação é bem mais estranho.

Olhe tudo que os desenvolvedores tiveram que construir em volta desse milhão de linhas. Arquitetura ainda importa. Fronteiras ainda importam. Testes precisam significar alguma coisa. Ambientes precisam se comportar. Observabilidade precisa dizer a verdade. Alguém precisa ter julgamento suficiente para notar quando um agente produziu código que funciona perfeitamente e nunca deveria ter existido. Tire a digitação e uma quantidade incômoda de engenharia de software continua de pé.

Parte disso fica mais difícil. Um desenvolvedor humano consegue notar um padrão estranho enquanto escreve o código, lembrar de um incidente feio de dois anos atrás, ir até outro engenheiro ou simplesmente se sentir desconfortável com uma mudança. Um agente consegue gerar mais dez mil linhas antes do almoço. A capacidade de produção sobe, o que soa fantástico até você lembrar que defeitos, duplicação, más abstrações e desvio arquitetural também são formas de produção.

Por anos, digitar código foi a prova visível de que engenharia estava acontecendo. Juniores praticavam isso. Entrevistas testavam isso. Desenvolvedores construíam identidades em torno de linguagens, editores e o pequeno prazer de saber exatamente o que um trecho de sintaxe faria. Agora a produção de código está sendo separada do resto do trabalho, e estamos tendo uma visão bem mais clara do que sobra por baixo.

Em 2023, o GitHub chamava o Copilot de "par de programação com IA" e desenvolvedores ficavam empolgados em conversar com ele dentro da IDE. Em 2026, empresas estão rodando frotas de agentes, entregando computadores a eles, escrevendo documentação para eles, deixando-os revisar o trabalho uns dos outros e construindo software em que humanos nunca digitam a implementação. Três anos. Fizemos tudo isso em três anos.

"Gerente de agentes de IA" parece um título organizado demais para onde isso está indo. Estamos desenhando a fábrica, escrevendo as regras, decidindo quais máquinas podem tocar quais alavancas, construindo alarmes para quando elas ficarem criativas e pulando para o chão de fábrica quando a autenticação de alguma forma pega fogo. Depois voltamos para o andar de cima e damos a elas mais uma alavanca.

Até 2029, eu suspeito que algumas coisas neste artigo vão soar como alguém se maravilhando porque um telefone consegue acessar e-mail. E dado como 2026 está indo, não tenho tanta certeza de quais.

> Eu sou o Maxime, um engenheiro de software sênior acompanhando a guerra da codificação por IA.
