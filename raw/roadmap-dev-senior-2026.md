# Roadmap Dev Sênior 2026 — 5 Pilares Fundamentais

**Fonte:** Vídeo (transcrição)
**Contexto:** Como alcançar sênior em 2026 com IA mudando o mercado

---

## Contexto

Com IA, qualquer dev gera código funcional. A régua subiu. Quem só executa virou commodity. Quem pensa em sistemas, toma decisões técnicas e sabe o *porquê* do código nunca foi tão valorizado.

Esse roadmap não é sobre linguagem ou framework. É o que fica quando tira tudo isso da jogada.

---

## Pilar 1 — Pensar antes de codar

O mais fundamental de todos.

Antes de qualquer linha de código: entender o problema. A maioria pula isso, abre o editor, e só descobre que entendeu errado quando já tem uma solução errada.

**Sub-tópicos:**
- **Vocabulário técnico** — acoplamento, abstração, estado. Entender o *porquê* desses termos existirem.
- **Quebra de problema** — pegar um problema grande e dividir em etapas menores executáveis.
- **Lógica como disciplina** — não só `if/else`. Lógica como fluxo de decisão e estado.

---

## Pilar 2 — Entender o que seu código faz de verdade

Você escreve (ou pede pra IA escrever) uma função. Ela funciona. Mas o que acontece quando roda? Memória alocada, CPU processando, dados navegando por estruturas.

A maioria tem uma caixa-preta entre o código e o sistema que executa.

**Sub-tópicos:**
- **Abstração** — camadas que escondem complexidade sem esconder clareza.
- **Estruturas de dados** — array, hash, pilhas, filas. Não só o que são: quando usar e quando *não* usar.
- **Performance e Big O** — vai além de matemática. Dita as consequências das suas decisões de estrutura.
- **Memória e execução** — entender o que o código faz quando é executado de verdade.

---

## Pilar 3 — Pensar em sistema, não em arquivos

Diferença entre código que funciona e sistema que funciona:
- Código funciona quando passa nos testes.
- Sistema funciona com milhares de usuários simultâneos, volume triplicando, inputs inesperados.

**Sub-tópicos:**
- **Modelar antes de codar** — fluxo de dados, responsabilidades, antes de abrir o editor.
- **Back-end** — não ser especialista, mas entender *por que* cada arquitetura existe e o que ela resolve.
- **Banco de dados** — cada banco é uma decisão que altera a forma de construir o sistema.
- **Acoplamento e dependências** — maior gargalo quando sistemas crescem.

---

## Pilar 4 — Entender sistemas em produção

Sistemas em produção se comportam diferente do que em desenvolvimento.

Em produção: usuários fazem o inesperado, picos de acesso, dados corrompidos que passaram por todas as validações, dependências externas que param de responder.

**Sub-tópicos:**
- **Como sistemas crescem e onde quebram** — entender o crescimento descontrolado e sem estrutura.
- **Debugging e observabilidade** — logs, métricas, ler o sistema como um sistema vivo.
- **Monolito vs microsserviços** — quando cada um faz sentido e, mais importante, quando *não* faz.

---

## Pilar 5 — Usar IA sem depender 100% dela

Usar IA todo mundo usa. Esse pilar é sobre usar de um jeito que te torne mais capaz, não mais dependente.

**A armadilha:** quanto mais você usa IA sem entender o que ela gerou, menos você consegue avaliar se aquilo é bom. É um ciclo de degradação de competência — acontece devagar, você não percebe até não conseguir resolver nada sem IA.

**Sub-tópicos:**
- **Validar código gerado por IA** — não é só testar se funciona. Avaliar se vai escalar, se vai parar daqui um tempo, se é bom dentro do contexto do seu sistema.
- **Pensamento crítico em equipe** — questionar sugestões da IA, de colegas, de documentação, sem parecer um bicho de sete cabeças.
- **Testes como validação real** — com geração massiva de código por IA, testes são um seguro contra decisões ruins (da IA e suas).
- **Git e versionamento** — quando você não entende o código gerado, o histórico de versão é o único lugar pra voltar em caso de bug crítico.

---

## Como usar o roadmap

Não percorra em ordem necessariamente. Olhe e pergunte: **onde estou agora?**

| Situação | Por onde começar |
|---|---|
| Trava no básico | Pilar 1 |
| Coda bem mas não explica decisões | Pilar 3 |
| Gera código com IA mas não explica o porquê | Pilar 5 |

---

## Próximos passos (série de vídeos)

Próximo vídeo: Pilar 1 — vocabulário técnico. Não sintaxe, não decorar termos. Entender o que significa abstração, acoplamento, estado. Sem isso: não entende documentação, não participa de discussão técnica.
