---
type: concept
title: "Dependência de IA"
aliases: ["ai dependency", "dependência ferramenta", "loop de prompts"]
date_created: 2026-05-31
date_updated: 2026-08-10
source_count: 4
tags: [dependencia-ia, ia-e-programacao, aprendizado-passivo, autonomia-tecnica, iniciante]
skill: tech-mentor-leadership
status: stable
---

# Dependência de IA

## TL;DR

Condição em que o desenvolvedor só consegue avançar pedindo à IA — sem conseguir raciocinar, depurar ou modificar código de forma autônoma. Diferente do uso produtivo da IA como tutora ou revisora. Construída gradualmente através do [[aprendizado-passivo]] e do ciclo preguiçoso.

## O Ciclo que Cria Dependência

```
1. Pede o código à IA
2. IA gera
3. Copia sem entender
4. Roda
5. Se funcionou → vai para a próxima feature (sem entender)
6. Se não funcionou → pede outro código (sem tentar entender o erro)
7. Repete indefinidamente
```

A cada volta do ciclo, o desenvolvedor constrói menos raciocínio e mais dependência.

## Como Reconhecer

- Não consegue explicar o código que gerou
- Qualquer bug exige um novo prompt (não sabe investigar)
- Não sabe se precisa corrigir uma linha, reescrever o módulo ou recomeçar do zero
- Portfólio com projetos que não consegue defender em entrevista
- A produtividade vai a zero quando a IA fica indisponível ou responde errado

## Diferença: Dependência vs. Uso Produtivo

| Dependência | Uso Produtivo |
|------------|---------------|
| IA faz o raciocínio | IA apoia o raciocínio |
| Pede antes de tentar | Tenta, depois pede |
| Aceita a resposta sem checar | Verifica, questiona, adapta |
| Não sabe explicar o que gerou | Consegue explicar cada parte |
| Loop de prompts para cada bug | Usa IA para entender o erro, não para apagar |

## Por que é Diferente de Usar Bem a IA

Usar IA como tutora é o oposto da dependência:
- Pedir explicação de conceito → ativo, não cria dependência
- Pedir analogias para entender melhor → ativo
- Tentar resolver, pedir correção, pedir explicação das mudanças → ativo

O marcador central: **você ainda está no centro do raciocínio?**

## Código Não Dominado Vira Retrabalho

> "Toda vez que alguma coisa quebrar você vai gastar mais e mais tokens para solucionar porque você não sabe mexer, não sabe se precisa refazer tudo ou tentar outra abordagem."

Dependência de IA é auto-amplificante: quanto menos você entende, mais tokens precisa para cada problema, mais depende da ferramenta.

## Relação com [[autonomia-tecnica]]

Dependência de IA é o antônimo direto de autonomia técnica. Quem depende da IA:
- Não consegue trabalhar em ambientes sem acesso à IA
- Não passa na pergunta "explica o que você fez" de uma entrevista
- Não consegue contribuir de forma independente em um time

## Relação com [[token-anxiety]]

Há uma sobreposição: [[token-anxiety]] é a ansiedade de não desperdiçar tokens disponíveis. Dependência de IA cria um loop similar — sempre precisando do próximo prompt, sempre preocupado em não "acabar" o acesso.

## Localização na Escala de Maturidade

Na [[escala-maturidade-ia-dev]], os níveis 0–2 são a zona onde o risco de dependência é maior — a IA não mudou fundamentalmente a forma de trabalhar, e o desenvolvedor ainda faz 100% do raciocínio (ou delega o raciocínio sem construir o próprio). A transição para o nível 4 (Diretor) é o ponto onde a relação se inverte: você especifica o comportamento e valida — em vez de copiar e aceitar.

## Caso de Uso na Fronteira: Revisar o Próprio Código com IA Antes do PR

Pedir para uma IA revisar/sugerir melhorias no próprio código antes de abrir um [[wiki/concepts/code-review]] é uso produtivo **somente se** vier acompanhado de pedir explicação do "porquê" de cada mudança sugerida. Aceitar as sugestões sem entendê-las transforma uma prática potencialmente boa em dependência disfarçada — o risco reaparece mais tarde, num teste técnico sem acesso à ferramenta.

## Key Sources

- [[wiki/sources/ia-e-aprendizado-programacao-iniciantes]]
- [[wiki/sources/escala-niveis-uso-ia-engenheiros]] — níveis 0–2 como zona de estagnação e dependência
- [[wiki/sources/como-nao-ser-humilhado-no-primeiro-code-review]] — revisar código com IA antes do PR só funciona se vier com "por que" explicado
- [[wiki/sources/como-usar-ia-para-aprender-programacao-sem-atrofiar]] — IA como "muleta" para fugir da dificuldade → [[wiki/concepts/atrofia-cognitiva]]; contraste com IA que *cria* dificuldade calibrada
