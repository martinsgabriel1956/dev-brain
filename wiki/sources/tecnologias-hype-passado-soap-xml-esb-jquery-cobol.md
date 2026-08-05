---
type: source
title: "Tecnologias que Já Foram Hype (e Ainda Sustentam o Mundo)"
aliases: ["SOAP XML ESB jQuery COBOL", "tecnologias ultrapassadas que ainda rodam"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 0
tags: [tech-mentor-backend, soap, xml, esb, jquery, cobol, legado, integracao, hype-cycle]
skill: tech-mentor-backend
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/tecnologias-hype-passado-soap-xml-esb-jquery-cobol.md
source_url:
author: Bernardo Lobato
date_published:
date_ingested: 2026-08-04
---

# Tecnologias que Já Foram Hype (e Ainda Sustentam o Mundo)

## TL;DR

Vídeo reflexivo de [[wiki/entities/bernardo-lobato]] sobre o descompasso entre o "ciclo de hype" da comunidade dev e o ritmo real com que tecnologias deixam de ser usadas em produção. Percorre cinco tecnologias — SOAP, XML, ESB, jQuery e COBOL — que saíram do mainstream de conferências e redes sociais mas continuam sustentando sistemas críticos (bancos, seguradoras, governo, sistema financeiro). Argumento central: nenhuma delas morreu de verdade, apenas saíram das notícias; a indústria é obcecada com o novo, mas o que sustenta o mundo na maior parte do tempo é o que já roda há décadas sem holofote.

## Key Claims

1. **O ciclo de hype da comunidade não é o mesmo ritmo da obsolescência real** — uma tecnologia pode sumir de conferências, cursos e redes sociais e continuar recebendo manutenção diária em empresas gigantescas.
2. **[[wiki/concepts/soap|SOAP]] (1998) resolveu interoperabilidade entre plataformas heterogêneas** com evidência: soluções same-platform como Java RMI e CORBA não resolviam integração entre Java, C++ e .NET; o ecossistema WS-Security/WS-ReliableMessaging/WS-AtomicTransaction supria exigências de segurança e transação distribuída que bancos/seguradoras exigiam.
3. **SOAP perdeu espaço em projetos novos a partir de 2010** com a evidência de que REST + JSON atendia a maior parte dos cenários web/mobile com muito menos complexidade de infraestrutura — mas continua rodando em bancos, seguradoras, saúde, governo, e na integração de NF-e com a Receita Federal brasileira.
4. **[[wiki/concepts/xml-extensible-markup-language|XML]] (1998) virou espinha dorsal da tecnologia corporativa** nos anos 2000 — evidência: formato de mensagem do SOAP, `pom.xml` do Maven, `build.xml` do Ant, ecossistema JAXB/DOM/SAX/XSD/XSLT.
5. **XML perdeu terreno principalmente em APIs web públicas**, não no uso corporativo/documental — JSON venceu por ser mais compacto e barato de serializar/desserializar em JavaScript, mas XML segue essencial em Office, projetos Java, config, NF-e e padrões internacionais de troca de dados.
6. **[[wiki/concepts/esb-enterprise-service-bus|ESB]] (início dos anos 2000) resolveu a explosão combinatória de integrações ponto-a-ponto** em grandes empresas com dezenas/centenas de sistemas (ERP, CRM, legados) — evidência: centraliza transformação de mensagens, roteamento e orquestração; muitos serviços SOAP eram publicados dentro de plataformas de ESB (MuleSoft, IBM Integration Bus, Oracle Service Bus).
7. **ESB perdeu espaço com a chegada de nuvem, arquitetura orientada a eventos e economia de APIs** — equipes passaram a preferir integração distribuída (REST, mensageria, Kafka) a um barramento central; ainda assim segue essencial em empresas com grande legado tecnológico que não podem substituir infraestrutura de integração de uma vez.
8. **[[wiki/concepts/jquery|jQuery]] (2006) resolveu fragmentação de DOM/JavaScript entre navegadores** — antes dele, uma funcionalidade que funcionava no Firefox podia falhar no Internet Explorer; a biblioteca padronizou seleção de elementos, manipulação de HTML e Ajax sob o lema "write less, do more".
9. **jQuery perdeu espaço por dois motivos simultâneos**: navegadores passaram a seguir padrões com mais consistência, e o próprio JavaScript absorveu funcionalidades via ES6 (2015); frameworks baseados em componente (React, Vue, Angular) completaram o deslocamento — mesmo assim, jQuery segue com manutenção ativa (release em 17/01/2026) e presente em sistemas corporativos.
10. **[[wiki/concepts/cobol|COBOL]] (1959) foi criado para representar regra de negócio de forma legível e portável entre fabricantes de hardware**, num momento em que computadores passavam de cálculo científico para automação administrativa.
11. **COBOL praticamente desapareceu de discussões sobre projetos novos, mas sustenta grande parte do sistema financeiro mundial** — incluindo, no Brasil, infraestrutura que dá suporte ao Pix; a estratégia dominante não é reescrever, é modernizar a borda (APIs, filas) mantendo o núcleo em COBOL.
12. **COBOL continua evoluindo formalmente** — versão mais recente do padrão publicada em 2023, com orientação a objetos, tipos definidos pelo usuário e suporte a Unicode, mais de 60 anos após a criação da linguagem.

## Entidades Mencionadas

- [[wiki/entities/microsoft]] — participação forte na criação original do SOAP; criadora do WCF (.NET) e do Windows como plataforma que motivou parte da demanda por interoperabilidade
- [[wiki/entities/w3c]] — padronizou SOAP e tornou XML recomendação oficial em 1998
- [[wiki/entities/john-resig]] — criador do jQuery em 2006
- [[wiki/entities/react]] — citado, junto com Vue e Angular, como parte do deslocamento de paradigma que reduziu o espaço do jQuery

## Conceitos Tocados

- [[wiki/concepts/soap]]
- [[wiki/concepts/xml-extensible-markup-language]]
- [[wiki/concepts/esb-enterprise-service-bus]]
- [[wiki/concepts/jquery]]
- [[wiki/concepts/cobol]]
- [[wiki/concepts/contrato-de-api]]
- [[wiki/concepts/microsservicos]]
- [[wiki/concepts/strangler-fig-pattern]]
- [[wiki/concepts/cargo-cult-tecnologico]]

## Open Questions

- Vídeo não cita fontes primárias para as datas e números apresentados (ex.: períodos exatos de "auge" de cada tecnologia) — didático, tom de canal técnico, mas sem rigor de citação acadêmica, mesmo padrão observado em outras fontes de vídeo já mapeadas na wiki (ver [[wiki/sources/10-conceitos-fundamentais-backend]]).
- O vídeo não aprofunda *como* uma equipe decide entre modernizar a borda (manter o núcleo legado) vs. reescrever — fica como lacuna prática frente ao conteúdo mais detalhado de padrões de integração com legado já presente na referência `architecture-specialized.md` da skill `tech-mentor-backend` (Strangler Fig, anti-corruption layer, dual write, ESB/iPaaS) — carregada durante esta ingestão mas não citada diretamente na transcrição.

## Raw Quotes

> "O SOAP ainda está rodando desde 98. Ele está lá, tranquilo. Você também pode ficar por um tempo."

> "A indústria de tecnologia é obcecada com o novo, mas o que realmente sustenta o mundo na maior parte do tempo é o que já está rodando há décadas, sem holofote nenhum."
