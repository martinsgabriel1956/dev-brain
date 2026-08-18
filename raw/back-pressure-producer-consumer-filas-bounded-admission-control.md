# Back Pressure — Produtor, Consumidor, Filas e Admission Control

*(Bloco de patrocínio omitido — hospedagem VPS não relacionada ao conteúdo técnico do vídeo.)*

## O que é back pressure

Hoje vamos falar de "dor nas costas" — back pressure. Traduzido literalmente: back (costas, parte de trás) + pressure (pressão) — pressão na parte de trás. Todo dev precisa entender isso porque aparece em diversos tipos de sistemas distribuídos.

Em muitos sistemas distribuídos existe uma relação entre **produtor** e **consumidor**, e essa relação pode se dar de diversas maneiras. Dois exemplos clássicos:

- Um **web crawler** que navega por diversas páginas na web e salva essas páginas — o ato de salvar é o ato de produzir. Existe uma ligação com o consumidor, que vai analisar e tratar os dados dessas páginas.
- Um **usuário fazendo upload de um vídeo** — o usuário está produzindo um vídeo. Uma peça do sistema armazena esse vídeo em algum lugar, e outra peça do sistema vai comprimir esse vídeo.

**Back pressure é o problema que ocorre quando o produtor produz numa velocidade que o consumidor não consegue consumir.**

## O exemplo do descasamento de velocidade

Imagine que o produtor está navegando a internet e encontrando 100 sites por minuto, mandando essa informação para o consumidor analisar, indexar e salvar. Só que o consumidor tem uma velocidade de apenas 10 sites por minuto. Ao longo de 10 minutos, vai existir um descasamento de 900 sites.

Geralmente a gente conecta um produtor a um consumidor através de uma **fila**. Sem essa fila — mandando direto do produtor pro consumidor — isso rapidamente sobrecarrega o consumidor. A fila dá um buffer, uma "azeitada" no sistema, permitindo lidar com esse fluxo de maneira mais contínua.

Mas a fila também tem um limite físico — um limite de bits, bytes e megabytes de quanto ela consegue armazenar. 900 itens numa fila é plausível, mas conforme o tempo passa a fila cresce, e surgem outros problemas:

- **Os itens envelhecem.** Se o produtor produz em um mês o que o consumidor demora 10 meses para processar, a informação pode já estar desatualizada quando finalmente for consumida.
- **A fila pode crashar.** Dado tempo suficiente, o uso de memória da fila cresce tanto que ela quebra o sistema.

Adicionar mais capacidade na fila, ou mais filas, só empurra o problema para frente — não resolve o descasamento fundamental entre um produtor mais rápido que o consumidor.

## Primeiro passo: identificar o gargalo real

Antes de qualquer solução, é essencial entender **onde está o gargalo**. Pode ser que o consumidor só consiga processar 10 por minuto porque o gargalo está no banco de dados, que tem uma limitação própria de velocidade. Nesse caso, aumentar a velocidade do consumidor ou jogar mais hardware nele não resolve nada — o problema não está ali. Entender o gargalo de verdade é o ponto de partida do back pressure.

## Técnicas mais baratas antes de escalar hardware

- **Podar stale jobs.** Conforme a fila cresce, aplicar alguma regra que remove itens antigos, com erro, ou que não fazem mais sentido.
- **Priorizar** os itens mais importantes dentro da fila.
- **Processar em batches.** Em vez de processar um site de cada vez, processar vários de uma vez (por exemplo, um batch insert no banco em vez de inserts individuais). Isso aumenta a vazão do sistema sem aumentar a capacidade de hardware.

Essas técnicas são mais fáceis e mais baratas do que simplesmente jogar mais hardware no problema.

## Soluções estruturais

**Fila bounded (limitada).** A fila não pode crescer infinitamente — precisa ter um tamanho máximo. Isso empurra o problema para o produtor (ele pode precisar lidar com rejeição ou retry), mas evita que o sistema estoure. O pior caso é perder alguns itens que o produtor não conseguiu enfileirar, ou estourar a memória do produtor se ele ficar tentando retry para sempre.

**Admission control.** Controlar se novos jobs entram na fila ou não. Pode ser implementado no próprio produtor ou como um middleware: se a fila está muito cheia, o admission control rejeita o job antes que ele entre.

**Rate limit no produtor.** Se o consumidor só processa 10 por minuto, o produtor é limitado a produzir na mesma medida — produzir mais rápido que isso só queima recurso computacional sem benefício, e só adiciona pressão que o sistema não consegue absorver.

**Mais consumidores / paralelização.** Rodar os consumidores em cluster (2, 3, 4, 5+ instâncias) em vez de um único servidor, paralelizando o trabalho. A fila também pode ser paralelizada para lidar com maior vazão.

**Auto scaling baseado no tamanho da fila.** É perfeitamente possível montar um setup de auto scaling usando o tamanho da fila como métrica — mais difícil de configurar, mas viável. Junto disso, monitoramento e alertas para garantir que a fila mantenha um número razoável de itens.

**Cuidado com retry.** Entre produtor e fila, uma política de retry que tenta muitas vezes pode colocar ainda mais pressão no sistema. Retry deve ser usado, mas com cautela.

## Demonstração prática

### Exemplo 1 — sem controle de back pressure

Um único arquivo JavaScript com uma fila (um array), uma função que produz e uma função que consome — a função consumidora tem um `sleep`, sendo mais lenta que a produtora.

Resultado observado ao rodar: jobs aceitos = 922, jobs processados = 123, lag = 799 itens na fila. Conforme o tempo passa, o job mais antigo envelhece cada vez mais, e o lag cresce sem controle.

### Exemplo 2 — com low watermark / high watermark

Uma implementação mais completa usando uma fila no **Redis** (rodando em Docker) via **BullMQ**. A técnica usada:

- O produtor checa o número de jobs na fila.
- Se o número de jobs for **maior que 100** (high watermark), o produtor **pausa** — para de produzir e fica apenas checando o tamanho da fila periodicamente.
- Quando o número de jobs cai **abaixo de 30** (low watermark), o produtor **retoma** a produção.

Resultado observado: o tamanho da fila cresce até por volta de 93, para, reduz até cerca de 30, e volta a crescer — o produtor alterna entre produzir e pausar, dando tempo para o consumidor drenar a fila. O lag nunca fica tão grande quanto no exemplo sem controle.

Essa demo é simplificada — só para ilustrar a técnica. Na vida real, produtor e consumidor normalmente não rodariam no mesmo servidor nem no mesmo arquivo `index.js`.

*(Encerramento com divulgação de curso de system design do canal, omitido por não ser conteúdo técnico.)*
