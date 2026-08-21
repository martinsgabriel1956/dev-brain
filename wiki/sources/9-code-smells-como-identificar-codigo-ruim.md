---
type: source
title: "9 Code Smells — Como Identificar que seu Código Pode Estar Piorando"
aliases: ["9 sinais de código ruim", "code smells vídeo", "funções longas god objects feature envy"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_file: "raw/9-code-smells-como-identificar-codigo-ruim.md"
source_url: ""
author: "não identificado (vídeo YouTube, português)"
date_published: ""
date_ingested: 2026-08-18
source_count: 0
tags: [code-smells, clean-code, refactoring, acoplamento, coesao, feature-envy, primitive-obsession, dry, god-object, craftsmanship]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Vídeo que cataloga nove code smells clássicos (linhagem Fowler/*Refactoring*, embora o autor não cite a fonte diretamente), cada um julgado pela mesma régua declarada no início: um bom código é compreensível, testável, com baixo acoplamento, alta coesão, modular e de fácil manutenção. Reforça explicitamente que smell não é bug nem prova determinística de código ruim — é sinal a considerar, não regra a aplicar cegamente. Cobre: funções muito longas, [[wiki/concepts/god-object|god objects]], [[wiki/concepts/dry|DRY]] (com uma posição deliberadamente contrária ao dogma), condicional gigante, números mágicos, [[wiki/concepts/feature-envy|feature envy]], [[wiki/concepts/data-clumps|grupos de dados]], comentários inúteis e [[wiki/concepts/primitive-obsession|uso exacerbado de tipos primitivos]]. Fecha com o mesmo aviso central de [[wiki/concepts/red-flags-de-design]]: aplicar pensamento crítico, não seguir exemplos específicos como regra rígida.

## Key Claims

**Claim:** Um bom código, na definição do autor, tem seis propriedades: compreensível, testável, baixo acoplamento, alta coesão, modular e de fácil manutenção — e é essa régua (não "código que dá dinheiro") que define se um smell é ou não um problema real num caso concreto.
**Evidence:** Declarado explicitamente como opinião pessoal do autor logo no início, antes de detalhar os nove smells; usado consistentemente para julgar cada smell ao longo do vídeo (ex.: "compreensível? testável? de fácil manutenção? se sim às três, não tem problema").
**Confidence:** alta quanto à consistência interna do vídeo — é a régua que o próprio autor aplica; é opinião declarada, não fato objetivo, e converge fortemente com os critérios já registrados em [[wiki/concepts/acoplamento]], [[wiki/concepts/coesao]] e [[wiki/concepts/refatoracao]].

**Claim:** Funções muito longas tendem a ser difíceis de compreender, testar e manter — mas isso não é determinístico; a recomendação é checar se a função é compreensível, testável e de fácil manutenção antes de decidir refatorar só por causa do tamanho.
**Evidence:** Argumento de carga cognitiva (difícil manter o contexto inteiro de uma função longa na cabeça) e de dificuldade prática de escrever teste para função muito longa.
**Confidence:** média-alta — consistente com o framework de [[wiki/concepts/tech-debt-como-ferramenta]] (nem todo smell exige ação imediata), mas o vídeo não cita um limite objetivo de linhas (diferente de [[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]], que propõe gate de CI com limite numérico).

**Claim:** God objects (ex.: uma classe `SystemManagement` fazendo autenticação, banco de dados e notificações) ainda podem ser compreensíveis e "mais ou menos" testáveis isoladamente — o problema real está em acoplamento altíssimo e baixa coesão, não em ilegibilidade. A solução recomendada é composição: injetar serviços especializados (autenticação, banco, notificação) na classe maior, permitindo substituir cada um sem afetar os outros.
**Evidence:** Exemplo de código com `UserManagement` recebendo três serviços por injeção de dependência como contraste direto ao god object.
**Confidence:** alta — alinhado com [[wiki/concepts/god-object]] (já registrado: degradação incremental sprint a sprint) e com o padrão de composição/DI já coberto na skill de backend.

**Claim:** DRY (Don't Repeat Yourself) não deveria ser seguido como dogma absoluto — repetição é aceitável quando poucos pontos duplicam o mesmo código (o autor cita 2 lugares como aceitável, 3+ como problemático), e abstração prematura é pior do que repetição moderada. O critério de decisão não é "existe duplicação?" mas "o custo de manutenção da duplicação supera o custo de uma abstração ainda instável?".
**Evidence:** Exemplo de chamadas de API duplicadas em várias partes do código, com posição explícita e autodeclarada como "controversa" pelo autor.
**Confidence:** média-alta — é uma posição de opinião, não um fato verificável, mas converge com [[wiki/concepts/yagni]] e com o princípio geral de evitar abstração prematura já presente na wiki; o número exato de repetições tolerável (2 vs. 3+) é um limiar arbitrário do autor, não uma métrica validada externamente.

**Claim:** Condicionais gigantes (cadeias longas de if/elif combinando múltiplas dimensões, ex.: país × peso × método de entrega) são "mais ou menos" compreensíveis e sua principal rede de segurança é a cobertura de testes de 100% dos branches — sem isso, uma indentação errada pode quebrar o comportamento de forma sutil. Uma melhoria incremental (não perfeita) é substituir a cadeia por uma estrutura de dados (dicionário de "base rates" por categoria).
**Evidence:** Exemplo concreto em pseudo-Python de cálculo de frete, refatorado para um dicionário aninhado por país.
**Confidence:** média — exemplo ilustrativo bem construído, mas o próprio autor reconhece que a solução de dicionário "ainda não está perfeita" (a ligação entre faixa de peso e valor não fica plenamente explícita na estrutura).

**Claim:** Números mágicos (e "coisas mágicas" em geral, incluindo URLs/chaves de API hard-coded) prejudicam compreensão e manutenção porque uma busca textual pelo valor cru (ex.: `16`) não distingue ocorrências relacionadas de coincidências (ex.: `1600`), enquanto uma constante nomeada é buscável sem ambiguidade.
**Evidence:** Exemplo de `if user.age >= 16` com comentário "idade para tomar cerveja" substituído por uma constante nomeada `LEGAL_BEER_BUYING_AGE_GERMANY = 16`.
**Confidence:** alta — argumento de manutenibilidade é diretamente verificável e não depende de opinião; converge com [[wiki/concepts/naming]].

**Claim:** Feature envy — quando uma classe (ex.: `OrderPrinter`) acessa atributos internos de outra classe (`Order`, que por sua vez acessa `Product`) para calcular algo que deveria ser responsabilidade da classe possuidora dos dados — é descrito como o smell de acoplamento mais grave do vídeo ("mais acoplado que espaguete", "um nó"), porque quebra uma classe a duas camadas de distância ao renomear um único campo interno.
**Evidence:** Exemplo de domínio e-commerce (`Order.items`, `Product.price`, `Product.discount`) com `print_total()` calculando o total fora da classe `Order`; solução proposta é mover o cálculo para um método `get_total()` dentro da própria `Order`.
**Confidence:** alta — é o exemplo mais didaticamente sólido do vídeo e converge exatamente com a definição clássica de feature envy (Fowler) e com [[wiki/concepts/acoplamento]] e [[wiki/concepts/coesao]] já registrados na wiki.

**Claim:** Grupos de dados (data clumps) — variáveis que sempre aparecem juntas em várias assinaturas de função (ex.: nome, e-mail, idade) mas são passadas soltas em vez de agrupadas num tipo — dificultam evolução: trocar `idade` por `data_de_nascimento` exige caçar manualmente todos os lugares que recebem os três parâmetros soltos, enquanto agrupá-los num tipo nomeado (`Usuario`) faz o compilador/type-checker acusar automaticamente todos os pontos afetados.
**Evidence:** Exemplo com data class hipotética `Usuario(nome, email, idade)`.
**Confidence:** alta — argumento de manutenibilidade mecanicamente verificável (refatoração de tipo vs. busca textual), sem depender de opinião.

**Claim:** Um uso primitivo (string) de dados como e-mail ou dinheiro, sem tipo dedicado, resulta em validação duplicada ou inconsistente ao longo do sistema, porque uma string não carrega informação sobre se já foi validada. Criar um tipo dedicado (validado na entrada do sistema, convertido de volta na saída) elimina a necessidade de revalidar em cada ponto de uso.
**Evidence:** Exemplo de classe `Email` com validação no `__init__`, e menção paralela a um tipo dedicado para dinheiro (casting na entrada e na saída do sistema).
**Confidence:** alta — é o clássico "primitive obsession" da literatura de refactoring, com exemplo consistente e mecanismo de validação por construção (parse, don't validate) bem descrito.

## Entities & Concepts Touched

- [[wiki/concepts/code-smells]] (novo)
- [[wiki/concepts/god-object]]
- [[wiki/concepts/acoplamento]]
- [[wiki/concepts/coesao]]
- [[wiki/concepts/red-flags-de-design]]
- [[wiki/concepts/naming]]
- [[wiki/concepts/comentarios-como-ferramenta-de-design]]
- [[wiki/concepts/feature-envy]] (novo)
- [[wiki/concepts/primitive-obsession]] (novo)
- [[wiki/concepts/data-clumps]] (novo)
- [[wiki/concepts/dry]] (novo)
- [[wiki/concepts/refatoracao]]
- [[wiki/concepts/tech-debt-como-ferramenta]]

## Open Questions

- O vídeo não cita Fowler nem *Refactoring* como fonte da taxonomia, apesar de "feature envy", "data clumps" e "primitive obsession" serem termos exatos do livro — não fica claro se é reformulação independente ou omissão de crédito. Vale checar contra [[wiki/sources/refatoracao-pragmatic-programmer-martin-fowler-2a-edicao]] numa ingestão futura do livro original.
- O limiar numérico dado para DRY ("2 lugares ok, 3+ problemático") é apresentado sem qualquer validação externa — é uma heurística pessoal do autor, tratada aqui como tal, não como métrica objetiva.
- O vídeo contém um bloco de patrocínio (AUVP, investimentos) que usa por analogia os mesmos critérios de "bom design" para vender um produto financeiro — conteúdo comercial, não técnico, mantido apenas na transcrição bruta em `raw/` por fidelidade à fonte, sem relevância para a wiki.
