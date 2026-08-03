# As 5 Escolas de Como Programar com IA

> Transcrição de vídeo do YouTube, canal Mano Deivin (autoidentificado no vídeo como "Deivin do canal Mano Davi" `[transcrição incerta sobre o nome exato do canal]`). Idioma original: português — sem necessidade de tradução. Texto abaixo reorganizado em seções e com pontuação corrigida para legibilidade; a ordem e o conteúdo das ideias foram preservados. Trechos de nomes próprios com grafia incerta na transcrição automática foram marcados com `[transcrição incerta]` e, quando possível, resolvidos por contexto (ex.: sobrenomes de figuras públicas conhecidas do meio tech) — a resolução em si também fica marcada como inferência, não como certeza absoluta.

## Abertura (bloco publicitário)

Abertura com um anúncio de um serviço de gestão de impostos para PJ ("Conta Deve o Leão") — sem relação com o tema técnico do vídeo, mantido apenas por integridade da transcrição.

## Introdução: o conflito de escolas

O apresentador descreve um cenário comum: você abre o Cloud Code, o Cursor, ou qualquer outro editor/harness agêntico (OpenCode, etc.) e ouve vozes conflitantes sobre a forma "certa" de programar com IA — um defende usar só autocomplete, outro defende usar agentes para tudo, um terceiro defende não usar IA nenhuma, e um quarto deixa um agente rodando sozinho de madrugada, gastando tokens de API enquanto dorme.

A tese central do vídeo: **não existe consenso**. Inclusive duas referências importantes do meio — que o autor chama de "Illuminatis" — que pregavam fazer tudo na unha e não terceirizar o cérebro para a IA, mudaram de lado nos últimos 6-12 meses.

O autor diz ter pesquisado e mapeado **cinco escolas** de pensamento sobre como programar com IA — cada uma com defensores fortes, e algumas se odeiam entre si.

## O framework do Andrej Karpathy: "Autonomy Slider"

Antes de descrever as escolas, o autor credita a [[Andrej Karpathy]] (autor do termo "vibe coding") por uma ideia organizadora: o **autonomy slider** — um controle deslizante de volume, como o de um rádio antigo, que regula o quanto de "rédea" você solta para a IA.

- Volume no mínimo → a IA só sugere ("dá uma tossidinha de solução"), e quem implementa é o humano.
- Volume no máximo → você diz "faz o que você quiser" e a máquina se vira sozinha.

Cada uma das cinco escolas ocupa um ponto diferente nesse controle — nenhuma escola é "a certa" isoladamente, cada uma é uma posição no slider.

Frase citada de Karpathy, parafraseada pelo autor: **"Você até consegue terceirizar o seu pensamento; agora, o seu entendimento, isso não dá para passar pra frente."**

## Escola 1 — IA como Copiloto ("você dirige")

Extremo mais conservador do slider. Representada por ferramentas como Cursor e GitHub Copilot — o próprio nome "Copilot" já é a tese: a IA senta ao lado, aponta o caminho, mas quem tem a mão no volante é o humano.

- O humano revisa cada sugestão, aceita ou rejeita, trabalha em paralelo com a IA.
- Justificativa citada: LLMs alucinam — inventam funções que não existem, "com a maior cara de pau".
- O autor observa que, apesar de essa escola parecer "coisa de 2023" à primeira vista, ela continua tendo defensores ativos hoje (2026).
- Ponto de atrito citado: [[Fábio Akita]] teria dito ao autor, em conversa/vídeo, que essa abordagem (só autocomplete revisado) já estaria datada — "isso é coisa de 2023" `[transcrição incerta sobre o contexto exato da fala de Akita]`.

## Escola 2 — Delegação Total a Agentes

Extremo oposto da Escola 1. O dev para de digitar código linha a linha e passa a atuar como "gerente" de um agente que trabalha em velocidade muito mais alta — terminal agêntico, Claude Code e afins.

Citações atribuídas:

- **Thorsten Ball** `[transcrição incerta sobre o nome exato — soou como "Thor Torstenbau"]`, criador de um agente chamado **AMP**: "o agente escreve uns 70-80% do código, eu só faço commit — quase não escrevo nada na mão."
- **Steve Yegge** `[transcrição incerta — soou como "Steve Egg"]`: o trabalho do dev vai virar majoritariamente "babá de agente" (pouco código escrito na mão, supervisão constante de múltiplos agentes rodando em paralelo).

### Variante mais madura: Spec-Driven Development

Em vez de soltar um prompt solto, o dev escreve uma especificação bem estruturada, e o agente constrói a partir dela.

- **Sean Grove** (OpenAI): "a especificação é o artefato valioso; o código é só uma projeção dela." O documento importa mais que o código gerado a partir dele.

### A virada de lado dos dois "Illuminatis"

- **DHH** (David Heinemeier Hansson, criador do Ruby on Rails): em 2025, dizia sentir "a competência escorregando para fora dos dedos", comparando IA-para-programar com nunca aprender a tocar violão de verdade — postura clara de "anti-agente raiz". Seis meses depois, segundo o autor, DHH virou "agent first": começa toda tarefa já delegando a um agente, chama escrever código na mão de "tediosa", e compara usar agente a "vestir uma armadura".
- **Antirez** (Salvatore Sanfilippo `[transcrição incerta sobre o sobrenome exato]`, criador do Redis): no começo de 2026, publicou um post (segundo o autor, virou referência para a comunidade "anti-agente") intitulado algo como "não use agente, escreva código na mão" — argumentando que agentes deixam a base de código frágil e inchada. Pouco tempo depois, reverteu publicamente a posição, escrevendo que "recusar usar agente não vai ajudar você nem sua carreira", passou a usar o Claude Code de forma intensiva, e batizou sua prática de **"automatic programming"**.

O autor usa essa reviravolta dupla (DHH e Antirez) como argumento central do vídeo: se as referências mais citadas de cada lado não sustentam a própria opinião por 12 meses, ninguém deveria se sentir "errado" por estar confuso sobre qual escola seguir.

### O princípio que Antirez levou consigo ao trocar de lado

Ao migrar de "anti-agente" para "automatic programming", Antirez preservou uma distinção importante entre dois conceitos que o autor trata como opostos:

- **Automatic programming**: usar um agente com direção e critério de qualidade — o código gerado, mesmo que a mão que digitou tenha sido a da IA, é *seu*, porque você entendeu e é dono da decisão.
- **Vibe coding**: aceitar o que a máquina cospe sem entender — nesse caso, mesmo que você use o agente, você deixa de ser dev e "vira um despachante de código" ("sabor dev" — trocadilho do autor com "sabor" + "dev").

## Escola 3 — "Na Unha" (sem IA)

A escola mais coerente do vídeo, segundo o autor — e, ao mesmo tempo, a que está sendo abandonada por seus próprios fundadores.

Base teórica citada: **Peter Naur**, no artigo de 1985 *"Programming as Theory Building"* (traduzido livremente como "Programação como Construção de Teoria"). A tese de Naur: um programa de computador não é o código-fonte — o código é apenas um **resíduo**. O que realmente "é" o programa é a **teoria mental** de como e por que ele funciona, e essa teoria só existe na cabeça de quem construiu o sistema.

Aplicação ao debate atual: quando um agente de IA escreve o código, ele nunca constrói essa teoria — ela "viveu" dentro de uma janela de contexto de ~1 milhão de tokens e depois se perdeu. Se o agente faz tudo, o humano nunca constrói nada. Quando o sistema quebra às 3h da manhã, não existe IA que "salve", porque ninguém — nem a própria IA — entende de fato como aquilo funciona.

Termo mais recente citado para o mesmo fenômeno: **Addy Osmani** (Google) chama isso de **"dívida de compreensão"** (comprehension debt) — uma conta que não faz barulho na hora, mas chega depois.

O problema apontado pelo autor: os fundadores originais dessa escola migraram (DHH, Antirez) ou já morreram antes de a IA existir (Peter Naur morreu em 2016, sem ver o boom de LLMs agênticos) — não há mais ninguém defendendo a posição "pura" de forma consistente.

## Escola 4 — O Loop (mais radical do slider)

Ponta mais extrema do controle de autonomia: colocar um agente rodando em **loop infinito**, sem ninguém supervisionando em tempo real, tentando de novo a cada falha, rodando a noite inteira até os testes passarem.

- Método citado: **Jeffrey Huntley** `[transcrição incerta — provavelmente Geoffrey Huntley]`, criador do método batizado de **"Half Wigun"** `[transcrição incerta — trocadilho provável com "Ralph Wiggum", personagem d'Os Simpsons; ver também o "Ralph Loop", técnica de loop agêntico já documentada nesta wiki, também atribuída a Geoffrey Huntley]`.
- Argumento de venda citado pelo autor: repositórios que seguem esse método reduzem "o custo de software" para menos que o salário de um atendente de fast food — cifra citada: algo em torno de **US$ 10-42 por hora** `[transcrição incerta sobre o valor exato]`.
- Comentário do autor, marcado explicitamente como opinião de bastidor: mesmo dentro da comunidade que já é adepta de IA, poucos "engolem" o argumento de deixar um loop puro rodar sem supervisão.

## Fechamento: cinco escolas, zero consenso

O autor resume: cinco escolas, cinco defensores fortes, cada um convencido de que sua abordagem é a certa — e vários dos "donos" de escola trocaram de posição nos últimos seis meses.

Argumento sobre aprender a programar hoje: cita [[Andrej Karpathy]] dizendo que "estamos na melhor hora para aprender" e contrasta com sua própria experiência de aprender programação em "livro xerocado" e "site apostilando" (analogia ao contexto de aprendizado pré-internet ampla no Brasil). O acesso à informação e a tutoria via IA nunca foram tão fáceis.

Crítica final: usar IA como **muleta** em vez de ferramenta é o erro real. Exemplo citado: alguém perguntou ao autor "para que vou aprender a programar se o Claude Code sabe tudo?" — resposta do autor: "se o Claude Code sabe tudo que você sabe, então ninguém precisa de você." Sem visão crítica — sem saber identificar onde a IA está alucinando, sem conseguir se virar sem a IA — o mercado "cospe" o profissional de volta.

## Fechamento do vídeo

Encerramento padrão de call-to-action (inscrição, like, notificação) e chamada para os comentários perguntando qual escola o espectador segue hoje e se já trocou de lado — seguido de recomendação de outro vídeo do canal sobre um caso de vibe coding no Nubank (fora do escopo desta transcrição).
