---
type: source
title: "Website estático vs. aplicação web: PHP com Apache no XAMPP, React e MySQL (FrontPUSH)"
aliases: ["FrontPUSH hospedagem aula 03", "Website vs. WebApp", "Módulo de hospedagem, aula 03", "Aplicações web x websites estáticos"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 0
tags: [site-estatico, aplicacao-web, php, apache, xampp, react, build, mysql, local-storage, hospedagem, hospedagem-compartilhada, curso, frontend, networking]
skill: tech-mentor-networking
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-21
---

# Website estático vs. aplicação web: PHP com Apache no XAMPP, React e MySQL (FrontPUSH)

## TL;DR

Terceira aula do módulo de hospedagem do [[wiki/entities/frontpush|FrontPUSH]], cerca de 8 minutos, com um slide e demonstração no [[wiki/entities/xampp|XAMPP]]. [[wiki/entities/nasser|Násser]] encena a pergunta "Násser, por que você não utilizou nenhuma biblioteca ou framework no FrontPUSH? [...] ReactJS" e diz que a aula explica. É a "diferença" prometida na aula 01 ([[wiki/sources/frontpush-introducao-hospedagem-de-websites-url-localhost-porta]]).

- **Website estático:** "construído com HTML, CSS e JavaScript", "denominado estático porque ele não consegue construir funcionalidades complexas"; a to-do list some no F5 porque estava num array; local storage some ao "limpar". Não precisa "instalar nem configurar nada" porque é "o que o browser entende"; basta copiar para uma pasta do servidor ([[wiki/concepts/site-estatico-vs-dinamico]]).
- **Aplicação web:** "detêm de um back-end, [...] front-end, [...] uma API, [...] banco de dados"; precisa "instalar" e "configurar alguma coisa a mais".
- **PHP precisa do Apache:** `http://localhost/frontpush` não abre ("o browser não entende PHP"); com o Apache ligado no XAMPP (portas 80 e 443), o F5 mostra o site. O FrontPUSH "é uma aplicação que está desenvolvida em PHP" ([[wiki/entities/php]], [[wiki/entities/apache-http-server]]).
- **React:** `localhost:3000` "não vai achar" sem "um build, que é a construção do ambiente"; e "eu preciso também de um banco de dados, de um MySQL" ([[wiki/entities/react]], [[wiki/concepts/mysql]]).
- **Terminal:** "na maioria das vezes, você vai precisar de um acesso ao terminal"; PHP é "um pouco mais simples", "só precisa do servidor Apache".
- **Hospedagem compartilhada:** [[wiki/entities/hostgator|HostGator]] e [[wiki/entities/hostinger|Hostinger]] "já vem com [o Apache] instalado, configurado na porta 80".
- **Próxima aula:** subir o [[wiki/entities/creatorpush|CreatorPUSH]] ("um website estático") e o FrontPUSH em PHP na HostGator; depois o mesmo com GitHub Pages.

## Slide

"Aplicações web x Websites Estáticos"
- **Website estático:** "Você não precisa instalar nem configurar nada para que o seu site funcione. Um website estático é um HTML, CSS e JS puros."
- **Aplicações web:** "Você precisa configurar o ambiente de desenvolvimento, instalar dependências corretas, subir o ambiente para que a sua aplicação web possa funcionar."
- **Exemplos:** "PHP: Precisa do Apache"; "React.js: precisa da configuração do ambiente com as dependências"; "MySQL: precisa instalar e criar sua base de dados"; "Acesso ao terminal" (com estrela).

## Key Claims

### Por que esta aula

- Conhecer "as funcionalidades daquilo que você está querendo implementar" serve "para você definir qual é o melhor jeito de você hospedar".
- A pergunta recorrente: "por que você não utilizou nenhuma biblioteca ou framework no FrontPUSH? Por que você não utilizou, sei lá, ReactJS quando você upou o seu site?" A resposta fica implícita: PHP roda pronto na hospedagem compartilhada (ver Precisões).

### Website estático

- "É basicamente um website que é construído com HTML, CSS e JavaScript." "Denominado estático porque ele não consegue construir funcionalidades complexas."
- To-do list: "se você apertar F5, toda a informação é apagada porque você construiu aquilo ali dentro de um array. Você não armazenou [...] dentro de um banco de dados." "Local storage [...] mas se dar um limpar, você perdeu todas as informações."
- "Nem navegação entre páginas dinâmicas e complexas, como, por exemplo, utilizando um ReactJS ou outra linguagem" (ver Precisões).
- "Porque é o que o browser entende. A única coisa que ele entende é HTML, [...] CSS e JavaScript", "ele já vai rodar diretamente". "Basta você copiar e colar um website estático em uma determinada pasta e acessar essa pasta no seu servidor."

### Aplicação web

- "Detêm de um back-end, detêm de um front-end, detêm de uma API, detêm de funcionalidades que exigem um banco de dados e é tudo mais complexo." É preciso "instalar" e "configurar alguma coisa a mais".

### PHP e Apache no XAMPP

- "O PHP precisa do Apache para rodar." `localhost/frontpush` "não achou"; com `http://localhost/frontpush`, "eu estou acessando a minha própria máquina no localhost, no protocolo HTTP e [...] indo na pasta raiz do FrontPUSH", e o browser diz "que não é possível acessar esse site".
- Motivo dado: "o FrontPUSH é uma aplicação que está desenvolvida em PHP, ele não é um website estático [...] o browser não entende PHP, ele precisa de um servidor Apache".
- O XAMPP tem "um serviço Apache, [...] MySQL, do FileZilla, do Mercury, do Tomcat, mas para poder rodar o PHP, eu só preciso do Apache". Start: "o servidor do Apache na porta 80 e na porta 443"; F5: "agora sim a minha aplicação vai rodar" ([[wiki/concepts/porta-de-rede]], [[wiki/concepts/localhost]]).
- "Isso acontece da mesmíssima forma quando você faz a hospedagem de uma aplicação web em um servidor [...] ele precisa ter o Apache já instalado."

### ReactJS e MySQL

- Blog do módulo de React em `localhost:3000`: "vai ficar rodando e não vai achar", "porque ele é uma aplicação web que necessita de configurações, necessita de um build, que é a construção do ambiente para poder essa aplicação rodar na porta 3000".
- "O ReactJS precisa da configuração do ambiente, eu preciso também de um banco de dados, de um MySQL": instalar, configurar, criar base, tabelas e usuário. "Isso eu já estou falando de back-end."
- "Quando ele é construído de maneira inteligente, se você apertar um build [...] ele já constrói tudo para você automático, mas [...] no background do negócio, você sempre vai precisar configurar alguma coisa." "Na maioria das vezes, você vai precisar de um acesso ao terminal" ([[wiki/concepts/shell-terminal]]).

### Na hospedagem

- "Muitos servidores, como, por exemplo, o HostGator ou o Hostinger já vem com a pasta instalada [...] configurado na porta 80" ("a pasta" na legenda; pelo contexto, o Apache).

## Precisões e ressalvas

1. **Estático é sobre o servidor, não sobre o que o site consegue fazer.** O servidor entrega arquivos prontos; no navegador, o JavaScript pode chamar APIs, autenticar, gravar em banco remoto (Jamstack). "Não consegue construir funcionalidades complexas" confunde os eixos que [[wiki/concepts/site-estatico-vs-dinamico]] separa `[skill: tech-mentor-frontend]` (alta).
2. **Um app React é, depois do build, um site estático.** `npm run build` gera HTML, CSS e JS que qualquer servidor de arquivos ou GitHub Pages/Netlify serve; a navegação "dinâmica" é [[wiki/concepts/client-side-routing]] dentro de uma [[wiki/concepts/single-page-application]], só pede um redirect para `index.html`. A frase "nem navegação [...] utilizando um ReactJS [...] com um website estático" está ao contrário `[external]` (https://create-react-app.dev/docs/deployment/; alta). O `localhost:3000` é o servidor de desenvolvimento (`npm start`), não exigência de produção.
3. **React não precisa de MySQL.** React roda no navegador; quem fala com o banco é o back-end (API). Juntar os dois no mesmo exemplo é o que o autor reconhece com "isso eu já estou falando de back-end" ([[wiki/entities/react]]).
4. **Apache sozinho não roda PHP.** Quem executa é o interpretador PHP, ligado ao Apache por `mod_php` ou via PHP-FPM (com Apache ou Nginx); para desenvolvimento, `php -S localhost:8000` basta `[external]` (https://www.php.net/manual/en/features.commandline.webserver.php; alta). O XAMPP já traz o PHP junto do Apache.
5. **A demo mostra falta de servidor, não falta de PHP.** Com o Apache desligado nada escuta na porta 80; um `index.html` puro em `http://localhost/frontpush` também não abriria. "Basta [...] copiar e colar [...] na pasta [...] do seu servidor" também pressupõe um servidor web ([[wiki/concepts/servidor-web-vs-servidor-de-aplicacao]]).
6. **"localhost barra frontpush" sem `http://`** em geral o navegador completa sozinho; o "não achou" da primeira tentativa provavelmente virou busca na barra de endereço (inferência, média).
7. **local storage persiste ao F5** e só some quando o usuário limpa os dados do site; é por origem e por navegador, não é banco compartilhado (alta).
8. **Hostinger usa LiteSpeed, não Apache**, na hospedagem compartilhada (compatível com `.htaccess`); a HostGator usa Apache `[external, não verificado]` (média). O ponto da aula vale: PHP já vem pronto.
9. **"Por que não React no FrontPUSH" não é respondido de frente.** O que a aula sustenta: em hospedagem compartilhada, PHP roda sem terminal nem build. React não seria impedimento: o build estático subiria na mesma pasta.
10. **Acesso ao terminal** (estrela no slide) = SSH; hospedagem compartilhada costuma limitar ou não dar; VPS e cloud dão ([[wiki/concepts/ssh]]).

## Entities

- [[wiki/entities/frontpush]], [[wiki/entities/nasser]], [[wiki/entities/creatorpush]]
- [[wiki/entities/xampp]] (novo), [[wiki/entities/php]] (novo), [[wiki/entities/filezilla]] (no painel), [[wiki/entities/apache-http-server]], [[wiki/entities/react]]
- [[wiki/entities/hostgator]], [[wiki/entities/hostinger]], [[wiki/entities/github]] (GitHub Pages, próxima aula)

## Concepts

- [[wiki/concepts/site-estatico-vs-dinamico]], [[wiki/concepts/servidor-web-vs-servidor-de-aplicacao]], [[wiki/concepts/hospedagem-de-sites]]
- [[wiki/concepts/single-page-application]], [[wiki/concepts/client-side-routing]], [[wiki/concepts/mysql]]
- [[wiki/concepts/localhost]], [[wiki/concepts/porta-de-rede]], [[wiki/concepts/shell-terminal]], [[wiki/concepts/ssh]]

## Open Questions

- O FrontPUSH usa PHP para quê, além de servir as páginas (includes, formulário, área de membros)?
- Na próxima aula, o upload é por FTP no cPanel ou pelo gerenciador de arquivos?

## Raw quotes

> "Porque é o que o browser entende. A única coisa que ele entende é HTML, [...] CSS e JavaScript."

> "O browser não entende PHP, ele precisa de um servidor Apache para poder rodar."

> "No background do negócio, você sempre vai precisar configurar alguma coisa."

## Continuação

Próxima aula: o CreatorPUSH (estático) e o FrontPUSH (PHP) na HostGator, com domínios; depois, GitHub Pages. A aula 04 ([[wiki/sources/frontpush-hostgator-parte-1-plano-turbo-name-servers-registro-br]]) cobre plano, e-mail técnico e domínios; os arquivos ficam para a parte 2.
