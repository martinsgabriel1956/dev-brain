# Context Engineering para Codebases Grandes — Progressive Disclosure, On-Demand Loading e o Workflow RPI

**Fonte:** Transcrição de vídeo (YouTube)  
**Autor:** Valdemar Neto (cofundador da Tech Leads Club)  
**Data de publicação:** desconhecida  
**Idioma original:** Português (Brasil)

---

## Introdução

Se você trabalha com codebase grande, provavelmente já pediu para a IA fazer uma mudança e ela voltou com código completamente fora do contexto — gastou horas iterando até desistir e fazer você mesmo.

A verdade: a diferença entre **ganhar 10 horas** ou **perder 10 horas corrigindo código da IA** está na gestão do contexto.

---

## O Problema: LLMs são Stateless

LLMs não guardam estado. Toda vez que você usa Cursor, Claude Code, Copilot, a ferramenta pega o contexto do projeto e passa no prompt — então o agente sempre começa do zero.

### Janela de Contexto e a Smart Zone

Janelas de contexto chegam hoje a 1 milhão de tokens, mas isso não é necessariamente melhor:

> Uma LLM é uma máquina de probabilidade. Quanto mais tokens você manda, mais probabilidades ela precisa calcular — como fazer várias perguntas ao mesmo tempo para uma pessoa. Ela vai se perder, demorar, responder sem sentido.

**Recomendação prática:** tentar ficar na faixa de 200.000 tokens e manter o uso abaixo de 40%.

| Zona | Uso da janela | Comportamento |
|---|---|---|
| **Smart Zone** | até ~40% | Boa efetividade, respostas coerentes |
| **Dumb Zone** | acima de ~60% | Alucinações frequentes, respostas sem sentido |

---

## Dois Conceitos Fundamentais

### 1. Progressive Disclosure

Entregar à LLM **gradualmente** as informações que ela precisa, conforme ela vai descobrindo o que a mudança exige.

**Na prática:** arquivos de contexto (`.md`) organizados por responsabilidade e por diretório. Cada módulo do projeto tem seu próprio arquivo de guidelines — quando o agente for modificar aquele módulo, ele carrega o arquivo correspondente.

```
/
├── CLAUDE.md              ← guidelines gerais (sempre carregado)
├── .cursor/rules/
│   ├── architecture.mdc   ← always: true
│   └── ddd-strategic.mdc  ← carregado sob demanda
├── billing/
│   └── GUIDELINES.md      ← carregado quando mexe neste módulo
└── identity/
    └── GUIDELINES.md
```

### 2. On-Demand Loading

Configurar o agente para carregar arquivos de contexto **apenas quando necessário**, com base em gatilhos específicos.

**Cursor Rules — exemplo de configuração:**

```yaml
# architecture.mdc
alwaysApply: true
description: "Carrega as architecture guidelines do projeto."
# → Sempre ativo

# feature-folders.mdc
alwaysApply: false
trigger: "criando ou modificando módulos / dúvidas sobre design patterns"
# → Carregado sob demanda pelo agente

# domain-identification.mdc
alwaysApply: false
trigger: "quando alguém pedir 'identify domains' no chat"
# → Carregado só quando explicitamente solicitado
```

Claude Code tem as **Skills** (similar às Rules do Cursor) — mesma ideia, carregar contexto extra sob demanda.

---

## O Workflow RPI

**R**esearch → **P**lan → **I**mplement

### Fase 1 — Research (Pesquisa)

O agente explora o codebase para **descobrir onde as coisas estão**. Pode usar janela maior (até 1M de tokens) nessa fase porque não vai gerar código ainda.

- O agente carrega guidelines, escaneia estrutura, identifica problemas
- Resultado: um output com achados (ex.: lista de arquivos fora dos padrões, transaction scripts, arquivos sem DDD tático)
- Contexto pode chegar a 40–50% — não tem problema nessa fase

**Nunca peça para implementar na mesma sessão do research.** A janela já está cheia.

### Fase 2 — Plan (Planejamento)

A partir do output do Research, gerar um **plano detalhado de implementação**.

O plano deve conter:
- Análise estrutural do que precisa ser feito
- Resultado esperado
- Comandos que serão rodados
- Como mover/criar arquivos
- Verificações de build e testes para validar cada etapa
- Garantia de que a versão nova cobre 100% dos casos de uso da anterior

**Importante:** sempre ativar o **modo plano** (Plan Mode no Claude Code, Shift+Tab) nessa fase — o agente planeja sem executar.

**Por que o plano é tão importante?**

Quando a IA vai implementar, ela carrega apenas o plano — não precisa fazer research de novo. A janela de contexto fica em 30–35%, bem dentro da Smart Zone.

### Fase 3 — Implement (Implementação)

Partir do plano, não do codebase inteiro. O agente executa o plano em partes, verificando build e testes ao final de cada etapa.

```
Plano carregado (~30% da janela)
    ↓
Agente executa passo 1
    ↓
Roda build + testes → passa? continua : corrige
    ↓
Passo 2 ...
    ↓
Pull Request revisado pelo time
```

---

## Sub-agentes: Delegação de Pesquisa

Sub-agentes no Claude Code permitem **delegar uma tarefa específica** sem encher a janela principal.

Em vez de o agente principal fazer a pesquisa (carregando centenas de arquivos no contexto), você delega para um sub-agente:

- O sub-agente vai, faz a pesquisa, retorna só o **output** — alguns tokens em vez de centenas
- A janela principal permanece pequena

**Como pensar sub-agentes:**

```
❌ Sub-agente de front-end, sub-agente de back-end  → gasto de tokens sem necessidade

✅ Sub-agente de análise de complexidade
✅ Sub-agente: "quais arquivos não seguem as guidelines?"
✅ Sub-agente: validador de arquitetura
✅ Sub-agente: identifica domínios DDD
```

Sub-agentes são para **tarefas específicas e bem definidas**, não para representar camadas da aplicação.

---

## Memória de Longo Prazo: Planos como Arquivos

Para refatorações grandes — que gerariam um plano enorme demais para uma sessão — a estratégia é salvar o plano em um arquivo `.md` (memória de longo prazo).

**Fluxo:**

```
Research → output salvo em refactoring-plan.md
                    ↓
            Revisar manualmente o plano
            Compartilhar com o time para validação
                    ↓
            Quebrar em subplanos por fase:
            - fase-1-outbox-pattern.md
            - fase-2-value-objects.md
            - fase-3-aggregates.md
                    ↓
            Executar cada fase como uma sessão separada
            (janela de contexto pequena em cada sessão)
                    ↓
            Pull Request por fase → revisão humana
```

**Por que funciona:**

- Cada subplano é pequeno → janela de contexto fica baixa
- O ser humano valida o plano antes de executar
- PRs menores são revisáveis
- Cada fase tem critérios claros de sucesso (build + testes passando)

### Exemplo de subplano bem estruturado

```markdown
## Fase 2 — Value Objects

**Pré-requisito:** Fase 1 (Outbox Pattern) concluída e testes passando

**Contexto a carregar:** billing/GUIDELINES.md

**Arquivos a modificar:**
- src/billing/domain/subscription.ts
- src/billing/domain/price.ts

**O que fazer:**
1. Extrair PriceAmount como Value Object
2. ...

**Comandos de validação:**
- npm run build
- npm test -- --testPathPattern=billing

**Critério de sucesso:** build e testes passando, 100% dos casos de uso cobertos
```

---

## RPI vs. Spec-Driven

Spec-Driven virou um guarda-chuva amplo: PRDs, prompts detalhados, API specs, arquivos markdown — tudo passou a ser chamado de "spec". Ficou vago.

RPI é mais preciso porque define o **fluxo lógico**:

| Etapa | O que é | Inclui |
|---|---|---|
| **Research** | Fase de descoberta | Escanear codebase, identificar problemas |
| **Plan** | Fase de especificação | Design doc, PRD, plano detalhado — aqui entra o spec-driven |
| **Implement** | Fase de execução | A partir do plano, não do zero |

Spec-driven é uma parte do Plan, não um substituto do workflow inteiro.

---

## Princípio Central

> O ser humano está no loop: valida os planos, valida o output, revisa os pull requests. A IA executa planos bem definidos — não explora o codebase do zero toda vez.

```
Codebase grande
      ↓
Research (janela grande, só leitura)
      ↓
Plano salvo em arquivo (revisado pelo humano)
      ↓
Subplanos por fase
      ↓
Implement (janela pequena, Smart Zone)
      ↓
Build + Testes passando
      ↓
PR revisado pelo time
```

---

## Ferramentas Mencionadas

- **Cursor** — Rules com `alwaysApply` e gatilhos para on-demand loading
- **Claude Code** — Skills (similar às Rules), Sub-agentes, Plan Mode
- **agents.md** — padrão menos flexível, sem gatilhos configuráveis
