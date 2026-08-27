---
type: concept
title: "Prompt Engineering"
aliases: ["engenharia de prompt", "prompt design"]
date_created: 2026-05-17
date_updated: 2026-08-27
source_count: 12
tags: [prompt-engineering, llm, few-shot, codex, software-3]
skill: tech-mentor-ai
status: stable
---

# Prompt Engineering

## Definição

Prática de construir sequências de texto (prompts) para elicitar outputs específicos de modelos de linguagem. É a primeira alavanca de controle sobre um LLM — barata, iterável e sem infra adicional.

Andrej Karpathy chama isso de [[software-3]] — a terceira geração de programação.

## Hierarquia de Abordagens (custo crescente)

```
Zero-shot → Few-shot → Chain-of-Thought → Self-Consistency → Fine-tuning
↑ Mais rápido, menos custo                    Mais lento, mais custo ↑
```

Sempre experimente da esquerda para a direita antes de ir para a próxima etapa.

## Quatro Padrões Fundamentais

### Tell It — Instrução de Alto Nível
Descreva a tarefa explicitamente: linguagem, tom, restrições, o que fazer e o que não fazer. Declare variáveis e tipos antes da instrução.

### Show It — Exemplos (Few-Shot)
Inclua pares input→output no prompt. O modelo aprende o padrão sem atualizar pesos. Sweet spot: 3–5 exemplos. Ver [[few-shot-learning]].

### Describe It — Descrever Contexto Desconhecido
Para APIs ou domínios que o modelo não conhece, descreva assinaturas de funções, schemas ou glossário diretamente no prompt antes de usá-los.

### Remind It — Histórico Conversacional
Modelos são stateless — não lembram turnos anteriores. Para manter contexto, inclua o histórico como exemplos adicionais. Use janela deslizante (rolling window) para não exceder o [[context-window]].

## Estrutura Completa de um Prompt

```
[Instrução de alto nível]
[Contexto / Schema / API hints]
[Exemplos few-shot]
[Input do usuário]
```

Não há estrutura obrigatória — os modelos são flexíveis. Itere e meça.

## Quando Usar vs Fine-Tuning

| Situação | Abordagem |
|---|---|
| Tarefa genérica, modelo grande | Zero-shot |
| Padrão de output específico | Few-shot |
| Raciocínio complexo | Chain-of-Thought |
| Dataset grande, latência crítica | Fine-tuning |

## Relação com Outros Conceitos

- [[in-context-learning]] — o mecanismo subjacente ao few-shot e zero-shot
- [[few-shot-learning]] — variante com exemplos no prompt
- [[zero-shot-learning]] — sem exemplos, só instrução
- [[chain-of-thought]] — forçar raciocínio passo a passo
- [[completion]] — o output gerado pelo modelo
- [[context-window]] — limite de tamanho do prompt
- [[hyperparameters-llm]] — controles de temperatura, stop sequence etc.
- [[fine-tuning]] — alternativa mais custosa

## Formato de Estrutura: Markdown, Tags ou HTML?

O Prompt Guidance da OpenAI recomenda Markdown estruturado (papel/objetivo + instrução), consistente com o padrão Tell/Show/Describe/Remind acima. Mas não há formato universalmente ótimo: a formatação ideal varia por modelo (a própria OpenAI mantém uma ferramenta para otimizar prompts por modelo específico), e modelos mais antigos de chain-of-thought historicamente performavam melhor com tags estruturais (estilo XML) do que com Markdown puro ou HTML. Ver [[wiki/concepts/html-vs-markdown-formato-de-saida-agentes]] para o debate equivalente aplicado ao *output* de um agente (não ao prompt de entrada).

## Verificação Embutida no Prompt (Agentes de Código)

Para agentes de codificação como o [[wiki/entities/claude-code]], a recomendação oficial da Anthropic é incluir no próprio prompt como o resultado deve ser verificado, não só o que deve ser feito — por exemplo, pedir casos de teste específicos (`user@mail.com` → verdadeiro, `user@.com` → falso) ou pedir que o agente tire um screenshot do resultado e compare com um design de referência, listando e corrigindo diferenças. Isso reduz o risco de o agente (ou o dev) aceitar como pronto um resultado que só *parece* correto. Consistente com o padrão "Tell It" acima, mas específico para tarefas com um estado final objetivamente checável.

Em modelos mais fortes (ex.: Fable), o mesmo princípio de "descreva o estado desejado, não os passos" se aplica com ainda mais força — focar em resultado, limitações e evidências de sucesso funciona melhor do que prescrever uma sequência de ações, porque o modelo tem mais capacidade de planejar o caminho sozinho.

## "Tell It" Fora de Contexto de Código

[[wiki/sources/sistema-produtividade-ia-adapta]] aplica o padrão Tell It a um domínio não técnico: prompts de planejamento pessoal que declaram explicitamente formato de saída esperado (divisão por dia, foco do dia, ordem de execução, período sugerido) e critérios de organização (energia, prioridade, carga mental) — mesma lógica de "declarar restrições e formato antes da instrução" usada em prompts de codificação, mostrando que o padrão não é específico de tarefas técnicas.

## Skills São Apenas Mais Texto no Prompt

[[wiki/sources/harness-explicado-function-calling-hag-evals]] argumenta contra a ideia de que skills dão "superpoder" a um agente: mecanicamente, uma skill só adiciona mais texto ao prompt enviado a cada chamada — tudo que entra e sai do data center do provider é texto. Reforça (sem contradizer) a distinção já registrada em [[wiki/concepts/harness]] entre "provider harness" e "user harness": skills fazem parte da alavanca do usuário, mas continuam sendo prompt engineering, não uma capacidade nova concedida ao modelo.

## Método de Seis Passos para Prompt de Pentest Assistido

[[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]] descreve um método específico de domínio (segurança/autopentest), mas que reafirma vários princípios já documentados nesta página em outro contexto: (1) declarar o papel de quem pede o teste (dono do sistema, não atacante externo); (2) apontar para documentação já existente do sistema em vez de deixar o modelo inferir arquitetura — instância direta de "Describe It"; (3) definir explicitamente o que o sistema **não é** (ex.: "não uso Kubernetes"), tão importante quanto dizer o que é, para restringir o espaço de hipóteses do modelo; (4) testar um escopo por vez em sessões separadas — a fonte relata que testar tudo de uma vez faz o modelo "delirar" e gasta mais tokens sem necessidade; (5) definir o formato de resposta esperado; (6) declarar explicitamente o que a IA **não pode fazer** sem nova autorização — contra-exemplo de "Tell It" mal calibrado: uma autorização ampla ("pode mexer, não pergunte mais") interpretada literalmente pode levar o agente a refatorar código sem solicitar confirmação em uma pergunta não relacionada.

## Prompt Bom Não Compensa Contexto Ausente

[[wiki/sources/engenharia-de-contexto-vs-prompt-engineering-gargalo-real-times-ia]] documenta um caso onde um prompt tecnicamente bem construído (Tell It completo: idempotência, formato de resposta, tratamento de erro) ainda assim gerou código que violava uma regra de negócio central, porque essa regra vivia fora da janela de contexto do modelo. A fonte trata isso como o limite estrutural do prompt engineering: nenhuma técnica de fraseado resolve a ausência de informação que o modelo nunca recebeu — esse é o problema que [[wiki/concepts/context-engineering-harness|context engineering]] existe para resolver, um nível acima do prompt individual. Ver essa página para o caso completo (fila de auditoria de cobrança) e os três movimentos aplicados para corrigi-lo.

## Versionamento de Prompt Não É Só Git

Uma nova versão de prompt pode quebrar o comportamento do sistema da mesma forma que uma nova versão de código pode quebrar um teste. Versionar num repositório Git ou banco de dados registra o histórico, mas não valida a mudança. O padrão recomendado é tratar prompt como artefato com **gate em CI/CD**: rodar o novo prompt contra um conjunto de [[wiki/concepts/llm-evals-testing|evals/snapshots]] antes de liberar, barrando automaticamente uma versão que regride o comportamento esperado — em vez de descobrir a regressão em produção.

## Por Que Prompt Engineering Deixou de Bastar Sozinho

[[wiki/sources/prompt-context-harness-engineering-tres-pilares]] narra, sem contradizer o que já está registrado nesta página, por que a importância relativa de "saber pedir" caiu (sem desaparecer) desde 2022: com janela de contexto de ~4.000 tokens naquela época, o prompt era praticamente a única alavanca disponível — não havia espaço para injetar codebase inteira, rules ou histórico extenso. Com janelas de 1 milhão de tokens hoje e modelos melhores, um prompt mediano já produz boa resposta com mais frequência, deslocando a alavanca principal de qualidade para [[wiki/concepts/context-engineering-harness|context engineering]] e depois para [[wiki/concepts/harness|harness engineering]]. Consistente com "Prompt Bom Não Compensa Contexto Ausente" acima, mas com o argumento histórico do porquê.

## Fontes

- [[wiki/sources/prompt-context-harness-engineering-tres-pilares]] — evolução histórica: janela de contexto pequena em 2022 (~4k tokens) tornava o prompt a única alavanca disponível; janela grande hoje desloca a alavanca principal para context/harness engineering
- [[wiki/sources/microsoft-prompt-engineering-guide]]
- [[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]] — método de seis passos para prompt de autopentest de segurança
- [[wiki/sources/gpt3-language-models-are-few-shot-learners]]
- [[wiki/sources/chain-of-thought-prompting]] — evidência empírica de que CoT (few-shot com passos intermediários) é a técnica mais eficaz para raciocínio multi-etapas
- [[wiki/sources/html-vs-markdown-para-agentes-de-ia]] — contraste entre a recomendação de Markdown da OpenAI e o uso de tags/HTML em fluxos de produção reais
- [[wiki/sources/sistema-produtividade-ia-adapta]] — padrão Tell It aplicado a prompts de planejamento pessoal, fora de contexto de codificação
- [[wiki/sources/20-melhores-praticas-claude-code-segundo-anthropic]] — verificação embutida no prompt e "descreva o resultado, não os passos" como práticas oficiais do Claude Code
- [[wiki/sources/vibe-coding-jogos-um-prompt-vs-varios-estagios-produto]] — a diferença entre entregar um jogo em 1 vs. 8 prompts é atribuída ao prompt (bom senso + fornecer assets/referências), não ao modelo; o "único prompt" na prática vira 20-30 iterações via [[wiki/concepts/loop-engineering|loop]]
- [[wiki/sources/extrair-melhor-codigo-de-agentes-ia-planejamento-plan-mode-skills]] — prompt específico + contexto (mencionar arquivos, URL de referência, o design pattern desejado) vs. prompt genérico que transfere decisões subjetivas para a IA
- [[wiki/sources/harness-explicado-function-calling-hag-evals]] — skills não dão "superpoder", só adicionam mais texto ao prompt; distinção reforçada entre o que roda localmente (código) e o que só existe como texto no data center do provider
- [[wiki/sources/8-pontos-arquitetura-de-software-na-era-da-ia]] — versionamento de prompt como artefato com gate em CI/CD (não só Git); prompt engineering como pilar fundamental da arquitetura de agente, ao lado de tree of thoughts, skeleton of thoughts, ReAct e self-refining
- [[wiki/sources/engenharia-de-contexto-vs-prompt-engineering-gargalo-real-times-ia]] — limite estrutural do prompt bem escrito quando a informação necessária nunca esteve na janela de contexto; crítica ao "prompt mágico" como bala de prata (Frederick Brooks)
