---
type: source
title: "Reação a Artigo Visual sobre Algoritmos de Load Balancing"
aliases: ["simulação visual load balancing", "round robin vs least connections vs ewma", "dynamic weighted round robin"]
date_created: 2026-08-06
date_updated: 2026-08-06
source_count: 0
tags: [load-balancer, round-robin, weighted-round-robin, least-connections, ewma, filas, latencia, infra, system-design]
skill: tech-mentor-infra
status: draft
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/reacao-artigo-visual-algoritmos-load-balancing.md
source_url:
author:
date_published:
date_ingested: 2026-08-06
---

# Reação a Artigo Visual sobre Algoritmos de Load Balancing

## TL;DR

Vídeo de reação/tradução simultânea a um artigo interativo em inglês que simula visualmente (bolinhas de requisição "encolhendo" enquanto são processadas) o comportamento de algoritmos de load balancing sob variação de potência de servidor e custo de requisição. Progressão didática: Round Robin dropa requisição quando servidor/custo variam → fila de requisições reduz drops ao custo de latência → Weighted Round Robin (peso manual, não escala) → Dynamic Weighted Round Robin (peso calculado por latência observada) → Least Connections (rastreia conexões abertas, só dropa quando *todas* as filas estão cheias) → PEWMA (combina latência ponderada por média móvel exponencial com monitoramento de carga em tempo real). Conclusão do artigo: sempre validar escolha de algoritmo com benchmark contra a carga real do próprio sistema.

## Key Claims

| Claim | Evidência |
|---|---|
| Round Robin distribui igualmente mesmo quando servidores/requisições têm custo desigual — droppa requisição nessas condições | Simulação com custo de requisição variado no artigo |
| Fila de requisições reduz drops, mas troca isso por latência maior em algumas requisições — trade-off, não solução gratuita | Simulação com fila + custo variado |
| Weighted Round Robin exige calibrar peso manualmente por servidor — não escala, pois exigiria benchmark de carga real por servidor | Argumento do artigo sobre WRR estático |
| Dynamic Weighted Round Robin calcula peso a partir da latência média das últimas requisições servidas, sem input manual | Descrição do algoritmo dinâmico |
| Least Connections só dropa requisição quando todas as filas de todos os servidores estão cheias — mais resiliente que os RR por eliminar estimativa e usar contagem exata de conexões abertas | Simulação de Least Connections sob alta variância |
| PEWMA (Pick Exponentially Weighted Moving Average) combina a adaptação por latência do Dynamic WRR com a resiliência de carga do Least Connections | Conclusão técnica do artigo antes do disclaimer final |
| Nginx usa Round Robin como algoritmo padrão de balanceamento HTTP | Afirmação feita durante a leitura, não verificada contra a documentação oficial do Nginx nesta ingestão |

## Conceitos

- [[wiki/concepts/load-balancer]] — Round Robin, Weighted Round Robin, Least Connections já documentados; esta fonte adiciona Dynamic Weighted Round Robin e PEWMA
- [[wiki/concepts/escalabilidade-horizontal]] — múltiplos servidores atrás de um load balancer como resposta ao limite de um servidor único
- [[wiki/concepts/alta-disponibilidade]] — requisição dropada é o sintoma direto de indisponibilidade sob carga
- [[wiki/concepts/pub-sub]] — fila de requisições como mecanismo de absorção de picos, análogo a message queue
- [[wiki/concepts/rate-limiting]] — mesmo dilema estrutural (dropar vs. enfileirar) aparece em proteção de API
- [[wiki/concepts/reverse-proxy]] — Nginx citado como exemplo de LB HTTP com Round Robin padrão
- [[wiki/concepts/cluster]] — arquitetura genérica de load balancer na frente de N nodes
- [[wiki/concepts/service-discovery]] — pré-requisito implícito: o LB precisa saber quais servidores existem antes de poder escolher entre eles
- [[wiki/concepts/sticky-session]] — contraste: os algoritmos aqui pressupõem servidores intercambiáveis, sem afinidade de sessão

## Open Questions

- A afirmação de que Nginx usa Round Robin como padrão HTTP é repetida aqui e em [[wiki/sources/escalabilidade-horizontal-load-balancer-algoritmos]] — permanece não verificada contra a documentação oficial atual do Nginx (mesma lacuna já registrada em [[wiki/concepts/load-balancer]]).
- PEWMA/EWMA não foi detalhado a fundo na fonte (o apresentador pulou parte da explicação por perda de voz) — vale revisitar o artigo original para captar a mecânica exata do cálculo da média móvel exponencial.
- Não foi possível confirmar a URL/autoria do artigo original comentado no vídeo — a fonte é a transcrição da reação, não o artigo em si.

## Key Sources

_Este é o documento primário._
