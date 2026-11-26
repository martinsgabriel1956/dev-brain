---
type: concept
title: "Carga Cognitiva"
aliases: []
date_created: 2026-09-22
date_updated: 2026-11-26
source_count: 12
tags: [carga-cognitiva]
skill: tech-mentor-leadership
status: stub
---

# Carga Cognitiva

Stub criado durante sweep de lint (links quebrados) a partir de referências em 1 página(s) da wiki — conteúdo completo pendente de ingest dedicado.

## Contexto das citações

- Em [[wiki/sources/por-que-devs-nao-terminam-projetos]]: **Cognitive load sem sistema**: sem roadmap e tracking, a memória de trabalho satura e gera burnout — ciência é chamada de Cognitive Load Theory. → [[wiki/concepts/carga-cognitiva]]

## Em interfaces

[[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]] parte da mesma ideia: o ser humano tem um ponto focal e "consome pouca coisa" de cada vez, então a UI deve apresentar a informação aos poucos ([[wiki/concepts/simplicidade-visual]]). O contraexemplo é o ERP que mostra tudo numa tela e "não conduz para nada". `[skill: ux-ui-mentor]` A meta do designer é eliminar a carga extrínseca (ruído da interface), reduzir a intrínseca e potencializar a germane.

## Pendências

Página não nasceu de um ingest próprio; TL;DR acima é reconstruído apenas a partir do texto das páginas que a citam. Precisa de fonte dedicada para virar `draft`/`stable`.

## Ícones

Ícone simples reduz a carga cognitiva: a engrenagem é reconhecida sem leitura porque é um pattern aprendido, e tópicos com ícone ao lado são mais fáceis de ler que um bloco de texto. A metáfora complexa (duas pessoas e um coração para "amor"; computadores ligados para "internet") comunica, "porém ele não é simples" ([[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]]). Ver [[wiki/concepts/icones-em-interfaces]].

## Ícone como resumo

Em [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]], a grade densa do curso vira cards com um ícone por módulo, "uma redução cognitiva"; e o ícone mostra só o objeto ("só o chapéuzinho") "para poder reduzir o máximo a carga cognitiva".

## Patterns como acessibilidade

Em [[wiki/sources/acessibilidade-wcag-contraste-textos-invisiveis-kiss-patterns]]: usar UX/UI patterns consagrados "reduz a carga cognitiva do usuário", porque algo "totalmente novo" obriga o usuário a "gastar tempo para poder aprender como é que utiliza a sua interface". `[skill: ux-ui-mentor]` A acessibilidade cognitiva (progressive disclosure, chunking, linguagem simples) beneficia todos em algum momento. Ver [[wiki/concepts/acessibilidade]].

## Parágrafo em tópicos

"Se o parágrafo está muito grande, procure deixar o parágrafo em tópicos": as vantagens do cartão do [[wiki/entities/nubank]] viram três itens curtos, porque "se você colocar só texto e estiver muito carregado na interface é capaz que ele não leia" ([[wiki/sources/wireframes-pratica-1-hero-page-map-frankenstein-referencias]]).

## Padrões que poupam o usuário e o designer

Na [[wiki/sources/frontpush-monetizacao-freelancer-como-ganhar-dinheiro-erros-e-principais-pontos|aula 02 do módulo Monetização e Freelancer]], [[wiki/entities/nasser|Násser]] explica por que e-commerces se parecem: "eu sempre preciso procurar soluções que diminuam a carga cognitiva do usuário", "que o usuário não pense mais". Reduzir a carga está "muito ligado a pattern", e todo padrão vira componente reaproveitável, o que também aumenta a produtividade de quem faz ([[wiki/concepts/padroes-de-interface]]).

## No portfólio

Na [[wiki/sources/frontpush-monetizacao-freelancer-como-construir-um-portfolio|aula 05 do módulo Monetização e Freelancer]], [[wiki/entities/nasser|Násser]] aplica a ideia ao portfólio: "muitas dobras, muita coisa" tiram a clareza; o portfólio deve "reduzir a carga cognitiva do usuário" e mostrar só o mais importante ([[wiki/concepts/estrutura-de-portfolio]]).

## Uma ação por tela

Na [[wiki/sources/frontpush-dashboards-principios-parte-1|aula 04 do módulo de dashboards]], uma tela com várias ações de pesos parecidos "já confundiu o usuário"; isolar cada fluxo numa ação central dá foco. Ver [[wiki/concepts/fluxos-bem-definidos]].

## Em código (Ousterhout)

Em design de software, [[wiki/entities/john-ousterhout]] define carga cognitiva como quanto o desenvolvedor precisa saber para concluir uma tarefa, e a trata como um dos três [[wiki/concepts/sintomas-de-complexidade-ousterhout|sintomas de complexidade]]. Exemplo: uma função em C que aloca memória e deixa a liberação para quem chama; esquecer gera *memory leak*. Fontes típicas: APIs com muitos métodos, variáveis globais, inconsistências e dependências entre módulos. Ele avisa que linhas de código não medem a carga: "às vezes, uma abordagem que exige mais linhas de código é, na verdade, mais simples" ([[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]]). É o mesmo princípio das seções de UX acima, aplicado a quem lê código em vez de quem usa a interface.

## Ocultamento de informação como redução de carga (Ousterhout, cap. 5)

O primeiro ganho do [[wiki/concepts/ocultamento-de-informacao]] é a interface mais simples, que "diminui a carga cognitiva dos desenvolvedores" que usam o módulo: quem usa uma árvore B não pensa no *fanout* nem no balanceamento. O red flag da superexposição é o oposto: a API de um recurso comum obriga a aprender recursos raros ([[wiki/sources/filosofia-do-design-de-software-cap-05-ocultacao-de-informacao-e-vazamento]]).

## Muitos métodos rasos contra poucos gerais (Ousterhout, cap. 6)

[[wiki/sources/filosofia-do-design-de-software-cap-06-modulos-de-proposito-geral-sao-mais-profundos]] mostra a carga cognitiva de uma API especializada: a classe de texto do editor ganhou um método por operação da UI, muitos chamados num lugar só, e quem trabalhava na UI tinha de aprender todos. A versão geral tem poucos métodos simples, reaproveitados para vários fins (6.2 e 6.4). Ver [[wiki/concepts/modulo-de-proposito-geral]].

## Key sources

- [[wiki/sources/frontpush-monetizacao-freelancer-como-ganhar-dinheiro-erros-e-principais-pontos]]: reduzir carga cognitiva liga a patterns e a componentes reaproveitáveis
- [[wiki/sources/por-que-devs-nao-terminam-projetos]]
- [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]] — simplicidade: apresentar a informação aos poucos
- [[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]] — ícones simples e patterns aprendidos reduzem a carga cognitiva
- [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]] — ícone por módulo como "redução cognitiva"; só o objeto
- [[wiki/sources/acessibilidade-wcag-contraste-textos-invisiveis-kiss-patterns]] — patterns reduzem a carga cognitiva; não reinventar a roda
- [[wiki/sources/wireframes-pratica-1-hero-page-map-frankenstein-referencias]] — parágrafo longo vira tópicos para o usuário de fato ler
- [[wiki/sources/frontpush-monetizacao-freelancer-como-construir-um-portfolio]]: portfólio sem dobras demais
- [[wiki/sources/frontpush-dashboards-principios-parte-1]]: FrontPUSH, dashboards aula 04: várias ações confundem; isolar dá foco
- [[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]] — carga cognitiva como sintoma de complexidade de código (Ousterhout, cap. 2.2)
- [[wiki/sources/filosofia-do-design-de-software-cap-05-ocultacao-de-informacao-e-vazamento]] — ocultamento reduz a carga cognitiva; superexposição a aumenta (cap. 5)
- [[wiki/sources/filosofia-do-design-de-software-cap-06-modulos-de-proposito-geral-sao-mais-profundos]] — muitos métodos especializados aumentam a carga; poucos gerais a reduzem (cap. 6)
