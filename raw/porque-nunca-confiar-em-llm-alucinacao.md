# Por Que Você Nunca Deve Confiar 100% numa LLM (Alucinação de LLMs)

Transcrição de vídeo em português (canal de tecnologia, apresentador não identificado na fala), sem necessidade de tradução. Fala corrida/coloquial reestruturada em markdown com uma seção por bloco temático, mantendo o conteúdo original sem sumarização. O nome do patrocinador citado na fala como "High Globe" foi mantido conforme ouvido, com nota de que provavelmente se refere à fintech **Global66** (transferências internacionais/multi-moeda, cartão, Pix), dado o contexto de câmbio, Pix, cartão e recebimento em dólar/euro descrito no segmento publicitário.

---

## Introdução: o mito que não é mito

Esse é o vídeo que eu vou mostrar por A + B por que você nunca deve confiar numa LLM: elas mentem muito. Vamos lá, gente, não é meme, não é exagero. É um estudo que fala sobre alucinação das LLMs, termo usado amplamente na academia para descrever o fenômeno de LLMs inventarem muita coisa: inventam fatos que não existem, inventam features que não existem, inventam libs de código que não existem, referências que não existem, coisas que não existem. É fato consolidado — tão consolidado que existem estudos demonstrando isso.

Esse estudo é um pouco antigo (os números de hoje em dia são melhores), mas nele o desempenho dos seres humanos em falar a verdade era 94%, enquanto o das LLMs era 58%. As LLMs simplesmente inventavam resposta quase metade das vezes. E isso é tão verdade que a própria OpenAI tem um artigo sobre isso — a OpenAI, claro, a empresa que vende inteligência artificial para você comprar, que tem o maior interesse possível em dizer que a IA não mente, que a IA fala a verdade. Pois bem, vamos ver o quanto de verdade ela fala.

## O estudo: correto, incorreto e "não tentado"

Nesse estudo eles têm um exemplo do que consideram correto, incorreto e não tentado. Por exemplo, perguntas factuais como "quem fez o gol no jogo de Holanda e Argentina de 2022". Eles testaram o A1 preview, GPT-4, GPT-4 Mini (também um pouco antigos). O melhor modelo deles deu resposta incorreta 48% das vezes, não tentou 9% das vezes, e acertou 42% das vezes. Ela mente, e mente muito.

## Demonstração ao vivo: a mentira sobre pagamento em euro

Quer ver um exemplo? Estou aqui no ChatGPT e vou perguntar sobre o patrocinador de hoje, o chat: "High Globe aceita pagamentos em euro?" Vamos ver o que ele responde: "Sim, pelo que consta atualmente, a High Globe aceita recebimentos em euro e também em USD." É sério isso? E, meus queridos, se você trabalha para os Estados Unidos e agora para a Europa, você vai ficar muito feliz de ouvir que sim, agora é possível receber dinheiro tanto dos Estados Unidos em dólar quanto da Europa em euro.

## Segmento publicitário (patrocínio)

Se você trabalha para a gringa, eu uso a High Globe há uns dois anos. Tenho o cartão da High Globe, que posso adicionar no celular no Apple Pay, no Google Pay, e gastar meu saldo, ou deixar esse saldo parado rendendo. Meu saldo já rendeu bastante só de deixar de um mês para o outro. Eu uso porque acho a melhor solução para receber dinheiro de fora do país.

Você tem seu saldo, clica em "retirar", seleciona sua CPF/CNPJ, escolhe um valor para sacar, clica em "next". O custo deles é o melhor que eu já vi: 0,3% (a cada 1.000, você paga 3 por esse serviço), sem nenhuma taxa ou imposto adicional em cima disso. O câmbio é o câmbio oficial do dia (no dia da gravação, 7 de julho, o dólar valia R$ 5,12). Você clica em "confirmar" e cai um Pix na sua conta.

É por isso que uso: é uma solução rápida, confiável, tecnológica, que recomendo para todos os meus amigos, e é a única que uso para receber dólares dos Estados Unidos e agora euros da Europa. Genuinamente acho eles excelentes, não tenho nada a reclamar — na verdade as únicas duas coisas que eu gostaria que eles tivessem (cartão de crédito e recebimento em euro) eles já me deram, então agora está perfeito. Clica no link na descrição, usa o cupom "Augusto 20" e você tem 20% de desconto na taxinha, fica mais barato ainda. Se você trabalha para a gringa, recomendo muito.

## Por que as LLMs alucinam: tool calling e o paper da OpenAI

Felizmente hoje as LLMs estão um pouco melhores, estão mentindo menos, porque existe a chamada de ferramentas (tool calling). Existe uma pesquisa muito boa dentro da própria OpenAI que pergunta por que os modelos de linguagem têm alucinação. A alucinação tem muito a ver com isto: "os procedimentos padrões de treinamento e avaliação recompensam o palpite ao invés do reconhecimento de incerteza."

Por isso, quando você escreve um prompt detalhado — "cara, pelo amor de Deus, ChatGPT, se você não tiver certeza do que está falando, me pergunta", ou fala que não tem certeza, ou busca uma fonte — isso de fato funciona, em parte por causa desse comportamento de treinamento.

O artigo da OpenAI é longo, fala sobre a avaliação de tarefas e a forma como fazem o reinforcement learning, e tem detalhes muito interessantes no fim, na própria conclusão do ChatGPT/OpenAI:

- A precisão jamais atingirá 100%, porque, independentemente do tamanho do modelo, da capacidade de busca e raciocínio, algumas questões do mundo real são inerentemente impossíveis de responder.
- Pode ser mais fácil para um modelo pequeno conhecer os seus limites do que para um modelo grande, entre aspas, "superinteligente" — mais ou menos como um ser humano real. Que loucura.

## Por que isso importa: risco jurídico e produto

Isso é muito importante de entender porque provavelmente você vai usar IA para fazer código, ou vai implementar IA na sua empresa. Se você implementar na sua empresa e o seu chatbot decide mentir para o cliente — porque, honestamente, você não tem nenhuma garantia de que a IA vai sempre falar a verdade ou estar baseada em fatos — talvez você tenha que pagar uma multa. A Air Canada foi condenada a pagar porque um cliente foi enganado pelo chatbot deles. Isso cria um passivo jurídico dentro das empresas, e é muito interessante evitar esse não-determinismo quando possível.

Pensa comigo: existe uma pessoa que pode pensar "a LLM mente, e eu estou falando com a LLM de uma empresa X (usei a Latam como exemplo, sem querer insinuar nada contra eles, só para ilustrar); se eu ficar tentando fazer uma pergunta de um jeito que ela responda de maneira incorreta, e eu tomar ações baseado nisso, talvez consiga uma vantagem." Nos sistemas que você for implementar, tome muito cuidado com esse tipo de chatbot, principalmente se ele tiver capacidades agênticas — por exemplo, oferecer desconto. Um usuário malicioso pode tentar conseguir um desconto de 99%. Não sei se funcionaria, mas se você vende produto físico, isso é um problema real.

## Alucinação em código: pacotes que não existem

Existem estudos extremamente compreensivos demonstrando alucinações a respeito de pacotes (libs) em linguagens como Python e JavaScript. Num conjunto de testes em que geraram 576.000 códigos, esses códigos incluíram um total de 205.000 pacotes totalmente alucinados — nomes de pacotes inventados. Você tem que pelo menos ficar atento quando estiver codando com IA, porque ela não só inventa pacotes: às vezes pega um pacote que existe e inventa uma funcionalidade que não funciona, que não existe, ou que não é bem daquela maneira.

## RAG (HAG) melhora, mas não resolve

Existe uma maneira de melhorar isso: dentro do próprio ferramental, usando MCPs, você pode injetar a documentação do pacote determinado como contexto, o que melhora um pouco a situação — mas não fica perfeito.

Existe um artigo sobre RAG (retrieval-augmented generation, aqui falado como "HAG"), ideia que já foi mencionada no canal algumas vezes: dentro de uma LLM você tem o "modelo mental" dela (o cérebro). No RAG, você pega alguns documentos — ao redigir um prompt, um sistema busca documentos parecidos com o prompt. Por exemplo, o prompt "Claude Code, me ajuda a gerar PDF em JavaScript" pega documentos relacionados (PDFs, documentação, links de artigos) e injeta isso junto com o prompt, esperando que o raciocínio interno da "caixa-preta" da LLM use esse mesmo documento para responder algo baseado nele.

Teoria linda, mas na prática esse estudo demonstra que sim, RAG melhora bastante a eficiência, mas não é perfeito. RAG não transforma magicamente a LLM em algo que nunca mais alucina — isso não existe. Vai sempre existir um grau de "bullshitagem". Como devs, tentamos reduzir essa incerteza injetando documentação e contexto, adicionando testes no output, tentando forçar a IA a fazer algo baseado numa spec ou num PRD, delimitando e deixando o mínimo de incerteza possível, usando modos tipo "plan mode" — tudo para aumentar o grau de confiança na LLM. Mas, no final das contas, a LLM continua mentindo.

## Isso significa não usar IA? Não.

Isso impede você de usar IA para trabalho? Claro que não. Não estou dizendo que o fato de as IAs alucinarem significa que você não deve usar IA para fazer código. A realidade é que todo mundo está usando — eu mesmo quase não escrevo linhas de código no trabalho hoje em dia, quase nada.

Outro exemplo comum de alucinação: você pede para a IA escrever um artigo científico e ela inventa uma referência que não existe.

## Como usar IA de uma maneira melhor

### Exemplo 1: chatbot de empresa com RAG e verificação (LLM-as-judge)

Você está desenvolvendo um chatbot para a empresa. Seu chefe quer um chatbot de IA de verdade (não um FAQ estático). O usuário vai fazer uma pergunta mais ou menos assim: "Como funciona o refund?" A abordagem correta não é jogar isso direto na LLM final para dar a resposta. O fluxo seria:

1. A pergunta do usuário passa por um prompt engineering (correção de erros de português, transformação num prompt mais detalhado).
2. Em paralelo, busca-se a documentação interna da empresa usando técnicas de RAG.
3. Junta-se as duas coisas, formando um prompt final orquestrado com algumas chamadas e retrievals de documentos. Algo como: "aqui está a documentação de refund [trecho da documentação, citando exatamente a frase que responde a pergunta]. Explique essa frase."
4. Internamente, testa-se isso várias vezes, usando um LLM-as-judge para avaliar métricas como **faithfulness** — o quão fiel a resposta está em relação ao documento fornecido (vale pesquisar "AI judge faithfulness").
5. O prompt final gera a resposta que vai para o cliente ou para outro sistema, que analisa a resposta novamente para checar se a IA não está inventando. Se estiver inventando, o processo volta até a resposta parar de inventar e responder exatamente o que está no documento.

Esse fluxo é para o caso de implementar IA num sistema em produção.

### Exemplo 2: uso pessoal

Para uso pessoal, a "palavra mágica" (geralmente em inglês) é pedir para o modelo "usar a ferramenta de busca" (use your search). Foi assim que o GPT respondeu corretamente sobre a Global66 aceitar euros — porque ele pesquisou na internet e trouxe as fontes.

Ao escrever código, você também pode pedir para a IA rodar os testes ("run tests"): escrever um teste que falha, depois escrever o código (TDD). Você pode usar IA agressivamente, mas precisa entender que é necessário criar um ferramental de guardrails ao redor da IA para que ela aja e responda adequadamente, porque ela vai mentir para você.
