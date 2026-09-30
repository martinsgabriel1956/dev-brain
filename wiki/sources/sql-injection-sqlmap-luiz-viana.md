---
type: source
title: "SQL Injection com SQLMap — Laboratório Prático (Luiz Viana)"
aliases: ["sql injection sqlmap luiz viana", "sqlmap na pratica", "sqlmap lab lesson 1 7 10 11 20"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/sql-injection-sqlmap-luiz-viana.md
source_url: ""
author: "Luiz Viana"
date_published: ""
date_ingested: 2026-09-30
source_count: 0
tags: [sql-injection, sqlmap, pentest, appsec, owasp, security, blind-injection, union-based, file-read, waf-bypass]
skill: tech-mentor-security
status: stable
---

## TL;DR

Vídeo prático de [[wiki/entities/luiz-viana]] (mesmo autor de [[wiki/sources/xss-cross-site-scripting-luiz-viana]]) ensinando [[wiki/concepts/sql-injection]] do zero (por que a aspa simples quebra a query) e depois automatizando detecção e exploração com [[wiki/concepts/sqlmap]] contra um laboratório com múltiplos desafios numerados (Lesson 1, 7, 10, 11, 20). Cobre a taxonomia de técnicas que o SQLMap escolhe automaticamente ([[wiki/concepts/sql-injection-tecnicas-de-exploracao]]: boolean-based blind, time-based blind, error-based, UNION-based), leitura e escrita de arquivos no servidor via [[wiki/concepts/load-file-into-outfile-mysql]], os parâmetros `--level`/`--risk` para detecção mais agressiva, injeção via POST e via cookie, e bypass de WAF com tampers, `--technique`, `--random-agent` e `--delay`. Reforça, como em [[wiki/sources/xss-cross-site-scripting-luiz-viana]], que explorar a ferramenta sem entender a técnica manual por trás é inútil.

## Key Claims

**Claim:** SQL injection nasce porque um valor de texto do usuário precisa ir entre aspas dentro da query; inserir uma aspa extra fecha essa string prematuramente, e tudo que vem depois passa a ser interpretado como instrução SQL, não mais como dado.
**Evidence:** Explicação do mecanismo no início do vídeo e demonstração no Lesson 1: substituir o parâmetro `id` (que normalmente carrega um inteiro) por uma aspa simples produz um erro de sintaxe SQL, que também revela o SGBD em uso (MariaDB, fork do MySQL).
**Confidence:** alta — mecanismo idêntico ao já documentado em [[wiki/concepts/sql-injection]] (exemplo "Bobby Tables") e em [[wiki/sources/injecao-sql-aula-modulo-seguranca]] e [[wiki/sources/sql-injection-guia-completo-solucoes-galego]].

**Claim:** O SQLMap adapta automaticamente a técnica de exploração ao comportamento observado da aplicação — se há mensagem de erro, tenta error-based; se o resultado aparece na tela, tenta UNION-based; se nada aparece, cai para boolean-based ou time-based blind.
**Evidence:** No Lesson 1, a primeira técnica encontrada é boolean-based blind (a aplicação não exibe o resultado da query, então o SQLMap infere dados a partir de condições verdadeiro/falso); a fonte então explica error-based (usa a mensagem de erro para extrair nomes de tabela) e UNION-based (junta um SELECT customizado ao original) como alternativas que o SQLMap escolhe conforme o que a aplicação revela.
**Confidence:** alta — consistente com a documentação oficial do SQLMap sobre detecção adaptativa de técnica; não verificado contra a doc oficial nesta sessão, mas coerente com o comportamento amplamente descrito na comunidade de pentest.

**Claim:** Bancos como o MySQL permitem ler (`LOAD_FILE`) e escrever (`INTO OUTFILE`) arquivos no sistema operacional do servidor através de funções SQL nativas, e o SQLMap automatiza essa leitura via `--file-read`; a proteção nativa contra isso é a opção `secure_file_priv`.
**Evidence:** Demonstração no Lesson 7: `sqlmap -u <url> -p id --file-read=/etc/passwd` recupera o arquivo de usuários do Linux; a fonte descreve `INTO OUTFILE` como o caminho inverso (escrita), citado como potencial vetor para RCE se o usuário do banco tiver permissão de escrita no sistema de arquivos.
**Confidence:** alta para a mecânica de `LOAD_FILE`/`secure_file_priv` (documentada oficialmente pelo MySQL); média para a afirmação de RCE via `INTO OUTFILE`, que a fonte menciona como possibilidade mas não demonstra na prática neste vídeo.

**Claim:** Os parâmetros `--level` e `--risk` do SQLMap controlam, respectivamente, quantos parâmetros/variações de payload são testados e quão agressivos os payloads são; o padrão (`level=1`, `risk=1`) pode gerar falso negativo em vulnerabilidades que só aparecem com payloads mais elaborados (ex.: aspas duplas).
**Evidence:** No Lesson 10, a varredura padrão do SQLMap não encontra nada no parâmetro testado; aumentar para `--level 2 --risk 2` (com `-v` para ver os payloads enviados) revela a vulnerabilidade que o modo padrão não detectava.
**Confidence:** alta — comportamento documentado oficialmente pelo SQLMap (trade-off cobertura vs. velocidade/agressividade dos níveis) e replicado ao vivo na fonte.

**Claim:** A mesma lógica de injeção se aplica a parâmetros POST (corpo de formulário) e a cabeçalhos HTTP como cookies, não só a parâmetros GET na URL — nos dois casos o SQLMap precisa que o parâmetro alvo seja informado explicitamente (`--data`, `-r` com requisição capturada, ou `*` marcando o ponto de injeção dentro de `--headers`).
**Evidence:** Lesson 11 demonstra injeção em um formulário de login via `--method POST --data` ou via arquivo de requisição HTTP completo capturado no navegador (`-r`); Lesson 20 demonstra um caso em que a aspa simples no formulário não gera erro direto, mas o cookie retornado após login (`o name`/nome de usuário) é a entrada vulnerável, testada via `--headers` com um asterisco marcando a posição exata do payload.
**Confidence:** alta — mecanismo plausível e consistente com a documentação do SQLMap sobre `-r`, `--data` e injeção customizada com `*`; não verificado contra a doc oficial nesta sessão.

**Claim:** Quando a aplicação tem uma proteção anti-injeção (WAF/filtro), payloads clássicos são bloqueados antes de chegar ao banco; o SQLMap oferece scripts de "tamper" (ex.: `space2comment`, que troca espaços por comentários SQL equivalentes; `randomcase`, que randomiza maiúsculas/minúsculas) para disfarçar o payload sem mudar seu efeito no banco, além de `--technique` para forçar uma técnica específica, `--random-agent` para rotacionar o user-agent e `--delay` para espaçar requisições.
**Evidence:** Seção final do vídeo descreve cada um desses mecanismos como forma de burlar WAF, com `--list-tampers` citado como forma de listar todos os scripts disponíveis e a possibilidade de combinar múltiplos tampers na mesma execução.
**Confidence:** alta para a existência e propósito geral dos tampers (documentado oficialmente pelo projeto SQLMap); não verificado nome-a-nome de cada flag nesta sessão.

## Entities & Concepts Touched

- [[wiki/entities/luiz-viana]]
- [[wiki/concepts/sql-injection]]
- [[wiki/concepts/sqlmap]]
- [[wiki/concepts/sql-injection-tecnicas-de-exploracao]]
- [[wiki/concepts/load-file-into-outfile-mysql]]
- [[wiki/concepts/pentest]]
- [[wiki/concepts/waf]]
- [[wiki/concepts/owasp]]
- [[wiki/concepts/bug-bounty]]
- [[wiki/concepts/xss]]

## Open Questions

- A fonte afirma que `INTO OUTFILE` pode levar a RCE, mas não demonstra o caminho completo (escrever um arquivo executável/webshell e executá-lo) — fica como claim não verificada na prática, distinto do `--file-read` que é demonstrado ao vivo.
- Nomes exatos de flags (`--list-tampers`, sintaxe exata de `--technique=T/B/U`, uso do `*` em `--headers`) não foram cruzados com a documentação oficial do SQLMap nesta sessão — plausíveis e consistentes com o conhecimento geral da ferramenta, mas candidatos a verificação `[external]` futura.
- O laboratório usado (numerado por "lessons") não foi identificado por nome/plataforma no raw — o vídeo menciona "um link na descrição", mas o link em si não está na transcrição.

## Raw Quotes

> "Se você já é da área, você já deve ter ouvido daquele truque do `or 1=1` para pular o login — então essa é só a ponta do iceberg."

> "Não se deve fazer concatenação de string para criar uma query de consulta SQL, e sim, além de sanitizar as entradas do usuário, utilizar queries parametrizadas."

> "Quem não domina a exploração manual dificilmente vai conseguir usar o SQLMap com eficiência — sem conhecimento técnico, o SQLMap se torna só mais uma ferramenta rodando sem sentido."

> "De maneira alguma eu digo que confiar só no modo padrão do SQLMap é suficiente — usar bem o level e o risk é essencial para extrair o máximo da ferramenta, mas também obviamente tomando cuidado com todo o impacto que a ferramenta causa na aplicação alvo."
