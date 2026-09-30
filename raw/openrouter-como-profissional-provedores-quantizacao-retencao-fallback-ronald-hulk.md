# OpenRouter como profissional — provedores, quantização, throughput, retenção de dados e fallback

Fonte: transcrição de vídeo de Ronald Hulk (autoapresentação no próprio vídeo; links na descrição, não disponíveis), já em português — sem necessidade de tradução. Transcrição automática colada pelo usuário; foram adicionados apenas pontuação, parágrafos e títulos de seção, e o texto foi limpo de erros de reconhecimento de fala.

Termos corrigidos por contexto: "Open Houter"/"Openouter"/"Open Router" → OpenRouter; "DeepSC V4 Flash"/"deepsic" → DeepSeek V4 Flash; "trupol"/"trolle"/"Troupol" → throughput; "Cory Wave" → CoreWeave; "Rock Pro"/"Rock" → Rock Pro (harness do autor); "Together" → Together AI; "L chain/Lraft/DP agent" → LangChain / LangGraph / Deep Agents (provável, [?]); "ADR"/"HW" → ADR; "Hermes" → Hermes Agent; "P90" mantido; "max pricing" → campo `max_price`; "data policy/denai" → `data_collection: "deny"`; "ya" → IA; "fornecedora" → provedor. Pedidos de like/inscrição omitidos.

---

## Abertura

No vídeo anterior o autor explicou por que moveu vários clientes para o DeepSeek V4 Flash usando a OpenRouter. Recebeu muitos comentários sobre preço, política de retenção de dados etc. Conclusão: a maioria das pessoas não está tirando o melhor da OpenRouter. Este vídeo mostra como usá-la "como um profissional". O autor (Ronald Hulk) ajuda indivíduos e empresas a colocar soluções de IA em produção e lucrar com isso.

## O que a OpenRouter faz: roteador com fallback

A OpenRouter é, literalmente, um roteador. Ao usar um modelo (exemplo: DeepSeek), há o provedor A, o B e o C: ela tenta o A; se falhar, usa o B; se o B falhar, usa o C.

Isso importa em produção porque, muitas vezes, o provedor para de funcionar. Dá para tratar isso do seu lado (construindo algo) ou usar o serviço deles — o famoso **fallback**: algo caiu, ele chama outra LLM. É um grande valor, e funciona já ao chamar a API "crua", como a maioria faz. Mas é exatamente essa chamada crua que causa a "ruína" de quem não consegue usar a ferramenta profissionalmente — o restante do vídeo explica como evitar isso.

## A tela inicial é ruído

Quem entra na OpenRouter vê uma lista enorme de modelos, parecendo um "feirão". Para a operação profissional isso é ruído: ignorar a tela inicial, promoções e modelos gratuitos com nome oculto (são curiosidade/brincadeira para testar, não para o dia a dia).

## Como ler a página de um modelo (seis características)

Na página de um modelo (exemplo: DeepSeek) há seis características avaliadas, e o **preço é a última coisa que deveria ser levada em conta** — embora seja com a que as pessoas mais se preocupam.

### 1. Preço — modelo + provedor, não modelo

O framework mental a apagar: o preço não é determinado por um lugar central. Nos modelos da OpenAI e da Anthropic (closed weight) a empresa é dona do modelo, não o divulga e define o preço. Aqui os modelos são **open weight**: qualquer um pode baixar o modelo e, tendo infraestrutura, oferecê-lo como serviço a um preço que ele define. Ou seja, sai-se de um **preço central para um preço distribuído**. Na OpenRouter, portanto, a unidade é **modelo + provedor**, e o preço depende do fornecedor. O preço é um critério de avaliação, mas não determinístico para a escolha.

### 2. Quantização

O autor sugere perguntar à sua harness (Rock Pro) o que é quantização. Na OpenRouter o valor aparece por provedor, porque o mesmo modelo é fornecido a diferentes pessoas/empresas com diferentes qualidades. A "pegadinha": você usa o Hermes (ou uma solução profissional), a resposta às vezes funciona bem e às vezes não — talvez porque o roteamento caiu num provedor com quantização menor.

Na lista vê-se que vários provedores fornecem em **FP4**, vários em **FP8** e alguns em **16** (FP16/BF16). Esse é o padrão: provavelmente quase sempre se consome o modelo quantizado, não "in natura". Nos testes do vídeo anterior deve-se considerar **modelo + provedor + quantização**. Segundo a experiência do autor, se você for rigoroso e fizer vários testes: o **FP8 geralmente funciona muito bem**; o **FP4 tem uma queda**, mas pode ser suficiente (e o preço pode agradar). A análise é sua.

### 3. Throughput (tokens por segundo)

Mostra os tokens por segundo de saída que aquele provedor consegue fornecer (na Rock Pro, é a velocidade com que a resposta "escorre"). Quanto mais tokens por segundo, melhor a experiência do cliente. Depende do caso: se o processo roda de madrugada, pode-se pagar menos por resposta mais lenta. "Não existe bala de prata": é preciso aprender a interpretar os sinais e tirar conclusões.

### 4. Latência

Irmã do throughput: quanto tempo o provedor leva para começar a responder.

### 5. Região

Modelos podem ser fornecidos de regiões diferentes. Exemplo: CoreWeave fornece nos Estados Unidos em FP8; Baidu fornece na China, também em FP8. A distância soma-se à latência (há um processo de comunicação "que você não vê", mas é grande).

### 6. Disponibilidade

Só se vê no final das contas. O perigo de usar a API crua: ela roteia para qualquer provedor da lista, sem controle — e a ideia é aprender a controlar isso.

### Retenção de dados (política)

Tópico quente por causa de LGPD e contratos. Na página do provedor há a **data policy**: com **"no retention"** não declarado, você não sabe o que ele faz com seu dado (se guarda ou descarta) — "não faz a mínima ideia". Tudo está escrito em contrato; a decisão é sua e baseada na sua necessidade ("não adianta dizer que não sabia: você viu o vídeo, já sabe"). Dá para buscar um provedor com **zero data retention** (exemplo mostrado: Together AI). Isso ajuda a justificar a solução ao cliente: "o provedor não armazena dado" e você fica **protegido por contrato**. Pode custar mais; pode não custar. Por isso o preço é o último critério: primeiro avaliam-se todas as condições compatíveis com o projeto, depois decide-se pelo preço, fazendo trade-offs.

## A tabelinha — pensar antes de delegar

Pegar caneta e papel e montar uma tabela (quantização, throughput, latência, região, retenção, preço) e classificar os modelos/provedores. O autor insiste: usar o cérebro quando tem que usar e a máquina para acelerar, não o contrário. "Você não pode delegar algo que não sabe fazer" — mesmo problema do gerente de projeto que nunca foi desenvolvedor e não sabe delegar ao time; agora se tem uma IA para delegar, e sem saber fazer não se delega bem.

## Criar um pool de provedores

Se você selecionar apenas um provedor na tabela, perde exatamente a feature que é a beleza da OpenRouter (rotear para outro se um falhar). Escolher **pelo menos três** provedores que atendam ao requisito (quatro ou cinco se quiser ser extra seguro). Assim há margem: garante-se a política (qualidade, retenção) e, ao mesmo tempo, melhor performance e melhor custo possível.

## Na prática: ADR + payload

Boa prática no mundo real: transformar o estudo e a tabela em uma **ADR** (e uma PR) no trabalho. Você é dono do problema; "liderança não é dada, é conquistada": mostra o estudo, as condições, a tabela, e o chefe pode adotar. O autor diz que, se você trabalhasse com ele, marcaria ele na PR. Só então implementar — com critérios definidos, não "sentar e pedir para implementar sem critério".

A stack do autor usa LangChain (LangGraph, Deep Agents etc.), mas como a OpenRouter tem uma API única, não importa se chama via framework ou direto: o payload é o mesmo. Campos importantes do objeto de preferências de provedor (`provider`). Nota: o autor descreve os campos falando ("only", "order", fallback, quantização, max pricing, throughput no P90, data policy deny); os nomes exatos dos campos abaixo foram mapeados pela documentação da OpenRouter (https://openrouter.ai/docs/features/provider-routing), não ditos literalmente no vídeo:

- **only** — "só quero esses provedores": fixa os três escolhidos; a OpenRouter não roteia para nenhum dos outros milhares.
- **order** — ordem de preferência: tenta o primeiro; se falhar ou tiver problema, chama o seguinte.
- **allow_fallbacks** — ("a chave do fallback") mantém o fallback entre os provedores permitidos; é um dos grandes objetivos de usar a OpenRouter.
- **quantizations** — restringe a certos tipos de quantização; se for de fora do tipo, não quer.
- **max_price** — preço máximo; dá para "barganhar"/fazer leilão se o uso é alto e a qualidade da resposta não é tão crítica, ou se o trabalho aceita provedores mais lentos e quantizados.
- **preferred_min_throughput** (com percentil, ex. P90) e latência máxima — o autor já falou disso no vídeo anterior.
- **data_collection: "deny"** — nega sempre provedores com política de retenção/coleta de dados. Como o provedor já foi selecionado, "não custa nada ser extra seguro e colocar este campo".

## Resumo do autor

Na OpenRouter não se escolhe modelo: escolhe-se **modelo + provedor**. O provedor determina o preço, não uma entidade central — pensamento natural de quem vem do mundo OpenAI/Anthropic, onde a empresa delimita tudo, para o mundo em que qualquer um pode pegar o modelo e fornecê-lo. A OpenRouter pode "bagunçar" a solução sem querer: é uma feature, não um bug, mas é preciso saber usá-la como profissional.
