---
date: 2026-08-04
tags: [clean-code, uncle-bob, agentes-ia, code-review, complexidade-ciclomatica, mutation-testing, tamanho-de-modulo, dependency-structure, sonarqube, ci-cd, quality-gate]
skill: tech-mentor-ai
type: transcript
---

# Quatro Técnicas de Gate de Qualidade no CI/CD Para Código Gerado por IA (reação a Uncle Bob)

> Transcrição de vídeo de reação a um tweet de Robert C. Martin (Uncle Bob) sobre não revisar mais código escrito por agentes de IA. Transcrição bruta já estava em português — limpa, pontuada e estruturada em markdown, sem necessidade de tradução. Bloco publicitário de patrocinador (fintech de câmbio, no meio do vídeo) omitido por não ser conteúdo técnico da transcrição.

---

## O tweet: "eu não reviso o código escrito por agentes"

Uncle Bob — o mesmo que ensinou basicamente duas gerações de engenheiros a fazer code review — postou no Twitter que não revisa mais código escrito por seus agentes de IA. No lugar disso, ele confia em métricas: cobertura de teste, dependency structure, complexidade ciclomática, tamanho de módulos, mutation tests, "e por aí vai". A tese dele: é possível inferir muita coisa sobre a qualidade de um código através dessas métricas — sem precisar ler o código linha a linha.

O autor do vídeo relata já ter trabalhado em time onde SonarQube era gate obrigatório antes de merge (por pull request), então reconhece a prática de longa data. O que muda agora é a justificativa de Uncle Bob para *não engajar* com o código em si: produtividade. Segundo ele, humanos são lentos no código, e para ganhar produtividade os humanos devem se desengajar do nível de código e gerenciar em nível mais alto.

O autor diz concordar com Uncle Bob, e evita chamar isso de apocalipse — o vídeo é uma lista prática de quatro técnicas para transformar esse tipo de checklist num gate real de CI.

## Por que isso está acontecendo agora: os números por trás do tweet

O tweet de Uncle Bob reage a uma matéria: *"Tech experts shift from coding to auditing AI-generated software"* — desenvolvedores estão virando auditores de código de IA. Dados citados no vídeo:

- Um estudo (referência a benchmark tipo SWE-bench) mostra taxa de sucesso de modelos subindo de **4,4% em 2023** para **mais de 70% em 2026**.
- Survey do Pragmatic Engineer, no começo do ano, mostrava taxa de aceitação de código gerado em torno de **30% a 55%** — número crescente, com metade do diff médio já não sendo mais digitada por humano.

O argumento central de Uncle Bob, na leitura do autor: se metade do código é da máquina, a pergunta parou de ser "esse for loop está bonito?" e virou "esse código passa em cinco provas objetivas?" — provas que não exigem leitura humana e rodam no CI em ~30 segundos.

## Técnica 1 — Complexidade ciclomática (CCN)

Complexidade ciclomática conta quantos **caminhos** existem dentro de uma função: um `if` abre um caminho, um `else` abre outro, uma chamada a outra função pode abrir mais caminhos ainda, e cada caminho novo soma ao total.

Por que isso importa especificamente para código gerado por LLM: modelos tendem a escrever funções longas (o exemplo citado é ~120 linhas) com muitos `if`s aninhados para tentar cobrir todos os casos. Isso é fácil de capturar automaticamente: definir um limite de CCN (o exemplo citado é 1–20) e bloquear o merge do PR se o número for ultrapassado.

Ferramenta citada pelo autor como já usada por ele: **SonarQube**, comum em times de QA. O vídeo pede sugestões de outras ferramentas equivalentes integradas a fluxos com IA.

## Técnica 2 — Cobertura de teste + mutation testing

Uncle Bob citou essas duas métricas juntas de propósito, porque uma sozinha não basta:

- **Cobertura de teste** diz quanto do código está tocado por algum teste.
- **Mutation testing** muta o código (troca `>` por `<`, `+` por `-`, `true` por `false`, etc.) e verifica se algum teste existente falha com a mutação. Se nenhum teste falhar, aquela mutação **sobreviveu** — e uma mutação sobrevivente é, na prática, um bug que nenhum teste detecta.

Ferramenta citada: **mutmut** (`pip install mutmut`, ecossistema Python). Exemplo dado: de 400 mutações geradas, 50 sobrevivem — essas 50 são o próximo sprint de testes. Metas de exemplo citadas pelo autor: 85% de cobertura + 60% de mutation score.

## Técnica 3 — Tamanho de módulo

Serve para evitar "god files" — arquivos de 3.000 a 5.000 linhas. Proposta: definir um limite (exemplo citado: 300 linhas por arquivo) e bloquear o CI se for ultrapassado.

## Técnica 4 — Estrutura de dependências (dependency structure)

Detecta acoplamento indevido entre módulos. Problemas citados como alvo dessa análise:

- **Import circular**: arquivo A importa arquivo B que importa arquivo A.
- **Camadas invertidas**: por exemplo, um controller chamando um model diretamente, pulando a camada de serviço.
- **Módulo de implementação chamando módulo de implementação de outro módulo diretamente**, quando deveria acessar por meio de um **módulo de API** exposto propositalmente para consumo externo — em vez do módulo de implementação de um lado acessar direto a implementação interna do outro.

O autor liga essa técnica de volta à técnica 3 (tamanho de módulo): ambas miram o mesmo problema de fundo, que é módulos malformados e mal isolados.

## Fechamento: o motivo real por trás da concordância com Uncle Bob

O autor admite abertamente sua motivação prática: não tem mais tempo de revisar código linha a linha. Sua preocupação recente tem sido como continuar gerando ~10.000 linhas de código por dia sem conseguir revisar essas mesmas 10.000 linhas por dia — e a conclusão dele é que **não dá**, não tem como escalar revisão manual nesse ritmo.

Isso não significa abandonar qualidade — significa realocar o esforço de qualidade para o pipeline de CI/CD: as quatro técnicas acima, mais análise de vulnerabilidade de pacotes, cobertura de teste unitário, instrumentation test, pain test, entre outras. O vídeo termina pedindo que espectadores comentem quais ferramentas usam para automatizar essas checagens antes de mergear um PR gerado por IA.
