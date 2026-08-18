---
type: source
title: "A História e Evolução das APIs"
aliases: ["história das APIs", "evolução das APIs", "de onde vêm as APIs"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 0
tags: [tech-mentor-backend, api, historia, soap, rest, graphql, grpc, corba, posix, winapi, api-economy]
skill: tech-mentor-backend
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/historia-e-evolucao-das-apis-bernardo-lobato.md
source_url:
author: Bernardo Lobato
date_published:
date_ingested: 2026-08-18
---

# A História e Evolução das APIs

## TL;DR

Primeira parte de uma série de [[wiki/entities/bernardo-lobato]] sobre APIs — percurso histórico década a década, do sentido original do termo (biblioteca/rotina local do sistema operacional, sem rede) até a "infraestrutura crítica" de hoje. Tese central: API não nasceu como "dois sistemas conversando pela internet" — esse é só o estágio mais recente de uma ideia que começou nos anos 60 como abstração de hardware dentro de um único mainframe, e foi ganhando camadas (interoperabilidade → rede → web → economia → governança) conforme a computação mudou de escala.

## Key Claims

1. **API = "Application Program Interface"**, um conjunto de regras/contratos que permite módulos conversarem — a palavra "módulo" não implica rede nem outra aplicação; é o sentido mais amplo e mais antigo do termo, anterior ao uso moderno de "API como integração entre sistemas via HTTP".
2. **Anos 60-70: APIs eram locais, sem rede** — coleções de rotinas/bibliotecas do sistema operacional (ex.: função para acessar disco em vez de escrever o driver na mão). [[wiki/entities/ibm]] com o System/360 forneceu essas interfaces para rodar múltiplas linguagens/aplicações no mesmo mainframe — reutilização de código e menor acoplamento a hardware específico, sem internet.
3. **Anos 70: o Unix consolidou "chamada de sistema" como API padronizada entre programa e kernel** — filosofia de pequenas funções reutilizáveis e combináveis. Fonte credita essa filosofia como influência direta em modelos posteriores, citando explicitamente REST+JSON como herdeiro dessa ideia (elo que a wiki não tinha registrado antes — ver [[wiki/concepts/unix]]).
4. **Anos 80: WinAPI (Microsoft) e POSIX (Unix) tornaram a API acessível ao PC pessoal** — WinAPI padronizou janelas/botões/menus/gráficos/entrada de usuário para quem desenvolvia para Windows (exemplo: jogos como Prince of Persia tinham que implementar vídeo/som/teclado na mão antes da API existir); POSIX (fim dos 80) unificou chamadas de sistema entre diferentes Unix, dando portabilidade a código C entre eles.
5. **Anos 90: CORBA e RMI foram a primeira geração de APIs remotas**, coincidindo com o nascimento da web — descritos como "complexos", mas abrindo caminho pra integração em rede.
6. **Anos 2000: SOAP (XML+HTTP, contrato formal via WSDL) e REST (tese de doutorado, ganha tração só depois com o JSON) nascem na mesma década** — SOAP como padronização pesada mas robusta para bancos/seguradoras (aprofundado em [[wiki/sources/tecnologias-hype-passado-soap-xml-esb-jquery-cobol]]); REST inicialmente acadêmico, sem tração real até o JSON virar formato dominante.
7. **Anos 2000: nasce a "economia das APIs"** — eBay, Amazon e Salesforce foram pioneiras em expor API pública, seguidas por Google, Facebook e Twitter; API deixa de ser ferramenta interna e vira estratégia de negócio.
8. **Anos 2010: REST+JSON vira padrão de mercado por causa do boom mobile**; GraphQL (Facebook/Meta, permite ao cliente pedir exatamente os dados que precisa, resolvendo over-fetching em telas complexas como feed de rede social) e gRPC (Google, 2015, Protobuf binário, alta performance, pensado para comunicação interna entre microsserviços) surgem como respostas a necessidades diferentes da mesma década — não competem diretamente, atacam problemas diferentes (cliente-servidor complexo vs. serviço-a-serviço de alta performance).
9. **Anos 2010: API vira produto em si** — Stripe, Twilio e SendGrid citadas como empresas que se tornaram bilionárias vendendo API como produto; AWS/GCP/Azure expandem oferecendo centenas de APIs de infraestrutura.
10. **Anos 2020: API vira infraestrutura crítica, não só técnica** — APIs de IA generativa (ex.: OpenAI) para integrar LLMs/visão; crescimento de APIs event-driven e tempo real (WebSocket, webhook) em fintechs e streaming; consolidação de padrões de segurança/governança (OAuth, OpenID Connect, API Gateway) como resposta ao uso massivo. Fonte fecha com a afirmação forte de que sem API a internet moderna (Pix, chatbots, IA) "simplesmente deixa de existir".

## Entidades Mencionadas

- [[wiki/entities/ibm]] — IBM System/360, pioneira em API de mainframe (anos 60-70)
- [[wiki/entities/microsoft]] — criadora da WinAPI (anos 80)
- [[wiki/entities/google]] — criador do gRPC (2015) e provedor de API economy via Google Cloud
- [[wiki/entities/meta]] — criadora do GraphQL (então Facebook, anos 2010)
- [[wiki/entities/openai]] — citada como referência de API de IA generativa nos anos 2020
- [[wiki/entities/amazon-web-services]] — AWS como expansão de API economy nos anos 2010; Amazon (pré-AWS) como uma das pioneiras de API pública nos anos 2000
- eBay, Salesforce, Twitter, Stripe, Twilio, SendGrid — citadas como marcos de "API economy"/"API como produto", sem página própria na wiki ainda (não centrais o suficiente ao conteúdo da fonte para justificar stub isolado)

## Conceitos Tocados

- [[wiki/concepts/contrato-de-api]]
- [[wiki/concepts/unix]]
- [[wiki/concepts/soap]]
- [[wiki/concepts/api-gateway]]
- [[wiki/concepts/grpc]]
- [[wiki/concepts/graphql]]
- [[wiki/concepts/oauth2]]
- [[wiki/concepts/openid-connect]]
- [[wiki/concepts/mainframe]]
- [[wiki/concepts/windows-api]]
- [[wiki/concepts/posix]]
- [[wiki/concepts/corba-rmi]]
- [[wiki/concepts/api-economy]]
- [[wiki/concepts/microsservicos]]

## Open Questions

- Vídeo não cita fontes primárias (papers, datas exatas, links) para nenhuma das afirmações históricas — mesmo padrão didático sem rigor acadêmico já observado em outras fontes deste autor (ver [[wiki/sources/tecnologias-hype-passado-soap-xml-esb-jquery-cobol]]) e de outros canais (ver [[wiki/sources/10-conceitos-fundamentais-backend]]).
- A tese de que REST+JSON "herda a filosofia do Unix" (pequenas funções combináveis) é uma afirmação de linhagem conceitual, não uma citação histórica direta (REST nasceu de uma tese de doutorado sobre arquitetura web, não de uma ligação documentada ao design do Unix) — registrado aqui como leitura do autor, não como fato verificado.
- A tese de doutorado do REST não é nomeada nem datada com precisão (é a tese de Roy Fielding, ano 2000 — fato de conhecimento geral, não citado explicitamente na fala) — fonte trata isso de forma vaga ("apresentada pela primeira vez em uma tese de doutorado").
- Não há menção a HTTP/1.1, HTTP/2 ou aos protocolos de transporte subjacentes às APIs remotas — a história é contada do lado do formato/contrato (SOAP, REST, GraphQL, gRPC), não do lado do transporte.

## Raw Quotes

> "API significa Application Program Interface, e é um conjunto de regras e contratos que permitem que módulos conversem entre si — destaque aqui pra palavra módulo, que não quer dizer necessariamente que seja uma outra aplicação ou uma aplicação disponibilizada via rede."

> "Nos anos 60 e 70 as APIs eram locais e voltadas para o próprio computador, ainda não existia internet, mas a essência já tava lá: fornecer uma camada de abstração que facilitasse a vida do desenvolvedor."

> "Muitas das ideias presentes nesse modelo do Unix foram reaproveitadas posteriormente em modelos como o REST com JSON, por exemplo."

> "Os anos 2000 marcaram uma transição entre as APIs locais e corporativas para APIs abertas e baseadas na web — foi quando a API deixou de ser apenas uma ferramenta interna de desenvolvimento e passou a ser uma estratégia de negócios."

> "Nos anos 20 as APIs deixaram de ser meramente um meio técnico para ajudar desenvolvedores e viraram infraestrutura crítica no mundo digital — sem elas a internet moderna simplesmente deixa de existir."
