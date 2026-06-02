# Os 7 Níveis de Como Engenheiros Usam IA — Por Que os Estudos de Produtividade Medem o Nível Errado

**Fonte:** Transcrição de vídeo (YouTube)  
**Autor:** Valdemar Neto (cofundador da Tech Leads Club)  
**Data de publicação:** desconhecida  
**Idioma original:** Português (Brasil)

---

## Por que os Estudos de Produtividade Estão Errados

A maioria dos estudos que diz que IA aumenta produtividade em 20–30% está **medindo o nível errado**. Eles mediram devs no nível 1 e no nível 2 de uma escala de 7.

A diferença entre um dev nível 2 e um dev nível 4 com a **mesma ferramenta** não é de 20% — é de aproximadamente **5 vezes mais**. E não porque o nível 4 digita mais rápido: é porque ele faz um trabalho **fundamentalmente diferente**.

---

## O Framework: Escala de 7 Níveis

Criado (ou documentado) por **Steve**, ex-Google e ex-Amazon. O ponto central da escala:

> O que muda de nível para nível não é a ferramenta — é o **modelo mental**. Como você pensa e como você usa as ferramentas.

E há uma regra importante: **não dá para pular níveis**. Cada um exige o anterior — não por causa da ferramenta, mas porque o modelo mental necessário precisa ser construído progressivamente.

---

## Os 7 Níveis

### Nível 0 — O Negacionista

Não usa IA. Acredita que é moda passageira, que escrever código na mão é melhor, que vai "ficar burro" se usar.

**Realidade:** Os devs ao redor estão ficando muito mais produtivos. Em comparação, você está ficando mais lento. Essa posição vai machucar sua carreira — não porque IA é mágica, mas pelo delta de produtividade relativa.

---

### Nível 1 — O Cauteloso

Usa **autocomplete na IDE**. Aceita ou rejeita sugestão por sugestão. Copilot básico, Cursor no modo simples.

É melhor que nada, mas você está usando ~5% das capacidades disponíveis.

---

### Nível 2 — O Perguntador

Usa o **chat da IA para tirar dúvidas**: "como fazer X em Python?", "qual a diferença entre A e B?".

Essencialmente substituiu o Stack Overflow — mais rápido, mais contextual. Mas você ainda faz **100% do trabalho**. A IA só responde perguntas.

---

### Os Três Primeiros Níveis em Perspectiva

Nos níveis 0, 1 e 2, a IA **não mudou fundamentalmente como você trabalha**:

- Você ainda é o único que pensa
- Você ainda decide e implementa tudo
- Você apenas ganhou uma ferramenta nova na caixa

---

### ⚠️ O Grande Gargalo: Transição do Nível 2 para o Nível 4

> A maioria dos devs trava exatamente aqui.

---

### Nível 3 — O Delegador Básico

Começa a **pedir para a IA escrever código**. Faz uma função de cada vez, copia e cola, adapta manualmente.

É um salto, mas o ciclo é lento: você ainda microgerencia cada linha, valida manualmente cada output. O ritmo é o dev pedindo → IA gerando → dev validando → dev adaptando → repete.

---

### Nível 4 — O Diretor *(o salto mais importante)*

O modelo mental muda completamente.

**Nível 3:** "Escreve uma função que valida CPF."  
**Nível 4:** Você escreve um arquivo de testes definindo todos os casos — CPF válido, inválido, com máscara, sem máscara, casos de exceção, CPF internacional — e pede para a IA **implementar** para satisfazer os testes. Então vai para a próxima tarefa enquanto a IA trabalha.

A transição:
- De: microgerenciador de código
- Para: especificador de comportamento e validador de resultado

**Por que a maioria não chega ao nível 4?**

Requer dois atributos que levam tempo para construir:

1. **Confiança** — para deixar a IA trabalhar sem microgerenciar
2. **Contexto** — você precisa conhecer seu sistema o suficiente para escrever uma spec que faça sentido

> *Paradoxo: o nível 4 exige **mais** conhecimento de domínio, não menos — mesmo que você esteja delegando mais tarefas.*

---

### Nível 5 — O Orquestrador

Ferramentas como Claude Code (agent mode), Cursor agent mode.

A IA não só escreve código — ela **navega o projeto, lê arquivos, roda testes, corrige erros**. Você define a tarefa de alto nível e ela executa.

O modelo mental: você é um tech lead dando direção para um junior.

---

### Nível 6 — Os Multi-Agentes

Roda **múltiplos agentes em paralelo**, cada um em uma tarefa diferente.

Referência: Boris Cherny (criador do Claude Code) documenta seu workflow com cinco terminais abertos, cada um com um agente trabalhando em paralelo.

O modelo mental: **engineering manager** — você gerencia, revisa, prioriza.

---

### Nível 7 — O Arquiteto

Raramente toca em código.

Define:
- Arquitetura do sistema
- Contratos de API
- Especificações do sistema
- Critérios de qualidade

Os agentes constroem tudo. O trabalho do arquiteto é pensar no **design do sistema inteiro** — quase impossível sem ter dominado os seis níveis anteriores.

---

## O Paradoxo Central

> Quanto mais alto o nível, **mais skill você precisa** — não menos.

| Nível | Skill adicional necessária |
|---|---|
| 5 | Entender sistemas |
| 6 | Saber gerenciar times |
| 7 | Visão arquitetural de Staff/Senior+  |

**Consequência direta:**

- Dev ruim com IA → faz coisas ruins mais rápido
- Dev bom com IA → faz coisas muito melhores muito mais rápido

A IA não substitui o skill — ela **amplifica o skill que você já tem**.

---

## Onde o Autor Está

Nível 6 — começando a usar multi-agentes no trabalho. Agente navega o codebase, implementa features, roda testes. Ainda executando um agente por vez; testando orquestração de múltiplos agentes em paralelo (com Tmux + Obsidian para contexto compartilhado).

---

## Recomendações Práticas por Nível

| Você está em... | Próximo passo |
|---|---|
| Nível 2 | Delegue um tipo de tarefa inteira — ex.: escreva a spec de um teste e deixe a IA escrever os testes |
| Nível 3 | Escreva uma spec completa para a próxima feature; defina os testes primeiro; avalie a qualidade do output |
| Nível 4 | Use Claude Code por uma semana numa tarefa real; deixe ele navegar o código sem microgerenciar cada arquivo |

**Regra:** você não precisa ir do nível 2 ao nível 7 em uma semana. Cada nível leva tempo. O que você não pode é **ficar no mesmo nível para sempre**.
