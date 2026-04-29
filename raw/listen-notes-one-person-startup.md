# Ultra Micro Startup de Uma Pessoa Só — Listen Notes

> Baseado em três artigos de Wenbin Fang sobre como ele construiu e opera o [Listen Notes](https://www.listennotes.com/) sozinho.
> Transcrição do vídeo original adaptada para leitura.

---

## Aviso

Este vídeo é perigoso. Se você tem emprego, pode querer sair para montar seu próprio projeto. Se não tem, vai ver que é possível transformar uma ideia simples em uma startup real — uma ultra micro startup gerenciada somente por você e seus sistemas.

O autor, **Wenbin Fang**, tem dois traços marcantes no perfil:
- **Over-engineering** — excesso de engenharia
- **Over-thinking** — pensar demais e não sair do lugar

Em um dos artigos ele lança uma bomba para quem se identifica com esses traços:

> *"O seu pensar demais é a minha oportunidade."*

Quantas vezes você teve uma ideia massa, ficou pensando até alguém lançar a mesma coisa na sua frente — numa versão ainda mais simples — e deu certo?

---

## A Ideia

A sacada não foi visionária. Foi pé no chão.

> *"É impossível criar uma ideia 100% original para uma startup hoje em dia. Se você acha que a sua ideia é única e original, a maior probabilidade é que você não está lendo livros ou escutando podcasts o suficiente."*

Wenbin percebeu que os **podcasts viraram a nova Wikipédia** — uma fonte absurda de conteúdo informal. Mas ao contrário de música, queria aprender enquanto trabalhava. O problema: não existia um buscador decente para encontrar episódios por **tópico**, não por show.

Comparação que ele faz:

| Plataforma | Volume |
|---|---|
| Wikipédia | 6 milhões de artigos (inglês) |
| IMDB | 6,5 milhões de títulos |
| Spotify | 50 milhões de músicas |
| Podcasts | **61 milhões de episódios** |

Ele queria parar de seguir shows específicos e começar a seguir **assuntos**. Então construiu o Listen Notes — inicialmente como side project enquanto trabalhava full-time como programador.

---

## O Modelo de Negócio

Múltiplas fontes de renda empilhadas na mesma infraestrutura:

- **Listen Alerts** — notificações quando qualquer episódio no mundo citar um tópico ($5/mês por 5 alertas). Perfeito para repórteres cobrindo assuntos, times de marketing monitorando menções à marca.
- **Export CSV** — cobrado pelo volume de dados encontrados
- **Podcast API** — acesso programático a todo o banco de dados rastreado
- **Anúncios** — via Google Ad Manager + Carbon + BuySellAds

> *"As informações existem na internet, mas num estado completamente bagunçado. Você gera valor por conseguir agregar e limpar tudo isso."*

---

## Infraestrutura — 20 Servidores em Produção (AWS)

Começou no DigitalOcean, migrou para AWS EC2.

### Servidores e responsabilidades

| Nome | Função |
|---|---|
| `production-web` (×2) | Serve o site ListenNotes.com |
| `production-lb` | Load balancer — também roda Redis + RabbitMQ (não ideal, reconhece) |
| `production-db1` (master) | PostgreSQL — fonte única de verdade |
| `production-db2` (slave) | Réplica PostgreSQL |
| `production-es1/2/3` | Cluster Elasticsearch (busca) |
| `production-worker1–8` | Workers assíncronos (crawling, ranking, alertas) |
| `production-api-v1` | API legada |
| `production-api-v2-1/2` | Nova API (2 máquinas) |
| `production-tango` | Máquina para scripts e testes manuais (mesmas características de prod) |

### Diagrama conceitual

```
[Browser]
    ↓
[Load Balancer — Nginx]
    ↓
[Web Servers — Django]
    ↓
[Data Store]
  ├── PostgreSQL (source of truth)
  ├── Elasticsearch (busca e ranking)
  └── Redis (cache)

[Scheduler — Celery Beat]
    ↓
[Message Queue — RabbitMQ]
    ↓
[Workers — Celery] → crawling, ranking, alertas, atualizações
```

A infraestrutura é segmentada em duas partes:
- **Síncrona** (esquerda): request → load balancer → web servers → data store → resposta
- **Assíncrona** (direita): scheduler → fila → workers fazem o trabalho pesado

O PostgreSQL é tratado como **single source of truth**. Redis e Elasticsearch são derivados — podem ficar temporariamente desatualizados, mas a verdade sempre está no Postgres.

---

## Tech Stack

### Backend
- **Django** (Python) — framework web
- **PostgreSQL** — banco principal / source of truth
- **Elasticsearch** — busca e ranking de episódios (cluster de 3 máquinas)
- **Redis** — cache
- **RabbitMQ** — message broker
- **Celery** — workers assíncronos + scheduler (Celery Beat)

### Frontend
- **React + Redux + Webpack** — padrão
- **Django templates** — server-side rendering parcial (SEO)
- **Amazon S3 + CloudFront** — assets estáticos (gerados no deploy, cacheados na CDN)
- **hls.js** — player de áudio customizado

### DevOps
- **Nginx** — load balancer
- **Ansible** — provisionamento dos servidores
- **Vagrant + VirtualBox** — ambiente de dev idêntico ao de prod
- **AWS EC2** — VPS de produção
- **GitHub (privado)** — monorepo

### Monitoramento
- **Datadog** — métricas e dashboard
- **PagerDuty** — integrado ao Datadog: detectou anomalia → avisa por SMS/email/ligação até alguém confirmar ciência. Configurável por escalonamento (tenta pessoa A, depois B, depois grupo)
- **Rollbar** — captura exceções Django, notifica via Slack
- **Slack** — automações internas (novo usuário registrado, nova compra, eventos de negócio)

### Outros serviços
- **G Suite** — email e calendário
- **Notion** — anotações
- **Mailchimp** — newsletter mensal
- **Amazon SES** — emails transacionais
- **Google Speech-to-Text** — transcrição de episódios
- **QuickBooks** — contabilidade
- **1Password** — gestão de senhas
- **Brex** — cartão corporativo
- **Google Ad Manager + Carbon + BuySellAds** — anúncios

---

## Desenvolvimento

- **Editor:** PyCharm
- **Filosofia de repo:** monorepo (backend + frontend + DevOps juntos)
- **Branch strategy:** trabalha direto na main, raramente usa feature branches
- **Dev local:** Vagrant + VirtualBox para simular prod com fidelidade
- **Escritório:** WeWork em San Francisco — escolha consciente de produtividade sobre economia

---

## A Lição Principal

> *"É impossível criar uma ideia 100% original hoje. Se você acha que sua ideia é única, provavelmente você não está lendo livros ou escutando podcasts o suficiente."*

Você não precisa reinventar a roda. Você precisa de:
1. Um problema real que você mesmo tem
2. Tecnologia boring que funciona
3. Parar de pensar e começar a construir

---

## Fontes

- [The Boring Technology Behind a One-Person Internet Company](https://www.freecodecamp.org/news/the-boring-technology-behind-a-one-person-internet-company/)
- [Good Enough Engineering to Start an Internet Company](https://www.freecodecamp.org/news/good-enough-engineering-to-start-an-internet-company/)
- [Podcasts Are My New Wikipedia](https://www.freecodecamp.org/news/podcasts-are-my-new-wikipedia-the-perfect-informal-learning-resource/)
