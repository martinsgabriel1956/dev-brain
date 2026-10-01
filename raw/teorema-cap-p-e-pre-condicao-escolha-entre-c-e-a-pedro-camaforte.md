# Teorema CAP — Por que o "P" não é uma opção (Pedro Camaforte)

> **Origem:** transcrição de vídeo em português (YouTube) de Pedro Camaforte sobre o Teorema CAP para entrevistas de System Design, colada pelo usuário em 2026-10-01. Já estava em português (sem tradução). Texto limpo e estruturado em seções; o conteúdo foi preservado.
>
> **Correções de reconhecimento de fala (por contexto):** "do anos" → "dois anos"; "sênnior"/"snior" → sênior; "volotar" → voltar; "pré-conda"/"précição" → pré-condição; "ele sabe do que que ele tá falando" mantido como fala; "eu esqueci um assento aqui nessa palavra" (trecho ininteligível, provavelmente "esqueci um acento") — mantido como aparece; "sior" → sênior; "sistem" → system design.

## Abertura

"Você conseguiria desenhar um sistema distribuído que fosse ao mesmo tempo altamente disponível, consistente e tolerante a falhas de rede? Se a sua resposta foi sim, eu sinto informar, mas é impossível." O vídeo promete provar o porquê e mostrar como isso impacta as entrevistas de system design e as decisões de arquitetura.

O Teorema CAP "cai em praticamente todas as entrevistas de System Design". Se você não o citou, ele provavelmente estava escondido e você não percebeu. Ele "dita e guia toda a construção da sua arquitetura desde os fundamentos": quais componentes, qual estilo de arquitetura, qual técnica, quais ferramentas. Por isso é preciso entendê-lo no detalhe, e não só decorado.

O autor se apresenta como Pedro Camaforte, desenvolvedor sênior, trabalhando há quase dois anos para empresa do exterior.

## O enunciado

O teorema foi desenvolvido por **Eric Brewer** — segundo o autor, vice-presidente de infraestrutura do Google. O enunciado:

> "Em um sistema distribuído você só pode ter duas das três opções ao mesmo tempo: consistência, disponibilidade e tolerância a partições."

CAP vem de *Consistency, Availability, Partition tolerance*.

### Contexto: o que é "sistema distribuído" aqui

Um sistema com mais de um servidor/nó: microsserviços, ou replicação de dados entre servidores em diferentes países. Dados replicados e passados por uma rede interna entre vários servidores.

### Os três componentes

- **Consistência:** toda leitura retorna o dado mais recente, igual em qualquer nó consultado. Consultar o servidor do Brasil ou o dos Estados Unidos precisa devolver o mesmo dado — "não considerando a latência, não considerando o tempo de replicação". Não pode haver dados diferentes se os dois forem consultados ao mesmo tempo.
- **Disponibilidade (Availability):** toda requisição recebe uma resposta, "sendo ela positiva ou negativa". O sistema nunca fica mudo. Pode ser uma resposta positiva ou "um 404, um erro, não encontrado", mas o servidor precisa responder.
- **Tolerância a partições:** o sistema continua funcionando mesmo quando a comunicação entre os nós (servidores) falha. Se o servidor dos EUA parar de conversar com o do Brasil, o sistema não pode entrar em colapso; precisa continuar funcionando mesmo com oscilação momentânea.

## O erro do triângulo "escolha 2 de 3"

A imagem comum mostra três opções e sugere que se pode escolher CP, CA ou AP "ao bel prazer", conforme os requisitos. O autor afirma que **isso é um erro e é o que mais confunde as pessoas**. Em parte, acredita, pela maneira como Brewer explicou o enunciado.

### Sistema simples (não distribuído)

Um usuário fala com um servidor, que tem um único banco de dados. Todos os dados estão ali; não há comunicação interna entre servidores nem replicação. "Guardem esse sistema, a gente já vai voltar nele."

### Sistema distribuído: o exemplo do e-commerce

Uma loja com vitrine de produtos. O servidor principal está nos EUA, onde ficam os cadastros; os produtos são replicados para o Brasil, Ásia, Oceania etc. O usuário consulta o servidor do Brasil e vê o catálogo replicado. Produto novo: o servidor dos EUA replica para o do Brasil, o usuário vê.

**Quando a comunicação falha:** deleta-se um produto nos EUA e, no momento de sincronizar com o Brasil, a comunicação falha. Quando o usuário pede a lista de produtos há duas decisões:

1. **Mostrar os produtos mesmo desatualizados** (o usuário pode ver um produto que não existe mais) — escolha por **disponibilidade**, "para uma melhor experiência do usuário".
2. **Não mostrar produto nenhum até todos os servidores sincronizarem** (página de "indisponível momentaneamente" ou carregando infinitamente), porque "vai que ele compra um produto que já foi deletado" — escolha por **consistência**.

A escolha entre mostrar o dado e não mostrar até sincronizar é a definição de quais "grandezas" do CAP o sistema usa.

### O detalhe que encaixa tudo

Só é possível escolher entre disponibilidade e consistência **a partir do momento em que houve uma falha entre os nós**. Sem a falha, não haveria o que escolher. Logo, **tolerância à partição é pré-requisito** nos sistemas distribuídos: "não tem como a gente viver sem".

Esclarecimento: tolerância a partição **não** é o sistema ser tolerante a "muitas partes/muitos servidores". Uma partição é **uma falha de comunicação, uma falha de rede entre os servidores**.

Conclusão do autor: não se escolhe "AP" ou "CA" livremente; **sempre** se precisa do P. O que se decide é **entre consistência e disponibilidade**. Muita gente ensina "o P é fixo, só escolhe C e A" sem explicar o porquê; o porquê é este: o **P não é uma terceira opção independente — é a pré-condição que ativa a escolha entre C e A**.

### Por que Brewer não disse isso diretamente?

Se não há outros nós onde a falha de rede possa ocorrer, num cenário hipotético que "não é real porque a gente está falando de sistemas distribuídos" — o sistema simples do começo — teríamos **CA**: um único banco, sem sincronização entre servidores, então há disponibilidade e consistência. Mas isso não é um sistema distribuído, e por isso numa entrevista de system design esse caso "nunca vai entrar" e nem se fala do teorema nele: "não existe o que aplicar".

## Exemplos: quando escolher consistência

- **Sistemas de ingressos/tickets** (Ingresso.com, Ticketmaster): como garantir que duas pessoas não comprem o mesmo assento — ou dez pessoas numa estreia famosa? Independente do servidor acessado, o assento "verde/disponível" e o "ocupado" precisam ser os mesmos. Precisa de algum mecanismo para lidar com isso.
- **Companhias aéreas:** escolha de assento do avião; precisa saber se está disponível ou ocupado independente do servidor.
- **Estoque (e-commerce):** dez pessoas tentam comprar o último produto; mandar confirmação a todas e descobrir depois que nove não vão receber. É preciso **consistência forte**.
- **Sistemas financeiros:** várias operações em ordem; duas transferências, e a primeira zerou o saldo — a segunda precisa falhar.

Estes são os que mais caem em entrevistas: ingressos, assentos de shows/cinema/companhia aérea, e-commerce (estoque) e sistemas financeiros. Há exceções, mas "todo o resto" tende a ser disponibilidade.

## Exemplos: quando escolher disponibilidade

- **Redes sociais** (Instagram, Facebook, Twitter): perfil, dashboards, comentários. Se alguém posta uma foto e outra pessoa acessa o perfil por outro servidor onde o dado ainda não replicou, o Instagram não mostra "perfil indisponível, sincronizando fotos": mostra as fotos desatualizadas; recarregando, segundos depois a foto aparece.
- **Perfil editado:** se você mudou o nome, as pessoas não ficam sem ver o perfil até a propagação; veem e, ao recarregar, veem o nome novo.
- **Comentários no YouTube:** alguém dos EUA acessa o vídeo e não vê seu comentário na hora; isso não impacta a experiência de assistir; vê minutos/segundos depois ao recarregar. "A gente não vai impedir um vídeo do YouTube de carregar porque algum comentário não está sincronizado."

Critério: "é muito do seu **feeling de produto**" — o quanto a feature impacta o usuário final e o quanto pode ficar desatualizada sem impactar o negócio — mais prática para reconhecer os padrões cobrados em entrevista.

Por isso entender o CAP **no começo**, ao desenhar a fundação, importa: as features e pré-requisitos guiam as escolhas de ferramentas, tipo de arquitetura, estratégia e conceito. "Sempre antes de você começar saindo desenhando a sua arquitetura."

## Nível sênior: grandezas diferentes por parte do sistema

Não é preciso escolher as grandezas de forma absoluta para o sistema inteiro. Em microsserviços, **partes diferentes do teorema podem ser aplicadas a segmentos/serviços diferentes**.

Exemplo, sistema de tickets de cinema:

- **Serviço de reservas (booking):** consistência absoluta — não se quer duas pessoas comprando o mesmo ingresso. Combina-se com outras estratégias (como locking de reservas, tema de outros vídeos do canal, "um dos conceitos que mais caem em entrevistas de system design").
- **Serviço de busca (search):** se alguém muda a descrição de um filme, travar a pesquisa de todos os usuários por alguns segundos até propagar para todos os servidores certamente não faz sentido; mostra-se a descrição desatualizada e, ao recarregar, a nova. Escolha por **disponibilidade**. É "uma escolha de produto".

Resultado: disponibilidade num serviço e consistência em outro.

## Resumo

"P é indispensável porque é ele que é a pré-condição da escolha entre consistência ou disponibilidade." Não é preciso decorar: basta entender que só se consegue escolher entre C e A **porque foi o P que causou a necessidade** da escolha.

Encerra pedindo likes, comentários, sugestões de temas e apoio como membro do canal; diz que o objetivo é ajudar o espectador a passar em entrevistas e conseguir uma vaga remota paga em dólar/euro.
