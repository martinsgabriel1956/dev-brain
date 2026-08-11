# Vibe Coding de Jogos: Por que Uns Entregam em 1 Prompt e Outros em 8 — e os Estágios de um Produto

> Transcrição de vídeo. O autor investiga por que algumas pessoas conseguem vibe codar um produto ou jogo em poucos prompts e outras não, replica um jogo de golfe usando o modo agente do ChatGPT (voice mode / "Mega Brain"), e aproveita para apresentar um framework de estágios de maturidade de produto.

---

## A pergunta central

Por que algumas pessoas conseguem vibe codar um produto ou um jogo em **poucos prompts** e outras não? Isso é uma questão de **bom senso**, de **detalhe técnico** no prompt, ou de **confiança no modelo** que se está utilizando?

O gatilho foi um jogo que viralizou no Twitter. O relato (possivelmente um exagero/rage bait, segundo o autor) era de que o **Opus 5** fez o "snowboarder test" em **one shot** — um simulador de snowboard com física de deslizamento correta, sem defeitos visuais, já acertando tudo na primeira implementação (o modelo teria empatado com o Fable nesse teste). Outro caso citado: o **Fable 5** gerando um jogo jogável em um único passe.

Em contraste, um outro criador (The Prime) fez um jogo com o **Opus 5** (no plano Max) gastando **8 prompts** e cerca de **72 milhões de tokens no total** (~1 milhão de tokens de cache write, ~70 milhões de cache read). A maior parte do custo foi gasta tentando fazer o corpo e o swing do jogador não parecerem "insanos". Provavelmente usou Three.js — você bate na bolinha com o mouse e há física da bola, mas o fundo ficou ruim.

**A questão:** qual é a diferença? Como uma pessoa entrega em 1 prompt o que outra entrega em 8? É o modelo treinado com mais exemplos daquele tipo de jogo? É o prompt? É o bom senso?

---

## O experimento: replicar um MVP de golfe

O autor decide replicar um MVP de jogo de golfe (primeiro exemplo que viu na timeline), testando algumas coisas diferentes:

- **Modelo/ferramenta:** ChatGPT no **modo agente com voice mode** (apelidado de "Mega Brain"). *(Vídeo não patrocinado pela OpenAI — foi só o primeiro exemplo que apareceu na timeline.)*
- **Confiança máxima no modelo:** ativou o **full access** ("turn on full access"), dando acesso total ao computador — de propósito, para não encostar em nada e ver se o modelo se vira sozinho (ou destrói o computador, ou tudo dá certo).

### O prompt inicial (por voz)

Pedido resumido ao modelo:

- Construir um **jogo de golfe** usando a **Unreal Engine**.
- Controle do swing via **trackpad/mouse**; quando o jogador bate na bola, a bola viaja.
- Foco em três eixos: **objetos, cenário e atores**.
- **Câmera híbrida 2D/3D:** o jogo começa em **2D lateral** controlado pelo mouse; quando a bola começa a viajar no ar, o **POV passa a ser o da bola** (um *follow camera rig* preso à bola, exigindo posição observável da bola) até ela tocar o solo; ao tocar o solo, volta ao 2D.
- **Atores principais:** o *golfer* (jogador) e a **bola** (posição, velocidade, colisão, o "kick", física).
- Começar com interface simples e **iterar** depois.
- Fazer o setup completo do que for preciso para rodar a Unreal — com acesso total, pode baixar o que precisar.

### Atritos com o modo voz ("Mega Brain")

O modo agente por voz se mostrou **lento** e travou em pontos triviais:

1. Tentou criar um **work tree**, mas a pasta não tinha **Git** instalado nem repositório.
2. Ficou confirmando o ambiente e perguntando se devia cancelar ou seguir.
3. Descobriu que a **Unreal ainda não estava instalada** na máquina.

Por causa da lentidão, o autor **cancelou o modo voz**, copiou o mesmo prompt e **colou no modo texto** (sem o "Mega Brain"), e rodou `git init` manualmente no terminal.

### Execução no modo texto

- O agente ("Sol"/GPT) gerou o primeiro protótipo: **~1600 linhas de código**, "passo 5 de 5", primeiro protótipo pronto.
- Segundo objetivo dado: **instalar tudo o que precisa para rodar o jogo e testar** se está funcionando.
- Intervenções manuais necessárias: **criar conta e fazer login na Epic Games** (o autor não tinha conta) para o agente conseguir rodar a Unreal Engine.
- Primeira versão rodou: visão da bola funcionando, mas a bola "caiu no espaço" (sem cenário ao redor).

O autor observa: não considera "rodar o jogo" como um prompt separado — o agente escreveu o próprio script para rodar no Mac e testou o jogo end-to-end sozinho.

### Iterações seguintes

- **Prompt 2 — construir o mundo:** pedir um mundo ao redor do 2D, para não ficar flutuando no espaço, com experiência imersiva. Resultado com bug: o jogador se **teletransportava** para onde a bola caía, e caía num abismo. Ainda iterável até ficar bom visualmente.
- **Prompt 3 — integração com o celular:** jogar usando o **celular como controle**. A solução do agente: um servidor **HTTPS temporário / local no Mac**, comunicação **UDP apenas em localhost** direto para a Unreal — nenhuma porta do jogo aberta na rede; o servidor descarta pacotes inválidos e aplica um **token de sessão embutido no QR code** (token aleatório por execução), o Node valida e reduz os dados antes de encaminhar à Unreal, e não grava telemetria. Funcionou: o iPhone conectou pelo Safari e o **acelerômetro** do celular controlava o movimento da bola através do túnel dentro da rede local.

---

## Conclusões sobre vibe coding

- Com **3 prompts** o autor criou o jogo na Unreal, melhorou o universo e conectou o celular via acelerômetro. Acredita que **poderia ter sido tudo em 1 prompt**, principalmente se tivesse **fornecido os assets** (imagens/referências) — supõe que quem fez o jogo de referência forneceu imagens ou disse de onde pegá-las. No caso dele, o GPT criou o visual mais básico possível com componentes gráficos padrão.
- **A grande diferença entre quem entrega em 1 prompt e quem entrega em muitos:**
  - **Conhecimento do domínio** (aqui, criação de jogos).
  - **Bom senso** para saber o que pedir e como descrever (incluindo fornecer assets/referências).
  - **Colocar o modelo em loop:** "aquele teu único prompt na verdade vira 20, 30 prompts" — o modelo faz **teste end-to-end**, verifica se o jogo funciona e **itera até o resultado final**. Não é complicado; é dar o objetivo e deixar o agente iterar.
- **Custo do experimento:** consumiu ~**5% do limite semanal** da subscription do ChatGPT (começou o dia em 96% de uso disponível, terminou em 91%). Não mediu tokens de input/output porque estava na subscription, não na API. Pergunta em aberto: quanto custaria o equivalente via API.

---

## Framework: os estágios de maturidade de um produto

O autor apresenta um framework (não é framework JavaScript — é um modelo replicado dos produtos que ele criou) para definir o estágio de desenvolvimento de um produto. "Produto" aqui não precisa ser um SaaS — pode ser um jogo ou até uma empresa de serviços.

Dados de uma enquete com >1000 "techfounders" brasileiros:
- **67%** ainda **não colocaram produto no ar**.
- **31%** colocaram e **faturam menos de R$ 5.000**.
- **1,7%** passaram de R$ 5.000.

Diagnóstico do autor: o gargalo dos dois primeiros grupos **não é falta de técnica**, é **falta de definição do produto** e do que significa "estar pronto".

**Os estágios:**

- **Estágio 0 — Ideia validada:** validar o *problema* com clientes reais (entrevistas, waitlist, pré-venda). Quem está nos 67% está *antes* do estágio 0 — não tem nada no ar que alguém possa pagar.
- **Estágio 1 — Um estranho consegue usar:** um usuário aleatório cai no produto e consegue usá-lo (antes disso, tudo bem usar amigos/beta testers diretos).
- **Estágio 2 — Primeiros R$ 1.000** de clientes reais.
- **Estágio 3 — Recorrência:** exige identificar os **canais de distribuição** (deixar de depender de pessoas individuais aparecendo). Exemplos de canais do autor: YouTube (canal principal), Instagram (cortes/sketches virais — que dependem de bots em DM e de bom **SEO**, tanto para orgânico quanto para tráfego pago e para quem procura no Google), e **afiliados**.
- **Estágio 4 — R$ 5.000/mês** por pelo menos 2 meses seguidos.
- **Estágio 5 — US$ 100.000** (faturamento recorrente de ~US$ 8.300/mês).

**O gap entre o estágio 4 e o 5:** quem fatura R$ 5.000/mês recorrente, conhecendo seu canal de distribuição e com tudo tracado, já consegue calcular **CAC** (custo de aquisição de cliente) e, após 3–5 meses de recorrência, começar a estimar o **LTV**. O que impede escalar não é técnica — é **manter o CAC baixo enquanto aumenta o volume de leads frios** entrando na plataforma.

- Leads **quentes** (ex.: audiência do YouTube que já conhece o criador) têm CAC mais baixo e são o ponto de partida natural.
- O desafio é atingir alguém que **nunca ouviu falar de você** mantendo o CAC baixo. Nos primeiros meses o CAC não é 100% confiável.
- Uma vez com a fórmula pronta e chegando a R$ 5.000, a diferença para R$ 50.000 é essencialmente **reinvestir dinheiro** (com criatividade de marketing).
- Exemplo citado: Antônio (Real Oficial) teria tuitado que gasta ~R$ 100.000/mês em ads no cartão de crédito pessoal — já achou a fórmula; a diferença entre 50k e 100k/mês é manter o CAC baixo e reinvestir. Se o **LTV** e a **precificação** estão saudáveis, o **cash flow** flui.

---

## Contexto de mercado

- A demanda por software está **aumentando**, mesmo com a IA escrevendo código: pessoas fora da área de tecnologia estão vibe codando soluções — e essas soluções são código (scripts Python, JavaScript). Enquanto isso continuar, a demanda por software cresce.
- Está crescendo também o movimento de **transformar serviço em produto**: uma software house cria uma **orquestração de agentes** / um produto que replica soluções para o mesmo problema e vende isso como serviço (ex.: ligar para restaurantes e vender um software pronto). Analogia do autor: é como o boom inicial da web, quando se oferecia a comércios locais sair da lista telefônica ("livro amarelo") para ter um site — só que agora com IA.

---

## Citações

> "Aquele teu único prompt, na verdade, vira 20, 30 prompts, porque o modelo vai fazer teste end-to-end, vai verificar se o jogo tá funcionando e vai ficar iterando até chegar no resultado final."

> "Depende muito do conhecimento que tu tem sobre criar jogos. (...) O que importa mesmo é tu colocar ele em loop."

> "Não é falta de técnica — é falta de definição do teu produto, do que é ele estar pronto."

> "A demanda por software, por incrível que pareça, tá aumentando. (...) A IA tá escrevendo um script em Python, tá escrevendo um script em JavaScript — e enquanto isso continuar acontecendo, a demanda por software vai aumentar."

> "O que te impede de chegar num valor maior recorrente é manter o CAC baixo enquanto tu aumenta os leads frios entrando na tua plataforma."
