---
type: entity
title: "Lucas Badico"
aliases: ["Badico"]
date_created: 2026-07-03
date_updated: 2026-08-18
source_count: 4
tags: [pessoa, programador, youtuber, go, brasil, agile, mentoria]
skill: tech-mentor-leadership
status: stub
---

# Lucas Badico

Programador e professor brasileiro, criador de conteúdo técnico focado em [[wiki/concepts/go-fundamentos|Golang]] e carreira/mercado de trabalho para desenvolvedores. Oferece um curso próprio de Golang voltado para devs que querem migrar de frontend/Node para backend.

## Perfil

- Especialista/defensor de Go como escolha sólida de carreira, não linguagem passageira
- Trabalha em uma empresa pequena (8 pessoas) onde a maioria dos devs frontend também atua com Go via [[wiki/concepts/ponte-fullstack-para-especializacao|caminho fullstack]]
- Compara filosofias de linguagem — Go (pragmatismo, poucas formas de fazer cada coisa) vs. Rust (expressividade, muitas features)
- Programa em Go profissionalmente há ~5 anos; nos últimos 3 meses (a partir de ~2026-04/05) deixou cargos de liderança/gestão para codar exclusivamente, em tempo integral

## Filosofia Técnica: Contra o "Código Fofo"

Defende, em [[wiki/sources/golang-profissional-sem-grandes-frameworks]], que Go é estruturalmente hostil a quem busca "código fofo" — soluções prontas via grande framework que dita como codar. Três pilares dessa visão: não existe framework dominante em Go equivalente a Rails/Express, apenas recomendações da comunidade; ~80% das dependências de um projeto profissional vêm da standard library, com o resto sendo pacotes pequenos e bem estabelecidos; e mesmo com generics disponíveis, a cultura Go prefere repetição estável a abstração genérica grande e frágil. Resume essa filosofia no ditado da comunidade "é melhor repetir um pouquinho de código do que acoplar a uma grande biblioteca".

## Visão de Carreira e Mercado

Defende que Go já superou a fase de "tendência passageira" por ter adoção estabelecida em grandes empresas brasileiras (Mercado Livre, Mercado Pago, Stone), ao contrário de tecnologias de nicho como Ruby on Rails. Recomenda que devs júnior mirem no nível pleno ao estudar Go — vagas júnior específicas da linguagem ainda são raras — e usem a posição de fullstack como ponte de entrada ao backend.

## Projeto em Live: Sistema de Mentoria em Go

Desde ~2026-06 constrói, inteiramente em [[wiki/concepts/build-in-public|live streams]], o "motor" da própria escola de mentoria em [[wiki/concepts/go-fundamentos|Go]] — organizado como [[wiki/concepts/monolito-modular]] com módulos internos (`appointment`, e futuramente `payment`, `chatbot`, `journey`), cada um expondo handlers HTTP e [[wiki/concepts/grpc]] próprios. Motivação declarada tripla: criar conteúdo/se expor (atualmente atua só como criador de conteúdo, não mais em múltiplas funções simultâneas), testar monolito modular na prática, e praticar Go com mais profundidade — reconhece ter mais bagagem de arquitetura/liderança em Go do que de codar de fato até este projeto. O primeiro módulo, `appointment`, é um clone do Calendly que resolve dores reais de sua mentoria: falta de visibilidade de sessões para o mentorado e retenção de ~R$50/sessão numa plataforma de pagamento subutilizada. Stack: Go, PostgreSQL/PostGIS, DynamoDB via [[wiki/concepts/localstack]], apenas três dependências externas (Gorilla Mux, gRPC do Google, GORM). Cita explicitamente logs, observabilidade e autenticação/autorização como desafios ainda não resolvidos na arquitetura. Ver [[wiki/sources/sistema-mentoria-golang-monolito-modular-live-lucas-badico]].

## Mentoria e Comunidade

Mantém um grupo de mentorados (mencionado como tendo mais de 50 pessoas) usado como fonte de discussão para conteúdo do canal — por exemplo, uma pergunta de um mentorado sobre metas forçadas de [[wiki/concepts/story-points]] virou a base de um vídeo sobre o papel do [[wiki/concepts/scrum-master]] e do PO. Oferece mentoria individual mediante contato direto (Instagram/e-mail).

## Key Sources

- [[wiki/sources/golang-mercado-trabalho-frontend-para-backend]]
- [[wiki/sources/story-points-po-forcando-30-40-pontos-por-sprint]]
- [[wiki/sources/golang-profissional-sem-grandes-frameworks]]
- [[wiki/sources/sistema-mentoria-golang-monolito-modular-live-lucas-badico]] — sistema de mentoria em Go construído em live, monolito modular com HTTP+gRPC
