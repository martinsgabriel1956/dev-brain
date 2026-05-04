# 5 Dicas para Elevar a Performance de Aplicações JavaScript

**Autor:** Erick Wendel (JavaScript Expert)
**Fonte:** Transcrição de vídeo (YouTube — playlist Performance JavaScript)
**Data de ingest:** 2026-05-01

---

## Contexto

Dicas que funcionam no mundo real para elevar a capacidade de aplicações JavaScript independente do ambiente (navegador, Node.js, etc.) — gastando menos recursos e entregando mais.

---

## Dica 1 — Não manipule listas grandes em memória

JavaScript usa um único event loop para processar código na grande maioria dos ambientes (web, Node.js). Manipulação de listas é um dos temas que mais compromete a capacidade de resposta.

**Anti-padrão:**
```
carregar lista inteira em memória
→ rodar for/map/filter
→ transformar e calcular todos os itens
→ retornar resultado
```

**Padrão correto:**
```
receber primeiro item
→ transformar + calcular
→ retornar resultado do item
→ ir pro próximo item (sem acumular em memória)
```

**O segredo:** trabalhar com dados **sob demanda** — processe, renderize e limpe a memória. Não acumule itens para trabalhar em lote.

### Ferramentas recomendadas

- **Web Streams** — parte da especificação JavaScript, funciona em qualquer ambiente que roda JS. Permite processar grandes volumes sem travar o event loop.
- **RxJS / Observables** — mesmo conceito de itens sob demanda, porém com curva de aprendizado maior.

> Exemplo prático: processar 10 GB de dados na web sem backend e sem travar a tela é possível com Web Streams.

---

## Dica 2 — Não trave a aplicação com código síncrono

**Regra prática:** procure nos seus projetos funções com sufixo `Sync`. Tudo que for `Sync` executa uma coisa por vez e bloqueia o event loop.

**Impacto em Node.js:**
```
10 clientes conectados
→ cliente 1 chama readFileSync
→ todos os outros 9 clientes aguardam
→ aplicação travada até o cliente 1 terminar
```

### O modelo correto

```
receber pedido
→ delegar para tarefa assíncrona
→ continuar respondendo outros usuários
→ quando tarefa terminar, entregar resposta ao cliente original
```

Não importa a ordem de chegada — quem devolver os dados primeiro responde ao respectivo cliente.

### Logs assíncronos

`console.log` é síncrono. Para logs em produção, use **Pino** — trabalha de forma assíncrona e usa multithreads para entregar logs em segundo plano.

> O maior problema de JavaScript não é a linguagem — é programadores que não estudam a fundo o event loop.

---

## Dica 3 — Prefira arquitetura assíncrona (não só código)

**Caso real:** cliente gastava muito com VMs de alto CPU/memória para processar arquivos CSV. O fluxo era:

```
cliente envia CSV
→ backend processa (síncrono, bloqueante)
→ backend responde "ok, processado"
```

**Solução assíncrona:**

```
cliente envia CSV
→ backend salva o arquivo
→ backend responde imediatamente: "estou processando, te aviso"
→ cliente fica livre para outras ações
→ outro processo lê, valida e processa o CSV em background
→ notifica o cliente via e-mail ou notificação na aplicação
```

### Benefícios

- Recursos dedicados separados por responsabilidade (API vs processamento)
- Menor custo de infraestrutura
- Maior capacidade de resposta
- Isolamento de falhas

> JavaScript foi feito para programação assíncrona. Sua arquitetura pode se beneficiar muito ao dividir o problema em processos menores.

---

## Dica 4 — Monitore e melhore

Não esperar um problema grave para começar a monitorar. Aplicações são imprevisíveis.

### O mínimo de visibilidade necessário

- **Métricas:** requests mais lentos, endpoints mais acessados, relação erros/sucesso
- **Tracing:** identificar gargalos no código e em iterações externas (queries de banco)
- **Alertas:** ser notificado antes do usuário perceber o problema

### Ferramenta recomendada

**OpenTelemetry** (open source) — sobe em container Docker, recebe dados das aplicações, monitora tudo. Funciona como camada de observabilidade agnóstica de vendor.

---

## Dica 5 — Testes automatizados + testes de carga

Testes automatizados não são só sobre qualidade — são sobre capacidade.

### Por que a combinação funciona

```
testes automatizados
→ validam comportamento esperado
→ permitem plugar ferramenta de carga
→ simulam N usuários virtuais simultâneos
→ monitoramento aponta gargalos (dica 4)
→ você sabe ANTES do incidente se vai aguentar
```

### Stack recomendada

| Ferramenta | Papel |
|---|---|
| **Playwright** | Testes end-to-end (automatiza ações do usuário) |
| **Artillery** | Testes de carga (simula N usuários virtuais) |
| **OpenTelemetry** | Observabilidade durante os testes |

> Antes da Black Friday: rode a bateria com usuários clicando em botões, preenchendo formulários, fazendo compras — e descubra se vai aguentar ou dar ruim.

---

## Resumo das Dicas

| # | Dica | Conceito central |
|---|---|---|
| 1 | Não manipule listas grandes em memória | Processamento sob demanda / Web Streams |
| 2 | Não trave com código síncrono | Event loop / async/await / Pino |
| 3 | Prefira arquitetura assíncrona | Background processing / notificação |
| 4 | Monitore e melhore | Observabilidade / OpenTelemetry |
| 5 | Testes automatizados + carga | Playwright + Artillery |

---

## Referências

- Web Streams API (especificação JavaScript)
- RxJS / Observables
- Pino — logger assíncrono para Node.js
- OpenTelemetry — observabilidade open source
- Playwright — testes E2E
- Artillery — testes de carga
