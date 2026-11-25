---
type: entity
title: "Augusto Galego"
aliases: ["Augusto Galego", "augustogalego.com"]
date_created: 2026-07-20
date_updated: 2026-11-25
source_count: 27
tags: [pessoa, programador, youtuber, brasil, devops, system-design, carreira, agentes-ia, code-review]
skill: tech-mentor-infra
status: stub
---

# Augusto Galego

Criador de conteúdo técnico em português, autor da demo de [[wiki/concepts/blue-green-deploy|deploy blue/green]] numa VPS com [[wiki/concepts/reverse-proxy|Nginx]]. Site pessoal/marca: `augustogalego.com`.

## Perfil

- Se descreve explicitamente como não sendo especialista em DevOps/infraestrutura ("nunca fui um cara de infra") — a demo é apresentada como reprodutível por qualquer pessoa seguindo tutoriais, não como conteúdo de autoridade técnica profunda em Nginx/systemd.
- Vídeo é continuação de uma aula anterior sobre tipos de deploy, sugerindo conteúdo seriado sobre deploy/infra para devs.
- Usa IA como apoio na criação do repositório de demonstração.

## Colaboração em Projeto de Terceiros

Convidado como editor/colaborador num projeto de outro criador de conteúdo ([[wiki/entities/replit|Replit]], vibe coding de um [[wiki/concepts/simulador-de-system-design|simulador de system design]]) — indício de rede de colaboração ativa entre criadores de conteúdo técnico brasileiros usando ferramentas de agentes de IA em conjunto.

## Conteúdo de Carreira e System Design

Além de conteúdo de infra/deploy, produz conteúdo sobre carreira e entrevistas técnicas — 12 anos de experiência, 5 deles em empresa gringa. Lançou curso pago próprio de System Design (mais de um ano de produção) cobrindo banco de dados, filas, load balancer, API Gateway, autenticação, WAF, rate limiting, Saga, CQRS, DNS, Blob Store, cache e CDN, com reembolso integral em um mês sem perguntas. Argumenta que é impossível definir com precisão universal o que é esperado de um júnior/pleno/sênior, pois nenhuma empresa concorda na própria definição desses níveis — mas ainda assim propõe uma progressão de referência específica para system design. → [[wiki/concepts/niveis-de-senioridade-system-design]]

## Possível Aula Irmã/Anterior sobre CI/CD e Deploy vs. Release (Autoria Inferida)

[[wiki/sources/continuous-integration-delivery-deploy-vs-release]] tem o mesmo padrão de patrocínio (HostGator, VPS, mesma faixa de preço e mesma promoção de Claude Code pré-instalado) e o mesmo estilo de demo prática de deploy — mas sem identificação de autor na transcrição. A fonte de [[wiki/sources/deploy-blue-green-na-pratica-vps-nginx]] é descrita como continuação de "uma aula anterior sobre tipos de deploy"; esta nova fonte, que cobre justamente CI/CD e deploy vs. release em nível mais introdutório, é uma candidata plausível a ser essa aula anterior (ou uma aula irmã da mesma série) — não confirmado, tratado como open question na fonte.

## Possível Conteúdo de Algoritmos/DSA (Autoria Inferida, Evidência Fraca)

[[wiki/sources/resolvendo-3-problemas-classicos-entrevista-coding-dsa]] — vídeo resolvendo três problemas clássicos de entrevista de coding, sem identificação de autor/canal na transcrição. O único indício de autoria é o cupom de patrocínio "Augusto 20" oferecido por um serviço de câmbio/remessas internacionais, repetido várias vezes no bloco publicitário — nome coincidente com esta entidade, mas evidência mais fraca que as inferências anteriores registradas nesta página (que se apoiavam em padrões de patrocínio idênticos, como HostGator, e citações diretas de produtos próprios, como "Mapa do Arquiteto" — aqui não há nenhum desses sinais, apenas o nome no cupom). Se confirmada, seria o primeiro conteúdo de algoritmos/estruturas de dados puro atribuído a este autor, distinto do conteúdo prévio de infraestrutura/deploy e carreira/system design. Tratado como open question na própria fonte.

## Possível Conteúdo de Infraestrutura como Código / AWS CDK (Autoria Inferida, Evidência de Conteúdo)

[[wiki/sources/infraestrutura-como-codigo-cdk-aws]] — vídeo sobre Infrastructure as Code com demo em AWS CDK, sem identificação de autor/canal no áudio. O indício de autoria aqui não é padrão de patrocínio (o sponsor deste vídeo, AmaX/infraestrutura de pagamentos, é diferente dos já associados a esta entidade), mas sim conteúdo: o fechamento do vídeo cita um curso pago próprio de System Design "o mais extenso já produzido" cobrindo exatamente API Gateway, Lambda, network e banco de dados — sobreposição quase total com a descrição do curso já documentada nesta entidade ("banco de dados, filas, load balancer, API Gateway, autenticação, WAF..."), com a mesma política de reembolso integral em um mês sem nenhum tipo de questionamento. Evidência de conteúdo mais forte que a inferência de [[wiki/sources/resolvendo-3-problemas-classicos-entrevista-coding-dsa]] (que se apoiava só num nome de cupom), mas mais fraca que as inferências apoiadas em padrão de patrocínio idêntico — tratada como open question na própria fonte.

## Conteúdo sobre Agentes de IA e Qualidade de Código

Além de infra/deploy, carreira e system design, produz conteúdo de reação/análise sobre a era agêntica. Em [[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]] reage ao tweet de [[wiki/entities/uncle-bob]] ("não reviso mais código de agentes") e propõe uma [[wiki/concepts/matriz-risco-dificuldade-review-ia|matriz risco × dificuldade]] para migrar gradualmente de revisão manual para merge automático. Relato pessoal relevante: trabalhou nos últimos meses numa **empresa de pagamentos** onde revisavam 100% do código do core business ("quem tem alguma coisa tem medo"), porque o valor entregue era robustez, não volume de features — usa esse caso como o extremo de alto risco que ainda justifica revisão manual total.

## Reação a Tweet sobre LeetCode/System Design vs. Trabalho Real

Em [[wiki/sources/leetcode-system-design-entrevista-versus-trabalho-real-na-era-da-ia]], reage a um tweet de [[wiki/entities/bero]] argumentando que, na era da IA, vale mais parecer bom dev (treinar LeetCode + System Design para entrevista) do que ser bom dev de fato. Concorda em parte: LeetCode caiu de valor prático, System Design subiu — inversão explícita do que ele mesmo defendia "dois anos atrás" no canal. Autorreferência direta pelo próprio nome em terceira pessoa na fala ("você pode argumentar Galego mas...") — a evidência de autoria mais forte já registrada nesta entidade, mais forte até que o padrão de patrocínio HostGator recorrente.

## Conteúdo Introdutório de Segurança: Armazenamento de Senhas

Além de infra/deploy, carreira/system design e reação a agentes de IA, produz conteúdo introdutório de segurança com disclaimer explícito de não-especialista ("não sou um expert em criptografia... cybersegurança... autenticação"). Em [[wiki/sources/armazenamento-seguro-de-senhas-hash-salt-pepper-galego]] explica hash/salt/pepper organizando a defesa em torno de dois modelos de ameaça — ataque online (rate limit + MFA) vs. ataque offline (hash + salt + pepper) — e fecha com uma escada de recomendação prática terminando em identity providers (Clerk, Auth0, Cognito) e passwordless (Magic Link, login social), incluindo preferência pessoal por não lidar com senha em SaaS B2C.

## Segunda Aula de Segurança: SQL Injection

Continuando a linha de conteúdo introdutório de segurança iniciada com hash/salt/pepper, em [[wiki/sources/sql-injection-guia-completo-solucoes-galego]] explica SQL Injection do zero e organiza a defesa em sete camadas concêntricas (query parametrizada, prepared statement, menor privilégio no banco, solução nativa do backend, ORM/query builder, validação de input, WAF), fechando com a mesma disciplina prática de "corrija primeiro a nível de código" e o mesmo padrão de patrocínio ("cupom Galego") que confirma autoria.

## Reação a "No Robots in the Gym" (Autoria Inferida)

Em [[wiki/sources/no-robots-in-the-gym-ia-tarefas-de-academia-ler-e-escrever]], reage ao artigo de [[wiki/entities/daniel-miessler]] e recomenda ler e escrever como [[wiki/concepts/tarefa-de-academia-vs-trabalho|tarefas de academia]]. Autoria inferida por HostGator (VPS, n8n, OpenClaw), catálogo de cursos (LeetCode, roadmap de emprego, System Design "o mais extenso") e viagem ao Reino Unido (Glasgow/Sheffield); o nome não aparece.

## Curso de carreira: módulo Mapeando Vagas (autoria inferida)

[[wiki/sources/introducao-mapeando-vagas]] é a abertura de um módulo de curso sobre onde achar vagas (buscadores, outsourcing, Big Techs), mapear requisitos, acompanhar candidaturas e faixas salariais por país e tipo de empresa, com aula bônus de um "professor Matheus". Autoria inferida pela pasta de transcrições "galego" e pelo catálogo de cursos de carreira; o nome não é dito.

Aulas curtas do mesmo curso pago de carreira (pasta "galego" das transcrições: Introdução - Mapeando Vagas, Onde encontrar vagas?, Buscadores e Outsourcing, Big Techs, Quais países podem fazer sentido?), com um PDF de job boards e outsourcings. Em [[wiki/sources/buscadores-e-outsourcing-galego]] prioriza [[wiki/entities/linkedin]] e, entre as [[wiki/concepts/empresa-de-outsourcing-remoto|outsourcings]], [[wiki/entities/bairesdev]] (volume) e [[wiki/entities/x-team]] (qualidade). Provavelmente o "curso de carreira" / "roadmap de emprego" já citado nesta página; o nome não é dito.

## Conteúdo sobre Candidatura a Vagas Internacionais

Vídeo de carreira sobre sete erros comuns de devs brasileiros ao aplicar para empresas de fora ([[wiki/sources/erros-dev-brasileiro-aplicar-vaga-gringa-augusto-galego]]). Declara ~6 anos de trabalho no Brasil e ~5 para empresas estrangeiras, além de já ter contratado brasileiros para a gringa; menciona canal e cursos de LeetCode/System Design e um curso de carreira (viés comercial possível). Autoria inferida por autorreferência ('Galego Solutions') e pelo tema.
- [[wiki/sources/erros-dev-brasileiro-aplicar-vaga-gringa-augusto-galego]] — lista de erros ao aplicar para vagas na gringa (inglês, storytelling, LeetCode/System Design, pesquisa da empresa); autoria por autorreferência 'Galego'

- [[wiki/sources/contribuidor-de-alto-impacto-high-agency-founder-mode-galego]] — vídeo sobre [[wiki/concepts/contribuidor-de-alto-impacto]] (autoria inferida)

## Aula "Quais países podem fazer sentido?" (módulo Mapeando Vagas)

Aula de um curso de busca de vagas. Avalia países por salário, língua e facilidade de contratação ([[wiki/concepts/criterios-para-escolher-pais-de-vaga]]) e coloca os EUA em primeiro lugar para quem fica no Brasil. Relatos pessoais: morava na Alemanha na gravação; antes trabalhou para uma empresa espanhola e depois para uma de Berlim morando na Itália ([[wiki/concepts/arbitragem-geografica-de-salario]]); já trabalhou para uma empresa australiana que pagava em USD; participou de processos para os Emirados (via outsourcing) e Bangkok. Autoria inferida pela pasta de origem "galego" e pela coerência com relatos anteriores; o nome não é dito.

- [[wiki/sources/quais-paises-podem-fazer-sentido-vagas-internacionais-galego]] — critérios por país, "remote" com restrição de residência, visa sponsorship, Portugal/Bálticos como porta de entrada (autoria inferida)

## Workshop Roadmap pro seu próximo emprego: onde encontrar vagas

Aula e PDF do workshop pago de carreira ([[wiki/sources/onde-encontrar-vagas-workshop-roadmap-emprego-galego]], [[wiki/sources/onde-procurar-vagas-guia-definitivo]]). Organiza a busca em [[wiki/concepts/tres-canais-de-vaga-internacional|três canais]] e recomenda [[wiki/concepts/outsourcing-como-porta-de-entrada-internacional|outsourcing]] para o primeiro emprego fora, que foi o caminho dele. Diz estar morando na Alemanha na gravação (abril de 2025). Autoria inferida pela pasta da transcrição e pelo nome do workshop, que já constava no catálogo de cursos dele.

## Módulo "Mapeando Vagas": aula sobre Big Techs

Na aula sobre Big Techs do curso de busca de vagas ([[wiki/concepts/big-tech]]), pesquisa salário no [[wiki/entities/levels-fyi]] e no [[wiki/entities/glassdoor]], filtra vagas na página de carreiras do Google e resume o [[wiki/concepts/processo-de-entrevista-big-tech]]. Relato pessoal: aplicou para ~10 vagas na Amazon, 9 rejeitaram o currículo e 1 time o chamou, mas ele não passou da segunda etapa ([[wiki/concepts/contratacao-por-time-em-big-tech]]). Autoria inferida pela pasta das transcrições e pelo módulo; o nome não é dito.

## Módulo "Mapeando Vagas": mapear requisitos de múltiplas vagas

Em [[wiki/sources/mapear-requisitos-de-multiplas-vagas-galego]] mostra um template no Notion ("eu uso o Notion pra tudo") para contar os requisitos de 10 a 15 vagas ([[wiki/concepts/mapeamento-de-requisitos-de-vagas]]). A demo usa vagas de [[wiki/entities/nubank]], Brex e [[wiki/entities/itau]]; diz ter "viés" pró-fintech ("eu acho que fintech vale muito a pena"), coerente com o relato da empresa de pagamentos. Autoria inferida pela pasta das transcrições; o nome não é dito.

## Aula sobre networking com criação de conteúdo

Em [[wiki/sources/networking-com-criacao-de-conteudo-galego]] diz que hoje é CTO e criador de conteúdo, e que só começou a publicar em 2024, já sênior, morando na Europa e com passagem por empresas dos EUA e da Austrália; antes, "você não vai encontrar quase nada que eu fiz na internet". O primeiro tema foi LeetCode. Defende que conteúdo é opcional e que o ganho inicial é network e visibilidade ([[wiki/concepts/criacao-de-conteudo-tecnico]]). Autoria inferida pela pasta e pelo relato; o nome não é dito.

## Módulo "Mapeando Vagas": acompanhando as applications

Em [[wiki/sources/acompanhando-as-applications-galego]] diz que já aplicou em volume, sem ler requisitos, e que "já funcionou"; para um núcleo de 20 a 30 empresas recomenda aplicação customizada, 2 ou 3 contatos por empresa e follow-up, num board do Notion ([[wiki/concepts/acompanhamento-de-candidaturas]]). Autoria inferida pela pasta; o nome não é dito.

## Módulo "Mapeando Vagas": aula bônus sobre salários invisíveis

Em [[wiki/sources/aula-bonus-artigo-salarios-invisiveis-galego]] comenta o artigo trimodal de [[wiki/entities/gergely-orosz]] e o traduz para o Brasil (agência local × Banrisul × Nubank/Brex). Diz que o modelo é "uma verdade quase que auto-evidente" e que vale no Brasil "tranquilamente". É a aula de faixas salariais "invisíveis" anunciada na introdução do módulo ([[wiki/concepts/modelo-trimodal-compensacao]]). Autoria inferida; o nome não é dito.

## Key Sources

- [[wiki/sources/deploy-blue-green-na-pratica-vps-nginx]]
- [[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]] — reação a Uncle Bob/Boris/Lucas Montano; matriz risco × dificuldade; relato da empresa de pagamentos revisando 100% do core business
- [[wiki/sources/infraestrutura-como-codigo-cdk-aws]] — autoria inferida por sobreposição de conteúdo do curso pago de System Design (API Gateway, Lambda, banco de dados) e política de reembolso idêntica, não confirmada por nome nem padrão de patrocínio
- [[wiki/sources/continuous-integration-delivery-deploy-vs-release]] — autoria inferida, não confirmada por nome no vídeo
- [[wiki/sources/system-design-simulador-hotel-booking-replit]] — convidado como colaborador/editor no projeto do simulador de system design
- [[wiki/sources/system-design-por-nivel-junior-pleno-senior]] — progressão de expectativas de system design por nível de senioridade (júnior/pleno/sênior), entrevista vs. trabalho real
- [[wiki/sources/anatomia-entrevista-system-design-bigtech]] — autoria inferida (não confirmada por nome no vídeo, ver open question na fonte): mesmo curso pago, mesma política de reembolso, mesmo bloco patrocinado UVP removido no início; detalha o pipeline de entrevista bigtech e o que cada etapa da sessão de system design avalia
- [[wiki/sources/resolvendo-3-problemas-classicos-entrevista-coding-dsa]] — autoria inferida com evidência fraca (nome no cupom de patrocínio "Augusto 20"), não confirmada; três problemas de algoritmos/estruturas de dados resolvidos ao vivo
- [[wiki/sources/escalar-para-um-milhao-de-usuarios]] — autoria inferida (mesmo curso pago de 90+ aulas, mesma política de reembolso de um mês): aula gratuita do curso reconstruindo o capítulo "de zero a milhões de usuários" de Alex Xu, desenho incremental guiado por SPOF
- [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]] — autoria confirmada (PWD do vídeo identifica o user "Augusto Galego"): comandos básicos de Linux e por que devs precisam reconhecê-los na era dos agentes; patrocínio Abacus
- [[wiki/sources/leetcode-system-design-entrevista-versus-trabalho-real-na-era-da-ia]] — autoria confirmada por autorreferência direta ao próprio nome na fala; reação a tweet sobre LeetCode/System Design como filtro de entrevista vs. diferencial real de trabalho
- [[wiki/sources/armazenamento-seguro-de-senhas-hash-salt-pepper-galego]] — autoria confirmada por autorreferência ("cupom galego"); introdução a hash/salt/pepper organizada por modelo de ameaça (online vs. offline), com escada de recomendação até identity providers e passwordless
- [[wiki/sources/sql-injection-guia-completo-solucoes-galego]] — autoria confirmada por "cupom Galego"; SQL Injection explicado do zero com sete camadas de defesa concêntricas, do banco (query parametrizada, prepared statement) à borda (WAF)
- [[wiki/sources/big-techs-salarios-vagas-processo-de-aplicacao]] — aula Big Techs (Mapeando Vagas): Levels.fyi, vesting, contratação por time, processo de entrevista; autoria inferida
- [[wiki/sources/estado-global-stateless-side-effects-reprodutibilidade-galego]] — vídeo sobre estado global/stateless/side effects/reprodutibilidade; divulga o curso de System Design e um patrocinador de cadeira ergonômica.
- [[wiki/sources/no-robots-in-the-gym-ia-tarefas-de-academia-ler-e-escrever]] — no robots in the gym; vibe ler; ler e escrever (autoria inferida)
- [[wiki/sources/introducao-mapeando-vagas]] — abertura do módulo Mapeando Vagas (autoria inferida pela pasta)
- [[wiki/sources/buscadores-e-outsourcing-galego]] — onde procurar vaga primeiro (job boards e outsourcing)
- [[wiki/sources/onde-encontrar-vagas-workshop-roadmap-emprego-galego]] — três canais, Total Compensation, outsourcing PJ (autoria inferida)
- [[wiki/sources/onde-procurar-vagas-guia-definitivo]] — PDF com links e manual de busca booleana (autoria inferida)
- [[wiki/sources/mapear-requisitos-de-multiplas-vagas-galego]] — tabela de requisitos (categoria, prioridade, contagem, proficiência); autoria inferida
- [[wiki/sources/networking-com-criacao-de-conteudo-galego]] — conteúdo é opcional; começou em 2024 com LeetCode; post na íntegra (autoria inferida)
- [[wiki/sources/acompanhando-as-applications-galego]] — board de candidaturas, aplicação em volume × seletiva (autoria inferida)
- [[wiki/sources/aula-bonus-artigo-salarios-invisiveis-galego]] — leitura comentada do modelo trimodal, com exemplos brasileiros (autoria inferida)
