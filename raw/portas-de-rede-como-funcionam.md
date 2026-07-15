# Portas de Rede — Como Funcionam

Hoje vamos descobrir o que é uma porta e como as portas funcionam. Vamos começar olhando algumas coisas essenciais primeiro.

## O que é uma porta

Portas são usadas principalmente para comunicação em rede, mas também ajudam programas na mesma máquina a conversarem entre si. Programas precisam de números de porta para enviar e receber dados, tanto localmente quanto pela rede. Em outras palavras, portas funcionam como portas (no sentido de "porta de entrada") para programas — elas garantem que os dados cheguem ao programa certo, seja no seu PC ou pela internet.

Um número de porta é um número virtual, parecido com um endereço IP. Não é um dispositivo físico — é só um número que indica para onde os dados devem ser enviados. Um detalhe importante: números de porta só existem no intervalo de 0 a 65.535.

## As portas mais conhecidas

- **Porta 80 — HTTP** (Hypertext Transfer Protocol). Aparece no início de endereços de sites. É usada frequentemente para websites e é insegura, porque os dados não são criptografados.
- **Porta 443 — HTTPS** (Hypertext Transfer Protocol Secure). A diferença do HTTP é que o "S" significa "secure" (seguro). Também aparece no início de endereços de sites. A diferença principal é que os dados são criptografados — ou seja, HTTP não é seguro, HTTPS é.
- **Porta 25 — SMTP**, usada para serviços de email.

## Como as portas funcionam na prática

Antes de mais nada, é importante entender o que é um IP. Um endereço IP é como o endereço do seu computador na internet — ele diz a outros dispositivos para onde enviar os dados. Portas e endereços IP trabalham juntos para alcançar serviços ou programas específicos. As portas 80, 443 e 25 estão sempre associadas a endereços IP.

### Exemplo

Este é o Paulo. Ele quer visitar um site. Para isso, primeiro ele precisa do endereço IP do servidor que hospeda o site — o IP indica a localização geográfica desse servidor.

Quando os dados chegam ao servidor, o servidor "pergunta" o que o usuário quer, porque servidores costumam oferecer serviços diferentes. É aí que os números de porta entram: eles dizem ao servidor qual "porta" (serviço) o usuário quer usar. No nosso exemplo, queremos apenas visitar um site simples — ou seja, queremos HTTP, que é a porta 80.

Resumindo: portas e endereços IP trabalham juntos. No exemplo, temos o IP 93.184.216.34 e a porta 80, geralmente combinados com dois-pontos (`93.184.216.34:80`).

- O endereço IP diz **onde** algo está na internet, geograficamente. O servidor tem um endereço IP, mas o nosso próprio computador também tem um.
- O número da porta diz a um dispositivo, como um servidor, **qual serviço** o usuário quer usar.

No exemplo, o IP diz onde o servidor está localizado no planeta; a porta diz que o usuário quer usar HTTP (porta 80).

### Analogia da casa

Imagine uma casa. Essa casa representa um servidor. O endereço da casa — digamos, "Rua das Flores, 1234" — é como o endereço IP: ele diz onde a casa está localizada. Só que uma casa tem portas (no sentido literal), e atrás de cada porta existe algo diferente. É isso que as portas de rede fazem: dizem qual porta queremos abrir. No nosso exemplo, isso pode ser SMTP, HTTPS ou HTTP — ou seja, porta 25, 443 ou 80. E como a porta 80 representa HTTP, é essa que estamos usando aqui.

## Como as portas são categorizadas

As portas são gerenciadas pela **IANA** (Internet Assigned Numbers Authority). A IANA é responsável por coordenar e manter o sistema global de endereços IP, nomes de domínio e números de porta, garantindo que tudo na internet fique organizado e funcione em conjunto de forma tranquila.

### 1. Portas conhecidas (well-known ports)

São usadas pelos serviços de internet mais comuns e essenciais — aqueles com os quais interagimos quase todos os dias. Exemplos: HTTP, HTTPS, SMTP e SSH.

SSH (Secure Shell) é um protocolo que permite acesso remoto a outro computador.

### 2. Portas registradas (registered ports)

Podem ser registradas oficialmente por desenvolvedores ou empresas para atribuir aplicações ou serviços específicos de forma única. Exemplos:

- **Porta 1433 — Microsoft SQL Server**: aplicação de banco de dados usada para armazenar grandes quantidades de dados, como informações de usuário, dados de site ou dados de outras aplicações.
- **Porta 3389 — RDP** (Remote Desktop Protocol): usada para acesso remoto ao Windows, permitindo controlar um computador a partir de outro PC. É basicamente o equivalente do Windows ao SSH, que é usado comumente em desktops Linux.

### 3. Portas privadas ou dinâmicas (private/dynamic ports)

Não são destinadas a servidores — são usadas no seu próprio computador para garantir que os dados voltem ao lugar certo.

Uma diferença fundamental: portas conhecidas e registradas se referem a **servidores**, para que clientes (você e eu) possam acessar serviços — por exemplo, para assistir a vídeos no YouTube. Já as portas privadas pertencem a **dispositivos finais**, como PCs.

#### Exemplo: assistindo a vídeos no YouTube

Imagine que queremos assistir a vários vídeos ao mesmo tempo. Esses vídeos são diferentes, então múltiplos fluxos de dados estão chegando simultaneamente. Quando o PC pede ao servidor do YouTube esses vídeos, os dados voltam, mas agora o PC precisa de uma forma de organizá-los — e é aqui que entram as portas privadas.

Sempre que o PC estabelece uma nova conexão com a internet — seja o YouTube ou um jogo online —, o sistema operacional atribui automaticamente um novo número de porta. Isso garante que os dados de retorno sejam enviados de volta para a porta correta no computador — aquela que fez a requisição originalmente.

- Queremos assistir a um vídeo do YouTube: o sistema operacional escolhe uma porta livre, digamos, a porta 50.000.
- Se abrimos uma segunda aba com um vídeo diferente, o sistema operacional atribui outra porta livre, por exemplo, 55.000.

Em outras palavras: o PC combina seu endereço IP local com o número de porta atribuído. Esse conjunto é então enviado ao servidor do YouTube, ao seu endereço IP, usando a porta 443 (a porta padrão para tráfego HTTPS). O servidor vê de qual endereço IP e porta veio a requisição — por isso ele envia os dados de retorno diretamente para o nosso IP e para a porta 50.000. Os dados chegam lá, e o sistema operacional sabe instantaneamente que pertencem àquela aba de vídeo específica.

## Estados de uma porta

Antes de irmos para a parte prática, é importante entender os diferentes estados em que uma porta pode estar.

- **Listening (escutando)**: a porta está esperando conexões de entrada. Isso normalmente acontece em servidores, mas também pode acontecer nos nossos próprios dispositivos — por exemplo, quando um app ou serviço local está esperando conexões. É importante saber que existe tanto tráfego de entrada quanto de saída: servidores principalmente recebem tráfego de entrada, enquanto nós geramos tráfego de saída ao visitar sites. Exemplo: a porta 80 de um servidor espera que clientes se conectem a um site — então a porta 80 está "listening".
- **Established/Connected (estabelecida/conectada)**: significa que há uma conexão ativa e dados estão sendo trocados entre dois dispositivos — por exemplo, quando estamos visitando um site no momento.
- **Closed (fechada)**: a porta não está em uso no momento. Não há conexão ativa e nenhum programa está "escutando" nela. Por isso, normalmente não vemos portas fechadas diretamente no CMD. Pode-se pensar em "closed" simplesmente como "a porta está desligada, não ativa".
- Existem também outros estados, como `TIME_WAIT` ou `CLOSE_WAIT`, mas eles não são importantes para iniciantes.

## Vendo portas na prática (CMD/Windows)

Agora que conhecemos os estados mais importantes de uma porta, podemos olhar ao vivo no CMD quais portas estão "listening" ou "established" e observar como isso se parece na prática.

1. Abra o CMD: vá até a barra de busca do Windows 10 (canto inferior esquerdo), digite `cmd` e pressione Enter.
2. Digite o comando `netstat -n` e pressione Enter. Você verá bastante texto com números e endereços IP — não se assuste, vamos passar por isso passo a passo.
   - **Proto**: protocolo. Na maior parte das vezes será TCP (Transmission Control Protocol), mas para este vídeo isso não é o mais importante.
   - **Local Address**: seu próprio endereço — basicamente, o seu dispositivo.
   - **Foreign Address**: com quem você está conectado — um servidor, por exemplo.
   - **State**: o status da conexão. Se aparecer "ESTABLISHED", significa que existe uma conexão ativa aberta no momento.

   Todos esses IPs e portas que aparecem fazem parte da comunicação de *loopback* — basicamente, tráfego interno no próprio computador (não entraremos em detalhes aqui, pois foge do escopo deste vídeo).

   No exemplo, vemos o endereço local (o IP do PC) junto com o número de porta dinâmica. Do outro lado, o endereço do servidor ao qual estamos conectados, junto com a porta 443 — ou seja, o PC está conectado a páginas HTTPS seguras (os IPs de servidor foram borrados por segurança; os exemplos mostrados são fictícios).

3. Digite `netstat -a` e pressione Enter. Isso mostra não só conexões estabelecidas, mas também as que estão "listening". Um pequeno exemplo: o endereço IP local com a porta **139** — usada frequentemente para compartilhamento de arquivos e impressoras na rede local. O estado diz "LISTENING", ou seja, a porta está esperando conexões de entrada. Na coluna "Foreign Address" aparece `0.0.0.0:0` — os quatro zeros são só um placeholder mostrando que não há conexão ativa, e o `:0` significa que também não há porta remota conectada. Nesse caso, nosso PC está agindo como um servidor.
