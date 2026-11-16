---
type: entity
title: "Nubank"
aliases: ["Nu", "Nu Holdings", "Nu Bank"]
date_created: 2026-05-31
date_updated: 2026-11-16
source_count: 29
tags: [nubank, fintech, banco-digital, clojure, datomic, event-sourcing, iso-27001, security, cell-based-architecture, observabilidade]
skill: tech-mentor-backend
status: stable
---

# Nubank

## TL;DR

Maior banco digital da América Latina. 122 milhões de clientes (Brasil, México, Colômbia — dado de 2025). Fundado ~2013. Pioneiro no uso de [[clojure]], [[datomic]] e [[wiki/concepts/event-sourcing]] em escala de banco de varejo, motivado pelo paper "Out of the Tar Pit" e pela necessidade de eliminar [[complexidade-acidental]]. Além da fundação em Clojure/Datomic, opera hoje com 4.000+ microsserviços particionados em 20 shards via [[wiki/concepts/cell-based-architecture|Scalability Units]], e construiu observabilidade própria ([[wiki/entities/alexandria-nubank|Alexandria]]) por custo de escala.

## Perfil

- **Sede:** São Paulo, Brasil
- **Fundação:** ~2013
- **Clientes:** 122 milhões (Brasil, México, Colômbia — 2025; era reportado como 100 milhões em fontes anteriores desta wiki)
- **Produtos:** conta digital, cartão de crédito, pagamentos, investimentos
- **Escala de infraestrutura (2025):** 4.000+ microsserviços, 72 bilhões de eventos Kafka/dia, 20 shards no Brasil, 600 TB de logs/dia, 450 milhões de eventos antifraude/dia

## Decisões Técnicas Fundamentais

| Decisão | Escolha | Motivação |
|---------|---------|-----------|
| Linguagem principal | [[clojure]] | Funcional, imutável, JVM |
| Banco de dados | [[datomic]] | Imutável, time-travel, auditoria |
| Arquitetura | [[wiki/concepts/event-sourcing]] + [[wiki/concepts/cqrs]] + [[ddd]] | Eliminar complexidade acidental |
| Framework | Interno (não público) | Controle total de threads e GC |
| Sharding | [[wiki/concepts/cell-based-architecture\|Scalability Units]] (clone de infra completa, não só do banco) | Sharding de banco sozinho parou de bastar em 2016 — AWS chegou a ficar sem máquinas para o ritmo de crescimento |
| Observabilidade | [[wiki/entities/alexandria-nubank\|Alexandria]] (construída internamente) | Solução de logs terceirizada ficou financeiramente inviável na escala do banco |

## Escala e Autorização de Transação (dado de 2025)

Autorização de transação de cartão precisa responder em menos de 100ms ponta a ponta (maquininha → adquirente → bandeira → Nubank → resposta). O time de engenharia reduziu a latência crítica desse caminho de ~10.000ms para **288ms no P90** (redução de 76%), removendo dependências síncronas do caminho crítico: em vez de buscar dados em tempo real, o sistema **precomputa e materializa** as informações necessárias no momento da escrita, deixando a leitura como um único lookup em datastore de baixa latência — [[wiki/concepts/cqrs|CQRS]] aplicado à latência do caminho crítico. Ver [[wiki/sources/nubank-arquitetura-escala-122-milhoes-clientes]].

A plataforma antifraude processa 450 milhões de eventos/dia, dividida em detecção (regras manuais + ML — regra simples classificando como suspeita evita rodar o modelo de ML) e ação (bloquear/alertar/deixar passar). Um orquestrador refatorado para modelo DAG (grafo acíclico dirigido — cada componente espera só pelos dados que precisa) reduziu a latência de 550ms para 350ms em fluxos complexos.

## Contexto das Escolhas

O CTO do Nubank leu o paper *"Out of the Tar Pit"* antes de construir o banco. A conclusão foi direta: para construir um banco que sobrevivesse a escala de varejo, era necessário eliminar [[imutabilidade|estado mutável]] e [[efeitos-colaterais]] desde o início.

A escolha de [[datomic]] veio da pergunta: "E o banco de dados? Como ter um banco imutável?" — Datomic resolve isso com um log append-only e time-travel nativo.

## Segurança e Compliance

Possui certificação [[wiki/concepts/iso-27001]], usada como garantia formal a investidores e reguladores de que os dados de mais de 100 milhões de clientes estão protegidos. O recurso "modo rua" do app — que limita transações quando o usuário sai de uma rede Wi-Fi segura — é citado como exemplo de controle de acesso contextual alinhado aos controles de segurança móvel e acesso lógico da norma.

## Na aula de formas

Na versão "W7" da aula de formas, o site do Nubank é exemplo de predominância geométrica amenizada por bordas arredondadas e por fotos de pessoas, que trazem comunidade e realidade ([[wiki/sources/formas-geometricas-organicas-exemplos-dropbox-madero-coco-bambu-nubank]]).

## Botões circulares

Em [[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]]: botão "continuar", links do topo (Pix) e CTAs ("entre para Nubank", "quero ser Nubank") "totalmente circulares para poder trazer mais para perto".

## Case do módulo de interfaces web

Na abertura do módulo de interfaces web, um projeto do Nubank é "o case do nosso curso": wireframes de baixa fidelidade por dobra (o [[wiki/concepts/page-map]]) e um [[wiki/concepts/style-guide]] editável ([[wiki/sources/interfaces-web-introducao-workflow-grids-pagemap-wireframes-style-guide]]).

## Projeto prático do curso de UI

Projeto isolado do curso de [[wiki/entities/nasser|Násser]]: wireframes e depois o style guide, com tipografia 48, 36, 24 (desktop x mobile) e uma família de ícones ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]).

## Arquivo de estudo com estilos de texto

O clone de estudo de [[wiki/entities/nasser]] no Figma tem o link guardado no "Master File, no Notion" e já usa estilos de texto: fonte Sora, headings de 48, 36 e 24, line-height 110 ([[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]]).

## Case do módulo de Interfaces Web

Em [[wiki/sources/style-guide-pratica-parte-2-documentacao-para-dev-sombra-gradiente-estados]], o projeto Nubank "vai servir de case" para demonstrar o [[wiki/concepts/style-guide]] e os estados dos componentes.

## Wireframes do módulo Nubank

O curso tem "um módulo específico só para a gente desenvolver o Nubank". Na aula 08, o wireframe do Nubank troca um parágrafo por tópicos ("resolvo tudo pelo app", "100% gratuito", "não tem taxas"); os wireframes de baixa fidelidade ficam para a aula seguinte ([[wiki/sources/wireframes-pratica-1-hero-page-map-frankenstein-referencias]]).

## Projeto de estudo no FrontPUSH

Em [[wiki/sources/wireframes-pratica-2-page-map-por-referencias-hero-processo-cta]], Násser cita de passagem um projeto no Nubank (frase confusa na legenda: "qual projeto custo eu coloquei aqui no Nubank") e promete mostrá-lo "com mais detalhes quando a gente [...] desenvolver esse projeto" no curso.

## Paleta: roxo e branco

Exemplo de paleta neutra + uma cor: "o Nubank é roxo e branco e as suas variações". O curso tem um projeto do Nubank que trabalha só com neutros e uma cor ([[wiki/sources/paleta-de-cores-na-pratica-dribbble-hsb-variacoes-cores-neutras]]). Ver [[wiki/concepts/paleta-de-cores]].

## Style guide do curso

Násser está fazendo um Style Guide do Nubank para o curso, com h1–h3 em versão desktop e mobile ([[wiki/sources/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma]]).

## Sass no projeto

Em [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]], o projeto do Nubank é "uma ótima vitrine" do uso do Sass para produtividade.

## Style guide e roxo no Sass

Em [[wiki/sources/frontpush-variaveis-sass]], o style guide do projeto Nubank é o exemplo de consistência, e o roxo dele vira variável no botão da demo. A fonte do guia estava como Montserrat; é Sora.

## & com pseudo-elementos

Em [[wiki/sources/frontpush-nesting-aninhamento-sass]]: "no próprio site da Nubank, eu utilizo o Sass dessa forma", com `&::before`/`&::after` nos links.

## Mixin de responsividade

Em [[wiki/sources/frontpush-mixin-e-content-sass]]: o mixin de responsividade com `@content` "eu já implementei no projeto do Nubank".

## Mixins de tipografia e layout

Em [[wiki/sources/frontpush-if-else-sass]]: `typeface-1` (Sora) e `typeface-2` (Source Sans Pro) com tamanho `h1`–`h5` e dispositivo; mixin de layout com `xl`/`l`/`m`/`s`/`xs` (1440/1140/960/540). Detalhados "na aula do Nubank", ainda não ingerida.

## Grid de colunas no layout

Em [[wiki/sources/frontpush-for-while-each-sass]]: o layout do projeto Nubank no Figma, com blocos vermelhos de 5 e 7 colunas (576 e 816 px), ilustra o grid de 12 × 96 px + gutter 24.

## Layout de 1920 e grid de 1416

Em [[wiki/sources/frontpush-funcoes-sass]]: o layout do projeto foi desenhado para 1920 × 1080; o grid de 12 colunas soma 1416 px; o bloco de 5 colunas (576 px) ilustra a função `grid()` em %.

## Flexbox "no olho"

Em [[wiki/sources/frontpush-grid-system-sass-parte-1]]: o projeto foi layoutado com Flexbox (`flex-grow` 2 e 1, ajustado no olho); o mixin `responsive` com `xl`–`xs` também vem dele.

Em [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]], o projeto do Nubank do FrontPUSH é lembrado como o lugar onde a "manipulação DOM de elementos" já foi usada para dar interatividade.

## Key Sources


- [[wiki/sources/senioridade-nao-e-so-tecnica-especializacao-negocio-dados-confianca-em-crise]] — relato de que, ao virar banco, a liberdade de ferramentas/inovação tende a diminuir (afirmação do autor, não verificada); palestras sobre Datomic em 2015/2016
- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
- [[wiki/sources/iso-27001-dicionario-programador]] — certificação ISO 27001 e "modo rua" como controle de acesso contextual
- [[wiki/sources/cqrs-event-sourcing-full-cycle-wesley-williams]] — citado como caso de uso do Datomic ao explicar Event Sourcing
- [[wiki/sources/nubank-arquitetura-escala-122-milhoes-clientes]] — números de 2025 (122M clientes, 4.000 microsserviços, 20 shards), Scalability Units, otimização da latência de autorização de transação (10.000ms → 288ms P90), plataforma antifraude (450M eventos/dia, DAG), Alexandria (observabilidade in-house)
- [[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]] — citado de passagem por Násser como projeto dele feito todo em SVG (clone de estudo do autor, não o produto oficial; confirmado pelo usuário em 2026-11-13)
- [[wiki/sources/formas-exemplos-praticos-radius-consistencia-projetos]] — página institucional citada por Násser como exemplo de botão (aparentemente totalmente arredondado)
- [[wiki/sources/formas-geometricas-organicas-exemplos-dropbox-madero-coco-bambu-nubank]] — site como exemplo de formas: geométrico, bordas arredondadas, fotos de pessoas
- [[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]] — botões e links totalmente circulares para aproximar
- [[wiki/sources/interfaces-web-introducao-workflow-grids-pagemap-wireframes-style-guide]] — case do curso: pagemap por dobras e style guide
- [[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]] — style guide do projeto prático: tipografia 48/36/24, família de ícones
- [[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]] — arquivo de estudo no Figma: link no Notion, fonte Sora, headings 48/36/24
- [[wiki/sources/style-guide-pratica-parte-2-documentacao-para-dev-sombra-gradiente-estados]] — projeto Nubank anunciado como case do style guide
- [[wiki/sources/wireframes-pratica-1-hero-page-map-frankenstein-referencias]] — wireframe com benefícios em tópicos; módulo próprio no curso
- [[wiki/sources/wireframes-pratica-2-page-map-por-referencias-hero-processo-cta]] — projeto de estudo do curso, detalhes prometidos
- [[wiki/sources/paleta-de-cores-na-pratica-dribbble-hsb-variacoes-cores-neutras]] — roxo e branco como paleta neutra + uma cor
- [[wiki/sources/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma]] — style guide do Nubank (escalas desktop e mobile)
- [[wiki/sources/frontpush-conclusao-modulo-css-estilo-layout-animacao-documentacao]]: projeto prático do FrontPUSH indicado como o primeiro depois do módulo de HTML e CSS
- [[wiki/sources/frontpush-justify-content-align-items-box-sizing]]: menu responsivo com `space-around` prometido para o projeto do Nubank (módulo de Flexbox do FrontPUSH)
- [[wiki/sources/frontpush-flexbox-pratica-2-desafio-estrutura-de-divs]]: citado como o projeto em que Násser já mostrou o menu com hambúrguer e media query
- [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]]: Sass no projeto do Nubank (FrontPUSH)
- [[wiki/sources/frontpush-variaveis-sass]]: style guide e roxo usados na aula de variáveis do Sass
- [[wiki/sources/frontpush-nesting-aninhamento-sass]]: `&` com pseudo-elementos nos links (Sass)
- [[wiki/sources/frontpush-mixin-e-content-sass]]: mixin de responsividade no projeto (Sass)
- [[wiki/sources/frontpush-if-else-sass]]: mixins de tipografia e de breakpoints com `@if`
- [[wiki/sources/frontpush-for-while-each-sass]]: grid de colunas do layout (Sass, aula de loops)
- [[wiki/sources/frontpush-funcoes-sass]]: layout 1920, grid 1416, função `grid()`
- [[wiki/sources/frontpush-grid-system-sass-parte-1]]: layout por flex-grow; mixin `responsive`
- [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]]: FrontPUSH, JavaScript aula 08: manipulação do DOM no projeto Nubank
