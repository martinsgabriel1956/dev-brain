---
type: concept
title: "CDN"
aliases: ["Content Delivery Network", "rede de distribuição de conteúdo", "edge cache"]
date_created: 2026-06-26
date_updated: 2026-07-27
source_count: 2
tags: [system-design, cdn, cache, performance, escalabilidade, rede]
skill: tech-mentor-system-design
status: draft
---

# CDN (Content Delivery Network)

Rede de servidores espalhados geograficamente que guarda **cópias do conteúdo estático** próximas aos usuários. Ao invés de toda requisição ir ao servidor de origem, o usuário é roteado para o nó mais próximo.

```
Usuário no Brasil  → servidor em São Paulo  (latência ~5ms)
Usuário no Japão   → servidor em Tóquio    (latência ~5ms)
(sem CDN: ambos → servidor nos EUA, latência ~200ms)
```

## Por que CDN escala tão bem

CDN é essencialmente um **[[cache]] global**. O conteúdo é buscado da origem uma vez e servido por edge servers para todos os usuários próximos. Quanto mais popular o conteúdo, melhor o hit rate — o servidor de origem recebe cada vez menos requisições.

## O que serve bem via CDN

- Arquivos estáticos: HTML, CSS, JavaScript, imagens, vídeos, fontes
- Assets de aplicações SPA (Single Page Application)
- Arquivos de download (APKs, ZIPs, documentos)
- Streams de vídeo (HLS/DASH segments)

## O que **não** serve bem via CDN

- Conteúdo personalizado por usuário (dados de sessão, feeds personalizados)
- Requisições de API com lógica de negócio
- Dados que mudam com frequência e exigem invalidação imediata

## Benefícios

| Benefício | Como acontece |
|---|---|
| **Latência reduzida** | Proximidade geográfica encurta o RTT |
| **Escalabilidade** | Distribui load entre centenas de edge servers |
| **Proteção DDoS** | Edge servers absorvem e filtram tráfego malicioso |
| **Disponibilidade** | Se a origem cair, o CDN pode continuar servindo cache |
| **Custo de banda** | Menos tráfego saindo do servidor de origem |

## Ferramentas comuns

- **Cloudflare** — CDN + DDoS protection + WAF
- **AWS CloudFront** — integrado ao ecossistema AWS (S3, ALB)
- **Fastly** — edge computing avançado
- **Akamai** — líder histórico, empresas enterprise

## CDN como camada web

Em um sistema com três camadas (web, aplicação, dados), CDN é a solução canônica para **escalar a camada web** sem tocar código de aplicação.

## Relação com outros conceitos

- [[cache]] — CDN é um cache de camada L3 (edge) na hierarquia de velocidade
- [[escalabilidade-horizontal]] — CDN é escalabilidade horizontal aplicada à entrega de conteúdo
- [[protocolo-de-rede]] — CDN opera nas camadas HTTP e TCP; usa Anycast para roteamento geográfico

## Exemplo de Nível Sênior: Restrição Geográfica de Conteúdo

[[wiki/concepts/niveis-de-senioridade-system-design]] usa o exemplo de um usuário poder assistir um filme no Brasil mas não na Alemanha (caso Netflix) como pergunta típica de entrevista sênior: a resposta esperada combina CDN regional (Brasil e Alemanha) com identificação global de onde pertence a assinatura do usuário, localizando o conteúdo por região.

## Key sources

- [[wiki/sources/escalabilidade-vertical-horizontal-system-design]]
- [[wiki/sources/system-design-por-nivel-junior-pleno-senior]]
