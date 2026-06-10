# Construir a coisa que constrói a coisa — O Product Engineer em 2026

**Fonte:** transcrição de vídeo (canal Valdemar Neto)
**Idioma original:** Português (Brasil)
**Data estimada:** 2026
**Contexto:** Relato de viagem ao Vale do Silício — conversas com pessoas do Cursor, Tray, Stripe, Databricks e outras empresas

---

## A frase que define o momento

> "Construir a coisa que constrói a coisa."

Essa frase apareceu em quase toda conversa em São Francisco. Parece poética, mas é a definição mais precisa do que o trabalho do dev virou em 2026.

---

## Descoberta 1 — Quem usa o Cursor hoje

Perguntando ao time do Cursor quais tipos de dev mais usam o produto, a resposta foi surpreendente: **40–50% dos usuários não são devs**. São designers, founders, PMs e pessoas de marketing — e não são vibe coders de fim de semana. São pessoas entregando features em produção que impactam clientes.

O Cursor não pivotou. Eles têm muitos devs. Mas a IA abriu um mercado gigante para outros públicos — os **builders**.

A Tray (ferramenta em crescimento) confirmou: o foco deles agora é atrair builders, não só devs.

### O que isso significa

Não é "todo mundo vai ser vibe coder e os devs acabaram". É que o overlap entre o trabalho do builder e do dev vai aumentar. Builders vão conseguir fazer coisas mais simples. Devs vão ficar na camada de baixo: funcionalidades mais complexas, partes críticas do sistema.

**Quanto mais infraestrutura os devs provêem com segurança, mais os builders conseguem fazer.**

A construção de software está se democratizando rapidamente. Mais gente conseguindo construir vira mais demanda para quem sabe colocar isso em produção com qualidade. Essa onda está abrindo, não fechando.

---

## Descoberta 2 — O que o dev profissional virou

No Cursor, ao perguntar para uma engenheira qual framework de IA ela usa, quais skills, ela ficou surpresa com a pergunta. Para ela, ferramenta não é decisão consciente — é infraestrutura.

A pergunta certa era outra: **o que ela faz com essas ferramentas no dia a dia?**

A resposta:
- O que ela mais gosta não é de código — é de analytics
- Tem acesso total aos dados da empresa
- Pareira com IA para medir impacto e decidir o que priorizar
- Tem vários MCPs que trazem contexto vivo do negócio: dados do Linear, dashboards de produto
- Boa parte do dia é conversar com PM e designer — não só "passar na ideia", mas juntar contexto

### O padrão do Vale

O Cursor cresceu **sem manager tradicional**: tech leads, builders e devs com autonomia total para priorizar o backlog. Esse padrão se repetiu em praticamente todas as empresas visitadas.

O dev profissional nessas empresas é:
- Orquestrador
- Validador
- Com autonomia de PM
- Com fluência em analytics e código
- Com **taste** — não como skill principal, mas como diferencial

---

## O conceito de "taste"

**Taste** (sabor não, julgamento) é a capacidade de fazer julgamento estético e de qualidade sobre produto, código e design **sem precisar de uma regra ou demanda explícita**.

O dev com taste decide o que entregar de ponta a ponta e faz isso com senso de produto. Esse conceito foi mencionado em praticamente todas as empresas visitadas no Vale.

---

## O gap Brasil × Vale do Silício

| Vale do Silício | Brasil (maioria das empresas) |
|---|---|
| Devs com acesso a analytics | Ticket pronto que já passou por PM/PO/Tech |
| Reuniões diretas com PM e stakeholders | Sem acesso a analytics |
| Autonomia para priorizar features | Sem conversa com stakeholders |
| Contexto profundo do negócio | Sem saber a métrica que a feature move |
| MCPs trazendo contexto do negócio para a IA | — |

Quem olha esse gap como ameaça se desmotiva. Quem olha como oportunidade ganha de **1 a 2 anos de vantagem** se se posicionar agora.

**A IA acelera quem já tem alavanca.** Quem só recebe ticket vai entregar código mais rápido, mas ainda tem todo o resto para arrumar. Quem tem contexto e autonomia vai trabalhar em escopo de produto, não só de ticket.

---

## O cargo tem nome: Product Engineer

Empresas como Stripe, Linear e Vercel já contratam com essa terminologia. Não é nome inventado — é terminologia real do mercado.

### Definição

> O Product Engineer é o dev que constrói a coisa que constrói a coisa.

Tem **duas faces inseparáveis**:

**Face 1 — Senso de produto:**
- Decide o que construir
- Fala com PM
- Mede impacto
- Tem taste

**Face 2 — Harness e qualidade:**
- Constrói a infra que permite builders entregarem rápido sem quebrar produção
- System design, code review crítico, debug em produção, intuição sobre o que escala

Se tiver só taste → vira PM disfarçado.
Se tiver só infra → vira Platform Engineer com outro nome.
**As duas juntas definem o cargo.**

---

## Quatro histórias concretas da prática

### História 1 — Tech Lead do Databricks: orquestração nos intervalos

A manhã do tech lead: reuniões, planejamento, mentoria. Isso não mudou. O que mudou foi **o que ele faz nos intervalos entre reuniões**.

> "Saio de uma reunião, em vez de pegar café enquanto checo o Slack, disparo dois ou três Claude agents para avançar tasks do projeto. Vou para a próxima reunião. Volto, os agentes deixaram um pull request para eu revisar. Reviso, boto novos agentes, e assim vou."

Ao longo do dia: 3 a 4 pull requests avançados. O tempo entre reuniões — antes basicamente perdido — virou onde mais código avança. O code review virou trabalho concentrado num bloco, não uma interrupção constante. O dia virou essencialmente **orquestração e review**.

---

### História 2 — Engenheira do Cursor: projetos longos viram tasks pro agente

Projetos de meses são quebrados em um padrão específico:

- Nível mensal: projeto → lista de partes (parte 0, parte 1, parte 2...)
- Cada parte é uma **feature full stack**: schema no banco → service layer → API → UI
- Cada feature é quebrada em tasks para o agente

**Critério da quebra** (palavras dela): "a menor quantidade de trabalho mais a maior quantidade que um agente consegue fazer sem esbarrar em outro agente."

Uma feature completa com migration, schema e API → task feita junto para que o agente entregue de ponta a ponta.

Na prática:
- Cada feature dispara ~5 Claude agents simultâneos rodando em paralelo
- Mais 1 agente fazendo code review
- Ela validando o resultado

Dev tradicional faz uma task por vez. Esse fluxo toca 6 a 7 em paralelo.

A coordenação antes era entre devs paralelos. Agora é entre agentes paralelos. **O trabalho de coordenação não acabou — mudou de objeto.**

---

### História 3 — Decisão informada antes de codar

Antes de implementar uma feature, várias engenheiras faziam algo que o dev tradicional pula: **pedir ao agente para consultar o banco de produção via MCP para entender o usuário antes de codar**.

Exemplo concreto de uma engenheira:

> "Para essa feature de listagem, quantos usuários teriam mais de X itens?"

O agente vai ao banco, traz o número. Se a maioria dos usuários tem muitos itens, a decisão já sai: paginação infinita, não simples. A decisão sai informada, não chutada.

O agente conecta: feedback do usuário + dados de produção + métricas de serviço + audit logs — tudo via MCP. O agente vira pesquisador, o dev vira decisor.

---

### História 4 — Incidente no Cursor: investigação em minutos

Bug crítico em produção. O jeito antigo: abrir Datadog em uma aba, audit log em outra, GitHub em outra, Slack em outra, correlacionar manualmente. Demora.

O que a engenheira fez: abriu o **Canvas** (feature do Cursor 3) e mandou um único prompt:

> "Consulta o Datadog, consulta os Audit Logs e cria uma timeline conectando esses dados ao histórico recente do GitHub com pull requests."

O agente puxou tudo, gerou um diagrama estruturado em poucos minutos. Ficou claro: havia um PR específico mergeado pouco antes do bug começar — era a causa. Cruzou tudo e gerou algo pronto para um post-mortem.

A engenheira:

> "Antes eu ia abrir um Confluence, passar o dia escrevendo um post-mortem com diagramas, buscando dados de todo lugar, provavelmente usando Illustrator para criar um gráfico. Hoje peço para ele fazer. Ele faz em minutos."

Isso não é código mais rápido. É **investigação, decisão e comunicação mais rápidas**. Empodera qualquer dev experiente.

---

## Quatro movimentos para começar essa semana

### Movimento 1 — Mentalidade de produto
Leituras recomendadas:
- *Product Minded Engineer* (artigo)
- *Extreme Programming Explained*

### Movimento 2 — Reunião com PM
Marca uma reunião com o PM da tua área essa semana. Pergunta exata:

> "Qual métrica de negócio o time está movendo esse trimestre e como minhas features se conectam com ela?"

Se ele souber responder: você ganhou contexto valioso. Se não souber: você foi a primeira pessoa do time a perguntar. Ambos os cenários jogam a seu favor.

### Movimento 3 — Construir uma peça de harness
Não precisa ser grande. Exemplos pequenos:
- Um template de spec que padroniza como o time pede features para a IA
- Uma skill que captura o conhecimento que você repete toda sprint
- Uma skill que melhora o code review do projeto
- Uma skill que melhora os testes do projeto

**Esse é o trabalho do Product Engineer: construir a coisa que constrói a coisa. Começando pequeno.**

### Movimento 4 — Voltar aos fundamentos de system design
Alguém precisa decidir se o código que a IA gerou escala e faz sentido arquiteturalmente. Esse alguém é o Product Engineer.

Recursos:
- *Designing Data-Intensive Applications* (livro)
- Canal Byte Byte Go no YouTube — um exercício por semana

> Nenhum desses movimentos é "construir agentes" ou "aprender machine learning". Os quatro te aproximam do perfil de Product Engineer a partir de segunda de manhã.

---

## Resumo da tese central

| Antes | 2026 |
|---|---|
| Dev constrói a coisa | Dev constrói a coisa que constrói a coisa |
| Código é o produto | Harness + senso de produto são o produto |
| Trabalho em ticket | Trabalho em escopo de produto |
| Coordenação entre devs | Coordenação entre agentes |
| Ferramentas são decisão | Ferramentas são infraestrutura |
