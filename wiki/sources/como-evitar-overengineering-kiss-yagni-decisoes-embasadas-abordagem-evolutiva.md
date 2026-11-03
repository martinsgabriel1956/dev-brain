---
type: source
title: "Como Evitar o Overengineering: KISS, YAGNI, Decisões Embasadas e Abordagem Evolutiva"
aliases: ["como evitar overengineering", "como se blindar do overengineering", "pense grande comece pequeno", "empresa não é laboratório de testes"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/como-evitar-overengineering-kiss-yagni-decisoes-embasadas-abordagem-evolutiva.md
source_url: ""
author: "Não identificado (criador de conteúdo com canal, lives e blog; o nome não aparece na transcrição)"
date_published: ""
date_ingested: 2026-11-03
source_count: 0
tags: [over-engineering, kiss, yagni, hype, prova-de-conceito, mvp, cqrs, decisao-arquitetural, requisitos, tech-mentor-backend]
skill: tech-mentor-backend
status: stable
---

# Como Evitar o Overengineering: KISS, YAGNI, Decisões Embasadas e Abordagem Evolutiva

## TL;DR

Trecho de uma live ou vídeo mais longo sobre [[wiki/concepts/over-engineering]]. A transcrição começa e termina no meio da fala. O autor dá cinco defesas:

1. **[[wiki/concepts/kiss]]:** usar o martelo que já existe em vez de inventar uma supermáquina de bater prego.
2. **[[wiki/concepts/yagni]], com [[wiki/concepts/requisitos-funcionais-e-nao-funcionais|levantamento de requisitos]]:** só entra o que é requisito levantado e documentado.
3. **Razão em vez de empolgação:** a empresa não é seu laboratório ([[wiki/concepts/empresa-como-laboratorio-de-testes]]), e adotar algo exige conhecer bem o que se adota.
4. **Números:** [[wiki/concepts/prova-de-conceito|provas de conceito]] e métricas sustentam a decisão e a explicação ao gestor ([[wiki/concepts/decisao-tecnica-embasada-em-metricas]]).
5. **[[wiki/concepts/abordagem-evolutiva]]:** começar pequeno com [[wiki/concepts/mvp]] e evoluir conforme dados de uso.

Ele fecha respondendo a uma objeção do chat: produto que começou simples e virou bagunça não falhou por começar simples, e sim por ser mal mantido ([[wiki/concepts/refatoracao]]).

**Limite da fonte:** todos os argumentos vêm de experiência declarada. Não há caso nomeado nem dado medido. Os números citados (5 para 1.000 usuários, 10 s para 1 s) são exemplos do que uma justificativa deveria conter.

## Key Claims

| Claim | Evidência | Confiança |
|---|---|---|
| Não há por que implementar algo complexo sem necessidade; a solução consolidada basta | Analogia do martelo; converge com [[wiki/sources/kiss-yagni-entrega-rapida-qualidade]] e [[wiki/sources/underengineering-overengineering-mario-souto]] | Alta |
| Uma feature só se justifica se for requisito levantado e documentado, com certeza de agregar valor | Opinião do autor | Média-alta: documentar não prova valor, e por isso a fonte também pede validação em produtos novos |
| Implementar por suposição gasta recurso e tempo, e pode gerar retrabalho se a feature for usada de outro jeito | Raciocínio do autor, sem caso | Alta |
| Levantar requisitos é, no fundo, entender o negócio, e isso protege contra o excesso | Opinião do autor; converge com [[wiki/concepts/requisitos-funcionais-e-nao-funcionais]] | Alta |
| Testar tecnologia em projeto de produção por empolgação é "tiro no pé"; o teste na empresa acontece em PoC ou P&D | Opinião do autor, citando também o chat; converge com [[wiki/concepts/prova-de-conceito]] | Alta |
| Adotar tecnologia ou prática exige no mínimo conhecimento razoável e, na visão dele, profundo | O autor avisa que é polêmico. Sem evidência | Média: ver "Tensões com a wiki" |
| Antes de adotar cache, Mediator ou CQRS, é preciso saber vantagens, desvantagens, impacto de memória e processamento, e complexidade adicional | Lista de perguntas do autor; converge com [[wiki/sources/cqrs-quando-faz-sentido-cqs-bernardo-lobato]] | Alta |
| A análise completa junta dois eixos: negócio e parte técnica | Opinião do autor; converge com [[wiki/concepts/tradeoff-arquitetural]] | Alta |
| Decisão técnica deve se apoiar em números de testes e PoCs, não em estimativa imaginada | Princípio do autor; os exemplos numéricos são hipotéticos | Alta como princípio |
| Números permitem justificar custo adicional ao gestor | Diálogo ilustrativo do autor | Alta |
| Não é preciso antecipar problemas para gerar algo bom, porque muitos nem acontecem, ou não como imaginado | Opinião do autor; converge com [[wiki/concepts/yagni]] | Média-alta: inferência minha, problemas já conhecidos entram como requisito, não como antecipação |
| Empresa consolidada decide com levantamento de requisitos; negócio novo precisa validar o produto | Distinção do autor | Alta |
| MVP mais feedback substituem imaginação por dados na hora de escolher o caminho | Opinião do autor; converge com [[wiki/concepts/build-measure-learn]] | Alta |
| Ideias dão errado por não seguirem abordagem evolutiva, como um produto que levou um ano para sair e não atendia o público | Anedota sem caso nomeado; "muitas vezes" não mede frequência | Média |
| Quando um produto simples vira bagunça, o erro está na manutenção (falta de código limpo e SOLID), não no começo simples | Opinião do autor; "SOLID" é correção inferida de ASR | Média-alta |
| Refatorar algo simples para algo maior é muito mais fácil do que cortar partes de algo inflado | Afirmação sem dados; próxima de [[wiki/concepts/yagni]] e de [[wiki/sources/monolith-first-martin-fowler]] | Média |

## Tensões com a wiki

- **Começar simples vs. under-engineering.** [[wiki/sources/como-evitar-over-engineering-david-farley]] e [[wiki/sources/underengineering-overengineering-mario-souto]] dizem que falta de engenharia é mais comum que excesso. Não é contradição: esta fonte separa começar simples (escolha) de não cuidar da evolução (falha), o que se aproxima de [[wiki/concepts/under-engineering]].
- **Conhecimento profundo vs. PoC curta.** A fonte pede conhecimento profundo para adotar. [[wiki/concepts/prova-de-conceito]] descreve PoC de 1 a 3 dias. Inferência minha: as duas coisas se conciliam se a PoC for o meio de aprender, com a profundidade cobrada na hora de ir para produção. A fonte não diz qual profundidade basta.
- **Evoluir é mais fácil que cortar.** [[wiki/sources/monolith-first-martin-fowler]] registra um contra-argumento sobre microsserviços em substituições de sistema, onde as fronteiras já são mais conhecidas. A afirmação desta fonte é geral e não trata dessa exceção.

## Nota sobre Mediator e CQRS

O autor cita "Mediator junto com Command pattern e os handlers" ao falar de CQRS, sem dizer que um exige o outro. Essa combinação lembra o ecossistema .NET, mas a associação é inferência minha. `[external]` Milan Jovanović argumenta que CQRS e MediatR costumam ser confundidos e são coisas separadas ([Stop Conflating CQRS and MediatR](https://milanjovanovic.tech/blog/stop-conflating-cqrs-and-mediatr), visto só no resumo da busca). A wiki já registra que CQRS tem critérios próprios de adoção em [[wiki/concepts/cqrs]].

## Open Questions

- Quem é o autor e qual é o restante da live? O início da transcrição pressupõe partes anteriores sobre hype e requisitos. O post citado, "Pense Grande, Comece Pequeno", não foi encontrado em duas buscas, e o título é reconstruído de "pense e onde começa pequeno".
- Qual profundidade de conhecimento é suficiente para adotar uma tecnologia, e como obtê-la sem usar produção?
- Que métrica justificar quando o ganho é de manutenção, não de performance? Os exemplos da fonte só cobrem usuários e latência.

## Citações

> "a empresa, que paga para você resolver os problemas dela e não para você sair testando coisa"

> "O erro não foi em começar simples."

## Conexões

- [[wiki/concepts/over-engineering]]
- [[wiki/concepts/under-engineering]]
- [[wiki/concepts/kiss]]
- [[wiki/concepts/yagni]]
- [[wiki/concepts/mvp]]
- [[wiki/concepts/prova-de-conceito]]
- [[wiki/concepts/avaliar-hype-tecnologico]]
- [[wiki/concepts/requisitos-funcionais-e-nao-funcionais]]
- [[wiki/concepts/cqrs]]
- [[wiki/concepts/mediator-pattern]]
- [[wiki/concepts/refatoracao]]
- [[wiki/concepts/comecar-simples-adicionar-peca-quando-doer]]
- [[wiki/concepts/abordagem-evolutiva]]
- [[wiki/concepts/decisao-tecnica-embasada-em-metricas]]
- [[wiki/concepts/empresa-como-laboratorio-de-testes]]
