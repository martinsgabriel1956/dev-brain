---
type: concept
title: "Entrevista Técnica de Coding"
aliases: ["coding interview", "entrevista estilo leetcode", "live coding interview", "whiteboard interview"]
date_created: 2026-07-20
date_updated: 2026-07-22
source_count: 3
tags: [carreira, entrevistas, coding-interview, algoritmos, comunicacao]
skill: tech-mentor-leadership
status: draft
---

# Entrevista Técnica de Coding

Formato de entrevista (estilo [[wiki/concepts/algoritmos-e-estruturas-de-dados|LeetCode]]) em que um candidato resolve um problema de algoritmo ao vivo, na frente de um entrevistador. O erro mais comum é tratá-la como uma versão cronometrada de praticar sozinho na plataforma — na prática, o que está sendo avaliado é outra coisa: processo de raciocínio, comunicação e capacidade de extrair informação, não só chegar à resposta certa.

## A diferença entre praticar sozinho e ser entrevistado

No LeetCode, o candidato recebe o enunciado completo, exemplos e dicas de uma vez. Numa entrevista real, o entrevistador **não entrega tudo de bandeja** — o candidato precisa saber pedir o que falta. O entrevistador está disposto a fornecer contexto adicional, mas só quando solicitado; ele não antecipa o trabalho que é do candidato.

**Sinal de alerta clássico de reprovação:** começar a digitar código imediatamente após ouvir o problema, sem fazer perguntas de esclarecimento antes. Normalmente indica solução incompleta por falta de informação reunida previamente.

## Por que resposta certa não é suficiente

Um entrevistador quer entender **como** o candidato pensa e se comunica, principalmente quando ele trava. Se o candidato já conhece a resposta de cara, isso não gera sinal nenhum sobre o processo — o entrevistador tende a aumentar a dificuldade ou trocar de pergunta até encontrar o limite real do candidato. Ficar travado (stuck) é esperado e faz parte do que está sendo avaliado — evitar isso a todo custo é sinal de despreparo, não de competência.

## Memorizar padrão, não problema

Entrevistadores evitam usar problemas prontos de plataformas justamente porque um candidato pode já ter memorizado a solução exata, o que não prova capacidade de resolver problemas novos. A recomendação é memorizar o **padrão** (ver [[wiki/concepts/reconhecimento-de-padroes]]), não a solução específica — é possível fazer centenas de problemas e continuar sem evoluir a capacidade real de resolver problemas, se o foco for memorização em vez de reconhecimento de padrão.

## Fazer perguntas é trabalho do candidato

Praticar muitos problemas ajuda a desenvolver a intuição de quais perguntas fazer. Estudar [[wiki/concepts/algoritmos-e-estruturas-de-dados|algoritmos, estruturas de dados]] e [[wiki/concepts/big-o|Big O]] serve, na prática de entrevista, para saber quais perguntas filtram ferramentas que não se aplicam à situação — ex.: perguntar se o input já está ordenado permite descartar algoritmos de ordenação do conjunto de opções.

Se houver mais de uma solução possível, é válido perguntar ao entrevistador qual ele prefere — evita gastar tempo implementando algo que os dois já sabem que não é ideal. Só implementar a solução ingênua (naive) de primeira sem cogitar alternativas é desperdiçar esse sinal.

## O roteiro de prática: "Os Seis Passos"

O artigo original do mesmo autor (fonte primária do vídeo já citado acima) detalha o framework prático completo por trás do conselho "pratique com outra pessoa": um roteiro de dez etapas de entrevista simulada — cronômetro real, ouvir o problema sem olhar o enunciado, perguntar e reafirmar suposições, estimar Big-O antes de codar, implementar sem pseudocódigo, testar contra uma checklist mental. Ver [[wiki/concepts/seis-passos-mock-interview]] para o detalhamento completo.

## Relação com outros conceitos

- [[wiki/concepts/seis-passos-mock-interview]] — o roteiro concreto de prática que operacionaliza os princípios acima
- [[wiki/concepts/reconhecimento-de-padroes]] — o mecanismo cognitivo por trás de "memorize o padrão, não o problema"
- [[wiki/concepts/algoritmos-e-estruturas-de-dados]] — fundamento que sustenta as perguntas certas a fazer
- [[wiki/concepts/big-o]] — usado para filtrar abordagens via perguntas de esclarecimento
- [[wiki/concepts/comunicacao-tecnica]] — verbalizar raciocínio é parte avaliada, não incidental
- [[wiki/concepts/aprendizado-por-luta]] — ficar travado é sinal esperado, não fracasso
- [[wiki/concepts/entrevista-system-design]] — mesma estrutura de "levar o candidato a dizer 'não sei'", em formato de arquitetura em vez de algoritmo

## Key sources

- [[wiki/sources/leetcode-como-se-preparar-entrevistas-coding-anthony-mays]]
- [[wiki/sources/como-praticar-leetcode-da-forma-certa-anthony-mays]] — artigo original com o roteiro completo de dez etapas ("Os Seis Passos")
- [[wiki/sources/5-dicas-entrevistas-lousa-branca-system-design]]
