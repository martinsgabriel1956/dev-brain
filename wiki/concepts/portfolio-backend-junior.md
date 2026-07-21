---
type: concept
title: "Portfólio Backend Júnior"
aliases: ["portfólio primeira vaga", "diferenciais backend junior", "primeira vaga backend"]
date_created: 2026-04-25
date_updated: 2026-07-21
source_count: 4
tags: [carreira, backend, junior, portfolio]
skill: tech-mentor-leadership
status: stable
---

# Portfólio Backend Júnior

O diferencial numa primeira vaga de backend não é arquitetura sofisticada — é demonstrar profissionalismo nos fundamentos que qualquer empresa vai exigir no dia a dia.

## O que diferencia (checklist)

| Item | Por que importa |
|---|---|
| [[docker-portfolio]] | Toda empresa usa; demonstra que a aplicação sobe em qualquer ambiente |
| Deploy em cloud real | AWS/GCP/Hetzner > Render/Heroku; mostra domínio de infra |
| [[testes-integracao-banco-real]] | Ausência de testes é eliminatório; 1 em 10 devs faz bem feito |
| [[sql-alem-do-basico]] | JOINs, agregações, subqueries — sai do CRUD e mostra domínio real |
| [[documentacao-api-swagger]] | 1 em 10 devs se preocupa; diferencial imediato e visível |
| [[error-handling-estruturado]] | Classes de erro + handler global = profissionalismo no código |
| [[observabilidade]] | Jaeger/Sentry no Docker Compose; mostra visibilidade sobre a aplicação |

## O que NÃO focar na primeira vaga

- **DDD / Clean Architecture complexa** — projetos grandes em produção usam estrutura simples com os fundamentos acima
- **Microsserviços** — complexidade desnecessária para o nível
- **MongoDB / NoSQL** — Redis como cache é ok; ir além não é prioritário
- **Escalabilidade / infra avançada** — habilidade que vem com experiência
- **Múltiplos frameworks** — todos usam os mesmos fundamentos; dominar um bem é suficiente

## Princípio central

> Uma aplicação bem testada é mais importante que uma com a melhor arquitetura do mundo.

## Mirando pleno em vez de júnior

Para tecnologias com menos vagas júnior formais (ex.: Go), a mesma lógica de portfólio se aplica com o alvo ajustado para cima: construir prova de nível pleno, não júnior, e usar isso para concorrer a vagas pleno oferecendo trabalhar por salário júnior. Ver [[wiki/concepts/ponte-fullstack-para-especializacao]] para a estratégia completa de migração via fullstack.

## Relações

- [[testes-integracao-banco-real]]
- [[docker-portfolio]]
- [[documentacao-api-swagger]]
- [[error-handling-estruturado]]
- [[sql-alem-do-basico]]
- [[observabilidade]]
- [[curriculo-vs-portfolio]]
- [[wiki/concepts/ponte-fullstack-para-especializacao]]

## Antes do portfólio: passar na triagem

Em processo real de triagem de currículos júnior, dois filtros vêm antes de qualquer avaliação de portfólio técnico: [[wiki/concepts/otimizacao-ats-curriculo]] (repetição da stack-alvo para passar no robô) e a presença do link de GitHub em si — sem ele, o portfólio nem chega a ser avaliado.

## Implementar uma única feature da empresa-alvo

[[wiki/sources/5-cuidados-antes-de-comecar-a-programar]] descreve uma variante mais radical do mesmo princípio, a partir da experiência de quem já esteve do lado de recrutamento: implementar sozinho uma única funcionalidade (ou tela, no caso de front-end) do sistema de uma empresa-alvo específica, e anexar o link na candidatura. O peso dessa demonstração é descrito como desproporcionalmente maior do que o esperado, porque uma pessoa sozinha entregando algo equivalente ao trabalho de um time evidencia domínio direto, sem a diluição de comunicação e prioridades que cresce com o tamanho do time. Ver [[wiki/concepts/projeto-com-adrenalina]] para o raciocínio mais amplo de escolher o projeto (e não a tecnologia) como primeiro passo.

## Key sources

- [[wiki/sources/diferenciais-portfolio-backend-junior]]
- [[wiki/sources/golang-mercado-trabalho-frontend-para-backend]]
- [[wiki/sources/analise-curriculos-programador-junior-dicas-ats]] — triagem de currículos reais confirmando GitHub/portfólio como filtro eliminatório, não apenas diferencial
- [[wiki/sources/5-cuidados-antes-de-comecar-a-programar]] — estratégia de implementar sozinho uma feature da empresa-alvo
