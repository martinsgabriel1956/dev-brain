# Escalabilidade: Vertical vs Horizontal — System Design

> Transcrição adaptada de vídeo sobre escalabilidade de sistemas — a arte de fazer seu app crescer de forma sustentável.

---

## O Problema

Seu app tem 100 usuários. Tudo funciona. Ele viraliza: 10.000 usuários — começa a travar. Chega a 100.000 — cai completamente.

É para isso que a **escalabilidade** serve: a arte de fazer seu sistema crescer de forma sustentável.

**Definição:** escalabilidade é a capacidade do sistema de lidar com mais carga — mais usuários, mais dados, mais requisições — sem que o usuário final perceba.

**O cenário ideal:** o sistema escala de forma linear. A carga dobrou → os recursos dobram → a performance se mantém. O mundo real nunca é assim: aparecem gargalos, contenção, limites físicos e de orçamento.

---

## As Duas Estratégias Fundamentais

### Escalabilidade Vertical

Pegar o servidor existente e deixá-lo mais potente: mais CPU, mais RAM, mais disco, mais rede.

**Vantagens:**

- **Simplicidade** — é só um servidor, sem complexidade de distribuição
- O código não precisa saber que existe mais de uma máquina
- Não muda arquitetura nem código

**Desvantagens:**

- **Custo não-linear** — um servidor com 2× a capacidade pode custar 3–4× o preço; 4× a capacidade pode custar 10× o preço
- **Teto físico** — o maior servidor do mundo ainda é só uma máquina; não existe RAM infinita, não existe CPU com 1000 cores
- **Single point of failure** — se o servidor cair, nenhum usuário acessa o app até ele reiniciar

---

### Escalabilidade Horizontal

Ao invés de um servidor potente, usar **vários servidores normais** distribuindo a carga entre eles.

**Exemplo:** 10.000 req/s → 10 servidores × 1.000 req/s cada. Precisa de mais? Adiciona mais servidores.

**Vantagens:**

- **Sem limite teórico** — servidores podem ser adicionados quase infinitamente
- **Custo linear e previsível** — 2× carga = 2× servidores = 2× o preço
- **Tolerância a falhas** — se um servidor cai, os outros continuam rodando

**Desvantagens:**

- **Complexidade** — precisa de Load Balancer, sincronização de dados, garantia de que qualquer servidor atende qualquer usuário
- Quando você distribui dados, entra o **Teorema CAP** (Consistência, Disponibilidade e Partições)

> **Resumo:** escalabilidade vertical é simples, mas limitada. Horizontal é praticamente ilimitada, mas complexa. A maioria dos grandes sistemas usa horizontal conforme a carga aumenta.

---

## Load Balancer

O maestro do sistema distribuído — decide qual servidor recebe cada requisição.

### Algoritmos de Roteamento

| Algoritmo | Comportamento |
|---|---|
| **Round Robin** | Alterna entre servidores em sequência (1 → 2 → 3 → 1 → ...) |
| **Least Connections** | Envia para o servidor com menos conexões ativas no momento |
| **IP Hash** | O mesmo IP sempre vai para o mesmo servidor |

### Health Checks

O Load Balancer fica "pingando" os servidores. Se um não responde → removido da lista. Quando volta → readicionado.

### Níveis de Operação

| Nível | Camada OSI | Como funciona | Trade-off |
|---|---|---|---|
| **L4** | Transporte | Enxerga só IP e porta; não abre o pacote | Rápido, mas sem contexto do protocolo |
| **L7** | Aplicação | Entende HTTP, roteia por URL, headers e cookies | Flexível, mas mais lento |

> Exemplo L7: rota `/api/*` → servidor de API; rota `/static/*` → servidor de arquivos estáticos.

**Ferramentas:** Nginx, HAProxy, AWS ALB/NLB, Cloudflare.

---

## Servidores Stateless

Para o Load Balancer funcionar bem, qualquer servidor precisa poder atender qualquer requisição.

### Servidor Stateful (problema)

Guarda a sessão do usuário em memória. Se o Load Balancer mandar a próxima requisição para outro servidor, é como se o usuário não estivesse logado — aquele servidor não tem a sessão na memória. Se o servidor cair, todas as sessões desaparecem.

**Solução paliativa: Sticky Sessions** — o Load Balancer sempre manda o mesmo usuário para o mesmo servidor. Funciona, mas perde o benefício de distribuição de carga.

### Servidor Stateless (solução)

O servidor não guarda nada em memória:

- **Sessão** → Redis ou outro cache externo
- **Arquivos** → S3 ou object storage
- **Dados** → banco de dados

O servidor vira descartável: pode cair e renascer sem perder nada.

**Resultado:** qualquer servidor atende qualquer requisição, o Load Balancer distribui livremente, escalar é só subir mais instâncias.

> **Regra de ouro:** se você quer escalar horizontalmente, seu servidor **precisa** ser stateless.

---

## As Três Camadas de um Sistema Web

### Camada Web (arquivos estáticos)

HTML, CSS, JavaScript, imagens.

**Solução:** **CDN** (Content Delivery Network) — rede de servidores espalhados pelo mundo com cópias do conteúdo. O usuário é roteado para o servidor mais próximo geograficamente.

- Usuário no Brasil → servidor em São Paulo
- Usuário no Japão → servidor em Tóquio

CDN escala bem porque é essencialmente um **cache global**.

### Camada de Aplicação (lógica de negócio)

APIs, processamento, regras de negócio.

- Escala horizontalmente com Load Balancer
- Deve ser stateless
- **Auto Scaling**: sobe instâncias automaticamente quando a carga aumenta; derruba quando cai (ex: Black Friday)

### Camada de Dados (banco de dados)

A mais complexa. Bancos são **stateful por natureza** — eles *são* o estado.

Duas estratégias principais:

| Estratégia | Como funciona |
|---|---|
| **Replicação** | Cópias do banco para leitura (read replicas) |
| **Sharding** | Divide os dados em múltiplos bancos independentes |

> **Atenção:** na maioria dos sistemas, o banco é o gargalo. A aplicação escala fácil; o banco, não. Por isso **cache é tão importante**: quanto menos você bater no banco, melhor.

---

## Quando Escalar?

### Métricas para acompanhar

- **Latência subindo** — requisições que levavam 100ms agora levam 500ms
- **CPU acima de 70%** consistentemente, sem folga para picos
- **Memória quase sempre no limite**, swap sendo usado
- **Fila de requisições crescendo** — chegando mais do que sendo processadas

### Abordagens

| Abordagem | Quando | Custo | Risco |
|---|---|---|---|
| **Reativa** | Esperar quase quebrar para consertar | Mais barato | Mais arriscado |
| **Preventiva** | Monitorar métricas e escalar antes do problema | Mais caro | Mais seguro |

**Ideal:** automatizar com Auto Scaling. Exemplo de regra:

- CPU > 70% por 5 minutos → adiciona servidor
- CPU < 30% por 10 minutos → remove servidor

---

## Regra Crítica: Identifique o Gargalo Antes de Escalar

- Não adianta adicionar servidores de aplicação se o banco está travando
- Não adianta otimizar código se o problema é rede
- Escalar não é desculpa para seu banco travar com 100 usuários

---

## Resumo — Decisões Práticas

1. **Comece vertical** — simples, funciona, barato no início. Só vá para horizontal quando o vertical não der mais conta ou custar demais.
2. **Faça a aplicação stateless desde o começo** — migrar depois vai ser muito mais difícil.
3. **Cache é seu melhor amigo** — antes de escalar, verifique se não dá para cachear.
4. **Banco de dados é o gargalo** — planeje cedo como vai escalar seus dados.
5. **Não escale prematuramente** — mas esteja arquiteturalmente pronto para quando precisar. Arquitetura boa é a que permite escalar sem reescrever tudo.
