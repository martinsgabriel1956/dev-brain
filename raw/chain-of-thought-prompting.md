# Chain-of-Thought Prompting Elicita Raciocínio em Grandes Modelos de Linguagem

**Autores:** Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le, Denny Zhou  
**Instituição:** Google Research, Brain Team  
**Publicado:** 28 jan. 2022 (arXiv:2201.11903) | Revisado: 10 jan. 2023  
**Link:** https://arxiv.org/abs/2201.11903

---

## Resumo

Este trabalho explora como gerar uma cadeia de pensamento — uma série de passos intermediários de raciocínio — melhora significativamente a capacidade de grandes modelos de linguagem de realizar raciocínio complexo.

A técnica, chamada **chain-of-thought prompting**, consiste em fornecer algumas demonstrações de cadeia de pensamento como exemplares no prompt (few-shot). Experimentos em três grandes LLMs mostram melhora em tarefas de raciocínio aritmético, de senso comum e simbólico.

Resultado de destaque: prompting do PaLM 540B com apenas 8 exemplares de cadeia de pensamento alcança estado da arte no benchmark GSM8K de problemas matemáticos, superando até o GPT-3 com fine-tuning + verificador.

---

## 1. Introdução

Escalar o tamanho dos modelos de linguagem traz benefícios, mas sozinho não é suficiente para tarefas desafiadoras como raciocínio aritmético, de senso comum e simbólico.

Este trabalho combina duas ideias:

1. **Rationales em linguagem natural** ajudam no raciocínio aritmético — trabalhos anteriores usaram fine-tuning para isso, mas exige dados anotados.
2. **In-context few-shot learning via prompting** — em vez de fazer fine-tuning, fornecer exemplares diretamente no prompt para tarefas novas.

A ideia central: combinar essas duas ideias. Fornecer exemplares que incluam passos de raciocínio intermediários (cadeias de pensamento) como parte do few-shot prompt.

**Propriedades do chain-of-thought prompting:**
- Permite ao modelo decompor problemas multi-etapas em etapas intermediárias
- Oferece interpretabilidade — é possível ver onde o raciocínio falhou
- Aplicável a qualquer tarefa que humanos resolvem com "raciocínio encadeado"
- Não requer fine-tuning — funciona com modelos off-the-shelf

---

## 2. Setup Experimental

**Modelos testados:**
- GPT-3 (série: Ada, Babbage, Curie, DaVinci — até 175B parâmetros)
- LaMDA (422M a 137B parâmetros)
- PaLM (8B, 62B, 540B parâmetros)

**Comparação:**
- **Standard prompting:** exemplares no formato `<input, output>` sem passos intermediários
- **Chain-of-thought prompting:** exemplares no formato `<input, cadeia de pensamento, output>`

**Setup:** 8 exemplares few-shot em todos os experimentos, mantidos fixos. Sem fine-tuning de nenhum modelo.

---

## 3. Raciocínio Aritmético

### Benchmarks

| Dataset | Descrição |
|---|---|
| GSM8K | Problemas matemáticos de nível escolar com múltiplos passos |
| SVAMP | Variações de problemas matemáticos robustos a perturbações |
| ASDiv | Problemas matemáticos com linguagem diversa |
| MAWPS | Inclui subsets: SingleOp, AddSub, SingleEq, MultiArith |

### Resultados

**Três conclusões principais:**

1. **Chain-of-thought é uma capacidade emergente de escala.** Não melhora — ou até piora — modelos pequenos. Só gera ganhos com modelos de ~100B+ parâmetros. Modelos menores produzem cadeias fluentes mas ilógicas.

2. **Ganhos notáveis com modelos grandes.** PaLM 540B com chain-of-thought supera, via prompting apenas, o estado da arte supervisionado anterior em muitos benchmarks.

3. **PaLM 540B supera GPT-3 com fine-tuning + verificador no GSM8K.** Ganho de ~57% vs. ~35% para o melhor fine-tuned anterior.

### Estudo de Ablação

Variações testadas para isolar o que contribui para a melhora:

- **Equation only:** Modelo gera apenas a equação matemática sem linguagem natural → não ajuda em GSM8K (problemas muito complexos para converter direto em equação). Ajuda em datasets de 1-2 etapas.
- **Variable compute only:** Usa `...` para simular tokens extras sem conteúdo → não ajuda, confirmando que é o conteúdo dos passos que importa.
- **Reasoning after answer:** Cadeia de pensamento gerada após a resposta → não ajuda, confirmando que o raciocínio precisa ser gerado antes.

**Conclusão:** o conteúdo das etapas intermediárias, não apenas a extensão da geração, é o que produz a melhora.

### Robustez

Chain-of-thought é robusto a:
- Diferentes anotadores (3 anotadores independentes testados)
- Estilos de escrita diferentes (conciso vs. detalhado)
- Diferentes exemplares (conjuntos alternativos de 8 exemplares)
- Variação no número de exemplares (de 1 a 8) — melhora se mantém

---

## 4. Raciocínio de Senso Comum

A natureza linguística do chain-of-thought o torna aplicável além de matemática.

### Benchmarks

| Dataset | Tipo |
|---|---|
| CSQA | Questões de senso comum sobre o mundo com semântica complexa |
| StrategyQA | Raciocínio multi-hop com estratégia inferida |
| Date Understanding (BIG-bench) | Compreensão de datas |
| Sports Understanding (BIG-bench) | Plausibilidade de frases sobre esportes |
| SayCan | Mapeamento de linguagem natural a ações de robôs |

### Resultados

Chain-of-thought prompting melhora ou iguala o desempenho em todos os benchmarks testados com modelos grandes. PaLM 540B com chain-of-thought alcança ou supera estado da arte em vários casos, mesmo sem fine-tuning.

---

## 5. Raciocínio Simbólico

### Tarefas (artificiais, bem definidas)

- **Last letter concatenation:** Concatenar a última letra de cada palavra em um nome (ex: "Amy Brown" → "yn"). Mais difícil que concatenar a primeira letra.
- **Coin flip:** Determinar se uma moeda ainda está cara para cima após uma sequência de pessoas que ou viram ou não viram a moeda.

### Setup

- **In-domain:** exemplares com o mesmo número de etapas do teste
- **Out-of-domain (OOD):** exemplares com menos etapas que o teste (generalização para sequências mais longas)

### Resultados

- **In-domain:** PaLM 540B com chain-of-thought atinge quase 100% de acerto. Modelos pequenos falham mesmo in-domain.
- **OOD:** Standard prompting falha completamente. Chain-of-thought mantém curva crescente com o tamanho do modelo — demonstra **generalização de comprimento** além dos exemplares vistos.
- A capacidade de manipulação simbólica abstrata só emerge a partir de ~100B parâmetros.

---

## 6. Discussão

### Por que chain-of-thought funciona?

A melhora envolve múltiplas **capacidades emergentes** que interagem:
- Compreensão semântica
- Mapeamento de símbolos
- Manutenção de contexto (staying on topic)
- Capacidade aritmética
- Fidelidade ao raciocínio

Modelos pequenos falham porque geram cadeias fluentes mas ilógicas — o problema não é o formato, mas a ausência das capacidades emergentes.

### Quando chain-of-thought ajuda mais?

Três condições para maior ganho:
1. A tarefa é **desafiadora** e requer raciocínio multi-etapas
2. Um **modelo grande** é usado (~100B+ parâmetros)
3. A curva de escala com standard prompting é **relativamente plana**

Benefícios menores quando o desempenho base já é alto (pouco espaço para melhora) ou quando a tarefa requer apenas 1-2 etapas.

### Limitações

- Chain-of-thought não garante raciocínio correto — cadeias geradas nem sempre são factuais
- Requer modelos muito grandes para funcionar bem
- Custo de inferência maior (mais tokens gerados)
- Não recomendado para uso em cenários reais sem verificação humana das cadeias geradas

---

## 7. Trabalhos Relacionados

- **Rationales em NLP:** trabalhos que usam explanações intermediárias (fine-tuning) — este trabalho mostra que o efeito pode ser obtido via prompting
- **Scratchpads:** Nye et al. (2021) — uso de rascunho intermediário; este trabalho diferencia por focar em few-shot prompting sem fine-tuning
- **Program synthesis e neuro-simbólico:** métodos que usam linguagens formais; chain-of-thought usa linguagem natural
- **Prompting:** Brown et al. (2020) GPT-3 — base do few-shot prompting; este trabalho adiciona raciocínio intermediário
- **Emergent abilities:** Wei et al. (2022) — capacidades que surgem apenas em modelos grandes

---

## 8. Conclusões

Chain-of-thought prompting é um método simples e amplamente aplicável para melhorar o raciocínio em LLMs.

**Conclusão central:** raciocínio em cadeia de pensamento é uma **propriedade emergente de escala** — permite que modelos suficientemente grandes realizem tarefas de raciocínio que, com prompting padrão, têm curvas de escala planas.

A expansão do alcance de tarefas de raciocínio que LLMs conseguem realizar — sem fine-tuning, apenas via prompting — é o principal contribuição do trabalho.
