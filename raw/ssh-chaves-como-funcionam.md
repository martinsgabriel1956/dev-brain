# Chaves SSH — como funcionam, servidor, cliente e configuração

> Transcrição de vídeo. Formatada em Markdown para ingest na wiki, sem alteração de conteúdo ou opinião do autor. Já estava em português, sem necessidade de tradução; falas foram limpas de repetições e organizadas em seções para leitura, sem alterar o conteúdo técnico.

Chave SSH é um daqueles assuntos em que ou você sabe, ou você basicamente não sabe nada — só cria uma chave e usa essa mesma chave eternamente. O objetivo deste vídeo é explicar como funciona o servidor SSH, como funciona a configuração do cliente, onde fica a chave, como gerar a chave e assim por diante.

O autor também menciona uma ferramenta própria (já existente antes deste vídeo) que gera configuração e comandos de SSH Tunnels, e permite hardening do servidor com presets prontos — "paranoico", "equilibrado", "básico" etc.

## O conceito: chave e fechadura

A chave SSH pode ser imaginada como uma chave e uma fechadura. Eu tenho a chave, que seria a minha chave privada, e o servidor tem a fechadura. Quando essas duas coisas se conectam e a fechadura abre, as chaves SSH "bateram" e eu consigo logar em locais sem senha específica — a chave é exatamente a minha senha para entrar no servidor.

Exemplo prático citado: bastou digitar `ssh m132`, sem passar chave nenhuma, e o login caiu direto no outro computador. Isso acontece porque a chave privada está de um lado e a chave pública correspondente está do outro; quando batem, o OpenSSH faz os cálculos internos (não detalhados no vídeo) e destranca a sessão sem exigir digitação de senha.

### O diagrama

No computador local existe um cliente SSH e um servidor SSH; do outro lado (o "servidor" da conversa) também existem cliente e servidor, e ambos os lados podem ter par de chave pública/privada.

- A chave privada nunca sai do computador onde foi gerada.
- A chave pública é a parte que pode ser compartilhada — ela vai para um arquivo no lado que vai autenticar a conexão, geralmente chamado `authorized_keys`, dentro do servidor.
- Assim que a chave pública está no `authorized_keys` do destino, já é possível autenticar.

Se a chave privada existe só no computador A e a chave pública correspondente só foi copiada para o computador B, a comunicação só pode sair de A para B — B não consegue logar de volta em A. Para permitir a via inversa, é preciso gerar (ou usar) outro par de chaves, com a chave privada em B e a chave pública correspondente copiada para A. As duas direções podem coexistir independentemente, cada uma com seu próprio par de chaves.

O SSH tem duas partes — servidor e cliente — que precisam estar instaladas nas duas pontas para a comunicação bidirecional funcionar.

## Configurando o servidor (openssh-server)

Instalação básica:

```bash
sudo apt install openssh-server
```

Isso já sobe boa parte da configuração, mas dependendo da distribuição os padrões vêm mais "fracos" e vale reforçar a configuração depois.

No exemplo em Docker usado no vídeo, o `Dockerfile` instala apenas `openssh-server` e `openssh-client`; a configuração do daemon fica em arquivos separados, aplicados na subida do container.

Localização padrão da configuração do servidor: `/etc/ssh` (requer sudo). O arquivo principal é `sshd_config` — o "d" no final indica que é o daemon (servidor). Esse arquivo normalmente já inclui (`Include`) tudo que estiver dentro do diretório `sshd_config.d/*.conf`, e as configurações são aplicadas de cima para baixo — a primeira regra que casar é a que vale.

Prática recomendada: em vez de editar `sshd_config` diretamente, criar um arquivo próprio dentro de `sshd_config.d/`, com um nome começando por um número baixo (ex.: `00-...`) para garantir que seja lido primeiro.

Configuração de exemplo usada no vídeo:

- `Port 22` — porta padrão do SSH (pode ser alterada).
- `ListenAddress 0.0.0.0` — escuta em todos os endereços de rede do computador (todas as redes do mundo em IPv4).
- `PubkeyAuthentication yes` — aceita autenticação por chave SSH. É o padrão da indústria; o autor diz que nunca desativaria isso a não ser que exista um sistema comprovadamente melhor.
- Desativação de qualquer outro tipo de autenticação: sem autenticação por senha (evita brute force), sem permitir senha vazia, sem permitir login de root.
- `AllowTcpForwarding` — no exemplo do vídeo estava como `yes` porque seria necessário em um vídeo seguinte sobre SSH Tunnels; normalmente, se não for necessário redirecionamento TCP, essa opção fica como `no`.

Sobre a ferramenta de hardening mencionada no início: o preset "paranoico" fecha praticamente tudo, mantendo só `PubkeyAuthentication` (inclusive desativa `AllowTcpForwarding`); o preset "equilibrado" já libera esse redirecionamento. A ideia é começar restritivo e ir liberando conforme a necessidade.

Como o servidor está configurado para não aceitar autenticação por senha, isso muda a forma como a configuração do lado cliente precisa ser feita — não existe fallback de senha.

## Primeira tentativa de conexão (sem chave)

Descobrindo os IPs dos dois containers Docker usados como exemplo (cliente e servidor) via:

```bash
ip -4 -brief address show eth0
```

Servidor: `10.0.0.3`. Cliente: `10.0.0.2`. O mesmo nome de usuário (`otavio`) foi mantido nos dois lados, por conveniência do Compose usado no exemplo — não é obrigatório, é possível ter usuários com nomes diferentes em cada lado.

Tentativa de conexão:

```bash
ssh otavio@10.0.0.3
```

Nessa primeira conexão a um host desconhecido, o SSH pergunta se a autenticidade do host é confirmada (proteção contra alguém se passando pelo servidor no meio da rede) — respondendo `yes`, a fingerprint é registrada. Como o cliente ainda não tem chave nenhuma e o servidor só aceita autenticação por chave pública, a conexão falha com `Permission denied (publickey)`.

## Criando a estrutura ~/.ssh manualmente

Ao tentar qualquer operação SSH, o diretório `~/.ssh` já é criado automaticamente pelo OpenSSH com permissão restrita: apenas o próprio usuário tem acesso total (leitura, escrita e execução).

Recomendação geral de permissões:

- Chaves privadas: leitura (e escrita) apenas para o dono.
- `authorized_keys` (parte pública): leitura e escrita para o dono, leitura para grupo e outros — ou, alternativamente, apenas o dono ter qualquer acesso. O autor relata nunca ter tido problema mantendo apenas o dono com acesso total.

Para criar a estrutura manualmente (caso `~/.ssh` não exista), o comando `install` é usado por já cuidar de criação de diretório/arquivo, permissões e dono/grupo numa tacada só (em vez de `mkdir` + `chmod` + `chown` separados):

```bash
install -d ~/.ssh -m 700 -o $(whoami) -g otavio
```

- `-d` indica que é um diretório.
- `-m 700` dá todas as permissões ao dono e nenhuma a mais ninguém.
- `-o` define o dono (owner).
- `-g` define o grupo.

Para criar o arquivo `authorized_keys` dentro desse diretório, com permissão `644` (leitura/escrita para o dono, leitura para grupo e outros), usando `/dev/null` como fonte de conteúdo vazio (já que não se está usando `-d` para diretório, mas criando um arquivo):

```bash
install -m 644 -o otavio -g otavio /dev/null ~/.ssh/authorized_keys
```

## Gerando o par de chaves

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_two
```

- `-t ed25519` define o algoritmo.
- `-f` define o caminho/nome do arquivo da chave. Convenção seguida no vídeo: prefixar com `id_` para indicar que é um `IdentityFile`, e nomear conforme o destino/uso da chave (`id_two` para a chave usada especificamente para acessar o host "two").

O `ssh-keygen` pergunta por uma *passphrase* opcional — uma senha adicional para usar a própria chave. É mais seguro (boa prática), mas exige digitar a passphrase toda vez que a chave for usada/carregada no agente SSH. O autor admite que, na prática, não costuma usar passphrase — prefere gerar uma chave dedicada por serviço.

O comando gera dois arquivos dentro de `~/.ssh`:

- A chave privada (`id_two`), com permissão restrita a leitura/escrita apenas para o dono — a parte que nunca deve ser compartilhada ou exposta.
- A chave pública (`id_two.pub`), com leitura/escrita para o dono e leitura para grupo e outros — a parte que pode (e deve, quando necessário) ser compartilhada com quem vai autorizar o acesso.

Nunca se deve compartilhar o arquivo sem a extensão `.pub` — apenas a chave pública sai do computador. Sem a chave privada correspondente, a chave pública sozinha não permite acesso a nada.

Para visualizar a chave pública a compartilhar:

```bash
cat ~/.ssh/id_two.pub
```

## Autorizando o acesso: copiando a chave pública para authorized_keys

No host que vai *receber* a conexão (o "servidor" do exemplo), depois de garantir a estrutura `~/.ssh` e `authorized_keys` (mesmos passos de `install` mostrados acima), basta colar o conteúdo da chave pública gerada no cliente dentro do `authorized_keys` do servidor:

```bash
echo "<conteúdo-da-chave-publica>" >> ~/.ssh/authorized_keys
```

Isso é a configuração padrão; se o caminho do `authorized_keys` for alterado no `sshd_config`, a configuração do servidor precisa refletir isso.

Depois de colar a chave pública no `authorized_keys` do servidor, a conexão especificando explicitamente a identidade funciona:

```bash
ssh otavio@10.0.0.3 -i ~/.ssh/id_two
```

- `-i` aponta para o arquivo de identidade (chave privada) a ser usado na autenticação.

## Configurando o sentido inverso

O mesmo processo, espelhado: no host "two", gerar um novo par de chaves (`ssh-keygen -t ed25519 -f ~/.ssh/id_one`), copiar a chave pública gerada e colá-la no `authorized_keys` do host "one". A partir daí, a conexão inversa também funciona:

```bash
ssh otavio@10.0.0.2 -i ~/.ssh/id_one
```

Com as duas direções configuradas, é possível encadear conexões: do host "two", conectar no "one"; de dentro do "one", conectar de volta no "two"; e assim por diante — cada sessão SSH aninhada precisa ser encerrada (`exit`) na ordem inversa em que foi aberta para voltar à conexão original.

## Arquivo de configuração do cliente (~/.ssh/config)

Para evitar digitar usuário, IP, porta e caminho da chave toda vez, o cliente SSH suporta um arquivo `~/.ssh/config` com blocos por host, criando apelidos (aliases):

```
Host two
    HostName 10.0.0.3
    User otavio
    Port 22
    IdentityFile ~/.ssh/id_two
    IdentitiesOnly yes
```

- `HostName` é o IP ou domínio real do destino.
- `IdentitiesOnly yes` restringe o SSH a usar apenas a identidade especificada — importante quando há muitas chaves configuradas, pois o SSH tenta cada uma em ordem e pode esgotar o número de tentativas antes de chegar na chave certa.

Com esse bloco, `ssh two` já resolve para o comando completo equivalente. O mesmo bloco espelhado (trocando o alias, `HostName` e `IdentityFile`) pode ser criado no outro host para permitir `ssh one` a partir dele.

## Encerramento

O vídeo é descrito como o "básico" sobre SSH, servindo de base para um vídeo seguinte sobre SSH Tunnels (que reaproveita a configuração `AllowTcpForwarding yes` mencionada durante a configuração do servidor).
