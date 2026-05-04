# Ports and Adapters — Codebase Preparada para IA

**Fonte:** Vídeo do canal (autor: Galego)
**Idioma original:** Português
**Data:** 2026-05-04

---

## Contexto

A qualidade do código que a IA vai interagir importa mais do que o prompt, o modelo ou a ferramenta utilizada. Quem já tentou refatorar um código legado complexo usando IA sabe que não é uma experiência boa. Na era da IA, ter uma codebase melhor continua sendo mais produtivo do que ter uma pior.

> "As mesmas técnicas que sempre foram úteis para deixar o código com maior manutenção, mais claro e mais coeso são as mesmas técnicas que a gente pode utilizar para transformar esse código em algo que a IA consiga trabalhar melhor."

O vídeo usa a técnica de **Ports and Adapters (Arquitetura Hexagonal)** para mostrar a diferença entre antes e depois de um refactor — com código real de um blog simples (users, posts, comments).

---

## O Problema: Código Espaguete (God Class)

### Estrutura típica do legado

Um único arquivo (`index.ts`) com uma única classe que faz absolutamente tudo:

- Inicializa banco de dados (em memória, nesse exemplo)
- Gerencia usuários, posts e comentários
- Valida e-mail no meio da lógica de roteamento
- Faz routing com uma cadeia de `if/else` baseada em método HTTP + path

```
if (method === 'GET' && path === '/users') { ... }
if (method === 'POST' && path === '/users') { ... }
if (method === 'GET' && path === '/posts') { ... }
if (method === 'DELETE' && path.startsWith('/users')) { ... }
// etc.
```

### Por que isso é problemático

- **Forte acoplamento:** mudar a estrutura interna de `User` quebra lógica de posts e de comments simultaneamente — três lugares afetados por uma única mudança
- **Sem extração possível:** a validação de e-mail é um loop inline, não uma função exportada. Para criar um novo endpoint que busca por e-mail, você duplica o código
- **Substituição impossível:** trocar o armazenamento de usuários para um serviço externo (ex: Clerk) exige reescrever tudo — não há onde "encaixar" uma nova implementação de forma limpa
- **Escala humana e de IA**: com 200 linhas, a IA entende bem. Com 20.000 linhas e quatro colaboradores, vira um problema real para humanos e modelos

---

## A Solução: Ports and Adapters

### Conceito

Separar a codebase em módulos com responsabilidades claras, conectados por **interfaces** (contratos) em vez de dependências diretas.

```
┌─────────────┐     interface     ┌─────────────┐
│   Users     │ ◄────────────── ► │   Posts     │
│             │                   │             │
│  adapter    │                   │  adapter    │
│  (impl)     │                   │  (impl)     │
└─────────────┘                   └─────────────┘
                                        ▲
                                   interface
                                        │
                                ┌─────────────┐
                                │  Comments   │
                                │             │
                                │  adapter    │
                                │  (impl)     │
                                └─────────────┘
```

- **Port (interface/repositório):** define o contrato — o que cada módulo pode fazer (`getAll`, `getUserById`, `findByEmail`, `create`, `delete`)
- **Adapter:** implementa o contrato — pode ser in-memory, PostgreSQL, API externa, outro microsserviço. Desde que implemente a interface, o resto da aplicação não sabe nem se importa

### Estrutura do projeto depois do refactor

```
src/
├── domain/          # tipos e regras de domínio (User, Post, Comment)
├── repositories/    # ports — as interfaces/contratos
│   ├── user.repository.ts
│   ├── post.repository.ts
│   └── comment.repository.ts
├── adapters/        # implementações concretas dos repositórios
│   ├── user.adapter.ts
│   ├── post.adapter.ts
│   └── comment.adapter.ts
├── services/        # regras de negócio (UserService, PostService, CommentService)
├── router/          # rotas baseadas nos services
└── index.ts         # instancia adapters e injeta nos services
```

### O que mudou no `index.ts`

Antes: god class de 238 linhas com tudo embutido.

Depois: apenas instanciação e injeção de dependências:

```typescript
const userRepository = new UserAdapter();
const postRepository = new PostAdapter();
const commentRepository = new CommentAdapter();

const userService = new UserService(userRepository);
const postService = new PostService(postRepository, userRepository);
const commentService = new CommentService(commentRepository, postRepository);
```

---

## Benefícios Concretos

### 1. Substituição limpa de implementação

Para migrar usuários para Clerk (serviço externo de autenticação):

```typescript
// Antes: reescrever tudo
// Depois: criar um novo adapter que implementa a mesma interface
class ClerkUserAdapter implements UserRepository {
  async getUserById(id: string) { /* chama Clerk API */ }
  async create(data: CreateUserDTO) { /* chama Clerk API */ }
  // ...
}

// No index.ts: trocar uma linha
const userRepository = new ClerkUserAdapter(); // era: new UserAdapter()
```

O resto da aplicação não muda nada.

### 2. Funções explícitas e reutilizáveis

O `findByEmail` que antes era um loop inline embutido no handler:

```typescript
// Antes (dentro do handler de POST /users):
const existing = users.find(u => u.email === body.email);

// Depois (método explícito no adapter):
async findByEmail(email: string): Promise<User | null> {
  return this.users.find(u => u.email === email) ?? null;
}
```

Agora é reutilizável por qualquer parte da aplicação.

### 3. Alterações localizadas

Mudar a estrutura interna de `User` afeta apenas:
- `user.adapter.ts` (implementação)
- `user.repository.ts` (contrato, se necessário)

Posts e comments não sabem nada sobre como User é armazenado internamente.

---

## Discussão: Service vs Domain para Regras de Negócio

O autor reconhece o debate: regras de negócio deveriam estar no domínio (DDD), não no service. Mas para uma codebase que estava muito ruim, um `UserService` com validação já é uma melhoria substancial:

```typescript
class UserService {
  async create(data: CreateUserDTO) {
    const existing = await this.userRepo.findByEmail(data.email);
    if (existing) throw new UserAlreadyExistsError(data.email);
    return this.userRepo.create(data);
  }
}
```

> "Eu não gosto de começar com uma função por arquivo e fazendo um negócio com muitos arquivos. Eu gosto de ir começando dessa maneira aqui e incrementando depois."

---

## Sobre Chamar Repositório vs Serviço em Dependências Cruzadas

No `PostService`, o autor usa `userRepository` diretamente (não `UserService`):

```typescript
class PostService {
  constructor(
    private postRepo: PostRepository,
    private userRepo: UserRepository // direto, não UserService
  ) {}

  async create(data: CreatePostDTO) {
    const user = await this.userRepo.getUserById(data.userId);
    if (!user) throw new UserNotFoundError(data.userId);
    return this.postRepo.create(data);
  }
}
```

**Argumento para chamar o repositório diretamente:** adequado para sistemas que não vão evoluir para microsserviços.

**Argumento para chamar o serviço:** se a evolução para microsserviços for esperada, chamar o `UserService` é melhor — evita que `PostService` saiba que existe um repositório de usuário.

---

## Por Que Isso Importa para IA

Uma codebase com ports and adapters:

- **Contexto menor por tarefa:** a IA precisa olhar apenas para o módulo relevante, não para 20.000 linhas de arquivo único
- **Intenção clara:** interfaces explícitas comunicam o que cada módulo pode fazer — a IA não precisa inferir de um `if/else` caótico
- **Alterações localizadas:** quando você pede para a IA alterar como usuários são criados, ela sabe exatamente onde mexer e o que não vai quebrar
- **Substituição sem medo:** pedir para a IA "trocar o adapter de in-memory para PostgreSQL" é uma tarefa bem delimitada; pedir para ela "trocar como usuários são armazenados" num arquivo de 20.000 linhas é uma catástrofe em potencial

> "Uma codebase boa legível para seres humanos também é uma codebase boa e legível para IAs."

---

## Quando NÃO Aplicar

Para MVPs pequenos (< 300 linhas, uma pessoa, sem planos de crescimento), a god class é perfeitamente adequada. O overhead de ports and adapters só compensa quando:

- O projeto vai crescer (mais features, mais colaboradores)
- Partes do sistema podem precisar ser substituídas
- A manutenção a longo prazo é uma preocupação real

---

## Termos-chave

- **Port:** interface/contrato que define as capacidades de um módulo
- **Adapter:** implementação concreta de um port — pode ser trocada sem quebrar o resto
- **God Class:** anti-pattern onde uma única classe faz absolutamente tudo
- **Forte acoplamento:** quando mudar uma parte quebra outras partes não relacionadas
- **Arquitetura Hexagonal:** nome alternativo para Ports and Adapters
