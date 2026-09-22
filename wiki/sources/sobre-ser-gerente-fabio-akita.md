---
type: source
title: "Sobre Ser Gerente"
aliases: ["sobre ser gerente akita", "gestão de projetos é gestão de pessoas", "o que é ser gerente"]
date_created: 2026-09-22
date_updated: 2026-09-22
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/sobre-ser-gerente-fabio-akita.md
source_url: ""
author: "Fábio Akita"
date_published: ""
date_ingested: 2026-09-22
source_count: 0
tags: [gestao-de-projetos, lideranca, engineering-management, estimativas, mentoria, pmbok, cargo-cult, agile]
skill: tech-mentor-leadership
status: stable
---

## TL;DR

Vídeo longo de [[wiki/entities/fabio-akita]] consolidando sua visão de gestão de projetos/pessoas: gerenciar é decidir com informação incompleta, não preencher planilha; PMP/PMBOK/MBA são caixas de ferramentas, não garantia de competência; a tríade escopo-tempo-custo tem uma quarta variável invisível — qualidade — que sempre cai quando se espreme as outras três; software não é linha de produção (o programador é arquiteto, não operário — quem executa mecanicamente é o compilador); só nível A contrata nível A; um gestor que nunca foi praticante nunca terá o respeito da equipe; gerenciar projetos é, na prática, gerenciar pessoas e gerenciar expectativas.

## Key Claims

**Claim:** Certificações (PMP, MBA) são "colecionar papel" — não ensinam a ser gestor, só dão vocabulário básico comum.
**Evidence:** Akita relata ter rasgado o próprio certificado PMP publicamente; compara o PMBOK a uma caixa de ferramentas — conhecer as ferramentas não torna ninguém carpinteiro. MBA critica como gerador de network, não de competência de gestão.
**Confidence:** alta (opinião do autor, não dado externo verificável)

**Claim:** A tríade clássica de projeto (escopo, tempo, custo) esconde uma quarta variável invisível: qualidade. Ao espremer tempo/custo mantendo escopo, qualidade cai — e os problemas gerados são empurrados para a fase de operação.
**Evidence:** Não é possível aumentar escopo sem aumentar tempo ou custo; como tempo/custo costumam ser fixos, o escopo é o que normalmente cede — mas quando se força os três fixos mesmo assim, quem cede sem ninguém perceber de imediato é a qualidade.
**Confidence:** alta — é reformulação de um framework de gestão de projetos amplamente aceito (Iron Triangle), com a adição pessoal da "quarta variável invisível"

**Claim:** Software não é engenharia de produção — o programador é arquiteto, não operário; quem executa mecanicamente (equivalente ao operário/músico de orquestra) é o compilador/interpretador.
**Evidence:** Duas construtoras com a mesma planta baixa constroem prédios equivalentes; dois programadores com a mesma especificação produzem códigos completamente diferentes — a especificação de software não converge como a de hardware, porque o próprio código É a especificação final.
**Confidence:** alta — mesmo argumento central já documentado em [[wiki/concepts/software-nao-e-engenharia-de-producao]] a partir de outra fonte do mesmo autor; esta fonte acrescenta a analogia do compilador como "operário automatizado" e a comparação orquestra clássica vs. jazz, ausentes na fonte anterior.

**Claim:** Só profissional nível A contrata outro nível A — um gestor que não é ele mesmo reconhecido como nível A tende a contratar nível C (quando precisava de A) ou dar tarefas de nível A para alguém nível C.
**Evidence:** Cadeia declarada sem dado externo: nível B só consegue reconhecer/contratar nível C, que só reconhece D, e assim por diante — auto-perpetuação da mediocridade quando o próprio gestor não é excelente.
**Confidence:** média — plausível e coerente com literatura de hiring bar (ver `references/leadership/engineering-hiring.md` do skill `tech-mentor-leadership`), mas apresentado como afirmação categórica sem evidência empírica citada.

**Claim:** Copiar a arquitetura/processo de empresas como Netflix ou Google sem ter o mesmo orçamento e a mesma escala é autoengano — essas empresas pagam profissionais nível A com orçamentos de milhões de dólares que a maioria dos projetos não tem.
**Evidence:** Comparação direta de budget e nível salarial entre grandes empresas de tecnologia e projetos comuns.
**Confidence:** alta — mesmo argumento central já documentado em [[wiki/concepts/cargo-cult-tecnologico]] a partir de outras fontes do mesmo autor ("compare-se com o dia um deles"); esta fonte acrescenta o ângulo específico de orçamento/nível salarial de equipe, não só de escala de usuários.

**Claim:** Confundir estimativa com previsão é o primeiro grande erro de gestão — são palavras diferentes porque significam coisas diferentes.
**Evidence:** "Muita gente ainda pede estimativa, mas na realidade está esperando previsão" — daí o atrito recorrente de "mas você disse que em duas semanas estaria pronto". O melhor tamanho de história é meio dia, no máximo dois ou três dias — mais que isso é épico e deve ser dividido.
**Confidence:** alta — coerente com a distinção formal estimativa vs. compromisso documentada em `references/engineering-management.md` do skill `tech-mentor-leadership` (T-Shirt sizing, PERT, comunicação de estimativas para stakeholders).

**Claim:** Um gestor precisa ter sido, ele mesmo, praticante da função que gerencia — um gestor não técnico nunca vai ter o respeito de uma equipe técnica, da mesma forma que um general que nunca foi soldado não é respeitado por soldados.
**Evidence:** Série de analogias (treinador de futebol que foi jogador, chef que foi descascador de batatas, general que foi soldado raso) para sustentar que respeito técnico não se conquista com "seminário de poucas semanas".
**Confidence:** média — é tese forte e categórica ("nem todo programador tem capacidade de virar gestor, mas certamente um gestor não técnico nunca vai saber o que é ser programador"), apresentada sem contraexemplos considerados; existem gestores tecnicamente não praticantes bem-sucedidos documentados na literatura de management (não citados pela fonte).

**Claim:** Métricas ruins corrompem comportamento — exemplo dado: medir "quantidade de bugs corrigidos" como métrica positiva incentiva criar mais bugs para depois corrigi-los.
**Evidence:** Anedota do autor sobre um lugar que media isso; ninguém se preocupa em não gerar bugs novos, porque a métrica premia corrigir, não prevenir.
**Confidence:** alta — instância direta e já bem documentada da Lei de Goodhart, ver [[wiki/concepts/goodharts-law]].

**Claim:** Terceirizar projetos novos para empresa terceira em vez de alocar os membros mais sêniores das próprias equipes é um erro recorrente — o caminho certo é alocar sêniores internos nos projetos novos e colocar terceiros (quando necessários) subordinados a eles, tratando-os como júnior.
**Evidence:** Ciclo proposto: sênior interno lidera projeto novo (com terceiros se necessário) → projeto passa para operação → sênior cria sucessor interno → sênior assume novo projeto, repetindo o ciclo. Times só-sênior são desperdício; times só-júnior são desastre à espera de acontecer.
**Confidence:** média-alta — coerente com [[wiki/concepts/equipe-mista-senior-junior]] e [[wiki/concepts/mentoria-tecnica]] já documentados a partir de outra fonte do mesmo autor; esta fonte acrescenta o ciclo explícito de "criar sucessor antes de assumir novo projeto" e a crítica direta à terceirização como primeira opção.

**Claim:** Confiança não é amizade — esconder erros de um colega achando que é lealdade prejudica tanto a equipe quanto a própria pessoa que erra, porque a rouba da chance de corrigir.
**Evidence:** Argumento de que feedback honesto dá à pessoa a chance de melhorar; quem se recusa a aceitar correção é quem, de fato, quebra a confiança.
**Confidence:** alta — coerente com modelo SBI de feedback documentado em `references/technical-mentoring.md` do skill `tech-mentor-leadership`.

## Entities & Concepts Touched

- [[wiki/entities/fabio-akita]]
- [[wiki/concepts/software-nao-e-engenharia-de-producao]]
- [[wiki/concepts/cargo-cult-tecnologico]]
- [[wiki/concepts/estimativas-de-software]]
- [[wiki/concepts/story-points]]
- [[wiki/concepts/scrum-master]]
- [[wiki/concepts/equipe-mista-senior-junior]]
- [[wiki/concepts/mentoria-tecnica]]
- [[wiki/concepts/goodharts-law]]
- [[wiki/concepts/apagao-de-seniors]]
- [[wiki/concepts/body-shop-terceirizacao]]
- [[wiki/concepts/gestao-de-riscos-e-controle-ilusorio]]
- [[wiki/concepts/triade-escopo-tempo-custo-qualidade]] (novo stub)
- [[wiki/concepts/nivel-a-contrata-nivel-a]] (novo stub)
- [[wiki/concepts/gestor-deve-ter-sido-praticante]] (novo stub)

## Open Questions

- A fonte afirma categoricamente que "nenhum gestor não técnico nunca vai saber o que é ser programador" — contraexemplos de gestores/executivos não técnicos bem-sucedidos existem na literatura de management geral; vale revisitar essa tese com uma fonte que defenda o lado oposto, se surgir.
- A anedota do PMP rasgado e a crítica ao MBA são posições pessoais fortes sem contraponto documentado na wiki — não há, até agora, nenhuma fonte defendendo valor prático de certificações formais de gestão para comparar.
- O trecho da transcrição sobre a analogia com *Peaky Blinders* está corrompido/ilegível na fonte original (ver nota no `raw/`) — o conteúdo específico dessa analogia não pôde ser capturado com confiança.

## Trecho Preservado

> "O problema é que o termo 'gerenciar projetos' é errado. Dizer que o objetivo é entregar o projeto está errado: você gerencia pessoas. Sua taxa de sucesso em projetos é diretamente proporcional ao seu bom relacionamento com suas equipes, e pessoas não são máquinas."

> "Como custo e tempo costumam ser os fatores limitantes, o que sempre precisa variar para menos é o escopo. [...] Quando se puxa o máximo de escopo num tempo pequeno cortando custos, a variável que naturalmente vai cair drasticamente é a qualidade. Essa é a quarta variável invisível."

> "O programador não é o operário — todo programador é tecnicamente um arquiteto."
