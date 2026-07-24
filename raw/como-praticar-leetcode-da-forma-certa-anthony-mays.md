---
title: "Como Praticar Questões de LeetCode (Do Jeito Certo)"
source_type: article
language: pt-BR
translated: true
author: "Anthony D. Mays"
source_url: "https://medium.com/@anthonydmays/how-to-practice-leetcode-questions-the-right-way-4f9735cf06c6"
date_published: "2022-05-10"
---

## Sobre a fonte

Artigo de 2022 de Anthony D. Mays, ex-engenheiro de software do Google e hoje coach de carreira e entrevistas. É o artigo original citado no vídeo já ingerido nesta wiki ([[wiki/sources/leetcode-como-se-preparar-entrevistas-coding-anthony-mays]]), no qual o autor detalha o framework que só havia sido resumido no vídeo: "Os Seis Passos" (na prática, um roteiro de dez etapas de entrevista simulada).

## Tese central

Quem pratica LeetCode e sente que não evolui nas entrevistas reais provavelmente não tem um problema de inteligência ou esforço — tem um problema de **método**. Praticar muitas questões com a estratégia errada não ajuda, independente da fonte das questões (Blind 75, Cracking the Coding Interview, etc.). Analogia usada: assim como na musculação, forma e técnica importam mais que volume.

## Por que a entrevista real é diferente de resolver sozinho

Entrevista técnica é um exercício **colaborativo** de resolução de problemas, não uma prova solo. Diferenças-chave listadas pelo autor:

- No LeetCode o enunciado, exemplos e restrições vêm completos de uma vez; numa entrevista real o entrevistador segura informação de propósito, para observar como o candidato lida com ambiguidade e se ele pergunta.
- LeetCode não dá dicas nem feedback sobre se a abordagem está no caminho certo; um entrevistador dá, e o candidato é avaliado por como reage a esse feedback.
- O entrevistador não é obrigado a fornecer exemplos ou casos de teste — quem só treinou com eles prontos tem dificuldade em criá-los sob pressão.

## "Os Seis Passos" — o framework, aplicado em 10 etapas práticas

1. **Ferramenta de código**: usar quadro branco, papel/caneta ou editor leve (nunca uma IDE completa) — para não depender de recursos que não existem numa entrevista real.
2. **Entrevistador simulado (fortemente recomendado) ou sozinho**: a pessoa não precisa ser técnica — o autor usou a própria esposa, não-técnica, para dar feedback de postura e presença. Praticar sozinho exige autodisciplina para não se dar mais liberdade do que uma entrevista real daria.
3. **Cronômetro**: simular o tempo real (45–60 min); parar quando o tempo acabar. Para quem está no início, pode-se só medir o tempo sem cortar, como baseline.
4. **Articular o problema**: o entrevistador simulado lê a questão em voz alta; o candidato não pode olhar o enunciado, só anotar e depois repetir o problema com as próprias palavras para confirmar entendimento.
5. **Perguntas e suposições**: sempre perguntar, mesmo já sabendo a resposta — tipo de dado, limites, se cabe em memória, se pode vir dado inválido, se a entrada já vem ordenada. Reafirmar suposições implícitas em voz alta (ex.: assumir inteiro de 32 bits) em vez de simplesmente agir sobre elas.
6. **Exemplos de entrada/saída**: fazer engenharia reversa dos exemplos dados (o que eles revelam sobre restrições) e criar exemplos próprios — tratados como casos de teste; ligação sugerida com TDD.
7. **Brainstorm de soluções + estimativa de Big-O**: estimar o formato da solução ótima *antes* de codar (ex.: é possível O(1)? O(log n)?); gerar 2–3 soluções viáveis, aceitando que a primeira costuma ser força bruta; dois princípios citados — trocar espaço por velocidade, e estruturas novas costumam ser combinação de duas estruturas existentes. É válido perguntar ao entrevistador qual solução ele prefere ver implementada.
8. **Implementação**: deve ser a parte mais fácil e mais rápida — se não for, é sinal de que falta prática de escrita de código. Nunca pseudocódigo (não conta em entrevista real). Dicas: narrar a intenção antes de escrever cada trecho, usar nomes de variável verbosos e legíveis, e usar idiomas/APIs da linguagem sabendo o custo real por trás delas (ex.: `sort()` custa O(n log n) ou O(n²) dependendo da linguagem, não é mágica).
9. **Testar o código**: percorrer linha a linha contra uma checklist mental (variável não declarada, off-by-one, condicional invertido, nome ruim, null pointer) usando os exemplos já criados no passo 6.
10. **Otimizar**: se ainda não é a solução ótima, voltar ao brainstorm ou implementar a versão melhor já pensada — até o tempo acabar.

## Encerramento e diário de prep

Documentar feedback após cada sessão — o próprio autor mantém até hoje seu diário de entrevistas simuladas. Duas perguntas centrais para calibrar autoavaliação: como você avalia seu desempenho, e como o entrevistador avaliaria (contratar / não contratar / em cima do muro) — o objetivo é checar se as duas percepções convergem. Feedback não-técnico também importa (gagueira, silêncios longos, tiques) porque comunicação é metade do desafio da entrevista.

## Frases originais (citações pontuais)

> "You're probably practicing wrong."

> "Technical interviewing is a collaborative problem-solving exercise."

> "Measure twice, cut once." (citado pelo autor sobre por que a implementação deve ser rápida)
