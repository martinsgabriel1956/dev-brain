---
type: concept
title: "Connection Pooling"
aliases: ["pgbouncer", "pool de conexões", "database pool", "poll vs pool"]
date_created: 2026-04-22
date_updated: 2026-08-10
source_count: 5
tags: [banco-de-dados, performance, pgbouncer, postgresql, mysql, escalabilidade, serverless]
skill: tech-mentor-system-design
status: stable
---

# Connection Pooling

Reutiliza conexões abertas ao banco. Sem pool, cada request abre/fecha uma conexão — overhead de handshake TCP + autenticação.

> **Pool vs. Polling:** *pool* (piscina, grupo de conexões reutilizadas) e *poll* (polling, tentar repetidamente um recurso para ver se está disponível) são termos frequentemente confundidos — são conceitos completamente diferentes. Ver [[wiki/sources/connection-pooling-pool-vs-polling-serverless]].

## O Problema

```
50 pods × 20 conexões = 1000 conexões simultâneas no PostgreSQL
PostgreSQL não escala bem com >200-300 conexões — overhead de memória e locks
```

## Solução com PgBouncer

```
50 pods × 20 conexões = 1000 → PgBouncer → 20 conexões reais no PostgreSQL
```

```ini
[databases]
mydb = host=postgres port=5432 dbname=mydb

[pgbouncer]
pool_mode = transaction    # recomendado: pool por transação
max_client_conn = 1000     # máximo de conexões de entrada
default_pool_size = 20     # conexões reais no banco
```

## Pool Modes

- `session` — conexão fica com o cliente durante toda a sessão. Menos eficiente.
- `transaction` — conexão retorna ao pool após cada transação. **Recomendado.**
- `statement` — retorna após cada statement. Incompatível com transações multi-statement.

## Instanciando a Pool como Singleton

A pool deve ser criada **uma única vez, fora do handler de rota**, e reutilizada entre requests — não instanciada (nem fechada) a cada requisição, senão o benefício do pooling desaparece. Em Node.js, um módulo é cacheado após o primeiro `require`/`import` — na prática um [[wiki/concepts/singleton-pattern]] — o que garante que a mesma pool seja compartilhada por todas as chamadas da rota. O comportamento exato depende de como a linguagem/runtime trata módulos.

```js
// pool instanciada uma única vez, fora da rota
const pool = new Pool({ max: 10 });

app.get('/users', async (req, res) => {
  const client = await pool.connect();
  try {
    const result = await client.query('SELECT * FROM users');
    res.json(result.rows);
  } finally {
    client.release(); // sempre libera, mesmo se houver erro
  }
});
```

## Vazamento por `client.release()` Esquecido

Bug comum e fácil de identificar em produção, porque estoura a aplicação rapidamente: cada request pega uma conexão do pool (`pool.connect()`) mas esquece de devolvê-la (`client.release()`). Uma pool de 10 conexões vai encolhendo — 9, 8, 7... — até esgotar e travar novos requests.

**Mitigação:** sempre liberar a conexão dentro de um `finally` (ou equivalente na linguagem). Sem isso, um erro lançado na query pode desviar o fluxo de execução e pular a linha do release, vazando a conexão silenciosamente a cada erro. Ver [[wiki/sources/connection-pooling-pool-vs-polling-serverless]].

## Connection Pooling em Ambientes Serverless

Em serverless (ex.: AWS Lambda) não existe memória compartilhada entre invocações — cada invocação é autossuficiente, instancia ao receber a requisição e morre ao terminar. Isso inviabiliza uma pool "normal" mantida em memória de processo dentro do código de negócio: 20 requests simultâneos instanciam 20 execuções isoladas, cada uma tentando abrir suas próprias conexões.

A solução depende do ambiente:

| Ambiente | Solução | Observação |
|---|---|---|
| AWS Lambda | **RDS Proxy** | Servidor intermediário que mantém a pool; cada Lambda faz request a ele em vez de abrir conexão direta com o banco |
| Vercel Functions | **Attach Database Pool** | Solução própria documentada nas Vercel Functions — lock-in de plataforma |
| Qualquer ORM | Suporte nativo equivalente | Vale checar a documentação da ORM usada antes de gerenciar pooling manualmente |
| Genérico | PgBouncer como proxy | Citado com disclaimer: sem relato de uso real em produção na fonte — usar com cautela |

Ver [[wiki/sources/connection-pooling-pool-vs-polling-serverless]].

## Diagnóstico Automatizado via Correlação de Telemetria com IA

Variante do vazamento por release esquecido: uma conexão PostgreSQL aberta e nunca encerrada em um endpoint específico (não um `pool.connect()` sem `release()` genérico, mas uma conexão manual mantida aberta) esgota o pool e vira timeout nos requests seguintes. Num caso demonstrado, um agente de IA conectado apenas às bases de observabilidade (logs, métricas e traces via [[wiki/concepts/model-context-protocol|MCP]] ou assistente equivalente) — sem acesso ao código-fonte — apontou a linha exata do vazamento a partir da correlação entre o padrão de timeouts nos logs e o crescimento do tempo de conexão segurada nas métricas. Ver [[wiki/concepts/investigacao-de-incidentes-com-ia-e-mcp]]. Reforça o ponto acima ("Diagnóstico: Tempo de Conexão Segurada, Não Latência de Query") — a assinatura desse tipo de bug é visível na telemetria antes mesmo de se olhar o código.

## Diagnóstico: Tempo de Conexão Segurada, Não Latência de Query

Um sistema pode ter CPU baixa e queries individuais rápidas e ainda assim bater um teto de escalabilidade — porque o gargalo real é uma parte do código segurando conexões do pool por mais tempo do que deveria, esgotando o pool para todo o resto. Otimizar a query em si não resolve, porque a query não é o problema. A técnica de diagnóstico é etiquetar cada operação SQL por origem (ex: "checkout", "reserva") e medir **quanto tempo cada uma segura uma conexão aberta**, não sua latência de execução. Foi assim que a [[wiki/entities/shopify]] descobriu que o gargalo de escalabilidade estava em código legado do checkout, não nas queries de reserva de estoque que pareciam ser o problema. Ver [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]].

## Key Sources

- [[sources/banco-de-dados]]
- [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]] — instrumentação por tempo de conexão segurada, não latência de query
- [[wiki/sources/connection-pooling-pool-vs-polling-serverless]] — pool como singleton, vazamento por release esquecido, pooling em serverless (RDS Proxy, Vercel, PgBouncer)
- [[wiki/sources/monitoramento-aplicacoes-ia-grafana-cloud-opentelemetry]] — vazamento de conexão PostgreSQL nunca encerrada, diagnosticado por um assistente de IA apenas com acesso à telemetria (sem código-fonte), correlacionando timeouts em logs com tempo de conexão segurada em métricas
- [[wiki/sources/escalar-leituras-banco-de-dados-entrevista-tier-s]] — pooling como dupla inseparável do índice para resolver ~80% dos gargalos de leitura: abrir conexão custa ~5-10ms de setup e o banco tem teto de conexões; sob alta carga esse custo vira erro para o usuário
