# Diferenciais de Portfólio para Dev Backend Júnior

**Fonte:** Transcrição de vídeo  
**Data:** 2026-04-25  
**Domínio:** Carreira / Backend

---

## Contexto

Para quem está disputando a primeira vaga de backend: o diferencial não está em arquitetura sofisticada, mas em demonstrar profissionalismo nas bases. Uma aplicação bem testada vale mais que uma com arquitetura impecável.

---

## O que É diferencial

### 1. Docker e Docker Compose

Qualquer dev backend vai precisar disso. O mínimo é um `docker-compose.yml` que sobe o ambiente completo (banco, serviços externos). O plus:

- `Dockerfile` com **multi-stage build** — imagem enxuta e pronta para deploy
- Configuração que facilita o deploy real (não apenas rodar localmente)

### 2. Deploy em cloud real

Preferir cloud real (AWS, Hetzner, Azure, GCP) ao invés de plataformas one-click (Render, Heroku). O esforço de configurar o ambiente manualmente demonstra domínio de infra que vai muito além do desenvolvimento.

### 3. Testes automatizados com coverage report

Ausência de testes é eliminatório. O padrão mínimo:

- **Testes end-to-end / integração** que batem nas rotas e no banco de dados real
- **Não mockar banco de dados** — usar um banco dedicado para testes (mock de banco é perigoso e mascara bugs reais)
- Mockar apenas integrações externas (envio de e-mail, APIs de terceiros)
- **Coverage report** — demonstrar cobertura concreta (ex: 96% nos arquivos propostos)

> 600+ testes de integração numa aplicação pequena em produção é mais valioso do que a melhor arquitetura sem testes.

### 4. SQL além do básico

Independente de usar ORM, demonstrar domínio de SQL:

- `JOIN` (inner, left, right)
- Agrupamentos e agregações (`GROUP BY`, `COUNT`, `SUM`)
- Subqueries
- Queries mais complexas que fujam do CRUD básico

Foco em **PostgreSQL** ou **MySQL** — os mais comuns no mercado.

### 5. Documentação de API (Swagger/Scalar)

Um a cada dez devs se preocupa com isso — grande diferencial.

- Integrar **Swagger** para gerar API reference automaticamente
- Usar **Scalar** como interface de visualização (open source, mais moderno que o Swagger UI padrão)
- Não precisa ser documentação elaborada com diagramas — API reference é suficiente para primeira vaga

### 6. Error Handling estruturado

Não deixar erros sem tratativa. O padrão:

- **Classes de erro** específicas para cada caso de negócio (ex: `EmailAlreadyExistsError`)
- Na rota: verificar o tipo do erro e retornar o **HTTP status code correto**
- **Error handler global** no servidor:
  - Erros esperados → HTTP code apropriado
  - Erros inesperados → log com stack trace (para sistema de observabilidade) + retorna 500 ao cliente
  - Em produção: não expor stack trace ao cliente

```typescript
// erro específico
export class EmailAlreadyExistsError extends Error {
  constructor() {
    super("E-mail já cadastrado");
    this.name = "EmailAlreadyExistsError";
  }
}

// na rota
try {
  await createUser(data);
} catch (error) {
  if (error instanceof EmailAlreadyExistsError) {
    return reply.status(409).send({ error: error.message });
  }
  throw error; // repassa para o error handler global
}
```

### 7. Observabilidade

Configurar junto com o Docker Compose:

- **Jaeger** (open source) para visualizar traces distribuídos
- Alternativas: Honeycomb, Grafana, Datadog, Sentry
- O que demonstrar:
  - Quais requisições estão sendo feitas
  - Quais são as mais lentas
  - Eventos/spans dentro de cada requisição (o passo a passo do que aconteceu)

---

## O que NÃO é diferencial para primeira vaga

| Item | Por quê não foca agora |
|---|---|
| DDD, Clean Architecture complexa | Projetos grandes em produção usam 5 pastas e os fundamentos acima |
| Microsserviços | Complexidade desnecessária para o nível |
| Banco NoSQL (MongoDB) | Redis como cache é ok; além disso, não prioritário |
| Escalabilidade / infra profunda | Habilidade que vem com experiência |
| Múltiplos frameworks (NestJS, Moleculer...) | Todos usam os mesmos fundamentos — dominar um bem é suficiente |

---

## Resumo: o que importa

```
✅ Docker + Docker Compose (+ Dockerfile com multi-stage)
✅ Deploy em cloud real
✅ Testes end-to-end com banco real + coverage report
✅ SQL além do básico (joins, agregações, subqueries)
✅ Documentação de API (Swagger + Scalar)
✅ Error handling estruturado (classes de erro + handler global)
✅ Observabilidade (Jaeger ou similar)

❌ DDD / Clean Architecture avançada
❌ Microsserviços
❌ MongoDB / NoSQL
❌ Escalabilidade / infra avançada
❌ Múltiplos frameworks
```

Uma aplicação bem testada é mais importante que uma aplicação com a melhor arquitetura do mundo.
