---
type: source
title: "SQL Injection: O Que É e Como Se Proteger (Guia Completo de Soluções)"
aliases: ["sql injection guia completo galego", "sql injection sete niveis de defesa", "sql injection query parametrizada prepared statement waf"]
date_created: 2026-08-28
date_updated: 2026-08-28
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/sql-injection-guia-completo-solucoes-galego.md
source_url: ""
author: "Augusto Galego"
date_published: ""
date_ingested: 2026-08-28
source_count: 0
tags: [sql-injection, appsec, owasp, security, defense-in-depth, prepared-statements, orm, waf, least-privilege, input-validation]
skill: tech-mentor-security
status: stable
---

## TL;DR

Vídeo de [[wiki/entities/augusto-galego]] (autoria confirmada por "cupom Galego" no patrocínio) explicando SQL Injection do zero e organizando as defesas em **sete camadas concêntricas**, da mais próxima do banco até a borda da rede: (1) query parametrizada, (2) prepared statements, (3) menor privilégio na conexão do banco, (4) solução nativa do backend/linguagem, (5) ORM ou query builder, (6) validação de input (camada complementar, não suficiente sozinha), (7) WAF. Fecha com uma recomendação de ação imediata — corrigir a nível de código/backend primeiro — e reforça que reduzir privilégio do usuário de banco protege contra mais do que SQLi (ex.: comprometimento total do servidor via SSH).

## Key Claims

**Claim:** SQL Injection ocorre quando o servidor concatena/interpola input do usuário diretamente numa query SQL pré-programada, permitindo que o atacante encerre a query original e injete um segundo comando (ex.: `'; DROP TABLE users;--` no campo de e-mail).
**Evidence:** Exemplo didático completo no vídeo: campo de e-mail em formulário, código de servidor fazendo substituição de string na query, payload de ataque explicado passo a passo mostrando a query final resultante com dois statements.
**Confidence:** alta — mecanismo idêntico ao já documentado em [[wiki/concepts/sql-injection]] (exemplo "Bobby Tables") e demonstrado ao vivo em [[wiki/sources/injecao-sql-aula-modulo-seguranca]].

**Claim:** Query parametrizada e prepared statement são, na prática, a mesma lógica de defesa (separar consulta de dado) aplicada a nível de banco de dados — prepared statement é a forma nativa de bancos como Postgres.
**Evidence:** Fonte descreve os dois como "nível 1" e "nível 2" de fix, ambos definidos como "o banco recebe a query separada do campo", com prepared statement descrito como a implementação específica do Postgres para essa mesma separação.
**Confidence:** alta — consistente com a seção "Como Prevenir" de [[wiki/concepts/sql-injection]] ("Queries parametrizadas / prepared statements" já tratados como a mesma defesa central).

**Claim:** O princípio do menor privilégio na conexão servidor↔banco não previne SQL Injection por si só, mas minimiza a superfície de ataque — um usuário de banco com permissão só de `SELECT`/`INSERT`/`DELETE` em tabelas específicas não consegue `DROP TABLE` mesmo que uma injeção bem-sucedida aconteça.
**Evidence:** Fonte propõe explicitamente múltiplos usuários de banco por serviço/aplicação (ex.: um usuário exclusivo para "aplicação de e-mails" com privilégios restritos), e generaliza o benefício para além de SQLi: mesmo em caso de comprometimento total do servidor (SSH, RCE), privilégios mínimos limitam o dano ao banco de dados.
**Confidence:** alta — mesmo argumento de defense-in-depth já documentado em [[wiki/concepts/principio-do-menor-privilegio]] ("Se um serviço comprometido só tem permissão de leitura, o dano é contido").

**Claim:** Cada linguagem/framework de backend (Node, Rust, Django, Ruby) tem uma solução nativa recomendada para SQLi, e essa é a correção mais direta e de maior taxa de sucesso ao encontrar a vulnerabilidade — "corta o mal pela raiz".
**Evidence:** Fonte recomenda, como ação imediata ao descobrir um SQLi em produção, olhar primeiro a solução nativa do backend em uso, antes de qualquer outra camada.
**Confidence:** média — recomendação prática plausível e consistente com o princípio geral de parametrização, mas a fonte não detalha a API nativa de nenhuma linguagem específica (trata de forma genérica, "cada uma tem a sua solução").

**Claim:** ORMs (Drizzle, Prisma, ORM embutida do Django) e query builders previnem SQLi por padrão ou oferecem mecanismo dedicado para isso — mas isso precisa ser verificado dentro da ferramenta específica em uso, não assumido universalmente.
**Evidence:** Fonte generaliza "a sua ORM ou vai prevenir por padrão, ou vai ter uma solução" sem detalhar mecanismo interno, e recomenda pesquisar a documentação da ferramenta específica.
**Confidence:** média-alta — consistente com [[wiki/concepts/orm]] (Prisma/TypeORM/Sequelize parametrizam por padrão) mas com ressalva já registrada em [[wiki/concepts/sql-injection]]: "raw queries com interpolação" dentro de uma ORM continuam vulneráveis, ponto que esta fonte não menciona explicitamente.

**Claim:** Validação de input (ex.: Zod validando formato de e-mail) é uma defesa fraca contra SQLi quando usada isoladamente — não cobre campos de texto livre (ex.: descrição de produto) onde um payload SQL pode estar embutido dentro de uma string "válida" segundo o schema.
**Evidence:** Fonte argumenta que o comportamento interno do validador (que regex/máquina de estado ele usa) é opaco, que e-mails válidos podem ser sintaticamente estranhos, e que campos de texto livre validados apenas como "é uma string" não barram um payload SQL embutido no meio do texto.
**Confidence:** alta — reforça e generaliza o padrão já documentado em [[wiki/concepts/validacao-de-entrada]] (validação de schema como camada complementar, não substituta de parametrização) e em [[wiki/sources/injecao-sql-aula-modulo-seguranca]] (Celebrate+Joi como "camada extra", não a defesa primária).

**Claim:** Um Web Application Firewall (WAF) não é desenhado para prevenir 100% dos SQL Injections, mas por ser um firewall de proteção geral, acaba bloqueando parte dos payloads de SQLi que passam pelo corpo de requests.
**Evidence:** Fonte enquadra o WAF como a última camada, "antes do servidor", explicitamente descartando a expectativa de cobertura total: "de maneira alguma eu digo que o WAF vai prevenir 100% das SQL Injections — não é esse o objetivo de um WAF".
**Confidence:** alta — consistente com a definição de [[wiki/concepts/waf]] ("bloqueia ataques conhecidos do OWASP Top 10... por padrão de payload") e com a limitação já documentada nessa página quanto a cobertura parcial (WAF é cego a DOM-based XSS, por exemplo — mesma classe de limitação: opera por padrão de payload, não por análise semântica completa).

## Entities & Concepts Touched

- [[wiki/entities/augusto-galego]]
- [[wiki/concepts/sql-injection]]
- [[wiki/concepts/principio-do-menor-privilegio]]
- [[wiki/concepts/orm]]
- [[wiki/concepts/waf]]
- [[wiki/concepts/validacao-de-entrada]]
- [[wiki/concepts/defense-in-depth]]
- [[wiki/concepts/attack-surface]]

## Open Questions

- A fonte não detalha a "solução nativa" de nenhuma linguagem específica de backend (Node, Rust, Django, Ruby) — fica genérico ("cada uma tem a sua solução"), diferente de [[wiki/sources/injecao-sql-aula-modulo-seguranca]], que mostra código real em Express/`pg`.
- Não menciona explicitamente o risco de raw query interpolada dentro de uma ORM (ponto já registrado em [[wiki/concepts/sql-injection]]) — a fonte trata ORM como defesa presumidamente confiável sem essa ressalva.
- Stored procedures são citadas como possibilidade adicional a nível de banco, mas sem exemplo prático nem discussão de quando preferi-las a prepared statements — candidato a fonte dedicada futura.

## Raw Quotes

> "Um usuário malicioso vai tentar passar pro seu servidor um código que vai injetar algo via SQL no seu banco de dados, e o seu servidor, caso não esteja preparado para isso, vai repassar essa instrução para o banco de dados."

> "O Drop Table Users não deveria ser possível a nossa aplicação executar esse comando — então essa conexão aqui entre o servidor e o banco de dados deve ter o menor privilégio possível para fazer aquilo que é preciso ser feito."

> "De maneira alguma eu digo que o WAF vai prevenir 100% das SQL Injections — não é o objetivo de um WAF. Porém o WAF é um firewall, e como o firewall é bom para proteção em geral da sua aplicação, de quebra ele acaba pegando SQL Injection aqui e ali no corpo de alguns requests."

> "Você olhou sua aplicação, você percebeu 'eu tenho um SQL Injection aqui' — o que você acha que eu devo fazer de imediato, o mais simples, mais fácil pra você fazer: olha como você tá acessando esse seu banco de dados a nível de código."
