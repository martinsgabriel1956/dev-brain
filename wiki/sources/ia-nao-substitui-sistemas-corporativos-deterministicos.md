---
type: source
title: "IA Não Substitui Sistemas Corporativos Determinísticos"
aliases: ["ferramenta probabilística vs tarefa determinística", "por que projetos de ia fracassam", "validador inteligente cobol"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_count: 0
tags: [tech-mentor-ai, determinismo, robustez-de-sistemas, cobol, mainframe, harness-de-qualidade, governanca-de-codigo-gerado-por-ia, era-agentica]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/ia-nao-substitui-sistemas-corporativos-deterministicos.md
source_url: ""
author: "canal de curso de COBOL não identificado"
date_published: ""
date_ingested: 2026-07-27
---

# IA Não Substitui Sistemas Corporativos Determinísticos

## TL;DR

Autor de um curso de COBOL/mainframe relata um experimento pessoal: tentou substituir scripts de validação de tarefa por um "validador inteligente" via LLM (GPT, Claude, Gemini) que analisaria código de aluno e evidências de teste. Funcionou por semanas até começar a falhar de forma inconsistente — aprovando código com variável não definida, reprovando código correto. As três IAs, quando questionadas, deram o mesmo diagnóstico: "você está tentando usar uma ferramenta de análise semântica para fazer análise determinística". Daí a tese central: LLMs processam código como tokens e geram resposta por probabilidade, não por leitura linha a linha — ótimos para interpretar e resumir, péssimos para reproduzir o mesmo resultado sempre. Sistemas corporativos (juros, impostos, folha de pagamento) exigem 100% de previsibilidade, sem espaço para "quase certo". A tese do autor: notícias de grandes empresas cortando projetos de IA não são evidência de bolha — são evidência de que a IA foi usada para substituir software tradicional em vez de alimentá-lo com interpretação. O modelo que funciona: IA interpreta até um certo ponto, e entrega o resultado para o sistema determinístico que decide e registra.

## Key Claims

1. **LLM não lê código linha a linha — tokeniza e gera resposta por probabilidade.** Evidência do autor: os três agentes (ChatGPT, Claude, Gemini) não conseguiam identificar de forma confiável se um programa COBOL estava em free format ou fixed format, e ora aprovavam código com variável não definida no working storage, ora reprovavam código correto — mesmo os três tendo conhecimento de COBOL "como ninguém". Conecta com [[wiki/concepts/tokenizacao]] e a explicação de LLMs como previsores de próximo token em [[wiki/sources/como-llms-funcionam]]. Confiança: alta (relato direto de experimento de três semanas, corroborado pelas três IAs de forma independente).
2. **Ferramenta de análise semântica ≠ ferramenta de análise determinística.** As três IAs consultadas deram o mesmo diagnóstico ao autor sobre por que o validador falhava — analogia do autor: usar carro de corrida para arar campo, ou chave de fenda para pregar prego. O problema não é a ferramenta, é a tarefa que se espera dela. Confiança: alta, mas é auto-diagnóstico relatado pelo próprio autor (a resposta da IA sobre si mesma não é garantia de precisão técnica, é uma explicação plausível e consistente com como transformers funcionam).
3. **Sistemas corporativos (juros, impostos, folha de pagamento) não toleram "quase certo" — exigem output 100% previsível para o mesmo input, hoje e daqui a 5 anos.** É por isso que esses sistemas são construídos com regras rígidas, não com julgamento de modelo. Confiança: alta — coerente com décadas de prática em sistemas financeiros e reforça [[wiki/concepts/robustez-de-sistemas]].
4. **Cortes/cancelamentos de projetos de IA por grandes empresas não indicam bolha — indicam projetos que tentaram usar IA para substituir (não alimentar) software tradicional.** Tese interpretativa do autor, não dado de mercado citado. Adiciona uma explicação mecanística a uma narrativa já presente na wiki via [[wiki/sources/custo-real-ia-tokens-produtividade-demissoes]] e [[wiki/sources/ia-custo-roi-bolha-ou-realidade]] (que documentam o fenômeno de corte/reestruturação por custo e ROI, mas sem essa explicação técnica de "ferramenta errada para a tarefa"). Confiança: média — é interpretação pessoal sem citar casos específicos de empresas.
5. **O modelo que funciona: IA interpreta, sistema tradicional decide e registra.** Projetos de IA bem-sucedidos, segundo o autor, têm a característica de que a IA vai até um ponto (entender o que o cliente quer, resumir um contrato) e depois entrega o resultado para o software que gera a transação e registra o processo. Reforça a arquitetura de [[wiki/concepts/harness-de-qualidade]] e [[wiki/concepts/pipeline-de-qualidade]]: pipeline determinística decide passa/não passa, a IA não decide sozinha. Confiança: alta, consistente com o padrão já documentado na wiki para geração de código com IA.
6. **A existência da IA torna mais evidente — não menos — a importância de sistemas e desenvolvedores que constroem previsibilidade.** Contra-narrativa direta à tese de que a IA substitui o desenvolvedor de sistemas corporativos/mainframe: quando bilhões de reais estão em jogo, a característica mais valiosa não é inteligência, é confiabilidade reproduzível — e é isso que sistemas corporativos (e quem os constrói) entregam há décadas. Conecta com [[wiki/concepts/governanca-de-codigo-gerado-por-ia]]. Confiança: média-alta — argumento coerente, mas é posição defendida pelo próprio autor sobre o valor do seu nicho (COBOL/mainframe).

## Entidades Mencionadas

Nenhuma entidade nomeada de forma verificável no áudio — autor e canal não se identificam explicitamente na transcrição (curso de COBOL/mainframe mencionado ao final, sem nome). Ver open question.

## Conceitos Tocados

- [[wiki/concepts/robustez-de-sistemas]]
- [[wiki/concepts/pipeline-de-qualidade]]
- [[wiki/concepts/harness-de-qualidade]]
- [[wiki/concepts/rubrica-de-verificacao]]
- [[wiki/concepts/governanca-de-codigo-gerado-por-ia]]
- [[wiki/concepts/tokenizacao]]
- [[wiki/concepts/determinismo-vs-probabilismo-em-ia]] (novo)

## Open Questions

- Nome do autor/canal não identificado no áudio — apenas "curso de COBOL" é mencionado ao final, sem marca. Se uma fonte futura identificar o canal, criar entidade e retroligar.
- O diagnóstico "você está usando ferramenta de análise semântica para tarefa determinística" foi dado pela própria IA quando questionada — é uma explicação plausível e coerente com a arquitetura de transformers, mas não deixa de ser a IA explicando sua própria falha; vale checar contra fontes técnicas independentes sobre confiabilidade de LLM-as-judge para validação de código (nenhuma encontrada na wiki até agora).
- Falta de exemplos concretos nomeados (quais empresas, quais projetos) para a claim 4 — é interpretação do autor sobre notícias genéricas, não análise de caso.
