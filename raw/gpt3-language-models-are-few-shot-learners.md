# Language Models are Few-Shot Learners (GPT-3)

**Autores:** Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei (OpenAI)
**Publicado em:** 28 de maio de 2020 (v1), revisado em 22 de julho de 2020 (v4)
**Link:** https://arxiv.org/abs/2005.14165

---

## Resumo

Trabalhos recentes demonstraram ganhos substanciais em tarefas de PLN (Processamento de Linguagem Natural) e benchmarks por meio de pré-treinamento em grandes corpora de texto seguido de fine-tuning para tarefas específicas. Embora geralmente agnóstico à arquitetura, esse método ainda requer conjuntos de dados de fine-tuning específicos com milhares ou dezenas de milhares de exemplos.

Em contraste, humanos geralmente conseguem realizar uma nova tarefa de linguagem a partir de apenas alguns exemplos ou de instruções simples — algo com o qual os sistemas de PLN ainda têm dificuldade. Este paper mostra que **escalar modelos de linguagem melhora drasticamente o desempenho few-shot agnóstico de tarefa**, às vezes chegando a competir com abordagens state-of-the-art de fine-tuning.

Especificamente, os autores treinam o **GPT-3**, um modelo de linguagem autorregressivo com **175 bilhões de parâmetros** — 10x mais do que qualquer modelo não-esparso anterior — e avaliam sua performance no cenário few-shot **sem qualquer atualização de gradiente ou fine-tuning**.

---

## 1. Introdução

### O problema com fine-tuning

A tendência recente em PLN é pré-treinar representações de linguagem e depois fazer fine-tuning em tarefas específicas. O problema é que isso exige:

- Grandes datasets rotulados para cada tarefa.
- Potencial para overfitting em distribuições de fine-tuning.
- Risco de se explorar espúrios de correlação no dataset de fine-tuning que não generalizam.

### A hipótese do paper

Modelos de linguagem maiores são meta-aprendizes melhores. Eles conseguem aprender tarefas a partir do contexto (exemplos no prompt) sem qualquer atualização de pesos.

### Três modos de avaliação

| Modo | Definição |
|---|---|
| **Zero-shot** | Nenhum exemplo; apenas a descrição da tarefa em linguagem natural |
| **One-shot** | Um único exemplo demonstrativo |
| **Few-shot** | Alguns exemplos demonstrativos (tipicamente 10–100) |

Em todos os casos, **nenhum gradiente é atualizado**. O aprendizado acontece puramente via contexto — chamado de **in-context learning**.

### Principais achados

- GPT-3 alcança forte performance em muitos datasets de PLN: tradução, QA (questão-resposta), tarefas de cloze, raciocínio aritmético.
- Modelos maiores fazem uso progressivamente mais eficiente de informação de contexto.
- Performance few-shot cresce mais rapidamente com o tamanho do modelo do que zero-shot.
- Ainda falha em: inferência de linguagem natural (ANLI), alguns datasets de compreensão de leitura (RACE, QuAC).
- GPT-3 gera artigos de notícias que avaliadores humanos têm dificuldade de distinguir de artigos humanos.

---

## 2. Abordagem

### 2.1 Modelo e Arquitetura

GPT-3 usa a mesma arquitetura do GPT-2, com:
- Transformer autorregressivo.
- Inicialização modificada, pré-normalização e tokenização reversível.
- **Padrões de atenção esparsa** alternados (densa + localmente em banda), similar ao Sparse Transformer.

Foram treinados 8 modelos de tamanhos diferentes para estudar como a performance escala com o tamanho:

| Modelo | Parâmetros | Camadas | d_model | Cabeças | d_head |
|---|---|---|---|---|---|
| GPT-3 Small | 125M | 12 | 768 | 12 | 64 |
| GPT-3 Medium | 350M | 24 | 1024 | 16 | 64 |
| GPT-3 Large | 760M | 24 | 1536 | 16 | 96 |
| GPT-3 XL | 1.3B | 24 | 2048 | 24 | 128 |
| GPT-3 2.7B | 2.7B | 32 | 2560 | 32 | 80 |
| GPT-3 6.7B | 6.7B | 32 | 4096 | 32 | 128 |
| GPT-3 13B | 13B | 40 | 5140 | 40 | 128 |
| **GPT-3 175B** | **175B** | **96** | **12288** | **96** | **128** |

Observação: com dados suficientes, a loss de validação segue uma **power law** suave em função do tamanho do modelo.

### 2.2 Dataset de Treinamento

O dataset principal é o **Common Crawl** (~1 trilhão de palavras). Porém, versões não filtradas têm baixa qualidade. Foram aplicadas três etapas:

1. **Filtragem por qualidade**: comparação com corpora de alta qualidade via similaridade.
2. **Deduplicação fuzzy** em nível de documento (dentro e entre datasets).
3. **Adição de corpora curados**: WebText expandido, dois corpora de livros (Books1, Books2) e Wikipedia em inglês.

| Dataset | Quantidade (tokens) | Peso no treinamento |
|---|---|---|
| Common Crawl (filtrado) | 410B | 60% |
| WebText2 | 19B | 22% |
| Books1 | 12B | 8% |
| Books2 | 55B | 8% |
| Wikipedia | 3B | 3% |

---

## 3. Resultados

### 3.1 Benchmarks de Linguagem (Penn Treebank, LAMBADA, HellaSwag)

- **LAMBADA** (prever última palavra de um parágrafo): GPT-3 175B few-shot → **86.4%** de acurácia (SOTA anterior: 68.0%).
- **HellaSwag** (completar sentenças com senso comum): GPT-3 few-shot → **79.3%** (fine-tuned SOTA: 85.6%).

### 3.2 QA em Livro Fechado (Closed-Book QA)

| Configuração | NaturalQS | WebQS | TriviaQA |
|---|---|---|---|
| T5-11B (fine-tuned, closed-book) | 34.5 | 37.4 | 50.1 |
| RAG (fine-tuned, open-domain) | 44.5 | 45.5 | 68.0 |
| GPT-3 Zero-Shot | 14.6 | 14.4 | 64.3 |
| GPT-3 One-Shot | 23.0 | 25.3 | 68.0 |
| GPT-3 Few-Shot | 29.9 | 41.5 | **71.2** |

No TriviaQA, GPT-3 few-shot supera o SOTA fine-tuned open-domain (RAG).

### 3.3 Tradução

GPT-3 few-shot supera modelos supervisionados no par **French→English** e **German→English**, apesar de ter sido treinado principalmente em inglês.

### 3.4 Winograd / Senso Comum

| Configuração | Winograd | Winogrande (XL) |
|---|---|---|
| Fine-tuned SOTA | 90.1 | 84.6 |
| GPT-3 Zero-Shot | 88.3 | 70.2 |
| GPT-3 One-Shot | 89.7 | 73.2 |
| GPT-3 Few-Shot | 88.6 | 77.7 |

### 3.5 Raciocínio de Senso Comum (PIQA, ARC, OpenBookQA)

| Configuração | PIQA | ARC (Easy) | ARC (Challenge) | OpenBookQA |
|---|---|---|---|---|
| Fine-tuned SOTA | 79.4 | 92.0 | 78.5 | 87.2 |
| GPT-3 Zero-Shot | 80.5 | 68.8 | 51.4 | 57.6 |
| GPT-3 Few-Shot | **82.8** | 70.1 | 51.5 | 65.4 |

### 3.6 Aritmética e Tarefas Sintéticas

GPT-3 consegue realizar aritmética de 2 e 3 dígitos few-shot, decodificar palavras embaralhadas e usar novas palavras em frases — tarefas que requerem raciocínio on-the-fly.

### 3.7 Geração de Texto / Artigos de Notícias

Humanos avaliadores tiveram apenas **52%** de acurácia distinguindo artigos gerados pelo GPT-3 de artigos humanos (próximo do acaso).

---

## 4. Contaminação de Dados (Data Contamination)

Como o dataset de treinamento é derivado da internet, é possível que benchmarks de teste estejam contidos no treinamento. O paper desenvolve ferramentas sistemáticas para medir isso:

- Para a maioria dos datasets, a contaminação tem efeito mínimo.
- Alguns datasets têm resultados marcados com `*` ou omitidos devido a possível contaminação.
- Os autores recomendam que trabalhos futuros com Large Language Models (LLMs) investiguem contaminação de forma proativa.

---

## 5. Limitações

1. **Tarefas onde GPT-3 ainda falha**: inferência de linguagem natural (ANLI), compreensão de leitura (RACE, QuAC), tarefas que requerem raciocínio de múltiplos passos.
2. **In-context learning não é fine-tuning**: GPT-3 pode ser menos eficiente do que modelos fine-tuned em tarefas onde dados rotulados estão disponíveis.
3. **Custo de inferência**: modelos de 175B parâmetros são caros e inconvenientes para produção. Destilação (distillation) é apontada como direção futura.
4. **Interpretabilidade**: decisões não são facilmente interpretáveis.
5. **Calibração**: alta variância de performance em inputs novos comparado com humanos.
6. **Vieses dos dados**: o modelo herda vieses do treinamento (vieses de gênero, raça, religião presentes na internet).

---

## 6. Impactos Mais Amplos (Broader Impacts)

### 6.1 Uso Malicioso

Modelos como GPT-3 tornam mais difícil distinguir texto sintético de texto humano, o que pode ser explorado para:
- Desinformação / fake news em escala.
- Spam, phishing e engenharia social.
- Geração de conteúdo prejudicial automatizado.

### 6.2 Fairness, Viés e Representação

Análise conduzida pelo paper indica:

- **Viés de gênero**: ocupações são associadas de forma estereotipada com gêneros (ex.: "nurse" → feminino, "programmer" → masculino).
- **Viés racial**: o modelo produz associações estereotipadas para grupos raciais.
- **Viés religioso**: associações diferentes entre religiões (ex.: Islã associado a palavras negativas com maior frequência).

Conclusão: *"modelos treinados na internet têm vieses na escala da internet"*.

### 6.3 Eficiência Energética

O treinamento de GPT-3 consumiu quantidades significativas de energia. O paper reconhece que modelos maiores têm pegada de carbono maior, e aponta eficiência computacional como área de pesquisa importante.

---

## 7. Conclusão

GPT-3 demonstra que **escalar modelos de linguagem é uma abordagem poderosa para melhorar o aprendizado few-shot**. O modelo alcança resultados impressionantes em dezenas de tarefas sem nenhuma atualização de pesos — apenas via exemplos no contexto.

Ao mesmo tempo, o paper é honesto sobre as limitações: GPT-3 não é uma solução completa, ainda falha em várias tarefas, e levanta questões sérias sobre uso malicioso, vieses e custo computacional.

A principal contribuição conceitual é o conceito de **in-context learning**: a capacidade emergente de modelos grandes de aprender a partir de exemplos no prompt, sem gradient descent.

---

## Conceitos-chave

- **Few-shot learning**: aprender uma tarefa a partir de poucos exemplos no contexto (sem fine-tuning).
- **In-context learning**: aprendizado que acontece no forward pass, via atenção ao contexto, sem atualização de pesos.
- **Zero-shot**: sem exemplos, apenas instrução em linguagem natural.
- **Scaling laws**: performance segue uma lei de potência (power law) em função do número de parâmetros, dados e compute.
- **Data contamination**: sobreposição entre dados de treinamento e benchmarks de teste — problema crescente em LLMs treinados em web-scale data.
- **Distillation**: técnica para comprimir modelos grandes em modelos menores para inferência eficiente.

---

## Referências Relevantes Citadas

- GPT-2: Radford et al., 2019 — arquitetura base do GPT-3.
- Scaling Laws for Neural Language Models: Kaplan et al., 2020 — fundamento teórico das leis de escala.
- Sparse Transformer: Child et al., 2019 — padrões de atenção esparsa usados no GPT-3.
- RAG: Lewis et al., 2020 — sistema de QA open-domain state-of-the-art.
- T5: Raffel et al., 2019 — modelo concorrente de fine-tuning.
