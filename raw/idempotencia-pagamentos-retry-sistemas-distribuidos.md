---
date: 2026-07-27
tags: [tech-mentor, backend, distributed-systems, idempotencia, pagamentos, retry, webhook, outbox]
skill: tech-mentor-backend/references/idempotency-patterns
level: intermediario
source_type: video-transcript
---

# Idempotência em Pagamentos: Retry, Sistemas Distribuídos e Chaves de Idempotência

> Transcrição bruta de ASR (fala em bloco único, sem pontuação, com CTA de aula grátis no meio), reescrita como markdown estruturado por tópico. Já em português — sem necessidade de tradução.

## O Problema: Cobrança Duplicada

Você clica em pagar uma vez. O celular manda a requisição. A resposta se perde. O app tenta de novo. Se o backend processa as duas tentativas, R$ 500 viram R$ 1.000 cobrados. O mecanismo que evita essa cobrança duplicada se chama **idempotência**.

Um timeout só diz que o cliente não recebeu uma resposta a tempo. A cobrança pode ter:

1. Falhado antes de chegar no servidor.
2. Estar em andamento.
3. Ter sido aprovada, e só a resposta foi perdida no caminho.

O app não consegue diferenciar esses três casos olhando só para o relógio — por isso ele vai tentar de novo.

## Retries São Inevitáveis em Sistemas Distribuídos

Retries fazem parte de sistemas distribuídos porque problemas acontecem: conexões caem, processos reiniciam, etc. Filas também podem entregar a mesma mensagem mais de uma vez. Repetir a entrega, porém, também pode repetir a cobrança — e é justamente quando a repetição é necessária (para tolerar falha) que o sistema precisa garantir que o *efeito* não se repita. Nesse caso, o efeito indesejado seria o pagamento duplicado.

Para isso, o backend precisa reconhecer que aquelas tentativas representam a **mesma intenção**.

## O Que É Idempotência

Quando uma operação é idempotente, executá-la mais de uma vez deixa o sistema com o mesmo efeito de negócio da primeira execução. No caso do pagamento: três tentativas com a mesma identidade continuam representando uma única cobrança.

Isso não exige que todos os detalhes técnicos da resposta sejam idênticos entre as tentativas — uma tentativa pode responder `201`, outra pode devolver a resposta que ficou salva — mas o saldo e o número de cobranças precisam continuar iguais.

### Métodos HTTP e Idempotência

Alguns métodos HTTP já carregam semântica idempotente por definição:

- `GET` — ler o mesmo recurso não deveria criar um novo efeito.
- `DELETE` — repetir a remoção continua removendo o recurso (ou constatando que ele já não existe).

Muitos produtos financeiros, porém, criam recursos com `POST`. `POST` pode ganhar idempotência quando o contrato da API inclui uma identidade estável para a intenção — e essa identidade costuma vir de uma **chave de idempotência**.

## Como o Cliente Deve Gerar e Usar a Chave

A proteção começa no cliente, que é quem conhece a intenção do usuário:

1. Na primeira linha do fluxo, o cliente cria um identificador único **antes** de iniciar as tentativas.
2. O bloco de retry manda a **mesma chave** em todas as chamadas subsequentes.

Se o código gerasse uma chave nova a cada tentativa, o servidor enxergaria três operações diferentes. Por isso o cliente precisa guardar a chave até receber um resultado definitivo — ou entregar a recuperação do fluxo para outro processo que também conheça essa chave.

### Uma Intenção, Uma Chave

Duas ações intencionais distintas precisam de duas chaves diferentes. O valor e o destinatário podem ser iguais — uma pessoa pode legitimamente fazer duas transferências de R$ 100 para a mesma conta. Deduplicar só pelo *conteúdo* apagaria uma operação válida. A chave identifica a **intenção**, enquanto o servidor decide como registrar e proteger essa identidade.

## O Que o Backend Precisa Guardar

Se o sistema é distribuído (múltiplas instâncias podem receber o retry), o backend precisa guardar a chave num **armazenamento compartilhado** entre todas as instâncias — não em memória local de um único processo.

No exemplo do vídeo, a chave fica associada à conta autenticada e à operação que ela pediu. Esse escopo evita que a chave de um cliente bloqueie por acidente a operação de outro cliente.

O registro da chave carrega, no mínimo:

| Campo | Papel |
|---|---|
| **Chave de idempotência** | Identidade estável da intenção |
| **Request hash** | Conteúdo relevante da requisição — detecta reuso da mesma chave com valor/destinatário diferente |
| **Status** | Se a operação está processando ou já terminou |
| **Resposta salva** | Permite devolver o mesmo resultado sem reexecutar a regra de negócio |

### Regras de Decisão do Servidor

- Chave igual **e** hash igual **e** operação terminou → servidor devolve o resultado salvo.
- Chave igual **e** conteúdo mudou → servidor rejeita a chamada, porque aquela identidade já pertence a outra intenção.
- Chave igual e a primeira tentativa ainda está rodando → servidor pode esperar um pouco ou informar que o processamento continua.

## A Corrida: Por Que "Select Depois Insert" Não Basta

Comparar e depois inserir em duas etapas soltas (um `SELECT` seguido de um `INSERT`) deixa uma brecha quando duas tentativas chegam ao mesmo tempo: as duas requisições podem consultar simultaneamente, descobrir que a chave ainda não existe, e as duas começarem a processar a cobrança. Por isso a disputa pela chave precisa acontecer de forma **atômica**.

A chave primária (ou uma constraint de unicidade) deixa o **banco** escolher a vencedora:

- Se o `INSERT` criou a linha, aquela requisição "ganhou" o direito de processar.
- Se nenhuma linha foi criada, outra tentativa já registrou a mesma intenção, e essa requisição deve consultar o estado existente em vez de processar de novo.

Uma transação com lock pode proteger as mudanças locais que acompanham essa decisão. Quando o efeito financeiro mora no mesmo banco, o lançamento contábil e a mudança de status para `completed`, por exemplo, devem confirmar na **mesma transação** — assim o banco nunca deixa uma chave concluída sem um lançamento correspondente, nem um lançamento confirmado com a chave ainda aberta.

## Idempotência ≠ Transação — Problemas Diferentes

A transação impede que a transferência fique pela metade. A idempotência impede que a transferência inteira aconteça duas vezes. Produtos financeiros geralmente precisam das **duas** proteções no mesmo fluxo — uma não substitui a outra.

## Idempotência do Lado do Consumidor: Webhooks

Mesmo quando a API funciona corretamente, outra repetição pode aparecer depois, no webhook. Provedores e filas podem entregar o mesmo evento mais de uma vez — isso acontece quando o receptor processa o evento, mas a confirmação de recebimento se perde por algum motivo. O provedor vê a chamada como pendente e entrega de novo.

Por isso o consumidor também precisa ser idempotente. Uma **inbox persistente** pode guardar a combinação `provedor + event ID`:

1. O primeiro evento cria o registro e aplica a mudança (ex.: crédito na fatura).
2. As próximas entregas encontram o mesmo registro, não aplicam outro crédito, e ainda respondem sucesso ao provedor — encerrando o retry do lado dele.

Essa proteção é importante em baixa de boleto, liquidação de cartão, recarga de carteira e conciliação.

## Cruzando a Fronteira Entre Sistemas

A parte mais difícil é quando a operação cruza mais de um sistema e o processo cai no meio — esse é o intervalo que mais testa a arquitetura. Exemplo: o processador de pagamento aprovou a cobrança, mas o backend caiu antes de salvar a resposta local. Quando o retry chegar, o registro `processing` sozinho não prova se o efeito externo aconteceu.

Por isso a mesma identidade precisa atravessar a fronteira entre serviços: sempre que o serviço seguinte aceita uma chave idempotente, o backend envia "cobrar 842" e o processador responde com a cobrança que já tinha aprovado, em vez de criar uma segunda cobrança. Se o serviço externo não oferece essa proteção, o produto precisa de uma referência estável para consultar e reconciliar o resultado antes de tentar criar outro efeito.

- Uma **Outbox** ajuda a publicar o trabalho que nasceu numa transação local.
- Uma **Inbox** ajuda o próximo serviço a consumir mensagens repetidas sem duplicar o efeito.

Assim cada fronteira de serviço mantém a identidade da operação mesmo com entrega **pelo menos uma vez** (at-least-once). O objetivo, na prática, é produzir um efeito financeiro único mesmo quando a infraestrutura entrega a intenção várias vezes.

## A Mesma Arquitetura, Identidades de Negócio Diferentes

Essa arquitetura se repete em outros produtos, mas cada um escolhe uma identidade de negócio diferente para a chave:

| Produto | Identidade de negócio |
|---|---|
| Carteira digital | Um **saque ID** impede que o mesmo pedido de saque debite o saldo duas vezes |
| Emissão de boleto | Um **emissão ID** devolve o título já criado em vez de gerar outro documento para o mesmo faturamento |
| Liberação de empréstimo | Um **crédito ID** liga o contrato ao único crédito que deve entrar na conta |
| Corretora | Um **client order ID** recupera a ordem que já chegou à mesa de execução |

Cancelar ou substituir uma ordem numa corretora cria uma **nova** intenção, com outra identidade e outras regras — não reaproveita a chave da ordem original.

## Retenção da Chave (TTL)

O tempo de retenção da chave depende do produto:

- Apagar cedo demais pode deixar um retry tardio repetir o mesmo efeito.
- Guardar tudo para sempre aumenta o custo e complica a operação.

A janela precisa cobrir o tempo real de retry e processamento, e também precisa incluir webhooks e a conciliação daquele fluxo.

## Testando a Garantia em Produção

Antes de confiar nisso em produção, falta ver se o sistema aguenta as falhas que o desenho promete absorver. Desabilitar o botão depois do clique melhora a experiência, mas **não protege o backend**: o usuário pode abrir duas abas, a biblioteca HTTP pode repetir a chamada, um worker pode reiniciar depois de já ter concluído o efeito. Por isso a garantia precisa morar perto da regra de negócio e do armazenamento que registra o efeito — não na UI.

O teste mais útil corta a resposta depois que o efeito acontece e antes que o cliente receba a confirmação — simulando exatamente a janela de incerteza descrita no início. Também vale testar:

- Disparar duas requisições simultâneas com a mesma chave.
- Duplicar a entrega do webhook.
- Reiniciar o worker no ponto mais crítico do processamento.

### O Que Observar em Produção

- Taxa de chaves repetidas e conflitos de payload — mostra se o cliente está usando o contrato de idempotência corretamente.
- Operações presas em `processing` e reconciliações pendentes — mostra onde o fluxo ainda não conseguiu fechar o resultado.

## Conclusão

Sistemas confiáveis assumem que a tentativa vai acontecer de novo, e dão uma identidade estável para o efeito que só pode acontecer uma vez.
