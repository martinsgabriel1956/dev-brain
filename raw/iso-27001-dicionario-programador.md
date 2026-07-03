# ISO 27001 — Dicionário do Programador

> Transcrição de vídeo/podcast, formato "Dicionário do Programador".
> Apresentadores: Gabriel e Vanessa Weber.
> Tema: ISO/IEC 27001 — o padrão internacional de gestão de segurança da informação, e sua relação com o dia a dia de desenvolvimento de software.

---

## Contextualização

A ISO 27001 é o padrão internacional mais rigoroso e reconhecido para a gestão de segurança da informação. Ela define as diretrizes exatas de como uma organização deve proteger seus dados, sistemas e infraestrutura contra acessos não autorizados, vazamentos e ataques cibernéticos.

Não é apenas sobre ter um antivírus ou um firewall robusto. A norma exige a criação de um **Sistema de Gestão de Segurança da Informação** (o famoso **SGSI**), que funciona como um ecossistema para garantir três pilares fundamentais: a confidencialidade, a integridade e a disponibilidade da informação.

Este é o episódio do Dicionário do Programador sobre ISO 27001 — por que conhecer essa norma é vital para a carreira de um dev, o que ela tem a ver com o código do dia a dia, e como automatizar essas regras de compliance direto na esteira de deploy.

---

## O que é a ISO, de fato

Se você pensa em ISO, provavelmente lembra dos adesivos desbotados na traseira de caminhões escrito "ISO 9001", ou dos arquivos `.iso` que baixávamos para instalar Windows e Linux nos anos 2000.

Mas a ISO — *International Organization for Standardization* — é muito mais do que isso. Está sediada em Genebra e é uma organização não governamental que define padrões para praticamente tudo: da rosca do parafuso que segura uma cadeira até o formato do cartão de crédito.

Neste episódio o foco é tecnologia, na família **27.000** da ISO. A **ISO/IEC 27001** define os requisitos para um SGSI. A "IEC" é a *International Electrotechnical Commission*, parceira da ISO nessa jornada.

O SGSI não é um software que se compra e instala no servidor. É um **framework de gestão**: um conjunto sistêmico de políticas, procedimentos, processos e tecnologia, desenhado para gerenciar riscos.

---

## A tríade CIA

Tudo gira em torno da chamada tríade **CIA** — e não, não é a CIA que você está pensando. Aqui, CIA significa **Confidentiality, Integrity e Availability**.

- **Confidencialidade** — o famoso "só entra quem pode". Garante, por exemplo, que um funcionário qualquer não tenha acesso de leitura à tabela de salários no banco de dados. Sem credencial, chave SSH ou token JWT válido, é *access denied*.
- **Integridade** — garante que o dado gravado é o mesmo que será lido. Não pode haver update malicioso no banco de dados nem ataque *man-in-the-middle* alterando o pacote JSON no meio da requisição. Aqui entram hashes, assinaturas digitais e commits Git assinados.
- **Disponibilidade** — o servidor precisa estar ativo, disponível e preparado para suportar picos de acesso. Envolve redundância, backup testado e proteção contra DDoS. Afinal, se o sistema é seguro mas ninguém consegue acessá-lo, ele é inútil.

A ISO 27001 é, basicamente, um manual de instruções auditável para garantir que esses três pilares se mantenham firmes mesmo quando o mundo digital está "pegando fogo" lá fora.

---

## Origem histórica

A padronização da gestão de segurança tem origem britânica:

- **1995** — publicação da **BS 7799** pelo BSI Group, no Reino Unido. Dividida em duas partes: a Parte 1 era um código de boas práticas; a Parte 2, publicada em 1998, era a especificação de requisitos.
- **2000** — a ISO adota a Parte 1 como a **ISO/IEC 17799**.
- **2005** — nasce formalmente a ISO/IEC 27001.
- **2013** — nova versão, que reinou por 9 anos. Nessa época o Docker estava nascendo, o Kubernetes nem existia e a nuvem não era o que é hoje — a norma precisava de uma atualização urgente.
- **2022** — versão atual, alinhada à realidade digital moderna. Trouxe conceitos como inteligência de ameaças, segurança em nuvem e continuidade de negócios focada em TIC. Também simplificou a estrutura: reduziu o número de controles do Anexo A de **114 para 93**, reorganizando os antigos 14 domínios em apenas **4 temas lógicos**.

Hoje, ter a certificação não é sobre "um selo na parede". Grandes players como AWS, Google, Microsoft e, no Brasil, Nubank e Mercado Livre, dependem dela para operar.

---

## Estrutura da norma

A norma é dividida em duas grandes seções.

### Cláusulas obrigatórias (requisitos do sistema de gestão)

As cláusulas 0 a 3 tratam de introdução, escopo e definições, e ficam fora do escopo prático. As relevantes são:

| Cláusula | Tema | Conteúdo |
|---|---|---|
| 4 | Contexto da organização | Define o escopo do SGSI — os limites do sistema e a aplicabilidade dos controles |
| 5 | Liderança | A alta direção deve documentar uma política envolvendo colaboradores e clientes |
| 6 | Planejamento | Estabelecer, medir e monitorar objetivos com base em riscos e oportunidades |
| 7 | Suporte | Competências, conscientização, comunicação e informação documentada (incluindo registros a manter) |
| 8 | Operação | Plano de tratamento de riscos e relatório de avaliação de riscos |
| 9 | Avaliação de desempenho | Monitoramento, medição, auditorias internas e análises críticas pela gestão |
| 10 | Melhoria | Ações sobre os resultados das avaliações da cláusula 9 |

### Anexo A — os controles

É aqui que devs mais interagem. Pense num restaurante self-service de segurança: a norma oferece **93 pratos** (controles). Você não precisa "comer" todos — isso daria indigestão — mas precisa justificar o que não vai usar.

Esse "prato feito" é a **SoA** — *Statement of Applicability* (Declaração de Aplicabilidade): um documento onde a empresa diz "desses 93 controles, aplicamos estes X porque fazem sentido para o nosso risco; os demais não se aplicam" (por exemplo, um controle de segurança física para escritório não se aplica a uma empresa 100% remota).

Na versão 2022, os controles do Anexo A foram organizados em 4 temas:

- **Organizacional** — 37 controles (governança, política, gestão de fornecedores, inteligência de ameaças)
- **Pessoas** — 8 controles (treinamento, onboarding, offboarding, trabalho remoto — o elo mais fraco costuma estar "entre a cadeira e o teclado")
- **Físico** — 14 controles (câmeras, crachás, proteção contra incêndio, mesa limpa)
- **Tecnológico** — 34 controles (criptografia, autenticação, logs, codificação segura) — os que impactam diretamente o trabalho de quem desenvolve software

---

## Os controles que mais impactam quem escreve código

### A.8.28 — Codificação segura

A norma diz explicitamente: *"princípios de codificação segura devem ser aplicados no desenvolvimento de software"*. Na prática:

- Não adianta ter código performático com uma falha de SQL injection — siga padrões como o OWASP Top 10 ou o CWE Top 25.
- **Input validation**: nunca confie no input do usuário. Valide tudo que vem de formulários, API e uploads.
- Cheque se as bibliotecas de terceiros (aquele `npm install`) não têm vulnerabilidades conhecidas.

### A.5.15 — Controle de acesso

O famoso "quem é você e o que você quer":

- **Least privilege** (privilégio mínimo) — se o microsserviço só precisa ler dados, ele não ganha permissão de escrita.
- **RBAC** (*role-based access control*) — acesso baseado na função, não na pessoa. O João não tem acesso ao banco; o grupo `db-admins` tem, e o João entra nesse grupo.
- Vale também para tokens de API e JWT com *scopes* bem definidos — nada de `admin: true` para todo mundo no payload.

### A.5.8 — Segurança da informação na gestão de projetos

Segurança não entra como camada posterior ao desenvolvimento — deve estar integrada em todo o processo (**security by design**). No planning, na concepção da feature, sempre alguém deve perguntar: "isso abre brecha de segurança? é preciso definir requisitos de segurança antes de codar?"

### A.8.25 — Ciclo de vida de desenvolvimento seguro

Aqui entra o CI/CD na prática: devem existir testes de segurança (SAST e DAST) rodando na pipeline, além de ambientes separados de desenvolvimento, staging e produção — dados de produção não podem vazar para teste.

### A.5.3 — Segregação de funções

Controle polêmico: a pessoa que desenvolve o código não deve ser a mesma que tem permissão para fazer deploy em produção sozinha. A ideia é evitar fraudes e erros operacionais. O pull request com aprovação de outro dev é a implementação técnica desse controle — mas em empresas e equipes pequenas, mantê-lo à risca é difícil, às vezes quase impossível.

---

## Compliance as Code / Policy as Code

A tendência de mercado é não depender da boa vontade humana de "ler a política", mas criar travas diretamente no código que impedem o erro.

Exemplo com **Open Policy Agent (OPA)** — motor de decisão de propósito geral que desacopla a decisão da aplicação, com regras declarativas escritas em Rego:

- **Infraestrutura como código**: se a política da empresa (baseada na ISO) diz que nenhum bucket S3 pode ser público, e um dev sobe um Terraform criando um bucket público, a pipeline quebra. O auditor não precisa entrar na AWS para verificar — basta olhar o código da política e o relatório da pipeline.
- **Containers**: a norma pode exigir que containers nunca rodem como `root` nem com a flag `--privileged`. Com **Gatekeeper** (o OPA nativo para Kubernetes), é possível inspecionar o objeto de admissão do container, verificar se `securityContext.privileged` é `true` e, se for, bloquear o processo com um aviso de restrição.

Isso também atende aos controles A.8.4 (acesso ao código-fonte) e A.5.15 (controle de acesso), já que se está controlando quem pode fazer o quê e como os recursos são configurados via código.

---

## Adoção no Brasil e casos reais

O Brasil está entre os **top 10 países** com mais certificações, ao lado de gigantes como China, Japão e Reino Unido — mais de 96.000 certificados válidos considerando várias normas, com destaque crescente para TI.

Segundo o *ISO Survey 2024*, empresas certificadas fecham contratos enterprise **40% mais rápido**.

- **Nubank** — possui a certificação ISO 27001, garantindo a investidores e reguladores que os dados de mais de 100 milhões de clientes estão protegidos. O recurso "modo rua" do Nubank é uma aplicação prática dos conceitos da norma: fora de uma rede Wi-Fi segura, o app limita transações — controle de acesso contextual, alinhado aos controles de segurança móvel e acesso lógico.
- **Mercado Livre** — opera pagamentos (Mercado Pago), logística e varejo, com superfície de ataque imensa. Combina ISO 27001 e PCI-DSS (padrão de segurança para cartões de crédito). No relatório anual de 2024, destacou a recertificação ISO 27001 como pilar de confiança do ecossistema, e aplica o conceito de **Zero Trust** — nada é confiável por padrão, tudo deve ser verificado — alinhado aos controles da versão 2022.
- **SciELO Brasil** — anunciou certificação ISO 27001 em 2025, vital para a preservação do conhecimento científico: garante integridade dos dados de pesquisa e disponibilidade dos artigos.

---

## ISO 27001 e Inteligência Artificial

A ISO 27001 foca em segurança da informação, mas o boom da IA generativa criou uma lacuna: ela não cobre, por exemplo, um LLM "alucinando" dados confidenciais de uma empresa.

Para isso, a ISO lançou a **ISO/IEC 42001**, no final de 2023 — focada em **IA responsável**: ética, viés algorítmico, transparência e *accountability*.

A 42001 foi desenhada para se plugar à 27001 como um módulo de expansão. Ambas usam o **Anexo SL**, uma estrutura padrão criada para unificar a forma como diferentes normas de sistema de gestão são organizadas. Empresas que já têm a 27001 conseguem implementar a 42001 até **40% mais rápido**.

O futuro da governança tech aponta para a união de três normas:

- **ISO 27001** — protege os dados
- **ISO 27701** — protege a privacidade (LGPD/GDPR)
- **ISO 42001** — garante a governança de IA

---

## Relação com a LGPD

A ISO 27001 funciona como um "como fazer" técnico para atender às exigências legais da LGPD. O controle **A.5.34** — privacidade e proteção de informações pessoais identificáveis — é um link direto com a lei brasileira.

---

## Conclusão

A certificação pode parecer burocrática, mas implementar controles de segurança, revisar acessos, segregar funções e automatizar políticas via código é, na prática, o caminho para software seguro e de qualidade de verdade.

---

## Nota de produção (fora do conteúdo técnico)

O vídeo inclui um patrocínio para os VPS da Hostinger (custo-benefício, cupom "código fonte", instalação com um clique de aplicações como n8n, OpenWebUI/Chatwoot, e gerenciamento de containers Docker). Trecho comercial, sem relação com o conteúdo técnico da ISO 27001.

Recomendação de conteúdo relacionado do mesmo canal: episódio do Dicionário do Programador sobre **DevSecOps** — cultura que introduz segurança mais cedo no ciclo de vida de desenvolvimento de software.
