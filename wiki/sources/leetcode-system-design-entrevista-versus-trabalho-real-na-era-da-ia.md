---
type: source
title: "LeetCode e System Design: Entrevista vs. Trabalho Real na Era da IA"
aliases: ["leetcode caiu system design subiu", "parecer bom dev vs ser bom dev", "reação ao tweet do bero"]
date_created: 2026-08-17
date_updated: 2026-08-17
source_count: 0
tags: [carreira, ia, leetcode, system-design, entrevistas, mercado-de-trabalho, engenharia-vs-programacao]
skill: tech-mentor-leadership
status: stable
source_file: "raw/leetcode-system-design-entrevista-versus-trabalho-real-na-era-da-ia.md"
source_url: ""
author: "Augusto Galego (inferido, alta confiança)"
date_published: ""
date_ingested: "2026-08-17"
---

## TL;DR

Reação a um tweet ("Bero"): já que todo mundo usa IA para escrever código, valeria mais parecer bom dev (LeetCode + System Design para passar em entrevista) do que ser bom dev. A fonte concorda em parte: LeetCode caiu de relevância prática, System Design subiu; ambos continuam funcionando como filtro de entrevista porque GitHub/portfólio deixou de provar competência (qualquer um gera um SaaS funcional com IA) e porque a maioria das entrevistas de Big Tech ainda é presencial, onde não dá para "colar" com IA. Mas o argumento tem um ponto cego: uma vez contratado, quem não entende como as coisas funcionam por baixo estagna no mesmo teto da IA — e nesse ponto a empresa contrata a IA, não a pessoa. O diferencial real no trabalho (não na entrevista) migrou para System Design, comunicação/tradução de requisitos, CI/CD, observabilidade, feature flags e capacidade interdisciplinar de produto — não para sintaxe ou "escovar bit".

---

## Reivindicações Principais

**Claim:** GitHub/portfólio pessoal perdeu força como prova de competência técnica porque hoje qualquer pessoa consegue gerar um SaaS funcional com IA sem entender profundamente o que foi gerado.
**Evidência:** Comparação temporal qualitativa — em 2019 um bom GitHub era forte sinal de bom dev; hoje um recrutador não consegue avaliar as nuances reais do sistema por trás de um SaaS funcional com 100 usuários.
**Confiança:** Média-alta como observação qualitativa; sem dados de recrutamento, mas coerente com [[wiki/concepts/curriculo-vs-portfolio]] (que já trata portfólio como prova, não promessa) — aqui a fonte argumenta que a própria prova se degradou em poder de sinal.

**Claim:** LeetCode e System Design continuam sendo o filtro de entrevista que as empresas usam para diferenciar candidatos, especialmente em Big Tech — mesmo com o valor prático de LeetCode caindo no dia a dia de trabalho.
**Evidência:** A maioria das vagas de Big Tech é híbrida/presencial e a maior parte das entrevistas presenciais não permite uso de IA durante a prova; algumas empresas (subgrupos do Google, startups) já adaptaram para testes técnicos com IA, mas ainda são minoria.
**Confiança:** Alta como leitura de mercado atual (2026), sem fonte quantitativa citada — relato de observação direta do autor.

**Claim:** No trabalho real (não na entrevista), o valor prático de LeetCode caiu e o de System Design subiu — inversão do que o próprio autor pregava há dois anos.
**Evidência:** Relato de primeira pessoa como dev profissional em exercício: LeetCode aprendido em ~20h já basta para passar em entrevista easy/medium (a maioria das vagas); no dia a dia, é System Design que aparece com mais frequência.
**Confiança:** Alta como relato pessoal qualificado (dev sênior ativo), mas é anedótico — não há medição formal.

**Claim:** Modelos de fronteira ainda não substituíram devs porque construir software é inerentemente iterativo — cada iteração exige atenção e cuidado que a IA não replica sozinha, e requisitos mudam ao longo do processo.
**Evidência:** Teste de sanidade proposto: se um modelo de fronteira fosse de fato melhor que qualquer dev, uma empresa rodando 5-10 agentes em paralelo deveria conseguir produzir um competidor do Figma em um mês — isso não aconteceu, embora fosse extremamente lucrativo se acontecesse.
**Confiança:** Média — argumento por ausência de evidência (ninguém fez, logo não é possível ainda), não uma medição direta da capacidade dos modelos.

**Claim:** O domínio de ferramentas de IA no trabalho de dev é permanente, não uma moda passageira, porque a maioria das tarefas não precisa de modelo de fronteira caro — modelos abertos/baratos (Kimi, DeepSeek, GLM) resolvem a maior parte, e a tendência é rotear tarefa difícil para modelo caro e tarefa simples para modelo barato.
**Evidência:** Referência à Artificial Analysis sobre modelos de fronteira ficando mais caros ao mesmo tempo que mais inteligentes; ~R$20/mês já produz "output absurdo" com modelos baratos.
**Confiança:** Alta como tese de mercado, consistente com [[wiki/entities/artificial-analysis]] já presente na wiki como fonte de benchmarks independentes; a previsão de modelos locais bons "daqui a pouco" é especulativa.

**Claim:** Quem só domina a mesma capacidade que a IA já entrega tende a estagnar profissionalmente, porque a empresa passa a contratar a IA em vez da pessoa — o diferencial sustentável é entender *como as coisas funcionam*, não só operar a ferramenta.
**Evidência:** Relato pessoal: devs júnior com acesso total a modelos de IA ainda cometiam erros típicos de júnior que um sênior com experiência identificava como não sendo a melhor forma de resolver o problema.
**Confiança:** Alta como argumento central da fonte, fortemente convergente com [[wiki/concepts/engenheiro-vs-programador]] e [[wiki/concepts/ia-como-amplificador]] já presentes na wiki.

**Claim:** O diferencial prático do dev na era da IA se traduz em habilidades concretas: System Design, modelagem de banco de dados, tradução de requisitos nebulosos em specs cristalinas, CI/CD com testes que cobrem casos de uso reais, observabilidade (leitura de log, causa raiz, reversão de PR), feature flags, e capacidade interdisciplinar (entender de onde vem o dinheiro, custo de cloud, estimativas).
**Evidência:** Lista extensa e específica de práticas — apresentada como observação direta do próprio trabalho do autor, não como pesquisa.
**Confiança:** Alta como lista qualitativa coerente com o restante do argumento; sem métricas de impacto.

**Claim:** "Escovar bit" (nuances de sintaxe/baixo nível de linguagem) perdeu valor porque testes ficaram baratos — cobrindo bem os casos com testes (inclusive de mutação), um bom dev consegue trabalhar numa codebase de linguagem com pouca familiaridade.
**Evidência:** Exemplos: `==` vs `===` em JavaScript, comportamento de `NaN`. Argumento de custo-benefício, não medição.
**Confiança:** Alta, e diretamente convergente com a tese já registrada em [[wiki/concepts/sintaxe-vs-conhecimento-perene]] (mesma distinção sintaxe vs. conhecimento perene, aqui reforçada com o mecanismo "testes baratos" como explicação de por que sintaxe importa cada vez menos).

---

## Entidades

- [[wiki/entities/augusto-galego]] — autor inferido com alta confiança: mesmo padrão de patrocínio HostGator/VPS/produto "Allstack" já visto em outras fontes atribuídas a ele, e autorreferência direta pelo próprio nome em terceira pessoa na fala ("você pode argumentar Galego mas...") — evidência mais forte de autoria já registrada nesta wiki para este autor
- [[wiki/entities/hostgator]] — patrocinador do vídeo (VPS, hospedagem, produto de agregação de assinaturas de IA "Allstack")
- [[wiki/entities/bero]] — autor do tweet reagido; identidade não confirmada na transcrição (ver Perguntas Abertas)

## Conceitos

- [[wiki/concepts/engenheiro-vs-programador]] — o argumento central da fonte (quem entende "como as coisas funcionam" não estagna no teto da IA) é uma reformulação direta desta distinção
- [[wiki/concepts/sintaxe-vs-conhecimento-perene]] — "escovar bit" caiu de valor com testes baratos; mecanismo explícito novo para uma tese já presente na wiki
- [[wiki/concepts/ia-como-amplificador]] — devs júnior com acesso total a IA ainda cometem erros de júnior; a IA amplifica o julgamento que já existe, não substitui
- [[wiki/concepts/fundacao-tecnica]] — fundamentos (System Design, banco de dados, CI/CD, observabilidade) continuam sendo o que diferencia o dev que "entende" do que só "opera" a IA
- [[wiki/concepts/dependencia-ia]] — risco de estagnar no mesmo teto de capacidade da IA quando não se entende o funcionamento por baixo
- [[wiki/concepts/apagao-de-seniors]] — menção a empresas ainda contratando sênior "letrado em IA" como pré-requisito, reforçando a tese de escassez futura de quem sabe revisar/corrigir o que a IA gera
- [[wiki/concepts/ciclo-de-mercado-tech]] — mudança de contratação (front-end reduzido, mesclado em full-stack) e concentração de cargos como sintoma de ciclo de mercado
- [[wiki/concepts/curriculo-vs-portfolio]] — a fonte argumenta que o poder de sinal do portfólio (GitHub, SaaS pessoal) caiu porque a IA barateou a produção do artefato que antes provava competência
- [[wiki/concepts/portfolio-backend-junior]] — tensão com esta página: se um SaaS funcional não prova mais competência, o que ainda prova?
- [[wiki/concepts/vaga-junior-vira-pleno]] — observação de que front-end como cargo segregado está sendo absorvido por full-stack, reduzindo volume de vagas segmentadas
- [[wiki/concepts/aprender-a-aprender]] — fechamento da fonte: "você não pode querer parar de aprender" — metacognição como requisito permanente da carreira

## Ver também

- [[wiki/sources/como-praticar-leetcode-da-forma-certa-anthony-mays]] — método prático de estudo de LeetCode; esta fonte argumenta que o *porquê* de estudar LeetCode mudou (filtro de entrevista, não ferramenta de trabalho), não o *como*
- [[wiki/sources/system-design-por-nivel-junior-pleno-senior]] — mesmo autor inferido (Augusto Galego); detalha a progressão de expectativas de System Design por nível que esta fonte trata como o novo eixo de diferenciação
- [[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]] — mesmo autor, mesmo tema de fundo (o que ainda exige julgamento humano na era da IA), aqui aplicado a revisão de código em vez de entrevista/carreira

---

## Conexões com Outras Sources

- [[wiki/sources/o-que-sobrou-pro-dev-junior-eric-wendel]] — tensão parcial: aquela fonte argumenta que a ordem de aprendizado pode ser invertida (alto nível antes do fundamento); esta fonte enfatiza que sem entender o "como" por baixo, o profissional estagna no teto da IA — ambas concordam que fundamentos continuam indispensáveis, divergem em ordem de aquisição
- [[wiki/sources/vibe-coding-limites-maturidade-profissional]] — mesmo tema de fundo (o que a IA não substitui: julgamento, contexto de negócio, arquitetura)

---

## Perguntas Abertas

- **Identidade de "Bero" não confirmada.** A transcrição cita um tweet de "Bero" ("cara que Twitch é isso aqui irmão" sugere contexto de streaming/Twitch) como gatilho da reação. Não há handle, sobrenome ou URL. Foneticamente "Bero" poderia ser confundido com "Boris" (já registrado em [[wiki/entities/boris]] como o criador do Claude Code, citado em outra fonte do mesmo autor) — mas não há nenhuma outra evidência de conteúdo que sustente essa ligação (o tema do tweet aqui é carreira/entrevista, não Claude Code/documentação). Tratado como identidade não resolvida; entidade `bero` criada como stub separado até confirmação.
- A fonte não cita nenhum caso real (nomeado, com link) de "SaaS vendido como pronto para produção sem essa validação" — fica apenas como afirmação de princípio, igual ao padrão já registrado em [[wiki/sources/vibe-coding-limites-maturidade-profissional]].
- Não há dado quantitativo sobre quantas entrevistas de Big Tech hoje já incorporam IA no teste técnico — apenas "alguns relatos" e "alguns subgrupos do Google".

---

## Citações

> "Agora que todo mundo usa IA para escrever código, vale muito mais a pena você investir seu tempo para parecer que você é um programador bom do que para você de fato ser um programador bom."

> "Se a sua capacidade é a mesma da IA, a gente contrata a IA e não você."

> "O seu diferencial pro cara de produto é entender onde que o cara de produto erraria se ele usasse [a IA] e onde que você vai acertar."

> "Pergunta pro melhor dev que você conhece o que que ele tá fazendo com IA hoje em dia."

> "Um engenheiro no dia a dia de trabalho dele usa uma calculadora e usa o AutoCAD; você no seu dia a dia vai usar pelo menos por hora um Claude Code ou similar."

> "Diferentemente de um trator, você não precisa de terra para manusear a IA — você precisa de um PC."

> "Você não pode querer parar de aprender."
