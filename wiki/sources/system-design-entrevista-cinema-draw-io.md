---
type: source
title: "System Design na Prática: Simulação de Entrevista com Reserva de Ingressos de Cinema (draw.io)"
aliases: ["entrevista system design cinema", "seatmap reserva 15 minutos", "system design ingressos de cinema"]
date_created: 2026-07-30
date_updated: 2026-07-30
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/system-design-entrevista-cinema-draw-io.md
source_url: ""
author: "João (Rocket City)"
date_published: ""
date_ingested: 2026-07-30
source_count: 0
tags: [system-design, entrevistas, arquitetura, carreira, redis, load-balancer, api-externa, consistencia]
skill: tech-mentor-system-design
status: stable
---

# System Design na Prática: Simulação de Entrevista com Reserva de Ingressos de Cinema (draw.io)

## TL;DR

Primeiro vídeo de uma série semanal do canal Rocket City, apresentado por João (3 anos trabalhando "pra gringa"). Diferente de outras fontes de system design já na wiki, que listam dicas ou descrevem o pipeline de entrevista em abstrato, esta é uma **demonstração ao vivo no draw.io**: o apresentador simula responder ao prompt "fazer um sistema de reserva de ingressos de cinema" desenhando a arquitetura passo a passo — client → load balancer → web server → MySQL (busca de filmes) → API externa de seatmap → API externa de pagamentos → Redis (reserva temporária de 15 minutos). O valor central da fonte não é o desenho em si (o autor mesmo o chama de "rascunho", "não é production ready"), mas o **processo**: como levantar requisitos via follow-up questions, como justificar cada peça, e principalmente uma auto-crítica explícita e rara nas fontes já ingeridas — o autor expõe um bug de consistência não resolvido no seu próprio desenho (assento aparece disponível via API externa mas já está reservado no Redis interno) e o discute em voz alta em vez de escondê-lo, ilustrando na prática a recomendação (já presente em [[wiki/concepts/entrevista-system-design]]) de que comunicação do raciocínio vale mais que a solução perfeita.

## Key Claims

- **Follow-up questions transformam um prompt vago em requisitos concretos**: a partir de "fazer um sistema de reserva de ingressos de cinema", o candidato levanta explicitamente: seatmap para escolha de assento, busca de filme por nome, compra com reserva de 15 minutos se o pagamento não for concluído, e acesso via web (mobile/desktop). → [[wiki/concepts/entrevista-system-design]]
- **Perguntar sobre login/autenticação de saída é uma tática de "ganhar tempo para pensar"**: o entrevistador tipicamente responde "pode assumir que tudo já está autenticado, não precisa desenhar" — o valor da pergunta não é a resposta em si, mas o tempo que ela abre para o candidato organizar as próximas perguntas.
- **Escalabilidade (RPS, usuários simultâneos, picos) é enquadrada como pergunta de senioridade mais alta, fora do escopo do exercício básico demonstrado** — o autor explicitamente não aprofunda estimativas de capacidade no rascunho, dizendo que esse tipo de pergunta "é mais para senioridades mais altas". Conecta diretamente com [[wiki/concepts/niveis-de-senioridade-system-design]] e [[wiki/concepts/estimativas-back-of-envelope]], que já documentam essa mesma gradação por nível a partir de outra fonte.
- **Load balancer é tratado como peça "de praxe" mesmo num desenho simples**: três web servers atrás de um load balancer, com a justificativa didática de que ele evita sobrecarregar uma instância já saturada, redirecionando por regras (ex.: uso de hardware) para outra instância. → [[wiki/concepts/load-balancer]]
- **Escolha de banco de dados justificada pela existência (ou não) de relação entre os dados**: MySQL para a tabela de filmes (id, nome, categoria) "por motivos didáticos", mas o autor afirma explicitamente que, numa entrevista real, veria que "filmes não têm relação com outra coisa" e poderia optar por um banco não relacional (MongoDB) para o mesmo dado. → [[wiki/concepts/modelagem-de-dados]]
- **APIs de domínio específico e de terceiros (seatmap, pagamentos) ficam fora do sistema principal**: seatmap não entra no web server porque lida com contexto próprio demais (salas físicas, disponibilidade) e porque poderia ser um produto white-label reaproveitado por outros vendedores de ingresso; pagamentos é externo porque APIs de pagamento maduras já resolvem escala e confiabilidade que o sistema não precisa reimplementar. → [[wiki/concepts/contrato-de-api]]
- **Endpoints citados explicitamente**: `/search` (GET, consulta MySQL por nome), `GET assentos` (consulta seatmap), `POST commit assento` (toggle de disponibilidade do assento). O autor reforça que numa entrevista real esses endpoints seriam detalhados com JSON de request/response — aqui ficam só nomeados. → [[wiki/concepts/contrato-de-api]]
- **Redis como mecanismo de reserva temporizada (TTL), não como cache de leitura tradicional**: guarda `seatmapId` + `seatId` com expiração automática em 15 minutos — a chave expira sozinha e libera o assento, implementando a regra de negócio "reserva por 15 minutos" sem job/cron externo. → [[wiki/concepts/redis]]
- **Bug de consistência assumido abertamente pelo autor**: como a API de seatmap não sabe da reserva interna (ela só conhece o estado "físico" do assento, não o estado transacional do sistema de vendas), um `GET assentos` pode retornar como disponível um assento que já está reservado no Redis. O sistema descobre isso só depois, ao verificar o Redis no momento da escolha — o usuário vê "disponível" no frontend e só ao tentar prosseguir descobre que já foi reservado por outra pessoa. O autor chama isso de "bem simplista", reconhece que "não é a melhor forma" e frisa que, numa entrevista real, isso seria resolvido em conversa com o entrevistador. → [[wiki/concepts/distributed-lock]]
- **Comunicação do raciocínio é apresentada como o verdadeiro objeto de avaliação, não o diagrama**: a recomendação explícita do vídeo é "deixar explícita" qualquer lógica não óbvia do sistema (como a consulta ao Redis) falando em voz alta com o entrevistador — eco direto da mesma conclusão de [[wiki/sources/anatomia-entrevista-system-design-bigtech]] e [[wiki/sources/5-dicas-entrevistas-lousa-branca-system-design]], já presentes na wiki.

## Entities

[[wiki/entities/joao-rocket-city]]

## Concepts

[[wiki/concepts/entrevista-system-design]] · [[wiki/concepts/load-balancer]] · [[wiki/concepts/modelagem-de-dados]] · [[wiki/concepts/contrato-de-api]] · [[wiki/concepts/redis]] · [[wiki/concepts/distributed-lock]] · [[wiki/concepts/high-level-design]] · [[wiki/concepts/estimativas-back-of-envelope]] · [[wiki/concepts/niveis-de-senioridade-system-design]]

## Conexão com outras fontes

Esta fonte complementa, em vez de repetir, as demais fontes de entrevista de system design já na wiki: [[wiki/sources/5-dicas-entrevistas-lousa-branca-system-design]] e [[wiki/sources/anatomia-entrevista-system-design-bigtech]] descrevem o *framework* da sessão em abstrato (requisitos → capacidade → modelagem → desenho); esta fonte é a primeira a mostrar esse framework sendo **executado ao vivo** num exemplo concreto (cinema, não URL shortener/social feed), com o rascunho real do candidato e seus erros preservados. A escala/RPS ficando fora de escopo por senioridade ecoa diretamente [[wiki/sources/system-design-por-nivel-junior-pleno-senior]]. O mecanismo de reserva via Redis com TTL é estruturalmente parecido com o `SET NX EX` de [[wiki/concepts/distributed-lock]] (caso Uber, já documentado), mas **não é a mesma coisa**: o desenho do vídeo não usa um lock atômico check-and-reserve — ele escreve no Redis só depois da escolha do usuário, e a leitura do seatmap não consulta o Redis antes de responder "disponível". É exatamente a ausência desse mecanismo atômico que gera o bug de consistência que o próprio autor reconhece — uma boa ilustração negativa (o que acontece quando falta o lock) para complementar o caso positivo (Uber) já presente na wiki.

## Open Questions

- **Skill `tech-mentor-system-design` carregada por analogia**: path local `/home/gabriel-martins/Documentos/skills/tech-mentor-system-design/` existe nesta máquina (diferente do path `/home/nemomartins/...` do CLAUDE.md) — `references/system-design.md` (framework de 4 etapas: clarify requirements, BOE, HLD, deep dive) usado para calibrar nomenclatura e confirmar que o fluxo demonstrado no vídeo é uma instância prática desse mesmo framework.
- **Correção arquitetural não resolvida pelo autor**: o vídeo não chega a propor uma solução para o bug de consistência seatmap/Redis (ex.: reservar atomicamente no Redis *antes* de expor o assento como disponível, ou o seatmap consultar o Redis como fonte adicional de verdade) — fica em aberto se a wiki deve registrar a correção como conteúdo `[external]` inferido ou deixar como está, já que a própria fonte trata isso como erro conhecido e não como recomendação.
- **"Rocket City" como canal**: já existe [[wiki/entities/eduarda-rocket-city]] na wiki como criadora de conteúdo do mesmo canal — este vídeo confirma que o canal tem múltiplos apresentadores. Criada entidade separada [[wiki/entities/joao-rocket-city]] para o apresentador João, sem fundir com Eduarda.

## Raw Quotes

> "A arquitetura de sistemas é a forma que os servidores se conectam."

> "Load balancer é uma forma de você não onerar, não deixar um servidor que já tá cheio de requisição com mais requisições."

> "Se eu tivesse numa entrevista e eu visse que filmes não têm relação com outra coisa, eu poderia criar um banco de dados não relacional."

> "Como é o nosso sistema interno que tá lidando com a reserva, tem que ter um mecanismo... eu não sei se é a melhor das formas, eu concordo que não é, mas quando você tá fazendo uma entrevista dessas de arquitetura é muita conversa."

> "Isso aqui eu não treinei antes, eu fiz da cabeça agora — baita rascunho, eu sei que tem bastante erro aqui, mas o foco aqui é a gente mostrar como que funcionaria uma entrevista de system design."
