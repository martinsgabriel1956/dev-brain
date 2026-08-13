---
type: source
title: "Por Que Pull Requests Falham (e Alternativas Sem PR)"
aliases: ["pull requests por que falham", "por que PR não funciona", "alternativas a pull request", "inventário é custo PR"]
date_created: 2026-08-13
date_updated: 2026-08-13
source_count: 0
tags: [tech-mentor-leadership, code-review, pull-request, trunk-based-development, pair-programming, feature-flag, reinertsen, inventario-e-custo]
skill: tech-mentor-leadership
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/pull-requests-por-que-falham-alternativas-sem-pr.md
source_url:
author: "Autor não identificado nominalmente na transcrição — atribuição provável a [[wiki/entities/lucas-montano]] por convergência de sinais: patrocínio AUVP (mesmo padrão de outras fontes já atribuídas ao canal), menção a conversar com quatro empresários antes do vídeo, estilo de fala ('cara'), e sobreposição temática direta com [[wiki/sources/code-review-morreu-uncle-bob-push-force-prod-lucas-montano]] e [[wiki/sources/git-flow-farsa-solucao-maturidade-rebase-lucas-montano]] (mesma série sobre processo de Git/PR). Não confirmado com certeza."
date_published:
date_ingested: 2026-08-13
---

# Por Que Pull Requests Falham (e Alternativas Sem PR)

## TL;DR

Vídeo em duas partes sobre pull requests: **(1)** o que faz um PR de fato funcionar — reduzir defeitos e ser rápido são os dois critérios de existência de um PR, e o problema central é que **o tempo de revisão não escala com o tamanho do PR** (200 e 2.000 linhas recebem a mesma janela de ~20-30min de atenção humana, então o PR grande recebe proporcionalmente menos escrutínio por linha). Recomenda tamanho ótimo (~100-300 linhas), revisão diária (idealmente 2x/dia), e cita a tese de **"inventário é custo"** de [[wiki/entities/principles-of-product-development-flow|Reinertsen]] aplicada a PRs abertos (código parado = dinheiro parado). **(2)** Alternativas usadas por empresas que não trabalham com PR: [[wiki/concepts/pair-programming|pair/mob programming]] (produtividade ~1,6x, não 2x, mas com menos retrabalho) + [[wiki/concepts/trunk-based-development|trunk-based development]] com pipeline de testes de integração fazendo o gate + [[wiki/concepts/feature-flag|feature flags]] para rollout progressivo. O autor é transparente sobre nunca ter trabalhado nesse modelo (só relatos de terceiros) e declara que, pessoalmente, ainda preferiria abrir PR mesmo nesse cenário.

## Key Claims

1. **O valor do PR vem de revisão assíncrona em equipe distribuída** — compartilhar informação, pegar problemas antes da `main`/produção, e evitar retrabalho por caminho de implementação errado. Fundamenta-se num corpo de evidências (não citado nominalmente) de que PR reduz defeitos.
2. **Dois critérios de existência de um PR: ser rápido e reduzir defeitos.** Se não cumprir os dois, o PR não serve seu propósito — enquadramento que orienta todo o resto do vídeo.
3. **O tempo de revisão não escala com o tamanho do PR** — 200 linhas e 2.000 linhas recebem, na prática, a mesma janela de atenção (~20-30min), porque quem revisa tem uma jornada cheia de outras tarefas. Resultado: a mesma quantidade absoluta de bugs encontrados representa uma fração muito menor de cobertura no PR grande. É o argumento central e mais original do vídeo — extensão intuitiva, mas com formulação própria, do problema geral de tamanho de PR.
4. **Extremos hipotéticos reforçam o argumento:** 5h de revisão dedicada deixaria de ser "rápido" (quase um dia de trabalho, PR levando semanas por causa do ciclo de idas e vindas); um PR de 20.000 linhas recebe efetivamente 0 minutos de revisão real.
5. **O meme do tamanho de PR** — PR de 10 linhas gera bikeshedding (revisor quer "sentir que contribuiu"); PR de 1.000 linhas recebe "looks good to me" superficial sem revisão de fato. Argumento sociológico, não técnico: é assim que pessoas reais trabalham, não como deveriam trabalhar.
6. **Tamanho ótimo de PR: ~100-300 linhas** (podendo ser menor para código complexo), como heurística grosseira — reconhece explicitamente que contagem de linhas não captura complexidade cognitiva real.
7. **"Inventário é custo" (Reinertsen) aplicado a PR aberto** — cita o livro *Principles of Product Development Flow* (referido na transcrição como "Principles of Software Development Flow", provável erro de transcrição/memória — mesma obra já registrada em [[wiki/entities/principles-of-product-development-flow]]) e a raiz toyotista da ideia. Um PR aberto por uma semana representa código que não gera valor; exemplifica com custo salarial (dev de R$10k/mês → ~R$2.500/semana "parados" no PR). Ver [[wiki/concepts/inventario-e-custo]].
8. **Recomendação de cadência: revisar PRs abertos todos os dias, idealmente 2x/dia** (início e fim do expediente) — para evitar perder uma noite inteira de "inventário parado" e reduzir o custo de troca de contexto (*context switching*) imposto sobre quem abriu o PR a cada ciclo de ida e volta.
9. **Fast follow como técnica anti-inventário** — em vez de negar um PR funcional que só precisa de ajustes menores (reabrindo o ciclo de idas e vindas), aprovar e mergear, e abrir um segundo PR menor só com as correções. Reduz carga cognitiva de revisão e mantém o inventário principal limpo.
10. **Draft PRs como ferramenta de poda precoce de caminho errado** — abrir PR ainda incompleto mas encaminhado para alguém validar a direção antes de terminar, evitando retrabalho de dias/semanas/meses se o caminho estivesse errado.
11. **Checklists de PR** — prática observada em algumas empresas (ex.: confirmar testes de integração, teste local, teste em staging) como camada adicional de qualidade antes do merge.
12. **PR não previne bugs, só reduz sua quantidade** — premissa explícita antes de introduzir as alternativas sem PR; nenhum processo de revisão é livre de falhas.
13. **Modelo "revisão contínua durante a criação" como alternativa ao PR** — empresas relatadas (não vivenciadas pelo autor) integram revisão ao próprio ato de escrever código, via pair/mob programming, eliminando a etapa separada de PR.
14. **Pair programming rende ~1,6x a velocidade de uma pessoa sozinha, não 2x** — perda de velocidade bruta de escrita compensada por menos retrabalho e menos tempo de revisão depois, citando estudos (não nomeados) como base.
15. **Mob/pair programming + trunk-based development + pipeline de testes de integração como gate + feature flags** é o pacote completo relatado para operar sem PR: commit direto na `main`, revisão já embutida no pairing, pipeline de testes de integração decidindo se o commit passa, e feature flags escondendo funcionalidade incompleta com rollout progressivo (interno → grupo pequeno → base toda).
16. **Opinião pessoal final do autor: mesmo nesse cenário sem-PR completo, ainda abriria um PR** — reconhece que é posição pessoal discutível, "várias pessoas mais inteligentes" concordam e discordam.

## Entidades Mencionadas

- Autor do vídeo — não identificado nominalmente; ver nota de atribuição no frontmatter (`author`).
- [[wiki/entities/lucas-montano]] — atribuição provável, não confirmada.
- Quatro empresários (não nomeados) — consultados pelo autor sobre processos de PR nas empresas deles, antes do vídeo.
- Patrocinador AUVP (escola de investimentos) — bloco de patrocínio removido do `raw/` por não ser conteúdo técnico.

## Conceitos Tocados

- [[wiki/concepts/code-review]]
- [[wiki/concepts/trunk-based-development]]
- [[wiki/concepts/pair-programming]]
- [[wiki/concepts/feature-flag]]
- [[wiki/concepts/quality-gate]] — implícito no papel da pipeline de testes de integração como gate no modelo trunk-based
- [[wiki/entities/principles-of-product-development-flow]]

## Open Questions

- **Título do livro citado com provável erro:** a transcrição diz "Principles of Software Development Flow"; o livro real (contexto: toyotismo, teoria de filas, "inventário é custo") é quase certamente *Principles of Product Development Flow* de Donald Reinertsen, já registrado em [[wiki/entities/principles-of-product-development-flow]] por outra fonte da wiki. Tratado aqui como o mesmo livro, mas sem confirmação literal contra a fala do autor.
- **Nenhum estudo é citado nominalmente** para as duas afirmações quantitativas centrais — "corpo de evidências" de que PR reduz defeitos, e o multiplicador de 1,6x em pair programming. Tratar como afirmações reportadas pelo autor, não dados verificados nesta ingestão.
- **Autoria não confirmada** — ver nota extensa no frontmatter. Se uma fonte futura confirmar ou refutar a atribuição a Lucas Montano, atualizar esta página e [[wiki/entities/lucas-montano]].
- Sem data de publicação nem URL na transcrição fornecida.

## Raw Quotes

> "Se o intuito é evitar retrabalho o mais rápido possível, se o intuito é pegar feedback o mais rápido possível, se o intuito é aumentar a velocidade de entrega de código, eu preciso que um PR seja rápido e eu preciso que ele reduza defeitos no código."

> "Se nesse PR aqui em 20 a 30 minutos você conseguiu achar 5, 10 bugs, nesse outro PR aqui de 2.000 linhas de código, em 20 a 30 minutos você também vai achar 5 a 10 bugs — só que vai ser um número muito menor dado a proporção do tamanho do PR."

> "Se você manda um PR com 10 linhas de código, a pessoa vai querer sentir que fez alguma contribuição, então vai fazer um monte de sugestão que é totalmente bikeshedding [...] e se você manda um PR de 1.000 linhas de código, você vai receber um looks good to me."

> "Se esse PR tá aberto há uma semana, é uma semana que o código não tá gerando dinheiro."

> "Existem vários estudos demonstrando [que] pair programming [...] vai fazer tipo assim 1,6 vezes a velocidade do código — não é o dobro."

> "Eu ainda criaria um PR aqui, na minha opinião — mesmo que eu tenha feito tudo em pair programming, mesmo que a gente tenha uma pipeline de testes."

## Key Sources

_(nova fonte — nenhuma outra página cita esta ainda)_
