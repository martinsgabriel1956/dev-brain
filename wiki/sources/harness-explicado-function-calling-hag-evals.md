---
type: source
title: "Harness Explicado: Function Calling, HAG (RAG Interno) e Evals"
aliases: ["hardness", "harness ultra simplória", "você é o harness"]
date_created: 2026-08-13
date_updated: 2026-08-13
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/harness-explicado-function-calling-hag-evals.md
source_url: ""
author: "não identificado (autor de canal de programação, menciona cursos próprios de DSA/LeetCode, roadmap de entrevistas e system design)"
date_published: ""
date_ingested: 2026-08-13
source_count: 0
tags: [harness, tool-call, function-calling, rag, hag, evals, llm-as-judge, openai, prompt-engineering, demo-codigo]
skill: tech-mentor-ai
status: stable
---

## TL;DR

Vídeo de resposta/comparação a um conteúdo anterior sobre harness (do autor "Téo/tio", que "venceu na corrida" em publicar primeiro), desmistificando o termo através de duas frentes: (1) um relato pessoal de ter construído, numa empresa anterior, um sistema RAG/HAG (chunking → vector DB → busca KNN/BM25 → prompt restrito aos documentos → avaliação de fidelidade por outra IA) antes mesmo do termo "harness" existir, argumentando que aquele sistema já era uma harness na prática; e (2) uma demonstração ao vivo de uma harness mínima em Python (~1 arquivo, API da OpenAI, uma única tool `run`/bash), mostrando o ciclo completo de tool call — usuário pergunta, modelo pede `ls`/`sed`, harness executa localmente, resultado volta ao contexto, modelo responde. Fecha com uma tríade proposta para sistemas de IA bem construídos: código determinístico + prompts + avaliação de qualidade (LLM-as-judge + custo em tokens).

## Key Claims

**Claim:** Um sistema RAG corporativo construído antes do termo "harness" popularizar — chunking de documentos, indexação em vector database, busca por similaridade via KNN ou BM25, injeção dos top-k chunks no prompt com system prompt restringindo a resposta apenas ao conteúdo fornecido, e avaliação posterior da resposta por outra IA (framework tipo Evals da OpenAI) medindo fidelidade aos documentos — já era, na essência, uma harness.
**Evidence:** Relato de experiência pessoal do autor (sem link, sem nome da empresa). Consistente com a definição de [[wiki/concepts/harness]] já registrada na wiki (código determinístico + orquestração de prompts em ciclo) e com o pipeline documentado em [[wiki/sources/rag-retrieval]] (chunking → embedding → vector store → busca → prompt + LLM) e em [[wiki/sources/evals-sistematicas]] (LLM-as-judge, faithfulness). O ponto original desta fonte não é o pipeline em si (já bem coberto na wiki), mas o enquadramento retroativo: "harness" é um nome novo para uma prática de engenharia que já existia.
**Confidence:** alta como relato pessoal coerente com a literatura já presente na wiki; sem forma de verificar detalhes específicos (nome da empresa, métricas exatas).

**Claim:** Antes do function calling nativo existir na Anthropic, o workaround usado para conseguir tool calls era pedir ao modelo que respondesse usando tags XML para sinalizar a chamada de função — funcionava ~99% das vezes, com retry cobrindo o restante.
**Evidence:** Relato histórico do autor sobre sua própria experiência de engenharia, sem data ou link específico. É uma claim nova para a wiki — nenhuma fonte anterior documentava o mecanismo de transição (XML tags como ponte) entre "function calling só existe na OpenAI" e "function calling nativo em todo provider".
**Confidence:** média — plausível tecnicamente (tags XML como delimitador parseável é uma técnica de prompt engineering bem estabelecida) e consistente com a cronologia já registrada em [[wiki/concepts/tool-call]] ("mecanismo introduzido pela OpenAI em 2023"), mas sem confirmação de fonte primária da Anthropic sobre quando o function calling nativo chegou.

**Claim:** Uma harness mínima e funcional pode ser construída em um único arquivo Python: chave de API, system prompt, lista de tools (uma tool `run`/bash), e um loop `while True` que alterna entre resposta do usuário e do modelo, executando localmente qualquer `function_call` retornada e reenviando o resultado ao contexto até obter um `output_text` final.
**Evidence:** Demonstração ao vivo do autor, com três testes de comportamento observado: "hi" (sem tool call, resposta direta), "what files are in this directory?" (tool call `run bash ls`, resposta correta com base no resultado real do comando) e "what is harness.py?" (tool call de leitura do próprio arquivo via `sed`, resposta descrevendo corretamente o conteúdo lido). Consistente ponto a ponto com o ciclo documentado em [[wiki/concepts/tool-call]] ("Como Funciona", passos 1-5) e com a analogia de syscall já registrada na mesma página.
**Confidence:** alta — é uma demonstração de código ao vivo com resultado observável, não uma alegação de terceiros; o mecanismo é o mesmo já documentado com mais detalhe em outras fontes da wiki, aqui reduzido ao esqueleto mínimo.

**Claim:** Skills não dão "superpoder" ao modelo — apenas adicionam mais texto ao prompt enviado a cada chamada.
**Evidence:** Argumento do autor em resposta a uma objeção antecipada do público. Consistente com a definição de [[wiki/concepts/harness]] ("tudo que entra e sai do data center é texto") e com a distinção já registrada entre "provider harness" e "user harness" na mesma página — skills fazem parte do "user harness" mas continuam sendo, mecanicamente, texto adicionado ao contexto, não uma capacidade nova do modelo.
**Confidence:** alta — reforça (sem adicionar dado novo) um princípio já bem estabelecido na wiki.

**Claim:** Um sistema de IA bem construído precisa de três camadas, não apenas duas: código determinístico, prompts, e avaliação sistemática de qualidade (LLM-as-judge medindo fidelidade + medição de custo em tokens por modelo, permitindo comparar qual modelo é melhor para qual tipo de tarefa).
**Evidence:** Síntese do autor a partir da própria experiência (2024-2025) construindo o sistema RAG/HAG descrito acima. O item "avaliação" já está coberto em profundidade por [[wiki/sources/evals-sistematicas]] (pipeline de 3 níveis: offline/online/CI, LLM-as-judge com biases conhecidos, RAGAS). Esta fonte não adiciona técnica nova, mas reforça a avaliação como componente obrigatório (não opcional) de um sistema de produção, vindo de experiência prática e não de documentação de ferramenta.
**Confidence:** média-alta — afirmação de princípio bem alinhada com o resto da wiki, mas sem dado quantitativo novo (não há número de score, taxa de fidelidade ou economia de custo citado nesta fonte especificamente).

## Entities & Concepts Touched

- [[wiki/concepts/harness]]
- [[wiki/concepts/tool-call]]
- [[wiki/concepts/prompt-engineering]]
- [[wiki/entities/openai]]
- [[wiki/entities/anthropic]]
- [[wiki/entities/abacus-ai]]

## Key Sources

- [[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]] — mesma tese central ("harness importa mais que parece"), mas com foco em erros compostos e mecanismos de mitigação; esta fonte complementa com um exemplo histórico pré-termo e uma demo de código mínima
- [[wiki/sources/rag-retrieval]] — pipeline RAG (chunking, embedding, busca híbrida) que o relato pessoal desta fonte descreve informalmente, sem o vocabulário técnico atual (hybrid search, RAGAS)
- [[wiki/sources/evals-sistematicas]] — LLM-as-judge e avaliação de faithfulness, aplicados aqui a um caso de uso concreto anterior à formalização do termo "evals sistemáticas"
- [[wiki/sources/structured-outputs-function-calling]] — mecanismo de function calling que esta fonte complementa com o contexto histórico (workaround via tags XML antes do function calling nativo existir em todo provider)
- [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]] — mesmo padrão de demonstração (harness executando comandos shell reais como `ls`/`sed` e devolvendo o resultado ao modelo), aqui com o código-fonte da harness exposto em vez de uma harness comercial já pronta

## Open Questions

- Nome da empresa e período exato em que o sistema RAG/HAG relatado foi construído não são citados — tratar como anedota não verificável, mas coerente com a cronologia geral do mercado (RAG como padrão pré-function-calling nativo generalizado).
- Data exata em que a Anthropic passou a oferecer function calling nativo (encerrando a necessidade do workaround via tags XML) não é mencionada nesta fonte — se uma fonte futura trouxer essa data, reconciliar com [[wiki/concepts/tool-call]].
- Identidade do autor não confirmada nesta ingestão (menciona apenas cursos próprios de DSA/LeetCode, roadmap de entrevistas e curso de system design em pré-lançamento) — mesmo perfil de conteúdo de várias fontes já presentes na wiki (ex. [[wiki/sources/como-ficar-bom-em-leetcode]]), possível mesmo autor/canal, não confirmado.
