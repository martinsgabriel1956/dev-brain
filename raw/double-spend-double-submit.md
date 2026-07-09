---
date: 2026-07-09
tags: [tech-mentor, backend, distributed-systems, idempotencia, double-spend, double-submit]
skill: tech-mentor-backend/references/idempotency-patterns
level: intermediario
source_type: video-transcript
---

# Double Spend / Double Submit

> Transcrição bruta de ASR (fala em bloco único, sem pontuação, com propaganda de patrocinador), reescrita como markdown estruturado por tópico. Já em português — sem necessidade de tradução.

## Contexto

Double spend (mais ligado a bancos e transações) e double submit (mais ligado a formulários) são, na prática, o mesmo problema, e felizmente compartilham a mesma família de soluções.

O request duplicado que chega ao servidor pode ter três origens:

1. **Bug** — um problema de rede, hardware de modem/roteador, ou falha no cliente que dispara dois `POST`s sem intenção de ninguém.
2. **Erro humano** — o usuário clica duas vezes rápido no botão de submit sem perceber.
3. **Abuso malicioso** — alguém tenta explorar o sistema de propósito: mandar vários requests simultâneos para comprar mais ingressos do que o permitido e revender, ou gastar o mesmo dinheiro duas vezes explorando uma falha do banco.

Em algum momento esse(s) request(s) chegam ao servidor e o resultado final pode chegar duplicado no banco de dados — por exemplo, duas compras armazenadas para uma única intenção de compra.

Não existe uma solução única: a melhor abordagem geralmente combina várias das soluções abaixo, aplicadas em camadas diferentes.

## Camada 1 — Frontend: bloquear o botão de submit

Se o usuário consegue clicar em "submit" duas vezes e o segundo clique dispara um novo request, o frontend está mal feito. Um frontend bem construído dá feedback tátil/visual imediato e impede o reenvio:

```jsx
const [isSubmitting, setIsSubmitting] = useState(false);

function handleSubmit(e) {
  if (isSubmitting) {
    e.preventDefault();
    return;
  }
  setIsSubmitting(true);
  // ... envia o request
}
```

Desabilitar o botão (ou trocar de tela) enquanto o request está em voo cobre o caso do usuário bem-intencionado que clicou duas vezes sem querer. **Não cobre o usuário malicioso**, que pode simplesmente copiar o request de rede e reenviá-lo via script (`curl`, etc.) quantas vezes quiser, ignorando completamente o frontend. Por isso essa camada sozinha nunca é suficiente — a validação real precisa estar no servidor e/ou no banco de dados. Se só um dos dois puder ser escolhido, o servidor é a opção preferida; o ideal é os dois.

## Camada 2 — Redirect após POST (Post/Redirect/Get)

Para usuários bem-intencionados, uma solução simples e padrão da web: depois do `POST`, o servidor responde com um redirect (303) para outra URL (ex.: uma página "obrigado").

```
POST /subscribe (email) → 303 See Other → GET /thank-you
```

Como o navegador não reenvia o `POST` original ao seguir o redirect, e a pessoa não está mais na página do formulário, fica difícil (embora não impossível em casos de bug) dar submit duplicado por acidente. Esse padrão já é familiar de UX real — cadastro em lista de e-mail costuma redirecionar para uma página de agradecimento.

**Limitação**: assim como o bloqueio de frontend, o redirect não impede um usuário malicioso, que não passa pelo navegador.

## Camada 3 — Idempotency Key no servidor

Aqui entra a solução "de verdade" para bloquear reenvios, incluindo os maliciosos.

### Quem gera a chave?

- **Frontend envia a chave** (ex.: header `X-Idempotency-Key`, um UUID): mais simples de implementar, mas um atacante pode simplesmente copiar o request e gerar uma chave diferente — não impede abuso deliberado.
- **Servidor gera a chave a partir dos campos submetidos**: mais robusto. A chave é um hash dos campos relevantes do request (ex.: nome, origem, destino, data/hora do voo) — se o mesmo conjunto de dados for reenviado, o hash é idêntico e o servidor identifica que é a mesma requisição.

### O que entra no hash?

Depende do domínio. Perguntas que ajudam a definir o escopo:

- Vale a pena incluir o valor monetário no hash? Se o frontend não deveria mandar o preço (por segurança), a chave não pode depender dele.
- A mesma compra pode ser legitimamente refeita depois (ex.: cancelei hoje, quero comprar de novo amanhã)? Nesse caso, o **horário/data do submit** também entra como parte do hash — assim a mesma compra em dias diferentes gera chaves diferentes.
- Dois Pix de R$ 5 para o mesmo destinatário em segundos de diferença provavelmente é duplicado; o mesmo valor um dia depois, provavelmente não é. Definir a janela de tempo que caracteriza duplicidade é uma decisão de negócio, não só técnica.

### Onde armazenar a chave

A chave **não pode viver em memória de um único servidor**. Aplicações web modernas costumam ter múltiplos servidores/instâncias (ou rodar em lambdas) — não há garantia de que o segundo `POST` caia na mesma instância que processou o primeiro. Se a chave ficar só em memória local, ela não serve para nada.

A chave precisa ficar num armazenamento compartilhado entre todas as instâncias — tipicamente **Redis** (ou solução equivalente gerenciada na cloud). Isso aumenta a complexidade de design do sistema, mas é inevitável para a solução funcionar de verdade.

### Dificuldades da idempotency key

- Complexidade adicional: exige um armazenamento compartilhado entre servidores.
- Definir a estratégia de "o que conta como duplicado" (quais campos entram no hash, qual a janela de tempo) é uma decisão nem sempre óbvia.
- Estratégia de expiração/invalidação das chaves: não dá para guardar chaves para sempre — é preciso um TTL e uma política de limpeza.

## Camada 4 — Unique Constraint no banco de dados

Para casos onde existe um campo que é, por definição de negócio, único, a solução mais definitiva é uma **constraint de unicidade no banco de dados**. Exemplo: cadastro em lista de e-mails — o campo `email` é `UNIQUE NOT NULL`. Mesmo que o servidor falhe em bloquear ambos os requests e tente criar duas entidades, o banco rejeita a segunda.

**Vantagem**: é a solução mais definitiva — o banco garante a unicidade independentemente do que acontece a montante.

**Limitação**: só funciona quando existe um campo (ou combinação de campos) que é genuinamente único por regra de negócio. Em uma transação bancária, por exemplo, não existe um campo "naturalmente único" — o que se usa ali, na prática, é a própria idempotency key armazenada como constraint única no banco (ex.: um ledger onde cada transação carrega sua chave de idempotência). Ou seja, as camadas de idempotency key e unique constraint acabam convergindo nesse caso.

## Como decidir o que usar em cada cenário

| Cenário | Solução recomendada |
|---|---|
| Cadastro em lista de e-mail | Redirect (PRG) + Unique Constraint no e-mail — idempotency key no servidor não compensa a complexidade aqui |
| Compra de passagem aérea / dados de passageiro | Redirect após a etapa de submissão dos dados; a etapa final de pagamento tem controles adicionais de segurança/anti-scalping |
| Transação bancária / Pix | Idempotency Key obrigatória, geralmente persistida como constraint única no ledger |
| Gestão de estoque / venda de ingressos com demanda alta | Idempotency Key importante — datasets de alta contenção onde duplicidade gera overselling |

Regra prática: quanto mais a duplicidade custa dinheiro ou gera inconsistência de estado real (estoque, saldo bancário, ingressos), mais vale investir em idempotency key no servidor. Quando a duplicidade é inócua e facilmente identificável (ex.: nome enviado duas vezes), redirect + unique constraint já é suficiente.

## Nota pessoal do autor

O autor relata ter visto esse problema pela primeira vez ainda júnior, na primeira empresa em que trabalhou com um sistema mais transacional que geria estoque. Um sênior próximo alertou: "você fez tudo certo, mas como a gente está gerindo estoque, precisamos prevenir que requests duplicados cheguem — isso precisa estar no servidor/serviço também." Desde então, o autor ficou atento a esse problema ao longo de toda a carreira, por ser muito comum.

## Ferramental (patrocínio, contexto tangencial)

O vídeo foi patrocinado pela Abacus AI — assinatura mensal com acesso a múltiplos modelos de IA (GPT, Claude Opus, Nano Banana), um agente autônomo (integração via Telegram, agendamento de tarefas, prototipagem) e uma IDE baseada em VS Code (Code LLM) com agente de código integrado, permitindo escolher o modelo (ex.: Claude Sonnet para tarefas mais baratas vs. Opus para tarefas mais caras) e gerar testes unitários/código com contexto adicional (ex.: incluir README como contexto). Não é conteúdo técnico central do vídeo — é o patrocínio.
