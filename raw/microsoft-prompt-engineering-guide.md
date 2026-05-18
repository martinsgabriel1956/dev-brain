# Como fazer modelos de código gerarem exatamente o que você quer

> Fonte: https://microsoft.github.io/prompt-engineering/
> Autor: Microsoft
> Data de acesso: 2026-05-17

---

## Introdução

Modelos de IA como o **Codex** (OpenAI) traduzem linguagem natural em código em mais de uma dúzia de linguagens de programação. A técnica que controla a qualidade dessas traduções chama-se **Prompt Engineering**.

**Prompt Engineering** é a prática de usar _prompts_ — sequências de texto como frases ou blocos de código — para obter o output desejado de um modelo de IA.

O modelo funciona como uma pessoa escrevendo: recebe o prompt e continua escrevendo a partir dele. O texto gerado pelo modelo é chamado de **completion** (conclusão).

Exemplo simples:

```python
# Prompt (comentário Python)
# Escreva uma função que soma dois números e retorna o resultado.

# Completion gerada pelo modelo
def add(a, b):
    return a + b
```

O Codex também alimenta o **GitHub Copilot**, disponível no Visual Studio e VS Code, que usa o contexto do código e comentários para sugerir completions.

---

## Os 4 Padrões Principais de Prompt Engineering

### 1. Tell It — Diga o que você quer (descrição de alto nível)

Sempre comece com uma descrição de alto nível da tarefa. A _qualidade_ das completions depende muito do que você diz ao modelo.

**Sem contexto:**
```python
# Carregue dados iris do scikit-learn e plote os dados de treino.
```
O modelo pode assumir imports incorretos ou estar faltando libs.

**Com contexto melhor:**
```python
# Gere um programa Python seguindo as instruções do usuário.
# Seja útil e importe as bibliotecas necessárias primeiro.
```

Isso instrui o modelo a seguir uma estrutura mais confiável — importar libs antes de usá-las.

**Variação: diga o que NÃO fazer**

Você também pode especificar o que o modelo deve evitar:

```python
# Gere um programa Python. Não use list comprehension.
```

**Variação: especifique tipos de dados e variáveis**

Declarar as variáveis e tipos esperados antes do prompt reduz ambiguidade:

```python
# Variáveis: name (str), age (int), is_active (bool)
# Gere uma função que retorna um dict com esses campos.
```

---

### 2. Show It — Mostre exemplos (few-shot learning)

Você pode guiar o modelo com exemplos de input → output. Essa técnica chama-se **few-shot learning**.

| Termo | Significado |
|---|---|
| **Zero-shot** | Prompt sem nenhum exemplo — só a descrição da tarefa |
| **One-shot** | Prompt com um exemplo de input → output |
| **Few-shot** | Prompt com múltiplos exemplos |

Padrão few-shot:

```
Tarefa: converter temperatura de Celsius para Fahrenheit.

Exemplos:
Input: 0°C → Output: 32°F
Input: 100°C → Output: 212°F

Input: 37°C → Output:
```

O modelo aprende o padrão pelos exemplos e aplica à nova entrada.

---

### 3. Describe It — Descreva o contexto de alto nível (APIs e schemas)

Quando o modelo não conhece uma biblioteca ou API específica, você pode **descrever** essa API antes de usá-la.

Exemplo com a Simulated Player API do Minecraft (TypeScript):

```typescript
/* Comandos do bot Minecraft usando a Simulated Player API.
   Quando o comentário for conversacional, o bot responde como
   um bot Minecraft útil. Caso contrário, executa o pedido. */

// Assinaturas da API disponíveis:
// player.moveForward(speed: number): void
// player.jump(): void
// player.chat(message: string): void
// player.mine(block: Block): void

// Mova o personagem para frente um pouco
```

Ao descrever a API com assinaturas de funções, o modelo gera código correto para aquela biblioteca específica — mesmo que seja nova demais para ele ter visto durante o treinamento.

---

### 4. Remind It — Lembre o histórico da conversa (contexto conversacional)

Modelos de linguagem são **stateless** — eles não lembram conversas anteriores automaticamente. Para manter contexto conversacional, você precisa incluir o histórico no prompt.

Exemplo do problema:

```
Usuário: Quero pedir um café de 350ml
Usuário: Ah, pode colocar em um copo de 600ml?
```

O modelo não sabe que "colocar" refere-se ao café de 350ml — a menos que o histórico seja passado junto.

**Solução:** adicionar o par input+completion anterior como um exemplo adicional no prompt.

```
[Histórico]
Usuário: Quero pedir um café de 350ml
Bot: Claro, anotei um café de 350ml.
Usuário: Ah, pode colocar em um copo de 600ml?
Bot:
```

Na prática, usa-se uma **janela deslizante** do histórico — mantendo apenas os N últimos pares — porque o contexto tem tamanho limitado (context window).

---

## Juntando Tudo: Estrutura Completa de um Prompt

Para aplicações reais, um prompt bem construído combina:

1. **Descrição de alto nível da tarefa** — instrua o modelo sobre tom, estilo e objetivo
2. **Contexto de alto nível** — schemas de banco, hints de API, informações de background
3. **Exemplos (few-shot)** — mostre o padrão input → output desejado
4. **Input do usuário** — o que o usuário disse na sessão atual

```
[Descrição]
Você é um assistente que gera queries SQL para um banco PostgreSQL.
Responda apenas com SQL válido, sem explicações.

[Schema do banco]
tabela: users (id UUID, name TEXT, email TEXT, created_at TIMESTAMPTZ)
tabela: orders (id UUID, user_id UUID, total NUMERIC, status TEXT)

[Exemplos]
Pergunta: Quantos usuários existem?
SQL: SELECT COUNT(*) FROM users;

Pergunta: Liste os pedidos com status 'pending'.
SQL: SELECT * FROM orders WHERE status = 'pending';

[Input]
Pergunta: Qual o total gasto pelo usuário com id '123'?
SQL:
```

> Os modelos são flexíveis — não há regra rígida sobre a estrutura. Experimente e ajuste conforme o caso.

---

## Hiperparâmetros

O comportamento dos modelos pode ser ajustado via hiperparâmetros:

| Hiperparâmetro | Efeito |
|---|---|
| **temperature** | Controla a criatividade. `0` = determinístico (mesmo output toda vez). Valores maiores = mais variação. |
| **max_tokens** | Limite de tokens no completion. Afeta diretamente o tamanho da resposta e a latência. |
| **stop sequence** | Sequência que interrompe a geração. Ex: `#` para Python, `//` para JavaScript — evita que o modelo gere variações desnecessárias. |

---

## Além do Básico: Considerações para Produção

### Performance

Prompts maiores → latência maior. Para produção:
- Reduza o tamanho do prompt sempre que possível
- Considere **fine-tuning** do modelo — além de melhorar a precisão, reduz a necessidade de exemplos longos no prompt, diminuindo a latência

### Experiência do Usuário

- **Sempre deixe o usuário revisar e rejeitar** outputs do modelo — o output não é 100% confiável
- Facilite a edição: o usuário deve conseguir corrigir o que o modelo gerou (ex: como o Copilot faz no VS Code)
- **Nunca execute código gerado automaticamente** sem revisão humana

### Uso Responsável

Modelos grandes são treinados em dados da internet e podem refletir vieses dos dados de treino. Para produção:
- Use **content filtering** (filtros de conteúdo) — tanto a OpenAI quanto o Azure OpenAI Service oferecem essa funcionalidade
- Siga os [princípios de IA responsável da Microsoft](https://www.microsoft.com/ai/responsible-ai)

---

## Zero-shot, One-shot e Few-shot: Quando Usar

| Situação | Abordagem recomendada |
|---|---|
| Tarefa simples e bem conhecida pelo modelo | Zero-shot (só descrição) |
| Tarefa com padrão de output específico | One-shot ou few-shot |
| API/biblioteca desconhecida pelo modelo | Describe It + few-shot |
| Aplicação conversacional | Remind It (histórico no prompt) |
| Produção com precisão crítica | Fine-tuning + prompts menores |

---

## Prompt Engineering como "Software 3.0"

Andrej Karpathy (ex-head de IA da Tesla) cunhou o conceito de **Software 3.0**: escrever prompts é uma nova forma de programar.

| Geração | Paradigma |
|---|---|
| Software 1.0 | Código imperativo escrito por humanos |
| Software 2.0 | Pesos de redes neurais (deep learning) |
| Software 3.0 | Prompts em linguagem natural |

Prompt engineering é a habilidade central dessa nova camada de desenvolvimento de software.

---

## Referências e Recursos

- [OpenAI Playground](https://beta.openai.com) — ambiente para testar prompts
- [Exemplos de código OpenAI](https://beta.openai.com/examples?category=code)
- [Best practices do Codex](https://beta.openai.com/docs/guides/code/best-practices)
- [GitHub Copilot](https://copilot.github.com)
- [Azure OpenAI Service](https://aka.ms/azure-openai)
- [Minecraft Codex Sample](https://github.com/microsoft/MinecraftCodex)
- [Codex Babylon (TypeScript + BabylonJS)](https://github.com/microsoft/Codex-Babylon)
- [Wikipedia: Prompt Engineering](https://en.wikipedia.org/wiki/Prompt_engineering)
