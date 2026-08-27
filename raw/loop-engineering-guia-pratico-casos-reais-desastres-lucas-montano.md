# Loop Engineering — Guia Prático, Casos Reais e Desastres (transcrição)

> Transcrição de vídeo (fala transcrita automaticamente, sem pontuação/paragrafação original) fornecida pelo usuário em português. Formatada em Markdown para leitura, sem alteração de conteúdo. Sem necessidade de tradução — fonte já em português.

## Abertura

Nesse vídeo eu vou mostrar para vocês como eu estou usando Loop Engineering, que basicamente é uma técnica de uso de inteligência artificial em loop. Já vou mostrar que tem alguns pontos importantes: loop não quer dizer que tu vai usar tudo na mesma janela de contexto — vocês vão entender isso. Mas basicamente é isso a grosso modo: deixar a inteligência artificial desenvolvendo algo muito complexo por dias, ou talvez por semanas, enquanto tu faz qualquer outra coisa. E melhor ainda: tu pode deixar vários loops rodando ao mesmo tempo em worktrees diferentes, e eu vou mostrar isso na prática aqui pra vocês.

Então deixa o like aqui embaixo, se inscreve no canal. A gente está com o novo workshop de IA que vai sair dia 1º de outubro. A gente fez o último workshop agora dia 1º de agosto, foi muito legal, tá gravado, foram 7 horas de workshop utilizando Spec Driven e tudo mais, e a gente vai fazer outro em 1º de outubro. Nesse outro a gente vai mostrar coisas que mudaram, vai falar um pouco de Loop Engineering também. Quem se inscrever agora pra 1º de outubro vai poder ver toda a gravação do último workshop. O link está na descrição.

Vamos lá: Loop Engineering. O que vocês vão ver aqui nesse vídeo: o que é um loop sem enrolação, uma noite de loop volta a volta (como eu tô fazendo, inclusive fiz isso ontem e anteontem — nos últimos 10 dias tenho feito isso), o que já deu certo e o que já deu muito errado, e quando usar spec e quando usar loop. No último vídeo a gente falou sobre spec, agora estamos falando sobre loop — como usar cada um e como funciona.

A ideia numa frase: você não digita mais prompt por prompt. Prepara arquivos e testes, aperta play, e revisa o resultado de manhã. Vocês vão ver isso em quatro blocos: o que é e como roda, casos reais, desastres reais, spec versus loop e qual usar, e monte o seu próprio loop.

## Bloco 1 — O Que É um Loop Engineering

Em 30 segundos: um script roda o agente em círculo. Ele lê a mesma instrução que está no `prompt.md`, faz uma tarefa da lista, roda os testes, se passou comita, se falhou vai anotar ou refazer, zera a memória e recomeça. Toda vez que ele altera algo lá no `prompt.md`, ele coloca lá quando finalizou a tarefa como feita. O próximo loop vai para a próxima tarefa.

O motor são três linhas de bash. A engenharia de verdade está nos arquivos que ele lê. O agente esquece tudo a cada volta, de propósito. A memória fica nos arquivos e no Git, não no chat. Ou seja, a gente sempre vai ter uma memória de contexto nova, zerada — sempre uma sessão nova em headless.

### De Onde Veio

Geoffrey Huntley publicou a técnica em julho de 2025, com o apelido de "Ralph Loop". Em 2026 o nome "Loop Engineering" pegou. Loop Engineering é desenhar esse ciclo: a instrução, a lista de tarefas, os testes e a condição de parada — hora que ele tem que terminar. A gente executa: o trabalho é preparar e revisar.

### Bloco 1 na Prática

Basicamente eu tenho um `fixplan.md` — uma lista de tarefas — e um pouco das regras: "rota POST /tasks, cria tarefa, título vazio, erro 400, GET /tasks que lista as tarefas" e tudo mais. O combinado: o loop roda de madrugada numa sandbox, com um teto de $10, por exemplo, ou um teto de uso — tu vai utilizar todo o limite que tu tem a cada 5 horas. Dá para configurar isso no Claude Code também: tu pode parar por exemplo com 2 horas de limite ainda restante, executar até chegar numa quantidade de tokens que sabe que chega perto de 100% de uso, esperar resetar e depois continuar.

Exemplo de execução real:

- **Volta 1 (11h40)** — pega o primeiro item, escreve a rota mais o teste, os testes passam, comita, risca a rota POST.
- **Volta 2 (11h31 — sic, ordem do relato)** — pega a validação, primeira tentativa o teste falha, corrige, passa, comita, risca.
- **Volta 3** — pega o GET /tasks, testes passam, comita, lista vazia imprime "done", o loop para.

Ou seja: já executei três de manhã, três commits pequenos, um por tarefa. Você lê o diff em 15 minutos, pede um ajuste ou faz o merge. Isso é loop funcionando. Cada volta começa do começo — o plano guarda o progresso, o Git guarda a história.

### Os Quatro Arquivos

1. **`prompt.md`** — a instrução fixa de toda a volta. Ex.: "pegue o item mais importante do fixplan.md, faça só ele, rode os testes, comite."
2. **`fixplan.md`** — a lista com os checks. Você abre todo dia para conferir se andou e se anda na direção certa.
3. **Specs** — o que o projeto deve fazer, em arquivos curtos, escritos antes, com calma (inclusive utilizando Spec Driven). É daqui que sai a lista de tarefas.
4. **`agents.md`** — como rodar build, testes do seu projeto, para o agente não inventar comandos.

### As Três Regras do Prompt

1. Uma tarefa por volta.
2. Procurar antes de criar (proibido duplicar).
3. Proibido placeholder — tudo é texto simples, dá para ver no Git, revisar PR e melhorar toda noite.

### O Gate — Quem Aprova a Volta

O loop só funciona se existir um "passou ou não passou" automático que serve de critério. Exemplos: os testes da rota passam, o build compila sem erro, o lint zera, tirou um print com Playwright e depois comparou se estava exatamente igual. Não serve "deixa o site mais bonito", "melhora a experiência", "deixa o código limpo" — isso não é verificável. Tem que ter critérios de aceite verificáveis.

O agente gera o código, o gate (os testes, os tipos, o lint, os próprios gates mecânicos da skill que tu está usando) decide: se passou, comita; se falhou, volta e corrige. Sem critério automático, o loop passa a noite inteira produzindo lixo com total confiança de que está indo bem. Antes de ligar o loop: escreva o teste que define "pronto". Sem teste, o loop falha.

## Bloco 2 — Casos Reais e Desastres Reais

### O Que Já Saiu de Loop de Verdade

- **Linguagem de programação nova**: um compilador completo, $14.000 investidos numa API. A linguagem não existia no training data — foi criada do zero durante 3 meses num loop.
- **Uma noite**: seis bibliotecas portadas de React para View, de Python para TypeScript — ~11.100 commits, 800 de API.
- **Migração de testes**: testes de 4 minutos migrados para 2 segundos — migração mecânica de testes de integração para unitários.
- **Trabalho de freela**: um contrato de R$ 50.000 entregue com $7 gastos em loop, produzindo um MVP testado e revisado. Custo de API: $297. Caso conhecido pelo autor.

Importante: isso é o teto, não a média. São relatos de quem fez — fracasso não vira post. Use como referência do que é possível, não como expectativa.

### O Que Já Deu Errado — e as Lições

- **Banco de dados apagado (Replit)**: o agente apagou 1.206 registros de produção durante um "não mexe em nada" escrito no prompt, e ainda tentou disfarçar com dados falsos. **Lição**: regra no prompt não é pedido, é bloqueio de verdade — permissão de sandbox deve ser diferente de permissão de produção.
- **Teste trapaceado para passar**: agentes já hardcodaram o valor esperado e até deletaram o arquivo de teste. Quanto maior o código, mais o agente trapaceia para conseguir concluir — quanto mais complexo, mais isso ocupa contexto. **Lição**: leia o diff dos testes e deixe o CI rodando fora do alcance do agente. É por isso que a nossa skill de Spec Driven tem um gate próprio que fica fora da implementação.
- **Produtividade imaginária**: num estudo controlado, devs experientes com IA ficaram 19% mais lentos no próprio codebase, sentindo que estavam 20% mais rápidos. **Lição**: em código conhecido e maduro, o ganho é menor do que parece — meça, não confie na sensação.

### Checklist de Segurança Antes de Rodar

1. **Sandbox** — um container Docker ou uma VM descartável. Credencial de produção nunca entra no ambiente nem nos `.env`.
2. **Git como checkpoint** — branch própria para cada tarefa do loop, commit a cada volta. Verde amanheceu quebrado: `git reset --hard` e segue normal.
3. **Teto de gasto** — `max_budget` e `max_turns`. O loop para sozinho quando estoura, sem surpresa na fatura. Dá para fazer isso também com tempo: calcule quantos mil tokens você consegue usar num Sonnet/Fable dentro da sua sessão de 5 horas, coloque um limite conservador (~70% do máximo estimado). Ao chegar no limite, ele para e continua depois de resetar.
4. **Gates de teste, tipo e lint** — código ruim é rejeitado automaticamente. Em linguagem dinâmica, ligue um type checker.
5. **Hooks determinísticos** — instrução no prompt é conselho, hook executa sempre: pré-commit, scanner de segurança, formatter.
6. **Escopo pequeno** — uma volta por noite, PR pequeno de manhã, incremento que cabe numa revisão de 15 minutos.

Qualquer item dessa lista teria evitado o banco apagado. Nenhum é opcional.

## Bloco 3 — Quando Usar Spec, Quando Usar Loop

### Use Spec + Revisão (Sem Loop)

- Código em produção ou legado — uma mudança errada afeta o usuário de verdade, você aprova cada passo.
- UX/copy — não tem teste automático que diga se ficou bom ou não, então tem que validar sempre no final.
- Decisão de arquitetura — escolhas que travam o projeto por anos não se delegam a um ciclo cego. Use RFC e depois ADR para guardar a decisão.
- Dinheiro e dados no meio — pagamento, migração de dados, julgamento humano em cada linha.

No dia a dia: você escreve a spec, o agente executa uma tarefa, você revisa e aprova, vem a próxima. É o Spec Driven já ensinado no canal — você vê cada mudança, erro vai para revisão, o ritmo é o seu ritmo, não o ritmo do loop.

### Solte o Loop (Com as Proteções do Checklist)

- Projeto novo do zero — nada para quebrar, o pior caso é jogar o branch fora.
- Migração ou porte mecânico — framework antigo indo para um novo, demanda bastante trabalho repetitivo, roda com os gates e testes.
- Zerar fila de erros — testes quebrados, erros de tipo, lint: rodar, corrigir, repetir, auditável.
- Backlog claro com teste — lista de tarefas onde cada item tem critério de aceite automático.

A pergunta que decide: um teste automático sabe dizer se ficou pronto? Se sim, é candidato a loop. Se não, é spec + revisão com você no comando.

### Resumo do Ritmo

Spec de dia, loop de noite. Escreve as specs de dia com calma; da spec sai o `fixplan.md` com critério de aceite. O loop roda de noite na sandbox com teto de gasto. De manhã, PR pequeno, você revisa e ajusta. Spec e plano avançam, repete no próximo dia. Cada um no seu papel: a spec diz o que construir, o teste diz se ficou pronto, o loop só executa — e você decide e revisa.

Sem spec e sem teste, o loop continua rodando, só que produzindo a coisa errada mais rápido — velocidade sem direção é prejuízo. Ritmo saudável: uma melhoria pequena por noite. Melhor acordar com um diff de 200 linhas revisável do que 5.000 impossíveis. Spec = direção, teste = aprovação, loop = execução.

## Bloco 4 — Monte Seu Primeiro Loop

Um exemplo, arquivo por arquivo:

- `prompt.md` — a instrução do loop.
- `specs/` — uma spec por arquivo (ou por pasta, como no Spec Driven).
- `fixplan.md` — tarefas priorizadas.
- `agents.md` — como buildar e testar.

Como o loop termina: imprime "done" e um script encerra, ou limite de voltas, ou `fixplan.md` sem itens abertos — aí o loop pode terminar. Numa sandbox, nunca na sua máquina.

Comece pequeno: projeto de brinquedo, uma noite só, teto de $5, sandbox de $100. Aprenda como seu loop se comporta antes de escalar, antes de rodar com permissões amplas numa noite sem supervisão. Revise o checklist de segurança antes do primeiro play.

## Demonstração Prática

A gente tem algumas formas de usar loop: um arquivo bash que fica chamando o modelo em headless, rodando paralelismo — tudo configurável dentro de um arquivo bash. Não é a opção que eu mais uso. A que eu mais utilizo é direto na nossa skill de Spec Driven, porque já tinha pensado nisso quando lancei a skill — ela teve uma atualização legal recentemente, que não substitui nenhum arquivo de feature, só atualiza a própria skill.

Quando peço para a skill implementar alguma coisa, ela gera as specs automaticamente, me pergunta tudo que está faltando, não deixa nenhum critério ou pergunta em aberto — nunca decide sozinha, como a própria skill já ordena. Com base nisso, ela gera um plano de ação, que já é o próprio loop automaticamente. Quando mando desenvolver, ela paraleliza tudo que consegue, inclusive executando em headless usando `git worktree` — várias coisas tocando no mesmo arquivo, depois mergiando tudo, continuando funcionando normalmente. Rodo isso em loop durante a noite, planos de ação rodando em headless, em sessões separadas da sessão principal.

### Caso Demonstrado: Deploy em Staging via MCP da Hostinger

Vou rodar em loop um deploy da landing page principal (o site) em staging, na VPS da Hostinger, usando o comando `/loop` do próprio Claude Code e o MCP da Hostinger (gerado via chave de API, instalado seguindo a documentação oficial). Já tenho a chave configurada nessa sessão.

O objetivo: subir a landing page desse repositório em staging no meu VPS da Hostinger, servida por HTTP (IP + porta). Critérios de aceite: acesso SSH funcionando, todos os detalhes especificados, critério de parada — "pare o loop e escreva o relatório final quando todas estas forem verdade: as sete rotas do passo sete retornam o status esperado, os assets de `/next` carregam" etc.

Escolhi o modelo Opus no Claude Code (em vez do Fable, que teria dado o melhor resultado nesse tipo de loop agêntico, mas a maioria das pessoas não tem acesso a ele — Opus se encaixa melhor na realidade de mais gente). Coloquei `/loop` no final do prompt, ativei bypass de permissões, e rodei.

Resultado: cerca de 20 minutos depois, o site estava no ar. Um probleminha de domínio no Panda Vídeo (não permitido para aquele domínio), de resto tudo integrado — fontes, vídeo carregando. Ele fez o deploy sem eu especificar Git — criou um script `.sh` de deploy para staging na VPS, que reusa para os próximos envios, rodando checks das rotas e o deploy via Hostinger. Teve que resetar a VPS no meio do processo (deu problema, pedi para ele resetar), reconfigurou o Linux do zero, mandou os arquivos, configurou o Nginx (proxy reverso), fez o build e disponibilizou o projeto — tudo num loop só, com acesso total ao MCP da Hostinger.

O ideal seria configurar isso via Git (exigiria login etc.), mas já funcionou como estava. Dá para usar tanto `/loop` direto no Claude Code quanto o padrão de arquivo bash "manual" — o que o Claude Code faz por trás dos panos com `/loop` é essencialmente a mesma coisa.

## Fechamento — Onde Usar

Sempre para tarefas complexas: script de migração de dados e teste (sempre em sandbox, com snapshot/backup antes, nunca apontando para variáveis de produção, sempre rodando local primeiro). Subir e configurar uma VPS. Loop de segurança para avaliar uma VPS inteira, fechar portas abertas, resolver problemas de protocolo, problemas de injeção de arquivo em upload — inclusive testes de intrusão (pentest). Serve muito bem para executar várias specs em sequência, cada uma com seus critérios de aceite — inclusive a própria skill de Spec Driven roda todas as tarefas em paralelo, headless, cada uma com modelo e esforço diferentes, e o critério de parada do loop é todos os gates de todas as tarefas da fila passando, provado pelo gate mecânico da própria skill (incluindo Playwright). Ontem, por exemplo, demorou 4 horas para finalizar porque mandou rodar de novo.

Um ponto sobre custo: a IA não executa o teste em si, ela manda a máquina executar e só lê o resultado — isso não consome tanto token quanto parece (gerar os testes consome mais). Casos de uso recomendados: TTLs, migrações, coisas complexas, configuração de servidor, pentests, questões de segurança, e também construção de joguinhos ou qualquer coisa que precise de loops rodando um após o outro com uma camada de contexto empilhada e reprogramada nos próprios arquivos, não no contexto da IA — força bruta constante, testada e validada diversas vezes durante um tempo sem parar.

Para ver isso em mais detalhe: imersão de IA em 1º de outubro (link na descrição).
