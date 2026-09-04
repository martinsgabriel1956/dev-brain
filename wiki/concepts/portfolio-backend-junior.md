---
type: concept
title: "Portfólio Backend Júnior"
aliases: ["portfólio primeira vaga", "diferenciais backend junior", "primeira vaga backend"]
date_created: 2026-04-25
date_updated: 2026-09-04
source_count: 7
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

## Repertório via Projetos Pessoais, Mesmo Sem Experiência Profissional

[[wiki/sources/o-que-sobrou-pro-dev-junior-eric-wendel]] reforça o mesmo princípio pela ótica de quem monta o portfólio, não de quem o avalia: o autor relata ter estudado por conta própria tema por tema alinhado a requisitos reais de vaga, construindo uma aplicação completa para ter "o que falar" em entrevista, mesmo antes de qualquer experiência profissional. A dica que ele destaca: mais projetos no GitHub demonstram vontade de aprender, autonomia e capacidade de resolver problemas — o que pesa na entrevista mesmo sem vínculo empregatício formal por trás do projeto.

## Comparação Entre Candidatos Reais: Trajetória + Projetos > Formatação de Currículo

[[wiki/sources/analise-curriculo-vaga-junior-desenvolvedor]] compara três currículos júnior reais aplicados a uma mesma vaga (Node/TypeScript/Java/React/AWS/Terraform) e observa que o candidato com a trajetória mais elogiada (empresa júnior → estágio → estágio, em ~2 anos) não foi o de melhor formatação de currículo, e sim o único com **três projetos pessoais documentados** (link, ferramentas, data), incluindo o projeto final do curso [[wiki/concepts/cs50]]. Nos três candidatos, o gap comum para a vaga-alvo específica foi o mesmo: Java e Terraform apareciam como "habilidade" listada, mas sem nenhum projeto, curso ou experiência que evidenciasse o uso real — reforçando que portfólio (evidência) supera lista de habilidades (promessa) mesmo dentro do próprio documento de currículo.

## Tensão: o Checklist Ainda Diferencia Se a IA Barateou o SaaS Funcional?

[[wiki/sources/leetcode-system-design-entrevista-versus-trabalho-real-na-era-da-ia]] argumenta que gerar um SaaS funcional deixou de provar competência por si só, já que a IA barateou a produção do artefato — ver detalhamento em [[wiki/concepts/curriculo-vs-portfolio]]. Isso reforça, e não contradiz, o checklist desta página: os itens listados (testes, SQL além do básico, observabilidade, error handling) são justamente o que a IA não gera bem sozinha e o recrutador leigo não sabe avaliar de olhar rápido — a tensão é sobre o que basta *mostrar* (rodar bonito na tela), não sobre o que basta *ter*.

## Key sources

- [[wiki/sources/diferenciais-portfolio-backend-junior]]
- [[wiki/sources/leetcode-system-design-entrevista-versus-trabalho-real-na-era-da-ia]] — SaaS funcional deixou de provar competência por si só; reforça por que os itens deste checklist (testes, SQL, observabilidade) continuam sendo o diferencial real
- [[wiki/sources/o-que-sobrou-pro-dev-junior-eric-wendel]] — projetos de portfólio como prova de autonomia e vontade de aprender, mesmo sem experiência profissional prévia
- [[wiki/sources/golang-mercado-trabalho-frontend-para-backend]]
- [[wiki/sources/analise-curriculos-programador-junior-dicas-ats]] — triagem de currículos reais confirmando GitHub/portfólio como filtro eliminatório, não apenas diferencial
- [[wiki/sources/5-cuidados-antes-de-comecar-a-programar]] — estratégia de implementar sozinho uma feature da empresa-alvo
- [[wiki/sources/analise-curriculo-vaga-junior-desenvolvedor]] — comparação de três currículos reais: trajetória + projetos pessoais documentados venceu formatação de currículo na avaliação
