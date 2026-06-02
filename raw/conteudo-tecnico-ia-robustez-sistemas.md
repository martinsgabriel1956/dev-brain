# Conteúdo Técnico Não Rende Mais — O que Isso Significa para Devs

> Transcrição de vídeo (canal de tecnologia — autor não identificado pelo nome no trecho)
> Tema: por que conteúdo técnico perdeu audiência, o papel da IA no mercado de devs e onde focar energia agora

---

## Por que Conteúdo Técnico Perdeu Espaço

Conteúdo técnico não rende mais — no YouTube, Twitter, LinkedIn, Medium, dev.to. Tudo foi absolutamente dominado por conteúdo de IA.

### Três razões que se somam

**1. É o que está em hype**
Sempre teve hype em tecnologia: frameworks JavaScript, React, Next.js, Go. IA é o produto novo no mercado. Novidade gera interesse natural — humanos são atraídos pelo que é inédito.

**2. O hype é financiado**
Empresas de IA captaram quantias enormes e estão dispostas a queimar dinheiro para conseguir mídia, notoriedade e usuários. O modelo de negócio não exige retorno imediato do usuário — exige crescimento de métricas para o **exit** (IPO ou aquisição). Anthropic e OpenAI parecem estar se encaminhando para IPO, o que corrobora a tese de que estão construindo narrativa para vender ao investidor.

> *"Elas gastam $500 para conseguir 20 usuários que nunca vão gerar $500 de volta — e tá OK porque o número que elas olham é ter 1 milhão de usuários para conseguir vender pro investidor."*

**3. FOMO engaja melhor que conteúdo técnico**
Em redes sociais, o tipo de conteúdo que mais engaja nessa área é medo de ficar para trás. FOMO + novidade + dinheiro de empresas que pagam muito bem para aparecer = inevitável dominância de conteúdo de IA.

> Praticamente todos os canais relevantes de tecnologia são patrocinados por alguma empresa de IA. O autor se inclui nisso — sem isenção.

---

## A Bolha da IA Vai Estourar?

**A resposta curta: não do jeito que as pessoas imaginam.**

O argumento de quem espera a bolha estourar:
> "Quando a bolha estourar, a IA vai ficar cara demais, vou precisar escovar bit na mão de novo e vou estar na frente."

Esse raciocínio está errado por três motivos:

### 1. Já existem alternativas open source

- Modelos open source de IA já existem e melhoram continuamente
- Modelos especializados e compactados ficam cada vez melhores
- Existem harnesses open source para geração de código
- Se Anthropic e OpenAI fechassem as portas hoje, o progresso continuaria

### 2. O custo vai cair, não subir

Na pior das hipóteses, em dois anos você vai conseguir rodar localmente no próprio computador (se tiver uma máquina decente) uma IA + harness open source para gerar código. Pode não ser melhor que os melhores modelos proprietários — mas vai vencer 80% dos devs em velocidade.

### 3. A natureza do trabalho já mudou

> *"Eu acho que a gente nunca mais vai voltar a escrever tanto código na mão."*

Mesmo que os modelos de ponta fiquem caros, modelos especializados ainda funcionarão bem para autocomplete e geração de código menor. Técnicas de quebrar tarefas complexas em menores e delegar via harness continuarão funcionando.

**Conclusão:** a natureza do trabalho de dev mudou de forma permanente. A pergunta não é "a bolha vai estourar?", mas "o que fazemos agora que isso é realidade?"

---

## O que a IA Resolveu (e o que Criou)

### CRUD está resolvido

> *"CRUD simples, monolito CRUD simples para funcionar para 10.000 usuários: tá resolvido. Acabou."*

Isso tem uma consequência séria para devs júnior: a porta de entrada tradicional — código de baixa complexidade, funcionalidades simples — foi fechada pela IA. Era exatamente isso que os júniors faziam. Esse trabalho agora é feito em horas por qualquer dev com IA.

### O que ficou difícil (e valioso)

**Manter sistemas complexos** — especialmente os que a própria IA gerou.

A demanda por **dev sênior** está aumentando: empresas pedem ajuda para encontrar profissionais que consigam manter sistemas complexos. O autor relata receber muitas propostas e não ter horas disponíveis para aceitar.

### Os erros típicos que a IA comete

**Problema N+1:** a IA está focada em entregar o que você pediu — não em como isso se enquadra no sistema como um todo. Ela faz query, depois outra query, depois outra, e não percebe que está criando um loop de chamadas ao banco.

**Deadlocks e problemas de concorrência:** a IA entrega a tela/feature que você pediu sem raciocinar sobre estados concorrentes.

**Segurança:** exemplo clássico — você pede um sistema de login, ela entrega. Você pergunta se é seguro. Ela responde: "Não, você não pediu para ser seguro."

> *"A IA não é como um ser humano. Eu acho que a gente não pode confiar tanto nela."*

---

## O Papel do Dev Agora: Orquestrador + Revisor de Qualidade

O foco muda de **escrever código** para **garantir que o código gerado é bom**. O dev vira uma espécie de professor que revisa a prova da IA e a ensina a fazer melhor.

### Como forçar qualidade via harness e tooling

**TDD (Test-Driven Development)**
Mande a IA fazer TDD. Com o ciclo test-first, ela gera código que precisa passar por testes antes de ser aceito. Resultado mais previsível.

**Linters e regras de código**
Configure linters com boas regras. A IA vai seguir as regras que você impôs via ferramenta — não as que você simplesmente pediu no prompt.

**Complexidade ciclomática**
Adicione ferramentas que medem complexidade ciclomática na pipeline. Feedback objetivo: a ferramenta passou ou não passou.

**Análise estática de segurança**
Ferramentas de análise estática de código para segurança adicionadas à pipeline. Não confia no julgamento da IA sobre segurança — usa ferramenta determinística.

**Code coverage elevado**
Hoje é mais fácil do que nunca levar coverage para cima. A IA consegue gerar testes unitários em quantidade que seria impraticável manualmente.

**Testes de mutação**
Ferramental de mutation testing garante que os testes de verdade validam o comportamento esperado — e não apenas executam sem quebrar.

**Testes end-to-end**
Mais fácil do que nunca criar o ferramental completo para E2E que testa o que importa.

**Revisão de PR automatizada + humana**
Existem ferramentas para revisar pull requests automaticamente. O diferencial humano é saber o que o revisor de IA *não* pega — e adicionar isso às instruções do revisor de IA.

### O ciclo de melhoria contínua

```
Você aprende o que é código bom
    ↓
Documenta esse conhecimento
    ↓
Configura ferramentas e skills para forçar esses padrões
    ↓
IA gera código dentro desses padrões
    ↓
Você analisa o output e refina os padrões
    ↓
Pipeline determina se é bom ou não (passa / não passa)
    ↓
Se não passa: não commita
```

> É menos "o que eu aprendo para eu escrever" e mais "o que eu aprendo para eu conseguir orquestrar a IA para escrever bem".

---

## A Palavra do Ano: Robustez

O autor encerra com uma observação de mercado:

> *"Eu tô vendo muito bug, muito problema de quebrar produção, muito problema de migração de banco de dados, muito sistema caindo que não deveria cair. Muita falha de segurança."*

A IA acelerou a entrega — e acelerou também a geração de problemas que demandam profissionais que sabem manter sistemas complexos.

### O que qualifica um sistema robusto

- **Escalabilidade** — funciona sob carga crescente
- **Boas abstrações** — interfaces claras entre componentes
- **Boas boundaries** — fronteiras bem definidas entre sistemas
- **Modularidade** — componentes independentes e substituíveis
- **Testabilidade** — cobertura real, não superficial
- **Segurança** — validada por ferramentas, não só por intenção
- **Observabilidade** — você sabe o que está acontecendo em produção

### O conselho final

Esqueça CRUD — está resolvido.

Esqueça o debate "Claude Code vs Codex" — não é o que vai te diferenciar.

Foque em: **como construir sistemas robustos com IA, numa velocidade interessante.**

---

## Referências Mencionadas

- **Lucas Montano** — vídeo sobre "A escassez de Dev Sênior" (recomendado no vídeo)
- **Harness open source** — alternativas que existiriam mesmo sem Anthropic/OpenAI
- **Métricas DORA** — mencionadas implicitamente no contexto de qualidade de entrega

---

## Tags

`conteudo-tecnico` `ia-e-dev` `robustez` `crud-resolvido` `dev-senior` `harness` `tdd` `code-quality` `pipeline` `teste-de-mutacao` `n-plus-one` `era-agentica` `mercado-de-trabalho-dev`
