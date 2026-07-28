# Dívida Técnica: Tudo que Você Precisa Saber

> Transcrição traduzida do inglês e reestruturada em seções para legibilidade. Conteúdo e ordem dos argumentos preservados; nenhuma claim foi adicionada ou removida. Vídeo patrocinado por Monday.com (parte específica sobre Monday Magic mantida por completude, mas não é o foco da ingestão).

## O que é dívida técnica

Dívida técnica nem sempre é algo ruim. É quando você toma atalhos para ir mais rápido, sabendo que isso vai te atrasar depois. Se você já programou e pensou "eu conserto isso depois", "eu refatoro isso depois" — você acabou de tomar dívida técnica.

### Os quatro quadrantes de Martin Fowler

Existem quatro tipos principais, conhecidos como os quatro quadrantes de Martin Fowler para dívida técnica:

1. **Deliberada e prudente** — "precisamos lançar agora e lidamos com as consequências depois". É uma decisão estratégica de negócio.
2. **Deliberada e imprudente** — "não temos tempo para design". Perigoso, mas ainda uma escolha consciente — ainda é deliberada.
3. **Inadvertida e prudente** — "agora sabemos como deveríamos ter feito". Você está aprendendo mais sobre a dívida técnica ao longo do caminho.
4. **Inadvertida e imprudente** — talvez o que a maioria de nós faz. Não é uma camada com nome elegante — só mostra falta de habilidade e consciência.

## A analogia com dívida financeira

Dívida técnica é como dívida financeira — como um empréstimo empresarial, por exemplo, onde você pega dinheiro emprestado que o "você do futuro" precisa pagar de volta. Em dívida técnica, você toma emprestado tempo que o "você do futuro" precisa pagar de volta. E assim como você paga juros sobre um empréstimo, você também paga juros sobre dívida técnica toda vez que toca aquele código. Os juros são todo o tempo extra trabalhando ao redor dela, debugando ou simplesmente sendo desacelerado por ela.

Muitos times nem percebem por que as coisas estão demorando tanto mais do que deveriam, ou do que costumavam demorar — a resposta é toda essa dívida técnica acumulada.

## Os números: quanto tempo e dinheiro isso consome

Pesquisas mostram que:

- Times gastam em média **entre 23% e 42%** do tempo lidando com dívida técnica.
- Isso desacelera a velocidade de desenvolvimento em **cerca de 20 a 40%** — parece ser o "número mágico".
- Orçamentos de TI também alocam **cerca de 20 a 40%** para endereçar dívida técnica.
- O custo de corrigir a dívida aumenta exponencialmente com o tempo se não for tratado — é juro composto, igual à analogia do empréstimo.

## Como lidar com dívida técnica: alocação de tempo

### A regra dos 80/20 (20% do tempo por sprint)

Uma das formas mais populares: gastar **20% do tempo a cada sprint** dedicado a atacar dívida técnica, incluindo manutenção. Em uma semana de 5 dias, isso é 1 dia por semana, dividido como for melhor para o time.

Isso permite manter a **velocidade de features** (a taxa em que o time entrega novas funcionalidades) e evita que a dívida se acumule. 80% do tempo e recursos em novas features/tecnologias, 20% em reduzir ou gerenciar dívida técnica.

### A regra dos 25% do Shopify

Outros times, como o Shopify, acham que 20% não é suficiente. Eles usam a **regra dos 25%**:

- **10% para dívida diária** — deixar o código em que você está trabalhando melhor. Totaliza 4 horas por semana. A ideia é incorporar a prática de refatoração à cultura do time. Esses 10% são sobre código com o qual você já está trabalhando no dia a dia — não é sair caçando código ruim aleatório (não é abrir o SonarQube procurando code smells). É a fricção que você sente ao implementar uma feature nova, e aí você tem permissão e é encorajado a entrar e refatorar aquela parte, para não sentir a mesma fricção da próxima vez.
- **10% para dívida semanal** — algo planejado de fato, com itens no board do projeto, que pode ser dividido entre o time (4h por pessoa em um time de 4 = 16h no total) ou uma pessoa dedicando 2 dias inteiros.
- **5% para dívida mensal/anual** — duas reuniões de uma hora por semana para planejar e endereçar os problemas maiores, e ver se precisam virar prioridade.

### O sprint dedicado

Outra abordagem: dedicar um sprint inteiro a cada 6-8 sprints (assumindo sprints de uma semana) só para dívida técnica e manutenção, enquanto os outros sprints são focados em features.

## Práticas de prevenção

- **Test-Driven Development (TDD)** — escrever os testes primeiro para prevenir que código mal desenhado entre no sistema. Não é gerenciar dívida técnica diretamente, é prevenir que ela entre, ou pelo menos desacelerar a entrada, porque é difícil escrever lógica confusa quando você precisa passar num teste limpo primeiro.
- **Pair programming** — duas pessoas olhando e implementando o mesmo código juntas torna muito mais difícil tomar atalhos idiotas, porque um vai questionar o outro ("vamos fazer direito"), ou você fica autoconsciente demais para escrever código ruim com alguém olhando por cima do ombro. Extremamente subestimado como prática de prevenção.
- **CI/CD com quality gates** — automatizar análise estática, cobertura de testes, regras de lint. A IA pode ajudar em alguns casos, mas não é para confiar cegamente nela para isso. Isso impede que código "lixo" chegue ao servidor de desenvolvimento e, principalmente, à produção. Nunca faça deploy direto para produção sem passar por servidor de desenvolvimento/teste.
- **Design patterns** — não é necessário superengenhar tudo (nem toda classe precisa ser um diagrama Gang of Four), mas usar arquitetura consistente torna a base de código mais fácil de entender e manter.
- **Boy Scout Rule** — deixe o código mais limpo do que você encontrou. Não significa reescrever tudo — significa: viu uma variável com nome ruim, renomeie; viu código morto, delete. Essas pequenas coisas se compõem nos dois sentidos (para bem ou para mal) — evite acabar como o caso do Knight Capital, que teve uma perda de $462 milhões.
- **Red-Green-Refactor** — onde TDD e Boy Scout Rule se encontram. Red: escreva testes que falham de propósito (o código ainda não existe). Green: escreva só o código suficiente para passar no teste, nada perfeito, só funcional. Refactor: limpe tudo, dê nomes melhores, remova duplicação, divida métodos — tudo aquilo que normalmente é pulado por falta de tempo.

## Como medir dívida técnica

### SQALE / debt ratio

Método estruturado: **SQALE** (S-Q-A-L-E). E a fórmula de debt ratio:

```
Technical Debt Ratio = Remediation Cost / Development Cost
```

Ou seja: quanto tempo/dinheiro custaria consertar a bagunça, dividido por quanto tempo/dinheiro custou construir a coisa originalmente. Exemplo: se custar $100.000 para consertar a dívida em um sistema de $500.000, isso é um debt ratio de 20%.

Faixas (como aparecem em ferramentas como o SonarQube):

- **< 5%** — bom, é onde você quer ficar.
- **5–10%** — ainda bom, mas de olho.
- **10–20%** — risco moderado, começa a prejudicar a velocidade de desenvolvimento.
- **> 20%** — ruim — você não consegue entregar nada sem brigar com a base de código a cada passo.

### O modelo de três fatores (triângulo)

Para priorizar o que atacar primeiro:

1. **Impacto** — quão mal isso está nos desacelerando?
2. **Custo fixo** — quão difícil é consertar?
3. **Espalhamento (spread)** — quanto da base de código está infectado?

Priorize o que é de alto impacto, não tão difícil de consertar, e que se espalha como um vírus pela base de código — atacar isso primeiro é o mais eficiente.

### Outros pontos de rastreamento

- **Complexidade ciclomática** — quantos branches de decisão existem no código. Mais branches = mais difícil de manter.
- **Cobertura de testes** — não só "temos testes", mas quanto da lógica está de fato protegida e testada.
- **Lead time** — tempo do commit até estar em produção. Se esse tempo cresce ao longo do tempo, pode ser dívida técnica entupindo o pipeline. É algo que acontece gradualmente e as pessoas geralmente não percebem, até olharem para trás e notarem "esse tipo de feature costumava levar 2 dias, agora leva uma semana".
- **Code churn** — se o mesmo arquivo continua mudando toda semana, alguma coisa está errada.
- **Regra de Pareto (80/20 dos hotspots)** — 80% da dor provavelmente vem de 20% dos arquivos.

A ideia não é eliminar completamente a dívida técnica — é ser inteligente sobre isso: caçar os hotspots, priorizar onde o incêndio está.

### O framework PAID

Framework simples para saber por onde começar:

- **P**erformance impact — isso está deixando o app lento?
- **A**rchitectural importance — isso é central ao sistema ou uma feature marginal?
- **I**ntegration complexity — isso está amarrado a 10 outros sistemas?
- **D**ependency — mudar isso vai quebrar um monte de coisa?

Combine isso com a regra 80/20 dos hotspots para montar um roadmap de por onde atacar.

## Refatorar ou reescrever?

Outra matriz 2x2 para decidir:

- **Alto valor de negócio + baixo risco técnico** → refatorar.
- **Alto valor de negócio + alto risco técnico** → reescrever.
- **Baixo valor de negócio + baixo risco técnico** → conviver com isso.
- **Baixo valor de negócio + alto risco técnico** → depreciar.

## Ferramentas e automação

- **SonarQube** (a mais usada pelo autor), Code Climate e Code Scene — cada uma com nichos diferentes.
- Fluxos de integração: gates de deploy baseados em thresholds de qualidade, tracking automatizado de dívida.
- Comunicação: notificações via Slack/Teams para acúmulo de dívida.
- Dashboards de reporting para stakeholders.
- Tracking em tempo real: alertas quando o debt ratio ultrapassa thresholds definidos, métricas de impacto na velocidade, inventário de dívida mantido no backlog.

## Comunicando dívida técnica para stakeholders

Ao explicar dívida técnica para quem não entende o conceito, a analogia com dívida financeira funciona bem. Além disso, fale com dados, números e estimativas de tempo — o impacto da dívida, tipo: "esse sistema de autenticação, por causa da dívida técnica envolvida, adiciona 2 dias a cada user story envolvendo login" ou "nosso processo de deploy — a dívida causa 30% dos incidentes de produção".

Framework completo de business case:

1. **Estado atual** — que dívida existe e seu impacto mensurável.
2. **Risco de negócio** — o que acontece se não for endereçada.
3. **Investimento necessário** — tempo e recursos.
4. **ROI esperado** — velocidade aumentada, incidentes reduzidos.
5. **Timeline** — abordagem faseada com marcos.

Exemplo de caso de falha real: uma empresa reescreveu um sistema inteiro em vez de fazer refatoração direcionada, e passou **18 meses sem adicionar nenhuma feature nova**. Sim, eles ficaram sem dívida técnica, mas estagnaram por um ano e meio — por isso é preciso pesar as opções e fazer refatoração direcionada.

## Roadmap de implementação (resumo prático)

**Fase 1** — instalar a ferramenta de medição, deixá-la mostrar a dívida existente na base de código; identificar os 5 principais hotspots de dívida; calcular o debt ratio atual; estabelecer métricas de baseline.

**Fase 2** — corrigir os itens de baixo esforço e alto impacto (low-hanging fruit); implementar as práticas de prevenção discutidas; configurar tracking automatizado (alertas de debt ratio, etc.).

**Fase 3** — escolher um framework de alocação (regra dos 20%, regra dos 25% do Shopify, ou um sprint dedicado a cada 6-8 sprints); endereçar os itens de dívida de maior impacto; estabelecer ciclos de revisão regulares (reviews mensais de dívida); acompanhar melhorias de velocidade (tempo de commit até produção); reportar aos stakeholders periodicamente; continuar com práticas de prevenção e cultivar a cultura de qualidade.

## Conclusão

Toda base de código tem dívida técnica. A diferença entre times de alta performance e times com dificuldades não é a ausência de dívida — é a disciplina de gerenciá-la conscientemente. O objetivo não é eliminar a dívida (o que pode significar 18 meses sem features) — é fazer o trade-off consciente entre velocidade e dívida técnica, para que ela sirva aos seus objetivos em vez de sabotá-los.

Sinais de alerta de dívida técnica não gerenciada: aumento na taxa de incidentes de produção, desenvolvedores evitando certas áreas da base de código, tempo crescente para mudanças simples, novos membros do time com dificuldade acima do normal para entender a base de código.
