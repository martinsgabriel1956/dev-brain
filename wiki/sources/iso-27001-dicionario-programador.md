---
type: source
title: "ISO 27001 — Dicionário do Programador"
aliases: ["iso 27001", "iso/iec 27001", "sgsi", "isms", "dicionário do programador iso"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/iso-27001-dicionario-programador.md
source_url: ""
date_published: ""
date_ingested: 2026-07-03
source_count: 0
tags: [iso-27001, sgsi, isms, compliance, security, tríade-cia, annex-a, policy-as-code, opa, segregacao-de-funcoes, iso-42001, lgpd]
skill: tech-mentor-security
status: stable
---

## TL;DR

ISO/IEC 27001 define os requisitos de um SGSI (Sistema de Gestão de Segurança da Informação) — framework de gestão, não produto — organizado em torno da tríade CIA (Confidentiality, Integrity, Availability). A versão 2022 reduziu o Anexo A de 114 para 93 controles, reorganizados em 4 temas (Organizacional, Pessoas, Físico, Tecnológico). Para devs, os controles mais relevantes são codificação segura (A.8.28), controle de acesso (A.5.15), segurança em gestão de projetos (A.5.8), SDLC seguro (A.8.25) e segregação de funções (A.5.3). A tendência de mercado é Policy as Code (OPA/Gatekeeper) para transformar essas exigências em travas automatizadas de pipeline em vez de depender de processo manual. A ISO 42001 (2023) estende a governança para IA responsável, plugando-se à 27001 via Anexo SL.

## Key Claims

**Claim:** SGSI não é um produto — é um framework de gestão sistêmico (políticas + procedimentos + processos + tecnologia) organizado em torno da tríade CIA.
**Evidence:** A norma exige a criação formal de um Sistema de Gestão de Segurança da Informação que garante confidencialidade (só entra quem pode — credencial/chave SSH/JWT), integridade (dado gravado = dado lido — hashes, assinaturas digitais, commits assinados) e disponibilidade (sistema ativo e resiliente a picos — redundância, backup testado, proteção DDoS).
**Confidence:** alta — consistente com [[wiki/sources/compliance-soc2-pci]], que já descreve o SGSI/ISMS com Risk Assessment formal.

**Claim:** A versão 2022 da norma reduziu o Anexo A de 114 para 93 controles e reorganizou 14 domínios em 4 temas lógicos (Organizacional: 37, Pessoas: 8, Físico: 14, Tecnológico: 34).
**Evidence:** Motivação explícita: a versão 2013 é anterior ao Docker, Kubernetes e à nuvem moderna, e não cobria inteligência de ameaças nem segurança em nuvem de forma nativa.
**Confidence:** média-alta — números específicos (114→93, 37/8/14/34) não foram cruzados com o texto oficial da norma nesta ingestão; tratar como declarado pela fonte, não verificado em texto primário.

**Claim:** A SoA (Statement of Applicability / Declaração de Aplicabilidade) é o documento onde a empresa justifica quais dos 93 controles do Anexo A aplica e por quê os demais não se aplicam ao seu contexto de risco.
**Evidence:** Exemplo dado: controles de segurança física (Anexo A "Físico") não se aplicam a uma empresa 100% remota sem escritório.
**Confidence:** alta.

**Claim:** Os controles do Anexo A com maior impacto direto no trabalho de quem escreve código são A.8.28 (codificação segura), A.5.15 (controle de acesso), A.5.8 (segurança em gestão de projetos), A.8.25 (SDLC seguro) e A.5.3 (segregação de funções).
**Evidence:** Detalhamento por controle — A.8.28: OWASP Top 10/CWE Top 25, input validation, checagem de vulnerabilidades em dependências; A.5.15: least privilege, RBAC, JWT com scopes definidos (nunca `admin:true` global); A.5.8: security by design desde o planning; A.8.25: SAST/DAST na pipeline + ambientes segregados (dev/staging/prod); A.5.3: quem desenvolve não deve ser quem faz deploy sozinho em produção — PR com aprovação de outro dev é a implementação técnica.
**Confidence:** alta para a intenção de cada controle; a numeração específica (A.8.28, A.5.15 etc.) reflete a reorganização 2022 e diverge da numeração usada em [[wiki/sources/compliance-soc2-pci]] e em [[wiki/concepts/audit-log]] (que citam "A.12.4" — numeração pré-2022). Ver nota de contradição abaixo.

**Claim:** A.5.3 (segregação de funções) é o controle mais polêmico na prática — em times pequenos, manter "quem codifica ≠ quem faz deploy sozinho" é difícil ou quase impossível.
**Evidence:** Aponta o PR com aprovação de outro dev como a implementação técnica padrão do controle, mas reconhece a tensão real em equipes enxutas.
**Confidence:** alta — julgamento qualitativo plausível, não uma medição.

**Claim:** Policy as Code (ex.: Open Policy Agent/Rego, Gatekeeper no Kubernetes) é a tendência de mercado para transformar política de compliance em trava automática de pipeline, eliminando dependência da leitura humana da política.
**Evidence:** Dois exemplos concretos — (1) Terraform subindo bucket S3 público quebra a pipeline via política Rego que proíbe ACL `public-read`; (2) Gatekeeper inspeciona `securityContext.privileged` em manifests de container e bloqueia admissão se `true`. Ambos os exemplos also satisfazem A.8.4 (acesso ao código-fonte) e A.5.15 (controle de acesso), pois codificam quem pode configurar o quê.
**Confidence:** alta — alinhado com [[wiki/sources/policy-as-code]] e [[wiki/sources/devsecops-pipeline]], que já cobrem OPA/Rego/Gatekeeper como padrão de DevSecOps.

**Claim:** A ISO 42001 (lançada no final de 2023) cobre a lacuna de governança de IA responsável (ética, viés algorítmico, transparência, accountability) que a 27001 não endereça — e se pluga à 27001 via Anexo SL, estrutura padrão comum a normas de sistema de gestão. Empresas já certificadas em 27001 implementariam a 42001 até 40% mais rápido.
**Evidence:** Nenhuma fonte primária citada no vídeo além da existência da norma; o percentual "40% mais rápido" é uma afirmação do apresentador, sem estudo referenciado.
**Confidence:** média — a existência e o escopo da ISO 42001 são verificáveis externamente [external], mas o número "40%" deve ser tratado como não verificado.

**Claim:** O controle A.5.34 (privacidade e proteção de PII) é o "link técnico direto" entre ISO 27001 e a LGPD brasileira.
**Evidence:** Não detalhado além da menção do número do controle.
**Confidence:** média — coerente com o que [[wiki/sources/lgpd-gdpr]] já cobre sobre bases legais e mapeamento de dados, mas a ligação de controle específico não foi cruzada com o texto da norma.

**Claim:** Nubank, Mercado Livre e SciELO Brasil são exemplos reais de certificação ISO 27001 no Brasil, cada um ilustrando um pilar diferente da tríade CIA.
**Evidence:** Nubank — "modo rua" do app (fora de rede Wi-Fi segura, limita transações) como controle de acesso contextual; Mercado Livre — combina ISO 27001 + PCI-DSS e aplica Zero Trust em uma superfície de ataque grande (pagamentos, logística, varejo); SciELO Brasil — certificação anunciada em 2025, focada em integridade e disponibilidade de dados de pesquisa científica.
**Confidence:** média-alta para a existência das certificações (checável externamente [external]); os detalhes de implementação (ex.: "modo rua" = controle de acesso contextual) são interpretação do apresentador, plausível mas não confirmada pelas próprias empresas nesta fonte.

## Entities & Concepts Touched

- [[wiki/concepts/iso-27001]]
- [[wiki/concepts/sgsi-isms]]
- [[wiki/concepts/triade-cia]]
- [[wiki/concepts/segregacao-de-funcoes]]
- [[wiki/concepts/iso-42001]]
- [[wiki/concepts/compliance]]
- [[wiki/concepts/audit-log]]
- [[wiki/concepts/principio-menor-privilegio]]
- [[wiki/entities/nubank]]
- [[wiki/entities/mercado-livre]]
- [[wiki/sources/compliance-soc2-pci]]
- [[wiki/sources/policy-as-code]]
- [[wiki/sources/devsecops-pipeline]]
- [[wiki/sources/lgpd-gdpr]]
- [[wiki/sources/rbac-abac-rebac]]
- [[wiki/sources/owasp-top10]]

## Open Questions

- Numeração de controles do Anexo A citada nesta fonte (A.8.28, A.5.15, A.5.8, A.8.25, A.5.3, A.8.4, A.5.34) diverge da numeração pré-2022 citada em [[wiki/sources/compliance-soc2-pci]] e [[wiki/concepts/audit-log]] ("A.12.4" para logging). Não é necessariamente uma contradição — a reorganização de 2022 de fato renumerou o Anexo A — mas nenhuma das duas fontes foi cruzada com o texto oficial da norma para confirmar o mapeamento exato entre numeração antiga e nova. Vale revisão contra a norma primária antes de tratar qualquer numeração como definitiva.
- Os números "40% mais rápido" (contratos enterprise por certificação, e implementação da ISO 42001 partindo da 27001) não têm fonte primária citada no vídeo — tratados como [external]/não verificados.
- Como a segregação de funções (A.5.3) se sustenta na prática em times pequenos sem virar teatro de compliance (aprovação de PR por alguém que não teve tempo de revisar de verdade)?
