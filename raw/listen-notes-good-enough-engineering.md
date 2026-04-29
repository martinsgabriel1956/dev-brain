# Engenharia Boa o Suficiente Para Começar Uma Empresa na Internet

> Artigo original: [Good enough engineering to start an Internet company](https://www.freecodecamp.org/news/good-enough-engineering-to-start-an-internet-company/)
> Autor: Wenbin Fang | Publicado: agosto 2019
> Baseado em palestra na CSCE431 (Texas A&M University, março 2019)

---

## Tese Central

Construir um produto de internet não é como construir um iPhone ou uma pirâmide. Seu produto **não precisa ser perfeito no início**. Se você está construindo algo útil, as pessoas vão te dizer o que fazer a seguir.

A primeira versão do Facebook foi lançada em fevereiro de 2004 — quatro semanas de trabalho de um estudante de graduação. Era um produto "good enough" com engenharia "good enough". Hoje qualquer formado em CS consegue replicar isso em um fim de semana com frameworks modernos (Rails, Django).

---

## Contexto do Autor

Wenbin Fang roda o Listen Notes, Inc. com apenas um funcionário em tempo integral (ele mesmo). Construiu um buscador de podcasts ([ListenNotes.com](https://www.listennotes.com/)) e uma [API de podcasts](https://www.listennotes.com/api/).

---

## Princípio "Existe Uma Ferramenta Para Isso"

> *"It's 2019 now. It's unlikely that you are the first person to encounter a fundamentally new problem. There must be tools and services out there that can help you solve problems — oftentimes, for free!"*

Você vai ouvir isso muito: **"existe uma ferramenta para isso"**. Isso é o que significa "good enough engineering".

### Exemplos práticos

| Problema | Ferramenta |
|---|---|
| Autenticação | Auth0, Firebase Auth |
| Pagamentos | Stripe |
| Email transacional | Amazon SES |
| Newsletter | Mailchimp |
| Monitoramento | Datadog, Rollbar |
| Alertas on-call | PagerDuty |
| Busca | Elasticsearch |
| Filas | RabbitMQ, SQS |
| Scraping | BeautifulSoup, Scrapy |

---

## Arquitetura "Good Enough" para 99% dos Casos

### Trajetória real do Listen Notes

1. **DigitalOcean / AWS Lightsail** — suficiente para começar
2. **AWS EC2** — quando precisou de mais flexibilidade

### Arquitetura padrão

```
[Browser]
    ↓
[Load Balancer]
    ↓
[Web Servers]
    ↓
[Data Store]
  ├── Banco de dados relacional (source of truth)
  ├── Search engine (opcional)
  └── Cache (opcional)
```

**Regra:** a arquitetura acima serve 99% dos casos. Só escale quando tiver evidência de que precisa.

### Processamento assíncrono

Para tarefas longas ou intensas em CPU, **não coloque no web server**. Use:

```
[Web Server] → [Message Queue] → [Workers]
```

Exemplo do Listen Notes: web servers colocam mensagens na fila (RabbitMQ), workers (Celery) processam — crawling, ranking, alertas.

---

## Mentalidade

### Sobre originalidade

> *"It's impossible for you to come up with a 100% original startup idea nowadays. If you think your idea is unique and original, then it's more likely that you don't read enough books or don't listen to enough podcasts."*

### Sobre perfeição

> *"Building an internet product is not like building an iPhone or a pyramid. Your product doesn't need to be perfect at the beginning."*

### Sobre incerteza

Se você quer começar sua própria empresa, precisa estar confortável lidando com incerteza. Você vai descobrir o que fazer a seguir conforme for construindo e ouvindo usuários.

### Sobre over-engineering

A armadilha clássica: você over-engenheira antes de ter qualquer usuário. A maioria das features falha. Não construa um palácio para algo que pode ser demolido. Construa o mínimo que resolve o problema, valide, depois evolua.

---

## Checklist para Começar

1. Identifique um problema que você mesmo tem
2. Escolha tecnologia que você já conhece (boring é melhor)
3. Use ferramentas existentes para tudo que não é core do seu negócio
4. Lance o mais rápido possível
5. Ouça os usuários para decidir o que vem a seguir

---

## Citações

> "There must be tools and services out there that can help you solve problems — oftentimes, for free!"

> "Your product doesn't need to be perfect at the beginning. If you are building something useful, other people will tell you what to do next."

> "You have to start from somewhere or nowhere."
