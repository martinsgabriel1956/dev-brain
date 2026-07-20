# Deploy Blue/Green na Prática — VPS + Nginx (Demo)

> Transcrição de vídeo em português, reescrita como Markdown estruturado a partir de fala corrida sem pontuação. Nenhuma tradução necessária (fonte já em PT-BR). Patrocínio: HostGator (VPS).

## Introdução — o setup

O apresentador está conectado via SSH numa VPS, acessando direto pelo IP (sem domínio configurado ainda). No navegador, simula acessar `augustogalego.com`. A VPS está rodando um deploy blue/green: o servidor está servindo a versão "green" (V1), mas já existe um deploy da V2 rodando em paralelo como "blue".

Ao rodar `switch-my-app blue` no terminal e dar F5 no navegador, o tráfego vira para a versão blue — demonstração de que ambas as versões rodam simultaneamente e a troca é apenas de roteamento.

A VPS é da HostGator (patrocinadora do vídeo). O apresentador reforça que os conceitos são generalizáveis: funciona em qualquer infraestrutura, inclusive localmente, sem precisar de múltiplas máquinas. Escolheu o menor plano de VPS da HostGator para o teste — barato, boa capacidade, servidores localizados no Brasil (latência boa para o público local), e fácil de escalar depois se precisar.

## Arquitetura da demo

```
Usuário → Nginx (porta 80, reverse proxy) → app Node (porta 3001 ou 3002)
```

- Nginx atua como web server / reverse proxy — faz a ponte entre o usuário e o servidor de aplicação (Node).
- Ambos (Nginx e a aplicação) rodam na mesma VPS — não precisa de máquinas separadas.
- V1 (versão atual) roda numa porta fixa; V2 (nova versão) roda em outra porta, em paralelo.
- No exemplo: a instância "blue" ficou na porta 3001 (é a que estava live no momento) e a "green" na porta 3002 (V2). O apresentador reconhece que se confundiu ao vivo trocando as cores (blue/green) várias vezes durante a gravação — mas destaca que **tradicionalmente, na prática, o nome da cor (azul ou verde) não importa**; o que importa é o conceito: uma cor é a versão live, a outra é a fica de standby.
- Analogia com commits: V1 = commit anterior na main, V2 = commit novo na main.

### Fluxo de deploy blue/green

1. Sobe uma instância nova (ex.: green) numa porta que o usuário não acessa.
2. Testa essa instância acessando a porta diretamente (bypass do Nginx).
3. Confirmado que funciona, "flipa" a configuração do Nginx — manda o tráfego do usuário para a nova instância.
4. A instância antiga fica de pé por um tempo (permite rollback instantâneo) e depois pode ser derrubada.

## Preparação do repositório e ambiente local

Repositório criado especificamente para a demo, com auxílio de IA. Estrutura: duas branches, `blue` e `green`, cada uma servindo uma versão do app (um servidor simples servindo um arquivo estático — o código do servidor em si não é o foco do vídeo).

Teste local antes de ir para a VPS:

```bash
git checkout green
npm install
npm start   # passando host/porta, ex: localhost:3000
# serviu a versão green

git checkout blue
npm start
# serviu a versão blue
```

Confirmado que ambas as branches funcionam localmente antes de subir para o servidor.

## Configurando a VPS

Acesso via SSH (a HostGator também oferece terminal web pela própria plataforma). Dependências necessárias na VPS:

- **Node** (a app é `server.js`, roda com Node diretamente — sem container/Docker; o apresentador comenta que poderia containerizar, mas não é o foco do vídeo)
- **Git** (para puxar o código do GitHub para dentro da VPS)
- **Nginx** (reverse proxy)

Verificação de versão: `node -v` → Node 20.

### Estrutura de diretórios criada na VPS

Pastas separadas manualmente (processo deliberadamente manual, não automatizado — o apresentador argumenta que aprender manual primeiro ajuda a depois automatizar com confiança, por exemplo com pipelines no GitHub Actions):

```
blue/       # código da versão blue
green/      # código da versão green
release/    # (pasta de suporte)
shared/     # (pasta de suporte)
nginx/      # configuração do nginx
```

Um usuário de deploy dedicado (`deploy`) já havia sido criado previamente.

### Clonando o código

```bash
mkdir tmp && cd tmp
git clone <url-do-repo>
cd blue-green
```

(Na demo, o primeiro `git clone` foi feito num diretório errado, corrigido logo em seguida.)

## Scripts de automação manual

O repositório de demo inclui um conjunto de scripts bash, instalados individualmente (`install` em cada um), que orquestram o processo:

- **`myapp-start`** — script mínimo que inicia o Node na cor passada como argumento (blue ou green). É o "start de verdade" da aplicação.
- **`deploy-myapp <blue|green>`** — faz o deploy: identifica a porta correspondente à cor (blue = 3001, green = 3002 no exemplo), identifica qual é a cor "oposta" (para evitar conflito de porta), ativa a instância, faz health checks, e emite mensagens de log confirmando a ativação e a porta usada.
- **`switch-myapp <blue|green>`** — altera a configuração do Nginx para redirecionar o tráfego do usuário para a cor especificada. Não sobe nem derruba nada — só muda o roteamento.
- Variáveis de ambiente (`blue.env`, `green.env`) — opcional; dá para fazer tudo só com os scripts sem elas, dependendo da abordagem.
- **systemd** — instalado para facilitar a administração dos processos do servidor.
- **Configuração do Nginx** — praticamente idêntica entre blue e green; a única diferença real é o número da porta de destino (`proxy_pass`), repetido em vários pontos do arquivo de config por redundância.

O apresentador é explícito sobre suas limitações: não é DevOps nem um profundo conhecedor de Nginx/infra — está seguindo o mesmo tipo de processo que qualquer pessoa seguiria via tutorial, só que já validado e funcionando.

### Rodando o deploy

```bash
deploy-myapp main     # primeira tentativa deu "connection refused" — mas o deploy em si funcionou
deploy-myapp blue
deploy-myapp green
```

Depois de rodar os dois deploys, confirma-se com `ss`/`netstat` (ou equivalente) que há processos escutando em três portas:

- **porta 80** → Nginx
- **porta 3001** → instância Node (blue)
- **porta 3002** → instância Node (green)

Ambas as instâncias Node rodam em paralelo, na mesma máquina. O que determina qual delas recebe o tráfego do usuário é exclusivamente a configuração do Nginx.

### Trocando o tráfego

```bash
switch-myapp green
switch-myapp blue
```

Cada execução altera o roteamento do Nginx e, após F5 no navegador, a versão servida muda imediatamente — sem downtime perceptível, sem redeploy.

Nota de humor do próprio apresentador: durante a gravação, ele havia feito o deploy da branch `green` do Git como sendo, na prática, a "V1" (a versão já live, que no vocabulário blue/green corresponderia a "blue"), e vice-versa — os nomes das branches Git (`blue`/`green`) e os papéis blue/green do deploy acabaram invertidos entre si por engano ao vivo. Ele reforça que isso não muda o conceito: cor é só rótulo, o que importa é qual delas está recebendo tráfego em cada momento.

## Encerramento — takeaways do apresentador

- Um deploy blue/green manual não é complicado: dá para montar com uns quatro scripts bash encontrados/adaptados de tutoriais, tudo rodando na mesma máquina.
- O vídeo cobriu reverse proxy e múltiplas instâncias na mesma VPS, mas deliberadamente não se aprofundou no código da aplicação em si (considerado menos relevante hoje, e fora da área de expertise do apresentador).
- É possível (e comum em produção real) rodar cada versão em máquinas fisicamente separadas, com maior grau de isolamento — o vídeo simplificou colocando tudo numa VPS só, para fins didáticos.
- Está cada vez mais fácil montar esse tipo de infra mesmo sem ser especialista, inclusive com ajuda de IA — o apresentador destaca que fez a demo com relativa tranquilidade apesar de não ser um "grande expert" em DevOps/infra.
- Vídeo é continuação de uma aula anterior sobre tipos de deploy.
