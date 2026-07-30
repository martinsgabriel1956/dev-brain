---
type: source
title: "DevSecOps — Origem, Cultura e Manifesto"
aliases: ["devsecops origem", "devopssec", "manifesto devsecops", "dicionário do programador devsecops"]
date_created: 2026-07-30
date_updated: 2026-07-30
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/devsecops-origem-cultura-manifesto.md
source_url: ""
author: "Código Fonte TV (quadro Dicionário do Programador)"
date_published: ""
date_ingested: 2026-07-30
source_count: 0
tags: [devsecops, devops, shift-left, manifesto, cultura-de-seguranca, sast, sca, compliance]
skill: tech-mentor-security
status: stable
---

## TL;DR

DevSecOps (*Development, Security and Operations*) é a extensão do DevOps que trata segurança como responsabilidade compartilhada em todo o ciclo de vida do software, não como setor isolado no fim do pipeline. O termo nasceu em 2012 (Gartner), três anos depois do próprio DevOps ser cunhado por Patrick Debois em 2009 — a partir da observação de que ciclos de deploy rápidos e colaborativos (o caso seminal é a palestra da Flickr na Velocity 2009, "10+ Deploys por Dia") não bastavam sem incorporar segurança da mesma forma ágil. Batizado inicialmente "DevOpsSec". O Manifesto DevSecOps propõe atacar produtos como um invasor externo faria, em vez de confiar só em scanners, e buscar anomalias não catalogadas em vez de só o que já é conhecido. A fonte mapeia ferramentas por fase do ciclo (planejamento → build → deploy → operação) e reforça que DevSecOps é tanto cultura/pessoas quanto ferramental — "pessoas verificam ferramentas, e ferramentas verificam pessoas".

## Key Claims

**Claim:** DevOps foi cunhado por Patrick Debois em 2009, inspirado pela palestra da Flickr na Velocity ("10+ Deploys por Dia: Cooperação entre Desenvolvedores e Operações no Flickr"), e formalizado no primeiro DevOps Day em Gante, Bélgica, no mesmo ano.
**Evidence:** Debois já defendia desde 2008 um "movimento ágil" aplicado a infraestrutura (não só a desenvolvimento), documentado em seu blog Jedi (*Just Enough Documented Information*). A palestra da Flickr na Velocity 2009 (apresentada por dois funcionários da empresa) é citada como o ponto de virada que deu tração à ideia.
**Confidence:** média — consistente com a narrativa histórica amplamente conhecida sobre a origem do DevOps (John Allspaw e Paul Hammond, Flickr, Velocity 2009), mas a fonte não cita os nomes dos palestrantes nem link direto para a apresentação original.

**Claim:** O termo "DevSecOps" surgiu em 2012, cunhado pela Gartner, três anos após o DevOps — inicialmente como "DevOpsSec", antes de se estabilizar na ordem atual.
**Evidence:** A fonte atribui a cunhagem à Gartner e situa a motivação na percepção de que segurança tratada como setor isolado ("em silos") não era compatível com entregas ágeis e colaborativas já praticadas sob DevOps.
**Confidence:** média — não há link ou citação direta ao relatório/analista da Gartner que originou o termo.

**Claim:** O Manifesto DevSecOps propõe postura ofensiva/proativa: atacar o próprio produto como um invasor externo faria, e procurar ativamente por anomalias não catalogadas, em vez de depender só de scanners e do que já é conhecido.
**Evidence:** Citação direta do manifesto na fonte: "Não vamos simplesmente confiar em scanners e relatórios para melhorar a segurança — atacaremos produtos e serviços como alguém de fora para ajudá-lo a defender o que você criou (...) Não nos contentaremos em encontrar o que já é conhecido; em vez disso, procuraremos por anomalias ainda não detectadas."
**Confidence:** alta — citação textual do manifesto, ainda que sem URL da fonte primária na transcrição.

**Claim:** DevSecOps segue a abordagem *shift-left testing* — segurança testada desde o início do ciclo (planejamento, código) e não só no fim (deploy/produção) — promovida por um guideline de uma fundação sem fins lucrativos de segurança de software (referência de áudio ambígua, provavelmente OWASP).
**Evidence:** A fonte descreve fases do ciclo DevOps (planejamento, código, build, teste, release, deploy, operação, monitoramento) mapeadas a ferramentas de segurança específicas em cada fase, e cita secret scanning, SCA e IAST como categorias de verificação que cobrem do planejamento ao deploy.
**Confidence:** baixa-média — o nome da fundação citada no áudio não corresponde exatamente a nenhuma organização conhecida ("Alexlog"); mantido como ouvido na transcrição, com nota de que o guideline DevSecOps mais conhecido do tipo descrito é o da OWASP (ver [[wiki/sources/owasp-top10]]).

**Claim:** DevSecOps não é apenas ferramental — pessoas e cultura são parte do sistema de segurança, resumido na frase "pessoas verificam ferramentas, e ferramentas verificam pessoas. Confie, mas verifique."
**Evidence:** A fonte argumenta que atualizações constantes em linguagens, frameworks, bibliotecas e sistemas operacionais exigem um "movimento ativo" de segurança contínua que não se resolve só automatizando — precisa de participação ativa de times.
**Confidence:** média — afirmação qualitativa/cultural, sem dado quantitativo de suporte.

**Claim:** Alta demanda de mercado para profissionais de cloud/segurança — pesquisa da Brasscom projetava ~565 mil vagas de tecnologia no Brasil até 2025, das quais ~125 mil em cloud e segurança; 5 mil vagas com o termo "DevSecOps" no LinkedIn para trabalho remoto no momento da gravação.
**Evidence:** Números citados na fala sem link direto à pesquisa da Brasscom ou à busca no LinkedIn.
**Confidence:** baixa — números desatualizados (o vídeo é anterior a 2025, hoje já passado) e sem fonte primária citada na transcrição.

## Entities & Concepts Touched

- [[wiki/concepts/devsecops]]
- [[wiki/concepts/shift-left-testing]]
- [[wiki/concepts/compliance]]
- [[wiki/concepts/sast]]
- [[wiki/entities/patrick-debois]]
- [[wiki/entities/flickr]]
- [[wiki/entities/gartner]]
- [[wiki/sources/devsecops-pipeline]]
- [[wiki/sources/owasp-top10]]

## Open Questions

- A fundação citada no áudio como autora do guideline DevSecOps ("Alexlog") não corresponde a nenhuma organização identificável — provavelmente OWASP, mas não confirmado na transcrição. Precisa de verificação externa se o guideline específico for citado de novo em fonte futura.
- Sem link direto ao relatório da Gartner de 2012 que teria cunhado "DevSecOps" — vale checar contra fontes futuras que tratem da história do termo.
- Números de mercado (Brasscom, LinkedIn) desatualizados mesmo na época da gravação (projeção "até 2025") — não usar como dado de mercado atual em respostas futuras.
