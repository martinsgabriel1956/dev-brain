---
type: entity
title: "Google"
aliases: ["Google DeepMind", "Gemini"]
date_created: 2026-07-03
date_updated: 2026-11-20
source_count: 46
tags: [google, gemini, llm, storage, organização]
skill: tech-mentor-ai
status: stub
---

## Quem É

Empresa de tecnologia, criadora da família de modelos **Gemini** (ex.: Gemini 2.0 Flash Lite) e do harness AntiGravity. Concorrente direta da [[wiki/entities/anthropic]] e da [[wiki/entities/openai]] no mercado de LLMs, com tokenizer e vocabulário próprios — o mesmo prompt gera contagens de tokens diferentes das dos outros provedores. Ver [[tokenizacao]].

---

## Gemini Flash como Referência de Velocidade

[[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]] cita o **Gemini 3.5 Flash** como exemplo de modelo otimizado para o eixo de velocidade em [[wiki/concepts/modelo-por-leverage-tarefa]] — pontuação 70 no coding index do [[wiki/entities/artificial-analysis|Artificial Analysis]], recomendado para tarefas simples e urgentes (ex.: bug fix rápido) em vez dos modelos de fronteira (Fable, Sol), mais lentos.

## Gemini CLI e Detecção de Uso Não-Oficial de Ferramenta

[[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]] cita o Gemini CLI (junto com o Claude Code) como tendo um mecanismo de detecção de uso da ferramenta fora do padrão esperado, que pode bloquear/banir a conta — citado como o principal risco prático de [[wiki/concepts/rotacao-de-contas-free-tier|rotacionar múltiplas contas free tier]] do Gemini atrás de um AI Gateway.

## Membro Fundador da OpenID Foundation (2007) e Adotante do OIDC

Google, junto com Yahoo, Facebook e AOL, fundou em 2007 a OpenID Foundation, criada para padronizar o ecossistema caótico e incompatível do protocolo [[wiki/concepts/openid-legado|OpenID original]]. Anos depois, é citada como uma das big techs (junto com Microsoft e Apple) que adotaram em massa o [[wiki/concepts/openid-connect|OpenID Connect]], tornando-o base de praticamente todo botão de login social ("Entrar com Google"). Ver [[wiki/sources/openid-connect-oidc-autenticacao-alem-do-oauth]].

## Participante Inicial das Discussões do OAuth (2007)

Pouco depois de [[wiki/entities/blaine-cook]] (Twitter) e [[wiki/entities/larry-halff]] (Magnolia) iniciarem o grupo de discussão OAuth em abril de 2007, o Google já havia se juntado às discussões — mesmo ano em que, separadamente, cofundou a OpenID Foundation (ver seção abaixo). Ver [[wiki/sources/historia-oauth2-antipadrao-senha-bernardo-lobato]].

## Origem do Paper "Attention Is All You Need" (2017) e do TensorFlow Embedding Projector

[[wiki/sources/self-attention-mecanismo-transformers]] atribui à equipe do Google a origem do paper [[wiki/entities/attention-is-all-you-need-paper|"Attention Is All You Need"]] (2017), que introduziu a [[wiki/concepts/transformer-architecture|arquitetura Transformer]] e o mecanismo de [[wiki/concepts/self-attention]] — base de praticamente toda LLM generativa moderna. A mesma fonte cita o **TensorFlow Embedding Projector** (ferramenta do Google) como demonstração visual de como [[wiki/concepts/embedding-vectors|embedding vectors]] de palavras se posicionam num espaço multidimensional por proximidade semântica.

## Google Drive como Exemplo de Armazenamento em Nuvem

Citada (ao lado de Dropbox e iCloud) como serviço de nuvem de referência em [[wiki/sources/tipos-de-armazenamento-de-dados]]: arquivos ficam em servidores remotos, criptografados e **duplicados em vários data centers** — geo-redundância que sobrevive à falha de um centro inteiro. Trade-off: espaço grande exige assinatura. Contraste com o [[wiki/concepts/nas-network-attached-storage|NAS]], em que o hardware é do próprio usuário.

## Google Cloud

Google Cloud citado entre os hyperscalers do imaginário de "ir para a nuvem" ([[wiki/concepts/cloud-como-modelo-de-consumo]]).

## Gemini em Exemplo de Versionamento

Em [[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]], uma versão de prompt registra o modelo Gemini com temperatura 0, contra outra versão com modelo da OpenAI ([[wiki/concepts/metadados-de-prompt]]).

## Google na Corrida da IA: Negócio e Eficiência

[[wiki/sources/google-nao-esta-perdendo-corrida-ia-memory-caching-gemini-live]] defende que o Google perde na percepção dos devs (Antigravity ruim, timing de lançamento), mas ganha em negócio ([[wiki/entities/google-cloud-platform]] +82% a/a; [[wiki/concepts/tensor-processing-unit|TPUs]]) e em pesquisa de eficiência ([[wiki/entities/google-research]], [[wiki/concepts/memory-caching-rnn]]); produto de voz: [[wiki/entities/gemini-live]].

## Ícones como pattern

Engrenagem para configurar e "nove pontinhos" para os apps do Google: exemplo de Násser de ícone aprendido pelo uso diário ([[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]]).

## Espaço e linhas nos resultados de busca

Na visão geral dos elementos de Násser, os resultados do Google mostram espaço que agrupa e separa e linha que reforça a divisão ([[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]).

## Google Maps: cor como informação

Via vermelha ou laranja no Google Maps (ou no Waze) se lê como bloqueio ou engarrafamento: exemplo de [[wiki/concepts/cor-semantica]] na abertura do módulo de cores ([[wiki/sources/teoria-das-cores-introducao-natureza-objetivos-fenomeno-fisico]]).

## Títulos azuis como hierarquia

Em [[wiki/sources/tipografia-e-cores-contraste-hierarquia-textual-cor-como-informacao]]: na busca, o usuário "vai procurar primeiro pelos itens em azul", maiores e com mais contraste; lê o título e só então clica ou lê a descrição. Ver [[wiki/concepts/hierarquia-visual]].

## Google Fonts e Chrome na aula de tipografia

Na abertura do módulo de tipografia, o Google aparece como interface que é "a maior parte texto", o Chrome como navegador da extensão WhatFont, e o [[wiki/entities/google-fonts]] como principal referência para baixar fontes ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]).

## Google Fonts

O catálogo [[wiki/entities/google-fonts]] aparece em [[wiki/sources/classificacoes-tipograficas-serifa-sem-serifa-script-monoespacada-display]] como fonte gratuita de fontes, espelhada no Figma.

## Tags meta e visibilidade

Em [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]], as tags meta do `<head>` "melhoram até a visibilidade do seu site pelo Google". `[external]` O Google ignora `meta keywords`; a `meta description` pode virar o snippet: https://developers.google.com/search/docs/appearance/snippet.
## Tags semânticas e busca

Na aula de box model do [[wiki/entities/frontpush|FrontPUSH]], o motivo dado para usar [[wiki/concepts/html-semantico|tags semânticas]] é que elas "facilita[m] a vida do Google quando você coloca o seu site na internet" ([[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]]).
## Salário de júnior em São Paulo

Em [[wiki/sources/introducao-mapeando-vagas]], o que o Google paga a um desenvolvedor júnior em São Paulo é o exemplo de faixa "totalmente separada" da média salarial local ([[wiki/concepts/modelo-trimodal-compensacao]]).

Em [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]], pesquisar "de forma leiga" no Google ("como fazer para clicar em um título e mudar a cor JavaScript") é o método de estudo recomendado para o DOM.

Em [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]], a lista de eventos vem de uma busca "events javascript" no Google, num site que ele "sempre" visita.

## Experiência de página no ranking

Em [[wiki/sources/frontpush-introducao-otimizacao-web-minificacao-css-js]]: "o Google vai melhor indexar a sua página de acordo com a experiência do usuário", com o relatório de UX do Chrome (CrUX). Os [[wiki/concepts/core-web-vitals]] pesam no ranking, não na indexação.

## PageSpeed: imagens do tamanho do dispositivo

Em [[wiki/sources/frontpush-otimizacao-de-imagens-mobile-desktop-classes-mixin]]: o PageSpeed "fala muito sobre [...] disponibilize imagens que são de acordo com o tamanho do dispositivo". A auditoria compara o arquivo com o tamanho exibido (vezes a densidade), não a orientação.

## PageSpeed: as quatro notas

Em [[wiki/sources/frontpush-google-pagespeed-core-web-vitals-acessibilidade-meta-tags]]: desempenho, acessibilidade, práticas recomendadas e SEO, mais o Googlebot que "baixa a internet todos os dias". As notas são do Lighthouse e não são o ranking ([[wiki/concepts/seo]]).

## PageSpeed: os avisos de diagnóstico

Em [[wiki/sources/frontpush-relatorio-pagespeed-imagens-render-blocking-dom-regra-80-20]]: formatos de última geração, tamanho de imagem, render-blocking, payload, texto visível e DOM grande, cada um com descrição e link. Desde 2024–2025 o Lighthouse agrupa esses avisos em "insights" (confiança média).

## web.dev e análise mobile × desktop

Em [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]]: o artigo do web.dev sobre animações de alto desempenho (60 fps, pipeline, compositor) e a separação de mobile e desktop no PageSpeed, que emula um celular médio com CPU mais lenta.

## Key Sources

- [[wiki/sources/mainframe-as-a-service-casas-bahia-sulamerica-kyndryl]] — Google Cloud entre os hyperscalers do imaginário de nuvem
- [[wiki/sources/tokens-llm-fundamentos-typescript]]
- [[wiki/sources/tipos-de-armazenamento-de-dados]] — Google Drive como exemplo de nuvem com geo-redundância
- [[wiki/sources/openid-connect-oidc-autenticacao-alem-do-oauth]] — membro fundador da OpenID Foundation (2007); adotante em massa do OpenID Connect
- [[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]] — Gemini 3.5 Flash como modelo de referência para tarefas que exigem velocidade
- [[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]] — Gemini CLI citado como um dos providers com detecção de uso não-oficial e risco de banimento por rotação de contas free tier
- [[wiki/sources/historia-e-evolucao-das-apis-bernardo-lobato]] — criadora do [[wiki/concepts/grpc]] (2015), lançado na mesma década do GraphQL (Meta) como resposta de performance para comunicação interna entre microsserviços
- [[wiki/sources/historia-oauth2-antipadrao-senha-bernardo-lobato]] — uma das primeiras empresas a se juntar às discussões do grupo OAuth, pouco após sua formação em abril de 2007
- [[wiki/sources/self-attention-mecanismo-transformers]] — origem do paper "Attention Is All You Need" (2017) e do TensorFlow Embedding Projector
- [[wiki/sources/historia-do-captcha-do-teste-de-turing-ao-turnstile]] — comprou o [[wiki/concepts/recaptcha]] (2009), matou o CAPTCHA de texto com IA (99%, 2014), lançou "Não sou um robô" e o v3
- [[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]] — Gemini como modelo de exemplo nos metadados de versão
- [[wiki/sources/teorema-cap-p-e-pre-condicao-escolha-entre-c-e-a-pedro-camaforte]] — citação: Eric Brewer, descrito como VP de infraestrutura do Google
- [[wiki/sources/rag-spring-ai-microagente-recomendacao-michele-brito]] — modelos Gemini de chat e de embedding usados via [[wiki/entities/spring-ai]] no demo de RAG
- [[wiki/sources/dotenv-arquivo-env-boas-praticas-secret-manager]] — Google Secret Manager citado como cofre
- [[wiki/sources/google-nao-esta-perdendo-corrida-ia-memory-caching-gemini-live]] — debate sobre corrida da IA: cloud +82%, TPU, Memory Caching, Gemini 3.8 Live
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — resultados de busca como exemplo de espaço e linhas
- [[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]] — resultados separados pelo espaço maior entre eles
- [[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]] — buscar "pessoas conversando" no Google como exemplo de foto genérica
- [[wiki/sources/teoria-das-cores-introducao-natureza-objetivos-fenomeno-fisico]] — Google Maps: vermelho/laranja = trânsito
- [[wiki/sources/tipografia-e-cores-contraste-hierarquia-textual-cor-como-informacao]] — títulos azuis da busca como hierarquia textual
- [[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]] — Google como interface de texto; Google Fonts; WhatFont no Chrome
- [[wiki/sources/classificacoes-tipograficas-serifa-sem-serifa-script-monoespacada-display]] — Google Fonts como catálogo gratuito espelhado no Figma
- [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]] — tags meta e visibilidade no Google
- [[wiki/sources/big-techs-salarios-vagas-processo-de-aplicacao]] — Google Brasil no Levels.fyi, vesting, vagas por país, contratação por time

## Adição (2026-10-14)

Lançou o [[wiki/entities/gemini-embedding-2]] (embedding multimodal); crítica do apresentador: custo e envio de dados à API ([[wiki/concepts/custo-e-privacidade-de-embedding-via-api]]).

- [[wiki/sources/gemini-embedding-2-embedding-multimodal-google]] — Gemini Embedding 2, embedding multimodal em 3072 dimensões
- [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]] — home do Google como exemplo de simplicidade e espaço em branco: um ponto focal, recursos atrás de "mais do Google"
- [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]] — home como macro espaço (foco); resultados de busca agrupados só com espaçamento e recuo, sem bordas de card
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]] — Material Design recomendado para diretrizes de imagem; ver [[wiki/entities/material-design]]
- [[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]] — engrenagem e nove pontinhos como pattern aprendido
- [[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]] — tags semânticas como ajuda ao buscador
- [[wiki/sources/introducao-mapeando-vagas]] — salário de júnior do Google em SP acima da média local

## Big Tech em Dublin e Londres

Em [[wiki/sources/quais-paises-podem-fazer-sentido-vagas-internacionais-galego]], o Google aparece entre as Big Techs que contratam presencialmente em Dublin, com visa sponsor e salários ≥ 100 mil €/ano, e em Londres ([[wiki/concepts/visa-sponsorship]]).

- [[wiki/sources/quais-paises-podem-fazer-sentido-vagas-internacionais-galego]] — contratação em Dublin/Londres como rota de imigração

## Google Careers como fonte da verdade das vagas

Em [[wiki/sources/onde-encontrar-vagas-workshop-roadmap-emprego-galego]], o board próprio do Google é "a fonte da verdade" das vagas abertas, que nem sempre chegam ao LinkedIn: 28 vagas em Zürich e 9 em Madrid na demo de abril de 2025, e a decomposição da [[wiki/concepts/total-compensation]] de um L3 via [[wiki/entities/levels-fyi]]. O PDF [[wiki/sources/onde-procurar-vagas-guia-definitivo]] indica o Google também como motor de [[wiki/concepts/busca-booleana-de-vagas|busca booleana]] e o bloco Google for Jobs.

## Chrome DevTools no FrontPUSH

Em [[wiki/sources/frontpush-propriedade-animation-parte-2-curvas-cubic-bezier-editor-chrome]], "esse editor do Google Chrome é muito legal": o editor de cubic-bezier do [[wiki/entities/chrome-devtools]].

## Key sources (adição 2026-11-16)

- [[wiki/sources/onde-encontrar-vagas-workshop-roadmap-emprego-galego]]
- [[wiki/sources/onde-procurar-vagas-guia-definitivo]]
- [[wiki/sources/frontpush-introducao-otimizacao-web-minificacao-css-js]]: FrontPUSH, otimização aula 01: experiência do usuário e ranking
- [[wiki/sources/frontpush-otimizacao-de-imagens-mobile-desktop-classes-mixin]]: FrontPUSH, otimização aula 04: aviso de tamanho de imagem
- [[wiki/sources/frontpush-google-pagespeed-core-web-vitals-acessibilidade-meta-tags]]: FrontPUSH, otimização aula 05: notas do PageSpeed e rastreamento

## Google como empregador: faixa salarial e vagas no Brasil

[[wiki/sources/big-techs-salarios-vagas-processo-de-aplicacao]] usa o Google como exemplo de [[wiki/concepts/big-tech]]: no [[wiki/entities/levels-fyi]], Brasil, L3 ≈ R$ 15 mil/mês e L5 ≈ R$ 33 mil; anual de entrada R$ 277 mil; ações com vesting 38/32/20/10% ([[wiki/concepts/equity-como-diferencial]]). No Google Careers havia 18 vagas de Software Engineer no Brasil, 4 em Málaga e 0 em Portugal na data da gravação. Times como YouTube e Google Ads contratam separadamente ([[wiki/concepts/contratacao-por-time-em-big-tech]]).
- [[wiki/sources/frontpush-o-que-e-html-linguagem-de-marcacao-tags-semantica]]: "o Google gosta [...] do HTML semântico"; div genérica dificulta a indexação
- [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]: link azul/roxo (visitado) como padrão que até o Google usa
- [[wiki/sources/frontpush-conclusao-modulo-css-estilo-layout-animacao-documentacao]]: "tenho dúvida, eu vou no Google e vou buscar a documentação"
- [[wiki/sources/jstack-como-funciona-o-nodejs]]: Chrome e V8 (2008) como origem do Node.js
- [[wiki/sources/frontpush-dom-parte-1-arvore-de-elementos-queryselector]]: FrontPUSH, JavaScript aula 08: pesquisar o DOM de forma leiga
- [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]]: FrontPUSH, JavaScript aula 10: buscar a lista de eventos
- [[wiki/sources/frontpush-relatorio-pagespeed-imagens-render-blocking-dom-regra-80-20]]: FrontPUSH, otimização aula 06: avisos do PageSpeed
- [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]]: FrontPUSH, otimização aula 07: web.dev sobre animações
- [[wiki/sources/frontpush-propriedade-animation-parte-2-curvas-cubic-bezier-editor-chrome]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 04: editor de curvas do Chrome
