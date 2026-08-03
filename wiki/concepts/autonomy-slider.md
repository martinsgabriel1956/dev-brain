---
type: concept
title: "Autonomy Slider (Karpathy)"
aliases: ["autonomy slider", "controle de autonomia da ia", "slider de autonomia"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
tags: [andrej-karpathy, agentes-ia, vibe-coding, delegacao, niveis-adocao-ia]
skill: tech-mentor-ai
status: stub
---

# Autonomy Slider (Karpathy)

Framework atribuído a [[wiki/entities/andrej-karpathy]] em [[wiki/sources/cinco-escolas-programacao-com-ia]]: uma metáfora de **controle deslizante contínuo** (como o volume de um rádio) para o quanto de autonomia/"rédea" se delega a um agente de IA em uma tarefa de código.

- **Volume no mínimo** — a IA apenas sugere ("dá uma tossidinha de solução"); quem implementa é o humano. Corresponde à Escola 1 (copiloto) descrita na fonte.
- **Volume no máximo** — "faz o que você quiser"; o agente decide e executa sozinho, sem checkpoint humano por etapa. Corresponde à Escola 4 (loop sem supervisão) descrita na fonte.

## A Ideia Central: Não Existe Posição "Certa" no Slider

O ponto do framework não é prescrever onde o slider deve ficar — é que **cada abordagem de programação com IA é simplesmente uma posição diferente nesse controle**, e a escolha depende da tarefa, do risco e do contexto, não de uma verdade única. [[wiki/sources/cinco-escolas-programacao-com-ia]] usa esse framework para organizar cinco "escolas" de pensamento observadas na comunidade (copiloto, delegação total/spec-driven, "na unha" sem IA, e loop sem supervisão) como pontos ao longo do mesmo eixo, em vez de posições incompatíveis.

## Frase-Chave Atribuída a Karpathy

> "Você até consegue terceirizar o seu pensamento; agora, o seu entendimento, isso não dá para passar pra frente."

O entendimento (a teoria mental de como e por que o sistema funciona) não escala com o slider — mesmo delegando toda a execução, quem não constrói esse entendimento paga o preço depois. Ideia diretamente paralela à de [[wiki/concepts/teoria-do-programa-naur]] (Peter Naur, 1985): o código é resíduo, a teoria vive na cabeça de quem construiu.

## Relação com Outros Frameworks de Autonomia

- [[wiki/concepts/niveis-adocao-ia-l0-l4]] — outro framework que tenta categorizar posições de adoção de IA, mas em níveis discretos (L0-L4/L7) em vez de um slider contínuo; eixos diferentes, mesmo problema de fundo (quanto delegar).
- [[wiki/concepts/human-in-the-loop]] — descreve granularidades específicas de intervenção humana (por tool call, por plano, por etapa) que, na prática, são pontos concretos no slider de Karpathy.
- [[wiki/concepts/vibe-coding]] — volume "no talo" sem critério de qualidade é, na prática, a definição de vibe coding; volume "no talo" **com** critério é o que [[wiki/entities/antirez]] batizou de "automatic programming" na mesma fonte.

## Key Sources

- [[wiki/sources/cinco-escolas-programacao-com-ia]]
