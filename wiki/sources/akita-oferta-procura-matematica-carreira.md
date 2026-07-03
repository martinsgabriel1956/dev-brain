---
type: source
title: "Oferta, Procura e Matemática Básica — Por Que Sua Carreira em Programação Vai Sofrer"
aliases: ["akita oferta e procura", "akita matematica carreira", "lei da oferta e procura programador"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_file: /home/nemomartins/Documentos/new/dev-study/raw/akita-oferta-procura-matematica-carreira.md
source_url: ""
author: "Fábio Akita"
date_published: ""
date_ingested: 2026-07-03
source_count: 0
tags: [carreira, ciclo-de-mercado, matematica, raciocinio, fundacao-tecnica, apego-a-ferramentas, seguranca, autodidata]
skill: tech-mentor-leadership
status: stable
---

## TL;DR

Mercado de programação é regido por lei de oferta e procura em ciclos de abundância e depressão — o ciclo de abundância de ~10 anos está terminando, e a oferta de programadores mal formados por cursos rápidos vai superar a demanda. O diferencial de valor não é a linguagem que você sabe, mas a capacidade de raciocínio matemático básico (testada com um exemplo real de juros compostos mal calculados no Twitter) e a ausência de apego a ferramentas específicas. Cursos que só ensinam a copiar comandos criam ilusão de aprendizado; fundação matemática é o que não envelhece.

## Key Claims

**Claim:** O mercado de programação segue ciclos de abundância e depressão regidos por oferta e procura, e o ciclo de abundância atual (~10 anos) está terminando.
**Evidence:** Comparação histórica: Visual Basic/Delphi/Java nos anos 90 → PHP/ASP/Flash na virada do século → Objective-C/Ruby/JavaScript uma década depois. Quem ficou preso a uma única ferramenta (ex. Visual Basic) perdeu sequencialmente as ondas da web, redes sociais, mobile e e-commerce. Cursos rápidos e abundantes aumentam a oferta de programadores mais rápido que a demanda cresce, derrubando o valor médio de cada profissional.
**Confidence:** média (é opinião/observação de mercado do autor, não estudo com dados formais)

**Claim:** A maioria dos programadores não sabe fazer contas básicas de juros compostos, e isso é sintoma direto de despreparo matemático generalizado na profissão.
**Evidence:** Caso real do Twitter: investidor calculou incorretamente 7 fundos × 0,5%/mês × 12 meses = 42% ao ano (deveria ser cálculo composto, resultando em ~6% ao ano bruto, ~1% líquido após inflação e taxas). Autor argumenta que o mesmo padrão de erro leva devs a aceitar propostas salariais de startup com números ilusórios.
**Confidence:** alta (o erro matemático em si é verificável; a generalização sobre a profissão é opinião)

**Claim:** Cursos baseados em tutoriais passo-a-passo ensinam a copiar e colar, não a raciocinar — e por isso não substituem fundação matemática/lógica sólida.
**Evidence:** Descrição do padrão de tutorial ("copia o comando, cola no terminal, cruza os dedos") como ensino de leitura e cópia, sem entender por que os comandos existem, que problema resolvem ou que alternativas existem. Contraste com a experiência do autor na faculdade, onde metade de um curso integral de 4 anos foi só matemática — conhecimento que só fez sentido ~15 anos depois, ao precisar entender complexidade de queries SQL (`SELECT LIKE`) e otimização de banco de dados.
**Confidence:** média (relato pessoal, não estudo controlado)

**Claim:** Apego a uma ferramenta específica (linguagem, framework) é sinal de perda de controle sobre a própria carreira, não de expertise.
**Evidence:** Metáfora do martelo e chave de fenda: "programador de verdade não tem lealdade a ferramentas e marcas". Quem só sabe usar uma ferramenta trata todo problema como se fosse o único tipo que ela resolve. Se em dez anos você ainda usa exatamente a mesma ferramenta de hoje, isso indica estagnação, não maestria.
**Confidence:** média (é heurística/opinião, não dado empírico)

**Claim:** Falhas básicas de segurança (senha em texto plano, credenciais no front-end) e falhas de performance (vazamento de memória) são detectáveis com raciocínio matemático/lógico simples, mas frequentemente ignoradas por resistência institucional.
**Evidence:** Caso relatado do projeto Vivo (~2002): teste de stress simples revelou que um framework proprietário nunca liberava memória (vazamento clássico), mas o alerta foi descartado por questões de hierarquia/certificação, resultando em reinícios de servidor a cada 30 minutos em produção. Citados também vazamentos reais no STF e Ministério da Saúde por senha em texto plano e credenciais expostas no JavaScript do front-end.
**Confidence:** alta para o padrão geral (senha em texto plano é falha básica documentada — ver [[password-hashing]]); relato específico do caso Vivo não é verificável externamente.

## Entities & Concepts Touched

- [[concepts/ciclo-de-mercado-tech]]
- [[concepts/raciocinio-matematico-aplicado]]
- [[concepts/apego-a-ferramentas]]
- [[concepts/autodidata]]
- [[concepts/aprendizado-passivo]]
- [[concepts/fundacao-tecnica]]
- [[concepts/password-hashing]]
- [[entities/fabio-akita]]

## Open Questions

- O autor não cita fonte formal para o "ciclo de ~10 anos" de mercado aquecido — é observação empírica pessoal. Existe algum dado de mercado (ex. relatórios de contratação tech) que sustente ou refute o timing específico desse ciclo?
- A relação causal entre "saber matemática básica" e "ser bom programador" é sugerida via anedota, mas nenhuma fonte no wiki até agora testa essa correlação de forma mais rigorosa — vale contrastar com [[wiki/sources/akita-como-aprender-programacao]], que enfatiza mais a postura autodidata do que conhecimento matemático per se.
