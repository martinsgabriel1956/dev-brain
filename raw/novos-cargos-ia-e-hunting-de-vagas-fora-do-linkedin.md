# Novos cargos pós-IA e como fazer hunting de vagas fora do LinkedIn

> Transcrição de vídeo de YouTube (apresentadora "Ana", canal não identificado na transcrição), colada pelo usuário e limpa. Já estava em português; sem tradução.
> Limpeza: correções de ASR (ex.: "Scally Draw" → Excalidraw? [incerto], "Starbook" → Storybook, "Linkedajin" → LinkedIn, "Laurer" → Lever? [incerto], "Cloud Code" → Claude Code, "Codex"), pontuação e parágrafos adicionados, repetições de fala removidas. Omitido: abertura/propaganda da mentoria Coders (link no comentário fixado, 60 min de consultoria gratuita), pedidos de like/inscrição e despedida. Números ("50%", "59%", "280%") e o valor "250.000 anuais" são ditos pela apresentadora, sem fonte verificada (ela diz que deixa o link dos dados na descrição do vídeo, que não veio na transcrição).

## Contexto e disclaimer

A apresentadora trabalha há ~2 anos ou mais no mercado internacional, com clientes americanos. Argumenta que a sociedade sempre foi movida por grandes transformações seguidas de períodos de equilíbrio (status quo) e que o surgimento de novos cargos **não** significa o fim do software engineer: é o mercado, principalmente startups, entendendo novas necessidades e criando cargos que antes não existiam. Insiste em fazer entrevistas no mercado internacional porque "tudo começa lá e depois vem para cá"; o mercado brasileiro demora a "pegar no tranco".

## Os dois perfis de dev pós-IA

1. **Dev genérico**: quem se apega a um ecossistema e não diversifica ("só faço front, não mexo em back, não contem comigo para DevOps"). Executa um ticket de uma camada só. Vagas para esse perfil teriam caído em quase **50%**; ainda aparecem em consultorias com clientes que querem perfis específicos, mas é um perfil "difícil de manter", mesmo dentro do cliente.
2. **Dev que usa IA / resolve problemas de ponta a ponta**: perfil com maior crescimento de vagas (cita **59%**). O mercado precisa de quem resolve o problema: se o problema exige melhorar o CI, melhora o CI. Se é de outro time (ex.: o time de Developer Experience que cuida do CI), leva o problema e uma possível solução ao time dono ("vocês acham que faz sentido? se precisarem de ajuda, posso colaborar"). Às vezes o cliente não precisa de uma tela nova, e sim de uma melhoria de processo. Em startups americanas essa abordagem é muito bem vista.

**Cuidado:** muita gente confunde autonomia de *sugerir* com *pegar para si*. Resolver ponta a ponta é entender o que é do seu escopo, para quem delegar o que não é, e continuar atuando no seu escopo para dar produtividade ao time.

## Os cargos (a IA "saiu da demo e foi para a produção")

### Forward Deployed Engineer
- Executor que atua diretamente com o cliente; na empresa dela (um SaaS) há muitas vagas. Nem sempre mexe em código, mas muitas vezes sim: implementar o SaaS no cliente exige personalização e configuração.
- Quem tem background de código sugere melhorias, ex.: automatizar a implementação do serviço no cliente e reduzir o tempo de configuração.
- Segundo as pesquisas dela, foi o cargo que **mais cresceu**, principalmente em 2026 ("crescimento absurdo").
- Indicado para quem, no Brasil, trabalha com Customer Experience ou suporte N3, tem familiaridade com código, projetos pessoais, conhecimento de cloud e de ferramentas como Claude Code/Codex — e inglês, pois fala sempre com o cliente.
- As empresas ainda estão ajustando o que o cargo deve entregar.

### AI Engineer
- Opinião dela: diferente do Agent Engineer. Atua em **produtos e modelos**; um dos cargos que mais crescem nos EUA.
- Exige aprofundamento em **machine learning**; faz sentido para quem faz pós/especialização em ML Engineer. Quem ainda não pegou o gancho de IA deveria se aprofundar no ecossistema de ML para conseguir bons salários.

### Agent Engineer
- Dev que pode ser cross-team: analisa um problema do time e sugere como automatizá-lo (n8n, agente agnóstico etc.); cria skills, automações e orquestra agentes. Ela diz atuar um pouco nos dois (AI e Agent Engineer).
- Cresceu mais de **280%** e deve crescer mais, por ser um trabalho que o software engineer já faz bastante.

### Designer / Design Engineer
- "O design acabou por causa do Claude Design?" Resposta: não; como em qualquer profissão, incorpora as mudanças. O comum agora é design + front-end: não fazer "caixa por caixa" no Figma do zero, e sim usar o **design system** para otimizar entregas de protótipos com IA / Claude Desktop.
- Papel do front especialista: criar o ecossistema de design system (com Storybook, com todos os componentes) para o design otimizar entregas com IA. Quando o produto tem uma ideia, o time entrega um protótipo rápido.
- Não acredita que design vire front ou vice-versa, mas que designer com conhecimento de código é cada vez mais necessário: em vez de esperar o time responder "isso é possível?", abra o Claude, peça uma varredura do projeto e converse com o código.

## Hard skills × cargos

- **Backend** (entender a code base, sugerir e validar APIs, latência, performance, conceitos de system design): vale para os três — Forward Deployed, AI e Agent Engineer.
- **Dados / machine learning**: não precisa se especializar totalmente, mas quem estuda se diferencia; tema bem presente em AI Engineer (as pós-graduações de AI Engineer trazem esses temas).
- **Design Engineer**: designer que já codifica um pouco, ou front-end especialista em UI/UX.

## Por que o LinkedIn é o último lugar para achar vaga

"É o último lugar onde a vaga chega e o primeiro onde a concorrência chega."
1. **Atraso:** a vaga nasce no **ATS** (Application Tracking System) da empresa; só depois alguém do time de RH republica no LinkedIn, às vezes dias depois.
2. **Volume:** quando aparece no feed já tem centenas de candidatos; o botão de candidatura fácil agrava.
3. **Vagas fantasmas:** o anúncio fica no ar depois que a posição fechou, porque alguém precisa ir ao LinkedIn fechá-lo.
4. **Filtro "remote" quebrado:** quase sempre significa remoto *dentro dos Estados Unidos*.

## O truque: buscar direto nos ATS

- Os ATS mais usados por startups de IA: **Ashby, Greenhouse, Lever**. Cada um publica vagas num formato de URL fixo.
- **Método:**
  1. Listar de **30 a 50 empresas-alvo** (pedir ajuda ao Claude/Codex). Ex.: 30 de senior software engineer + 20 de forward deployed engineer.
  2. Preparar **3 a 4 currículos diferentes** (um destacando experiência com cliente, outro como software engineer etc.), em PDF.
  3. Descobrir o ATS de cada empresa pela página de Careers (ou ir direto pela busca por URL). Salvar em favoritos, planilha ou como parâmetro para a IA.
  4. Usar o Google com o operador `site:` — ex.: `site:jobs.ashbyhq.com "forward deployed engineer"` — e filtrar pela última semana (ferramentas → última semana; ou parâmetro na URL da busca). O Google Alerts pode rodar sozinho todo dia.
  5. É possível buscar os três ATS de uma vez com `site:` combinado por `OR` (Ashby, Greenhouse, Lever) para um título como "AI engineer". Resultados patrocinados aparecem primeiro; focar nos não patrocinados. Ela gosta bastante do Ashby ("um dos melhores"; ex.: vagas de OpenAI no Ashby).
  6. Também dá para o caminho inverso: usar a query para **excluir** o que não serve (ex.: `"must be authorized to work in"` filtra vagas que exigem autorização nos EUA).
  7. Depois, pesquisar a empresa no LinkedIn, achar o recruiter, conectar e mandar mensagem.
- LinkedIn fica como último recurso ou em paralelo (posts, relevância, SEO do perfil).
- **Automação:** criar um agente especialista com as ambições de carreira que rode a query diariamente, liste empresas/vagas e alerte quando achar um perfil específico. Citou os MCPs de busca web do Google.

### APIs públicas dos ATS
- Ashby, Greenhouse e Lever têm **APIs públicas, sem autenticação**, que devolvem as vagas em **JSON** (mais fácil para agentes).
- Endpoints: `api.ashbyhq.com`, `api.greenhouse.io`, `api.lever.co` com o nome da empresa (o Lever tem formato um pouco diferente). Nenhum endpoint exato foi dado em texto na transcrição.
- O parâmetro `includeCompensation=true` do Ashby traz a **faixa salarial** (campos de moeda, mínimo e máximo). No exemplo mostrado: uma vaga de ~250.000 por ano (valor lembrado de memória pela apresentadora: "se eu não estou enganada").

### Fragmentação de títulos (erro comum: buscar só um termo)
A mesma vaga aparece com nomes diferentes em cada empresa. Fazer uma busca por cada nome ("5 minutos") mostra o mercado que a maioria não vê.
- **Forward Deployed Engineer** → deployment engineer, solutions engineer, applied AI engineer, AI engineer.
- **AI Engineer** → GenAI engineer, LLM engineer, **Applied AI Engineer** ("quase o novo software engineer do dia antes").
- **Agent Engineer** → agentic AI engineer, AI automation engineer.
- **Designer / Design Engineer** → product engineer, UI engineer (front-end especializado em UI/UX, responsividade, acessibilidade).

## Inversão: caçar a empresa, não a vaga

Caçar a vaga depende de estar no lugar certo na hora certa; caçar a empresa faz você saber onde a vaga vai nascer antes de ela existir e conhecer o business. Método: listar 30–50 empresas onde realmente quer trabalhar, descobrir o ATS de cada uma pela página Careers, salvar os links (favoritos/planilha/IA) e passar a lista uma vez por semana, automatizando com as APIs. Fonte de listas: **Y Combinator** (aceleradora; a página "companies" lista as empresas aceleradas).

## Sinais de que a vaga vale (ou não) a candidatura

| Sinal | Leitura |
|---|---|
| LATAM, South America, Brazil, Remote Worldwide | Contratam brasileiro |
| Menção a "contractor", "deel/remote.com" etc. (ASR: "dearremote.com") | Têm estrutura para contratar de fora |
| "Must be authorized to work in the US" | Não adianta aplicar (pede autorização de trabalho nos EUA) |
| "Remote US" / "US time zones only" | Quase sempre exigem estar nos EUA; não é impeditivo absoluto, mas priorizar as outras |
| Faixa salarial publicada | Vaga real e recente (algumas leis dos EUA obrigam a exibir) |
| Data de publicação recente no ATS | Concorrência ainda baixa — vale caprichar no currículo e mostrar evidências |
| Sem data e sem movimentação há meses | Vaga fantasma — não perder tempo |

## Conclusão

Os novos cargos não indicam que software engineer está acabando; são possibilidades, sobretudo para quem se sentia perdido na atuação. Ela hesitou em gravar sobre as dicas de busca por achá-las "básicas", mas nas mentorias o pessoal tinha muita dificuldade de achar boas vagas. Se a vaga já veio com uma resposta/possibilidade de entrevista, "não podem fazer dar errado".
