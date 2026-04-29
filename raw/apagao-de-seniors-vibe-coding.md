# Apagão de Devs Sêniors e Vibe Coding — Como Garantir Qualidade no Código da IA

> Transcrição de vídeo sobre os riscos do vibe coding para o mercado de desenvolvimento e técnicas práticas para garantir qualidade no código gerado por IA.

---

## O Alerta

Tweet do Poker Dev que motivou o vídeo:

> *"Rapaz, se o Vibe Coding realmente virar padrão, a gente vai criar um apagão de sêniors. Menos gente aprendendo fundamentos e mais gente só orquestrando prompts. Daqui alguns anos, sistemas complexos com performance, confiabilidade, segurança e arquitetura vão ficar caros e muito arriscados de manter."*

Os quatro pilares mencionados — **performance, confiabilidade, segurança e arquitetura** — são o fio condutor deste vídeo.

---

## O Contexto: Custo da IA e o "Apocalipse"

Há sinais de que as empresas de IA estão começando a limitar acesso e degradar modelos gradualmente:

- O Opus 4.6 foi aparentemente "nerfado" sem aviso — ficou menos capaz de repente
- O Opus 4.7, lançado como substituto, é percebido como pior que o 4.6
- A Anthropic está adicionando controles de usage (plan usage, cotas visíveis) preparando o terreno para cobrar mais
- Parâmetros como `thinking budget` e `effort level` estão sendo progressivamente removidos do controle do usuário ("adaptive thinking" — o modelo decide quanto pensar)
- Novos níveis de esforço foram adicionados: low → medium → high → extra high → max

**Hipótese:** não é que o 4.7 é pior — é que as ferramentas que dão acesso ao 4.7 estão cada vez mais restritas para reduzir custo de inferência.

**Conclusão prática:** agora é o melhor momento para usar IA ao máximo. Daqui a pouco fica mais caro ou mais restrito. Use para construir projetos que gerem renda extra.

---

## O Conhecimento que Protege

Se a IA evaporar amanhã, quem souber os fundamentos abaixo volta a escrever código sem problema. É como andar de bicicleta — a memória muscular volta em meses.

Os quatro pilares para garantir que o código da IA tem qualidade real:

1. **Performance** — detectar N+1, memory leaks, flame graphs
2. **Confiabilidade** — testes de falha, race conditions, property-based testing
3. **Segurança** — dependency scanning, secret scanning, supply chain attacks
4. **Arquitetura** — conhecer o diagrama do sistema e seus tradeoffs

---

## Técnica 1 — Detector de N+1 (Performance)

**O problema:** LLMs adoram fazer loops chamando queries individuais em vez de usar batch ou JOIN. No ambiente de dev com 100 requests ninguém percebe. Em produção com 10.000 requests, cada um fazendo 20 queries = 200.000 queries no banco.

**A solução:** um middleware que conta queries por request.

```python
# Pseudocódigo — adapte para sua stack (Django, Node, Prisma, qualquer ORM)
def query_counter_middleware(request, next):
    query_count = 0

    # hook no ORM que incrementa query_count a cada query
    with count_queries() as counter:
        response = next(request)
        query_count = counter.total

    if query_count > THRESHOLD:  # ex: 15
        log.warning(f"N+1 detectado: {query_count} queries em {request.path}")
        flag_for_review(request)

    return response
```

**Implementação:** plante esse hook no middleware da sua stack. Se o ORM suportar hooks (Django, Prisma, ActiveRecord), é simples de instrumentar. Rode em dev e staging — vai ser surpreendente quantos warnings aparecem.

---

## Técnica 2 — Detectar Race Conditions (Confiabilidade)

**O problema:** LLMs constroem sequências assíncronas sem considerar duas requests chegando ao mesmo tempo. Resultado: saldo negativo, double booking, contador errado, deadlock.

**A solução:** Property-Based Testing.

Em vez de testar "dado input X, espero output Y":
- Você define uma **propriedade** que deve ser verdadeira no final (ex: "o saldo nunca deve ser negativo")
- A biblioteca bombardeia a função com inputs aleatórios e concorrentes
- Se a propriedade for violada em alguma combinação, o teste falha

**Bibliotecas por stack:**

| Stack | Biblioteca |
|---|---|
| Python | `hypothesis` |
| JavaScript/Node | `fast-check` |
| Haskell | `QuickCheck` (original) |
| Java | `jqwik` |
| Go | `gopter` |

**Exemplo com Hypothesis (Python):**

```python
from hypothesis import given, strategies as st
from hypothesis.stateful import RuleBasedStateMachine

@given(st.integers(min_value=0, max_value=1000))
def test_saldo_nunca_negativo(valor_deposito):
    conta = Conta()
    conta.depositar(valor_deposito)
    conta.sacar(valor_deposito)
    assert conta.saldo >= 0  # propriedade que nunca deve ser violada
```

---

## Técnica 3 — Memory Leak Detection (Performance)

**O problema:** uma fila que nunca esvazia, um cache em memória sem TTL. Em dev: invisível. Em prod: memória sobe de 200 MB para 2 GB até o OOM killer derrubar tudo.

**Ferramentas por plataforma:**

| Plataforma | Ferramenta |
|---|---|
| Android | LeakCanary + testes instrumentalizados |
| Android/iOS | Sentry Performance Monitor |
| Python | `py-spy` — monitora processo vivo sem reinicializar |
| Chrome/Node | Chrome DevTools → Memory → Heap Snapshot |
| Go/C++ | `pprof` + visualização no Chrome |

**Fluxo básico:**

1. Rode o profiler em cima do processo vivo (`py-spy top --pid <PID>`)
2. Capture snapshots de heap ao longo do tempo
3. Compare snapshots: se objetos sem referência estão acumulando na heap, você tem um leak
4. Use flame graphs para visualizar onde a memória está sendo alocada

**Sinal de alerta:** memória crescendo continuamente sem se estabilizar ao longo do tempo de execução.

---

## Segurança

Três práticas mínimas para código gerado por IA:

### 1. Dependency Scanning
Verifique vulnerabilidades conhecidas nas bibliotecas que a IA adicionou. Rode no GitHub Actions a cada PR:

```yaml
# GitHub Actions — verificação de CVEs
- name: Audit dependencies
  run: npm audit --audit-level=high  # ou pip-audit, bundler-audit, etc.
```

### 2. Secret Scanning
Garanta que a IA não commitou credenciais no código:

```bash
# Ferramentas
gitleaks detect --source .
truffleHog git file://. --only-verified
```

### 3. Supply Chain Attacks — Pinagem de Versões
Sempre fixe versões exatas de dependências. Muitos supply chain attacks exploram ranges de versão (`^1.0.0`, `>=1.0.0`):

```json
// package.json — RUIM
"express": "^4.18.0"

// package.json — BOM
"express": "4.18.2"
```

---

## Arquitetura — Conheça os Tradeoffs

A pergunta certa não é "qual é a melhor arquitetura?". É **"qual é o tradeoff da sua arquitetura?"**

Toda arquitetura deixa algo na mesa. Sempre. Não existe arquitetura boa em tudo. Quem sabe nomear o que está sendo sacrificado — e por que — é quem tem conhecimento real de arquitetura.

**Checklist mínimo:**

- [ ] Você tem um diagrama atualizado do sistema?
- [ ] Você sabe quais são os tradeoffs da arquitetura atual?
- [ ] Você sabe o que acontece se o banco de dados cair no meio de uma request?
- [ ] A IA considerou os cenários de falha ao escrever o código?

---

## Confiabilidade — Testes de Falha

A IA escreve código para o caminho feliz. Você precisa verificar o que acontece nos caminhos de falha:

- O que acontece se o banco de dados cair no meio de uma transação?
- O que acontece se o serviço externo retornar timeout?
- O que acontece se a fila de mensagens ficar indisponível?
- O que acontece se dois usuários executarem a mesma operação simultaneamente?

Se você não sabe responder essas perguntas sobre o código que a IA gerou, o código não está pronto para produção.

---

## Resumo — O Kit de Sobrevivência

| Pilar | Técnica |
|---|---|
| Performance | Middleware contador de N+1 queries por request |
| Performance | Profiling de memória com py-spy / LeakCanary / pprof |
| Confiabilidade | Property-based testing com Hypothesis / fast-check |
| Confiabilidade | Testes de falha para cenários extremos |
| Segurança | Dependency scanning (npm audit, pip-audit) |
| Segurança | Secret scanning (gitleaks, truffleHog) |
| Segurança | Pinagem de versões de dependências |
| Arquitetura | Diagrama atualizado + tradeoffs documentados |
