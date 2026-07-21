# O que a IA realmente impactou no mercado de frontend

Transcrição de vídeo. Tá, Isaac, mas o que que a IA impactou no frontend? Vamos falar um pouquinho disso hoje. Há uns 7 meses atrás eu fiz um post extremamente provocativo sobre a carreira de frontend. Teve uma repercussão tanto positiva quanto negativa. Mas o que eu trouxe aqui é o que a gente geralmente tá ignorando no mercado de frontend: a IA não substitui o dev, mas a gente teve uma mudança brusca em alguns nichos.

## Os nichos que sumiram

Se você, assim como eu, começou em algum desses tipos de trabalho — agência, freelancer de landing page, consultoria de pequeno porte — lembra que fazia CRUD, aquelas tarefas mais básicas. Isso aqui já não existe mais. Boa parte desse escopo caiu:

- **Agência**: a maioria hoje já tem um processo bem automatizado e não precisa de tantos devs.
- **Freelancer de landing page**: o cliente hoje mesmo gera em qualquer plataforma de IA.
- **Consultorias pequenas**: os times ficaram ainda mais enxutos porque a produtividade é maior.
- **Consultoria de médio porte**: para fazer aqueles CRUDs, antes precisava de um time de cinco, seis pessoas — hoje com duas pessoas você entrega todos esses projetos.

Querendo ou não, o número de vagas diminuiu nesse escopo geral. A gente já tinha tido várias ondas assim antes (no-code, low-code), mas a IA realmente refletiu nisso e gerou um movimento de tornar os times mais enxutos.

## Refletiu em salário? Sim.

Durante a pandemia a média de sênior remoto era algo entre 14k e 18k. Pós-IA, a gente tá vendo 11k a 14k, com vagas majoritariamente híbridas — considerando empresas como Luiza Labs, Hotmart, Itaú. As vagas que oferecem um pouco acima desse range também são todas híbridas, todas em São Paulo, com requisitos a mais.

## O que mudou no dia a dia

**Mais afetado:**
- Escrever teste (antes brigava pra conseguir escrever, hoje não tem mais esse problema)
- Documentação (gerada em minutos)
- Componentes (boa parte automatizada)

**Menos afetado:**
- Arquitetura e design system (identidade de plataforma)
- Performance, sistemas complexos, observabilidade e governança

Se a estrutura organizacional em que você trabalha se parece com isto — microfrontends, design system, libs customizadas (a nível de org ou de monorepo), um time de plataforma/infra que provê deploy e rollback automatizados, ferramentas de observabilidade e monitoramento, gerenciamento de secrets, gestão de CDN/cloud provider/database, métricas correlacionadas (ex.: 90% de cobertura mínima, P99 de performance nas telas core do projeto) — você provavelmente não viu tanta mudança, porque não atua dentro daqueles escopos pequenos e simples que foram os mais impactados.

## O que mudou nas vagas

A gente tá vendo bem menos vagas de frontend — isso é inevitável, até pela demanda: aquela parte simples que era o grosso do trabalho do júnior hoje se faz rápido demais. Em compensação, há um número maior de vagas fullstack/mobile, porque surge a necessidade de o dev assumir mais escopo e responsabilidade, entregando de ponta a ponta.

Mobile, apesar de também ter sido afetado, sofreu um pouco menos porque é mais complexo que frontend web — uma aplicação mobile que funciona offline tem complexidade bem maior. Naturalmente as vagas de mobile ficam um pouco mais preservadas.

## O ponto principal: os requisitos mudaram

Se eu quisesse que você saísse desse vídeo com um único ensinamento, seria este: os requisitos mudaram. Naturalmente você vai ter mais exigência de processo IA-native — o projeto já começando pensando em trabalhar com IA. Spec-driven hoje é obrigatório; se você não sabe disso, eu mesmo te reprovaria numa entrevista, não tem como se defender. Ter um harness apropriado também é obrigatório. Tudo isso leva a um ferramental e estratégias de arquitetura pensadas para IA.

### Monorepo vs. microfrontends para IA

Arquiteturalmente, hoje, para IA, o monorepo é muito interessante: você junta um contexto específico e consegue fazer uma alteração vertical que altera vários módulos de uma vez. Já com microfrontends, uma alteração simples pode gerar, por exemplo, seis tarefas — e você pode ter que linkar um worktree em outro (ex.: linkar o PR do backend com o PR do frontend para sinalizar a interface, para a IA conseguir extrair contexto do outro PR). Ou seja, tudo isso gera um contexto e um trabalho a mais que um monorepo não tem.

### Construir a ferramenta que constrói a coisa

A gente tá vendo uma necessidade de ferramental diferente para os projetos. Antes a gente se preocupava em construir as telas. Hoje a preocupação é gerar ferramental para que a IA gere código de qualidade. A gente constrói a coisa que constrói a coisa. Perguntas para se fazer: você já construiu algum skill? Já gerou algum harness? Já executou alguma tarefa de ponta a ponta com IA? Se você não está seguindo essa onda, pode ser pego desprevenido num layoff e não conseguir se realocar.

Exemplos de aplicação prática:
- **Prevenção de bug**: teve 10 incidentes na empresa — qual a causa principal? Tem algo que a IA poderia fazer para prevenir isso? Dá pra criar um agente de code review que pega os cenários mais comuns de incidente e sinaliza o problema.
- **Pipeline reflete em qualidade**: muitas vezes a gente coloca métricas na pipeline (ex.: cobertura de teste) e trata isso como qualidade única, sem nenhum outro ferramental — só que essa métrica isolada não reflete a qualidade real do projeto.
- **Skills coladas ao dia a dia**: ex. skill pra Linear, skill pra lidar com spec-driven, com todo um harness por trás. Isso vai ser essencial no seu dia a dia — não tem muito para onde fugir.

## Escopos maiores: não dá pra ser só front

Se eu pudesse dar um conselho: não dá para você ser só frontend hoje. O front vai te limitar. Você precisa ganhar espaço em mobile, ganhar espaço em backend. Se você nunca entendeu de fato o que é uma arquitetura distribuída, como funciona uma fila — esse é o momento de estudar. Estudar ferramental de IA: o que é um worktree, como funciona, qual o melhor jeito de tocar duas tasks ao mesmo tempo, como otimizar processos para que os colegas entreguem mais, se existe algum agente que multiplicaria valor pra empresa.

Hoje a gente ganha escopo entre tecnologia e também ganha escopo de produto — não dá para ficar distante do produto. Você tem que pensar em termos de produto: será que esse favorito no e-commerce não faz sentido ter depois uma notificação de preço mais barato? Será que numa lista de presentes não cabe uma notificação real, pensando em que dor isso resolve pro cliente? A gente veio de uma onda de "dev executor", distante do produto, puxando task, entregando task, entregando produto sem pensar nele como ferramental que resolve um problema. Isso trocou.

## Conclusão

Você não é mais um engenheiro de frontend. Você é um desenvolvedor fullstack que entende de produto, que entende como o processo de IA funciona, que entende como seu produto gera valor, que entende como isso afeta a organização.
