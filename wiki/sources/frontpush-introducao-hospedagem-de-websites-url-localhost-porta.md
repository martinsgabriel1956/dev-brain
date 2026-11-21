---
type: source
title: "Introdução ao módulo de hospedagem de websites: URL, localhost e porta (FrontPUSH)"
aliases: ["FrontPUSH hospedagem aula 01", "Introdução hospedagem de websites", "Módulo de hospedagem, aula 01", "módulo bônus de hospedagem"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 0
tags: [hospedagem, deploy, url, localhost, loopback, porta, http, dominio, dns, ssl, github-pages, netlify, vercel, heroku, cloud, curso, frontend, networking]
skill: tech-mentor-networking
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-introducao-hospedagem-de-websites-url-localhost-porta.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-21
---

# Introdução ao módulo de hospedagem de websites: URL, localhost e porta (FrontPUSH)

## TL;DR

Abertura do "módulo bônus" de hospedagem do [[wiki/entities/frontpush|FrontPUSH]], cerca de 9 minutos, com slide e um esquema de URL. [[wiki/entities/nasser|Násser]] não diz o nome; a autoria vem da sequência e de "eu tenho o FrontPUSH, o CreatorPUSH e o meu portfólio tudo no mesmo servidor". Nasceu porque "muita gente sempre me pergunta de como eu hospedo os meus websites".

- **Grade prometida:** método tradicional (contratar [[wiki/entities/hostgator|HostGator]]/[[wiki/entities/hostinger|Hostinger]], domínio, vincular, certificado SSL), clouds gratuitas e pagas (GitHub Pages, [[wiki/entities/netlify|Netlify]], [[wiki/entities/vercel|Vercel]]) e as grandes (Amazon, Microsoft Azure, Google Cloud); rede privada × pública; [[wiki/concepts/dominio|domínio]] e [[wiki/concepts/dns|DNS]]; vários sites no mesmo servidor; [[wiki/concepts/http-vs-https|HTTPS]].
- **O que é hospedagem:** "um serviço online que permite a publicação de um site ou aplicação web na internet", e "tem diferença": a aplicação web "necessita de mais configurações" ([[wiki/concepts/hospedagem-de-sites]], [[wiki/concepts/site-estatico-vs-dinamico]]).
- **A pergunta-gancho:** por que `127.0.0.1:5500/index.html` não abre "de outro celular, por mais que esteja na rede da minha própria casa?" ([[wiki/concepts/localhost]]).
- **Anatomia da URL** (esquema na tela): protocolo, host, porta, arquivo ou diretório ([[wiki/concepts/url]], [[wiki/concepts/porta-de-rede]]).
- **Os principais sites** (slide): GitHub, Netlify, Heroku = "Gratuitos*"; Amazon, Google, Microsoft Azure = "Clouds"; Hostinger, Hostgator (com estrela), "Outros..." = "Pagos". Na fala entram ainda Vercel e Locaweb.
- **Deploy pelo Git:** no Netlify dá para "buildar a sua aplicação sem precisar [...] entrar no servidor [...] por meio de um FTP"; o módulo fará isso no Netlify e no GitHub Pages.

## Key Claims

### Por que um módulo bônus

- "Esse módulo aqui [...] é meio que um módulo bônus", reunindo "as principais informações, que eu acredito que é muito interessante todo o desenvolvedor web front-end também saber".
- Método tradicional: "a gente contrata um serviço como a HostGator, como a Hostinger [...] sobe as informações, contrata o domínio, vincula, instala certificado de SSL e tudo mais", mostrando "na prática como eu fiz com os meus websites".
- Clouds "tanto gratuitas como as pagas": "o próprio GitHub Pages, maneira bem simples", "o próprio Netlify ou a Vercel também são muito bons"; e "plataformas maiores, como a Amazon, Microsoft Azure ou o Google Cloud", com "as diferenças também".
- "Um pouco mais introdutório": primeiro "o que é hospedagem e por que é necessário a gente ter uma hospedagem".

### A pergunta da rede

- "Por que você não consegue upar [...] para a internet, um site que está direto no seu computador, sendo que está rodando no seu computador, por que ninguém consegue acessar?" Resposta prometida: "conceitos de rede privada e rede pública", sem "descer muito".
- Também prometidos: "O que é domínio?", DNS, "como é que a gente registra um domínio", "como colocar vários sites no mesmo servidor" (FrontPUSH, CreatorPUSH e portfólio, "três domínios diferentes") e "como instalar certificados SSL, que é para poder a gente colocar o protocolo HTTPS".

### O que é hospedagem

- Slide: "É um serviço online que permite a publicação de um site ou aplicação na internet." Na fala: "olha que tem diferença, viu? O website você upa ele e ele vai funcionar de uma determinada forma. A aplicação web necessita de mais configurações [...] mais para frente."
- Exemplo: a "animação para a live do FrontPUSH" roda em `127.0.0.1:5500/index.html`. "Por que ela não vai funcionar se eu digitar esse endereço em outro celular, por mais que esteja na rede da minha própria casa?" A aula não responde; só desmonta a URL.

### As partes da URL

Esquema na tela: `http://127.0.0.1:5500/index.html`, com "protocolo", "host", "porta" e "arquivo ou diretório".

- **Protocolo:** "o HTTP se diz respeito ao protocolo [...] Hypertext Transfer Protocol, ou seja, é um protocolo de transferência de hipertexto".
- **Host:** "O 127.0.0.1 está apontando para o host, ou seja, para a sua própria máquina", "a mesma coisa de você digitar localhost".
- **Porta:** "o número que vem em seguida é a porta, 5500". Sem número, "é porque ele está na porta 80, a porta 80 é a porta padrão, e quando ela é a padrão, ela meio que não existe". Fora da 80, "precisa especificar".
- **Arquivo ou diretório:** a barra "está na raiz do meu projeto [...] isso aqui é um diretório", e dele vem o `index.html`, "sempre [...] o arquivo padrão [...] em que não precisa dele ser escrito. Quando eu adiciono barra, automaticamente ele já vai puxar o index.html e o próprio browser faz isso" (ver Precisões).
- "Nós vamos voltar [...] nessa URL, e aprofundar [...] nas próximas aulas."

### Os principais sites

- "Eu tenho o GitHub, o Netlify e a Heroku. Eles têm planos gratuitos [...] e a gente também vai estar utilizando eles."
- Netlify, em pricing: "o plano starter, que é um plano básico para projetos pessoais"; "você pode buildar a sua aplicação sem precisar [...] entrar no servidor, propriamente dito, por meio de um FTP e puxar os seus arquivos. Você consegue colocar os arquivos direto pelo Git." O processo será feito "tanto no Netlify, como no GitHub Pages".
- Heroku: "da mesmíssima forma tem aqui um plano gratuito, Free and Hobby, ou seja, são aplicativos não comerciais, são projetos pessoais".
- "O próprio GitHub Pages também tem essa possibilidade e também tem a Vercel [...] Então são todas clouds, porém, eles têm planos gratuitos e planos pagos."
- Amazon, Google, Microsoft Azure: "empresas gigantescas [...] muito parecidos. Uma vez que você aprende um, você só precisa mexer um pouquinho na plataforma para poder aprender o outro."
- Tradicionais: "a Hostinger, a HostGator ou a Locaweb"; virão "os tipos de hospedagem, quais são as vantagens, quando eu indico um, quando eu indico o outro".

## Precisões e ressalvas

1. **Porta 80 é o padrão do HTTP; HTTPS usa 443** `[external]` (RFC 9110, https://www.rfc-editor.org/rfc/rfc9110#section-4.2; confiança alta). Os sites que se abrem hoje sem porta visível estão quase todos na 443, e o próprio módulo promete instalar SSL. Mesma ressalva já registrada na NLW (ver [[wiki/concepts/porta-de-rede]]).
2. **Quem serve o `index.html` é o servidor, não o browser.** O browser pede `/`; o servidor (Live Server, Apache com `DirectoryIndex`, Nginx com `index`) responde com o documento padrão do diretório `[external]` (https://httpd.apache.org/docs/2.4/mod/mod_dir.html; alta). A wiki já corrigiu a mesma frase em [[wiki/concepts/servidor-web-vs-servidor-de-aplicacao]].
3. **A resposta à pergunta do celular** (a aula deixa para depois) `[skill: tech-mentor-networking]`: `127.0.0.1` é o *loopback*; digitado no celular, aponta para o próprio celular. Na mesma rede, o caminho seria o IP privado do computador (ex.: `192.168.x.x:5500`), desde que o servidor escute nessa interface e o firewall deixe passar. Para a internet, o IP privado fica atrás do NAT do roteador e o computador precisaria ficar ligado; a hospedagem resolve as duas coisas. Ver [[wiki/concepts/localhost]] e [[wiki/concepts/endereco-ip]].
4. **O plano gratuito da Heroku acabou em 28/11/2022** `[external]` (https://blog.heroku.com/next-chapter; alta). O "Free and Hobby" da aula é anterior; hoje o mais barato é pago (Eco/Basic). O asterisco de "Gratuitos*" no slide envelheceu. Ver [[wiki/entities/heroku]].
5. **"Starter" do Netlify:** o plano gratuito trocou de nome e de modelo de cobrança desde a gravação `[external]` (https://www.netlify.com/pricing/; média, nomes mudam).
6. **Site × aplicação web, na prática:** GitHub Pages só serve arquivos estáticos; Netlify e Vercel servem estático e funções serverless; Heroku roda processos (back-end). É a "diferença" que a aula promete explicar ([[wiki/concepts/site-estatico-vs-dinamico]], [[wiki/concepts/hospedagem-de-sites]]).
7. **"Vários sites no mesmo servidor"** costuma ser *virtual host* ([[wiki/concepts/virtual-host]]): o servidor escolhe o site pelo cabeçalho `Host` (e, com HTTPS, pelo SNI do TLS) `[skill: tech-mentor-networking]`. A aula só anuncia.
8. **FTP sem criptografia** ([[wiki/concepts/ftp]]): o FTP simples manda senha em texto claro; quando o upload manual é preciso, SFTP ou FTPS `[external]` (alta). O deploy por Git do Netlify evita o problema.
9. **"Muito parecidos"** vale para os conceitos (VM, storage, DNS gerenciado, CDN); nomes, IAM e preços diferem. Ver [[wiki/concepts/vendor-lock-in-cloud]].
10. A estrela ao lado de "Hostgator" no slide não é explicada; talvez marque o provedor que o autor usa (inferência, baixa).

## Entities

- [[wiki/entities/frontpush]], [[wiki/entities/nasser]], [[wiki/entities/creatorpush]]
- [[wiki/entities/github]] (GitHub Pages), [[wiki/entities/netlify]], [[wiki/entities/vercel]], [[wiki/entities/heroku]]
- [[wiki/entities/amazon-web-services]], [[wiki/entities/google-cloud-platform]], [[wiki/entities/microsoft]] (Azure)
- [[wiki/entities/hostinger]], [[wiki/entities/hostgator]]; Locaweb (sem página)

## Concepts

- [[wiki/concepts/hospedagem-de-sites]], [[wiki/concepts/localhost]] (novos)
- [[wiki/concepts/url]], [[wiki/concepts/porta-de-rede]], [[wiki/concepts/endereco-ip]], [[wiki/concepts/http-vs-https]]
- [[wiki/concepts/dominio]], [[wiki/concepts/dns]]
- [[wiki/concepts/servidor-web-vs-servidor-de-aplicacao]], [[wiki/concepts/site-estatico-vs-dinamico]]

## Open Questions

- Como o autor separa os três domínios no mesmo servidor: virtual hosts no painel da HostGator, subpastas, ou outra coisa?
- Que critério ele vai usar para "quando eu indico um, quando eu indico o outro"?
- A aula de rede privada × pública vai responder a pergunta do celular (IP privado, NAT)?

## Raw quotes

> "Por que você não consegue upar [...] para a internet, um site que está direto no seu computador, sendo que está rodando no seu computador, por que ninguém consegue acessar?"

> "A porta 80 é a porta padrão, e quando ela é a padrão, ela meio que não existe."

> "Você consegue colocar os arquivos direto pelo Git."

## Continuação

A próxima aula promete "aprofundar um pouco mais os conhecimentos que a gente acabou de citar aqui". Cumprida em [[wiki/sources/frontpush-ip-e-dns-ipv4-ipv6-ip-publico-privado-registro-br]]: a pergunta do celular é respondida com `192.168.1.92:5500` na mesma rede, e IP público × privado, DNS e Registro.br entram como previsto (Precisão 3 confirmada).
