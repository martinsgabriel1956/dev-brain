---
type: entity
title: "Augusto Galego"
aliases: ["Augusto Galego", "augustogalego.com"]
date_created: 2026-07-20
date_updated: 2026-08-11
source_count: 10
tags: [pessoa, programador, youtuber, brasil, devops, system-design, carreira, agentes-ia, code-review]
skill: tech-mentor-infra
status: stub
---

# Augusto Galego

Criador de conteúdo técnico em português, autor da demo de [[wiki/concepts/blue-green-deploy|deploy blue/green]] numa VPS com [[wiki/concepts/reverse-proxy|Nginx]]. Site pessoal/marca: `augustogalego.com`.

## Perfil

- Se descreve explicitamente como não sendo especialista em DevOps/infraestrutura ("nunca fui um cara de infra") — a demo é apresentada como reprodutível por qualquer pessoa seguindo tutoriais, não como conteúdo de autoridade técnica profunda em Nginx/systemd.
- Vídeo é continuação de uma aula anterior sobre tipos de deploy, sugerindo conteúdo seriado sobre deploy/infra para devs.
- Usa IA como apoio na criação do repositório de demonstração.

## Colaboração em Projeto de Terceiros

Convidado como editor/colaborador num projeto de outro criador de conteúdo ([[wiki/entities/replit|Replit]], vibe coding de um [[wiki/concepts/simulador-de-system-design|simulador de system design]]) — indício de rede de colaboração ativa entre criadores de conteúdo técnico brasileiros usando ferramentas de agentes de IA em conjunto.

## Conteúdo de Carreira e System Design

Além de conteúdo de infra/deploy, produz conteúdo sobre carreira e entrevistas técnicas — 12 anos de experiência, 5 deles em empresa gringa. Lançou curso pago próprio de System Design (mais de um ano de produção) cobrindo banco de dados, filas, load balancer, API Gateway, autenticação, WAF, rate limiting, Saga, CQRS, DNS, Blob Store, cache e CDN, com reembolso integral em um mês sem perguntas. Argumenta que é impossível definir com precisão universal o que é esperado de um júnior/pleno/sênior, pois nenhuma empresa concorda na própria definição desses níveis — mas ainda assim propõe uma progressão de referência específica para system design. → [[wiki/concepts/niveis-de-senioridade-system-design]]

## Possível Aula Irmã/Anterior sobre CI/CD e Deploy vs. Release (Autoria Inferida)

[[wiki/sources/continuous-integration-delivery-deploy-vs-release]] tem o mesmo padrão de patrocínio (HostGator, VPS, mesma faixa de preço e mesma promoção de Claude Code pré-instalado) e o mesmo estilo de demo prática de deploy — mas sem identificação de autor na transcrição. A fonte de [[wiki/sources/deploy-blue-green-na-pratica-vps-nginx]] é descrita como continuação de "uma aula anterior sobre tipos de deploy"; esta nova fonte, que cobre justamente CI/CD e deploy vs. release em nível mais introdutório, é uma candidata plausível a ser essa aula anterior (ou uma aula irmã da mesma série) — não confirmado, tratado como open question na fonte.

## Possível Conteúdo de Algoritmos/DSA (Autoria Inferida, Evidência Fraca)

[[wiki/sources/resolvendo-3-problemas-classicos-entrevista-coding-dsa]] — vídeo resolvendo três problemas clássicos de entrevista de coding, sem identificação de autor/canal na transcrição. O único indício de autoria é o cupom de patrocínio "Augusto 20" oferecido por um serviço de câmbio/remessas internacionais, repetido várias vezes no bloco publicitário — nome coincidente com esta entidade, mas evidência mais fraca que as inferências anteriores registradas nesta página (que se apoiavam em padrões de patrocínio idênticos, como HostGator, e citações diretas de produtos próprios, como "Mapa do Arquiteto" — aqui não há nenhum desses sinais, apenas o nome no cupom). Se confirmada, seria o primeiro conteúdo de algoritmos/estruturas de dados puro atribuído a este autor, distinto do conteúdo prévio de infraestrutura/deploy e carreira/system design. Tratado como open question na própria fonte.

## Possível Conteúdo de Infraestrutura como Código / AWS CDK (Autoria Inferida, Evidência de Conteúdo)

[[wiki/sources/infraestrutura-como-codigo-cdk-aws]] — vídeo sobre Infrastructure as Code com demo em AWS CDK, sem identificação de autor/canal no áudio. O indício de autoria aqui não é padrão de patrocínio (o sponsor deste vídeo, AmaX/infraestrutura de pagamentos, é diferente dos já associados a esta entidade), mas sim conteúdo: o fechamento do vídeo cita um curso pago próprio de System Design "o mais extenso já produzido" cobrindo exatamente API Gateway, Lambda, network e banco de dados — sobreposição quase total com a descrição do curso já documentada nesta entidade ("banco de dados, filas, load balancer, API Gateway, autenticação, WAF..."), com a mesma política de reembolso integral em um mês sem nenhum tipo de questionamento. Evidência de conteúdo mais forte que a inferência de [[wiki/sources/resolvendo-3-problemas-classicos-entrevista-coding-dsa]] (que se apoiava só num nome de cupom), mas mais fraca que as inferências apoiadas em padrão de patrocínio idêntico — tratada como open question na própria fonte.

## Conteúdo sobre Agentes de IA e Qualidade de Código

Além de infra/deploy, carreira e system design, produz conteúdo de reação/análise sobre a era agêntica. Em [[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]] reage ao tweet de [[wiki/entities/uncle-bob]] ("não reviso mais código de agentes") e propõe uma [[wiki/concepts/matriz-risco-dificuldade-review-ia|matriz risco × dificuldade]] para migrar gradualmente de revisão manual para merge automático. Relato pessoal relevante: trabalhou nos últimos meses numa **empresa de pagamentos** onde revisavam 100% do código do core business ("quem tem alguma coisa tem medo"), porque o valor entregue era robustez, não volume de features — usa esse caso como o extremo de alto risco que ainda justifica revisão manual total.

## Key Sources

- [[wiki/sources/deploy-blue-green-na-pratica-vps-nginx]]
- [[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]] — reação a Uncle Bob/Boris/Lucas Montano; matriz risco × dificuldade; relato da empresa de pagamentos revisando 100% do core business
- [[wiki/sources/infraestrutura-como-codigo-cdk-aws]] — autoria inferida por sobreposição de conteúdo do curso pago de System Design (API Gateway, Lambda, banco de dados) e política de reembolso idêntica, não confirmada por nome nem padrão de patrocínio
- [[wiki/sources/continuous-integration-delivery-deploy-vs-release]] — autoria inferida, não confirmada por nome no vídeo
- [[wiki/sources/system-design-simulador-hotel-booking-replit]] — convidado como colaborador/editor no projeto do simulador de system design
- [[wiki/sources/system-design-por-nivel-junior-pleno-senior]] — progressão de expectativas de system design por nível de senioridade (júnior/pleno/sênior), entrevista vs. trabalho real
- [[wiki/sources/anatomia-entrevista-system-design-bigtech]] — autoria inferida (não confirmada por nome no vídeo, ver open question na fonte): mesmo curso pago, mesma política de reembolso, mesmo bloco patrocinado UVP removido no início; detalha o pipeline de entrevista bigtech e o que cada etapa da sessão de system design avalia
- [[wiki/sources/resolvendo-3-problemas-classicos-entrevista-coding-dsa]] — autoria inferida com evidência fraca (nome no cupom de patrocínio "Augusto 20"), não confirmada; três problemas de algoritmos/estruturas de dados resolvidos ao vivo
- [[wiki/sources/escalar-para-um-milhao-de-usuarios]] — autoria inferida (mesmo curso pago de 90+ aulas, mesma política de reembolso de um mês): aula gratuita do curso reconstruindo o capítulo "de zero a milhões de usuários" de Alex Xu, desenho incremental guiado por SPOF
- [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]] — autoria confirmada (PWD do vídeo identifica o user "Augusto Galego"): comandos básicos de Linux e por que devs precisam reconhecê-los na era dos agentes; patrocínio Abacus
