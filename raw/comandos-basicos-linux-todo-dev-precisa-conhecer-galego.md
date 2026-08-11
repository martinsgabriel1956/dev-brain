# Comandos Básicos de Linux que Todo Dev Precisa Conhecer (Augusto Galego)

> Transcrição limpa e organizada de vídeo. Conteúdo original em português; sem tradução necessária.

## Por que conhecer comandos de Linux

Hoje vamos ver comandos básicos de Linux que todo dev precisa conhecer — comandos para criar pastas, navegar pastas, ler pastas. Por que você precisa conhecer isso?

- **Porque é assim que as IAs estão manipulando o seu computador.** Quando você abre um Claude Code ali dentro do seu Linux ou do seu MacBook, ela está rodando comandos nativos do Linux/Unix. Ela vai estar rodando um `cd`, um `mkdir`, um `grep`, um `sed`.
- **Porque algo próximo de 90% dos servidores do mundo rodam Linux/Unix** — alguma distro, um Debian, um Ubuntu. Para manipular essas máquinas — nas suas pipelines de CI/CD ou quando você fizer um SSH para a máquina — você vai utilizar esses comandos.

É importante que todo dev conheça pelo menos por cima alguns desses comandos. Você não vai usar todos eles todos os dias, mas no trabalho profissional de um desenvolvedor de software você sempre esbarra num comando desse ou outro. É bom ter uma noção.

## Patrocínio — Abacus

Rapidamente sobre o patrocínio de hoje, que é a Abacus. Na Abacus você tem todas as IAs num só lugar: GPT 5.5, Claude Opus 4.8, Fable 5 — você pode utilizar tudo isso dentro da mesma subscription (a Abacus "ZI") por apenas $10. Você pode usar todos esses chats na própria IDE da Abacus. Também tem o Agent Sessions (agente poderoso que faz muitas coisas). Dá para gerar foto, vídeo, texto, áudio, aplicativos; pedir para criar aplicações; hospedar aplicações dentro do "super computer" da Abacus. Há vários exemplos no site (ex.: um jogo mobile). É bom para MVPs, pequenos softwares, ferramental interno da empresa, ou só para ter acesso a várias IAs diferentes. Você pode pegar um prompt e mandar para cinco IAs diferentes pagando uma única subscription. Acaba saindo mais barato que a subscription "pro" de cada uma dessas IAs individualmente. Link na descrição.

## O terminal

Vamos ao Linux. Primeira coisa: o seu terminal. Estou com o terminal cru aqui, sem nada. O terminal é como você usa para executar comandos direto na máquina, sem precisar de uma interface gráfica.

Antigamente os computadores eram meio que baseados nisso; depois caminhamos para um negócio mais de interface gráfica (janelinha, pastinha). Mas tudo que você consegue fazer com interface gráfica — criar pastas, criar arquivos, escrever arquivos, rodar softwares — você consegue fazer também via terminal.

## Navegação e listagem

- `pwd` — **print working directory** — mostra o diretório em que estou nesse exato momento. Ex.: as coisas estão organizadas dentro de pastas — tem `users`, o user `Augusto Galego`, a pasta `dev/linux` que acabei de criar.
- `ls` — mostra todos os arquivos dentro da pasta.
- `touch agents.md` — cria um arquivo vazio (`agents.md`). Depois um `ls` já cita esse `agents.md`.
- `ls -l` — dá muito mais detalhes. O ponto (`.`) é o próprio diretório; o `d` no início da linha indica que é um diretório; um ifen (`-`) no início indica arquivo normal. Depois vêm as permissões (`r` = read, `w` = write, `x` = execute) e o dono do arquivo.
- Arquivos que começam com ponto (ex.: `.DS_Store` no Mac) são **ocultos** — não aparecem no explorador por padrão. (No MacBook: `command + shift + .` mostra arquivos ocultos.)

## Comandos mais comuns do dia a dia

- `ls` — listar diretórios.
- `cd` — **change directory** — mudar de diretório.
- `mkdir` — **make directory** — criar diretório novo. Ex.: `mkdir subfolder`.
- `cd subfolder` — navega para a subpasta (equivalente a dar clique duplo e entrar na pasta). É ali dentro que o terminal executa os comandos.
- `cd ..` — sobe uma pasta.

### Caminhos relativos vs. absolutos

- Caminhos relativos: `cd ..`, `cd subfolder`.
- Caminho absoluto: `cd ~` leva ao **home directory**. Estando na home, dá para ver tudo que tem nela.
- `cd -` volta para a pasta em que você estava anteriormente.

### Pastas aninhadas (nested)

- `mkdir -p sub1/subpasta/subpasta-grandissima` — o `-p` cria os diretórios-pai (**parents**) e as subpastas de uma vez. Sem o `-p`, se a pasta-pai não existe, o comando reclama que a pasta não existe e não consegue criar as subpastas.

## Escrevendo e lendo arquivos sem editor

Você consegue manipular arquivos mesmo sem abrir um editor de texto. Inclusive, o Claude Code dentro do seu computador **não** abre um editor gráfico — ele manipula o arquivo via comandos.

- `echo "hello" > agents.md` — escreve `hello` dentro do `agents.md`. O sinal `>` **sobrescreve** todo o conteúdo. Um segundo `echo "hello de novo" > agents.md` apaga o `hello` anterior.
- `cat agents.md` — printa o que está escrito dentro do arquivo. É isso que o Claude Code executa para ler seus arquivos: um `cat`, pega o output e faz uma requisição para o servidor da Anthropic com aquele conteúdo como parte do prompt.
- `echo "hello de novo" >> agents.md` — o `>>` faz **append** (joga o texto novo no final), em vez de sobrescrever. Assim você não precisa reescrever o arquivo inteiro.

> É assim que a **harness** funciona na prática: ela usa comandos de Linux (ou de Windows) para ler, escrever e manipular arquivos, ficando o tempo todo conversando com o servidor da Anthropic.

## Copiar e mover arquivos

- `cp agents.md cloud.md` — copia o conteúdo de `agents.md` para `cloud.md` (a Anthropic gosta muito do nome "cloud/claude"). Um `cat cloud.md` mostra todo o conteúdo copiado.
- `mv cloud.md sub1/` — move o `cloud.md` para dentro da pasta `sub1`. Depois de mover, ele não aparece mais na pasta original.

> Quando você der SSH para um servidor em produção, provavelmente vai ter que fazer as coisas dessa maneira, pois via SSH você geralmente não terá interface gráfica (e, mesmo quando há, costuma ser travada). Para a maioria dos devs com alguma experiência, é mais fácil usar esse tipo de comando. (Servidor Windows é outra história — nunca trabalhei com isso.)

## Remover arquivos e pastas

- `rm sub1/cloud.md` — remove o arquivo (auto-complete com Tab ajuda).
- `rm sub1` — **não** funciona para diretórios: reclama que `sub1` é um diretório.
- `rm -rf sub1` — `-r` (recursivo) + `-f` (force) deleta a pasta e tudo que há dentro dela, recursivamente.

> **Cuidado com `rm -rf`.** Ele deleta recursivamente e não pede permissão nenhuma — sai quebrando tudo. Se você fizer isso numa pasta core do sistema, pode dar ruim muito rápido. (O clássico trote de mandar alguém rodar `rm -rf` numa pasta do sistema quebra o PC da pessoa.)

## Arquivos ocultos e variáveis de ambiente

- `touch .env` — o ponto no início cria um arquivo **oculto**. `.env` não tem nada de especial além de começar com ponto, mas é muito usado em aplicações reais para guardar variáveis de ambiente.
- `echo "DATABASE_URL=..." >> .env` — adiciona uma variável de ambiente ao `.env`.

## git init (curiosidade)

- `git init` — aparentemente não cria nada visível, mas um `ls -l` mostra uma pasta oculta `.git` (é um diretório, começa com `d`). É onde o Git guarda o que precisa para lidar com o repositório: em qual branch você está, quais arquivos estão staged, etc. Se você deletar a pasta `.git`, terá que configurar o Git de novo naquele repositório.

## Exportar variáveis de ambiente

- `export PORT=3000` — nessa instância do terminal, cria uma variável de ambiente `PORT` valendo `3000`. Comum ao testar/rodar scripts.
- É comum, ao instalar coisas (ex.: Python), configurar variáveis para que já estejam exportadas por padrão sempre que o terminal iniciar. Isso costuma ficar em arquivos como `.zshrc` (ou `.bashrc`).
- `echo $PORT` — imprime `3000`; a variável funciona dentro dos scripts que você roda.

## Permissões e chmod

- `ls -l` mostra as permissões de cada arquivo.
- Ex.: criei um `hello.sh` (um script que dá `echo "hello from script"`). Ao tentar `./hello.sh`, dá **permissão negada**: o arquivo tem read e write, mas **não tem `x`** (execute).
- `chmod +x hello.sh` — adiciona a permissão de execução. Depois, `ls -l` mostra `r`, `w` e `x`, e `./hello.sh` roda o script.

> Você provavelmente já esbarrou nesse erro e já deu um monte de `chmod` na vida porque a IA ou o Stack Overflow mandaram — é exatamente isso: você não tinha permissão para executar o arquivo, deu a permissão, e passou a executar.

## sudo

- `sudo` significa rodar algo como **super user / admin**. Às vezes você não tem permissão para fazer algo, mas com `sudo` você tem.
- Ex.: `sudo mkdir pasta-nova` — pede a senha de admin e cria a pasta. (Nesse caso foi desnecessário, pois eu já tinha permissão — mas quando não se tem, o `sudo` permite forçar.)
- **Cuidado ao usar `sudo`.**

## grep — buscar dentro de arquivos

Supondo um arquivo grande, de 1000 linhas: como o Claude Code encontra onde tal função é usada?

- `grep "erro" agents.md` — busca pelo termo `erro` e retorna a linha onde está.
- `grep -i "erro"` — **case insensitive** (insensível a maiúsculas/minúsculas): acha `erro` mesmo escrito em outro case.
- `grep -n` — retorna o **número da linha** onde o termo está.
- `grep -r "hello"` — busca **recursivamente** por todas as pastas, mostrando todos os lugares onde `hello` aparece.

> É assim que uma LLM consegue encontrar o que está onde, achar utilizações de função, etc. Isso é o puro suco da harness e do tool calling das LLMs — a harness está fazendo isso o tempo todo.

## pipe operator

O pipe operator (`|`) pega o **output** de um comando e usa como **input** de outro.

- `cat agents.md | grep "erro"` — o `cat` printa o arquivo, o `|` passa esse output como input para o `grep`, que filtra e imprime só a linha com `erro`.
- Dá para encadear vários pipes.

## sed — substituição de texto

O `sed` transforma texto. É um comando meio rebuscado (tem detalhes chatos de escapar caracteres), então geralmente se pesquisa a sintaxe.

- `sed 's/ERRO/error/' agents.md` — substitui `ERRO` (maiúsculo) por `error` (minúsculo) no texto. (É preciso fechar as aspas corretamente, senão dá erro.)

> Você pode misturar `grep`, vários pipe operators e `sed` — aí explode a loucura.

## O que ficou de fora

Estamos raspando a superfície. Não falamos de:

- **Processos** — matar processos (`kill`); ex.: quando "já tem algo rodando na porta 3000", você pega o output, dá um `grep` com pipe e mata o número do processo.
- **ping**, **curl**.
- **SSH** — foi mencionado, mas não demonstrado.

## Fechamento

Você **não precisa decorar tudo isso**. Eu mesmo não decoro — revisei e testei antes de gravar, e fiz outras partes no freestyle porque não uso isso todos os dias. O importante é: quando eu leio numa pipeline um `sed`, um `grep` ou um `echo`, eu sei o que está acontecendo. É isso que espero ter conseguido mostrar. Dá para gravar uma parte 2 tranquilamente.
