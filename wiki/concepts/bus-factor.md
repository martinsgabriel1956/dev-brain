---
type: concept
title: "Bus Factor (Dev Gandalf)"
aliases: ["bus factor", "truck factor", "dev gandalf", "fator ônibus", "conhecimento concentrado"]
date_created: 2026-08-10
date_updated: 2026-08-10
source_count: 1
tags: [engineering-management, risco, conhecimento, documentação, onboarding, liderança]
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

## Key Sources

- [[wiki/sources/por-que-code-bases-degradam-estrategias-code-rot]] — o "Dev Gandalf" como sintoma de código não-modificável e conhecimento não-documentado
