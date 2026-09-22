---
type: entity
title: "Fábio Akita"
aliases: ["Akita", "Akita On Rails"]
date_created: 2026-05-16
date_updated: 2026-09-22
source_count: 12
tags: [pessoa, programador, youtuber, brasil]
skill: tech-mentor-leadership
status: stable
---

# Fábio Akita

Programador brasileiro, criador de conteúdo técnico no canal *Akita On Rails* (YouTube). Conhecido por episódios longos sobre carreira, aprendizado, história da computação e filosofia de desenvolvimento de software.

## Perfil

- Programador desde 1991
- Aprendeu programação de forma autodidata em 1990 (~13 anos), em computadores de 8 bits, sem internet
- Trabalhou com dezenas de linguagens: Java, C#, PHP, Ruby, Objective-C, Elixir, Crystal, Go, entre outras
- Forte defensor do [[wiki/concepts/autodidata|autodidatismo]] e do [[wiki/concepts/hacker-mindset|hacker mindset]]
- Não concluiu a faculdade de ciência da computação, mas cursou os dois primeiros anos (metade de um curso integral de 4 anos, majoritariamente matemática) — descreve isso como determinante para acelerar sua formação como autodidata
- Fundador e administrador de uma empresa de outsourcing de desenvolvimento com quase 100 desenvolvedores e baixo índice de turnover, atuando majoritariamente em projetos para os EUA
- Foi consultor em ~2002 no projeto de unificação de sistemas da Vivo (unificação de operadoras de telecom regionais no Brasil, ex-Telesp Celular) — identificou vazamento de memória em framework proprietário via teste de stress simples, alerta ignorado por hierarquia/certificação

## Filosofia de aprendizado

- Aprender fazendo, não estudando teoria primeiro
- [[wiki/concepts/aprendizado-por-exposicao|Exposição massiva]] a código real antes de criar
- [[wiki/concepts/algoritmos-e-estruturas-de-dados|Algoritmos e estruturas de dados]] como fundação inegociável
- [[wiki/concepts/design-patterns|Design Patterns]] são para depois — não para iniciantes

## Visão de Carreira e Mercado

Defende que o mercado de programação segue [[wiki/concepts/ciclo-de-mercado-tech|ciclos de abundância e depressão]] regidos por oferta e procura, e que [[wiki/concepts/raciocinio-matematico-aplicado|raciocínio matemático básico]] — não a linguagem da moda — é o que diferencia profissionais entre ciclos. Crítico de [[wiki/concepts/apego-a-ferramentas|apego a ferramentas]] específicas ("tecnologia não é time de futebol").

## Raiz Filosófica

Em [[wiki/sources/akita-discurso-howard-roark-a-nascente-ayn-rand]], Akita lê o discurso de defesa de Howard Roark (*A Nascente*, [[wiki/entities/ayn-rand]]) e afirma que tentou viver seguindo esses princípios — apontando essa fonte como origem de vários temas que já tratou sobre a vida de empreendedores, criadores e inovadores. O discurso defende [[wiki/concepts/objetivismo|Objetivismo]]: a dicotomia [[wiki/concepts/criador-vs-parasita|criador vs. parasita]] e a [[wiki/concepts/independencia-como-motor-criativo|independência]] como necessidade básica de quem cria — coerente com sua defesa do autodidatismo e sua crítica ao apego a ferramentas, ainda que a fonte trate de filosofia moral, não de carreira tech diretamente.
## Visão de Tomada de Decisão

Rejeita explicitamente o papel de conselheiro de carreira: recusa-se a dizer o que alguém deve estudar ou decidir, argumentando que ninguém tem [[wiki/concepts/skin-in-the-game|skin in the game]] suficiente na vida alheia para opinar com propriedade sobre [[wiki/concepts/decisao-terceirizada|decisões terceirizadas]]. Defende [[wiki/concepts/antifragilidade|apostas antifrágeis]] de ~10 anos em tecnologia (ex.: aposta pessoal em Ruby on Rails em 2005) em vez de tentar prever com certeza a próxima tecnologia vencedora. Critica o [[wiki/concepts/cargo-cult-tecnologico|cargo cult tecnológico]] de copiar arquitetura de Netflix/Google/Facebook sem considerar o próprio contexto de escala — "compare-se com o dia um deles, não com a versão madura de hoje". Também nomeia a [[wiki/concepts/falacia-do-custo-afundado|falácia do custo afundado]] como o principal motivo de as pessoas persistirem em cursos e livros ruins.

## Áudio Reproduzido Sobre Fim do Dinheiro Fácil e Layoffs

[[wiki/sources/aprenda-a-programar-do-jeito-dificil]] cita, de segunda mão (via vídeo de [[wiki/entities/filipe-deschamps]]), um áudio de Akita argumentando que o fim do dinheiro fácil de investimento forçou as empresas a priorizar lucro e eficiência (menos gasto com servidor, código mais otimizado), o que aperta processos seletivos e leva a layoffs — coerente com sua tese já documentada de [[wiki/concepts/ciclo-de-mercado-tech|ciclos de mercado]] de abundância e depressão.

## Segurança: AI Jail

Em janeiro de 2026, publicou um artigo propondo o **AI Jail** — ferramenta de linha de comando (~170 linhas de shell script, sobre o [[wiki/entities/bubblewrap]]) para isolar agentes de codificação de IA do restante do sistema do usuário, endereçando o risco de [[wiki/concepts/supply-chain-security|ataques de supply chain]] via dependências comprometidas. O tema também foi abordado por ele no Flow Podcast. Ver [[wiki/concepts/agent-containment]] e [[wiki/concepts/defense-in-depth]] para o modelo de três camadas que o artigo propõe (sessão/AI Jail, código/Git, sistema operacional imutável). Coerente com sua defesa geral de [[wiki/concepts/principio-do-menor-privilegio|privilégio mínimo]] e ceticismo em relação a confiar cegamente em ferramentas/pacotes só por serem populares.

## Citado Sobre a Escola 1 (Copiloto) Estar "Datada"

Em [[wiki/sources/cinco-escolas-programacao-com-ia]], o autor da fonte relata (de passagem, sem contexto completo) que Akita teria dito, em conversa ou vídeo, que a abordagem "copiloto" (autocomplete revisado sugestão-a-sugestão, ex.: Cursor/GitHub Copilot) seria "coisa de 2023" — já datada. O próprio autor da fonte discorda parcialmente, observando que essa escola segue com adesão ativa em 2026. `[transcrição incerta sobre o contexto exato da fala de Akita — citação de segunda mão, sem link à fonte primária]`.

## Visão sobre Organização de Equipes de Tecnologia

Em [[wiki/sources/organizando-equipes-de-tecnologia-fabio-akita]], defende que [[wiki/concepts/equipe-mista-senior-junior|nenhuma equipe só de sêniors ou só de júniors funciona bem]] — usa a metáfora de pedreiro vs. mestre de obras para justificar times mistos, com o sênior orientando júniors ([[wiki/concepts/escalabilidade-vertical-vs-horizontal-de-pessoas|escalabilidade horizontal de pessoas]]) via [[wiki/concepts/feedback-continuo-diario|feedback diário e específico]], não elogio vazio. Relata sua própria trajetória como consultor em ~2002 no projeto de unificação de sistemas da Vivo/Claro (mesma passagem já documentada acima) como pano de fundo para sua crítica ao modelo [[wiki/concepts/body-shop-terceirizacao|Body Shop]] de contratação. Também traça um paralelo entre o mercado aquecido atual e a bolha da internet (2000-2001), incluindo a crítica de que "cultura corporativa" costuma funcionar como [[wiki/concepts/cultura-corporativa-vs-manifesto-na-parede|manifesto de marketing em vez de comportamento real]] — coerente com sua defesa geral, já documentada acima, de que fundamentos e raciocínio próprio superam modismos e cópia de padrões de empresas maiores (ver [[wiki/concepts/cargo-cult-tecnologico]]).

## Série "Aprendendo a Aprender": Contra o Mito do Talento

Em [[wiki/sources/akita-pratica-deliberada-mito-do-talento]], segundo episódio de uma série sobre metacognição e aprendizado, defende que talento inato não existe — citando *Talent Is Overrated* de [[wiki/entities/geoff-colvin]] para desconstruir o mito de Mozart como "faísca divina" (ver [[wiki/concepts/mito-do-genio-mozart]]). Detalha a estrutura da [[wiki/concepts/pratica-deliberada|prática deliberada]] (zona de aprendizado, alta repetição, foco solitário) e fecha defendendo [[wiki/concepts/autoavaliacao-vs-validacao-externa|autoavaliação rigorosa em vez de validação externa]] — relata nunca pedir feedback de terceiros, por considerar isso "a maneira mais fácil de sabotar seu talento". Reforça o tema recorrente do "esvaziar o copo" (questionar tudo, inclusive as próprias certezas) já presente em [[wiki/concepts/aprender-a-aprender]].

## Crítica à Indústria de Consultoria e Coaching Ágil

Em [[wiki/sources/agilidade-manifesto-agil-fabio-akita]], segundo episódio de uma série sobre "profissão de prática" (o primeiro é [[wiki/sources/pare-de-terceirizar-suas-decisoes]]), reconstrói a origem do Manifesto para o Desenvolvimento Ágil de Software (2001) e seus 17 signatários, apoiando-se num argumento de [[wiki/entities/dave-thomas]] (palestra GOTO 2015): "ágil" é adjetivo, não substantivo vendável — ver [[wiki/concepts/manifesto-agil-como-adjetivo]]. Argumenta que técnicas de engenharia de produção física (Lean, Kanban, Six Sigma) não se transferem para software por este não ter restrições físicas (ver [[wiki/concepts/software-nao-e-engenharia-de-producao]]), e que consultorias ágeis sobrevivem porque gestores terceirizam decisões por medo — mesmo mecanismo de [[wiki/concepts/decisao-terceirizada|terceirização de decisão]] já documentado em [[wiki/sources/pare-de-terceirizar-suas-decisoes]]. Fecha com a tese "ser ágil é ser adulto": *accountability* (responsabilidade + ônus pelas consequências), não apenas autonomia — ver [[wiki/concepts/accountability-em-equipes-ageis]] e [[wiki/concepts/gestao-de-riscos-e-controle-ilusorio]].

## Aprendizado, Gestão e Beira do Caos (Teoria Geral)

Em [[wiki/sources/aprendizado-gestao-e-beira-do-caos-fabio-akita]], vídeo comemorativo dos 300 mil inscritos, apresenta sua "teoria geral" sobre aprendizado, gestão de projetos e administração de empresas: usa a quebra histórica do [[wiki/concepts/determinismo-newtoniano-e-seus-limites|determinismo newtoniano]] (relatividade, física quântica, teoria do caos) como metáfora para argumentar que não existe receita determinista de sucesso além de escalas curtas de tempo. Reconstrói a origem do movimento de qualidade dos anos 80 ([[wiki/entities/edwards-deming|Deming]]/PDCA, [[wiki/entities/eliyahu-goldratt|Goldratt]]/Teoria das Restrições, Six Sigma) para defender que [[wiki/concepts/tentativa-e-erro-como-metodo-cientifico|PDCA, DMAIC, Kaizen, Scrum e o método científico são o mesmo ciclo]]. Introduz [[wiki/concepts/beira-do-caos|beira do caos]] como hipótese pessoal sobre o que significa "balanço": não ordem estática, mas oscilação disciplinada entre ordem e caos controlado. Aplica isso a planejamento de curto prazo, [[wiki/concepts/mvp|MVP]] e [[wiki/concepts/jogar-codigo-fora-como-pratica|escrever e jogar código fora]] como disciplina de programação, fechando com [[wiki/concepts/gestao-de-riscos-e-controle-ilusorio|gestão de risco]] (repetindo a analogia do seguro já registrada em fonte anterior) e a tese de que medo da opinião alheia, não falta de método, é a raiz da inação.

## Teoria Consolidada de Gestão de Projetos e Pessoas

Em [[wiki/sources/sobre-ser-gerente-fabio-akita]], apresenta sua visão mais ampla e consolidada sobre o papel de gerente. Rejeita certificações formais (PMP, MBA) como garantia de competência — descreve tê-las tratado como "colecionar papel" — e define gestão, na essência, como a capacidade de tomar decisões com informação incompleta. Reformula a tríade clássica de projeto (escopo-tempo-custo) acrescentando uma quarta variável invisível, qualidade, que absorve a pressão quando as outras três são mantidas fixas — ver [[wiki/concepts/triade-escopo-tempo-custo-qualidade]]. Aprofunda, com nova analogia (compilador como "operário automatizado", orquestra clássica vs. jazz), a tese já registrada em [[wiki/concepts/software-nao-e-engenharia-de-producao]] de que o programador é arquiteto, não operário. Introduz duas teses de contratação e liderança não documentadas em fontes anteriores: [[wiki/concepts/nivel-a-contrata-nivel-a]] (só nível A reconhece e contrata nível A) e [[wiki/concepts/gestor-deve-ter-sido-praticante]] (um gestor sem experiência prática na função nunca conquista respeito genuíno da equipe). Fecha com a tese central: "gerenciar projetos é gerenciar pessoas, e gerenciar pessoas é gerenciar expectativas" — confiança não é amizade, e feedback honesto é o que de fato preserva a confiança dentro de uma equipe.

## Key Sources

- [[wiki/sources/akita-como-aprender-programacao]]
- [[wiki/sources/akita-pratica-deliberada-mito-do-talento]] — segundo episódio da série "Aprendendo a Aprender"; mito do talento, caso Mozart, autoavaliação vs. validação externa
- [[wiki/sources/akita-oferta-procura-matematica-carreira]]
- [[wiki/sources/akita-discurso-howard-roark-a-nascente-ayn-rand]]
- [[wiki/sources/pare-de-terceirizar-suas-decisoes]]
- [[wiki/sources/ai-jail-sandbox-para-agentes-de-ia-akita]] — artigo/projeto AI Jail, comentado por terceiros (fonte não é o próprio canal de Akita)
- [[wiki/sources/aprenda-a-programar-do-jeito-dificil]] — áudio de segunda mão sobre fim do dinheiro fácil e aperto de processos seletivos
- [[wiki/sources/cinco-escolas-programacao-com-ia]] — citação de segunda mão sobre a Escola 1 (copiloto) estar "datada"
- [[wiki/sources/organizando-equipes-de-tecnologia-fabio-akita]] — como organizar equipes mistas de tecnologia, feedback diário, paralelo com a bolha da internet e crítica à "cultura" como manifesto de marketing
- [[wiki/sources/agilidade-manifesto-agil-fabio-akita]] — segundo episódio da série "profissão de prática"; crítica à indústria de consultoria ágil, origem do manifesto, "ágil é adjetivo", accountability vs. autonomia
- [[wiki/sources/aprendizado-gestao-e-beira-do-caos-fabio-akita]] — vídeo dos 300 mil inscritos; teoria geral sobre aprendizado/gestão via quebra do determinismo newtoniano, origem do movimento de qualidade (Deming, Goldratt, Six Sigma), tese "PDCA=DMAIC=Kaizen=Scrum=método científico", hipótese da beira do caos
- [[wiki/sources/sobre-ser-gerente-fabio-akita]] — teoria consolidada sobre gestão de projetos e pessoas: crítica a PMP/MBA, quarta variável invisível (qualidade), programador como arquiteto (não operário), "nível A contrata nível A", gestor precisa ter sido praticante, confiança ≠ amizade
