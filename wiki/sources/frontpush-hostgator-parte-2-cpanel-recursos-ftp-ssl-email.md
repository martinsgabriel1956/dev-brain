---
type: source
title: "Hospedagem na HostGator, parte 2: tour pelo cPanel (banco, arquivos, FTP, domínios, e-mail, SSH, SSL) (FrontPUSH)"
aliases: ["FrontPUSH hospedagem aula 05", "Hostgator pt. 2", "Módulo de hospedagem, aula 05", "tour pelo cPanel"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 0
tags: [hospedagem, hospedagem-compartilhada, hostgator, cpanel, phpmyadmin, mysql, ftp, public-html, email, mx, largura-de-banda, ssh, ssl, autossl, wordpress, php, curso, frontend, networking]
skill: tech-mentor-networking
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-hostgator-parte-2-cpanel-recursos-ftp-ssl-email.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-21
---

# Hospedagem na HostGator, parte 2: tour pelo cPanel (banco, arquivos, FTP, domínios, e-mail, SSH, SSL) (FrontPUSH)

## TL;DR

Quinta aula do módulo de hospedagem do [[wiki/entities/frontpush|FrontPUSH]], cerca de 11 minutos, sem slide: tour pelo [[wiki/entities/cpanel|cPanel]] da conta [[wiki/entities/hostgator|HostGator]] do autor. [[wiki/entities/nasser|Násser]] se nomeia ("eu, Násser, prefiro deixar separado") e encena as perguntas ("Ah, Násser..."). Não sobe arquivo nenhum: só mostra onde cada coisa fica; a prática vem nas "próximas aulas".

- **Recapitulação:** e-mail técnico (plano, domínio principal, DNS, usuário e senha); domínio na [[wiki/entities/registro-br|Registro.br]] separado do host, "porque quando eu vou modificar alguma coisa, eu vou modificar direto pelo Registro.br"; os name servers "precisam combinar" com o host ([[wiki/concepts/name-server]]).
- **Acesso:** domínio principal + "barra cPanel", usuário e senha.
- **Banco:** [[wiki/entities/phpmyadmin|phpMyAdmin]] "já vem [...] instalado"; "banco de dados MySQL"; num "servidor cru" seria `sudo apt-get install mysql-server` ([[wiki/concepts/mysql]], [[wiki/concepts/linux]]).
- **Arquivos:** gerenciador de arquivos = "a minha pasta do meu usuário no servidor deles"; arrastar a pasta "que já vai funcionar"; `public_html` "é onde a gente coloca os nossos websites" (80 MB usados).
- **FTP:** "protocolo de transferência de arquivos"; conta FTP ou upload direto pelo painel ([[wiki/concepts/ftp]]).
- **Domínios:** primeiro o pessoal, depois FrontPUSH e [[wiki/entities/creatorpush|CreatorPUSH]] adicionados no painel.
- **E-mail com o próprio domínio:** `contato@frontpush.com.br` em vez de `@gmail.com`, "um e-mail um pouco mais profissional" ([[wiki/entities/gmail]]).
- **Largura de banda:** plano com banda baixa e muito acesso "vai comer a largura de banda"; já aconteceu com ele, "hoje é mais difícil".
- **SSH, bloqueador de IP, SSL:** SSH = "essa pastinha aqui, só que via terminal"; certificado "grátis, [...] com alguns cliques", instalado nos três domínios, "tanto para e-mail, tanto para o protocolo HTTPS" ([[wiki/concepts/ssh]], [[wiki/concepts/http-vs-https]]).
- **PHP e WordPress:** a hospedagem vem "muito preparada para o [[wiki/entities/wordpress|WordPress]]"; para PHP, "eu indico" esse tipo de serviço ([[wiki/entities/php]]).
- **Os principais:** gerenciador de arquivos, banco/phpMyAdmin, domínios e certificado SSL.

## Key Claims

### Recapitulando a parte 1

- O e-mail técnico traz "qual é o plano que você adquiriu, qual é o seu principal domínio, quais são os endereços DNS, qual é o seu usuário e a sua senha" ([[wiki/sources/frontpush-hostgator-parte-1-plano-turbo-name-servers-registro-br]]).
- "Muitos deles oferecem domínios grátis [...] mas eu, Násser, prefiro deixar separado, porque quando eu vou modificar alguma coisa, eu vou modificar direto pelo Registro.br. Ah, troquei, não quero mais a HostGator, venho aqui e altero o DNS para apontar para os servidores da Hostinger."
- "Um precisa combinar com o outro. Não adianta nada eu digitar www.frontpush.com.br e ele não apontar para os servidores do HostGator, que é onde está o meu site."

### Acessando o cPanel

- "Você vai entrar no seu domínio principal, no caso é nusefale.com.br barra cPanel" (domínio pessoal truncado pela legenda; ver Open Questions); redireciona para a página de usuário e senha.
- "Ele detém todas as principais funções que você precisa fazer no seu website."

### Banco de dados

- "Ele já vem com o phpMyAdmin instalado", "um programinha que facilita eu criar banco de dados com uma interface gráfica, sem precisar utilizar terminal". "Já utilizei muito ele."
- Criar o banco: "banco de dados MySQL". "Se você fosse pegar, por exemplo, um servidor cru, você teria que instalar tudo isso na mão": `sudo apt-get install mysql-server` no terminal.

### Arquivos e FTP

- Gerenciador de arquivos: "essa pastinha aqui é a minha pasta do meu usuário no servidor deles", "é aqui que eu vou colocar as minhas páginas web": "clica e arrasta, copia a nossa pastinha da nossa aplicação web para aqui para dentro, que já vai funcionar".
- "O FTP, pessoal, é um protocolo de transferência de arquivos", para passar "a sua aplicação web, que está naquela pastinha que você construiu"; "você está criando uma conta FTP para poder fazer isso, ou você pode puxar daqui diretamente".
- "Tem controle de Git [...] Fuce, descubra."
- Uso do disco: "na public_html, que é onde a gente coloca os nossos websites, 80 MB".

### Domínios

- "Antes só foi o nucf-ali, que foi o meu primeiro. Depois eu registrei o FrontPUSH lá no Registro.br, adicionei ele aqui. Depois [...] o CreatorPUSH, adicionei ele aqui de novo." A demonstração fica para depois.

### Métricas e e-mail

- Na conta Google, o e-mail é "fulano de tal, arroba, gmail.com", e "esse Gmail é o domínio do Google". "Como você comprou o seu próprio domínio, agora você pode ter um e-mail": "contato, arroba, frontpush.com.br", "um e-mail um pouco mais profissional, não é utilizando o Google, não é utilizando o Yahoo". As contas vêm "grátis".
- Métricas: "relatório de erros, largura de banda, relatório de acesso".

### Largura de banda

- "Se você comprar [...] um plano de hospedagem que tem a largura de banda baixa e o seu site tem muito acesso, isso vai comer a largura de banda e meio que ele vai travar o acesso do seu site." "Já chegou de vez que eu acessei tanto o meu site que comeu toda a largura de banda e eu tinha que pagar mais." "Hoje é mais difícil."

### SSH, segurança e SSL

- "O acesso SSH é quando você vai acessar diretamente essa pastinha aqui, só que via terminal. Você faz um acesso remoto utilizando o comando do SSH no Linux."
- "Tem bloqueador de IP e aqui é onde a gente instala o certificado SSL, que é para a gente ter o protocolo HTTPS grátis", "só com alguns cliques".
- Status do certificado: "instalei esse certificado para todos os domínios, tanto o Creator [...] tanto o FrontPUSH quanto o NUCFL", "tanto para e-mail, tanto para o protocolo HTTPS, que quando eu entro aparece o cadeadinho".

### PHP e WordPress

- "Muitas coisas do PHP já vêm pré-instaladas, [...] porque esses servidores [...] vêm muito preparados para o WordPress."
- "Eu sempre trabalho com WordPress, o que isso indica para mim? Serviços como o da HostGator, como o da Hostinger, que já vem com tudo isso preparado", "sem precisar pegar em absolutamente nada de código ou linha de comando". "A tecnologia que eu estou mexendo é o PHP, eu indico."
- "Gerenciar aplicações", "versão do PHP, instalar o WordPress". Os principais: "o gerenciador de arquivos, banco de dados, se você tiver, ou phpMyAdmin, os domínios e o certificado SSL".

## Precisões e ressalvas

1. **FTP simples manda senha e arquivos em texto claro.** Em vez dele: SFTP (sobre SSH) ou FTPS (FTP com TLS), que o cPanel costuma oferecer; ou o gerenciador de arquivos, que vai por HTTPS ([[wiki/concepts/ftp]]) (alta).
2. **`public_html` é a raiz do domínio principal.** Domínios adicionados ganham pasta própria (dentro dela ou ao lado, conforme a versão do cPanel). "Arrastar a pastinha" só funciona se o `index.html`/`index.php` ficar na raiz certa; uma subpasta vira `dominio.com.br/pasta` `[external]` (https://docs.cpanel.net; alta).
3. **"Largura de banda" no painel é transferência mensal**, não velocidade: a cota de dados enviados no mês. Estourar a cota suspende ou cobra; planos "ilimitados" têm política de uso justo (alta).
4. **SSH é um shell remoto na conta**, não só "a pastinha"; dá para rodar comandos, Git, Composer. Também existe no Windows (OpenSSH). Na hospedagem compartilhada o shell é restrito à conta ([[wiki/concepts/ssh]]) (alta).
5. **E-mail com o próprio domínio depende do DNS.** Funciona porque o domínio foi delegado à HostGator, cujo DNS já publica o registro MX para o servidor de e-mail dela. Para não cair em spam, SPF, DKIM e DMARC; o cPanel configura parte disso. Alternativa comum: Google Workspace/Microsoft 365 com MX apontado para eles ([[wiki/concepts/dns]]) (alta).
6. **Certificado "para e-mail":** o AutoSSL do cPanel inclui subdomínios como `mail.`, `webmail.` e `cpanel.` no mesmo certificado (alta).
7. **phpMyAdmin não cria o banco no cPanel:** banco e usuário nascem em "Bancos de dados MySQL"; o phpMyAdmin administra tabelas e dados depois. O "MySQL" pode ser MariaDB, conforme o servidor ([[wiki/entities/phpmyadmin]]) (média-alta).
8. **`apt-get install mysql-server`** vale para Ubuntu; no Debian o pacote padrão é MariaDB (`default-mysql-server`). Instalar é o começo: no servidor cru ainda faltam usuário, firewall, backup ([[wiki/concepts/linux]]) (alta).
9. **"80 MB [...] já está cheio"** é força de expressão: 80 MB ocupados; planos compartilhados têm gigabytes de disco (média).
10. **"Eu sempre trabalho com WordPress"** soa como "se você trabalha com WordPress": é a recomendação da aula para quem usa PHP/WordPress. Para Node, Python ou SPA com build, essa hospedagem pesa contra (ver [[wiki/sources/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react]]).
11. **Credenciais no vídeo:** a aula mostra o caminho de login, não a senha; é bom ativar 2FA no cPanel (alta).

## Entities

- [[wiki/entities/frontpush]], [[wiki/entities/nasser]], [[wiki/entities/creatorpush]]
- [[wiki/entities/hostgator]], [[wiki/entities/hostinger]], [[wiki/entities/registro-br]], [[wiki/entities/cpanel]]
- [[wiki/entities/phpmyadmin]] (novo), [[wiki/entities/wordpress]] (novo), [[wiki/entities/php]], [[wiki/entities/gmail]]

## Concepts

- [[wiki/concepts/ftp]] (novo), [[wiki/concepts/ssh]], [[wiki/concepts/http-vs-https]], [[wiki/concepts/dns]], [[wiki/concepts/name-server]]
- [[wiki/concepts/mysql]], [[wiki/concepts/linux]], [[wiki/concepts/hospedagem-de-sites]]

## Open Questions

- O domínio pessoal do autor aparece como "nusefale", "nucf-ali" e "NUCFL" na legenda (aula 04: "nucfl.com.br"). Qual é o certo?
- Os domínios adicionais ficam em subpastas de `public_html`?

## Raw quotes

> "Um precisa combinar com o outro."

> "Se você fosse pegar, por exemplo, um servidor cru, você teria que instalar tudo isso na mão."

> "Com poucos cliques você consegue fazer assim muita coisa sem precisar pegar em absolutamente nada de código ou linha de comando."

## Continuação

As próximas aulas prometem adicionar um domínio, instalar o certificado SSL e subir o CreatorPUSH e o FrontPUSH. Cumprido em [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]].
