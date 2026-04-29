# A Tecnologia Boring Por Trás de Uma Empresa de Uma Pessoa Só

> Artigo original: [The boring technology behind a one-person Internet company](https://www.freecodecamp.org/news/the-boring-technology-behind-a-one-person-internet-company/)
> Autor: Wenbin Fang | Publicado: junho 2019

---

## Contexto

O Listen Notes é um buscador de podcasts e banco de dados. A tecnologia por trás dele é deliberadamente **boring**: sem AI, sem deep learning, sem blockchain.

> *"Any man who must say I am using AI is not using True AI."*

Após ler este artigo, você deveria ser capaz de replicar o que foi construído no Listen Notes — ou fazer algo similar. Você não precisa contratar muitos engenheiros. Quando o Instagram levantou $57.5M e foi adquirido pelo Facebook por $1B, tinha apenas 13 funcionários. Em 2019, é mais possível do que nunca construir algo significativo com um time minúsculo — ou uma pessoa.

---

## O que o Listen Notes oferece

1. **Website ListenNotes.com** para ouvintes de podcast: busca, banco de dados, playlists Listen Later, Listen Clips (cortar segmentos), Listen Alerts (notificações por keyword)
2. **Podcast Search & Directory API** para desenvolvedores

---

## Infraestrutura — 20 Servidores AWS (maio 2019)

| Servidor | Responsabilidade |
|---|---|
| `production-web` (×2) | Serve tráfego web do ListenNotes.com |
| `production-api-v1` | API legada |
| `production-api-v2-1`, `v2-2` | Nova versão da API (2 máquinas) |
| `production-db1` (primary) | PostgreSQL — fonte de verdade |
| `production-db2` (replica) | Réplica PostgreSQL |
| `production-es1/2/3` | Cluster Elasticsearch |
| `production-worker1–8` | Workers offline (crawling, ranking, recomendações) |
| `production-lb` | Load balancer + Redis + RabbitMQ (conveniente, não ideal) |
| `production-tango` | Scripts manuais e testes com características de prod |

### Diagrama de arquitetura

```
[Browser]
    ↓
[Load Balancer — Nginx]  ← Redis + RabbitMQ aqui também (conveniência)
    ↓
[Web Servers — Django]
    ↓
[Data Store]
  ├── PostgreSQL (source of truth)
  ├── Elasticsearch (busca)
  └── Redis (cache)

[Celery Beat — Scheduler]
    ↓
[RabbitMQ — Message Queue]
    ↓
[Celery Workers ×8] → crawl, rank, alertas, recomendações
```

**Regra central:** PostgreSQL é o single source of truth. Redis e Elasticsearch são derivados — podem estar desatualizados temporariamente.

---

## Stack Técnica Completa

### Backend
| Camada | Tecnologia |
|---|---|
| Framework web | Django (Python) |
| Banco principal | PostgreSQL |
| Busca | Elasticsearch |
| Cache | Redis |
| Message broker | RabbitMQ |
| Workers assíncronos | Celery |
| Scheduler | Celery Beat |

### Frontend
| Camada | Tecnologia |
|---|---|
| Framework | React + Redux + Webpack |
| SSR parcial (SEO) | Django templates |
| Assets estáticos | Amazon S3 + CloudFront |
| Player de áudio | hls.js (customizado) |

### DevOps
| Ferramenta | Uso |
|---|---|
| Nginx | Load balancer |
| Ansible | Provisionamento de servidores |
| Vagrant + VirtualBox | Ambiente local = prod |
| AWS EC2 | VPS de produção |
| GitHub (privado) | Monorepo |

### Monitoramento
| Ferramenta | Uso |
|---|---|
| Datadog | Métricas e dashboards |
| PagerDuty | Alertas on-call integrado ao Datadog |
| Rollbar | Captura exceções Django → Slack |
| Slack | Webhooks de eventos de negócio (novo usuário, nova compra) |

### Outros serviços
- G Suite — email e calendário
- Notion — anotações
- Mailchimp — newsletter mensal
- Amazon SES — emails transacionais
- Google Speech-to-Text — transcrição de episódios
- QuickBooks — contabilidade
- 1Password — gestão de senhas
- Brex — cartão corporativo
- Google Ad Manager + Carbon + BuySellAds — anúncios

---

## Desenvolvimento

- **Editor:** PyCharm
- **Repo:** monorepo GitHub privado (backend + frontend + DevOps)
- **Branch strategy:** trabalha direto na main, feature branches raramente
- **Dev local:** Vagrant + VirtualBox para espelhar prod
- **Escritório:** WeWork em San Francisco (otimiza produtividade)

---

## Citações

> "The technology behind Listen Notes is actually very very boring. No AI, no deep learning, no blockchain."

> "Remember, when Instagram raised $57.5M and got acquired by Facebook for $1B, they had only 13 employees."

> "I know this is not ideal." (sobre rodar Redis e RabbitMQ no load balancer)
