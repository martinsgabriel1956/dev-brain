---
type: source
title: "Endereço IP, Domínio, DNS, HTTP/HTTPS e Configuração de Domínio na AWS (Fernanda Kipper)"
aliases: ["ip dominio dns https aws fernanda kipper", "configurar dominio aws route53 cloudfront s3", "endereco ip ipv4 ipv6 dns fernanda kipper"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_count: 0
tags: [tech-mentor-networking, dns, endereco-ip, ipv4, ipv6, dominio, https, ssl, aws, route-53, cloudfront, s3, acm]
skill: tech-mentor-networking
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/enderecos-ip-dns-dominios-https-aws-fernanda-kipper.md
source_url:
author: Fernanda Kipper
date_published:
date_ingested: 2026-08-12
---

# Endereço IP, Domínio, DNS, HTTP/HTTPS e Configuração de Domínio na AWS (Fernanda Kipper)

## TL;DR

Aula de fundamentos de web/rede (Fernanda Kipper) que amarra a teoria de **endereçamento da internet** a uma configuração prática de deploy na AWS. Cobre quatro conceitos-base: [[wiki/concepts/endereco-ip|endereço IP]] (sequência numérica que identifica um dispositivo na rede; [[wiki/concepts/endereco-ip|IPv4]] com formato de 4 octetos 0–255 e teto de ~4,3 bilhões de endereços, já se esgotando → IPv6); [[wiki/concepts/dominio|domínio]] (nome legível = nome personalizado + [[wiki/concepts/dominio|TLD]], onde TLD diferente = domínio diferente); [[wiki/concepts/dns|DNS]] como "agenda telefônica" que resolve domínio → IP; e [[wiki/concepts/http-vs-https|HTTP vs HTTPS]] (o *Secure* adiciona criptografia com troca de chaves e [[wiki/concepts/certificado-ssl-acm|certificado SSL]], mitigando Man-in-the-Middle — mas o SSL só prova que quem responde é dono *daquele* domínio, não que é a marca esperada). A parte prática configura o domínio `kdev.xyz` no [[wiki/concepts/aws-route-53|Route 53]]: cria hosted zone, troca os name servers no registrador ([[wiki/entities/godaddy|GoDaddy]]) para os NS da AWS (com nota sobre **propagação DNS**), aponta para um site estático em [[wiki/concepts/amazon-s3|S3]] (só HTTP), e depois adiciona HTTPS via certificado no **ACM** (validação por CNAME) + distribuição [[wiki/concepts/aws-cloudfront|CloudFront]] com redirect HTTP→HTTPS. Antes do AWS, mostra que seu site real está hospedado na [[wiki/entities/vercel|Vercel]] (name servers do domínio na GoDaddy apontam para lá).

## Key Claims

| Claim | Evidence | Confidence |
|---|---|---|
| Endereço IP é uma sequência numérica que identifica um dispositivo em uma rede (que pode ou não ser a internet) | "usada para identificar o endereço de um dispositivo conectado a uma rede... essa rede pode ser tanto uma rede de computadores quanto a internet" | Alta |
| IPv4 é a versão 4 do protocolo da internet; seu maior padrão é o formato do endereço IP | "IPv4 é o protocolo da internet na versão 4... o maior padrão definido pelo IPv4 é o formato dos endereços IP" | Alta |
| Formato IPv4: 4 grupos separados por ponto, cada grupo de 0 a 255 | "três números seguido por três números... esses números podem variar entre 0 a 256" (aproximação; correto é 0–255) | Alta (com imprecisão do teto) |
| Total de endereços IPv4 é finito, ~4,3 bilhões, e está se esgotando | "esse número aqui é aproximadamente 4,3 bilhões... em algum momento esse número vai acabar" | Alta |
| IPv6 é a versão 6 do protocolo, com novo formato; IPv4 ainda é o mais usado; há coexistência | "aí que surge o famoso IPv6... a versão mais utilizada hoje ainda é a versão 4... uma coexistência entre IPv4 e IPv6" | Alta |
| Domínio é um nome legível que traduz endereços IP; composto por nome personalizado + TLD | "os domínios são uma forma de traduzir endereços IP para nomes legíveis... nome personalizado seguido da extensão do domínio" | Alta |
| Mesmo nome com TLD diferente = domínios diferentes (podem ter donos diferentes) | "eu posso ter o fernandakipper.com e não possuir o fernandakipper.com.br porque são domínios diferentes" | Alta |
| Servidores DNS funcionam como agenda telefônica: recebem o domínio e devolvem o IP | "servidores espalhados por todo o mundo que funcionam como uma agenda telefônica" | Alta |
| A resolução costuma partir do provedor de internet, que consulta o DNS | "essa requisição sai do meu computador vai pro meu provedor de internet... a Claro se conecta a um servidor DNS para fazer a resolução" | Alta |
| HTTP não tem criptografia; HTTPS adiciona criptografia com troca de chaves (SSL) | "o HTTP é só o protocolo, o HTTPS é o mesmo protocolo numa versão segura... criptografia que envolve uma troca de chaves entre o navegador e o servidor" | Alta |
| HTTP puro é vulnerável a Man-in-the-Middle | "eu posso sofrer ataques de Middle Man... uma pessoa no meio que altera essa requisição" | Alta |
| Certificado SSL prova que quem responde é o dono do domínio — não que é a marca/empresa esperada | "o SSL me garante que a pessoa que é dona do domínio é realmente a pessoa que tá respondendo... não me garante que é a Adidas" | Alta |
| Route 53 gerencia domínios/DNS na AWS via hosted zone (pública ou privada) | "Route 53... usado para gerenciar domínios e fazer o gerenciamento de DNS... zona hospedada pública/privada" | Alta |
| Mudança de name servers no registrador precisa propagar por todos os DNS do mundo (leva minutos) | "demora um pouco para quando a gente faz uma alteração que essa alteração seja replicada para todos esses servidores DNS" | Alta |
| Endpoint de site estático do S3 é HTTP puro (sem SSL) → navegador marca "not secure" | "essa é uma URL HTTP não é HTTPS porque isso aqui não tem certificado SSL" | Alta |
| Para HTTPS num site estático S3: certificado no ACM (validação CNAME) + distribuição CloudFront com redirect HTTP→HTTPS | "solicitar um certificado no Certificate Manager... criar uma distribuição no CloudFront... redirect HTTP para HTTPS" | Alta |
| Backend (Lambda/EC2) usaria Load Balancer no lugar do CloudFront | "se fosse alguma função Lambda ou máquina do EC2... ia precisar criar um load balancer" | Alta |

## Fluxo de configuração (parte prática)

```
1. Route 53 → criar hosted zone pública para kdev.xyz → gera 4 name servers (NS)
2. Registrador (GoDaddy) → trocar name servers do domínio pelos NS da AWS  (⏳ propagação DNS)
3a. [HTTP] Route 53 → registro Alias → site do S3 (região us-east-1, bucket kdev.xyz)
        └─ resultado: só http://, "not secure"
3b. [HTTPS] ACM → solicitar certificado p/ kdev.xyz → cadastrar CNAME de validação no Route 53 → cert emitido
    CloudFront → distribuição: origem = bucket S3 (website endpoint),
                 viewer = Redirect HTTP→HTTPS, Custom SSL = cert ACM, Alternate name = kdev.xyz
    Route 53 → registro A → Alias → distribuição CloudFront
        └─ resultado: https://kdev.xyz servindo index.html do S3
```

## Anatomia do domínio

```
fernandakipper . com
└─ nome        └─ TLD (Top Level Domain / extensão)
   personalizado

fernandakipper.com  ≠  fernandakipper.com.br   (TLDs diferentes = domínios diferentes)
```

## Entidades Mencionadas

- [[wiki/entities/fernanda-kipper]] — autora do vídeo; desenvolvedora e criadora de conteúdo (canal no YouTube)
- [[wiki/entities/amazon-web-services]] — provedor cujo Route 53, ACM, CloudFront e S3 são usados na demo
- [[wiki/entities/vercel]] — onde o site real da autora (`fernandakipper.com`) está hospedado
- [[wiki/entities/godaddy]] — registrador onde o domínio antigo foi comprado (name servers configurados lá)
- [[wiki/entities/hostinger]] — registrador onde a autora tem os domínios mais novos (mencionado de passagem)

## Conceitos Tocados

- [[wiki/concepts/endereco-ip]]
- [[wiki/concepts/dominio]]
- [[wiki/concepts/dns]]
- [[wiki/concepts/http-vs-https]]
- [[wiki/concepts/certificado-ssl-acm]]
- [[wiki/concepts/aws-route-53]]
- [[wiki/concepts/aws-cloudfront]]
- [[wiki/concepts/amazon-s3]]
- [[wiki/concepts/cdn]]
- [[wiki/concepts/tls-handshake]]

## Open Questions

- A fonte diz que cada octeto IPv4 varia "entre 0 a 256" — o correto é **0 a 255** (8 bits). Imprecisão didática; o teto de ~4,3 bilhões (2³²) que ela cita está correto e é derivado do intervalo certo.
- Descreve HTTPS como "criptografia de ponta a ponta". Tecnicamente TLS é criptografia **em trânsito** entre cliente e servidor (o servidor descriptografa); "end-to-end" no sentido estrito (só as pontas leem, servidor intermediário não) é outra coisa. Coberto por `references/protocols-transport.md` `[skill: tech-mentor-networking]`.
- Não menciona **DNSSEC**, **TTL** (fator central da velocidade de propagação — reduzir TTL antes de migrar), nem registros AAAA (IPv6) na prática. Lacunas cobertas por `references/dns-advanced.md`.
- Não distingue **CNAME no apex** (proibido pelo RFC) do **ALIAS** do Route 53 — que é justamente o motivo de a AWS oferecer o registro Alias usado na demo. `[skill: tech-mentor-networking]`

## Raw Quotes

> "O endereço IP nada mais é do que uma sequência numérica usada para identificar o endereço de um dispositivo conectado a uma rede."

> "Os domínios nada mais são do que um nome legível pelos humanos para endereços de servidores na internet."

> "Servidores DNS são servidores espalhados por todo o mundo que funcionam como uma agenda telefônica."

> "O HTTPS adiciona uma camada de segurança nas requisições... uma criptografia que envolve uma troca de chaves entre o navegador e o servidor."

> "O SSL me garante que a pessoa que é dona do domínio é realmente a pessoa que tá respondendo, não que ela é a Adidas."
