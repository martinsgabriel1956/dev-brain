---
type: source
title: "Agilidade e o Manifesto Ágil"
aliases: ["ágil está morto", "agilidade é ser adulto", "crítica ao movimento ágil akita"]
date_created: 2026-09-18
date_updated: 2026-09-18
source_count: 0
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/agilidade-manifesto-agil-fabio-akita.md"
source_url: ""
author: "Fábio Akita (Akita On Rails)"
date_published: "desconhecida (segundo episódio de uma série sobre profissão de prática)"
date_ingested: 2026-09-18
tags: [agile, manifesto-agil, scrum, extreme-programming, engineering-management, accountability, consultoria, estimativa, gestao-de-riscos]
skill: tech-mentor-leadership
status: draft
---

# Agilidade e o Manifesto Ágil

**Formato:** Transcrição de vídeo (fala corrida, sem pontuação, transformada em markdown estruturado antes da ingestão). Segundo episódio de uma série sobre "profissão de prática", já referenciando [[wiki/sources/pare-de-terceirizar-suas-decisoes]] como episódio anterior. Fonte já em português — nenhuma tradução foi necessária.

## TL;DR

Rant de [[wiki/entities/fabio-akita]] contra a indústria de consultoria/coaching ágil, argumentando que o termo "ágil" foi distorcido de adjetivo (um jeito de agir) em substantivo vendável (um pacote de cerimônias, certificações e ferramentas). Reconstrói a origem do [[wiki/entities/martin-fowler|Manifesto para o Desenvolvimento Ágil de Software]] (2001, Snowbird) e seus 17 signatários, apoiando-se numa palestra de [[wiki/entities/dave-thomas]] (GOTO 2015) para defender que "ágil" é um adjetivo, não um nome — não existe "fazer ágil", só "ser ágil". Argumenta que técnicas de engenharia de produção física (Lean, Kanban, Six Sigma, PERT) não se transferem para software porque software não tem restrições físicas, e que a indústria de consultoria ágil sobrevive vendendo processos de controle porque empresas têm medo de tomar decisões e assumir riscos. Fecha com a tese central: **ser ágil é ser adulto** — ter *accountability* (responsabilidade + ônus pelas consequências), não apenas liberdade/autonomia sem custo.

## Key Claims

1. **O manifesto se chama "Manifesto para o Desenvolvimento Ágil de Software", não "Manifesto Ágil"** — "ágil" é um adjetivo, não um nome de metodologia. Não existe "fazer ágil" ou "implementar ágil", só "ser ágil" ou não ser. Confidence: alta — argumento central atribuído explicitamente a [[wiki/entities/dave-thomas]] numa palestra específica (GOTO 2015), citada como fonte primária pelo próprio Akita. `[não verificado nesta ingestão contra a gravação original — ver Open Questions]`.
2. **Scrum não menciona "ágil" no seu guia original e foi inventado nos anos 80**, antes do manifesto — a associação popular "implementar Scrum = ser ágil" é uma distorção posterior, não uma equivalência original. Confidence: média-alta — consistente com a cronologia amplamente documentada do Scrum, mas não cross-checada com o Scrum Guide nesta ingestão.
3. **Kanban usado em software hoje "não se parece em nada" com o Kanban original da Toyota** — premissas e objetivos diferentes, nome reaproveitado por ser "marketável". Confidence: média — afirmação qualitativa do autor, sem comparação ponto a ponto entre o Kanban de manufatura e o Kanban de software nesta fonte.
4. **Técnicas de engenharia de produção física (Lean, Six Sigma, Kanban, PERT, Monte Carlo) não se transferem para desenvolvimento de software** porque software (assim como literatura, música, pintura) é uma abstração sem forma física, sem peso, sem restrições físicas — ao contrário de hardware/construção civil, onde duas equipes seguindo a mesma especificação produzem resultados em custo/tempo/qualidade parecidos. Em software, a diferença entre um profissional medíocre e um excelente é de ordens de grandeza, não de percentual. Confidence: alta enquanto argumento filosófico/qualitativo do autor — não é uma tese testada empiricamente nesta fonte, é uma analogia recorrente no canal.
5. **Números/métricas usados para validar metodologias ágeis raramente vêm com controle de condições, repetibilidade ou grupo de controle** — "funciona no Google/Spotify" não informa sob quais premissas funcionou, e sobrevivência de uma empresa não prova causalidade da metodologia. Confidence: alta como crítica metodológica (viés de sobrevivência é um problema real e bem documentado), mas a fonte não cita literatura específica sobre viés de sobrevivência.
6. **Consultoria/coaching ágil se assemelha a personal trainer: só funciona se a disciplina continua depois que o consultor vai embora**, e a maioria das equipes volta ao comportamento anterior — criando um ciclo de recontratação. A motivação de fundo para contratar é medo/insegurança do gestor, que terceiriza a decisão para poder dizer "fiz o que todo mundo recomenda" se der errado. Confidence: média-alta — argumento coerente com a tese já registrada em [[wiki/sources/pare-de-terceirizar-suas-decisoes]] sobre terceirização de decisões, mas é opinião do autor, não estudo de mercado de consultorias.
7. **Ironicamente, contratar uma consultoria externa para "implementar processos e ferramentas" viola o primeiro valor do próprio manifesto** ("indivíduos e interações mais que processos e ferramentas") — indivíduos de fora do time impondo processos e mecanismos de controle. Confidence: alta como observação lógica/retórica sobre o próprio texto do manifesto.
8. **Ser ágil é fazer o que precisa ser feito para atingir objetivos concordados, com expectativas alinhadas e sem meias palavras** — inclui o direito de recusar um projeto mal definido, ou de entregar só metade do escopo com transparência total, em vez de prometer o impossível. Ligado à crítica ao movimento #NoEstimates (citado como "estúpido") e à defesa de que estimar, mesmo sendo tarefa ingrata, é necessária. Confidence: alta como posição do autor, consistente com [[wiki/sources/por-que-estimativas-de-software-falham-como-melhorar]] já registrada na wiki.
9. **Gestão de projetos é, em grande parte, gestão de riscos — e gestão de riscos não é eliminação de todo risco.** Tentar garantir 100% de certeza via microgerenciamento/controle excessivo é pior do que aceitar uma pequena margem de erro; a analogia usada é seguro (cobertura total custa caro demais para valer a pena) e "não bater o carro nunca = nunca tirar o carro da garagem". Confidence: alta como princípio de gestão de risco, amplamente aceito fora desta fonte também.
10. **"Ter controle" e "achar que tem controle" são coisas diferentes** — a resposta correta a incerteza é assumir risco de forma deliberada (planejamento com ponto de corte, teste curto, cortar cedo se não funcionar), não empilhar ferramentas/procedimentos para simular certeza. Confidence: alta como posição do autor.
11. **"Ser ágil é ser adulto"** — o valor "indivíduos e interações mais que processos" pressupõe que todos os envolvidos são adultos que resolvem problemas entre si, sem microcontroles. *Accountability* (responsabilidade + ônus pelas consequências da liberdade) é o núcleo do conceito, não apenas autonomia. Esconder-se atrás de checklists cumpridos ("preenchi todos os tickets, fiz a sprint planning, não é minha culpa") é o oposto de *accountability*, e é o mesmo padrão de evasão de responsabilidade que existia antes do movimento ágil. Confidence: alta como tese central e autoral do vídeo, não uma citação de terceiros.
12. **Para iniciantes, as práticas que valem a pena vêm do Extreme Programming, não do Scrum**: TDD, build/integração contínua, design incremental — não cerimônias ("brincar de cartas", "chapéu em círculo para falar"). Confidence: alta como recomendação pessoal do autor.

## Entidades

- [[wiki/entities/fabio-akita]] — autor da fonte
- [[wiki/entities/martin-fowler]] — citado como um dos 17 signatários do manifesto; autor de *Refactoring*
- [[wiki/entities/kent-beck]] — citado como um dos 17 signatários; criador (com Ward Cunningham) do XP
- [[wiki/entities/uncle-bob]] — citado como um dos 17 signatários; citação direta sobre "não existe metodologia ágil, existe ser ágil"
- [[wiki/entities/dave-thomas]] — signatário, coautor de *The Pragmatic Programmer* e da editora Pragmatic Bookshelf; fonte primária do argumento central (palestra GOTO 2015) sobre "ágil como adjetivo"
- Demais signatários citados sem página própria nesta ingestão: Alistair Cockburn (Crystal Clear), Jim Highsmith (Adaptive Software Development), Ward Cunningham (wiki, C2, coautor do XP), Andy Hunt (coautor de *The Pragmatic Programmer*), Steve Mellor (método Shlaer-Mellor), Arie van Bennekum, James Grenning, Jon Kern, Mike Beedle, Ken Schwaber e Jeff Sutherland (fundadores do Scrum)

## Conceitos

- [[wiki/concepts/manifesto-agil-como-adjetivo]] — conceito central novo desta fonte
- [[wiki/concepts/software-nao-e-engenharia-de-producao]] — conceito novo: por que Lean/Kanban/Six Sigma não se transferem de fábrica para software
- [[wiki/concepts/accountability-em-equipes-ageis]] — conceito novo: ser ágil como accountability, não autonomia sem ônus
- [[wiki/concepts/gestao-de-riscos-e-controle-ilusorio]] — conceito novo: gestão de risco vs. controle ilusório via processo
- [[wiki/concepts/extreme-programming]]
- [[wiki/concepts/scrum-master]]
- [[wiki/concepts/goodharts-law]]
- [[wiki/concepts/story-points]]
- [[wiki/concepts/cultura-corporativa-vs-manifesto-na-parede]]

## Conexões com Wiki Existente

- [[wiki/concepts/scrum-master]] e [[wiki/concepts/goodharts-law]] já documentam o mesmo fenômeno que esta fonte chama de "muleta das metodologias" — Scrum Master como fiscal de números em vez de facilitador, e story points forçados como caso concreto de métrica que vira alvo e perde sentido. Esta fonte generaliza esse mecanismo específico para toda a indústria de consultoria ágil.
- [[wiki/sources/pare-de-terceirizar-suas-decisoes]] (mesmo autor, episódio anterior da mesma série) já estabelece [[wiki/concepts/skin-in-the-game]] como critério de quem tem propriedade para opinar — esta fonte aplica o mesmo raciocínio a consultores/coaches ágeis: eles não sofrem o prejuízo se a implementação falhar, o time e a empresa sim.
- [[wiki/sources/por-que-estimativas-de-software-falham-como-melhorar]] já documenta, de forma mais técnica e sem o tom de rant, a mesma posição pró-estimativa (contra #NoEstimates) que Akita defende aqui de forma mais filosófica/retórica.
- [[wiki/concepts/cultura-corporativa-vs-manifesto-na-parede]] (mesmo autor, fonte diferente) já registra a tese geral de Akita de que "manifestos" corporativos (cultura, valores) tendem a virar marketing estático desconectado do comportamento real — esta fonte aplica exatamente o mesmo padrão argumentativo ao Manifesto Ágil especificamente: um texto de quatro valores simples, interpretado livremente para justificar qualquer comportamento, incluindo falta de profissionalismo.
- **Nenhuma contradição direta encontrada** com conteúdo pré-existente da wiki — a fonte é consistente com o material já registrado sobre estimativa, métricas e a crítica geral de Akita a terceirização de julgamento.

## Questões em Aberto

- (1) **A palestra de Dave Thomas na GOTO 2015** e o blog post de 2014 citados como fontes primárias do argumento "ágil é adjetivo, não substantivo" não foram assistidos/lidos nesta ingestão — apenas a transcrição de Akita relatando o conteúdo. Candidato a ingestão futura como fonte primária independente, se a gravação/post forem localizados.
- (2) **O artigo do próprio Akita, "Ágil está morto" (2014)**, mencionado como escrito na mesma época do blog post de Dave Thomas, também não foi lido nesta ingestão — é uma fonte separada em potencial.
- (3) A citação atribuída a Uncle Bob ("não existe metodologia ágil, existe ser ágil") é parafraseada pela transcrição, sem link ou data ao post/vídeo original — mesma cautela de atribuição já registrada em várias outras menções a Uncle Bob nesta wiki (ver [[wiki/entities/uncle-bob]]).
- (4) Comparação factual entre o Kanban de manufatura da Toyota e o Kanban de software (claim 3) é afirmada qualitativamente pelo autor, sem detalhamento ponto a ponto nesta fonte — candidato a uma página dedicada de comparação, se surgir uma fonte que faça essa análise em profundidade.
