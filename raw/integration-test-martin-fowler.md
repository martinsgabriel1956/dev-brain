---
title: "Integration Test"
author: "Martin Fowler"
source_url: "https://martinfowler.com/bliki/IntegrationTest.html"
date_published: 2018-01-16
date_revised: 2021-06-03
date_ingested: 2026-07-07
note: "Resumo/paráfrase em PT-BR preparado para a wiki, não é tradução literal do artigo original. Para o texto exato, consultar a source_url."
---

# Integration Test — resumo comentado

Martin Fowler observa que "teste de integração" é um dos termos mais ambíguos do vocabulário de testes de software, e por isso ele evita usá-lo sem qualificação. O artigo reconstrói a origem do termo e mostra como ele passou a significar coisas diferentes para pessoas diferentes.

## Origem histórica (anos 80, mundo waterfall)

Em projetos grandes dos anos 80, a fase de design especificava a interface e o comportamento de cada módulo antes de qualquer código ser escrito. Um único desenvolvedor podia passar meses construindo um módulo isoladamente e só depois entregava para o time de QA.

O processo de QA tinha duas etapas sequenciais:
1. **Teste unitário**: validar o módulo isolado contra a especificação de design.
2. **Teste de integração**: ativar vários módulos juntos (ou o sistema inteiro) e rodar testes de nível mais alto para garantir que eles funcionassem em conjunto.

Fowler aponta que essa definição original, sem perceber, misturava duas preocupações diferentes:
- verificar que módulos desenvolvidos separadamente conseguem se comunicar corretamente;
- verificar que o sistema composto por vários módulos se comporta como esperado.

Nos anos 80 era difícil separar essas duas coisas: para testar se o módulo de carrinho de compras conversava direito com o módulo de catálogo, bastava rodar os dois juntos e observar o resultado — não havia alternativa prática.

## A alternativa moderna: dublês de teste

A perspectiva atual (2010s em diante) oferece uma saída que raramente era cogitada nos anos 80: testar a integração do carrinho com o catálogo exercitando apenas a fatia de código do carrinho que conversa com o catálogo, rodando contra um **dublê de teste** (test double) do catálogo — desde que esse dublê seja fiel ao comportamento real do serviço.

Essa abordagem não muda muito quando os dois módulos vivem no mesmo processo de uma aplicação monolítica, mas se torna decisiva quando o catálogo é um **serviço separado**, com seu próprio pipeline de build, ambiente e rede. Nesses casos o dublê pode ser algo local (in-process) ou algo que responde de fato pela rede, usando ferramentas como o *mountebank*.

O ponto fraco óbvio dessa técnica é garantir que o dublê realmente reflita o comportamento do serviço real — problema que Fowler resolve remetendo a **testes de contrato** ([[contract-testing]]), verificados separadamente. Combinando integração estreita + contract tests, é possível confiar numa integração externa sem nunca rodar testes contra uma instância real do serviço, o que acelera bastante o pipeline de build. Times que adotam esse padrão ainda podem manter algum teste de sistema ponta a ponta com serviços reais, mas normalmente reduzido a um smoke test final — e times com QA in Production madura podem até dispensar esse smoke test.

## Duas definições concorrentes de "teste de integração"

Fowler formaliza a distinção em duas categorias:

**Teste de integração estreito (narrow):**
- exercita só a fatia do código do serviço que fala com um serviço externo;
- usa dublês desse serviço externo, locais ou remotos;
- é, na prática, um conjunto de testes pequenos e numerosos — geralmente no mesmo escopo (e rodando no mesmo framework) que os testes unitários.

**Teste de integração amplo (broad):**
- exige instâncias reais e ativas de todos os serviços envolvidos;
- requer ambiente de teste substancial e acesso de rede;
- exercita caminhos de código através de todos os serviços, não só o trecho responsável pela integração em si.

Segundo o autor, boa parte da comunidade de desenvolvimento usa "teste de integração" só no sentido amplo, o que gera confusão constante ao conversar com quem pratica o estilo estreito. A recomendação de Fowler: quem só tem testes amplos deveria explorar o estilo estreito, já que ele tende a rodar muito mais rápido, sendo viável nos estágios iniciais de um pipeline de deploy e dando feedback mais cedo em caso de falha.

## A confusão fica pior: "unit test" também mudou de sentido

No fim dos anos 2010 surgiu mais uma camada de ambiguidade. Parte da comunidade passou a reservar o termo "teste unitário" só para o que Fowler chama de **teste unitário solitário** — aquele em que todo elemento do programa fora da unidade testada é substituído por um dublê. Com essa definição mais restrita, alguns autores passaram a chamar de "teste de integração" o que Fowler descreve como **teste unitário sociável** (que permite colaboração real entre objetos internos, sem dublês para tudo).

## Como Fowler resolve isso na própria escrita

Por causa dessa sobreposição de sentidos, Fowler adota convenções pessoais:
- para o que a maioria chama de teste de integração amplo, ele prefere os termos **"system test"** ou **"end-to-end test"**;
- para o teste de integração estreito, ele não tem um nome melhor e mantém "integration test", mas sempre qualificado como **"narrow"** para deixar claro o escopo;
- para "unit test", continua usando o termo para os dois casos, diferenciando com **"solitary"** / **"sociable"** quando a distinção importa.

## Metadados do artigo

- Publicado em 16 de janeiro de 2018; revisado em 3 de junho de 2021 (a revisão moveu a discussão sobre "teste de integração como sinônimo de teste unitário sociável" de uma nota de rodapé para o corpo principal do texto).
- Agradecimentos do autor a revisores internos da Thoughtworks: Birgitta Böckeler, Brian Oxley, Dave Rice, Deepti Mittal, Jonny Leroy, Kief Morris, Raimund Klein, Rogerio Chaves e Tiago Griffo.
- Termos correlatos cunhados/usados por Fowler no bliki: `TestDouble`, `ContractTest`, `DeploymentPipeline`, `UnitTest`.
