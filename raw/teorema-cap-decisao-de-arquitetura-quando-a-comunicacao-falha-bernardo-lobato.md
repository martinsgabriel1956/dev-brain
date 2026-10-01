# Teorema CAP — A decisão de arquitetura quando a comunicação falha (Bernardo Lobato)

> **Origem:** transcrição de vídeo em português (YouTube) de Bernardo Lobato sobre o Teorema CAP, colada pelo usuário em 2026-10-01. Já estava em português (sem tradução). Texto limpo, pontuado e dividido em seções; o conteúdo foi preservado. Foram omitidos apenas pedidos de like/inscrição/comentário, a despedida e um ruído de legenda no fim (caracteres tailandeses).
>
> **Correções de reconhecimento de fala (por contexto):** "Beckley" → Berkeley; "Brill" → Brewer; "Nancy Lint" → Nancy Lynch; "Devon" → dev; "com SD" → com ACID (a transcrição trouxe "SD"); "extrapulação" → extrapolação; "WS pela EUR ou GCP" → AWS, Azure ou GCP; "reageforme eles aparecem" → reage conforme eles aparecem; "to face com que" → provavelmente "two-phase commit"; "agendamento de vo" → voo; "teorema de CAPS" → teorema CAP; "Zom combinado" → "fechou, combinado"; "tolerância a partição disponibilidade e consistência dos três escolha dois" mantido como a frase-clichê citada pelo autor. O exemplo numérico do depósito ("deposita R$ 50 … recebe R$ 100") está ambíguo na fala; mantido como dito.

## Abertura

Em caso de falha na comunicação dos seus serviços distribuídos, você prefere que o sistema continue respondendo sem erros, ou que ele pare de responder até conseguir garantir que os dados relevantes estejam consistentes? O vídeo diz que essa pode ser uma grande responsabilidade do arquiteto de software ou do tech lead do projeto, e que o tema aparece sempre em entrevistas de emprego. Vamos conhecer o teorema CAP ("já prepara sua API para retornar 500 e 200 dependendo de onde a requisição cai").

O autor, Bernardo Lobato, promete explorar: de onde o teorema veio, o que ele visa responder, a diferença entre ele e as transações distribuídas, e como tomar decisões mais complicadas em arquitetura de software e system design.

## Origem: Brewer (2000) e Gilbert & Lynch (2002)

No ano 2000, um professor de ciência da computação da Universidade de Berkeley, na Califórnia, **Eric Brewer**, que também trabalhava com sistemas distribuídos em grande escala, refletia sobre as decisões arquiteturais críticas que esse tipo de sistema exigia de quem projeta a solução. Em um simpósio de computação distribuída, Eric apresentou uma palestra defendendo basicamente a ideia: em um sistema distribuído existem três propriedades desejáveis — **consistência, disponibilidade e tolerância a partições** — mas não é possível garantir as três simultaneamente. Naquele momento era uma **conjectura** baseada em experiência prática.

Dois anos depois, em 2002, os pesquisadores do MIT **Seth Gilbert e Nancy Lynch** formalizaram e provaram matematicamente a conjectura. A partir daí temos o **CAP Theorem** formalizado.

## Escopo: bancos replicados primeiro, serviços depois

Brewer formulou isso pensando em sistemas distribuídos de grande escala, e o conceito se tornou especialmente importante para **bancos de dados e sistemas de armazenamento replicados**. O autor comenta o teorema "puro" com esse cenário primeiro; depois mostra como a mesma tensão aparece ao projetar serviços e por que isso é uma extrapolação válida, endossada pelo próprio Brewer em 2012.

## O enunciado

> "Em um sistema distribuído, quando ocorre uma partição de rede você não consegue garantir simultaneamente consistência e disponibilidade."

### Partição de rede

Acontece quando partes de um sistema distribuído **continuam funcionando mas deixam de conseguir se comunicar entre si**. Não é necessário que os serviços tenham caído; eles simplesmente não conseguem se comunicar por alguma falha de rede ou de comunicação: cabo ou fibra rompida, falha de roteador, problema de firewall, perda de conectividade entre regiões, falha de rede no data center.

### Consistência

Em arquitetura de software: depois de uma operação ser concluída, uma leitura posterior deve enxergar o resultado mais recente daquela operação, **independente do nó**. Exemplo: dois servidores da mesma aplicação ou banco replicados; você deposita R$ 50 pelo servidor A, que sinaliza que a operação foi concluída; se uma consulta chegar ao servidor B imediatamente e receber R$ 100 (valor antigo), o sistema não está fornecendo consistência forte.

**Observação do autor:** a consistência do CAP **não é a mesma coisa** que a propriedade de consistência do ACID. São conceitos diferentes que usam a mesma palavra; no ACID/bancos relacionais ela diz respeito às regras de integridade do banco que não devem ser quebradas.

### Disponibilidade

Toda requisição recebida por um nó disponível deve receber uma resposta, mesmo em caso de falhas de comunicação ou partição de rede. No exemplo anterior, se a requisição cair no servidor B, ele poderia responder com dados desatualizados. O autor antecipa a objeção ("não posso devolver informação errada deliberadamente"): num sistema financeiro esse raciocínio pode estar correto, mas ele volta ao assunto com outros casos.

### Tolerância a partições

É aqui que consistência e disponibilidade entram em conflito. Se a comunicação entre os servidores é interrompida, os dois continuam funcionando mas não trocam informações. Durante a partição há duas possibilidades, e é preciso conhecer o negócio para escolher:

1. **Priorizar consistência (CP):** o servidor diz "não tenho como garantir que minha informação está atualizada, então não vou responder". Preserva a consistência, sacrifica a disponibilidade.
2. **Priorizar disponibilidade (AP):** mesmo sem conseguir conversar com os outros servidores, é mais importante continuar respondendo as requisições com sucesso. Preserva a disponibilidade, mas pode precisar aceitar informações divergentes temporariamente.

As siglas **AP e CP são uma forma simplificada de representar o comportamento durante uma partição**. Não significa que uma tecnologia inteira possa ser resumida como CP ou AP em qualquer situação.

## Contra o "escolha dois de três"

Quem já teve contato superficial com o teorema pode ter visto a frase "tolerância a partição, disponibilidade e consistência: dos três, escolha dois". O autor diz que **não é bem assim**. O diagrama tradicional mostra as três propriedades, mas em um sistema distribuído **partições de rede são uma possibilidade que precisamos tolerar sempre**; não é uma decisão nossa, é uma característica intrínseca da arquitetura distribuída. Não dá para "desligar a tolerância a partições e fingir que ela não existe". Quando a partição acontece, o conflito que interessa é: continuar disponível ou preservar a consistência dos dados.

## Bancos de dados replicáveis (onde o teorema surgiu)

Quando os dados são replicados entre nós e eles perdem a capacidade de se comunicar, o sistema precisa lidar com o conflito entre manter os dados consistentes e continuar respondendo. Diferentes bancos adotam estratégias distintas: alguns priorizam consistência, outros disponibilidade, e alguns permitem **configurar o comportamento conforme a operação**.

Exemplos citados (brevemente, "para você pesquisar depois"):

- **MongoDB:** usa replicação e permite configurar diferentes níveis de preocupação (concern) de leitura e escrita.
- **Cassandra:** projetado com forte foco em disponibilidade e escalabilidade, oferecendo consistência configurável.

O importante é **não classificar simplesmente uma tecnologia como CP ou AP**, porque as garantias dependem da configuração, da operação e do comportamento durante uma partição.

Nos **serviços gerenciáveis de banco em nuvem** (AWS, Azure, GCP), o provedor assume grande parte da complexidade de infraestrutura (replicação, backups, distribuição dos dados), mas isso **não elimina o CAP**; só abstrai boa parte da implementação, à qual temos acesso menos direto. Quando você escolhe entre uma configuração que prioriza consistência e outra que privilegia disponibilidade durante uma falha entre regiões, está fazendo uma escolha relacionada ao teorema CAP.

## Do teorema para o design de serviços

No dia a dia, o desenvolvedor raramente mexe direto numa réplica de banco; ele projeta serviços. Falar de CAP em sistemas/serviços é, de certa forma, uma **extrapolação do teorema original**, hoje bem aceita na prática e **endossada pelo próprio Brewer em 2012, no artigo "CAP Twelve Years Later: How the Rules Have Changed"** (o autor traduz o título livremente). Disclaimer: o tema ainda gera debate em materiais acadêmicos, então outros materiais podem divergir ligeiramente.

**Nem toda falha de comunicação entre serviços é CAP.** Se o serviço A chama o B e ele simplesmente está fora do ar, isso é só uma falha de comunicação. O CAP entra quando **existe um estado compartilhado que dois serviços precisam coordenar** e o sistema tem que decidir o que fazer quando essa coordenação quebra.

### Exemplo: serviços de Estoque e Pedido

A consistência desejada aqui não é sobre duas réplicas do mesmo banco, mas sobre o **estado de negócio**: a quantidade em estoque que dois serviços diferentes precisam enxergar de forma coerente. É a mesma pergunta do CAP, agora no desenho dos serviços, que podem estar em máquinas, contêineres ou regiões diferentes e trocam informação pela rede.

Imagine que o serviço de estoque sabe que há apenas uma unidade de um produto, e o serviço de pedido recebe uma solicitação de compra, mas os dois não conseguem conversar. Surge a mesma questão: o serviço deve continuar respondendo sem confirmar o estado do outro, ou interromper a operação até a comunicação ser restabelecida? Na prática: "aceito pedido mesmo sem conseguir dar baixa no estoque?". É aqui que consistência, disponibilidade e tolerância a partição passam a fazer parte do system design, e que se fortalece o papel de quem desenha a aplicação: mapear o problema e escolher a melhor direção **conforme o negócio**. "Não existe solução mágica"; é esse tipo de decisão que diferencia uma arquitetura pensada de uma que "simplesmente reage conforme os problemas aparecem".

## Aplicando a sistemas hipotéticos

### Catálogo estilo Netflix

Um serviço com dados de filmes (títulos, capa, descrição, duração). Em caso de partição, manter o acesso mesmo com dados possivelmente desatualizados? Decisão do autor: **priorizar disponibilidade**. Nomes de filmes ligeiramente desatualizados por alguns segundos não são problema; o problema seria o usuário não conseguir assistir. Se priorizasse consistência, o problema seria muito maior, porque não entregaria os vídeos que o usuário precisa assistir.

### Reserva de voos (teorema aplicado **por funcionalidade**)

- **Busca de voos:** o usuário está navegando. Decisão: **disponibilidade**. Os usuários querem navegar mesmo que preços e disponibilidade estejam levemente desatualizados; é melhor mostrar resultados aproximados do que nenhum resultado e deixar o usuário sem ideia de valores ou datas.
- **Compra/reserva do bilhete:** o usuário já pesquisou e quer finalizar. Decisão: **consistência**. Priorizar disponibilidade poderia vender o mesmo assento a dois usuários diferentes, uma péssima experiência para todos; é preciso consistência forte.

Conclusão do autor: é preciso entender do negócio e da parte técnica.

## O que o CAP não resolve

O CAP ajuda a decidir **o que fazer na hora da falha** (responder com dado desatualizado ou priorizar consistência), mas **não resolve como arrumar a bagunça depois**, quando a comunicação volta e pedido e estoque precisam voltar a bater. Isso é assunto de **transações distribuídas** (saga, two-phase commit), tema para outro vídeo.

## Fechamento

O teorema CAP nos ajuda a entender uma limitação fundamental dos sistemas distribuídos: quando ocorre uma partição de rede, é preciso decidir quais garantias são mais importantes para aquele sistema ou funcionalidade. Em alguns casos a consistência é a prioridade; em outros, continuar disponível. O papel do arquiteto é entender o que o negócio pode aceitar quando a comunicação falha e projetar o sistema a partir dessa decisão.

**Mini desafio proposto:** pegue as funcionalidades mais importantes do sistema em que você atua hoje e aplique o teorema CAP a elas; você concorda com o que está acontecendo atualmente?

## Frases-chave

> "Em caso de falha na comunicação dos seus serviços distribuídos, você prefere que o sistema continue respondendo sem erros ou que ele pare de responder até conseguir garantir que os dados relevantes estejam consistentes?"

> "Não dá para simplesmente desligar a tolerância a partições e fingir que ela não existe."

> "O CAP entra quando existe um estado compartilhado que dois serviços precisam coordenar e o sistema tem que decidir o que fazer quando essa coordenação quebra."

> "É esse tipo de decisão que diferencia uma arquitetura pensada de uma arquitetura que simplesmente reage conforme eles aparecem."
