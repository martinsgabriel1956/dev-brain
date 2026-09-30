# Como Fazer Perguntas Certas (e o Ciclo de 2 Horas)

Transcrição de vídeo em PT-BR de um desenvolvedor/líder técnico que explica como fazer boas perguntas no trabalho, quando pedir ajuda e a regra do **"ciclo de 2 horas"** usada na empresa dele. Autor e canal desconhecidos. Já em português — sem tradução. Título derivado do conteúdo. O vídeo usa um quadro/whiteboard (cores e desenhos citados na fala); a descrição visual está reconstruída a partir da narração.

> **Nota de limpeza:** a transcrição automática corrompeu alguns termos, corrigidos por contexto: "no pointer exception" → NullPointerException; "sior" / "Dev Senor" → sênior; "tên amarela" → linha amarela; "per programming" → pair programming; "techia" → tech lead (provável); "I" → IA; "chat EPT da Open AI" → ChatGPT da OpenAI; "pleno ou Dev Júnior ou até mesmo estagiário por não chega" → "…estagiário, por vezes, chega". Vícios de fala (é, ã, né, tá) removidos e pontuação reorganizada em parágrafos; o conteúdo não foi alterado.

## Abertura

Tecnologias mudam, requisitos mudam, frameworks, linguagens, pessoas, times, stakeholders e usuários mudam — tudo muda. Para ser eficiente, é preciso conseguir informação da melhor e mais rápida maneira possível, e o melhor jeito é **fazer as perguntas certas**. Perguntas têm boas intenções, mas, quando mal feitas, criam uma percepção errada e ruim sobre você.

## Dois tipos de pergunta

**Pergunta ruim.** Cenário: você é sênior, recebeu tarefas importantes, está focado e concentrado. Um pleno, júnior ou estagiário chega e diz:

> "Oi, o aplicativo está dando erro. Você pode me ajudar?"

**Pergunta boa (com empatia):**

> "Oi, estou tentando implementar o ticket 123 no aplicativo X. O erro é NullPointerException. Já vasculhei a possibilidade dessa variável estar nula e não consigo descobrir. Você já viu algo assim?"

O apresentador destrincha a versão boa:

1. **Contexto específico** — "estou tentando implementar o ticket 123 no aplicativo X".
2. **Erro exato e (idealmente) localização** — "NullPointerException". No Java é uma das exceções mais comuns numa linguagem orientada a objetos: usar um objeto nulo dispara o erro. Ele nota que seria ainda melhor informar a classe/local, mas mostrar o erro exato já é ótimo.
3. **O que já tentou** — "já vasculhei a possibilidade dessa variável estar nula e não consigo descobrir". Indiretamente diz: "estou te chamando porque de fato já tentei e não consegui resolver".

Conclusão: uma pergunta ruim **rouba o tempo do sênior**; uma pergunta boa **respeita esse tempo** — o sênior já chega sabendo o contexto e provavelmente resolve só de olhar o código. É a mesma coisa para quem trabalha em **suporte**: quem só diz "está dando erro aqui" obriga o suporte a pedir detalhes e conectar no cliente; se a pessoa traz tudo isso, a análise é muito mais rápida.

## Quando pedir ajuda: a gangorra

Muita gente tem medo de pedir ajuda. O apresentador observa dois cenários típicos:

- **Cenário 1 — o dev nunca pergunta.** Persiste sozinho por dias, perde a deadline, não tem update para dar na daily e não resolve o problema.
- **Cenário 2 — o dev pergunta demais.** Qualquer sinal de dúvida vira pergunta; não tenta pensar nem pesquisar. Com o tempo vira "um pesadelo pro time", "um fardo, um peso"; os colegas pensam "cara, tu não cala a boca, tu não tenta resolver".

Ele desenha isso como uma **balança/gangorra**: os dois extremos em vermelho, faixas amarelas de transição e o **meio-termo em verde — o equilíbrio**, onde a pessoa deveria estar. O que empurra cada um para um extremo é o medo: "se eu perguntar demais, sou incompetente" leva ao cenário 1 ("nunca pergunto nada"); quem pensa "peça ajuda sempre que possível" cai no cenário 2. **"O que toda empresa gosta é que você se mantenha estável, no meio."**

## O "ciclo de 2 horas"

Conceito que ele define como regra na empresa. Para tentar resolver a tarefa, em até 2 horas:

1. **Procurar código parecido ou uma funcionalidade** na qual se basear por proximidade — pesquisa interna, **10 a 15 minutos**.
2. **Ler a documentação** da empresa ou da linguagem, **ou questionar a IA** (ele não indica qual; cita que gosta do ChatGPT da OpenAI) — **5 a 10 minutos**.
3. **Tentar resolver por conta própria** — estudou, validou, verificou, agora codifica e faz uma tentativa; às vezes mesmo tendo encontrado o que queria não dá certo e é preciso ir ajustando o código — **30 a 70 minutos** (a fala fala em "uma hora" de tentativa).

Se não conseguir, **aí sim pede ajuda — e nunca deve passar dessas 2 horas**, "porque já vai ser atrasado e tarde demais, e eles vão pensar que tu não consegue resolver o problema". Passado o limite, entra o **quadrante vermelho: "peça ajuda com contexto"** — usando o formato da pergunta boa acima, saindo da "linha amarela da pergunta errada".

## Exceções (quadrante amarelo): pedir ajuda antes das 2 horas

"Tudo na vida tem uma exceção." Pode-se pedir ajuda antes de esgotar o ciclo quando:

- Há **deadline e urgência**.
- Você é **novato ou júnior** que recebeu uma tarefa urgente que, idealmente, não deveria acontecer (o tech lead não devia ter passado, mas acontece) — pede ajuda também com contexto.
- Está em **trabalho de equipe** em vez de tarefa individual — por exemplo em **pair programming**, em que se questiona sempre a dupla ("time global").

Essas são "exceções na vida do programador". A regra é a que ele usa e repassa ao seu time.

## Última dica: documente tudo o que aprendeu

> "Documente tudo o que você aprendeu."

Porque o que você fez vira **referência para situações futuras**, serve para **outras pessoas** e até para o **seu eu do futuro**.

## Fechamento

Resumo do apresentador: faça boas perguntas, dê-se bem com o time, decida em que ponto da gangorra quer ficar e trabalhe em ciclos de 2 horas. Ele diz que a empresa "faz parte da nossa vida, do nosso dia a dia" e que essa é uma forma usada lá que "vem dando muito certo". Pede like, comentário (se você usa o ciclo de duas horas) e se despede.
