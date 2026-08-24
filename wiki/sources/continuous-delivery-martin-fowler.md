---
type: source
title: "Continuous Delivery (Martin Fowler)"
aliases: ["continuous delivery bliki", "entrega contínua fowler"]
date_created: 2026-08-23
date_updated: 2026-08-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/continuous-delivery-martin-fowler.md
source_url: "https://martinfowler.com/bliki/ContinuousDelivery.html"
author: "Martin Fowler"
date_published: 2013-05-30
date_ingested: 2026-08-23
source_count: 0
tags: [cicd, continuous-delivery, continuous-deployment, martin-fowler, devops-culture, jez-humble]
skill: tech-mentor-infra
status: stable
---

# Continuous Delivery (Martin Fowler)

## TL;DR

Bliki (2013, atualizado em 2014) em que Fowler define formalmente "Continuous Delivery": uma disciplina onde o software é construído de forma que **possa** ser lançado em produção a qualquer momento — não que **seja** lançado a cada mudança. Lista quatro indicadores concretos de que um time está praticando CD (desenvolvidos pelo grupo de trabalho de Continuous Delivery da própria Thoughtworks), separa com precisão Continuous Delivery de Continuous Deployment (a primeira é pré-requisito da segunda, e a distinção é só sobre o lançamento em produção ser ou não automático/obrigatório), e lista três benefícios centrais (risco de deploy reduzido, progresso mais crível, feedback de usuário mais rápido). Reforça que CD exige tanto uma [[wiki/concepts/pipeline-de-ci|deployment pipeline]] quanto uma cultura colaborativa entre todos os envolvidos na entrega — o que ele batiza, via nota de rodapé, de "DevOps culture", fazendo questão de esclarecer que o termo vai além de "devs + ops": inclui QA, times de banco de dados e qualquer outro grupo necessário para colocar software em produção.

## Key Claims

- **Definição central**: Continuous Delivery é a disciplina de construir software de forma que ele **possa** ser lançado em produção a qualquer momento — a capacidade, não o ato.
- **Quatro indicadores** (desenvolvidos pelo grupo de trabalho de CD da Thoughtworks) de que um time pratica CD: (1) o software é deployável durante todo o seu ciclo de vida; (2) o time prioriza manter o software deployável em vez de trabalhar em novas features; (3) qualquer pessoa consegue feedback rápido e automatizado sobre a prontidão de produção do sistema, a qualquer momento que alguém faça uma mudança; (4) é possível fazer deploy "de um botão" de qualquer versão do software para qualquer ambiente, sob demanda.
- **O teste decisivo**: um patrocinador de negócio poderia pedir que a versão de desenvolvimento atual fosse implantada em produção a qualquer momento, e ninguém "pestanejaria", muito menos entraria em pânico.
- **Dois requisitos para alcançar CD**: (1) relação de trabalho próxima e colaborativa entre todos os envolvidos na entrega — o que ele chama de "DevOps culture", estendendo explicitamente o termo além de developers/operations para incluir testers, times de banco de dados e qualquer outro grupo necessário para produção; (2) automação extensiva de todas as partes possíveis do processo de entrega, geralmente via [[wiki/concepts/pipeline-de-ci|deployment pipeline]].
- **Continuous Delivery ≠ Continuous Deployment**: Continuous Deployment significa que toda mudança passa pelo pipeline e é automaticamente colocada em produção, resultando em muitos deploys de produção por dia. Continuous Delivery só significa que você **consegue** fazer deploys frequentes, mas pode escolher não fazer — geralmente porque o negócio prefere um ritmo mais lento. Continuous Deployment exige Continuous Delivery como pré-requisito; a via inversa não é obrigatória.
- **Três benefícios principais**: Reduced Deployment Risk (mudanças menores, mais fácil de corrigir se algo der errado); Believable Progress ("pronto" declarado por deploy em produção/ambiente parecido é mais crível do que "pronto" declarado pelos próprios desenvolvedores); User Feedback (colocar software funcionando na frente de usuários reais o quanto antes é a forma mais rápida de descobrir se ele é realmente útil).
- **User Feedback exige Continuous Deployment**, não apenas Delivery — mas dá para obter parte do benefício sem expor a totalidade da base de usuários, fazendo deploy para um subconjunto (funcionários primeiro, depois clientes convidados, depois todos — exemplo de um varejista citado por Fowler).
- **O livro de Jez Humble e Dave Farley** (*Continuous Delivery*) é citado como a obra fundacional do tema; Fowler recomenda também a página online de Humble sobre o assunto, incluindo um artigo específico de Humble explicando por que ele e Farley escolheram o nome "Continuous Delivery" em vez de "Continuous Deployment".
- **Agradecimento explícito a Jez Humble** por ajuda detalhada com a própria página do bliki.

## Entities

[[wiki/entities/martin-fowler]] · [[wiki/entities/jez-humble]] · [[wiki/entities/david-farley]] · [[wiki/entities/thoughtworks]]

## Concepts

[[wiki/concepts/ci-cd]] · [[wiki/concepts/deploy-vs-release]] · [[wiki/concepts/devops-culture]] · [[wiki/concepts/pipeline-de-ci]]

## Conexão com o que a wiki já sabia

[[wiki/concepts/ci-cd]] já documentava os "três níveis" (CI/CD/Continuous Deployment) e já citava [[wiki/sources/deployment-pipeline-martin-fowler]] como origem do princípio de estágios progressivos — esta fonte é a definição primária do próprio termo "Continuous Delivery" que aquele bliki de 2013 (mesma data de publicação) pressupõe sem definir. [[wiki/concepts/deploy-vs-release]] já tratava deploy e release como eventos separáveis via feature flag — a distinção CD vs. Continuous Deployment aqui é o mesmo raciocínio aplicado num nível acima (capacidade de lançar vs. lançamento de fato ser automático). "DevOps culture" nunca tinha página própria nesta wiki, apesar de o termo "devops" aparecer solto em tags de várias páginas de estratégia de deploy — esta ingestão cria a página a partir da definição precisa de Fowler (nota de rodapé), que explicitamente rejeita a leitura estreita de "devops = dev + ops". [[wiki/entities/david-farley]] já existia como stub citando o livro *Continuous Delivery* com Jez Humble, mas Jez Humble nunca teve entity própria — corrigido aqui.

## Open Questions

- Fowler cita, sem detalhar, "um projeto recente nosso" (da Thoughtworks) em que um varejista fez deploy do novo sistema online primeiro para funcionários, depois para um grupo convidado de clientes premium, e só depois para todos os clientes — nenhum nome de empresa ou link é dado; permanece anônimo/não verificável.
- O artigo linka para [[wiki/concepts/observed-requirement|ObservedRequirement]] (outro bliki de Fowler) como conceito relacionado a User Feedback, ainda não ingerido nesta wiki.
- Não fica claro no texto se as métricas usadas para decidir "ninguém pestanejaria" com um deploy a qualquer momento (o "teste decisivo") são formalizadas em algum lugar do livro de Humble/Farley ou se ficam apenas no nível de heurística qualitativa.

## Raw Quotes

*(Artigo já em inglês no original; tradução/paráfrase acima. Para o texto exato, ver `raw/continuous-delivery-martin-fowler.md` ou `source_url`.)*
