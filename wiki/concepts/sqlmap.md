---
type: concept
title: "SQLMap"
aliases: ["sqlmap", "sql map", "sql-map"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [sqlmap, sql-injection, pentest, redteam, automation, appsec]
skill: tech-mentor-security
status: draft
---

# SQLMap

Ferramenta open source que automatiza a **detecção e exploração** de [[wiki/concepts/sql-injection]]. Identifica o SGBD, testa parâmetros em busca de pontos vulneráveis, escolhe a técnica de exploração mais adequada ao comportamento observado da aplicação e extrai dados de forma estruturada.

Citada como ferramenta padrão de [[wiki/concepts/pentest]] também em [[wiki/concepts/redteam-pentest|metodologia de red team/pentest]].

## Pré-requisito: entender a exploração manual

[[wiki/sources/sql-injection-sqlmap-luiz-viana]] é enfático: rodar o SQLMap sem entender como uma query pode ser manipulada manualmente reduz a ferramenta a "mais um comando rodando sem sentido". O SQLMap executa a lógica de exploração que o operador define — não substitui o entendimento de como o parâmetro se comporta nem qual técnica se aplica a cada caso.

## Uso básico

```bash
sqlmap -u "https://alvo.com/pagina?id=1" -p id --dbms=mysql
```

- `-u` — URL alvo.
- `-p` — parâmetro específico a testar (evita testar todos os parâmetros da URL).
- `--dbms` — não obrigatório, mas acelera a detecção ao restringir os payloads testados a um único SGBD (ex.: informado por uma mensagem de erro prévia).

## Extração de dados

Uma vez confirmada a injeção:

```bash
sqlmap -u "..." --dbs                    # lista bancos de dados
sqlmap -u "..." -D <banco> --tables       # lista tabelas do banco
sqlmap -u "..." -D <banco> -T <tabela> --columns   # lista colunas da tabela
sqlmap -u "..." -D <banco> -T <tabela> -C <col1,col2> --dump  # extrai colunas específicas
sqlmap -u "..." --dump-all                # extrai tudo (pode ser lento em bancos grandes)
```

## Técnicas que o SQLMap escolhe automaticamente

Ver detalhamento em [[wiki/concepts/sql-injection-tecnicas-de-exploracao]]. Resumo: o SQLMap adapta a técnica ao que a aplicação revela — erro visível → error-based; resultado aparece na tela → UNION-based; nada aparece → boolean-based ou time-based blind.

## Headers customizados e autenticação

```bash
sqlmap -u "..." --headers="User-Agent: Mozilla/5.0 ..."
sqlmap -u "..." --cookie="session=..."
```

Útil quando a aplicação exige autenticação ou quando se quer simular um navegador real.

## Leitura e escrita de arquivos no servidor

```bash
sqlmap -u "..." --file-read=/etc/passwd
```

Ver [[wiki/concepts/load-file-into-outfile-mysql]] para o mecanismo por trás (`LOAD_FILE`/`INTO OUTFILE`) e os riscos (exposição de credenciais, chaves SSH, potencial RCE).

## `--level` e `--risk`: detecção mais profunda

Padrão: `level=1`, `risk=1` — testes básicos, payloads seguros e rápidos, cobrindo os parâmetros mais comuns. Isso pode gerar **falso negativo** em vulnerabilidades menos óbvias (ex.: que só respondem a payloads com aspas duplas ou estruturas mais elaboradas).

- `--level` (1-5) — aumenta o número de parâmetros e variações de payload testados.
- `--risk` (1-3) — aumenta a agressividade dos payloads (mais intrusivos, mas também mais eficazes).
- `-v` — modo verbose, mostra cada payload sendo injetado.

[[wiki/sources/sql-injection-sqlmap-luiz-viana]] demonstra um caso concreto: `level`/`risk` padrão não encontra nada; `--level 2 --risk 2 -v` revela a vulnerabilidade. Trade-off: mais cobertura tem custo de tempo e de impacto na aplicação alvo, relevante em qualquer engajamento de pentest com escopo e janela definidos.

## Injeção via POST e via headers/cookies

- `--method POST --data "campo1=valor1&campo2=valor2"` — testa parâmetros do corpo de uma requisição POST.
- `-r <arquivo>` — aponta para um arquivo com a requisição HTTP completa (headers + corpo), capturada por exemplo na aba Network do navegador (copiar como "raw"). Testa todos os parâmetros encontrados na requisição.
- `*` dentro de `--headers` ou da URL — marca manualmente o ponto exato onde o payload deve ser injetado, mesmo que o SQLMap não reconheça aquele ponto como testável por padrão. Útil para cookies, APIs e path parameters.

## Bypass de WAF/filtros anti-injeção

Quando a aplicação tem um [[wiki/concepts/waf]] ou filtro anti-injeção, payloads clássicos são detectados e bloqueados antes de chegar ao banco. Recursos do SQLMap para tentar contornar isso:

- **Tampers** (`--tamper=<script>`) — disfarçam o payload sem alterar seu efeito no banco. Exemplos citados: `space2comment` (troca espaços por comentários SQL equivalentes, que o banco interpreta igual mas o filtro pode não reconhecer) e `randomcase` (randomiza maiúsculas/minúsculas de palavras-chave, contra filtros case-sensitive). `--list-tampers` lista todos os scripts disponíveis; combináveis entre si.
- `--technique=<letra>` — força uma técnica específica (ex.: `T` para time-based, `B` para boolean-based, `U` para UNION-based), o que também pode ajudar a evitar padrões que o WAF reconhece.
- `--random-agent` — rotaciona o User-Agent a cada requisição, simulando navegadores diferentes.
- `--delay` — adiciona intervalo entre requisições, para evitar bloqueio por excesso de requisições.

## Relação com Outros Conceitos

- [[wiki/concepts/sql-injection]] — vulnerabilidade que o SQLMap detecta e explora
- [[wiki/concepts/sql-injection-tecnicas-de-exploracao]] — taxonomia de técnicas (blind, error-based, UNION-based) que o SQLMap escolhe automaticamente
- [[wiki/concepts/load-file-into-outfile-mysql]] — leitura/escrita de arquivo no servidor via SQLi, automatizada por `--file-read`
- [[wiki/concepts/waf]] — alvo dos mecanismos de bypass (tampers, `--random-agent`, `--delay`)
- [[wiki/concepts/pentest]] — ferramenta padrão de fase de exploração em engajamentos autorizados

## Key Sources

- [[wiki/sources/sql-injection-sqlmap-luiz-viana]] — demonstração completa: detecção básica, técnicas automáticas, `--file-read`, `--level`/`--risk`, injeção POST/cookie, bypass de WAF com tampers
