---
type: concept
title: "DevSecOps"
aliases: ["devsecops", "devopssec", "development security and operations"]
date_created: 2026-07-30
date_updated: 2026-08-06
source_count: 3
tags: [devsecops, devops, security-culture, shift-left, sast, sca, ci-cd-security]
skill: tech-mentor-security
status: stable
---

# DevSecOps

*Development, Security and Operations.* Extensão cultural e técnica do [[wiki/concepts/compliance|DevOps]] que trata segurança como responsabilidade compartilhada em todo o ciclo de vida do software, em vez de setor isolado que só entra no fim do pipeline (revisão de segurança pré-produção, isolada, feita por outro time).

## Origem

O termo surgiu em 2012, cunhado pela [[wiki/entities/gartner]], três anos depois do próprio DevOps ter sido formalizado por [[wiki/entities/patrick-debois]] em 2009 no primeiro DevOps Day (Gante, Bélgica). Foi tratado inicialmente como "DevOpsSec", antes de se estabilizar na ordem atual. A motivação: ciclos de deploy ágeis e colaborativos (o caso seminal de referência é a palestra "10+ Deploys por Dia" da [[wiki/entities/flickr]] na Velocity 2009) não bastavam sem incorporar segurança com a mesma agilidade — segurança em silo virou o gargalo que a cultura DevOps já tinha resolvido para desenvolvimento e operações.

## O Manifesto DevSecOps

Postura deliberadamente ofensiva/proativa, não apenas reativa a scanners:

- Não confiar só em scanners e relatórios — atacar o próprio produto como um invasor externo faria.
- Não esperar que a organização seja vítima de erros e invasores — antecipar.
- Não se contentar em encontrar apenas o que já é conhecido — procurar ativamente por anomalias ainda não catalogadas.

## Segurança em Todo o Ciclo, Não Só no Fim

Segue a abordagem [[wiki/concepts/shift-left-testing]]: testes de segurança entram desde o planejamento e o código, não só no deploy/produção. Mapeamento típico de ferramentas por fase:

| Fase do ciclo | Tipo de verificação |
|---|---|
| Planejamento | Threat modeling, gestão de risco |
| Código / Build | [[wiki/concepts/sast]], secret scanning, SCA |
| Deploy | Certificados TLS, verificação de integridade |
| Operação / Monitoramento | Detecção de intrusão, runtime security |

Categorias de verificação citadas: **secret scanning** (vazamento de credenciais em repositório), **SCA** — Software Composition Analysis (dependências vulneráveis) e **IAST** — Interactive Application Security Testing (testes interativos em runtime). Ver [[wiki/sources/devsecops-pipeline]] para o detalhamento técnico de gates de pipeline (Semgrep, Trivy, OPA/Conftest, Kyverno) que implementam esse modelo na prática.

## Cultura, Não Só Ferramental

DevSecOps não se resolve automatizando sozinho — pessoas e times são parte do sistema de segurança, não só usuários dele. Resumo da fonte: "pessoas verificam ferramentas, e ferramentas verificam pessoas. Confie, mas verifique." Atualizações constantes em linguagens, frameworks e bibliotecas exigem um movimento ativo e contínuo, não uma auditoria pontual.

## DevSecOps e Compliance

Diante de brechas de segurança, frameworks como ITIL, COBIT e [[wiki/concepts/iso-27001]] — e [[wiki/concepts/compliance]] de forma geral — fornecem o conjunto de regras que orienta a reação, mas a fonte enfatiza que a resposta precisa vir de processos ágeis integrados ao fluxo de desenvolvimento, não de auditorias isoladas pós-deploy.

## Cadência de Review Precisa Acompanhar a Velocidade de Produção com IA

[[wiki/sources/codigo-gerado-por-ia-mais-falhas-seguranca-degradacao-iterativa]] argumenta que times que adotaram IA para gerar código sem atualizar a cadência de security review estão acumulando dívida de segurança na mesma velocidade da produtividade ganha — o ritmo típico de "uma vez por sprint ou por mês" deixou de ser suficiente e precisa passar a ser **por feature ou por iteração significativa**, dado que refinamento iterativo com IA pode degradar segurança rapidamente (ver [[wiki/concepts/degradacao-de-seguranca-iterativa-ia]]). É uma aplicação concreta e específica do princípio geral desta página de que segurança precisa acompanhar o ritmo real do ciclo de desenvolvimento, não ser um checkpoint isolado no fim.

## Key Sources

- [[wiki/sources/devsecops-origem-cultura-manifesto]] — origem histórica, Manifesto DevSecOps, mapeamento de ferramentas por fase do ciclo, cultura de pessoas
- [[wiki/sources/devsecops-pipeline]] — implementação técnica em CI/CD: SAST, SCA, container scanning, DAST, Policy as Code
- [[wiki/sources/codigo-gerado-por-ia-mais-falhas-seguranca-degradacao-iterativa]] — cadência de security review precisa escalar com a velocidade de geração de código por IA

## Conceitos Relacionados

[[wiki/concepts/shift-left-testing]] · [[wiki/concepts/sast]] · [[wiki/concepts/compliance]] · [[wiki/concepts/supply-chain-security]] · [[wiki/concepts/defense-in-depth]] · [[wiki/concepts/attack-surface]]
