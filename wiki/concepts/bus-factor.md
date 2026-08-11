---
type: concept
title: "Bus Factor (Dev Gandalf)"
aliases: ["bus factor", "truck factor", "dev gandalf", "fator ônibus", "conhecimento concentrado"]
date_created: 2026-08-10
date_updated: 2026-08-11
source_count: 3
tags: [engineering-management, risco, conhecimento, documentação, onboarding, liderança, processo]
skill: tech-mentor-leadership
status: stub
---

# Bus Factor (Dev Gandalf)

Número de pessoas de um time que precisariam ser "atropeladas por um ônibus" (sair, adoecer, ser promovidas) para que um conhecimento crítico se perdesse. **Bus factor = 1** significa que uma única pessoa detém o conhecimento de como determinada parte do sistema funciona — um ponto único de falha organizacional.

## O "Dev Gandalf"

[[wiki/sources/por-que-code-bases-degradam-estrategias-code-rot]] apelida essa pessoa de **"Dev Gandalf"**: o engenheiro que está na empresa há ~10 anos e é o único que sabe como certa parte funciona. Ponto central da fonte: o Gandalf é **extremamente valioso e não deve ser demitido — mas é sintoma, não causa**. Ele é evidência de um código que não pode ser modificado facilmente e de conhecimento que nunca foi externalizado. Enquanto o conhecimento vive só na cabeça dele, a code base permanece frágil.

## Como reduzir o bus factor

A fonte propõe mover o conhecimento *para perto do código*, aliviando a dependência do Gandalf:

- **Testes como documentação** de regras de negócio (ver [[wiki/concepts/living-documentation]]).
- **[[wiki/concepts/adr-architecture-decision-record|ADRs]]** e comentários explicando o *porquê* de decisões não usuais.
- **Code owners** com as partes externas de cada módulo documentadas (APIs, pontos de conexão).

Conecta com [[wiki/concepts/entropia-de-software]]: quanto mais caótica a base, mais o conhecimento tácito de um Gandalf vira a única cola que a mantém evoluindo.

## Bus Factor Explica Por Que a Empresa Grande Rejeita Accountability Individual

[[wiki/sources/code-review-morreu-uncle-bob-push-force-prod-lucas-montano]] usa o bus factor para explicar uma tensão sobre o futuro do [[wiki/concepts/code-review|code review]]: responsabilizar cada dev individualmente pelo que coloca em produção ("fez o merge, deu merda, o culpado é você") funciona em empresa de porte médio, mas **empresa grande recusa esse modelo justamente porque ele aumenta o bus factor** — se só um dev entende o que colocou em prod, o sistema fica na mão dele e ele deixa de ser substituível. A grande empresa prefere **processos** (e review como um deles) a heróis individuais, priorizando substituibilidade sobre velocidade individual. É o outro lado da moeda do "Dev Gandalf": aqui o bus factor não é só um risco a mitigar, é o critério pelo qual a organização decide *quanta* autonomia individual tolera.

## Por Que o Rebase-Flow Centralizado Não Escala

[[wiki/sources/git-flow-farsa-solucao-maturidade-rebase-lucas-montano]] chega ao bus factor pelo lado do **processo de Git**. O fluxo de integração por [[wiki/concepts/rebase-vs-merge|rebase]] que [[wiki/entities/lucas-montano]] defende para times pequenos depende de **ownership centralizado** — uma pessoa madura e atenta cuidando dos merges/rebases (que reescrevem branches e resolvem conflitos commit a commit). Isso é bus factor = 1 por construção: excelente enquanto o time é pequeno, mas em time grande "centralizar o merge vira uma loucura" e concentra risco/conhecimento numa pessoa. É por isso que ele conclui que o rebase-flow **não escala** — a mesma lógica pela qual a empresa grande prefere processos distribuídos a heróis (ver seção acima). Ver [[wiki/concepts/trunk-based-development]].

## Key Sources

- [[wiki/sources/por-que-code-bases-degradam-estrategias-code-rot]] — o "Dev Gandalf" como sintoma de código não-modificável e conhecimento não-documentado
- [[wiki/sources/code-review-morreu-uncle-bob-push-force-prod-lucas-montano]] — bus factor como razão pela qual a empresa grande prefere processos/substituibilidade a accountability individual
- [[wiki/sources/git-flow-farsa-solucao-maturidade-rebase-lucas-montano]] — ownership centralizado do rebase-flow como bus factor = 1 que impede escalar para times grandes
