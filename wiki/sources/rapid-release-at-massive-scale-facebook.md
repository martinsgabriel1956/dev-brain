---
type: source
title: "Rapid Release at Massive Scale (Facebook Engineering, 2017)"
aliases: ["rapid release at massive scale", "push from master facebook", "meta continuous deployment web"]
date_created: 2026-07-31
date_updated: 2026-07-31
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/rapid-release-at-massive-scale-facebook.md
source_url: "https://engineering.fb.com/2017/08/31/web/rapid-release-at-massive-scale/"
author: "Chuck Rossi"
date_published: "2017-08-31"
date_ingested: 2026-07-31
source_count: 0
tags: [ci-cd, deploy, feature-flags, canary-release, dora-metrics, meta, facebook, deploy-strategies]
skill: tech-mentor-infra
status: stable
---

# Rapid Release at Massive Scale (Facebook Engineering, 2017)

## TL;DR

Post de engenharia do Facebook (2017) descrevendo a transição do deploy web de um modelo de branch de release com 500-700 cherry-picks manuais por dia para um sistema quase-contínuo de "push direto da master", atingindo 100% dos servidores de produção em abril de 2017. É um caso real, em escala massiva, do que a pesquisa [[wiki/concepts/dora-metrics|DORA]] só formalizaria depois: deploy mais frequente e com lead time menor, sem sacrificar qualidade — sustentado por rollout escalonado (funcionários → 2% → 100%) e por [[wiki/concepts/feature-flags|feature flags]] (Gatekeeper) para desacoplar deploy de release.

## Key Claims

- **O modelo antigo (branch de release + cherry-pick) ficou insustentável pelo volume, não por escolha filosófica.** Em 2016 a master já recebia mais de 1.000 diffs/dia e os pushes semanais acumulavam até 10.000 diffs — o cherry-pick manual (500-700/dia) não escalava mais. → [[wiki/concepts/ci-cd]]
- **A migração foi gradual e escalonada, não um "big bang".** De abril de 2016 a abril de 2017, o rollout foi de funcionários internos para porcentagens crescentes de tráfego de produção, até 100%. Esse padrão de expansão gradual é o mesmo princípio do [[wiki/concepts/canary-release]], aplicado à mudança de *processo* de deploy, não só a uma versão de código.
- **O deploy contínuo publica dezenas a centenas de diffs a cada poucas horas**, num rollout em 3 estágios: funcionários → ~2% de produção → 100%. Isso permite monitorar e interromper antes de atingir todo o tráfego.
- **Gatekeeper desacopla deploy de release.** O sistema de feature toggle da Meta (Gatekeeper) permite habilitar/desabilitar funcionalidades sem reverter ou re-deployar uma versão — instância concreta de [[wiki/concepts/deploy-vs-release]] e do mecanismo geral descrito em [[wiki/concepts/feature-flags]]. *Nota de desambiguação: este "Gatekeeper" da Meta (feature-flag/release toggle) é uma entidade diferente do [[wiki/concepts/gatekeeper-pattern]] já documentado na wiki (padrão de segurança de ponto único de entrada) — mesmo nome, conceitos não relacionados.*
- **Deploy contínuo elimina a necessidade de hotfix de emergência**, porque mudanças chegam a produção quase imediatamente pelo fluxo normal, em vez de exigir push fora de banda.
- **Remove a dependência de fuso horário para os pushes**, importante para um time de engenharia distribuído globalmente.
- **O ritmo de deploy força melhorias de infraestrutura** (testes, tooling, automação) — a pressão de deploy contínuo é motor de investimento em plataforma interna, não o contrário.
- **Mobile não permite deploy verdadeiramente contínuo** (lojas de app, tempo de propagação para o usuário), mas a Meta aplicou os mesmos princípios ao ciclo mobile, saindo de releases de 4 semanas para 1 semana, com ferramentas internas (Nuclide, Buck, Phabricator, React Native, Infer). → [[wiki/concepts/mobile-feature-flags]]
- **Escala 15x do time (Android/iOS) sem queda de produtividade por engenheiro nem aumento de incidentes críticos por release** — evidência empírica pré-DORA de que velocidade e qualidade não são trade-off, indo na mesma direção do achado central documentado em [[wiki/concepts/dora-metrics]].

## Entities

[[wiki/entities/meta]]

## Concepts

[[wiki/concepts/ci-cd]] · [[wiki/concepts/canary-release]] · [[wiki/concepts/feature-flags]] · [[wiki/concepts/deploy-vs-release]] · [[wiki/concepts/dora-metrics]] · [[wiki/concepts/mobile-feature-flags]] · [[wiki/concepts/deploy-strategies]] · [[wiki/concepts/gatekeeper-pattern]] (desambiguação)

## Conexão com fontes existentes

Esta fonte é o caso de origem por trás da menção já registrada em [[wiki/concepts/canary-release]] ("o que a Meta chama de massive rollout at massive scale") — antes desta ingestão, essa menção não tinha uma fonte própria citada. Também complementa [[wiki/concepts/dora-metrics]] com um exemplo real, anterior à formalização acadêmica da pesquisa DORA (livro *Accelerate*, 2018), de uma empresa observando exatamente a correlação "mais deploys, mesma ou melhor qualidade" na prática, em escala de milhares de engenheiros.

## Open Questions

- O artigo não detalha como o Gatekeeper decide o percentual de rollout (manual vs. automático por métrica) — diferente do Canary/Argo Rollouts já documentado na wiki, que tem análise automática via Prometheus. Não está claro se em 2017 a Meta já tinha esse nível de automação ou se a decisão de avançar de estágio era humana.
- Não há dados numéricos de Change Failure Rate ou MTTR no artigo — as afirmações de "qualidade constante" são qualitativas ("praticamente constante"), sem tabela de métricas.
- O artigo é de 2017; não cobre como o sistema evoluiu desde então (ex.: se o Gatekeeper atual da Meta ainda opera da mesma forma).

## Raw Quotes

Não incluídas — o artigo original está sob copyright da Meta/Engineering at Meta; o resumo acima e o arquivo em `raw/rapid-release-at-massive-scale-facebook.md` são paráfrases fiéis do conteúdo, não transcrição literal.
