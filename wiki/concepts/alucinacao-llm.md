---
type: concept
title: "Alucinação de LLM"
aliases: ["hallucination", "llm hallucination", "alucinacao", "llm mente"]
date_created: 2026-07-30
date_updated: 2026-08-10
source_count: 2
tags: [alucinacao, hallucination, ai-safety, rag, guardrails, llm-as-judge, faithfulness]
skill: tech-mentor-ai
status: draft
---

# Alucinação de LLM

Fenômeno amplamente documentado na academia em que um LLM gera com confiança fatos, referências, features, pacotes de código ou dados que não existem. Não é falha ocasional nem exagero anedótico: benchmarks mostram taxas de erro factual substanciais mesmo em modelos considerados estado da arte no momento do teste.

## Causa Raiz (Segundo Pesquisa da OpenAI)

Os procedimentos padrão de treinamento e avaliação de LLMs recompensam o palpite em vez do reconhecimento de incerteza — um modelo que "chuta" uma resposta tem, em média, expectativa de pontuação maior em benchmarks do que um modelo que responde "não sei". Duas consequências práticas descritas em [[wiki/sources/porque-nunca-confiar-em-llm-alucinacao]]:

- **A precisão nunca chegará a 100%**, independente do tamanho do modelo ou da capacidade de busca/raciocínio — algumas perguntas do mundo real são inerentemente impossíveis de responder com certeza.
- **Modelos pequenos podem reconhecer seus próprios limites mais facilmente do que modelos grandes** ("superinteligentes"), um paralelo direto com o comportamento de confiança excessiva observado em humanos.

Prompts que pedem explicitamente reconhecimento de incerteza ("me pergunta se não tiver certeza", "busca uma fonte antes de responder") reduzem a alucinação na prática — efeito consistente com essa causa raiz, já que dá ao modelo permissão explícita para não "chutar".

## Onde Alucinação Aparece na Prática

- **Fatos factuais** — datas, eventos, dados verificáveis apresentados com o mesmo tom de confiança de uma resposta correta.
- **Código** — pacotes/libs inventados (nomes que não existem) ou funcionalidades inexistentes atribuídas a pacotes reais. Um corpus citado de 576.000 gerações de código continha 205.000 pacotes totalmente alucinados.
- **Referências acadêmicas** — pedir para a LLM escrever um artigo científico tipicamente produz citações que não existem.

## Mitigações (Reduzem, Não Eliminam)

| Técnica | Efeito | Limite |
|---|---|---|
| [[wiki/concepts/tool-call]] (busca na web, execução de testes) | Ancora a resposta em dado externo verificável em tempo real | Depende do modelo de fato invocar a ferramenta e da fonte encontrada ser confiável |
| [[wiki/sources/rag-retrieval]] (RAG) | Injeta documentos reais no contexto, reduzindo a dependência do "modelo mental" interno da LLM | Não elimina alucinação — o modelo ainda pode ignorar ou distorcer o documento fornecido |
| LLM-as-judge medindo **faithfulness** (ver [[wiki/sources/evals-sistematicas]]) | Verifica, num segundo passo, se a resposta está ancorada no documento antes de entregá-la ao usuário | Adiciona latência/custo; o próprio juiz é uma LLM sujeita a viés |
| Prompt explícito pedindo reconhecimento de incerteza | Reduz "chute" ao dar permissão para o modelo admitir não saber | Não resolve a causa raiz do incentivo de treinamento, só mitiga no nível de prompt |

Nenhuma dessas técnicas, isolada ou combinada, zera a alucinação — sempre resta um grau residual de invenção, conforme o próprio paper da OpenAI conclui sobre o limite teórico de 100% de precisão.

## Consequência de Produto: Risco Jurídico

Uma LLM em produção que alucina para o usuário final gera passivo jurídico direto para a empresa — caso citado: Air Canada foi condenada a indenizar um cliente porque o chatbot da empresa deu uma informação falsa sobre política de reembolso. Esse risco cresce com [[wiki/concepts/tool-call|capacidades agênticas]] do chatbot (ex.: oferecer descontos automaticamente): um usuário mal-intencionado pode tentar induzir a LLM a alucinar uma resposta favorável a si mesmo.

## Pipeline de Produção Recomendado (Chatbot Corporativo)

1. Prompt engineering sobre a pergunta bruta do usuário (correção, detalhamento).
2. Retrieval de documentação interna via RAG.
3. Prompt final citando o trecho exato da documentação relevante, pedindo para a LLM explicar apenas aquele trecho.
4. Segunda verificação via LLM-as-judge medindo faithfulness (fidelidade da resposta ao documento).
5. Se reprovar, o processo recicla até a resposta ficar ancorada no documento antes de ir ao usuário.

Esse fluxo é a aplicação concreta do modelo de guardrails de entrada/saída já documentado em [[wiki/sources/ai-safety-guardrails]] (grounding check como output filter).

## Key Sources

- [[wiki/sources/porque-nunca-confiar-em-llm-alucinacao]] — origem desta página: estatísticas de taxa de erro factual, paper da OpenAI sobre causa raiz, caso Air Canada, alucinação de pacotes de código, pipeline de produção com RAG + LLM-as-judge
- [[wiki/sources/como-usar-ia-para-aprender-programacao-sem-atrofiar]] — "informações falsas" como o principal risco factual do estudo com IA; exige [[wiki/concepts/pensamento-critico]], sobretudo em conteúdo complexo
