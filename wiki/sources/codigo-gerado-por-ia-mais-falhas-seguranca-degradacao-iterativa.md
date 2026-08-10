---
type: source
title: "Código Gerado por IA Tem 2,77x Mais Falhas de Segurança — e Piora a Cada Refinamento"
aliases: ["degradação de segurança em geração iterativa de código", "código de ia 2.77x mais vulnerável"]
date_created: 2026-08-06
date_updated: 2026-08-06
source_count: 0
tags: [tech-mentor-ai, seguranca, sast, code-review, ai-assisted-engineering, vulnerabilidade, devsecops]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/codigo-gerado-por-ia-mais-falhas-seguranca-degradacao-iterativa.md
source_url:
author: desconhecido (canal de vídeo em português, formato educativo/mentoria técnica, CTA para treinamento pago próprio)
date_published:
date_ingested: 2026-08-06
---

# Código Gerado por IA Tem 2,77x Mais Falhas de Segurança — e Piora a Cada Refinamento

## TL;DR

Transcrição de vídeo que reúne três fontes de dados independentes (CodeRabbit, Veracode, Black Duck) para sustentar que código gerado por IA tem ~2,77x mais falhas de segurança que código escrito por humanos, e usa um paper do arXiv ("Security Degradation in Iterative AI Code Generation") para mostrar que **refinar iterativamente o código com IA piora a segurança em vez de melhorá-la** — 37,6% mais vulnerabilidades críticas depois de 5 rodadas de refinamento, mesmo quando um dos prompts testados pedia explicitamente foco em segurança a cada rodada. O vídeo explica o mecanismo (LLMs treinam em código público que inclui padrões inseguros, e reproduzem esses padrões com a mesma fluência/confiança de código seguro, sem o "alerta interno" que um dev experiente tem) e propõe 5 mudanças concretas de processo: SAST no delta a cada modificação, limite de iterações antes de revisão manual, testes de segurança escritos antes de iterar, revisão de segurança em contexto/chat limpo (não o mesmo que gerou o código), e mudança de expectativa mental sobre o que "iterar" custa.

## Key Claims

1. **Código gerado por IA tem ~2,77x mais falhas de segurança que código escrito por humanos**, segundo dois estudos independentes: CodeRabbit (análise de PRs reais — 320 gerados por IA vs. 150 por humanos) e Veracode (relatório 2025, testando mais de 100 modelos diferentes). Confiança: alta como *claim relatado por segunda fonte* — a fonte não linka os relatórios originais, mas cita metodologia (tamanho de amostra do CodeRabbit) com especificidade suficiente para não parecer estatística solta. [external: metodologia exata dos relatórios CodeRabbit/Veracode não verificada nesta ingestão — apenas relatada pela fonte]
2. **Relatório Black Duck (open source security), 947 codebases analisados**: aumento de 107% em vulnerabilidades por codebase em um ano; média de 581 vulnerabilidades por codebase; 87% dos codebases com pelo menos uma vulnerabilidade conhecida; 85% das empresas já usam IA para gerar código; mas **apenas 24% fazem avaliação completa** (segurança + licença + qualidade) do código gerado por IA, e 76% fazem só checagem parcial.
3. **Mecanismo causal proposto**: LLMs generativos treinam em código público que inclui padrões inseguros (SQLi em snippets do Stack Overflow, XSS em projetos do GitHub, tutoriais desatualizados) e reproduzem esses padrões com a mesma fluência e "confiança" textual de um padrão seguro — a fluência da geração não é sinal de correção de segurança. Isso contrasta com um dev humano, que hesita e verifica quando está inseguro sobre uma prática de risco (ex.: concatenar string em query SQL); o modelo "completa o padrão" sem esse sinal interno de alerta.
4. **Paper "Security Degradation in Iterative AI Code Generation"** (arXiv; autoria citada foneticamente como Shivani Chukala, Rimanchu Joshi e Romília Sid — grafia dos nomes não confirmada, ver Open Questions) testou a premissa comum de que mais rodadas de refinamento produzem código melhor, aplicada especificamente à dimensão de segurança. Metodologia: 400 amostras, 40 rodadas de refinamento, 4 estratégias de prompt diferentes, vulnerabilidade medida a cada passo via análise estática (mesmo tipo de ferramenta usada em pipelines de CI). Resultado: **37,6% de aumento em vulnerabilidades críticas após 5 interações** de refinamento.
5. **Nenhuma estratégia de prompt eliminou a degradação** — uma das quatro estratégias testadas pedia explicitamente para focar em segurança a cada rodada; mesmo assim houve melhora nas primeiras interações seguida de piora nas rodadas seguintes. A fonte interpreta isso como evidência de que o problema é estrutural (mecanismo do modelo), não solucionável só ajustando o prompt.
6. **Três mecanismos propostos para a degradação sistêmica**: (a) o modelo não retém memória do contexto de segurança de rodadas anteriores — trabalha sobre o código presente, sem histórico de que vulnerabilidade foi introduzida/corrigida onde; (b) cada refactor pode mover a lógica de validação de lugar, fazendo-a sumir ou mudar de comportamento sem alterar a aparência do código; (c) testes funcionais continuam passando porque cobrem o happy path, não o edge case adversarial — a regressão de segurança passa despercebida pela suíte de testes padrão.
7. **Cinco mudanças de processo propostas**: (1) rodar SAST antes e depois de cada modificação e revisar o delta, não o código inteiro de novo; (2) definir um limite de iterações antes de forçar revisão manual (o paper mostra que 5 rodadas já bastam para +37% de críticas); (3) escrever testes de segurança antes de começar a iterar, como contrato que qualquer mudança futura precisa respeitar; (4) revisar segurança em um contexto/chat novo, sem o histórico de quem escreveu o código — a fonte argumenta que um modelo "sem memória de autoria" é mais crítico que um que acabou de escrever aquele código; (5) mudança de expectativa mental — tratar iteração como algo que tem custo (inclusive de segurança), não como melhoria estritamente monotônica.
8. **Recomendação em nível de time**: cadência de security review precisa acompanhar a velocidade de produção de código via IA — de "uma vez por sprint/mês" para "por feature, por iteração significativa" — sob pena de acumular dívida de segurança na mesma velocidade da produtividade ganha. Ilustrado com anedota de segunda mão: um endpoint passou, após iteração com IA, a logar PII (nome e telefone) na response, sem que ninguém tivesse notado antes de um review manual.

## Entidades Mencionadas

- [[wiki/entities/coderabbit]] *(nova)* — fonte do dado dos 2,77x, análise de PRs reais gerados por IA vs. humanos.
- [[wiki/entities/veracode]] *(nova)* — relatório 2025 corroborando o mesmo múltiplo de 2,77x, testando mais de 100 modelos.
- [[wiki/entities/black-duck]] *(nova)* — relatório de segurança open source, dados sobre crescimento de vulnerabilidades por codebase e cobertura de avaliação de código de IA pelas empresas.

## Conceitos Tocados

- [[wiki/concepts/degradacao-de-seguranca-iterativa-ia]] *(nova)* — conceito central extraído do paper citado.
- [[wiki/concepts/governanca-de-codigo-gerado-por-ia]]
- [[wiki/concepts/sast]]
- [[wiki/concepts/devsecops]]
- [[wiki/concepts/shift-left-testing]]
- [[wiki/concepts/sql-injection]]
- [[wiki/concepts/xss]]
- [[wiki/concepts/exposicao-excessiva-de-dados]]
- [[wiki/concepts/degradacao-de-contexto]]
- [[wiki/concepts/vibe-coding]]

## Open Questions

- Os nomes dos autores do paper citado ("Shivani Chukala, Rimanchu Joshi e Romília Sid") foram ouvidos foneticamente pela fonte e podem estar incorretos — não foi possível localizar/confirmar o paper exato no arXiv a partir desta transcrição isolada. Se uma fonte futura confirmar o paper (título, autores, link), esta página e [[wiki/concepts/degradacao-de-seguranca-iterativa-ia]] devem ser atualizadas com a referência precisa.
- Os relatórios da CodeRabbit, Veracode e Black Duck são citados de segunda mão (números e metodologia resumida), sem link direto verificável nesta ingestão — tratados como `[external, não verificado diretamente]`.
- A fonte não detalha se as "40 rodadas de refinamento" do paper ocorreram numa única sessão/contexto de conversa (o que aproximaria o mecanismo de [[wiki/concepts/degradacao-de-contexto]]) ou em chamadas independentes sem contexto compartilhado — essa distinção mudaria qual dos dois mecanismos (falta de memória entre chamadas vs. degradação de atenção dentro de uma janela de contexto longa) é o dominante. Fica registrado como lacuna.

## Raw Quotes

> "O código gerado por IA tem 2,77 vezes mais falhas de segurança do que código escrito por humanos — quase o triplo. Isso não é o pior. O pior é que quase ninguém te conta: cada vez que você pede para melhorar o seu código, a segurança na verdade piora."

> "Só 24% das empresas fazem uma avaliação completa do código gerado por IA — segurança, licença, qualidade, tudo. 76% checam alguma coisinha ali... mas só um quarto olha o pacote inteiro."

> "O modelo não tem esse alerta: ele completa o padrão. Se o padrão tem vulnerabilidade, ele vai achar que está certo... a fluência com que o modelo escreve código inseguro é a mesma fluência com que ele escreve código seguro."

> "37,6% de aumento de vulnerabilidades críticas depois de cinco interações... e o detalhe que mata qualquer esperança de resolver isso só com prompt: uma das estratégias pedia explicitamente para focar em segurança a cada rodada. Mesmo assim, degradou."

> "Se você adotou IA no desenvolvimento e não atualizou os processos de segurança de code review, você está acumulando débito técnico — dívida de segurança — na mesma velocidade em que está produzindo código."
