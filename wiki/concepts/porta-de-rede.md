---
type: concept
title: "Porta de Rede"
aliases: ["port", "port number", "well-known ports", "registered ports", "dynamic ports", "ephemeral ports"]
date_created: 2026-07-15
date_updated: 2026-07-15
source_count: 1
tags: [porta, tcp-ip, iana, networking, cs-fundamentals]
skill: tech-mentor-networking
status: draft
---

# Porta de Rede

**Número virtual (0–65.535) que identifica um serviço ou processo dentro de um host** — não é hardware, é só um rótulo que o sistema operacional usa para rotear dados ao programa certo. Junto com o endereço IP (que diz *onde* — qual host, geograficamente/topologicamente), a porta diz *qual serviço naquele host* (`IP:porta`, ex. `93.184.216.34:80`). Ver [[wiki/concepts/protocolo-de-rede]] para onde a porta se encaixa no modelo em camadas (camada de transporte, junto com TCP/UDP).

## As três faixas administradas pela IANA

A [[wiki/entities/iana]] organiza o espaço de 0–65.535 em três categorias:

1. **Well-known ports (0–1023)** — serviços essenciais e universais. `80` HTTP (sem criptografia), `443` HTTPS (TLS por cima — ver [[wiki/concepts/criptografia]]), `25` SMTP (email), `22` SSH (acesso remoto — ver [[wiki/concepts/ssh]]).
2. **Registered ports** — registradas por empresas/projetos para uma aplicação específica, mas não universais como as well-known. Ex.: `1433` Microsoft SQL Server, `3389` RDP (equivalente Windows do SSH para acesso remoto gráfico).
3. **Private/dynamic (ephemeral) ports** — não pertencem a serviços, pertencem a **clientes**. Ver seção abaixo.

## Well-known/registered vs. dynamic: servidor vs. cliente

Essa é a distinção central do conceito: well-known e registered ports identificam **o que um servidor oferece** (a "porta de entrada" que o cliente bate); dynamic ports identificam **de onde no cliente uma requisição saiu**, para que a resposta consiga voltar ao processo exato que pediu.

Exemplo: ao assistir a dois vídeos do YouTube em abas diferentes, o sistema operacional atribui uma porta dinâmica distinta a cada aba (ex.: `50000` e `55000`). Ambas as conexões saem para o mesmo servidor remoto na porta `443` (HTTPS), mas o par `IP-local:porta-dinâmica` é único por aba — é isso que permite ao SO devolver cada stream de vídeo à aba correta quando os pacotes de resposta chegam, todos vindos do mesmo `IP:443` remoto. Sem a porta dinâmica, o SO não teria como demultiplexar múltiplas conexões simultâneas para o mesmo destino.

## Estados de uma porta/conexão

| Estado | Significado |
|---|---|
| **Listening / LISTEN** | Porta aguardando conexões de entrada — típico em servidores (ex.: porta 80 esperando clientes), mas também acontece localmente quando um app expõe um serviço na própria máquina. |
| **Established / ESTABLISHED** | Conexão ativa, dados trafegando nos dois sentidos. |
| **Closed** | Nenhum processo escutando; sem conexão ativa. Não aparece como uma linha "ativa" nas ferramentas de diagnóstico — é a ausência de listener. |
| `TIME_WAIT`, `CLOSE_WAIT` | Estados transitórios de encerramento de conexão TCP — fora do escopo para iniciantes, mas relevantes para diagnosticar esgotamento de portas em servidores com muitas conexões curtas. |

## Ferramentas de diagnóstico: netstat (Windows) vs. ss (Linux)

No Windows, `netstat -n` lista conexões ativas (colunas: `Proto`, `Local Address`, `Foreign Address`, `State`); `netstat -a` acrescenta as portas em listening. No Linux moderno, `netstat` é considerado legado — o equivalente é `ss` (ex.: `ss -tan`, `ss -tan state established`), que lê diretamente das estruturas do kernel em vez de `/proc`, sendo mais rápido em hosts com muitas conexões. `[skill: tech-mentor-networking]`

## Relação com outros conceitos

- [[wiki/concepts/protocolo-de-rede]] — porta é o identificador de serviço na camada de transporte, ao lado de TCP/UDP e do IP na camada de rede.
- [[wiki/concepts/ssh]] — porta 22 é a well-known port do protocolo, e a configuração de cliente/servidor SSH permite trocá-la explicitamente.
- [[wiki/concepts/dns]] — DNS resolve o nome para o IP; a porta então seleciona o serviço dentro daquele IP (os dois resolvem endereçamento em camadas diferentes: nome→host, host→serviço).
- [[wiki/concepts/load-balancer]] — um load balancer L4 roteia exatamente por `IP:porta`, sem inspecionar o conteúdo da aplicação.
- [[wiki/entities/iana]] — autoridade que administra as faixas de porta globalmente.

## Key sources

- [[wiki/sources/portas-de-rede-como-funcionam]]
