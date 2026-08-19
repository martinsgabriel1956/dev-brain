# XSS na Prática — Reflected, Stored e DOM-based (DVWA)

Transcrição de vídeo (pt-BR, ASR bruto limpo e pontuado; já estava em português, sem necessidade de tradução). Autor: Luiz Viana, especialista em hacking/pentest. Plataforma de treino citada: "Solyd" (ouvido como "Solid One" no áudio). Laboratório usado na demonstração: DVWA (Damn Vulnerable Web Application).

## Abertura

Eu consigo executar o código que eu quiser no seu navegador, roubar suas senhas, capturar seus dados bancários e até mesmo tomar controle completo das suas contas online — tudo isso fazendo você simplesmente clicar num link. Parece impossível, então deixa eu te mostrar como milhões de sites pelo mundo inteiro estão vulneráveis a um dos ataques mais comuns mas devastadores da internet: o cross-site scripting, mais conhecido como XSS.

Muito prazer, eu sou o Luiz Viana, especialista em hacking, pentest, e neste vídeo eu vou te ensinar tudo sobre cross-site scripting na prática: desde como funciona, até como identificar e explorar essa falha em pentests e programas de bug bounty.

Não preciso nem falar que esse conteúdo é apenas para fins educacionais — só faça qualquer teste de segurança em sistemas que você tem permissão para fazer. Tem um monte de programas de bug bounty abertos por aí onde você pode procurar por falhas e ainda ganhar uma boa grana se encontrar.

## O que é XSS

XSS significa cross-site scripting (o X aparece ali para não ficar igual a CSS e causar confusão). Traduzindo: "execução de scripts entre sites" — basicamente quando o atacante consegue injetar código client-side JavaScript numa página legítima, e quando a vítima acessa essa página o código executa no navegador dela como se fosse parte do site.

A vulnerabilidade de XSS acontece quando a aplicação web recebe dados do usuário e coloca isso diretamente na página HTML sem nenhuma validação ou sanitização. Exemplo: um formulário de busca numa loja online onde você busca por "notebook" e o site responde "você pesquisou por notebook". Por trás dos panos, o servidor está pegando o que você digitou naquele parâmetro e jogando na página. Parece inofensivo, mas se ao invés de "notebook" eu colocar um código HTML/JavaScript malicioso, quando o HTML for retornado o navegador vai processar isso e executar o código como se fosse parte do site.

## Os três tipos de XSS

**Reflected XSS** — o mais simples de entender. O código é injetado através da própria requisição HTTP, seja por um parâmetro na URL ou por dados de um formulário via POST. O atacante cria uma URL maliciosa que, se a vítima clicar, o site processa essa requisição e inclui o payload malicioso na resposta que vai para o navegador da vítima. O código então pode roubar cookies, efetuar qualquer ação com a sessão ativa daquele site — por isso o XSS é tão perigoso.

**Stored XSS** — o código malicioso fica armazenado permanentemente no servidor do site (num comentário, numa mensagem de fórum, no perfil do usuário). A diferença é que aqui não é preciso nem enviar um link para a vítima: qualquer pessoa que acessar aquela página vai executar o código malicioso automaticamente.

**DOM-based XSS** — o código malicioso é injetado na página diretamente pelo navegador, ou seja, o payload não passa pelo servidor. O JavaScript da própria página pega dados do usuário de forma insegura e reflete isso como HTML, ou passa por uma função insegura que acaba executando. Esse tipo é especialmente perigoso porque acontece totalmente no lado do cliente — nem sempre o ataque aparece nos logs do servidor, e nem um WAF conseguiria detectar.

## Demonstração prática — laboratório DVWA

Laboratório usado: DVWA (Damn Vulnerable Web Application), disponível na plataforma Solyd (basta clicar em "conectar" para levantar uma máquina isolada pronta para teste). Login: usuário `admin`, senha `password`. O DVWA tem um seletor de nível de segurança (DVWA Security: low / medium / high / impossible) e sessões dedicadas para DOM XSS, Reflected XSS e Stored XSS.

### DOM XSS

**Nível low**: a página tem um seletor de idioma que manipula a URL via parâmetro. Um script na página pega o conteúdo do parâmetro e insere como uma opção no dropdown. Injetando `<script>alert(1)</script>` no parâmetro, o navegador interpreta e executa o script — DOM XSS confirmado.

**Nível medium**: o mesmo payload de script é removido — existe um filtro no servidor que corta a tag `<script>` na resposta. Como a lógica de montagem do HTML acontece inteiramente no JavaScript da própria página (client-side), é possível usar uma hashtag (`#`) na URL: tudo que vem depois da hashtag nunca é enviado ao servidor, fica só no navegador. Como o filtro roda no servidor, ele nunca vê o payload — e o JavaScript do lado do cliente processa o conteúdo normalmente, executando o script.

**Nível high**: o mesmo payload de hashtag ainda funciona nesse laboratório específico. Em geral, quando um filtro bloqueia a tag `<script>` mas não trata outras tags (ex.: `<img>`), é possível usar um vetor como `<img src=x onerror=alert(1)>` — o atributo `src` aponta para algo inexistente, dispara o evento `onerror`, e o navegador executa o JavaScript sem nunca usar a palavra "script".

### Reflected XSS

**Nível low**: campo de nome — o valor digitado é refletido diretamente na página ("Hello, <valor>"). Injetando `<script>alert(1)</script>` o alerta executa.

**Nível medium**: a tag `<script>` é removida do valor antes da resposta ser montada (o alerta mostrado antes, no vídeo, veio de um teste anterior — sem a tag script o payload não roda). Testando outras tags, `<img>` não é filtrada, então `<img src=x onerror=alert(1)>` funciona.

**Nível high**: mesmo payload de `<img src=x onerror=alert(1)>` ainda funciona nesse laboratório.

Com esse tipo de acesso, o código executado poderia ser qualquer coisa: roubar cookies de sessão via `document.cookie`, enviar isso para um servidor do atacante e obter acesso à sessão da vítima, ou efetuar qualquer ação em nome dela. Controle total do navegador da vítima, só enviando um link.

### Stored XSS

**Nível low**: formulário com campo de nome e campo de mensagem (guestbook). Um payload `<script>alert(1)</script>` na mensagem é salvo no banco sem sanitização — toda vez que a página é carregada, o payload roda, porque o valor armazenado é renderizado como código, não como texto.

**Nível medium**: existe um filtro que remove a tag `<script>` (inclusive tentativas de burlar duplicando a tag, ex. `<scr<script>ipt>`, continuam sendo neutralizadas — o filtro aplicado ao campo de mensagem parece robusto). O campo de nome tem um `maxlength` de 10 caracteres no HTML, mas essa é uma restrição client-side: removendo o atributo `maxlength` via DevTools, é possível inserir um payload maior nesse campo. Ainda assim, o filtro do lado do servidor também se aplica ao campo de nome — a primeira tentativa com `<script>` é neutralizada, mas usando `<img src=x onerror=alert(1)>` no lugar (depois de remover o `maxlength`), o payload passa e o alerta executa.

**Nível high**: a mesma técnica (remover `maxlength` via DevTools + payload de `<img>` ou de `<body onload=alert(1)>` no campo de nome/mensagem) ainda consegue passar pelo filtro e executar.

**Nível impossible**: nenhum dos payloads testados (`<img>`, remoção de `maxlength`, etc.) funciona mais — o campo faz sanitização de fato: o navegador recebe texto, não código, e não interpreta nada como script.

## Mitigação

O que neutraliza XSS é sanitizar a entrada do usuário: ao invés do navegador receber código, ele recebe texto (encoded) — não executa, não interpreta. Existem outras camadas de proteção complementares, como o Content Security Policy (CSP), que indica ao navegador de onde ele pode aceitar scripts. Mas se o CSP estiver mal configurado, ainda é possível fazer bypass.

## Fechamento

Existem milhões de aplicações web gigantescas com vulnerabilidades tão simples quanto as demonstradas no DVWA. Também existem cenários muito mais complexos — bypass de CSP, DOM XSS avançado, WAF na frente da aplicação bloqueando payloads que exigem bypass antes de qualquer coisa. Mas só com o conteúdo desse vídeo, quem se aventurar no mundo do bug bounty tem grandes chances de encontrar alguma falha.
