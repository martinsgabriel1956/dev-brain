---
type: source
title: "[Off-Topic] Agile: a Verdade por trás do Método"
aliases: ["agile a verdade por trás do método", "ágil exige boa equipe", "ágil como mecanismo de exposição"]
date_created: 2026-11-05
date_updated: 2026-11-05
source_count: 0
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/agile-a-verdade-por-tras-do-metodo-akita.md"
source_url: "https://www.akitaonrails.com/2014/09/28/off-topic-agile-a-verdade-por-tras-do-metodo/"
author: "Fabio Akita (AkitaOnRails.com)"
date_published: 2014-09-28
date_ingested: 2026-11-05
tags: [agile, scrum, extreme-programming, engineering-management, gestao-de-riscos, consultoria, open-source, contratacao]
skill: tech-mentor-leadership
status: draft
---

# [Off-Topic] Agile: a Verdade por trás do Método

**Formato:** post de blog de 2014, convertido de HTML para Markdown sem alteração de texto. O próprio autor o apresenta como introdução, sem solução, e deixa uma continuação em aberto.

## TL;DR

Partindo da declaração de [[wiki/entities/dave-thomas]] de que "Ágil" morreu, [[wiki/entities/fabio-akita]] separa as práticas de programação, sobre as quais diz não haver dúvida, do gerenciamento de projeto, onde as consultorias distorceram a ideia. Sua tese: nenhuma prática ágil salva uma equipe ruim. Elas servem para [[wiki/concepts/agil-como-exposicao-de-problemas|expor problemas cedo e reduzir risco]], e o problema exposto costuma ser de comportamento. Por isso, consertar uma equipe depressa exigiria trocar pessoas, compromisso que quase ninguém aceita. É a mesma linha do seu artigo de 2009 sobre o [[wiki/concepts/net-negative-producing-programmer|programador de produtividade líquida negativa]].

## Key Claims

1. **Dave Thomas, signatário do manifesto, declarou a morte de "Ágil" em 2014.** Evidência: o post de Thomas, de 04/03/2014, propõe aposentar a palavra, mas mantém os valores e defende a agilidade como prática ([external](https://pragdave.me/thoughts/active/2014-03-04-time-to-kill-agile.html)). Confiança: alta quanto ao fato. "Morte do Ágil" é a formulação de Akita; Thomas mira o termo.
2. **As práticas de programação não estão em debate; o problema é o processo de gestão.** Akita lista propriedade coletiva de código, integração contínua, [[wiki/concepts/tdd]], refatoração, [[wiki/concepts/yagni]] e [[wiki/concepts/user-stories|escopo]], e aponta o open source como exemplo. Chama de falso o embate entre [[wiki/concepts/modelo-cascata-vs-desenvolvimento-incremental|Waterfall e Agile]]. Evidência: observação do autor. Confiança: média, por ser opinião. A wiki registra uma crítica ao TDD, ver [[wiki/concepts/tdd]].
3. **Não contrate terceiros para "implementar metodologia".** Se for inevitável, avalie quanta experiência prática em código e no dia a dia o candidato tem. Evidência: experiência do autor, sem dados. Confiança: média.
4. **Ágil exige boa equipe, e boa equipe não quer dizer só de sêniores.** O critério é o compromisso com a prática, seja de júnior ou de sênior. Muitos dos tidos como sêniores ou "ninjas" seriam pouco comprometidos e arrogantes. Evidência: opinião. Confiança: média para o critério, baixa para a generalização sobre sêniores.
5. **A melhora inicial é só efeito da mudança.** Práticas novas alteram algo por um tempo, sem transformar uma equipe ruim. Evidência: nenhuma além do raciocínio do autor. Confiança: média-baixa.
6. **Programação é profissão de prática.** Um treinamento de dois dias não faz um artilheiro; só a prática contínua, com pequenas melhorias, talvez faça. Ver [[wiki/concepts/pratica-deliberada]]. Evidência: analogia. Confiança: média, com apoio de outras fontes da wiki.
7. **As práticas ágeis não eram novidade para quem programava nos anos 80 e 90; o novo foi o pacote comercial, sobretudo o Scrum, que sozinho não inclui as práticas de programação do [[wiki/concepts/extreme-programming|XP]].** Evidência: o Scrum Guide de 2020 não menciona TDD, pair programming, integração contínua nem refatoração ([external](https://scrumguides.org/scrum-guide.html)). O manifesto é de fevereiro de 2001 ([external](https://agilemanifesto.org/history.html)). Confiança: alta para a ausência no guia atual, sem conferir a versão vigente em 2014; média para o resto. Akita recomenda *The Cathedral and the Bazaar* e *The Mythical Man-Month* de [[wiki/entities/fred-brooks]] para ver a evolução anterior.
8. **Práticas ágeis surgem naturalmente entre bons programadores experientes e não ajudam uma equipe novata.** Evidência: opinião. Confiança: média-baixa. Ver tensão 2 abaixo.
9. **O open source expõe problemas de imediato e mata projetos muito mais depressa que o mundo comercial.** Akita o resume como a forma capitalista mais eficiente de manter commodities, movida por interesses como exposição e redução de custos. Evidência: nenhum número, e o exemplo de [[wiki/entities/linus-torvalds]] é contestado pelo próprio link citado. Confiança: baixa para a comparação quantitativa, média para a ideia geral.
10. **Práticas ágeis são mecanismos de exposição de problemas e de gestão de risco.** Encontrar o obstáculo quando ele surge e tratá-lo logo evita desperdício. Ver [[wiki/concepts/gestao-de-riscos-e-controle-ilusorio]]. Evidência: argumento conceitual. Confiança: alta como leitura do método, sem medição na fonte.
11. **Consertar uma equipe em pouco tempo significa substituir pessoas, às vezes todas. Quem implanta Ágil e não demite ninguém estaria errando.** Isso incluiria o gerente e o programador influente, mas de mau caráter, que Akita considera o tipo mais perigoso. Evidência: nenhuma além da experiência do autor. Confiança: baixa como regra geral. Ver tensão 3 abaixo.

> "Ágil foi feito para **expor** os problemas o quanto antes." (Fabio Akita)

## Entidades

- [[wiki/entities/fabio-akita]]: autor.
- [[wiki/entities/dave-thomas]]: gatilho do texto, com o post de 2014.
- [[wiki/entities/uncle-bob]]: Akita conta ter exposto a ele, na RailsConf 2010, sua teoria sobre a motivação da certificação de Scrum.
- [[wiki/entities/linus-torvalds]]: exemplo de que nem toda opinião pesa igual no open source.
- [[wiki/entities/fred-brooks]]: *The Mythical Man-Month* como leitura recomendada.
- Sem página própria: Ken Schwaber, criticado pela certificação de Scrum; Richard Bishop e Giles Bowkett, autores de textos críticos citados; Eric Raymond, autor de *The Cathedral and the Bazaar*, cujo nome o post não traz (`[external]`, conhecimento geral).

## Conceitos

- [[wiki/concepts/agil-como-exposicao-de-problemas]]: conceito novo desta fonte.
- [[wiki/concepts/net-negative-producing-programmer]]: conceito novo, citado pelo post e conferido no artigo de 2009.
- [[wiki/concepts/manifesto-agil-como-adjetivo]]
- [[wiki/concepts/accountability-em-equipes-ageis]]
- [[wiki/concepts/gestao-de-riscos-e-controle-ilusorio]]
- [[wiki/concepts/extreme-programming]]
- [[wiki/concepts/scrum-master]]
- [[wiki/concepts/pratica-deliberada]]
- [[wiki/concepts/disciplina-vs-talento]]
- [[wiki/concepts/equipe-mista-senior-junior]]

## Conexões e Tensões com a Wiki

**Reforça:** [[wiki/sources/agilidade-manifesto-agil-fabio-akita]] retoma, anos depois, a crítica às consultorias e a ideia de que nenhuma metodologia corrige gente. O risco aparece aqui como função do método e lá como núcleo da gestão de projetos. [[wiki/concepts/equipe-mista-senior-junior]] é compatível com o critério de compromisso em vez de senioridade.

**Tensões (a wiki não decide entre elas):**

1. **Talento.** Este post fala de quem não tem talento nem predisposição e não vai mudar. Já [[wiki/sources/akita-pratica-deliberada-mito-do-talento]] afirma que talento inato não existe. O próprio post insiste que só a prática forma o profissional, o que deixa a tensão também dentro do texto. Ver [[wiki/concepts/disciplina-vs-talento]].
2. **Iniciantes.** Aqui, as práticas ágeis não servem a uma equipe novata. Em [[wiki/sources/agilidade-manifesto-agil-fabio-akita]], TDD, integração contínua e design incremental são o que iniciantes devem buscar. As duas posições só se conciliam se "equipe novata" e "iniciante individual" forem casos diferentes, mas isso é inferência da wiki.
3. **Demissão.** `[skill: tech-mentor-leadership]` A referência sobre conversas difíceis trata o plano de melhoria como algo que nunca deve surpreender, precedido de feedback documentado e de suporte; a de turnaround começa por diagnóstico. Isso contrasta com trocar pessoas como critério de boa implantação. A diferença pode ser de horizonte, já que Akita fala em consertar "em pouco tempo".
4. **Vocabulário.** O post fala em "implementar" práticas ágeis, enquanto [[wiki/concepts/manifesto-agil-como-adjetivo]] registra a posição posterior de que não existe "implementar ágil". É mais uma mudança de formulação que de ideia: aqui Akita já escreve o termo entre aspas e evita os rótulos na própria empresa.

## Questões em Aberto

- A teoria sobre a motivação da certificação de Scrum não está escrita: o link leva a uma entrevista em vídeo, e o texto da página não cita Schwaber. Vídeo não assistido.
- A continuação prometida não foi identificada. Candidatos, não lidos, na tag `agile` do blog: "People over Processes" (21/11/2014) e a coletânea "Processos e Metodologias não vão te ajudar" (07/01/2015).
- Este post pode ou não ser o "Ágil está morto" (2014) mencionado em [[wiki/sources/agilidade-manifesto-agil-fabio-akita]]. Nenhum post com esse título aparece na tag `agile`. O mais próximo em nome é "Lean está morto, longa vida à eficiência" (27/03/2014), não lido.
- Não há dados sobre o resultado de trocar pessoas versus desenvolvê-las, nem sobre a taxa de morte de projetos open source.
- O link sobre Linus Torvalds trata de uma desenvolvedora do kernel pedindo que ele parasse de usar linguagem abusiva. O caso serve mal de prova de meritocracia, e só o título da URL foi visto; a página não foi lida.
