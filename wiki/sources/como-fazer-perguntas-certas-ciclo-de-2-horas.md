---
type: source
title: "Como Fazer Perguntas Certas (e o Ciclo de 2 Horas)"
aliases: ["como fazer perguntas certas", "ciclo de 2 horas", "quando pedir ajuda"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 0
tags: [tech-mentor-leadership, perguntas, pedir-ajuda, junior, senior, comunicacao, produtividade, timeboxing, pair-programming, documentacao]
skill: tech-mentor-leadership
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/como-fazer-perguntas-certas-ciclo-de-2-horas.md
source_url: ""
author: "desconhecido (vídeo PT-BR de dev/líder técnico; canal não identificado)"
date_published: ""
date_ingested: 2026-09-29
---

# Como Fazer Perguntas Certas (e o Ciclo de 2 Horas)

## TL;DR

Vídeo PT-BR de um dev/líder técnico com uma regra prática de time: (1) **faça perguntas bem formuladas** — contexto, erro exato, o que já tentou — porque a pergunta vaga ("o app está dando erro, pode me ajudar?") rouba o tempo do sênior e cria má impressão ([[wiki/concepts/pergunta-bem-formulada]]); (2) **encontre o equilíbrio** entre nunca pedir ajuda e pedir demais ([[wiki/concepts/equilibrio-ao-pedir-ajuda]]); (3) use o **ciclo de 2 horas** — código parecido → documentação/IA → tentativa própria — e só então peça ajuda com contexto ([[wiki/concepts/ciclo-de-2-horas]]); (4) **documente** o que aprendeu.

## Key Claims

1. **A pergunta ruim custa o tempo de quem responde; a boa o respeita.** Exemplo contrastado: "o aplicativo está dando erro, pode me ajudar?" × "estou implementando o ticket 123 no app X, o erro é NullPointerException, já verifiquei se a variável está nula e não achei; você já viu algo assim?" Evidência: o apresentador destrincha os três elementos (contexto, erro exato, o que já tentou) e afirma que o sênior, assim, "provavelmente bota o olho no código e resolve". → [[wiki/concepts/pergunta-bem-formulada]]
2. **Vale também para suporte:** "está dando erro aqui" sem detalhes obriga o suporte a pedir informação e conectar no cliente; trazer tudo antes acelera a análise. → [[wiki/concepts/pergunta-bem-formulada]]
3. **Dois modos de falha simétricos.** *Nunca perguntar* (persiste dias, estoura deadline, sem update na daily) e *perguntar demais* (não pensa nem pesquisa, vira "fardo" para o time). O ponto ótimo é o meio da "gangorra"; o medo de "parecer incompetente" empurra para o extremo do silêncio. → [[wiki/concepts/equilibrio-ao-pedir-ajuda]]
4. **Ciclo de 2 horas:** 10–15 min de código próximo (pesquisa interna) → 5–10 min de documentação da empresa/linguagem ou IA → 30–70 min de tentativa própria; depois, pedir ajuda **com contexto**, sem passar de 2 h ("já é tarde demais"). → [[wiki/concepts/ciclo-de-2-horas]], [[wiki/concepts/documentacao-oficial-como-recurso]]
5. **Exceções que antecipam o pedido:** deadline urgente; júnior/novato com tarefa urgente atribuída pelo tech lead; trabalho em equipe/[[wiki/concepts/pair-programming]] (questiona-se a dupla o tempo todo). → [[wiki/concepts/ciclo-de-2-horas]]
6. **Documentar o que aprendeu** serve de referência para situações futuras, outras pessoas e "o eu do futuro". → [[wiki/concepts/documentar-conquistas]]
7. **Percepção importa:** perguntas mal feitas geram "uma percepção errada e ruim sobre você" — a regra é apresentada como cultura da empresa do autor ("vem dando muito certo"), sem dados. → [[wiki/concepts/equilibrio-ao-pedir-ajuda]]

## Entidades Mencionadas

- ChatGPT / OpenAI — citado como exemplo de IA para consulta na etapa 2 do ciclo (o apresentador diz "cada um tem a sua"). Sem página tocada; a fonte não avalia a ferramenta.
- Java (`NullPointerException`) — apenas exemplo do erro; sem página própria.

## Conceitos Tocados

Criados: [[wiki/concepts/pergunta-bem-formulada]], [[wiki/concepts/equilibrio-ao-pedir-ajuda]], [[wiki/concepts/ciclo-de-2-horas]].

Atualizados: [[wiki/concepts/debugar-antes-de-perguntar]], [[wiki/concepts/pair-programming]], [[wiki/concepts/mentoria-tecnica]], [[wiki/concepts/equipe-mista-senior-junior]], [[wiki/concepts/documentar-conquistas]], [[wiki/concepts/documentacao-oficial-como-recurso]], [[wiki/concepts/pomodoro]], [[wiki/concepts/debugging]], [[wiki/concepts/foco-profundo]], [[wiki/concepts/sindrome-do-impostor]], [[wiki/concepts/comunicacao-tecnica]], [[wiki/concepts/ia-ciclo-dependencia]].

## Open Questions

- **Aritmética do ciclo não fecha em 2 h:** 10–15 + 5–10 + 30–70 min somam 45–95 min; a fala também menciona "uma hora" de tentativa. As 2 h parecem um teto, não a soma das etapas (ou há folga não explicada). Interpretação minha (inferência).
- Os tempos (10–15, 5–10, 30–70 min, 2 h) são heurística pessoal de uma empresa, **sem evidência** empírica; o limite ideal provavelmente varia com senioridade, criticidade e o quão bloqueante é o problema — o próprio autor admite exceções.
- Tensão com [[wiki/concepts/debugar-antes-de-perguntar]]: aquela fonte defende resistir a perguntar para gerar aprendizado (risco de "proxy super conectado"); esta fixa um **limite de tempo** para não cair no extremo oposto. São complementares (o limite é o que falta na primeira), mas a segunda enfatiza o custo de prazo, não o de aprendizado.
- Em ambiente com baixa segurança psicológica, o medo de "parecer incompetente" não se resolve com regra individual — depende do time (ideia geral da skill de liderança, `references/psychological-safety.md` [skill: tech-mentor-leadership]; não dita na fonte).
- Nada sobre **como o sênior deve responder** (tom, tempo de resposta, canais assíncronos): a regra é toda do lado de quem pergunta.
- Não define "urgente" nem "novato/júnior"; a exceção pode virar brecha para o cenário 2.

## Raw Quotes

> "Uma pergunta ruim rouba muito o tempo do desenvolvedor sênior e uma pergunta boa respeita esse tempo."

> "O que toda empresa gosta é que você se mantenha estável, perfeito, que fique no meio."

> "Tu nunca tem que passar dessas 2 horas, porque já vai ser atrasado e tarde demais, e eles vão pensar que tu não consegue resolver o problema."

> "Documente tudo o que você aprendeu … o teu documento também vai servir para outras pessoas, até para o seu eu do futuro."
