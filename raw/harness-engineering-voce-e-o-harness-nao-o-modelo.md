# Harness Engineering — "Você Não É Mais o Modelo, Você É o Harness"

Transcrição de vídeo (canal do autor não identificado por nome no material — autor se dirige ao público como "mava dev"). Já em português, sem necessidade de tradução — apenas reestruturada em markdown a partir de transcrição bruta em bloco único, sem pontuação/seções. Nomes próprios citados de ouvido pelo autor original e possivelmente distorcidos pela transcrição automática — mantidos como ouvidos, com identificação mais provável indicada entre colchetes quando razoavelmente inferível.

---

## A Frase Viral

"Você não devia mais estar promptando agentes de código, você devia estar desenhando loops que prontam seus agentes." Duas frases, 6,5 milhões de views. Quem escreveu foi Peter Steinberger [provável Peter Steinberger], criador do OpenClaw [o autor cita "opencla" — o canal já tem vídeo sobre OpenClaw]. Na semana anterior à gravação, a Anthropic publicou um guia oficial concordando com ele. E tem o caso de "Lang Shen" [nome citado de ouvido, identificação incerta], que pegou o mesmo modelo, os mesmos pesos, mudou só a infraestrutura ao redor, e saiu de fora do top 30 para o ranking 5 em benchmark.

Esse "algo" tem dois nomes: **harness engineering** e **looping engineering** (loop engineering). Este vídeo mostra o que eles são, por que importam mais que o modelo escolhido, e por que o espectador provavelmente já faz isso sem saber.

## O Que é Harness

**Harness** vem do inglês — o equipamento que conecta um cavaleiro ao cavalo, ou um alpinista à parede. No contexto de IA, harness é tudo que não é o modelo em si.

- **Analogia do motor:** o modelo é o motor; o harness é o resto do carro.
- **Analogia do andaime:** o engenheiro citado como "Aksai Patar" [nome citado de ouvido, identificação incerta] viralizou essa comparação com um post de 1,5 milhões de views no X — o andaime de construção é temporário e você não vê o produto final nele, mas o prédio acabado é inteiramente determinado pelo andaime durante a construção.

**Frase central do argumento:** *"If you are not the model, you are the harness."* Se você não é o modelo, você é o harness — ou seja, tudo ao redor do modelo (como o prompt é estruturado, quais ferramentas são dadas, como o contexto é gerenciado, como o próprio trabalho é verificado) é engenharia de harness.

## Erros Compostos: Por Que Agentes Falham Diferente de Código Imperativo

Ideia central (atribuída a um artigo lido pelo autor, citado como "Adios Money" [identificação incerta]): agentes de IA são processos de muitas etapas, e erros se compõem — uma pequena chance de erro em cada passo vira uma chance significativa de falha no resultado final.

Exemplo: um processo de 10 etapas, cada uma com 99% de chance de sucesso individual (excelente, quase perfeito). A chance de todas as 10 darem certo:

- **10 etapas:** 0,99¹⁰ ≈ **90,4%**
- **20 etapas:** 0,99²⁰ ≈ **81,8%**
- **50 etapas:** 0,99⁵⁰ ≈ **60%**

Entender como agentes falham (de forma composta, não binária) muda o que precisa ser construído no harness.

## Quatro Formas de Atacar Erros Compostos

1. **Mecanismos de verificação** — dar ao agente uma forma de checar o próprio trabalho antes de avançar para o próximo passo. Citado o criador do Claude Code (referido como "Bshine" [provável Boris Cherny]) afirmando que isso melhora a qualidade do output de **2 a 3 vezes** — não o modelo, o mecanismo de verificação.
2. **Checkpoints** — pontos onde o agente para e um humano (ou sistema automatizado) verifica antes dele continuar. Reduz a propagação do erro.
3. **Ferramentas corretas** — menos ambiguidade em cada etapa, menos chance de erro. Ponto contraintuitivo: **mais ferramentas não significa menos erro**.
4. **Contexto limpo** — quanto menos ruído no contexto, menor a chance de má interpretação do estado atual.

A verificação é o ponto que volta mais adiante — é o que separa "o loop que funciona" do "loop que queima tokens".

## Exemplo Concreto: Vercel

A Vercel (plataforma de deploy usada por devs, especialmente com IA) fazia um experimento interno com agentes: o agente tinha muitas ferramentas disponíveis e a performance estava ruim. A decisão intuitiva seria adicionar mais ferramentas para aumentar capacidade — a Vercel foi na direção contrária: **removeu 80% das ferramentas disponíveis**, e a performance melhorou. Motivo: em cada etapa o agente passou a escolher entre menos opções, com menos espaço de decisão e, portanto, menos chance de escolher errado.

**Conclusão do exemplo:** harness não é sobre maximizar capacidade, é sobre otimizar o caminho até o resultado certo.

## Exemplo Concreto: Claude Code

O criador do Claude Code documentou publicamente o que faz diferença no harness da ferramenta:

- Dar ao modelo uma forma de verificar o próprio trabalho (rodar testes, checar se o arquivo existe, verificar se o output faz sentido) — melhora a qualidade de 2 a 3 vezes.
- Estrutura clara de quando parar e pedir confirmação antes de continuar — o agente não decide sozinho quando escalar; o harness define isso.
- Contexto sobre o projeto (arquitetura, convenções, o que nunca fazer) para qualquer tarefa.
- Separação clara entre planejar e executar — o agente não planeja e executa na mesma passagem; planeja em uma fase, executa em outra.

## Ralph Loop: a Origem "Boba" do Loop Engineering

Em julho de 2025, o engenheiro australiano **Geoffrey Huntley** publicou uma técnica descrita como "tão simples que parecia piada": uma linha de bash que pega o prompt, manda para o agente e roda em loop — se não terminou, roda de novo. Batizou de **Ralph Loop**, em homenagem ao Ralph Wiggum, personagem d'Os Simpsons descrito como o mais "burro" da série — porque é uma técnica muito simples. A lição destacada: com IA não é sobre complexidade — é fazer o simples, "como jogar futebol".

Um ano depois, essa "piada" virou disciplina: em julho (do ano da gravação), a **Anthropic** publicou um guia oficial, "Getting Started with Loops".

## Os Quatro Níveis de Loop (Guia Oficial da Anthropic)

A cada nível, mais responsabilidade é entregue ao agente:

1. **Turn-based** — cada prompt enviado já é o próprio loop: o agente coleta contexto, age, executa, checa, repete e responde. O humano dirige cada rodada/turno. É o que a maioria já faz hoje.
2. **Goal-based** — o humano entrega a condição de parada (ex.: "roda até esses testes passarem", "roda até o build compilar"). O agente não para quando *acha* que terminou — para quando o critério objetivo é atingido.
3. **Time-based** — o humano entrega o gatilho (trigger); o loop roda em intervalo ou agendado, sem presença humana.
4. **Proactive** — o humano entrega só o prompt; o sistema observa e decide o quê e quando agir.

**A relação entre os dois termos:** harness engineering é o que você constrói ao redor do modelo; loop engineering é como isso roda sem você. Analogia: o harness é o carro, o loop é o piloto automático.

## Contraponto: o Gargalo do Loop é o Verificador, Não o Modelo

Razão pela qual o autor não fez o vídeo no auge do hype: no looping, o gargalo não é o modelo, é o verificador. Voltando à matemática dos erros compostos — com 50 etapas a chance cai para 60%. Se o humano é retirado da frente e o processo roda a noite inteira **sem** um critério de sucesso objetivo (teste, build, benchmark), o resultado não é um loop funcional — é um "Chevete/Opala queimando gasolina", isto é, o agente queimando tokens sem produzir valor.

**Frase-resumo do contraponto:** loop engineering sem mecanismo de verificação só faz a conta de API ficar mais cara sem entregar nada.

## Doze Componentes do Harness (Sete Cobertos no Vídeo)

O autor cita a existência de 12 componentes de harness e cobre 7 considerados mais importantes:

1. **System prompt** — não é o "você é um assistente útil" de 2025; é o caráter do agente, seus limites, suas convenções, o que nunca fazer. É a "constituição" do agente.
2. **Ferramentas** — o que o agente pode fazer. Aplica a lição da Vercel: menos ferramentas bem escolhidas supera todas as ferramentas possíveis.
3. **Gestão de contexto** — o que o agente tem acesso, qual a janela de contexto (que tem limite), o que incluir e o que descartar. Decisão de engenharia, não do modelo.
4. **Mecanismos de verificação** — como o agente checa se o que fez está correto antes de avançar. Componente com o maior retorno comprovado; decide se o loop dá certo.
5. **Memória** — o que persiste entre sessões. Sem memória, o agente recomeça do zero a cada interação do loop; com memória estruturada, cada rodada aprende com a anterior.
6. **Sandboxes** — ambiente isolado para executar código, testar outputs, fazer chamadas de API sem afetar produção nem expor dados sensíveis. Menos obrigatório para trabalho local; obrigatório em grandes empresas antes de deixar qualquer loop rodar sem supervisão.
7. **Hooks** — pontos definidos em que um humano ou sistema automatizado intervém. Não é o agente decidindo quando escalar — é o harness definindo isso explicitamente.

## Dado de Benchmark: o Mesmo Modelo, Harness Diferente, Resultado Diferente

O mesmo Claude Opus performa significativamente melhor dentro do harness do Claude Code do que em benchmark padrão sem harness. Mesmo modelo, harness diferente, resultado diferente.

## Você Provavelmente Já Faz Isso Sem Saber

Harness engineering não é algo totalmente novo para quem já segue certas práticas — o autor mapeia práticas já cobertas no canal:

- **CLAUDE.md** — tempo escrito nas convenções do projeto, o que nunca fazer, como estruturar o código: já é o system prompt, já é o caráter e as restrições do agente.
- **Spec-driven development** — escrever a spec antes de pedir para codificar é a separação clara entre planejar e executar (pode ser feito via ferramenta de planejamento dedicada ou por conversa com o próprio agente decidindo um plano). Também funciona como checkpoint humano entre planejar e começar a executar.
- **TDD** — escrever os testes antes de pedir a implementação. Não precisa ser manual, só é preciso garantir que o agente sabe o que vai ter que testar antes de começar a executar. Ponto destacado como especial: os testes escritos antes não são só verificação — são a **condição de parada de um loop**. Mandar o agente "rodar até os testes passarem" só funciona se os testes já existirem antes do código. Quem já faz TDD já tem o pré-requisito do nível 2 da escada de loop (goal-based) — falta só apertar o play.

**A diferença entre "usar IA" e "usar IA bem" é o harness já construído ao redor — a maioria nunca pensou nisso explicitamente, mesmo já fazendo há bastante tempo.**

## Como Usar o Framework Sem Precisar Pensar Muito

A grande chave da área é evitar tomada de decisão repetida para que tudo seja feito da melhor forma possível. Em vez de perguntar "qual modelo é melhor?", a pergunta correta vira: **"o que no meu harness está causando esse tipo de falha?"** — e, antes de deixar algo rodar sozinho: **"qual é minha condição de parada?"**

### Quatro Perguntas para Diagnosticar e Evoluir o Harness

1. **Onde o agente falha mais?** Cada tipo de falha aponta para um componente diferente a melhorar:
   - Falha de interpretação → system prompt.
   - Falha de execução → ferramenta ou sandbox.
   - Falha de consistência → memória.
   - Falha que se propaga → verificação.
2. **O agente tem como verificar o próprio trabalho?** Se não, adicionar — maior retorno documentado (2 a 3x), conforme já citado sobre o Claude Code.
3. **Que contexto o agente não tem, mas deveria ter?** Às vezes a falha não é do modelo — é informação que está na cabeça do autor da tarefa mas não está documentada em nenhum lugar (nenhum `.md`) que o agente possa consultar.
4. **Qual tarefa tem critério de sucesso 100% objetivo?** (testes que passam, build que compila) — essas são candidatas ao primeiro loop. Começar pequeno, com sandbox, e observar a tendência.

**Conclusão final:** a tendência natural é trocar de modelo quando as coisas não funcionam — mas o caso "Lang Shen" citado no início sugere que essa é frequentemente a resposta errada. Antes de trocar de modelo (ou pagar mais por um modelo mais novo), investir no harness; antes de acelerar o looping, investir nos mecanismos de verificação.

## Encerramento do Vídeo (CTA, fora do escopo técnico)

O autor anuncia material avançado só de harness engineering (link na descrição, lista de e-mail) e convite para virar membro do canal, citando como conteúdo exclusivo um curso de programação funcional com DDD.
