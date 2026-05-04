# Os Três Erros do Workflow RPI com 10.000 Devs

**Fonte:** Vídeo do canal (análise do vídeo da EAI Engineering)
**Idioma original:** Português
**Data:** 2026-05-04

---

## Contexto

Uma empresa publicou um workflow de IA que hoje tem mais de 10.000 devs usando — e ficaram famosos por isso. Alguns meses depois, subiram num palco numa conferência e admitiram: **"A gente errou em duas coisas importantes."**

O autor do vídeo identifica um terceiro erro, mencionado de passagem sem o peso merecido.

O workflow em questão se chama **Research → Plan → Implement (RPI)** — três fases:

- **Research:** o agente explora o codebase sem modificar nada, coleta informação, vê quais arquivos existem, como o código está organizado e quais são as dependências.
- **Plan:** com o resultado da pesquisa, monta-se um plano de implementação — o que vai mudar, em que ordem, e quais são os impactos.
- **Implement:** o dev revisa o plano, aprova, e o agente executa.

> Quem conhece Spec-Driven Development vai reconhecer. É basicamente a mesma família. Research = fase de contexto. Plan = spec. Implement = implementação guiada. Os nomes são diferentes, mas a filosofia é a mesma.

---

## Erro 1 — Não ler o código durante o research

Durante a fase de research, eles decidiram que **não precisavam ler o código** que o agente estava explorando.

A lógica fazia sentido na teoria: ou você lê, ou você planeja. Por que ler o código também se o agente já leu e você confia nele? Bastava revisar o plano.

Eles passaram seis meses fazendo isso — e depois tiveram que jogar fora uma parte grande do sistema.

**O problema é sutil:** quando você não lê o código, você perde a capacidade de detectar quando o agente está indo na direção errada *antes de ele ir longe demais*. É como revisar um PR de 500 linhas só pela descrição. Às vezes funciona. Às vezes você descobre que o problema é muito pior seis meses depois.

**Conclusão deles:** você precisa entender o que o agente está fazendo. Não linha por linha, não com a mesma profundidade de um code review manual — mas o suficiente para ter um modelo mental do que está acontecendo.

---

## Erro 2 — Planos grandes demais

Na fase de plan, eles deixavam o agente gerar um plano enorme e muito detalhado: quais arquivos seriam criados, quais funções seriam escritas, quais imports seriam adicionados. Planos de 500 a 800 linhas.

A lógica também fazia sentido: quanto mais detalhado o plano, menor a chance de surpresa na implementação.

**O problema:** revisar um plano de 1.000 linhas dá praticamente o mesmo trabalho que revisar o código que vai ser gerado a partir dele. Você dobra o trabalho sem garantia de que o código vai bater com o plano.

---

## Erro 3 (o terceiro, identificado pelo autor) — Instruction budget ignorado

No começo, eles tinham um system prompt enorme com **85 instruções** — tudo que o agente precisava saber: como se comportar, quais ferramentas usar, em que ordem, e o que nunca fazer.

Faz sentido querer um agente consistente com instruções detalhadas. Só que os LLMs têm o que se chama de **instruction budget** (não documentado oficialmente, mas estimado em uso real): o modelo consegue seguir algo em torno de **150 a 200 instruções** com boa consistência. Mais do que isso, a atenção começa a fragmentar.

**O ponto crítico:** você não tem só o system prompt. Você tem:

- System prompt
- CLAUDE.md do projeto
- MCPs instalados
- Contexto acumulado da conversa

Tudo isso junto forma o seu **instruction budget real**. Um prompt de 85 instruções + CLAUDE.md com 30 + instruções de MCPs = facilmente no limite ou além. Cada instrução além do orçamento é um dado — o modelo pode ou não seguir.

> "Se você nunca parou para contar as instruções totais do seu agente, para agora e dá uma olhada."

---

## O que eles mudaram — Método CRISPY

Eles evoluíram o workflow para um método que chamaram de **CRISPY**. Três conceitos principais:

### 1. Design Discussion no lugar de Plan grande

Ao invés de pedir um plano de 1.000 linhas, eles passaram a pedir uma **design discussion**.

A diferença: numa discussão de design, você trabalha no entendimento, não no código que vai ser gerado. Você consegue corrigir a direção antes de qualquer linha ser escrita.

É a diferença entre revisar a planta de um edifício e revisar a construção depois que as paredes já foram levantadas. Uma discussão de design de 200 linhas é revisável em 10 minutos — e você sai sabendo exatamente o que vai ser feito.

### 2. Plano vertical no lugar de plano horizontal

Quando você pede um plano de implementação sem especificar a estrutura, o modelo tem um viés natural: faz tudo do banco primeiro, depois os serviços, depois a API. Você chega na implementação com 1.200 linhas de código e não tem como testar nada no meio.

Se há algo errado no banco, você só descobre quando chegar na API — e aí refatora as três camadas.

**A solução é o plano vertical:** cada pedaço entregue é testável imediatamente. Se há um problema, você para ali. Você não descobre o problema depois de 1.500 linhas de contexto acumulado.

> É exatamente o mesmo problema de um PR horizontal: quem tocou em banco + serviço + API de uma vez, sem caminho testável no meio. A diff vira uma massa impossível de revisar.

O plano vertical = PRs pequenos com o mínimo possível testável. Mais fácil de reverter, mais fácil de identificar bugs, mais fácil para o colega revisar.

### 3. Separação de janelas de contexto

Quando você pesquisa e planeja na **mesma janela de contexto**, acontece contaminação: o modelo começa a misturar o que observou com o que acha que deveria ser construído.

A solução é separar fisicamente os contextos:

- Uma sessão só para coletar os fatos (research)
- Outra sessão recebe esses fatos e decide o que vai construir (plan)

A janela de research não sabe sobre o que vai ser construído — ela só observa. Isso evita que o modelo tome decisões de arquitetura escondidas no meio de uma suposta fase de coleta de informações.

Na prática: começar uma conversa nova pro planning depois que o research acabou. Não deixar o modelo carregar as interferências de uma fase para outra.

---

## O que o autor mudaria no próprio workflow

- Usar **plano vertical** — pedir PR por PR, não todos juntos
- Usar **janelas de contexto separadas** para research e implementação
- Continuar **lendo o código** — não necessariamente linha por linha, mas o suficiente para ter um modelo mental do que está acontecendo

---

## Conclusão

> "Não existe um prompt mágico. Não tem uma instrução secreta que resolve tudo. O que existe é um método — e o método falha quando você pula alguma etapa ou quando você não mede o que está funcionando."

Eles mediram, encontraram os problemas, ajustaram. É exatamente isso que boas equipes de engenharia fazem — inclusive com ferramentas novas.
