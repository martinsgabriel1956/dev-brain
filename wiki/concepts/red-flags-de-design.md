---
type: concept
title: "Red Flags de Design"
aliases: ["design red flags", "sinais de alerta de design", "code smell (ousterhout)"]
date_created: 2026-07-10
date_updated: 2026-11-25
source_count: 7
tags: [design, code-review, ousterhout, complexidade, qualidade]
skill: tech-mentor-backend
status: draft
---

# Red Flags de Design

## TL;DR

Método prático de [[wiki/entities/john-ousterhout]] para reconhecer complexidade desnecessária: um red flag é um sinal de que um trecho de código provavelmente é mais complicado do que precisa ser. Ao ver um, a resposta é parar e procurar um design alternativo que elimine o problema — mesmo que isso exija testar várias alternativas antes de achar uma boa.

## Por que via code review, não introspecção

Princípios de design abstratos são difíceis de aplicar olhando só para o próprio código — é mais fácil ver problemas de design no código de outra pessoa do que no próprio. Por isso o método recomendado é usar os red flags durante [[wiki/concepts/code-review]]: identificar o sinal, sugerir a melhoria, e no processo se expor a novas abordagens de design.

## O ciclo de aprendizado

1. Ver o red flag (ou no próprio código, ou revisando o de outra pessoa).
2. Parar e procurar um design alternativo que elimine o problema — não aceitar o primeiro que aparece.
3. Testar várias alternativas se necessário; quanto mais alternativas testadas antes de corrigir, mais se aprende.
4. Com o tempo, o código tende a ter cada vez menos red flags, e a experiência revela novos red flags não catalogados previamente.

## Limite do princípio

Todo red flag e todo princípio de design tem exceções — levar qualquer ideia ao extremo tipicamente piora o resultado. Design bonito é equilíbrio entre ideias concorrentes, não aplicação mecânica de regras.

## Catálogo completo (Summary of Red Flags, apêndice do livro)

[[wiki/sources/filosofia-do-design-de-software-livro-completo]] traz, no apêndice final, a lista consolidada de todos os red flags nomeados ao longo do livro. Reproduzida aqui (paráfrase, não citação literal) por ser referência prática de consulta rápida durante code review:

| Red Flag | O que sinaliza | Capítulo |
|---|---|---|
| **Shallow Module** | Interface de uma classe/método não é muito mais simples que sua implementação | 4 |
| **Information Leakage** | Uma decisão de design se reflete em múltiplos módulos | 5 |
| **Temporal Decomposition** | Estrutura do código segue a ordem de execução, não o conhecimento necessário | 5 |
| **Overexposure** | API força quem usa um recurso comum a conhecer recursos raramente usados | 5 |
| **Pass-Through Method** | Um método só repassa argumentos para outro de assinatura quase idêntica | 7 |
| **Repetition** | Um trecho de código não trivial se repete várias vezes | 9 |
| **Special-General Mixture** | Código de propósito especial não está separado do código de propósito geral | 9 |
| **Conjoined Methods** | Dois métodos têm tantas dependências entre si que só dá para entender um lendo o outro | 9 |
| **Comment Repeats Code** | Toda a informação do comentário já é óbvia a partir do código ao lado | 13 |
| **Implementation Documentation Contaminates Interface** | Comentário de interface descreve detalhes de implementação desnecessários para quem só usa a coisa documentada | 13 |
| **Vague Name** | Nome de variável/método é tão genérico que não carrega informação útil | 14 |
| **Hard to Pick Name** | É difícil achar um nome preciso e intuitivo para algo — sinal de que o design subjacente pode não estar limpo | 14 |
| **Hard to Describe** | Para ser completo, o comentário de uma variável ou método precisa ser longo | 15 |
| **Nonobvious Code** | O comportamento ou significado de um trecho de código não é fácil de entender rapidamente | 18 |

## Linhagem paralela: Code Smells (Fowler)

[[wiki/concepts/code-smells]] é o vocabulário equivalente da linhagem Fowler/*Refactoring*, não uma continuação direta deste catálogo de Ousterhout. Os dois compartilham o mesmo espírito central — um sinal a investigar, não uma regra determinística a aplicar cegamente — e há sobreposição parcial de conteúdo: **Repetition** (red flag, item da tabela acima) cobre o mesmo território que [[wiki/concepts/dry]]; **Information Leakage** é próximo de [[wiki/concepts/feature-envy]] (uma classe acessando dados internos de outra); **Vague Name** e **Hard to Pick Name** se sobrepõem parcialmente com o smell "números mágicos" quando o problema é falta de um nome, não falta de nome preciso. Nenhum dos dois catálogos é subconjunto do outro — cada um nomeia sinais que o outro não cobre (ex.: [[wiki/concepts/god-object]], [[wiki/concepts/data-clumps]] e [[wiki/concepts/primitive-obsession]] não aparecem nesta lista de red flags).

## Shallow Module na Prática: A API de I/O do Java

[[wiki/sources/filosofia-design-software-podcast-eduardo-matos-otavio-santana-mauricio-linhares]] traz um exemplo real e recorrente do red flag **Shallow Module** citado como referência até hoje pelo comitê executivo do Java: a API de I/O (`java.io`) exige compor manualmente uma cadeia de classes (`FileInputStream` → `BufferedInputStream` → `ObjectInputStream`) para uma operação comum — abrir e ler um arquivo com buffer — porque foi desenhada priorizando opções de otimização sobre um caminho simples para o caso comum. Ver detalhamento em [[wiki/concepts/modulo-profundo]].

## Relação com outros conceitos

- [[wiki/concepts/code-review]] — o veículo prático recomendado para exercitar o reconhecimento de red flags.
- [[wiki/concepts/modulo-profundo]] — módulo raso é, na prática, um dos red flags mais citados no livro (interface complexa demais para a funcionalidade que expõe).
- [[wiki/concepts/complexidade-acidental]] — red flags são heurísticas para detectar complexidade acidental antes que ela se acumule.
- [[wiki/concepts/ocultamento-de-informacao]] — Information Leakage e Temporal Decomposition são os red flags específicos desse conceito.
- [[wiki/concepts/comentarios-como-ferramenta-de-design]] — Comment Repeats Code, Implementation Documentation Contaminates Interface e Hard to Describe são os três red flags de comentários.
- [[wiki/concepts/naming]] — Vague Name e Hard to Pick Name.
- [[wiki/concepts/sintomas-de-complexidade-ousterhout]] — red flags detectam as causas estruturais que produzem os três sintomas (change amplification, cognitive load, unknown unknowns).

## "Sinais de alerta" na tradução revisada

[[wiki/sources/filosofia-do-design-de-software-cap-01-traducao-revisada]] traduz *red flags* como "sinais de alerta". Uma nota do tradutor os define como "antipadrões ou cheiros no código (*code smells*)". Isso vai além do livro: pela seção "Linhagem paralela" acima, os dois catálogos só se sobrepõem em parte, e vários red flags (Pass-Through Method, Conjoined Methods, Comment Repeats Code) não têm smell equivalente em Fowler. A mesma tradução preserva o aparte de Ousterhout pedindo novos sinais aos leitores, de modo que o catálogo é aberto por intenção do autor.

## O quadro de Módulo Raso no texto do cap. 4

[[wiki/sources/filosofia-do-design-de-software-cap-04-modulos-devem-ser-profundos]] traz o quadro do sinal de alerta em primeira mão (4.5): módulo raso é aquele "cuja interface é complicada em relação à funcionalidade que ele fornece", e o benefício de não aprender como ele funciona por dentro é anulado pelo custo de aprender a interface. Fecha com "módulos pequenos tendem a ser rasos". O exemplo que o livro põe junto do quadro é o método `addNullValueForAttribute`, de uma linha só. O I/O do Java, que a seção acima atribui a este red flag a partir do podcast, aparece no livro na 4.7 como [[wiki/concepts/classite]] e como falha em tornar o caso comum simples. As duas leituras são compatíveis, porque a classite produz classes rasas.

## Os três quadros do cap. 5 no texto (2026-11-25)

[[wiki/sources/filosofia-do-design-de-software-cap-05-ocultacao-de-informacao-e-vazamento]] traz os quadros de **Vazamento de Informação**, **Decomposição Temporal** e **Superexposição** ([[wiki/concepts/decomposicao-temporal]], [[wiki/concepts/ocultamento-de-informacao]]). O texto chama o vazamento de "um dos principais sinais de alerta" e diz que a melhor habilidade de um designer é ter alta sensibilidade a ele. Duas notas da tradução: os dois primeiros quadros saem como "Sinal de Alerta" e o terceiro como "Bandeira Vermelha", embora o original use *Red Flag* nos três; e cada quadro aparece uma seção depois do tema (vazamento na 5.3, decomposição temporal na 5.4), provável efeito do layout do livro.

## Key Sources

- [[wiki/sources/filosofia-do-design-de-software-introducao]]
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]] — catálogo completo dos 14 red flags nomeados no livro (apêndice "Summary of Red Flags")
- [[wiki/sources/9-code-smells-como-identificar-codigo-ruim]] — catálogo paralelo de 9 code smells (linhagem Fowler), com sobreposição parcial (Repetition ≈ DRY, Information Leakage ≈ feature envy) mas cobrindo sinais distintos (god object, data clumps, primitive obsession)
- [[wiki/sources/filosofia-design-software-podcast-eduardo-matos-otavio-santana-mauricio-linhares]] — exemplo real recorrente de Shallow Module (API de I/O do Java), citado pelo comitê executivo do Java como erro de design reconhecido
- [[wiki/sources/filosofia-do-design-de-software-cap-01-traducao-revisada]] — tradução revisada da 1.1; a N.T. iguala red flags a code smells (discutido acima)
- [[wiki/sources/filosofia-do-design-de-software-cap-04-modulos-devem-ser-profundos]] — quadro de Módulo Raso (4.5) e seu exemplo original, `addNullValueForAttribute`
- [[wiki/sources/filosofia-do-design-de-software-cap-05-ocultacao-de-informacao-e-vazamento]] — texto dos quadros Vazamento de Informação, Decomposição Temporal e Superexposição
