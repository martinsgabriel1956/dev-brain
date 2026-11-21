---
type: source
title: "Hospedagem na HostGator, parte 1: plano Turbo, e-mail técnico, name servers e Registro.br (FrontPUSH)"
aliases: ["FrontPUSH hospedagem aula 04", "Hostgator pt. 1", "Módulo de hospedagem, aula 04"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 0
tags: [hospedagem, hospedagem-compartilhada, hostgator, hostinger, cpanel, name-server, dns, dominio, registro-br, delegacao-dns, propagacao-dns, ssl, curso, frontend, networking]
skill: tech-mentor-networking
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-hostgator-parte-1-plano-turbo-name-servers-registro-br.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-21
---

# Hospedagem na HostGator, parte 1: plano Turbo, e-mail técnico, name servers e Registro.br (FrontPUSH)

## TL;DR

Quarta aula do módulo de hospedagem do [[wiki/entities/frontpush|FrontPUSH]], cerca de 8,5 minutos, sem slide: site da [[wiki/entities/hostgator|HostGator]], o e-mail técnico da contratação (com dados tampados) e o painel da [[wiki/entities/registro-br|Registro.br]]. [[wiki/entities/nasser|Násser]] não se apresenta; autoria pela sequência e pelos domínios "no meu CPF". Primeira aula prática: "como eu fiz para poder hospedar todos os meus sites utilizando a HostGator nesse modelo mais tradicional", que "não quer dizer que ele é mais difícil, só é diferente".

- **Escolha:** HostGator, [[wiki/entities/hostinger|Hostinger]], Locaweb, [[wiki/entities/godaddy|GoDaddy]]; "eu sempre procuro ir naquelas maiores, porque elas vão oferecer mais serviços por um preço menor".
- **Plano:** P, M e Turbo; assinou o Turbo porque "era o único que tinha SSD na época", tem "certificado SSL grátis" e "mais poder de processamento". Acha que a Hostinger "tem sido um plano melhor" (Git, SSH, CDN), mas o plano dele "já está pago".
- **E-mail técnico:** traz "o DNS do seu plano de hospedagem" (`nspro34.hostgator.com.br` e o 35, "o master e o slave"), o IP do servidor e usuário e senha do [[wiki/entities/cpanel|cPanel]], "o painel geral" para domínio, certificado, banco e WordPress.
- **Registro.br:** prefere "sempre pagar o meu domínio na Registro.br"; preços na tela (R$ 40 por um ano, R$ 76 por dois); titularidade por CPF ou CNPJ; três domínios no CPF dele (CreatorPUSH, FrontPUSH e o pessoal).
- **Apontar:** na Registro.br, troca os servidores DNS do domínio pelos da HostGator; trocou de host, troca de novo. "Demora algumas horas" ([[wiki/concepts/name-server]], [[wiki/concepts/dns]]).
- **Domínio grátis do host:** "no background, ele já está fazendo isso com a Registro.br", como vantagem comercial.
- **Parte 2:** acessar o cPanel e "colocar os seus arquivos lá".

## Key Claims

### Abertura

- "Agora nós vamos de fato partir para a prática", depois das "diferenças de como hospedar aplicações web para websites estáticos" ([[wiki/sources/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react]]).
- "Você precisa adequar a tecnologia que você está escolhendo com a hospedagem, de forma que ela sempre seja mais fácil para poder você trabalhar" ([[wiki/concepts/hospedagem-de-sites]]).

### Escolhendo o serviço e o plano

- "Seja a HostGator, seja a Hostinger, seja a Locaweb, todos esses serviços são de boas empresas, mas eu sempre procuro ir naquelas maiores, porque elas vão oferecer mais serviços por um preço menor."
- "Tem a hospedagem P, o M e o Turbo. Eu assinei o Turbo [...] Porque era o único que tinha SSD na época, hoje até o plano P tem SSD." Também "certificado SSL grátis, [...] muito fácil de instalar", "para você ter o protocolo HTTPS no seu browser para poder garantir confiabilidade", e "mais poder de processamento" ([[wiki/concepts/http-vs-https]]).
- Hostinger: "serviços muito parecidos", "mas tem acesso Git, tem acesso a SSH, tem CDN, então eu acredito que a Hostinger tem sido um plano melhor que da HostGator"; "porém, contudo, entretanto, o meu plano aqui já está pago" ([[wiki/concepts/ssh]], [[wiki/concepts/cdn]], [[wiki/concepts/git]]).

### O e-mail técnico e o DNS da HostGator

- "Eles sempre enviam esse e-mail técnico", com o plano adquirido e "guarde este e-mail para futuras referências". Primeiro ponto: "eles me passaram o DNS deles".
- Ligação com a aula 02: "para poder fazer essa conversão de um nome para um IP, eu preciso de um servidor DNS e o servidor DNS é meio que um IP, onde você precisa apontar o servidor DNS para esse IP" (ver Precisões).
- "frontpush.com.br, você precisa apontar para os servidores de onde você contratou, ou seja, você precisa apontar o seu registro de domínio, que quem faz é a Registro.br, para o DNS da HostGator." Trocou para a Hostinger: "aponta para esse outro servidor aqui, então é esse DNS que resolve".
- "nspro34.hostgator.com.br, tem o master e o slave, são dois servidores DNS."
- cPanel: "meio que o painel geral para você adicionar um novo domínio, instalar o certificado, instalar um banco de dados, ou então instalar o WordPress" ([[wiki/entities/wordpress]]). O e-mail traz "o IP do servidor, de fato, e o usuário e a senha", "assim que eu contrato o serviço".

### O domínio na Registro.br

- "A maioria das plataformas hoje em dia já oferecem o domínio grátis. Eu prefiro sempre pagar o meu domínio na Registro.br", "o órgão que registra todos os domínios do Brasil".
- www.creatorpush2.com.br "está disponível": "R$ 40 por um ano, R$ 76 por dois anos, R$ 185 por dois anos" (o terceiro período provavelmente é maior; ver Precisões), pago e registrado "vinculando ao seu CPF ou o CNPJ".
- Titularidade: "tenho o CreatorPUSH, tenho o FrontPUSH e tenho o meu nucfl.com.br" (nome do domínio pessoal truncado pela legenda; na aula 02 aparecia como "o Násser"), "vinculados à minha conta no meu CPF" ([[wiki/entities/creatorpush]]).

### Apontando o domínio

- "Eu tenho que indicar, na Registro.br, qual é o DNS do servidor que eu contratei." Em domínios → DNS, "eu peguei esses carinhas aqui, nspro34.hostgator.com.br e o 35 e coloquei como servidores DNS de onde está registrado o meu domínio."
- Domínio grátis do host: "na própria plataforma deles é feito isso, que a Registro.br faz. Na realidade, no background, ele já está fazendo isso com a Registro.br, [...] para oferecer mais uma vantagem".
- "Sempre você vai precisar apontar [...] o domínio que eu comprei aqui [...] para o servidor onde está hospedado o meu site." "Mudei para Hostinger, [...] alterar servidores DNS, [...] copiar os dois DNS da Hostinger."
- "Demora algumas horas para ele fazer essa modificação, é rápido, ele sempre te manda um e-mail dizendo que está tudo ok." Depois, cPanel e arquivos, "em uma parte 2".

## Precisões e ressalvas

1. **Name server é um nome, não "meio que um IP".** O que se coloca na Registro.br são *hostnames* (`nspro34.hostgator.com.br`), gravados como registros NS na zona `.br`: é a **delegação**. O IP do site fica num registro A dentro da zona, nos servidores da HostGator ([[wiki/concepts/name-server]]) `[skill: tech-mentor-networking]` (alta).
2. **Dois caminhos para apontar.** (a) Delegar: trocar os name servers para os do host (o que a aula faz); a zona inteira passa a ser editada no cPanel. (b) Manter o DNS da Registro.br e criar só um registro A para o IP do servidor. A aula só mostra (a), e o "sempre você vai precisar apontar [...] os DNS" vale para ela (alta).
3. **"Master e slave"** é o par primário/secundário de servidores autoritativos (ns34 e ns35), por redundância. Hoje se diz primário/secundário (alta).
4. **"Algumas horas" é cache, não processamento.** A troca na Registro.br é rápida; o que demora é o TTL dos registros NS em cache nos resolvers, que costuma ser de horas e pode chegar a um ou dois dias ([[wiki/concepts/ttl]]) (alta). A Registro.br também testa se os novos servidores respondem pela zona antes de aceitar a delegação `[external, a conferir]` (média).
5. **"No background é a Registro.br"** só vale para `.br`, via provedor credenciado. Para `.com`, o host usa um registrador próprio ou parceiro. Em qualquer caso, vale conferir em nome de quem o domínio fica (titular) e quanto custa a renovação depois do ano grátis (alta). A preferência do autor por registrar direto evita esse risco.
6. **Preços:** R$ 40/ano é o valor que a Registro.br pratica para `.com.br` `[external]` (https://registro.br; média, preços mudam). O "R$ 185 por dois anos" deve ser outro período (cinco anos, pela proporção); a legenda ou a fala erraram.
7. **SSL grátis não é mais diferencial de plano:** AutoSSL do cPanel e Let's Encrypt deram certificado gratuito a praticamente qualquer hospedagem (alta). Os nomes e recursos dos planos da HostGator também mudaram desde a gravação (média).
8. **E-mail com usuário, senha e IP** é material sensível; o autor fez bem em tampar. Além disso: trocar a senha inicial e ativar 2FA no painel (alta).
9. **"Maiores oferecem mais por menos"** é opinião do autor; HostGator e outras marcas grandes pertencem a grupos (ex.: Newfold Digital) e a comparação depende do plano `[external, não verificado]` (baixa).

## Entities

- [[wiki/entities/frontpush]], [[wiki/entities/nasser]], [[wiki/entities/creatorpush]]
- [[wiki/entities/hostgator]], [[wiki/entities/hostinger]], [[wiki/entities/godaddy]], Locaweb (sem página)
- [[wiki/entities/registro-br]], [[wiki/entities/cpanel]] (novo)

## Concepts

- [[wiki/concepts/name-server]] (novo), [[wiki/concepts/dns]], [[wiki/concepts/dominio]], [[wiki/concepts/ttl]]
- [[wiki/concepts/hospedagem-de-sites]], [[wiki/concepts/http-vs-https]], [[wiki/concepts/ssh]], [[wiki/concepts/cdn]], [[wiki/concepts/git]]

## Open Questions

- Qual é o domínio pessoal do autor ("nucfl.com.br" na legenda)?
- Na parte 2, como os três domínios convivem no mesmo plano: domínio principal + domínios adicionais (*addon domains*) no cPanel?

## Raw quotes

> "Não quer dizer que ele é mais difícil, só é diferente."

> "Eu prefiro sempre pagar o meu domínio na Registro.br."

> "Sempre você vai precisar apontar [...] o domínio que eu comprei [...] para o servidor onde está hospedado o meu site."

## Continuação

A parte 2 promete acessar o cPanel e "colocar os seus arquivos lá". Em [[wiki/sources/frontpush-hostgator-parte-2-cpanel-recursos-ftp-ssl-email]] vem o tour pelo cPanel; o upload dos arquivos fica para as aulas seguintes.
