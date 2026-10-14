---
type: concept
title: "Provar que Corrigiu"
aliases: ["debug não é prova", "mesmo teste antes e depois", "acho que corrigi"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [bugs, testes, evidencia, senioridade, confianca, teste-unitario]
skill: tech-mentor-testing
status: draft
---

# Provar que Corrigiu

Passo 3 de [[wiki/concepts/tres-passos-para-lidar-com-bug]]. Pergunta-teste de [[wiki/entities/andre-casciotti]]: "corrigiu, ou você *acha* que corrigiu?". Prova traz **segurança real** ao dev, ao time e ao gestor e sinaliza senioridade; não garante 100%, mas reduz a recorrência.

- **Debug não é prova**: passar pelo ponto sem exception não mostra o que o usuário vê. Debug **diagnostica**; a prova é o resultado final observável.
- **Dinâmica**: com a [[wiki/concepts/evidenciar-o-problema|evidência]], rode o teste e veja o erro; corrija; rode **exatamente o mesmo teste**; se não erra mais, está provado.
- **Teste unitário** quando possível: só para a alteração, não 300 testes; é prova empírica e repetível (30 execuções, mesmo resultado) e quebra se a entrada/saída mudar. Ver [[wiki/concepts/tdd]], [[wiki/sources/test-driven-bug-fixing-xunitpatterns]].
- Depois da prova, a [[wiki/concepts/analise-de-impacto-da-correcao]].
- **Desculpas típicas**: "não tenho acesso em produção", "só testo lá". O custo do erro é reputação e transtorno ao negócio (ex. preço errado em produção).

Liga a [[wiki/concepts/plano-de-testes-escrito]] (roteiro), [[wiki/concepts/inseguranca-na-entrega]] e [[wiki/concepts/testar-proprio-codigo]]. Ressalva: a prova cobre só o cenário reproduzido; o fluxo todo continua a precisar de olhar macro.

## Key Sources

- [[wiki/sources/como-sair-do-ciclo-de-bugs-e-retrabalho-andre-casciotti]]
