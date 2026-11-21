---
type: source
title: "Hospedagem na HostGator, parte 3: upload em public_html, FileZilla, domínios adicionais e AutoSSL (FrontPUSH)"
aliases: ["FrontPUSH hospedagem aula 06", "Hostgator pt. 3", "Módulo de hospedagem, aula 06", "domínios adicionais no cPanel"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 0
tags: [hospedagem, hospedagem-compartilhada, hostgator, cpanel, public-html, upload, ftp, sftp, filezilla, addon-domain, virtual-host, autossl, ssl, tls, site-estatico, php, react, gsap, curso, frontend, networking]
skill: tech-mentor-networking
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-21
---

# Hospedagem na HostGator, parte 3: upload em public_html, FileZilla, domínios adicionais e AutoSSL (FrontPUSH)

## TL;DR

Sexta aula do módulo de hospedagem do [[wiki/entities/frontpush|FrontPUSH]], cerca de 20 minutos, sem slide, no [[wiki/entities/cpanel|cPanel]] da [[wiki/entities/hostgator|HostGator]] e no [[wiki/entities/filezilla|FileZilla]]. [[wiki/entities/nasser|Násser]] não se apresenta; autoria pela sequência e pelos projetos próprios. Fecha o "tutorial" da HostGator: onde os arquivos vão, como três domínios dividem o servidor e como sai o HTTPS.

- **`public_html` é a raiz do domínio principal:** lá está o portfólio dele, `index.html` com GSAP "como um script, eu não utilizei nenhum npm" ([[wiki/entities/gsap]]).
- **Por que o portfólio é estático:** "qual é a funcionalidade que eu preciso que ele tenha? Nenhuma." Página de vendas idem: "texto, imagem e link"; estático é "bem leve", "bem escalável", "bem mais performático" ([[wiki/concepts/site-estatico-vs-dinamico]]).
- **Upload:** "carregar" no gerenciador de arquivos; o `index.html` executa "por padrão". Ou [[wiki/concepts/ftp|FTP]] pelo FileZilla com IP, usuário e senha; o aviso de segurança aparece porque o FTP "não é criptografado".
- **Subpastas:** "tudo são pastinhas, tudo são diretórios": `/Nubank` e `/Spider-Man` no mesmo domínio ([[wiki/entities/nubank]], [[wiki/entities/spider-man-projeto-nasser]]).
- **Domínios adicionais:** FrontPUSH e [[wiki/entities/creatorpush|CreatorPUSH]] apontam para o mesmo servidor DNS; no cPanel, cada um ganha a raiz `public_html/frontpush` e `public_html/creatorpush` ([[wiki/concepts/virtual-host]]).
- **Por que o FrontPUSH é PHP:** precisa de "outras páginas" (cadastro, lista de espera); "para fazer uma rota em React, eu tenho que configurar todo um ecossistema, com PHP é bem mais fácil", e o PHP vem pronto ([[wiki/entities/php]]).
- **AutoSSL:** status do certificado verde ou vermelho por domínio; "executar AutoSSL" em todos ([[wiki/concepts/http-vs-https]]).

## Key Claims

### Abertura

- Se faltou algo do cPanel, "não hesitem em pesquisar": "hoje em dia o cPanel vem com muita coisa instalada", e HostGator e [[wiki/entities/hostinger|Hostinger]] têm "blogs inteiros" de tutorial.
- Objetivo: passar os arquivos "local na sua máquina" para o servidor, "para quando você digitar www.frontpush.com.br, ele acessar a pasta certa".

### A pasta public_html

- "Você sempre vai procurar por essa pastinha aqui, que é a public-underline-html [...] ela é a pasta raiz de quando você acessa o seu domínio."
- O domínio principal (o pessoal, grafado "nucfile"/"nucfl"/"NUCFI" pela legenda) abre o portfólio: `index.html`, svg, src, js, imagem, css. "Eu não digitei nenhuma barra para entrar em nenhuma pasta. Então eu estou entrando na pasta raiz."

### Por que o portfólio é estático

- "Inteiramente feita com HTML, CSS e JavaScript. Tem uma biblioteca em JavaScript, que é a GSAP, porém eu adicionei a página como um script, eu não utilizei nenhum npm." "É um website estático, porque ele não detém de nenhuma funcionalidade a mais."
- "Esse é o grande porquê" das aulas anteriores ([[wiki/sources/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react]]). O portfólio só precisa reunir links, contato, e-mail e trabalhos: "para que eu vou fazer uma aplicação web que vai me demandar bem mais trabalho de configuração de ambiente, de buildar".
- Página de vendas: "só precisa de texto, imagem e link"; "algum modal [...] só com JavaScript puro você já consegue fazer". "Não há necessidade de você complicar o processo."
- "Ah, eu vou lá fazer o React, mas [...] você vai ter que buildar todo o ecossistema do React no servidor para poder isso funcionar" (ver Precisões).
- Estático é "bem leve, vai ser bem escalável", "não precisa carregar todo um ambiente para poder rodar", "bem mais performático". "Avaliar qual é a aplicação que você está buildando, se é necessário mesmo ou não."

### Upload pelo gerenciador de arquivos

- "Clicar em carregar", escolher os arquivos do portfólio e enviar. "Quando ele ver index.html, por padrão, ele já vai executar o que tem nessa página index.html, que é a minha página única e principal" ([[wiki/concepts/servidor-web-vs-servidor-de-aplicacao]]).

### Upload pelo FileZilla

- "Programas FTP, onde basicamente eu tenho o FileZilla, que é, inclusive, indicado pelo próprio pessoal do HostGator": IP do servidor, usuário e senha. IP na tela: `162.241.61.25`.
- "Pode ser que apareça uma dialogue de segurança [...] porque o FTP [...] não é criptografado [...] é só você clicar em sim. Se você quer algo criptografado, [...] ele não envia FTP, mas envia SFTP, basicamente só muda isso, mas é o mesmo protocolo de transferência" (ver Precisões).
- `public_html` no FileZilla "é exatamente a mesma pasta" do gerenciador. Arrastar a pasta "NY" do portfólio; arquivos com o mesmo nome são substituídos.

### Projetos em subpastas

- "Tudo são pastinhas, tudo são diretórios, então o seu site é um diretório": uma pasta `Nubank` dentro da raiz vira `domínio/Nubank`, "o projeto do Nubank"; o mesmo com `Spider-Man`. "Porém, contudo, entretanto, eu estou utilizando o mesmo domínio."

### Domínios adicionais

- "Eu preciso primeiro registrar um novo domínio": FrontPUSH e CreatorPUSH "apontam também para esse mesmo servidor DNS" ([[wiki/concepts/name-server]]).
- No cPanel, "domínios adicionais": "quando você receber esse domínio como requisição, eu quero que você direcione ele para uma outra pasta, que não seja a pasta raiz". Em vez de `public_html`, "public_html, barra frontpush"; a pasta é criada no gerenciador de arquivos. O CreatorPUSH aponta para `public_html/creatorpush`, "que também tem uma página estática".
- "O FrontPUSH não é uma página estática, ele é uma aplicação web em PHP, [...] está agora index.php."

### Por que o FrontPUSH é em PHP

- "Na página do FrontPUSH eu tenho [...] outras páginas dentro dela que eu preciso de uma navegação dentro do site": "uma página de cadastro", "entrar para a lista de espera".
- "Eu não vou fazer uma aplicação web em React que vai me demandar bem mais configurações para algo muito simples, porque eu só quero uma rota diferente aqui dentro, para fazer uma rota em React, eu tenho que configurar todo um ecossistema, com PHP é bem mais fácil."
- O cPanel "já vem com o PHP já todo instalado, porque ele já vem preparado para o WordPress"; "o procedimento é exatamente o mesmo que uma página estática", "mas é porque a HostGator já deixa pré-configurado e instalado o Apache nesse servidor, então não se engane" ([[wiki/entities/wordpress]], [[wiki/entities/apache-http-server]]).
- Resumo: "adiciono um domínio adicional, redirecionando para uma pasta em específico que eu mesmo crio [...] é assim que eu consigo ter vários sites"; Nubank e Spider-Man ficam em subpastas, sem domínio próprio.

### Certificado SSL com AutoSSL

- "Muito fácil, porque ele já vem na interface gráfica": "ele vai te gerar uma chave, a chave padrão para o seu SSL barra TLS certificado".
- "Status do certificado SSL barra TLS": domínios sem AutoSSL "vai ficar vermelho"; "estão todos verdinhos". Para um domínio novo, "selecionar aqui todos os domínios e executar AutoSSL".
- "Se eu fosse fazer por linha de comando eu teria que pegar um certificado e instalar ele manualmente", mas "tanto o cloud como o cPanel" fazem isso "de maneira fácil e rápida".

## Precisões e ressalvas

1. **O build do React não é feito no servidor.** Roda na máquina (ou no CI), e a pasta `build`/`dist` resultante é HTML, CSS e JS estático, subido igual ao portfólio, sem Node no servidor `[external]` (https://create-react-app.dev/docs/deployment/; alta). O argumento "React = ecossistema no servidor" repete o erro da aula 03.
2. **Várias páginas não pedem PHP nem React.** `cadastro.html` com link já é navegação entre páginas num site estático. O motivo forte para PHP no FrontPUSH seria o **formulário** da lista de espera (gravar, mandar e-mail) e o reaproveitamento de cabeçalho e rodapé por `include` (inferência, média; a aula fala em "rota").
3. **SFTP não é "o mesmo protocolo".** SFTP é o protocolo de arquivos do SSH (porta 22; na HostGator compartilhada o SSH costuma ficar na 2222 `[external, não verificado]`); FTP com criptografia é **FTPS** (TLS). Clicar "sim" no aviso do FileZilla manda a senha do cPanel em claro; melhor escolher "FTP explícito sobre TLS" ou SFTP ([[wiki/concepts/ftp]]) (alta).
4. **Domínio adicional tem efeitos colaterais.** Com a raiz em `public_html/frontpush`, o FrontPUSH também abre em `dominio-principal/frontpush` e, nas versões antigas do cPanel, num subdomínio `frontpush.dominio-principal` criado junto. Raízes fora de `public_html` evitam isso `[external]` (https://docs.cpanel.net; alta).
5. **Quem escolhe a pasta é o Apache, pelo nome pedido.** Domínio adicional é *virtual host* por nome: o servidor lê o cabeçalho `Host` (e o SNI, no HTTPS) e serve a raiz configurada. É a resposta à "vários sites no mesmo servidor" da aula 01 ([[wiki/concepts/virtual-host]]) (alta).
6. **URLs no Linux diferenciam maiúsculas.** `/Nubank` ≠ `/nubank` no Apache em Linux; pastas em minúsculas evitam 404 (alta).
7. **AutoSSL valida o domínio antes de emitir.** Fica vermelho, em geral, porque o DNS ainda não aponta para o servidor (delegação recente ou errada). O certificado (Let's Encrypt ou Sectigo) dura cerca de 90 dias e é renovado sozinho; a chave e o CSR são gerados automaticamente (alta).
8. **"SSL barra TLS":** SSL está obsoleto; o protocolo em uso é TLS, e "certificado SSL" é nome de mercado (alta).
9. **Linha de comando também é automática:** `certbot` (Let's Encrypt) obtém, instala e renova em um comando (alta).
10. **IP divergente:** a aula 02 resolveu frontpush.com.br para `162.241.61.29`; aqui o IP do servidor no FileZilla é `162.241.61.25`. Pode ser erro de legenda ou IPs diferentes da mesma máquina (a conferir).
11. **"Estático porque não detém funcionalidade a mais":** com GSAP, o portfólio tem JavaScript; continua estático porque o servidor só entrega arquivos ([[wiki/concepts/site-estatico-vs-dinamico]]).

## Entities

- [[wiki/entities/frontpush]], [[wiki/entities/nasser]], [[wiki/entities/creatorpush]]
- [[wiki/entities/hostgator]], [[wiki/entities/hostinger]], [[wiki/entities/cpanel]], [[wiki/entities/filezilla]] (novo)
- [[wiki/entities/gsap]], [[wiki/entities/nubank]], [[wiki/entities/spider-man-projeto-nasser]]
- [[wiki/entities/php]], [[wiki/entities/apache-http-server]], [[wiki/entities/wordpress]], [[wiki/entities/react]]

## Concepts

- [[wiki/concepts/virtual-host]] (novo), [[wiki/concepts/name-server]], [[wiki/concepts/hospedagem-de-sites]]
- [[wiki/concepts/site-estatico-vs-dinamico]], [[wiki/concepts/servidor-web-vs-servidor-de-aplicacao]]
- [[wiki/concepts/ftp]], [[wiki/concepts/http-vs-https]]

## Open Questions

- O formulário da lista de espera do FrontPUSH é processado em PHP (banco, e-mail) ou é um serviço externo?
- Qual o IP certo do servidor: `.25` ou `.29`?

## Raw quotes

> "Para mim, esse portfólio, qual é a funcionalidade que eu preciso que ele tenha? Nenhuma."

> "Tudo são pastinhas, tudo são diretórios, então o seu site é um diretório."

> "Não se engane e tenha em mente essa particularidade."

## Continuação

Fim do "tutorial" da HostGator. Na aula 03, o autor anunciou o mesmo processo com GitHub Pages depois.
