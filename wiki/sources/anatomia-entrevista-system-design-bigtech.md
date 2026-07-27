---
type: source
title: "O que o Entrevistador Está Pescando numa Entrevista de System Design (Padrão BigTech)"
aliases: ["anatomia entrevista system design", "padrão bigtech system design", "o que o entrevistador procura"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/anatomia-entrevista-system-design-bigtech.md
source_url: ""
author: "Augusto Galego (inferido)"
date_published: ""
date_ingested: 2026-07-27
source_count: 0
tags: [system-design, entrevistas, carreira, arquitetura, bigtech, requisitos, cap-theorem]
skill: tech-mentor-system-design
status: stable
---

# O que o Entrevistador Está Pescando numa Entrevista de System Design (Padrão BigTech)

## TL;DR

Vídeo (autoria inferida: Augusto Galego, ver Open Questions) descrevendo o pipeline completo de entrevistas em empresas que seguem o "padrão bigtech" (RH → técnica/questionário → LeetCode/take-home → system design → fit com equipe) e detalhando, etapa por etapa, o que o entrevistador de system design está de fato avaliando: não é decorar caixinhas e setas, é a **compreensão do problema** — do levantamento de requisitos funcionais/não funcionais, passando por back-of-envelope estimations, design de API, esquema híbrido SQL+NoSQL, arquitetura de alto nível, até a discussão de tradeoffs e escala sob pressão de tempo. Fecha com a tese de que, acima de tudo, a entrevista é sobre comunicação: expor o raciocínio em voz alta, não só tê-lo na cabeça.

## Key Claims

- **Pipeline padrão bigtech de 5 etapas**: entrevista de RH → entrevista técnica/questionário → teste LeetCode ou take-home → entrevista de system design → reunião final de fit com engineering manager/equipe. Autor argumenta que preparar-se para o padrão mais difícil (bigtech) cobre automaticamente entrevistas menos exigentes. → [[wiki/concepts/entrevista-system-design]]
- **"Garbage in, garbage out" aplicado a entrevista**: a solução só pode ser tão boa quanto a compreensão do problema — por isso entender o problema vago e levantar requisitos pontualmente pesa mais na avaliação do que desenhar componentes de arquitetura precocemente.
- **Requisitos funcionais antes dos não funcionais**: funcionais definem como o negócio funciona (regras, features, limites); não funcionais definem latência, disponibilidade, retenção e volume — e são o que de fato separa uma solução de brinquedo (VPS de R$ 20 para 1.000 usuários) de uma solução de bigtech (milhões de usuários distribuídos globalmente). → [[wiki/concepts/estimativas-back-of-envelope]]
- **BOE (back-of-envelope) mede noção de escala, não precisão**: requests/segundo, volume de dados armazenados e banda necessária são as três perguntas centrais; o objetivo é saber se a solução "de VPS de R$ 20" ainda serve ou se é preciso cache/replicação/particionamento. → [[wiki/concepts/estimativas-back-of-envelope]]
- **Design de API revela conhecimento do domínio real**: exemplo trivial (encurtador de URL: `POST /urls` com `longUrl` → `shortUrl`) vs. exemplo não trivial (upload de vídeo longo exige multipart upload, autenticação e presigned URL — um `POST` com binário no corpo "não funciona"). → [[wiki/concepts/contrato-de-api]]
- **Esquema híbrido SQL + NoSQL é o padrão esperado em sistemas grandes**: parte transacional (consistência forte) em SQL, parte de alto throughput/dados menos estruturados em NoSQL — com colunas SQL apontando para chaves em stores NoSQL (ex.: DynamoDB) ou para objetos em blob store (ex.: S3). → [[wiki/concepts/modelagem-de-dados]]
- **A arquitetura de alto nível (HLD) é o "vocabulário" da entrevista, mas também pode expor decoreba**: entrevistador tenta distinguir quem só memorizou os nomes das peças (load balancer, CDN, API gateway, cache, filas, workers, blob store) de quem já usou essas peças de verdade — citar experiência concreta ("já usei X para resolver Y") é sinal de domínio real, não decorado. → [[wiki/concepts/high-level-design]]
- **Pressão de tempo no fim da sessão força a discussão de tradeoffs e escala**: perguntas do tipo "e se o banco cair?" ou "como resolver o gargalo?" levam a falar de monolito vs. microsserviço, síncrono vs. assíncrono, teorema de CAP, e a identificar bottlenecks — nenhuma escolha em computação vem sem custo. → [[wiki/concepts/cap-theorem]]
- **SQL tem tradeoff notório em escrita**: sistemas de throughput muito alto preferem NoSQL e abrem mão de garantias ACID por causa disso — conectando diretamente ao tradeoff SQL vs. NoSQL já documentado na wiki. → [[wiki/concepts/db-sharding]]
- **Consistência é negociável conforme o domínio, não um absoluto técnico**: transação bancária não abre mão de consistência forte; contador de likes de vídeo pode aceitar garantia BASE (301 vs. 302 exibido não faz diferença prática) — a compreensão do problema é o que define essa fronteira, ligando diretamente ao teorema de CAP. → [[wiki/concepts/cap-theorem]]
- **Glossário PT/EN como parte da preparação**: gargalo → *bottleneck*, vazão de banco → *throughput*, problema N+1, *celebrity problem* — justificativa explícita de que a área é nativa do inglês e a maioria estuda system design mirando entrevista em inglês.
- **Comunicação é o eixo central, acima de qualquer padrão técnico**: raciocínio claro só vale se for exposto em voz alta — fazer perguntas de verificação ("faz sentido isso?") durante a sessão é recomendação explícita, ecoando o mesmo princípio já documentado em outras fontes de entrevista técnica. → [[wiki/concepts/entrevista-tecnica-coding]]

## Entities

[[wiki/entities/augusto-galego]]

## Concepts

[[wiki/concepts/entrevista-system-design]] · [[wiki/concepts/estimativas-back-of-envelope]] · [[wiki/concepts/high-level-design]] · [[wiki/concepts/cap-theorem]] · [[wiki/concepts/modelagem-de-dados]] · [[wiki/concepts/contrato-de-api]] · [[wiki/concepts/db-sharding]] · [[wiki/concepts/entrevista-tecnica-coding]] · [[wiki/concepts/niveis-de-senioridade-system-design]]

## Conexão com outras fontes

Esta fonte é o par estrutural de [[wiki/sources/5-dicas-entrevistas-lousa-branca-system-design]] (Wesley Willians/Full Cycle) — ambas descrevem a mesma sequência de sessão (requisitos → capacidade → API/esquema → desenho → tradeoffs), mas esta detalha mais a fundo o *porquê* de cada etapa existir do ponto de vista do entrevistador ("o que ele tá pescando"), em vez de apenas listar o "como fazer". Também complementa diretamente [[wiki/sources/system-design-por-nivel-junior-pleno-senior]]: aquela fonte (mesmo autor inferido) mapeia como a profundidade cobrada nessas mesmas etapas varia por nível de senioridade; esta detalha o conteúdo de cada etapa em si, sem segmentar por nível. O exemplo de consistência negociável (likes de vídeo) e a fronteira SQL/NoSQL conectam diretamente com [[wiki/concepts/cap-theorem]] e [[wiki/concepts/db-sharding]] já estabelecidos na wiki a partir de fontes anteriores.

## Open Questions

- **Autoria inferida, não confirmada**: a transcrição fornecida não contém o nome do autor/canal. A inferência para Augusto Galego se baseia na coincidência textual com [[wiki/entities/augusto-galego]] já documentado na wiki: mesma trajetória (~12 anos de experiência, hiperfoco recente em system design), mesmo curso pago próprio "mais de um ano de produção", mesma política de reembolso integral em um mês sem perguntas, e o mesmo bloco patrocinado de terceiros ("UVP", escola de investimentos) no início do vídeo — já removido do `raw/` por não ser conteúdo técnico, seguindo o mesmo critério aplicado em ingestões anteriores. Se a inferência estiver errada, esta fonte e a entidade precisam ser corrigidas.
- Assim como na fonte irmã sobre níveis de senioridade, o vídeo termina com pitch do próprio curso pago — o conteúdo técnico é consistente com o canal gratuito, mas o enquadramento de "o que o entrevistador quer" pode estar calibrado para tornar o curso relevante.
- Não é possível confirmar a skill `tech-mentor-system-design` pelo motivo já registrado em ingestões anteriores (path `/home/nemomartins/Documentos/new/skills/` inexistente neste ambiente) — ingest feito por analogia com as fontes de system design já calibradas na wiki.

## Raw Quotes

> "A gente precisa saber quantos usuários vão utilizar, quais são as features que esses usuários vão utilizar, quais as limitações, o que que tá dentro do escopo, o que que tá fora do escopo."

> "Nossa solução só pode ser tão boa quanto a nossa capacidade de compreensão desse problema."

> "A minha solução que funciona na minha máquina para mim não vai funcionar para milhões de clientes distribuídos ao longo do mundo inteiro."

> "O código é o detalhe de implementação quase. Aqui a gente tá muito mais preocupado com arquitetura, com a infraestrutura, com os fluxos de dados."

> "Se o número verdadeiro de likes for 301, só que para você aparece o número 302, tem alguma diferença? Não tem. Na prática não tem nenhuma diferença."

> "Numa entrevista o que eu recomendo é que você esteja sempre expondo aquilo que você tá pensando, expondo o seu raciocínio, fazendo perguntas."
