# Context Engineering Avançado para Coding Agents

**Fonte:** Talk de Dex na conferência AI Engineer (palestra "12 Factor Agents" + seguimento)
**Idioma original:** Inglês (traduzido)
**Data:** 2026-05-04

---

## Contexto

Dex — autor da talk "12 Factor Agents" no AI Engineer em junho, uma das mais assistidas do evento — apresenta o que sua equipe aprendeu sobre context engineering para coding agents após meses de uso intenso.

Ponto de partida: uma pesquisa com 100.000 desenvolvedores (Eigor) mostrou que, na maioria dos casos de uso de IA para engenharia de software, há muito retrabalho e churn de codebase. Não funciona bem para tarefas complexas nem para codebases brownfield.

> "Você está entregando muito mais, mas boa parte é só retrabalhar a sujeira que você entregou semana passada."

O que funciona bem: greenfield, dashboards simples, projetos novos. O que não funciona bem: codebase Java de 10 anos.

---

## O que é context engineering

LLMs são stateless. A única forma de obter melhor performance de um LLM é colocar tokens melhores — e então você recebe tokens melhores de volta.

Em cada turno do loop, o agente está escolhendo entre centenas de próximos passos certos e centenas de errados. A única coisa que influencia o que sai é o que está na conversa até aquele momento.

**Otimize a context window para:**
- **Correção** — informações certas
- **Completude** — nada importante faltando
- **Tamanho** — o menor possível
- **Trajetória** — o histórico da conversa importa

> Cuidado com trajetória: se você corrigiu o agente várias vezes numa mesma sessão, o próximo token mais provável é o agente errar de novo — porque é o padrão estabelecido na conversa.

**O pior que você pode ter (em ordem):**
1. Informação incorreta
2. Informação faltando
3. Ruído demais

---

## A Dumb Zone

Você tem ~168.000 tokens de context window (varia por modelo). Alguns são reservados para output e compaction.

A partir de **~40% de uso da context window**, você começa a ver retornos decrescentes dependendo da complexidade da tarefa. Se você tem MCPs demais no seu coding agent, está fazendo todo o trabalho na "dumb zone" e nunca vai ter bons resultados.

> 40% é uma diretriz. Varia conforme a complexidade da tarefa.

---

## Compaction intencional

A forma mais ingênua de usar um coding agent: pedir algo, corrigir quando erra, pedir de novo, até acabar o contexto.

Uma melhoria simples: quando você percebe que foi na direção errada, inicia uma nova context window com o mesmo prompt mas evitando o caminho ruim.

**Compaction intencional** vai além: independente de estar no caminho certo ou não, você periodicamente pede ao agente que comprima o contexto atual num arquivo markdown. Você revisa, tagueia, e quando o novo agente começa já parte direto para o trabalho — sem precisar re-explorar o codebase.

**O que ocupa espaço na context window:**
- Busca de arquivos
- Entendimento de fluxo de código
- Edição de arquivos
- Output de testes e builds
- MCPs despejando JSON com UUIDs

**Uma boa compaction inclui:** os arquivos exatos e números de linha relevantes para o problema sendo resolvido.

---

## Sub-agentes (para controle de contexto, não para papéis)

Sub-agentes existem para controlar contexto — não para antropomorfizar papéis.

**Errado:** sub-agente de frontend + sub-agente de backend + sub-agente de QA.

**Certo:** quando você precisa entender como algo funciona num codebase grande, você dispara um sub-agente com uma nova context window para fazer toda a leitura, busca e exploração — e ele retorna apenas uma mensagem sucinta para o agente pai. O agente pai lê só o arquivo relevante e vai direto ao trabalho.

---

## Workflow Research → Plan → Implement (RPI)

O objetivo é ficar na "smart zone" (abaixo de 40% da context window) durante todo o processo.

### Research
- Entender como o sistema funciona
- Encontrar os arquivos certos
- Manter objetividade (só observar, não planejar)
- Output: documento de research com arquivos e trechos relevantes

### Plan
- Delinear os passos exatos
- Incluir nomes de arquivos e trechos de código
- Ser explícito sobre como testar após cada mudança
- Output: plano com snippets reais do que vai mudar

Planos bons incluem snippets de código reais. Com um plano assim, até o modelo mais simples dificilmente vai errar.

### Implement
- Executar o plano mantendo o contexto baixo
- Não deixar o contexto crescer além do necessário

---

## Mental Alignment — o verdadeiro propósito do code review

Code review existe para **mental alignment**: manter todo o time na mesma página sobre como o codebase está mudando e por quê.

Com o RPI, líderes técnicos podem ler os planos (não necessariamente todo o código gerado) e manter entendimento de como o sistema está evoluindo. Isso escala.

Uma sugestão prática: incluir as threads de interação com o agente no PR (não só o diff), para que o revisor veja os passos exatos, os prompts usados e os resultados de build. Isso leva o revisor numa jornada que um PR normal no GitHub não consegue.

---

## Onboarding de agentes (o problema do Memento)

Referência ao filme Memento: o personagem não tem memória, tem que ler as próprias tatuagens para saber quem é e o que está fazendo.

Se você não faz onboarding dos seus agentes, eles vão inventar coisas.

**Opção 1 — Documentação no repo:** um arquivo de contexto na raiz de cada repo com resumo do codebase. O problema: fica desatualizado e consome muito da smart zone só para aprender como o sistema funciona.

**Opção 2 — Divulgação progressiva:** contexto na raiz + contexto adicional em cada subdiretório, carregado sob demanda. Assim o agente só puxa o que precisa saber.

**Opção preferida — Contexto comprimido sob demanda:** ao invés de documentação estática, um prompt de research (ou slash command) que dispara sub-agentes para fazer fatias verticais pelo codebase e retorna um documento de research que é um snapshot verdadeiro (baseado no código em si) das partes relevantes.

> "Estamos comprimindo verdade."

---

## Calibrando quanto context engineering usar

Não existe uma resposta fixa. Depende do tamanho e complexidade da tarefa:

- **Mudar a cor de um botão:** só fale com o agente diretamente
- **Feature simples, arquivo único:** plan simples
- **Feature média, múltiplos repos:** research + plan
- **Problemas complexos:** research + design discussion + plano vertical

> "Leva repetição. Você vai errar. Às vezes vai grande demais, às vezes pequeno demais. Escolha uma ferramenta e pegue reps."

---

## Sobre Spec-Driven Development

O autor argumenta que "spec-driven dev" sofreu de **semantic diffusion** (conceito de Martin Fowler, 2006): um termo com boa definição inicial que todo mundo começa a usar para significar coisas diferentes até virar inútil.

Spec-driven dev virou: prompt mais detalhado / PRD / loops de feedback verificáveis / tratar código como assembly / usar vários arquivos markdown durante o coding / documentação de biblioteca open source.

O que realmente importa: **compaction e context engineering, ficar na smart zone**. O nome RPI provavelmente vai sofrer o mesmo destino. O que importa são os princípios.

---

## Não terceirize o pensamento

> "IA não pode substituir o pensamento. Ela só pode amplificar o pensamento que você fez — ou a falta dele."

Não existe prompt mágico. Não existe bala de prata. O método falha quando você:
- Pula etapas
- Não lê os planos que o agente gera
- Não mantém o humano no loop para validar direção

A parte mais valiosa do RPI é você, o builder, em diálogo constante com o agente, lendo os planos conforme são criados.

---

## O problema cultural

Está crescendo uma divisão nas equipes:

- **Staff engineers** não adotam IA porque não acelera tanto para eles
- **Juniors/mids** usam muito porque preenche lacunas de skill — mas também produz sujeira
- **Seniors** odeiam cada vez mais porque ficam limpando a sujeira gerada pelo cursor da semana anterior

Isso não é culpa da IA. Não é culpa dos engenheiros mid. Mudança cultural é difícil e precisa vir de cima.

> "Se você é um líder técnico na sua empresa: escolha uma ferramenta e pegue reps."

---

## Resultados práticos

- Equipe de 3 pessoas, 8 semanas, 2-3x mais throughput — mudaram completamente como colaboram
- Oneshot de fix em codebase Rust de 300.000 linhas (linguagem de programação) — PR aceito pelo CTO
- 35.000 linhas de código entregues em 7 horas (estimativa: 1-2 semanas de trabalho normal)
- Tentativa de remover dependências Hadoop do Parquet Java: **não funcionou** — chegou um ponto onde tiveram que voltar ao whiteboard e pensar de verdade antes de continuar

---

## Termos-chave

- **Dumb Zone:** porção da context window acima de ~40% onde a qualidade de resposta cai
- **Smart Zone:** abaixo de ~40%, onde o modelo performa melhor
- **Compaction intencional:** compressão periódica do contexto em markdown para reiniciar com foco
- **Instruction budget:** limite implícito de instruções que um LLM consegue seguir consistentemente (~150-200)
- **Mental alignment:** manutenção do entendimento compartilhado do codebase pela equipe
- **RPI:** Research → Plan → Implement
