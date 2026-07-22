---
type: concept
title: "Os Seis Passos (Mock Interview)"
aliases: ["the six steps", "seis passos leetcode", "roteiro de entrevista simulada", "mock interview framework"]
date_created: 2026-07-22
date_updated: 2026-07-22
source_count: 1
tags: [entrevistas, coding-interview, carreira, pratica-deliberada, mock-interview]
skill: tech-mentor-leadership
status: draft
---

# Os Seis Passos (Mock Interview)

Framework de resolução de problemas criado por Anthony D. Mays, aplicado como um roteiro de **dez etapas práticas** para transformar a prática solo de LeetCode numa simulação fiel de [[wiki/concepts/entrevista-tecnica-coding|entrevista técnica de coding]]. A ideia central: o formato importa tanto quanto o conteúdo — resolver o problema certo do jeito errado (sozinho, sem cronômetro, olhando o enunciado completo) não treina o que a entrevista real avalia.

## As dez etapas

1. **Ferramenta de código sem IDE completa** — quadro branco, papel/caneta ou editor leve, para não depender de recursos (autocomplete, refactor automático) que não vão existir na entrevista real.
2. **Entrevistador simulado (recomendado) ou sozinho** — a pessoa não precisa ser técnica; o papel dela é observar postura, comunicação e dar feedback, não avaliar a solução em si.
3. **Cronômetro real** — simular os 45–60 minutos de uma entrevista real; parar quando o tempo acabar treina trabalhar sob restrição de tempo.
4. **Articular o problema de ouvido** — o candidato não pode olhar o enunciado escrito; precisa anotar enquanto ouve e repetir o problema com as próprias palavras, replicando a dinâmica de uma entrevista real onde a informação chega falada, não em texto completo.
5. **Perguntas e suposições** — perguntar sempre, mesmo sabendo a resposta, e reafirmar suposições implícitas em voz alta em vez de simplesmente agir sobre elas.
6. **Exemplos de entrada/saída como casos de teste** — reverter os exemplos dados para entender restrições, e criar exemplos próprios.
7. **Brainstorm com estimativa de Big-O antes de codar** — decidir o formato da solução ideal (é possível O(1)? O(log n)?) antes de escrever qualquer linha de código. Ver [[wiki/concepts/big-o]].
8. **Implementação rápida, narrada, sem pseudocódigo** — narrar a intenção antes de escrever cada trecho; a implementação deve ser a etapa mais rápida do processo.
9. **Teste contra checklist mental** — variável não declarada, off-by-one, condicional invertido, nome de variável ruim, null pointer — usando os exemplos já criados na etapa 6.
10. **Otimizar até o tempo acabar** — se a solução não é ótima, voltar ao brainstorm ou implementar a versão melhor já cogitada.

## Por que o roteiro existe

Cada etapa neutraliza uma diferença específica entre "resolver um problema de LeetCode sozinho" e "ser entrevistado por um humano": o enunciado que chega falado (não lido), o cronômetro real, a ausência de dicas/feedback automático, a obrigação de gerar os próprios exemplos e casos de teste. Praticar sem essas restrições treina uma habilidade diferente da que a entrevista real avalia.

## Diário de entrevistas simuladas

Documentar feedback após cada sessão — inclusive pontos não-técnicos (fala, silêncios, tiques) — e comparar a autoavaliação do candidato com a avaliação do entrevistador simulado (contratar / não contratar / em cima do muro). O objetivo é calibrar a percepção do próprio desempenho ao longo do tempo, não só acumular repetições.

## Relação com outros conceitos

- [[wiki/concepts/entrevista-tecnica-coding]] — o "porquê" (o que a entrevista de fato avalia); este conceito é o "como" (o roteiro concreto de prática)
- [[wiki/concepts/big-o]] — usado na etapa 7 para estimar a solução ideal antes de implementar
- [[wiki/concepts/reconhecimento-de-padroes]] — o repertório que sustenta um bom brainstorm na etapa 7
- [[wiki/concepts/aprendizado-por-luta]] — ficar travado durante o roteiro é esperado, não motivo para abandoná-lo

## Key sources

- [[wiki/sources/como-praticar-leetcode-da-forma-certa-anthony-mays]] — artigo original que detalha o framework completo em dez etapas
