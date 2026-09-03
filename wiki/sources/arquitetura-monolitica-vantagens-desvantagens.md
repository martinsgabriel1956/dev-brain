---
type: source
title: "Arquitetura Monolítica: Vantagens e Desvantagens"
aliases: ["arquitetura monolítica vídeo introdutório", "monolito vantagens desvantagens"]
date_created: 2026-09-03
date_updated: 2026-09-03
source_count: 1
tags: [monolito, arquitetura, deploy, single-point-of-failure, auto-scaling, backend]
skill: tech-mentor-backend
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/arquitetura-monolitica-vantagens-desvantagens.md
source_url: ""
author: "desconhecido (transcrição de vídeo, canal e autor não identificados na fala)"
date_published: "desconhecida"
date_ingested: 2026-09-03
---

## TL;DR

Vídeo introdutório (transcrição bruta, autor não identificado) explica arquitetura monolítica em nível de fundamentos: uma aplicação única, com múltiplos módulos (vendas, estoque, relatórios) interligados no mesmo servidor e comunicando-se por chamada de função direta. Cobre três vantagens (deploy único mais simples, reuso de código sem duplicidade, comunicação entre módulos sem custo de rede) e quatro desvantagens (cadência de deploy cai conforme o time cresce, single point of failure, auto scaling operacionalmente mais difícil — resize vertical exige desligar a máquina —, e conflito entre desenvolvedores mexendo na mesma base). Não traz dado novo além do que a wiki já documenta com mais profundidade em [[wiki/concepts/monolito]], mas serve como versão didática/introdutória do mesmo argumento, com um ângulo específico não coberto antes: a mecânica operacional de escalar verticalmente um monolito tradicional (desligar → trocar tipo de instância → religar).

## Key Claims

1. **Reuso de código como vantagem central do monolito, explicado via exemplo concreto de classe compartilhada:** uma classe "produtos" definida uma vez é chamada diretamente por estoque, vendas e relatórios; atualizar a classe num único lugar propaga a mudança para todos os módulos automaticamente. A fonte contrasta isso com microsserviços, onde replicar a mesma lógica em serviços diferentes é "geralmente mais difícil" — mas não detalha o mecanismo (contratos de API, client libraries versionadas) que microsserviços usam para mitigar essa duplicidade. Confiança alta para o mecanismo dentro do monolito (chamada de função direta, sem rede); confiança baixa para a generalização não qualificada sobre microsserviços.
2. **Cadência de deploy cai conforme o time cresce, mesmo com ferramentas de gestão ágil (kit/sprint) — múltiplos desenvolvedores mexendo na mesma aplicação forçam deploys coordenados e menos frequentes**, tipicamente amarrados a um dia fixo da semana (ex.: toda quinta ou duas vezes por semana) em vez de deploy contínuo por módulo. A causa raiz apontada é a impossibilidade de fazer deploy de um módulo isolado — o artefato é único, então a esteira espera a sprint inteira fechar.
3. **Single point of failure explicado por causa e efeito, não só nomeado:** um bug numa nova versão do módulo de estoque pode derrubar a aplicação inteira, incluindo vendas — porque todos os módulos compartilham processo e deploy. A fonte nomeia isso explicitamente como "single point of failure", reforçando [[wiki/concepts/single-point-of-failure]] com o caso específico de falha de módulo (não só falha de servidor físico).
4. **Auto scaling vertical num monolito tradicional descrito como processo manual com indisponibilidade: desligar a instância, trocar o tipo (mais CPU/memória), religar.** A fonte enquadra isso como desvantagem operacional do monolito de servidor único frente a arquiteturas que escalam com menos fricção — mas não menciona auto scaling horizontal automatizado (ASG, HPA) como alternativa aplicável a monolitos também, tratando escala vertical manual como se fosse a única opção disponível. Isso é uma simplificação: [[wiki/concepts/auto-scaling]] e [[wiki/concepts/escalabilidade-horizontal]] já documentam que monolitos rodam perfeitamente atrás de load balancer com múltiplas réplicas idênticas, sem downtime de resize — a fonte conflates "monolito" com "servidor único sem réplicas", o que é comum na prática mas não é definição estrita do estilo arquitetural.
5. **Comunicação entre módulos sem custo de rede (chamada de função em vez de chamada HTTP/RPC) é citada como vantagem de latência/simplicidade** — mecanismo consistente com o que já está documentado em [[wiki/concepts/monolito]] ("comunicam-se por chamadas de função diretas").

## Entidades e Conceitos Tocados

- [[wiki/concepts/monolito]]
- [[wiki/concepts/microsservicos]]
- [[wiki/concepts/single-point-of-failure]]
- [[wiki/concepts/auto-scaling]]
- [[wiki/concepts/escalabilidade-vertical]]
- [[wiki/concepts/dry]]
- [[wiki/concepts/zero-downtime-deploy]]

## Contradições / Reforços com o Resto da Wiki

**Reforço direto, sem dado novo relevante:** [[wiki/concepts/monolito]] já cobre "um único artefato, deploy único... módulos comunicam-se por chamadas de função diretas" e a relação com [[wiki/concepts/single-point-of-failure]] via [[wiki/concepts/escalabilidade-vertical]]. Esta fonte não adiciona claim quantitativo ou caso real (ao contrário de [[wiki/sources/microsservicos-monolito-first-renato-augusto]], que traz o caso Amazon Prime Video) — o valor dela é puramente didático/introdutório, útil como fonte de baixo nível para quem está aprendendo o conceito pela primeira vez.

**Tensão não resolvida, sinalizada nesta ingestão:** a claim 4 (auto scaling do monolito = desligar/religar manualmente) simplifica demais frente ao que [[wiki/concepts/auto-scaling]] e [[wiki/concepts/escalabilidade-horizontal]] já documentam — um monolito pode escalar horizontalmente (múltiplas instâncias idênticas atrás de load balancer, com Auto Scaling Group) sem downtime, exatamente como qualquer outra arquitetura stateless. O que a fonte descreve é especificamente escala **vertical** de single-server, não uma limitação inerente ao estilo monolítico. Registrado como observação de calibração, não como contradição factual grave — a fonte não afirma que monolito não possa escalar horizontalmente, só não menciona a alternativa.

## Open Questions

- **Autoria e canal não identificados** — a transcrição não nomeia o apresentador nem o canal; sem contexto para verificar credenciais ou comparar com outras fontes do mesmo autor.
- **Nenhuma fonte primária ou dado quantitativo citado** — todas as afirmações são generalizações qualitativas de experiência, sem benchmark, link ou caso real nomeado (diferente de [[wiki/sources/microsservicos-monolito-first-renato-augusto]] ou [[wiki/sources/monolith-first-martin-fowler]]).

## Raw Quotes

> "Se alguém vier aqui e fizer um deploy do estoque... por algum motivo ela estiver defeituosa, com um bug, ela pode afetar toda a sua aplicação... isso é conhecido como single point of failure."

> "Você cria uma classe dentro da sua aplicação que chama produtos... o estoque pode usar essa classe, vendas pode usar essa classe, eventualmente relatórios pode usar essa classe, e é só uma classe — se você for atualizar alguma coisa nela, simplesmente altera ali e todos eles acabam tendo acesso a essa informação."
