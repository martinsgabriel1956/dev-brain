---
type: source
title: "A Insanidade de Ser um Programador Hoje"
aliases: ["insanity of being a software engineer", "insanidade programador", "vitor sousa pereira insanidade"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_count: 0
tags: [carreira, historia-da-computacao, complexidade, especializacao, unix, react, devops, cargo-cult-tecnologico, curva-de-aprendizado]
skill: tech-mentor-leadership
status: stable
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/a-insanidade-de-ser-um-programador-hoje.md"
source_url: "https://0x1.pt/2025/04/06/the-insanity-of-being-a-software-engineer/"
author: "Vitor Sousa Pereira"
date_published: 2025-04-06
date_ingested: 2026-07-27
---

## TL;DR

Vídeo de reação (canal/narrador não identificado no áudio) ao artigo ["The Insanity of Being a Software Engineer"](https://0x1.pt/2025/04/06/the-insanity-of-being-a-software-engineer/) de [[wiki/entities/vitor-sousa-pereira]] (2025-04-06). O artigo é uma lista satírica-mas-séria da escalada de exigências para ser programador hoje — tipagem, gerenciamento de estado, build tooling, Docker, Ansible, Terraform, virar gestor — e o narrador reage concordando, intercalando com história pessoal (aprendeu a mandar e-mail via SMTP em PHP no início dos 2000s) e reflexões sobre como a área mudou estruturalmente: o senso de comunidade herdado do Unix, a distinção front-end/back-end como invenção recente (2006-2007, não "sempre existiu"), o fullstack como corte de custos disfarçado de evolução técnica, e a tese central de que a área ficou **mais complexa e menos especializada ao mesmo tempo** — mais abstração em cima de protocolos que praticamente ninguém aprende mais diretamente (SMTP, POP3, IMAP).

## Key Claims

- **Senso de comunidade como diferencial da área**: o `grep` foi criado por Ken Thompson como comando privado, antes de virar público; o Unix nasceu como subproduto de Thompson tentando rodar melhor seu jogo *Space Travel*, e depois foi absorvido e expandido pela comunidade sem fins lucrativos — o narrador argumenta que esse padrão (compartilhar trabalho sem cobrar, outros construírem em cima) é incomum fora da nossa área. Relacionado a [[wiki/concepts/unix]] (histórico do sistema) e novo candidato a entity [[wiki/entities/ken-thompson]].
- **Sistemas complexos como montagem de peças simples (Lego)**: citação do artigo original comparando construção de software complexo a encaixar sistemas menores — mesmo princípio por trás de composição de bibliotecas open source.
- **A curva de aprendizado da programação é descontínua, com barreiras**: eixo "o que você sabe" vs. "o que você consegue criar" não cresce linear — cada objetivo novo (ex.: enviar um e-mail) esconde uma cadeia de pré-requisitos não óbvios (Apache, diferença entre código no browser e no servidor, e por fim descobrir que e-mail não é HTTP, é SMTP). Nova página dedicada: [[wiki/concepts/curva-de-aprendizado]]. Relacionado a [[wiki/concepts/aprendizado-por-luta]] (a dificuldade em si como parte do processo de retenção).
- **A distinção front-end/back-end NÃO é histórica — é uma invenção de 2006-2007**: antes disso existia "dev desktop" e "dev web" (webmaster), sem separação de especialidade; a separação surgiu quando o front-end ficou mais complexo (o quanto essa complexidade era necessária é debatível, segundo o narrador). Contradiz a percepção comum de que sempre houve duas trilhas de especialização. Ver nota de reforço/nuance em [[wiki/concepts/nexialista]] (tabela "full stack → especialização extrema → conexão de áreas").
- **Fullstack nasceu de corte de custo, não de escolha técnica**: quando a "mente coletiva" decidiu que React era "a forma certa" de fazer front-end, empresas simultaneamente decidiram não contratar dois especialistas separados — daí o engenheiro fullstack, e depois BFF/GraphQL como remendo arquitetural para essa fusão de responsabilidades.
- **"React é a forma certa" como cargo cult da mente coletiva**: o artigo trata a adoção quase religiosa de React/Redux/TypeScript/Webpack como convenção imposta, não escolha técnica sempre justificada — mesmo padrão de adoção-sem-questionamento documentado em [[wiki/concepts/cargo-cult-tecnologico]], mas aqui o gatilho é consenso de mercado/ferramenta, não benchmark de escala de big tech.
- **De sysadmin a DevOps a SRE — responsabilidade de infraestrutura foi empurrada para o engenheiro de aplicação**: o admin de sistemas cuidava disso; "empresas com dificuldades financeiras decidiram que os próprios engenheiros" assumiriam essa carga, e "todo mundo concordou" — mesmo tom cético do narrador sobre pressão de mercado presente em outras fontes de carreira já na wiki (ex.: cargo cult, apagão de sêniors).
- **Virar gestor não é fuga da complexidade, é acúmulo dela**: promoção para gestão soma responsabilidades (estimativa, atribuição de tarefas, revisões, feedback em reuniões de produto) em vez de substituir as técnicas — e, segundo observação do narrador, após os *layoffs* recentes a maioria dos engineering managers voltou a codar, evidência de que a pressão de mercado reverteu a separação código/gestão.
- **Complexidade subiu, especialização caiu**: nível de abstração aumentou (menos gente aprende SMTP/POP3/IMAP para mandar e-mail — a pergunta hoje é "qual API eu uso", ex.: Resend, Vercel) ao mesmo tempo que o número de peças/ferramentas que é preciso encaixar também aumentou — o narrador chama isso de ficar "mais especializado e mais generalista ao mesmo tempo antes", e hoje nem uma coisa nem outra, porque a abstração escondeu o protocolo de baixo nível que antes era conhecimento comum.
- **Analogia com construção civil**: uma casa envolve dezenas de especialistas dedicados (arquiteto, eletricista, encanador etc.) e ninguém espera que uma pessoa só faça tudo — contraste implícito com a expectativa do mercado de tech sobre o engenheiro fullstack "que faz tudo".

## Entities

[[wiki/entities/vitor-sousa-pereira]] · [[wiki/entities/ken-thompson]]

## Concepts

[[wiki/concepts/unix]] · [[wiki/concepts/curva-de-aprendizado]] · [[wiki/concepts/nexialista]] · [[wiki/concepts/cargo-cult-tecnologico]] · [[wiki/concepts/aprendizado-por-luta]]

## Open Questions

- A skill `tech-mentor-leadership` (referenciada em `/home/nemomartins/Documentos/new/skills/tech-mentor-leadership/SKILL.md` conforme as instruções do projeto) **não está acessível neste ambiente/máquina**. Ingest feito por analogia com fontes já calibradas do mesmo domínio ([[wiki/sources/topicos-desenvolvimento-software-mudei-de-ideia-6-anos]], [[wiki/sources/pare-de-terceirizar-suas-decisoes]]). Sinalizado como skill drift para revisão futura.
- **O narrador/canal do vídeo de reação não foi identificado no áudio** — a transcrição não contém autoapresentação nem menção ao nome do canal. O estilo de fala ("cara", "tá ligado", histórico pessoal de ter programado dentro da sala do servidor e aprendido PHP para enviar e-mail no início dos 2000s) sugere um criador de conteúdo técnico brasileiro sênior, mas nenhuma correspondência segura foi encontrada com entidades já registradas na wiki (ex.: [[wiki/entities/fabio-akita]], que tem estilo de fala mais formal em outras fontes já ingeridas). Se o canal for identificado numa fonte futura, atualizar `author`/frontmatter aqui e criar entity dedicada.
- O artigo original (`0x1.pt`) não foi lido integralmente nesta ingestão — apenas os trechos citados/traduzidos pelo narrador no vídeo foram capturados. Uma leitura direta do artigo completo poderia revelar claims adicionais não cobertos na reação.
