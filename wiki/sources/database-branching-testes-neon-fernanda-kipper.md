---
type: source
title: "Database Branching: Como Criar Bancos de Dados de Teste Isolados por Branch"
aliases: ["database branching", "banco de dados de teste por branch", "Neon copy-on-write", "certificates dev certificates app"]
date_created: 2026-09-02
date_updated: 2026-09-02
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/database-branching-testes-neon-fernanda-kipper.md
source_url: ""
author: "Fernanda Kipper"
date_published: ""
date_ingested: 2026-09-02
source_count: 0
tags: [banco-de-dados, testes, migrations, postgresql, neon, ci-cd, arquitetura, database-branching]
skill: tech-mentor-backend
status: stable
---

# Database Branching: Como Criar Bancos de Dados de Teste Isolados por Branch

## TL;DR

[[wiki/entities/fernanda-kipper]] explica **[[wiki/concepts/database-branching|database branching]]**: a prática comum de compartilhar um único banco de dados de teste entre todas as branches causa colisão de esquema quando migrations concorrentes se atropelam, gerando testes instáveis, dados contaminados e times bloqueados numa fila pelo banco. A solução é dar a cada branch um banco isolado via **copy-on-write** — uma técnica de armazenamento em que a branch nova só copia metadados/ponteiros para os dados originais, materializando uma cópia física apenas do bloco específico alterado no momento em que é alterado. Demonstra a aplicação prática no portal `fernandakipper.com` usando **[[wiki/entities/neon-database|Neon]]** (Postgres serverless): um banco `certificates dev` com branch `main` funcionando como staging (schema idêntico a produção, dados de seed/mock em vez de dados reais), e uma branch de banco nova criada automaticamente a cada deploy de PR na [[wiki/entities/vercel|Vercel]] — integração nativa Vercel↔Neon atualiza a `DATABASE_URL` e roda as migrations pendentes no momento do deploy, sem intervenção manual.

## Key Claims

- **Banco de teste único compartilhado por todas as branches causa colisão de esquema quando a aplicação controla suas próprias migrations**: duas branches concorrentes (ex.: feature de login adicionando um valor de enum em `subscription_type`; feature de billing mexendo em regra de negócio sobre assinatura, sem tocar o schema) aplicam migrations no mesmo banco físico. A segunda branch herda alterações de schema que não existem na sua própria branch de código — sintoma clássico do problema mais geral já documentado em [[wiki/concepts/database-migration]] (migrations tratadas com a mesma seriedade que código, versionadas e revisáveis) quando esse versionamento por-branch de código não tem um equivalente por-branch de dado. → [[wiki/concepts/database-migration]]
- **Três consequências nomeadas do banco único**: (1) testes instáveis — nem unitário, nem integração, nem manual são confiáveis, porque o ambiente de teste não é uma réplica de produção + só as minhas mudanças, é produção + minhas mudanças + mudanças de todo mundo; (2) dados contaminados — testes manuais rodam contra dados deixados por migrations de outras branches; (3) times bloqueados numa fila esperando a vez de usar o banco. *Nota de calibração:* a fonte generaliza esse terceiro ponto mesmo para setups com **deploy replicável por branch** (uma instância de app por branch) — o gargalo não é o deploy da aplicação, é o banco físico único por trás de todos eles.
- **Copy-on-write é o mecanismo técnico por trás do database branching**: uma branch nova de banco não duplica os dados originais — compartilha os mesmos blocos físicos e só materializa uma cópia física de um bloco específico no momento em que esse bloco é escrito (schema change ou dado alterado). Uma branch que só lê nunca gera cópia; o custo de storage e o tempo de criação da branch são ambos ~O(mudanças), não O(tamanho do banco). *Confiança: alta* — descrição bate exatamente com o mecanismo documentado em [skill: tech-mentor-backend] `backend-tooling.md` para o Neon (branches como snapshot copy-on-write do `parent`).
- **Staging (não produção) é a branch-mãe de onde as branches de teste derivam**: a fonte é explícita em nunca ramificar direto de produção ("até porque no de produção pode ter dados reais dos clientes") — o fluxo correto é produção → staging (schema espelhado, dados de seed/mock) → branch efêmera por PR/deploy, derivada do staging. → [[wiki/concepts/expand-contract]] (mesma preocupação de nunca expor dado real de cliente em ambiente de teste, resolvida aqui por isolamento de branch em vez de mascaramento)
- **Exemplo real do próprio canal (`fernandakipper.com`) confirma o padrão em escala pequena**: dois devs (autora + colega) fazendo migrations concorrentes em features diferentes (trilhas de aprendizagem, certificados) num banco de teste compartilhado geravam os mesmos conflitos descritos na teoria — mesmo em um projeto pequeno, sem muitos devs nem muitos deploys. Após adotar branching por banco via Neon, cada um evolui sua feature aplicando quantas migrations precisar sem atropelar o outro.
- **Setup concreto: dois projetos Neon separados, um deles com sub-branching**: `certificates app` é o banco de produção (nunca ramificado); `certificates dev` tem uma branch `main` que funciona como staging estável (schema espelhado de produção, dados de seed) — é a partir dessa `main` de dev, não da de produção, que cada branch de PR/deploy é derivada.
- **Integração Vercel↔Neon automatiza o ciclo completo do deploy de preview**: a cada branch nova criada no GitHub, a Vercel dispara um deploy de preview que aciona a criação da branch de banco correspondente (a partir da `main` do Neon dev), atualiza automaticamente a variável de ambiente `DATABASE_URL` do ambiente de preview para apontar para essa branch nova, e roda as migrations pendentes no momento do deploy. Sem essa integração nativa, o mesmo fluxo exigiria: criar a branch via CLI/API do Neon, obter o novo host/connection string, escrever isso na variável de ambiente do ambiente de preview manualmente antes de cada deploy — mecanismo que teria que ser construído à mão. → [[wiki/concepts/variaveis-de-ambiente]]
- **O banco de dados de teste vem com seed próprio, menor que o de produção**: o exemplo mostra 6 cursos no banco de teste vs. 11 em produção no momento da gravação — a branch de dev não é sincronizada retroativamente com o crescimento de produção, ela carrega o seed definido quando a branch `main` de dev foi criada. Isso é uma limitação prática do fluxo descrito, não do mecanismo de copy-on-write em si — poderia ser mitigado recriando a `main` de dev periodicamente a partir de um snapshot de produção mascarado.
- **Recomendação explícita de quando vale o custo do database branching**: aplicações com controle próprio de schema (roda suas próprias migrations) e alta frequência de mudança de schema entre branches concorrentes. *Confiança: alta* — critério idêntico ao documentado em [skill: tech-mentor-backend] `backend-tooling.md` ("times com migrations frequentes e medo de aplicar em produção, especialmente com dados sensíveis que não podem ser copiados para staging").

## Entities

[[wiki/entities/fernanda-kipper]] · [[wiki/entities/neon-database]] · [[wiki/entities/vercel]]

## Concepts

[[wiki/concepts/database-branching]] · [[wiki/concepts/database-migration]] · [[wiki/concepts/expand-contract]] · [[wiki/concepts/postgresql]] · [[wiki/concepts/testes-integracao-banco-real]] · [[wiki/concepts/variaveis-de-ambiente]] · [[wiki/concepts/checklist-primeiro-dia-projeto]]

## Conexão com outras fontes

Complementa diretamente [[wiki/concepts/database-migration]] (já cobrindo migrate up/down, SQL cru vs. ORM, e riscos de lock em produção via [[wiki/sources/database-migrations-sql-cru-vs-orm-drizzle]]): aquela fonte foca em *como escrever e aplicar* uma migration com segurança; esta fonte foca em *onde* essa migration é testada antes de chegar em produção — um ambiente de teste isolado por branch em vez de um banco compartilhado. Também dialoga com [[wiki/concepts/expand-contract]] — ambos os conceitos resolvem "não corromper o que está em produção durante uma mudança de schema", mas em eixos diferentes: expand-contract isola no *tempo* (três fases sequenciais convivendo com duas versões do código), database branching isola no *espaço* (cada branch de código tem seu próprio banco físico via copy-on-write). São técnicas complementares, não concorrentes — um mesmo pipeline poderia usar expand-contract *dentro* de uma branch de banco Neon antes do merge. [skill: tech-mentor-backend] confirma que a descrição da fonte do mecanismo copy-on-write e o caso de uso (Neon, workflow de CI por PR) batem exatamente com `backend-tooling.md` — nenhuma divergência técnica encontrada.

## Open Questions

- **Estratégia de refresh do seed de dev não é coberta pela fonte**: a `main` de dev ficou "presa" no seed original (6 cursos vs. 11 em produção) sem que a fonte mencione um processo de sincronização periódica — em pipelines mais maduros isso normalmente seria resolvido recriando a branch-mãe de staging a partir de um snapshot mascarado de produção; candidato a fonte futura se aparecer conteúdo sobre data masking em ambientes de teste.
- **Cleanup de branches efêmeras não é mencionado**: a fonte descreve a criação automática de branch por PR/deploy, mas não menciona explicitamente a deleção automática ao fechar o PR — o exemplo de workflow de CI documentado em [skill: tech-mentor-backend] `backend-tooling.md` inclui um passo `neon branches delete` `if: always()`; vale confirmar em fonte futura se o setup real de `fernandakipper.com` também limpa as branches ou se elas acumulam.
- **Nenhuma contradição** com conteúdo já presente na wiki — a fonte introduz um mecanismo novo (branching de banco a nível de infraestrutura) que resolve o mesmo tipo de problema que [[wiki/concepts/expand-contract]] e [[wiki/concepts/testes-integracao-banco-real]] já discutem, sem competir com nenhuma recomendação existente.

## Raw Quotes

> "No final acaba tendo um único banco de dados compartilhado por todas as branches de teste, todos os ambientes de teste, e isso acaba causando diversos problemas e muita dor de cabeça."

> "Isso aqui é uma técnica de armazenamento onde eu vou ter um ambiente que na verdade compartilha os mesmos blocos dos dados originais, sem duplicar esses blocos, realizando uma cópia física do bloco específico que eu for alterar no momento que ele precisa ser alterado."

> "Eu posso rodar quantas migrations eu quiser, quebrar esse banco de cima para baixo, e não vai ter risco nenhum, nem com o que o Léo tiver testando ou que alguém tiver testando aqui, nem com as coisas que vão pra produção."

> "Como a Vercel faz automático, a gente nem precisa se preocupar com isso: ele já atualiza meu `DATABASE_URL` ali para mim."
