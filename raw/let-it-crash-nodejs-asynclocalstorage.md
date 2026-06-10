# Let It Crash — Graceful Shutdown com AsyncLocalStorage no Node.js

**Fonte:** Transcrição de vídeo (YouTube)  
**Autor:** Eric Lenda (canal de JavaScript/Node.js)  
**Data de publicação:** desconhecida  
**Idioma original:** Português (Brasil)

---

## Introdução

E se você não usasse mais blocos `try/catch` para validar erro de conexão de banco de dados, uma IA indisponível, ou exceções gerais de aplicação?

Nesse vídeo vou falar sobre a estratégia conhecida como **Let it Crash** — uma filosofia de design de sistemas onde o sistema é projetado para **quebrar** e uma nova cópia ser criada em resposta a certos tipos de erros, ao invés de tentar se recuperar de todos os erros possíveis.

---

## Contexto

Fiz um vídeo no canal falando sobre sistemas confiáveis em JavaScript e muita gente ficou em dúvida sobre como aplicar esse conceito na prática. O nome do conceito é literalmente: **deixa quebrar**.

Mas antes de deixar a aplicação quebrar, é necessário:

1. **Responder o usuário** que fez o pedido com feedback dizendo que o seu pedido falhou
2. **Cortar o canal de comunicação** para que novos usuários não façam pedidos
3. **Encerrar conexões externas** com bancos de dados
4. **Encerrar a aplicação**

Dessa forma, se o canal de comunicação foi fechado para o mundo externo, você tem a liberdade de criar novas cópias da sua aplicação e evitar que novos pedidos não sejam respondidos.

---

## Erro vs. Exceção

Para entender esse conceito, é importante entender a diferença entre um **erro** e uma **exceção**.

### Erros (domínio)

Comportamentos **previsíveis** e dentro do controle da aplicação:

- Validações de campos
- Tipos de dados inválidos
- Usuário inválido
- Produto inexistente

São erros de domínio — podem acontecer a qualquer momento. Você não precisa lançar uma exceção para isso.

### Exceções (fora do controle)

Comportamentos **imprevisíveis** e fora do seu controle:

- Sistema indisponível
- Falta de memória no servidor
- Sem conexão com a internet
- Conexão com banco de dados falhou

Se exceções acontecerem, **você não precisa se recuperar do erro**.

### Por que não tentar se recuperar?

É comum tentar se reconectar com um banco de dados se a conexão cair — fazer estratégias de retry e assim por diante. O problema é que mesmo fazendo retries, não necessariamente o problema se resolve, como por exemplo:

- Vazamento de memória
- Estouro de limite de conexões

Por isso, a estratégia *Let it Crash* é mais robusta nesses cenários.

---

## A Aplicação de Exemplo

Uma Web API em Node.js que:

1. Recebe um corpo em formato de texto
2. Converte para JSON
3. Insere no banco de dados (via Sequelize + PostgreSQL)
4. Responde ao cliente com sucesso

**Comportamento esperado em caso de falha (banco de dados fora do ar):**

1. Responde o usuário com um erro genérico
2. Encerra o canal de comunicação (nenhum outro usuário acessa)
3. Aguarda pedidos em andamento terminarem
4. Encerra conexões externas ativas
5. Encerra a aplicação

Tudo isso **sem usar `try/catch`**.

---

## O Desafio: Contexto Assíncrono

O problema central: com múltiplos usuários conectados simultaneamente, como identificar **qual cliente específico** gerou o erro e responder **somente para ele**?

A solução está em uma das APIs mais poderosas — e mais complexas — do Node.js:

> **`AsyncLocalStorage`**

Permite rastrear o contexto assíncrono de cada usuário individual sem comprometer a performance da aplicação.

---

## Implementação

### Handler da Requisição

```javascript
// handleRequest — sem try/catch
function handleRequest(req, res) {
  // Nota: texto inválido são erros de domínio — fora do escopo do Let it Crash
  const json = JSON.parse(req.body);
  
  Hero.create(json).then((result) => {
    res.json(result);
  });
}
```

### Rastreando o Contexto com AsyncLocalStorage

```javascript
import { AsyncLocalStorage } from 'async_hooks';

const storage = new AsyncLocalStorage();

// Ao receber a requisição, iniciamos um novo contexto
storage.run({ response: res, clientId: req.id }, () => {
  handleRequest(req, res);
});
```

A chavinha `{}` do `.run()` define um **novo contexto assíncrono**. Tudo que acontecer dentro dessa função terá acesso a esse contexto específico — `response` e `clientId` daquele cliente.

### Observando Erros Globais

```javascript
// Erros síncronos (throw)
process.on('uncaughtException', (error) => {
  const { response, clientId } = storage.getStore();

  console.log(`Erro do cliente ${clientId}:`, error);

  // 1. Responde o cliente que gerou o erro
  response.status(500).json({ message: 'Algo deu errado, seu pedido falhou.' });

  // 2. Fecha o servidor para novas conexões (aguarda pendentes terminarem)
  server.close(async () => {
    // 3. Encerra conexão com banco de dados
    await sequelize.close();

    // 4. Encerra o processo
    process.exit(1);
  });
});

// Erros assíncronos (Promise rejeitada)
process.on('unhandledRejection', (reason) => {
  const { response, clientId } = storage.getStore();

  console.log(`Rejeição do cliente ${clientId}:`, reason);

  response.status(500).json({ message: 'Algo deu errado, seu pedido falhou.' });

  server.close(async () => {
    await sequelize.close();
    process.exit(1);
  });
});
```

---

## Armadilha: `async` na função raiz do contexto

Uma pegadinha importante sobre contextos assíncronos:

```javascript
// ❌ NÃO funciona — o async externo quebra o rastreamento do AsyncLocalStorage
storage.run({ response: res }, async () => {
  await handleRequest(req, res);
});

// ✅ CORRETO — o async deve estar dentro da função de contexto
storage.run({ response: res }, () => {
  handleRequest(req, res); // handleRequest pode usar async/await internamente
});
```

Se o `async` for colocado na função passada para `.run()`, o Node.js não consegue rastrear o contexto assíncrono corretamente — e o `storage.getStore()` retorna `undefined` no handler de erro.

**Regra:** todo uso de `async/await`, Promises e callbacks deve acontecer *dentro* do `handleRequest`, não na função de contexto do `.run()`.

---

## Fluxo Completo com Orquestrador

```
Usuário → API Node.js
                │
           Banco de dados fora do ar
                │
         [unhandledRejection disparado]
                │
         1. Responde o cliente com erro
         2. server.close() — para novas conexões
         3. Aguarda requisições em andamento
         4. sequelize.close()
         5. process.exit(1)
                │
         Kubernetes / orquestrador detecta processo morto
                │
         Cria 3 novas cópias da aplicação
                │
         Novos pedidos respondidos normalmente
```

O orquestrador (Kubernetes, etc.) é inteligente o suficiente para detectar que a conexão HTTP foi encerrada e iniciar novas réplicas automaticamente.

---

## Resumo

| Conceito | Descrição |
|---|---|
| **Let it Crash** | Deixar a aplicação morrer de forma controlada ao invés de tentar recuperar exceções |
| **Erro de domínio** | Previsível, controlável — não lança exceção |
| **Exceção** | Imprevisível, fora do controle — *Let it Crash* |
| **`AsyncLocalStorage`** | API do Node.js para rastrear contexto assíncrono por cliente |
| **`uncaughtException`** | Captura `throw` síncronos globais |
| **`unhandledRejection`** | Captura Promises rejeitadas sem handler |
| **`server.close()`** | Para novas conexões mas aguarda as ativas terminarem |
| **Orquestrador** | Kubernetes ou equivalente — recria réplicas após o processo morrer |

---

## Links

- Código-fonte: disponível na descrição do vídeo original
- Vídeo anterior referenciado: "Sistemas Confiáveis em JavaScript"
