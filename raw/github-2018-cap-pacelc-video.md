# GitHub 2018, Teorema CAP e PACELC (vídeo)

> Transcrição de vídeo em português (canal não identificado). Texto limpo e estruturado em seções a partir de transcrição automática; já estava em português, sem tradução. Termos distorcidos pelo reconhecimento de voz foram corrigidos pelo contexto.
>
> **Correções de transcrição aplicadas:** "Nok" → *nó*; "apicionamento / parção / partição" → *partição*; "teorema Passelk / Passel que" → *teorema PACELC*; "coro" → *quórum*; "road trip" → *round trip*; "0.05 msos / 0.19 msundos" → *0,05 ms / 0,19 ms*; "operação de rede" (no trecho "não existe a operação de rede") → *partição de rede*; "Enquete lá no Discord" → *enquete no Discord*.
>
> **Incertezas:** o trecho "eu fiz um teste local subindo né" está incompleto na transcrição (provavelmente um cluster local de 3 nós); a frase sobre "eu isolei um" refere-se a um dos três nós.

## 1. O caso GitHub (outubro de 2018)

Em outubro de 2018, no GitHub, a troca de um equipamento de rede derrubou o link entre dois data centers (um na costa leste e outro na costa oeste). A rede voltou em **43 segundos**, porém o serviço só voltou ao normal **mais de 24 horas depois**.

Os dois data centers replicavam um para o outro. Quando o link caiu, a aplicação continuou gravando no leste; do outro lado, o sistema achou que o leste tinha caído e passou a aceitar escritas também no oeste. Resultado: **ambos os lados tinham dados que o outro não tinha**. Mesmo com a rede de volta em segundos, foi preciso mais de 24 horas para reconciliar, porque nenhum dos dois conjuntos de dados podia ser perdido.

## 2. O que "disponibilidade" significa no teorema CAP

Quando se fala em disponibilidade, o senso comum pensa em "o sistema está no ar". Pelo teorema CAP é outra coisa: **todo nó que não caiu precisa responder sem erro**, inclusive o nó que ficou sozinho, do lado errado da partição.

Por isso, pelo CAP, o GitHub esteve **disponível** durante as 24 horas: estava no ar e respondendo, só que com dados divergentes entre os lados. Ou seja, ele escolheu disponibilidade e pagou com consistência.

## 3. A analogia das agências de banco

Uma rede de agências de banco: cada agência atende com o dinheiro que tem em caixa, e o movimento vai e volta para a matriz por malote. A estrada fecha e o malote não chega. Existe uma escolha:

- **recusar o saque** (consistência: não paga sem saber o saldo global), ou
- **pagar com o caixa local e acertar depois** (disponibilidade).

Essa decisão só existe nessa situação específica: quando a comunicação está fechada. E do ponto de vista do nó, o outro lado pode ter **caído**, estar **lento** ou ter simplesmente **cortado a comunicação** — três situações muito diferentes que chegam da mesma forma: **em silêncio, sem aviso**.

## 4. O experimento do autor

O autor fez um teste local com **3 nós**, isolou 1 e observou:

- **Escrita** no nó isolado: queimou 5 segundos de timeout e desistiu (falhou).
- **Leitura com garantia forte** no nó isolado: também falhou.
- **Leitura local** no nó isolado: respondeu na hora, porém com o dado de antes da partição (desatualizado).

Depois, sem nenhuma partição (rede saudável):

- **Leitura local** para no primeiro nó: cerca de **0,05 ms** nos testes.
- **Leitura forte** exige que o nó pergunte ao **quórum**, somando o tempo de ida e volta (round trip): mais cerca de **0,19 ms**.

Isso acontece em **toda leitura forte, todos os dias, enquanto a rede está de pé**. A pergunta que fica: "existe partição?" — se existe, estamos no território do teorema CAP.

## 5. Teorema CAP

Em sistemas distribuídos é impossível ter as três características ao mesmo tempo: **consistência, disponibilidade e tolerância a particionamento**. Tolerância a partição não é opção: ela vai acontecer. Quando acontecer, é preciso priorizar **consistência ou disponibilidade**.

## 6. Teorema PACELC

Partições são raras. Quando **não** há partição de rede, ainda assim existe uma escolha: **latência ou consistência**. Isso vale para a maior parte do tempo e tem nome: **teorema PACELC**.

O PACELC **não invalida** o CAP; ele adiciona uma camada: mesmo sem partição, há um trade-off entre latência e consistência.

## 7. Falácias da computação distribuída

Entre as várias falácias, duas são especialmente fortes: **"a rede é confiável"** e **"a latência é zero"**. Na prática, a rede está longe disso.

## 8. Ressalvas do autor

Voltando ao exemplo do GitHub (dois data centers, leste e oeste, os dois lados gravando ao mesmo tempo): **o autor não conseguiu reproduzir** esse cenário. Os três nós do teste não permitiam formar um grupo com a maioria dos dois lados, e ele **também não mediu a latência entre zonas e regiões**. Os resultados são de um teste local.

## 9. Encerramento

Pedido de like/inscrição. A enquete no Discord e na aba Comunidade do YouTube mostrou que a grande maioria quer vídeos sobre **system design e arquitetura**; o canal vai trazer mais conteúdo sobre isso.
