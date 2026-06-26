# Como Arquitetar com Cache e Redis

**Fonte:** Transcrição de vídeo (YouTube)
**Idioma original:** Português

---

## Introdução

No conteúdo de hoje vamos falar sobre como arquitetar usando cache, mais especificamente fazendo uso do Redis. Vamos desde o básico — o que é o Redis, para que serve, os pontos fortes, os fracos — para você tomar uma decisão acertada em relação a decidir se vai usar o Redis ou outro tipo de banco não relacional para o seu cache.

---

## O Que é um Banco NoSQL?

Redis é um dispositivo de armazenamento de dados, também conhecido como banco não relacional ou **NoSQL**.

Bancos NoSQL têm esse nome porque você não trabalha com as estruturas convencionais de dados: não há esquema, tabelas, colunas ou linhas — e também não há linguagem SQL. Cada banco NoSQL tem seus próprios comandos proprietários.

| Banco Relacional (SQL) | Banco NoSQL |
|---|---|
| PostgreSQL, Oracle, MySQL | Redis, MongoDB, Cassandra |
| Estrutura e consistência dos dados | Performance e velocidade |
| Escalabilidade **vertical** (mais CPU/RAM) | Escalabilidade **horizontal** (mais máquinas) |
| Normalização, sem redundâncias | Pode ter dados duplicados por estratégia |

---

## O Que é o Redis?

Redis é um banco NoSQL que trabalha no modelo **in-memory**: ele armazena tudo na memória RAM.

- Possui suporte a réplica em arquivos (para persistência após reinicialização), mas isso **não é garantido** — há periodicidade e o desempenho cai um pouco.
- É feito para ser rápido: leitura e gravação com latência mínima.
- É o tipo perfeito para **cache**, pois o objetivo do cache é encurtar o caminho entre a aplicação e os dados.

### Modelo chave-valor

Redis trabalha com o modelo **chave → valor**:

```
nome_da_chave   →   valor
```

A chave pode ser longa e semântica, como `saldo-cliente-123` ou `extrato-cliente-456`.

**Tipos de valor suportados:**

- `string`
- `hash` (permite estruturas como JSON)
- `list`
- `set`

A busca é feita pela chave (ex: `GET cod_cliente_*`), o que permite recuperar ou limpar grupos de registros por prefixo.

---

## Pontos Fortes do Redis

1. **Extremamente performático** — muito rápido, ideal quando performance e latência baixa são requisito.
2. **Muito conhecido e difundido** — ampla documentação e suporte na internet.
3. **Suporte em praticamente todas as linguagens de programação.**
4. **Suportado nativamente pelas grandes clouds** (AWS, GCP, Azure) como serviço gerenciado. Também pode ser instalado em container, local ou em servidor físico.
5. **Fácil de clusterizar** — escalar horizontalmente é simples, com bastante material disponível.

---

## Pontos Fracos do Redis

1. **Limitado à memória disponível** — 2 GB, 4 GB, 8 GB... depende do hardware. Não há armazenamento ilimitado.
2. **Não suporta SQL** — nenhum banco NoSQL suporta, mas é um ponto de atenção para quem está acostumado com `SELECT`, `INSERT`, `UPDATE`.
3. **Segurança limitada** — as permissões de acesso são estáticas. Quem tem acesso ao banco consegue ler e gravar todas as chaves do DB.
4. **Roda em um único CPU** — não importa quantos núcleos a máquina tenha, o Redis utiliza apenas um. A solução é **clusterizar** (múltiplas instâncias/containers).

---

## Arquitetando com Redis

### Exemplo 1 — Feature Toggles (Feature Flags)

Feature toggles são interruptores dentro do código — liga/desliga trechos de funcionalidade — usados para evitar branches e permitir Trunk-Based Development.

O problema: a aplicação precisa consultar os toggles com latência mínima, pois eles ficam no meio do fluxo de execução. Um banco relacional seria lento demais para isso.

**Arquitetura:**

```
[Tela de Gestão] → [Microsserviço de Manutenção] → [Banco SQL]
                                                         ↓
                                                    [Batch Job]
                                                         ↓
                                                      [Redis]
                                                         ↑
[Aplicação (front/back)] → [Microsserviço de Feature Toggle] ─┘
```

- A tela administrativa salva os toggles no banco SQL via microsserviço de manutenção.
- Um batch sincroniza os dados do SQL para o Redis.
- A aplicação consulta o microsserviço de feature toggle, que lê do Redis — resposta quase instantânea.

---

### Exemplo 2 — Padrão Flyweight com Cache

Ao invés de um batch, o próprio microsserviço popula o cache sob demanda:

```
Aplicação → Microsserviço → Redis (existe?) → retorna
                                  ↓ (não existe)
                              Banco SQL → grava no Redis → retorna
```

- Tenta buscar no Redis primeiro.
- Se não existir, busca no SQL, grava no Redis e retorna.
- Cada entrada no Redis recebe um **TTL (timeout)** — ex: 1 hora ou 1 dia — após o qual o dado é buscado novamente no SQL.

> Esse ciclo é análogo ao padrão de projetos **Flyweight**: construir objetos em memória de forma lazy e reutilizá-los enquanto forem válidos.

---

### Exemplo 3 — CQRS com Redis

Redis pode ser a camada de leitura em uma arquitetura **CQRS** (Command Query Responsibility Segregation):

```
[Camada de Domínio]
     ├── Gravação → [Banco SQL]  ← fonte de verdade
     └── Leitura  → [Redis]     ← cache otimizado para consultas
                        ↑
                  [Batch/Trigger de sincronismo]
```

- Gravações vão sempre para o SQL.
- Leituras vão para o Redis (mais rápido).
- Um processo de sincronismo mantém o Redis atualizado a partir do SQL.

---

## Quando Usar Cache (e Quando Não Usar)

**Use cache para dados com:**

- Alta frequência de leitura
- Baixa volatilidade (mudam raramente)

**Exemplos adequados:**

- Feature toggles
- Menus e permissões de usuário
- Saldo e extrato de clientes (atualiza só em transações)
- Tokens de sessão
- Chaves de configuração

**Tradeoffs ao adicionar cache:**

- Aumenta a **complexidade** da aplicação
- É necessário pensar em estratégia de **sincronização** entre cache e banco
- É mais uma tecnologia para manter, versionar e evoluir
- Não use cache para tudo — avalie os casos de uso com cuidado

---

## Resumo

| Aspecto | Redis |
|---|---|
| Tipo | NoSQL, in-memory, chave-valor |
| Velocidade | Muito alta |
| Persistência | Memória (réplica em arquivo opcional) |
| Escalabilidade | Horizontal (cluster) |
| CPU | Single-threaded (1 núcleo por instância) |
| Suporte cloud | AWS, GCP, Azure (nativo) |
| Caso de uso ideal | Cache, session store, feature flags, CQRS read layer |
