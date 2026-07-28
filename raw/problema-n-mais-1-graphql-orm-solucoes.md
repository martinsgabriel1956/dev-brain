# O Problema de N+1: Como Ele Moldou a Computação (e Como Resolver)

> Transcrição de vídeo, reestruturada em Markdown. Conteúdo já em português, sem necessidade de tradução.

## Introdução

Vamos falar sobre o problema clássico da computação chamado **N+1**. Esse problema acontece o tempo todo, e aparece em duas interfaces/comunicações diferentes:

1. Entre **frontend e backend**, através de uma API.
2. Entre **backend e banco de dados**, através do acesso ao banco — essa é a origem mais notória e mais descrita do problema.

Todo desenvolvedor backend deveria conseguir identificar e resolver esse problema. Ele apareceu em todas as empresas em que o autor já trabalhou, de uma forma ou de outra.

---

## Parte 1 — O Problema Descrito no Frontend/Backend

### Cenário

Imagine dois endpoints:

- `GET /users` → retorna uma lista de usuários (`id`, `nome`, `idade`).
- `GET /users/{user_id}/posts` → lista os posts de um usuário específico (`id`, `título`, `body`).

O frontend é um app standalone que se comunica com o backend via API. Se o frontend precisa mostrar uma lista de usuários **com** os posts de cada um, e só existem esses dois endpoints, o fluxo obrigatório é:

1. Um request para `GET /users` (o "**1**" de N+1). Cada chamada custa ~100ms de rede.
2. Um request para `GET /users/{id}/posts` **para cada usuário retornado** (o "**N**"). Com 50 usuários, são 50 requests adicionais.

**Problema de N+1:** você precisa de 1 request para obter a lista, e de N requests adicionais — um por item da lista — para obter os dados relacionados de cada item.

### Por que é ineficiente

- Custo de ida-e-volta de rede (latência) multiplicado por N.
- Mais chamadas no backend → mais uso de CPU, mais conexões, mais carga.
- Eliminar o N+1 significa ganho de eficiência, velocidade, uso de recursos e experiência do usuário.

---

## Parte 2 — Tentativas de Solução com REST

### Opção A: endpoint especializado (`GET /users-and-posts`)

Um endpoint dedicado que já retorna, para cada usuário, a lista de posts embutida.

### Opção B: endpoint que recebe lista de IDs (`GET /posts?users=[...]`)

Recebe uma lista de IDs de usuário e retorna todos os posts correspondentes, cada um marcado com o `user_id` dono.

### Problemas de cada opção

**Opção B** tem dois problemas:
1. Você já precisa ter os IDs dos usuários — para obtê-los, ainda precisa de um primeiro request a `GET /users`. Isso reduz N+1 para **1+1**, o que já é uma melhoria grande.
2. **Paginação.** Em produção, `GET /users` nunca retorna todos os usuários do banco — retorna uma página (ex.: 50 de muitos). Isso já é usual e conhecido. Só que dentro de `GET /posts`, cada usuário pode ter, por exemplo, 1000 posts — que também precisam de paginação. Agora você tem paginação em dois níveis (usuários e posts por usuário), e não fica claro como estruturar isso: offset de posts geral? Offset de posts por usuário? Fica complicado rápido.

**Opção A** (`GET /users-and-posts`) tem problema parecido: se um usuário tem 1000 posts, o que o endpoint retorna? Um usuário com 1000 posts, ou 1000 usuários com só os 3 primeiros posts de cada? É preciso decidir um limite fixo (ex.: "no máximo 3 posts por usuário nesta tela") e aceitar que esse endpoint vira específico para uma tela.

### A saída prática: Backend for Frontend (BFF)

Na prática, empresas costumam implementar **várias dessas soluções ao mesmo tempo**, para propósitos diferentes — um endpoint bem específico por tela (BFF). Se a tela mostra no máximo 3 posts por usuário, o endpoint retorna exatamente isso, sem paginação interna de posts (só paginação de usuários).

O problema aparece quando a empresa cresce rápido e cria tela atrás de tela: cada tela nova (mobile, web, um caso "eventos → usuários", outro "posts → comentários") tende a pedir um novo endpoint especializado, e o backend fica sobrecarregado com uma quantidade absurda de endpoints.

---

## Parte 3 — A Origem do GraphQL

Seria ótimo se o frontend pudesse dizer exatamente que estrutura de dados ele quer — por exemplo: "quero uma estrutura `post`, e dentro dela os `comments` que pertencem àquele post" — e o backend "se virasse" para montar exatamente isso, em vez de expor um endpoint genérico e engessado.

Essa foi exatamente a motivação por trás da criação do **GraphQL** pela **Meta** (antes Facebook). O Facebook, na época, tinha múltiplos frontends evoluindo muito rápido (mobile, web, iPad), com estruturas de dados profundamente aninhadas (usuário → post → comentário), e precisava de uma forma mais genérica de expor dados sem multiplicar endpoints especializados a cada nova tela. Fato: a Meta criou o GraphQL. (É provável que estruturas parecidas já existissem antes de alguma forma, mas o GraphQL como o conhecemos veio da Meta.)

**Onde o GraphQL fica:** entre o frontend e o backend.

### Por que o N+1 entre frontend e backend não é o N+1 "tradicional"

O problema de N+1 é tradicionalmente descrito entre **backend e banco de dados**, não entre frontend e backend. Ele passou a existir também nessa segunda camada por uma mudança histórica: antes, o frontend pedia uma **página inteira já pronta**, construída no backend (o modelo hoje chamado de **server-side rendering** / "HTML over the wire" — ainda usado por frameworks como Ruby on Rails, Django com templates, ou Laravel). Nesse modelo, não existe N+1 entre front e back, porque a página inteira já vem pronta — não há endpoints separados para "buscar mais dados".

Quando o frontend passou a ser um app mais interativo (React e afins), que busca dados via chamadas a endpoints em vez de receber HTML pronto, o mesmo problema estrutural do banco de dados foi replicado para a camada front↔back. A resposta a esse novo problema foi o GraphQL.

### Por que GraphQL é sempre POST

GraphQL nunca usa GET, sempre POST. Motivo técnico: uma URL de GET tem um limite prático de caracteres (por volta de 2000–2048). Se cada ID de usuário tiver, por exemplo, 64 caracteres, um GET com lista de IDs como parâmetro comportaria pouco menos de 40 usuários antes de estourar o limite. Usando POST, os parâmetros vão no body, sem esse limite — mesmo sendo uma operação que não cria nada (limitação técnica, não semântica REST).

---

## Parte 4 — O Problema "Tradicional": Backend ↔ Banco de Dados

O N+1 mais conhecido historicamente é entre backend e banco de dados, e aparece o tempo todo no uso de **ORMs**.

### Exemplo com lazy loading (Django)

```python
users = User.objects.all()  # nada é executado no banco ainda

for user in users:
    print(user.name)
    # ao acessar user.name, a ORM finalmente dispara o SELECT de users

    for post in user.posts:
        # para CADA usuário, a ORM dispara um novo SELECT de posts
        print(post.title)
```

ORMs fazem **lazy loading**: elas adiam ao máximo a busca no banco, e quando buscam, trazem só o mínimo necessário para o que está sendo acessado naquele momento. O resultado prático: 1 query para usuários + 1 query de posts **por usuário** = N+1 queries.

### A solução: dizer à ORM o que você vai precisar

Se o programador já sabe que vai precisar de usuários **e** posts, dá para pedir isso de uma vez. Praticamente toda ORM séria tem uma forma de fazer **eager loading** / prefetch para isso. No Django:

```python
users = User.objects.prefetch_related('posts')
# Django já carrega os posts relacionados numa segunda query otimizada,
# em vez de uma query de posts por usuário
```

### Traduzindo para SQL puro

O equivalente de "`users_and_posts`" em SQL é um **LEFT JOIN**:

```sql
SELECT * FROM users
LEFT JOIN posts ON users.id = posts.user_id;
```

Se você já sabe quais IDs de usuário precisa (por exemplo, uma lista que já está disponível no frontend, sem precisar de outro request), a alternativa é:

```sql
SELECT * FROM posts WHERE user_id IN (...);
```

Ou seja: os mesmos dois padrões de solução do problema no frontend (endpoint especializado vs. endpoint que recebe uma lista de IDs) se repetem, com as mesmas soluções, entre backend e banco — **LEFT JOIN** (unir tabelas) ou **selecionar por IDs já conhecidos**.

### ORMs mais ergonômicas (Drizzle)

Drizzle permite uma sintaxe próxima do SQL puro:

```typescript
db.select().from(users).leftJoin(posts, eq(users.id, posts.userId))
```

Pergunta natural: se a sintaxe é quase idêntica a SQL, por que não escrever SQL puro? Resposta: o principal ganho de uma ORM como essa é **type safety** — ela sabe exatamente o que a query vai retornar e devolve um objeto tipado.

### Fechando o círculo: relational queries inspiradas em GraphQL

O Drizzle também tem **relational queries**, com uma sintaxe que lembra diretamente o GraphQL:

```typescript
db.query.users.findMany({
  with: {
    posts: true,
  },
})
```

Isso **não é GraphQL** — é açúcar sintático (syntax sugar) para dar, na camada backend↔banco, uma ergonomia parecida com a que o GraphQL oferece na camada frontend↔backend. Não é (ainda) amplamente adotado, mas mostra que a indústria "reinventa a roda" resolvendo o mesmo problema estrutural em camadas diferentes.

---

## Conclusão

- O N+1 existe tanto entre frontend↔backend quanto entre backend↔banco de dados.
- Toda ferramenta (ORM ou SQL puro) tem uma solução conhecida para o problema — vale pesquisar a solução específica da sua stack.
- As estratégias de solução se repetem nas duas camadas: endpoint/query especializada, endpoint/query que recebe uma lista de IDs já conhecida, ou prefetch/eager loading/JOIN.
- Cada abordagem tem trade-offs diferentes (paginação aninhada, granularidade do endpoint, acoplamento a uma tela específica).
- Saber identificar e resolver N+1 é, na visão do autor, requisito básico para qualquer desenvolvedor backend — o problema apareceu em todas as empresas por onde o autor passou.
