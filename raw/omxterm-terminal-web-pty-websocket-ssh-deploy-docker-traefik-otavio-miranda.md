# OMXTerm: como funciona o terminal (TTY, PTY, shell), terminal na web com WebSocket + SSH, deploy com Docker + Traefik e segurança

> **Origem:** transcrição de vídeo em português (brasileiro), colada pelo usuário em 2026-09-30. O falante é o dono do canal ligado ao cupom/link "Otávio Miranda" (`hostinger.com/OtávioMiranda`) e ao domínio `otaviomiranda.cloud`; título original do vídeo e data de publicação não informados (o falante diz que "estamos em 18 de agosto"; ano não dito). Já estava em português; **não houve tradução**.
>
> **Tratamento:** a transcrição original é corrida, sem pontuação confiável e com repetições/frases cortadas. Aqui foi limpa e dividida em seções, sem alterar o conteúdo.
>
> **Termos corrompidos pela transcrição, corrigidos por contexto:**
> - "Teletype/teleprinter/TTY" → TTY (teletypewriter); "TTY com T de tatu" / "PTY com P de pato" é mnemônico falado
> - "OMXTerm" / "OMXTerm Web" → nome do projeto do autor (terminal web); grafia mantida como na transcrição, mas não confirmada
> - "Pi" (o agente que o autor usa no dia a dia e cujas skills/config estão num repositório público) → provavelmente o *coding agent* "Pi"; **incerto**
> - "Linus Åkesson, de 2008" → artigo sobre TTY; **provavelmente** "The TTY demystified" (linusakesson.net), mas a transcrição não diz o título; **inferência**
> - "Zsh"/"Bash"/"htop"/"ls"/"tmux" → nomes de programas; "xterm.js" e "TermBench" mantidos
> - "sshd_host_ed25519_key.pub" → `/etc/ssh/ssh_host_ed25519_key.pub`
> - "Traefik", "Fastify", "SSH2", "Zod", "Vite", "React", "Let's Encrypt", "WireGuard", "UFW", "rsync" → grafias corrigidas
> - "Cross-Site WebSocket Hijacking", "DNS rebinding", "timing attack", "backpressure", "RBAC", "WAF" → termos técnicos preservados
> - "WSS" no abertura = WebSocket Secure
> - "Hostinger", "KVM2/KVM4/KVM8" → planos de VPS da Hostinger (bloco patrocinado)
> - "otávio miranda.cloud" → `otaviomiranda.cloud`
> - Trechos com frases quebradas/repetidas foram unificados; onde o sentido ficou incerto, marcado como **[incerto]**.

---

## Abertura: o projeto

O autor criou o terminal como projeto de fim de semana para estudar o próprio terminal. Só que **não é um terminal instalado no computador: é um site**, o que trouxe uma "gama enorme de problemas" que o vídeo discute: como funciona o terminal (do físico ao emulador), como converter o terminal para a web, como fazer o deploy do terminal web com **Docker e Traefik**, e os problemas de segurança: **HTTPS, WebSocket seguro (WSS), SSH e política de allowlist**.

## Como funciona o terminal: do telégrafo ao emulador

O que hoje se chama de terminal **não são terminais reais, mas emuladores de terminal**. Eles emulam um aparelho físico que já existia **antes mesmo do computador**. Exemplo: o telégrafo/teleprinter de ~1940. Pressionar uma tecla não faz nada "ali": emite um sinal, que gera dados, que vão parar em uma impressora em outro local. É uma máquina de escrever com *transmitter* e *receiver* que imprime à distância.

Quando isso chegou ao computador (exemplo do Unix): um **Teletype/teleprinter** se comunicava com um computador enorme; como o computador já suportava várias sessões, vários terminais podiam estar conectados ao mesmo servidor. O lado do usuário tinha teclado, e a saída era inicialmente uma impressora, depois telas de tubo, até chegar ao computador normal. Esse aparelho era um **dumb terminal**: não tem sistema, não faz nada sozinho, só é responsável por digitar a tecla e imprimir/exibir os dados. O dispositivo se chama **teletypewriter**, hoje **Teletype** ou **dispositivo TTY**; também é chamado de **console**; e o nome dado à "telinha preta" é **terminal**.

Exemplo: a página da Wikipedia de **Ken Thompson** mostra o computador das primeiras versões do Unix, "do tamanho de uma parede" (não daria para levar a uma cafeteria); o dispositivo não tem tela, só teclado, e o que se digita sai impresso no papel.

Como isso virou o terminal de hoje? **Ninguém substituiu ninguém**: o TTY continua funcionando normalmente; há gente no YouTube usando Linux moderno rodando aquele TTY. Para ter um terminal que "finge ser aquilo", é preciso **fingir também que existe um dispositivo para se comunicar**, e aí entra o **shell**.

## Patrocínio (Hostinger) e escolha do servidor

Bloco patrocinado: o autor precisa de um servidor para o deploy e oferece link + cupom "Otávio Miranda" da Hostinger (VPS e outros produtos). Usa o **KVM4** (tem KVM2 em uso e KVM8 em experimentos); recomenda o **KVM2** como mais popular e melhor custo-benefício; sugere o período de **24 meses** para manter o desconto (servidores tendem a ficar mais caros); país Brasil; aplicativo **Docker** (Ubuntu 24.04 com Docker). O autor afirma que o preço muda a cada visita.

## PTY: o terminal falso, na prática

O autor mostra um outro terminal, feito em Python, só para explicar como as coisas funcionam por dentro (sem relação com o terminal web). Escreveu "fingindo ser uma linguagem de baixo nível", usando diretamente o módulo `os`; poderia ser em C ou outra linguagem.

O sistema operacional baseado em Unix já tem isso pronto: em vez de um **TTY** ("T de tatu"), pede-se um **PTY** ("P de pato"), **pseudoteletype / pseudoterminal**, um terminal virtual. Ele tem **duas pontas: master e slave**. A janela (o **emulador de terminal**) lê e escreve no **master**; ou seja, envia coisas ao **kernel** e recebe coisas dele. Master e slave são **dois arquivos** que o SO trata de forma especial. O master não fala diretamente com o slave: entre eles há, no kernel, um componente chamado **line discipline**.

### Line discipline

É "muito importante". Quando se digita qualquer coisa, isso vai ao kernel e volta: digitar `L` já foi ao kernel e voltou, aparecendo na tela do terminal (é o **echo**). Ele faz **buffer da linha**: até pressionar Enter, segura as teclas, o que impede que algum processo receba as teclas automaticamente antes disso. O slave aparece no shell como `/dev/pts/N` (comando `tty`), um device TTY por sessão; o shell conversa com ele como se fosse um teletype normal.

`stty -a` mostra `icanon` ativo e `echo` ativo (o que tem "-" não está ativo). Com `stty -echo`, ao digitar não aparece nada: só há input, sem output, porque o echo do line discipline foi desativado. Utilidade: em terminais com papel, um pedido de senha não a imprimiria. Outra utilidade do line discipline: se ele não existisse, **cada tecla teria que chegar a algum processo**, o que não seria prudente; ele também permite **edição de linha** (digitar `ls`, apagar, corrigir) sem chamar programa a toda hora.

### Fork e redirecionamento de file descriptors

O shell (Bash, Zsh…) é o programa que precisa ser conectado ao slave. No código Python: pega-se a variável de ambiente do shell, pede-se ao módulo `os` para abrir um PTY e faz-se um **fork** do programa.

Demonstração simples: um programa conta de 1 a 10 imprimindo e dormindo 1s. Com `fork()` no 5, o processo é **duplicado**: passam a aparecer o "6" e o "6 clonado", etc., porque são **dois processos**. No processo clonado (filho) o valor de retorno do fork é **0**; no original (pai) é diferente de 0. Isso permite ter código diferente para **processo pai** e **processo filho**.

Por que importa: no clone dá para pegar `stdin`, `stdout`, `stderr` (file descriptors padrão) e **apontá-los para outra coisa**. Exemplo: abrir um arquivo no Desktop, pegar o file descriptor e apontar o `stdout` para ele; ao executar, nada aparece na tela, pois o stdout do clone foi redirecionado para o arquivo.

O shell funciona assim. O processo Python **herdou** stdin/stdout/stderr do shell que o iniciou (o PID do shell aparece em `$$`; `ps` mostra o Zsh como pai). No filho, o autor **desplugue 0, 1 e 2 e pluga no fd do slave**, fecha o que sobrou, e agora todo mundo aponta para o PTY criado por `openpty`. Além disso, o fork/exec pode **substituir o processo**: o processo Python é substituído pelo **shell (Bash)**. No processo pai fica a configuração do master.

O pai cria uma janela **Tkinter** com um `Text` de fundo preto, "que não renderiza absolutamente nada" (só mostra os bytes); lê a saída que vem do master e a exibe; envia teclas de controle (Backspace, Enter → `\r`, Ctrl+C) e fecha a janela para terminar. Exemplo: ao abrir o `htop` nesse terminal, passa uma enorme quantidade de bytes (sequências de controle) que ele **não sabe interpretar/renderizar**; no terminal normal, funciona.

Quando se executa `ls`, o shell faz **fork** do `ls`, que herda os mesmos file descriptors; todos apontam para o mesmo lugar, então o retorno chega ao master e volta ao emulador. **O maior trabalho do emulador de terminal é renderizar isso na tela.**

### SSH, tmux

O SSH usa tudo isso: o "ls" da cena passa a ser o **cliente SSH**; do lado remoto, o **daemon SSH (sshd)** fala com o master (quase invertido). Após a conexão, tem-se o shell remoto passando por toda essa cadeia. Sobre o tmux: "vai complicar tanto a sua vida" (piada; não abordado). O terminal web é uma variação porque **a web não conversa com o terminal nem com SSH**.

## A história do projeto e o papel da IA

O terminal existe desde **27 de junho** e o autor está em **18 de agosto**: praticamente **dois meses estudando o próprio código**. **Não fez com vibe coding**: ainda tem o processo na mente. Tudo começou com um **artigo de Linus Åkesson, de 2008** (sobre TTY). Daí: "quero criar um terminal e jogá-lo na web para acessar de qualquer lugar".

Consultou o **OWASP Cheat Sheet Series** (recomenda ler tudo, "se você publica qualquer coisa, web ou não"): aprendeu ali o **Cross-Site WebSocket Hijacking**. Também decidiu tudo ser **efêmero**: não salvar nada no servidor por causa de chave privada SSH etc. Escreveu páginas em um caderno, montou o projeto na cabeça e então criou um **PRD/spec** para "fazer o dump" numa IA e ter o código escrito. Como o escopo era pequeno, optou por um **MVP**. Depois de aprovar o PRD, quebrou-o em **34 issues**.

**Processo com agentes** (ninguém sabe ainda como trabalhar com IA; todos tentam algo novo): usa o **Pi** no dia a dia, com configuração e **skills** em repositório público. A skill pega um documento enorme e o quebra em issues que cabem no contexto de um agente. **Antes de enviar a um agente**, faz **auditoria** da issue: (1) a issue é criada; (2) outro agente com **contexto limpo** lê a issue e **explica o que entendeu** que é para ser feito; (3) o agente que criou a issue vê se há divergência; (4) por desencargo, issue + resposta vão a um **segundo agente com contexto limpo**; (5) os dois agentes julgam se o entendimento é válido. Fez isso nas 34 issues. "Gasta muito token", mas resolve o problema de "não estava escrito" ou de o prompt não ter sido entendido.

Depois usou outra skill de **orquestração**: o **orquestrador** manda para um **writer** (escreve o código), o resultado vai a outro agente (contexto limpo) para **revisar** o código do writer, volta ao orquestrador com possíveis correções, o orquestrador corrige, **fecha a issue** e abre **outro orquestrador com contexto limpo** para continuar até terminar. Ele "vai dormir" e o agente implementa tudo.

**O problema**: acordou com o código pronto — **10 mil linhas de código que ele não tocou** (um monorepo "perfeito", como pedido) — e a revisão tomou quase dois meses (não revisando o tempo todo; ele também criou o terminal que aparece no vídeo). **O entendimento não ficou igual**: quando tentou gravar um vídeo explicando, não conseguiu explicar; percebeu que faltava entendimento **no código em si**. Lição: mesmo achando que entendeu algo, **tente explicar a alguém ou grave-se explicando e assista**; talvez descubra que não entendeu "nada daquilo que é seu". Não achou solução que não seja **fazer ou revisar o código**, "o que as pessoas realmente não estão fazendo agora". Alerta: "a gente está se distanciando muito do código e isso pode não ser muito bom, principalmente para quem está iniciando".

## Deploy do OMXTerm

O servidor já tem **Docker** e o código do OMXTerm; o autor já fez o **hardening completo** e a configuração do **VPN com WireGuard** (tratados em outros vídeos do canal). Sugere ao espectador pedir ao próprio agente para ler a documentação e fazer uma **auditoria de segurança** do projeto.

O código é um **MVP de final de semana**: falta muita coisa "necessária para algo útil", mas o *core*, como configurado, "presumo que esteja bastante seguro; não posso garantir nada". Pode-se usar o core para desenvolver em cima; só se tiraria uma **regra**: **"não salvo nada no servidor nem no computador do cliente. Tudo que recebo descarto assim que possível; ao fechar a conexão descarto o que for possível e só mantenho os *hashes* dos tokens de autenticação para saber quem é você."**

O autor tem um **script pessoal** (não faz parte do código do OMXTerm) com configuração do **Traefik** e partes dinâmicas: **rate limit como middleware do Traefik**, **Let's Encrypt**, porta. Tudo por **variáveis de ambiente**. O `.env` (real, mostrado como exemplo):

- **Domínio** onde o OMXTerm será configurado; no DNS, um registro **A** com **wildcard (`*`)** para `otaviomiranda.cloud`.
- **E-mail** para o Let's Encrypt (usar um e-mail válido).
- **Redes/IPs permitidos para a saída do OMXTerm** (`OMXTERM_SSH_ALLOWED_CIDR`): em vez de liberar `/24` da VPN inteira, o autor libera **IP por IP** (IPs da VPN, IP da própria residência, IPs de outras VPS), separados por vírgula.
- **Diretório** do OMXTerm Web; e a seção **edge** (Traefik).
- **Nome da rede Docker** com **IPs fixos** para o Traefik e o OMXTerm Web, porque houve problema com IP dinâmico: o OMXTerm define para onde permite conectar, mas o **UFW** também precisa conhecer os IPs internos; senão, o IP colocado no OMXTerm pode não estar liberado no firewall e o **broker** não consegue se comunicar com aquele IP interno. Também o IP do proxy (Traefik).
- **Porta do SSH** e **configurações de rate limit**: há rate limit no proxy reverso (Traefik) **e** um interno no OMXTerm: **10 tentativas de token em 60 s** bloqueiam o IP, que passa a ser ignorado.

Depois de configurar, copiam-se os dois arquivos (ambiente + script) ao servidor. Há um outro script "mais destrutivo" que usa **rsync** para copiar a pasta de scripts para a KVM4 e roda o de deploy. O script **mostra as configurações** e exige digitar `yes`. Ao terminar: gera automaticamente um **token** (guardado no `.env` interno do projeto) e deixa um **comando de redeploy**, que o autor salva num script `deploy` no servidor. Ele troca o token por um qualquer (mínimo **24 caracteres**), refaz o deploy (`./deploy`) e a página volta a ser acessível.

### Stack do OMXTerm

Monorepo com **apps** de backend e frontend e um **core**. Backend/API: **Fastify**, `.env`, **SSH2** (SSH), **WebSocket**, **Zod** (validação). Frontend: o core, **Vite**, **React** (single-page).

## Lista de estudo de segurança (só os nomes)

O autor passa os nomes para o espectador pesquisar (cada um "daria no mínimo um vídeo ou uma faculdade"; "isso aqui tem um ano de estudo"):

- **Timing attack** — usa o tempo que a linguagem leva para comparar strings para descobrir a senha; um rate limit já ajuda a resolver.
- **Rate limit** — pode ser por conexão (requisições por IP) ou por tentativas de login.
- **CSRF (Cross-Site Request Forgery)** — site malicioso usando cookies de um usuário logado para ações maliciosas se o site não estiver protegido.
- **Cross-Site WebSocket Hijacking**, **cookies em geral**, **XSS**. Para quem está começando, "isso é meio básico na internet".
- Mais específicos de WebSocket + SSH: **controle de backpressure** (WebSocket e SSH), **autenticação e autorização**, **permissões / RBAC**, **OAuth**, e o **WAF** (Web Application Firewall), que também controla a saída.
- **DoS e DDoS** — não implementados no OMXTerm (dependeria de Hostinger/Cloudflare, proteção de borda).
- Também **DNS rebinding** (adicionado depois no vídeo).

Não há nada implementado no OMXTerm para **DoS/DDoS**, nem **permissões** (é para uma única pessoa, há **um único token para uma única pessoa**).

## Fluxo de autenticação guiado (DevTools do navegador)

1. **Formulário 1 (token):** digita o token (o autor já trocou o "token de sacanagem" inicial). Ao logar cai no formulário de destino SSH; o acesso é combinado com `OMXTERM_SSH_ALLOWED_CIDR` — não se consegue acessar qualquer domínio/IP sem essa configuração.
2. **Cookies:** ao autenticar são criados **três cookies** (Application → Cookies): **Device Token, Session ID e Session Token**. São **de sessão** (somem ao fechar o navegador), **HttpOnly** (JavaScript não acessa), **Secure** (só em HTTPS) e **SameSite=Strict** (o navegador só os envia quando o domínio de destino é o mesmo da aplicação). "Aqui já começa a programação defensiva" (as palavras de segurança citadas antes).
3. **Network (POST de acesso):** enviou o token no payload; o servidor respondeu `ok: true` e, nos response headers, configurou o cookie `omxterm-session-id`, além de `session-token` e `device-token`. A partir daí **todas as rotas HTTP** usam esses cookies para provar autenticação (HTTP é stateless, então o navegador reenvia os cookies a cada request — "por isso protegemos o cookie com unhas e dentes").
4. **Formulário 2 (dados SSH):** IP/host (o autor usa o IP da própria KVM4 na VPN, `10.100.0.4`), porta, usuário, **private key** (colada ou por arquivo) e passphrase. Ao clicar "Continue to Fingerprint", o **broker** faz uma chamada direta ao servidor de destino para **obter o fingerprint** e mostra na página ("a gente não salva nada; o MVP ainda não tem `known_hosts`, nem sei se vou colocar").
5. **Conferência do fingerprint:** o autor confere no servidor com `ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub` (o final `bpvx8` bate). Há **60 segundos** para isso.
6. **Trust for this session:** o navegador envia os cookies ao broker de novo (chamada "terminal ticket"). Nesse POST vão os **dados completos do SSH** (incluindo chave privada, IP, porta, usuário, passphrase). O servidor faz "meio mundo de checagem": se o IP de destino é permitido (allowlist) etc.
7. **Proteção contra DNS rebinding:** na primeira vez que vê um domínio, resolve-o e **guarda o IP**; depois **usa apenas o IP**, sem nova consulta ao DNS.
8. **Resposta com ticket:** passando tudo, o servidor devolve a **URL do WebSocket**, um **ticket** e o **tempo de expiração** (**60 s**). O ticket é de **uso único**: ao usar, **é apagado** (não "se autodestrói"). Motivos: se alguém obtiver o ticket, não o reusa; e ajuda a prevenir **Cross-Site WebSocket Hijacking**.
9. **WebSocket sem cookies:** o WebSocket é **contínuo e stateful** (diferente de HTTP request/response); o autor **não usa cookies no WebSocket**, e sim o ticket. Ao **atualizar a página**, a conexão com o servidor SSH é perdida, "justamente porque não uso cookies no WebSocket" (o ticket é de uso único, inclusive para o próprio usuário).
10. **Sessão:** navegador → **xterm.js** (emulador) → WebSocket → **broker** → SSH → **sshd** → line discipline → Bash. Ao redimensionar a janela, o navegador envia mensagens de resize ao servidor (o servidor faz **debounce**, ficando com o último valor). Cada tecla aparece como mensagem input/output no WebSocket (`L`, `S`, Enter → saída do `ls` + prompt).

## Desempenho e observações finais

O `htop` funciona dentro do xterm.js. O OMXTerm Web **não usa o addon WebGL do xterm.js** (há uma *issue* aberta no repositório); o outro terminal do autor tem mais liberdade e o web tem **mais restrição de backpressure**, mas "se olhar o TermBench, ele não é lento". Demonstra despejando uma enorme quantidade de caracteres: "isto é um terminal normal, que funciona perfeitamente". Encerra pedindo comentários se o espectador quer mais vídeos desse tipo (pedido de engajamento; sem conteúdo técnico).
