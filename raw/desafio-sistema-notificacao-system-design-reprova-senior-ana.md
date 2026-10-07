# O desafio simples de System Design que reprova Dev Sênior (sistema de notificação)

> Transcrição de vídeo (autora: "Ana", canal de System Design; sobrenome/canal exatos não confirmados na transcrição). Já em português; sem tradução. Erros de ASR corrigidos (ex.: "Cáfica" → Kafka, "FCM/APNs", "Twilio", "Resend", "reconciliation", "idempotency key", "cost-aware"). Patrocínio da Locaweb Cloud (cupom, CFounder) e pedidos de like/inscrição omitidos.

## Tese
Um exercício aparentemente simples (sistema de notificação) reprova seniores não por falta de conteúdo, mas por hábito: o sênior "se desespera por saber demais" e pula etapas. O problema é "enganosamente fácil".

## Enunciado
Projete um sistema de notificação que permite a serviços internos (pedidos, fraude, marketing) enviar notificações ao usuário final por e-mail, SMS e push.

## Erro 1: começar pela API
Candidato real (mock interview) começou com `/v1/notifications/...` e `channel ID`, sem `user ID` nem prioridade. É "progresso falso": tem código e rota, parece avanço. A API é consequência de decisões arquiteturais, não ponto de partida. Ele gastou ~15 dos 45 minutos nisso e não fez perguntas. Dica: imagine um brainstorm com colegas; falar de endpoint antes de escalar o sistema atropela o time.

## Ordem correta
1. Requisitos (ler funcionais e não funcionais junto com o entrevistador; não precisa escrever ponto a ponto).
2. Entidades (máx. ~3 minutos).
3. Arquitetura de alto nível (client → server → backend → infra).
4. API, só se sobrar tempo.

## Requisitos: perguntas que importam
- Um serviço manda para um canal só ou vários? (vários → faz sentido mensageria)
- O usuário pode dar opt-out por canal/tipo ("nunca me mande SMS")?
- Templates: reutilizáveis, compartilhados entre times, com variáveis.
- Prioridade: se o usuário aceita os três canais, chegam juntos ou com ordem?
- A palavra **custo** no enunciado: o sistema precisa ser *cost-aware*. Em toda entrevista de system design, custo estará em jogo. SMS custa entre 10 e 500 vezes mais que push ou e-mail; em 10 milhões de notificações/dia, só SMS seria algo entre US$ 5 e 25 mil por dia (valores ditos no vídeo).
- Volume: ~10 milhões/dia, mas não uniforme: picos de campanha (Black Friday).

## Entidades
User, Notification, Channel, Template, **UserPreference** (preferências), **DeliveryAttempt** (cada tentativa de envio por canal, com estado). Sem UserPreference e DeliveryAttempt como entidades de primeira classe é impossível desenhar rate limit, fallback de canal ou rastrear status depois. Duas entidades mostram se a pessoa entendeu o problema ou só decorou o desenho "fila + workers".

## Desenho
- Serviços internos (order, fraud, marketing, Salesforce) → **API de ingestão**: valida payload, checa **idempotency key** (chave no Redis com TTL), checa preferências do usuário, aplica rate limit.
- **Kafka com três tópicos por prioridade**: crítico, normal, baixa prioridade.
- **Channel router** (pode ser uma classe/facade na aplicação): decide com base em prioridade + preferência + custo.
- Workers separados: push (FCM/APNs), e-mail (Resend), SMS (Twilio).
- **Delivery callback** assíncrono (webhook dos provedores) → salva status.
- **Job de reconciliação**: reprocessa falhas, escala de canal se for crítico e sem confirmação.
- O desenho não precisa ser perfeito; versões de API (v1/v2) não são o ponto.

## Os três pontos para levar
1. **Três tópicos separados por prioridade.** Uma fila só: campanha de marketing para 500 mil–1 milhão de usuários pode deixar um código de autenticação (crítico) preso atrás e chegar atrasado. Separar por infraestrutura (não "resolver no código do consumidor") distingue quem já operou isso em produção.
2. **Channel router centraliza o fallback e a lógica de custo**: push primeiro (grátis), depois e-mail (mais barato), SMS por último (mais caro), reservado para quando os outros falham. Resolve o requisito *cost-aware*.
3. **Confirmação de entrega de push não é confiável**: não há garantia de que FCM/APNs entregaram. Para notificação crítica, não confiar cegamente em "enviado": exige timeout + job de reconciliação.

## Por que reprova (as três dificuldades, nenhuma é "saber o padrão")
1. Resistir ao impulso de mostrar progresso visível cedo demais.
2. Puxar informação que não veio de graça no enunciado: perceber que "cost-aware" muda a arquitetura inteira, não é adjetivo bonito.
3. Pensar em modo de falha antes de ser perguntado (ex.: lembrar sozinho que a confirmação de push não é confiável).

## Checklist mental
- Perguntou sobre a palavra "custo"?
- Criou `User`, `UserPreference` e `DeliveryAttempt` como entidades (não ficou só em "system")?
- Isolou prioridade no nível de infraestrutura (filas separadas) ou deixou para o código?
- Desenhou a arquitetura antes de (ou em vez de) a API?

## Fecha
Praticar de verdade (implementar um sistema de notificação) dá domínio; desenhar bonito não. A autora usa este caso para treinar e avaliar candidatos em mentorias.
