---
type: source
title: "O Que Diferencia um Dev Pleno de um Júnior — Decisões, Legibilidade e Modelagem"
aliases: ["pleno vs júnior forma de pensar", "calcularDesconto júnior pleno", "código lido mais vezes do que escrito"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 0
tags: [carreira, pleno, junior, clean-code, legibilidade, naming, modelagem-de-dominio, java, ia-para-devs]
skill: tech-mentor-leadership
status: draft
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/o-que-diferencia-pleno-de-junior-decisoes-legibilidade-modelagem.md
source_url: ""
author: "não identificado (professor de Java, canal não informado)"
date_published: ""
date_ingested: 2026-09-30
---

## TL;DR

Um professor de Java responde à pergunta "o que aprender para virar pleno?" contrariando a resposta-padrão (lista de Spring Boot, Docker, Kafka, Kubernetes): tecnologias são **meios**, e o que separa pleno de júnior, com a mesma stack e a mesma sintaxe dominada, é **como se decide** ao escrever código. Três exemplos: (1) `calcularDesconto` com `if (isVip)` funciona, mas o pleno antecipa ouro/prata/sazonalidade e modela para a regra mudar; (2) `double d` vs. `valorDescontoPedido` — [[wiki/concepts/naming]] importa porque "o código será muito mais lido do que escrito"; (3) uma classe `Produto` com setters aceita preço/estoque negativo — classes são [[wiki/concepts/classe-como-conceito-de-dominio|conceitos do negócio]], não estruturas de dados. A transição acontece quando o raciocínio muda (ver [[wiki/concepts/transicao-junior-pleno-forma-de-pensar]]); IA pode gerar o código, desde que se entenda o que ela gera e a regra de negócio.

## Key Claims

**Claim:** Listas de tecnologias não transformam júnior em pleno; o diferencial é a forma de decidir ao desenvolver.
**Evidence:** Argumento do autor; comparação de duas pessoas na mesma stack/ticket — uma entrega código simples e compreensível, a outra entrega código com biblioteca de terceiros "cheio de problemas", ambas dominando a sintaxe.
**Confidence:** média — opinião de ensino, sem dado empírico; consistente com [[wiki/sources/o-que-esperam-de-pleno-2026-revisao]] (itens técnicos viram commodity; julgamento e soft skills permanecem) e com [[wiki/sources/formar-para-pleno-nao-junior-mercado-fundamentos-livros-algoritmos]].

**Claim:** O pleno projeta para a **variação futura da regra de negócio** (VIP → ouro/prata, sazonalidade); um `if/else` simples hoje vira cascata de condicionais amanhã.
**Evidence:** Exemplo `calcularDesconto` (15% VIP, 5% demais). O autor não mostra a modelagem alternativa na transcrição (o código estava só na tela).
**Confidence:** média — o princípio é coerente com [[wiki/concepts/open-closed-principle]] e [[wiki/concepts/strategy-pattern]] [skill: tech-mentor-leadership, `software-craftsmanship.md` lista SOLID/Clean Code), mas a solução concreta não foi dita; ver tensão com antecipação excessiva em [[wiki/concepts/antecipar-variacao-de-regra]].

**Claim:** "O código será muito mais vezes lido do que escrito" — projetos duram anos (Netflix, ~15; ERP, ~20) e há rotatividade de pessoas.
**Evidence:** Máxima conhecida de engenharia de software citada pelo autor; os números de longevidade são ilustrativos.
**Confidence:** alta como princípio aceito; ver [[wiki/concepts/codigo-lido-mais-que-escrito]].

**Claim:** Nome de variável legível (`valorDescontoPedido` em vez de `d`) é decisivo em métodos longos: na linha 533 de um método de 1000 linhas, a declaração está fora de vista e a variável é alterada várias vezes.
**Evidence:** Exemplo didático. O autor admite que método de 500–1000 linhas "já estaria errado".
**Confidence:** alta — coerente com [[wiki/concepts/naming]]; nuance [external]: em métodos curtos o escopo reduz o problema, e o remédio primário é o método pequeno.

**Claim:** Classe `Produto` com campos primitivos e setters permite estado inválido (`setPreco(-30)`, `setEstoque(-30)`); esse objeto "nunca deveria existir" para o negócio.
**Evidence:** Exemplo `Produto(String nome, double preco, int estoque)`.
**Confidence:** alta — é o argumento de [[wiki/concepts/encapsulamento]] ("proteger o estado inválido", [[wiki/sources/encapsulamento-proteger-estado-invalido]]) e [[wiki/concepts/primitive-obsession]]; ver [[wiki/concepts/classe-como-conceito-de-dominio]].

**Claim:** Conhecer novidades da linguagem (streams, generics, `Optional`, virtual threads do Java 25) só ajuda quando se entende o problema que resolvem e suas limitações.
**Evidence:** Afirmação do autor; ele não nega que se deva estudá-las.
**Confidence:** média-alta; "virtual threads" vem de "virtual trades" na transcrição (corrigido por contexto).

**Claim:** Uso de IA é aceitável (copiar/colar) desde que o dev entenda o que foi gerado e a regra de negócio do produto.
**Evidence:** Fechamento do vídeo.
**Confidence:** média; alinhado a [[wiki/concepts/ia-como-amplificador]] e [[wiki/concepts/dev-e-negocio]].

## Entidades e Conceitos

- Novos: [[wiki/concepts/transicao-junior-pleno-forma-de-pensar]], [[wiki/concepts/codigo-lido-mais-que-escrito]], [[wiki/concepts/antecipar-variacao-de-regra]], [[wiki/concepts/classe-como-conceito-de-dominio]]
- Existentes: [[wiki/concepts/naming]], [[wiki/concepts/encapsulamento]], [[wiki/concepts/primitive-obsession]], [[wiki/concepts/anemic-domain-model]], [[wiki/concepts/open-closed-principle]], [[wiki/concepts/strategy-pattern]], [[wiki/concepts/codigo-para-o-mantenedor]], [[wiki/concepts/codigo-para-o-futuro-eu]], [[wiki/concepts/equipe-mista-senior-junior]], [[wiki/concepts/soft-skills-como-diferencial-de-pleno]], [[wiki/concepts/vaga-junior-vira-pleno]], [[wiki/concepts/ia-como-amplificador]], [[wiki/concepts/dev-e-negocio]], [[wiki/concepts/validacao-de-entrada]]
- Autor/canal não identificado: sem página de entidade.

## Open Questions

- Qual modelagem o autor considera "de pleno" para o desconto (Strategy, tabela de regras, polimorfismo)? Não consta na transcrição.
- Onde fica o limite entre antecipar mudanças e over-engineering (YAGNI)? Ver [[wiki/concepts/antecipar-variacao-de-regra]].
- O vídeo trata só de legibilidade/modelagem; omite testes, comunicação e ownership, que a skill lista como sinais de Mid (testes sem ser pedido, reviews úteis, edge cases) [skill: tech-mentor-leadership, `engineering-levels-ladder.md`].

## Quotes

> "O código será muito mais vezes lido do que escrito."

> "A quantidade de tecnologias que tu conhece não vai fazer tu ser destaque… o que vai fazer tu ser destaque é o teu raciocínio."

> "Essa transição… não acontece no momento em que você aprende um framework… ela acontece quando a sua forma de pensar começa a mudar."
