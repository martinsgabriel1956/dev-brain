---
type: concept
title: "Production Code"
aliases: ["código de produção", "código de produto"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 3
tags: [testes, xunit, terminologia, production-code, test-code]
skill: tech-mentor-testing
status: stub
---

# Production Code

Termo cunhado por [[wiki/entities/gerard-meszaros]] ([[wiki/sources/production-code-xunitpatterns]]) para nomear **todo código que não é código de teste** — o código que se escreve para embarcar num produto ou implantar em [[wiki/concepts/production|production]], o ambiente onde aplicações rodam em IT, agora também com fonte primária dedicada ([[wiki/sources/production-xunitpatterns]]). É o contraponto direto de [[wiki/concepts/test-code|test code]], que agora também tem fonte primária dedicada ([[wiki/sources/test-code-xunitpatterns]]): test code é "código escrito especificamente para testar outro código", seja esse outro código production code ou até outro test code.

## Por que o termo existe

Meszaros precisava de uma forma de distinguir o código de teste do código sendo testado. "Test code" era óbvio; "production code" tomou emprestado o nome do ambiente de produção, mesmo quando o código em questão ainda não foi de fato implantado — o critério é a **intenção** (ship/deploy), não o estado atual de deploy.

## Onde o termo aparece implicitamente na wiki

O par test code / production code é o pressuposto silencioso por trás de todo o vocabulário SUT/DOC documentado em [[wiki/concepts/test-doubles]] e [[wiki/concepts/indirect-input-output]]:

- **SUT** e **DOC** são sempre production code — nunca test code.
- A regra de design "control points/observation points exclusivos de teste não devem ser usados pelo production code" ([[wiki/sources/control-point-xunitpatterns]], [[wiki/sources/observation-point-xunitpatterns]]) só faz sentido com essa distinção nomeada: existem control/observation points que vazam para dentro do production code exatamente porque foram criados só para viabilizar teste — e isso é tratado como um risco de design, não preferência de estilo.
- [[wiki/sources/test-driven-development-xunitpatterns]] e [[wiki/sources/test-first-development-xunitpatterns]] usam "production code" para diferenciar TDD (production code feito funcionar um teste de cada vez, emergent design) de test-first development (production code apenas escrito depois do teste, sem essa implicação).

## Ver também

- [[wiki/concepts/production]] — a palavra-raiz da qual este termo deriva: o ambiente de execução em si, não o código
- [[wiki/concepts/test-code]] — contraponto formal do termo, agora com fonte primária própria
- [[wiki/concepts/test-doubles]] — SUT/DOC como instâncias de production code substituídas ou observadas durante o teste
- [[wiki/concepts/indirect-input-output]] — regra de design que depende da distinção test code / production code

## Key Sources

- [[wiki/sources/production-code-xunitpatterns]] — fonte primária dedicada ao termo; origem e definição formal
- [[wiki/sources/test-code-xunitpatterns]] — fonte primária do termo-irmão "test code", fechando o par terminológico completo
- [[wiki/sources/production-xunitpatterns]] — fonte primária isolada da palavra-raiz "production" (o ambiente), até agora só citada de passagem
