---
type: source
title: "Organizando Equipes de Tecnologia — Fábio Akita"
aliases: ["equipes mistas sênior-júnior", "pedreiro vs mestre de obras", "body shop vs empresa de desenvolvimento"]
date_created: 2026-08-26
date_updated: 2026-08-26
source_file: raw/organizando-equipes-de-tecnologia-fabio-akita.md
source_url: ""
author: "Fábio Akita"
date_published: ""
date_ingested: 2026-08-26
source_count: 1
tags: [carreira, liderança, mentoria, contratação, cultura, mercado-de-trabalho, ciclo-economico, senior, junior]
skill: tech-mentor-leadership
status: draft
---

## TL;DR

Entrevista/bate-papo com [[wiki/entities/fabio-akita]] sobre como montar equipes de tecnologia: nem só sêniors, nem só júniors — o time ideal é sempre misto, com o sênior orientando 2-3 júniors (escalabilidade horizontal de pessoas) via feedback diário e honesto, não elogio vazio. A segunda metade traça um paralelo entre o mercado aquecido atual e a bolha da internet de 2000-2001: contratação como métrica de vaidade para investidores, "cultura" como manifesto de parede em vez de comportamento real, e o contraste Google (eficiência nascida da escassez) vs. Cadê/kd.com.br (modelo manual insustentável sem dinheiro sobrando).

## Key Claims

**Claim:** Uma equipe só de sêniors — ou só de júniors — não funciona bem para a maioria dos casos; o time ideal é sempre misto.
**Evidence:** Metáfora do pedreiro vs. mestre de obras: um sênior forçado a fazer tarefas rotineiras (tela simples, CSS) é improdutivo nelas — um júnior faz mais rápido porque é o trabalho dele no dia a dia. Um júnior sozinho, sem orientação, comete erros não por incompetência, mas porque é da natureza de qualquer pessoa errar numa área ainda não dominada.
**Confidence:** alta (mas é opinião/experiência pessoal do autor, não estudo formal)

**Claim:** Sênior orientando júniors é "escalabilidade horizontal" de pessoas — mais eficiente que o sênior tentar escalar sozinho ("escalabilidade vertical").
**Evidence:** Sênior já testou várias opções ao longo da carreira e sabe filtrar rápido para as 1-2 que valem a pena; um júnior sem essa experiência testaria todas as opções, levando tempo desproporcional. Delegar esse filtro multiplica a produtividade da equipe.
**Confidence:** média-alta — analogia útil, sem dado quantitativo de produtividade real

**Claim:** Feedback de verdade é diário e específico ("essa linha vai dar problema em produção"), não elogio genérico ("você está indo bem").
**Evidence:** Sinal de que está indo bem: o código para de ser barrado em revisão. Sinal de que falta estudo: o código volta toda vez — e a pergunta certa nesse caso é "o que devo estudar para não repetir esse erro?".
**Confidence:** alta, consistente com [[wiki/concepts/mentoria-tecnica]] e [[wiki/concepts/one-on-one]] já documentados na wiki

**Claim:** O momento de mercado aquecido (muita liquidez, todos os canais de recrutamento saturados) gera contratação por métrica de vaidade — headcount e "usuários" no lugar de receita/lucro — e isso se repete ciclicamente, como na bolha da internet de 2000-2001.
**Evidence:** Empresas oferecendo salário de sênior para júnior; propaganda de curso prometendo virar sênior em 6 meses; Body Shops vendendo júnior com currículo florido a preço de sênior por falta de mão de obra disponível. Paralelo histórico: mercado pré-2001 pagando salários "astronômicos" sem correlação com valor gerado, corrigido bruscamente quando o investimento secou e as empresas terceirizaram para a Índia por eficiência de custo.
**Confidence:** média — narrativa histórica plausível e consistente com [[wiki/concepts/ciclo-de-mercado-tech]], mas sem dado quantitativo citado na fonte

**Claim:** Quantidade de pessoas numa equipe é frequentemente o oposto de eficiência, por causa do overhead de coordenação entre elas.
**Evidence:** Custo de coordenação cresce mais rápido que o número de pessoas (2 pessoas = 1 canal; N pessoas = combinação crescente de canais). Isso gera estruturas piramidais de gestão que não produzem diretamente. Cortar parte do time pode não reduzir a eficiência, porque elimina esse overhead.
**Confidence:** média-alta — raciocínio análogo à lei de Brooks (não citada nominalmente na fonte), mas apresentado como observação empírica do autor, não como referência formal

**Claim:** O Google nasceu de restrição de recursos (PageRank + máquinas baratas), enquanto o Cadê (kd.com.br) dependia de um modelo manual (diretório com centenas de pessoas cadastrando páginas) que só se sustentava com dinheiro sobrando.
**Evidence:** Contraste histórico apresentado pelo autor como exemplo de "eficiência nascida da escassez" vs. modelo dependente de capital abundante que quebra quando o dinheiro seca.
**Confidence:** média — plausível e coerente com a história pública do Google, mas apresentado sem fonte primária dentro da própria fala; tratar como `[external, não verificado nesta fonte]` até checagem cruzada

**Claim:** "Cultura corporativa" como manifesto escrito na parede é, na prática, majoritariamente marketing de atração de talento — cultura real é comportamento, evolui com o tempo, e muda mais com a liderança do que com o texto oficial.
**Evidence:** Exemplo citado: mudança de comportamento observável na Microsoft entre a era pré e pós-Satya Nadella, mesmo com o texto oficial de cultura praticamente inalterado.
**Confidence:** média — opinião fundamentada, exemplo pontual, sem dado sistemático

## Entities & Concepts Touched

- [[wiki/entities/fabio-akita]]
- [[wiki/concepts/equipe-mista-senior-junior]]
- [[wiki/concepts/escalabilidade-vertical-vs-horizontal-de-pessoas]]
- [[wiki/concepts/feedback-continuo-diario]]
- [[wiki/concepts/overhead-de-coordenacao-tamanho-de-equipe]]
- [[wiki/concepts/cultura-corporativa-vs-manifesto-na-parede]]
- [[wiki/concepts/body-shop-terceirizacao]]
- [[wiki/concepts/ciclo-de-mercado-tech]]
- [[wiki/concepts/custo-de-capital-e-contratacao-tech]]
- [[wiki/concepts/contratacao-barra-alta]]
- [[wiki/concepts/mentoria-tecnica]]
- [[wiki/concepts/apagao-de-seniors]]
- [[wiki/concepts/vaga-junior-vira-pleno]]

## Open Questions

- O ano/contexto exato da gravação é incerto (a fala sobre pandemia e promessas de relocação sugere ~2020-2021, mas não é afirmado explicitamente) — datar com precisão ajudaria a calibrar se os exemplos de mercado aquecido ainda se aplicam ao ciclo atual (2026).
- O contraste Google vs. Cadê é apresentado de memória, sem fonte citada — vale checagem cruzada externa antes de tratar como fato consolidado na wiki.
- Não fica claro na transcrição quem é o interlocutor/entrevistador (citado uma vez como "Guilherme") nem em qual canal a conversa foi originalmente publicada — marcado como incerto ao longo do texto.

## Raw Quotes

> "Um time só de sêniors, ou um time só de júniors — nenhum dos dois funciona. Você precisa sempre de um time misto."

> "Feedback não é só dizer 'você está indo bem'. Isso não é feedback."

> "Quantidade de pessoas é diretamente oposto à eficiência, porque quanto mais pessoas, mais esforço de coordenação entre elas."

> "Cultura não é um manifesto escrito em pedra — cultura evolui com o tempo."

## Key Sources

(fonte nova — nenhuma outra fonte ainda cita esta página)
