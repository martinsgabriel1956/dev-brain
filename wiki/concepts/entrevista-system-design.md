---
type: concept
title: "Entrevista de System Design (Whiteboard Interview)"
aliases: ["system design interview", "whiteboard interview", "lousa branca", "entrevista de arquitetura"]
date_created: 2026-07-20
date_updated: 2026-08-21
source_count: 7
tags: [system-design, entrevistas, arquitetura, carreira]
skill: tech-mentor-system-design
status: draft
---

# Entrevista de System Design (Whiteboard Interview)

Etapa de entrevista técnica em grandes empresas em que o candidato precisa desenhar, ao vivo, a arquitetura de um sistema (ex.: "como você faria um Twitter", "como você criaria um encurtador de URL"). Diferente da [[wiki/concepts/entrevista-tecnica-coding|entrevista de coding]] (que avalia resolução de algoritmo), aqui o que está em jogo é repertório de arquitetura, maturidade técnica e capacidade de propor um sistema escalável e disponível. **System design não é design system** — são coisas diferentes.

## Estrutura recomendada da sessão (40–50 minutos)

A ordem importa tanto quanto o conteúdo — desenhar antes de levantar requisitos é um erro clássico porque faltam elementos e passa a impressão de que o candidato não está engajando com o entrevistador.

1. **Levantar requisitos, não presumir.** Perguntar explicitamente quais são as funcionalidades *core* (essenciais) vs. auxiliares. O foco do desenho deve estar nas core; auxiliares ficam para o final, se sobrar tempo.
2. **Plano de capacidade.** Ver [[wiki/concepts/estimativas-back-of-envelope]] — requisições por segundo/minuto, picos de acesso, banda necessária, custo de armazenamento em disco (dia/ano/5 anos) e replication factor.
3. **Modelagem de dados e API.** Mostrar repertório de bancos de dados (RDBMS, chave-valor, busca) por caso de uso — sem se aprofundar em modelagem complexa — e modelar a [[wiki/concepts/contrato-de-api|API]]: endpoints principais, request/response, protocolo (HTTP, gRPC).
4. **Só então desenhar o [[wiki/concepts/high-level-design|high-level design]].** O desenho na lousa é a última etapa, não a primeira — e o entrevistador avalia se o desenho é coerente com tudo que foi levantado antes.

## Regra de ouro: só cite tecnologia que você domina

Depois do desenho, entrevistadores tendem a perguntar detalhes cada vez mais específicos sobre qualquer tecnologia citada (ex.: citar Prometheus como stack de métricas pode levar a perguntas sobre como funciona seu sistema de alarmes, o banco de dados interno, consultas em PromQL). Citar algo que você não domina de verdade é um risco alto — se for citar mesmo assim, faça um disclaimer explícito ("o time onde trabalhei usava isso, mas não tenho profundidade nela").

## O objetivo estrutural é levar você a dizer "não sei"

Assim como na [[wiki/concepts/entrevista-tecnica-coding|entrevista de coding]], o entrevistador desce o nível de dificuldade das perguntas até encontrar o limite real de conhecimento do candidato. Isso é esperado, não reprovável — o erro é tentar "sabonetear" (enrolar) a resposta em vez de admitir a lacuna e demonstrar interesse em aprender sobre o tema.

## Relação com outros conceitos

- [[wiki/concepts/estimativas-back-of-envelope]] — o plano de capacidade é etapa obrigatória, não opcional
- [[wiki/concepts/high-level-design]] — o desenho final da sessão
- [[wiki/concepts/modelagem-de-dados]] e [[wiki/concepts/contrato-de-api]] — etapas intermediárias antes do desenho
- [[wiki/concepts/entrevista-tecnica-coding]] — mesma estrutura de "levar o candidato ao limite", formato diferente (algoritmo vs. arquitetura)
- [[wiki/concepts/arquitetura-de-software]] — o repertório que a sessão avalia
- [[wiki/concepts/simulador-de-system-design]] — ferramenta de prática que simula tráfego sobre o desenho e pontua com IA, pensada para treinar o mesmo repertório fora do contexto de entrevista

## Practicar Fora do Contexto de Entrevista

[[wiki/sources/system-design-simulador-hotel-booking-replit]] argumenta que esse repertório não serve só para passar em entrevista — é a competência que sobra quando a IA escreve o código, inclusive para quem está apenas [[wiki/concepts/vibe-coding|vibe codando]] um projeto sem saber programar. Isso motivou a criação de um [[wiki/concepts/simulador-de-system-design]] como produto: um playground onde o mesmo repertório de gargalo, cache, escalabilidade e mensageria é treinado com feedback em tempo real, em vez de só desenhado numa lousa estática.

## O Mesmo Formato, Profundidade Diferente por Nível

[[wiki/concepts/niveis-de-senioridade-system-design]] argumenta que a estrutura de sessão descrita acima é aplicada de forma quase idêntica para júnior, pleno e sênior (herança do padrão popularizado pelo Google) — o que muda entre os níveis não é o formato, é a profundidade esperada: júnior demonstra fundação e resolve um sistema simples (encurtador de URL, jogo de xadrez com 2 usuários); pleno soma requisitos não funcionais e racional prático de tradeoffs; sênior discute escalabilidade, CAP e sharding em profundidade e **lidera** a conversa em vez de apenas reagir a ela. Importante: essa cobrança na entrevista não reflete necessariamente o uso real de system design no trabalho — júnior e pleno usam pouco no dia a dia, enquanto a compreensão do sistema inteiro só se torna central a partir de sênior.

## O Pipeline Completo ao Redor da Sessão (Padrão BigTech)

[[wiki/sources/anatomia-entrevista-system-design-bigtech]] situa a sessão de system design dentro de um pipeline maior de 5 etapas comum a empresas que seguem o padrão bigtech: entrevista de RH → entrevista técnica/questionário → LeetCode ou take-home → **entrevista de system design** → reunião final de fit com engineering manager/equipe. Argumenta que preparar-se para o padrão mais exigente (bigtech) cobre automaticamente entrevistas menos rigorosas. Detalha também o *porquê* de cada etapa da sessão em si (requisitos funcionais/não funcionais, BOE, design de API, esquema híbrido SQL+NoSQL, HLD, tradeoffs) do ponto de vista do que o entrevistador está avaliando — não é decorar caixinhas, é compreensão do problema exposta em voz alta. Resume com "garbage in, garbage out": a solução só é tão boa quanto a compreensão do problema que a precede.

## O Framework Executado ao Vivo, com Erros Preservados

[[wiki/sources/system-design-entrevista-cinema-draw-io]] é a primeira fonte na wiki a mostrar a estrutura de sessão sendo **executada**, não só descrita: o apresentador levanta requisitos via follow-up questions (seatmap, busca por nome, reserva de 15 minutos, acesso web) sobre o prompt vago "sistema de reserva de ingressos de cinema", justifica cada peça do desenho (load balancer, MySQL vs. não-relacional, APIs externas de seatmap e pagamento, Redis com TTL) e — de forma incomum entre as fontes já ingeridas — expõe abertamente um bug de consistência não resolvido no próprio rascunho (assento aparece disponível numa API externa mas já está reservado no Redis interno), tratando isso como material de conversa com o entrevistador em vez de esconder. Reforça na prática a regra de ouro desta página: comunicar o raciocínio vale mais que a solução perfeita.

## Um Framework de 7 Passos, Ensinado do Zero Sobre um Caso Só

[[wiki/sources/como-projetar-sistemas-encurtador-de-urls-passo-a-passo]] é a fonte mais didática/introdutória da wiki sobre a estrutura da sessão: em vez de listar etapas em abstrato, ensina um framework de 7 passos (entender o problema → requisitos funcionais/não-funcionais → padrões de tráfego/estimativas → componentes em alto nível sem nomear tecnologia → definir API → só então escolher a stack técnica → revisar requisitos contra o desenho final) executando cada passo sobre um encurtador de URL do início ao fim — a mesma regra de "tecnologia por último" já implícita na estrutura de 4 etapas descrita acima, aqui explicitada como regra central: **"não invente as regras, faça perguntas de esclarecimento."** Contribuição própria: demonstra ao vivo o valor do passo final de revisão — o autor revisita a lista de requisitos originais contra o desenho e encontra uma lacuna real não tratada (unicidade 1:1 entre URL curta e longa), tratando isso como parte esperada do processo, não como falha grave a esconder — reforço direto da mesma lição de [[wiki/sources/system-design-entrevista-cinema-draw-io]] sobre expor lacunas em vez de escondê-las.

## Key sources

- [[wiki/sources/5-dicas-entrevistas-lousa-branca-system-design]]
- [[wiki/sources/system-design-por-nivel-junior-pleno-senior]]
- [[wiki/sources/anatomia-entrevista-system-design-bigtech]]
- [[wiki/sources/system-design-entrevista-cinema-draw-io]] — demonstração ao vivo do framework num exemplo concreto (cinema), incluindo um bug de consistência auto-reconhecido pelo autor
- [[wiki/sources/escalar-leituras-banco-de-dados-entrevista-tier-s]] — o erro que "elimina 90% dos candidatos" é pular para a solução sem investigar o contexto (volumetria, hotspots, criticidade de dados); o sênior faz perguntas primeiro, o pleno já dá a receita ("é só cache e réplicas")
- [[wiki/sources/como-projetar-sistemas-encurtador-de-urls-passo-a-passo]] — framework de 7 passos ensinado do zero sobre um encurtador de URL, com a regra de ouro "não invente as regras" e demonstração ao vivo do valor do passo final de revisão de requisitos
