---
title: "Monolith First"
author: "Martin Fowler"
source_url: "https://martinfowler.com/bliki/MonolithFirst.html"
date_published: 2015-06-03
date_ingested: 2026-08-18
note: "Resumo/paráfrase em PT-BR do artigo original (bliki entry), com trechos curtos entre aspas preservados no idioma original para citação exata. Não é uma tradução integral — para o texto completo em inglês, consultar a source_url."
---

# Monolith First (resumo)

Fowler observa um padrão em histórias de times usando microsserviços: quase todo caso de sucesso começou como um monolito que cresceu e foi quebrado depois; quase todo sistema construído como microsserviços desde o zero, de que ele ouviu falar, acabou em sérios problemas. Isso leva vários colegas dele a defenderem que projetos novos não deveriam começar com microsserviços, mesmo com a expectativa de que a aplicação vá crescer o bastante para justificá-los depois.

**MicroservicePremium**: até defensores de microsserviços reconhecem um "prêmio" — o custo de operar um conjunto de serviços distribuídos — que só compensa em sistemas mais complexos. Para aplicações simples, esse prêmio favorece o monolito.

**Argumento 1 (YAGNI)**: no início, não há certeza de que a aplicação será útil; a forma mais confiável de descobrir costuma ser construir algo simples e testar. Nessa fase, prioriza-se velocidade de ciclo de feedback, e o prêmio de microsserviços é peso desnecessário.

**Argumento 2 (BoundedContexts)**: microsserviços só funcionam bem com fronteiras de serviço estáveis. Mesmo arquitetos experientes erram essas fronteiras no início; refatorar entre serviços já distribuídos é bem mais caro do que dentro de um monolito. Construir o monolito primeiro dá tempo de descobrir as fronteiras certas — e de desenvolver os pré-requisitos (`MicroservicePrerequisites`) necessários para serviços mais granulares — antes que o design distribuído as trave.

Fowler descreve quatro caminhos práticos que já observou para executar a estratégia:

1. Desenhar um monolito modular com cuidado desde o início (fronteiras de API e de dados bem pensadas) e migrar depois — ele mesmo pondera que confiaria mais nisso com mais histórias reais de sucesso.
2. Começar com o monolito e ir "descascando" microsserviços gradualmente nas bordas, deixando um monolito residual relativamente quieto no centro.
3. Tratar o monolito como uma `SacrificialArchitecture` — construí-lo sabendo que será descartado por inteiro depois, sem culpa nisso, se acelerar a chegada ao mercado.
4. Começar com poucos serviços de granulação grossa (maiores do que os serviços finais esperados) — o que ele brinca em nota de rodapé que, a rigor, deveria ser chamado de "duolith" — para reduzir a refatoração entre serviços enquanto as fronteiras ainda não estão estáveis, quebrando em serviços menores só depois que elas se estabilizam.

**Contra-argumento reconhecido**: começar direto com microsserviços acostuma o time ao ritmo de desenvolvimento distribuído desde cedo, e times separados por fronteira de serviço facilitam escalar o esforço de desenvolvimento. Isso é especialmente viável em substituições de sistemas existentes, onde as fronteiras já são mais conhecidas — mas Fowler condiciona isso à equipe já ter experiência razoável construindo sistemas de microsserviços.

Fowler fecha o artigo com uma ressalva epistêmica explícita: em 2015 ainda não tinha anedotas suficientes para uma posição firme sobre quando usar a estratégia monolito-primeiro — "estes são dias iniciais em microsserviços" — e trata qualquer conselho sobre o tema como tentativo, por mais confiante que soe o argumento.

## Citações diretas preservadas (idioma original)

> "Almost all the successful microservice stories have started with a monolith that got too big and was broken up"

> "you shouldn't start a new project with microservices, even if you're sure your application will be big enough to make it worthwhile."

> "By building a monolith first, you can figure out what the right boundaries are, before a microservices design brushes a layer of treacle over them."

## Metadados do artigo

- Publicado em 3 de junho de 2015.
- Tags do artigo: "evolutionary design", "microservices".
- Imagem central (`images/microservice-verdict/path.png`): dois caminhos a partir de um mesmo ponto de partida — caminho de cima, direto para microsserviços, ilustrado com dragões (risco/complexidade); caminho de baixo, começando com monolito, sem dragões.
- Leitura adicional citada por Fowler: estudo de caso de Sam Newman sobre um time considerando microsserviços num projeto greenfield.
