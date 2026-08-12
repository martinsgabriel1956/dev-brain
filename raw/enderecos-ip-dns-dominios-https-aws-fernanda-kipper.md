# Endereço IP, Domínio, DNS, HTTP/HTTPS e Configuração de Domínio na AWS

> Transcrição limpa e estruturada (PT-BR original, sem tradução necessária). Erros de reconhecimento de fala (ASR) corrigidos e normalizados: "WS" → AWS, "Golder/goldery" → GoDaddy, "versel" → Vercel, "Rot 53/route 63" → Route 53, "Fernand ker/keeper" → Fernanda Kipper, "kerd pon xyz" → `kdev.xyz`, "aaro" → Claro, "US East One" → us-east-1, "Middle Man" → Man-in-the-Middle, "Flu espes/Fluence" → Fluencypass, "cname/siname/C" → CNAME.
>
> **Autora:** Fernanda Kipper (canal do YouTube)

---

## Introdução

Endereço IP, protocolo IPv4, domínio, servidor DNS — todos esses termos formam a base da estrutura da internet. Se você quer ser um desenvolvedor web (frontend ou backend), precisa entender esses conceitos. Neste vídeo discutimos a teoria por trás desses termos e, no final, fazemos a configuração de um domínio personalizado na AWS, fazendo o deploy de um site.

---

## Endereço IP

O **endereço IP** é uma sequência numérica usada para identificar o endereço de um dispositivo conectado a uma rede. Essa rede pode ser tanto uma rede de computadores (privada) quanto a internet.

Nem sempre estar conectado a uma rede significa estar conectado à internet: pode existir uma rede privada em que os computadores da minha casa ou empresa conversam entre si, mas não com o mundo exterior.

**Analogia:** o endereço IP é como o endereço de uma casa — a rua e o número identificam onde a casa está. O IP identifica a posição/endereço do dispositivo dentro da rede.

### IPv4

**IPv4** é a versão 4 do protocolo da internet. Cada versão do protocolo define novos padrões; o maior padrão definido pelo IPv4 é o **formato dos endereços IP**.

- Formato: quatro grupos de números separados por ponto, cada grupo variando de **0 a 255** (na fala aproximada, "0 a 256").
- Exemplos válidos: `192.168.1.1`, `198.123.255.255`.
- Como o número de grupos e o intervalo são finitos, o total de endereços IPv4 é finito: **aproximadamente 4,3 bilhões**.

O problema: já existe um número muito próximo de 4,3 bilhões de dispositivos conectados à internet. Em algum momento os endereços IPv4 vão acabar — não haverá mais endereços disponíveis para novos dispositivos.

### IPv6

**IPv6** é a versão 6 do protocolo da internet e estabelece um novo formato para os endereços IP, resolvendo o esgotamento do IPv4.

- O IPv4 ainda é a versão **mais utilizada**, adotada por todos os servidores e com suporte universal.
- Provedores de nuvem e de internet já começaram a adotar o IPv6 para identificar servidores. É uma adoção gradual (já ocorre há anos e vai continuar por mais anos).
- Hoje há **coexistência** entre IPv4 e IPv6. Em algum momento o IPv4 vai "morrer" e o IPv6 assumirá, mas por enquanto "endereço IP" quase sempre significa IPv4.

---

## Domínio

O **domínio** é um nome legível pelos humanos para endereços de servidores na internet. Em vez de decorar uma sequência numérica enorme (como um endereço IPv4), decoramos um nome.

No navegador, digitamos `google.com` ou `fernandakipper.com` porque é fácil de lembrar — não digitamos `192.178.255.255`. O domínio é, na prática, uma **tradução** de endereços IP para nomes legíveis.

Em algum momento, porém, essa tradução do domínio para o endereço IP precisa acontecer. Quem faz isso é o servidor DNS.

### Anatomia de um domínio (nome + TLD)

Um domínio é composto por **duas partes**:

1. **Nome personalizado** — a parte inicial escolhida por quem registra.
2. **Extensão / TLD (Top Level Domain)** — a extensão do domínio.

O ponto separa as duas partes: `nomepersonalizado.extensao`.

- `testefef.tech` → nome = `testefef`, TLD = `.tech`.
- `fernandakipper.com` → nome = `fernandakipper`, TLD = `.com`.

Domínios com o **mesmo nome e TLD diferente são domínios diferentes**. `fernandakipper.com` e `fernandakipper.com.br` são domínios distintos e poderiam pertencer a pessoas diferentes. (No caso, a autora comprou os dois e redirecionou ambos para a mesma página.)

Ao pesquisar em um registrador (ex.: Hostinger), `fernandakipper.com` aparece como indisponível ("already taken"), mas variações como `fernandakipper.net`, `.info`, `.xyz` podem estar disponíveis. As extensões mais populares são `.com` e `.com.br`; `.org` é muito usada por órgãos governamentais/regulamentados.

---

## Servidor DNS

Os **servidores DNS** são servidores espalhados pelo mundo todo que funcionam como uma **agenda telefônica**: recebem uma requisição (normalmente enviada pelo provedor de internet) e devolvem o endereço IP correspondente ao domínio.

Fluxo ao acessar `fernandakipper.com`:

1. A requisição sai do computador e vai para o provedor de internet (ex.: Claro).
2. O provedor se conecta a um servidor DNS para **resolver** o domínio em endereço IP.
3. O DNS devolve, por exemplo, `192.178.255.212`.
4. O computador envia a requisição ao servidor onde o site está rodando.
5. O servidor responde com os arquivos do site (HTML, CSS, JavaScript etc.).

### Demonstração: descobrir o IP de um domínio

Usando um site do tipo "find IP address of domain", ao buscar `fernandakipper.com` retornou o IP `76.76.21.241`. Acessando esse IP diretamente no navegador, caiu no site da **Vercel** — porque o site está **hospedado na Vercel**.

Na Vercel, o projeto tem os domínios conectados (`fernandakipper.com.br`, `www.fernandakipper.com`, `fernandakipper.com`), todos apontando para o servidor da Vercel. O domínio foi comprado na **GoDaddy** (há mais de 3 anos; os domínios mais novos da autora estão na Hostinger). No painel de DNS da GoDaddy, os **servidores de nome (name servers)** foram configurados para encaminhar para os servidores da Vercel. Por isso, ao buscar o IP do domínio, retorna o IP de um servidor da Vercel.

---

## Configuração de um domínio na AWS

### Route 53 e a zona hospedada

O **Route 53** é o serviço da AWS para gerenciar domínios e DNS, redirecionando o domínio para aplicações rodando na AWS.

- Cria-se uma **zona hospedada (hosted zone)** — um mapeamento do domínio usado depois para apontar para serviços/aplicações na AWS.
- É essencial usar **exatamente** o domínio registrado (nome personalizado + TLD corretos). Ex.: domínio de teste `kdev.xyz`.
- **Zona hospedada pública**: domínio disponível na internet, acessível por qualquer pessoa.
- **Zona hospedada privada**: acessível apenas por quem está dentro da rede (ex.: VPN da empresa). Muitas empresas têm sites internos acessíveis só via VPN — desconectando, o site não abre porque o domínio é privado.

Ao criar a zona hospedada, o Route 53 gera **registros do tipo Name Server (NS)**, indicando para quais servidores o tráfego deve ser roteado.

### Apontar o registrador para os name servers da AWS

No painel do registrador (GoDaddy, no caso), troca-se os servidores de nome do domínio para os **name servers gerados pelo Route 53** (quatro servidores: `.org`, `.net`, `.com` etc.). Antes o domínio apontava para os servidores da GoDaddy; agora aponta para os da AWS.

**Propagação:** a alteração demora alguns minutos porque precisa ser **replicada** para todos os servidores DNS espalhados pelo mundo. Enquanto propaga, é possível continuar as demais configurações. Existem sites "DNS propagation checker" (ex.: dnschecker.org) que mostram, servidor por servidor no mundo, para onde o domínio está apontando (durante a propagação alguns ainda mostram o endereço antigo da Vercel, outros já mostram o da AWS).

### Site estático no S3 (conexão HTTP)

O site está em um **bucket S3 público** (`kdev.xyz`), acessível pela URL de site estático do bucket (o `index.html` renderiza "home works").

Para o domínio apontar direto para o bucket, cria-se no Route 53 um registro com **Alias → site do S3**, escolhendo a **região** (ex.: us-east-1) e o bucket. Isso já roteia o tráfego do domínio para o S3.

**Limitação:** esse mapeamento simples entrega apenas uma **conexão HTTP**. O endpoint de site estático do S3 é uma URL `http://` (sem certificado SSL), então o navegador marca como **"não seguro" (not secure)**.

---

## HTTP vs HTTPS

Ambos são **HyperText Transfer Protocol**. A diferença:

- **HTTP** — só o protocolo, **sem camada de segurança**, sem criptografia na transferência de dados entre cliente e servidor.
- **HTTPS** — HyperText Transfer Protocol **Secure**, a mesma coisa com uma **camada de segurança**. Envolve criptografia com **troca de chaves** entre o navegador e o servidor.

**Risco do HTTP puro:** ataque **Man-in-the-Middle** — alguém no meio pode alterar a requisição/resposta ou se passar pelo servidor. No HTTPS esse risco cai muito por causa da criptografia de ponta a ponta.

**Certificado SSL:** é um certificado digital que garante que quem responde à requisição é **realmente o dono daquele domínio**. Importante: o SSL **não** garante que o dono do domínio é a empresa que você imagina — garante apenas que quem responde é o dono do domínio acessado. Por isso é preciso atenção com **domínios parecidos** (ex.: `adidas` vs. `aidas`): um golpe pode ter HTTPS válido (conexão "segura"), mas o domínio é diferente. Acessando `adidas.com.br` via HTTPS, garante-se que quem responde é o dono de `adidas.com.br`.

---

## Adicionando HTTPS: ACM + CloudFront

Para ter HTTPS no domínio, é preciso configuração adicional. Exclui-se o registro direto para o S3 e faz-se:

### 1. Certificado SSL no AWS Certificate Manager (ACM)

No **Certificate Manager**, solicita-se um certificado para o domínio (`kdev.xyz`). Para provar a propriedade do domínio, o ACM fornece um **valor CNAME** (nome + valor) que deve ser cadastrado no DNS do domínio.

No Route 53, cria-se um registro do tipo **CNAME** com o nome e o valor fornecidos pelo ACM. Quando o ACM "bate" no domínio e encontra esse valor, valida que o solicitante é o dono do domínio e **emite o certificado** (status: emitido / êxito).

### 2. Distribuição CloudFront

Com o certificado, cria-se uma **distribuição no CloudFront** (serviço de content delivery / CDN da AWS) para servir o site via HTTPS:

- **Origem:** o bucket S3 (`kdev.xyz`), habilitando "use website endpoint".
- **Viewer protocol policy:** "Redirect HTTP to HTTPS" (toda requisição HTTP é redirecionada para HTTPS).
- **Web Application Firewall:** desabilitado por enquanto.
- **Custom SSL certificate:** o certificado SSL criado no ACM.
- **Alternate domain name (CNAME):** adicionar `kdev.xyz`.

> Observação: se fosse um backend rodando em Lambda ou EC2, seria preciso um **Load Balancer** em vez de CloudFront. Como aqui é um frontend estático no S3, usa-se CloudFront.

### 3. Apontar o domínio para o CloudFront no Route 53

No Route 53, cria-se um registro do tipo **A** com **Alias → distribuição CloudFront** (que já traz automaticamente o domain name da distribuição). Isso faz o domínio apontar para o CloudFront, que aponta para o S3, com redirecionamento HTTP→HTTPS e o certificado SSL.

Após a propagação, ao acessar `kdev.xyz` a conexão já é **HTTPS** e retorna o `index.html` do bucket S3 ("homeworks").

---

## Resumo dos conceitos

Aprendemos o que é: domínio, endereço IP, servidores DNS, como funcionam as conexões HTTP e HTTPS, o que é o certificado SSL. E configuramos, na AWS, um domínio apontando para um CloudFront que redireciona para um site estático hospedado em um bucket do S3.

## Bloco patrocinado (condensado)

Patrocínio da **Fluencypass** (escola de inglês da autora), com oferta de aniversário em junho: desconto de até 47%, 12 meses de garantia, acesso ao módulo de inglês para negócios e aulas particulares em dobro (do plano Professional). Conteúdo comercial, sem relação técnica com o tema do vídeo.
